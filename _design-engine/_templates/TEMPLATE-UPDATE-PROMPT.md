---
Item_Prototype: Fleeting
Item_ID: <ov-slug>-update-prompt
Title: "<OV-Name> — AI-Assisted Update Prompt"
Date_Added: YYYY-MM-DD
Date_Modified: YYYY-MM-DD
Needs_Processing: false
---

# `<OV-Name>` — AI-Assisted Update Prompt

> **What this file is.** A copy-pasteable prompt that asks an AI assistant to walk you through updating this Operating Volume to the latest release. Open this file, copy the **prompt block** below, paste it to your AI assistant (Claude, ChatGPT, Gemini, Cursor, Claude Code, etc.) with read/write access to this folder, and the AI will read this OV's update protocol and walk you through it step by step.
>
> Per OVE Convention 7 (`Operating-Volume-Engineering/_design-engine/_meta/CONVENTIONS.md`). One file per OV; ships at the OV root.

## The prompt — copy this verbatim to your AI

```
I want to update this Operating Volume (<OV-Name>) to the latest release. Please walk me through it:

1. Read INSTALL.md § "Updating" and OPERATOR-GUIDE.md § "Updates and troubleshooting" so you know this OV's update protocol.

2. Run `git fetch origin` and report what's incoming. Show me the output of:
       git log --oneline HEAD..origin/main
   Tell me how many commits, and read the new CHANGELOG.md entry/entries so you can summarize what's changing.

3. Check `git status`. If there are local engine modifications that would block a fast-forward pull, propose a stash strategy before doing anything destructive — name which files are modified and explain whether they look like incidental edits or load-bearing customizations.

4. Walk me through `git pull --ff-only origin main` step by step. Stop and ask before running it. If it fails (because of local edits), fall back to the stash → pull → pop pattern documented in OPERATOR-GUIDE.md, and walk me through any conflicts.

5. Check the new CHANGELOG.md entry for:
   (a) a migration recipe I need to run (e.g., a perl/python substitution to apply to existing cartridges),
   (b) a major.minor folder rename I should perform (e.g., v1.7 → v1.8),
   (c) any breaking-change notes or backward-compatibility warnings I should be aware of.
   Surface each one explicitly; do not silently apply anything.

6. After the update lands, confirm that my Operator-Extension Zone (my own cartridges) and Operator-Private Zone (gitignored files) are intact and untouched. Report the file counts before/after for the key folders.

Discipline:
- Do not modify any of my work in the Operator-Extension Zone or Operator-Private Zone. The four-zone boundary is documented in CONTRIBUTING.md § "Content zones".
- Do not run any destructive command without stopping to confirm with me first (no auto `git reset --hard`, no auto `git clean`, no auto `git checkout --theirs` without my approval).
- If anything is unclear or you encounter an unexpected state, stop and ask. Don't improvise.

Begin.
```

## How to use this file

1. Open this file in your AI environment — Claude Code in this folder, or paste-and-attach in any AI chat that has access to the folder.
2. Copy the prompt block above (everything between the triple-backticks).
3. Paste it to your AI assistant.
4. The AI reads the docs, runs the diagnostic, and walks you through the update step by step. **Approve each step before it executes.**
5. When the AI says the update is complete, you're done.

## When this file is the wrong tool

- **Major version transitions** (e.g., v2.0 ships while you're at v1.7). The CHANGELOG.md entry for the major version will include explicit migration instructions that may go beyond this prompt's scope. Read the CHANGELOG entry first, then ask the AI to apply that specific migration rather than the generic update flow.
- **You're at a folder that needs renaming first.** If the latest release announces a major.minor folder transition (e.g., `<OV-Name>-v1.7 → <OV-Name>-v1.8`) the rename happens at the filesystem level before `git pull`. Do that manually first, then run this prompt.
- **You want to fork and customize the engine.** This prompt assumes you're a downstream operator pulling upstream releases. If you're forking to customize the engine yourself, you want OVE's design protocol, not this update prompt.

## Relationship to other docs

| Doc | Role |
|-----|------|
| `INSTALL.md § "Updating"` | The canonical update workflow (`git fetch`, `git pull --ff-only`, stash-pop fallback) |
| `OPERATOR-GUIDE.md § "Updates and troubleshooting"` | Conflict resolution, recovery, major.minor folder transitions, contributing-back |
| `CONTRIBUTING.md § "Content zones"` | The four-zone boundary the AI must respect during the update |
| `CHANGELOG.md` | Release-specific migration recipes and breaking-change notes |
| **`UPDATE-PROMPT.md`** | **This file. The AI-facing prompt that ties the above together for a hands-off update conversation.** |

## Why this exists

Convention 7's `INSTALL.md` and `OPERATOR-GUIDE.md` give the operator the *workflow* (what commands to run, what conflicts to expect, how to resolve them). Convention 7's `UPDATE-PROMPT.md` gives the operator a *one-shot delegation*: "AI, do the update." Both are valid paths — pick the one that matches how you want to spend the next ten minutes. The prompt path is recommended for routine releases (patches and small minors); the manual path is recommended for major-version transitions and any release with a non-trivial migration recipe.
