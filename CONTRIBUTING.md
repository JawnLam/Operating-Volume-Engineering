---
type: Fleeting
timestamp: "2026-06-06T00:00:00Z"
Item_ID: ove-contributing
title: "Operating-Volume-Engineering — Contributing"
Date_Added: 2026-06-01
Date_Modified: 2026-06-06
Needs_Processing: false
---

# Contributing to Operating-Volume-Engineering

OVE ships at v1.0.0 with a stable cartridge schema and engine file structure. This document describes when a contribution is in-scope at v1.x, when it requires a major version bump, and how to propose either.

For day-to-day operation, see `OPERATOR-GUIDE.md`. For release history, see `CHANGELOG.md`.

---

## 1. What is in-scope at v1.x

The following contributions do **not** require a major version bump:

| Contribution                                                                | Where it lives                                                                |
|-----------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| New worked-example cartridge for a different domain                         | `<Domain>/` at the root, paralleling the five shipped examples                |
| New entry in the failure-modes catalog                                       | `_design-engine/_meta/FAILURE-MODES.md`                                       |
| New template for an OV-ship file                                             | `_design-engine/_templates/TEMPLATE-<name>.md`                                |
| Clarification, correction, or expansion in any engine file (00–07, BOOTSTRAP) | Edit in place; minor version bump                                            |
| Documentation fix (README, INSTALL, OPERATOR-GUIDE, this file)              | Edit in place                                                                  |
| New optional field on a cartridge backbone file (additive only)             | Update `_meta/SCHEMA-OF-SCHEMAS.md` + the template + minor version bump        |

## 2. What requires a major version bump (v2.0)

Any change that breaks existing cartridges:

- Adding a **required** field to `_ov-manifest.md`, `_design-state.md`, `_design-decisions.md`, or `_schema-draft.md`
- Renaming or removing an engine file
- Changing the cartridge folder convention (e.g., renaming `Sessions/`, `Artifacts/`)
- Restructuring the engine such that v1 cartridges can't be read
- Changing what `_design-state.md` is the source of truth for

Major bumps require: documented migration path, scripted or manual migration steps, clear `CHANGELOG.md` flag.

## 3. What is explicitly out of scope

- **Hardcoded references to a specific domain in `_design-engine/`.** The engine is subject-agnostic. Domain-specific guidance lives in worked-example cartridges, not the engine.
- **Personal data in shipped files.** No real names, emails, paths, or project references. Use placeholders.
- **AI-platform-specific code.** The system is markdown only. If you have Claude Skills, ChatGPT Custom GPT JSON, or platform-specific files, ship them in a clearly-marked `integrations/` directory as optional add-ons.

## 4. How to propose a change

### In-scope contribution (no version bump)

1. Locate the right path per §1.
2. Conform to existing conventions (read 2–3 existing files in the target folder first).
3. Test your change against at least one cartridge — does the engine still work?
4. Submit (PR if hosted on GitHub, or share by other means).

### Major version bump (v2.0)

1. Draft the schema/structure change as a markdown spec — what changes, why, what breaks, what migration looks like.
2. Author the migration path.
3. Test against multiple cartridges of different shapes.
4. Update `CHANGELOG.md` flagging the break.
5. Update `VERSION.md`.

## 5. Voice and tone conventions

When authoring engine content (`_design-engine/` and its subfolders):

- **Subject-agnostic.** Never name a specific domain except in illustrative tables.
- **Peer register.** Adult learner, direct, substantive. Match the tone of existing files.
- **No flattery, no filler.** "Great question," "interesting," etc. are forbidden.
- **No emojis.** Plain prose.

When authoring docs at the root (README, INSTALL, OPERATOR-GUIDE, this file): explanatory prose is fine. Still no emojis, still no flattery.

## 6. Content zones (Convention 8)

Every file in this repo belongs to one of four zones. Knowing which zone a file is in tells you whether the release owns it (the engine) or the operator owns it.

### Engine Zone — release-owned; updated by `git pull`

| Path pattern | Notes |
|--------------|-------|
| `README.md`, `AI-BOOTSTRAP.md`, `INSTALL.md`, `OPERATOR-GUIDE.md`, `CONTRIBUTING.md`, `LICENSE.md`, `VERSION.md`, `CHANGELOG.md` | Front-door docs |
| `_design-engine/**` | Engine prose, templates, meta, validator |
| `_types/**` | Convention 6 — OVE's own Prototype definitions |
| `_USER.md.template` | Template only; the populated `_USER.md` is operator-private |
| `.gitignore` | This file defines the Operator-Private patterns below |

**Engine Zone files do not get hand-edited by operators.** Customizations belong in the Operator-Extension Zone.

### Operator-Private Zone — gitignored; never tracked

| Pattern | Why |
|---------|-----|
| `_USER.md` | Operator profile; identity, communication preferences, private context (per `_meta/FAILURE-MODES.md` F3) |
| `<Cartridge>/_design-state.md` | Per-cartridge state; operator's active design work |
| `<Cartridge>/Sessions/*.md` | Per-cartridge session logs; verbatim AI/operator conversation |
| `.DS_Store`, `.obsidian/`, IDE cache files | Filesystem-noise |

These patterns are in `.gitignore`. If you want to track your own design history despite the default ignore, see `INSTALL.md § 3a`.

### Operator-Extension Zone — operator-created; survives `git pull`

The OV is designed to be extended at the OV root by adding new design cartridge folders parallel to the shipped examples.

| Pattern | Notes |
|---------|-------|
| `<Cartridge>/` at the OVE root | Your own design cartridges; not in the release; untracked unless you `git add -f` |

`git pull` never touches Operator-Extension folders because they aren't in the release tree.

### Shipped Examples Zone — release-owned; updated by `git pull`

| Path | Notes |
|------|-------|
| `Long-Form-Writing/` | OVE worked example |
| `LifeLong-Learning-Retrospective/` | OVE worked example |
| `Negotiation-Preparation/` | OVE worked example |
| `Relationship-Cultivation/` | OVE worked example |
| `SOLVE-eX-Retrospective/` | OVE worked example |

**Shipped Examples are reference implementations.** If you want to riff on one, copy it into an Operator-Extension Zone cartridge.

## 7. Sharing cartridges

A worked-example cartridge is a complete `<Domain>/` folder. To share as a contribution:

- Strip personal references (any real names, sensitive details, project specifics)
- Submit as a PR adding `<Domain>/` at the OVE root with the standard internal structure
- Useful for demonstrating the OV pattern's range across domains

## Version

This contribution guide ships with Operating-Volume-Engineering v1.2.0.
