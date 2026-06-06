---
Item_Prototype: Fleeting
Item_ID: ove-engine-03-design-protocol
Title: "OVE Engine — 03 Design Protocol"
Date_Added: 2026-06-01
Date_Modified: 2026-06-06
Needs_Processing: false
type: design-engine
role: session-protocol
scope: subject-agnostic
updated: 2026-06-01
---

# 03 — DESIGN PROTOCOL

> **How a design engagement actually unfolds across sessions. Activities, decision algorithm, audit-mode protocol, and quality gates.**

## Session lifecycle

```
1. READ design engine + cartridge state (per 00-START-HERE.md)
2. DIAGNOSE current design state
3. PROPOSE a session activity with rationale
4. WAIT for user confirmation or override
5. EXECUTE the activity
6. CAPTURE decisions, schema updates, artifact drafts
7. WRITE the session log
8. UPDATE _design-state.md and _design-decisions.md
9. END with one explicit Open Thread for next session
```

Steps 1, 6, 7, 8, 9 are non-negotiable. Step 5 varies by activity.

## The six universal session activities

| Code | Activity | Right default when |
|------|----------|---------------------|
| **INTERVIEW** | Socratic clarifying questions about the domain, the user, the intended use | Cartridge is new OR interview is documented as unfinished |
| **SCHEMA-DESIGN** | Walk through Q1–Q8 from `04-SCHEMA-DESIGN.md` to design the new OV's schema | Domain is clear; schema is not yet locked |
| **CARTRIDGE-SHAPE** | Decide what a cartridge represents in the new OV, what its backbone files are, what its state-persistence model is | Schema is locked; cartridge analog undecided |
| **ARTIFACT-DRAFT** | Draft a specific shipping file (`AI-BOOTSTRAP`, `README`, an engine file, a template) inside `Artifacts/` | Schema + cartridge shape locked; missing artifacts |
| **REVIEW** | Critique an existing draft against the design principles in `02-DESIGN-PRINCIPLES.md` | An artifact has a draft but no review pass |
| **SHIP-PREP** | Walk the checklist in `07-SHIPPING-CHECKLIST.md` (scrubbing, license, README, GitHub) | All artifacts drafted |

## Decision algorithm

Evaluate in order. First condition that fires determines the default proposal.

### Step 1 — Hard overrides

- **If** `_design-state.md` is missing or contradictory → stop and tell the user
- **If** the user has explicitly named the activity for this session → execute that

### Step 2 — Interview not complete

- **If** `_ov-manifest.md` is missing required sections (domain, user goals, intended use, prior-art references) → propose **INTERVIEW**

### Step 3 — Schema not locked

- **If** `_schema-draft.md` doesn't yet answer Q1–Q8 from `04-SCHEMA-DESIGN.md` → propose **SCHEMA-DESIGN**

### Step 4 — Cartridge shape undecided

- **If** `_design-decisions.md` doesn't yet record "Cartridge represents: ___" → propose **CARTRIDGE-SHAPE**

### Step 5 — Artifacts incomplete

- **If** any of the standard artifacts (`AI-BOOTSTRAP`, `README`, the engine files, the templates) is missing from `Artifacts/` → propose **ARTIFACT-DRAFT** for the highest-priority missing one
  - Priority order: `AI-BOOTSTRAP` → engine files (00, then 01) → BOOTSTRAP cartridging prompt → templates → `README`/`INSTALL`/other root docs

### Step 6 — Artifacts unreviewed

- **If** all artifacts exist but ≥ 1 has no `## Reviewed` marker → propose **REVIEW**

### Step 7 — Ready to ship

- **If** all artifacts exist and all are reviewed → propose **SHIP-PREP**

### Step 8 — Post-proposal

Present the proposal:

```
Proposed activity: <CODE> — <plain-English description>
Rationale: <which conditions fired>
Alternative: <next-priority activity>
Your call.
```

Wait. Do not begin until confirmation or override.

## §4 Audit Mode

When a user asks you to audit an existing OV (not design a new one):

1. **Ask for the path.** Where on disk is the OV? If it's accessible to you, proceed. If not, ask for relevant files to be pasted.

2. **Read the OV in order:**
   - Its `AI-BOOTSTRAP.md`
   - Its `README.md`
   - Its engine folder (all files)
   - Its `_meta/` or schema-of-schemas equivalent
   - One representative cartridge in full
   - Skim its other cartridges

3. **Audit against the design principles** in `02-DESIGN-PRINCIPLES.md`. Specifically check:
   - [ ] **P1 Substrate-agnostic.** Does it lock to a platform?
   - [ ] **P2 Statefulness through files.** Is state on disk? Is the source-of-truth clear?
   - [ ] **P3 Self-describing.** Does the folder bootstrap the AI without external setup?
   - [ ] **P4 Cartridge specialization.** Is domain content properly cartridge-scoped?
   - [ ] **P5 Conversational interface.** Does it require special syntax?
   - [ ] **P6 Multi-session.** Does the bootstrap work on session N?
   - [ ] **P7 Identity rule.** Are real names handled properly?
   - [ ] **P8 Fabrication discipline.** Any suspect references?
   - [ ] **P9 Self-similarity.** Could OVE re-design this OV cleanly?
   - [ ] **P10 One-question protocol.** Does the bootstrap allow for it?
   - [ ] **P11 Propose-don't-decide.** Does the engine respect user agency?
   - [ ] **P12 Write before end.** Are state-persistence contracts explicit?
   - [ ] **P13 Schema-freeze.** Is the version/schema policy explicit?

4. **Surface findings** in three buckets:
   - **Critical:** violations that break the OV's substrate-agnostic / stateful / shippable nature
   - **Significant:** weaknesses that will produce drift or user frustration over time
   - **Cosmetic:** small improvements

5. **Propose fixes** in priority order. Do NOT silently modify the OV — propose and wait for the user's call.

## Writing the session log

At the end of every session, create a new file in `<Cartridge>/Sessions/` named:

```
YYYY-MM-DD_NNN_<activity-code>.md
```

`NNN` is zero-padded sequential. Use `_design-engine/_templates/TEMPLATE-Session.md`.

## Updating `_design-state.md` and `_design-decisions.md`

After every session:

**`_design-state.md`** (overwritten):
- Update `Design phase` if it advanced
- Update `Decided` list with any new locked choices
- Update `Open` list with any new open questions
- Update `Artifact status` table
- Update `Recent Sessions` (prepend new session)
- Update `Open Threads` (close any addressed, add new ones)

**`_design-decisions.md`** (append-only):
- Append a dated entry for each significant decision: what was decided, why, what alternative was rejected and why

## Quality gates

Before ending any session, confirm:

- [ ] At least one concrete design step taken
- [ ] Session log written
- [ ] `_design-state.md` updated
- [ ] `_design-decisions.md` updated (if a decision was made)
- [ ] Explicit Open Thread for next session
- [ ] Any new artifact drafts saved in `Artifacts/`

If any is no, the session is not complete.
