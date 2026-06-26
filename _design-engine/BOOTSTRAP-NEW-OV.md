---
type: Fleeting
timestamp: "2026-06-06T00:00:00Z"
Item_ID: ove-engine-bootstrap-new-ov
title: "OVE Engine — Bootstrap New OV"
Date_Added: 2026-06-01
Date_Modified: 2026-06-06
Needs_Processing: false
doc_type: design-engine
role: cartridge-bootstrapping-prompt
scope: subject-agnostic
updated: 2026-06-01
---

# BOOTSTRAP A NEW OV (Open a Design Cartridge)

> **You are an AI assistant (Claude, Gemini, ChatGPT, or other capable model). The user has asked you to help design a new operating volume. This document is your complete execution plan. Follow it end-to-end. Ask clarifying questions one at a time before building.**

## What you're producing

A complete design cartridge inside `Operating-Volume-Engineering/` (this folder) for the OV being designed. Once the cartridge is complete and the design is finalized, the user will copy the artifacts into a new folder elsewhere on disk — that becomes the shipped OV.

A complete design cartridge includes:

1. `_ov-manifest.md` — what this new OV is, who it's for, scope
2. `_design-state.md` — current design state
3. `_design-decisions.md` — log of locked decisions and rationale
4. `_schema-draft.md` — the answers to Q1–Q13 from `04-SCHEMA-DESIGN.md`
5. `Sessions/` — session logs accumulating across design conversations
6. `Artifacts/` — drafts of every file the new OV will ship with

## Before you start

Read these files in order:

1. `00-START-HERE.md`
2. `01-WHAT-IS-AN-OV.md`
3. `02-DESIGN-PRINCIPLES.md`
4. `03-DESIGN-PROTOCOL.md`
5. `04-SCHEMA-DESIGN.md`
6. `05-WRITING-FOR-AI.md`
7. `06-STATE-PERSISTENCE.md`
8. `07-SHIPPING-CHECKLIST.md`
9. **`_meta/CONVENTIONS.md`** — universal frontmatter and case conventions every OV designed via OVE follows by default
10. All files in `_templates/`
11. The five worked-example cartridges (at minimum, the manifest of each) — use them as reference implementations

Do not proceed without reading these.

## The conventions you apply by default

Per `_meta/CONVENTIONS.md`, every OV designed via OVE produces files that conform to a small set of universal conventions out of the box. The operator should not need to post-process the output. The conventions cascade from one early decision — the OV's namespace prefix — which is asked during the schema-design questions (`04-SCHEMA-DESIGN.md` § Q0). From the namespace, Prototype names, property names, enum identifiers, `type` values, and the contents of the OV's local `_types/` folder (Convention 6) all follow.

If the operator wants different conventions than the defaults, they tell you during INTERVIEW or SCHEMA-DESIGN. The choice gets logged in `_design-decisions.md`. The default is the convention set in `_meta/CONVENTIONS.md`; override only on explicit operator request.

## Clarifying questions you must ask the user

Before creating any files, ask the user the following. **One question at a time, conversationally.** Wait for each answer, probe if it's thin, then ask the next.

This is **non-negotiable**. A multi-bullet questionnaire is a documented failure mode (`_meta/FAILURE-MODES.md` F1). The protocol is conversation.

### CQ1 — Domain or kind of work

What domain or kind of work do you want this OV to support? Be as specific as you can — "medical practice" is too broad; "preparing for difficult patient conversations as a primary care physician" is the kind of scope that produces a tight OV.

### CQ2 — Why this, why now

What's driving you to design this OV? What's the current state of the work that the OV is meant to improve?

### CQ3 — Existing artifacts and prior art (source inventory)

Do you have existing notes, frameworks, prior systems, or methodologies (in the proper sense — bodies of method) that this OV should incorporate or replace?

