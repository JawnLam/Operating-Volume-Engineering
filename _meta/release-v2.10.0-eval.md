---
type: Fleeting
timestamp: "2026-08-28T00:00:00Z"
Item_ID: ove-release-v2-10-0-eval
title: "OVE v2.10.0 — Release Eval (pre-registered)"
Date_Added: 2026-08-28
Date_Modified: 2026-08-28
Needs_Processing: false
---

# OVE v2.10.0 — Release Eval (pre-registered before build)

**Ruler declaration.** Fixed ruler for the release in `release-v2.10.0-plan.md`, committed before the build. The evaluator judges against these criteria only — "does the work satisfy the plan?", never "could it be better?" Observations beyond the rows bank, non-blocking. Every criterion is binary; evidence cites file + line/section, grep output, or git output.

**Evaluator independence.** Executed by a fresh agent instance with no drafting role. The behavioral row (E14) uses a second fresh instance as subject.

## Criteria

| # | Criterion | PASS condition |
|---|---|---|
| E1 | Convention 16 exists and is general | `_meta/CONVENTIONS.md` contains `## Convention 16` defining specialist delegation subject-agnostically — specialist, detection trigger, requisition, mount, fulfillment all defined without ICM-specific vocabulary in the general contract — with ICME referenced only as the first registry instance |
| E2 | The boundary rule | Convention 16 states that the generalist holds only the detection trigger and requisition interface, that requisitions carry WHAT/WHY/constraints and never internal design, and names F18 as the violation |
| E3 | Mount contract | Convention 16's mount contract covers: declared in the host manifest, vendored location, versioned/pinned, updated only via specialist re-engagement, and the pre-fulfillment state (declared placeholder + banked requisition; host ships functional) |
| E4 | Registry exists with ICME planned | `_design-engine/_meta/SPECIALISTS.md` exists with a general entry format and an ICME entry whose status is `planned` |
| E5 | Detection: factory signature | The ICM detection criterion states all five structural marks (terminating; spec-completable in advance; linear/near-linear; consistency-preferred; run-scoped state) as jointly required |
| E6 | Detection: counter-indicators | The criterion lists counter-indicators including at least: answer-dependent elicitation, cross-run state accumulation inside the process, state-driven dispatch/branching, mid-process cross-session resume, and in-process normative walls (with walls assigned to the host as requisition output constraints) |
| E7 | Detection: hybrid-split + acid test + markers | The criterion contains the hybrid-split rule (judgment half stays host-side and parameterizes the requisitioned pipeline half), the run-fresh-amnesia acid test, design-time markers referencing Q1/CQ10/Q7, and the requirement that every candidate is classified `ov-native | requisition | hybrid-split` with classifications (including negative ones) logged in the design record |
| E8 | Requisition template | `_templates/TEMPLATE-specialist-requisition.md` exists with: need, interface contract (host-supplied inputs; host-received outputs incl. filing/Type), host-imposed constraints, consistency posture, an explicit out-of-scope declaration naming internal design as an F18 defect, a status ledger, and a filled example whose fiction is NOT the operator's placeholder name |
| E9 | Engine hooks | All four hooks present: Q7 sweep in `04-SCHEMA-DESIGN.md`; the sweep + artifact-list + quality-gate additions in `BOOTSTRAP-NEW-OV.md`; the advisory sweep step in `03-DESIGN-PROTOCOL.md` §4; Phase 3.13 (HARD STOP — conditional, `n-a` logged otherwise) in `07-SHIPPING-CHECKLIST.md` verifying requisitions complete and HOW-free |
| E10 | Composition concept + manifest field | `01-WHAT-IS-AN-OV.md` contains a Composed-OVs section stated subject-agnostically AND `TEMPLATE-ov-manifest.md` declares a `Sub_Artifact_Mounts` list (empty default) |
| E11 | F18 exists | `_meta/FAILURE-MODES.md` contains `## F18` in house format, primary form generalist overreach (stage-structure drafting as canonical instance), sibling missed-detection form noted, prevention pointing at Convention 16 / the sweeps / Phase 3.13 |
| E12 | Wiring + traceability + records | `00-START-HERE.md` load table has a SPECIALISTS.md row; `TRACEABILITY.md` has rows for Convention 16 and the specialist sweep mapping to F18; `Date_Modified` synced on every file the build commit edits; `VERSION.md` identifiers table's release-date row reads 2026-08-28 (the v2.9.0 banked drift corrected) |
| E13 | Release identity | `VERSION.md` declares 2.10.0 naming Convention 16, SPECIALISTS.md, and F18; `CHANGELOG.md` has a § 2.10.0 entry including the focus-by-delegation thesis and this release's governance record |
| E14 | Behavioral probe | A fresh instance given `SPECIALISTS.md` (and the Q7 sweep text), presented with a mixed slate of five candidate activities for a fictional host OV — including at least one answer-dependent elicitation activity, one clear template-deliverable pipeline, one stateful monitoring activity, one judgment+production hybrid, and one refusal-walled decision activity — classifies the clear pipeline as `requisition`, keeps the elicitation, monitoring, and walled-decision activities `ov-native`, splits the hybrid with the judgment half host-side, emits requisition-shaped output containing **zero stage structure**, and notes the banked path (specialist status `planned`). Any stage design in its output, or the walled activity classified `requisition`, = FAIL |
| E15 | Additivity + consistency | Build-commit diff shows no existing numbered convention, failure mode, phase, check, chapter, or CQ/Q renamed, renumbered, or removed; grep finds no stale enumeration (convention/F-code/chapter counts and ranges current across engine and root docs — including any surface asserting Convention 15 or F17 is the last entry) |
| E16 | Pre-registration proof | The commit adding this eval and the plan precedes the build commit(s); neither governance file modified after its pre-registration commit |

## Disposition (pre-registered)

- **All 16 PASS** → done; results to `release-v2.10.0-eval-results.md` with banked notes; commit and close.
- **Any FAIL** → blocking: fix, re-run the eval in full. Same criterion failing twice for distinct causes → escalate to the operator.
- Observations beyond E1–E16 → banked to the next release's hopper via the results file; never silently fixed in-flight, never dropped.
