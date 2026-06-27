---
type: Fleeting
Item_ID: <ov-slug>-standalone-sufficiency-posture
title: "<OV Name> — Standalone Sufficiency Posture (Convention 10)"
Date_Added: YYYY-MM-DD
Date_Modified: YYYY-MM-DD
Needs_Processing: false
doc_type: ov-posture
role: standalone-sufficiency-statement
scope: ov-specific
ove_OV_Name: "<OV Name>"
ove_OV_Slug: "<ov-slug>"
ove_Domain_Stakes: "<low | high>"
ove_Convention_10_Revision: "1.2"
updated: YYYY-MM-DD
---

# <OV Name> — Standalone Sufficiency Posture

> **Convention 10 (Standalone Sufficiency Posture) declaration. This OV's operator-facing one-pager: which T0 hard gates pass, which TG conditional gates apply and pass, which T1/T2 requirements are met, and which moat items are committed.**

## Test the OV must pass

> *"Would a general LLM (Claude / ChatGPT / Gemini) be better for this user's work than this OV?"*

A `No` answer requires this OV to clear:

- All **5 T0 hard gates** (parity floor — if absent, the user defaults to a general LLM).
- All **8 TG conditional gates** if `ove_Domain_Stakes: high` (regulated / high-stakes domain).
- ≥1 **moat commitment** with a concrete schema-feature pointer (the un-absorbable claim).

Two master tests every claim must pass:

- **Displacement Test** — a competent user cannot reproduce this in <10 min with a good prompt in a general LLM.
- **Absorption Test** — the platform (OpenAI / Anthropic / Google) is not on track to ship this natively within ~12 months.

The substrate (47 requirements across 13 categories) lives at `_design-engine/_meta/standalone-sufficiency/requirements.yaml` in the OVE engine. This document presents this OV's posture against that substrate.

## Tier coverage summary

| Tier | Definition | This OV's coverage |
|---|---|---|
| **T0 — Parity** (5 hard gates) | Non-negotiable. If absent, user defaults to general LLM. | <N>/5 met |
| **T1 — Differentiators** (15 items) | The active reason to choose the specialist over the default. | <N>/15 met |
| **T2 — Durability / Retention** (19 items) | The reason to stay, and the reason value can't be absorbed. | <N>/19 met |
| **TG — Trust-Gated** (8 items) | Required to enter a regulated / high-stakes domain at all. | <N>/8 met (applicable: yes / no) |

## T0 hard gates — disposition

All 5 must be `met` to ship. No exceptions.

| REQ-ID | Title | Disposition | Evidence |
|---|---|---|---|
| REQ-A1 | Capability Parity | <met \| partial \| n-a \| deferred> | `<file:line or design-decision pointer>` |
| REQ-A2 | Graceful Scope Boundaries | <met \| partial \| n-a \| deferred> | `<…>` |
| REQ-A3 | No Artificial Lobotomy | <met \| partial \| n-a \| deferred> | `<…>` |
| REQ-B1 | Persistent User Model | <met \| partial \| n-a \| deferred> | `<…>` |
| REQ-H4 | Time-to-First-Value Activation | <met \| partial \| n-a \| deferred> | `<…>` |

## TG conditional gates — disposition

Required if `ove_Domain_Stakes: high`. Mark `n-a` with justification only if the OV is unambiguously low-stakes.

| REQ-ID | Title | Disposition | Evidence |
|---|---|---|---|
| REQ-I1 | Calibrated Confidence | <met \| partial \| n-a \| deferred> | `<…>` |
| REQ-I2 | Guardrails & Domain Constraints | <met \| partial \| n-a \| deferred> | `<…>` |
| REQ-I3 | Human Escalation | <met \| partial \| n-a \| deferred> | `<…>` |
| REQ-I4 | Auditability & Explainability | <met \| partial \| n-a \| deferred> | `<…>` |
| REQ-I5 | Accountable Point of View | <met \| partial \| n-a \| deferred> | `<…>` |
| REQ-K1 | Data Handling Exceeding Base Provider | <met \| partial \| n-a \| deferred> | `<…>` |
| REQ-K2 | User Data Ownership & Portability | <met \| partial \| n-a \| deferred> | `<…>` |
| REQ-K3 | Domain Compliance Posture | <met \| partial \| n-a \| deferred> | `<…>` |

## Moat commitments

At least one of the following must be committed with a concrete schema-feature pointer (the schema feature that *makes the moat real*, not just words).

| REQ-ID | Title | Committed? | Schema feature making this real |
|---|---|---|---|
| REQ-E4 | Scenario & Counterfactual Simulation | <yes \| no> | `<schema feature / type name>` |
| REQ-M1 | Data Flywheel | <yes \| no> | `<…>` |
| REQ-M2 | Legitimate Switching Cost | <yes \| no> | `<…>` |
| REQ-M3 | Absorption Resistance | <yes \| no> | `<…>` |
| REQ-M4 | Cohort & Network Effects | <yes \| no> | `<…>` |

## Verdict band (from `_meta/vetting-rubric-filled.md`)

| Indicator | Value |
|---|---|
| Weighted score | <N> / 558 |
| Percentage | <N>% |
| Gating-rule veto fires? | <yes \| no> |
| Verdict | <Defensible specialist \| Viable \| At risk> |

## How to read this

- **Source of truth:** `_meta/posture.yaml` is the YAML registry from which this document and `_meta/vetting-rubric-filled.md` are rendered. Edit `_meta/posture.yaml`, regenerate this file and the rubric.
- **Substrate:** the 47 requirements, the two master tests, and the §17 Anti-Requirements live at `_design-engine/_meta/standalone-sufficiency/` in the OVE engine.
- **Validator:** C14 in `_design-engine/_meta/validate.py` enforces this declaration at ship time.

> **Commerce-neutral framing.** "Standalone Sufficiency" is OVE's neutral framing of the field-agnostic spec the substrate calls "Loyalty & Retention." The construction standard is identical; the surface language is translated so the test applies whether this OV is commercial or not. See `_design-engine/_meta/standalone-sufficiency/README.md` for the terminology seam.
