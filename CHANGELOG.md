---
Item_Prototype: Fleeting
Item_ID: ove-changelog
Title: "Operating-Volume-Engineering — Changelog"
Date_Added: 2026-06-01
Date_Modified: 2026-06-25
Needs_Processing: false
---

# Changelog

All notable changes to Operating-Volume-Engineering are documented in this file. Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versioning follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.3.0] — 2026-06-25

Minor release introducing **Convention 11 — Knowledge-Augmented OVs**, integrating Google Cloud's **Open Knowledge Format (OKF) v0.1** as an optional, read-only **data plane**. An OV's control plane (engine, lifecycle, rules of engagement) is now cleanly separable from its data plane (curated domain knowledge). Every OV declares `ove_Knowledge_Source`; the default `self_contained` preserves prior behavior exactly. A `knowledge_augmented` OV (KAOV) mounts vendored OKF bundles under `_knowledge/` and retrieves from them at runtime under a new bridge protocol. **Additive over v2.2.0 — no breaking changes** (the new field defaults to `self_contained`, so existing OVs validate and behave unchanged; full validator suite stays green).

### Added — Convention 11 — Knowledge-Augmented OVs (`_meta/CONVENTIONS.md`)

Every OV is structurally capable of mounting an OKF data plane; the default disposition is `self_contained` (empty `Knowledge_Mounts`). A KAOV sets `ove_Knowledge_Source: knowledge_augmented` and declares one or more mounts. Convention 11 requires `ship_disposition: vendored` — the OKF bundle's bytes are copied into the OV under `_knowledge/` and ship with it, so a KAOV remains a self-contained corpus and Convention 10's Absorption story stays intact (the moat is the control-plane discipline + curated/vetted mount, never bare access to the bytes).

### Added — Engine chapter `08-KNOWLEDGE-RETRIEVAL.md` (the OKF bridge)

The bridge protocol — four rules: (1) progressive disclosure (read a directory's `index.md` before any concept beneath it; stricter than OKF, which makes `index.md` optional); (2) workspace isolation (retrieve only from declared mounts); (3) explicit sourcing (every data-plane claim carries an OKF-conformant citation — a file-relative markdown link and/or a `# Citations` entry — F13 extended to the data plane); (4) boot-time re-verification (diff each depended-on concept's `timestamp` / git SHA / `okf_version` against the recorded `pin`; re-confirm on drift).

### Added — OKF v0.1 conformance contract

`_proposals/OKF-conformance-notes.md` distills the binding format facts read directly from the OKF spec **and** its reference implementation ([GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog)): the unit is a **Concept** (addressed by **Concept ID**), reserved filenames (`index.md`, `log.md`), required frontmatter (`type`; the reference validator also requires `title`/`description`/`timestamp`, so OVE producers emit all four), file-relative links, `# Citations` form, and permissive consumption. Two spec-vs-reference-code contradictions are resolved by producing the stricter superset.

### Added — Schema (additive; manifest)

`TEMPLATE-ov-manifest.md` and the `OVE_OV_Manifest` prototype gain `ove_Knowledge_Source` (frontmatter, default `self_contained`) and a `Knowledge_Mounts` array (`bundle_root`, `okf_version`, `provenance`, `ship_disposition: vendored`, `pin`).

### Added — Lifecycle, failure mode, validator

- `03-DESIGN-PROTOCOL.md` — new **KNOWLEDGE-MOUNT** session activity (KAOV-only) + Decision Algorithm Step 4.6; gates ARTIFACT-DRAFT until mounts are vendored, OKF-conformant, and pinned; boot-time re-verification each session.
- `_meta/FAILURE-MODES.md` — **F14** (stale / non-conformant data plane): the F13 vector relocated to the data plane.
- `_meta/validate.py` — **C15** (mount resolution + OKF v0.1 §9 conformance + vendored + pin) and **C16** (data-plane citation form — no `[Source: …]` pseudo-syntax; file-relative links into declared mounts). Dispatcher range `range(1, 17)`; `_proposals` added to the scan-skip set. Prose mirror added to `VALIDATION-CHECKLIST.md`.

### Added — Engine prose + docs

- `01-WHAT-IS-AN-OV.md` — new section "Self-contained vs knowledge-augmented (Convention 11 framing)" + distinguishing property #9.
- `02-DESIGN-PRINCIPLES.md` — KAOV corollary on Trap 9 (a moat that reduces to mount access fails Absorption).
- `README.md` — knowledge-augmented paragraph under "What is an operating volume?".

### Added — Worked example

`Knowledge-Augmented-Demo/` — the Convention 11 dogfood: a `knowledge_augmented` OV mounting one vendored, OKF-conformant bundle (`_knowledge/demo-catalog/`), passing C15/C16 end-to-end.

## [2.2.0] — 2026-06-15

Minor release introducing **Convention 10 — Standalone Sufficiency Posture**: the OVE-side enforcement mechanism for the test "would a general LLM be better for this work than this OV?" The convention vendors a field-agnostic 47-requirement substrate, requires every new OV to declare a posture against it, ships a new validator check (C14), elevates two master tests + ten anti-requirement traps as load-bearing canon, and adds a new SHIP-PREP hard-gate (Phase 3.10). Additive over v2.1.0; no breaking changes.

### Added — Convention 10 — Standalone Sufficiency Posture