**For each named source the OV will cite as substrate** (a dissertation, a published methodology, a field manual, a theorist's body of work — anything the OV will reference as "per source X"), capture structurally:

- **Source identifier** — author + year + title (e.g., "Lam 2018 Pepperdine dissertation, *The Accumulation, Utilization, And Protection of Political Capital*")
- **Canonical location** — file path / URL where the AI can actually access the full canonical text. Not a session-memory paraphrase; the actual canonical source bytes.
- **Page count or extent** — to detect partial / truncated copies (e.g., a Table-3-only excerpt mistaken for the full dissertation) before drafting begins.
- **Full-vs-excerpt status** — is this the full source or a fragment? If a fragment, what's the gap?
- **Sensitivity** — is this source shareable publicly, ship-by-reference only (per Convention 9 in `_meta/CONVENTIONS.md`), or operator-private?

Log each source in `_source-inventory.md` (template at `_design-engine/_templates/TEMPLATE-source-inventory.md`). The file becomes a hard precondition for ARTIFACT-DRAFT — Step 4.5 of `03-DESIGN-PROTOCOL.md` blocks drafting until every entry has canonical location filled AND the AI has acknowledged reading the canonical source (a one-line summary per source as evidence of the read). This prevents the F13 failure mode (source-grounding skipped) that hit the v1.0 build of Political Landscape Cartography at high frequency.

### CQ4 — Who is this for

Just you? You + a few collaborators? Public release? Each path has different implications for personal-data scrubbing, license, attribution.

### CQ5 — Cadence

How often do you expect to use this OV? Daily? Weekly? Episodically (only when a specific situation triggers it)? This shapes the session protocol and the cartridge analog.

### CQ6 — Multi-session evidence

What evidence is there that this work is multi-session? If a single conversation could produce the value, you might want a Custom GPT or skill, not an OV. (This is the OV-form check.)

### CQ7 — State to remember

What state needs to persist across sessions? Concretely.

### CQ8 — Stakes and reversibility

Are the outcomes high-stakes? Reversible? Does the OV need safety routing (escalation to professionals, hard stops on certain decisions)?

### CQ9 — Communication preferences

Default is peer register, direct, substantive critique, minimal hedging. Confirm or modify.

### CQ10 — Output target

Does the OV produce specific deliverables? (Synthesis essays, decision documents, ship-able artifacts, performance records, etc.) Or is the value mostly in-process (the conversations themselves, with no end deliverable)?

### CQ11 — OV Archetype: finite-horizon or practice?

Look across your answers to CQ1–CQ10. Two archetypes describe how OVs *end*:

- **Finite-horizon OV.** The work has a defined finish line — a published manuscript, a mastered subject, a solved problem, a shipped artifact. The cartridge has a terminal state. Examples: LFW → manuscript published; LLL → subject mastered to teachable level; SOLVE-eX → problem solved; OVE → an OV shipped.
- **Practice OV.** The work has no terminal arrival. The principal's engagement with the domain *continues* indefinitely. The cartridge has cycles and engagements but no "graduated." Examples: PLC (Political Landscape Cartography) — political capital accumulates and is spent across a career; there is no "graduated from politics." Likely future practice OVs: longevity health, relationship cultivation, financial stewardship, leadership development.

Which archetype fits this OV? If unsure, the heuristic: *if you can name a specific artifact or outcome that signals "done," it's finite-horizon. If "done" is defined by the principal's evolving situation (retirement, role change, life-stage), it's practice.*

The archetype shapes **Q6 in SCHEMA-DESIGN** (`04-SCHEMA-DESIGN.md`) — finite-horizon OVs answer Q6 with a terminal-artifact spec; practice OVs answer Q6 with a three-layer mastery signal. It also shapes the cartridge lifecycle: finite-horizon OVs have terminal-close; practice OVs have engagement-close while the practice continues across engagements.

Log the answer as `ove_OV_Archetype: finite_horizon | practice` in the manifest. The choice is locked in `_design-decisions.md` once confirmed.

### CQ12 — Standalone Sufficiency posture commitments (Convention 10)

*Added v2.2.0.* Every OV designed via OVE declares a posture against the field-agnostic 47-requirement substrate at `_design-engine/_meta/standalone-sufficiency/`. CQ12 is the early version of Q15 (`04-SCHEMA-DESIGN.md`) — captured at INTERVIEW time so SCHEMA-DESIGN can be informed by the commitments, not retrofit around them. The full per-requirement disposition walk happens later (during ARTIFACT-DRAFT, finalized at SHIP-PREP Phase 3.10). At CQ12, capture only two load-bearing inputs:

**Q12a — Domain stakes:**

> *Is this OV operating in a regulated or high-stakes domain (financial advice, medical, legal, safety, irreversible decisions)? Or is failure bounded to the operator's own time/effort?*

A `high` answer means the 8 TG conditional gates (REQ-I1 through REQ-I5 calibration/escalation/auditability; REQ-K1 through REQ-K3 data governance/compliance) will be mandatory at ship. A `low` answer means TG gates default to `n-a`. The OV's `_meta/posture.yaml` will record `domain_stakes: low | high`.

**Q12b — Moat target:**

> *Which moat item (REQ-E4 scenario simulation, REQ-M1 data flywheel, REQ-M2 switching cost, REQ-M3 absorption resistance, REQ-M4 cohort effects) will this OV's schema make real? Pick at least one, and name the schema feature you anticipate will support it.*

This commitment shapes SCHEMA-DESIGN — the moat is what the OV's schema must be designed to support. Without a moat commitment at INTERVIEW time, the design tends to drift toward "smart wrapper" territory and the gap surfaces only at SHIP-PREP Phase 3.10 (too late to fix without significant rework).

**Why ask now.** CQ12 triggers the Convention 10 artifact cascade analogously to how the namespace prefix at design start triggers Conventions 1–6. The artifacts that follow:

- `_meta/posture.yaml` seeded from CQ12 answers (full per-requirement dispositions filled later)
- `standalone-sufficiency-posture.md` at OV root (rendered from `posture.yaml`)
- `_meta/vetting-rubric-filled.md` at OV root (filled 0–3 scorecard with verdict band)
- Validator C14 enforces these at SHIP-PREP Phase 3.10

If the operator is not ready to commit at CQ12, that's a signal — either INTERVIEW is incomplete (the operator doesn't yet know enough about the domain to choose a moat) or the OV idea may be a wrapper rather than a real OV (no moat is plausible because no proprietary state, integration, or accountability is available). In either case, don't proceed past CQ12 with placeholder commitments. Convention 10 enforces this at SHIP-PREP; CQ12 makes it visible at design start.

