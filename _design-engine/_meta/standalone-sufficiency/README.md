---
type: Fleeting
timestamp: "2026-06-14T00:00:00Z"
Item_ID: ove-meta-standalone-sufficiency-readme
title: "OVE Meta — Standalone Sufficiency Substrate (Convention 10)"
Date_Added: 2026-06-14
Date_Modified: 2026-06-14
Needs_Processing: false
doc_type: design-engine-meta
role: substrate-readme
scope: subject-agnostic
updated: 2026-06-14
---

# OVE Meta — Standalone Sufficiency Substrate

> **This folder is the vendored substrate Convention 10 (Standalone Sufficiency Posture) consumes. It is a field-agnostic, 47-requirement specification for whether a specialized AI agent — including any OV designed via OVE — survives the question *"would a general LLM be better?"* The substrate is read-only from OVE's perspective; OVE owns this folder as a downstream consumer, not as the upstream author.**

## Why OVE bundles this spec

In market-facing terms, an OV is a specialized AI agent. The objection an OV must defeat is structural:

> *"Why use your specialized agent over Claude / ChatGPT / Gemini?"*

The spec at `requirements.yaml` is the field-agnostic answer: 47 requirements across 13 categories, grouped into 4 tiers (T0 parity hard gates, T1 differentiators, T2 retention/moat, TG trust-gated), with 5 moat items as the un-absorbable core. Every requirement is written to pass two master tests:

- **Displacement Test** — Can a competent user reproduce this in <10 minutes with a good prompt in a general LLM? If yes → it's a prompt, not a product.
- **Absorption Test** — Will the platform ship this natively within ~12 months? If yes → table stakes, not a durable distinction.

OVE bundles the spec rather than referencing it externally so that:

1. Convention 10 has a single, stable source-of-truth for all 47 requirement IDs (REQ-A1, …, REQ-M4) — the same IDs the per-OV `_meta/posture.yaml` files reference and the C14 validator checks.
2. OVE upgrades on its own cadence (the spec can land at rev 1.2 in v2.2.0 of OVE and rev 1.3 in v2.3.0 — explicit version coupling, no silent drift).
3. The full substrate is available offline / on a fresh clone of OVE — no external download required.

## Files in this folder

Three **source** files (the substrate's authority — edit these to evolve the spec):

| File | Role |
|---|---|
| `requirements.yaml` | Single source of truth. Every entry carries its tier, journey stage, gate type, weight, and moat flag. |
| `render.py` | Generator. Reads the YAML and writes the three views below. |
| `specialized-agent-requirements.md` | Narrative master — the prose conceptual document. Hand-maintained, not generated. |

Three **generated** views (regenerable any time):

| File | Role |
|---|---|
| `build-standard.md` | Internal build standard — acceptance tests as binary pass/fail gates with ship logic. |
| `vetting-rubric.md` | Client-facing vetting rubric — 0–3 weighted scorecard (max 558) with gate-veto and verdict bands. |
| `requirements-registry.csv` | Flat dump of every field for spreadsheet / automation consumption. |

## Regenerate

```bash
cd _design-engine/_meta/standalone-sufficiency
python3 render.py --src requirements.yaml --out .
```

Requires PyYAML (`pip install pyyaml`).

## Known seam — YAML vs. narrative (drift risk)

Requirement text currently lives in **two** places: `requirements.yaml` (the source of truth) and the narrative `specialized-agent-requirements.md` (hand-maintained prose). They agree at rev 1.2. **This is the one drift risk in the substrate.** The upstream spec owner is responsible for keeping them aligned. OVE consumes both; if drift is later detected, OVE's bundled copies refresh by re-vendoring from the upstream source.

If the seam is closed upstream (`render.py` extended to also emit the narrative's per-requirement tables from the YAML), OVE simply re-vendors all six files.

## Substrate-vs-OVE-surface terminology seam (LOAD-BEARING)

The substrate retains its **original commercial framing** because OVE does not modify vendored upstream content. The spec was originally authored for commercial specialized AI agents, so it uses:

- "Loyalty & Retention Requirements" (the title)
- "Customer" / "subscriber" (the agent's user)
- "Retention" as Tier T2's label
- REQ-J4 framed as "Why pay $100 when ChatGPT is $20?"

**OVE's surface area does NOT use these terms.** Many OVs designed via OVE are not commercialized — internal tools, personal systems, team operating volumes, methodology corpora. The construction standard still applies (the user should not prefer a general LLM for the OV's domain), but the framing must be commerce-neutral. OVE's wrapping prose (Convention 10, the engine cross-references, the per-OV artifact names, the validator messages, the templates) translates the commercial terms to neutral equivalents:

| Source spec (commercial) | OVE surface (neutral) |
|---|---|
| "Loyalty & Retention" | "Standalone Sufficiency" |
| "Loyalty driver" | "Sufficiency driver" |
| "Customer" / "subscriber" | "User" / "operator" |
| "Retention" (as tier label) | "Durability" |
| REQ-J4 "Why pay $100?" framing | "Value attribution: is this delivering value vs a general LLM?" |

This is a deliberate seam, not a bug. If you encounter "loyalty" or "retention" wording while reading source files in this folder, it is **expected** — the substrate is upstream, OVE is downstream. When wiring substrate concepts into OVE artifacts (`standalone-sufficiency-posture.md`, `_meta/posture.yaml`, `_meta/vetting-rubric-filled.md`, validator messages, Convention 10 prose, the master tests in `02-DESIGN-PRINCIPLES.md`), always translate to the neutral OVE-surface terms above.

## How Convention 10 consumes this folder

Convention 10 (defined in `_design-engine/_meta/CONVENTIONS.md`) requires every OV designed via OVE to declare a **Standalone Sufficiency Posture** against the 47 requirements in `requirements.yaml`. The artifact cascade:

1. **The operator declares** `domain_stakes: low|high` and ≥1 moat-item target in `_meta/posture.yaml` at the OV root (or `posture-deferred.yaml` at the OV root to opt out with a horizon date).
2. **Each requirement gets a disposition** in `posture.yaml`: `met` / `partial` / `n-a` / `deferred` with an evidence pointer.
3. **`standalone-sufficiency-posture.md`** at the OV root presents an operator-facing one-pager rendered from `posture.yaml`.
4. **`_meta/vetting-rubric-filled.md`** at the OV root renders the substrate's `vetting-rubric.md` scorecard with the OV's actual scores, weighted total, gating-rule veto, and verdict band.
5. **C14 validator** (`_design-engine/_meta/validate.py`) checks the 4 artifacts and dispositions against gate requirements per declared `domain_stakes`.

The substrate's `build-standard.md` and `vetting-rubric.md` provide the *template structure* the per-OV `standalone-sufficiency-posture.md` and `vetting-rubric-filled.md` follow; the substrate's `requirements.yaml` provides the canonical REQ-ID list each posture entry references.

## Revision history

| Revision | OVE version | Date | Change |
|---|---|---|---|
| 1.2 | v2.2.0 | 2026-06-14 | Initial OVE vendoring. Spec at rev 1.2: 47 requirements, 13 categories, REQ-J4 (Value Attribution) added, interactive-surface clause folded into REQ-C1. |
