---
type: Fleeting
timestamp: "2026-06-06T00:00:00Z"
Item_ID: ove-template-ai-bootstrap
title: "OVE Template — AI Bootstrap (for new OV)"
Date_Added: 2026-06-01
Date_Modified: 2026-06-06
Needs_Processing: false
doc_type: bootstrap
audience: ai
read_order: 0
last_updated: <YYYY-MM-DD>
---

# <OV Name> — AI Bootstrap (Read Me First)

> **If you're a human reading this:** this file is the AI's reading list, not yours. For an overview see `README.md`; for setup see `INSTALL.md`; for day-to-day operation see `OPERATOR-GUIDE.md`.

> **If you're an AI assistant (Claude, Gemini, ChatGPT, or any capable model):** the user has pointed you at an <OV Name> folder. Read this file in full, then complete the bootstrap below, then respond to the user.

You are inside an <OV Name> folder. The user has likely said something like *"<typical first-message for this OV>"*.

Your job is to <one-sentence high-level role>.

`{ROOT}` in any instruction below means the absolute path to this folder.

## Phase 0: Pre-flight (mandatory before first response)

### 1. Mandatory reads (in order)

Read these in full from `{ROOT}/_<purpose>-engine/`:

1. `00-START-HERE.md`
2. *(other engine files in order)*
3. `_USER.md` at the OV root, if present
4. The active cartridge's manifest, state, and recent sessions (if continuing an existing engagement)

Read each in full. "Skim" is not a valid mode for these core files.

### 2. Mandatory environment checks

- **Folder writability.** Verify you can write to `{ROOT}/<Cartridge>/Sessions/` and the cartridge's state file. If read-only, declare **sandbox mode**.
- **Existing cartridges.** List the subfolders.

### 3. Decide the path

- *(branch logic based on user message and existing cartridges)*

### 4. Readiness statement

Your first user-facing message should be short — two to four sentences — and confirm:

- That you've read the engine
- Which path you took
- Either your proposed session activity or your first clarifying question

## What's in this folder

```
{ROOT}/
├── README.md, INSTALL.md, OPERATOR-GUIDE.md, CONTRIBUTING.md
├── AI-BOOTSTRAP.md   ← this file
├── VERSION.md, CHANGELOG.md, LICENSE.md
├── _<purpose>-engine/
└── <Cartridge>/      ← zero or more engagements
```

## Core principles

*Inherit from your OV's engine; cite or restate succinctly.*

End of bootstrap. Proceed with Phase 0.
