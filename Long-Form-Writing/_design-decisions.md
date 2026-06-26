---
type: OVE_Design_Decisions
timestamp: "2026-06-01T00:00:00Z"
Item_ID: "long-form-writing-decisions"
title: "Long-Form-Writing — Design Decisions Log"
Date_Added: 2026-06-01
Date_Modified: 2026-06-01
Needs_Processing: false
ove_OV_Name: "Long-Form-Writing"
---

# Long-Form-Writing — Design Decisions Log

## Decisions

### 2026-06-01 — Decision 1: Cartridge = one manuscript-in-progress

**Decided:** Each cartridge represents one specific long-form manuscript: a book, a dissertation, a screenplay, a play. Cartridge naming: `<Working-Title>-<Genre>/`. E.g., `The-Empire-Question-NonFic/`, `Pho-Recipe-Memoir-Memoir/`.

**Alternatives considered:**
- One cartridge per writer (rejected: multiple manuscripts collide; voice differs per project)
- One cartridge per genre (rejected: too coarse; specific manuscripts need state)
- One cartridge per chapter (rejected: too granular; loses macro-structure)

**Rationale:** Manuscripts are the unit of long-form work. Each has its own voice, structure, characters/threads, research, history.

---

### 2026-06-01 — Decision 2: Daily-practice cadence

**Decided:** The session protocol accommodates daily writing sessions (15–90 min typical). This differs from SOLVE-eX (episodic), Negotiation-Prep (per-event), and LLL (3–5 hrs/week-ish). The OV needs activities that fit a short-but-frequent rhythm.

**Alternatives considered:**
- Weekly cadence (rejected: long-form writers typically work daily or near-daily)
- No assumed cadence (rejected: protocol assumes some pacing model; "no cadence" produces no rhythm)

**Rationale:** Long-form work depends on momentum. Daily-or-near-daily is the canonical writer's discipline.

**Implications:** Session activities need short-form variants. State updates need to be cheap. The "session log" might be more like a "daily log."

---

## Open decisions (not yet locked)

- **D3 (open):** Fiction-and-non-fiction-and-screenplay in one OV, or separate OVs per genre? Leaning toward one OV with per-cartridge genre-specific schema variations (the cartridge specifies `genre: fiction | non-fiction | screenplay | play` and the schema branches).
- **D4 (open):** Atom types — exact split for Scene/Chapter/Section. Likely depends on D3.
- **D5 (open):** How does the engine handle voice consistency? Possibilities: (a) voice samples stored in the cartridge as reference; (b) per-session voice-check; (c) writer-only (engine doesn't try).

## Patterns worth surfacing

1. **Cadence shape varies dramatically by domain.** Each OV needs a deliberate decision about pacing.
2. **Manuscript-as-cartridge** is a generative pattern transferable to any long-form creative or scholarly work (academic papers, business plans, RFPs, anything multi-month).
