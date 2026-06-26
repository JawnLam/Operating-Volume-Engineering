---
type: Fleeting
timestamp: "2026-06-25T00:00:00Z"
Item_ID: ove-version
title: "Operating-Volume-Engineering — Version"
Date_Added: 2026-06-01
Date_Modified: 2026-06-25
Needs_Processing: false
ove_Version: "2.4.0"
schema_version: "2.0"
schema_status: "STABLE"
release_date: 2026-06-25
release_phase: "Minor release — Convention 11 (Knowledge-Augmented OVs): every OV declares ove_Knowledge_Source (self_contained default | knowledge_augmented). A knowledge_augmented OV (KAOV) mounts one or more vendored OKF v0.1 bundles as a read-only data plane under _knowledge/, retrieved at runtime under the bridge protocol (new engine chapter 08-KNOWLEDGE-RETRIEVAL.md): progressive disclosure, workspace isolation, explicit OKF-conformant sourcing, boot-time re-verification. New lifecycle activity KNOWLEDGE-MOUNT (03-DESIGN-PROTOCOL Step 4.6); new failure mode F14 (stale/non-conformant mount); new validator checks C15/C16. New dogfood cartridge Knowledge-Augmented-Demo. Additive over v2.2.0 — ove_Knowledge_Source defaults to self_contained, so existing OVs are unaffected; no breaking changes."
---

# Operating-Volume-Engineering — Version

This is Operating-Volume-Engineering **v2.4.0** — minor release bringing the engine into **Google OKF v0.1 conformance**. **Convention 1's Universal Core is renamed to OKF-native field names** (`Item_Prototype`→`type`, `Title`→`title`, `Tags`→`tags`; added `timestamp` derived from `Date_Modified`, plus optional `description`/`resource`), mirroring vault Master_Schema v1.23.0 — **so every OV designed via OVE now emits OKF-compliant items by default.** Convention 6's per-OV folder is renamed `_Prototypes/`→`_types/` (vocabulary consistency with the `type` discriminator); the validator (`C7`) and all engine docs follow. `Date_Modified` is kept and time-synced with `timestamp`. Hugo (`hugo_*`) remains excluded and untouched. The OVE corpus itself (93 notes + 24 prototypes) was migrated; `validate.py` updated to key on `type`/`_types`. This is the OVE half of the coordinated OKF release (vault done in schema v1.23.0; LFW/LLL/SOLVE-eX/PLC migrate in parallel).

### Prior: v2.3.0

v2.3.0 was a minor release introducing **Convention 11 — Knowledge-Augmented OVs**, integrating Google Cloud's **Open Knowledge Format (OKF) v0.1** as an optional, read-only **data plane**. Every OV now declares `ove_Knowledge_Source`; the default is `self_contained` (all knowledge baked into the corpus, the v2.0 F13 pipeline). An OV may instead be `knowledge_augmented` (a KAOV): it mounts one or more **vendored** OKF bundles under `_knowledge/` and retrieves from them at session runtime under the bridge protocol in the new engine chapter `08-KNOWLEDGE-RETRIEVAL.md` (progressive disclosure, workspace isolation, OKF-conformant explicit sourcing, boot-time re-verification). The release adds the `KNOWLEDGE-MOUNT` lifecycle activity, failure mode `F14`, validator checks `C15`/`C16`, and a dogfood worked example (`Knowledge-Augmented-Demo`). Because mounts are vendored, a KAOV remains a self-contained corpus. The change is **additive** over v2.2.0 — `ove_Knowledge_Source` defaults to `self_contained`, so existing OVs validate and behave unchanged.

## Version identifiers

| Identifier              | Value         | Notes                                                                  |
|-------------------------|---------------|------------------------------------------------------------------------|
| **Software**            | v2.3.0        | Minor release — Convention 11 (Knowledge-Augmented OVs / OKF data plane), engine chapter 08, KNOWLEDGE-MOUNT activity, F14, validator C15/C16, dogfood KAOV cartridge. Additive over v2.2.0 |
| **Design schema**       | v2.0          | Unchanged required set from v2.0.0. v2.3 adds the additive, defaulted field `ove_Knowledge_Source` (`self_contained` default) + the `Knowledge_Mounts` array (empty unless `knowledge_augmented`) — no breaking change |
| **Design engine**       | v2.3          | v2.3: Convention 11 added to `_meta/CONVENTIONS.md`; new chapter `08-KNOWLEDGE-RETRIEVAL.md`; self-contained-vs-knowledge-augmented framing in `01-WHAT-IS-AN-OV.md`; KAOV moat corollary in `02-DESIGN-PRINCIPLES.md`; KNOWLEDGE-MOUNT activity + Step 4.6 in `03-DESIGN-PROTOCOL.md`; F14 in `_meta/FAILURE-MODES.md` |
| **Templates**           | v2.3          | v2.3: `TEMPLATE-ov-manifest.md` + `OVE_OV_Manifest` prototype gain `ove_Knowledge_Source` + `Knowledge_Mounts` |
| **Substrate**           | v2.2 (rev 1.2) | Unchanged — vendored 47-requirement Standalone Sufficiency substrate at `_design-engine/_meta/standalone-sufficiency/` |
| **OKF integration**     | OKF v0.1      | v2.3: KAOVs vendor OKF v0.1 bundles ([GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog)); binding format contract distilled at `_proposals/OKF-conformance-notes.md` |
| **Validator**           | v2.3          | v2.3: C15 (Knowledge-mount conformance) + C16 (data-plane citation form) added; dispatcher range `range(1, 17)`; `_proposals` added to skip set; prose-mode mirror in `VALIDATION-CHECKLIST.md` |
| **Worked examples**     | v2.3          | Seven examples — six unchanged from v2.2 plus `Knowledge-Augmented-Demo` (the Convention 11 dogfood: one vendored OKF bundle, passes C15/C16) |
| **Release date**        | 2026-06-25    |                                                                        |

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
  - Nine core operating files (`00–08`) plus `BOOTSTRAP-NEW-OV.md` (v2.3 adds `08-KNOWLEDGE-RETRIEVAL.md`, the OKF bridge protocol)
  - Templates for every standard OV-ship file (`_templates/`) — v2.3 extends the manifest template with the data-plane fields
  - Schema-of-schemas + failure-modes catalog (`_meta/`) — v2.3 adds F14; Convention 11 in `CONVENTIONS.md`
  - Validator (`_meta/validate.py`) — v2.3 adds C15 / C16
- **Front-door docs at the root**: `README`, `AI-BOOTSTRAP`, `INSTALL`, `OPERATOR-GUIDE`, `CONTRIBUTING`, `LICENSE`, `VERSION`, `CHANGELOG`, `UPDATE-PROMPT`
- **Optional user profile template**: `_USER.md.template`
- **Seven worked-example cartridges** (one added in v2.1; `Knowledge-Augmented-Demo` added in v2.3 as the Convention 11 dogfood — a `knowledge_augmented` OV mounting one vendored, OKF-conformant bundle under `_knowledge/demo-catalog/`):
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
