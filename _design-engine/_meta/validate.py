#!/usr/bin/env python3
"""
validate.py — OVE structural and scrub validator (optional).

Standalone, pure stdlib. Run from the OVE root or pass --root.
Exits 0 on full pass, 1 on warnings only, 2 on any failure.

Checks (independently togglable via --skip):

  C1  cartridge-backbone-presence
        Every cartridge has _ov-manifest.md, _design-state.md,
        _design-decisions.md, _schema-draft.md.

  C2  cartridge-frontmatter-present
        Cartridge backbone files start with a non-empty YAML frontmatter block.

  C3  placeholder-leakage
        No <USER_NAME> / [USER NAME] / <author> / <COMPANY> / <TBD> etc.
        appears in shipped files (templates folder is exempt).

  C4  identity-from-indirect-signals (F3 class)
        If the operator has confirmed a name in _USER.md, LICENSE.md
        attribution must match it.

  C5  dangling-wikilinks
        [[X]] references resolve to a file in the OV.

  C6  bootstrap-vs-engine-agreement (F6 drift)
        AI-BOOTSTRAP.md and _design-engine/00-START-HERE.md state the same
        Tier 1 read protocol and name 00-START-HERE.md as canonical.

This validator is a safety net, not a replacement for the SHIPPING-CHECKLIST
or operator judgment. It catches the high-embarrassment failure modes (F3
identity, F6 drift, placeholder leaks) without requiring perfect discipline.
The prose-fallback equivalent for markdown-only environments is in
_design-engine/_meta/VALIDATION-CHECKLIST.md.
"""

import argparse
import os
import re
import sys
from pathlib import Path

PLACEHOLDER_PATTERNS = [
    r'<USER[_ ]NAME>',
    r'\[USER[_ ]NAME\]',
    r'<USER[_ ]EMAIL>',
    r'<COMPANY>',
    r'<CLIENT>',
    r'<author>',
    r'\[author\]',
    r'<TBD>',
    r'<TODO>',
    r'<your-name-here>',
    r'<your[_ ]domain>',
    r'<placeholder>',
    r'<your name>',
    r'<your email>',
]
PLACEHOLDER_RE = re.compile('|'.join(PLACEHOLDER_PATTERNS), re.IGNORECASE)

WIKILINK_RE = re.compile(r'\[\[([^\]]+)\]\]')
FRONTMATTER_RE = re.compile(r'^---\n(.*?)\n---\n', re.DOTALL)

CARTRIDGE_BACKBONE = [
    "_ov-manifest.md",
    "_design-state.md",
    "_design-decisions.md",
    "_schema-draft.md",
]

# Folders/paths skipped during file scans. Templates legitimately contain
# placeholder text; .git and node_modules are noise; .obsidian is workspace.
SKIP_FOLDERS = {
    "_design-engine/_templates",
    ".git",
    "node_modules",
    ".obsidian",
}


class Finding:
    def __init__(self, check, severity, file, line=None, message=""):
        self.check = check
        self.severity = severity  # 'fail', 'warn', 'info'
        self.file = file
        self.line = line
        self.message = message

    def format(self, root):
        try:
            rel = self.file.relative_to(root) if self.file else None
        except Exception:
            rel = self.file
        loc = f"{rel}:{self.line}" if self.line else (str(rel) if rel else "")
        return f"  [{self.severity.upper():4}] {self.check:18} {loc}\n           {self.message}"


def find_ov_root(start):
    """Walk up from start to find a directory that looks like an OVE root."""
    current = Path(start).resolve()
    for _ in range(8):
        if (current / "AI-BOOTSTRAP.md").exists() and (current / "_design-engine").is_dir():
            return current
        if current.parent == current:
            break
        current = current.parent
    return None


def is_skip_path(path, root):
    try:
        rel = str(path.relative_to(root))
    except Exception:
        return False
    for skip in SKIP_FOLDERS:
        if rel == skip or rel.startswith(skip + "/") or skip in rel.split("/"):
            return True
    return False


