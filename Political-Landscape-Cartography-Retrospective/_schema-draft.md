---
type: OVE_Schema_Draft
timestamp: "2026-06-13T00:00:00Z"
Item_ID: "plc-retrospective-schema-draft"
title: "Political-Landscape-Cartography — Retrospective Schema Draft"
Date_Added: 2026-06-13
Date_Modified: 2026-06-13
Needs_Processing: false
ove_OV_Name: "Political-Landscape-Cartography"
ove_Schema_Status: shipped
---

# Political-Landscape-Cartography — Retrospective Schema Draft

> **Retrospective answers to Q0–Q14 for PLC v1.0.0 (shipped 2026-06-13). Demonstrates the v2.1 schema-design protocol applied to a practice-archetype OV. The Q6 fork (Q6a finite-horizon / Q6b practice) is shown in concrete form for the practice path.**

## Q0 — Namespace prefix

`plc_` (Political Landscape Cartography).

## Q1 — Kinds of knowledge or work

Mixed; weighted toward decisional, relational, and procedural:

- **Decisional** (primary) — political moves under uncertainty; ethical trade-offs; resource allocation
- **Relational** (primary) — actors, alliances, debts, perception gaps
- **Procedural** (high) — ADAPT Loop cycles; sphere-open / sphere-close protocols; OPC Assessment walkthrough
- **Conceptual** (high) — political-capital theory; 9-type resource taxonomy; pattern atoms
- **Operational** (medium) — cycle logging; resource ledger maintenance; cross-engagement portfolio tracking
- Lighter: formal/propositional, declarative/factual, experiential, creative

## Q2 — Canonical authority

The Methodology Author's 2018 Pepperdine dissertation is the canonical authority for the political-capital theory, 9-type resource taxonomy, and tactical move catalogue (Table 3). Secondary: the ADAPT Loop Field Manual (operational), OPC Assessment v3.0 (diagnostic), Political Warfare Catalogue (50 theorists across 16 strategies).

## Q3 — Smallest unit

A **Move** (in Catalogue / dissertation Table 3 terms) or a **cycle constituent** (in ADAPT operational terms). A Move is the smallest unit of political action with a classifiable signature (Option Affected, Consideration Affected, Effect on Component). A cycle constituent is the smallest unit of cycle structure (actor / interest / move / target).

## Q4 — Relationships between Items

- **Hierarchical:** sphere contains engagements; engagement contains cycles; cycle contains constituents; constituent references actors and moves
- **Sequential:** cycle constituents in slash-addressing order (`α.actor/δ.detection/i.interest/...`)
- **Causal:** move affects target's decision matrix; debt accrues to actor over cycles
- **Reference:** move cites theorist; cycle cites OPC § X.Y; cartridge cites dissertation p.NNN
- **Logical:** prerequisite-of (resource X enables move Y); contrasts-with (archetype A vs archetype B)
- **Lateral:** related-to (cross-sphere pattern recognition)

## Q5 — Natural progression

Phased: pre_engagement → routine → close_out → closed for engagement lifecycle (D22). Within an engagement: cycles run in arbitrary order; no strict sequence beyond the ADAPT five-beat per cycle. Across engagements: the operator's practice has no natural progression (practice archetype).

## Q6 — Mastery / completion endpoint

**Q6b path — practice archetype (per CQ11 / `ove_OV_Archetype: practice`).**

Three-layer mastery signal:

### L1 — Per-cycle: audit-trail integrity

Every cycle the operator runs IS a mastery demonstration. The observable: did the cycle's required disciplines all complete?

- Alternatives audit complete? (Did the operator consider at least N alternative moves before selecting?)
- Ethical accounting complete? (Did the operator walk the 3×10 harm grid + 5 ethical frameworks?)
- Perception-gap capture at cycle-close? (Did the operator log what they expected the target to do vs what the target did?)
- Tactic explicitly selected (not stumbled into)?

Each cycle passes or fails this audit; the per-engagement audit-pass-rate is the L1 quality metric.

### L2 — Per-engagement: sphere-close retrospective

The OV produces a sphere-close retrospective at engagement-close (per D13). Contents:

- Cycles run + their audit-pass rate
- Campaigns opened / executed / closed with their lifecycle history (D22)
- Per-actor perception-gap trajectory (gap delta over cycles, D5)
- Per-principal resource trajectory (9-type ledger over time)
- Forecasted-vs-actual outcomes (D21 family 12)
- Pattern-recognition accuracy (D21 family 4)
- Eight Benefits inventory at sphere-open vs sphere-close (D4)
- Explicit instances where the OV's `UNCOVER` output produced action that wouldn't have happened otherwise
- For consultant mode: handoff documentation per OPC § 17.7

**This is the closest a practice OV has to a terminal artifact** — bounded, concrete, observable, recurring on every engagement-close.

### L3 — Per-operator practice: longitudinal signals

The operator's overall practice has signals, not endpoints:

- Forecast skill calibration improving across engagements (D21 family 12)
- No-loop discipline holding rate (cycles correctly rescoped vs forced-through)
- Pattern-tagging accuracy (D10, D15)
- Recursive resource accumulation aggregate (per dissertation thesis)
- For consultants: cross-client portfolio quality

No terminal state at this layer. The practice is a trajectory.

### Meta-cartridge decision

**Structured export at sphere-close; no meta-cartridge in v1.0.** Each sphere exports its L3 signals as structured data (YAML / JSON) that the operator composes into their own cross-engagement practice tracker outside the OV. v1.0 ships without a meta-cartridge architecture; future v2.x may add one if demand surfaces from operators running multiple spheres in parallel.

## Q7 — Custom session activities

PLC adds three activities beyond the six universal OVE ones (which apply to *designing* PLC, not *using* it):

- **CYCLE-OPEN** — opens a new ADAPT Loop cycle within an active sphere; populates initial Agenda / Decide constituents
- **CYCLE-RUN** — executes the five-beat ADAPT protocol for an in-progress cycle (one beat per session typical)
- **SPHERE-CLOSE** — runs the L2 retrospective deliverable per Q6b above; exports L3 signals

Plus two cross-cutting:

- **OPC-WALKTHROUGH** — runs the OPC v3.0 sphere diagnostic (17 sections, 6-level hierarchical IDs)
- **CATALOGUE-LOOKUP** — searches the Political Warfare Catalogue (782 tactics, 16 strategies, 84 clusters, 50 theorists) for moves matching a current cycle's constituents

## Q8 — Mastery / progress scale

Per-archetype:

- For cycles: pass / partial / fail on the audit-trail-integrity check (L1)
- For engagements: closeable / closed (binary, with L2 retrospective quality scored qualitatively)
- For the operator's practice: trajectory metrics (L3) — none of which has a "mastered" terminus

No 0-5 Bloom-style scale — practice archetype rejects the destination framing. The operator's L3 signals improve indefinitely.

## Q9 — Cartridge representation

A **sphere** represents one engagement — either a consultant-client engagement or a principal-self-coaching context. A sphere has a defined open (sphere-open ritual) and close (sphere-close retrospective + L3 export). Multiple spheres in parallel for consultant operators with portfolios.

## Q10 — Cartridge backbone files

Per sphere:

- `_sphere-manifest.md` (PLC_Sphere_Manifest) — what this engagement is, who, scope, eight benefits inventory at open
- `_sphere-state.md` (PLC_Sphere_State) — current cycles open, current campaigns, current actor map snapshot
- `_sphere-decisions.md` (PLC_Sphere_Decisions) — append-only locked decisions, escalations
- `_actor-map.md` (PLC_Actor_Map) — actors + their resource holdings + perception gaps
- `_resource-ledger.md` (PLC_Resource_Ledger) — 9-type resource accounting per cycle
- `Cycles/` — one .md per ADAPT Loop cycle
- `Sessions/` — session logs across the engagement

## Q11 — State-persistence contract

- `_sphere-state.md` — overwrite-with-history (latest state on top, prior states in collapsed history block below)
- `_sphere-decisions.md` — append-only
- `_actor-map.md` — overwrite-with-history per actor entry
- `_resource-ledger.md` — append-only per cycle entry
- `Cycles/<cycle-id>.md` — overwrite during cycle (in-progress); frozen at cycle-close
- `Sessions/<date>_<NNN>_<activity>.md` — write-once per session

## Q12 — Templates

PLC ships templates for every cartridge backbone file (PLC_Sphere_Manifest, PLC_Sphere_State, PLC_Sphere_Decisions, PLC_Actor_Map, PLC_Resource_Ledger, PLC_Cycle, PLC_Session). Plus templates for Catalogue Items (PLC_Tactic, PLC_Strategy, PLC_Theorist), pattern atoms (PLC_Pattern_Stakeholder_Archetype, etc.), and the dissertation Table 3 moves (PLC_Move).