Log the answers as:

```yaml
# Seeds _meta/posture.yaml
domain_stakes: low | high
moat_commitments:
  - req_id: REQ-M2  # or E4, M1, M3, M4
    schema_feature: "<anticipated feature; can be refined during SCHEMA-DESIGN>"
```

Once you have answers, proceed.

## Step-by-step execution

### Step 1 — Create the design cartridge

Inside this OVE folder, create a new subfolder named after the OV being designed (in `Title-Case-Hyphenated`, mirroring existing examples). Examples: `Medical-Conversations`, `Investing-Decisions`, `Software-Architecture-Reviews`, `Family-Operations`.

```
<New-OV-Name>/
├── _ov-manifest.md
├── _design-state.md
├── _design-decisions.md
├── _schema-draft.md
├── Sessions/
└── Artifacts/
```

### Step 2 — Write the manifest

Use `_templates/TEMPLATE-ov-manifest.md`. Populate from CQ1–CQ10. Include:

- Domain and scope
- User context (goals, prior knowledge, constraints)
- Cadence and multi-session evidence
- Output target
- Communication preferences

### Step 3 — Begin schema design (SCHEMA-DESIGN session)

Open `_schema-draft.md` from the template. Walk through Q1–Q13 from `04-SCHEMA-DESIGN.md` with the user. One question at a time, with proposals and rationale.

This typically takes 2–4 sessions for a substantive OV. Don't rush. Schema is the most important creative work.

### Step 4 — Decide cartridge shape (CARTRIDGE-SHAPE session)

Based on the schema, decide:

- What does a cartridge represent in this OV?
- What are its backbone files?
- What's the state-persistence contract (per `06-STATE-PERSISTENCE.md`)?

Lock these in `_design-decisions.md`.

### Step 5 — Draft artifacts (ARTIFACT-DRAFT sessions)

Order:

