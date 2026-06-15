#!/usr/bin/env python3
"""
render.py — one source, two views.

Reads requirements.yaml (the single source of truth) and emits:
  1. build-standard.md        internal build standard, expressed as pass/fail gates
  2. vetting-rubric.md        client-facing rubric, weighted scoring with verdict
  3. requirements-registry.csv  flat dump for Excel / n8n / Obsidian

Usage:
  python3 render.py --src requirements.yaml --out /mnt/user-data/outputs
"""
import argparse, csv, os, sys

try:
    import yaml
except ImportError:
    sys.exit("PyYAML required: pip install pyyaml --break-system-packages")


def load(src):
    with open(src) as f:
        return yaml.safe_load(f)


def flat(data):
    """Flatten to a list of requirement dicts with category context + resolved weight."""
    wbt = data["meta"]["weights_by_tier"]
    rows = []
    for cat in data["categories"]:
        for r in cat["requirements"]:
            r = dict(r)
            r["category"] = cat["id"]
            r["category_name"] = cat["name"]
            r["weight"] = r.get("weight", wbt[r["tier"]])
            rows.append(r)
    return rows


# ---------------------------------------------------------------- build standard
def build_standard(data, rows):
    m = data["meta"]
    hard = [r for r in rows if r["gate"] == "hard"]
    cond = [r for r in rows if r["gate"] == "conditional"]
    diff = [r for r in rows if r["tier"] == "T1"]
    moat = [r for r in rows if r["tier"] == "T2"]

    L = []
    L.append(f"# {m['title']} — Build Standard (rev {m['revision']})")
    L.append("")
    L.append("> Generated from `requirements.yaml`. Do not hand-edit — change the registry and regenerate.")
    L.append("")
    L.append("Each line is a binary gate. Check it only when the acceptance condition is "
             "demonstrably met in the product, not merely planned.")
    L.append("")
    L.append("**Ship logic**")
    L.append("")
    L.append(f"- **All {len(hard)} hard gates (T0) MUST pass to ship.** A single failure means the "
             "agent is displaceable by a general LLM on day one.")
    L.append(f"- **All {len(cond)} conditional gates (TG) MUST pass in any high-stakes or regulated "
             "domain.** Mark N/A only with explicit justification.")
    L.append(f"- **Differentiators (T1, {len(diff)}) and Retention/Moat (T2, {len(moat)}) are tracked "
             "as coverage**, not veto. Target: 100% of T2 moat items before claiming durability.")
    L.append("")

    def block(title, items, note=None):
        L.append(f"## {title}")
        if note:
            L.append(f"*{note}*")
        L.append("")
        for r in items:
            L.append(f"- [ ] **{r['id']} — {r['title']}**  ·  _{r['category']}_  ·  weight {r['weight']}"
                     + ("  ·  🛡 moat" if r["moat"] else ""))
            L.append(f"    - SHALL: {r['statement']}")
            L.append(f"    - GATE (pass when): {r['acceptance']}")
            L.append(f"    - Kills: \"{r['neutralizes']}\"")
        L.append("")

    block("🔒 Hard Ship-Gates (T0) — all must pass", hard)
    block("⚖️ Conditional Gates (TG) — must pass in high-stakes / regulated domains", cond)
    block("➕ Differentiators (T1) — coverage target 100%", diff)
    block("🏰 Retention & Moat (T2) — coverage target 100%, moat items first", moat)
    return "\n".join(L)


