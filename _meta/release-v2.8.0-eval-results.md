---
type: Fleeting
timestamp: "2026-08-28T00:00:00Z"
Item_ID: ove-release-v2-8-0-eval-results
title: "OVE v2.8.0 — Eval Results"
Date_Added: 2026-08-28
Date_Modified: 2026-08-28
Needs_Processing: false
---

# OVE v2.8.0 — Eval Results

**Verdict: 17/17 PASS — DoD met; 0 blocking; 5 banked.** Release is done per the pre-registered disposition.

**Execution record.** Evaluator: independent `claude-sonnet-5` instance (no participation in drafting), judging only against `release-v2.8.0-eval.md`. Behavioral probe (E16) subject: a second fresh `claude-sonnet-5` instance. Pre-registration proof (E17): plan+eval committed at `39bfe6b`, build at `14cfdd7`, neither governance file touched by the build commit; the plan/eval files show exactly one commit in their history.

## Per-criterion verdicts (evaluator's evidence abridged; full form in the session record)

| # | Verdict | Evidence |
|---|---|---|
| E1 | PASS | CONVENTIONS.md `## Convention 15 — Pre-Registered Quality Governance` |
| E2 | PASS | Contract item 1 names DoD + QC plan + severity rubric, all pre-declared |
| E3 | PASS | Item 2: verification vs budgeted exploration; findings bank by default |
| E4 | PASS | Item 4: common/special cause; two-consecutive; third-distinct-cause escalation |
| E5 | PASS | Item 5 (ratchet) + item 3 (report form "DoD met; N blocking; M banked") |
| E6 | PASS | Prose-register rule with the measured 0-for-3 vs 5-for-5 basis |
| E7 | PASS | F16 in house format; Prevention cites Convention 15 |
| E8 | PASS | 03 § QC governance: declarations carry the standard; "look again" = declared verification; exploration budgeted |
| E9 | PASS | Phase 3.11: plan-predates-runs, stopping rules, banked-findings record |
| E10 | PASS | GOLDEN-SESSION § Sampling, not proof: sample-not-proof + both stopping rules |
| E11 | PASS | Template plan block precedes the criteria log |
| E12 | PASS | TRACEABILITY row: Convention 15 → enforcement → C17 (extended) → F16 |
| E13 | PASS | C17 walk: plan block present and predates runs (`info` pre-v2.8.0) |
| E14 | PASS | VERSION 2.8.0 + CHANGELOG § 2.8.0 incl. the governance record |
| E15 | PASS | Build diff additive-only; no renumbering; `C1–C19` ranges remain accurate (no C20 shipped) |
| E16 | PASS | Probe re-ran declared verification, used the report form, offered budgeted exploration with default banking |
| E17 | PASS | `39bfe6b` precedes `14cfdd7`; governance files untouched after pre-registration |

## Banked — the next OVE release's hopper (recorded, not fixed in-flight)

1. `TRACEABILITY.md` frontmatter `Date_Modified` not bumped despite a body edit in the build commit (Convention 1 timestamp-sync drift).
2. `VERSION.md`'s sub-identifier rows (design engine / templates / validator versions) not bumped alongside the top-level 2.8.0.
3. Mechanical validator **C20** for the plan-block check (pre-banked in the plan; reaffirmed).
4. Vendored folder rename `-v2.7` → `-v2.8` per Convention 7 — operator-side call; all in-vault references move with it (pre-banked; reaffirmed).
5. A deeper multi-turn behavioral probe for the third-distinct-cause escalation path (E16 exercised only the first "look again" turn) — candidate ratchet probe for the next release's gate.

Items 1 and 2 are two-minute fixes left deliberately unfixed: they fell outside the pre-registered criteria, so under the severity rubric they bank. Absorbing them in-flight would have been the first violation of the convention this release ships.