## Q13 — Bootstrap-new-cartridge protocol

PLC's `BOOTSTRAP-NEW-SPHERE.md` asks five clarifying questions per engagement-open:

1. What is this engagement? (consultant-client / principal-self-coach / other; describe the political situation in one paragraph)
2. Who is the principal? (named; their role; their stated objectives)
3. What's the engagement horizon? (weeks, months, quarters, open-ended)
4. What's the sensitivity? (internal-only / shareable with peer / public-eligible — drives export-redaction profile)
5. What are the eight benefits the principal is pursuing in this engagement? (D4 Eight Benefits inventory at sphere-open)

Plus a confirmation step where the AI proposes the initial actor map skeleton from the principal's description and the operator approves before cycle-open.

## Q14 — Audience register declaration

- **Target reader:** COO of a $20B+ market-cap public company aspiring to CEO within five years. Secondary: Senior Managing Partners at strategy consultancies running political engagements with C-suite principals.
- **Business / life context:** Active client engagement where political navigation determines whether strategic moves land — or principal-self-coaching context preparing for a board interaction, reorg, succession, or high-stakes political conversation.
- **Prose register:** Senior Managing Partner at a global strategy consultancy speaking to a peer. Direct, substantive, no flattery, no academic jargon at business dinners. No deliverable-promise nouns without substrate (dashboard, scorecard, etc.).

This Q14 declaration cascaded into PLC's prose voice during ARTIFACT-DRAFT and is verified at SHIP-PREP Phase 3.9 (Vocabulary Audit).

---

## Derived schema documents

### Prototype definitions

PLC namespace declares 16 Prototypes:

- `PLC_Sphere_Manifest`, `PLC_Sphere_State`, `PLC_Sphere_Decisions` (cartridge backbone)
- `PLC_Actor_Map`, `PLC_Resource_Ledger`, `PLC_Cycle`, `PLC_Session` (sphere content)
- `PLC_Tactic`, `PLC_Strategy`, `PLC_Theorist`, `PLC_Move` (Catalogue + dissertation)
- `PLC_Pattern_Stakeholder_Archetype`, `PLC_Pattern_Change_Initiator_Posture`, `PLC_Pattern_Opposition_Posture`, `PLC_Pattern_Arc_Dynamic`, `PLC_Pattern_Power_Dynamic_Theme`, `PLC_Pattern_Ethical_Dilemma` (pattern atoms — 6 families totaling 72 atoms)

Each Prototype shipped with its own `_types/PLC_<TypeName>.md` per Convention 6.

### Relationship vocabulary

Per Q4 above. The slash-addressing notation (`α.<actor>/δ.<detection>/i.<interest>/...`) is PLC-specific and operates within cycle constituents.

### Folder structure

```
Political-Landscape-Cartography/
├── README.md, INSTALL.md, OPERATOR-GUIDE.md, CONTRIBUTING.md, LICENSE.md, VERSION.md, CHANGELOG.md, AI-BOOTSTRAP.md, UPDATE-PROMPT.md, BOOTSTRAP-NEW-SPHERE.md
├── .gitignore (excludes _frameworks/sources/Lam-2018-Pepperdine.pdf per Convention 9)
├── _plc-engine/
│   ├── 00-START-HERE.md ... 07-SHIPPING-CHECKLIST.md
│   ├── _meta/ (SCHEMA-OF-SCHEMAS, FAILURE-MODES)
│   ├── _templates/ (per-Prototype templates)
│   └── _yaml/ (scaffolding YAML)
├── _types/ (16 files per Convention 6)
├── _PATTERNS/ (6 family folders, 72 pattern atoms)
├── _frameworks/
│   ├── ADAPT.md, OPC-Assessment.md, 4R.md, 4R-coaching-script.md, ...
│   ├── sources/
│   │   ├── Lam-2018-Pepperdine.pdf (LOCAL ONLY — gitignored per Convention 9)
│   │   └── Lam-2018-Pepperdine.md (placeholder; ships per Convention 9)
│   ├── dissertation-table-3/ (3 worked Move files at v1.0; ~95 backlog for v1.0.1)
│   └── political-warfare-catalogue/ (tactics, strategies, theorists)
└── Spheres/<sphere-name>/ (operator's engagement cartridges; operator-private per Convention 8)
```
