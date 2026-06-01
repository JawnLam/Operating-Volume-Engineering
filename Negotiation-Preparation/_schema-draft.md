---
Item_Prototype: OVE_Schema_Draft
Item_ID: "negotiation-prep-schema-draft"
Title: "Negotiation-Preparation — Schema Draft"
Date_Added: 2026-06-01
Date_Modified: 2026-06-01
Needs_Processing: false
ove_ov_name: "Negotiation-Preparation"
ove_schema_status: locked
---

# Negotiation-Preparation — Schema Draft

## Q1 — Kinds of knowledge or work

- **Decisional** (high) — choices: opening, concession, walk-away
- **Relational** (high) — stakeholder dynamics, interests, fears
- **Conceptual** (medium) — frameworks (BATNA, ZOPA, integrative-distributive distinction)
- **Procedural** (medium) — concession sequencing, opening anchoring
- **Operational** (low) — scheduling, follow-up

## Q2 — Canonical authorities

No single canonical text; multiple complementary traditions:
- Harvard Negotiation Project (Fisher, Ury, Patton; Diamond)
- Tactical (Voss; Karrass)
- Game-theoretic (Raiffa; Schelling)
- Cross-cultural (Salacuse)

The OV integrates without privileging.

## Q3 — Smallest quizzable / actionable unit

**Atom types — five:**

- **Party** — a stakeholder
- **Issue** — a negotiated point
- **Concession-Asset** — a tradeable value
- **Tactic** — a specific move
- **Pattern** — a cross-negotiation recurring shape (lives at OV level, not cartridge)

## Q4 — Relationships between atoms

| Relation | Between | Captured in |
|----------|---------|-------------|
| `wants` | Party → Issue | Party atom frontmatter |
| `fears` | Party → outcome | Party atom body |
| `can-give` | Party → Concession-Asset | Party atom body |
| `traded-for` | Concession-Asset ↔ Concession-Asset | Concession-Asset body |
| `appropriate-for` | Tactic → Pattern / Issue | Tactic frontmatter |
| `recognized-in` | Pattern → Cartridge | Pattern frontmatter |
| `applied-by` | Pattern ↔ Party | Pattern body |
| `escalates-to` | Issue → safety-route | Issue body |

## Q5 — Natural progression

Per cartridge: lifecycle (prep → live → post-mortem → closed). Not curricular (no phase structure).

Across cartridges: Pattern mastery accumulates (recognized → applied → mastered).

## Q6 — Mastery / completion endpoint

Per cartridge: a closed cartridge with a usable post-mortem.

Across cartridges: a body of Pattern atoms the user can deploy instinctively. The user's negotiation outcomes improve over time, measured by their own assessment + observable indicators (better terms, less stress, fewer surprises).

## Q7 — Custom session activities

Six (defined in `_design-decisions.md` Decision 3):

- **STAKEHOLDER-MAP**
- **BATNA-ANALYSIS**
- **ISSUE-FRAMING**
- **CONCESSION-PLAN**
- **WARGAME**
- **POST-MORTEM**

Each has trigger conditions in `_negotiation-engine/01-NEGOTIATION-FOUNDATIONS.md`.

## Q8 — Mastery scale

**Per-Pattern, not per-atom.** Three levels:

- **recognized** — the user has seen this pattern in a real negotiation
- **applied** — the user has successfully navigated the pattern
- **mastered** — the user recognizes the pattern early and adjusts without conscious effort

Tracked in the Pattern atom's `ove_mastery_level` field.

## Q9 — What does a cartridge represent?

**A specific negotiation.** Named, dated, with identifiable counter-party. Examples:

- `Acme-Salary-2026-07/`
- `Vendor-Contract-Buildit-2026-Q3/`
- `Property-Sale-Smith-2026-06/`
- `Estate-Settlement-Family-2026-Q4/`

## Q10 — Cartridge backbone files

- `_negotiation-manifest.md` — what this negotiation is, parties, stakes, date
- `_state.md` — current lifecycle stage, progress
- `_stakeholder-map.md` — Party atoms for this negotiation (this cartridge's instance)
- `_issues.md` — Issue atoms for this negotiation
- `_concessions.md` — Concession-Asset atoms
- `_tactics-deployed.md` — Tactic atoms used or planned
- `_wargame-scenarios.md` — likely conversation paths
- `_prep-summary.md` — the document the user takes into the conversation
- `_post-mortem.md` — after-action report
- `Sessions/` — design conversations
- `Patterns-Recognized/` — Pattern atoms recognized in this cartridge (sym-linked from OV-level patterns)

## Q11 — State-persistence contract

- `_state.md` — Mode C (overwrite at session end)
- `_negotiation-manifest.md` — Mode C (overwrite when scope changes)
- `_stakeholder-map.md`, `_issues.md`, `_concessions.md` — Mode D (append-friendly; entities accrete during prep)
- `_wargame-scenarios.md` — Mode D
- `_prep-summary.md` — Mode D until live, then Mode E (immutable — the user takes this into the conversation)
- `_post-mortem.md` — Mode D during post-mortem, then Mode E
- `Sessions/*.md` — Mode E
- Pattern atoms (OV-level) — Mode D (mastery levels update; body accretes notes)

## Q12 — Templates list

Eight templates in `_negotiation-engine/_templates/`:

1. `TEMPLATE-negotiation-manifest.md`
2. `TEMPLATE-state.md`
3. `TEMPLATE-stakeholder-map.md`
4. `TEMPLATE-issues.md`
5. `TEMPLATE-concessions.md`
6. `TEMPLATE-wargame-scenarios.md`
7. `TEMPLATE-prep-summary.md`
8. `TEMPLATE-post-mortem.md`

Plus Session log + Pattern atom templates.

## Q13 — Bootstrap-new-cartridge protocol

`BOOTSTRAP-NEW-NEGOTIATION.md` in the engine. Asks the user, one question at a time:

- What's the negotiation? (counter-party, topic, date)
- What's at stake? (financial, relational, reputational, legal)
- Where in the lifecycle? (just heard about it / scheduled / imminent / in progress)
- Who needs to be at the table on your side? (just you / + advisors / + lawyer / + collaborators)
- What's your current sense of your BATNA?
- Are there any safety / legal flags I should know about?

Then opens the cartridge with `_negotiation-manifest.md` populated.
