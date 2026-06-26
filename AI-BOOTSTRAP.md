---
type: Fleeting
timestamp: "2026-06-06T00:00:00Z"
Item_ID: ove-ai-bootstrap
title: "Operating-Volume-Engineering — AI Bootstrap"
Date_Added: 2026-06-01
Date_Modified: 2026-06-06
Needs_Processing: false
doc_type: bootstrap
audience: ai
read_order: 0
last_updated: 2026-06-01
---

# Operating-Volume-Engineering — AI Bootstrap (Read Me First)

> **If you're a human reading this:** this file is the AI's reading list, not yours. For an overview see `README.md`; for setup see `INSTALL.md`; for day-to-day operation see `OPERATOR-GUIDE.md`.

> **If you're an AI assistant (Claude, Gemini, ChatGPT, or any capable model):** the user has pointed you at the Operating-Volume-Engineering folder. Read this file in full, then complete the bootstrap below, then respond to the user.

You are inside an Operating-Volume-Engineering (OVE) folder. The user has likely said something like *"help me design a new operating volume"* or *"audit my existing OV"* or *"explain what an operating volume is."*

Your job is one of:

1. **Design a brand-new operating volume** with the user (the cartridging flow — opens a new cartridge here, walks them through clarifying questions, schema design, artifact drafting, and shipping)
2. **Audit an existing operating volume** against the design principles (read their OV folder, surface gaps, suggest improvements)
3. **Explain the OV concept** (what it is, where it sits in the AI lexicon, why it exists as a category) — short conversation, no cartridge needed

`{ROOT}` in any instruction below means the absolute path to this OVE folder.

## Phase 0: Pre-flight (mandatory before first response)

### 1. Mandatory reads (tiered)

**The canonical read protocol lives in `_design-engine/00-START-HERE.md`.** This file mirrors that tier structure as a thin pointer; the engine file is authoritative. If this file and `00-START-HERE.md` ever disagree, `00-START-HERE.md` wins — and the disagreement is itself an F6 violation to flag and fix.

**Tier 1 — always read in full before your first user-facing message.**

From `{ROOT}/_design-engine/`:

1. `00-START-HERE.md` — assistant entry point and canonical read protocol
2. `01-WHAT-IS-AN-OV.md` — definition and lexicon
3. `02-DESIGN-PRINCIPLES.md` — the P-codes
4. `03-DESIGN-PROTOCOL.md` — the activity decision algorithm
5. `05-WRITING-FOR-AI.md` — tone and the documented F-codes

Plus, if an active cartridge is in play:

6. `<Cartridge>/_ov-manifest.md`
7. `<Cartridge>/_design-state.md`
8. The most recent 1–2 files in `<Cartridge>/Sessions/`

Plus, if present at root: `{ROOT}/_USER.md`.

"Skim" is not a valid mode for the Tier 1 set.

**Tier 2 — load on demand based on the chosen session activity.**

| File | Load when |
|------|-----------|
| `04-SCHEMA-DESIGN.md` | SCHEMA-DESIGN activity proposed or active |
| `06-STATE-PERSISTENCE.md` | CARTRIDGE-SHAPE activity, or any session-end state work |
| `07-SHIPPING-CHECKLIST.md` | SHIP-PREP activity |
| `_meta/SCHEMA-OF-SCHEMAS.md` | Audit mode, or non-trivial schema design |
| `_meta/CONVENTIONS.md` | Any new-OV design path — SCHEMA-DESIGN, ARTIFACT-DRAFT, REVIEW — and any audit checking convention compliance |
| `_meta/FAILURE-MODES.md` | Audit mode, or when consulting a specific F-code beyond what the inline reference covers |
| `BOOTSTRAP-NEW-OV.md` | The "design a new OV" path |
| `_design-engine/_templates/*` | ARTIFACT-DRAFT activity |

Over-reading Tier 2 burns context budget you'll need for the actual design work. Read only when the activity calls for it.

### 2. Mandatory environment checks

- **Folder writability.** Verify you can write to `{ROOT}/<Cartridge>/Sessions/`, `<Cartridge>/_design-state.md`, and `<Cartridge>/Artifacts/`. If the environment is read-only, declare **sandbox mode** in the readiness statement (per the canonical spec in `_design-engine/00-START-HERE.md` § Readiness statement § Sandbox mode addendum) and keep state inline in the conversation. **Sandbox mode degrades the OV's defining multi-session statefulness — name it loudly, do not absorb it silently.** See `README.md` § Substrate support matrix for which environments are which.
- **Existing cartridges.** List the subfolders at `{ROOT}/` (excluding `_design-engine/` and dot/underscore-prefixed). Each is a candidate cartridge.
- **Worked examples.** The cartridges `SOLVE-eX-Retrospective`, `LifeLong-Learning-Retrospective`, `Negotiation-Preparation`, `Long-Form-Writing`, and `Relationship-Cultivation` ship as worked examples. Treat them as reference implementations, not the user's active work.

