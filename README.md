# Operating-Volume-Engineering

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Version](https://img.shields.io/badge/version-v1.0.0-blue.svg)](VERSION.md)

A discipline-and-toolkit for designing **operating volumes** — self-contained markdown corpora that an AI assistant loads to orchestrate a specific kind of work. Point any capable AI at this folder, tell it to read `AI-BOOTSTRAP.md`, and it will walk you through designing your own.

---

## What is an operating volume?

An **operating volume** (OV) is the slot in the AI lexicon between a *Custom GPT / Project* and an *AI harness*. Larger than a skill, deeper than a Custom GPT, smaller than a harness. Substrate-agnostic — it runs on Claude, GPT, Gemini, or anything else that can read markdown and parse YAML frontmatter.

An OV consists of:

- A **bootstrap protocol** — instructions the AI reads first to load the volume
- An **engine** — the operating manual the AI consults during sessions
- **Templates** — scaffolding for the artifacts the work produces
- **Schema** — the structural contract every artifact conforms to
- **Cartridges** — per-engagement workspaces where the actual work accumulates
- **State files** — durable records the AI reads and writes across sessions

Two existing operating volumes by the same author:

- **[SOLVE-eX](https://github.com/JawnLam/SOLVE-eX)** — an OV for structured problem-solving and decision-making
- **[LifeLong-Learning](https://github.com/JawnLam/LifeLong-Learning)** — an OV for AI-orchestrated self-directed deep study

This OV is the *propagator*: it teaches an AI how to help you design more.

## What this is for

You point an AI at this folder when you want to build a new operating volume for a domain that matters to you. The AI:

1. Interviews you about the domain (what kind of work, what cadence, what artifacts, what state)
2. Designs the schema, cartridge shape, and session protocol with you
3. Drafts the bootstrap protocol, engine files, and templates
4. Walks you through scrubbing, versioning, and shipping
5. Optionally drives the GitHub setup

You end the engagement with a complete, shippable OV folder — schema-validated, scrubbed of personal data, licensed, and ready to push.

## What this is not

- Not a no-code OV builder. The AI writes the markdown; you make the design decisions.
- Not a framework you import. There's no library; the folder *is* the artifact.
- Not opinionated about your domain. It works for problem-solving, learning, negotiation, relationship maintenance, writing, anything with the right shape.
- Not a substitute for thinking. Designing a good OV is real intellectual work; the AI is a competent partner, not the designer.

## Quick start

You just got this folder. Here's how to use it.

### 1. Open the folder in your AI environment

Plain markdown. Any environment where your AI assistant can read local files works (Claude Code, Claude Desktop, Claude.ai with Projects, ChatGPT Projects, Gemini, Cursor, Windsurf, VS Code with an AI side-panel, Obsidian, plain text editors with AI integration).

### 2. Tell the AI to bootstrap

In your first message, say:

> **"Read `AI-BOOTSTRAP.md` and help me design a new operating volume."**

Or, if you want to audit an existing OV:

> **"Read `AI-BOOTSTRAP.md` and help me audit [my OV name]."**

### 3. Have the conversation

The AI asks one question at a time about the domain. Don't expect a multi-bullet questionnaire — that's a documented failure mode this OV specifically guards against. Expect Socratic clarification, design proposals you can accept or push back on, and incremental construction of the new OV's files inside a cartridge here.

For environment setup, see [`INSTALL.md`](INSTALL.md). For day-to-day operation and troubleshooting, see [`OPERATOR-GUIDE.md`](OPERATOR-GUIDE.md). To extend or contribute, see [`CONTRIBUTING.md`](CONTRIBUTING.md).

## System requirements

- **AI assistant** — any model capable of reading markdown and parsing YAML frontmatter (Claude Sonnet/Opus class, GPT-4 class and above, Gemini 2.x and above)
- **OS** — Mac, Windows, or Linux
- **Editor** — any text editor with AI integration; Obsidian works well; Claude Code / Cursor / Windsurf are excellent
- **Python / network / runtime dependencies** — none

## Folder structure

| Folder / file                          | Contents                                                          |
|----------------------------------------|-------------------------------------------------------------------|
| `AI-BOOTSTRAP.md`                      | AI entry point — first file the AI reads                          |
| `README.md`                            | This file                                                         |
| `INSTALL.md`                           | Setup instructions                                                |
| `OPERATOR-GUIDE.md`                    | Day-to-day operation and troubleshooting                          |
| `CONTRIBUTING.md`                      | How to extend the engine or share improvements back               |
| `VERSION.md` / `CHANGELOG.md`          | Release metadata and history                                      |
| `LICENSE.md`                           | CC-BY 4.0                                                         |
| `_USER.md.template`                    | Optional user-profile template                                    |
| `_design-engine/`                      | The subject-agnostic OV-design operating manual                   |
| `_design-engine/_templates/`           | Templates for every standard file an OV ships with                |
| `_design-engine/_meta/`                | Schema-of-schemas + the failure-modes catalog                     |
| `SOLVE-eX-Retrospective/`              | Worked example: retrospective design analysis of SOLVE-eX         |
| `LifeLong-Learning-Retrospective/`     | Worked example: retrospective design analysis of LifeLong-Learning |
| `Negotiation-Preparation/`             | Worked example: fresh-design walkthrough (anchor demonstration)   |
| `Long-Form-Writing/`                   | Worked example: fresh design for book/dissertation/screenplay work |
| `Relationship-Cultivation/`            | Worked example: fresh design for a relational-CRM-style OV        |

Each cartridge contains: `_ov-manifest.md`, `_design-state.md`, `_design-decisions.md`, `_schema-draft.md`, `Sessions/`, `Artifacts/`.

## Where the term "operating volume" comes from

The category sits at a real gap in the public AI lexicon — larger than a skill, deeper than a Custom GPT or Project, smaller than a harness. It needed a name that wasn't already claimed and that signaled what it does. *Volume* implies a series (you'll likely have several), carries gravitas, isn't claimed by any platform, and has the bound-self-contained-artifact feel. *Operating* parallels operating system — the OV is *to* an AI what an OS is *to* hardware.

The associated discipline is called **operating volume engineering**, parallel to *prompt engineering*, *agent engineering*, *harness engineering*. See `_design-engine/01-WHAT-IS-AN-OV.md` for the full taxonomy.

## License

Operating-Volume-Engineering is released under the **Creative Commons Attribution 4.0 International License (CC-BY 4.0)**. You are free to share, adapt, and build upon this material for any purpose — including commercially — provided you give appropriate attribution.

See [`LICENSE.md`](LICENSE.md) for the full license text. Attribution format:

> Built on **Operating-Volume-Engineering v1.0** by Jawn Lam — https://github.com/JawnLam/Operating-Volume-Engineering
> Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

## Version

See [`VERSION.md`](VERSION.md). This is the **v1.0.0 initial public release**.
