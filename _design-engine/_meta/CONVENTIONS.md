---
Item_Prototype: Fleeting
Item_ID: ove-meta-conventions
Title: "OVE Meta — Universal Conventions for OV-Designed Output"
Date_Added: 2026-06-06
Date_Modified: 2026-06-06
Needs_Processing: false
type: design-engine-meta
role: conventions
scope: subject-agnostic
updated: 2026-06-06
---

# OVE Meta — Universal Conventions for OV-Designed Output

> **An OV designed via OVE produces files that conform to a small set of universal conventions out of the box. The operator should not need to post-process the output to make it vault-compatible. This file is the canonical statement of those conventions. Reference from `04-SCHEMA-DESIGN.md`, `05-WRITING-FOR-AI.md`, and `BOOTSTRAP-NEW-OV.md`.**

## Why these conventions exist

A new OV designed by OVE produces files that live alongside the operator's other notes — in an Obsidian vault, a folder of markdown, a Hugo content directory, etc. If the new OV's files don't conform to the operator's existing conventions (frontmatter shape, property naming, prototype declarations), the operator does cleanup work after every design engagement. The operator hired OVE to *avoid* that work, not generate it.

These conventions are not platform-specific. They work in any tool that reads YAML frontmatter. They are minimum-friction defaults; an operator who has different conventions can override them per-OV in the schema design.

## Convention 1 — Universal Core fields on every shipped note

Every `.md` file that ships in an OV designed via OVE declares these six fields in YAML frontmatter:

```yaml
---
Item_Prototype: <Prototype_Name>      # See Convention 4
Item_ID: <slug-or-uuid>
Title: "<Human-readable title>"
Date_Added: YYYY-MM-DD
Date_Modified: YYYY-MM-DD
Needs_Processing: false
---
```

OV-specific properties live below these. `Item_Prototype` is the discriminator that tells humans, queries, and automation which schema the note follows.

## Convention 2 — Case conventions for property names

Five rules govern frontmatter property naming. They apply universally to every OV designed via OVE.

| Position | Convention | Example |
|----------|------------|---------|
| **Core keys** (`Item_ID`, `Title`, `Date_Added`, etc.) | `Title_Snake_Case` | `Publication_Date`, `Item_ID` |
| **Domain prefix** (the namespace) | `lowercase_snake_case` | `lll_`, `lfw_`, `ove_`, `cook_` |
| **Domain-prefixed property body** (after the prefix) | `Title_Snake_Case` | `lll_Status`, `lfw_Item_Type`, `ove_OV_Name` |
| **Acronyms in either position** | Fully capitalized | `URL`, `ISBN`, `POV`, `OV` |
| **Enum identifiers** (under `enums:` in schema) | `lowercase_snake_case` (typically plural) | `lll_statuses`, `lfw_item_types`, `ove_design_phases` |

These rules ensure cross-namespace consistency. They are also documented at the top of any published `Master_Schema.yaml` (case rules 1–5).

## Convention 3 — One namespace per OV

Every OV chooses a short lowercase namespace prefix at design time (e.g., `cook_` for a cooking OV, `negotiation_` for a negotiation-prep OV). All OV-specific frontmatter properties carry that prefix.

Per Convention 2, the prefix is `lowercase_snake_case` and the body after the prefix is `Title_Snake_Case`. The namespace + Title_Snake_Case body pattern is what makes a property name belong to a particular OV.

## Convention 4 — Every Prototype gets its own `Item_Prototype` value

Every Prototype in the OV is declared with an `Item_Prototype` value, named `<NAMESPACE_UPPER>_<TypeName>`. Every Item in a cartridge carries the value of the Prototype it conforms to. Examples from existing OVs:

| OV | Prototype names |
|----|-----------------|
| LLL | `LLL_Unit`, `LLL_Subject_Manifest`, `LLL_Session`, … |
| LFW | `LFW_Character_Bible`, `LFW_Motif`, `LFW_Scene`, … |
| OVE | `OVE_OV_Manifest`, `OVE_Design_State`, `OVE_Session`, … |

For non-Item files (front-door docs, engine prose, meta), use `Item_Prototype: Fleeting`. This is the universal "this is a note but not an instance of any OV-specific Prototype" value.

## Convention 5 — Schema-of-namespace declaration

