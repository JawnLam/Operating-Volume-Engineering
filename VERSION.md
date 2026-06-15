---
Item_Prototype: Fleeting
Item_ID: ove-version
Title: "Operating-Volume-Engineering — Version"
Date_Added: 2026-06-01
Date_Modified: 2026-06-15
Needs_Processing: false
ove_Version: "2.2.0"
schema_version: "2.0"
schema_status: "STABLE"
release_date: 2026-06-15
release_phase: "Minor release — Convention 10 (Standalone Sufficiency Posture): every OV designed via OVE declares a posture against a vendored 47-requirement substrate; two master tests (Displacement + Absorption) and 10 anti-requirement traps elevated as load-bearing in 02-DESIGN-PRINCIPLES; new validator check C14; SHIP-PREP Phase 3.10. Worked-example retrofits: Negotiation-Preparation + SOLVE-eX-Retrospective ship full posture; LFW, LLL, Relationship-Cultivation, PLC-Retrospective opt-out via posture-deferred.yaml (horizon 2026-12-01). Additive over v2.1.0; no breaking changes."
---

# Operating-Volume-Engineering — Version

This is Operating-Volume-Engineering **v2.2.0** — minor release introducing **Convention 10 — Standalone Sufficiency Posture**, the OVE-side enforcement mechanism for the test "would a general LLM be better for this work than this OV?" The convention vendors a field-agnostic 47-requirement substrate, requires every new OV to declare a posture against it, ships a new validator check (C14), elevates the two master tests (Displacement + Absorption) and the 10 anti-requirement traps as load-bearing canon in `02-DESIGN-PRINCIPLES`, and adds a new SHIP-PREP hard-gate (Phase 3.10). Two worked examples are retrofitted (Negotiation-Preparation, SOLVE-eX-Retrospective); four others carry a bounded deferral marker (horizon 2026-12-01) per dogfood scope.

## Version identifiers

| Identifier              | Value         | Notes                                                                  |
|-------------------------|---------------|------------------------------------------------------------------------|
| **Software**            | v2.2.0        | Minor release — Convention 10 (Standalone Sufficiency Posture), validator C14, SHIP-PREP Phase 3.10, master tests + anti-requirement traps elevated, 2 worked-example retrofits + 4 deferred markers |
| **Design schema**       | v2.0          | Unchanged from v2.0.0 — `ove_OV_Archetype`, `ove_Audience_Target_Reader`, `ove_Audience_Business_Context`, `ove_Audience_Prose_Register` |
| **Design engine**       | v2.2          | v2.2: Convention 10 added to `_meta/CONVENTIONS.md`; master tests + anti-requirement traps elevated in `02-DESIGN-PRINCIPLES.md`; OV-as-specialized-AI-agent paragraph in `01-WHAT-IS-AN-OV.md`; POSTURE-DECLARATION activity in `03-DESIGN-PROTOCOL.md`; Q15 in `04-SCHEMA-DESIGN.md`; REQ-B1/B2/B3 cross-link in `06-STATE-PERSISTENCE.md`; Phase 3.10 in `07-SHIPPING-CHECKLIST.md`; CQ12 in `BOOTSTRAP-NEW-OV.md` |
| **Templates**           | v2.2          | v2.2: four new templates — `TEMPLATE-standalone-sufficiency-posture.md`, `TEMPLATE-posture-yaml.yaml`, `TEMPLATE-vetting-rubric-filled.md`, `TEMPLATE-posture-deferred.yaml` |
| **Substrate**           | v2.2 (rev 1.2) | v2.2: vendored 47-requirement Standalone Sufficiency substrate at `_design-engine/_meta/standalone-sufficiency/` (Loyalty & Retention spec rev 1.2; commerce-neutral OVE surface) |
| **Validator**           | v2.2          | v2.2: C14 (Standalone Sufficiency Posture) added; dispatcher range `range(1, 15)`; prose-mode mirror in `VALIDATION-CHECKLIST.md` |
| **Worked examples**     | v2.2          | Six examples — Negotiation-Preparation and SOLVE-eX-Retrospective retrofit with full posture; LFW, LLL, Relationship-Cultivation, PLC-Retrospective carry `posture-deferred.yaml` (horizon 2026-12-01, scheduled v2.3.0 retrofit) |
| **Release date**        | 2026-06-15    |                                                                        |

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
- **Six worked-example cartridges** (one added in v2.1):
  - `SOLVE-eX-Retrospective/` — retrospective design analysis of [SOLVE-eX](https://github.com/JawnLam/SOLVE-eX) (finite-horizon)
  - `LifeLong-Learning-Retrospective/` — retrospective design analysis of [LifeLong-Learning](https://github.com/JawnLam/LifeLong-Learning) (finite-horizon)
  - `Negotiation-Preparation/` — fresh worked example, anchor demonstration (full depth; finite-horizon)
  - `Long-Form-Writing/` — fresh worked example, lighter depth (finite-horizon)
  - `Relationship-Cultivation/` — fresh worked example, lighter depth (finite-horizon)
  - `Political-Landscape-Cartography-Retrospective/` — **v2.1, canonical practice-archetype demonstration**; retrospective analysis of [Political-Landscape-Cartography v1.0.0](https://github.com/JawnLam/Political-Landscape-Cartography) (private). Shows Q6b three-layer mastery signal, Q14 audience register, Convention 9 sensitive-source pattern, and restrictive LICENSE template applied concretely.
- **`.gitignore`** that keeps a user's private design work out of source control by default while preserving the five shipped worked examples

## Compatibility

- **AI:** any capable assistant (Claude Sonnet/Opus class, GPT-4 class and above, Gemini 2.x and above)
- **OS:** Mac, Windows, Linux
- **Editor:** Obsidian, VS Code, Cursor, Windsurf, Zed, JetBrains, or plain text editors with AI integration
- **Python / network / runtime dependencies:** none (validator uses pure stdlib)

## License

See `LICENSE.md`. OVE itself remains under CC-BY 4.0. The v2.0 release adds a restrictive LICENSE template (`_design-engine/_templates/TEMPLATE-LICENSE-restrictive.md`) for new OVs that need it — OVE itself does not adopt the restrictive license.

Original work by Jawn Lam.
