---
type: design-engine
role: cartridge-bootstrapping-prompt
scope: subject-agnostic
updated: 2026-06-01
---

# BOOTSTRAP A NEW OV (Open a Design Cartridge)

> **You are an AI assistant (Claude, Gemini, ChatGPT, or other capable model). The user has asked you to help design a new operating volume. This document is your complete execution plan. Follow it end-to-end. Ask clarifying questions one at a time before building.**

## What you're producing

A complete design cartridge inside `Operating-Volume-Engineering/` (this folder) for the OV being designed. Once the cartridge is complete and the design is finalized, the user will copy the artifacts into a new folder elsewhere on disk — that becomes the shipped OV.

A complete design cartridge includes:

1. `_ov-manifest.md` — what this new OV is, who it's for, scope
2. `_design-state.md` — current design state
3. `_design-decisions.md` — log of locked decisions and rationale
4. `_schema-draft.md` — the answers to Q1–Q13 from `04-SCHEMA-DESIGN.md`
5. `Sessions/` — session logs accumulating across design conversations
6. `Artifacts/` — drafts of every file the new OV will ship with

## Before you start

Read these files in order:

1. `00-START-HERE.md`
2. `01-WHAT-IS-AN-OV.md`
3. `02-DESIGN-PRINCIPLES.md`
4. `03-DESIGN-PROTOCOL.md`
5. `04-SCHEMA-DESIGN.md`
6. `05-WRITING-FOR-AI.md`
7. `06-STATE-PERSISTENCE.md`
8. `07-SHIPPING-CHECKLIST.md`
9. All files in `_templates/`
10. The five worked-example cartridges (at minimum, the manifest of each) — use them as reference implementations

Do not proceed without reading these.

## Clarifying questions you must ask the user

Before creating any files, ask the user the following. **One question at a time, conversationally.** Wait for each answer, probe if it's thin, then ask the next.

This is **non-negotiable**. A multi-bullet questionnaire is a documented failure mode (`_meta/FAILURE-MODES.md` F1). The protocol is conversation.

### CQ1 — Domain or kind of work

What domain or kind of work do you want this OV to support? Be as specific as you can — "medical practice" is too broad; "preparing for difficult patient conversations as a primary care physician" is the kind of scope that produces a tight OV.

### CQ2 — Why this, why now

What's driving you to design this OV? What's the current state of the work that the OV is meant to improve?

### CQ3 — Existing artifacts and prior art

Do you have existing notes, frameworks, prior systems, or methodologies (in the proper sense — bodies of method) that this OV should incorporate or replace?

### CQ4 — Who is this for

Just you? You + a few collaborators? Public release? Each path has different implications for personal-data scrubbing, license, attribution.

### CQ5 — Cadence

How often do you expect to use this OV? Daily? Weekly? Episodically (only when a specific situation triggers it)? This shapes the session protocol and the cartridge analog.

### CQ6 — Multi-session evidence

What evidence is there that this work is multi-session? If a single conversation could produce the value, you might want a Custom GPT or skill, not an OV. (This is the OV-form check.)

### CQ7 — State to remember

What state needs to persist across sessions? Concretely.

### CQ8 — Stakes and reversibility

Are the outcomes high-stakes? Reversible? Does the OV need safety routing (escalation to professionals, hard stops on certain decisions)?

### CQ9 — Communication preferences

Default is peer register, direct, substantive critique, minimal hedging. Confirm or modify.

### CQ10 — Output target

Does the OV produce specific deliverables? (Synthesis essays, decision documents, ship-able artifacts, performance records, etc.) Or is the value mostly in-process (the conversations themselves, with no end deliverable)?

Once you have answers, proceed.

## Step-by-step execution

### Step 1 — Create the design cartridge

Inside this OVE folder, create a new subfolder named after the OV being designed (in `Title-Case-Hyphenated`, mirroring existing examples). Examples: `Medical-Conversations`, `Investing-Decisions`, `Software-Architecture-Reviews`, `Family-Operations`.

```
<New-OV-Name>/
├── _ov-manifest.md
├── _design-state.md
├── _design-decisions.md
├── _schema-draft.md
├── Sessions/
└── Artifacts/
```

### Step 2 — Write the manifest

Use `_templates/TEMPLATE-ov-manifest.md`. Populate from CQ1–CQ10. Include:

