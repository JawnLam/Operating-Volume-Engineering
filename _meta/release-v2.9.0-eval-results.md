---
type: Fleeting
timestamp: "2026-08-28T00:00:00Z"
Item_ID: ove-release-v2-9-0-eval-results
title: "OVE v2.9.0 — Eval Results"
Date_Added: 2026-08-28
Date_Modified: 2026-08-28
Needs_Processing: false
---

# OVE v2.9.0 — Eval Results

**Verdict: 16/16 PASS on eval run 2 — DoD met; 0 blocking; 2 banked.** Release is done per the pre-registered disposition, after one remediation cycle.

## Execution record

- **Eval run 1** (independent `claude-sonnet-5` evaluator, no drafting role): **15/16.** E14 FAIL — `VERSION.md` still read "Nine core operating files (`00–08`)" after the release added the tenth chapter; the evaluator also noted `CONTRIBUTING.md`'s pre-existing "(00–07, BOOTSTRAP)" range.
- **Remediation** (commit `5e0ddfb`): both chapter-range enumerations corrected. The CONTRIBUTING fix was judged in-scope of E14's plain text ("no stale enumeration survives — grep across the engine and root docs"), i.e., criterion remediation, not banked absorption; its `Date_Modified` synced per 09's own records discipline.
- **Eval run 2** (a second independent evaluator, no drafting role, no part in run 1): **16/16**, including verification that the remediation commit did not touch the E15 probe's source files (probe transcript remained valid evidence) and a fresh stale-enumeration grep finding no further hits.
- **E15 behavioral probe** subject: fresh `claude-sonnet-5` instance given 09-CLOSE-OUT + Phase 9 and a "gate's clear — ship it" scenario (installed OV with an operator-private filled file, an eleven-entry grown catalog, a vault console, schema unmoved). The subject enumerated, unprompted and in order: snapshot before touching anything; the preservation walk naming both operator files (merge-not-clobber for the catalog); rename + overlay; post-overlay verification with restore-and-re-run on loss; registry sync with the schema leg logged `n/a` and the full catalog update; the independence sweep; records discipline; the Phase 9 cartridge close.
- **E16 pre-registration proof:** plan+eval at `6c19f94` (surviving a mid-flight rebase over the operator's `-v2.7` → `-v2.8` folder rename) → build `d6fe051` → remediation `5e0ddfb`; governance files untouched after pre-registration.

## Per-criterion verdicts (run 2)

E1–E13, E15, E16: PASS (chapter complete with all five sections + records discipline; three-copies doctrine; preservation walk + post-overlay verification; registry sync both halves; independence sweep with recipe; graduation criteria + three-part departure record; records discipline; Convention 12 in position with numbering-note history; F17 in house format; Phase 9 rewire incl. the N→N+1 rule; 00/03 wiring with no new activity code; traceability rows + O-3 RESOLVED; VERSION/CHANGELOG at 2.9.0 with corrected sub-identifiers and the governance record). E14: PASS after remediation — additivity confirmed across both commits; no surviving stale enumerations.

## Banked — the next OVE release's hopper (recorded, not fixed in-flight)

1. **`VERSION.md`'s identifiers-table `Release date` row still reads 2026-07-16**, stale against the frontmatter's `release_date: 2026-08-28` — outside E1–E16's literal wording, so it banks under the rubric. Noted with appropriate humility: this is precisely the drift class 09's records discipline targets, caught by the eval's evaluator rather than the release's own build — the strongest argument yet recorded for the banked mechanical check.
2. **Mechanical validator coverage for close-out/independence (C20/C21-class)** — pre-banked in the plan; reaffirmed, and item 1 is its motivating exhibit.
