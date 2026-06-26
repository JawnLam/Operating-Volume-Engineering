---
type: Fleeting
timestamp: "2026-06-06T00:00:00Z"
Item_ID: ove-meta-validation-checklist
title: "OVE Meta — Validation Checklist"
Date_Added: 2026-06-01
Date_Modified: 2026-06-06
Needs_Processing: false
doc_type: design-engine-meta
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

- [ ] Every cartridge `.md` file's `type:` value (excluding `Fleeting`) has a corresponding definition file in `_types/<NAMESPACE>_<TypeName>.md` at the OV root, or in `<Cartridge>/_types/<NAMESPACE>_<TypeName>.md` (cartridge-local override)

Shell recipe:

```bash
# List every distinct type value used in any cartridge
grep -rh '^type:' <Cartridge>/*.md <Cartridge>/**/*.md 2>/dev/null \
  | sort -u | grep -v 'Fleeting'

# For each value, confirm a matching file exists in _types/
```

If any value lacks a definition file, ship is locked. Materialize the missing Prototype per `04-SCHEMA-DESIGN.md § "Materializing the _types/ folder"`.

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
  _*-engine _types README.md OPERATOR-GUIDE.md CONTRIBUTING.md INSTALL.md 2>/dev/null

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
  _*-engine _types README.md OPERATOR-GUIDE.md CONTRIBUTING.md INSTALL.md 2>/dev/null

# Broader sweep (operator-discretion — these have legitimate role-uses too)
grep -rEhin '\b(report|framework|tool)\b' \
  _*-engine _types README.md OPERATOR-GUIDE.md CONTRIBUTING.md INSTALL.md 2>/dev/null
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

## C14 — Standalone Sufficiency posture (Convention 10)

For each cartridge (each OV designed via OVE), check Convention 10 compliance. This mirrors `check_C14_standalone_sufficiency_posture()` in `validate.py`.

### Step 1 — Opt-out marker (skip rest of C14 if present)

```bash
# Per cartridge, check for opt-out marker first
ls <Cartridge>/posture-deferred.yaml
```

If `posture-deferred.yaml` exists:

- [ ] Open it and confirm `deferred_until: "YYYY-MM-DD"` is present
- [ ] Confirm `rationale:` is non-empty (`warn` if missing)
- [ ] Confirm `responsible_party:` is non-empty (`warn` if missing)
- [ ] Confirm `deferred_until` is in the future (`warn` if past — escalate to operator)

If all four are clean: this cartridge is **deferred-with-rationale**; C14 status = `info`. Skip to next cartridge.

### Step 2 — Full posture artifacts must exist

If no `posture-deferred.yaml`, the cartridge must ship the full Convention 10 cascade:

```bash
ls <Cartridge>/standalone-sufficiency-posture.md
ls <Cartridge>/_meta/posture.yaml
ls <Cartridge>/_meta/vetting-rubric-filled.md
```

- [ ] `standalone-sufficiency-posture.md` present at OV root — `fail` if missing
- [ ] `_meta/posture.yaml` present — `fail` if missing
- [ ] `_meta/vetting-rubric-filled.md` present — `fail` if missing

### Step 3 — `domain_stakes` is declared

```bash
grep -E '^domain_stakes:' <Cartridge>/_meta/posture.yaml
```

- [ ] Value is `low` OR `high` — anything else (or missing) is `fail`

### Step 4 — All 5 T0 hard gates ship as `met`

The five T0 hard gates: **REQ-A1, REQ-A2, REQ-A3, REQ-B1, REQ-H4**. None may ship as `partial` or `deferred` without a `waiver_reason` (and the waiver must be reviewable in `_design-decisions.md`).

For each REQ-ID, find its disposition in `_meta/posture.yaml`:

```bash
# For verbose form
grep -A 3 'REQ-A1:' <Cartridge>/_meta/posture.yaml | grep 'disposition'

# For compact inline-dict form
grep 'REQ-A1:' <Cartridge>/_meta/posture.yaml
```

- [ ] `REQ-A1` (Capability Parity) = `met` — `fail` otherwise
- [ ] `REQ-A2` (Graceful Scope Boundaries) = `met` — `fail` otherwise
- [ ] `REQ-A3` (No Artificial Lobotomy) = `met` — `fail` otherwise
- [ ] `REQ-B1` (Persistent User Model) = `met` — `fail` otherwise
- [ ] `REQ-H4` (Time-to-First-Value Activation) = `met` — `fail` otherwise

### Step 5 — 8 TG conditional gates per declared stakes

