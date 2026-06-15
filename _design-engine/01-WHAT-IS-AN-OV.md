---
Item_Prototype: Fleeting
Item_ID: ove-engine-01-what-is-an-ov
Title: "OVE Engine — 01 What Is an OV"
Date_Added: 2026-06-01
Date_Modified: 2026-06-06
Needs_Processing: false
type: design-engine
role: concept-definition
scope: subject-agnostic
updated: 2026-06-01
---

# 01 — WHAT IS AN OPERATING VOLUME?

> **A definitional chapter. Use this to anchor design conversations and to answer the question directly when a user asks "what is this thing I'm building?"**

## One-sentence definition

An **operating volume** is a self-contained markdown corpus that, when loaded into an AI assistant, orchestrates a particular kind of long-running, stateful work between the AI and the user.

## The slot it fills

Operating volumes occupy a real gap in the AI-instruction lexicon. The full spectrum, from smallest to largest:

| # | Term | What it is | Engineering form |
|---|------|------------|------------------|
| 1 | Token | The model's internal unit (~3–4 chars). | (niche) |
| 2 | Prompt | A single input message. | **Prompt engineering** |
| 3 | System prompt | Initial behavior-setting message. | Sub-form of prompt engineering |
| 4 | Few-shot examples | Example pairs embedded in a prompt. | Sub-technique |
| 5 | Persona / role | A character or stance. | Persona design |
| 6 | Template | Reusable prompt with variable slots. | Prompt-template design |
| 7 | Chain / CoT | Sequence of prompts, or in-prompt reasoning chain. | Prompt chaining |
| 8 | Tool / function | A single invokable capability. | Tool / function-calling design |
| 9 | Command (slash) | User-triggered shortcut. | Command design |
| 10 | Hook | Event-triggered callback. | (emerging) |
| 11 | Skill | Packaged capability bundle. | Skill design |
| 12 | MCP server | Server exposing tools/resources via Model Context Protocol. | MCP server design |
| 13 | Pipeline / workflow | Multi-step orchestrated sequence. | Pipeline design |
| 14 | RAG corpus | Indexed reference material for retrieval. | **RAG engineering** |
| 15 | Custom GPT / Project / Assistant | Packaged AI: instructions + files + tools. | Informal "GPT design" |
| **16** | **Operating volume (OV)** | **Self-contained markdown corpus an AI loads to orchestrate a kind of long-running work; substrate-agnostic.** | **Operating volume engineering** |
| 17 | Subagent | AI agent invoked by another agent. | Sub-form of agent engineering |
| 18 | Agent | Autonomous AI running an observe-think-act loop. | **Agent engineering** |
| 19 | Multi-agent system | Orchestrated set of agents. | Multi-agent design |
| 20 | Harness | The framework around the model (loop, context, tools, hooks, state). | **Harness engineering** |
| 21 | Framework / platform / stack | Broader infrastructure (LangChain, LlamaIndex, Vercel AI SDK). | Framework engineering |

OV sits at #16 — larger than a skill, deeper than a Custom GPT or Project, smaller than a harness. The closest existing things in the lexicon are Custom GPTs and Projects, but OVs are structurally different:

- **Custom GPTs and Projects are configured AI instances.** They live on a platform (OpenAI, Anthropic, Google). They are configurations.
- **OVs are domain operating systems.** They live on disk as plain markdown. They're substrate-agnostic — they run on any capable AI.

## What an OV is composed of

| Component | Role | Lives in |
|-----------|------|----------|
| **Bootstrap protocol** | First file the AI reads; tells it what to load and what role to take | `AI-BOOTSTRAP.md` at root |
| **Engine** | The subject-agnostic operating manual the AI consults during sessions | `_<purpose>-engine/` |
| **Templates** | Scaffolding for the artifacts the work produces | `_<purpose>-engine/_templates/` |
| **Schema** | Structural contract every artifact conforms to | `_<purpose>-engine/_meta/SCHEMA-OF-SCHEMAS.md` + per-cartridge `_schema.md` |
| **Cartridges** | Per-engagement workspaces where the actual work accumulates | `<Engagement-Name>/` at root |
| **State files** | Durable records the AI reads and writes across sessions | `<Engagement-Name>/_state.md` |
| **Front-door docs** | Human-facing README, INSTALL, OPERATOR-GUIDE, CONTRIBUTING | At root |
| **Versioning + license** | Treats the OV as a serious shipping artifact | `VERSION.md`, `CHANGELOG.md`, `LICENSE.md` |

The names of these components vary per OV. In `LifeLong-Learning`, the engine is `_teaching-engine/` and a cartridge represents a *subject being studied*. In `SOLVE-eX`, the engine is `00-Instructions/` and the cartridge analog is a *case file*. In OVE itself, the engine is `_design-engine/` and a cartridge represents *an OV being designed*. The pattern is invariant; the names adapt.