The new OV's `_<purpose>-engine/_meta/SCHEMA-OF-SCHEMAS.md` declares its namespace, Prototypes, enum identifiers, and properties in YAML — ready to be lifted into a `Master_Schema.yaml` if the operator maintains one. Even if no `Master_Schema.yaml` exists, the per-OV schema declaration is the canonical source for that OV's structural rules.

## Convention 6 — Each OV ships its own `_Prototypes/` folder

Every OV bundles a top-level `_Prototypes/` folder containing one `.md` file per Prototype in its namespace. Each file is a self-contained declaration of that Prototype: its frontmatter shape, required body sections, and an example. The structure of each file follows `_design-engine/_templates/TEMPLATE-Prototype.md`.

**This folder is the canonical home for the OV's Prototype definitions.** A reader who clones the OV without any surrounding infrastructure can open `_Prototypes/<NAMESPACE>_<TypeName>.md` and learn what an Item of that Prototype is supposed to look like, what frontmatter fields it carries, and what its body should contain.

**Why this matters.** Without Convention 6, an OV's Prototypes live only by reference. A cartridge note declares `Item_Prototype: COOK_Recipe` — that's a name pointer. If the reader has no `COOK_Recipe.md` definition available, the name is meaningless. Operators with a vault-wide central registry (e.g., a Master_Schema and an `_Infrastructure/_Prototypes/` folder) get the definition from the central registry, but operators without such infrastructure are stranded. Convention 6 makes the OV portable: the Prototype definitions travel with it.

