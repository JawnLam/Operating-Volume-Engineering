---
Item_Prototype: Fleeting
Item_ID: ove-meta-validation-checklist
Title: "OVE Meta — Validation Checklist"
Date_Added: 2026-06-01
Date_Modified: 2026-06-06
Needs_Processing: false
type: design-engine-meta
role: validation-checklist
scope: subject-agnostic
updated: 2026-06-06
---

# Validation Checklist (Prose Fallback)

> **For markdown-only environments where `validate.py` cannot be run, or when the operator prefers a manual walkthrough. Mirrors the checks the script performs. Run before `07-SHIPPING-CHECKLIST.md` Phase 3 (personal-data scrub) and Phase 6 (README polish).**

## C1 — Cartridge backbone presence

For each cartridge folder in the OV root (excluding `_design-engine/` and dot/underscore-prefixed entries):

- [ ] `_ov-manifest.md` exists
- [ ] `_design-state.md` exists
- [ ] `_design-decisions.md` exists
- [ ] `_schema-draft.md` exists

If any is missing, the cartridge is incomplete — return to the design protocol.

## C2 — Cartridge frontmatter present

For each backbone file:

- [ ] Starts with a YAML frontmatter block (`---` … `---`)
- [ ] The block is not empty

## C3 — Placeholder leakage

Walk every `.md` file except those inside `_design-engine/_templates/`. Check for these tokens:

- `<USER_NAME>`, `[USER NAME]`, `<USER NAME>`, `[USER_NAME]`
- `<USER_EMAIL>`, `<COMPANY>`, `<CLIENT>`
- `<author>`, `[author]`
- `<TBD>`, `<TODO>`
- `<your-name-here>`, `<your-domain>`, `<placeholder>`

Or via grep:

```bash
grep -rEn '<USER[_ ]NAME>|\[USER[_ ]NAME\]|<USER[_ ]EMAIL>|<COMPANY>|<CLIENT>|<author>|\[author\]|<TBD>|<TODO>|<your-name-here>|<your[_ ]domain>|<placeholder>' \
  <NewOV> --include="*.md" --exclude-dir=_templates
```

- [ ] Zero hits (any hit is a leak — replace with the operator-confirmed value or remove)

## C4 — Identity from indirect signals (F3 class)

- [ ] `_USER.md` exists with the operator-confirmed name (or the absence of `_USER.md` is acknowledged)
- [ ] `LICENSE.md` attribution name matches the operator-confirmed name exactly (case-insensitive)
- [ ] No third-person reference to the operator in shipping files uses a name that could have been parsed from a username (e.g., "John Lam" from `jawnlam`)

The "Jawn-Lam-not-John-Lam" pattern is documented in `_design-engine/_meta/FAILURE-MODES.md`. Treat any name in a shipping file as suspect until confirmed against the source.

## C5 — Dangling wikilinks

