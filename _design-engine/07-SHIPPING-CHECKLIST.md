---
Item_Prototype: Fleeting
Item_ID: ove-engine-07-shipping-checklist
Title: "OVE Engine — 07 Shipping Checklist"
Date_Added: 2026-06-01
Date_Modified: 2026-06-06
Needs_Processing: false
type: design-engine
role: shipping-checklist
scope: subject-agnostic
updated: 2026-06-01
---

# 07 — SHIPPING CHECKLIST

> **The end-of-design-engagement protocol. Walk this with the user when their OV's artifacts are drafted and reviewed. The output: a shippable folder, optionally pushed to GitHub.**

## Phase 1 — Pre-flight

Before any shipping work:

- [ ] All Q1–Q13 from `04-SCHEMA-DESIGN.md` have explicit answers
- [ ] `_schema-draft.md` is complete
- [ ] All standard artifacts have drafts in `Artifacts/`:
  - [ ] `AI-BOOTSTRAP.md`
  - [ ] `README.md`
  - [ ] `INSTALL.md`
  - [ ] `OPERATOR-GUIDE.md`
  - [ ] `CONTRIBUTING.md`
  - [ ] `LICENSE.md`
  - [ ] `VERSION.md`
  - [ ] `CHANGELOG.md`
  - [ ] `.gitignore`
  - [ ] Engine files (the new OV's `_<purpose>-engine/` contents)
  - [ ] Templates (the new OV's `_<purpose>-engine/_templates/` contents)
  - [ ] BOOTSTRAP-NEW-CARTRIDGE prompt (the new OV's cartridging prompt)
  - [ ] At least one worked-example cartridge for demonstration
- [ ] All artifacts have been REVIEW-passed

If any is no, return to ARTIFACT-DRAFT or REVIEW.

## Phase 2 — Create the new OV folder

Decide on a final location for the new OV. Common patterns:

- Sibling to other OVs in a cloud-synced folder (Dropbox, iCloud, etc.) — convenient for cross-device work
- A dedicated `Projects/` directory for code-style work
- An Obsidian vault parent if the user works in Obsidian

Create the empty folder. Copy artifacts from the cartridge's `Artifacts/` to the new folder:

```
<NewOV>/
├── README.md
├── AI-BOOTSTRAP.md
├── INSTALL.md
├── OPERATOR-GUIDE.md
├── CONTRIBUTING.md
├── LICENSE.md
├── VERSION.md
├── CHANGELOG.md
├── .gitignore
├── _USER.md.template     (if applicable)
├── _<purpose>-engine/
│   ├── 00-START-HERE.md
│   ├── (other engine files)
│   ├── BOOTSTRAP-NEW-<cartridge-kind>.md
│   ├── _templates/
│   └── _meta/
└── <Example-Cartridge>/  (the worked example that demonstrates the OV)
```

## Phase 3 — Personal-data scrub (HARD STOP)

**This phase is a hard ship gate. No proceeding to Phase 7 (git init) until Phase 3 returns clean.** The scrub guards the highest-embarrassment failure class — a wrong real name, a personal path, an internal client term in a shipped file. F3 (identity-from-indirect-signals) is documented as recurring; this gate exists because "remember to check" is not enough.

### Walk the file list

Walk through the new folder file by file. Check for:

- [ ] Real names (other than the author's intended attribution)
- [ ] Real email addresses
- [ ] Real phone numbers
- [ ] Personal file paths
- [ ] Real client/employer/project names
- [ ] Confidential domain terms
- [ ] Identifiers from the user's other work

For anything found, replace with placeholders (`<USER_NAME>`, `<COMPANY>`, etc.) or remove.

**Specifically check for**:

- The "name parsed from username" failure mode — anywhere a name appears, confirm it's the author's actual name as they provided it (e.g., "Jawn Lam," not "John Lam" inferred from `jawnlam`)
- Internal references to the design cartridge (paths that include the OVE folder)

### Run the gate

Preferred — automated:

```bash
python3 _design-engine/_meta/validate.py --root "<NewOV>"
```

The script runs C3 (placeholder leakage) and C4 (identity-from-indirect-signals) plus structural checks (C1, C2, C5, C6). Exit codes: **0 = clean (proceed); 1 = warnings only (each warning must be explicitly waived in writing — see below); 2 = failures (HARD STOP, return to scrub work).**

Markdown-only fallback when `python3` isn't available — walk the checks in `_design-engine/_meta/VALIDATION-CHECKLIST.md` and run the combined grep:

```bash
grep -rEn '<USER[_ ]NAME>|\[USER[_ ]NAME\]|<USER[_ ]EMAIL>|<COMPANY>|<CLIENT>|<author>|\[author\]|<TBD>|<TODO>|<your-name-here>|<your[_ ]domain>|<placeholder>|\bERA\b|Wingspire|Exit Ready|<specific-personal-terms>' "<NewOV>" --include="*.md" --exclude-dir=_templates
```

The grep must return **zero hits**, or every hit must be explicitly waived (see below).

### Waiving a hit (warnings only)

A `warn` finding (C4 attribution mismatch, C5 dangling wikilink) may be a legitimate edge case — but it does not pass silently. To waive, append a one-line entry to the cartridge's `_design-decisions.md` naming:

- the file and line,
- the apparent issue,
- the reason the apparent placeholder/mismatch is intentional.

Only `info`-class findings (e.g., C4 skipped because no `_USER.md`) and explicitly-waived `warn` findings count as "clean." A `fail` finding cannot be waived — it must be fixed before Phase 7.

### Acceptance — all must be true

- [ ] Validator returns exit code 0, **or** exit code 1 with every warning waived in `_design-decisions.md`
- [ ] (Markdown-only fallback) The combined grep returns zero hits, or every hit is waived in writing
- [ ] No real name, email, phone, path, client, or employer remains in shipping content (operator-confirmed)

**If any of these is no, return to scrub work. Phase 7 is locked until this gate is clean.**

## Phase 3.5 — `_Prototypes/` coverage gate (HARD STOP)

Convention 6 (`_meta/CONVENTIONS.md`) requires every OV to ship its own `_Prototypes/` folder containing one `.md` file per Prototype declared in the OV's namespace. Without this, every cartridge note's `Item_Prototype:` reference is a dangling pointer for anyone without a vault-wide central registry.

### Walk the Prototype list

- [ ] `<New-OV>/_Prototypes/` folder exists at the OV root
- [ ] Every Prototype declared in `_<purpose>-engine/_meta/SCHEMA-OF-SCHEMAS.md` (under `prototypes:` or equivalent) has a corresponding `<NAMESPACE>_<TypeName>.md` file in `_Prototypes/`
- [ ] Every `Item_Prototype: <NAMESPACE>_<TypeName>` value used anywhere in the OV's cartridges has a corresponding `<NAMESPACE>_<TypeName>.md` file in `_Prototypes/`
- [ ] Each Prototype file conforms to `_design-engine/_templates/TEMPLATE-Prototype.md` (Purpose, Required frontmatter, Body structure, Naming, Example, Relationships sections present)
- [ ] Each Prototype file's required frontmatter matches the property declarations in `_meta/SCHEMA-OF-SCHEMAS.md`
- [ ] The Fleeting Prototype is *not* duplicated in `_Prototypes/` — it's a vault-universal Prototype, not OV-specific

### Run the gate

If `validate.py` is in use:

```bash
python3 _design-engine/_meta/validate.py
```

Check 7 (C7 — Prototype coverage) walks every cartridge and confirms every distinct `Item_Prototype:` value resolves to a file in `_Prototypes/`. Missing files fail with `<file>:<line>` and the missing Prototype name.

If running markdown-only:

```bash
# List every Item_Prototype value used in any cartridge
grep -rh '^Item_Prototype:' <Cartridge>/*.md <Cartridge>/**/*.md 2>/dev/null | \
  sort -u | \
  grep -v 'Fleeting'
```

For each value listed, confirm a matching file exists in `_Prototypes/`.

### Acceptance — all must be true

- [ ] Every cartridge `Item_Prototype:` value (excluding `Fleeting`) has a definition file in `_Prototypes/`
- [ ] Every definition file conforms to `TEMPLATE-Prototype.md`
- [ ] No leftover stub Prototypes (placeholder text not replaced with domain-specific content)

**If any of these is no, return to ARTIFACT-DRAFT to materialize the missing Prototype definitions per `04-SCHEMA-DESIGN.md` § "Materializing the `_Prototypes/` folder". Phase 7 is locked until this gate is clean.**

## Phase 3.6 — Convention 7 / 8 readiness (HARD STOP)

Conventions 7 (install-and-update pattern) and 8 (engine vs operator-content boundary) require concrete artifacts to be in place before shipping. Without them, operators have no documented path for installing or updating the OV, and no contract for what they can or cannot edit.

### Walk the artifact list

- [ ] **`INSTALL.md`** contains the Convention 7 install snippet (clone + push-disable) with the OV's actual GitHub URL filled in — not `<author>` or `<OV-Name>` placeholders
- [ ] **`INSTALL.md`** documents the `<OV-Name>-v<major>.<minor>` folder-naming convention with at least one concrete example
- [ ] **`INSTALL.md` § "Updating"** (or `OPERATOR-GUIDE.md § "Updates and troubleshooting"`) contains the canonical update workflow (fetch + ff-only pull + stash-pop fallback)
- [ ] **`OPERATOR-GUIDE.md` § "Engine vs your work"** explains the four content zones in plain operator-facing English (Convention 8)
- [ ] **`CONTRIBUTING.md` § "Content zones"** enumerates all four zones with at least one concrete path pattern per zone (Convention 8)
- [ ] **`.gitignore`** exists at the OV root with at least one Operator-Private Zone pattern; each pattern has an inline comment explaining what it excludes and why
- [ ] **`README.md` § "What is in this folder"** identifies the zones or links to `CONTRIBUTING.md § "Content zones"`
- [ ] **`UPDATE-PROMPT.md`** exists at the OV root, drawn from `_design-engine/_templates/TEMPLATE-UPDATE-PROMPT.md`. The OV's name is filled in concretely (no `<OV-Name>` placeholders); the prompt references the four-zone boundary; the prompt instructs the AI to stop and confirm before destructive commands.

### Run the gate

If `validate.py` is in use:

```bash
python3 _design-engine/_meta/validate.py
```

Checks 8 (C8 — zone-boundary documentation) and 9 (C9 — gitignore sanity) verify the artifacts.

If running markdown-only:

```bash
# Verify all four zone-name strings appear in CONTRIBUTING.md (or OPERATOR-GUIDE.md fallback)
grep -E 'Engine Zone|Operator-Private Zone|Operator-Extension Zone|Shipped Examples Zone' \
  CONTRIBUTING.md OPERATOR-GUIDE.md

# Verify .gitignore has substantive patterns
grep -v '^\s*$\|^#' .gitignore | wc -l   # expect > 0
```

### Acceptance — all must be true

- [ ] All four zone-name strings (`Engine Zone`, `Operator-Private Zone`, `Operator-Extension Zone`, `Shipped Examples Zone`) appear in either `CONTRIBUTING.md` or `OPERATOR-GUIDE.md` (operator-chosen synonyms are acceptable if documented in `_design-decisions.md`)
- [ ] `.gitignore` contains at least one non-comment, non-blank pattern matching the Operator-Private Zone
- [ ] `INSTALL.md`'s clone URL is concrete (no `<author>` / `<OV-Name>` placeholders)
- [ ] `OPERATOR-GUIDE.md`'s update workflow includes the stash-pop fallback for when fast-forward fails
- [ ] `UPDATE-PROMPT.md` exists at the OV root; the OV's name is filled in concretely (no `<OV-Name>` placeholders); the prompt block references the four-zone boundary and instructs the AI to stop before destructive commands

**If any of these is no, return to ARTIFACT-DRAFT to populate the install / operator / contributing / update-prompt docs. Phase 7 is locked until this gate is clean.**

## Phase 3.7 — Citation Audit (HARD STOP)

Every "p.XX / § X.Y / named theorist / verbatim quote" in shippable content traces back to an entry in `_source-inventory.md` (template at `_design-engine/_templates/TEMPLATE-source-inventory.md`) and verifies against the canonical source. This phase exists to prevent F13 (source-grounding skipped — fabricated cites that survive to ship). The historical motivation: the v1.0 build of Political Landscape Cartography shipped multiple fabricated cites that survived the pre-v2.0 SHIP-PREP gauntlet and only surfaced via operator spot-check. v2.0 makes the gate structural.

### Walk the cite list

- [ ] `_source-inventory.md` exists at the OV root with `ove_Source_Inventory_Status: read-acknowledged` (or `locked`)
- [ ] For every "p.XX" cite in shippable content, the citing source is in inventory AND the citation content matches the canonical page
- [ ] For every "§ X.Y" cite (or other structural identifier) in shippable content, the cited structural element exists in the canonical source
- [ ] For every named theorist / concept / framework cited, the citation is verifiable against the canonical source's text
- [ ] For every verbatim quote, the quote matches the canonical source word-for-word
- [ ] No structural-count claims ("the framework has N steps," "the dissertation lists M categories") that don't appear explicitly in the canonical source
- [ ] No `[SOURCE-VERIFICATION-REQUIRED]` placeholders remain in shippable content

### Run the gate

If `validate.py` is in use:

```bash
python3 _design-engine/_meta/validate.py
```

Check 11 (C11 — source-inventory presence and completeness) verifies the inventory file exists and every entry is fully filled in. Check 12 (C12 — citation audit log) requires a `_citation-audit-log.md` documenting verified cites with one entry per cite.

If running markdown-only:

```bash
# Extract all "p.NN" and "§ N.N" cites from shippable content
grep -rEhn 'p\.\s*[0-9]+|§\s*[0-9]+(\.[0-9]+)+' \
  <NewOV>/_*-engine <NewOV>/_Prototypes <NewOV>/README.md <NewOV>/OPERATOR-GUIDE.md
```

For each cite, manually verify against `_source-inventory.md` and the canonical source text. Log each verification in `_citation-audit-log.md` as `<cite> | <source> | <verification status>`.

### Acceptance — all must be true

- [ ] `_source-inventory.md` exists with `ove_Source_Inventory_Status: read-acknowledged` or `locked`
- [ ] Every cite in shippable content traces to a source in inventory
- [ ] Every cite's content verifies against the canonical source (operator-confirmed)
- [ ] `_citation-audit-log.md` records the verification of every cite
- [ ] No `[SOURCE-VERIFICATION-REQUIRED]` placeholders remain

**If any of these is no, return to ARTIFACT-DRAFT to resolve the unverified cites. Phase 7 is locked until this gate is clean.**

If this gate passes, flip `ove_Source_Inventory_Status` to `locked`.

## Phase 3.8 — Worked-Example Slot-ID Verification (HARD STOP)

If the OV ships a worked-example cartridge with references to specific Prototype slot IDs (e.g., "Sam → § 13.1.1.8 `incumbent_defender`" mapping a worked-example character to a canonical archetype), every such mapping carries an inline one-line source-justification. Without this, worked-example mappings drift toward session-inferred fabrications that survive to ship.

This phase exists to prevent F13 (source-grounding skipped) at its highest-stakes locus: the worked example, which the operator uses as the canonical "how to use this OV" demonstration. The v1.0 build of Political Landscape Cartography shipped four fabricated worked-sphere archetype assignments that survived the SHIP-PREP gauntlet — the motivating incident for this phase.

### Walk the worked-example mappings

- [ ] Every worked-example reference to a Prototype slot ID (e.g., `<name> → § X.Y.Z <slot-id>`) carries an inline one-line source-justification (why this mapping, against which source page or section)
- [ ] Every cited slot ID exists in the OV's canonical schema (cross-check against `_meta/SCHEMA-OF-SCHEMAS.md` or the worked-example's underlying source)
- [ ] No worked-example mapping is "best guess from name" / "by inference from similar archetype" / "based on session memory" — the source-justification must be verifiable
- [ ] If the worked example draws from a real underlying case (a real person, a real organization, a real event), the source-justification cites the underlying source verbatim or by canonical reference

### Acceptance — all must be true

- [ ] Every worked-example slot-ID assignment has an inline source-justification
- [ ] Every cited slot ID exists in the canonical schema or source
- [ ] No "by inference" / "by memory" / "best guess" assignments remain

**If any of these is no, return to ARTIFACT-DRAFT to verify or remove the unverified assignments. Phase 7 is locked until this gate is clean.**

## Phase 3.9 — Vocabulary Audit (HARD STOP)

The OV's shippable prose is swept for two failure-class words/phrases: **deliverable-promise nouns** that anchor reader expectations the OV doesn't actually ship, and **audience-register violations** (jargon, hedging, academic prose) that conflict with the Q14 declared register.

This phase exists because of two documented historical incidents in the v1.0 build of Political Landscape Cartography:

- "Dashboard" was used as a noun in two coaching documents — anchoring a deliverable expectation (the operator's client would ask "where's my dashboard?") that the OV did not actually ship. The fix was to replace "dashboard" with role-words ("conceptual frame," "mental map") that don't carry artifact-promise weight.
- The 4R coaching script drafted prose using "dissertation-defined set" — an academic register slip in a script declared for "Senior Managing Partner voice; no academic terms at business dinners."

### Walk the prose

**Deliverable-promise noun sweep.** Scan for nouns that imply a shipped artifact unless the OV actually ships one with that name:

| Noun | Replace with role-word unless OV ships | Examples of role-word replacement |
|------|-----------------------------------------|-----------------------------------|
| `dashboard` | a dashboard generator | frame / lens / mental map |
| `scorecard` | a structured rating output | rubric / audit list |
| `report` | a written-output template | summary / capture / log |
| `framework` (as deliverable noun) | a portable framework artifact | method / approach / discipline |
| `tool` (as delivered noun) | runnable software | practice / pattern / move |
| `playbook` | a packaged playbook | protocol / sequence |
| `template` (as marketed deliverable, not the design-time template) | shipped template files for end-users | scaffold / structure |

If the OV does ship one of these as a real artifact, the word is fine — just verify it's grounded in a real shipped file.

**Audience-register violation sweep.** Cross-reference shippable prose against the manifest's `ove_Audience_Prose_Register`:

- If `prose_register` is "Senior Managing Partner / business dinner voice" — scan for academic phrasings: "dissertation-defined," "as the literature suggests," "theoretical framework," "operationalized as," "construct of."
- If `prose_register` is "peer engineering" — scan for excessive formality, marketing-coded adjectives, consultant-speak.
- If `prose_register` is "warm coaching" — scan for cold-clinical phrasings, jargon, hedging.

### Run the gate

```bash
# Deliverable-promise noun sweep
grep -rEhin '\b(dashboard|scorecard|report|framework|tool|playbook)\b' \
  <NewOV>/_*-engine <NewOV>/_Prototypes <NewOV>/README.md <NewOV>/OPERATOR-GUIDE.md <NewOV>/CONTRIBUTING.md

# Inspect each hit. For each, log to _vocabulary-audit-log.md as:
#   <file:line> | <word> | <decision: kept-with-justification | replaced-with-<role-word>>
```

Validator check C13 (vocabulary audit log) requires `_vocabulary-audit-log.md` documenting each flagged word and its resolution.

### Acceptance — all must be true

- [ ] Every deliverable-promise noun in shippable content is either (a) a real artifact the OV ships, or (b) replaced with a role-word
- [ ] Every audience-register violation against `ove_Audience_Prose_Register` is either fixed or explicitly waived in `_design-decisions.md`
- [ ] `_vocabulary-audit-log.md` records the sweep + resolution

**If any of these is no, return to ARTIFACT-DRAFT or REVIEW to resolve. Phase 7 is locked until this gate is clean.**

## Phase 3.10 — Standalone Sufficiency readiness (HARD STOP)

**This phase is a hard ship gate. Convention 10 is enforced here.** No proceeding to Phase 4 until this returns clean. Like Phase 3 (personal-data scrub), this phase is non-advisory — if any sub-step fails, the OV does not ship until it's resolved.

The OV is being checked against the field-agnostic 47-requirement substrate at `_design-engine/_meta/standalone-sufficiency/`. The substrate's two master tests (Displacement, Absorption) are the criteria; Convention 10 in `_design-engine/_meta/CONVENTIONS.md` is the enforcement contract. The OV's `_meta/posture.yaml` was seeded at Q15 (SCHEMA-DESIGN) and the dispositions were filled during ARTIFACT-DRAFT — this phase verifies the result.

### Step 1 — Regenerate posture-derived artifacts

`standalone-sufficiency-posture.md` (operator-facing one-pager) and `_meta/vetting-rubric-filled.md` (0–3 scorecard) are derived from `_meta/posture.yaml`. Regenerate them from the current `posture.yaml`:

- If the OV ships a render script for posture artifacts, run it.
- If posture artifacts are hand-rolled, sweep both files against the current `posture.yaml` and update any stale dispositions / scores / verdict bands. Both files must reflect the current source of truth.

Verify:

- [ ] `standalone-sufficiency-posture.md` exists at the OV root
- [ ] `_meta/posture.yaml` exists at the OV root and is YAML-valid (`python3 -c "import yaml; yaml.safe_load(open('<OV>/_meta/posture.yaml'))"`)
- [ ] `_meta/vetting-rubric-filled.md` exists at the OV root
- [ ] Universal Core fields (Convention 1) present in each artifact's frontmatter

### Step 2 — Validate C14 against the OV root

Run the C14 check (Standalone Sufficiency Posture) in `_design-engine/_meta/validate.py`:

```bash
python3 _design-engine/_meta/validate.py --root <OV-root> --skip C1,C2,C3,C4,C5,C6,C7,C8,C9,C10,C11,C12,C13
```

(The skip list runs only C14; remove the skip flag once the OV is ready for the full sweep.)

- [ ] C14 exits 0 (pass) or 1 (warn-only). **Any C14 fail blocks ship.**

### Step 3 — Verify all 5 T0 hard gates = `met`

The five T0 gates are non-negotiable. None may ship as `partial` or `deferred` without an explicit `waiver_reason` field documenting why (and the waiver must be reviewable — "we'll get to it later" is not a waiver).

Open `_meta/posture.yaml` and confirm:

- [ ] `REQ-A1` (Capability Parity) — disposition `met` with evidence pointer
- [ ] `REQ-A2` (Graceful Scope Boundaries) — disposition `met` with evidence pointer
- [ ] `REQ-A3` (No Artificial Lobotomy) — disposition `met` with evidence pointer
- [ ] `REQ-B1` (Persistent User Model) — disposition `met` with evidence pointer (typically into chapter 06's state-persistence decisions)
- [ ] `REQ-H4` (Time-to-First-Value Activation) — disposition `met` with evidence pointer (the engineered first-win mechanism)

### Step 4 — Verify 8 TG conditional gates per declared `domain_stakes`

If `domain_stakes: high`, all 8 TG gates (REQ-I1 through REQ-I5; REQ-K1 through REQ-K3) must ship as `met`. If `domain_stakes: low`, the 8 gates may be `n-a` with no justification needed (low stakes don't justify TG ceremony).

- [ ] `domain_stakes` flag set in `posture.yaml` (`low` or `high`)
- [ ] If high: all 8 TG dispositions = `met` with evidence pointers
- [ ] If low: 8 TG dispositions = `n-a` (or `met` if the OV chose to clear them anyway)

### Step 5 — Verify ≥1 moat commitment with concrete schema-feature pointer

At least one of REQ-E4, REQ-M1, REQ-M2, REQ-M3, or REQ-M4 must be committed in `posture.yaml` under `moat_commitments`, with a non-empty `schema_feature` pointer naming the concrete schema feature that makes the moat real. A moat commitment without a schema pointer is a wish, not a moat.

- [ ] At least one entry in `moat_commitments` in `posture.yaml`
- [ ] Each commitment's `schema_feature` points to a real, named schema artifact (a Prototype, a state file structure, a methodology field)

### Step 6 — Confirm vetting-rubric verdict + gating veto

Open `_meta/vetting-rubric-filled.md` and confirm:

- [ ] Weighted score and percentage are populated (not `<N>` placeholders)
- [ ] Gating-rule veto status is named (`fires` / `does not fire`)
- [ ] Verdict band is one of: *Defensible specialist*, *Viable*, *At risk*
- [ ] If verdict is *At risk* with no T0/TG floor violation, return to ARTIFACT-DRAFT to close the gaps before shipping; *At risk* is a ship block unless the operator explicitly documents the choice in `_design-decisions.md` (rare; usually means the OV is a first iteration and the operator accepts a v0.x positioning)

### If any sub-step fails

Return to ARTIFACT-DRAFT to close the gap. **Phase 4 is locked until Phase 3.10 returns clean.**

> **Why this phase exists at the ship boundary.** Convention 10's claims are easy to leave at "we'll get to it" until the final ship moment. Phase 3.10 makes the posture work non-deferrable — the OV does not ship until the substitution-defense story is real, documented, and validator-checked. Without this phase as a hard gate, posture decay is the dominant failure mode (the operator commits at Q15, the dispositions get filled aspirationally during ARTIFACT-DRAFT, and the gap between aspiration and reality goes unflagged into release).

## Phase 4 — License + attribution

The default for the OV ecosystem is CC-BY 4.0 (matching SOLVE-eX, LifeLong-Learning, OVE itself). Reasonable open alternatives: MIT, Apache-2.0. For OVs where the Methodology Author wants restrictive licensing (proprietary methodology, sensitive substrate per Convention 9, monetized release), use the v2.0 restrictive template. Confirm the choice with the user.

Three paths:

### Path A — CC-BY 4.0 (default for the open OV ecosystem)

1. Copy `_design-engine/_templates/TEMPLATE-LICENSE-CCBY40.md` to the new OV's `LICENSE.md`
2. Update the attribution line with the user's actual name (operator-confirmed) and the GitHub URL (if applicable)
3. Ensure the attribution format appears in `README.md` under a "License" heading

### Path B — MIT or Apache-2.0

Use canonical text from [choosealicense.com](https://choosealicense.com). Fill in the user's actual name (operator-confirmed).

### Path C — Restrictive (proprietary methodology)

*Added v2.0. Modeled on the LICENSE that the v1.0 build of Political Landscape Cartography landed on after multiple rounds of refinement (self-coaching loophole closure, academic-archive carve-out, personal-evaluation 14-day window with 6 limits).*

1. Copy `_design-engine/_templates/TEMPLATE-LICENSE-restrictive.md` to the new OV's `LICENSE.md`
2. Fill in the Methodology Author's name (operator-confirmed) and the OV's name throughout
3. Fill in `<Jurisdiction>` (§ 8) and `<Contact Method>` (§ 9) with operator-confirmed values
4. If the OV cites sensitive source material per Convention 9 (`_meta/CONVENTIONS.md`), § 5 of the LICENSE applies as drafted
5. **Add to `CONTRIBUTING.md`:** "Before any public release, `LICENSE.md` must be reviewed by an IP attorney." The template includes this notice at the top; mirror it in CONTRIBUTING for operator visibility.
6. **Public-release decision is deferred until IP-attorney review.** The OV may ship to private GitHub during the interim per Phase 8 — the public-flip happens later via a single `gh repo edit --visibility public` after legal sign-off.

### Phase 4 acceptance

- [ ] LICENSE path chosen and documented in `_design-decisions.md`
- [ ] `LICENSE.md` populated from the selected template with no placeholders remaining
- [ ] If Path C: `CONTRIBUTING.md` flags IP-attorney review as ship-blocker for public release
- [ ] `README.md` § "License" includes the attribution format from the chosen LICENSE

## Phase 5 — Version + changelog

- [ ] `VERSION.md` shows `v1.0.0` with release date
- [ ] `CHANGELOG.md` has a v1.0.0 entry listing what shipped
- [ ] Schema policy is documented in `VERSION.md`

## Phase 6 — README polish

The README is the front door. Specifically check:

- [ ] One-sentence pitch in the opening paragraph
- [ ] Quick-start under 5 lines, on the first screen
- [ ] "What this is" and "What this is not" sections
- [ ] Folder structure table
- [ ] System requirements
- [ ] License section with attribution format
- [ ] No emojis (unless the user explicitly requested them)
- [ ] Reads aloud without flattery or filler

### Optional: run the validator's drift check

If `_design-engine/_meta/validate.py` is available, its C6 check catches divergence between `AI-BOOTSTRAP.md` and the engine's `00-START-HERE.md` — a quiet drift that degrades the AI's first-response quality:

```bash
python3 _design-engine/_meta/validate.py --root "<NewOV>" --skip C3,C4
```

`--skip C3,C4` focuses on the structural drift check at this phase. Markdown-only fallback: `_design-engine/_meta/VALIDATION-CHECKLIST.md` § C6.

## Phase 7 — Git init (optional but recommended)

**Precondition: Phase 3 (personal-data scrub) returned clean.** If you cannot show a clean validator run (exit code 0) or a fully-waived equivalent, do not proceed — a leaked name or path in the very first commit is permanent in the git history.

```bash
cd <NewOV>
git init -b main
git add .
git status   # verify .gitignore is doing its job
git commit -m "Initial release: <OV-name> v1.0.0"
```

## Phase 8 — GitHub push (optional)

If the user wants to publish:

```bash
gh repo create <user>/<OV-name> --public --description "<one-line>" --source=. --remote=origin --push
```

For CC-BY 4.0 OVs, public is the typical choice. Private is fine for personal-use OVs not intended for sharing.

## Phase 9 — Post-ship close-out

In the OVE cartridge for this design engagement:

- [ ] Update `_design-state.md` to mark phase as "shipped"
- [ ] Append final entry to `_design-decisions.md` noting ship date and version
- [ ] Write the final session log capturing what shipped
- [ ] Open Thread for next session: typically "audit after 30 days of use" or "v1.1 backlog"

## What "done" looks like

The user can now:

1. Point any capable AI at the new folder
2. Say *"Read `AI-BOOTSTRAP.md` and help me with [domain]"*
3. Get a productive first session

If that doesn't work in a clean AI session against the new folder, ship is not done — return to debug.

## Recommended post-ship verification

In a **fresh AI session** (not the design session), point the AI at the new OV folder and ask it to do the things the OV is designed to do. Confirm:

- The AI produces a proper readiness statement (Phase 0 pre-flight pattern)
- The AI doesn't dump a multi-bullet questionnaire
- The AI proposes appropriate session activities
- The AI writes session logs and state files when it should

If any of these fail, the OV needs work. Don't claim ship done.
