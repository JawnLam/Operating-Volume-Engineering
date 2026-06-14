---
Item_Prototype: Fleeting
Item_ID: ove-version
Title: "Operating-Volume-Engineering — Version"
Date_Added: 2026-06-01
Date_Modified: 2026-06-13
Needs_Processing: false
ove_Version: "2.0.0"
schema_version: "2.0"
schema_status: "STABLE"
release_date: 2026-06-13
release_phase: "Major release — OV Archetype Declaration (finite-horizon vs practice); Source Discipline gates (F13 prevention); Voice + Client Promise gates (Audience Register + Vocabulary Audit); Convention 9 (Sensitive Source Materials); restrictive LICENSE template. Breaking against v1.x in Q6 framing, manifest schema, and SHIP-PREP phase structure."
---

# Operating-Volume-Engineering — Version

This is Operating-Volume-Engineering **v2.0.0** — the first major release. Breaking against v1.x in three places: Q6 framing (now forks by archetype), manifest schema (new required fields `ove_OV_Archetype` and Q14 audience register fields), and SHIP-PREP phase structure (new Phase 3.7 / 3.8 / 3.9 hard-stops). No runtime impact on OVs *already shipped* under v1.x — see "Compatibility with v1.x OVs" below.

## Version identifiers

| Identifier              | Value         | Notes                                                                  |
|-------------------------|---------------|------------------------------------------------------------------------|
| **Software**            | v2.0.0        | Major release — five v2.0 packages (Archetype Declaration, Source Discipline, Voice + Client Promise, Sensitive Sources + Restrictive LICENSE, Bookkeeping) |
| **Design schema**       | v2.0          | BREAKING — `ove_OV_Archetype`, `ove_Audience_Target_Reader`, `ove_Audience_Business_Context`, `ove_Audience_Prose_Register` added to manifest as required for v2.0-designed OVs |
| **Design engine**       | v2.0          | Q6 forks by archetype; Q14 audience register; INTERVIEW CQ11 (archetype) + strengthened CQ3 (structured source inventory); 03-DESIGN-PROTOCOL.md Step 4.5 source-inventory gate |
| **Templates**           | v2.0          | Three new templates: TEMPLATE-source-inventory, TEMPLATE-LICENSE-restrictive, TEMPLATE-sensitive-source-placeholder. TEMPLATE-ov-manifest and TEMPLATE-schema-draft extended for archetype + audience register |
| **Validator**           | v2.0          | Three new checks: C11 source-inventory-completeness, C12 citation-audit-log, C13 vocabulary-audit-log. `range(1, 14)` |
| **Worked examples**     | v1.0          | Unchanged — five v1.x worked-example cartridges grandfather (see "Compatibility with v1.x OVs") |
| **Release date**        | 2026-06-13    |                                                                        |

## Schema policy

v1.x policy (cartridge backbone files + engine file numbering frozen at v1.0; additive only for v1.x) ends with this release. **v2.0 makes a deliberate breaking change** justified by P13 (`02-DESIGN-PRINCIPLES.md`):

1. The Q6 fork by archetype changes the meaning of the question; v1.x OVs that didn't declare archetype get the finite-horizon path by default (which is what they used historically).
2. New required manifest fields (`ove_OV_Archetype`, the three `ove_Audience_*` fields) for v2.0-designed OVs.
3. New SHIP-PREP hard-stops (Phase 3.7 / 3.8 / 3.9) that block public ship for any OV that doesn't satisfy them.

The cartridge backbone files (`_ov-manifest.md`, `_design-state.md`, `_design-decisions.md`, `_schema-draft.md`) themselves are not renamed. The engine file numbering (`00-START-HERE` through `07-SHIPPING-CHECKLIST` plus `BOOTSTRAP-NEW-OV`) is not renamed. The new template files added in v2.0 (`TEMPLATE-source-inventory`, `TEMPLATE-LICENSE-restrictive`, `TEMPLATE-sensitive-source-placeholder`) are additive.

Future v2.x patch/minor releases will be additive against the v2.0 schema. v3.0 will be the next major-bump opportunity.

## Compatibility with v1.x OVs

**An OV has no runtime dependency on OVE.** OVE is build-time-only — once an OV is shipped, it stands alone with its own engine, conventions, and protocol baked in. The OVE version that produced an existing OV is provenance, not operational metadata.

Practical implication: **v1.x-built OVs do not need migration to v2.0**. SOLVE-eX v2.x, LFW v1.7.x, LLL v1.3.x, OVE-itself v1.2.1, and Political-Landscape-Cartography v1.0 (built under OVE v1.2 conventions) all continue to function as they shipped. v2.0 changes how the *next* OV gets built.

If an operator chooses to rebuild an existing OV under v2.0 conventions, the path is **rebuild, not migrate**: open a fresh OVE design cartridge, run the v2.0 INTERVIEW + SCHEMA-DESIGN flow against the same domain, and re-ship.

## What is in this version

- **Design engine** in `_design-engine/`:
  - Eight core operating files (`00–07`) plus `BOOTSTRAP-NEW-OV.md` (v2.0: 03 + 04 + 07 + BOOTSTRAP extended; 01 + 02 augmented; archetype + source-discipline + voice cascade)
  - Templates for every standard OV-ship file (`_templates/`) — v2.0 adds three new templates
  - Schema-of-schemas + failure-modes catalog (`_meta/`) — v2.0 adds F13 + Convention 9
  - Validator (`_meta/validate.py`) — v2.0 adds C11 / C12 / C13
- **Front-door docs at the root**: `README`, `AI-BOOTSTRAP`, `INSTALL`, `OPERATOR-GUIDE`, `CONTRIBUTING`, `LICENSE`, `VERSION`, `CHANGELOG`, `UPDATE-PROMPT`
- **Optional user profile template**: `_USER.md.template`
- **Five worked-example cartridges** (unchanged from v1.x):
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
- **Python / network / runtime dependencies:** none (validator uses pure stdlib)

## License

See `LICENSE.md`. OVE itself remains under CC-BY 4.0. The v2.0 release adds a restrictive LICENSE template (`_design-engine/_templates/TEMPLATE-LICENSE-restrictive.md`) for new OVs that need it — OVE itself does not adopt the restrictive license.

Original work by Jawn Lam.