# ---------------------------------------------------------------- vetting rubric
def vetting_rubric(data, rows):
    m = data["meta"]
    sc = m["scoring"]
    gmin = sc["gate_min"]

    L = []
    L.append(f"# {m['title']} — Vetting Rubric (rev {m['revision']})")
    L.append("")
    L.append("> Generated from `requirements.yaml`. Score a candidate agent 0–3 per requirement; "
             "the weighted roll-up yields a verdict.")
    L.append("")
    L.append("## Scoring scale")
    for k in sorted(sc["scale"]):
        L.append(f"- **{k}** — {sc['scale'][k]}")
    L.append("")
    L.append("## Gating rule (veto)")
    L.append(f"Any **hard gate (T0)** — or any **applicable conditional gate (TG)** — scoring below "
             f"**{gmin}** caps the verdict at *At risk*, regardless of the weighted total. You cannot "
             "score your way past a broken floor.")
    L.append("")

    # per-category tables
    max_total = 0
    moat_total = 0
    for cat in data["categories"]:
        L.append(f"## {cat['id']}. {cat['name']}")
        L.append(f"*{cat['tagline']}*")
        L.append("")
        L.append("| ID | Requirement | Tier | Gate | Moat | Weight | Score (0–3) | Weighted |")
        L.append("|---|---|---|---|---|---|---|---|")
        wbt = m["weights_by_tier"]
        for r in cat["requirements"]:
            w = r.get("weight", wbt[r["tier"]])
            gate = {"hard": "🔒 hard", "conditional": "⚖️ cond", "none": "—"}[r["gate"]]
            moatf = "🛡" if r["moat"] else "—"
            max_total += w * 3
            if r["moat"]:
                moat_total += 1
            L.append(f"| {r['id']} | {r['title']} | {r['tier']} | {gate} | {moatf} | {w} | ___ | ___ |")
        L.append("")

    # rollup
    L.append("## Roll-up")
    L.append("")
    L.append(f"- **Maximum weighted score:** {max_total}  (sum of weight × 3 across all requirements)")
    L.append("- **Your weighted score:** sum of (weight × score) across all rows.")
    L.append("- **Percentage:** your weighted score ÷ maximum weighted score.")
    L.append(f"- **Moat coverage:** count of the {moat_total} moat items scoring ≥ {gmin}, ÷ {moat_total}.")
    L.append("")
    L.append("## Verdict bands")
    L.append("")
    L.append("| If… | Verdict |")
    L.append("|---|---|")
    L.append(f"| any hard/applicable-conditional gate < {gmin} | **At risk — thin wrapper; a savvy user defaults to the general model.** |")
    for b in m["verdict_bands"]:
        pct = int(b["min"] * 100)
        L.append(f"| no gate failure and score ≥ {pct}% | **{b['label']}** |")
    L.append("")
    L.append("> A high percentage with a failed gate is still *At risk*. Durability is only claimed "
             "when moat coverage reaches 100%.")
    return "\n".join(L)


# ---------------------------------------------------------------- csv
def write_csv(rows, path):
    cols = ["id", "category", "category_name", "title", "tier", "journey",
            "gate", "moat", "weight", "statement", "neutralizes", "acceptance"]
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow(r)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", default="requirements.yaml")
    ap.add_argument("--out", default=".")
    a = ap.parse_args()

    data = load(a.src)
    rows = flat(data)
    os.makedirs(a.out, exist_ok=True)

    with open(os.path.join(a.out, "build-standard.md"), "w") as f:
        f.write(build_standard(data, rows) + "\n")
    with open(os.path.join(a.out, "vetting-rubric.md"), "w") as f:
        f.write(vetting_rubric(data, rows) + "\n")
    write_csv(rows, os.path.join(a.out, "requirements-registry.csv"))

    # summary
    by_tier = {}
    for r in rows:
        by_tier[r["tier"]] = by_tier.get(r["tier"], 0) + 1
    moat = sum(1 for r in rows if r["moat"])
    print(f"Rendered {len(rows)} requirements across {len(data['categories'])} categories.")
    print("By tier:", ", ".join(f"{k}={by_tier[k]}" for k in sorted(by_tier)))
    print(f"Hard gates: {sum(1 for r in rows if r['gate']=='hard')}  "
          f"Conditional gates: {sum(1 for r in rows if r['gate']=='conditional')}  "
          f"Moat items: {moat}")
    print(f"Outputs written to {a.out}")


if __name__ == "__main__":
    main()