- Domain and scope
- User context (goals, prior knowledge, constraints)
- Cadence and multi-session evidence
- Output target
- Communication preferences

### Step 3 — Begin schema design (SCHEMA-DESIGN session)

Open `_schema-draft.md` from the template. Walk through Q1–Q13 from `04-SCHEMA-DESIGN.md` with the user. One question at a time, with proposals and rationale.

This typically takes 2–4 sessions for a substantive OV. Don't rush. Schema is the most important creative work.

### Step 4 — Decide cartridge shape (CARTRIDGE-SHAPE session)

Based on the schema, decide:

- What does a cartridge represent in this OV?
- What are its backbone files?
- What's the state-persistence contract (per `06-STATE-PERSISTENCE.md`)?

Lock these in `_design-decisions.md`.

### Step 5 — Draft artifacts (ARTIFACT-DRAFT sessions)

Order:

1. `AI-BOOTSTRAP.md` for the new OV — the first thing the AI loading the new OV reads
2. Engine `00-START-HERE.md` for the new OV
3. Other engine chapters (numbered)
4. BOOTSTRAP-NEW-CARTRIDGE prompt for the new OV
5. Templates
6. `README.md`
7. `INSTALL.md`, `OPERATOR-GUIDE.md`, `CONTRIBUTING.md`
8. `LICENSE.md`, `VERSION.md`, `CHANGELOG.md`
9. `.gitignore`
10. At least one worked-example cartridge for the new OV

Each draft lives in `Artifacts/` inside the design cartridge.

### Step 6 — Review (REVIEW sessions)

For each artifact, do a REVIEW pass. Check against `02-DESIGN-PRINCIPLES.md` and the writing conventions in `05-WRITING-FOR-AI.md`.

### Step 7 — Ship (SHIP-PREP session)

Walk `07-SHIPPING-CHECKLIST.md`. Create the new OV folder, copy artifacts, scrub, version, license, optionally git init and push.

### Step 8 — Post-ship verification

In a fresh AI session, point the AI at the new OV and confirm it works.

### Step 9 — Close the design cartridge

Update `_design-state.md` to "shipped." Final session log. Done.

## Quality gates

Before considering bootstrapping (CQ phase) complete:

- [ ] CQ1–CQ10 asked and answered (conversationally, one at a time)
- [ ] Design cartridge folder exists
- [ ] `_ov-manifest.md` populated
- [ ] Multi-session evidence confirmed (CQ6) — if not, propose the user step down to a smaller artifact (Custom GPT, skill, prompt pack) instead of an OV

Before considering the OV ready to ship:

- [ ] All artifacts drafted and reviewed
- [ ] Worked example cartridge for the new OV is filled in (not just templated)
- [ ] Personal-data scrub complete
- [ ] License + version + changelog populated
- [ ] README passes the front-door test (one-line pitch + quick-start visible on first screen)
- [ ] Post-ship verification passed in a fresh AI session

## Common failure modes to avoid

1. **Skipping CQ1–CQ10.** Don't start designing before you understand the domain and user. This produces generic, unhelpful OVs.
2. **Multi-bullet questionnaire.** F1 in the failure-modes catalog. Conversation, not assignment.
3. **Designing for an OV when a smaller artifact would do.** If CQ6 (multi-session evidence) comes back weak, say so. Sometimes the right answer is "this should be a Custom GPT" or "this should be a few well-crafted prompts." Don't OV everything.
4. **Schema-by-template.** Cloning an existing OV's schema without re-running Q1–Q13 produces a generic schema that fits nothing well.
5. **Fabricating tools/frameworks the user references.** F2 in the failure-modes catalog. If you don't know whether something is real, ask.
6. **Inferring the user's name from username or path.** F3 in the failure-modes catalog. Use placeholders until they tell you.
7. **Drafting artifacts before schema is locked.** Order matters. Drafts done early get thrown away.
8. **Engine bleed into cartridge content.** Engine stays subject-agnostic. Domain content goes in the cartridge.
9. **Not testing in a fresh session.** Self-confirmation bias is real. A fresh session is the only honest test.

## A note on conversational tone

The user is an adult building something serious. They want competent collaboration. No flattery, no filler, no "great question." If they're wrong about something, say so directly. If they're right, say so without overselling it.

This OV — like the ones it teaches you to design — is in the peer-register family. Match that.
