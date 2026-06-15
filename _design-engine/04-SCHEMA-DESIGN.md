---
Item_Prototype: Fleeting
Item_ID: ove-engine-04-schema-design
Title: "OVE Engine — 04 Schema Design"
Date_Added: 2026-06-01
Date_Modified: 2026-06-06
Needs_Processing: false
type: design-engine
role: schema-design-protocol
scope: subject-agnostic
updated: 2026-06-01
---

# 04 — SCHEMA DESIGN

> **How to design the schema of a new operating volume. This is the most important creative act of OV design. A bad schema produces a stilted OV; a good schema disappears into the work.**

## What "schema" means in an OV

A schema is the structural contract every artifact in the OV conforms to. It defines:

1. **The Prototypes** — the unit(s) of knowledge or work the OV produces (a "concept" in LLL, a "case file" in SOLVE-eX, a "design decision" in OVE)
2. **The relationships** — how Items link to each other
3. **The state model** — what state files exist, what they own
4. **The cartridge backbone** — what every cartridge has at minimum
5. **The session log structure** — how work is recorded
6. **The custom activities** — anything beyond the universal session-protocol activities

A well-designed schema makes the work feel natural; a poorly-designed schema forces the user to bend the work to fit.

## Convention compliance — the cascade from one early decision

Before Q1, the OV's namespace prefix is chosen. Everything else cascades from it. The full convention set lives in `_meta/CONVENTIONS.md`; the cascade is summarized here.

### Q0 — Namespace prefix

Ask the user:

> *"What namespace prefix will this OV use? Three to six lowercase letters, ending with an underscore. Example: `cook_` for a cooking OV; `negotiation_` for a negotiation-prep OV; `family_` for a family-operations OV."*

Once chosen, everything propagates automatically per `_meta/CONVENTIONS.md`:

- **Prototype names:** `<NAMESPACE_UPPER>_<TypeName>` (e.g., `COOK_Recipe`, `COOK_Technique`)
- **Property names:** `<namespace>_<Title_Snake_Case_Body>` (e.g., `cook_Recipe_Status`, `cook_Difficulty_Tier`). Acronyms in the body stay fully capitalized (`URL`, `ISBN`, `POV`).
- **Enum identifiers** (under `enums:` in schema): `<namespace>_<lowercase_plural>` (e.g., `cook_recipe_statuses`, `cook_difficulty_tiers`)
- **`Item_Prototype` value** on each Item: the prototype name from above
- **`Item_Prototype: Fleeting`** on non-Item files (front-door docs, engine prose, meta)

The operator's answer to Q0 determines all of these — there is no additional decision-making required for the case convention or the prototype-naming convention. They are locked.

If the operator wants different conventions than the defaults in `_meta/CONVENTIONS.md`, they tell you during this session. Log the override in `_design-decisions.md` so future sessions know which conventions apply.

## The Q1–Q8 protocol

Walk through these with the user, one at a time, conversationally. Don't rush.

### Q1 — What kind of knowledge or work does this OV consist of?

Choose all that apply, with relative weights:

- **Formal/propositional** (theorems, definitions, rules)
- **Conceptual** (ideas, frameworks, theories)
- **Procedural** (techniques, skills, methods)
- **Declarative/factual** (names, dates, data)
- **Experiential** (embodied, tacit, practiced)
- **Creative/interpretive** (works, performances, compositions)
- **Decisional** (choices under uncertainty, tradeoffs)
- **Relational** (people, dynamics, histories)
- **Operational** (recurring procedures, checklists)

The mix shapes everything downstream.

### Q2 — Who or what is the canonical authority in this domain?

Some domains have named experts (cybernetics has thinkers; philosophy has philosophers). Some have traditions (cuisine has regional traditions). Some have institutions (law has courts and codes). Some have none.

This question determines whether you need a "thinker" or "authority" Prototype.

### Q3 — What is the smallest quizzable / actionable / discussable unit?

That unit is what each Item in this OV represents. Anything smaller is a fragment; anything larger should decompose.

Examples:
- LLL: a concept (or a piece, a kanji, a technique, etc. — varies by subject cartridge)
- SOLVE-eX: a tool application within a case file
- OVE: a design decision

### Q4 — What relationships exist between Items?

Pick a vocabulary of named relations. Common patterns:

