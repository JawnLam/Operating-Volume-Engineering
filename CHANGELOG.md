---
Item_Prototype: Fleeting
Item_ID: ove-changelog
Title: "Operating-Volume-Engineering — Changelog"
Date_Added: 2026-06-01
Date_Modified: 2026-06-06
Needs_Processing: false
---

# Changelog

All notable changes to Operating-Volume-Engineering are documented in this file. Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versioning follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] — 2026-06-06

Additive minor release focused on four goals: (a) the quality of the design conversation the AI runs, (b) the quality of the OV folders an engagement ships, (c) OVE itself + the OVs it designs conforming to universal vault conventions out of the box, and (d) every OV designed via OVE being **portable** — readable and operable by someone without the OV author's surrounding vault infrastructure. No v1.0 cartridges are broken; no required cartridge backbone fields added; no engine files renamed or removed; no folder conventions changed.

### Changed — read protocol is now tiered, with a canonical/pointer relationship

- `_design-engine/00-START-HERE.md` is the canonical source of the read protocol; `AI-BOOTSTRAP.md` mirrors as a thin pointer. Both name the relationship in-prose so future divergence is itself an F6 violation to flag.
- **Tier 1** (always read before the first user-facing message): `00-START-HERE.md`, `01-WHAT-IS-AN-OV.md`, `02-DESIGN-PRINCIPLES.md`, `03-DESIGN-PROTOCOL.md`, `05-WRITING-FOR-AI.md`, plus the active cartridge's `_ov-manifest.md` / `_design-state.md` / most recent 1–2 Sessions logs, plus `_USER.md` if present.
- **Tier 2** (load on demand by activity): `04-SCHEMA-DESIGN.md` (SCHEMA-DESIGN), `06-STATE-PERSISTENCE.md` (CARTRIDGE-SHAPE / state work), `07-SHIPPING-CHECKLIST.md` (SHIP-PREP), `_meta/SCHEMA-OF-SCHEMAS.md` (audit / non-trivial schema), `_meta/FAILURE-MODES.md` (audit / specific F-code lookup), `BOOTSTRAP-NEW-OV.md` (new-OV path), `_design-engine/_templates/*` (ARTIFACT-DRAFT).
- Eliminates the v1.0 contradiction where AI-BOOTSTRAP demanded ~12 files "no skim" while `00-START-HERE.md` documented some of them as on-demand.

### Changed — readiness statement is now verifiable

The AI's first user-facing message must satisfy three conditions or it does not count as a readiness statement:

1. Two to four sentences.
2. State the path taken (existing cartridge, new OV, audit, orientation).
3. Cite **one** non-guessable thing — for existing-cartridge work, a concrete fact from cartridge state (current design phase, most recent locked decision in `_design-decisions.md`, or a named open thread); for new-OV / orientation, a specific Tier 1 rule the AI will enforce in the first turn (e.g., P10's one-question-at-a-time rule, P7's identity-placeholder rule).

A confident greeting without a cited fact or named rule is now the operator's diagnostic that the reads did not actually happen. Canonical spec in `_design-engine/00-START-HERE.md` § Readiness statement; AI-BOOTSTRAP.md § 4 is a thin pointer.

### Added — optional validator and prose fallback

- `_design-engine/_meta/validate.py` — pure-stdlib Python script that runs six checks: C1 cartridge backbone presence, C2 frontmatter present and non-empty, C3 placeholder leakage (with code-span and fenced-block exemption), C4 identity-from-indirect-signals (F3 class), C5 dangling wikilinks, C6 bootstrap-vs-engine drift (F6 class). Exit codes: 0 = pass, 1 = warnings only, 2 = failures. Optional; no core flow depends on it.
- `_design-engine/_meta/VALIDATION-CHECKLIST.md` — prose fallback walkthrough for markdown-only environments.

### Changed — personal-data scrub is now a hard ship gate

`07-SHIPPING-CHECKLIST.md` Phase 3 explicitly blocks progression to Phase 7 (git init) until the validator returns exit code 0, or exit code 1 with every warning explicitly waived in writing in `_design-decisions.md`. The markdown-only fallback is the combined grep, which must return zero hits or every hit must be waived. F3 (identity-from-indirect-signals) is documented as recurring; "remember to check" was previously the only guard.

### Added — substrate support matrix and sandbox-mode loudness

