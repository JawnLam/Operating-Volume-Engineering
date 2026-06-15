# Specialized AI Agent — Loyalty & Retention Requirements — Vetting Rubric (rev 1.2)

> Generated from `requirements.yaml`. Score a candidate agent 0–3 per requirement; the weighted roll-up yields a verdict.

## Scoring scale
- **0** — Absent — no evidence the requirement is met.
- **1** — Partial — gestured at, but weak or inconsistent.
- **2** — Adequate — present and reliable.
- **3** — Strong — a clear, differentiating implementation.

## Gating rule (veto)
Any **hard gate (T0)** — or any **applicable conditional gate (TG)** — scoring below **2** caps the verdict at *At risk*, regardless of the weighted total. You cannot score your way past a broken floor.

## A. Foundational Parity & Scope Integrity
*If the specialist feels dumber or more caged than the general model, no other feature matters.*

| ID | Requirement | Tier | Gate | Moat | Weight | Score (0–3) | Weighted |
|---|---|---|---|---|---|---|---|
| REQ-A1 | Capability Parity | T0 | 🔒 hard | — | 5 | ___ | ___ |
| REQ-A2 | Graceful Scope Boundaries | T0 | 🔒 hard | — | 5 | ___ | ___ |
| REQ-A3 | No Artificial Lobotomy | T0 | 🔒 hard | — | 5 | ___ | ___ |

## B. Memory & Statefulness
*The single biggest structural gap between a service and a chat window.*

| ID | Requirement | Tier | Gate | Moat | Weight | Score (0–3) | Weighted |
|---|---|---|---|---|---|---|---|
| REQ-B1 | Persistent User Model | T0 | 🔒 hard | — | 5 | ___ | ___ |
| REQ-B2 | Longitudinal Continuity | T2 | — | — | 4 | ___ | ___ |
| REQ-B3 | Compounding Context Value | T2 | — | — | 4 | ___ | ___ |

## C. Workflow Orchestration & Guided Process
*Sells the knowledge of how to extract value, not the value itself. Kills the prompting deficit.*

| ID | Requirement | Tier | Gate | Moat | Weight | Score (0–3) | Weighted |
|---|---|---|---|---|---|---|---|
| REQ-C1 | Expert Interactive Intake | T1 | — | — | 3 | ___ | ___ |
| REQ-C2 | Multi-Step Task Chaining | T1 | — | — | 3 | ___ | ___ |
| REQ-C3 | Process State & Resumability | T1 | — | — | 3 | ___ | ___ |
| REQ-C4 | Opinionated Default Path | T1 | — | — | 3 | ___ | ___ |

## D. Proprietary Knowledge & Grounding
*Anchors the reasoning engine to data the general model never saw and cannot guess.*

| ID | Requirement | Tier | Gate | Moat | Weight | Score (0–3) | Weighted |
|---|---|---|---|---|---|---|---|
| REQ-D1 | Curated Authoritative Corpus (RAG) | T1 | — | — | 3 | ___ | ___ |
| REQ-D2 | Recency / Freshness | T1 | — | — | 3 | ___ | ___ |
| REQ-D3 | Source Attribution & Verifiability | T1 | — | — | 3 | ___ | ___ |
| REQ-D4 | Anti-Hallucination Grounding | T1 | — | — | 3 | ___ | ___ |

## E. Integration, Action & Simulation
*The verb matters more than the noun. Advice is commoditized; doing — and forecasting — the thing is not.*

| ID | Requirement | Tier | Gate | Moat | Weight | Score (0–3) | Weighted |
|---|---|---|---|---|---|---|---|
| REQ-E1 | Systems-of-Record Connectivity | T1 | — | — | 3 | ___ | ___ |
| REQ-E2 | Action Over Advice | T1 | — | — | 3 | ___ | ___ |
| REQ-E3 | Closed-Loop Tool Feedback | T1 | — | — | 3 | ___ | ___ |
| REQ-E4 | Scenario & Counterfactual Simulation | T1 | — | 🛡 | 3 | ___ | ___ |

## F. Structured Deliverables & Artifacts
*A coach produces a roadmap and a scorecard. A chatbot produces text you must assemble yourself.*

| ID | Requirement | Tier | Gate | Moat | Weight | Score (0–3) | Weighted |
|---|---|---|---|---|---|---|---|
| REQ-F1 | Finished Domain Artifacts | T1 | — | — | 3 | ___ | ___ |
| REQ-F2 | Format Consistency | T1 | — | — | 3 | ___ | ___ |
| REQ-F3 | Export & Portability | T1 | — | — | 3 | ___ | ___ |

## G. Personalization & Adaptive Tailoring
*Generic advice is the tell of a wrapper. Constrained, situation-specific advice is the product.*

| ID | Requirement | Tier | Gate | Moat | Weight | Score (0–3) | Weighted |
|---|---|---|---|---|---|---|---|
| REQ-G1 | Situation-Specific Tailoring | T2 | — | — | 4 | ___ | ___ |
| REQ-G2 | Outcome-Driven Adaptation | T2 | — | — | 4 | ___ | ___ |
| REQ-G3 | Preference & Style Learning | T2 | — | — | 4 | ___ | ___ |

