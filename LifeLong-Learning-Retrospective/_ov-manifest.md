---
Item_Prototype: OVE_OV_Manifest
Item_ID: "lll-retrospective-manifest"
Title: "LifeLong-Learning — Retrospective Design Analysis"
Date_Added: 2026-06-01
Date_Modified: 2026-06-01
Needs_Processing: false
ove_OV_Name: "LifeLong-Learning"
ove_OV_Slug: "lifelong-learning"
ove_Design_Phase: shipped
ove_User_Name: "Jawn Lam"
ove_Bootstrapped: 2026-06-01
ove_Engagement_Kind: retrospective
---

# LifeLong-Learning — Retrospective Design Analysis

> **This cartridge analyzes LifeLong-Learning (v1.0.0, [github.com/JawnLam/LifeLong-Learning](https://github.com/JawnLam/LifeLong-Learning)) as if it had been designed using this OVE.**

## What this OV is

LifeLong-Learning (LLL) is an operating volume for AI-assisted self-directed deep study. The user picks a subject they want to master, points an AI at the folder, tells it to read `AI-BOOTSTRAP.md`, and the AI designs a curriculum, runs study sessions, and tracks progress over months or years.

Key features:

- A subject-agnostic teaching engine
- Per-subject *cartridges* (cybernetics, Roman Empire, language X, cooking, etc.)
- Six universal session activities (TEACH, QUIZ-SR, QUIZ-SOCRATIC, REVIEW-WEAK, SYNTHESIZE, INTEGRATE)
- A schema that adapts per subject through a Q1–Q8 design protocol
- Multi-phase curricula (typically 4–6 phases per subject)
- Synthesis cadence (weekly journals, monthly essays, phase-end translations, quarterly drafts)
- Spaced-repetition support via the user's SR tool of choice

## Why this user designed it

The author wanted a way to take on serious subjects (cybernetics, history, language, etc.) with AI assistance, while owning their notes in plain markdown and avoiding lock-in to any specific AI vendor's product. Existing options (Anki for SR, Obsidian for notes, ChatGPT for tutoring) didn't compose into a single coherent multi-session system.

## Who is this for

Public release. Designed for any adult, self-directed learner who wants to study something seriously over weeks, months, or years with AI partnership.

## Domain shape

- **Conceptual** (primary) — frameworks, theories, ideas
- **Declarative/factual** (high) — names, dates, vocabulary
- **Creative/interpretive** (medium) — synthesis output
- **Procedural** (medium) — applies for skill-based subjects via custom atom types
- Lighter: experiential, decisional, relational

## Cadence

Variable per subject. Typically 3–5 hours/week per subject, over 6–24 months.

## Multi-session evidence

Very strong. Study unfolds over months. Spaced repetition is inherently multi-session. Synthesis cadence is multi-week (weekly → monthly → phase-end → quarterly).

## Output target

Multiple. Per session: a session log + atom updates. Per week: a journal. Per month: an essay. Per phase: a translation piece. Per quarter: a public-facing draft. Across the study: a body of synthesis work that can become a book, course, framework, or portfolio.

## Prior art

The author drew from andragogy (Knowles), spaced repetition (the SuperMemo lineage via Anki), and the structured-knowledge tradition in Obsidian / second-brain communities. The teaching engine's tone draws from rigorous adult-education traditions.

## Stakes and safety

Low to medium. The user is studying for their own development; failure mode is wasted time, not harm. Some subjects might overlap with sensitive content (medical, legal); the system doesn't have formal safety routing the way SOLVE-eX does.

## Communication preferences

Peer register, substantive critique, no flattery. Adapted from the author's own learning style — *"The user is a peer. Do not condescend. Press hard on conceptual soft spots."*

## Scope boundaries

Not a tutor for accredited coursework (no formal assessment). Not a substitute for a domain expert when one is available. Not opinionated about what subjects the user should study.

## Notes for future OV designers

LLL is the most flexibly-schema-bearing OV in this trio. Its key innovations:

1. **The cartridge-as-subject pattern.** A cartridge is a complete subject-of-study, with its own custom atom types defined per-subject. This is the most powerful demonstration that one OV can serve many domains.
2. **Q1–Q8 schema design protocol.** Forced the per-subject schema to be a deliberate design exercise, not a copy-paste. Adopted in OVE's Q1–Q13 protocol.
3. **Six universal activities + per-subject custom activities.** Right balance between standardization and flexibility. Music gets COOK-ALONG-equivalent; cybernetics gets standard six only.
4. **Synthesis cadence at four time-scales.** Weekly / monthly / phase-end / quarterly is opinionated but defensible. Other OVs with long-running engagements should consider similar cadence structures.
5. **No platform lock.** Works in Obsidian (with SR plugin), Claude Code, ChatGPT, anywhere markdown reads.