- `README.md` now carries a Substrate support matrix distinguishing read+write environments (Claude Code, Cursor, Windsurf, Claude Desktop, etc.) from read-only environments (ChatGPT Projects, Claude.ai with Projects, Gemini chat). Read-only environments produce **degraded multi-session statefulness**.
- `AI-BOOTSTRAP.md` Phase 0.2 makes the writability check explicit and routes sandbox-mode declaration to the canonical readiness-statement spec.
- `_design-engine/00-START-HERE.md` § Readiness statement now includes a Sandbox-mode addendum requiring the AI to announce read-only substrate loudly, before stating the path. A read-only substrate without an announcement is the failure mode the v1.0 docs did not catch.

### Changed — `.gitignore` trade-off is documented

- `.gitignore` comment block now names the trade-off explicitly: excluding `_design-state.md` and `Sessions/*.md` by default keeps the folder shareable but means your own history isn't tracked without opt-in.
- `INSTALL.md` now has a § "Tracking your own design history" with a copy-paste `git add -f` recipe and a rationale for the default.

### Added — universal conventions for OV-designed output

OVE now produces OVs that conform to a small set of universal frontmatter and naming conventions out of the box. The operator no longer post-processes the output to make it vault-compatible.

- **New file `_design-engine/_meta/CONVENTIONS.md`** — canonical statement of five conventions: Universal Core fields on every shipped note (`Item_Prototype`, `Item_ID`, `Title`, `Date_Added`, `Date_Modified`, `Needs_Processing`); case rules for property names (prefix `lowercase_snake_case_`, body `Title_Snake_Case`, acronyms fully capitalized, enum identifiers lowercase plural); one namespace per OV; one `Item_Prototype` per Prototype with `Fleeting` for non-Item files; one schema-of-namespace declaration.
- **`BOOTSTRAP-NEW-OV.md`** mandates reading `CONVENTIONS.md` and routes the new-OV-design path through the namespace cascade.
- **`04-SCHEMA-DESIGN.md` Q0** added: the AI asks for the new OV's namespace prefix before Q1, and everything (prototype names, property names, enum identifiers, `Item_Prototype` values) cascades from that single answer.
- **`05-WRITING-FOR-AI.md`** extended with a frontmatter-conventions section pointing back to `CONVENTIONS.md`.
- **Tier 2 read protocol** (in `00-START-HERE.md` and `AI-BOOTSTRAP.md`) now lists `_meta/CONVENTIONS.md` as on-demand for new-OV design and convention-compliance audits.
- **Operator-override path**: if the operator wants different conventions, they say so during SCHEMA-DESIGN; the choice is logged in `_design-decisions.md` and applied throughout.

### Changed — OVE itself conforms to its own conventions

OVE is now a first-class citizen of the conventions it teaches. Concretely:

- **All 24 non-cartridge OVE files** now carry the six Universal Core fields in YAML frontmatter — front-door docs (`README.md`, `INSTALL.md`, `AI-BOOTSTRAP.md`, `OPERATOR-GUIDE.md`, `CONTRIBUTING.md`, `LICENSE.md`, `VERSION.md`, `CHANGELOG.md`), all 9 engine pages, the 3 `_meta/` docs (`SCHEMA-OF-SCHEMAS.md`, `FAILURE-MODES.md`, `VALIDATION-CHECKLIST.md`), and the 3 templates that previously lacked `Item_Prototype`. Engine and meta files declare `Item_Prototype: Fleeting`; cartridge Items continue to declare `Item_Prototype: OVE_*`.
- **All `ove_*` property names migrated** from pre-rule `lowercase_snake_case` body to `Title_Snake_Case` body per the universal case convention. Migration applied via word-boundary-anchored regex across 17 distinct property names plus 2 prose-mention stragglers (e.g., `ove_design_phase` → `ove_Design_Phase`, `ove_ov_name` → `ove_OV_Name` with OV fully capitalized as an acronym, `ove_quality_gates_passed` → `ove_Quality_Gates_Passed`).
- **`ove_Version`** introduced as the property name for OV-version metadata in `VERSION.md` (was previously the now-non-canonical `ove_version`).
- All 5 worked-example cartridges now have schema-compliant frontmatter that passes the `validate.py` C1 / C2 / C3 / C4 / C5 / C6 / C7 checks when the corresponding namespace prototypes exist in an operator's vault infrastructure.

### Changed — vocabulary clean-up: "atom" → "Item" and "atom type" → "Prototype"

The word "atom" had been doing two jobs in OVE prose: naming the *type definition* (the schema), and naming the *instance* (the note). This release separates the two:

- **Prototype** — the type definition. A schema-bearing declaration that lives in `_Prototypes/`. There is exactly one Prototype per kind of thing in an OV's namespace. The frontmatter field `Item_Prototype:` points at one.
- **Item** — the universal noun for *any instance of any Prototype*. A specific cartridge note declaring `Item_Prototype: LFW_Beat` is an Item of the LFW_Beat Prototype. Replaces all generic uses of "atom" across the engine, templates, conventions, validator messages, and the five worked-example cartridges.

Concretely:

- All occurrences of "atom" / "atoms" → "Item" / "Items" across `00-START-HERE.md`, `01-WHAT-IS-AN-OV.md`, `02-DESIGN-PRINCIPLES.md`, `04-SCHEMA-DESIGN.md`, `05-WRITING-FOR-AI.md`, `06-STATE-PERSISTENCE.md`, `_meta/CONVENTIONS.md`, `_meta/SCHEMA-OF-SCHEMAS.md`, `_meta/FAILURE-MODES.md`, `_templates/TEMPLATE-schema-draft.md`, `AI-BOOTSTRAP.md`, `OPERATOR-GUIDE.md`, and this CHANGELOG.
- All occurrences of "atom type" / "atom types" → "Prototype" / "Prototypes".
- `04-SCHEMA-DESIGN.md` Q3 reworded from "the atomic unit of this OV" to "what each Item in this OV represents" — the original phrasing carried the type/instance confusion.
- `CONVENTIONS.md` Convention 4 reworded from "One `Item_Prototype` per atom type" to "Every Prototype gets its own `Item_Prototype` value" — clearer and reads as plain English.

### Changed — vault Infrastructure side: `LLL_Atom` → `LLL_Unit` and matching property/enum cascade

OVE v1.1.0's vocabulary clean-up cascades into the user's vault Infrastructure as **Master_Schema v1.19.0** (separately released). The cascade:

- `LLL_Atom` prototype → `LLL_Unit` (the LLL polymorphic study-unit placeholder — a subject cartridge overrides what a Unit *is*: kanji, piece, theorem, concept). The word "Unit" is LLL-specific; "Item" is the cross-OV universal noun. The distinction keeps the universal/specific layers clean — a `LLL_Curriculum` note is also an Item (of the `LLL_Curriculum` Prototype), so naming the polymorphic Prototype `LLL_Item` would have muddled the vocabulary.
- `lll_Atom_Type` → `lll_Unit_Type`; `lll_Primary_Atom_Types` → `lll_Primary_Unit_Types`; `lll_Atoms_Engaged` → `lll_Units_Engaged`; `lll_Atoms_Referenced` → `lll_Units_Referenced`.
- `lfw_Atom_Type` → `lfw_Item_Type` (LFW has no polymorphic placeholder — every LFW Prototype is concrete, so `Item` is the right cascade); `lfw_atom_types` enum → `lfw_item_types`; `lfw_Atoms_Touched` → `lfw_Items_Touched`; `lfw_Custom_Atoms` → `lfw_Custom_Items`.
- LLL deployed cartridges `Atoms/` folders → `Units/` (Cybernetics, Git-For-Vibe-Coding); LFW deployed cartridges `Atoms/` folders → `Items/` (Shepherds-Game-Book-1, Late-Frost, Persistence-Question).
- `TEMPLATE-Atom-Generic.md` → `TEMPLATE-Unit-Generic.md` (LLL teaching engine); LFW engine chapter `04-ATOMS-AND-STRUCTURE.md` → `04-ITEMS-AND-STRUCTURE.md`.
- Master_Schema section header `# 3. PROPERTIES (The "Atoms")` → `# 3. PROPERTIES (The "Item Fields")`; comment label "Universal atom fields" → "Universal Item fields"; CONCEPT Prototype subtitle "The Atom" → "The Smallest Discrete Unit".

Total vault-side scope: 1 prototype rename, 8 property/enum renames, 197 notes migrated (280 individual substitutions), 5 folder renames, 2 engine/template file renames, 26 additional files updated for `lfw_Custom_Atoms` and all-caps `ATOMS` cleanups. See the user's Master_Schema.yaml v1.19.0 changelog and the Infrastructure Decision Log entry `2026-06-06 (follow-up) — Schema v1.19.0` for the full vault-side record.

OVE itself adopts these conventions: the engine docs use the new vocabulary; the validator's messages name Items and Prototypes; the cartridge files cite them. New OVs designed via OVE inherit the conventions through `CONVENTIONS.md` and the namespace cascade.

### Added — Convention 6: every OV ships its own `_Prototypes/` folder

