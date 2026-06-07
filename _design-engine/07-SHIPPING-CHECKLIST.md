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

## Phase 4 — License + attribution

The default for the OV ecosystem is CC-BY 4.0 (matching SOLVE-eX and LifeLong-Learning). Other reasonable options: MIT, Apache-2.0. Confirm with the user.

For CC-BY 4.0:

1. Copy `_design-engine/_templates/TEMPLATE-LICENSE-CCBY40.md` to the new OV's `LICENSE.md`
2. Update the attribution line with the user's actual name (operator-confirmed) and the GitHub URL (if applicable)
3. Ensure the attribution format appears in `README.md` under a "License" heading

For MIT or Apache: use canonical text from [choosealicense.com](https://choosealicense.com).

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
