---
type: Fleeting
timestamp: "2026-08-28T00:00:00Z"
Item_ID: ove-template-specialist-requisition
title: "TEMPLATE — Specialist Requisition (Convention 16)"
Date_Added: 2026-08-28
Date_Modified: 2026-08-28
Needs_Processing: false
doc_type: design-engine-template
role: requisition-skeleton
scope: subject-agnostic
updated: 2026-08-28
---

# Specialist Requisition — <sub-artifact name>

> **This document specifies WHAT the host OV needs and WHY, plus the constraints the deliverable must satisfy. It never specifies HOW.** Internal design — stages, folder layouts, context budgets, stage contracts, or any structure inside the sub-artifact — belongs to the specialist; content of that kind in this document is an **F18 defect** and must be removed before the requisition is accepted. (Convention 16; `_meta/SPECIALISTS.md`.)

## Identity

- **Host OV / engagement:** `<host OV name; design-cartridge or upgrade engagement reference>`
- **Specialist / sub-artifact class:** `<registry entry, e.g., ICME / ICM workspace>`
- **Requisition ID:** `<host-namespace>-req-<nn>`
- **Classification record:** `<pointer to the _design-decisions.md entry logging this candidate as requisition or hybrid-split, with the one-line reason>`

## The need

- **Purpose:** `<what this sub-artifact produces for the host, in one or two sentences — outcome language, not process language>`
- **Invoking host activity & trigger:** `<which OV activity invokes a run, and what conditions trigger it — e.g., "operator-requested during <ACTIVITY>", "fires at each <event>">`
- **Cadence / volume:** `<how often runs happen; roughly how many per period>`
- **Hybrid-split note (if applicable):** `<which retained host activity parameterizes and invokes this pipeline; what it gathers/decides before a run starts>`

## Interface contract

- **Inputs the host supplies:** `<the Items, files, and parameter values a run consumes — names and Types, with locations in the host's backbone>`
- **Outputs the host receives:** `<the deliverable class; where it is filed in the host; which host Type records it; what filing metadata the host requires>`

## Host-imposed constraints (norms the deliverable must satisfy)

- `<output constraints from the host's walls and rules — e.g., "the deliverable carries no values from <file>", "every figure in the deliverable carries the host's provenance tags", "no verdict/score language">`
- `<confidentiality: which host zones the pipeline may read; which it must never read>`
- **Consistency posture:** `<default: no learning from prior runs. If the host wants precedent sensitivity, state it here and let the specialist judge whether the need is still their form>`

## Status ledger

| Date | Status | Note |
|---|---|---|
| `<YYYY-MM-DD>` | `banked` | `<specialist status planned; placeholder mount declared at <path>; host behavior meanwhile: <what the host does without it>>` |
| | `fulfilled` | `<specialist engagement ref; fulfillment version; mount path>` |

---

## Filled example (fictional host: "Docket," a litigation-practice OV)

*Identity:* Docket v1.2 upgrade engagement · ICME / ICM workspace · `dkt-req-01` · classification logged 2026-08-28 ("hearing-binder assembly: full factory signature, no counter-indicators — the interview that selects exhibits is retained host-side as BINDER-PREP").

*The need:* Produces a court-ready hearing binder (indexed exhibit PDF set + cover index) from a case cartridge's filed exhibits. Invoked by the retained BINDER-PREP activity after the operator confirms the exhibit list; triggered per scheduled hearing. Cadence: one to four runs per case-month. Hybrid-split: BINDER-PREP gathers the exhibit selection, confirms redactions with the operator, and hands the confirmed list as run parameters.

*Interface contract:* Inputs — the confirmed exhibit list (`DKT_Exhibit` Items), the case caption block from `_case-manifest.md`, the court's formatting parameters. Outputs — the binder package filed to `Filings/binders/<hearing-date>/`, recorded as a `DKT_Filing` Item with hearing date and exhibit-count metadata.

*Host-imposed constraints:* The binder contains nothing from `_strategy-notes.md` (privileged zone — the pipeline may not read it); every exhibit page carries its exhibit ID; no annotations of any kind on exhibit content. Consistency posture: strict — binder N formatted identically to binder 1; no learning from prior binders.

*Status ledger:* 2026-08-28 · `banked` · ICME status planned; placeholder at `_pipelines/hearing-binder/`; meanwhile BINDER-PREP ends with the operator assembling the binder manually from the confirmed list.
