---
type: Fleeting
timestamp: "2026-06-06T00:00:00Z"
Item_ID: ove-engine-05-writing-for-ai
title: "OVE Engine — 05 Writing for AI"
Date_Added: 2026-06-01
Date_Modified: 2026-06-06
Needs_Processing: false
doc_type: design-engine
role: writing-discipline
scope: subject-agnostic
updated: 2026-06-01
---

# 05 — WRITING FOR AI

> **Writing the prose that an AI will execute as instructions is different from writing prose for humans. Different conventions, different failure modes, different quality bar.**

## The four audiences of an OV's prose

Every line of prose in an OV is read by one of four audiences. Understand which before writing.

1. **The AI on session start** — reads bootstrap and engine files in full. Writes for this audience must be operational, unambiguous, ordered.
2. **The AI mid-session** — consults specific engine files on demand. Writes here must be retrieval-friendly with clear headers and self-contained sections.
3. **The user reading docs** — README, INSTALL, OPERATOR-GUIDE, CONTRIBUTING. Writes here must be explanatory, persuasive, lightly motivating.
4. **The user reading the cartridge** — manifests, state files, decision logs. Writes here must be terse, factual, scannable.

Don't blur the lines. README prose belongs in README, not in the engine. Engine prose belongs in the engine, not in README.

## Conventions for AI-facing prose

### Be operational, not theoretical

Don't write *"Consider the relationship between the user's goals and the schema."* Write *"Before locking the schema, ask the user to point to one example Item in this domain. If they can't, the Prototype is probably wrong — return to Q3."*

The AI is going to execute the prose. Make it executable.

### Use imperative voice

*"Read the file."* not *"The file should be read."*
*"Ask one question."* not *"Multi-bullet questionnaires are to be avoided."*

### Numbered steps for sequences; lists for sets

Sequences are ordered; sets are unordered. Use the right structure.

### Headers must reflect actual structure

The AI navigates by headers when consulting on demand. Headers must be descriptive enough to find without reading the body.

### State the negative as well as the positive

For every "do this," include "don't do that" where there's a known failure mode. The AI's default behavior is often the failure mode; the explicit "don't" prevents reversion.

### Reference other files explicitly

When a section depends on another file, link it: *"See `03-DESIGN-PROTOCOL.md` §4 for the audit-mode protocol."* The AI will follow the reference if needed.

### Use YAML frontmatter for machine-readable metadata

Every file the AI parses has YAML frontmatter at the top. Schemas and prototypes live in YAML. Prose lives in the body.

### Apply the universal conventions in frontmatter

When drafting any file with YAML frontmatter — whether it's a cartridge Item, an engine page, or a front-door doc for the new OV — apply the conventions in `_meta/CONVENTIONS.md`:

- Six Universal Core fields: `type`, `Item_ID`, `Title`, `Date_Added`, `Date_Modified`, `Needs_Processing`
- Property naming: prefix `lowercase_snake_case_`, body `Title_Snake_Case`, acronyms fully capitalized
- Enum identifiers in schema: lowercase plural

These are not subject-specific stylistic choices. They are vault-compatibility defaults that let the OV's output live alongside the operator's other notes without post-processing. If the operator has overridden the defaults during SCHEMA-DESIGN (logged in `_design-decisions.md`), apply the override instead.

### Don't write trivia

If the AI doesn't need it to do the work, leave it out. The context window is a public good.

## Conventions for user-facing prose

### README

- Lead with the one-line pitch
- Show the quick-start in the first screen
- Tell the user what to read next based on what they want to do
- Don't explain what you're building until they're invested

### INSTALL

- Step-by-step, minimal prose
- Anticipate the failure modes
- Provide a troubleshooting table

### OPERATOR-GUIDE

- Pattern: symptom → likely cause → fix
- Be specific about the failures users will actually hit
- Reference the engine sections where the underlying rule lives

### CONTRIBUTING

- Crisp distinction: what's in-scope vs. what requires a major version bump
- Be specific about file paths
- Voice and tone conventions stated explicitly