- Hierarchical: `contains` / `part-of`
- Sequence: `precedes` / `follows`
- Causal: `causes` / `caused-by`
- Reference: `originated-by` / `analyzed-by` / `cited-by`
- Logical: `prerequisite-of` / `instantiates` / `contrasts-with`
- Lateral: `related-to`

The relationships become wiki-links in Item bodies and structured fields in frontmatter.

### Q5 — Does the domain have a natural progression?

Some domains have strict prerequisite order (math). Some are lateral (cuisine). Some have phases (a study curriculum, a project lifecycle, a negotiation timeline).

This shapes the **cartridge progression** (curriculum, phases, stages, or none).

### Q6 — What does "done" look like?

**Q6 has two forms — the answer depends on the OV's archetype, declared in CQ11 (`BOOTSTRAP-NEW-OV.md`) and logged in the manifest's `ove_OV_Archetype` field. Confirm the archetype before answering Q6. If the archetype is not yet declared, return to CQ11 first.**

#### Q6a — Finite-horizon archetype (terminal artifact)

Concretely, what is the user trying to be able to *do* at the end of this kind of engagement? Be specific.

"Mastery" or "completion" is too vague. The mastery endpoint should be **observable** — a specific kind of artifact, demonstrated behavior, or measurable outcome.

Examples from existing OVs:

- LFW → a published manuscript
- LLL → a study subject mastered to teachable level
- SOLVE-eX → a solved problem with a documented decision path
- OVE → a shipped OV

#### Q6b — Practice archetype (three-layer mastery signal)

Practice OVs have no terminal artifact. The principal's engagement with the domain *continues* indefinitely. "Mastery" is operationalized as **observable signals at three nested time-scales**, each with its own contract.

**Layer 1 — Per-cycle: discipline demonstrated.** Every cycle the operator runs IS a mastery demonstration. The observable: *audit-trail integrity* — did the cycle's required disciplines (decision-quality audit, ethical accounting, perception-gap capture, alternatives review, whatever the OV requires) all complete? Each cycle either passes or fails this audit; the percentage that pass is a per-engagement quality metric.

**Layer 2 — Per-engagement: retrospective deliverable.** The OV produces an *engagement retrospective* at engagement-close. Contents: cycles run + their audit-pass rate; sub-engagement lifecycle history; trajectory metrics (whatever quantities the OV tracks per engagement); forecasted-vs-actual outcomes; explicit instances where the OV's machinery earned its keep. **This is the closest a practice OV has to a terminal artifact.** It's bounded, concrete, observable — and it ships at engagement-close, not at "done with the domain."

**Layer 3 — Per-operator practice: longitudinal signals across engagements.** The operator's overall practice has *signals*, not endpoints — calibration improving over time, discipline holding rate, pattern-recognition accuracy, aggregate quantitative trajectories the OV tracks, cross-engagement portfolio quality (if a consultant or principal-with-multiple-spheres). There is no terminal state at this layer. The practice is a trajectory.

Practice OVs answer Q6 by specifying:

- **L1 spec:** what audit-trail integrity check fires per cycle?
- **L2 spec:** what does the engagement-close retrospective contain?
- **L3 spec:** what longitudinal signals get exported at engagement-close for the operator's cross-engagement view?

Plus a **meta-cartridge decision:** does the OV ship with a meta-cartridge concept (one practice-level cartridge aggregating from N engagement cartridges), or does each engagement export structured data the operator composes externally? Default: **structured export, no meta-cartridge** — keeps the OV's schema clean and serves both solo-principal-self-coach and consultant-with-portfolio modes.

#### Why the fork matters

The pre-v2.0 framing of Q6 implicitly assumed every OV has a terminal artifact. v2.0 acknowledges that some OV domains — political navigation, longevity health, relationship cultivation, leadership development, financial stewardship — have **no terminal arrival**. The principal's engagement with the domain continues across their career or life-stage. Forcing those OVs into a finite-horizon Q6 frame produces stilted designs (the design conversation invents fake terminal artifacts; the shipped OV mis-represents itself to the operator). The fork lets each archetype answer Q6 in its own native form.

### Q7 — What subject-specific session activities are needed?

The six universal OVE activities (INTERVIEW, SCHEMA-DESIGN, CARTRIDGE-SHAPE, ARTIFACT-DRAFT, REVIEW, SHIP-PREP) work for OVE itself. The OV you're designing may need different activities.

