---
Item_Prototype: Fleeting
Item_ID: ove-version
Title: "Operating-Volume-Engineering — Version"
Date_Added: 2026-06-01
Date_Modified: 2026-06-06
Needs_Processing: false
ove_Version: "1.2.0"
schema_version: "1.0"
schema_status: "STABLE"
release_date: 2026-06-06
release_phase: "Minor release — Conventions 7 (install-and-update pattern) + 8 (engine vs operator-content boundary); validator C8/C9 checks; full dogfooding across INSTALL/OPERATOR-GUIDE/CONTRIBUTING"
---

# Operating-Volume-Engineering — Version

This is Operating-Volume-Engineering **v1.1.0** — first minor release. Additive only; v1.0 cartridges remain readable.

## Version identifiers

| Identifier              | Value         | Notes                                                                  |
|-------------------------|---------------|------------------------------------------------------------------------|
| **Software**            | v1.1.0        | Minor release — quality improvements (read protocol, readiness statement, validator, scrub gate, substrate matrix) |
| **Design schema**       | v1.0          | STABLE — cartridge backbone unchanged at this version                  |
| **Design engine**       | v1.1          | Tiered read protocol (canonical in `00-START-HERE.md`); mandatory readiness-statement specification; sandbox-mode loudness addendum |
| **Templates**           | v1.0          | Unchanged                                                              |
| **Validator**           | v1.0          | New — `_design-engine/_meta/validate.py` plus prose fallback at `_design-engine/_meta/VALIDATION-CHECKLIST.md` |
| **Worked examples**     | v1.0          | Unchanged                                                              |
| **Release date**        | 2026-06-06    |                                                                        |

## Schema policy

The cartridge backbone files (`_ov-manifest.md`, `_design-state.md`, `_design-decisions.md`, `_schema-draft.md`) and the engine file numbering (`00-START-HERE` through `07-SHIPPING-CHECKLIST` plus `BOOTSTRAP-NEW-OV`) are stable at v1.0. Any change that:

- Adds a required field to a cartridge backbone file
- Renames or removes an engine file
- Changes the cartridge folder convention

requires a major version bump (v2.0). Additive changes (new optional fields, new templates, new worked examples) are minor version bumps (v1.x).

## What is in this version

- **Design engine** in `_design-engine/`:
  - Eight core operating files (`00–07`) plus `BOOTSTRAP-NEW-OV.md`
  - Templates for every standard OV-ship file (`_templates/`)
  - Schema-of-schemas + failure-modes catalog (`_meta/`)
- **Front-door docs at the root**: `README`, `AI-BOOTSTRAP`, `INSTALL`, `OPERATOR-GUIDE`, `CONTRIBUTING`, `LICENSE`, `VERSION`, `CHANGELOG`
- **Optional user profile template**: `_USER.md.template`
- **Five worked-example cartridges**:
  - `SOLVE-eX-Retrospective/` — retrospective design analysis of [SOLVE-eX](https://github.com/JawnLam/SOLVE-eX)
  - `LifeLong-Learning-Retrospective/` — retrospective design analysis of [LifeLong-Learning](https://github.com/JawnLam/LifeLong-Learning)
  - `Negotiation-Preparation/` — fresh worked example, anchor demonstration (full depth)
  - `Long-Form-Writing/` — fresh worked example, lighter depth
  - `Relationship-Cultivation/` — fresh worked example, lighter depth
- **`.gitignore`** that keeps a user's private design work out of source control by default while preserving the five shipped worked examples

## Compatibility

- **AI:** any capable assistant (Claude Sonnet/Opus class, GPT-4 class and above, Gemini 2.x and above)
- **OS:** Mac, Windows, Linux
- **Editor:** Obsidian, VS Code, Cursor, Windsurf, Zed, JetBrains, or plain text editors with AI integration
- **Python / network / runtime dependencies:** none

## License

See `LICENSE.md`. Released under CC-BY 4.0. Original work by Jawn Lam.