## Tone (applies across all prose)

**Defaults** (override per `_USER.md` if user prefers otherwise):

- **Peer register.** Adult-to-adult, not teacher-to-student.
- **Direct.** Substantive over encouraging.
- **No filler.** "Great question," "interesting," etc. are forbidden.
- **No flattery.** Strong work is called strong; weak work is called weak.
- **Minimal hedging.** When you're unsure, say so once and move on — don't pile up qualifiers.
- **No emojis.** Plain prose unless the user explicitly asks.

## Documented failure modes the writing must guard against

### F1 — Multi-bullet questionnaire

When opening a clarifying interview, the AI's natural failure is to dump a numbered list of 5–10 questions in one message. **This must not happen.**

The fix in the writing: every prompt that initiates an interview includes the literal instruction *"Ask one question at a time, conversationally."* The engine repeats this instruction in `BOOTSTRAP-NEW-OV.md`, in `03-DESIGN-PROTOCOL.md`, in `00-START-HERE.md`. Triple-redundant by design — this failure is documented, recurring, and worth the prose overhead.

### F2 — Fabrication of tools, frameworks, people, facts

When the OV-being-designed needs a reference (a methodology to extend, a tool to integrate, a thinker to cite), the AI's failure is to fabricate plausibly. **This must not happen.**

The fix in the writing: every section that involves naming external references includes *"If you are not certain a tool/framework/person/book exists in the form you describe, say so or decline to name it."*

### F3 — Identity inference from indirect signals

When the AI needs to write a name into a shippable artifact (LICENSE, README, attribution lines), the failure is to parse a username or path into a guessed real name. **This must not happen.**

The fix in the writing: the principle is stated in `02-DESIGN-PRINCIPLES.md` P7 and called out in `_meta/FAILURE-MODES.md`. Every template that includes a name field uses a `[USER NAME]` placeholder, not a guessed value.

### F4 — Engine drift into domain specifics

When writing engine files, the failure is to slip in domain-specific examples that become hardcoded. **This must not happen.**

The fix in the writing: examples in engine files come from a small fixed set (existing shipped OVs: SOLVE-eX, LifeLong-Learning, OVE itself; or generic domains: history, music, math, cuisine) and are always introduced as *"for example"* or *"in OV X, …"* — never as the canonical case.

### F5 — Schema slipping in through prose

The failure: writing a section that *implies* a schema constraint without making it explicit in the schema doc. **This must not happen.**

The fix: any structural rule the AI must enforce belongs in `_meta/SCHEMA-OF-SCHEMAS.md` or the OV's `_schema.md`, not buried in prose. If you find yourself writing a rule in prose, lift it to the schema doc.

### F6 — Drift between root mirror and engine canonical

Many OVs have both a root-level `AI-BOOTSTRAP.md` and an `00-START-HERE.md` inside the engine. The failure: these drift out of sync.

The fix: the root file is a thin pointer ("read the engine"); the engine file is canonical. Or the two are explicitly synchronized at every release with a check. Decide which pattern, document it, enforce it.

### F7 — Writing for the user when the AI is the reader

The failure: the engine starts with "In this section we will discuss…" — that's writing for a human reader of a textbook, not for an AI executing instructions. **The AI doesn't need to know what's coming; it needs to know what to do.**

The fix: cut all meta-prose about what the section is going to do. Open with the operational directive.

## Quality checks before committing prose

For engine files:

- [ ] Can a fresh AI follow this without prior context? (Test by reading top-to-bottom as if for the first time.)
- [ ] Are the failure modes explicit?
- [ ] Are cross-references to other files specific (file + section)?
- [ ] Is the imperative voice consistent?
- [ ] Is there any meta-prose ("In this section…") that should be cut?

For user-facing files:

- [ ] Does the first screen contain enough for the user to start?
- [ ] Is the quick-start under 5 lines?
- [ ] Is the troubleshooting table representative of actual user failures?
- [ ] Is the prose readable aloud without sounding stilted?

If any check fails, revise.