Examples from existing OVs:
- LLL: TEACH, QUIZ-SR, QUIZ-SOCRATIC, REVIEW-WEAK, SYNTHESIZE, INTEGRATE
- SOLVE-eX: implicit in its 21-step process framework
- A negotiation-prep OV might have: STAKEHOLDER-MAP, BATNA-ANALYSIS, ROLE-PLAY, POST-MORTEM
- A writing OV might have: OUTLINE, DRAFT, REVISE, EDITORIAL-REVIEW
- A relational OV might have: TOUCH-LOG, CONTEXT-REFRESH, ANNUAL-AUDIT

Define each custom activity with its trigger conditions.

### Q8 — What's the right mastery / progress scale?

Default 0–5 (not-started → introduced → recognized → applied → mastered → teachable) works for most domains. Some need different scales:

- Language: CEFR (A1–C2)
- Skill: novice → apprentice → journeyman → master
- Project: not-started → drafting → review → polish → shipped
- Decision: framing → analysis → choice → execution → review

Pick what fits the domain.

## Beyond Q1–Q8 — additional schema questions

Once Q1–Q8 are answered, work through these:

### Q9 — What does a cartridge represent?

In LLL: a subject being studied. In SOLVE-eX: a problem being worked through. In OVE: an OV being designed. In a negotiation OV: a specific negotiation. In a writing OV: a specific manuscript-in-progress.

This is the **central abstraction** of the OV. Get it wrong and the whole shape feels off.

### Q10 — What cartridge backbone files exist?

At minimum, every cartridge needs:
- A **manifest** — what this engagement is, who it's for, scope, goals
- A **state file** — current position, decisions, open threads
- A **session record** — what happened across sessions

Beyond those, what else needs its own dedicated file? (Schema draft? Decision log? Curriculum? Reading list?)

### Q11 — What is the state-persistence contract?

For each backbone file: is it overwritten, append-only, or hybrid? What gets written when? See `06-STATE-PERSISTENCE.md`.

### Q12 — What templates ship with the OV?

Templates scaffold the work. Every Prototype needs one. Every artifact-kind (session log, quiz, journal, draft) needs one.

### Q13 — What's the bootstrap-new-cartridge protocol?

This is the OV's analog to `BOOTSTRAP-NEW-OV.md`. It's the prompt the AI follows to open a new cartridge from a user request.

### Q14 — Audience register declaration

Who is the OV's intended reader / operator, and in what voice should the OV's prose and templates be written? This is distinct from CQ9 (which captured the AI ↔ operator communication preferences during the *design* conversation). Q14 captures the voice of the *shipped* OV's prose for *its* future operator.

Answer specifically — three slots:

- **Target reader** — concrete persona. Not "professionals" or "executives." Specific personas like: *"COO of a $20B+ market-cap public company aspiring to CEO within five years"*; *"Senior software engineer (10+ years) leading a small platform team"*; *"Self-directed adult learner working through a specialist subject without a teacher"*; *"Pre-med student preparing for residency interviews."*
- **Business / life context** — what context the reader is in when they consult the OV. *"In a business engagement with a senior client"*; *"alone late at night with a personal problem"*; *"in a coaching conversation with a peer"*; *"preparing materials for a board meeting."*
- **Prose register** — the voice the OV's prose should embody when read aloud. *"Senior Managing Partner at a global strategy consultancy speaking to a peer — direct, substantive, no flattery, no academic jargon at business dinners"*; *"Surgical attending teaching a senior resident — precise, time-conscious, anatomically specific"*; *"Veteran beat reporter explaining a story to a smart but non-expert friend — concrete, no inside-baseball without unpacking."*

**Why this matters.** Without an explicit audience-register declaration, OV prose drifts toward the AI's default register (academic, hedged, peer-coded). The drift is most visible at the artifact level — the worked-example coaching script that reads as a textbook chapter; the operator-guide section that uses jargon the target reader wouldn't tolerate. Documented historical recurrence: the v1.0 build of Political Landscape Cartography drafted a 4R coaching script with the phrase "dissertation-defined set" before the audience register was explicitly declared as "Senior Managing Partner voice; no academic terms at business dinners." The slip was caught only at REVIEW, after rework.

**Cascade.** Q14's answer cascades into every ARTIFACT-DRAFT session: prose voice, example selection, jargon tolerance, hedging level, the kinds of analogies that resonate vs land flat. SHIP-PREP Phase 3.9 (Vocabulary Audit, `07-SHIPPING-CHECKLIST.md`) cross-checks shippable prose against the declared register.

