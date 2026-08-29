---
type: Fleeting
timestamp: "2026-08-28T00:00:00Z"
Item_ID: ove-release-v2-9-0-eval
title: "OVE v2.9.0 — Release Eval (pre-registered)"
Date_Added: 2026-08-28
Date_Modified: 2026-08-28
Needs_Processing: false
---

# OVE v2.9.0 — Release Eval (pre-registered before build)

**Ruler declaration.** Fixed ruler for the release in `release-v2.9.0-plan.md`, committed before the build. The evaluator judges against these criteria only — "does the work satisfy the plan?", never "could it be better?" Observations beyond the rows are banked, non-blocking. Every criterion is binary; evidence cites file + line/section, grep output, or git output.

**Evaluator independence.** Executed by a fresh agent instance with no drafting role. The behavioral row (E15) uses a second fresh instance as subject.

## Criteria

| # | Criterion | PASS condition |
|---|---|---|
| E1 | Chapter exists | `_design-engine/09-CLOSE-OUT.md` exists with sections covering all five plan areas: three copies, upgrade re-ship choreography, registry sync, independence sweep, graduation — plus records discipline |
| E2 | Three-copies doctrine | 09 names all three copies (working tree, `_shipped/` record, live install), states the ship record is written once and never edited after, and that prior records are untouchable |
| E3 | Preservation list | 09's upgrade choreography includes an explicit pre-overlay preservation list naming at least: Operator-Private Zone files, Grows-Through-Use Zone with merge-not-clobber (Convention 14 cited), documented local override blocks, and one-time setup blocks (paths retargeted, instruction content unchanged) — plus a post-overlay verification step |
| E4 | Registry sync in 09 | 09 requires ecosystem-catalog updates in the same change as the ship, conditional (`n-a` logged where no catalog exists), and distinguishes the catalog half from Phase 3.12's schema half |
| E5 | Independence sweep | 09 states the attribution-vs-functional-dependence rule with a greppable recipe and the attribution-by-link exception |
| E6 | Graduation | 09 defines maturity criteria (at minimum: schema freeze policy, passes own audit, gate-clearance history, demonstrated use, own governance loop), a departure record (final decision entry; registry status `graduated` + pointer; design cartridge retained, never deleted), and the post-graduation stewardship change |
| E7 | Records discipline | 09 requires `Date_Modified` sync on every file edited in a release and joint regeneration/agreement of the release-identity surfaces (VERSION identifiers incl. sub-identifier rows, CHANGELOG) |
| E8 | Convention 12 claimed | `_meta/CONVENTIONS.md` contains `## Convention 12` (Registry Sync) in numeric position, covering both index halves and pointing at Phase 3.12 and 09; the Convention-13 numbering note no longer claims 12 is reserved/skipped (historical note may remain) |
| E9 | F17 exists | `_meta/FAILURE-MODES.md` contains `## F17` in house format (Trigger pattern / Why it matters / Fix / Prevention), citing the shipped-by-precedent basis and pointing at 09 + Convention 12 |
| E10 | Phase 9 rewired | `07-SHIPPING-CHECKLIST.md` Phase 9 points into `09-CLOSE-OUT.md` and states that subsequent releases (N → N+1) require the 09 upgrade choreography beyond the first-ship checklist |
| E11 | Wiring | `00-START-HERE.md` load table has a `09-CLOSE-OUT.md` row AND `03-DESIGN-PROTOCOL.md`'s SHIP-PREP row references close-out, with no new activity code added |
| E12 | Traceability | `_meta/TRACEABILITY.md` has rows for Convention 12 and close-out execution mapping to F17; orphan O-3 is resolved (removed or marked resolved with a note); the file's frontmatter `Date_Modified` reflects this release |
| E13 | Release identity | `VERSION.md` declares 2.9.0 naming the close-out chapter, Convention 12, and F17; sub-identifier rows read Design engine v2.9 / Templates v2.8 / Validator v2.7; `CHANGELOG.md` has a § 2.9.0 entry including the release-governance (dogfood) record |
| E14 | Additivity + consistency | Build-commit diff shows no existing numbered convention, failure mode, phase, check, or chapter renamed, renumbered, or removed (extending Phase 9's body in place is permitted); no stale enumeration survives (greps for reserved-Convention-12 claims outside historical notes, F-code ranges, chapter counts) |
| E15 | Behavioral probe | A fresh instance given `09-CLOSE-OUT.md` (plus 07's Phase 9) and a scenario — an OV's v1.2.0 cleared its golden gate; the live install `<OV>-v1.1/` contains an operator-filled private file and an operator-appended portfolio catalog; operator says "ship it" — enumerates, unprompted: the `_shipped/` snapshot, the rename + overlay with the preservation walk naming the private and grown files, registry/catalog sync, and the records close. Declaring done at gate-pass, or overlaying without the preservation walk, = FAIL |
| E16 | Pre-registration proof | The commit adding this eval and the plan precedes the build commit(s); neither governance file is modified after its pre-registration commit |

## Disposition (pre-registered)

- **All 16 PASS** → done; results to `release-v2.9.0-eval-results.md` with banked notes; commit and close.
- **Any FAIL** → blocking: fix, re-run the eval in full. Same criterion failing twice for distinct causes → escalate to the operator.
- Observations beyond E1–E16 → banked to the next release's hopper via the results file; never silently fixed in-flight, never dropped.
