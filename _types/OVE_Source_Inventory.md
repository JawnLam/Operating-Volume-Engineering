---
Item_ID: "UUID-OR-SLUG"
type: OVE_Source_Inventory
title: "<OV Name> — Source Inventory"
ove_OV_Name: ""
ove_Source_Inventory_Status: drafting
Date_Added:
Date_Modified:
Needs_Processing: false
AI_Instructions: ""
---

# <OV Name> — Source Inventory

> **Captures every external source the OV-being-designed will cite as substrate. Per CQ3 (`_design-engine/BOOTSTRAP-NEW-OV.md`) and F13 (`_design-engine/_meta/FAILURE-MODES.md`). ARTIFACT-DRAFT cannot begin until every entry has `Canonical location` filled AND `AI-read acknowledgment` filled. SHIP-PREP Phase 3.7 (`_design-engine/07-SHIPPING-CHECKLIST.md`) verifies every citation against this inventory. Added in OVE v2.0.**

## Status values

- `drafting` — sources being enumerated; not yet fully captured
- `inventoried` — every source has identifier, canonical location, page count, full-vs-excerpt status, sensitivity filled
- `read-acknowledged` — AI has read each canonical source and filled `AI-read acknowledgment` with a substantive one-line summary (ARTIFACT-DRAFT can proceed)
- `locked` — SHIP-PREP Phase 3.7 Citation Audit cleared; `_citation-audit-log.md` exists with one entry per cite (Phase 7 can proceed)

## Sources

### Source N — `<author year title>`

| Field | Value |
|-------|-------|
| **Source identifier** | author + year + title |
| **Canonical location** | actual file path or URL where the AI can access the full canonical text |
| **Page count / extent** | page count, or extent description for non-paginated sources |
| **Full-vs-excerpt status** | FULL / EXCERPT (with the gap described if EXCERPT) |
| **Sensitivity** | Public / Ship-by-reference (Convention 9) / Operator-private |
| **AI-read acknowledgment** | one-line summary of what the source contains, written after the AI has read the canonical text |
| **Verification status** | Pending / Located-not-read / Read / Verified |

## Related references

- `_design-engine/_templates/TEMPLATE-source-inventory.md` — the template new OVs copy
- `_design-engine/BOOTSTRAP-NEW-OV.md` § CQ3 — the source-capture conversation
- `_design-engine/02-DESIGN-PRINCIPLES.md` § P8 — fabrication discipline
- `_design-engine/_meta/FAILURE-MODES.md` § F13 — source-grounding skipped
- `_design-engine/03-DESIGN-PROTOCOL.md` § Step 4.5 — ARTIFACT-DRAFT gate
- `_design-engine/07-SHIPPING-CHECKLIST.md` § Phase 3.7 — Citation Audit gate
- `_design-engine/_meta/CONVENTIONS.md` § Convention 9 — sensitive source materials ship-by-reference pattern
