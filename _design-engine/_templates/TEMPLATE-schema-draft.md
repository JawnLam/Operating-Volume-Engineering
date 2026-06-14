---
Item_Prototype: OVE_Schema_Draft
Item_ID: "<ov-slug>-schema-draft"
Title: "<OV Name> — Schema Draft"
Date_Added:
Date_Modified:
Needs_Processing: false
ove_OV_Name: "<OV Name>"
ove_Schema_Status: drafting    # drafting | locked | shipped
---

# <OV Name> — Schema Draft

> **The working draft of the OV-being-designed's schema. Answers to Q1–Q13 from `_design-engine/04-SCHEMA-DESIGN.md`. Updated across SCHEMA-DESIGN sessions; locked when status flips to `locked` in frontmatter.**

## Q1 — Kinds of knowledge or work

*To be answered.*

## Q2 — Canonical authorities

*To be answered.*

## Q3 — Smallest unit

*To be answered.*

## Q4 — Relationships between Items

*To be answered.*

## Q5 — Natural progression

*To be answered.*

## Q6 — Mastery / completion endpoint

**This question forks based on the OV's archetype (CQ11 in `BOOTSTRAP-NEW-OV.md`, manifest field `ove_OV_Archetype`). Confirm archetype before answering. See `04-SCHEMA-DESIGN.md` § Q6 for the fork specification.**

### If archetype = finite-horizon (Q6a)

*Terminal-artifact spec. To be answered: what observable artifact, demonstrated behavior, or measurable outcome signals "done"?*

### If archetype = practice (Q6b)

*Three-layer mastery signal. To be answered:*

- **L1 — Per-cycle audit-trail integrity:** *(what discipline check fires per cycle?)*
- **L2 — Per-engagement retrospective contents:** *(what the engagement-close deliverable contains)*
- **L3 — Per-operator practice longitudinal signals exported at engagement-close:** *(what cross-engagement quantities are exported as structured data)*
- **Meta-cartridge decision:** *(structured-export-only — recommended default — vs ship a per-operator aggregate meta-cartridge)*

## Q7 — Custom session activities

*To be answered. If none beyond a standard set, say so.*

## Q8 — Mastery scale

*To be answered. Default 0–5 or custom.*

## Q9 — What does a cartridge represent?

*To be answered.*

## Q10 — Cartridge backbone files

*To be answered. List the minimum set of files every cartridge has.*

## Q11 — State-persistence contract

*To be answered. Per file: mode (A/B/C/D/E per `06-STATE-PERSISTENCE.md`), owner, read-at, written-at.*

## Q12 — Templates list

*To be answered. What ships in `_<purpose>-engine/_templates/`.*

## Q13 — Bootstrap-new-cartridge protocol

*To be answered. The CQ-style questions the AI asks to open a new cartridge in this OV.*

## Q14 — Audience register declaration

*Per Q14 in `_design-engine/04-SCHEMA-DESIGN.md`. Cascades into every ARTIFACT-DRAFT; verified at SHIP-PREP Phase 3.9 (Vocabulary Audit).*

- **Target reader:** *concrete persona of the OV's intended user*
- **Business / life context:** *context the reader is in when consulting the OV*
- **Prose register:** *voice the OV's prose embodies, with at least one concrete analogue (e.g., "Senior Managing Partner at a global strategy consultancy")*

---

## Derived schema documents

When Q1–Q13 are answered, derive:

### Prototype definitions

*One per Q3-defined unit type. Frontmatter, required body sections, naming, location.*

### Relationship vocabulary

*Table of named relations from Q4.*

### Folder structure

*Where Items live within a cartridge.*