## H. Proactivity & Lifecycle Management
*A general LLM only acts when you open it. A service drives the cadence.*

| ID | Requirement | Tier | Gate | Moat | Weight | Score (0–3) | Weighted |
|---|---|---|---|---|---|---|---|
| REQ-H1 | Proactive Cadence | T2 | — | — | 4 | ___ | ___ |
| REQ-H2 | Anticipation | T2 | — | — | 4 | ___ | ___ |
| REQ-H3 | Deadline & Milestone Awareness | T2 | — | — | 4 | ___ | ___ |
| REQ-H4 | Time-to-First-Value Activation | T0 | 🔒 hard | — | 5 | ___ | ___ |

## I. Trust, Safety, Accountability & Calibration
*In high-stakes domains, a confident wrong answer is worse than no answer.*

| ID | Requirement | Tier | Gate | Moat | Weight | Score (0–3) | Weighted |
|---|---|---|---|---|---|---|---|
| REQ-I1 | Calibrated Confidence | TG | ⚖️ cond | — | 5 | ___ | ___ |
| REQ-I2 | Guardrails & Domain Constraints | TG | ⚖️ cond | — | 5 | ___ | ___ |
| REQ-I3 | Human Escalation | TG | ⚖️ cond | — | 5 | ___ | ___ |
| REQ-I4 | Auditability & Explainability | TG | ⚖️ cond | — | 5 | ___ | ___ |
| REQ-I5 | Accountable Point of View | TG | ⚖️ cond | — | 5 | ___ | ___ |

## J. Outcome Orientation & Measurement
*A general model answers questions. A coach owns the result with you — and proves it.*

| ID | Requirement | Tier | Gate | Moat | Weight | Score (0–3) | Weighted |
|---|---|---|---|---|---|---|---|
| REQ-J1 | Goal Definition | T2 | — | — | 4 | ___ | ___ |
| REQ-J2 | Progress Tracking | T2 | — | — | 4 | ___ | ___ |
| REQ-J3 | Outcome Ownership | T2 | — | — | 4 | ___ | ___ |
| REQ-J4 | Value Attribution / ROI Surfacing | T2 | — | — | 4 | ___ | ___ |

## K. Data Governance, Privacy & Ownership
*Privacy is only a differentiator if it genuinely exceeds what the base provider already offers.*

| ID | Requirement | Tier | Gate | Moat | Weight | Score (0–3) | Weighted |
|---|---|---|---|---|---|---|---|
| REQ-K1 | Data Handling Exceeding Base Provider | TG | ⚖️ cond | — | 5 | ___ | ___ |
| REQ-K2 | User Data Ownership & Portability | TG | ⚖️ cond | — | 5 | ___ | ___ |
| REQ-K3 | Domain Compliance Posture | TG | ⚖️ cond | — | 5 | ___ | ___ |

## L. Reliability, Consistency & Methodological Integrity
*A general model is brilliant but variable. A professional tool has a quality floor.*

| ID | Requirement | Tier | Gate | Moat | Weight | Score (0–3) | Weighted |
|---|---|---|---|---|---|---|---|
| REQ-L1 | Reproducibility / Quality Floor | T2 | — | — | 4 | ___ | ___ |
| REQ-L2 | Methodological Consistency | T2 | — | — | 4 | ___ | ___ |
| REQ-L3 | Versioned Methodology | T2 | — | — | 4 | ___ | ___ |

## M. Compounding Moat & Retention (Durability)
*The requirements that make value un-absorbable and switching genuinely costly.*

| ID | Requirement | Tier | Gate | Moat | Weight | Score (0–3) | Weighted |
|---|---|---|---|---|---|---|---|
| REQ-M1 | Data Flywheel | T2 | — | 🛡 | 4 | ___ | ___ |
| REQ-M2 | Legitimate Switching Cost | T2 | — | 🛡 | 4 | ___ | ___ |
| REQ-M3 | Absorption Resistance | T2 | — | 🛡 | 4 | ___ | ___ |
| REQ-M4 | Cohort & Network Effects | T2 | — | 🛡 | 4 | ___ | ___ |

## Roll-up

- **Maximum weighted score:** 558  (sum of weight × 3 across all requirements)
- **Your weighted score:** sum of (weight × score) across all rows.
- **Percentage:** your weighted score ÷ maximum weighted score.
- **Moat coverage:** count of the 5 moat items scoring ≥ 2, ÷ 5.

## Verdict bands

| If… | Verdict |
|---|---|
| any hard/applicable-conditional gate < 2 | **At risk — thin wrapper; a savvy user defaults to the general model.** |
| no gate failure and score ≥ 80% | **Defensible specialist — earns loyalty over a general LLM.** |
| no gate failure and score ≥ 60% | **Viable — real differentiation, but close the gaps before claiming the moat.** |
| no gate failure and score ≥ 0% | **At risk — thin wrapper territory; a savvy user will default to the general model.** |

> A high percentage with a failed gate is still *At risk*. Durability is only claimed when moat coverage reaches 100%.