Every OV designed via OVE post-v2.2.0 declares a posture against the field-agnostic 47-requirement substrate at `_design-engine/_meta/standalone-sufficiency/`. The substrate's two master tests (Displacement, Absorption) and 10 anti-requirement traps (persona-only OVs, clever-prompt OVs, "smarter-Claude" OVs, epistemic-closure-as-moat, raw-memory-as-permanent-distinction, unqualified privacy claims, being-cheaper, etc.) are now load-bearing canon in `02-DESIGN-PRINCIPLES.md`'s top section. The convention is **commerce-neutral** in OVE's surface — the test applies whether the OV is commercialized or not.

Three required artifacts per OV (root-level):

- `standalone-sufficiency-posture.md` — operator-facing one-pager with tier coverage, T0 dispositions, TG applicability + dispositions, moat commitments, verdict band.
- `_meta/posture.yaml` — source-of-truth registry; per-requirement disposition (met / partial / n-a / deferred), evidence pointer, domain-stakes flag, moat commitments with schema-feature pointers.
- `_meta/vetting-rubric-filled.md` — generated 0–3 scorecard with weighted total (max 558), gating-rule veto outcome, verdict band.

Plus an optional `posture-deferred.yaml` opt-out marker for retrofitting pre-existing OVs.

### Added — Substrate at `_design-engine/_meta/standalone-sufficiency/`

Six vendored files (the upstream Loyalty & Retention Requirements spec, rev 1.2):

- `requirements.yaml` — single source of truth, 47 reqs across 13 categories
- `render.py` — generator script (PyYAML)
- `specialized-agent-requirements.md` — narrative master
- `build-standard.md` — binary-gate view (generated)
- `vetting-rubric.md` — weighted-scorecard view (generated)
- `requirements-registry.csv` — flat dump (generated)
- `README.md` — OVE-specific consumption notes + documented substrate-vs-OVE-surface terminology seam

The substrate retains its original commercial framing ("Loyalty & Retention," "customer," REQ-J4's price-objection wording) because OVE does not modify upstream content. OVE's surface translates to neutral equivalents ("Standalone Sufficiency," "user," generic value-attribution) — seam documented in `_design-engine/_meta/standalone-sufficiency/README.md` and `_design-engine/_meta/CONVENTIONS.md` Convention 10.

### Added — Templates (four new in `_design-engine/_templates/`)

- `TEMPLATE-standalone-sufficiency-posture.md`
- `TEMPLATE-posture-yaml.yaml`
- `TEMPLATE-vetting-rubric-filled.md`
- `TEMPLATE-posture-deferred.yaml`

### Added — Engine prose elevation

- `02-DESIGN-PRINCIPLES.md` — new top section "The two master tests" (Displacement, Absorption) and new section "Anti-requirements OVE refuses to enable" (10 named traps with neutral framing).
- `01-WHAT-IS-AN-OV.md` — new section "An OV is a specialized AI agent (Convention 10 framing)" — explicitly commerce-neutral.
- `03-DESIGN-PROTOCOL.md` — new universal session activity **POSTURE-DECLARATION** (between INTERVIEW and SCHEMA-DESIGN); new Decision Algorithm Step 2.5.
- `04-SCHEMA-DESIGN.md` — new **Q15 — Domain stakes & moat commitments**.
- `06-STATE-PERSISTENCE.md` — new top section explicitly mapping REQ-B1 (T0)/B2/B3 (T2) to state-persistence design.
- `07-SHIPPING-CHECKLIST.md` — new **Phase 3.10 — Standalone Sufficiency readiness** (hard gate, 6 verification steps).
- `BOOTSTRAP-NEW-OV.md` — new **CQ12 — Standalone Sufficiency posture commitments** (early version of Q15).

### Added — Validator C14 (Convention 10)

`_design-engine/_meta/validate.py`:

- New `check_C14_standalone_sufficiency_posture(root, cartridges)` function (per-cartridge, ~300 LOC).
- Module-level constants `T0_REQ_IDS`, `TG_REQ_IDS`, `MOAT_REQ_IDS` mirror substrate definitions.
- Regex-based YAML parsing (validator is pure stdlib; no PyYAML dep). Tolerates both verbose and inline-dict disposition forms in `posture.yaml`.
- Opt-out via `posture-deferred.yaml` short-circuits to info-level finding when `deferred_until` is in the future.
- Dispatcher updated to `range(1, 15)`.

Prose-mode mirror added to `_design-engine/_meta/VALIDATION-CHECKLIST.md` (new "C14 — Standalone Sufficiency posture (Convention 10)" section).

### Retrofit — Two worked examples ship full posture

- `Negotiation-Preparation/` — `domain_stakes: high`. 5/5 T0 + 8/8 TG met. 2 moat commitments (REQ-E4 wargame simulation + REQ-M2 negotiation library as system of record). Weighted 494/558 (88.5%) → Defensible specialist.
- `SOLVE-eX-Retrospective/` — `domain_stakes: high`. 5/5 T0 + 8/8 TG met. 3 moat commitments (REQ-E4 + REQ-M2 + REQ-M3 absorption resistance). Weighted 503/558 (90.1%) → Defensible specialist.

### Deferred — Four worked examples opt out with bounded horizon

`Long-Form-Writing/`, `LifeLong-Learning-Retrospective/`, `Relationship-Cultivation/`, `Political-Landscape-Cartography-Retrospective/` each ship `posture-deferred.yaml` with `deferred_until: 2026-12-01`. v2.2.0 dogfood scope was limited to the two potentially high-stakes worked examples; the remaining four retrofit at v2.3.0 (or extend the horizon with documented reason). C14 returns info-level for deferred OVs, not fail, until the horizon date.

### Changed — Section/phase numbering callouts

- `03-DESIGN-PROTOCOL.md`: activities table renamed from "six" to "seven universal session activities" (POSTURE-DECLARATION added between INTERVIEW and SCHEMA-DESIGN). SCHEMA-DESIGN row updated to reference Q1–Q15 (was Q1–Q8) and SHIP-PREP row references Phase 3.10.
- `04-SCHEMA-DESIGN.md`: Q15 added; the cross-reference table at the bottom of Q15 names Phase 3.10 as the enforcement gate.

### Compatibility

v2.0-built and v2.1-built OVs continue to function as-is. New OVs designed under v2.2.0 must satisfy Convention 10 at SHIP-PREP Phase 3.10. Pre-existing OVs that have not retrofitted may add a `posture-deferred.yaml` opt-out marker with a horizon date to suppress C14 fails temporarily.

---

## [2.1.0] — 2026-06-13

First minor release after v2.0.0 (same day; v2.0 cleared the major-version break, v2.1 adds the practice-archetype dogfood + a validator bug fix + markdown-only fallbacks). Additive over v2.0.0; no breaking changes.

### Added — `Political-Landscape-Cartography-Retrospective/` worked example

OVE's sixth worked-example cartridge and the canonical demonstration of the practice archetype (Q6b in v2.0's Q6 fork). v1.x's five worked examples all map to the finite-horizon archetype; until v2.1 ships, Q6b had specification but no dogfood.