**The vault-wide central registry, if any, is a downstream union view.** Operators who run multiple OVs may choose to maintain a central registry that aggregates Prototypes across all of their OVs (the user's `_Infrastructure For All Vaults/_Prototypes/` is one example). That central registry is convenience, not authority — the canonical home of each Prototype is still the OV's local `_Prototypes/` folder. If the two disagree, the OV's local folder wins.

**Concretely:**

- `_Prototypes/COOK_Recipe.md`
- `_Prototypes/COOK_Technique.md`
- `_Prototypes/COOK_Ingredient.md`
- *(one file per Prototype declared in the OV's namespace)*

Non-Item file types (Fleeting, the universal "this is a note but not a recurring Prototype") do not need to be redeclared in the OV's `_Prototypes/` folder — Fleeting is a vault-universal Prototype with no OV-specific behavior.

**Materialization happens during ARTIFACT-DRAFT.** As the AI walks `04-SCHEMA-DESIGN.md` and locks the OV's Prototype list (Q4, Q9, Q12), it materializes one `_Prototypes/<NAMESPACE>_<TypeName>.md` file per Prototype, conforming to `TEMPLATE-Prototype.md`. The shipping checklist gates whether all declared Prototypes have a corresponding file in `_Prototypes/` before the OV ships (`07-SHIPPING-CHECKLIST.md` Phase 3.5).

**Validator coverage.** The optional `validate.py` includes a check (C7 — Prototype coverage) that scans every cartridge for `Item_Prototype:` values and confirms each has a matching `<NAMESPACE>_<TypeName>.md` in either the OV root's `_Prototypes/` or, if present, an enclosing cartridge's `_Prototypes/`. Missing files fail with a precise file:line pointer.

## Convention 7 — Install-and-update pattern

Every OV ships an install pattern that produces a git-trackable working copy on the operator's machine. The pattern enables `git pull` updates while protecting against accidental publishing of operator-private work.

**Default install (copy-pasteable; appears verbatim in every OV's `INSTALL.md`):**

```bash
# 1. Clone into a folder named with the OV's current major.minor version
git clone https://github.com/<author>/<OV-Name>.git \
  ~/path/to/<OV-Name>-v<major>.<minor>

# 2. Disable push remote (protects against accidental upload of personal content)
cd ~/path/to/<OV-Name>-v<major>.<minor>
git remote set-url --push origin DISABLED_TO_PREVENT_ACCIDENTAL_PUSH_OF_PERSONAL_WORK

# 3. Verify
git remote -v
# Should show: fetch = real URL; push = DISABLED_TO_PREVENT_ACCIDENTAL_PUSH_OF_PERSONAL_WORK
```

**Update workflow (every OV documents this in `OPERATOR-GUIDE.md` § Updates):**

```bash
cd ~/path/to/<OV-Name>-v<major>.<minor>

git fetch origin
git log --oneline HEAD..origin/main          # preview what's incoming

# If you have no local engine modifications: clean fast-forward
git pull --ff-only origin main

# If you have local engine modifications: stash → pull → pop
git stash push --include-untracked -m "pre-update local state"
git pull --ff-only origin main
git stash pop                                 # resolve any conflicts
```

**Major.minor folder transitions.** When the OV ships a new major.minor (e.g., v1.7 → v1.8), rename the folder to match. The OV's CHANGELOG.md announces these transitions explicitly.

```bash
cd ~/path/to/
mv <OV-Name>-v<old-major-minor> <OV-Name>-v<new-major-minor>
```

**Contributing back upstream.** If you intend to contribute back to the OV (PR your fork to upstream), re-enable push to your own fork — not to upstream:

```bash
# Replace with your own fork's URL
git remote set-url --push origin https://github.com/<your-username>/<OV-Name>.git
```

**Required artifacts in every OV designed via OVE:**

- `INSTALL.md` contains the install snippet (copy-pasteable; concrete URL filled in).
- `OPERATOR-GUIDE.md` contains the update-workflow snippet plus troubleshooting for common scenarios (stash-pop conflicts, fast-forward failures, major.minor folder transitions).
- `README.md` § "Install" links to `INSTALL.md`.
- `UPDATE-PROMPT.md` at the OV root — a copy-pasteable AI prompt that asks an AI assistant to walk the operator through the update by reading `INSTALL.md § Updating` and `OPERATOR-GUIDE.md § Updates and troubleshooting`. Drawn from `_design-engine/_templates/TEMPLATE-UPDATE-PROMPT.md`. Must reference the OV's name concretely (no `<OV-Name>` placeholders), reference the four-zone boundary, and instruct the AI to stop and confirm before any destructive command. *Added v1.2.1.*
- Folder naming convention (`<OV-Name>-v<major>.<minor>`) is stated in `INSTALL.md` and `OPERATOR-GUIDE.md`.

**Why this pattern.** Operators of OVs almost always do private work inside the OV folder (manuscripts in LFW, subjects in LLL, design cartridges in OVE, case files in SOLVE-eX). The push-disabled default prevents the worst-case operator-error (`git push` upstreaming personal work) while still allowing `git pull` to deliver engine updates. The major.minor folder suffix lets operators run multiple parallel versions of the same OV side-by-side during a transition.

**Two update paths.** Convention 7 supports two equivalent paths for updates:

- **Manual path** — operator reads `INSTALL.md § Updating` and `OPERATOR-GUIDE.md § Updates and troubleshooting`, runs the git commands themselves. Recommended for major-version transitions and any release with a non-trivial migration recipe.
- **AI-assisted path** — operator opens `UPDATE-PROMPT.md`, copies the prompt block, pastes to an AI session, and approves each step. Recommended for routine releases (patches and small minors).

Both paths consult the same canonical docs; `UPDATE-PROMPT.md` is the operator's hands-off delegation to an AI, not a second update protocol.

## Convention 8 — Engine vs operator-content boundary

Every OV explicitly declares four content zones. The boundary lets `git pull` update the engine without disturbing operator work and lets the operator extend the OV without fearing the next pull.

### The four zones

**1. Engine Zone** *(release-owned; updated by `git pull`)*

The files that the OV's release ships. Updates from `git pull` are non-destructive to operator content because the engine zone doesn't overlap with the operator's working data.

- Front-door docs: `README.md`, `INSTALL.md`, `OPERATOR-GUIDE.md`, `CONTRIBUTING.md`, `LICENSE.md`, `VERSION.md`, `CHANGELOG.md`, optional `MIGRATION-NOTES.md`
- The OV's engine folder: `_<purpose>-engine/` (e.g., `_writing-engine/`, `_teaching-engine/`, `_design-engine/`)
- `_Prototypes/` (Convention 6)
- `_USER.md.template` (the template, not a populated `_USER.md`)
- `.gitignore` (engine-zone file; its *patterns* define the Operator-Private Zone)

Operators **do not edit Engine-Zone files directly.** If customization is desired, use the Operator-Extension Zone or any override mechanism the engine provides (e.g., LFW's per-cartridge style sheet, LLL's per-subject schema).

**2. Operator-Private Zone** *(gitignored; never tracked)*

Path patterns that the `.gitignore` excludes from tracking. These files exist in the operator's working copy but are not visible to `git pull` and never get pushed.

- `_USER.md` (operator profile — never auto-inferred per P7 / F3)
- Per-OV operator-private artifacts (LFW's `_craft-profile.md`, `_craft-log.md`, `_voice-samples.md`; LLL's per-subject SR logs if private; SOLVE-eX's private case files; OVE's design cartridges in progress)
- Operator's own working state (`_USER.md`, `.obsidian/`, IDE caches)

The `.gitignore` patterns are documented in `CONTRIBUTING.md` with rationale per pattern.

**3. Operator-Extension Zone** *(operator-created; survives `git pull`)*

New folders/files outside the Engine and Shipped-Examples zones. The OV is *designed* to be extended here. `git pull` does not affect these paths because they are untracked or fall outside the engine's path patterns.

Typical examples:
- LFW: the operator's own manuscript cartridges (parallel to `Example-Project-The-Late-Frost/`)
- LLL: the operator's own subject cartridges (parallel to `Example-Subject-Roman-Empire/`)
- OVE: the operator's own design cartridges (parallel to the worked-example cartridges)
- SOLVE-eX: the operator's own case files (parallel to shipped examples)

The CONTRIBUTING.md enumerates which top-level paths are Extension Zones (i.e., what kinds of folders the operator may freely add at the OV root).

**4. Shipped Examples Zone** *(release-owned; updated by `git pull`)*

The worked-example cartridges that demonstrate the OV. Tracked by git, updated by pulls, treated as reference implementations.

- LFW: `Example-Project-The-Late-Frost/`, `Example-Project-The-Persistence-Question/`
- LLL: `Example-Subject-Roman-Empire/`
- OVE: the 5 worked-example cartridges (`Long-Form-Writing/`, `LifeLong-Learning-Retrospective/`, `Negotiation-Preparation/`, `Relationship-Cultivation/`, `SOLVE-eX-Retrospective/`)
- SOLVE-eX: shipped sample sessions, tool entries, etc.

Operators **do not edit Shipped-Examples directly.** If customization is desired, copy the example into an Operator-Extension Zone cartridge and customize there.

### Required artifacts in every OV designed via OVE

- **`README.md` § "What is in this folder"** identifies the four zones explicitly (or links to `CONTRIBUTING.md`'s declaration).
- **`CONTRIBUTING.md` § "Content zones"** enumerates path patterns for each of the four zones with at least one concrete example per zone.
- **`.gitignore`** contains the Operator-Private Zone path patterns; each pattern has a comment explaining what it excludes and why.
- **`OPERATOR-GUIDE.md` § "Engine vs your work"** explains the boundary to operators in plain English (one screen of prose, not a wall of policy).

### Validator coverage (C8 — zone-boundary documentation)

The optional `validate.py` scans `CONTRIBUTING.md` (with `OPERATOR-GUIDE.md` as fallback) for the four canonical zone-name strings:

- `Engine Zone`
- `Operator-Private Zone`
- `Operator-Extension Zone`
- `Shipped Examples Zone`

(Or operator-chosen synonyms documented in `_design-decisions.md` for the OV.) **C8 outcomes:**

- All four declared → pass
- Some declared → warn with the missing names listed
- None declared → fail

### Validator coverage (C9 — gitignore sanity)

`.gitignore` must exist at the OV root and contain at least one Operator-Private Zone path pattern. **C9 outcomes:**

- `.gitignore` missing → fail
- `.gitignore` empty or comment-only → warn
- `.gitignore` contains at least one pattern → pass

### Why the four zones

Without explicit zoning, the operator and the engine compete for the same paths. The operator hand-edits a `00-START-HERE.md` to taste; the next `git pull` produces a conflict. The operator adds private work to an example cartridge; the next pull silently rewrites part of it. The four zones prevent both failure modes by making the contract legible: engine moves; operator moves; nobody steps on each other.

## Convention 9 — Sensitive source materials (ship-by-reference)

*Added v2.0.* Some OVs cite source material that is sensitive — typically the Methodology Author's personal academic work (a dissertation, in-progress research), an internal client report used as basis, or any source the operator does not want bundled into the public OV release. Convention 9 codifies the pattern OVs use to **cite sensitive material as substrate while excluding the source file itself from the shipped artifact**.

### When Convention 9 applies

Apply Convention 9 to any source listed in `_source-inventory.md` (Convention 9 depends on the source-inventory pattern documented in `BOOTSTRAP-NEW-OV.md` CQ3) with `Sensitivity: Ship-by-reference (Convention 9)`. Examples:

- A Methodology Author's personal academic dissertation referenced as substrate but not redistributed
- An internal client report whose ideas inform the OV's structure but whose contents are confidential
- In-progress academic work the author is not yet ready to release publicly
- Proprietary methodology documents licensed for the author's use but not for republication

### The ship-by-reference pattern

For every Convention 9 source, the OV ships **the inventory listing and a placeholder**, not the source itself. Concretely:

1. **`_source-inventory.md`** lists the sensitive source with `Sensitivity: Ship-by-reference (Convention 9)`. This makes the source visible to readers as known substrate.
2. **`.gitignore`** excludes the physical source file at its canonical path. Example pattern:
   ```
   # Sensitive substrate — Convention 9 (sensitive source materials)
   # Source file stays local in operator's working copy; never tracked.
   _frameworks/sources/<source-slug>.pdf
   _frameworks/sources/<another-source-slug>.docx
   ```
3. **A placeholder `.md` file** at the canonical location (e.g., `_frameworks/sources/<source-slug>.md`) directs readers to contact the Methodology Author for source access. Drawn from `_design-engine/_templates/TEMPLATE-sensitive-source-placeholder.md`. This file IS tracked (it ships as the public artifact that points at the private substrate).
4. **`LICENSE.md`** — if the OV uses a restrictive license (drawn from `_design-engine/_templates/TEMPLATE-LICENSE-restrictive.md`), the restrictive template includes language acknowledging the sacred-source distinction and the academic-archive carve-out for cited work.

### Required artifacts per OV (Convention 9 sources only)

- `_source-inventory.md` entry with `Sensitivity: Ship-by-reference (Convention 9)`
- `.gitignore` block excluding each sensitive source file at its canonical path, with inline comment naming Convention 9
- Placeholder `.md` file at the canonical location of each sensitive source, drawn from `TEMPLATE-sensitive-source-placeholder.md` with the source slug + Methodology Author contact filled in
- If the OV ships restrictive LICENSE, language acknowledging the sacred-source distinction (the restrictive template includes this by default)

### Defense-in-depth

The pattern is **belt-and-suspenders** on purpose:

- Physical exclusion: the source file is held back from the staging tree before `git init` runs
- `.gitignore` exclusion: even if the file is later re-added, the gitignore prevents tracking
- Post-push verification: after `git push`, fetch the canonical source's expected path via `gh api repos/<user>/<repo>/contents/<path>` — a 404 confirms the source is not on the remote

Both physical exclusion and gitignore are required because either alone is brittle: physical-only fails if the operator copies the file in later; gitignore-only fails if `.gitignore` is misconfigured or removed.

### Why this matters

The v1.0 build of Political Landscape Cartography needed to ship public-facing methodology while keeping its Methodology Author's 294-page dissertation private. The pattern (physical exclusion + gitignore + placeholder + post-push 404 verification) was invented during that build's SHIP-PREP phase. v2.0 formalizes the pattern as a numbered Convention so future OVs that cite sensitive source material can apply it out of the box rather than inventing it on the fly. The convention also documents the academic-archive friction (operators legitimately archiving cited work for published scholarly research need a carve-out from delete-or-destroy obligations in restrictive LICENSEs) and the self-coaching loophole (a principal coaching themselves is NOT personal evaluation under a restrictive license).

## How to apply during a new-OV design

The AI walking `BOOTSTRAP-NEW-OV.md` asks the operator one question early:

> *"What namespace prefix will this OV use? (Three to six lowercase letters ending in underscore. Example: `cook_` for a cooking OV.)"*

From that single answer, everything else follows:

- Prototype names: `COOK_<TypeName>`
- Property names: `cook_<Title_Snake_Case_Body>`
- Enum identifiers under `enums:`: `cook_<lowercase_plural>`
- `Item_Prototype` values on each Item: `COOK_<TypeName>`
- `Item_Prototype: Fleeting` on non-Item files
- `_Prototypes/` folder at the OV root with one `COOK_<TypeName>.md` per Prototype, each following `_design-engine/_templates/TEMPLATE-Prototype.md`
- `INSTALL.md` with the canonical install snippet (Convention 7) wired to the OV's actual GitHub URL
- `OPERATOR-GUIDE.md` § "Updates" with the canonical update-workflow snippet (Convention 7)
- `UPDATE-PROMPT.md` at the OV root drawn from `_design-engine/_templates/TEMPLATE-UPDATE-PROMPT.md` with the OV's name filled in (Convention 7)
- `CONTRIBUTING.md` § "Content zones" enumerating the four zones with concrete path patterns (Convention 8)
- `.gitignore` containing the Operator-Private Zone patterns documented in CONTRIBUTING (Convention 8)
- `README.md` § "What is in this folder" linking to the zone declaration

When drafting templates, Prototype declarations, install instructions, and example Items, the AI applies these conventions throughout. The operator does not post-process the output.

## When the operator wants different conventions

If the operator has different conventions (e.g., they prefer all-lowercase property bodies for backwards-compatibility with a legacy schema), they say so during INTERVIEW or SCHEMA-DESIGN. The AI then applies the operator's conventions instead — but documents the choice in `_design-decisions.md` so future sessions know which conventions apply.

**The default is the conventions above. Override only on explicit operator request.**

## Verifying the output

After ARTIFACT-DRAFT and during REVIEW, the AI checks every drafted file for:

- [ ] Six Universal Core fields present and non-empty (Convention 1)
- [ ] Property bodies in Title_Snake_Case (Convention 2)
- [ ] Acronyms fully capitalized (Convention 2)
- [ ] Namespace prefix consistent across all properties (Conventions 2, 3)
- [ ] `Item_Prototype` value matches a Prototype defined in the OV's `_meta/SCHEMA-OF-SCHEMAS.md` (Convention 4)
- [ ] Non-Item files declare `Item_Prototype: Fleeting` (Convention 4)
- [ ] Schema declaration exists at `_<purpose>-engine/_meta/SCHEMA-OF-SCHEMAS.md` (Convention 5)
- [ ] `_Prototypes/` folder exists at the OV root with one `<NAMESPACE>_<TypeName>.md` per Prototype declared in the OV's namespace (Convention 6)
- [ ] Each `_Prototypes/<NAMESPACE>_<TypeName>.md` conforms to `TEMPLATE-Prototype.md` and matches the Prototype's `_meta/SCHEMA-OF-SCHEMAS.md` declaration (Convention 6)
- [ ] `INSTALL.md` contains the install snippet with the OV's actual GitHub URL filled in (Convention 7)
- [ ] `OPERATOR-GUIDE.md` § "Updates" contains the update-workflow snippet (Convention 7)
- [ ] `UPDATE-PROMPT.md` exists at the OV root with the OV's name filled in (no `<OV-Name>` placeholders), references the four-zone boundary, and instructs the AI to confirm before destructive commands (Convention 7)
- [ ] Folder-naming convention (`<OV-Name>-v<major>.<minor>`) is documented in INSTALL.md (Convention 7)
- [ ] `CONTRIBUTING.md` § "Content zones" declares all four zones with at least one concrete example per zone (Convention 8)
- [ ] `.gitignore` exists and contains the Operator-Private Zone patterns documented in CONTRIBUTING (Convention 8)
- [ ] `README.md` § "What is in this folder" identifies the zones or links to the CONTRIBUTING declaration (Convention 8)

These checks are also covered by the optional `validate.py` (`C1` backbone presence, `C2` frontmatter presence, `C3` placeholder leakage — the wider scrub, `C7` Prototype coverage, `C8` zone-boundary documentation, `C9` gitignore sanity, `C10` UPDATE-PROMPT sanity) and by walking `VALIDATION-CHECKLIST.md` for markdown-only environments.

## Related references

- `_design-engine/04-SCHEMA-DESIGN.md` § "Convention compliance" — points back to this file when designing the new OV's schema
- `_design-engine/05-WRITING-FOR-AI.md` § "Property-naming conventions" — points back to this file when drafting any property-bearing prose
- `_design-engine/BOOTSTRAP-NEW-OV.md` — the namespace CQ that triggers the convention cascade; the Convention 7/8 artifact list per new OV
- `_design-engine/07-SHIPPING-CHECKLIST.md` § "Phase 3.6 — Convention 7/8 readiness" — gates ship until INSTALL/OPERATOR-GUIDE/CONTRIBUTING/.gitignore are all in place
