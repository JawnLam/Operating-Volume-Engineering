---
Item_Prototype: Fleeting
Item_ID: solve-ex-standalone-sufficiency-posture
Title: "SOLVE-eX — Standalone Sufficiency Posture (Convention 10)"
Date_Added: 2026-06-14
Date_Modified: 2026-06-14
Needs_Processing: false
type: ov-posture
role: standalone-sufficiency-statement
scope: ov-specific
ove_OV_Name: "SOLVE-eX"
ove_OV_Slug: "solve-ex"
ove_Domain_Stakes: "high"
ove_Convention_10_Revision: "1.2"
updated: 2026-06-14
---

# SOLVE-eX — Standalone Sufficiency Posture

> **Convention 10 declaration. SOLVE-eX is v2.1.0 (publicly shipped at `github.com/JawnLam/SOLVE-eX`). This declaration is a retrospective posture against the field-agnostic 47-requirement substrate.**

## Test the OV must pass

> *"Would Claude / ChatGPT / Gemini be better for structured decision-making and problem-solving than this OV?"*

A `No` answer rests on:

- **All 5 T0 hard gates pass** — engine prose + 5 personas + 21-step process match or exceed a general LLM on overlapping queries; adjacent-topic handling is graceful; the operator can ask direct questions and bypass the 21-step process when appropriate; each Case File holds persistent state across sessions; session 1 produces the framed problem + initial tool applications.
- **All 8 TG conditional gates pass** — high-stakes domain (decisions with irreversible consequences); calibrated confidence, hard guardrails, named escalation, auditable trail through tool corpus, named accountable methodology, files-on-disk privacy beats vendor defaults, operator owns and exports, regulated-profession deflection in place.
- **Three moat commitments are real** — REQ-E4 (methodology-bounded tool application against actual case-file state), REQ-M2 (case-file library as system of record for decision-making practice), REQ-M3 (677-entry curated corpus + 14-chapter methodology + 21-step process is proprietary curation, not promptable behavior).

## Tier coverage summary

| Tier | Definition | Coverage |
|---|---|---|
| **T0 — Parity** (5 hard gates) | If absent, user defaults to general LLM. | **5/5 met** |
| **T1 — Differentiators** (15 items) | Active reason to choose this OV over the default. | 12 met · 2 partial · 1 n-a |
| **T2 — Durability** (19 items) | Reason to stay; un-absorbable value. | 14 met · 3 partial · 1 deferred · 1 n-a |
| **TG — Trust-Gated** (8 items) | Required to enter high-stakes domain at all. | **8/8 met** (applicable: yes) |

## T0 hard gates — disposition (all 5 must be `met`)

| REQ-ID | Title | Disposition | Evidence |
|---|---|---|---|
| REQ-A1 | Capability Parity | **met** | Engine prose + 5 personas + 21-step process match general-LLM on overlapping queries, often exceed on structured-thinking |
| REQ-A2 | Graceful Scope Boundaries | **met** | Persona switching rules permit informal engagement when 21-step process isn't warranted |
| REQ-A3 | No Artificial Lobotomy | **met** | Operator can bypass the 21-step process and ask direct questions |
| REQ-B1 | Persistent User Model | **met** | Case File holds problem context, criteria, tools applied, conclusions, action plan across sessions |
| REQ-H4 | Time-to-First-Value Activation | **met** | Session 1 produces the framed problem + initial tool-application set |

## TG conditional gates — disposition (high stakes domain)

| REQ-ID | Title | Disposition | Evidence |
|---|---|---|---|
| REQ-I1 | Calibrated Confidence | **met** | Engine signals uncertainty proportionate to stakes; decision-tree outcomes carry confidence bands |
| REQ-I2 | Guardrails & Domain Constraints | **met** | Hard stops on medical / legal / financial / safety advice; routes to licensed professionals |
| REQ-I3 | Human Escalation | **met** | External Expert Switch persona explicitly handles escalation triggers |
| REQ-I4 | Auditability & Explainability | **met** | Case file traces every conclusion to the tool entry that produced it |
| REQ-I5 | Accountable Point of View | **met** | Named SOLVE-eX methodology + 677-entry corpus with named tool authors |
| REQ-K1 | Data Handling Exceeding Base Provider | **met** | Files-on-disk (Operator-Private Zone) keeps decision data local; beats vendor-server defaults |
| REQ-K2 | User Data Ownership & Portability | **met** | Markdown files; operator owns, exports, deletes on demand |
| REQ-K3 | Domain Compliance Posture | **met** | Structured decision-making isn't a regulated profession at OV layer; deflects regulated domains to licensed pros |

## Moat commitments (3 committed)

| REQ-ID | Title | Schema feature making this real |
|---|---|---|
| **REQ-E4** | Scenario & Counterfactual Simulation | 21-step process applied to a Case File runs methodology-bounded thinking-tool applications against the operator's actual situation — quantified next-action traceable to the specific tool entry that produced it |
| **REQ-M2** | Legitimate Switching Cost | Per-case-file accumulated state becomes the operator's system of record for their decision-making practice. Leaving the OV forfeits the case-file library |
| **REQ-M3** | Absorption Resistance | Core value rests on the 677-entry curated tool corpus + 14-chapter methodology + 21-step process + 5 operational personas — proprietary curation, not promptable behavior the platform can ship in 12 months |

## Verdict band (from `_meta/vetting-rubric-filled.md`)

| Indicator | Value |
|---|---|
| Weighted score | **503 / 558** |
| Percentage | **~90.1%** |
| Gating-rule veto fires? | No (no T0/TG floor violation) |
| Moat coverage | 4/5 moat items scoring ≥2 (M1 deferred at 0; M4 n-a treated as cleared) |
| **Verdict** | **Defensible specialist — earns operator preference over a general LLM for structured decision-making.** |

## How to read this

- **Source of truth:** `_meta/posture.yaml`. Edit there, regenerate this file and `_meta/vetting-rubric-filled.md`.
- **Substrate:** the 47 requirements live at `_design-engine/_meta/standalone-sufficiency/` in the OVE engine.
- **Validator:** C14 in `_design-engine/_meta/validate.py` enforces this declaration at ship time.

> **Note on REQ-J4.** OVE consumes the substrate's J4 ("Value Attribution") as generic value-attribution (is the OV delivering value vs a general LLM?). SOLVE-eX's J4 is `partial` — outcome logging exists but no formal time-saved/decisions-accelerated metering. A future revision could add explicit value-attribution surfacing.

> **Note on REQ-M1.** Data flywheel is `deferred` because v2.1.0 doesn't aggregate cross-operator outcome data. The moat rests on M2/M3 instead, both of which clear cleanly.

> **Note on REQ-M4.** Cohort & Network Effects is `n-a` — structured decision-making frequently involves confidential business context; gated cohort with peer benchmarks creates confidentiality conflicts. Domain-inappropriate per substrate §15 caveat.