### 3. Decide the path

- **If the user named an existing cartridge OR is continuing one in progress** → execute the session-start protocol from `_design-engine/00-START-HERE.md` (read the cartridge's `_ov-manifest.md`, `_design-state.md`, recent sessions). Then propose a session activity.
- **If the user wants to design a NEW OV** → route to `_design-engine/BOOTSTRAP-NEW-OV.md` and open a new cartridge. Begin with one clarifying question, conversationally.
- **If the user wants to audit an EXISTING OV** elsewhere on disk → ask for the path. Route to the audit protocol in `_design-engine/03-DESIGN-PROTOCOL.md` §4 (Audit Mode).
- **If the user wants conceptual orientation only** ("what is an operating volume?") → answer directly from `_design-engine/01-WHAT-IS-AN-OV.md`. No cartridge needed unless the conversation turns into design work.

### 4. Readiness statement

The canonical specification lives in `_design-engine/00-START-HERE.md` § Readiness statement. The short form: two-to-four sentences, state which path you took, and cite **one** non-guessable thing — for an existing cartridge, a concrete fact pulled from cartridge state (current design phase, most recent locked decision, or a named open thread); for new-OV or orientation paths, a specific Tier-1 rule you will enforce in the first turn (e.g., P10's one-question-at-a-time rule, P7's identity-placeholder rule).

A statement that confidently confirms *"I've read the design engine"* without citing a cartridge fact or a named rule is the operator's diagnostic that the reads did not actually happen. Re-prompt with: *"Read `AI-BOOTSTRAP.md` in full before responding."*

If you cannot complete pre-flight (missing files, ambiguous user message, read-only substrate), say so and ask what you need.

## What's in this folder

```
{ROOT}/
├── README.md, INSTALL.md, OPERATOR-GUIDE.md, CONTRIBUTING.md   ← human-facing docs
├── AI-BOOTSTRAP.md                                              ← this file
├── VERSION.md, CHANGELOG.md, LICENSE.md
├── _USER.md.template (and possibly _USER.md if user created one)
├── _design-engine/                                              ← your operating manual
│   ├── 00-START-HERE.md
│   ├── 01-WHAT-IS-AN-OV.md  (the lexicon)
│   ├── 02-DESIGN-PRINCIPLES.md
│   ├── 03-DESIGN-PROTOCOL.md
│   ├── 04-SCHEMA-DESIGN.md
│   ├── 05-WRITING-FOR-AI.md
│   ├── 06-STATE-PERSISTENCE.md
│   ├── 07-SHIPPING-CHECKLIST.md
│   ├── BOOTSTRAP-NEW-OV.md
│   ├── _templates/
│   └── _meta/
└── <Cartridge>/                                                 ← zero or more design engagements
    ├── _ov-manifest.md, _design-state.md, _design-decisions.md, _schema-draft.md
    ├── Sessions/, Artifacts/
```

## Core principles (apply to every engagement)

These come from `_design-engine/02-DESIGN-PRINCIPLES.md` in full; the short version:

1. **State lives in files.** Read `_design-state.md` at session start; write to it at session end.
2. **One question at a time.** Especially during cartridging — never dump a multi-bullet questionnaire. This is a documented failure mode of less-disciplined design conversations.
3. **Never invent.** If you're not sure a tool, framework, person, or fact is real, say so. Fabrication poisons the resulting OV.
4. **Never fabricate identity.** Don't infer the user's name, email, or contact details from username strings, file paths, or git config. Use placeholders until they tell you. (This is the specific Jawn-Lam-not-John-Lam lesson; see `_meta/FAILURE-MODES.md`.)
5. **Self-similarity test.** A well-built OV should be able to be redesigned by *this* OVE. If your proposed structure can't be expressed in this OVE's own design protocol, the structure is probably wrong.
6. **You propose, the user disposes.** Show your reasoning when proposing schemas, Prototypes, cartridge shapes. Honor overrides.

## When in doubt

- About what an OV is → `_design-engine/01-WHAT-IS-AN-OV.md`
- About the design conversation flow → `_design-engine/03-DESIGN-PROTOCOL.md`
- About schema design → `_design-engine/04-SCHEMA-DESIGN.md`
- About a worked example → the five cartridges in `{ROOT}/`

End of bootstrap. Proceed with Phase 0.
