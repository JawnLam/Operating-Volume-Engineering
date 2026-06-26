---
type: Fleeting
timestamp: "2026-06-06T00:00:00Z"
Item_ID: ove-meta-conventions
title: "OVE Meta — Universal Conventions for OV-Designed Output"
Date_Added: 2026-06-06
Date_Modified: 2026-06-06
Needs_Processing: false
doc_type: design-engine-meta
role: conventions
scope: subject-agnostic
updated: 2026-06-06
---

# OVE Meta — Universal Conventions for OV-Designed Output

> **An OV designed via OVE produces files that conform to a small set of universal conventions out of the box. The operator should not need to post-process the output to make it vault-compatible. This file is the canonical statement of those conventions. Reference from `04-SCHEMA-DESIGN.md`, `05-WRITING-FOR-AI.md`, and `BOOTSTRAP-NEW-OV.md`.**

## Why these conventions exist

A new OV designed by OVE produces files that live alongside the operator's other notes — in an Obsidian vault, a folder of markdown, a Hugo content directory, etc. If the new OV's files don't conform to the operator's existing conventions (frontmatter shape, property naming, prototype declarations), the operator does cleanup work after every design engagement. The operator hired OVE to *avoid* that work, not generate it.

These conventions are not platform-specific. They work in any tool that reads YAML frontmatter. They are minimum-friction defaults; an operator who has different conventions can override them per-OV in the schema design.

## Convention 1 — Universal Core fields on every shipped note (OKF v0.1 conformant)