def list_cartridges(root):
    """Cartridges = top-level subfolders that aren't engine, dot-prefixed, or underscore-prefixed."""
    cartridges = []
    for entry in sorted(root.iterdir()):
        if not entry.is_dir():
            continue
        name = entry.name
        if name.startswith(".") or name.startswith("_"):
            continue
        cartridges.append(entry)
    return cartridges


def iter_md_files(root):
    """Iterate over markdown files in the OV, skipping configured paths."""
    for p in sorted(root.rglob("*.md")):
        if is_skip_path(p, root):
            continue
        yield p


_CODE_SPAN_RE = re.compile(r'`[^`\n]*`')


def iter_prose_lines(file_path):
    """
    Yield (lineno, prose_line) for a markdown file, skipping fenced code blocks
    and stripping inline code spans. Documentation that *discusses* placeholder
    patterns inside backticks should not be flagged as a placeholder leak.
    """
    in_fenced = False
    with file_path.open(encoding="utf-8") as fh:
        for lineno, line in enumerate(fh, 1):
            stripped_lead = line.lstrip()
            if stripped_lead.startswith("```") or stripped_lead.startswith("~~~"):
                in_fenced = not in_fenced
                continue
            if in_fenced:
                continue
            cleaned = _CODE_SPAN_RE.sub("", line)
            yield lineno, cleaned


# ---------------------------------------------------------------------------
# Individual checks
# ---------------------------------------------------------------------------

def check_C1_backbone(root, cartridges):
    findings = []
    for cart in cartridges:
        for backbone_file in CARTRIDGE_BACKBONE:
            f = cart / backbone_file
            if not f.exists():
                findings.append(Finding(
                    "C1-backbone", "fail", cart,
                    message=f"missing required backbone file: {backbone_file}"
                ))
    return findings


def check_C2_frontmatter(root, cartridges):
    findings = []
    for cart in cartridges:
        for backbone_file in CARTRIDGE_BACKBONE:
            f = cart / backbone_file
            if not f.exists():
                continue  # reported by C1
            try:
                text = f.read_text(encoding="utf-8")
            except Exception as e:
                findings.append(Finding(
                    "C2-frontmatter", "fail", f,
                    message=f"could not read file: {e}"
                ))
                continue
            if not text.lstrip().startswith("---"):
                findings.append(Finding(
                    "C2-frontmatter", "fail", f,
                    message="file does not start with YAML frontmatter (---)"
                ))
                continue
            m = FRONTMATTER_RE.match(text)
            if not m:
                findings.append(Finding(
                    "C2-frontmatter", "fail", f,
                    message="malformed YAML frontmatter block (no closing ---)"
                ))
                continue
            fm = m.group(1).strip()
            if not fm:
                findings.append(Finding(
                    "C2-frontmatter", "fail", f,
                    message="YAML frontmatter is empty"
                ))
    return findings


def check_C3_placeholders(root):
    findings = []
    for f in iter_md_files(root):
        try:
            for lineno, line in iter_prose_lines(f):
                for m in PLACEHOLDER_RE.finditer(line):
                    findings.append(Finding(
                        "C3-placeholder", "fail", f, line=lineno,
                        message=f"placeholder leak: {m.group(0).strip()}"
                    ))
        except Exception as e:
            findings.append(Finding(
                "C3-placeholder", "warn", f,
                message=f"could not scan: {e}"
            ))
    return findings


def operator_name(root):
    """Resolve operator's confirmed name from _USER.md."""
    user_md = root / "_USER.md"
    if not user_md.exists():
        return None
    try:
        text = user_md.read_text(encoding="utf-8")
    except Exception:
        return None
    # Match `name: "Jawn Lam"` or `name: Jawn Lam` style lines.
    m = re.search(r'^(?:name|operator_name|full_name)\s*:\s*"?([^"\n]+)"?\s*$',
                  text, re.MULTILINE | re.IGNORECASE)
    if m:
        return m.group(1).strip()
    return None