Log the answer as three manifest fields:

```yaml
ove_Audience_Target_Reader: "<concrete persona>"
ove_Audience_Business_Context: "<context of use>"
ove_Audience_Prose_Register: "<voice description>"
```

### Q15 — Domain stakes & moat commitments (Convention 10)

*Added v2.2.0.* Q15 is the formal version of the POSTURE-DECLARATION activity (see `03-DESIGN-PROTOCOL.md`). It captures the two load-bearing inputs Convention 10 requires for every OV: the domain-stakes flag (which determines whether the 8 TG conditional gates apply) and the moat commitments (which un-absorbable claim(s) the OV's schema will support).

The canonical 47-requirement list lives at `_design-engine/_meta/standalone-sufficiency/requirements.yaml`. The operator should have it open while answering Q15 — the question is "which of these requirements will this OV's schema make real?" not "do you think this is good?"

#### Q15a — Domain stakes

> *Is this OV operating in a regulated or high-stakes domain?*

A domain is **high-stakes** if any of the following are true. Mark `domain_stakes: high` in `_meta/posture.yaml` if so; the 8 TG conditional gates (REQ-I1 through REQ-I5 calibration/escalation/auditability; REQ-K1 through REQ-K3 data governance/compliance) then become mandatory.

- The OV outputs guidance the user may rely on for decisions with irreversible consequences (financial, medical, legal, safety, regulatory exposure).
- The OV touches data subject to compliance regimes (HIPAA, FERPA, financial-services rules, EU AI Act high-risk categories, attorney-client privilege).
- The OV's failure mode includes harm to third parties, not just inconvenience to the operator.
- The OV produces artifacts that may be presented as authoritative to regulators, boards, or auditors.

A domain is **low-stakes** when failure is bounded to the operator's own time/effort. Personal productivity OVs, methodology corpora for self-study, internal-team brainstorm aids, and similar are typically `low`. Mark `n-a` on each TG gate when domain is low; the OV does not need to (and arguably should not) carry the TG ceremony for stakes that don't justify it.

#### Q15b — Moat commitments

> *Which moat items (REQ-E4, REQ-M1, REQ-M2, REQ-M3, REQ-M4) will this OV's schema support? Pick ≥1, and for each, name the schema feature that will make it real.*

This is the most important question in Q15 because it pulls Convention 10 into the schema itself — the schema must support the moat commitments, or the commitments are wishes. The 5 moat items:

| REQ-ID | Title | What "supports this in the schema" usually looks like |
|---|---|---|
| **REQ-E4** | Scenario & Counterfactual Simulation | A Prototype or state structure that holds the user's actual data + a methodology field defining the simulation contract (inputs, outputs, methodology version). |
| **REQ-M1** | Data Flywheel | A schema field marking which artifacts contribute anonymized outcome data; a cartridge-level outcome-record format the engine can aggregate without breaking privacy. |
| **REQ-M2** | Legitimate Switching Cost | A cartridge backbone whose state files become the operator's system of record for the domain — substantive enough that leaving the OV means leaving real, accumulated value. |
| **REQ-M3** | Absorption Resistance | The schema's distinctive feature must rest on proprietary data, real integration, or accountability — NOT on promptable behavior. Name the feature that the platform cannot ship natively even if it wanted to. |
| **REQ-M4** | Cohort & Network Effects | A schema field or cartridge contract that enables privacy-preserving aggregation across operators (gated cohort benchmarks, peer-progress signals). Domain-gated — not appropriate for confidential or adversarial domains. |

Pick the moat items honestly. Single-moat commitment is acceptable. Committing to a moat the schema cannot actually support is worse than not committing — Convention 10's C14 validator will let it slip past today, but the operator will discover the gap when they try to make the claim externally.

#### Q15c — T0 hard gates flagged as design-challenging (optional)

> *Among the 5 T0 hard gates (REQ-A1, A2, A3, B1, H4), are any anticipated to be design-challenging for this OV?*

Optional but useful. Naming a T0 gate as "challenging" at Q15 time means SCHEMA-DESIGN's remaining questions will pay extra attention to it. Example: a low-budget personal OV may anticipate REQ-A1 (Capability Parity) as challenging because the operator can't afford to add per-domain RAG indexing; SCHEMA-DESIGN can then design Q1 (knowledge shape) to lean on the LLM's general knowledge rather than try to build a corpus the operator can't sustain.

#### How the answer flows into `_meta/posture.yaml`

Q15's answer seeds the OV's `_meta/posture.yaml` source-of-truth file:

```yaml
domain_stakes: low   # Q15a
moat_commitments:    # Q15b — at least one entry
  - req_id: REQ-M2
    schema_feature: "<concrete schema feature pointer>"
  # - req_id: REQ-E4
  #   schema_feature: "..."
```

The remaining per-requirement dispositions in `posture.yaml` get filled in during ARTIFACT-DRAFT and finalized at SHIP-PREP Phase 3.10 (Standalone Sufficiency readiness). Q15 commits to the posture's load-bearing frame; the dispositions follow.

> **Cross-references.** Convention 10 in `_design-engine/_meta/CONVENTIONS.md` defines the artifact cascade. The substrate's `requirements.yaml` is the canonical REQ-ID list. POSTURE-DECLARATION in `03-DESIGN-PROTOCOL.md` is the lighter pre-schema activity that seeds Q15. SHIP-PREP Phase 3.10 in `07-SHIPPING-CHECKLIST.md` is the gate that enforces the posture at ship time. Validator C14 checks the artifact at any time.

## Materializing the `_Prototypes/` folder

Once Q9 (cartridge analog) and Q12 (Prototype list) are answered, the Prototypes are *named*. Convention 6 (see `_meta/CONVENTIONS.md`) requires that they are also *defined* — one canonical `_Prototypes/<NAMESPACE>_<TypeName>.md` file per Prototype, structured per `_templates/TEMPLATE-Prototype.md`.

This is a hard step, not optional. An OV that ships without `_Prototypes/` populated is one where every cartridge reference (`Item_Prototype: <NAMESPACE>_<TypeName>`) is a name pointer with no definition behind it — fine for the operator with a central vault-wide registry, broken for everyone else.

**During ARTIFACT-DRAFT**, walk one Prototype at a time:

1. Open `_templates/TEMPLATE-Prototype.md` (or copy it into `_Prototypes/<NAMESPACE>_<TypeName>.md` and edit).
2. Fill in:
   - Purpose (what this Prototype models in the domain)
   - Required frontmatter (Universal Core + Prototype-specific fields from Q12)
   - Body structure (the required sections an Item must contain)
   - Naming pattern + cartridge folder location
   - A concrete example Item
   - Relationships (which other Prototypes this one links to, per Q4)
3. Cross-check against `_meta/SCHEMA-OF-SCHEMAS.md` — every property declared there should appear in at least one Prototype's required-frontmatter block, and every Prototype declared in `_meta/SCHEMA-OF-SCHEMAS.md` must have a corresponding `_Prototypes/<NAMESPACE>_<TypeName>.md`.
4. Repeat until every Prototype in the OV's namespace has a definition file.

The shipping checklist verifies this at Phase 3.5 (see `07-SHIPPING-CHECKLIST.md`); the optional validator's C7 check enforces it programmatically.

## Required sections of the new OV's `_schema.md`

The new OV's schema document must contain:

1. **Domain identity** — name, shape (Q1 categories), summary
2. **Answers to Q1–Q13** — the analytical answers that justify the design
3. **Prototype definitions** — frontmatter, required body sections, naming, location
4. **Relationship vocabulary** — the named relations
5. **Mastery / progress scale** — default or custom
6. **Custom session activities** — with trigger conditions
7. **Cartridge backbone** — files, content contracts
8. **State-persistence contract** — per file
9. **Templates list** — what ships in `_templates/`
10. **Folder structure** — how cartridges are organized

## How to know the schema is good

Run these checks before locking the schema:

- [ ] Could you describe an example Item in this domain that fits naturally? (If not, the Prototypes are off.)
- [ ] Are the relationships sufficient to express how Items actually link in your head?
- [ ] Does the cartridge analog match how the user *thinks* about the work, not just how it's structured on disk?
- [ ] Would a user-domain-expert recognize this schema as "yes, that's how this domain works"?
- [ ] Does it pass the **self-similarity test**? Could OVE itself be designed using this schema? (For OVE: trivially yes. For other OVs: not always relevant, but a useful sanity check.)

If any check fails, iterate. Schema design is the most important creative work in OV design — taking an extra session here pays back across the OV's entire lifetime.
