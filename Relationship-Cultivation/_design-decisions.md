---
Item_Prototype: OVE_Design_Decisions
Item_ID: "relationship-cultivation-decisions"
Title: "Relationship-Cultivation — Design Decisions Log"
Date_Added: 2026-06-01
Date_Modified: 2026-06-01
Needs_Processing: false
ove_ov_name: "Relationship-Cultivation"
---

# Relationship-Cultivation — Design Decisions Log

## Decisions

### 2026-06-01 — Decision 1: Cartridge = one person

**Decided:** Each cartridge represents one important personal relationship — a person the user is intentionally cultivating contact with over the long term. Cartridge naming: `<Person-Slug>/` (using a slug the user chooses; doesn't have to be a real name).

**Alternatives considered:**
- One cartridge per relationship category (friends, mentors, family) — rejected: collapses individuals into groups; loses per-person depth
- One cartridge per touch / event — rejected: too granular; relationships span events
- One global cartridge — rejected: loses person-level isolation

**Rationale:** The unit of relational work is a person. Touches, conversations, commitments, traditions all cohere around a person.

**Implications:** Network view (across cartridges) becomes a first-class concern, since the user has many cartridges in active maintenance simultaneously.

---

### 2026-06-01 — Decision 2: Ethics as a dedicated engine chapter

**Decided:** `_relational-engine/05-ETHICS-AND-CONSTRAINTS.md` is a dedicated chapter. It covers:

- **Personal-information discipline** — factual notes only; never psychological interpretations the relationship-other hasn't volunteered
- **Refusal lines** — the OV will not help design manipulation, persuasion-against-stated-interests, or other relationship-harming behavior
- **Therapy-adjacent routing** — when the cartridge starts being about what the user wants to *do to* the other rather than *do with* them, route to a therapist
- **Privacy and sharing** — cartridges are for the user's eyes only; sharing without the relationship-other's consent is a violation

**Alternatives considered:**
- Soft mention in another chapter — rejected: surveillance-adjacent domain demands explicit framing
- No ethics chapter — rejected: irresponsible for the domain

**Rationale:** Relational data is sensitive. Without explicit ethics, the OV slides toward manipulation toolkit territory.

**Implications:** Bootstrap mentions ethics upfront. Refusal patterns are baked into the engine, not just operator discretion.

---

### 2026-06-01 — Decision 3: Network view is a first-class concern

**Decided:** The OV has cross-cartridge state — a network-level rollup that surfaces patterns the user can't see by reading any single cartridge:

- *"You haven't been in touch with anyone in [category] for 2+ months"*
- *"Three people in your network have birthdays in the next 30 days"*
- *"You have a Commitment open with [person] that's overdue"*

Lives in a root-level file (tentatively `_network-state.md`) that's derived from cartridge state at session end.

**Alternatives considered:**
- Cartridges only (no network view) — rejected: misses the network-level patterns that are the point of the OV
- Network view as the primary structure with people as sub-units — rejected: loses per-person depth

**Rationale:** Both views are needed. Per-person for depth; per-network for breadth. The cross-cartridge atom problem (also surfaced in Negotiation-Prep with Patterns) is becoming a recurring pattern across OV designs.

**Implications:** State-persistence contract has to specify how the network rollup gets generated — derived from cartridges, or maintained separately and reconciled.

---

## Pattern emerging: cross-cartridge state

Both Negotiation-Preparation (Patterns) and Relationship-Cultivation (Network) need state that lives **above the cartridge level**. This is a recurring architectural pattern worth surfacing in OVE itself — perhaps as a v1.x extension to the schema-of-schemas documenting "OV-level atoms" as a valid pattern.

Logged for future OVE evolution consideration.

## Open decisions

- **D4 (open):** Atom types — exact set (Touch / Context-Note / Thread / Commitment / Tradition is tentative)
- **D5 (open):** Active vs. ambient nudging model — does the AI proactively raise gaps, or wait for user-initiated sessions?
- **D6 (open):** Per-cartridge state file vs. network-level state file with cartridge derivations