def check_C4_identity(root, cartridges):
    findings = []
    confirmed = operator_name(root)
    if confirmed is None:
        findings.append(Finding(
            "C4-identity", "info", root,
            message="no operator name confirmed in _USER.md; C4 identity check skipped"
        ))
        return findings
    lic = root / "LICENSE.md"
    if lic.exists():
        try:
            text = lic.read_text(encoding="utf-8")
        except Exception as e:
            findings.append(Finding("C4-identity", "warn", lic, message=f"could not read: {e}"))
            return findings
        # Look for "by <Name>" or "© <Name>" or "(c) <Name>" attribution patterns.
        attributions = re.findall(
            r'(?:\bby\b|copyright|©|\(c\))\s+([A-Z][a-zA-Z]+\s+[A-Z][a-zA-Z]+)',
            text, re.IGNORECASE
        )
        for attr in attributions:
            if attr.strip().lower() != confirmed.strip().lower():
                findings.append(Finding(
                    "C4-identity", "warn", lic,
                    message=f"LICENSE attribution '{attr}' does not match confirmed operator '{confirmed}'"
                ))
    return findings


def check_C5_wikilinks(root):
    findings = []
    # Build index of all .md files (by stem and by filename).
    index = {}
    for p in root.rglob("*.md"):
        if is_skip_path(p, root):
            continue
        index[p.stem] = p
        index[p.name] = p
    for f in iter_md_files(root):
        # Prototype definition files (Convention 6) contain placeholder example
        # wikilinks by design — they are templates of structure, not consumers
        # of vault state. Skip C5 for files inside any _Prototypes/ folder.
        if "_Prototypes" in f.parts:
            continue
        try:
            for lineno, line in iter_prose_lines(f):
                for m in WIKILINK_RE.finditer(line):
                    raw = m.group(1)
                    target = raw.split("|", 1)[0].split("#", 1)[0].strip()
                    if not target:
                        continue
                    if target in index or (target + ".md") in index:
                        continue
                    findings.append(Finding(
                        "C5-wikilink", "warn", f, line=lineno,
                        message=f"dangling wikilink: [[{raw}]]"
                    ))
        except Exception:
            pass
    return findings


def _extract_tier1_engine_files(text):
    """From a tiered read protocol section, extract referenced NN-FILE.md names in Tier 1."""
    m = re.search(r'Tier 1.*?(?=Tier 2|\Z)', text, re.DOTALL)
    if not m:
        return set()
    section = m.group(0)
    return set(re.findall(r'\b(\d{2}-[A-Z][A-Z0-9\-]*\.md)', section))


ZONE_NAMES = [
    "Engine Zone",
    "Operator-Private Zone",
    "Operator-Extension Zone",
    "Shipped Examples Zone",
]


def check_C8_zone_documentation(root):
    """Convention 8: CONTRIBUTING.md (or OPERATOR-GUIDE.md fallback) must declare the
    four content zones by name. Operator-chosen synonyms are not detected; if the OV
    uses different names, the operator can skip C8 via --skip=C8 once that decision
    is documented in _design-decisions.md.
    """
    findings = []
    candidates = [
        root / "CONTRIBUTING.md",
        root / "OPERATOR-GUIDE.md",
    ]
    text = ""
    found_file = None
    for c in candidates:
        if c.exists():
            try:
                text += "\n" + c.read_text(encoding="utf-8")
                if found_file is None:
                    found_file = c
            except Exception:
                pass
    if not text:
        findings.append(Finding(
            "C8-zones", "fail", root,
            message="neither CONTRIBUTING.md nor OPERATOR-GUIDE.md exists — cannot verify "
                    "Convention 8 zone-boundary documentation"
        ))
        return findings

    missing = [z for z in ZONE_NAMES if z not in text]
    if not missing:
        return findings  # all four present — pass
    if len(missing) == len(ZONE_NAMES):
        findings.append(Finding(
            "C8-zones", "fail", found_file,
            message=("Convention 8 violation: none of the four canonical zone names "
                     "(" + ", ".join(ZONE_NAMES) + ") found in CONTRIBUTING.md or "
                     "OPERATOR-GUIDE.md. Use operator-chosen synonyms if documented in "
                     "_design-decisions.md, then --skip=C8.")
        ))
    else:
        findings.append(Finding(
            "C8-zones", "warn", found_file,
            message=("Convention 8 partial: missing zone names " + ", ".join(missing) +
                     ". Either declare them or document operator-chosen synonyms in "
                     "_design-decisions.md.")
        ))
    return findings


