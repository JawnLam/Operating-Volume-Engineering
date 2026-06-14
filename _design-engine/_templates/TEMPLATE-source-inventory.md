---
Item_Prototype: OVE_Source_Inventory
Item_ID: "<ov-slug>-source-inventory"
Title: "<OV Name> — Source Inventory"
Date_Added:
Date_Modified:
Needs_Processing: false
ove_OV_Name: "<OV Name>"
ove_Source_Inventory_Status: drafting   # drafting | inventoried | read-acknowledged | locked
---

# <OV Name> — Source Inventory

> **Captures every external source the OV will cite as substrate. Per CQ3 (`_design-engine/BOOTSTRAP-NEW-OV.md`) and F13 (`_design-engine/_meta/FAILURE-MODES.md`). ARTIFACT-DRAFT cannot begin until every entry has `Canonical location` filled AND `AI-read acknowledgment` filled with a one-line summary per source. SHIP-PREP Phase 3.7 (`_design-engine/07-SHIPPING-CHECKLIST.md`) verifies every citation in shippable content against the sources listed here.**

## How to use this file

1. During CQ3 (`BOOTSTRAP-NEW-OV.md`), the AI asks the operator to enumerate every source the OV will cite as substrate.
2. For each source, the AI fills in the table below — canonical location, page count, full-vs-excerpt status, sensitivity.
3. The AI then **locates and reads** each canonical source. After each read, the AI fills `AI-read acknowledgment` with a substantive one-line summary as proof-of-read.
4. Once every source has been located, classified, and read-acknowledged, the AI sets `ove_Source_Inventory_Status` to `read-acknowledged` and proceeds to ARTIFACT-DRAFT.
5. At SHIP-PREP Phase 3.7, the Citation Audit cross-references every "p.XX / § X.Y / named theorist / verbatim quote" in shippable content against this inventory.
6. On clean Phase 3.7, the status flips to `locked`.

## Sources

### Source 1 — <author year title>

| Field | Value |
|-------|-------|
| **Source identifier** | *e.g., Lam 2018 Pepperdine dissertation, "The Accumulation, Utilization, And Protection of Political Capital"* |
| **Canonical location** | *e.g., /path/to/source.pdf or https://canonical-url. Must be an actual location the AI can access — not "operator's memory" or "Google it."* |
| **Page count / extent** | *e.g., 294 pages — confirmed against publisher's listing* |
| **Full-vs-excerpt status** | *e.g., FULL — confirmed 294 pages match the dissertation's known page count, NOT a Table-3-only excerpt* |
| **Sensitivity** | *Public / Ship-by-reference (Convention 9) / Operator-private* |
| **AI-read acknowledgment** | *One substantive sentence summarizing what the source actually contains, written after the AI has read the canonical text. This becomes the per-source proof-of-read that gates ARTIFACT-DRAFT.* |
| **Verification status** | *Pending / Located-not-read / Read / Verified* |

### Source 2 — <author year title>

*(Duplicate the table above per source. Add as many sources as the OV cites.)*

---

## Inventory gate (ARTIFACT-DRAFT precondition)

ARTIFACT-DRAFT cannot begin until **all** of these are true:

- [ ] Every source has `Canonical location` filled (not `<TBD>`, not "the operator's memory")
- [ ] Every source has `Full-vs-excerpt status` confirmed against the source itself (not against a citation of the source)
- [ ] Every source has `AI-read acknowledgment` filled with a substantive one-line summary
- [ ] `ove_Source_Inventory_Status` in this file's frontmatter set to `read-acknowledged`

`03-DESIGN-PROTOCOL.md` Step 4.5 enforces this gate in the activity-decision algorithm.

## Audit gate (SHIP-PREP precondition)

SHIP-PREP Phase 3.7 (`07-SHIPPING-CHECKLIST.md`) verifies:

- Every "p.XX / § X.Y / named theorist / verbatim quote" in shippable content traces back to a source listed here
- Every cite's content is verifiable against the canonical source (no fabricated "per source X" claims surviving to ship)
- A companion `_citation-audit-log.md` lists each cite with its source and the verification status

`ove_Source_Inventory_Status` flips to `locked` after Phase 3.7 passes.

## Sensitive sources

For any source flagged `Ship-by-reference` (per Convention 9 in `_design-engine/_meta/CONVENTIONS.md`):

- The physical source file (PDF, etc.) stays local in the operator's working copy
- The OV's `.gitignore` excludes the file from version control
- A placeholder `.md` file (`<source-slug>.md`) at the canonical location directs readers to contact the Methodology Author for source access
- `LICENSE.md` (drawn from `_design-engine/_templates/TEMPLATE-LICENSE-restrictive.md` if the OV is restrictive-licensed) acknowledges the sacred-source distinction

Examples:

- A Methodology Author's personal academic dissertation may ship by reference only — operator-private substrate that the OV cites but does not redistribute.
- A published peer-reviewed paper accessible via journal may ship as a citation with the canonical URL — public substrate.
- An internal client report used as the basis for a Sphere cartridge is operator-private — never inventoried into a shipped OV.

## Related references

- `_design-engine/BOOTSTRAP-NEW-OV.md` § CQ3 — the source-capture conversation
- `_design-engine/02-DESIGN-PRINCIPLES.md` P8 — fabrication discipline (the principle this inventory operationalizes)
- `_design-engine/_meta/FAILURE-MODES.md` § F13 — source-grounding skipped (the failure mode this inventory prevents)
- `_design-engine/03-DESIGN-PROTOCOL.md` § Step 4.5 — ARTIFACT-DRAFT gate
- `_design-engine/07-SHIPPING-CHECKLIST.md` § Phase 3.7 — Citation Audit gate
- `_design-engine/_meta/CONVENTIONS.md` § Convention 9 — sensitive source materials ship-by-reference pattern