## An OV is a specialized AI agent (Convention 10 framing)

In market-facing terms, every OV is a **specialized AI agent**: a system that holds focused expertise in a domain and delivers it through state, workflow, action, and accountability that a raw chat session structurally cannot provide. The structural pieces above (bootstrap protocol, engine, cartridges, state files) are the delivery system around the expertise; the expertise is the entry ticket, not the differentiator.

This framing matters because every OV must defeat one question — whether its user is a paying customer, an internal-team operator, a personal-use operator, or a methodology principal:

> *"Would a general LLM be better for this work than this OV?"*

A `No` answer is **earned**, not asserted. The two master tests in `02-DESIGN-PRINCIPLES.md` (Displacement + Absorption) are the criteria; **Convention 10 — Standalone Sufficiency Posture** (`_design-engine/_meta/CONVENTIONS.md`) is the enforcement mechanism. Every OV designed via OVE declares a posture against the 47-requirement substrate at `_design-engine/_meta/standalone-sufficiency/` and ships three artifacts (`standalone-sufficiency-posture.md`, `_meta/posture.yaml`, `_meta/vetting-rubric-filled.md`) at the OV root. The validator (`C14` in `_design-engine/_meta/validate.py`) checks the declaration at ship time.

The test applies whether the OV is paid for or not. Many OVs are not commercialized (internal tools, personal systems, methodology corpora) — and the test still applies because the substitution risk is real regardless of monetization: if a general LLM would serve the user better, the OV has no reason to exist.

## What an OV is NOT

- **Not a Custom GPT.** Custom GPTs lock to OpenAI and are configuration, not corpus.
- **Not a skill.** Skills are single capabilities; an OV contains many skills' worth of structured guidance plus a schema, templates, and embedded discipline.
- **Not a prompt or prompt pack.** Prompts are single inputs; an OV is a multi-file system the AI loads progressively across a session.
- **Not an agent.** Agents are autonomous workers; an OV is what an agent (or any AI) loads to specialize for a domain.
- **Not a harness.** Harnesses are AI runtimes (Claude Code, Cursor); OVs run *inside* a harness.
- **Not framework-bound.** No LangChain, no LlamaIndex, no Python. Plain markdown.

## Properties that distinguish an OV

1. **Substrate-agnostic.** Runs on Claude, GPT, Gemini, anything that can read markdown and parse YAML frontmatter.
2. **Stateful across sessions.** Files on disk are the memory. The AI re-reads state at every session start.
3. **Self-describing.** The folder contains instructions for the AI on how to use the folder. No external configuration.
4. **Forkable, versionable, licensable.** Like code — except the code is prose.
5. **Conversational interface.** No GUI, no CLI flags. The user talks to the AI; the AI consults the OV.
6. **Cartridge-specializable.** The engine is subject-agnostic; cartridges specialize it for a specific engagement.
7. **Multi-session by design.** Built to support work that unfolds over weeks, months, or years.
8. **Archetype-declared — finite-horizon or practice.** Every OV declares its archetype at design time. **Finite-horizon OVs** have a defined finish line (manuscript published, subject mastered, problem solved, artifact shipped). **Practice OVs** have no terminal arrival — the principal's engagement continues indefinitely (political navigation, longevity health, ongoing relationship cultivation, lifelong leadership development). The archetype shapes how the OV answers "what does done look like" — terminal-artifact spec vs three-layer mastery signal. See `04-SCHEMA-DESIGN.md` § Q6 and `BOOTSTRAP-NEW-OV.md` § CQ11.

## When is OV the right form?

Use the OV form when **all** of the following hold:

- The work is **multi-session** — a single conversation isn't enough
- The work is **stateful** — what happened last time matters
- The work has **structure** worth encoding (Items, relationships, phases, activities)
- You want **substrate flexibility** — not locked to one AI vendor
- You want **the artifact to be portable** — clone, fork, share, license

If any of those don't hold, a smaller artifact is usually better:

- One-shot? → a well-crafted prompt
- Single capability? → a skill
- Single AI on a single platform? → a Custom GPT or Project
- Highly automated, low-conversation? → an agent or pipeline

## Why the term "operating volume"

The category needed a name. The candidates considered:
- *Methodology* — incorrect usage of the word (methodology = study of methods)
- *Playbook* — too sports/corporate-coded
- *Codex* — right shape, but OpenAI claimed it as a product name
- *Doctrine, tome, canon, pandect* — close but each had problems
- *Score* — beautiful metaphor (composer/performer) but music-coded

**"Volume"** carries the right associations: implies a series (most users will have several), has gravitas, isn't claimed by any platform, and has the bound-self-contained-artifact feel.

**"Operating"** parallels *operating system* — an OV is to an AI what an OS is to hardware. It's the substrate the AI operates against.

The associated discipline — designing OVs well — is **operating volume engineering**, parallel to prompt engineering, agent engineering, harness engineering.
