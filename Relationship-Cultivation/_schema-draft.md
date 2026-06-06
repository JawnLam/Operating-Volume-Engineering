---
Item_Prototype: OVE_Schema_Draft
Item_ID: "relationship-cultivation-schema-draft"
Title: "Relationship-Cultivation — Schema Draft (in progress)"
Date_Added: 2026-06-01
Date_Modified: 2026-06-01
Needs_Processing: false
ove_OV_Name: "Relationship-Cultivation"
ove_Schema_Status: drafting
---

# Relationship-Cultivation — Schema Draft (in progress)

> **Incomplete. Q1–Q3 and Q5/Q6/Q9 are partially answered; the others would be filled across 4–6 more design sessions.**

## Q1 — Kinds of knowledge or work

- **Relational** (primary)
- **Operational** (high)
- **Declarative/factual** (medium)
- **Decisional** (low)

## Q2 — Canonical authorities

None in the formal sense. No single canon for "how to be a good friend to important people." Folk wisdom, some attachment-theory literature, some etiquette traditions, but no domain-authoritative text the OV is structured around.

## Q3 — Smallest quizzable / actionable unit

**Tentative atom types:**

- **Touch** — a single contact event (text, call, meal, card)
- **Context-Note** — a factual thing to remember (their kid started college this fall)
- **Thread** — an ongoing topic across multiple touches (the book they've been writing)
- **Commitment** — something the user promised
- **Tradition** — recurring touch (birthday, annual dinner, etc.)

Plus the **Person** atom (the cartridge itself), which has its own frontmatter and body sections — not really a separate atom type so much as the cartridge backbone.

## Q4 — Relationships between atoms

*Not yet specified.*

## Q5 — Natural progression

Per-cartridge: no curricular progression. Ongoing engagement until the relationship ends (the user stops, the other person stops, life changes, death). Cartridges can be archived but rarely "complete."

Across cartridges: no network-level progression either. The OV is maintained continuously, not progressed through.

## Q6 — Mastery / completion endpoint

Not applicable in the SOLVE-eX or LLL sense. The "endpoint" is **a richer relational life** — more thoughtful touches, fewer missed moments, deeper conversations because context is preserved. Not measurable as a finished artifact.

Possible *proxy* indicators:
- Reduced "I haven't been in touch with [person] in months" guilt
- More thoughtful gifts and gestures
- The user's important people report (when asked) that the user is a thoughtful presence in their life

## Q7 — Custom session activities

*Not yet specified. Likely candidates:*

- **TOUCH-LOG** — record a touch that happened
- **CONTEXT-REFRESH** — review what's stored about a person before a planned contact
- **NETWORK-AUDIT** — scan the network for gaps, overdue commitments, upcoming events
- **ANNUAL-AUDIT** — deeper retrospective on relational priorities

## Q8 — Mastery scale

Not applicable in the per-atom sense. Possibly per-Person relational health: thriving / stable / drifting / lapsed. But this is sensitive — putting your friends on a health scale feels gross.

Tension to resolve: do we need a mastery scale at all for a relational OV?

## Q9 — What does a cartridge represent?

**One person** the user is intentionally cultivating contact with. Cartridges:

- `Marcus-K/`
- `Aunt-Linda/`
- `Mentor-Sarah/`
- `Best-Friend-J/`

The user chooses how to slug; it doesn't have to be the person's real name.

## Q10–Q13

*Not yet answered.*

## Cross-cartridge state — open question

The OV has **network-level state** that doesn't fit any single cartridge. Recurring touch-gap reports, birthday rollups, network-wide commitment tracking. This needs explicit schema design — either:

- Network-level state file derived from cartridges (more flexible; harder to keep consistent)
- Network-level state file maintained separately (consistent; harder to keep in sync with cartridge edits)
- Network-level *atoms* (a new schema layer) that live at the OV root, not in any cartridge

This is the same pattern that surfaced in Negotiation-Preparation's Pattern atoms (cross-cartridge learning). Worth surfacing as a v1.x extension to OVE itself: explicit support for OV-level atoms beyond cartridges.

## Note on incomplete schema

This cartridge demonstrates an OV design at 2 sessions in, with the **unusual cartridge shape** (cartridge = person; cross-cartridge view first-class) and the **ethics-first design** that the domain demands.

A full schema lock would need approximately 4–6 more SCHEMA-DESIGN sessions to resolve the cross-cartridge state question, the active-vs-ambient nudging model, and the mastery-scale question (or its absence).
