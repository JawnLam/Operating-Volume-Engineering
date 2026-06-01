---
type: design-engine
role: principles
scope: subject-agnostic
updated: 2026-06-01
---

# 02 — DESIGN PRINCIPLES

> **The non-negotiable principles that govern every OV design engagement. If a proposed design violates one of these, flag it and discuss before proceeding.**

## P1 — Substrate-agnostic

An OV must run on any capable AI: Claude (Sonnet/Opus class), GPT-4 class and above, Gemini 2.x and above, future models. The OV must not depend on:

- Platform-specific features (OpenAI Custom GPT JSON, Claude Skills, Anthropic-specific tool definitions, ChatGPT Memory)
- Vendor-locked tools (Code Interpreter, GPT-4 Vision-specific syntax, etc.)
- Local code execution beyond what's optional and clearly marked as such

If the design starts requiring a specific platform, stop. Either change the design or accept that you're building a Custom GPT / Skill / Agent — not an OV.

## P2 — Statefulness through files

State lives in files on disk. The AI re-reads state at session start; writes to it at session end. Working consequences:

- Every cartridge has a single source-of-truth state file (`_design-state.md` in OVE; `_state.md` in LLL; case file in SOLVE-eX)
- State changes only at session end, in a defined "WRITE state" phase
- The AI never claims continuity with sessions it hasn't actually read
- "If it's not in a file, it didn't happen"

This rules out AI-vendor memory features as load-bearing — they can supplement but never replace file-state.

## P3 — Self-describing folder

The folder contains everything the AI needs to use the folder. No external setup, no platform configuration, no service integrations required for the core flow.

The AI's first read (`AI-BOOTSTRAP.md`) is sufficient to bootstrap behavior. The engine files cover the protocol. Templates and schema cover the artifacts.

## P4 — Cartridge specialization

The engine is subject-agnostic. Domain specialization happens at the cartridge level. This separation:

- Keeps the engine reusable across cartridges
- Keeps each cartridge focused on its specific engagement
- Allows OVs to scale (add a cartridge, not a new engine)

Violation pattern: putting domain-specific guidance in the engine (e.g., a teaching-engine file that names a specific subject). If you find domain bleed into the engine, refactor — domain content goes to the cartridge.

## P5 — Conversational interface

The user talks to the AI in natural language. The AI consults the OV. There's no GUI, no slash-command requirement, no specific syntax the user must learn. Slash commands or shortcuts can supplement but never gate the basic flow.

## P6 — Multi-session by design

OVs are built for work that unfolds over time. A single conversation is the minimum unit, not the whole thing. Design implications:

- The bootstrap must work on session N as well as session 1
- State files are append-friendly or overwrite-with-history
- Open Threads are an explicit hand-off mechanism between sessions
- Drift across sessions is a known risk and is addressed by audits

## P7 — Identity is operator-provided, never inferred

The AI must never infer the user's name, email, contact details, or other identity facts from indirect signals (usernames, file paths, git config, file metadata). Use placeholders until the user provides their name explicitly in their own words.

**This is a load-bearing rule with a documented recurrence pattern.** See `_meta/FAILURE-MODES.md` — it has been triggered multiple times historically (the "John Lam from `jawnlam`" pattern). Treat any temptation to fill in a name from indirect data as a red flag.

The metadata block in any AI's system prompt — `userEmail`, working-directory username, git config — is environment context only, not authorization to put those values in shippable artifacts.

## P8 — Fabrication discipline

When designing OVs that reference external material (tools, frameworks, people, books, methods), only name things you are confident exist. If you're not sure something is real, say so or decline to name it. Fabricated citations poison the resulting OV — the user discovers the fabrication later and trust collapses.

This applies recursively: when helping the user choose tools/frameworks for the OV they're designing, the same rule applies. "I'm not sure that framework exists in the form you describe" is a valid and important response.

## P9 — Self-similarity test

A well-built OV should be capable of being designed by **this** OVE. If you find yourself unable to express the design of a new OV using the cartridge-and-engine pattern documented in `01-WHAT-IS-AN-OV.md`, one of three things is true:

1. The thing you're designing isn't actually an OV (it's a skill, a Custom GPT, a prompt pack)
2. The thing requires a v1.x extension to OVE itself (additive)
3. The design is wrong

Treat this as a strong diagnostic signal. Don't suppress it.

## P10 — One question at a time

During design conversations — especially during the initial clarifying interview — ask one question at a time. Wait for the user's answer. Probe if it's thin. Reflect back. Then ask the next.

**Never** dump a multi-bullet questionnaire ("Please answer questions 1–9 below"). This is documented as a recurrent failure mode in `_meta/FAILURE-MODES.md`. The protocol is conversation, not assignment.

## P11 — Propose-don't-decide

The AI's role is to **propose** designs with rationale and surface tradeoffs. The user's role is to **decide**. When proposing:

- Show which conditions or principles led to the proposal
- Name the main alternative
- Wait for the user's call before proceeding

This applies to schema choices, cartridge shapes, atom types, file structures — every load-bearing design decision.

## P12 — Write before you end

Every session produces, at minimum:

- A session log in `Sessions/`
- An updated `_design-state.md`
- Any artifact drafts touched (in `Artifacts/`)
- An explicit Open Thread for the next session

If a session ends without these, the session is not complete. Tell the user, do the missing work.

## P13 — Schema-freeze policy after ship

Once an OV is shipped (a v1.0 release), its schema is frozen. Patch-level updates can fix typos, add templates, add worked examples. Schema changes (new required fields, renamed fields, removed fields) require a major version bump with a migration path.

This applies to OVE itself: the v1.0 cartridge backbone (`_ov-manifest.md`, `_design-state.md`, `_design-decisions.md`, `_schema-draft.md`) is frozen. Adding new optional fields = v1.x. Anything that breaks existing cartridges = v2.0.