The new convention makes OVs **portable**. Without it, a cartridge note that declares `Item_Prototype: <NAMESPACE>_<TypeName>` is a name pointer with no definition behind it — fine for an operator with a vault-wide central registry, broken for everyone else. Convention 6 fixes that.

- **New file `_design-engine/_meta/CONVENTIONS.md` § Convention 6** — every OV bundles a top-level `_Prototypes/` folder containing one `.md` file per Prototype in its namespace. The folder is the canonical home for Prototype definitions; any vault-wide central registry the operator maintains is a downstream union view, not authority.
- **New template `_design-engine/_templates/TEMPLATE-Prototype.md`** — the standard structure every Prototype definition follows: Purpose, Required frontmatter, Body structure, Naming, Example Item, Relationships, Notes. Each section is operational (executable by the AI when materializing Prototypes), not descriptive.
- **`04-SCHEMA-DESIGN.md` new section "Materializing the `_Prototypes/` folder"** — step-by-step guidance the AI follows during ARTIFACT-DRAFT to write one Prototype file per declared Prototype, cross-checked against `_meta/SCHEMA-OF-SCHEMAS.md`.
- **`BOOTSTRAP-NEW-OV.md` Step 5** — adds `_Prototypes/` materialization between BOOTSTRAP-NEW-CARTRIDGE drafting and template drafting. Names Convention 6 in-prose so the AI sees why the folder is non-optional.
- **`07-SHIPPING-CHECKLIST.md` new Phase 3.5** — hard-stop gate. Verifies the `_Prototypes/` folder exists, every `Item_Prototype:` value used in any cartridge has a corresponding `.md` file in `_Prototypes/`, and every file conforms to `TEMPLATE-Prototype.md`. Phase 7 (git init) is locked until the gate is clean.
- **`validate.py` new check C7 — Prototype coverage** — walks every cartridge, collects distinct `Item_Prototype:` values (excluding `Fleeting`), and verifies each resolves to a `<NAMESPACE>_<TypeName>.md` in either the cartridge's local `_Prototypes/` (cartridge-local override) or the OV root's `_Prototypes/` (canonical home). Misses fail with `<file>:<line>` and the missing Prototype name. C5 (dangling wikilinks) now skips any `_Prototypes/` file because Prototype definitions contain placeholder example wikilinks by design.

### Added — OVE ships its own `_Prototypes/` folder

OVE itself follows Convention 6. The OV root now contains `_Prototypes/` with five files corresponding to the OVE namespace's Prototypes:

- `_Prototypes/OVE_OV_Manifest.md`
- `_Prototypes/OVE_Design_State.md`
- `_Prototypes/OVE_Design_Decisions.md`
- `_Prototypes/OVE_Schema_Draft.md`
- `_Prototypes/OVE_Session.md`

Verbatim mirrors of the corresponding entries in the user's vault Infrastructure `_Prototypes/`. Anyone cloning OVE without that vault Infrastructure now gets the Prototype definitions out of the box.

### Added — worked-example cartridges ship verbatim Prototype mirrors where vault Prototypes exist

- **`Long-Form-Writing/_Prototypes/`** — 9 LFW_* files (LFW_Beat, LFW_Chapter, LFW_Character_Bible, LFW_Motif, LFW_Note, LFW_Reader, LFW_Scene, LFW_Session, LFW_Source) copied verbatim from the user's vault Infrastructure.
- **`LifeLong-Learning-Retrospective/_Prototypes/`** — 9 LLL_* files (LLL_Unit, LLL_Curriculum, LLL_Quiz, LLL_Session, LLL_SR_Log, LLL_State, LLL_Subject_Manifest, LLL_Synthesis, LLL_Thinker) copied verbatim, with LLL_Unit reflecting the post-rename name.
- **Negotiation-Preparation, Relationship-Cultivation, SOLVE-eX-Retrospective** — no `_Prototypes/` folder. These cartridges show OVE in active design phase with no shipped vault Prototypes for their target OVs. Per the operator's "mirror verbatim" rule, no fabrication: the folder is absent rather than populated with illustrative placeholders.

### Notes

This release is the minor-version product of an audit run against v1.0 plus a convention-conformance pass plus an operator-driven scope expansion for portability (Convention 6) and vocabulary clarity (atom → Item, LLL_Atom → LLL_Unit). Every change is additive: no required cartridge backbone field added, no engine file renamed or removed, no folder conventions changed. v1.0 cartridges remain readable and operable under v1.1; the case migration and vocabulary rename apply cleanly to any v1.0 cartridge by running the same word-boundary-anchored regex.

