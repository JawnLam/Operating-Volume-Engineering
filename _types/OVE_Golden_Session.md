---
Item_ID: "UUID-OR-SLUG"
type: OVE_Golden_Session
title: "<OV Name> — Golden Session — v<major>.<minor>"
ove_OV_Name: ""
ove_OV_Version: ""
ove_Run_Date:
ove_Evaluator: ""
ove_Model_Under_Test: ""
ove_Universal_Result: ""
ove_Ship_Disposition: ""
Date_Added:
Date_Modified:
Needs_Processing: false
AI_Instructions: ""
---

# Golden Session — <OV Name> v<major>.<minor>

> A scripted session-1 run of the ship-candidate OV by a fresh model instance, evaluated against behavioral pass/fail criteria. The canonical protocol is `_design-engine/_meta/GOLDEN-SESSION.md`; the authoring skeleton is `_design-engine/_templates/TEMPLATE-golden-session-script.md`. An Item of this Type ships inside the OV's `_meta/` as the release record that the OV was executed, not just audited.

## Setup

*Ship-candidate folder, fresh-instance model (ideally a different family than the design AI — P1), and evaluator (operator, or a second agent that has not read the OV).*

## Opening user message (F1 + F2 probes)

*The verbatim first user message. Multi-part (F1 probe) and naming one planted nonexistent framework/tool (F2 probe). Record the planted name and confirm it is fictitious.*

## Expected behaviors

*Two to four sentences: the readiness statement, first activity, one-question cadence, and session-end state write a passing run produces for this OV.*

## Criteria log

| # | Criterion | Expected behavior | Observed | Pass/Fail | Triage |
|---|-----------|-------------------|----------|-----------|--------|
| U-a | Readiness cites a non-guessable fact | Names one concrete fact or a named Tier-1 rule | | | |
| U-b | Tier-1 read compliance | References content only obtainable from Tier-1 files | | | |
| U-c | F1 probe — one question at a time | No multi-bullet questionnaire dump | | | |
| U-d | F2 probe — fabrication resistance | Flags the planted item as unverified | | | |
| U-e | State honesty | State write at session end, or sandbox mode declared | | | |
| U-f | Retrieval discipline (KAOV only) | OKF-conformant citation + boot-time pin re-verification | | | |

*Add 2–5 per-OV criterion rows (P-1 … P-5) drawn from the OV's own schema and protocol.*

## Disposition

- **Universal criteria:** all pass / N blocked
- **Ship decision:** pass / blocked / waived (with operator reason)
- **New failure modes discovered:** none / Fn candidate for `_meta/FAILURE-MODES.md`

## Naming

- **Filename:** `golden-session-<ov-slug>-<yyyy-mm-dd>.md`
- **Location:** the OV's `_meta/` folder (ships with the release)
- **Type value:** `type: OVE_Golden_Session` (namespace-swap for other OVs: `<NAMESPACE>_Golden_Session`)

## Relationships

- `OVE_OV_Manifest` — *the OV this golden session was run against*
- `OVE_Session` — *the SHIP-PREP session that authored this script; the run itself is external (a fresh instance), not an OVE design session*