If `domain_stakes: high`, the 8 TG conditional gates are mandatory: **REQ-I1, REQ-I2, REQ-I3, REQ-I4, REQ-I5, REQ-K1, REQ-K2, REQ-K3**. If `domain_stakes: low`, the 8 gates default to `n-a` (no justification required).

- [ ] If high: all 8 dispositions = `met` — `fail` otherwise
- [ ] If low: 8 dispositions = `n-a` (or `met` if the OV chose to clear them anyway)

### Step 6 — ≥1 moat commitment with concrete `schema_feature`

The 5 moat items: **REQ-E4, REQ-M1, REQ-M2, REQ-M3, REQ-M4**. At least one must be in `posture.yaml` under `moat_commitments` with a non-empty `schema_feature`. A commitment without a schema feature is a wish, not a moat.

```bash
grep -A 5 'moat_commitments:' <Cartridge>/_meta/posture.yaml
```

- [ ] At least one entry under `moat_commitments` — `warn` if none
- [ ] That entry's `req_id` is one of E4/M1/M2/M3/M4 — `warn` if not
- [ ] That entry's `schema_feature` is a non-empty string pointer — `warn` if empty

### Step 7 — Vetting rubric verdict populated

Open `_meta/vetting-rubric-filled.md` and confirm:

- [ ] Weighted score + percentage are populated (not `<N>` placeholders) — `fail` if placeholders remain
- [ ] Verdict band is one of *Defensible specialist*, *Viable*, *At risk* — `fail` if missing

### Outcome

- All Step 2–7 checks pass → C14 = `pass`
- Any Step 4 or 5 disposition missing/wrong → C14 = `fail`
- Step 6 issues only → C14 = `warn`
- `posture-deferred.yaml` present with valid future date → C14 = `info` (no further checks)

## C15 — Knowledge-mount conformance (Convention 11 — KAOV only)

Applies only if the manifest declares `ove_Knowledge_Source: knowledge_augmented`. A `self_contained` OV (the default, empty `Knowledge_Mounts`) passes trivially — skip to C16.

For each entry in `Knowledge_Mounts`:

- [ ] `ship_disposition` is `vendored` — `fail` otherwise (Convention 11 forbids live external mounts)
- [ ] `bundle_root` resolves to a directory under `_knowledge/` that actually contains the vendored bytes — `fail` if absent
- [ ] `okf_version` is set, and `pin` records a `git_sha` and/or `vetted_timestamp` — `fail` if missing (no re-verification baseline)
- [ ] The bundle passes **OKF v0.1 §9 conformance**: every non-reserved `.md` file has a parseable YAML frontmatter block with a non-empty `type` — `fail` otherwise

Shell recipe:

```bash
# Knowledge source disposition
grep -E '^ove_Knowledge_Source:' <Cartridge>/_ov-manifest.md

# For each vendored bundle: every non-reserved .md must carry a non-empty type:
for f in $(find <Cartridge>/_knowledge -name '*.md' ! -name index.md ! -name log.md); do
  head -20 "$f" | grep -qE '^type:\s*\S' || echo "FAIL (no type): $f"
done
```

Expected: declared disposition is `knowledge_augmented`; every concept file reports a `type`; no FAIL lines.

## C16 — Data-plane citation form (Convention 11 — KAOV only)

Applies only to knowledge-augmented OVs. Guards against the non-conformant citation syntax Gemini's source PRD proposed (`_proposals/OKF-conformance-notes.md` §6).

- [ ] No `[Source: …]` pseudo-citations anywhere in shippable content — `fail` on any hit
- [ ] Data-plane citations are real markdown links resolving into a declared mount (file-relative; not leading-slash) — `warn` on leading-slash links into `_knowledge/`

Shell recipe:

```bash
# Forbidden pseudo-citation syntax
grep -rEn '\[Source:[^]]*\]' <Cartridge> --include="*.md" --exclude-dir=_templates && echo "FAIL: [Source: …] pseudo-citation"

# Leading-slash links into the data plane (OKF reference tooling forbids these)
grep -rEn '\]\(/[^)]*_knowledge/' <Cartridge> --include="*.md" && echo "WARN: leading-slash data-plane link"
```

Expected: zero `[Source: …]` hits; data-plane references use file-relative markdown links.

---

## Overall outcome

- [ ] All C1–C16 checks pass, or every warning is explicitly waived by the operator with a written rationale
- [ ] No `fail`-class finding remains unresolved

If `validate.py` is available, run it as well; this prose walkthrough is the fallback, not the canonical check.