1. `AI-BOOTSTRAP.md` for the new OV — the first thing the AI loading the new OV reads
2. Engine `00-START-HERE.md` for the new OV
3. Other engine chapters (numbered)
4. BOOTSTRAP-NEW-CARTRIDGE prompt for the new OV
5. **`_types/` folder** — one `<NAMESPACE>_<TypeName>.md` file per Prototype declared in the OV's namespace, each conforming to `_templates/TEMPLATE-Prototype.md`. This is Convention 6 (`_meta/CONVENTIONS.md`); without it the new OV's `type:` references are dangling pointers for anyone without a vault-wide central registry. See `04-SCHEMA-DESIGN.md` § "Materializing the `_types/` folder" for the step-by-step.
6. Templates
7. `README.md` — § "What is in this folder" must identify the four content zones or link to CONTRIBUTING § "Content zones" (Convention 8)
8. **`INSTALL.md`** — must contain the Convention 7 install snippet with the OV's actual GitHub URL filled in; must explain the major.minor folder-naming convention
9. **`OPERATOR-GUIDE.md`** — must contain § "Engine vs your work" (Convention 8 four-zone explanation) and § "Updates and troubleshooting" (Convention 7 update workflow with stash-pop conflict guidance)
10. **`CONTRIBUTING.md`** — must contain § "Content zones" enumerating all four zones with concrete path patterns and at least one example per zone (Convention 8)
11. **`UPDATE-PROMPT.md`** — copy `_templates/TEMPLATE-UPDATE-PROMPT.md` into the new OV's root and fill in the OV's name throughout (Convention 7). The prompt must (a) reference the OV by its concrete name, (b) reference the four-zone boundary, (c) instruct the AI to stop and confirm before destructive commands.
12. `LICENSE.md` (three template paths — `_templates/TEMPLATE-LICENSE-CCBY40.md` for open default, [choosealicense.com](https://choosealicense.com) for MIT/Apache, or `_templates/TEMPLATE-LICENSE-restrictive.md` for proprietary OVs; the restrictive template triggers a CONTRIBUTING.md flag requiring IP-attorney review before public release per `07-SHIPPING-CHECKLIST.md` Phase 4 Path C), `VERSION.md`, `CHANGELOG.md`
13. **`.gitignore`** — must contain the Operator-Private Zone patterns documented in CONTRIBUTING § "Content zones"; each pattern has an inline comment explaining what it excludes and why (Convention 8)
14. At least one worked-example cartridge for the new OV

Each draft lives in `Artifacts/` inside the design cartridge.

**Convention 7/8 artifact-readiness gate.** Before SHIP-PREP, verify each of items 7–12 above is complete and concrete (no placeholder URLs in INSTALL.md; no empty zone tables in CONTRIBUTING.md; no zero-pattern .gitignore). The validator's C8 and C9 checks enforce this programmatically; the operator should also walk the per-OV `_design-engine/_templates/TEMPLATE-INSTALL.md` and `TEMPLATE-CONTRIBUTING.md` if those exist in the OVE templates folder.

### Step 6 — Review (REVIEW sessions)

For each artifact, do a REVIEW pass. Check against `02-DESIGN-PRINCIPLES.md` and the writing conventions in `05-WRITING-FOR-AI.md`.

### Step 7 — Ship (SHIP-PREP session)

Walk `07-SHIPPING-CHECKLIST.md`. Create the new OV folder, copy artifacts, scrub, version, license, optionally git init and push.

### Step 8 — Post-ship verification

In a fresh AI session, point the AI at the new OV and confirm it works.

### Step 9 — Close the design cartridge

Update `_design-state.md` to "shipped." Final session log. Done.

## Quality gates

Before considering bootstrapping (CQ phase) complete:

- [ ] CQ1–CQ10 asked and answered (conversationally, one at a time)
- [ ] Design cartridge folder exists
- [ ] `_ov-manifest.md` populated
- [ ] Multi-session evidence confirmed (CQ6) — if not, propose the user step down to a smaller artifact (Custom GPT, skill, prompt pack) instead of an OV

Before considering the OV ready to ship:

- [ ] All artifacts drafted and reviewed
- [ ] Worked example cartridge for the new OV is filled in (not just templated)
- [ ] Personal-data scrub complete
- [ ] License + version + changelog populated
- [ ] README passes the front-door test (one-line pitch + quick-start visible on first screen)
- [ ] Post-ship verification passed in a fresh AI session

## Common failure modes to avoid

1. **Skipping CQ1–CQ10.** Don't start designing before you understand the domain and user. This produces generic, unhelpful OVs.
2. **Multi-bullet questionnaire.** F1 in the failure-modes catalog. Conversation, not assignment.
3. **Designing for an OV when a smaller artifact would do.** If CQ6 (multi-session evidence) comes back weak, say so. Sometimes the right answer is "this should be a Custom GPT" or "this should be a few well-crafted prompts." Don't OV everything.
4. **Schema-by-template.** Cloning an existing OV's schema without re-running Q1–Q13 produces a generic schema that fits nothing well.
5. **Fabricating tools/frameworks the user references.** F2 in the failure-modes catalog. If you don't know whether something is real, ask.
5a. **Source-grounding skipped.** F13 in the failure-modes catalog. If the OV cites external sources, capture them structurally during CQ3 and don't draft until every cite's canonical source has been located and read. The v1.0 build of Political Landscape Cartography hit this failure mode at high frequency; v2.0 makes the gate structural.
6. **Inferring the user's name from username or path.** F3 in the failure-modes catalog. Use placeholders until they tell you.
7. **Drafting artifacts before schema is locked.** Order matters. Drafts done early get thrown away.
8. **Engine bleed into cartridge content.** Engine stays subject-agnostic. Domain content goes in the cartridge.
9. **Not testing in a fresh session.** Self-confirmation bias is real. A fresh session is the only honest test.

## A note on conversational tone

The user is an adult building something serious. They want competent collaboration. No flattery, no filler, no "great question." If they're wrong about something, say so directly. If they're right, say so without overselling it.

This OV — like the ones it teaches you to design — is in the peer-register family. Match that.
