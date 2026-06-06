---
Item_Prototype: OVE_Design_State
Item_ID: "negotiation-prep-state"
Title: "Negotiation-Preparation — Design State"
Date_Added: 2026-06-01
Date_Modified: 2026-06-01
Needs_Processing: false
ove_OV_Name: "Negotiation-Preparation"
ove_Design_Phase: artifact-draft
ove_Sessions_Completed: 4
ove_Last_Session_Date: 2026-06-01
ove_Next_Session_Default_Activity: ARTIFACT-DRAFT
---

# Negotiation-Preparation — Design State

> **Single source of truth for this design engagement. The AI reads at session start, writes at session end.**

## Current Design Phase

- **Phase:** artifact-draft
- **Phase entry date:** 2026-06-01 (Session 003)
- **Sessions completed:** 4

## Decided (locked choices)

From `_design-decisions.md`:

- **Cartridge = a specific negotiation** (one negotiation per cartridge)
- **Five atom types:** Party (stakeholder), Issue, Concession-Asset, Tactic, Pattern
- **Six custom activities** beyond OVE's set: STAKEHOLDER-MAP, BATNA-ANALYSIS, ISSUE-FRAMING, CONCESSION-PLAN, WARGAME, POST-MORTEM
- **Cartridge lifecycle stages:** prep / live / post-mortem / closed
- **Safety routing:** explicit chapter on when to stop and route to a lawyer or therapist
- **License:** CC-BY 4.0 (matching the OVE ecosystem)

## Open (questions still in play)

- Do `Pattern` atoms live at the cartridge level (this negotiation's patterns) or at the OV level (cross-negotiation patterns)? Leaning OV-level with cartridge-level pattern-instances.
- Whether to ship a `_TEMPLATE` cartridge that demonstrates a worked-out fictional negotiation, or just an empty cartridge skeleton. Leaning toward worked-out fictional (salary negotiation).
- Whether the WARGAME activity should structurally include the AI playing the counter-party, or just reasoning about likely paths. Leaning toward configurable (user picks).

## Artifact Status

| Artifact | Status |
|----------|--------|
| `AI-BOOTSTRAP.md` | drafted |
| `_negotiation-engine/00-START-HERE.md` | drafted |
| `_negotiation-engine/01-NEGOTIATION-FOUNDATIONS.md` | drafted |
| `_negotiation-engine/02-STAKEHOLDER-MAPPING.md` | drafted |
| `_negotiation-engine/03-BATNA-AND-ZOPA.md` | drafted |
| `_negotiation-engine/04-CONCESSION-STRATEGY.md` | not-started |
| `_negotiation-engine/05-WARGAME-PROTOCOL.md` | not-started |
| `_negotiation-engine/06-SAFETY-AND-ROUTING.md` | not-started |
| `_negotiation-engine/07-POST-MORTEM-DISCIPLINE.md` | not-started |
| `_negotiation-engine/BOOTSTRAP-NEW-NEGOTIATION.md` | drafted |
| Templates (8 expected) | drafting (2 of 8 done) |
| Root docs | not-started |
| Worked-example cartridge (fictional salary negotiation) | not-started |

## Recent Sessions

- [[2026-06-01_004_ARTIFACT-DRAFT]]
- [[2026-06-01_003_CARTRIDGE-SHAPE]]
- [[2026-06-01_002_SCHEMA-DESIGN]]
- [[2026-06-01_001_INTERVIEW]]

## Open Threads (to address next session)

- [ ] Draft `04-CONCESSION-STRATEGY.md` — the analytical heart of the engine
- [ ] Draft `06-SAFETY-AND-ROUTING.md` — needs careful consideration of legal/therapeutic boundaries
- [ ] Decide whether the worked example is a salary negotiation or vendor contract (lean salary; more relatable)

## Schema Q1–Q13 Status

| Question | Answered? |
|----------|-----------|
| Q1 — Knowledge kinds | ✅ Decisional + relational + conceptual + procedural |
| Q2 — Canonical authorities | ✅ Multiple frameworks; no single canon |
| Q3 — Smallest unit | ✅ Party / Issue / Concession-Asset / Tactic / Pattern |
| Q4 — Relationships | ✅ wants / fears / can-give / threatens / aligns-with / mirrors |
| Q5 — Natural progression | ✅ prep → live → post-mortem (life-cycle), not curricular |
| Q6 — Mastery endpoint | ✅ Better outcomes + improving across cartridges |
| Q7 — Custom activities | ✅ Six (STAKEHOLDER-MAP, BATNA-ANALYSIS, ISSUE-FRAMING, CONCESSION-PLAN, WARGAME, POST-MORTEM) |
| Q8 — Mastery scale | ✅ Per-pattern (recognized / applied / mastered) rather than per-atom |
| Q9 — Cartridge represents | ✅ A specific negotiation |
| Q10 — Backbone files | ✅ See decisions doc |
| Q11 — State-persistence | ✅ See decisions doc |
| Q12 — Templates list | ✅ Eight |
| Q13 — Bootstrap protocol | ✅ Drafted (`BOOTSTRAP-NEW-NEGOTIATION.md`) |
