---
Item_Prototype: OVE_Session
Item_ID: "negotiation-prep-session-002"
Title: "Negotiation-Preparation — Session 002 — SCHEMA-DESIGN"
Date_Added: 2026-06-01
Date_Modified: 2026-06-01
Needs_Processing: false
ove_OV_Name: "Negotiation-Preparation"
ove_Session_Number: 2
ove_Activity: SCHEMA-DESIGN
ove_Duration_Minutes: 0
ove_Decisions_Locked: ["five-atom-types", "six-custom-activities", "per-pattern-mastery"]
ove_Artifacts_Touched: ["_schema-draft.md", "_design-decisions.md"]
ove_Quality_Gates_Passed: true
---

# Session 002 — 2026-06-01 — SCHEMA-DESIGN

## Opening State Summary

Interview complete. Cartridge in phase: schema-design. Manifest populated, decisions log open.

## Activity Proposal & Rationale

**Activity:** SCHEMA-DESIGN

**Rationale:** `_schema-draft.md` has not yet answered Q1–Q13. Per the design protocol, schema design is next.

## What Happened

Walked Q1–Q13 with explicit reasoning on each. The hardest questions:

**Q3 — Smallest unit.** Initial proposal: a single Party atom type with sub-types. Counter-proposal: distinct atom types for Party / Issue / Concession-Asset / Tactic / Pattern. The five-atom split won on grounds that each kind of atom has distinct frontmatter needs and relationships.

**Q4 — Relationships.** Concession-Asset trading is interesting — concessions are traded *between* atoms (Party gives → Party receives), so the relationship is asymmetric across negotiation rounds. Captured as `traded-for` (between Concession-Assets, with implicit context from the round).

**Q5/Q9 — Progression vs. cartridge boundary.** Decided: per-cartridge progression is *lifecycle stages* (prep → live → post-mortem → closed), not curricular phases. This OV doesn't have "Phase 1, Phase 2" structure — each cartridge has a lifecycle, and cross-cartridge there's Pattern accumulation.

**Q8 — Mastery scale.** The hardest. Per-atom mastery doesn't make sense (atoms are negotiation-specific). The user's learning lives at the Pattern level. New scale: recognized → applied → mastered (per Pattern atom).

**Cross-cartridge atoms.** Pattern atoms live at the OV level, not in any single cartridge. Each cartridge's POST-MORTEM proposes Patterns; Patterns get added to a central `Patterns/` folder at the OV root. Cartridges can reference Patterns; Patterns can reference cartridges where they were recognized.

## Decisions Locked

| # | Decision |
|---|----------|
| 2 | Five atom types (Party, Issue, Concession-Asset, Tactic, Pattern) |
| 3 | Six custom activities (STAKEHOLDER-MAP, BATNA-ANALYSIS, ISSUE-FRAMING, CONCESSION-PLAN, WARGAME, POST-MORTEM) |
| 6 | Per-Pattern mastery scale (recognized / applied / mastered) |

All locked in `_design-decisions.md`.

## Artifacts Touched

| Artifact | Action |
|----------|--------|
| `_schema-draft.md` | populated through Q1–Q13 |
| `_design-decisions.md` | three decisions appended |

## Open Threads for Next Session

- [ ] CARTRIDGE-SHAPE session — backbone files, lifecycle-stage handling, state-persistence per file
- [ ] Pattern atoms: confirm OV-level location is right (vs. duplicating in each cartridge that recognizes the pattern)

## Quality Gates Checklist

- [x] Schema draft answered through Q13
- [x] Three decisions locked
- [x] Session log written
- [x] `_design-state.md` updated (phase: schema-design → cartridge-shape)
- [x] `_design-decisions.md` appended
- [x] Open Thread for next session