The schema (cartridge backbone) is unchanged. Schema work — including the OV-level / cross-cartridge Items surfaced by the Negotiation-Preparation and Relationship-Cultivation cartridges — is deferred to a future minor release with a deliberate schema-of-schemas extension, or to a v2.0 conversation with migration path.

**Vault-Infrastructure dependency.** The vocabulary cascade described above (`LLL_Atom` → `LLL_Unit` etc.) happened in the operator's vault as **Master_Schema v1.19.0** in coordination with this OVE release. The two ship together; either alone would leave a half-migrated state. If you are not the operator and you are reading this from the OVE repo, the vault-side migration is informational — it describes the change the OVE author made to their own vault to match the OVE v1.1.0 vocabulary. Your own vault stays untouched.

**Deferred follow-ups.** Sibling LFW and LLL GitHub repos in the operator's local vault were not migrated by this release — those need separate coordinated public releases. The vault's `My Operating Volumes/` deployed working state IS fully migrated.

## [1.0.0] — 2026-06-01

### Added — initial public release

- **Design engine** (`_design-engine/`):
  - `00-START-HERE.md` — assistant entry point + mandatory read order
  - `01-WHAT-IS-AN-OV.md` — definition, the lexicon spectrum (token → harness), where OV sits, why the category exists
  - `02-DESIGN-PRINCIPLES.md` — substrate-agnostic, statefulness, cartridge pattern, self-similarity test, operator-confirmed-identity rule
  - `03-DESIGN-PROTOCOL.md` — session protocol for designing an OV; audit-mode protocol
  - `04-SCHEMA-DESIGN.md` — Q1–Q8 protocol for designing the schema of a new OV
  - `05-WRITING-FOR-AI.md` — writing AI-readable prose; tone; the multi-bullet-questionnaire failure mode; fabrication discipline
  - `06-STATE-PERSISTENCE.md` — what gets written when, durability contracts, the file-as-memory principle
  - `07-SHIPPING-CHECKLIST.md` — scrubbing, versioning, license, README structure, GitHub workflow
  - `BOOTSTRAP-NEW-OV.md` — the cartridging prompt for opening a new design engagement
- **Templates** (`_design-engine/_templates/`):
  - Root-doc templates (README, AI-BOOTSTRAP, INSTALL, OPERATOR-GUIDE, CONTRIBUTING, LICENSE-CCBY40, VERSION, CHANGELOG, .gitignore, _USER.md)
  - Cartridge backbone templates (`_ov-manifest.md`, `_design-state.md`, `_design-decisions.md`, `_schema-draft.md`, session log, artifact)
- **Meta** (`_design-engine/_meta/`):
  - `SCHEMA-OF-SCHEMAS.md` — the meta-ontology (engine → cartridge → instance, three layers, applied recursively to OVs)
  - `FAILURE-MODES.md` — canonical catalog (fabrication, identity-from-indirect-signals, multi-bullet questionnaire, drift, schema violation, etc.)
- **Root docs**: `README.md`, `AI-BOOTSTRAP.md`, `INSTALL.md`, `OPERATOR-GUIDE.md`, `CONTRIBUTING.md`, `LICENSE.md` (CC-BY 4.0), `VERSION.md`, this file, `_USER.md.template`, `.gitignore`
- **Five worked-example cartridges**:
  - `SOLVE-eX-Retrospective/` — retrospective design analysis of SOLVE-eX
  - `LifeLong-Learning-Retrospective/` — retrospective design analysis of LifeLong-Learning
  - `Negotiation-Preparation/` — fresh-design anchor demonstration (full depth)
  - `Long-Form-Writing/` — fresh-design walkthrough for book/dissertation/screenplay work (lighter depth)
  - `Relationship-Cultivation/` — fresh-design walkthrough for relational-CRM-style OV (lighter depth)

### Notes

Operating-Volume-Engineering v1.0 is the propagator of the form, completing a trio of operating volumes alongside [SOLVE-eX](https://github.com/JawnLam/SOLVE-eX) (decision-making and problem-solving) and [LifeLong-Learning](https://github.com/JawnLam/LifeLong-Learning) (self-directed deep study). The term "operating volume" was coined to name the slot in the AI lexicon between *Custom GPT / Project* and *AI harness* — larger than a skill, deeper than a Custom GPT, smaller than a harness, substrate-agnostic. The associated discipline is "operating volume engineering," parallel to prompt / agent / harness engineering.
