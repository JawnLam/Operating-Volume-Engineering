---
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

## Phase 3 — Personal-data scrub

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

Run a grep:

```bash
grep -rEn "\bERA\b|Wingspire|Exit Ready|<specific-personal-terms>" "<NewOV>"
```

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

## Phase 7 — Git init (optional but recommended)

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
