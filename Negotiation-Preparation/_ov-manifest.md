---
Item_Prototype: OVE_OV_Manifest
Item_ID: "negotiation-prep-manifest"
Title: "Negotiation-Preparation — Fresh Worked Example"
Date_Added: 2026-06-01
Date_Modified: 2026-06-01
Needs_Processing: false
ove_ov_name: "Negotiation-Preparation"
ove_ov_slug: "negotiation-prep"
ove_design_phase: artifact-draft
ove_user_name: "<USER_NAME placeholder — never inferred from indirect signals>"
ove_bootstrapped: 2026-06-01
ove_engagement_kind: fresh-worked-example
---

# Negotiation-Preparation — Fresh Worked Example (Anchor Demonstration)

> **This is the anchor worked example for OVE v1.0. It demonstrates how a complete design engagement unfolds from scratch. The OV being designed: a tool for preparing for specific negotiations — salary discussions, vendor contracts, real-estate deals, multi-party disputes, anything where preparation matters more than improvisation.**

## What this OV would be

An OV for **negotiation preparation**: helping a user systematically prepare for a specific, named upcoming negotiation. Each engagement is one specific negotiation, end to end:

1. **Stakeholder mapping** — who's at the table, what they want, what they fear, what they can give
2. **BATNA development** — your best alternative; their likely BATNA; the ZOPA (zone of possible agreement)
3. **Issue analysis** — what's actually being negotiated, in what order, with what tradeoffs
4. **Opening / anchor strategy** — what you'll lead with, what you'll concede, what's untouchable
5. **Concession planning** — what you'll trade away in what order
6. **Wargame** — role-play of likely conversation paths
7. **Post-mortem** — what happened, what surprised you, what to remember for next time

The cartridge analog is **a specific negotiation** — name, parties, date, stakes. The OV produces a structured prep document the user takes into the actual conversation, then a debrief after.

## Why this user would design this

The user has at least one important upcoming negotiation. They want more than ad-hoc prep — they want a structured, reusable system they can apply to every significant negotiation in their professional and personal life.

## Who is this for

Public release as an OVE worked example. In an actual production design engagement, scope would be defined by the user (just them; them + collaborators; etc.).

## Domain shape

- **Decisional** (high)
- **Relational** (high) — stakeholder dynamics central
- **Conceptual** (medium) — frameworks like BATNA, ZOPA, mutual gains, distributive vs integrative
- **Procedural** (medium) — concession sequencing is a procedure
- **Operational** (low)

## Cadence

**Episodic.** Each negotiation triggers an engagement. Engagement lifecycle:

- Prep (days to weeks before the conversation)
- Live (the conversation itself, sometimes a single meeting, sometimes a multi-session series)
- Post-mortem (within a week after)

## Multi-session evidence

Strong:

- Prep typically unfolds over multiple sessions as new information surfaces
- Live negotiations themselves may span multiple sessions
- Post-mortem informs the next negotiation
- A negotiator improving over time wants their post-mortems to be searchable / referenceable

## Output target

Per cartridge:

- **Prep document** — stakeholder map + BATNA analysis + opening strategy + concession plan + wargame scenarios
- **Post-mortem document** — what happened, what surprised, what to remember

Across cartridges:

- A growing library of patterns — what works with this counter-party type, what fails, what surprises recur

## Prior art

- Fisher & Ury, *Getting to Yes* (interest-based negotiation, BATNA, mutual gains)
- Stuart Diamond, *Getting More* (perception-of-fairness, emotional intelligence in negotiation)
- Chris Voss, *Never Split the Difference* (tactical empathy, calibrated questions)
- Howard Raiffa, *The Art and Science of Negotiation* (analytical / game-theoretic frame)

The OV would integrate these without copying them. The schema reflects the underlying domain, not any one framework.

## Stakes and safety

High. Bad negotiations have lasting consequences (financial, professional, relational). The OV needs:

- **Safety routing** — for high-conflict situations involving legal exposure, the OV routes the user to a lawyer
- **Personal-relationship caveat** — for negotiations inside ongoing relationships (marriage, family, partnership), the OV flags that "winning" can damage the relationship and proposes integrative framing first

## Communication preferences

Peer register, direct, substantive critique. Negotiation prep is high-stakes; flattery wastes the user's time.

## Scope boundaries

- Not legal advice. Hard stop on anything that looks like substituting for counsel.
- Not therapy. Hard stop on anything that looks like substituting for a therapist (especially for family/relationship negotiations).
- Not a manipulation toolkit. The OV refuses to design persuasion against the counter-party's clearly-articulated interests.

## Notes for OV design students

This is the anchor worked example because:

1. The domain is **clearly OV-shaped** (multi-session, stateful, structured, substrate-agnostic value)
2. The shape is **distinct from SOLVE-eX and LLL** (episodic-with-deadline, not open-ended; pre-deliverable + post-deliverable; relational primary)
3. The schema requires **interesting design choices** — what's an atom (a *party*? a *concession*? an *issue*?), what's the cartridge backbone, what custom activities are needed
4. Safety routing is real and needs to be designed in, not bolted on
