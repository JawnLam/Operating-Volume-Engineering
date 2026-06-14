---
Item_Prototype: OVE_Design_Decisions
Item_ID: "plc-retrospective-design-decisions"
Title: "Political-Landscape-Cartography — Retrospective Design Decisions"
Date_Added: 2026-06-13
Date_Modified: 2026-06-13
Needs_Processing: false
ove_OV_Name: "Political-Landscape-Cartography"
---

# Political-Landscape-Cartography — Retrospective Design Decisions

> **Append-only log of design decisions, retrospectively reconstructed from PLC v1.0.0's build to show how OVE v2.1's protocol would have shaped the decisions had it existed at design-time. Each entry: date | decision | rationale | alternative considered.**

---

## 2026-06-13 | D-A-1: OV Archetype = practice

Per CQ11 (`_design-engine/BOOTSTRAP-NEW-OV.md` in OVE v2.1). PLC is a **practice OV** — the principal's engagement with political navigation continues indefinitely. Spheres open and close; engagements end (sphere-close for the consultant; role change for the principal); the political work continues.

**Rationale:** The dissertation explicitly defines mastery as recursive — *"sustained competence over many cycles is the only kind of strategic skill that compounds"* (ADAPT foreword). And: *"control the resources that facilitate the ability and opportunity to control more resources"* (dissertation p.226). Both are sustained-operation claims, not destination claims. Forcing PLC into a finite-horizon Q6 frame produces stilted designs (the design conversation invents fake terminal artifacts).

**Alternative considered:** finite-horizon (artificial). Rejected during the actual PLC build at SCHEMA-DESIGN Q6 — the moment the design conversation tried to name a terminal artifact and could not. The honest answer ("there is no terminal artifact") motivated OVE v2.0's Q6 fork as a structural fix.

---

## 2026-06-13 | D-A-2: Q14 Audience Register declared

Per Q14 (`_design-engine/04-SCHEMA-DESIGN.md` in OVE v2.1):

- **Target reader:** COO of $20B+ market-cap public company aspiring to CEO within five years. Secondary: Senior Managing Partners at strategy consultancies running political engagements with C-suite principals.
- **Business / life context:** Active client engagement or principal-self-coaching context where political navigation determines whether strategic moves land.
- **Prose register:** Senior Managing Partner at a global strategy consultancy speaking to a peer — direct, substantive, no flattery, no academic jargon at business dinners.

**Rationale:** Two failure incidents during PLC v1.0's actual build motivated the explicit declaration:

1. The 4R coaching script slipped into academic register ("dissertation-defined set") — caught at REVIEW. Replaced with "Nine specific categories."
2. The 4R docs used "dashboard" as a noun in two places — anchoring a client-expectation PLC did not ship. Caught at REVIEW. Replaced with "conceptual frame," "mental map," "conversational frame."

Both incidents survived pre-v2.0 SHIP-PREP without flagging — they were caught by operator spot-check. v2.0's Q14 declaration + Phase 3.9 Vocabulary Audit gate make the check structural rather than judgment-based.

**Alternative considered:** implicit / undeclared register (the v1.x default). Rejected — the v1.x failure pattern produced the slips above.

---

## 2026-06-13 | D-B-1: Source inventory pattern

Per Convention 9 (`_design-engine/_meta/CONVENTIONS.md` in OVE v2.1) and CQ3 strengthened source-capture. The Lam 2018 Pepperdine dissertation is flagged `Sensitivity: Ship-by-reference (Convention 9)`. Physical PDF stays local in the Methodology Author's working copy; PLC's `.gitignore` excludes the file; a placeholder `.md` at `_frameworks/sources/Lam-2018-Pepperdine.md` directs readers to contact the Methodology Author.

**Rationale:** The dissertation is the Methodology Author's personal academic work. The OV cites it as substrate (specific page numbers, structural elements, theoretical concepts) but does not redistribute it. The Methodology Author retains canonical control.

**Alternative considered:** (a) bundle the dissertation in full — rejected, loses the Methodology Author's retention and creates licensing complexity for the OV; (b) cite without inventory — rejected, vulnerable to F13 (the actual failure pattern during PLC v1.0's build: fabricated "15-step protocol" with false "p.223-224" cite, invented OPC § 16.7 label, four fabricated worked-sphere archetype assignments, wrong dissertation year). v2.0's Phase 3.7 Citation Audit and Phase 3.8 Worked-Example Slot-ID Verification gates structurally prevent (b)'s failure pattern.

---

## 2026-06-13 | D-B-2: Citation Audit gate cleared (retrospectively)

PLC v1.0.0 ships with a clean Citation Audit per the gate that would have been v2.0 Phase 3.7. Every "p.XX" cite traces to the Lam 2018 dissertation at the verified canonical location; every "§ X.Y" cite (OPC § 16, § 17 references) matches the OPC v3.0 JSON source; every named theorist in the Political Warfare Catalogue is verified.

**Rationale:** Multiple historical fabrications during the PLC v1.0 build (the F13 documented recurrence) made the Citation Audit non-negotiable for PLC's ship. The "15-step protocol with p.223-224 cite" fabrication, the "schedule-flexibility for client crisis response" OPC § 16.7 fabrication, and the wrong "2020" dissertation year were all corrected by operator spot-check + rework before ship. v2.0's Phase 3.7 codifies the audit so future practice-archetype OVs don't reinvent the discipline.

**Alternative considered:** ship with `[SOURCE-VERIFICATION-REQUIRED]` placeholders for un-audited cites — rejected, defeats the purpose of shipping; partial-audit-ship-then-patch — rejected, F13 fabrications poison downstream cartridges.

---

## 2026-06-13 | D-B-3: Worked-Example Slot-ID Verification gate cleared

