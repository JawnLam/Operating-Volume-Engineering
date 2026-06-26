---
Item_ID: "UUID-OR-SLUG"
type: OVE_OV_Manifest
title: "<OV Name> — Design Cartridge Manifest"
ove_OV_Name: ""
ove_OV_Slug: ""
ove_Design_Phase: interview
ove_User_Name: ""
ove_Bootstrapped:
ove_Engagement_Kind: ""
ove_Knowledge_Source: self_contained   # self_contained (default) | knowledge_augmented — Convention 11
Date_Added:
Date_Modified:
Needs_Processing: false
AI_Instructions: ""
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

`ove_Knowledge_Source` above is `self_contained` (default) or `knowledge_augmented`. Self-contained OVs leave `Knowledge_Mounts` empty. Knowledge-augmented OVs (KAOVs) vendor one or more OKF v0.1 bundles under `_knowledge/` and declare one entry each below. See `_design-engine/08-KNOWLEDGE-RETRIEVAL.md` and `_design-engine/_meta/CONVENTIONS.md` § Convention 11.

```yaml
Knowledge_Mounts: []   # self-contained default
# Knowledge_Mounts:
#   - bundle_root: _knowledge/<bundle-slug>   # vendored OKF bundle under the OV root
#     okf_version: "0.1"                       # OKF spec version the bundle targets
#     provenance: "<where this bundle came from + how it was vetted>"
#     ship_disposition: vendored               # bytes ship with the OV (Convention 11 requires this)
#     pin:
#       git_sha: "<commit the bundle was vetted at, if sourced from git>"
#       vetted_timestamp: "<ISO 8601 — boot-time re-verification baseline>"
```

## Notes

*Anything else a fresh AI session would need to calibrate.*
