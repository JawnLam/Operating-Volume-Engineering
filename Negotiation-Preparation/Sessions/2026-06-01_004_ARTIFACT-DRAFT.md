---
Item_Prototype: OVE_Session
Item_ID: "negotiation-prep-session-004"
Title: "Negotiation-Preparation — Session 004 — ARTIFACT-DRAFT"
Date_Added: 2026-06-01
Date_Modified: 2026-06-01
Needs_Processing: false
ove_ov_name: "Negotiation-Preparation"
ove_session_number: 4
ove_activity: ARTIFACT-DRAFT
ove_duration_minutes: 0
ove_decisions_locked: []
ove_artifacts_touched: ["Artifacts/AI-BOOTSTRAP.md", "Artifacts/00-START-HERE.md", "Artifacts/01-NEGOTIATION-FOUNDATIONS.md", "Artifacts/02-STAKEHOLDER-MAPPING.md", "Artifacts/03-BATNA-AND-ZOPA.md", "Artifacts/BOOTSTRAP-NEW-NEGOTIATION.md", "Artifacts/TEMPLATE-negotiation-manifest.md", "Artifacts/TEMPLATE-stakeholder-map.md"]
ove_quality_gates_passed: true
---

# Session 004 — 2026-06-01 — ARTIFACT-DRAFT

## Opening State Summary

Schema and cartridge shape locked. Six decisions in the log. Now drafting engine files in priority order: AI-BOOTSTRAP, then engine chapters, then templates.

## Activity Proposal & Rationale

**Activity:** ARTIFACT-DRAFT

**Rationale:** Per the protocol decision algorithm, all schema/cartridge-shape questions are answered; standard artifacts are missing. Priority order: AI-BOOTSTRAP → engine chapters → BOOTSTRAP-NEW-NEGOTIATION → templates → root docs.

## What Happened

Drafted the foundational artifacts. Major ones drafted in `Artifacts/`:

- **AI-BOOTSTRAP.md** — entry point; references the engine chapter list and the safety chapter prominently
- **00-START-HERE.md** — assistant entry to the engine; six custom activities introduced
- **01-NEGOTIATION-FOUNDATIONS.md** — BATNA, ZOPA, integrative-distributive distinction, interest-based negotiation core concepts (without privileging any single framework)
- **02-STAKEHOLDER-MAPPING.md** — protocol for populating Party atoms
- **03-BATNA-AND-ZOPA.md** — protocol for the BATNA-ANALYSIS activity
- **BOOTSTRAP-NEW-NEGOTIATION.md** — opens a new cartridge with the six clarifying questions
- **TEMPLATE-negotiation-manifest.md** — manifest template
- **TEMPLATE-stakeholder-map.md** — Party-atom-bearing file template

Remaining to draft (in priority order):
- `04-CONCESSION-STRATEGY.md`
- `05-WARGAME-PROTOCOL.md`
- `06-SAFETY-AND-ROUTING.md` (the dedicated safety chapter)
- `07-POST-MORTEM-DISCIPLINE.md`
- Six more templates
- Root docs (README, INSTALL, OPERATOR-GUIDE, CONTRIBUTING, LICENSE, VERSION, CHANGELOG, .gitignore)
- The worked-example cartridge (fictional salary negotiation)

## Decisions Locked

None this session — artifact-draft sessions implement decisions; they don't lock new ones.

## Artifacts Touched

| Artifact | Action |
|----------|--------|
| `Artifacts/AI-BOOTSTRAP.md` | drafted |
| `Artifacts/00-START-HERE.md` | drafted |
| `Artifacts/01-NEGOTIATION-FOUNDATIONS.md` | drafted |
| `Artifacts/02-STAKEHOLDER-MAPPING.md` | drafted |
| `Artifacts/03-BATNA-AND-ZOPA.md` | drafted |
| `Artifacts/BOOTSTRAP-NEW-NEGOTIATION.md` | drafted |
| `Artifacts/TEMPLATE-negotiation-manifest.md` | drafted |
| `Artifacts/TEMPLATE-stakeholder-map.md` | drafted |

## Open Threads for Next Session

- [ ] Draft `04-CONCESSION-STRATEGY.md` — the analytical heart of the engine
- [ ] Draft `06-SAFETY-AND-ROUTING.md` — needs careful consideration of routing criteria
- [ ] Decide worked-example domain (salary negotiation vs vendor contract; leaning salary)
- [ ] WARGAME sub-mode decision: AI plays counter-party? Or reasons about paths?

## Quality Gates Checklist

- [x] Eight artifact drafts produced
- [x] Session log written
- [x] `_design-state.md` artifact status table updated
- [x] No new decisions to lock this session
- [x] Open Thread for next session

## Note for OV-design students

This cartridge stops mid-drafting deliberately. The five worked-example cartridges in OVE v1.0 demonstrate **the design process**, not finished shippable OVs. A real engagement would continue through more ARTIFACT-DRAFT sessions, then REVIEW, then SHIP-PREP. The cartridge here shows what the first four sessions look like — interview, schema design, cartridge shape, initial drafting — at full depth.

To complete this OV in a real engagement, you'd need approximately 6–10 more sessions to finish the remaining drafts, review them all, build the worked-example cartridge inside the new OV, and ship.