PLC v1.0.0's worked sphere ships with verified slot-ID assignments: Sam → § 13.1.1.8 `incumbent_defender`; Carol → § 13.1.2.3 `covert_operator`; Robert → § 2.2.1.3 `the_kingmaker`; Elena → § 2.2.1.8 `the_technician`. Each carries a one-line source-justification.

**Rationale:** All four assignments were originally fabricated in the actual PLC v1.0 build (session-inferred from character names rather than verified against the canonical schema). The fabrications surfaced when the cited § IDs were checked. Correction was substantial rework. v2.0's Phase 3.8 codifies the verification so future OVs with worked-example slot-ID mappings carry inline source-justifications from the start.

---

## 2026-06-13 | D-C-1: Vocabulary Audit gate cleared

Two specific replacements:

1. **`dashboard` → `conceptual frame` / `mental map` / `conversational frame`** in 4R coaching docs. The 4R is a baseball-diamond mental model (Resources / Results / Rationale / Relationship), not a visual artifact. "Dashboard" anchored a deliverable-promise the OV did not ship — clients would have asked "where's my dashboard?" upon seeing the term. Replacement preserves the conceptual function while not promising an artifact.
2. **`dissertation-defined set` → `Nine specific categories`** in the 4R coaching script's "Resources" section. The script's declared register is Senior Managing Partner voice. Academic phrasing ("dissertation-defined") is the prototypical register violation — *no one wants to hear academic terms at a business dinner.*

**Rationale:** v2.0's Phase 3.9 Vocabulary Audit was specifically motivated by these two incidents. The audit sweeps for deliverable-promise nouns (dashboard, scorecard, report, framework, tool, playbook) and audience-register violations against the declared `ove_Audience_Prose_Register`.

---

## 2026-06-13 | D-D-1: LICENSE = restrictive template

Per `_design-engine/_templates/TEMPLATE-LICENSE-restrictive.md` (the template codified from PLC v1.0's LICENSE after multiple rounds of refinement during the actual build).

Key sections:

- **§ 1 Personal Evaluation** — 14-day window with 6 limits (application-prohibited, no-sphere-creation, no-reference-during-engagement, no-retention-after-expiration, burden-of-distinction, no-derivative-works).
- **§ 2 Principal Self-Coaching ≠ personal evaluation under any circumstance.** Closes the loophole where a principal might claim "self-coaching is personal evaluation." It is not. Authorized self-coaching is licensed application governed by separate written authorization.
- **§ 3 Commercial use, redistribution, derivative works** — require explicit written authorization.
- **§ 4 Academic Archive Carve-Out** — resolves the academic fair-use friction with delete-or-destroy obligations. A scholar who cited the OV's substrate in published scholarship can preserve the archive beyond the 14-day window subject to four conditions (time-bound, archival-use-only, notification-on-request, lapses on withdrawal).
- **§ 5 Sensitive Source Materials** — acknowledges Convention 9; access to sensitive substrate is governed separately, not by this LICENSE.

**Rationale:** PLC is the Methodology Author's life's work codification. CC-BY 4.0 was rejected — too permissive given the substrate's value. MIT / Apache were rejected — wrong shape. The restrictive template captures the maximum-control-with-evaluation-pathway posture the Methodology Author wanted.

**Alternative considered:** all-rights-reserved with NO evaluation pathway — rejected, prevents legitimate peer review and scholarly citation. The 14-day window with limits + Academic Archive Carve-Out balances control with the legitimate use cases.

---

## 2026-06-13 | D-D-2: Sensitive source materials pattern applied

Per Convention 9. The Lam 2018 dissertation PDF is excluded from PLC's GitHub repository via `.gitignore` (`_frameworks/sources/Lam-2018-Pepperdine.pdf`); a placeholder `.md` at `_frameworks/sources/Lam-2018-Pepperdine.md` ships in its place, directing readers to contact the Methodology Author. Post-push verification confirmed the PDF's absence from the remote (404 on `gh api repos/JawnLam/Political-Landscape-Cartography/contents/_frameworks/sources/Lam-2018-Pepperdine.pdf`).

**Rationale:** Defense-in-depth. Physical exclusion + `.gitignore` + post-push 404 verification. Either alone is brittle (physical-only fails if the file is later re-added; gitignore-only fails if `.gitignore` is misconfigured).

---

## 2026-06-13 | D-D-3: Public-release decision deferred until IP-attorney review

PLC v1.0.0 ships to a **private** GitHub repository. Public-release decision is deferred until an IP attorney reviews the LICENSE language against the Methodology Author's jurisdiction.

**Rationale:** The restrictive LICENSE template (`_design-engine/_templates/TEMPLATE-LICENSE-restrictive.md`) explicitly flags IP-attorney review as required before public release. The OV ships to private GitHub during the interim; public flip is one command (`gh repo edit --visibility public`) after legal sign-off.

**Alternative considered:** public release at v1.0.0 without legal review — rejected, the restrictive LICENSE's enforceability has not been validated against the jurisdiction.

---

## Notes

This decisions log was authored retrospectively after PLC v1.0.0 shipped and OVE v2.1 was being prepared. The decisions documented above were the *actual* decisions made during the PLC v1.0 build — but several of them were made *ad hoc* during the build because OVE v1.x's protocol did not have the structural support (CQ11, Q14, Convention 9, Phase 3.7 / 3.8 / 3.9). v2.0 codified the patterns; v2.1 ships this retrospective as the canonical demonstration.

For future practice-archetype OVs designed via OVE v2.1+: the decisions above should be made *during* SCHEMA-DESIGN and INTERVIEW, not retrospectively. If a design conversation finds itself reinventing one of these patterns, the OV designer has probably skipped a CQ or Q step that v2.0 codified.
