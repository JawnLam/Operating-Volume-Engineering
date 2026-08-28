---
type: Fleeting
timestamp: "2026-08-28T00:00:00Z"
Item_ID: ove-release-v2-8-0-plan
title: "OVE v2.8.0 — Release Plan (pre-registered)"
Date_Added: 2026-08-28
Date_Modified: 2026-08-28
Needs_Processing: false
---

# OVE v2.8.0 — Release Plan (pre-registered before build)

**Operator directive (2026-08-28):** fold the QC-governance discipline surfaced by the Spreadwright v1.4.0 engagement — pre-registered acceptance criteria, the verification/exploration split, anti-tampering stopping rules, the probe ratchet, and the calm-register prose lesson — into Operating-Volume-Engineering itself. This plan and its companion eval (`release-v2.8.0-eval.md`) are committed **before** any engine file is edited; the commit order in git history is the proof of pre-registration. This release is itself the first execution of the discipline it ships.

## What ships (scope)

A **minor, additive** release: **v2.8.0**. One new convention, one new failure mode, edits to two engine chapters, two meta protocols, one template, the traceability matrix, and the release records. Precedent for shape and weight: v2.7.0 (Convention 14 + C19).

1. **`_design-engine/_meta/CONVENTIONS.md` — Convention 15: Pre-Registered Quality Governance.** The rationale in two named parts (defect-count is a joint property of artifact and inspection resolution — the coastline; genuinely novel failures are generated adversarially against current text and cannot be enumerated in advance — the monsters), then the contract: (a) every scoped release declares, before build, a **Definition of Done** (binary checks), a **QC plan** (which reviews run, how many gate runs, what sampling plan), and a **severity rubric** (which finding classes block ship, which bank); (b) **verification vs exploration**: verification (the pre-registered script/eval) runs per release; exploration (open-ended crucibles, audit-mode sweeps) runs on cadence or by explicit operator request with a declared budget, and its findings **bank to the next scoped release's hopper by default** — the in-flight release absorbs only pre-declared blocking classes; (c) **report form**: QC reports lead with the verdict against the pre-registered standard ("DoD met; N blocking; M banked"), banked findings listed separately — a clean report is possible and therefore means something; (d) **stopping rules**: a single stochastic miss is not proof of a corpus defect — distinguish common-cause variation (address via the sampling plan) from special-cause gaps (patch) before editing; two consecutive same-probe misses establish a real failure; the same probe failing a **third time for a distinct cause** stops prose-patching and escalates to the operator as an architecture question; (e) **the ratchet**: every real failure becomes a permanent probe in the OV's acceptance script, and the script is versioned so finding-counts stay legible across releases; (f) **the prose-register rule**: corpus text that must bind a model's behavior explains what each rule does for the operator rather than escalating compliance demands — escalation provokes the refusal it targets (measured basis: the Spreadwright v1.4.0 gate, 0-for-3 escalated vs 5-for-5 calm).
2. **`_design-engine/_meta/FAILURE-MODES.md` — F16: Unbounded QC (fractal gold-plating).** House format (Trigger pattern / Why it matters / Fix / Prevention). The trigger: open-ended review ("look again for anything to improve") treated as a ship gate; findings-per-look never reaches zero, so the loop cannot terminate; late-stage form is tampering — fixes injected in response to stochastic variation that create new defects. Fix and prevention point at Convention 15 and the Phase 3.11 additions.
3. **`_design-engine/03-DESIGN-PROTOCOL.md`** — a new **"QC governance (Convention 15)"** section: scope declarations carry the DoD, QC plan, and severity rubric; an operator's mid-engagement "go back and look" defaults to running the declared verification; an exploration pass requires an explicit request plus a budget, and its findings bank.
4. **`_design-engine/07-SHIPPING-CHECKLIST.md` — Phase 3.11 additions:** checklist items requiring that the sampling plan (run count, pass threshold, never-waived criteria) and the severity rubric were declared **before** the first run; that stopping rules were honored during triage; and that banked findings are recorded in the design record rather than silently fixed in-flight or silently dropped.
5. **`_design-engine/_meta/GOLDEN-SESSION.md`** — a new **"Sampling, not proof"** section: on a stochastic substrate a passing run is a draw from a distribution, not a theorem; the disposition table is an acceptance-sampling plan; the two-consecutive and third-distinct-cause rules; the ratchet; the prose-register rule for writing hardenings.
6. **`_design-engine/_templates/TEMPLATE-golden-session-script.md`** — a pre-registered **"Sampling plan & severity rubric"** block positioned before the criteria log, so every future script carries its plan ahead of its results.
7. **`_design-engine/_meta/TRACEABILITY.md`** — one new matrix row: Convention 15 → enforcement (03 § QC governance; Phase 3.11; GOLDEN-SESSION § Sampling, not proof) → check (C17 prose walk, extended) → failure (F16).
8. **`_design-engine/_meta/VALIDATION-CHECKLIST.md` § C17** — extended prose walk: confirm the script's sampling plan and severity rubric are present and predate the recorded runs.
9. **`VERSION.md` + `CHANGELOG.md`** — v2.8.0 identifiers and a changelog section that records this release's own DoD/eval execution (the dogfood record).
10. **Consistency sweep** — any surface that enumerates conventions or failure modes (counts, "F1–F15" style ranges) is updated; no numbered item is renamed, renumbered, or removed.

## Out of scope (banked, not forgotten)

- **`validate.py` changes** (a mechanical C20). Banked: the C17 prose extension covers the walk; automating it is a future minor.
- **Upstream push** to the standalone Operating-Volume-Engineering repository. This vendored copy is the operating truth for this vault; mirroring upstream is an operator-side or follow-up action.
- **Retrofitting shipped OVs** (Spreadwright et al. already embody most of the discipline; formal retrofit rides their next scoped release).
- **A full golden session of OVE itself.** Proportionality: this is a doctrine addition, precedent v2.7.x; the eval below includes one targeted behavioral probe instead. The discipline's full behavioral exercise is the next real OV engagement.

## QC plan for this release (pre-registered)

- **Verification:** the companion eval (`release-v2.8.0-eval.md`) — mechanical checks plus one behavioral probe — executed after build by an **independent evaluator agent** (fresh instance, no participation in drafting), returning binary verdicts per criterion.
- **No open-ended crucible.** Any observation the evaluator volunteers beyond the criteria is recorded as **banked**, non-blocking.
- **Severity rubric:** any eval criterion FAIL = **blocking** (fix and re-run the eval in full); evaluator notes outside the criteria = **banked** to the next OVE release's hopper (recorded in the results file).
- **Stopping rule:** if the same criterion fails twice for distinct causes, escalate to the operator rather than iterating a third time.

## Definition of Done

The release is done when: every scope item 1–10 is on disk; the eval has been run by an independent evaluator; every criterion is PASS; blocking = 0; banked findings are recorded in `release-v2.8.0-eval-results.md`; VERSION/CHANGELOG agree on 2.8.0; and the work is committed and pushed with the plan/eval commit preceding the build commit.
