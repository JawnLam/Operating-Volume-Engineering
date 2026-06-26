---
type: OVE_Schema_Draft
timestamp: "2026-06-01T00:00:00Z"
Item_ID: "lll-retrospective-schema-draft"
title: "LifeLong-Learning — Reverse-Engineered Schema"
Date_Added: 2026-06-01
Date_Modified: 2026-06-01
Needs_Processing: false
ove_OV_Name: "LifeLong-Learning"
ove_Schema_Status: shipped
---

# LifeLong-Learning — Reverse-Engineered Schema

## Q1 — Kinds of knowledge or work

- **Conceptual** (primary, but varies)
- **Declarative/factual** (high, varies)
- **Creative/interpretive** (medium — through synthesis)
- **Procedural** (medium — for skill-based subjects)
- The mix shifts per subject

## Q2 — Canonical authorities

Varies per subject. Cybernetics has canonical thinkers (Wiener, Ashby, Beer); cuisine has traditions; math has theorems; languages have native-speaker corpora. The OV accommodates this through the per-subject `_subject.md` and the optional `thinker` atom type.

## Q3 — Smallest unit

An **atom** — generalizes across subjects. Cybernetics atoms are concepts and thinkers; cuisine atoms are techniques and ingredients; languages have kanji and grammar patterns.

## Q4 — Relationships between atoms

Generic relationship vocabulary defined per-subject in `_schema.md`. Common: prerequisite-of, related-to, contrasts-with, originated-by, developed-by, applied-by.

## Q5 — Natural progression

Per-subject. Some subjects have strict prerequisite order (math); some are lateral (cuisine); most have a multi-phase structure (4–6 phases) reflected in the `_curriculum.md`.

## Q6 — Mastery / completion endpoint

Per-subject. Defined concretely in `_subject.md` — *"the user can [demonstrate X]"* rather than *"the user has read Y books."* Per-subject `_state.md` tracks atom-level mastery on the 0–5 scale.

## Q7 — Custom session activities

Six universal activities (TEACH, QUIZ-SR, QUIZ-SOCRATIC, REVIEW-WEAK, SYNTHESIZE, INTEGRATE) cover most subjects. Per-subject custom activities allowed (COOK-ALONG, SPEAK, PROVE, COMPOSE, PERFORM) when the domain demands them.

## Q8 — Mastery scale

Default 0–5 (not-introduced → introduced → recognized → explained → applied → taught). Custom scales allowed (CEFR for languages, novice-apprentice-journeyman-master for skills).

## Q9 — What does a cartridge represent?

A **subject being studied**. One folder per subject. Self-contained: own schema, curriculum, state, atoms, sources, sessions, synthesis.

## Q10 — Cartridge backbone files

- `_subject.md` — manifest (what, why, for whom, prior knowledge, communication preferences)
- `_schema.md` — per-subject atom definitions
- `_curriculum.md` — phase roadmap
- `_state.md` — current progress (source of truth)
- `Atoms/` — the atoms organized per the schema
- `Sources/` — external material (books, papers, videos, etc.)
- `Sessions/` — session logs
- `Quizzes/` — quiz history + SR performance log
- `Synthesis/` — weekly / monthly / phase-end / quarterly
- `SR-Cards/` — optional dedicated SR card files

## Q11 — State-persistence contract

- `_state.md` — Mode C (overwrite at session end)
- `_subject.md`, `_schema.md`, `_curriculum.md` — Mode C (overwrite when changes warrant)
- `Atoms/*.md` — Mode D (append-friendly; atom notes grow as mastery increases)
- `Sessions/*.md` — Mode E (immutable after creation)
- `Quizzes/Socratic-Conceptual/*.md` — Mode E (immutable)
- `Quizzes/SR-Performance-Log/Phase-N-SR-Log.md` — Mode A (append-only)
- `Synthesis/*/*.md` — Mode D until shipped, then Mode E

## Q12 — Templates list

Ten templates in `_teaching-engine/_templates/`:
- `TEMPLATE-Atom-Generic.md`
- `TEMPLATE-Session.md`
- `TEMPLATE-State.md`
- `TEMPLATE-Source.md`
- `TEMPLATE-Quiz.md`
- `TEMPLATE-SR-Log.md`
- `TEMPLATE-Weekly-Journal.md`
- `TEMPLATE-Monthly-Essay.md`
- `TEMPLATE-Phase-End.md`
- `TEMPLATE-Quarterly-Draft.md`

## Q13 — Bootstrap-new-cartridge protocol

`BOOTSTRAP-NEW-SUBJECT.md` in the engine. Walks the user through eight clarifying questions (subject name, why, prior knowledge, goals, time commitment, depth, scope boundaries, modality preferences) before designing the schema, curriculum, and seed atoms.

## How the schema would look if redesigned today using OVE

LLL's schema is well-built. Redesigning today through OVE would mostly validate the existing choices but surface a few refinements:

1. **The universal atom-generic template is broad enough to be slightly underspecified.** It works because per-subject schemas tighten it; a stricter universal could surface schema bugs earlier.

2. **The synthesis cadence is opinionated — possibly worth flagging more explicitly that other cadences are valid.** A user studying for a deadline might want denser synthesis; one studying casually might want sparser.

3. **No formal safety routing.** SOLVE-eX has it; LLL doesn't. For most learning subjects this is fine, but a study cartridge on a sensitive subject (medical, legal, psychological) could benefit from optional escalation routing. Worth flagging as a v1.x addition.

4. **The "operator-confirmed identity" rule is now stronger** post the John-vs-Jawn correction (2026-06-01). LLL's shipped engine handled this correctly in the abstract (user identity in `_USER.md`/`_subject.md` only), but the rule could be more prominent.

5. **Self-similarity test passes cleanly.** OVE can re-design LLL. Both share the cartridge-and-engine pattern; LLL's per-cartridge schema becomes OVE's per-OV schema at the meta level. The recursion works.
