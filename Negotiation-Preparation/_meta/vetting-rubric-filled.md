---
type: Fleeting
timestamp: "2026-06-14T00:00:00Z"
Item_ID: negotiation-prep-vetting-rubric-filled
title: "Negotiation-Preparation — Vetting Rubric (filled, Convention 10)"
Date_Added: 2026-06-14
Date_Modified: 2026-06-14
Needs_Processing: false
doc_type: ov-posture
role: vetting-rubric-filled
scope: ov-specific
ove_OV_Name: "Negotiation-Preparation"
ove_OV_Slug: "negotiation-prep"
ove_Domain_Stakes: "high"
ove_Convention_10_Revision: "1.2"
updated: 2026-06-14
---

# Negotiation-Preparation — Vetting Rubric (filled)

> **Generated from `_meta/posture.yaml` against `_design-engine/_meta/standalone-sufficiency/vetting-rubric.md`. Score 0–3 per requirement; weighted roll-up yields verdict.**

## Scoring scale

- **0** Absent — **1** Partial — **2** Adequate — **3** Strong

Disposition → score convention used: `met` → 3, `partial` → 1, `n-a` → 2 (treated as cleared), `deferred` → 0.

## A. Foundational Parity & Scope Integrity

| ID | Requirement | Tier | Gate | Weight | Score | Weighted |
|---|---|---|---|---|---|---|
| REQ-A1 | Capability Parity | T0 | 🔒 hard | 5 | 3 | 15 |
| REQ-A2 | Graceful Scope Boundaries | T0 | 🔒 hard | 5 | 3 | 15 |
| REQ-A3 | No Artificial Lobotomy | T0 | 🔒 hard | 5 | 3 | 15 |

## B. Memory & Statefulness

| ID | Requirement | Tier | Gate | Weight | Score | Weighted |
|---|---|---|---|---|---|---|
| REQ-B1 | Persistent User Model | T0 | 🔒 hard | 5 | 3 | 15 |
| REQ-B2 | Longitudinal Continuity | T2 | — | 4 | 3 | 12 |
| REQ-B3 | Compounding Context Value | T2 | — | 4 | 3 | 12 |

## C. Workflow Orchestration & Guided Process

| ID | Requirement | Tier | Gate | Weight | Score | Weighted |
|---|---|---|---|---|---|---|
| REQ-C1 | Expert Interactive Intake | T1 | — | 3 | 3 | 9 |
| REQ-C2 | Multi-Step Task Chaining | T1 | — | 3 | 3 | 9 |
| REQ-C3 | Process State & Resumability | T1 | — | 3 | 3 | 9 |
| REQ-C4 | Opinionated Default Path | T1 | — | 3 | 3 | 9 |

## D. Proprietary Knowledge & Grounding

| ID | Requirement | Tier | Gate | Weight | Score | Weighted |
|---|---|---|---|---|---|---|
| REQ-D1 | Curated Authoritative Corpus (RAG) | T1 | — | 3 | 1 | 3 |
| REQ-D2 | Recency / Freshness | T1 | — | 3 | 2 | 6 |
| REQ-D3 | Source Attribution & Verifiability | T1 | — | 3 | 1 | 3 |
| REQ-D4 | Anti-Hallucination Grounding | T1 | — | 3 | 3 | 9 |

## E. Integration, Action & Simulation

| ID | Requirement | Tier | Gate | Moat | Weight | Score | Weighted |
|---|---|---|---|---|---|---|---|
| REQ-E1 | Systems-of-Record Connectivity | T1 | — | — | 3 | 2 | 6 |
| REQ-E2 | Action Over Advice | T1 | — | — | 3 | 3 | 9 |
| REQ-E3 | Closed-Loop Tool Feedback | T1 | — | — | 3 | 1 | 3 |
| REQ-E4 | Scenario & Counterfactual Simulation | T1 | — | 🛡 | 3 | 3 | 9 |

## F. Structured Deliverables & Artifacts

| ID | Requirement | Tier | Gate | Weight | Score | Weighted |
|---|---|---|---|---|---|---|
| REQ-F1 | Finished Domain Artifacts | T1 | — | 3 | 3 | 9 |
| REQ-F2 | Format Consistency | T1 | — | 3 | 3 | 9 |
| REQ-F3 | Export & Portability | T1 | — | 3 | 3 | 9 |

## G. Personalization & Adaptive Tailoring

| ID | Requirement | Tier | Gate | Weight | Score | Weighted |
|---|---|---|---|---|---|---|
| REQ-G1 | Situation-Specific Tailoring | T2 | — | 4 | 3 | 12 |
| REQ-G2 | Outcome-Driven Adaptation | T2 | — | 4 | 3 | 12 |
| REQ-G3 | Preference & Style Learning | T2 | — | 4 | 1 | 4 |