def check_C10_update_prompt_sanity(root):
    """Convention 7 (via C10): UPDATE-PROMPT.md exists at the OV root with the OV's
    name filled in concretely (no placeholders) and references the four-zone boundary
    and a no-destructive-commands-without-confirmation discipline. Soft checks; a
    missing UPDATE-PROMPT.md is a fail, but the content checks are warnings (operators
    may legitimately customize the prompt to a different shape).
    """
    findings = []
    up = root / "UPDATE-PROMPT.md"
    if not up.exists():
        findings.append(Finding(
            "C10-update-prompt", "fail", root,
            message="UPDATE-PROMPT.md missing at OV root (Convention 7: required artifact). "
                    "Copy from _design-engine/_templates/TEMPLATE-UPDATE-PROMPT.md if OVE is the engine."
        ))
        return findings
    try:
        text = up.read_text(encoding="utf-8")
    except Exception as e:
        findings.append(Finding(
            "C10-update-prompt", "fail", up,
            message=f"UPDATE-PROMPT.md present but unreadable: {e}"
        ))
        return findings

    # Placeholder check — the template literal `<OV-Name>` should not appear post-customization.
    if "<OV-Name>" in text or "<ov-slug>" in text or "<author>" in text:
        findings.append(Finding(
            "C10-update-prompt", "fail", up,
            message="UPDATE-PROMPT.md still contains template placeholders (<OV-Name>, <ov-slug>, "
                    "or <author>). Fill in the OV's concrete name throughout."
        ))

    # Content sanity — soft warnings if the prompt is missing key elements.
    missing_signals = []
    # The prompt must reference INSTALL.md and OPERATOR-GUIDE.md so the AI consults the canonical docs.
    if "INSTALL.md" not in text:
        missing_signals.append("reference to INSTALL.md")
    if "OPERATOR-GUIDE.md" not in text:
        missing_signals.append("reference to OPERATOR-GUIDE.md")
    # The prompt must reference the four-zone boundary so the AI honors it.
    if "zone" not in text.lower() and "four-zone" not in text.lower() and "Operator-Extension" not in text:
        missing_signals.append("four-zone boundary reference")
    # The prompt must instruct the AI to stop before destructive commands.
    destructive_signals = ["destructive", "confirm", "approve", "stop and ask", "stop and confirm"]
    if not any(sig in text.lower() for sig in destructive_signals):
        missing_signals.append("destructive-command-confirmation discipline")
    if missing_signals:
        findings.append(Finding(
            "C10-update-prompt", "warn", up,
            message="UPDATE-PROMPT.md present but missing: " + ", ".join(missing_signals) +
                    ". See _design-engine/_templates/TEMPLATE-UPDATE-PROMPT.md for the canonical shape."
        ))
    return findings


def check_C9_gitignore_sanity(root):
    """Convention 8 (via C9): .gitignore exists at the OV root and contains at least
    one non-comment, non-blank pattern (presumed to be an Operator-Private Zone
    pattern). Empty or comment-only .gitignore is a warning.
    """
    findings = []
    gi = root / ".gitignore"
    if not gi.exists():
        findings.append(Finding(
            "C9-gitignore", "fail", root,
            message=".gitignore missing at OV root (Convention 8: Operator-Private Zone "
                    "patterns must be declared in .gitignore)"
        ))
        return findings
    try:
        text = gi.read_text(encoding="utf-8")
    except Exception as e:
        findings.append(Finding(
            "C9-gitignore", "fail", gi,
            message=f".gitignore present but unreadable: {e}"
        ))
        return findings
    substantive = [
        line for line in text.splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    ]
    if not substantive:
        findings.append(Finding(
            "C9-gitignore", "warn", gi,
            message=".gitignore exists but contains no substantive patterns "
                    "(all blank or comment lines) — Convention 8 expects at least one "
                    "Operator-Private Zone pattern"
        ))
    return findings


def _find_prototype_definition(root, cartridge, prototype_name):
    """Return the Path of the Prototype definition file, or None if missing.

    Search order:
      1. <cartridge>/_Prototypes/<NAME>.md  (cartridge-local override)
      2. <root>/_Prototypes/<NAME>.md       (OV-root canonical home)
    """
    if cartridge is not None:
        local = cartridge / "_Prototypes" / f"{prototype_name}.md"
        if local.exists():
            return local
    canonical = root / "_Prototypes" / f"{prototype_name}.md"
    if canonical.exists():
        return canonical
    return None


