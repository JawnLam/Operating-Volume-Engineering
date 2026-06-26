---
type: OVE_Source_Inventory
timestamp: "2026-06-13T00:00:00Z"
Item_ID: "plc-retrospective-source-inventory"
title: "Political-Landscape-Cartography — Source Inventory (Retrospective)"
Date_Added: 2026-06-13
Date_Modified: 2026-06-13
Needs_Processing: false
ove_OV_Name: "Political-Landscape-Cartography"
ove_Source_Inventory_Status: locked
---

# Political-Landscape-Cartography — Source Inventory (Retrospective)

> **Retrospective source inventory for PLC v1.0.0. Demonstrates the v2.1 source-inventory pattern (`_design-engine/_templates/TEMPLATE-source-inventory.md`) applied to PLC's three substrate sources. Status `locked` because PLC v1.0.0 shipped with a clean Citation Audit (Phase 3.7) and Worked-Example Slot-ID Verification (Phase 3.8). The historical incidents that motivated v2.0's Source Discipline package are documented in `_design-decisions.md` D-B-2 / D-B-3.**

## Sources

### Source 1 — Lam 2018 Pepperdine dissertation

| Field | Value |
|-------|-------|
| **Source identifier** | Lam, Cong "Jawn" (2018). *The Accumulation, Utilization, And Protection of Political Capital.* Doctoral dissertation, Pepperdine University, Graziadio Business School. |
| **Canonical location** | Operator-local: `/Users/jawnlam/Obsidian/VGer/Deep Thought 42/Operating Volumes (in use)/Political-Landscape-Cartography-v1.0/_frameworks/sources/Lam-2018-Pepperdine.pdf`. Methodology Author retains canonical control. |
| **Page count / extent** | 294 pages — confirmed against the canonical PDF (full document, not Table-3-only excerpt). |
| **Full-vs-excerpt status** | FULL — confirmed against the Methodology Author's records. The historical incident: during the v1.0 build, a Downloads-folder copy was discovered to be a 17-page Table-3-only excerpt rather than the full 294-page dissertation. The full version was located via broad disk search and is the canonical source. |
| **Sensitivity** | Ship-by-reference (Convention 9). Physical PDF stays local; `.gitignore` excludes from PLC's GitHub repository; placeholder `.md` at `_frameworks/sources/Lam-2018-Pepperdine.md` directs readers to contact the Methodology Author for access. Sacred to the Methodology Author. |
| **AI-read acknowledgment** | The dissertation operationalizes a theory of political capital: capital accumulates via control of resources that enable further resource control (recursive thesis); is spent on tactical moves that shift other actors' decision matrices via Option Affected × Consideration Affected × Effect on Component; sustained competence over many cycles ("adapt") is the only kind of strategic skill that compounds. Substrate for the 9-type resource taxonomy, Table 3 tactical move catalogue (~100 moves), the ADAPT Loop coaching framework, and the OPC Assessment v3.0 sphere diagnostic. |
| **Verification status** | Verified — every PLC v1.0.0 cite was Phase 3.7 Citation-Audited against this canonical source. The full audit log is in PLC's own repository at `_citation-audit-log.md`. |

### Source 2 — ADAPT Loop Field Manual

