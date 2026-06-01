# Changelog

All notable changes to Operating-Volume-Engineering are documented in this file. Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versioning follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
