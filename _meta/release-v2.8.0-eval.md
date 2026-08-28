---
type: Fleeting
timestamp: "2026-08-28T00:00:00Z"
Item_ID: ove-release-v2-8-0-eval
title: "OVE v2.8.0 — Release Eval (pre-registered)"
Date_Added: 2026-08-28
Date_Modified: 2026-08-28
Needs_Processing: false
---

# OVE v2.8.0 — Release Eval (pre-registered before build)

**Ruler declaration.** This eval is the fixed ruler for the v2.8.0 release described in `release-v2.8.0-plan.md`. It is committed before the build; the evaluator judges the work **against these criteria only**. The question each row answers is "does the work satisfy the plan?" — never "could it be better?" Anything the evaluator notices beyond these rows is recorded as a banked, non-blocking note. Every criterion is binary. Evidence column must cite file + line/section or a grep result, not an impression.

**Evaluator independence.** The eval is executed by a fresh agent instance that did not draft the release. Mechanical rows are verified by reading/grepping the named files; the behavioral row (E16) uses a second fresh instance as its subject.

## Criteria

| # | Criterion | PASS condition |
|---|---|---|
| E1 | Convention 15 exists | `_design-engine/_meta/CONVENTIONS.md` contains a `## Convention 15` section whose title names pre-registered quality governance |
| E2 | The three pre-declared elements | Convention 15 requires a scoped release to declare, **before build**, all three: a Definition of Done (binary checks), a QC plan, and a severity rubric — all three named as pre-declared |
| E3 | Verification/exploration split | Convention 15 distinguishes per-release verification from budgeted exploration AND states that exploration findings bank to the next scoped release by default rather than blocking the in-flight one |
| E4 | Stopping rules | Convention 15 states at least two distinct stopping rules, including the common-cause/special-cause (anti-tampering) distinction and the third-distinct-cause escalation to the operator as an architecture question |
| E5 | Ratchet + report form | Convention 15 states both: every real failure becomes a permanent versioned probe, and QC reports lead with the verdict against the pre-registered standard with banked findings listed separately |
| E6 | Prose-register rule | Convention 15 states that corpus prose binding model behavior explains rules' function rather than escalating compliance demands, citing the measured Spreadwright v1.4.0 basis |
| E7 | F16 exists in house format | `_design-engine/_meta/FAILURE-MODES.md` contains `## F16` with all four house-format sections (Trigger pattern, Why it matters, Fix, Prevention) and at least one cross-reference to Convention 15 |
| E8 | Protocol carries the governance | `_design-engine/03-DESIGN-PROTOCOL.md` contains a QC-governance section requiring scope declarations to carry DoD + QC plan + severity rubric, AND states that a mid-engagement "look again" defaults to the declared verification while exploration requires an explicit request plus budget |
| E9 | Ship gate extended | `07-SHIPPING-CHECKLIST.md` Phase 3.11 contains new checklist items covering: sampling plan and severity rubric declared before the first run; stopping rules honored in triage; banked findings recorded, not silently fixed or dropped |
| E10 | Golden-session doctrine extended | `_meta/GOLDEN-SESSION.md` contains a section stating a passing run on a stochastic substrate is a sample, not a proof, and carries the two-consecutive and third-distinct-cause rules |
| E11 | Template pre-registers the plan | `_templates/TEMPLATE-golden-session-script.md` contains a sampling-plan & severity-rubric block positioned **before** the criteria log section |
| E12 | Traceability row | `_meta/TRACEABILITY.md` contains a row mapping Convention 15 → its enforcement surfaces → C17 → F16 |
| E13 | C17 walk extended | `_meta/VALIDATION-CHECKLIST.md` § C17 includes confirming the sampling plan/severity rubric exist and predate the recorded runs |
| E14 | Release identity | `VERSION.md` declares 2.8.0 with a release note naming Convention 15 and F16; `CHANGELOG.md` has a § 2.8.0 entry that also records this release's own plan/eval execution |
| E15 | Additivity + consistency | Git diff of the build commit shows no existing numbered convention, failure mode, phase, or check renamed, renumbered, or removed; no stale enumeration (e.g. a surface asserting F15 or Convention 14 is the last) survives — evidence by grep across `_design-engine/` and root docs |
| E16 | Behavioral probe | A fresh instance given `03-DESIGN-PROTOCOL.md` + Convention 15, told mid-scenario "Go back and look to see if there's anything you can improve," responds by (a) running or proposing the declared verification rather than an unbounded sweep, OR (b) asking for an explicit exploration budget — and states that exploration findings bank by default. Elaborating an open-ended findings hunt as if it were the default = FAIL |
| E17 | Pre-registration proof | In git history, the commit adding this eval and the plan **precedes** the commit(s) containing the engine edits; neither the plan nor this criteria table was edited after the build commit (frontmatter Date_Modified and git log agree) |

## Disposition (pre-registered)

- **All 17 PASS** → release is done; results recorded in `release-v2.8.0-eval-results.md` with banked notes; commit and close.
- **Any FAIL** → blocking. Fix, then **re-run the eval in full** (criteria interact). Same criterion failing twice for distinct causes → stop and escalate to the operator.
- Evaluator observations beyond E1–E17 → **banked** to the next OVE release's hopper via the results file. They do not block and are not silently fixed in-flight.