## H. Proactivity & Lifecycle Management

| ID | Requirement | Tier | Gate | Weight | Score | Weighted |
|---|---|---|---|---|---|---|
| REQ-H1 | Proactive Cadence | T2 | — | 4 | 1 | 4 |
| REQ-H2 | Anticipation | T2 | — | 4 | 3 | 12 |
| REQ-H3 | Deadline & Milestone Awareness | T2 | — | 4 | 3 | 12 |
| REQ-H4 | Time-to-First-Value Activation | T0 | 🔒 hard | 5 | 3 | 15 |

## I. Trust, Safety, Accountability & Calibration

| ID | Requirement | Tier | Gate | Weight | Score | Weighted |
|---|---|---|---|---|---|---|
| REQ-I1 | Calibrated Confidence | TG | ⚖️ cond | 5 | 3 | 15 |
| REQ-I2 | Guardrails & Domain Constraints | TG | ⚖️ cond | 5 | 3 | 15 |
| REQ-I3 | Human Escalation | TG | ⚖️ cond | 5 | 3 | 15 |
| REQ-I4 | Auditability & Explainability | TG | ⚖️ cond | 5 | 3 | 15 |
| REQ-I5 | Accountable Point of View | TG | ⚖️ cond | 5 | 3 | 15 |

## J. Outcome Orientation & Measurement

| ID | Requirement | Tier | Gate | Weight | Score | Weighted |
|---|---|---|---|---|---|---|
| REQ-J1 | Goal Definition | T2 | — | 4 | 3 | 12 |
| REQ-J2 | Progress Tracking | T2 | — | 4 | 3 | 12 |
| REQ-J3 | Outcome Ownership | T2 | — | 4 | 3 | 12 |
| REQ-J4 | Value Attribution / ROI Surfacing | T2 | — | 4 | 1 | 4 |

## K. Data Governance, Privacy & Ownership

| ID | Requirement | Tier | Gate | Weight | Score | Weighted |
|---|---|---|---|---|---|---|
| REQ-K1 | Data Handling Exceeding Base Provider | TG | ⚖️ cond | 5 | 3 | 15 |
| REQ-K2 | User Data Ownership & Portability | TG | ⚖️ cond | 5 | 3 | 15 |
| REQ-K3 | Domain Compliance Posture | TG | ⚖️ cond | 5 | 3 | 15 |

## L. Reliability, Consistency & Methodological Integrity

| ID | Requirement | Tier | Gate | Weight | Score | Weighted |
|---|---|---|---|---|---|---|
| REQ-L1 | Reproducibility / Quality Floor | T2 | — | 4 | 3 | 12 |
| REQ-L2 | Methodological Consistency | T2 | — | 4 | 3 | 12 |
| REQ-L3 | Versioned Methodology | T2 | — | 4 | 3 | 12 |

## M. Compounding Moat & Retention (Durability)

| ID | Requirement | Tier | Gate | Moat | Weight | Score | Weighted |
|---|---|---|---|---|---|---|---|
| REQ-M1 | Data Flywheel | T2 | — | 🛡 | 4 | 0 | 0 |
| REQ-M2 | Legitimate Switching Cost | T2 | — | 🛡 | 4 | 3 | 12 |
| REQ-M3 | Absorption Resistance | T2 | — | 🛡 | 4 | 3 | 12 |
| REQ-M4 | Cohort & Network Effects | T2 | — | 🛡 | 4 | 2 | 8 |

## Roll-up

| Indicator | Value |
|---|---|
| Maximum weighted score | 558 |
| **This OV's weighted score** | **494** |
| **Percentage** | **88.5%** |
| Moat coverage | **4/5** (E4=3, M1=0, M2=3, M3=3, M4=2) |

## Gating rule check

- All 5 T0 hard gates scored ≥2? **Yes** (all 3)
- All 8 applicable TG gates scored ≥2? **Yes** (all 3)
- Gating-rule veto fires? **No**

## Verdict

**Defensible specialist — earns operator preference over a general LLM for negotiation preparation.**

Percentage ≥80% AND no gate failure → top verdict band. Two moat items (REQ-E4 wargame simulation, REQ-M2 legitimate switching cost) carry durability; REQ-M3 (Absorption Resistance) clears via the moat items themselves; REQ-M1 (Data Flywheel) is the only gap and is honestly deferred. REQ-M4 (Cohort) is domain-inappropriate per substrate caveat.

> **One transparent caveat:** REQ-J4 (Value Attribution) scores partial. The OV captures lessons in post-mortems but does not meter time saved / surprises caught / dollars-impact. A future revision could add explicit value-attribution surfacing for operators who want it.