| Field | Value |
|-------|-------|
| **Source identifier** | Lam, Cong "Jawn" — *ADAPT Loop Field Manual.* Operationalization of the dissertation's coaching protocol. |
| **Canonical location** | `/Users/jawnlam/Obsidian/VGer/Deep Thought 42/Operating Volumes (in use)/SOLVE-eX-v2.1/10-Reference/ADAPT-Loop-Field-Manual.pdf` (within the SOLVE-eX OV; Methodology Author's prior work). |
| **Page count / extent** | Operational manual — multiple pages; full text consulted. |
| **Full-vs-excerpt status** | FULL |
| **Sensitivity** | Public — the ADAPT Loop is the Methodology Author's published framework, available via the linked SOLVE-eX OV. |
| **AI-read acknowledgment** | The ADAPT Loop is a five-beat cycle protocol — Agenda / Decide / Act / Perceive / Track — for political decision discipline. Each beat is a cycle constituent. Multiple cycles compound across an engagement. *"Sustained competence over many cycles is the only kind of strategic skill that compounds"* is the foreword's substrate claim and the motivation for PLC's practice archetype. |
| **Verification status** | Verified — every ADAPT cite in PLC v1.0.0 was Phase 3.7 Citation-Audited. Ships in full as PLC's `_frameworks/ADAPT.md`. |

### Source 3 — OPC Assessment v3.0

| Field | Value |
|-------|-------|
| **Source identifier** | Lam, Cong "Jawn" — *Organizational Political Context Assessment, v3.0.* Sphere diagnostic with 17 sections at 6-level hierarchical IDs. |
| **Canonical location** | `/Users/jawnlam/Obsidian/VGer/Deep Thought 42/Organizational Politics/Organizational Political Context Assessment.json` (Methodology Author's prior work). |
| **Page count / extent** | 17 sections; 9 § 16 subsections; 9 § 17 subsections; 10 constructive approaches; 3×10 harm grid; 5 ethical frameworks. |
| **Full-vs-excerpt status** | FULL — JSON source. The historical incident: during the v1.0 build, OPC § 16.7 was initially fabricated as "schedule-flexibility for client crisis response" before the canonical JSON was located. The actual § 16.7 is `cognitive_distortions_in_play`. Multiple other section labels were similarly corrected. |
| **Sensitivity** | Public (within scope of PLC's restrictive LICENSE — citation permitted, redistribution requires authorization). |
| **AI-read acknowledgment** | OPC v3.0 is a 17-section diagnostic that the operator walks during sphere-open to characterize the political context of an engagement. Section count + hierarchical ID structure is verified against the canonical JSON. The 10 constructive approaches and 3×10 harm grid + 5 ethical frameworks feed into the ethical-accounting L1 audit-trail check. |
| **Verification status** | Verified — every OPC cite in PLC v1.0.0 was Phase 3.7 Citation-Audited against the canonical JSON. Ships in full as PLC's `_frameworks/OPC-Assessment.md`. |

---

## Inventory gate (ARTIFACT-DRAFT precondition — retrospectively satisfied)

- [x] Every source has `Canonical location` filled with an actual location
- [x] Every source has `Full-vs-excerpt status` confirmed against the source itself
- [x] Every source has `AI-read acknowledgment` filled with a substantive one-line summary
- [x] `ove_Source_Inventory_Status` set to `locked` (post-SHIP-PREP Phase 3.7 clearance)

## Audit gate (SHIP-PREP Phase 3.7 — retrospectively satisfied)

- [x] Every "p.XX / § X.Y / named theorist / verbatim quote" in PLC v1.0.0's shippable content traces to a source listed here
- [x] Every cite's content verified against the canonical source (operator-confirmed during PLC v1.0 SHIP-PREP rework)
- [x] No `[SOURCE-VERIFICATION-REQUIRED]` placeholders remain
- [x] PLC's `_citation-audit-log.md` records the verification of every cite

## Notes

The sources above were all consulted during PLC v1.0's actual build. The historical incidents documented in `_design-decisions.md` (D-B-2 Citation Audit, D-B-3 Worked-Example Slot-ID Verification) describe the F13 fabrications that surfaced *before* the canonical sources were located — the AI was operating on session-memory paraphrase rather than the canonical text. Once each source was located and read, the audit could be cleared.

The OVE v2.1 source-inventory pattern (this file's structure) was directly motivated by PLC's build experience. Future practice-archetype OVs designed via OVE v2.1+ start with the structured source-capture at CQ3 and the inventory gate at Step 4.5, preventing the F13 vector at design-time rather than ship-time.
