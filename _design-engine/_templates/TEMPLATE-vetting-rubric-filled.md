---
Item_Prototype: Fleeting
Item_ID: <ov-slug>-vetting-rubric-filled
Title: "<OV Name> — Vetting Rubric (filled, Convention 10)"
Date_Added: YYYY-MM-DD
Date_Modified: YYYY-MM-DD
Needs_Processing: false
type: ov-posture
role: vetting-rubric-filled
scope: ov-specific
ove_OV_Name: "<OV Name>"
ove_OV_Slug: "<ov-slug>"
ove_Domain_Stakes: "<low | high>"
ove_Convention_10_Revision: "1.2"
updated: YYYY-MM-DD
---

# <OV Name> — Vetting Rubric (filled)

> **Generated from `_meta/posture.yaml` against the substrate's structure at `_design-engine/_meta/standalone-sufficiency/vetting-rubric.md`. Score each requirement 0–3; the weighted roll-up yields a verdict.**

## Scoring scale

- **0** — Absent — no evidence the requirement is met.
- **1** — Partial — gestured at, but weak or inconsistent.
- **2** — Adequate — present and reliable.
- **3** — Strong — a clear, differentiating implementation.

## Gating rule (veto)

Any **hard gate (T0)** — or any **applicable conditional gate (TG)** — scoring below **2** caps the verdict at *At risk*, regardless of the weighted total. You cannot score your way past a broken floor.

## A. Foundational Parity & Scope Integrity

| ID | Requirement | Tier | Gate | Moat | Weight | Score | Weighted |
|---|---|---|---|---|---|---|---|
| REQ-A1 | Capability Parity | T0 | 🔒 hard | — | 5 | <0–3> | <w*s> |
| REQ-A2 | Graceful Scope Boundaries | T0 | 🔒 hard | — | 5 | <0–3> | <w*s> |
| REQ-A3 | No Artificial Lobotomy | T0 | 🔒 hard | — | 5 | <0–3> | <w*s> |

## B. Memory & Statefulness

| ID | Requirement | Tier | Gate | Moat | Weight | Score | Weighted |
|---|---|---|---|---|---|---|---|
| REQ-B1 | Persistent User Model | T0 | 🔒 hard | — | 5 | <0–3> | <w*s> |
| REQ-B2 | Longitudinal Continuity | T2 | — | — | 4 | <0–3> | <w*s> |
| REQ-B3 | Compounding Context Value | T2 | — | — | 4 | <0–3> | <w*s> |

## C. Workflow Orchestration & Guided Process

| ID | Requirement | Tier | Gate | Moat | Weight | Score | Weighted |
|---|---|---|---|---|---|---|---|
| REQ-C1 | Expert Interactive Intake | T1 | — | — | 3 | <0–3> | <w*s> |
| REQ-C2 | Multi-Step Task Chaining | T1 | — | — | 3 | <0–3> | <w*s> |
| REQ-C3 | Process State & Resumability | T1 | — | — | 3 | <0–3> | <w*s> |
| REQ-C4 | Opinionated Default Path | T1 | — | — | 3 | <0–3> | <w*s> |

## D. Proprietary Knowledge & Grounding

| ID | Requirement | Tier | Gate | Moat | Weight | Score | Weighted |
|---|---|---|---|---|---|---|---|
| REQ-D1 | Curated Authoritative Corpus (RAG) | T1 | — | — | 3 | <0–3> | <w*s> |
| REQ-D2 | Recency / Freshness | T1 | — | — | 3 | <0–3> | <w*s> |
| REQ-D3 | Source Attribution & Verifiability | T1 | — | — | 3 | <0–3> | <w*s> |
| REQ-D4 | Anti-Hallucination Grounding | T1 | — | — | 3 | <0–3> | <w*s> |

## E. Integration, Action & Simulation

| ID | Requirement | Tier | Gate | Moat | Weight | Score | Weighted |
|---|---|---|---|---|---|---|---|
| REQ-E1 | Systems-of-Record Connectivity | T1 | — | — | 3 | <0–3> | <w*s> |
| REQ-E2 | Action Over Advice | T1 | — | — | 3 | <0–3> | <w*s> |
| REQ-E3 | Closed-Loop Tool Feedback | T1 | — | — | 3 | <0–3> | <w*s> |
| REQ-E4 | Scenario & Counterfactual Simulation | T1 | — | 🛡 | 3 | <0–3> | <w*s> |

## F. Structured Deliverables & Artifacts

| ID | Requirement | Tier | Gate | Moat | Weight | Score | Weighted |
|---|---|---|---|---|---|---|---|
| REQ-F1 | Finished Domain Artifacts | T1 | — | — | 3 | <0–3> | <w*s> |
| REQ-F2 | Format Consistency | T1 | — | — | 3 | <0–3> | <w*s> |
| REQ-F3 | Export & Portability | T1 | — | — | 3 | <0–3> | <w*s> |

## G. Personalization & Adaptive Tailoring