The retrospective documents how Political-Landscape-Cartography v1.0.0 (shipped 2026-06-13, private GitHub, restrictive LICENSE pending IP-attorney review) would have been designed under OVE v2.1's protocol. PLC was the concurrent substrate that motivated v2.0's five packages; v2.1's retrospective sits between PLC v1.0.0 and OVE v2.0.0 as the canonical example.

Six cartridge files:

- `_ov-manifest.md` — full v2.1 manifest with `ove_OV_Archetype: practice`, three `ove_Audience_*` fields populated with PLC's actual register declarations, restrictive-LICENSE acknowledgment
- `_design-state.md` — phase `shipped`; nine retrospective decisions locked
- `_design-decisions.md` — nine decisions reconstructed from PLC v1.0's actual build (D-A-1 archetype, D-A-2 audience register, D-B-1 source inventory, D-B-2 Citation Audit cleared, D-B-3 Worked-Example Slot-ID Verification cleared, D-C-1 Vocabulary Audit cleared with concrete `dashboard` → `conceptual frame` + `dissertation-defined set` → `Nine specific categories` replacements, D-D-1 restrictive LICENSE, D-D-2 Convention 9 sensitive-source pattern applied, D-D-3 IP-attorney review pending)
- `_schema-draft.md` — Q0–Q14 answers, with **Q6b spelled out concretely** as the canonical example of the practice-archetype three-layer mastery signal (L1 per-cycle audit-trail integrity / L2 per-engagement sphere-close retrospective with 9 named contents / L3 per-operator practice longitudinal signals exported, no meta-cartridge in v1.0)
- `_source-inventory.md` — three sources verified, with the Lam 2018 Pepperdine dissertation flagged `Sensitivity: Ship-by-reference (Convention 9)`. Demonstrates the inventory pattern's full structure: identifier, canonical location, page count, full-vs-excerpt status with the documented "Table-3-only excerpt" historical incident, sensitivity classification, AI-read acknowledgment, verification status.
- `Sessions/RETROSPECTIVE.md` — one session log; new `ove_Session_Activity: RETROSPECTIVE` value documented.

### Fixed — `_Prototypes/OVE_Source_Inventory.md` backfilled (v2.0.0 omission)

The v2.0.0 release added `_design-engine/_templates/TEMPLATE-source-inventory.md` and `TEMPLATE-LICENSE-restrictive.md` + `TEMPLATE-sensitive-source-placeholder.md`. The two LICENSE/placeholder templates correctly use `Item_Prototype: Fleeting`, but the source-inventory template declares a new Prototype (`OVE_Source_Inventory`) that needed a corresponding definition file in `_Prototypes/` per Convention 6. v2.0.0 shipped without that definition file; v2.1.0 backfills it as `_Prototypes/OVE_Source_Inventory.md`. The PLC-Retrospective worked example's `_source-inventory.md` (which uses the new Prototype) now resolves cleanly via C7 Prototype-coverage check.

### Fixed — C7 walks design-cartridge `Artifacts/_Prototypes/` (v2.0.0 regression)

`validate.py`'s `_find_prototype_definition()` now also checks `<cartridge>/Artifacts/_Prototypes/<NAME>.md` in addition to the cartridge-local and OV-root paths. This is the OVE design-cartridge layout per `BOOTSTRAP-NEW-OV.md` Step 1 — a design cartridge nests its in-progress OV under `Artifacts/`, and the new OV's Prototype definitions live there during design.

