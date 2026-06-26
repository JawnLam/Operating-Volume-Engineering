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

## The session activities

Seven universal activities, plus **KNOWLEDGE-MOUNT** which fires only for knowledge-augmented OVs (Convention 11).

| Code | Activity | Right default when |
|------|----------|---------------------|
| **INTERVIEW** | Socratic clarifying questions about the domain, the user, the intended use | Cartridge is new OR interview is documented as unfinished |
| **POSTURE-DECLARATION** | Operator commits to Convention 10's three load-bearing posture inputs: (a) `domain_stakes: low \| high` flag in `_meta/posture.yaml`, (b) at least one moat-item target (REQ-E4, M1, M2, M3, or M4) with the schema feature that will make it real, (c) any T0 hard-gates flagged as design-challenging early so SCHEMA-DESIGN accounts for them | INTERVIEW complete; SCHEMA-DESIGN not yet started; `_meta/posture.yaml` does not exist or has placeholder values |
| **SCHEMA-DESIGN** | Walk through Q1–Q15 from `04-SCHEMA-DESIGN.md` to design the new OV's schema (Q15 is the formal version of POSTURE-DECLARATION's commitments) | Domain is clear; posture declared; schema is not yet locked |
| **CARTRIDGE-SHAPE** | Decide what a cartridge represents in the new OV, what its backbone files are, what its state-persistence model is | Schema is locked; cartridge analog undecided |
| **KNOWLEDGE-MOUNT** *(KAOV only)* | Vendor and verify the OV's OKF data-plane bundle(s) per Convention 11 / `08-KNOWLEDGE-RETRIEVAL.md`: copy each bundle under `_knowledge/`, confirm OKF conformance, and record `okf_version` + `pin` in `Knowledge_Mounts` | `ove_Knowledge_Source: knowledge_augmented` AND ≥1 declared mount is unresolved, non-conformant, or unpinned |
| **ARTIFACT-DRAFT** | Draft a specific shipping file (`AI-BOOTSTRAP`, `README`, an engine file, a template) inside `Artifacts/` | Schema + cartridge shape locked; missing artifacts |
| **REVIEW** | Critique an existing draft against the design principles in `02-DESIGN-PRINCIPLES.md` | An artifact has a draft but no review pass |
| **SHIP-PREP** | Walk the checklist in `07-SHIPPING-CHECKLIST.md` (scrubbing, license, README, GitHub, Phase 3.10 Standalone Sufficiency readiness) | All artifacts drafted |

> **KNOWLEDGE-MOUNT is new in v2.3.0** and fires only when the manifest declares `ove_Knowledge_Source: knowledge_augmented`. It gates ARTIFACT-DRAFT the way Step 4.5 (source inventory) does: a KAOV cannot draft artifacts that cite the data plane until the data plane is vendored, OKF-conformant, and pinned. Self-contained OVs (the default) never see this activity. See Convention 11 in `_design-engine/_meta/CONVENTIONS.md`.

> **POSTURE-DECLARATION is new in v2.2.0.** It separates the posture-commitment step (operator commits to stakes + moat target + schema-challenging T0 flags) from SCHEMA-DESIGN's full Q1–Q15 walk. The commitments seed `_meta/posture.yaml` before schema design proceeds, so the schema work can be informed by which moat item the OV is committing to and which T0 gates need design attention. Without this separation, posture work tends to be retrofitted at SHIP-PREP — too late to shape the schema. See Convention 10 in `_design-engine/_meta/CONVENTIONS.md`.

## Decision algorithm

Evaluate in order. First condition that fires determines the default proposal.

### Step 1 — Hard overrides

- **If** `_design-state.md` is missing or contradictory → stop and tell the user
- **If** the user has explicitly named the activity for this session → execute that

### Step 2 — Interview not complete

- **If** `_ov-manifest.md` is missing required sections (domain, user goals, intended use, prior-art references, **OV archetype** per CQ11) → propose **INTERVIEW**
- **If** `ove_OV_Archetype` is empty in the manifest → INTERVIEW is incomplete (CQ11 unanswered); proposed activity remains **INTERVIEW** until archetype is declared. The archetype gates Q6 in SCHEMA-DESIGN; SCHEMA-DESIGN cannot proceed past Q5 without it.

### Step 2.5 — Posture not declared (Convention 10)

- **If** `_meta/posture.yaml` does not exist OR exists but `domain_stakes` is unset (or placeholder), `moat_commitments` is empty, and Convention 10 has not been formally walked → propose **POSTURE-DECLARATION**.
- POSTURE-DECLARATION must complete (a seeded `_meta/posture.yaml` with declared `domain_stakes` + ≥1 `moat_commitments` entry) before SCHEMA-DESIGN proceeds. Q15 in `04-SCHEMA-DESIGN.md` is the formal version of the same commitments; the activity exists separately because the commitments are load-bearing for Q1–Q8 schema choices (the moat target shapes the schema; the domain-stakes flag shapes which TG gates the schema must support).

### Step 3 — Schema not locked

- **If** `_schema-draft.md` doesn't yet answer Q1–Q15 from `04-SCHEMA-DESIGN.md` → propose **SCHEMA-DESIGN**

### Step 4 — Cartridge shape undecided

- **If** `_design-decisions.md` doesn't yet record "Cartridge represents: ___" → propose **CARTRIDGE-SHAPE**

### Step 4.5 — Source inventory not read-acknowledged

- **If** `_source-inventory.md` exists and any source is missing `Canonical location` OR is missing `AI-read acknowledgment` → propose **INTERVIEW** (return to CQ3 source-capture to fill the gaps). ARTIFACT-DRAFT is locked until every cited source has been located, the canonical-source-extent has been verified (not a Table-3-only excerpt; not a wrong-year edition), and the AI has read the canonical source.
- **If** `_source-inventory.md` doesn't exist but CQ3 surfaced cited sources → return to **INTERVIEW** (CQ3 was incomplete).
- **If** CQ3 surfaced no cited sources → skip this step.

This step exists to prevent F13 (source-grounding skipped) — see `_meta/FAILURE-MODES.md`.

### Step 4.6 — Knowledge mounts unresolved (Convention 11, KAOV only)

- **If** `ove_Knowledge_Source: knowledge_augmented` AND any `Knowledge_Mounts` entry is unresolved (no vendored bundle under `_knowledge/`), non-conformant (fails OKF v0.1 §9), or unpinned (missing `okf_version` / `pin`) → propose **KNOWLEDGE-MOUNT**. ARTIFACT-DRAFT is locked until every declared mount is vendored, OKF-conformant, and pinned.
- **At every session boot for a KAOV**, run the Rule 4 re-verification from `08-KNOWLEDGE-RETRIEVAL.md`: diff each depended-on concept's `timestamp` (and the bundle's git SHA / `okf_version`) against the recorded `pin`; surface drift to the operator and re-confirm affected claims before reuse. This prevents F14 (stale/format-drift mount).
- **If** `ove_Knowledge_Source: self_contained` (the default) → skip this step.

This step exists to prevent F14 (stale or non-conformant data plane) — see `_meta/FAILURE-MODES.md`.

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
