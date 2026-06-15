---
Item_Prototype: Fleeting
Item_ID: negotiation-prep-standalone-sufficiency-posture
Title: "Negotiation-Preparation — Standalone Sufficiency Posture (Convention 10)"
Date_Added: 2026-06-14
Date_Modified: 2026-06-14
Needs_Processing: false
type: ov-posture
role: standalone-sufficiency-statement
scope: ov-specific
ove_OV_Name: "Negotiation-Preparation"
ove_OV_Slug: "negotiation-prep"
ove_Domain_Stakes: "high"
ove_Convention_10_Revision: "1.2"
updated: 2026-06-14
---

# Negotiation-Preparation — Standalone Sufficiency Posture

> **Convention 10 declaration. This OV defends its existence against the question: would a general LLM be better for negotiation preparation than this OV?**

## Test the OV must pass

> *"Would Claude / ChatGPT / Gemini be better for preparing a specific upcoming negotiation than this OV?"*

A `No` answer rests on:

- **All 5 T0 hard gates pass** — the OV is at least as capable as a general LLM on overlapping queries, handles adjacent topics gracefully, doesn't lobotomize itself to force workflow, retains a persistent stakeholder/BATNA model across sessions per negotiation, and engineers a first-win prep document within session 1.
- **All 8 TG conditional gates pass** — high-stakes domain (financial, professional, relational consequences); the OV signals calibrated confidence, enforces refuse-legal-advice and refuse-manipulation guardrails, escalates to lawyer/therapist/mediator at named thresholds, traces every recommendation to the methodology, ships under a named methodology (Fisher/Ury, Diamond, Voss, Raiffa), keeps negotiation data local on operator's disk (beats base-API default), preserves operator ownership, and avoids regulated-profession overreach.
- **Two moat commitments are real** — REQ-E4 (wargame against the user's actual stakeholder map) and REQ-M2 (accumulated negotiation library is the operator's system of record).

## Tier coverage summary

| Tier | Definition | Coverage |
|---|---|---|
| **T0 — Parity** (5 hard gates) | If absent, user defaults to general LLM. | **5/5 met** |
| **T1 — Differentiators** (15 items) | Active reason to choose this OV over the default. | 10 met · 3 partial · 2 n-a |
| **T2 — Durability** (19 items) | Reason to stay; un-absorbable value. | 14 met · 3 partial · 1 deferred · 1 n-a |
| **TG — Trust-Gated** (8 items) | Required to enter high-stakes domain at all. | **8/8 met** (applicable: yes) |

## T0 hard gates — disposition (all 5 must be `met`)

| REQ-ID | Title | Disposition | Evidence |
|---|---|---|---|
| REQ-A1 | Capability Parity | **met** | Engine prose + structured intake matches general-LLM output on overlapping queries |
| REQ-A2 | Graceful Scope Boundaries | **met** | `_ov-manifest.md` §scope-boundaries — handles adjacent topics, refuses only sign-off-grade out-of-domain |
| REQ-A3 | No Artificial Lobotomy | **met** | Operator can always ask a direct question and get a direct answer |
| REQ-B1 | Persistent User Model | **met** | Per-cartridge state file holds stakeholder map / BATNA / concession plan across sessions |
| REQ-H4 | Time-to-First-Value Activation | **met** | Session 1 ships the opening-version prep document |

## TG conditional gates — disposition (high stakes domain)

| REQ-ID | Title | Disposition | Evidence |
|---|---|---|---|
| REQ-I1 | Calibrated Confidence | **met** | Methodology explicit; uncertainty signaled proportionate to stakes |
| REQ-I2 | Guardrails & Domain Constraints | **met** | Hard stops on legal advice, therapy, manipulation toolkit |
| REQ-I3 | Human Escalation | **met** | Routes to lawyer for legal exposure, therapist for relational, mediator for high-conflict |
| REQ-I4 | Auditability & Explainability | **met** | Prep doc traces every recommendation to named methodology |
| REQ-I5 | Accountable Point of View | **met** | Fisher/Ury, Diamond, Voss, Raiffa methodology stands behind the OV's recommendations |
| REQ-K1 | Data Handling Exceeding Base Provider | **met** | Files-on-disk (Convention 8 Operator-Private Zone) keeps negotiation data local; beats vendor-server defaults |
| REQ-K2 | User Data Ownership & Portability | **met** | Markdown files; operator owns, exports, deletes on demand |
| REQ-K3 | Domain Compliance Posture | **met** | Negotiation prep is not a regulated profession; OV deflects legal/therapy to licensed pros |

## Moat commitments (2 committed)

| REQ-ID | Title | Schema feature making this real |
|---|---|---|
| **REQ-E4** | Scenario & Counterfactual Simulation | Wargame role-play (step 6 of the 7-step process) simulates plausible counter-party responses against this negotiation's stakeholder map, BATNA, and concession plan — producing a quantified projection traceable to Fisher/Ury/Voss methodology |
| **REQ-M2** | Legitimate Switching Cost | Per-cartridge prep + post-mortem documents accumulate into a queryable library of patterns across all of the operator's negotiations. Leaving the OV forfeits this library |

## Verdict band (from `_meta/vetting-rubric-filled.md`)

| Indicator | Value |
|---|---|
| Weighted score | **494 / 558** |
| Percentage | **~88.5%** |
| Gating-rule veto fires? | No (no T0/TG floor violation) |
| Moat coverage | 4/5 moat items scoring ≥2 (M1 deferred at 0; M4 n-a treated as cleared) |
| **Verdict** | **Defensible specialist — earns operator preference over a general LLM for negotiation preparation.** |

## How to read this

- **Source of truth:** `_meta/posture.yaml`. Edit there, regenerate this file and `_meta/vetting-rubric-filled.md`.
- **Substrate:** the 47 requirements, the two master tests, and the §17 Anti-Requirements live at `_design-engine/_meta/standalone-sufficiency/` in the OVE engine.
- **Validator:** C14 in `_design-engine/_meta/validate.py` enforces this declaration at ship time.

> **Note on REQ-J4.** OVE consumes the substrate's J4 ("Value Attribution") as generic value-attribution (is the OV delivering value vs a general LLM?) rather than the substrate's commercial price-objection framing. Negotiation-Preparation's J4 is `partial` — post-mortem surfaces lessons but no formal metering — and this is honest, not a downgrade. A future revision could add explicit time-saved / surprise-caught metering.

> **Note on REQ-M1.** Data flywheel is `deferred` because v1 doesn't collect cross-operator outcome data. This is the only gap; the moat rests on M2/M3 instead, both of which clear cleanly.