Before v2.1.0, C7 only looked in `<cartridge>/_Prototypes/` and `<root>/_Prototypes/`, so it could not find Prototypes for OVE-design-cartridges with content nested under `Artifacts/`. This produced spurious C7 failures when running the validator against an OVE folder containing operator-private design cartridges (e.g., the PLC design cartridge in the operator's canonical OVE folder).

Search order is now:

1. `<cartridge>/_Prototypes/<NAME>.md` (cartridge-local override)
2. `<cartridge>/Artifacts/_Prototypes/<NAME>.md` (OVE design-cartridge layout — new in v2.1.0)
3. `<root>/_Prototypes/<NAME>.md` (OV-root canonical home)

This is a bug fix, not a behavior change for shipped OVs — finite-horizon worked examples (SOLVE-eX-Retrospective, LFW, etc.) and the new PLC-Retrospective use the cartridge-local pattern (path 1), which was already supported.

### Added — VALIDATION-CHECKLIST.md prose fallbacks for C11/C12/C13

`_design-engine/_meta/VALIDATION-CHECKLIST.md` gains markdown-only operator fallback sections for the three checks added in v2.0.0:

- **C11 — Source inventory completeness.** Prose walkthrough + shell recipe for verifying `_source-inventory.md` presence, status value, no placeholders, and the ARTIFACT-DRAFT vs SHIP-PREP status gates.
- **C12 — Citation audit log.** Prose walkthrough + shell recipe for verifying `_citation-audit-log.md` exists when inventory status is `locked`, and the operator's responsibility to cross-check each cite in shippable content against the audit log.
- **C13 — Vocabulary audit log.** Prose walkthrough + two shell recipes (high-confidence sweep for `dashboard | scorecard | playbook`; broader operator-discretion sweep for `report | framework | tool`). Disposition guidance with concrete role-word replacements (frame, lens, mental map, conceptual frame, capture, log, method, approach, discipline, practice, pattern, move).

Closes the v2.0.0 gap where `validate.py` had the three new checks but markdown-only operators (per v1.1.0's substrate-agnostic commitment) lacked the prose fallback. The "Overall outcome" section now references C1–C13.

### Notes

This release is fully additive. No engine prose modified beyond the new worked example, the C7 patch, and the VALIDATION-CHECKLIST extension. No schema change; no Prototype change; no Convention change.

The PLC-Retrospective is the operationally meaningful addition — it converts v2.0's practice-archetype spec from "spec without dogfood" to "spec + canonical demonstration." Future practice-archetype OV designers walking OVE v2.1+'s protocol can read PLC-Retrospective as the reference implementation, particularly for:

- How to spell out Q6b's three-layer mastery signal concretely (L1 audit-trail integrity criteria; L2 sphere-close retrospective contents; L3 longitudinal signals)
- How to populate the audience register with concrete persona (not "professionals")
- How Convention 9 ship-by-reference works in practice (`.gitignore` + placeholder `.md` + post-push 404 verification)
- How the restrictive LICENSE template's six load-bearing sections actually read

The C7 fix is a bug fix, not a feature addition — operators running `validate.py` against their canonical OVE folder (containing operator-private design cartridges) will see fewer spurious failures.

The VALIDATION-CHECKLIST extension closes a v2.0.0 ship gap that the v2.0 build noticed but punted to v2.0.1.

## [2.0.0] — 2026-06-13

First major release. Codifies the architectural and process lessons surfaced during the v1.0 build of Political Landscape Cartography (PLC) — a practice-archetype OV citing a 294-page dissertation as substrate. Five packages, each fixing a documented v1.x gap that PLC's build either hit or worked around inventively at design time.

**v2.0 is breaking against v1.x in three places:** (a) Q6 framing now forks by archetype, (b) manifest schema adds four new required fields for v2.0-designed OVs (`ove_OV_Archetype` + three `ove_Audience_*` fields), (c) SHIP-PREP gains three new hard-stop phases (3.7 / 3.8 / 3.9). **No runtime impact on already-shipped v1.x OVs** — OVs have no runtime dependency on OVE; v1.x OVs stand alone with their own engine + conventions baked in, and the OVE version that produced them is provenance trivia, not operational metadata. v2.0 changes how the *next* OV gets built.

### Added — Package A: OV Archetype Declaration

A new CQ11 in `BOOTSTRAP-NEW-OV.md` asks the operator whether the OV is **finite-horizon** (defined finish line — manuscript published, subject mastered, problem solved, artifact shipped) or **practice** (no terminal arrival — political navigation, longevity health, relationship cultivation, leadership development). The archetype is logged as `ove_OV_Archetype` in the manifest and shapes Q6 in SCHEMA-DESIGN.

- **`BOOTSTRAP-NEW-OV.md`** — new CQ11 (OV Archetype) after CQ10
- **`_templates/TEMPLATE-ov-manifest.md`** — `ove_OV_Archetype` frontmatter field + `## OV Archetype` body section (with rationale field)
- **`04-SCHEMA-DESIGN.md` § Q6** — forks into **Q6a (finite-horizon: terminal-artifact spec)** and **Q6b (practice: three-layer mastery signal — L1 per-cycle audit integrity / L2 per-engagement retrospective / L3 per-operator practice trajectory)**. Explains why the fork matters with the PLC motivating case.
- **`_templates/TEMPLATE-schema-draft.md`** — Q6 fork rendering for both archetypes
- **`01-WHAT-IS-AN-OV.md`** — new Property 8 (archetype-declared)
- **`02-DESIGN-PRINCIPLES.md` § P6** — extended with two-archetype framing
- **`03-DESIGN-PROTOCOL.md` § Step 2** — interview-not-complete check now includes archetype declaration

**Why this matters.** Pre-v2.0 Q6 implicitly assumed every OV has a terminal artifact. PLC broke that assumption mid-protocol; v2.0 acknowledges that practice-archetype OVs (whose principal's engagement with the domain continues indefinitely) need a different Q6 form to avoid stilted designs.

### Added — Package B: Source Discipline (F13 prevention)

Three structural gates that prevent F2-class fabrication when an OV cites external source material. Replaces the honor-system "say so when unsure" of pre-v2.0 P8 with mechanical enforcement.

- **`_meta/FAILURE-MODES.md` § F13** — Source-grounding skipped. New failure-mode catalog entry documenting the F2 vector specific to source-grounded OVs (fabricated "p.XX" cites, invented structural counts, fabricated worked-example slot-ID mappings, wrong publication metadata). Documents the PLC v1.0 build as the motivating recurrence — multiple fabrications survived the SHIP-PREP gauntlet and only surfaced via operator spot-check.
- **`02-DESIGN-PRINCIPLES.md` § P8** — extended with the v2.0 source-grounding contract: structural capture at CQ3 → ARTIFACT-DRAFT gate at Step 4.5 → SHIP-PREP Phase 3.7 + 3.8.
- **`BOOTSTRAP-NEW-OV.md` § CQ3** — strengthened from "Do you have prior art?" to a structured source-capture conversation. For each named source: identifier, canonical location (where the AI can actually access the full source), page count / extent, full-vs-excerpt status, sensitivity. Logged in `_source-inventory.md`. CQ3 also added to the "Common failure modes" list as F13.
- **`_templates/TEMPLATE-source-inventory.md`** — new template. The inventory file is the substrate for the gates: ARTIFACT-DRAFT cannot begin until every entry has canonical location filled AND the AI has acknowledged reading the canonical source with a one-line summary.
- **`03-DESIGN-PROTOCOL.md` § Step 4.5** — new decision-algorithm step. If `_source-inventory.md` exists and any entry is missing `Canonical location` or `AI-read acknowledgment`, INTERVIEW is proposed (CQ3 incomplete). ARTIFACT-DRAFT is locked.
- **`07-SHIPPING-CHECKLIST.md` § Phase 3.7** — Citation Audit (HARD STOP). Every "p.XX / § X.Y / named theorist / verbatim quote" in shippable content traces back to a source in inventory and verifies against the canonical source. Backed by validator check C11 (source inventory) and C12 (citation audit log).
- **`07-SHIPPING-CHECKLIST.md` § Phase 3.8** — Worked-Example Slot-ID Verification (HARD STOP). Every worked-example reference to a Prototype slot ID (e.g., `<character> → § X.Y.Z <slot-id>`) carries an inline one-line source-justification. Prevents the highest-stakes locus of F13: the worked example, which operators consume as canonical "how to use this OV."

### Added — Package C: Voice + Client Promise

Two new gates that prevent prose-level drift: an audience-register declaration at design time, and a vocabulary audit at ship time.

- **`04-SCHEMA-DESIGN.md` § Q14** — new Audience Register Declaration. The operator specifies three slots: target reader (concrete persona — not "professionals"), business / life context, and prose register (the voice the OV's prose embodies when read aloud, with a concrete analogue). Distinct from CQ9 (which captures AI ↔ operator communication during the *design* conversation); Q14 captures the voice of the *shipped* OV's prose for *its* future operator.
- **`_templates/TEMPLATE-ov-manifest.md`** — three frontmatter fields (`ove_Audience_Target_Reader`, `ove_Audience_Business_Context`, `ove_Audience_Prose_Register`) + `## Audience Register (Q14)` body section
- **`_templates/TEMPLATE-schema-draft.md`** — Q14 section after Q13
- **`07-SHIPPING-CHECKLIST.md` § Phase 3.9** — Vocabulary Audit (HARD STOP). Two-pass sweep: (1) deliverable-promise nouns (dashboard, scorecard, report, framework, tool, playbook) flagged unless the OV ships a real artifact with that name; (2) audience-register violations against the declared `ove_Audience_Prose_Register`. Backed by validator check C13.

**Why this matters.** Without explicit audience-register declaration, OV prose drifts toward the AI's default register (academic, hedged, peer-coded). PLC's 4R coaching script drafted "dissertation-defined set" before the register was explicitly named as "Senior Managing Partner voice; no academic terms at business dinners." PLC also used "dashboard" as a noun in two coaching documents, anchoring a client-expectation the OV didn't ship. Both slipped past pre-v2.0 REVIEW and only surfaced via operator spot-check.

### Added — Package D: Sensitive Sources + Restrictive LICENSE template

Convention 9 codifies the ship-by-reference pattern for sensitive substrate. A new restrictive LICENSE template captures the legal language PLC landed on after multiple rounds of refinement.

- **`_meta/CONVENTIONS.md` § Convention 9** — Sensitive source materials (ship-by-reference). For sources flagged `Ship-by-reference` in `_source-inventory.md`: the physical source stays local, `.gitignore` excludes it at its canonical path, a placeholder `.md` at the canonical location directs readers to contact the Methodology Author, and (if restrictive-licensed) the LICENSE acknowledges the sacred-source distinction. Defense-in-depth (physical exclusion + gitignore + post-push 404 verification) because either alone is brittle.
- **`_templates/TEMPLATE-sensitive-source-placeholder.md`** — new template. The placeholder `.md` that ships in place of the sensitive source file; directs readers to contact the Methodology Author with structured guidance on what to mention and what to expect.
- **`_templates/TEMPLATE-LICENSE-restrictive.md`** — new template. Maximally restrictive license modeled on PLC's: § 1 personal-evaluation 14-day window with 6 limits (application-prohibited, no-sphere-creation, no-reference-during-engagement, no-retention-after-expiration, burden-of-distinction, no-derivative-works); § 2 principal self-coaching ≠ personal evaluation under any circumstance (closing the loophole); § 3 commercial-use authorization required; § 4 Academic Archive Carve-Out (resolves the academic fair-use friction with delete-or-destroy obligations); § 5 sensitive source materials per Convention 9; § 6 automatic termination; § 7 warranty disclaimer; § 8 governing law; § 9 contact. **Prominent IP-attorney review notice at top** — restrictive-template OVs must complete legal review before public release; private GitHub is the default interim posture.
- **`07-SHIPPING-CHECKLIST.md` § Phase 4** — restructured into three paths (Path A: CC-BY 4.0 default; Path B: MIT / Apache; Path C: restrictive with IP-attorney review flag and private-GitHub interim).
- **`BOOTSTRAP-NEW-OV.md` § Step 5 item 12** — references all three LICENSE template paths.

### Added — Validator checks C11, C12, C13

- **`_meta/validate.py`** — three new checks added; `range(1, 11)` → `range(1, 14)`:
  - **C11 — source-inventory-completeness.** Absence of `_source-inventory.md` is info-class. If present: valid `ove_Source_Inventory_Status` value, no unfilled template placeholders, status `read-acknowledged` or `locked` before ARTIFACT-DRAFT.
  - **C12 — citation-audit-log.** If inventory status is `locked`, `_citation-audit-log.md` must exist with substantive content (more than placeholder lines).
  - **C13 — vocabulary-audit-log.** Sweep for high-confidence deliverable-promise nouns (dashboard, scorecard, playbook — broader sweep deferred to operator markdown-grep at Phase 3.9). Hits without `_vocabulary-audit-log.md` recording disposition produce warn-class findings.
- Header docstring updated to document C11 / C12 / C13.
- Run dispatch wires new checks into `run()`.

### Added — Package E: Bookkeeping

- **`VERSION.md`** — bumped to v2.0.0; major-version rationale documented; "Compatibility with v1.x OVs" section confirms v1.x-built OVs do not need migration (OVs have no runtime dependency on OVE).
- **`UPDATE-PROMPT.md`** — updated to acknowledge the v1.x → v2.0 transition. The major-version-transition guidance is now first-class: operators upgrading from v1.x should read this CHANGELOG entry's "v2.0 is breaking" paragraph before running the standard update flow.
- **`CHANGELOG.md`** — this entry.

### Notes

This is the first major release since v1.0 (2026-06-01, twelve days ago). The compressed release cadence reflects the v2.0 substrate: the lessons codified in v2.0 were discovered concurrently with the PLC v1.0 build (the first practice-archetype OV designed via OVE). Rather than ship the lessons as a v1.3 patch and force a later v2.0 break, the v2.0 jump consolidates the breaking changes in one release.

**Vault-Infrastructure dependency:** none. v2.0's manifest schema additions are OV-local; no vault-wide schema cascade required.

**Sibling OV releases:** none coordinated with this release. SOLVE-eX, LFW, LLL all stay on their current v1.x releases — they are finite-horizon OVs that ship under v1.x conventions and do not benefit from v2.0's practice-archetype-specific additions. Adoption of v2.0 conventions in those OVs is at each OV's discretion when they next ship.

**Restrictive LICENSE template — operator action required.** The template includes a prominent IP-attorney review notice. Operators who adopt the restrictive LICENSE for their own OV must complete legal review against their jurisdiction before any public release. The OV may ship to a private GitHub repository during the interim.

## [1.2.1] — 2026-06-07

Adds `UPDATE-PROMPT.md` as the fourth required artifact under Convention 7. The file is a copy-pasteable AI prompt that asks any AI assistant to read the OV's update protocol (`INSTALL.md § Updating` + `OPERATOR-GUIDE.md § Updates and troubleshooting`) and walk the operator through the update step by step, with explicit discipline against destructive commands.

### Added — `UPDATE-PROMPT.md` (fourth Convention 7 artifact)

Sits at the OV root alongside `INSTALL.md`, `OPERATOR-GUIDE.md`, `CONTRIBUTING.md`. Contents:

- A brief explanation of what the file is and how to use it.
- **The prompt block** — copy-pasteable verbatim to any AI assistant (Claude, ChatGPT, Gemini, Cursor, Claude Code, etc.) with read/write access to the OV folder. The prompt instructs the AI to:
  1. Read `INSTALL.md § Updating` and `OPERATOR-GUIDE.md § Updates and troubleshooting`
  2. Run `git fetch` and report incoming commits + the new CHANGELOG entry
  3. Check `git status` and propose a stash strategy if local engine modifications exist
  4. Walk through `git pull --ff-only` step by step; stop and confirm before running
  5. Surface migration recipes, major.minor folder renames, breaking-change notes from the CHANGELOG
  6. Verify Operator-Extension and Operator-Private zones are intact after the update
  7. (For OVE) run the validator and report findings
- A "How to use this file" section for the operator.
- A "When this file is the wrong tool" section (major-version transitions, folder-rename-required releases, fork-and-customize work).
- A "Relationship to other docs" table showing where `UPDATE-PROMPT.md` fits with INSTALL/OPERATOR-GUIDE/CONTRIBUTING/CHANGELOG.

The prompt's discipline:

- Do not modify Operator-Extension or Operator-Private Zone content.
- Do not run destructive commands without explicit operator confirmation (no auto `git reset --hard`, no auto `git clean`, no auto `git checkout --theirs`).
- Stop and ask if anything is unclear or unexpected; don't improvise.

### Added — `_design-engine/_templates/TEMPLATE-UPDATE-PROMPT.md`

The canonical template used to generate per-OV `UPDATE-PROMPT.md` files. New OVs designed via OVE start from this template; the operator fills in the OV's name and customizes per OV-specific concerns (e.g., LFW mentions manuscripts; LLL mentions subjects; SOLVE-eX mentions case files; OVE mentions design cartridges).

### Added — validator check C10 (`UPDATE-PROMPT.md` sanity)

`_design-engine/_meta/validate.py` gains `check_C10_update_prompt_sanity`. Verifies:

- `UPDATE-PROMPT.md` exists at the OV root — missing → **fail**.
- No template placeholders remain (`<OV-Name>`, `<ov-slug>`, `<author>`) — found → **fail**.
- The prompt references `INSTALL.md` and `OPERATOR-GUIDE.md` — missing → **warn**.
- The prompt references the four-zone boundary (`zone`, `four-zone`, or `Operator-Extension`) — missing → **warn**.
- The prompt includes destructive-command-confirmation discipline (`destructive`, `confirm`, `approve`, `stop and ask`) — missing → **warn**.

Wired into `run()` dispatcher and `main()` defaults (`range(1, 11)`).

### Changed — Convention 7 docs, BOOTSTRAP-NEW-OV Step 5, Phase 3.6 gate, VALIDATION-CHECKLIST

- `_meta/CONVENTIONS.md § Convention 7` adds `UPDATE-PROMPT.md` to the "Required artifacts" list with concrete content requirements (OV name filled in, four-zone reference, destructive-command discipline). New subsection "Two update paths" explains the manual path (operator runs the git commands) vs the AI-assisted path (operator delegates via UPDATE-PROMPT.md).
- `_meta/CONVENTIONS.md § Cascade list and verification checklist` add `UPDATE-PROMPT.md` as a required artifact.
- `BOOTSTRAP-NEW-OV.md` Step 5 inserts `UPDATE-PROMPT.md` as item 11 in the artifact draft order, referencing `_templates/TEMPLATE-UPDATE-PROMPT.md` as the source.
- `07-SHIPPING-CHECKLIST.md` Phase 3.6 hard-stop gate adds a `UPDATE-PROMPT.md` check to the artifact list and to the acceptance criteria.
- `_meta/VALIDATION-CHECKLIST.md` gains a § "C10 — UPDATE-PROMPT.md sanity" prose fallback for markdown-only environments.

### Changed — `README.md` links to UPDATE-PROMPT.md

`README.md`'s "For environment setup..." paragraph now includes a reference to `UPDATE-PROMPT.md` for one-shot AI-assisted updates.

### Coordinated multi-OV release

This release ships in parallel with retrofits in the three sibling OVs:

- **LFW v1.7.2** — `UPDATE-PROMPT.md` added at the LFW root, customized for the manuscript domain.
- **LLL v1.3.1** — `UPDATE-PROMPT.md` added at the LLL root, customized for the subject domain.
- **SOLVE-eX v2.1.3** — `UPDATE-PROMPT.md` added at the SOLVE-eX root, customized for the case-files domain.

### Notes

Patch release because the change is purely additive (a new optional artifact) and the underlying Convention 7 contract is otherwise unchanged. No engine prose modified beyond the documentation additions; no schema change; no Prototype change.

The "AI-assisted update" path was already supported informally before this release — any AI session pointed at the existing INSTALL/OPERATOR-GUIDE docs would handle an update on request. `UPDATE-PROMPT.md` makes this path first-class: the operator opens one file, copies one prompt, pastes once, and approves the AI's proposed steps. Lower friction for routine updates.

## [1.2.0] — 2026-06-06

Codifies the install-and-update contract that v1.0 and v1.1 left implicit. Every OV designed via OVE will now ship a documented install pattern (Convention 7) and a documented engine-vs-operator boundary (Convention 8). The retrofit across the OV ecosystem (LFW v1.7.1, LLL v1.3.0, SOLVE-eX v2.1.2) ships in parallel.

### Added — Convention 7: install-and-update pattern

Every OV ships a copy-pasteable install snippet that produces a git-trackable working copy on the operator's machine. The pattern enables `git pull` updates while protecting against accidental publishing of operator-private work.

- **Default install** = `git clone <upstream>` + immediate `git remote set-url --push origin DISABLED_TO_PREVENT_ACCIDENTAL_PUSH_OF_PERSONAL_WORK`. Fetch stays enabled (so updates work); push is locked (so personal design work can't leak upstream).
- **Update workflow** = `git fetch && git log --oneline HEAD..origin/main && git pull --ff-only`; stash → pull → pop fallback for when local engine edits would conflict.
- **Folder naming** = `<OV-Name>-v<major>.<minor>`. New major.minor releases prompt a folder rename so old and new can briefly coexist during transitions.
- **Contributing back** = re-enable push to your own fork (never upstream), then re-disable when done.
- **Required artifacts per OV:** `INSTALL.md` with the install snippet wired to the concrete GitHub URL; `OPERATOR-GUIDE.md § "Updates and troubleshooting"` with the update workflow plus stash-pop conflict guidance; `README.md § "Install"` linking to `INSTALL.md`.

Documented in `_design-engine/_meta/CONVENTIONS.md § Convention 7`. OVE itself dogfoods: see this release's `INSTALL.md § 1`, `OPERATOR-GUIDE.md § 9 — Updates and troubleshooting`.

### Added — Convention 8: engine vs operator-content boundary

Every OV explicitly declares **four content zones**. The boundary lets `git pull` update the engine without disturbing operator work and lets the operator extend the OV without fearing the next pull.

- **Engine Zone** — release-owned; updated by `git pull` (front-door docs, `_<purpose>-engine/`, `_Prototypes/`, `_USER.md.template`, `.gitignore`)
- **Operator-Private Zone** — gitignored; never tracked (`_USER.md`, per-cartridge state files, session logs, IDE caches)
- **Operator-Extension Zone** — operator-created; survives `git pull` (operator's own cartridges parallel to shipped examples)
- **Shipped Examples Zone** — release-owned; updated by `git pull` (the worked-example cartridges)

Required artifacts per OV: `CONTRIBUTING.md § "Content zones"` enumerating all four zones with concrete path patterns; `.gitignore` containing the Operator-Private patterns with inline comments; `OPERATOR-GUIDE.md § "Engine vs your work"` explaining the boundary; `README.md § "What is in this folder"` linking to the zone declaration.

Documented in `_design-engine/_meta/CONVENTIONS.md § Convention 8`. OVE itself dogfoods: see this release's `CONTRIBUTING.md § 6`, `OPERATOR-GUIDE.md § 8`.

### Added — validator checks C8 (zone-boundary docs) + C9 (`.gitignore` sanity)

- **C8** scans `CONTRIBUTING.md` (with `OPERATOR-GUIDE.md` as fallback) for the four canonical zone-name strings. All four present → pass; some → warn with the missing names; none → fail. Operator-chosen synonyms can be accommodated by documenting the synonym choice in `_design-decisions.md` and running `validate.py --skip=C8`.
- **C9** verifies `.gitignore` exists at the OV root and contains at least one substantive (non-comment, non-blank) pattern. Missing → fail; empty/comment-only → warn; non-empty → pass.

Wired into `validate.py`'s dispatcher and `main()` defaults (`range(1, 10)`). `VALIDATION-CHECKLIST.md` extended with prose fallbacks for C7, C8, C9.

### Added — Phase 3.6 ship gate

`07-SHIPPING-CHECKLIST.md` gains a new hard-stop **Phase 3.6 — Convention 7/8 readiness**. Verifies that `INSTALL.md` has a concrete GitHub URL (no placeholders), `OPERATOR-GUIDE.md` has the four-zone explanation and the update workflow with stash-pop fallback, `CONTRIBUTING.md` has all four zone names with concrete patterns, and `.gitignore` has substantive patterns. Phase 7 (git init / push) is locked until this gate is clean.

### Added — INSTALL/OPERATOR-GUIDE/CONTRIBUTING/BOOTSTRAP-NEW-OV updates

OVE itself adopts every Convention 7 and Convention 8 artifact:

- `INSTALL.md` rewritten with § 1 (canonical git-clone-with-push-disabled install), § 1a (alternative no-git install), and § 7 (update workflow with stash-pop fallback).
- `OPERATOR-GUIDE.md` gains § 8 (Engine vs your work — four zones, Convention 8) and § 9 (Updates and troubleshooting — clean fast-forward, conflict resolution, major.minor folder transition, contributing back).
- `CONTRIBUTING.md` gains § 6 (Content zones — all four zones with concrete path patterns per zone for OVE).
- `BOOTSTRAP-NEW-OV.md` Step 5 lists `INSTALL.md`, `OPERATOR-GUIDE.md`, `CONTRIBUTING.md`, `.gitignore` as load-bearing artifacts and names Convention 7/8 as the gate; a new Convention 7/8 artifact-readiness check precedes SHIP-PREP.

### Coordinated multi-OV release

This release ships in parallel with retrofits in the three sibling OVs to bring them into Convention 7/8 conformance:

- **LFW v1.7.1** — fixes the stale `.gitignore` `Atoms/`→`Items/` patterns missed in v1.7.0, adds Convention 7 install snippet to `INSTALL.md`, adds Convention 8 § "Content zones" to `CONTRIBUTING.md`.
- **LLL v1.3.0** — adds `INSTALL.md` (Convention 7 install snippet), `CONTRIBUTING.md § "Content zones"` (Convention 8 four zones), `.gitignore`. The minor bump reflects that v1.2 shipped without these artifacts and v1.3 makes Convention 7/8 conformance a first-class feature.
- **SOLVE-eX v2.1.2** — adds Convention 7 install snippet to `INSTALL.md`, Convention 8 § "Content zones" to `CONTRIBUTING.md`. Working OV push remote also flipped to `DISABLED_TO_PREVENT_ACCIDENTAL_PUSH_OF_PERSONAL_WORK` to match the OVE/LFW pattern.

### Notes

This release is fully additive — no engine prose removed, no schema changes, no breaking architectural changes. The two new conventions formalize patterns that LFW and OVE were already informally following; LLL and SOLVE-eX needed the retrofit to come into compliance.

The Phase 3.6 ship gate is intentionally a hard-stop: shipping an OV without an install-and-update story or a documented zone boundary is shipping an OV that operators can't safely use. The gate is non-negotiable.

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
