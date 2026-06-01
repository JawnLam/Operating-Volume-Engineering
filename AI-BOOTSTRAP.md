---
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

### 1. Mandatory reads (in order)

Read these in full from `{ROOT}/_design-engine/`:

1. `00-START-HERE.md` — the assistant entry point
2. `01-WHAT-IS-AN-OV.md` — definition, the lexicon table, where OV sits
3. `02-DESIGN-PRINCIPLES.md` — substrate-agnostic, statefulness, cartridge pattern, the operator-confirmed-identity rule
4. `03-DESIGN-PROTOCOL.md` — the session protocol for designing an OV with a user
5. `04-SCHEMA-DESIGN.md` — how to design the schema for a new OV (parallels LLL's schema-design protocol at one level up)
6. `05-WRITING-FOR-AI.md` — writing AI-readable prose; specific failure modes
7. `06-STATE-PERSISTENCE.md` — what gets written when, durability contracts
8. `07-SHIPPING-CHECKLIST.md` — versioning, scrubbing, license, GitHub workflow
9. `BOOTSTRAP-NEW-OV.md` — the cartridging prompt for opening a new design engagement
10. `_meta/SCHEMA-OF-SCHEMAS.md` — meta-ontology (only required for audit work)
11. `_meta/FAILURE-MODES.md` — the catalog you actively guard against
12. `{ROOT}/_USER.md` if present — the user's global profile

Read each in full. "Skim" is not a valid mode for these core files.

### 2. Mandatory environment checks

- **Folder writability.** Verify you can write to `{ROOT}/<Cartridge>/Sessions/`, `<Cartridge>/_design-state.md`, and `<Cartridge>/Artifacts/`. If the environment is read-only, declare **sandbox mode** and keep state inline in the conversation.
- **Existing cartridges.** List the subfolders at `{ROOT}/` (excluding `_design-engine/` and dot/underscore-prefixed). Each is a candidate cartridge.
- **Worked examples.** The cartridges `SOLVE-eX-Retrospective`, `LifeLong-Learning-Retrospective`, `Negotiation-Preparation`, `Long-Form-Writing`, and `Relationship-Cultivation` ship as worked examples. Treat them as reference implementations, not the user's active work.

### 3. Decide the path

- **If the user named an existing cartridge OR is continuing one in progress** → execute the session-start protocol from `_design-engine/00-START-HERE.md` (read the cartridge's `_ov-manifest.md`, `_design-state.md`, recent sessions). Then propose a session activity.
- **If the user wants to design a NEW OV** → route to `_design-engine/BOOTSTRAP-NEW-OV.md` and open a new cartridge. Begin with one clarifying question, conversationally.
- **If the user wants to audit an EXISTING OV** elsewhere on disk → ask for the path. Route to the audit protocol in `_design-engine/03-DESIGN-PROTOCOL.md` §4 (Audit Mode).
- **If the user wants conceptual orientation only** ("what is an operating volume?") → answer directly from `_design-engine/01-WHAT-IS-AN-OV.md`. No cartridge needed unless the conversation turns into design work.

### 4. Readiness statement

Your first user-facing message should be short — two to four sentences — and confirm:

- That you've read the design engine
- Which path you took
- Either your proposed session activity (existing cartridge), your first clarifying question (new OV), the path to audit (audit mode), or a direct answer (orientation)

Examples:

> *"Pre-flight complete. I've read the design engine and your Negotiation-Preparation cartridge. You're in design state 'schema-drafting,' three sessions in, with one open thread on whether 'stakeholder' is its own atom type or a sub-type of 'party.' My proposal: continue schema-drafting and close that thread. Your call."*

> *"Pre-flight complete. No cartridge for a new OV exists yet, so I'll open one. First question: what domain or kind of work do you want this OV to support? Be as specific as you can — 'medical practice' is too broad; 'preparing for difficult patient conversations' is the kind of scope that produces a tight OV."*

If you can't complete pre-flight (missing files, ambiguous user message), say so and ask what you need.

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
6. **You propose, the user disposes.** Show your reasoning when proposing schemas, atom types, cartridge shapes. Honor overrides.

## When in doubt

- About what an OV is → `_design-engine/01-WHAT-IS-AN-OV.md`
- About the design conversation flow → `_design-engine/03-DESIGN-PROTOCOL.md`
- About schema design → `_design-engine/04-SCHEMA-DESIGN.md`
- About a worked example → the five cartridges in `{ROOT}/`

End of bootstrap. Proceed with Phase 0.