| ID | Requirement | Tier | Gate | Moat | Weight | Score | Weighted |
|---|---|---|---|---|---|---|---|
| REQ-G1 | Situation-Specific Tailoring | T2 | — | — | 4 | <0–3> | <w*s> |
| REQ-G2 | Outcome-Driven Adaptation | T2 | — | — | 4 | <0–3> | <w*s> |
| REQ-G3 | Preference & Style Learning | T2 | — | — | 4 | <0–3> | <w*s> |

## H. Proactivity & Lifecycle Management

| ID | Requirement | Tier | Gate | Moat | Weight | Score | Weighted |
|---|---|---|---|---|---|---|---|
| REQ-H1 | Proactive Cadence | T2 | — | — | 4 | <0–3> | <w*s> |
| REQ-H2 | Anticipation | T2 | — | — | 4 | <0–3> | <w*s> |
| REQ-H3 | Deadline & Milestone Awareness | T2 | — | — | 4 | <0–3> | <w*s> |
| REQ-H4 | Time-to-First-Value Activation | T0 | 🔒 hard | — | 5 | <0–3> | <w*s> |

## I. Trust, Safety, Accountability & Calibration

| ID | Requirement | Tier | Gate | Moat | Weight | Score | Weighted |
|---|---|---|---|---|---|---|---|
| REQ-I1 | Calibrated Confidence | TG | ⚖️ cond | — | 5 | <0–3> | <w*s> |
| REQ-I2 | Guardrails & Domain Constraints | TG | ⚖️ cond | — | 5 | <0–3> | <w*s> |
| REQ-I3 | Human Escalation | TG | ⚖️ cond | — | 5 | <0–3> | <w*s> |
| REQ-I4 | Auditability & Explainability | TG | ⚖️ cond | — | 5 | <0–3> | <w*s> |
| REQ-I5 | Accountable Point of View | TG | ⚖️ cond | — | 5 | <0–3> | <w*s> |

## J. Outcome Orientation & Measurement

> Note: REQ-J4 is consumed in OVE as generic value-attribution (is the OV delivering value vs a general LLM?), reframing the substrate's commercial price-objection wording. Score the underlying capability, not the commercial framing.

| ID | Requirement | Tier | Gate | Moat | Weight | Score | Weighted |
|---|---|---|---|---|---|---|---|
| REQ-J1 | Goal Definition | T2 | — | — | 4 | <0–3> | <w*s> |
| REQ-J2 | Progress Tracking | T2 | — | — | 4 | <0–3> | <w*s> |
| REQ-J3 | Outcome Ownership | T2 | — | — | 4 | <0–3> | <w*s> |
| REQ-J4 | Value Attribution / ROI Surfacing | T2 | — | — | 4 | <0–3> | <w*s> |

## K. Data Governance, Privacy & Ownership

| ID | Requirement | Tier | Gate | Moat | Weight | Score | Weighted |
|---|---|---|---|---|---|---|---|
| REQ-K1 | Data Handling Exceeding Base Provider | TG | ⚖️ cond | — | 5 | <0–3> | <w*s> |
| REQ-K2 | User Data Ownership & Portability | TG | ⚖️ cond | — | 5 | <0–3> | <w*s> |
| REQ-K3 | Domain Compliance Posture | TG | ⚖️ cond | — | 5 | <0–3> | <w*s> |

## L. Reliability, Consistency & Methodological Integrity

| ID | Requirement | Tier | Gate | Moat | Weight | Score | Weighted |
|---|---|---|---|---|---|---|---|
| REQ-L1 | Reproducibility / Quality Floor | T2 | — | — | 4 | <0–3> | <w*s> |
| REQ-L2 | Methodological Consistency | T2 | — | — | 4 | <0–3> | <w*s> |
| REQ-L3 | Versioned Methodology | T2 | — | — | 4 | <0–3> | <w*s> |

## M. Compounding Moat & Retention (Durability)

| ID | Requirement | Tier | Gate | Moat | Weight | Score | Weighted |
|---|---|---|---|---|---|---|---|
| REQ-M1 | Data Flywheel | T2 | — | 🛡 | 4 | <0–3> | <w*s> |
| REQ-M2 | Legitimate Switching Cost | T2 | — | 🛡 | 4 | <0–3> | <w*s> |
| REQ-M3 | Absorption Resistance | T2 | — | 🛡 | 4 | <0–3> | <w*s> |
| REQ-M4 | Cohort & Network Effects | T2 | — | 🛡 | 4 | <0–3> | <w*s> |

## Roll-up

- **Maximum weighted score:** 558
- **This OV's weighted score:** <N>
- **Percentage:** <N>%
- **Moat coverage:** <count of the 5 moat items scoring ≥ 2> / 5

## Verdict bands

| If… | Verdict |
|---|---|
| any hard / applicable-conditional gate < 2 | **At risk — thin wrapper; user defaults to general LLM.** |
| no gate failure AND score ≥ 80% | **Defensible specialist — earns user preference over a general LLM.** |
| no gate failure AND score ≥ 60% | **Viable — real differentiation; close gaps before claiming durability.** |
| no gate failure AND score < 60% | **At risk — thin wrapper territory.** |

## Verdict

**<Defensible specialist | Viable | At risk>** — <one-line summary of the OV's posture>.

> Durability is only claimed when moat coverage reaches 100% (all 5 moat items scoring ≥ 2 OR explicitly n-a with rationale).
