---
Item_Prototype: OVE_OV_Manifest
Item_ID: "solve-ex-retrospective-manifest"
Title: "SOLVE-eX — Retrospective Design Analysis"
Date_Added: 2026-06-01
Date_Modified: 2026-06-01
Needs_Processing: false
ove_OV_Name: "SOLVE-eX"
ove_OV_Slug: "solve-ex"
ove_Design_Phase: shipped
ove_User_Name: "Jawn Lam"
ove_Bootstrapped: 2026-06-01
ove_Engagement_Kind: retrospective
---

# SOLVE-eX — Retrospective Design Analysis

> **This cartridge analyzes SOLVE-eX (v2.1.0, [github.com/JawnLam/SOLVE-eX](https://github.com/JawnLam/SOLVE-eX)) as if it had been designed using this OVE. The artifact already exists and shipped publicly; the goal here is to surface its design choices so future OV designers (including the author) can learn from them.**

## What this OV is

SOLVE-eX is an operating volume for structured decision-making and problem-solving. The corpus consists of:

- 14 instruction chapters (the operating manual)
- 677 thinking-tool entries (a curated library of structured-thinking techniques, each with a frozen schema)
- A 21-step process framework (6 phases × ~3.5 steps)
- Five operational personas with switching rules
- Question banks indexed by phase-step and clarification need
- Application patterns
- Case files (the cartridge analog) where session work accumulates
- Schema definitions, validation scripts (optional), sample sessions, reference material

The user points an AI at the folder, tells it to read `AI-BOOTSTRAP.md`, and the AI walks them through structured thinking on whatever is in front of them.

## Why this user designed it

The author was looking for a way to bring rigorous decision-making discipline into AI-assisted thinking sessions. Existing approaches (prompts, custom GPTs) didn't carry the structural depth needed for high-stakes problem-solving with proper safety routing.

## Who is this for

Public release. Designed for any individual using a capable AI assistant who wants structured thinking applied to decisions, problems, or stuck situations.

## Domain shape

- **Decisional** — choices under uncertainty
- **Conceptual** — frameworks, theories, structures
- **Procedural** — applied technique
- Lighter: relational, operational, declarative

## Cadence

Episodic. Used when a specific decision or problem is in front of the user.

## Multi-session evidence

Strong. Case files persist across sessions; complex problems unfold over weeks; the AI must re-establish context every time.

## Output target

A Case File capturing the user's situation, the diagnostic state, the tools applied, the conclusions reached, and an actionable plan. The Case File is itself the deliverable.

## Prior art

The author's background in management consulting (structured-thinking frameworks, change-management, executive influence) informs both the tool library and the personas.

## Stakes and safety

High-stakes. The user may bring decisions involving career, money, relationships, geography. Chapter 9 (Safety and Stakes) handles routing to professionals (therapists, lawyers, doctors, etc.) when warranted.

## Communication preferences

Peer register, substantive critique, no flattery, voice-neutrality discipline (Chapter 13 enforces strict bans on filler, composition-meta, and adjective injection).

## Scope boundaries

Not a therapist. Not a lawyer. Not a marketing pitch. Not opinionated about what the user should decide.

## Notes for future OV designers

SOLVE-eX is the most institutionally-mature OV in this trio. Its key innovations:

1. **Frozen schema with versioning policy.** v3.0 STABLE master plan + v1.14.0 schema FROZEN. Any change requires explicit version bump and migration. Other OVs should adopt this discipline.
2. **Validation scripts that enforce the schema.** Optional but powerful — the schema is testable, not just documented.
3. **Persona switching rules.** Five distinct operational personas (Partner, Counselor, Therapist, Guide, Consultant) with explicit switching protocol. Heavier than most OVs need but powerful when the domain warrants it.
4. **Voice-neutrality lint.** Chapter 13's regex enforcement of forbidden voice patterns is the most aggressive prose-discipline mechanism in any OV. Worth studying as an upper bound.
5. **Case File template as the cartridge.** Each Case File is structurally identical, schema-validated, and reusable as a teaching example after anonymization.
