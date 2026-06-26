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

  C11 source-inventory-completeness (F13 vector — v2.0)
        If _source-inventory.md exists at OV root, status is valid and no
        template placeholders remain. Status must be read-acknowledged or
        locked before ARTIFACT-DRAFT proceeds.

  C12 citation-audit-log (F13 vector — v2.0)
        If _source-inventory.md is marked 'locked', _citation-audit-log.md
        must exist documenting verified cites (SHIP-PREP Phase 3.7).

  C13 vocabulary-audit-log (v2.0)
        If shippable content contains deliverable-promise nouns (dashboard,
        scorecard, playbook), _vocabulary-audit-log.md must record each
        instance's disposition (kept-with-justification or replaced).

This validator is a safety net, not a replacement for the SHIPPING-CHECKLIST
or operator judgment. It catches the high-embarrassment failure modes (F3
identity, F6 drift, F13 source-grounding, placeholder leaks) without requiring
perfect discipline. The prose-fallback equivalent for markdown-only environments
is in _design-engine/_meta/VALIDATION-CHECKLIST.md.
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
    "_proposals",
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
      1. <cartridge>/_Prototypes/<NAME>.md           (cartridge-local override)
      2. <cartridge>/Artifacts/_Prototypes/<NAME>.md (OVE design-cartridge layout — v2.0.1)
      3. <root>/_Prototypes/<NAME>.md                (OV-root canonical home)

    The Artifacts/_Prototypes/ path covers OVE design cartridges specifically:
    per BOOTSTRAP-NEW-OV.md Step 1, a design cartridge nests its in-progress
    OV under Artifacts/. The new OV's Prototype definitions live there during
    design and only move to the OV root's _Prototypes/ when the OV ships.
    """
    if cartridge is not None:
        local = cartridge / "_Prototypes" / f"{prototype_name}.md"
        if local.exists():
            return local
        nested = cartridge / "Artifacts" / "_Prototypes" / f"{prototype_name}.md"
        if nested.exists():
            return nested
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


SOURCE_INVENTORY_PLACEHOLDERS = [
    "<TBD>",
    "<source-slug>",
    "<author year title>",
    "<OV Name>",
    "<ov-slug>",
    "<Source Identifier>",
]

VALID_INVENTORY_STATUSES = {"drafting", "inventoried", "read-acknowledged", "locked"}


def check_C11_source_inventory(root):
    """v2.0 Source Discipline (F13 prevention): if _source-inventory.md exists
    at OV root, status is valid and no template placeholders remain. Absence
    of the inventory file is informational (not every OV cites external sources)."""
    findings = []
    inv = root / "_source-inventory.md"
    if not inv.exists():
        findings.append(Finding(
            "C11-source-inv", "info", root,
            message="no _source-inventory.md at OV root — OK if this OV cites no external sources. "
                    "If sources are cited (CQ3 in BOOTSTRAP-NEW-OV.md), create the inventory before "
                    "ARTIFACT-DRAFT per 03-DESIGN-PROTOCOL.md Step 4.5."
        ))
        return findings
    try:
        text = inv.read_text(encoding="utf-8")
    except Exception as e:
        findings.append(Finding("C11-source-inv", "fail", inv, message=f"unreadable: {e}"))
        return findings

    status_m = re.search(r'^ove_Source_Inventory_Status:\s*([a-z\-]+)', text, re.MULTILINE)
    status = status_m.group(1) if status_m else None
    if status not in VALID_INVENTORY_STATUSES:
        findings.append(Finding(
            "C11-source-inv", "fail", inv,
            message=(f"ove_Source_Inventory_Status is '{status}' — must be one of "
                     f"{sorted(VALID_INVENTORY_STATUSES)}")
        ))

    for placeholder in SOURCE_INVENTORY_PLACEHOLDERS:
        if placeholder in text:
            findings.append(Finding(
                "C11-source-inv", "fail", inv,
                message=f"unfilled template placeholder remains: {placeholder}"
            ))

    if status in ("drafting", "inventoried"):
        findings.append(Finding(
            "C11-source-inv", "warn", inv,
            message=(f"inventory status '{status}' — ARTIFACT-DRAFT is gated until "
                     "'read-acknowledged' (03-DESIGN-PROTOCOL.md Step 4.5). Add per-source "
                     "AI-read acknowledgments and bump status.")
        ))

    return findings


def check_C12_citation_audit(root):
    """v2.0 Source Discipline: if _source-inventory.md is marked 'locked',
    _citation-audit-log.md must exist documenting verified cites (SHIP-PREP
    Phase 3.7 requirement)."""
    findings = []
    inv = root / "_source-inventory.md"
    audit = root / "_citation-audit-log.md"
    if not inv.exists():
        return findings  # no inventory → no audit obligation

    try:
        inv_text = inv.read_text(encoding="utf-8")
    except Exception:
        return findings

    status_m = re.search(r'^ove_Source_Inventory_Status:\s*([a-z\-]+)', inv_text, re.MULTILINE)
    status = status_m.group(1) if status_m else None

    if status == "locked":
        if not audit.exists():
            findings.append(Finding(
                "C12-citation-audit", "fail", root,
                message=("_source-inventory.md is marked 'locked' but _citation-audit-log.md "
                         "is missing. SHIP-PREP Phase 3.7 (07-SHIPPING-CHECKLIST.md) requires "
                         "the audit log before claiming inventory-locked.")
            ))
        else:
            try:
                audit_text = audit.read_text(encoding="utf-8")
                substantive = [l for l in audit_text.splitlines()
                               if l.strip() and not l.lstrip().startswith("#")
                               and not l.strip().startswith("---")]
                if len(substantive) < 3:
                    findings.append(Finding(
                        "C12-citation-audit", "warn", audit,
                        message=("audit log present but appears empty / placeholder-only. "
                                 "Phase 3.7 expects one entry per cite verified against source.")
                    ))
            except Exception:
                pass
    else:
        if not audit.exists():
            findings.append(Finding(
                "C12-citation-audit", "info", root,
                message=(f"_source-inventory.md present (status: {status}); audit log not yet "
                         "required (only at ship-time, Phase 3.7).")
            ))
    return findings


DELIVERABLE_PROMISE_NOUN_RE = re.compile(
    r'\b(dashboard|scorecard|playbook)\b',
    re.IGNORECASE
)


def check_C13_vocabulary_audit(root):
    """v2.0 Voice + Client Promise: if shippable content contains the high-
    confidence deliverable-promise nouns (dashboard, scorecard, playbook),
    _vocabulary-audit-log.md must record each instance's disposition. Broader
    sweep (report, framework, tool, etc.) is operator-driven via markdown grep
    at SHIP-PREP Phase 3.9 — those words have legitimate role-uses that would
    produce too many false positives here."""
    findings = []
    audit = root / "_vocabulary-audit-log.md"

    hits = []
    shippable_root_files = ["README.md", "OPERATOR-GUIDE.md", "CONTRIBUTING.md", "INSTALL.md"]
    for fname in shippable_root_files:
        f = root / fname
        if not f.exists():
            continue
        try:
            for lineno, line in iter_prose_lines(f):
                for m in DELIVERABLE_PROMISE_NOUN_RE.finditer(line):
                    hits.append((f, lineno, m.group(0)))
        except Exception:
            continue

    for sub in ("_design-engine", "_Prototypes"):
        subroot = root / sub
        if not subroot.is_dir():
            continue
        for f in subroot.rglob("*.md"):
            if is_skip_path(f, root):
                continue
            try:
                for lineno, line in iter_prose_lines(f):
                    for m in DELIVERABLE_PROMISE_NOUN_RE.finditer(line):
                        hits.append((f, lineno, m.group(0)))
            except Exception:
                continue

    if not hits:
        return findings

    if not audit.exists():
        for (f, lineno, word) in hits[:5]:
            findings.append(Finding(
                "C13-vocab-audit", "warn", f, line=lineno,
                message=(f"deliverable-promise noun '{word}' found; _vocabulary-audit-log.md "
                         "must record its disposition (kept-with-justification or replaced) "
                         "before ship (07-SHIPPING-CHECKLIST.md Phase 3.9).")
            ))
        if len(hits) > 5:
            findings.append(Finding(
                "C13-vocab-audit", "warn", root,
                message=f"...and {len(hits) - 5} more deliverable-promise noun hits not shown."
            ))
    else:
        try:
            audit_text = audit.read_text(encoding="utf-8")
            for (f, lineno, word) in hits:
                try:
                    rel_f = str(f.relative_to(root))
                except ValueError:
                    rel_f = f.name
                if word.lower() not in audit_text.lower() and rel_f not in audit_text:
                    findings.append(Finding(
                        "C13-vocab-audit", "warn", f, line=lineno,
                        message=(f"deliverable-promise noun '{word}' found, but no matching "
                                 "entry in _vocabulary-audit-log.md.")
                    ))
        except Exception:
            pass

    return findings


# ---------------------------------------------------------------------------
# C14 — Standalone Sufficiency posture (Convention 10)
# ---------------------------------------------------------------------------

# T0 hard gates that must ship as 'met' on every OV (Convention 10).
T0_REQ_IDS = ["REQ-A1", "REQ-A2", "REQ-A3", "REQ-B1", "REQ-H4"]

# TG conditional gates — mandatory when domain_stakes: high.
TG_REQ_IDS = [
    "REQ-I1", "REQ-I2", "REQ-I3", "REQ-I4", "REQ-I5",
    "REQ-K1", "REQ-K2", "REQ-K3",
]

# Five moat items — at least one must be committed with a schema_feature.
MOAT_REQ_IDS = ["REQ-E4", "REQ-M1", "REQ-M2", "REQ-M3", "REQ-M4"]

VALID_DISPOSITIONS = {"met", "partial", "n-a", "deferred"}


def _parse_disposition(text, req_id):
    """Find the disposition for req_id in a posture.yaml text. Returns the
    disposition string or None. Tolerates both verbose ('REQ-X:\\n  disposition: met')
    and compact ('REQ-X: { disposition: met, ... }') YAML forms.
    """
    # Match REQ-ID followed by anything up to its disposition. Non-greedy to
    # avoid running into the next REQ-ID. Allow ~400 chars of separation for
    # the verbose form's evidence/notes lines.
    pattern = re.compile(
        re.escape(req_id) + r":\s*(?:\{[^{}]*?disposition:|.*?\n\s*disposition:)\s*([\w-]+)",
        re.DOTALL,
    )
    m = pattern.search(text)
    if m:
        return m.group(1).strip().lower()
    return None


def _parse_domain_stakes(text):
    m = re.search(r'^domain_stakes:\s*"?(\w+)"?', text, re.MULTILINE)
    return m.group(1).strip().lower() if m else None


def _parse_moat_commitments(text):
    """Return list of dicts with keys 'req_id' and 'schema_feature' (each may be empty)."""
    # Find moat_commitments: block and grab everything until the next top-level key.
    m = re.search(r'^moat_commitments:(.*?)(?=^\w|\Z)', text, re.MULTILINE | re.DOTALL)
    if not m:
        return []
    block = m.group(1)
    commitments = []
    # Each entry begins with "- req_id:" (allowing leading whitespace).
    entries = re.findall(
        r'-\s*req_id:\s*"?([\w-]+)"?(?:.*?schema_feature:\s*"([^"]*)")?',
        block, re.DOTALL,
    )
    for req_id, schema_feature in entries:
        commitments.append({
            "req_id": req_id.strip(),
            "schema_feature": (schema_feature or "").strip(),
        })
    return commitments


def _parse_deferred(text):
    """Return (deferred_until_str, rationale, responsible_party) from posture-deferred.yaml."""
    until = re.search(r'^deferred_until:\s*"?([\d-]+)"?', text, re.MULTILINE)
    rationale = re.search(r'^rationale:\s*[|>]?\s*\n((?:\s+\S.*\n?)+)', text, re.MULTILINE)
    if not rationale:
        rationale = re.search(r'^rationale:\s*"([^"]*)"', text, re.MULTILINE)
    party = re.search(r'^responsible_party:\s*"?([^"\n]+)"?', text, re.MULTILINE)
    return (
        until.group(1) if until else None,
        rationale.group(1).strip() if rationale else None,
        party.group(1).strip() if party else None,
    )


def _is_date_past(date_str):
    """Return True if YYYY-MM-DD string is in the past relative to today.
    Returns False on parse failure (treats unparseable as not-yet-expired).
    """
    if not date_str:
        return False
    try:
        from datetime import date
        parts = date_str.strip().split("-")
        if len(parts) != 3:
            return False
        target = date(int(parts[0]), int(parts[1]), int(parts[2]))
        return target < date.today()
    except Exception:
        return False


def check_C14_standalone_sufficiency_posture(root, cartridges):
    """Convention 10 (v2.2.0): each cartridge (OV) ships a Standalone Sufficiency
    posture — standalone-sufficiency-posture.md at root, _meta/posture.yaml at
    root (source of truth), _meta/vetting-rubric-filled.md at root (filled
    scorecard). All 5 T0 hard gates must be 'met'; if domain_stakes is 'high',
    all 8 TG gates must be 'met'; at least one of the 5 moat items must be
    committed with a non-empty schema_feature.

    OVs may opt out via posture-deferred.yaml at root (with deferred_until,
    rationale, responsible_party). Deferred OVs warn (not fail) until the
    horizon date elapses, then warn escalates to surfacing.
    """
    findings = []

    for cart in cartridges:
        posture_md = cart / "standalone-sufficiency-posture.md"
        posture_yaml = cart / "_meta" / "posture.yaml"
        rubric = cart / "_meta" / "vetting-rubric-filled.md"
        deferred = cart / "posture-deferred.yaml"

        # Opt-out path: posture-deferred.yaml present.
        if deferred.exists():
            try:
                dtext = deferred.read_text(encoding="utf-8")
            except Exception as e:
                findings.append(Finding(
                    "C14-posture", "warn", deferred,
                    message=f"posture-deferred.yaml present but unreadable: {e}"
                ))
                continue
            until, rationale, party = _parse_deferred(dtext)
            if not until:
                findings.append(Finding(
                    "C14-posture", "fail", deferred,
                    message="posture-deferred.yaml is missing required 'deferred_until' field."
                ))
                continue
            if not rationale:
                findings.append(Finding(
                    "C14-posture", "warn", deferred,
                    message="posture-deferred.yaml has no 'rationale' field — please document why."
                ))
            if not party:
                findings.append(Finding(
                    "C14-posture", "warn", deferred,
                    message="posture-deferred.yaml has no 'responsible_party' field."
                ))
            if _is_date_past(until):
                findings.append(Finding(
                    "C14-posture", "warn", deferred,
                    message=(f"posture-deferred.yaml deferred_until={until} is in the past — "
                             "retrofit the posture now or extend the horizon with documented reason.")
                ))
            else:
                findings.append(Finding(
                    "C14-posture", "info", cart,
                    message=(f"Standalone Sufficiency posture deferred until {until}. "
                             "Convention 10 C14 check skipped per opt-out marker.")
                ))
            continue  # Skip the rest of the C14 checks for this cartridge.

        # Full-posture path: all three artifacts must exist.
        if not posture_md.exists():
            findings.append(Finding(
                "C14-posture", "fail", cart,
                message=("Convention 10 violation: standalone-sufficiency-posture.md is missing "
                         "at the OV root. Either ship the posture artifact or add posture-deferred.yaml "
                         "with deferred_until + rationale.")
            ))
            continue

        if not posture_yaml.exists():
            findings.append(Finding(
                "C14-posture", "fail", cart,
                message=("Convention 10 violation: _meta/posture.yaml (source of truth) is missing. "
                         "The posture markdown cannot be verified without it.")
            ))
            continue

        try:
            ptext = posture_yaml.read_text(encoding="utf-8")
        except Exception as e:
            findings.append(Finding(
                "C14-posture", "fail", posture_yaml,
                message=f"could not read posture.yaml: {e}"
            ))
            continue

        # domain_stakes flag.
        stakes = _parse_domain_stakes(ptext)
        if stakes is None:
            findings.append(Finding(
                "C14-posture", "fail", posture_yaml,
                message="posture.yaml is missing 'domain_stakes' (must be 'low' or 'high')."
            ))
            continue
        if stakes not in ("low", "high"):
            findings.append(Finding(
                "C14-posture", "fail", posture_yaml,
                message=f"posture.yaml domain_stakes='{stakes}' is not 'low' or 'high'."
            ))
            continue

        # T0 hard gates: all 5 must be 'met'.
        for req in T0_REQ_IDS:
            disp = _parse_disposition(ptext, req)
            if disp is None:
                findings.append(Finding(
                    "C14-posture", "fail", posture_yaml,
                    message=f"T0 hard gate {req} has no disposition in posture.yaml."
                ))
            elif disp not in VALID_DISPOSITIONS:
                findings.append(Finding(
                    "C14-posture", "fail", posture_yaml,
                    message=f"T0 hard gate {req} has invalid disposition '{disp}'."
                ))
            elif disp != "met":
                # Allow partial/deferred only with explicit waiver field; we don't parse the
                # waiver shape (free text), so any non-'met' T0 fails C14 to force operator
                # to explicitly justify it elsewhere (e.g., _design-decisions.md).
                findings.append(Finding(
                    "C14-posture", "fail", posture_yaml,
                    message=(f"T0 hard gate {req} disposition='{disp}' — T0 gates must ship as 'met' "
                             "(no exceptions without explicit waiver_reason).")
                ))

        # TG conditional gates: required if domain_stakes high.
        if stakes == "high":
            for req in TG_REQ_IDS:
                disp = _parse_disposition(ptext, req)
                if disp is None:
                    findings.append(Finding(
                        "C14-posture", "fail", posture_yaml,
                        message=(f"TG conditional gate {req} has no disposition; required because "
                                 "domain_stakes: high.")
                    ))
                elif disp not in VALID_DISPOSITIONS:
                    findings.append(Finding(
                        "C14-posture", "fail", posture_yaml,
                        message=f"TG conditional gate {req} has invalid disposition '{disp}'."
                    ))
                elif disp != "met":
                    findings.append(Finding(
                        "C14-posture", "fail", posture_yaml,
                        message=(f"TG conditional gate {req} disposition='{disp}' — TG gates must "
                                 "ship as 'met' when domain_stakes: high.")
                    ))

        # Moat commitments: at least one with non-empty schema_feature.
        commitments = _parse_moat_commitments(ptext)
        valid_moats = [
            c for c in commitments
            if c["req_id"] in MOAT_REQ_IDS and c["schema_feature"]
        ]
        if not commitments:
            findings.append(Finding(
                "C14-posture", "warn", posture_yaml,
                message=("No moat commitments declared. Convention 10 requires ≥1 moat item "
                         "(REQ-E4/M1/M2/M3/M4) with a concrete schema_feature pointer.")
            ))
        elif not valid_moats:
            findings.append(Finding(
                "C14-posture", "warn", posture_yaml,
                message=("Moat commitments are present but none has both a valid moat REQ-ID "
                         "AND a non-empty schema_feature. A commitment without a schema feature "
                         "is a wish, not a moat.")
            ))

        # Vetting rubric filled artifact.
        if not rubric.exists():
            findings.append(Finding(
                "C14-posture", "fail", cart,
                message=("Convention 10 violation: _meta/vetting-rubric-filled.md is missing. "
                         "The filled 0-3 scorecard with verdict band must ship.")
            ))

    return findings


# ---------------------------------------------------------------------------
# Convention 11 — Knowledge-augmented OVs (OKF data plane)
# ---------------------------------------------------------------------------

_OKF_RESERVED = {"index.md", "log.md"}
_TYPE_RE = re.compile(r'^type:\s*(\S.*)$', re.MULTILINE)
_SOURCE_PSEUDO_RE = re.compile(r'\[Source:[^\]]*\]', re.IGNORECASE)
_LEADING_SLASH_KNOWLEDGE_RE = re.compile(r'\]\(/[^)]*_knowledge/')


def _parse_knowledge_source(manifest_text):
    """Return the declared ove_Knowledge_Source value (default 'self_contained')."""
    m = re.search(r'^ove_Knowledge_Source:\s*"?([\w-]+)"?', manifest_text, re.MULTILINE)
    return m.group(1).strip().lower() if m else "self_contained"


def _iter_uncommented_lines(text):
    """Yield lines whose first non-space character is not '#' (skips YAML comments
    and the commented-out scaffold in the manifest template)."""
    for line in text.splitlines():
        if line.lstrip().startswith("#"):
            continue
        yield line


def _parse_knowledge_mounts(manifest_text):
    """Parse active (uncommented) Knowledge_Mounts entries from a manifest.

    Tolerates the entries living in frontmatter or in a fenced YAML block in the
    body; commented scaffold lines are ignored. Returns a list of dicts with keys
    bundle_root, ship_disposition, okf_version, has_pin.
    """
    lines = list(_iter_uncommented_lines(manifest_text))
    mounts = []
    current = None
    for line in lines:
        bm = re.match(r'\s*-\s*bundle_root:\s*"?([^"\n]+?)"?\s*$', line)
        if bm:
            if current is not None:
                mounts.append(current)
            current = {"bundle_root": bm.group(1).strip(),
                       "ship_disposition": None, "okf_version": None, "has_pin": False}
            continue
        if current is None:
            continue
        sd = re.match(r'\s*ship_disposition:\s*"?([\w-]+)"?', line)
        if sd:
            current["ship_disposition"] = sd.group(1).strip().lower()
            continue
        ov = re.match(r'\s*okf_version:\s*"?([^"\n]+?)"?\s*$', line)
        if ov:
            current["okf_version"] = ov.group(1).strip()
            continue
        if re.match(r'\s*pin:\s*$', line):
            current["has_pin"] = True
            continue
        if re.match(r'\s*(git_sha|vetted_timestamp):\s*"?\S', line):
            current["has_pin"] = True
            continue
    if current is not None:
        mounts.append(current)
    return mounts


def check_C15_knowledge_mounts(root, cartridges):
    """Convention 11 (v2.3.0): a knowledge-augmented OV must vendor each declared
    OKF mount under _knowledge/, set okf_version + pin, and the bundle must pass
    OKF v0.1 conformance (every non-reserved .md carries a non-empty `type`).
    A self_contained OV (the default, empty mount list) passes trivially.
    """
    findings = []
    for cart in cartridges:
        manifest = cart / "_ov-manifest.md"
        if not manifest.exists():
            continue  # reported by C1
        try:
            text = manifest.read_text(encoding="utf-8")
        except Exception:
            continue  # reported by C2
        source = _parse_knowledge_source(text)
        if source == "self_contained":
            continue
        if source != "knowledge_augmented":
            findings.append(Finding(
                "C15-mounts", "fail", manifest,
                message=(f"ove_Knowledge_Source: '{source}' is invalid — "
                         "must be 'self_contained' or 'knowledge_augmented' (Convention 11).")
            ))
            continue

        mounts = _parse_knowledge_mounts(text)
        if not mounts:
            findings.append(Finding(
                "C15-mounts", "fail", manifest,
                message=("ove_Knowledge_Source: knowledge_augmented but no Knowledge_Mounts "
                         "entries are declared (Convention 11).")
            ))
            continue

        for mount in mounts:
            br = mount["bundle_root"]
            if mount["ship_disposition"] != "vendored":
                findings.append(Finding(
                    "C15-mounts", "fail", manifest,
                    message=(f"mount '{br}': ship_disposition must be 'vendored' "
                             f"(got {mount['ship_disposition']!r}) — Convention 11 forbids live external mounts.")
                ))
            if not mount["okf_version"]:
                findings.append(Finding(
                    "C15-mounts", "fail", manifest,
                    message=f"mount '{br}': missing okf_version (no OKF version pin)."
                ))
            if not mount["has_pin"]:
                findings.append(Finding(
                    "C15-mounts", "fail", manifest,
                    message=f"mount '{br}': missing pin (git_sha and/or vetted_timestamp) — no re-verification baseline."
                ))

            bundle_dir = (cart / br).resolve()
            try:
                inside = str(bundle_dir).startswith(str((cart / "_knowledge").resolve()))
            except Exception:
                inside = False
            if not inside:
                findings.append(Finding(
                    "C15-mounts", "fail", manifest,
                    message=f"mount '{br}': bundle_root must live under {cart.name}/_knowledge/ (vendored)."
                ))
                continue
            if not bundle_dir.is_dir():
                findings.append(Finding(
                    "C15-mounts", "fail", manifest,
                    message=f"mount '{br}': vendored bundle directory not found (bytes must ship with the OV)."
                ))
                continue

            # OKF v0.1 §9 conformance: every non-reserved .md has a non-empty `type`.
            concepts = [p for p in bundle_dir.rglob("*.md") if p.name not in _OKF_RESERVED]
            if not concepts:
                findings.append(Finding(
                    "C15-mounts", "warn", bundle_dir,
                    message=f"mount '{br}': no OKF concept documents found under the vendored bundle."
                ))
            for concept in concepts:
                try:
                    ctext = concept.read_text(encoding="utf-8")
                except Exception as e:
                    findings.append(Finding(
                        "C15-mounts", "fail", concept,
                        message=f"OKF concept unreadable: {e}"
                    ))
                    continue
                fm = FRONTMATTER_RE.match(ctext)
                if not fm:
                    findings.append(Finding(
                        "C15-mounts", "fail", concept,
                        message="OKF non-conformant: concept has no parseable YAML frontmatter (OKF §9)."
                    ))
                    continue
                tm = _TYPE_RE.search(fm.group(1))
                if not tm or not tm.group(1).strip():
                    findings.append(Finding(
                        "C15-mounts", "fail", concept,
                        message="OKF non-conformant: concept frontmatter has no non-empty `type` (OKF §9)."
                    ))
    return findings


def check_C16_dataplane_citations(root, cartridges):
    """Convention 11 (v2.3.0): data-plane citations must be real markdown links,
    not the [Source: ...] pseudo-syntax (which is not OKF). Leading-slash links
    into _knowledge/ warn (OKF reference tooling forbids leading-slash links).
    Scoped to cartridge content; engine/proposal prose discussing the anti-pattern
    keeps it inside backticks, which iter_prose_lines strips.
    """
    findings = []
    for cart in cartridges:
        for f in sorted(cart.rglob("*.md")):
            if is_skip_path(f, root):
                continue
            try:
                for lineno, line in iter_prose_lines(f):
                    if _SOURCE_PSEUDO_RE.search(line):
                        findings.append(Finding(
                            "C16-citations", "fail", f, line=lineno,
                            message="[Source: ...] pseudo-citation is not OKF — use a markdown link or a # Citations entry (Convention 11)."
                        ))
                    if _LEADING_SLASH_KNOWLEDGE_RE.search(line):
                        findings.append(Finding(
                            "C16-citations", "warn", f, line=lineno,
                            message="leading-slash link into _knowledge/ — OKF reference tooling uses file-relative links (Convention 11)."
                        ))
            except Exception as e:
                findings.append(Finding(
                    "C16-citations", "warn", f,
                    message=f"could not scan: {e}"
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
    if "C11" in checks:
        findings.extend(check_C11_source_inventory(root))
    if "C12" in checks:
        findings.extend(check_C12_citation_audit(root))
    if "C13" in checks:
        findings.extend(check_C13_vocabulary_audit(root))
    if "C14" in checks:
        findings.extend(check_C14_standalone_sufficiency_posture(root, cartridges))
    if "C15" in checks:
        findings.extend(check_C15_knowledge_mounts(root, cartridges))
    if "C16" in checks:
        findings.extend(check_C16_dataplane_citations(root, cartridges))
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
    checks = {f"C{i}" for i in range(1, 17)} - skip

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