Walk every `.md` file except `_design-engine/_templates/`. For each `[[X]]` reference, verify `X` resolves to a file in the OV (the file's basename or stem matches `X`).

```bash
grep -rEn '\[\[[^]]+\]\]' <NewOV> --include="*.md" --exclude-dir=_templates
```

- [ ] Every wikilink target resolves
- [ ] (Wikilinks with `|alias` or `#heading` modifiers: strip them and resolve the base target)

## C6 — Bootstrap vs engine agreement (F6 drift)

This is the highest-risk drift to catch — the root-mirror / engine-canonical divergence the engine itself warns about.

- [ ] `AI-BOOTSTRAP.md` and `_design-engine/00-START-HERE.md` both have a "Tier 1" section and a "Tier 2" section
- [ ] Both list the **same** Tier 1 engine files (the `NN-NAME.md` references inside the Tier 1 section)
- [ ] `AI-BOOTSTRAP.md` explicitly names `00-START-HERE.md` as canonical
- [ ] The relationship between the two files is stated in-prose ("if they disagree, the engine file wins")

If any of these fails, the F6 violation must be fixed before ship — silent drift between root and engine is the failure mode the engine itself catalogues.

## C7 — Prototype coverage (Convention 6)

- [ ] Every cartridge `.md` file's `Item_Prototype:` value (excluding `Fleeting`) has a corresponding definition file in `_Prototypes/<NAMESPACE>_<TypeName>.md` at the OV root, or in `<Cartridge>/_Prototypes/<NAMESPACE>_<TypeName>.md` (cartridge-local override)

Shell recipe:

```bash
# List every distinct Item_Prototype value used in any cartridge
grep -rh '^Item_Prototype:' <Cartridge>/*.md <Cartridge>/**/*.md 2>/dev/null \
  | sort -u | grep -v 'Fleeting'

# For each value, confirm a matching file exists in _Prototypes/
```

If any value lacks a definition file, ship is locked. Materialize the missing Prototype per `04-SCHEMA-DESIGN.md § "Materializing the _Prototypes/ folder"`.

## C8 — Zone-boundary documentation (Convention 8)

- [ ] `CONTRIBUTING.md` (or `OPERATOR-GUIDE.md` as fallback) contains all four canonical zone-name strings: **`Engine Zone`**, **`Operator-Private Zone`**, **`Operator-Extension Zone`**, **`Shipped Examples Zone`**
- [ ] If using operator-chosen synonyms, the synonym choice is documented in `_design-decisions.md`

Shell recipe:

```bash
grep -E 'Engine Zone|Operator-Private Zone|Operator-Extension Zone|Shipped Examples Zone' \
  CONTRIBUTING.md OPERATOR-GUIDE.md
```

Expected: all four phrases appear at least once. Missing any of them is a Convention 8 partial; missing all four is a Convention 8 violation.

## C9 — `.gitignore` sanity (Convention 8)

- [ ] `.gitignore` exists at the OV root
- [ ] `.gitignore` contains at least one substantive (non-blank, non-comment) pattern matching the Operator-Private Zone declared in `CONTRIBUTING.md`

Shell recipe:

```bash
# .gitignore present?
ls -la .gitignore

# substantive patterns count
grep -v '^\s*$\|^#' .gitignore | wc -l
```

Expected: file exists; count > 0.

## C11 — Source inventory completeness (F13 prevention — v2.0)

If the OV cites external source material (per CQ3 in `BOOTSTRAP-NEW-OV.md`), `_source-inventory.md` exists at the OV root and is fully populated. Absence of the inventory file is OK only if the OV cites no external sources.

- [ ] `_source-inventory.md` exists at the OV root (or the OV cites no external sources, in which case skip this check)
- [ ] `ove_Source_Inventory_Status` in the frontmatter is one of: `drafting`, `inventoried`, `read-acknowledged`, `locked`
- [ ] No unfilled template placeholders remain (`<TBD>`, `<source-slug>`, `<author year title>`, `<OV Name>`, `<ov-slug>`, `<Source Identifier>`)
- [ ] For ARTIFACT-DRAFT to proceed: status is `read-acknowledged` or `locked` (not `drafting` or `inventoried`)
- [ ] For SHIP-PREP to proceed (Phase 3.7): status is `locked`

Shell recipe:

```bash
# Inventory present?
ls -la _source-inventory.md

# Status check
grep '^ove_Source_Inventory_Status:' _source-inventory.md

# Placeholder check
grep -E '<TBD>|<source-slug>|<author year title>|<OV Name>|<ov-slug>|<Source Identifier>' _source-inventory.md && echo "FAIL: placeholders remain"
```

If `_source-inventory.md` does not exist but the OV's prose cites external sources, return to CQ3 (`BOOTSTRAP-NEW-OV.md`) to structurally capture them. F13 (`_meta/FAILURE-MODES.md`) documents the source-grounding-skipped failure mode this gate prevents.

## C12 — Citation audit log (F13 prevention — v2.0)

If `_source-inventory.md` is marked `locked`, `_citation-audit-log.md` must exist documenting that every "p.XX / § X.Y / named theorist / verbatim quote" in shippable content has been verified against its canonical source. Required at SHIP-PREP Phase 3.7.

- [ ] If `_source-inventory.md` is `locked`: `_citation-audit-log.md` exists with substantive content (more than placeholder lines)
- [ ] Every cite in shippable content traces to a source listed in `_source-inventory.md`
- [ ] Every cite's content verified against the canonical source (operator-confirmed; not session-memory paraphrase)

Shell recipe:

```bash
# Citation audit log present?
ls -la _citation-audit-log.md

# Cites in shippable content
grep -rEhn 'p\.\s*[0-9]+|§\s*[0-9]+(\.[0-9]+)+' \
  _*-engine _Prototypes README.md OPERATOR-GUIDE.md CONTRIBUTING.md INSTALL.md 2>/dev/null

# Cross-check: each grep hit appears in the audit log (the operator's responsibility)
```

If `_source-inventory.md` exists but status is not `locked`, the audit log is not yet required (it only becomes required at SHIP-PREP Phase 3.7).

## C13 — Vocabulary audit log (Voice + Client Promise — v2.0)

If shippable content contains deliverable-promise nouns (dashboard, scorecard, playbook — the high-confidence set; broader sweep operator-driven), `_vocabulary-audit-log.md` must record each instance's disposition (kept-with-justification or replaced).

- [ ] Sweep shippable content for deliverable-promise nouns
- [ ] If any hit: `_vocabulary-audit-log.md` exists and records each instance's disposition
- [ ] Audience-register violations against `ove_Audience_Prose_Register` (declared in the OV's manifest per Q14) are either fixed or explicitly waived in `_design-decisions.md`

Shell recipe:

```bash
# High-confidence deliverable-promise noun sweep
grep -rEhin '\b(dashboard|scorecard|playbook)\b' \
  _*-engine _Prototypes README.md OPERATOR-GUIDE.md CONTRIBUTING.md INSTALL.md 2>/dev/null

# Broader sweep (operator-discretion — these have legitimate role-uses too)
grep -rEhin '\b(report|framework|tool)\b' \
  _*-engine _Prototypes README.md OPERATOR-GUIDE.md CONTRIBUTING.md INSTALL.md 2>/dev/null
```

For each hit, decide:

- **Kept-with-justification:** the word is a real artifact the OV ships, OR a meta-reference (OVE itself naming the noun in its own vocabulary-audit documentation), OR a role-word use that's clearly not a deliverable promise.
- **Replaced:** the word is a deliverable-promise noun that anchors an artifact the OV does not actually ship — replace with a role-word (frame, lens, mental map, conceptual frame, conversational frame, capture, log, summary, method, approach, discipline, practice, pattern, move).

Log each disposition to `_vocabulary-audit-log.md` as `<file:line> | <word> | <disposition> | <one-line justification>`.

## C10 — `UPDATE-PROMPT.md` sanity (Convention 7)

- [ ] `UPDATE-PROMPT.md` exists at the OV root
- [ ] The OV's name is filled in concretely (no `<OV-Name>`, `<ov-slug>`, or `<author>` template placeholders remain)
- [ ] The prompt block references `INSTALL.md` and `OPERATOR-GUIDE.md` so the AI consults canonical docs
- [ ] The prompt block references the four-zone boundary (any of: "zone", "four-zone", "Operator-Extension")
- [ ] The prompt block instructs the AI to stop and confirm before destructive commands (any of: "destructive", "confirm", "approve", "stop and ask")

Shell recipe:

```bash
# present?
ls -la UPDATE-PROMPT.md

# placeholders?
grep -E '<OV-Name>|<ov-slug>|<author>' UPDATE-PROMPT.md && echo "FAIL: placeholders remain"

# content sanity
grep -q 'INSTALL.md' UPDATE-PROMPT.md && echo "OK: references INSTALL.md"
grep -q 'OPERATOR-GUIDE.md' UPDATE-PROMPT.md && echo "OK: references OPERATOR-GUIDE.md"
grep -qE 'zone|four-zone|Operator-Extension' UPDATE-PROMPT.md && echo "OK: references zone boundary"
grep -qiE 'destructive|confirm|approve|stop and ask' UPDATE-PROMPT.md && echo "OK: confirms before destructive commands"
```

Missing file is a `fail`. Content sanity gaps are `warn`-level (operators may legitimately customize the prompt to a different shape).

---

## Overall outcome

- [ ] All C1–C13 checks pass, or every warning is explicitly waived by the operator with a written rationale
- [ ] No `fail`-class finding remains unresolved

If `validate.py` is available, run it as well; this prose walkthrough is the fallback, not the canonical check.