ITEM_PROTOTYPE_RE = re.compile(r'^Item_Prototype:\s*["\']?([A-Za-z_][A-Za-z0-9_]*)["\']?\s*$')


def check_C7_prototype_coverage(root, cartridges):
    """Convention 6: every Item_Prototype value used in any cartridge must have
    a definition file in either the cartridge's local _Prototypes/ or the OV
    root's _Prototypes/. Fleeting is excluded (vault-universal Prototype)."""
    findings = []

    # Verify the OV root has a _Prototypes/ folder at all
    root_proto = root / "_Prototypes"
    if not root_proto.is_dir():
        findings.append(Finding(
            "C7-coverage", "fail", root,
            message="OV root is missing _Prototypes/ folder (Convention 6)"
        ))

    # For each cartridge, walk .md files, collect Item_Prototype values, verify coverage
    seen = {}  # prototype_name -> list of (file, lineno) where first observed
    for cartridge in cartridges:
        for md in cartridge.rglob("*.md"):
            if is_skip_path(md, root):
                continue
            # Skip Prototype-definition files themselves (they ARE the source of truth,
            # not consumers of it). They live in _Prototypes/ and use Item_Prototype: Fleeting.
            if "_Prototypes" in md.parts:
                continue
            try:
                with md.open(encoding="utf-8") as fh:
                    in_frontmatter = False
                    for lineno, line in enumerate(fh, start=1):
                        stripped = line.rstrip("\n")
                        if lineno == 1:
                            if stripped == "---":
                                in_frontmatter = True
                                continue
                            else:
                                break  # no frontmatter; nothing to check
                        if in_frontmatter and stripped == "---":
                            break
                        if not in_frontmatter:
                            continue
                        m = ITEM_PROTOTYPE_RE.match(stripped)
                        if not m:
                            continue
                        name = m.group(1)
                        if name == "Fleeting":
                            continue
                        seen.setdefault(name, []).append((md, lineno, cartridge))
            except Exception:
                continue

    # For each distinct Prototype name, verify a definition file exists
    for name, occurrences in sorted(seen.items()):
        # Use the first occurrence's cartridge for the cartridge-local search;
        # if any cartridge has a local override, the canonical search will also pick it up
        # for cartridges that don't have one.
        # We report against the OV-root view: if no _Prototypes/<name>.md anywhere, it's a miss.
        cartridges_using = sorted({c for (_, _, c) in occurrences}, key=lambda p: p.name)
        unresolved_cartridges = []
        for cartridge in cartridges_using:
            if _find_prototype_definition(root, cartridge, name) is None:
                unresolved_cartridges.append(cartridge)
        if unresolved_cartridges:
            # Point at the first occurrence for a concrete file:line
            first_md, first_line, _ = occurrences[0]
            cartridge_list = ", ".join(c.name for c in unresolved_cartridges)
            findings.append(Finding(
                "C7-coverage", "fail", first_md, line=first_line,
                message=(f"Item_Prototype: {name} is used but has no definition file "
                         f"at _Prototypes/{name}.md "
                         f"(neither OV-root nor cartridge-local); "
                         f"cartridges affected: {cartridge_list}")
            ))

    return findings


