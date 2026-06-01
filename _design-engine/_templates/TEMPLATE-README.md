# <OV Name>

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Version](https://img.shields.io/badge/version-v1.0.0-blue.svg)](VERSION.md)

*One-sentence pitch — what this OV does, who it's for.*

---

## What this is

*One to three paragraphs. The full thing. What it is, what makes it different.*

## What it can help with

- *Use case 1*
- *Use case 2*
- *Use case 3*

## What this is not

- *Common confusion 1*
- *Common confusion 2*

## Quick start

### 1. Open the folder in your AI environment

Plain markdown. Any environment where your AI can read local files works (Claude Code, Claude Desktop, ChatGPT, Gemini, Cursor, Obsidian + Copilot).

### 2. Tell the AI to bootstrap

> **"Read `AI-BOOTSTRAP.md` and help me with [the kind of work this OV does]."**

### 3. Have the conversation

*One-line note about the interaction style (one question at a time, no questionnaires, etc.).*

For setup details, see [`INSTALL.md`](INSTALL.md).

## System requirements

- **AI assistant** — any model capable of reading markdown and parsing YAML frontmatter (Claude Sonnet/Opus class, GPT-4 class and above, Gemini 2.x and above)
- **OS** — Mac, Windows, or Linux
- **Python / network / runtime dependencies** — none

## Folder structure

| Folder / file | Contents |
|---------------|----------|
| `AI-BOOTSTRAP.md` | AI entry point |
| `README.md` | This file |
| `INSTALL.md`, `OPERATOR-GUIDE.md`, `CONTRIBUTING.md` | Human-facing docs |
| `VERSION.md`, `CHANGELOG.md`, `LICENSE.md` | Release metadata |
| `_<purpose>-engine/` | The AI's operating manual |
| `<Cartridge>/` | Per-engagement workspaces |

## License

Released under **CC-BY 4.0**. Attribution format:

> Built on **<OV Name> v1.0** by <USER_NAME> — <GitHub URL>
> Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

## Version

See [`VERSION.md`](VERSION.md).
