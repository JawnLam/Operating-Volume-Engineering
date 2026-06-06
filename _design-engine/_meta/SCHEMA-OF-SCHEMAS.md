---
Item_Prototype: Fleeting
Item_ID: ove-meta-schema-of-schemas
Title: "OVE Meta — Schema of Schemas"
Date_Added: 2026-06-01
Date_Modified: 2026-06-06
Needs_Processing: false
type: design-engine
role: meta-ontology
scope: subject-agnostic
updated: 2026-06-01
---

# Schema of Schemas — The Meta-Ontology

> **The recursive structure that makes OVE work. An OV has a schema; OVE has a schema of OV-schemas; and OVE is itself an OV (so its schema is an instance of its own schema). This chapter documents the three-layer ontology and the recursion.**

## The three layers

### Layer 1 — Universals of the OV form

These hold across every OV:

- A `AI-BOOTSTRAP.md` at the root
- A `<purpose>-engine/` folder containing operating prose
- A schema (per cartridge or per OV) defining Prototypes and relationships
- Cartridges representing specific engagements
- State files persisting across sessions
- A bootstrap protocol for new cartridges
- Templates scaffolding the work
- Front-door human-facing docs (README, INSTALL, OPERATOR-GUIDE, CONTRIBUTING)
- License and versioning

These are the **invariants of the OV form**. Any OV that lacks them is either incomplete or not an OV.

### Layer 2 — OV-specific schema

Each OV defines its own:

- Specific Prototypes (concept, case file, design decision, piece, character, stakeholder, etc.)
- Specific relationship vocabulary
- Specific cartridge backbone files
- Specific custom session activities
- Specific state-persistence contract
- Specific naming conventions

Documented in the OV's own `_schema.md` (or `_meta/SCHEMA-OF-SCHEMAS.md` for OVs that have an explicit schema-of-schemas).

### Layer 3 — Instance

Each cartridge and each note inside it. Every instance:

- Declares its prototype via `Item_Prototype:` in YAML frontmatter (or a similar mechanism)
- Conforms to the relevant Layer 2 type definition
- Conforms to Layer 1 universals through inheritance

## The recursion (OVE is an OV about OVs)

OVE is itself an OV. Therefore:

- OVE's Layer 1 universals are the same as every OV's Layer 1 universals (it has `AI-BOOTSTRAP.md`, an engine, cartridges, templates, etc.)
- OVE's Layer 2 schema defines Prototypes specific to designing OVs (design decisions, schema drafts, artifacts-in-progress)
- OVE's Layer 3 instances are the five worked-example cartridges (and any user-created design cartridges)

The recursion produces a useful diagnostic: a well-built OV should be capable of being **redesigned by OVE itself**. If you can't express an OV's design using OVE's design protocol, either:

1. The thing being designed isn't an OV (it's a Custom GPT, a skill, a prompt pack)
2. OVE needs an extension to handle this case (v1.x additive)
3. The design is wrong

This is the **self-similarity test** from `02-DESIGN-PRINCIPLES.md` P9.

## OVE's Layer 2 schema (in brief)

### Prototypes specific to OVE

**Design decision** — a locked choice made during the design of an OV.
- Where: `<Cartridge>/_design-decisions.md`
- Frontmatter: date, decision, alternatives considered, rationale
- Mode: append-only

**Schema draft** — the working draft of the OV-being-designed's schema.
- Where: `<Cartridge>/_schema-draft.md`
- Body: answers to Q1–Q13 from `04-SCHEMA-DESIGN.md`
- Mode: append-friendly with sections

**Artifact draft** — a draft of a shipping file for the OV being designed.
- Where: `<Cartridge>/Artifacts/`
- Mode: append-friendly until shipped, then immutable

**Session log** — a record of one design conversation.
- Where: `<Cartridge>/Sessions/`
- Mode: immutable after creation

### Cartridge backbone

Every OVE cartridge has:

- `_ov-manifest.md` — what OV is being designed, for whom, scope
- `_design-state.md` — current design state (source of truth)
- `_design-decisions.md` — decision log (append-only)
- `_schema-draft.md` — the OV-being-designed's schema in progress
- `Sessions/` — session logs
- `Artifacts/` — drafts of shipping files

### Custom session activities

The six OVE-specific activities (defined in `03-DESIGN-PROTOCOL.md`): INTERVIEW, SCHEMA-DESIGN, CARTRIDGE-SHAPE, ARTIFACT-DRAFT, REVIEW, SHIP-PREP.

## Cross-layer rules

1. **Layer 1 never mentions a specific domain.** The engine is subject-agnostic.
2. **Layer 2 never redefines Layer 1 universals.** A cartridge can't redefine what a session log is.
3. **Layer 3 must conform to Layer 2 where Layer 2 applies.**
4. **Adding a new optional Layer 2 field** is a minor version bump.
5. **Changing Layer 1 universals** is a major version bump.

## Auditing an OV against the meta-ontology

A well-formed OV satisfies:

- [ ] Has all Layer 1 universals
- [ ] Has an explicit Layer 2 schema (`_schema.md` or `_meta/SCHEMA-OF-SCHEMAS.md`)
- [ ] Every cartridge has the required backbone files per Layer 2
- [ ] Every note instance has valid frontmatter per its Layer 3 prototype
- [ ] No domain bleed from Layer 2/3 back into Layer 1 (engine)
- [ ] No dangling wiki-links
- [ ] Cartridges can be moved between users without breaking (substrate-agnostic, P1)

If a cartridge fails audit, it's not ready for study/use. Fix before continuing.

## The version-policy implication

OVE v1.0 freezes its Layer 1 universals and the Layer 2 schema documented above. Any change to:

- Required cartridge backbone files
- Required engine file numbering
- Required Layer 1 file presence

requires a v2.0 major release.

Additive changes:

- New optional cartridge backbone field
- New template
- New worked-example cartridge
- New entry in the failure-modes catalog

are minor releases (v1.x).
