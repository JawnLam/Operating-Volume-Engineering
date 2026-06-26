---
type: OVE_Schema_Draft
timestamp: "2026-06-01T00:00:00Z"
Item_ID: "long-form-writing-schema-draft"
title: "Long-Form-Writing — Schema Draft (in progress)"
Date_Added: 2026-06-01
Date_Modified: 2026-06-01
Needs_Processing: false
ove_OV_Name: "Long-Form-Writing"
ove_Schema_Status: drafting
---

# Long-Form-Writing — Schema Draft (in progress)

> **This schema is incomplete. The worked example deliberately stops mid-design. Q1–Q3 and Q5/Q6/Q9 are partially answered; the others would be filled in over 4–6 more design sessions.**

## Q1 — Kinds of knowledge or work

- **Creative/interpretive** (primary)
- **Procedural** (high) — writing is a daily practice
- **Conceptual** (medium) — structural design, voice
- **Declarative/factual** (varies — high for non-fiction; low for fiction)

## Q2 — Canonical authorities

No single canon. Multiple traditions: craft books (Strunk, King, Le Guin, McKee), genre-specific masters, the writer's own taste. The OV doesn't privilege any single voice.

## Q3 — Smallest quizzable / actionable unit

**Tentative atom types** (not yet locked):

- **Beat** — a single dramatic or rhetorical move (smallest)
- **Scene** (fiction/screenplay) or **Section** (non-fiction) — composed of beats
- **Chapter** — composed of scenes/sections (where applicable)
- **Character** (fiction) or **Thread** (non-fiction) — recurring elements that span scenes
- **Source** — books, papers, interviews (heavier for non-fiction)
- **Note** — unplaced fragment, idea, possible inclusion

Open question: does the smallest unit differ between fiction and non-fiction enough to warrant separate OVs? Or does the schema branch on `genre`?

## Q4 — Relationships between atoms

*Not yet specified. Tentative:*

- `contained-by` — Beat → Scene → Chapter
- `follows` — Scene → Scene (sequence)
- `appears-in` — Character → Scene
- `cites` — Section → Source (non-fiction)
- `unplaced-for` — Note → potential location

## Q5 — Natural progression

Per-cartridge: phases of work (drafting → revising → editing → polishing → finishing). NOT a curriculum — this is project-lifecycle, similar to Negotiation-Prep's lifecycle stages but with different stage names.

## Q6 — Mastery / completion endpoint

A finished manuscript. *Concretely:* a draft the writer is willing to send to a beta reader / editor / agent / publisher / committee — whoever the next external reader is.

## Q7 — Custom session activities

*Tentative:*

- **OUTLINE** — structural design
- **DRAFT** — generate new prose
- **REVISE** — pass over existing prose
- **RESEARCH-INTEGRATION** — fold sources into work (non-fiction)
- **READ-THROUGH** — assess work at higher scale than line edit
- **STUCK-DIAGNOSTIC** — when the writer is blocked

## Q8–Q13

*Not yet answered. Would take 4–6 more SCHEMA-DESIGN sessions.*

## Note on incomplete schema

This cartridge demonstrates **what an OV design looks like 2 sessions in.** A full schema lock would require continuing through Q4 and Q7–Q13, with particular attention to:

1. The fiction-vs-non-fiction question (one OV or two)
2. Voice consistency model
3. Research integration depth (especially for dissertation use)
4. The interaction between daily-cadence and macro-structure work
