---
Item_Prototype: OVE_Design_Decisions
Item_ID: "negotiation-prep-decisions"
Title: "Negotiation-Preparation — Design Decisions Log"
Date_Added: 2026-06-01
Date_Modified: 2026-06-01
Needs_Processing: false
ove_OV_Name: "Negotiation-Preparation"
---

# Negotiation-Preparation — Design Decisions Log

## Decisions

### 2026-06-01 — Decision 1: Cartridge = one specific negotiation

**Decided:** Each cartridge represents a single, named, dated negotiation. Cartridge naming convention: `<Counter-Party-or-Topic>-<YYYY-MM>/`. E.g., `Acme-Salary-2026-07/`, `Vendor-Contract-Acme-2026-Q3/`, `Property-Sale-Smith-2026-06/`.

**Alternatives considered:**
- One cartridge per counter-party (rejected: counter-parties recur in different negotiations with different stakes)
- One cartridge per quarter / year (rejected: collapses distinct negotiations into noise)
- One global cartridge (rejected: violates the multi-session-state-per-engagement model)

**Rationale:** Negotiations are episodic and case-shaped, like SOLVE-eX cases. The cartridge needs to hold prep + live + post-mortem state for one specific engagement.

**Implications:** Cartridges close (move to `_closed/` or get an `ove_Lifecycle_Stage: closed` flag) after the post-mortem. Active cartridges live in the root; closed ones get archived.

---

### 2026-06-01 — Decision 2: Five atom types

**Decided:**

- **Party** — a stakeholder in the negotiation (self, counter-party, advisor, lawyer, board, family, etc.)
- **Issue** — a specific point being negotiated (price, timeline, scope, terms, etc.)
- **Concession-Asset** — something one party can offer in exchange (money, time, scope, relationship value, future commitment)
- **Tactic** — a specific negotiation move available (anchoring, framing, calibrated questions, BATNA-reveal, etc.)
- **Pattern** — a recognized recurring shape across negotiations (e.g., *"counter-party plays high anchor"*, *"deadline pressure benefits them"*)

**Alternatives considered:**
- Single "atom" type — too generic
- Many narrow atoms (e.g., separate Concern / Want / Fear) — collapses cleanly into Party properties
- No "Tactic" atom — too thin without explicit tactic-level reasoning

**Rationale:** Five gives enough resolution without bloat. Each atom has a clearly-distinct role.

**Implications:** Per-atom-type frontmatter conventions need to be defined in `_schema.md`. Relationships are atom-type-specific (a Party `wants` an Issue; an Issue is `traded-by` a Concession-Asset; a Tactic is `appropriate-for` a Pattern).

---

### 2026-06-01 — Decision 3: Six custom session activities

**Decided:** Beyond OVE's six (INTERVIEW, SCHEMA-DESIGN, CARTRIDGE-SHAPE, ARTIFACT-DRAFT, REVIEW, SHIP-PREP — which are OVE-design-specific anyway), the negotiation OV defines:

- **STAKEHOLDER-MAP** — populate Party atoms, surface wants/fears/can-gives
- **BATNA-ANALYSIS** — your BATNA, their likely BATNA, the ZOPA, walk-away
- **ISSUE-FRAMING** — decompose the negotiation into named Issues; identify integrative opportunities
- **CONCESSION-PLAN** — sequence of trades, what's tradeable, what's untouchable
- **WARGAME** — role-play likely conversation paths; surprise testing
- **POST-MORTEM** — after the fact: what happened, what surprised, patterns to remember

**Alternatives considered:**
- Fewer activities (rejected: each captures genuinely different work)
- More activities (e.g., split BATNA-ANALYSIS into MINE and THEIRS — rejected: false granularity)

**Rationale:** Each maps to a distinct mode of work. Together they sequence the prep arc.

**Implications:** Session protocol algorithm needs trigger conditions for each. WARGAME has a sub-mode (AI plays counter-party? AI reasons about likely paths?) — that's an open question still.

---

### 2026-06-01 — Decision 4: Cartridge lifecycle stages

**Decided:** Each cartridge moves through four stages via `ove_Lifecycle_Stage` in `_state.md` frontmatter:

- **prep** — before the negotiation; default for new cartridges
- **live** — during; the conversation is happening (may span multiple sessions)
- **post-mortem** — after; capturing what happened and what to remember
- **closed** — work complete; cartridge archived

**Alternatives considered:**
- No formal stages (rejected: stages signal which activity is appropriate)
- More stages (e.g., "scheduled" before "prep") — rejected as over-engineering

**Rationale:** Activities make sense in stage-specific ways. STAKEHOLDER-MAP is for prep; WARGAME is for prep; POST-MORTEM is by definition after live.

**Implications:** State file tracks stage explicitly. Stage transitions are explicit events captured in the decision log.

---

### 2026-06-01 — Decision 5: Safety routing is its own engine chapter

**Decided:** `_negotiation-engine/06-SAFETY-AND-ROUTING.md` is a dedicated chapter (not a section buried in another chapter). It covers:

- When to route to a lawyer (anything with legal exposure: employment contracts, real-estate, family law, criminal matters)
- When to route to a therapist (negotiations inside ongoing relationships where emotional stakes dominate)
- When the OV refuses to proceed (clear ethical lines — designing manipulation, helping fraud, etc.)

**Alternatives considered:**
- Soft / advisory routing (rejected: high-stakes domain demands explicit routing)
- No safety routing (rejected: irresponsible for the domain)

**Rationale:** Negotiation has real failure modes — legal exposure, relationship damage, ethical drift. Explicit routing in a dedicated chapter mirrors SOLVE-eX chapter 9.

**Implications:** Some users will find this restrictive. The chapter explains why and when, so users understand the model.

---

### 2026-06-01 — Decision 6: Mastery scale = per-Pattern, not per-atom

**Decided:** The user's improvement isn't tracked at the atom level (Parties and Issues are specific to this negotiation) but at the Pattern level. A Pattern starts as `recognized` (the user sees it in a current negotiation), advances to `applied` (the user successfully navigated it), and reaches `mastered` (the user recognizes it instinctively across new negotiations).

**Alternatives considered:**
- Per-atom mastery (rejected: most atoms are negotiation-specific, can't aggregate)
- No mastery tracking (rejected: improvement should be visible)

**Rationale:** Patterns are the cross-cartridge atoms. They're where learning compounds.

**Implications:** Patterns live at the OV level (cross-cartridge), not in any single cartridge. Each cartridge's POST-MORTEM proposes additions to the pattern library.

---

## Patterns worth surfacing for other OV designs

1. **Episodic-with-lifecycle-stages** is a useful cartridge shape. Pattern transfers to legal-case-prep, medical-conversation-prep, sales-call-prep.
2. **Safety routing as a dedicated chapter** when the domain warrants it.
3. **Cross-cartridge atoms (Patterns)** for tracking improvement that wouldn't fit in any single cartridge.
4. **Mastery scale matched to the kind of learning** (per-pattern instead of per-atom).