Every `.md` file that ships in an OV designed via OVE declares these Universal Core fields in YAML frontmatter. **As of v2.4.0 the core is Google OKF v0.1 conformant** — the discriminator is lowercase `type` (OKF's single required field), and `title`/`timestamp`/`tags` use OKF's lowercase names:

```yaml
---
type: <Prototype_Name>        # OKF REQUIRED discriminator (renamed from Item_Prototype); see Convention 4
Item_ID: <slug-or-uuid>
title: "<Human-readable title>"      # OKF (renamed from Title)
timestamp: <ISO 8601 datetime>       # OKF — e.g. 2026-06-26T00:00:00Z
Date_Added: YYYY-MM-DD
Date_Modified: YYYY-MM-DD             # kept; time-synced with timestamp, each in its own format
Needs_Processing: false
# Optional OKF fields when applicable: description (one sentence), resource (canonical asset URI), tags
---
```

OV-specific properties live below these. **`type`** is the discriminator that tells humans, queries, and automation which schema the note follows — and it is OKF's required field, so every shipped OV note is OKF-conformant by construction. A note without `type` is malformed.

> **Renamed in v2.4.0 for OKF v0.1 conformance** (mirrors vault Master_Schema v1.23.0): `Item_Prototype`→`type`, `Title`→`title`, `Tags`→`tags`; added `timestamp` (derived from `Date_Modified`), and optional `description`/`resource`. `Date_Modified` is kept and stays time-synced with `timestamp`. This is the change that makes every OV designed via OVE emit OKF-compliant items by default. The lowercase OKF field names are a deliberate exception to Convention 2's Title_Snake_Case rule for core keys.

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

> **OKF interop exception (v2.4.0).** The six Google OKF v0.1 interop fields — `type`, `title`, `timestamp`, `tags`, `description`, `resource` — are a deliberate **lowercase** exception to the Core-keys `Title_Snake_Case` rule. OKF mandates lowercase field names; matching them is what makes every OV note conformant with the Open Knowledge Format. All other core keys (`Item_ID`, `Date_Added`, `Date_Modified`, `Needs_Processing`, …) keep `Title_Snake_Case`.

## Convention 3 — One namespace per OV

Every OV chooses a short lowercase namespace prefix at design time (e.g., `cook_` for a cooking OV, `negotiation_` for a negotiation-prep OV). All OV-specific frontmatter properties carry that prefix.

Per Convention 2, the prefix is `lowercase_snake_case` and the body after the prefix is `Title_Snake_Case`. The namespace + Title_Snake_Case body pattern is what makes a property name belong to a particular OV.

## Convention 4 — Every Prototype gets its own `type` value

Every Prototype in the OV is declared with a `type` value, named `<NAMESPACE_UPPER>_<TypeName>`. Every Item in a cartridge carries the value of the Prototype it conforms to. Examples from existing OVs:

| OV | Prototype names |
|----|-----------------|
| LLL | `LLL_Unit`, `LLL_Subject_Manifest`, `LLL_Session`, … |
| LFW | `LFW_Character_Bible`, `LFW_Motif`, `LFW_Scene`, … |
| OVE | `OVE_OV_Manifest`, `OVE_Design_State`, `OVE_Session`, … |

For non-Item files (front-door docs, engine prose, meta), use `type: Fleeting`. This is the universal "this is a note but not an instance of any OV-specific Prototype" value.

## Convention 5 — Schema-of-namespace declaration

The new OV's `_<purpose>-engine/_meta/SCHEMA-OF-SCHEMAS.md` declares its namespace, Prototypes, enum identifiers, and properties in YAML — ready to be lifted into a `Master_Schema.yaml` if the operator maintains one. Even if no `Master_Schema.yaml` exists, the per-OV schema declaration is the canonical source for that OV's structural rules.

## Convention 6 — Each OV ships its own `_types/` folder

Every OV bundles a top-level `_types/` folder containing one `.md` file per Prototype in its namespace. Each file is a self-contained declaration of that Prototype: its frontmatter shape, required body sections, and an example. The structure of each file follows `_design-engine/_templates/TEMPLATE-Prototype.md`.

**This folder is the canonical home for the OV's Prototype definitions.** A reader who clones the OV without any surrounding infrastructure can open `_types/<NAMESPACE>_<TypeName>.md` and learn what an Item of that Prototype is supposed to look like, what frontmatter fields it carries, and what its body should contain.

**Why this matters.** Without Convention 6, an OV's Prototypes live only by reference. A cartridge note declares `type: COOK_Recipe` — that's a name pointer. If the reader has no `COOK_Recipe.md` definition available, the name is meaningless. Operators with a vault-wide central registry (e.g., a Master_Schema and an `_Infrastructure/_types/` folder) get the definition from the central registry, but operators without such infrastructure are stranded. Convention 6 makes the OV portable: the Prototype definitions travel with it.

**The vault-wide central registry, if any, is a downstream union view.** Operators who run multiple OVs may choose to maintain a central registry that aggregates Prototypes across all of their OVs (the user's `_Infrastructure For All Vaults/_types/` is one example). That central registry is convenience, not authority — the canonical home of each Prototype is still the OV's local `_types/` folder. If the two disagree, the OV's local folder wins.

**Concretely:**

- `_types/COOK_Recipe.md`
- `_types/COOK_Technique.md`
- `_types/COOK_Ingredient.md`
- *(one file per Prototype declared in the OV's namespace)*

Non-Item file types (Fleeting, the universal "this is a note but not a recurring Prototype") do not need to be redeclared in the OV's `_types/` folder — Fleeting is a vault-universal Prototype with no OV-specific behavior.

**Materialization happens during ARTIFACT-DRAFT.** As the AI walks `04-SCHEMA-DESIGN.md` and locks the OV's Prototype list (Q4, Q9, Q12), it materializes one `_types/<NAMESPACE>_<TypeName>.md` file per Prototype, conforming to `TEMPLATE-Prototype.md`. The shipping checklist gates whether all declared Prototypes have a corresponding file in `_types/` before the OV ships (`07-SHIPPING-CHECKLIST.md` Phase 3.5).

**Validator coverage.** The optional `validate.py` includes a check (C7 — Prototype coverage) that scans every cartridge for `type:` values and confirms each has a matching `<NAMESPACE>_<TypeName>.md` in either the OV root's `_types/` or, if present, an enclosing cartridge's `_types/`. Missing files fail with a precise file:line pointer.

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
- `_types/` (Convention 6)
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

## Convention 10 — Standalone Sufficiency Posture

*Added v2.2.0.* In market-facing terms, an OV is a specialized AI agent. The objection any specialized agent must defeat is structural: *"Would a general LLM be better for this work?"* Convention 10 codifies the operative test — the **two master tests** elevated as load-bearing in `02-DESIGN-PRINCIPLES.md`'s top section — and requires every OV designed via OVE to declare a posture against the field-agnostic 47-requirement substrate at `_design-engine/_meta/standalone-sufficiency/`.

### When this applies

Every OV designed via OVE. No exceptions. The Convention applies whether the OV is commercial (sold to paying customers), internal (a team tool), personal (a single operator's system), or methodology corpora — the test "would the user (whoever they are) prefer a general LLM?" doesn't depend on monetization.

### The pattern

Every OV ships **three artifacts at the OV root** (the operator-facing posture + the source-of-truth registry + the filled scorecard), plus an optional **fourth artifact** for deferral. The 47-requirement substrate itself is NOT duplicated in every OV — it's referenced by REQ-ID from the engine's `_meta/standalone-sufficiency/`.

```
<OV root>/
├── standalone-sufficiency-posture.md      ← operator-facing one-pager (Convention 10 artifact 1)
├── _meta/
│   ├── posture.yaml                       ← source-of-truth registry (Convention 10 artifact 2)
│   └── vetting-rubric-filled.md           ← 0–3 scorecard with verdict (Convention 10 artifact 3)
└── posture-deferred.yaml                  ← OPTIONAL: opt-out marker (Convention 10 artifact 4)
```

The operator declares two things in `posture.yaml`: (a) `domain_stakes: low | high`, which determines whether the 8 TG conditional gates apply; (b) ≥1 moat-item commitment (one of REQ-E4, REQ-M1, REQ-M2, REQ-M3, REQ-M4) with a concrete schema-feature pointer. Per-requirement dispositions then follow (`met` / `partial` / `n-a` / `deferred`) with evidence pointers.

### Required artifacts per OV (Convention 10)

| Artifact | Location | Role |
|---|---|---|
| `standalone-sufficiency-posture.md` | OV root | Operator-facing one-pager. Tier coverage summary, T0 dispositions, TG applicability + dispositions, moat commitments with schema-feature pointers, verdict band. Drawn from `_design-engine/_templates/TEMPLATE-standalone-sufficiency-posture.md`. |
| `_meta/posture.yaml` | OV root | Source of truth. `ov_name`, `domain_stakes`, per-requirement `disposition` / `evidence` / `notes`, `moat_commitments`. Drawn from `_design-engine/_templates/TEMPLATE-posture-yaml.yaml`. |
| `_meta/vetting-rubric-filled.md` | OV root | Generated 0–3 scorecard rendering `posture.yaml` through the substrate's `vetting-rubric.md` template. Max weighted score = 558. Includes gating-rule veto outcome + verdict band. Drawn from `_design-engine/_templates/TEMPLATE-vetting-rubric-filled.md`. |
| `posture-deferred.yaml` (optional) | OV root | Opt-out marker for OVs whose posture work is deliberately deferred. Required fields: `deferred_until` (horizon date), `rationale`, `responsible_party`. Drawn from `_design-engine/_templates/TEMPLATE-posture-deferred.yaml`. With this file, C14 warns (not fails) until the horizon date. New OVs designed via OVE post-v2.2.0 may NOT use this marker — it exists only for retrofitting pre-existing OVs. |

### Substrate vs OVE-surface terminology seam (LOAD-BEARING)

The substrate at `_design-engine/_meta/standalone-sufficiency/` retains the upstream spec's **commercial framing** ("Loyalty & Retention," "customer," REQ-J4's "$100 vs $20" price-objection wording) because OVE does not modify vendored content. **OVE's surface — this Convention, the engine prose, the per-OV artifact names, the validator messages, the templates — uses neutral framing throughout** because many OVs are not commercialized:

| Source spec (commercial) | OVE surface (neutral) |
|---|---|
| "Loyalty & Retention" | "Standalone Sufficiency" |
| "Loyalty driver" | "Sufficiency driver" |
| "Customer" / "subscriber" | "User" / "operator" |
| "Retention" (as Tier T2's label) | "Durability" |
| REQ-J4 "Why pay $100 when ChatGPT is $20?" | "Value attribution: is this delivering value vs a general LLM?" |

See `_design-engine/_meta/standalone-sufficiency/README.md` for the seam in full. When wiring substrate concepts into OVE artifacts, always translate to the neutral OVE-surface terms.

### Validator coverage (C14 — Standalone Sufficiency Posture)

The optional `validate.py` includes a check (C14) that enforces the Convention at ship time. **C14 outcomes:**

| Outcome | Conditions |
|---|---|
| **pass** | `standalone-sufficiency-posture.md` exists at OV root; `_meta/posture.yaml` exists + schema-conformant; all 5 T0 dispositions present + = `met`; if `domain_stakes: high`, all 8 TG dispositions present + = `met`; ≥1 moat commitment with non-empty `schema_feature`; OR `posture-deferred.yaml` exists with valid future `deferred_until` date. |
| **fail** | `standalone-sufficiency-posture.md` missing AND no `posture-deferred.yaml`. Any T0 disposition missing or = `partial`/`deferred` without `waiver_reason`. If `domain_stakes: high`, any TG disposition missing. |
| **warn** | Zero moat items committed. T1 coverage <80% with no `_design-decisions.md` rationale. `posture-deferred.yaml` present but `deferred_until` past today's date. T2 coverage <80% with no rationale. |

### Why this matters

The two master tests (Displacement + Absorption) live in `02-DESIGN-PRINCIPLES.md` as load-bearing canon: any proposed feature must clear them, and the §17 anti-requirement traps (persona-only OVs, clever-prompt OVs, "smarter-Claude" OVs, epistemic-closure-as-moat, raw-memory-as-permanent-distinction, unqualified privacy claims) are explicitly disowned as OVE design traps. The principles set the design ceiling; Convention 10 enforces the ship floor.

Without Convention 10, the principles are advisory. With it, every shipped OV carries a declared, validator-checked record of which T0 hard gates pass, which TG conditional gates apply per declared domain stakes, which moat items are committed, and what the OV's verdict band is. The vetting rubric (`_meta/vetting-rubric-filled.md`) gives the operator a single page they can show a stakeholder when asked *"why use this OV instead of Claude?"* — and the answer rests on the substrate, not a sales pitch.

## Convention 11 — Knowledge-Augmented OVs (OKF data plane)

*Added v2.3.0.* Every OV designed via OVE is **structurally capable** of mounting an external knowledge corpus as a read-only **data plane**, using Google Cloud's **Open Knowledge Format (OKF) v0.1**. This separates the two things an OV holds: the **control plane** (the engine, the lifecycle, the rules of engagement — what the AI *does*) from the **data plane** (the curated domain knowledge — what the AI *knows*). OVE is the control plane; OKF is the data plane; this Convention is the bridge.

### When this applies

Every OV designed via OVE — but the **default disposition is `self_contained`**, and a self-contained OV mounts *nothing*. Convention 11 is "core" in the sense that every OV's manifest carries the data-plane fields and every OV is *capable* of becoming knowledge-augmented; it is not a mandate to mount anything. A normal OV is simply a Convention-11 OV with an empty `Knowledge_Mounts` list. This is how Convention 11 coexists with Convention 10 and the self-contained-corpus identity (`01-WHAT-IS-AN-OV.md`): see *The two dispositions* below.

### The two dispositions

Every OV declares `ove_Knowledge_Source` in its manifest:

| Disposition | Meaning | `Knowledge_Mounts` |
|---|---|---|
| **`self_contained`** (default) | All knowledge is baked into the OV's own corpus at design time and verified by ship (the F13 pipeline). The OV is the substrate. | empty |
| **`knowledge_augmented`** (KAOV) | The OV additionally mounts one or more OKF bundles as a read-only data plane and retrieves from them at session runtime under the bridge protocol (`08-KNOWLEDGE-RETRIEVAL.md`). | one or more mounts |

**Self-containment is preserved in both dispositions** because Convention 11 requires `ship_disposition: vendored` — a knowledge-augmented OV *copies the mounted OKF bundle into its own tree at ship time*. The bytes always ship with the OV; the data plane is a curated, version-pinned part of the corpus, not a live external dependency. This is what keeps Convention 10's Absorption story intact: a general LLM pointed at the same public folder is not equivalent, because the OV's value is the control-plane discipline + the curated, vendored, re-verified mount — not mere access to bytes. **A KAOV whose only moat reduces to "it can read the mount" fails Absorption** (the substrate's raw-memory-as-permanent-distinction anti-trap); the moat must live in the control plane.

### The pattern

A knowledge-augmented OV ships its mounts under a dedicated **Mounted Data Plane** zone (Convention 8's fifth zone — read-only, vendored, externally-authored):

```
<OV root>/
├── _ov-manifest.md                 ← declares ove_Knowledge_Source + Knowledge_Mounts
└── _knowledge/                      ← Mounted Data Plane zone (vendored OKF bundles)
    └── <bundle-slug>/               ← one vendored OKF bundle = one mount
        ├── index.md                 ← OKF directory listing (progressive disclosure)
        ├── <concept>.md             ← OKF concept documents
        └── <subdir>/ …
```

Each entry in the manifest's `Knowledge_Mounts` array records: `bundle_root` (path under `_knowledge/`), `okf_version` (the OKF spec version the bundle targets), `provenance` (where the bundle came from), `ship_disposition: vendored`, and `pin` (the git SHA and/or the per-concept `timestamp` set the bundle was vetted against — the boot-time re-verification baseline).

### OKF conformance (LOAD-BEARING)

A vendored mount MUST be a conformant OKF v0.1 bundle. Conformance is not OVE's invention — it is Google's spec, and matching it exactly is what makes a KAOV's knowledge **interoperable** with the wider OKF ecosystem (anyone's producer, anyone's consumer). The binding facts:

- **Unit terms.** The unit of knowledge is a **Concept** (one markdown document), addressed by its **Concept ID** (the file path within the bundle, `.md` removed). Never "node" / "node file."
- **Required frontmatter.** OKF's spec requires only `type`. OKF's *reference validator* additionally requires `title`, `description`, `timestamp`. **OVE producers emit all four** (plus `resource` when the concept maps to a real asset) to satisfy both. As a consumer, be permissive: accept any concept with a non-empty `type`.
- **Reserved filenames.** `index.md` (directory listing — no frontmatter except an optional `okf_version` at the bundle root) and `log.md` (update history). All other `.md` files are concepts.
- **Links and citations.** Cross-links and citations are **standard markdown links**, written **file-relative** (never leading-slash — that breaks GitHub rendering and is what every shipped Google bundle does). Citations sit under a `# Citations` heading (numbered) and/or inline-link the source concept. The `[Source: <path>]` pseudo-syntax is **not** OKF and must never be emitted.
- **Permissive consumption.** Never reject a bundle for missing optional fields, unknown `type` values, unknown extra keys, broken links, or a missing `index.md`.

The full distilled contract — read from the spec *and* the reference implementation — is captured at `_proposals/OKF-conformance-notes.md`. The engine chapter `08-KNOWLEDGE-RETRIEVAL.md` is the operator/AI-facing protocol.

### The bridge protocol (summary; full text in `08-KNOWLEDGE-RETRIEVAL.md`)

1. **Progressive disclosure.** The AI MUST read a directory's `index.md` before reading any concept beneath it. (OKF makes `index.md` optional; OVE makes reading-index-first mandatory — a stricter discipline that prevents context exhaustion, per the "Lost in the Middle" effect.)
2. **Workspace isolation.** The AI may retrieve only from bundles declared in `Knowledge_Mounts`. It may not traverse outside mounted paths.
3. **Explicit sourcing.** Every factual claim drawn from the data plane that lands in a drafted artifact or `_design-decisions.md` MUST carry an OKF-conformant citation (file-relative markdown link to the source concept, and/or a `# Citations` entry). This is F13 extended to the data plane.
4. **Boot-time re-verification.** At session start, for every mount a session depends on, the AI compares each depended-on concept's current `timestamp` (and the bundle's git SHA) against the `pin` recorded in the manifest. Any drift is surfaced to the operator and the affected claims are re-confirmed before reuse. This closes the gap that runtime citations prove *provenance*, not *currency* (F14).

### Required artifacts per OV (Convention 11)

| Artifact | Location | Role |
|---|---|---|
| `ove_Knowledge_Source` field | `_ov-manifest.md` frontmatter | `self_contained` (default) or `knowledge_augmented`. |
| `Knowledge_Mounts` array | `_ov-manifest.md` | Empty for self-contained OVs; one entry per vendored OKF bundle for KAOVs. |
| `_knowledge/<bundle-slug>/` | OV root | *KAOV only.* The vendored, OKF-conformant bundle(s). |

### Validator coverage (C15, C16)

The optional `validate.py` includes two checks:

- **C15** — for each `Knowledge_Mounts` entry: the `bundle_root` resolves under `_knowledge/`; the vendored bytes are present (`ship_disposition: vendored`); `okf_version` is set; and the bundle passes OKF v0.1 §9 conformance (every non-reserved `.md` has parseable frontmatter with a non-empty `type`). A `self_contained` OV with an empty mount list passes trivially.
- **C16** — no `[Source: …]` pseudo-citations anywhere in shippable content; data-plane citations are real markdown links resolving into a declared mount (workspace isolation).

### Why this matters

Convention 10 answers *"why this OV instead of a general LLM?"* Convention 11 answers the next question for knowledge-heavy domains: *"how does this OV hold a large, curated body of domain knowledge without drowning its context or fabricating?"* — by mounting it as a progressively-disclosed, vendored, re-verified OKF data plane that the control plane is disciplined about touching. Choosing OKF rather than a bespoke format is deliberate: it makes a KAOV's knowledge a portable asset that any OKF-speaking tool can produce, browse, diff, or consume, which widens the OV's integration surface instead of locking it in.

## How to apply during a new-OV design

The AI walking `BOOTSTRAP-NEW-OV.md` asks the operator one question early:

> *"What namespace prefix will this OV use? (Three to six lowercase letters ending in underscore. Example: `cook_` for a cooking OV.)"*

From that single answer, everything else follows:

- Prototype names: `COOK_<TypeName>`
- Property names: `cook_<Title_Snake_Case_Body>`
- Enum identifiers under `enums:`: `cook_<lowercase_plural>`
- `type` values on each Item: `COOK_<TypeName>`
- `type: Fleeting` on non-Item files
- `_types/` folder at the OV root with one `COOK_<TypeName>.md` per Prototype, each following `_design-engine/_templates/TEMPLATE-Prototype.md`
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
- [ ] `type` value matches a Prototype defined in the OV's `_meta/SCHEMA-OF-SCHEMAS.md` (Convention 4)
- [ ] Non-Item files declare `type: Fleeting` (Convention 4)
- [ ] Schema declaration exists at `_<purpose>-engine/_meta/SCHEMA-OF-SCHEMAS.md` (Convention 5)
- [ ] `_types/` folder exists at the OV root with one `<NAMESPACE>_<TypeName>.md` per Prototype declared in the OV's namespace (Convention 6)
- [ ] Each `_types/<NAMESPACE>_<TypeName>.md` conforms to `TEMPLATE-Prototype.md` and matches the Prototype's `_meta/SCHEMA-OF-SCHEMAS.md` declaration (Convention 6)
- [ ] `INSTALL.md` contains the install snippet with the OV's actual GitHub URL filled in (Convention 7)
- [ ] `OPERATOR-GUIDE.md` § "Updates" contains the update-workflow snippet (Convention 7)
- [ ] `UPDATE-PROMPT.md` exists at the OV root with the OV's name filled in (no `<OV-Name>` placeholders), references the four-zone boundary, and instructs the AI to confirm before destructive commands (Convention 7)
- [ ] Folder-naming convention (`<OV-Name>-v<major>.<minor>`) is documented in INSTALL.md (Convention 7)
- [ ] `CONTRIBUTING.md` § "Content zones" declares all four zones with at least one concrete example per zone (Convention 8)
- [ ] `.gitignore` exists and contains the Operator-Private Zone patterns documented in CONTRIBUTING (Convention 8)
- [ ] `README.md` § "What is in this folder" identifies the zones or links to the CONTRIBUTING declaration (Convention 8)
- [ ] `standalone-sufficiency-posture.md` exists at OV root with all 5 T0 hard-gate dispositions populated (Convention 10)
- [ ] `_meta/posture.yaml` exists at OV root, is schema-conformant, and the `domain_stakes` flag is set to `low` or `high` (Convention 10)
- [ ] If `domain_stakes: high`: all 8 TG conditional-gate dispositions are present in `posture.yaml` (Convention 10)
- [ ] At least one moat item (`REQ-E4`, `REQ-M1`, `REQ-M2`, `REQ-M3`, or `REQ-M4`) is committed in `posture.yaml` with a concrete `schema_feature` pointer — or the absence is justified in `_design-decisions.md` (Convention 10)
- [ ] `_ov-manifest.md` declares `ove_Knowledge_Source` (`self_contained` or `knowledge_augmented`) and a `Knowledge_Mounts` array — empty for self-contained OVs (Convention 11)
- [ ] If `ove_Knowledge_Source: knowledge_augmented`: every `Knowledge_Mounts` entry is `ship_disposition: vendored`, its bundle is vendored under `_knowledge/`, sets `okf_version` + `pin`, and passes OKF v0.1 conformance (Convention 11)
- [ ] No `[Source: …]` pseudo-citations; data-plane citations are file-relative markdown links into a declared mount (Convention 11)

These checks are also covered by the optional `validate.py` (`C1` backbone presence, `C2` frontmatter presence, `C3` placeholder leakage — the wider scrub, `C7` Prototype coverage, `C8` zone-boundary documentation, `C9` gitignore sanity, `C10` UPDATE-PROMPT sanity, `C14` Standalone Sufficiency posture, `C15` Knowledge-Mount conformance, `C16` data-plane citation form) and by walking `VALIDATION-CHECKLIST.md` for markdown-only environments.

## Related references

- `_design-engine/04-SCHEMA-DESIGN.md` § "Convention compliance" — points back to this file when designing the new OV's schema
- `_design-engine/05-WRITING-FOR-AI.md` § "Property-naming conventions" — points back to this file when drafting any property-bearing prose
- `_design-engine/BOOTSTRAP-NEW-OV.md` — the namespace CQ that triggers the convention cascade; the Convention 7/8 artifact list per new OV
- `_design-engine/07-SHIPPING-CHECKLIST.md` § "Phase 3.6 — Convention 7/8 readiness" — gates ship until INSTALL/OPERATOR-GUIDE/CONTRIBUTING/.gitignore are all in place
