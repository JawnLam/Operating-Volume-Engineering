---
type: OVE_Schema_Draft
timestamp: "2026-06-01T00:00:00Z"
Item_ID: "solve-ex-retrospective-schema-draft"
title: "SOLVE-eX — Reverse-Engineered Schema"
Date_Added: 2026-06-01
Date_Modified: 2026-06-01
Needs_Processing: false
ove_OV_Name: "SOLVE-eX"
ove_Schema_Status: shipped
---

# SOLVE-eX — Reverse-Engineered Schema

> **Q1–Q13 from `_design-engine/04-SCHEMA-DESIGN.md`, answered retrospectively for SOLVE-eX. This is what the shipped OV's schema would look like if it had been designed using OVE's protocol.**

## Q1 — Kinds of knowledge or work

- **Decisional** (primary) — choices under uncertainty, tradeoffs, reversibility analysis
- **Conceptual** (high) — frameworks, models, structured-thinking techniques
- **Procedural** (medium) — applying the right tool at the right moment
- **Relational** (medium) — stakeholder dynamics, power, leverage
- **Operational** (low) — checklists, sequences
- Minimal: formal/propositional, declarative, experiential, creative

## Q2 — Canonical authorities

Yes. Two layers:

- **Tool authors / framework originators** — Eisenhower, Pareto, Goldratt, etc. (cited in tool entries; not first-class atoms)
- **Operational personas** — Partner, Counselor, Therapist, Guide, Consultant (first-class atoms in `05-Personas/`)

## Q3 — Smallest quizzable / actionable unit

A **tool application** — applying a specific structured-thinking tool to a specific case-file context within a specific phase-step. The tool itself is the static unit; the application is the dynamic unit captured in the case file.

## Q4 — Relationships between atoms

- `applied-in` — tool → case file
- `appropriate-for` — tool → phase-step
- `prerequisite-of` — phase-step → phase-step
- `escalates-to` — situation → safety-route (chapter 9)
- `belongs-to-phase` — tool → phase
- `clarifies` — question-bank-entry → clarification-need

## Q5 — Natural progression

Yes — the 21-step process framework (6 phases × ~3.5 steps). Phases are ordered; within a phase, steps are mostly ordered with some flexibility. Different problems may enter at different phases (a Phase-3 problem can be diagnosed and entered there directly).

## Q6 — Mastery / completion endpoint

A closed Case File that captures:

1. The user's situation framed clearly
2. The diagnostic state (where in the process framework)
3. The tools applied and what they surfaced
4. Conclusions reached
5. An actionable plan with reversibility analysis

The Case File itself is the deliverable.

## Q7 — Custom session activities

The shipped OV uses the SOLVE-eX-specific 21 process steps as its activity model rather than a small set of universal activities. Each step has trigger conditions in the diagnostic loop (chapter 03). This is **structurally different from LLL's six-activity model** — SOLVE-eX has many smaller activities; LLL has fewer larger ones.

## Q8 — Mastery scale

Not directly applicable in the standard 0–5 sense. SOLVE-eX uses a *case file state* progression (framing → diagnosis → tool application → synthesis → decision → execution-plan → review) rather than mastery levels per atom.

## Q9 — What does a cartridge represent?

A **Case File** — one specific problem or decision the user is working through. Lives in `06-Case-Files/_ACTIVE/`. Closed cases move to `_ARCHIVED/`.

## Q10 — Cartridge backbone files

A Case File is a single markdown document (not a folder), with:

- Frontmatter: case ID, stage, stakes, modes
- Body sections: framing, current state, tools applied, decisions made, open questions, action plan
- Schema-validated against v1.14.0

This is **structurally lighter than LLL or OVE cartridges** — a Case File is a single file, not a folder. The choice matches the case-shaped nature of the work.

## Q11 — State-persistence contract

- **Case File:** Mode D (append-friendly with sections). Frontmatter overwrites; body sections append.
- **Engine files (chapters):** Mode C (overwrite at release).
- **Tool entries:** Mode E (immutable after schema validation).
- **Sample sessions:** Mode E (immutable).
- **Sprint archives:** Mode E (immutable, in `99-Archive/`).

## Q12 — Templates list

- `06-Case-Files/_TEMPLATE.md` — the case file template
- Tool-entry template (in `08-Schema/`)
- Sample-session template (in `09-Sample-Sessions/`)

Note: SOLVE-eX has *fewer* templates than LLL because most artifacts are already-curated content (677 tool entries don't need a new template). The Case File template is the main user-facing one.

## Q13 — Bootstrap-new-cartridge protocol

The AI opens a new Case File when the user describes a new problem. The bootstrap is implicit in chapter 02 (the bootstrap protocol) and the diagnostic loop (chapter 03). There isn't a separate `BOOTSTRAP-NEW-CASE-FILE.md` because the entry pattern is "user describes problem → AI opens case file."

This is **lighter than OVE's BOOTSTRAP-NEW-OV** because the case file creation is part of normal session flow, not a special mode.

## How the schema would look if redesigned today using OVE

The shipped schema is largely correct, but redesigning today through OVE would surface:

1. **Personas could be a more explicit Layer 2 schema element.** Currently they're documented in `05-Personas/` but not formally part of the schema. OVE's `_meta/SCHEMA-OF-SCHEMAS.md` pattern would lift personas to a schema-level concept.

2. **The 21 process steps blur the line between activity and atom.** OVE's six-activity model would suggest collapsing some steps into broader activities, treating individual steps as atoms within activities. This is a real tension worth weighing.

3. **The schema-validated tool entries are exemplary.** This is the gold standard for an OV's content corpus. Future OVs should emulate.

4. **The voice-neutrality lint is exemplary but heavier than most OVs need.** Document the trade-off explicitly: regex enforcement is appropriate when voice failures have high blast radius (public-facing AI conversations); skip it for private-use OVs.
