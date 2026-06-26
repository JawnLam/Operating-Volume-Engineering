---
type: Fleeting
timestamp: "2026-06-07T00:00:00Z"
Item_ID: ove-update-prompt
title: "Operating-Volume-Engineering — AI-Assisted Update Prompt"
Date_Added: 2026-06-07
Date_Modified: 2026-06-07
Needs_Processing: false
---

# `Operating-Volume-Engineering` — AI-Assisted Update Prompt

> **What this file is.** A copy-pasteable prompt that asks an AI assistant to walk you through updating this Operating Volume to the latest release. Open this file, copy the **prompt block** below, paste it to your AI assistant (Claude, ChatGPT, Gemini, Cursor, Claude Code, etc.) with read/write access to this folder, and the AI will read OVE's update protocol and walk you through it step by step.
>
> Per OVE Convention 7 (`_design-engine/_meta/CONVENTIONS.md`). One file per OV; ships at the OV root. OVE eats its own dogfood: this is the same template OVE provides for new OVs.

## The prompt — copy this verbatim to your AI

```
I want to update this Operating Volume (Operating-Volume-Engineering) to the latest release. Please walk me through it:

1. Read INSTALL.md § "Updating" and OPERATOR-GUIDE.md § "Updates and troubleshooting" so you know this OV's update protocol.

2. Run `git fetch origin` and report what's incoming. Show me the output of:
       git log --oneline HEAD..origin/main
   Tell me how many commits, and read the new CHANGELOG.md entry/entries so you can summarize what's changing.

3. Check `git status`. If there are local engine modifications that would block a fast-forward pull, propose a stash strategy before doing anything destructive — name which files are modified and explain whether they look like incidental edits or load-bearing customizations of OVE's design engine.

4. Walk me through `git pull --ff-only origin main` step by step. Stop and ask before running it. If it fails (because of local edits), fall back to the stash → pull → pop pattern documented in OPERATOR-GUIDE.md, and walk me through any conflicts.

5. Check the new CHANGELOG.md entry for:
   (a) a migration recipe I need to run (e.g., a perl/python substitution to apply to existing design cartridges),
   (b) a major.minor folder rename I should perform (e.g., Operating-Volume-Engineering-v1.2 → v1.3),
   (c) any breaking-change notes or new validator checks that might flag previously-passing design cartridges.
   Surface each one explicitly; do not silently apply anything.

6. After the update lands, confirm that my Operator-Extension Zone (my own design cartridges parallel to the worked examples) and Operator-Private Zone (gitignored files: _USER.md, per-cartridge _design-state.md and Sessions/*.md) are intact and untouched. Report the file counts before/after for the key folders.

7. Run the validator (`python3 _design-engine/_meta/validate.py`) and report findings. New checks may have been added in this release.

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

- **Major version transitions** — including the **v1.x → v2.0 transition shipped 2026-06-13**. The CHANGELOG.md entry for v2.0.0 includes explicit notes on what's breaking (Q6 framing now forks by archetype; manifest schema gains `ove_OV_Archetype` + three `ove_Audience_*` fields for v2.0-designed OVs; SHIP-PREP gains Phase 3.7 / 3.8 / 3.9 hard-stops). Read the CHANGELOG entry's "v2.0 is breaking" paragraph **before** running the standard update flow.
  - **v1.x-built OVs do not need migration.** OVs have no runtime dependency on OVE — they stand alone once shipped. v2.0's changes affect how the *next* OV gets built; existing OVs grandfather as-shipped. Operators currently mid-design under v1.x can choose to (a) finish the current OV under v1.x conventions (recommended), or (b) restart the design under v2.0 conventions.
- **You're at a folder that needs renaming first.** If the latest release announces a major.minor folder transition (e.g., `Operating-Volume-Engineering-v1.2 → Operating-Volume-Engineering-v2.0`) the rename happens at the filesystem level before `git pull`. Do that manually first, then run this prompt.
- **You're forking to customize OVE's engine.** This prompt assumes you're a downstream operator pulling upstream releases. If you're forking to customize OVE itself (adding conventions, extending the validator, restructuring the engine), you want to do that work in a branch and contribute back per OPERATOR-GUIDE.md § "Contributing back upstream," not this update flow.

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