def check_C6_bootstrap_engine_drift(root):
    findings = []
    bootstrap = root / "AI-BOOTSTRAP.md"
    engine = root / "_design-engine" / "00-START-HERE.md"
    if not bootstrap.exists() or not engine.exists():
        return [Finding(
            "C6-drift", "fail", root,
            message="AI-BOOTSTRAP.md or _design-engine/00-START-HERE.md missing — cannot run drift check"
        )]
    b_text = bootstrap.read_text(encoding="utf-8")
    e_text = engine.read_text(encoding="utf-8")
    for label, text, file in [("AI-BOOTSTRAP.md", b_text, bootstrap),
                               ("00-START-HERE.md", e_text, engine)]:
        if "Tier 1" not in text:
            findings.append(Finding(
                "C6-drift", "fail", file,
                message=f"{label} missing 'Tier 1' section — read protocol not tiered"
            ))
        if "Tier 2" not in text:
            findings.append(Finding(
                "C6-drift", "fail", file,
                message=f"{label} missing 'Tier 2' section"
            ))
    if "00-START-HERE.md" not in b_text or "canonical" not in b_text.lower():
        findings.append(Finding(
            "C6-drift", "warn", bootstrap,
            message="AI-BOOTSTRAP.md does not reference 00-START-HERE.md as canonical"
        ))
    b_files = _extract_tier1_engine_files(b_text)
    e_files = _extract_tier1_engine_files(e_text)
    if b_files != e_files:
        only_b = sorted(b_files - e_files)
        only_e = sorted(e_files - b_files)
        parts = []
        if only_b:
            parts.append(f"only in AI-BOOTSTRAP.md: {only_b}")
        if only_e:
            parts.append(f"only in 00-START-HERE.md: {only_e}")
        findings.append(Finding(
            "C6-drift", "fail", root,
            message="Tier 1 file lists differ between AI-BOOTSTRAP.md and 00-START-HERE.md; "
                    + "; ".join(parts)
        ))
    return findings


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------

def run(root, checks):
    findings = []
    cartridges = list_cartridges(root)
    if "C1" in checks:
        findings.extend(check_C1_backbone(root, cartridges))
    if "C2" in checks:
        findings.extend(check_C2_frontmatter(root, cartridges))
    if "C3" in checks:
        findings.extend(check_C3_placeholders(root))
    if "C4" in checks:
        findings.extend(check_C4_identity(root, cartridges))
    if "C5" in checks:
        findings.extend(check_C5_wikilinks(root))
    if "C6" in checks:
        findings.extend(check_C6_bootstrap_engine_drift(root))
    if "C7" in checks:
        findings.extend(check_C7_prototype_coverage(root, cartridges))
    if "C8" in checks:
        findings.extend(check_C8_zone_documentation(root))
    if "C9" in checks:
        findings.extend(check_C9_gitignore_sanity(root))
    if "C10" in checks:
        findings.extend(check_C10_update_prompt_sanity(root))
    return findings, cartridges


def main(argv=None):
    p = argparse.ArgumentParser(
        description="OVE structural and scrub validator (optional safety net)."
    )
    p.add_argument("--root", help="OVE root directory (default: search upward from CWD)")
    p.add_argument("--skip", default="",
                   help="comma-separated check IDs to skip (e.g., C4,C5)")
    p.add_argument("--quiet", action="store_true", help="only print findings, not progress")
    args = p.parse_args(argv)

    if args.root:
        root = Path(args.root).resolve()
        if not (root / "AI-BOOTSTRAP.md").exists():
            print(f"ERROR: {root} does not look like an OVE root (no AI-BOOTSTRAP.md)",
                  file=sys.stderr)
            return 2
    else:
        root = find_ov_root(Path.cwd())
        if root is None:
            print("ERROR: could not find OVE root from current directory.", file=sys.stderr)
            return 2

    if not args.quiet:
        print(f"Validating OVE at: {root}")

    skip = {c.strip() for c in args.skip.split(",") if c.strip()}
    checks = {f"C{i}" for i in range(1, 11)} - skip

    findings, cartridges = run(root, sorted(checks))

    if not args.quiet:
        print(f"Cartridges discovered: {len(cartridges)}"
              + (f" ({', '.join(c.name for c in cartridges)})" if cartridges else ""))
        print(f"Checks run: {', '.join(sorted(checks))}")
        print()

    if not findings:
        print("PASS: no findings.")
        return 0

    fails = [f for f in findings if f.severity == "fail"]
    warns = [f for f in findings if f.severity == "warn"]
    infos = [f for f in findings if f.severity == "info"]

    print(f"Findings: {len(fails)} fail, {len(warns)} warn, {len(infos)} info")
    print()
    for f in findings:
        print(f.format(root))
    print()
    if fails:
        print("FAIL")
        return 2
    if warns:
        print("WARN (no failures, but issues to review)")
        return 1
    print("PASS (info-only findings)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
