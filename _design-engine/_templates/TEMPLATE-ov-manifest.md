---
type: OVE_OV_Manifest
Item_ID: "<ov-slug>-manifest"
title: "<OV Name> — Design Cartridge Manifest"
Date_Added:
Date_Modified:
Needs_Processing: false
ove_OV_Name: "<OV Name>"
ove_OV_Slug: "<ov-slug>"
ove_OV_Archetype: ""           # finite_horizon | practice (per CQ11; shapes Q6 in SCHEMA-DESIGN)
ove_Audience_Target_Reader: ""      # Q14 — concrete persona of the OV's intended user
ove_Audience_Business_Context: ""   # Q14 — context the reader is in when consulting the OV
ove_Audience_Prose_Register: ""     # Q14 — voice the OV's prose embodies
ove_Design_Phase: interview   # interview | schema-design | cartridge-shape | artifact-draft | review | ship-prep | shipped
ove_User_Name: ""              # operator-confirmed; never inferred from indirect signals
ove_Bootstrapped: <YYYY-MM-DD>
ove_Knowledge_Source: self_contained   # self_contained (default) | knowledge_augmented — Convention 11
---

# <OV Name> — Design Cartridge Manifest

## What this OV is

*One or two paragraphs. Domain, scope, intended use. Tight.*

## Why this user is designing it

*The motivating need. What's broken or missing in the current state of the work.*

## Who is this for

- [ ] Self only
- [ ] Self + a few collaborators
- [ ] Public release

## Domain shape

Q1 categories from `_design-engine/04-SCHEMA-DESIGN.md`:

- [ ] Formal/propositional
- [ ] Conceptual
- [ ] Procedural
- [ ] Declarative/factual
- [ ] Experiential
- [ ] Creative/interpretive
- [ ] Decisional
- [ ] Relational
- [ ] Operational

## Cadence

*How often will this OV be used? Daily / weekly / episodic / once-per-event?*

## Multi-session evidence

*Why this needs to be an OV rather than a Custom GPT / skill / prompt pack. Specifically: what state needs to persist across sessions?*

## Output target

*What deliverables does this OV produce? Synthesis pieces? Decision documents? Performance records? Ship-able artifacts?*

## OV Archetype

Per CQ11 (`_design-engine/BOOTSTRAP-NEW-OV.md`):

- [ ] **Finite-horizon** — the work has a defined finish line (manuscript published, subject mastered, problem solved, artifact shipped). Q6 (`_design-engine/04-SCHEMA-DESIGN.md`) is answered as a terminal-artifact spec.
- [ ] **Practice** — the work has no terminal arrival; the principal's engagement with the domain continues indefinitely. Q6 is answered as a three-layer mastery signal (per-cycle audit integrity / per-engagement retrospective / per-operator practice trajectory).

*Rationale for the choice:*

## Audience Register (Q14)

Per Q14 (`_design-engine/04-SCHEMA-DESIGN.md`). Distinct from the AI ↔ operator communication preferences in `## Communication preferences` below (CQ9) — this section captures the voice of the *shipped* OV's prose for *its* future operator.

- **Target reader:** *Concrete persona. Not "professionals" or "executives." Examples: "COO of $20B+ market-cap public company aspiring to CEO within five years"; "Self-directed adult learner working through a specialist subject without a teacher."*
- **Business / life context:** *Context the reader is in when consulting the OV — business engagement with senior client, alone with a personal problem, coaching conversation with a peer, preparing for a board meeting, etc.*
- **Prose register:** *The voice the OV's prose embodies when read aloud — e.g., "Senior Managing Partner at a global strategy consultancy speaking to a peer — direct, substantive, no flattery, no academic jargon at business dinners."*

The Audience Register cascades into every ARTIFACT-DRAFT (engine prose, templates, worked examples). SHIP-PREP Phase 3.9 (Vocabulary Audit) verifies shippable prose against this declaration.

## Prior art / existing material to incorporate

*Existing notes, frameworks, methods (in the proper sense), prior systems.*

## Stakes and safety

*High-stakes outcomes? Irreversible decisions? Need for professional-escalation routing?*

## Communication preferences

Defaults (override if needed):

- **Register:** peer
- **Critique style:** substantive
- **Hedging:** minimal
- **Filler tolerance:** none

## Scope boundaries

*Anything explicitly out of scope for this OV.*

## Knowledge mounts (Convention 11)

Most OVs are `self_contained` — all knowledge is baked into the corpus at design time (the F13 source pipeline) and `Knowledge_Mounts` stays empty. Set `ove_Knowledge_Source: knowledge_augmented` only if this OV mounts an external **OKF v0.1** knowledge bundle as a read-only data plane. Convention 11 requires mounts to be **vendored** — the bundle is copied under `_knowledge/` and ships with the OV, so self-containment is preserved. See `_design-engine/08-KNOWLEDGE-RETRIEVAL.md` for the bridge protocol and `_design-engine/_meta/OKF-conformance-notes.md` for the OKF format contract.

```yaml
Knowledge_Mounts: []   # self-contained default; leave empty unless knowledge_augmented
# Knowledge_Mounts:
#   - bundle_root: _knowledge/<bundle-slug>   # vendored OKF bundle under the OV root
#     okf_version: "0.1"                       # OKF spec version the bundle targets
#     provenance: "<source of the bundle + how/when it was vetted>"
#     ship_disposition: vendored               # required by Convention 11 — bytes ship with the OV
#     pin:
#       git_sha: "<commit the bundle was vetted at, if from git>"
#       vetted_timestamp: "<ISO 8601 — boot-time re-verification baseline>"
```

## Notes

*Anything else a fresh AI session would need to calibrate.*
