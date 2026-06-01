---
type: design-engine
role: schema-design-protocol
scope: subject-agnostic
updated: 2026-06-01
---

# 04 — SCHEMA DESIGN

> **How to design the schema of a new operating volume. This is the most important creative act of OV design. A bad schema produces a stilted OV; a good schema disappears into the work.**

## What "schema" means in an OV

A schema is the structural contract every artifact in the OV conforms to. It defines:

1. **The atom types** — the unit(s) of knowledge or work the OV produces (a "concept" in LLL, a "case file" in SOLVE-eX, a "design decision" in OVE)
2. **The relationships** — how atoms link to each other
3. **The state model** — what state files exist, what they own
4. **The cartridge backbone** — what every cartridge has at minimum
5. **The session log structure** — how work is recorded
6. **The custom activities** — anything beyond the universal session-protocol activities

A well-designed schema makes the work feel natural; a poorly-designed schema forces the user to bend the work to fit.

## The Q1–Q8 protocol

Walk through these with the user, one at a time, conversationally. Don't rush.

### Q1 — What kind of knowledge or work does this OV consist of?

Choose all that apply, with relative weights:

- **Formal/propositional** (theorems, definitions, rules)
- **Conceptual** (ideas, frameworks, theories)
- **Procedural** (techniques, skills, methods)
- **Declarative/factual** (names, dates, data)
- **Experiential** (embodied, tacit, practiced)
- **Creative/interpretive** (works, performances, compositions)
- **Decisional** (choices under uncertainty, tradeoffs)
- **Relational** (people, dynamics, histories)
- **Operational** (recurring procedures, checklists)

The mix shapes everything downstream.

### Q2 — Who or what is the canonical authority in this domain?

Some domains have named experts (cybernetics has thinkers; philosophy has philosophers). Some have traditions (cuisine has regional traditions). Some have institutions (law has courts and codes). Some have none.

This question determines whether you need a "thinker" or "authority" atom type.

### Q3 — What is the smallest quizzable / actionable / discussable unit?

That's the atomic unit of this OV. Anything smaller is a fragment; anything larger should decompose.

Examples:
- LLL: a concept (or a piece, a kanji, a technique, etc. — varies by subject cartridge)
- SOLVE-eX: a tool application within a case file
- OVE: a design decision

### Q4 — What relationships exist between atoms?

Pick a vocabulary of named relations. Common patterns:

- Hierarchical: `contains` / `part-of`
- Sequence: `precedes` / `follows`
- Causal: `causes` / `caused-by`
- Reference: `originated-by` / `analyzed-by` / `cited-by`
- Logical: `prerequisite-of` / `instantiates` / `contrasts-with`
- Lateral: `related-to`

The relationships become wiki-links in atom bodies and structured fields in frontmatter.

### Q5 — Does the domain have a natural progression?

Some domains have strict prerequisite order (math). Some are lateral (cuisine). Some have phases (a study curriculum, a project lifecycle, a negotiation timeline).

This shapes the **cartridge progression** (curriculum, phases, stages, or none).

### Q6 — What does "done" look like?

Concretely, what is the user trying to be able to *do* at the end of this kind of engagement? Be specific.

This question is harder than it looks. "Mastery" or "completion" is too vague. The mastery endpoint should be **observable** — a specific kind of artifact, demonstrated behavior, or measurable outcome.

### Q7 — What subject-specific session activities are needed?

The six universal OVE activities (INTERVIEW, SCHEMA-DESIGN, CARTRIDGE-SHAPE, ARTIFACT-DRAFT, REVIEW, SHIP-PREP) work for OVE itself. The OV you're designing may need different activities.

Examples from existing OVs:
- LLL: TEACH, QUIZ-SR, QUIZ-SOCRATIC, REVIEW-WEAK, SYNTHESIZE, INTEGRATE
- SOLVE-eX: implicit in its 21-step process framework
- A negotiation-prep OV might have: STAKEHOLDER-MAP, BATNA-ANALYSIS, ROLE-PLAY, POST-MORTEM
- A writing OV might have: OUTLINE, DRAFT, REVISE, EDITORIAL-REVIEW
- A relational OV might have: TOUCH-LOG, CONTEXT-REFRESH, ANNUAL-AUDIT

Define each custom activity with its trigger conditions.

### Q8 — What's the right mastery / progress scale?

Default 0–5 (not-started → introduced → recognized → applied → mastered → teachable) works for most domains. Some need different scales:

- Language: CEFR (A1–C2)
- Skill: novice → apprentice → journeyman → master
- Project: not-started → drafting → review → polish → shipped
- Decision: framing → analysis → choice → execution → review

Pick what fits the domain.

## Beyond Q1–Q8 — additional schema questions

Once Q1–Q8 are answered, work through these:

### Q9 — What does a cartridge represent?

In LLL: a subject being studied. In SOLVE-eX: a problem being worked through. In OVE: an OV being designed. In a negotiation OV: a specific negotiation. In a writing OV: a specific manuscript-in-progress.

This is the **central abstraction** of the OV. Get it wrong and the whole shape feels off.

### Q10 — What cartridge backbone files exist?

At minimum, every cartridge needs:
- A **manifest** — what this engagement is, who it's for, scope, goals
- A **state file** — current position, decisions, open threads
- A **session record** — what happened across sessions

Beyond those, what else needs its own dedicated file? (Schema draft? Decision log? Curriculum? Reading list?)

### Q11 — What is the state-persistence contract?

For each backbone file: is it overwritten, append-only, or hybrid? What gets written when? See `06-STATE-PERSISTENCE.md`.

### Q12 — What templates ship with the OV?

Templates scaffold the work. Every atom type needs one. Every artifact-kind (session log, quiz, journal, draft) needs one.

### Q13 — What's the bootstrap-new-cartridge protocol?

This is the OV's analog to `BOOTSTRAP-NEW-OV.md`. It's the prompt the AI follows to open a new cartridge from a user request.

## Required sections of the new OV's `_schema.md`

The new OV's schema document must contain:

1. **Domain identity** — name, shape (Q1 categories), summary
2. **Answers to Q1–Q13** — the analytical answers that justify the design
3. **Atom type definitions** — frontmatter, required body sections, naming, location
4. **Relationship vocabulary** — the named relations
5. **Mastery / progress scale** — default or custom
6. **Custom session activities** — with trigger conditions
7. **Cartridge backbone** — files, content contracts
8. **State-persistence contract** — per file
9. **Templates list** — what ships in `_templates/`
10. **Folder structure** — how cartridges are organized

## How to know the schema is good

Run these checks before locking the schema:

- [ ] Could you describe an example atom in this domain that fits naturally? (If not, the atom types are off.)
- [ ] Are the relationships sufficient to express how atoms actually link in your head?
- [ ] Does the cartridge analog match how the user *thinks* about the work, not just how it's structured on disk?
- [ ] Would a user-domain-expert recognize this schema as "yes, that's how this domain works"?
- [ ] Does it pass the **self-similarity test**? Could OVE itself be designed using this schema? (For OVE: trivially yes. For other OVs: not always relevant, but a useful sanity check.)

If any check fails, iterate. Schema design is the most important creative work in OV design — taking an extra session here pays back across the OV's entire lifetime.
