---
type: Fleeting
timestamp: "2026-07-16T00:00:00Z"
Item_ID: ove-meta-traceability
title: "OVE Meta — Traceability Matrix"
Date_Added: 2026-07-16
Date_Modified: 2026-07-16
Needs_Processing: false
doc_type: design-engine-meta
role: traceability-matrix
scope: subject-agnostic
updated: 2026-07-16
---

# Traceability Matrix

> **Walk this table, not your memory, when auditing OVE or verifying that a principle has teeth. Each row traces one principle, convention, or discipline through the mechanism that enforces it, the validator check that gates it, and the failure mode it prevents. When you add or amend any `P`, `F`, `C`, or `Convention`, update this file in the same change (Convention 13) — an ID that lives in a defining file but not here is an untraced requirement, which is exactly the drift this matrix exists to kill.**

## How to read a row

- **Principle / Convention / Discipline** — the requirement being traced (a `P`-code, a numbered `Convention`, or a named cross-cutting discipline that carries an `F`-code but no `P`-code).
- **Enforcement mechanism** — the protocol step, template, ship phase, or read-tier rule that makes the requirement operative. "Manual-only" means a human or a reading AI enforces it; there is no mechanical check.
- **Validator check** — the `C`-check in `validate.py` (mirrored in `VALIDATION-CHECKLIST.md`) that gates it, or `manual-only`.
- **Failure mode(s) prevented** — the `F`-code(s) this chain guards against, or `—` if the requirement is constructive rather than failure-driven.
- **Notes** — version, cross-references, caveats.

Every ID defined in the engine's authority files (`02-DESIGN-PRINCIPLES.md`, `_meta/CONVENTIONS.md`, `_meta/FAILURE-MODES.md`, `_meta/validate.py`) appears at least once below. The trailing **Orphans** section lists any requirement that reaches this file without a full chain, each with a disposition. An empty orphan section is the goal; a *silent* one — a gap that exists but isn't listed — is a Convention 13 violation.

## Principles (P1–P13)

| Principle / Convention / Discipline | Enforcement mechanism | Validator check | Failure mode(s) prevented | Notes |
|---|---|---|---|---|
| **P1 — Substrate-agnostic** | Markdown-only + Python-free discipline (`00-START-HERE.md`); audit-mode P1 check (`03-DESIGN-PROTOCOL.md` §4); tooling-posture doctrine (Convention preamble / README) | manual-only | — | Not mechanically detectable; audited by reading. |
| **P2 — Statefulness through files** | Cartridge backbone + WRITE-state phase (`06-STATE-PERSISTENCE.md`, `03-DESIGN-PROTOCOL.md`); Convention 10 REQ-B1 | C1, C2 | F12 | State files present + frontmatter present are the mechanical proxies. |
| **P3 — Self-describing folder** | `AI-BOOTSTRAP.md` bootstrap; Convention 7 (self-contained install); Convention 6 (`_types/` travel with the OV) | manual-only | — | Portability is audited, not measured. |
| **P4 — Cartridge specialization** | Engine subject-agnostic discipline; audit-mode P4 check (`03-DESIGN-PROTOCOL.md` §4) | manual-only | F4 | Domain bleed is caught by reading, not grep. |
| **P5 — Conversational interface** | Audit-mode P5 check; no-required-syntax rule (`01-WHAT-IS-AN-OV.md`) | manual-only | — | — |
| **P6 — Multi-session by design** | Bootstrap works on session N (`00-START-HERE.md`); Open Threads hand-off (`03-DESIGN-PROTOCOL.md`) | manual-only | F12 | — |
| **P7 — Identity operator-provided** | Placeholder templates; personal-data scrub (`07-SHIPPING-CHECKLIST.md` Phase 3) | C3, C4 | F3 | Highest-embarrassment class; C3 leak-scan + C4 attribution-match. |
| **P8 — Fabrication discipline** | Source inventory CQ3 (`BOOTSTRAP-NEW-OV.md`); ARTIFACT-DRAFT gate (Step 4.5); Citation Audit (Phase 3.7) + Slot-ID Verify (Phase 3.8) | C11, C12 | F2, F13 | Structural, not honor-based, since v2.0. |
| **P9 — Self-similarity** | Self-similarity check during SCHEMA-DESIGN Q-walk (`04-SCHEMA-DESIGN.md`) | manual-only | F10 | Diagnostic signal, not a gate. |
| **P10 — One question at a time** | Triple-redundant directive (`BOOTSTRAP-NEW-OV.md`, `03-DESIGN-PROTOCOL.md`, `00-START-HERE.md`) | manual-only | F1 | Redundancy is deliberate — recurrent failure. |
| **P11 — Propose-don't-decide** | Decision-algorithm Step 8 (propose + wait) (`03-DESIGN-PROTOCOL.md`) | manual-only | F11 | — |
| **P12 — Write before you end** | Session-end quality gates (`03-DESIGN-PROTOCOL.md`) | manual-only | F12 | See Orphans O-2: no mechanical proof a log was written. |
| **P13 — Schema-freeze after ship** | Schema policy (`VERSION.md`); major-bump rule (`CONTRIBUTING.md` §2) | manual-only | — | — |

## Conventions (1–11, 13)

| Principle / Convention / Discipline | Enforcement mechanism | Validator check | Failure mode(s) prevented | Notes |
|---|---|---|---|---|
| **Convention 1 — Universal Core fields (OKF v0.1)** | Every template carries the core; REVIEW frontmatter checklist (`_meta/CONVENTIONS.md`) | C2 | — | OKF-native `type`/`title`/`timestamp` since v2.4.0. |
| **Convention 2 — Case conventions** | REVIEW frontmatter checklist | manual-only | — | Lowercase OKF-interop exception documented in-convention. |
| **Convention 3 — One namespace per OV** | Namespace CQ (`BOOTSTRAP-NEW-OV.md`) triggers the cascade | manual-only | — | — |
| **Convention 4 — Every Type gets its own `type` value** | SCHEMA-DESIGN Type list; `_types/` materialization | C7 | — | — |
| **Convention 5 — Schema-of-namespace declaration** | `_meta/SCHEMA-OF-SCHEMAS.md` per OV | manual-only | F5 | Lifts structure out of prose. |
| **Convention 6 — Each OV ships its own `_types/`** | ARTIFACT-DRAFT materialization; `_types/` coverage gate (Phase 3.5) | C7 | — | Makes the OV portable without a central registry. |
| **Convention 7 — Install-and-update pattern** | `INSTALL.md` / `OPERATOR-GUIDE.md` / `UPDATE-PROMPT.md`; readiness gate (Phase 3.6) | C10 | — | — |
| **Convention 8 — Engine vs operator-content boundary** | Four-zone declaration (`CONTRIBUTING.md`); readiness gate (Phase 3.6) | C8, C9 | — | Zones documented + `.gitignore` sanity. |
| **Convention 9 — Sensitive source materials (ship-by-reference)** | Sensitivity flag in `_source-inventory.md`; `.gitignore` exclusion + placeholder + post-push 404 verify | manual-only | — | Defense-in-depth; partially observed via C11 inventory. |
| **Convention 10 — Standalone Sufficiency Posture** | POSTURE-DECLARATION activity; SCHEMA-DESIGN Q15; readiness gate (Phase 3.10) | C14 | — | Enforces the two master tests + disowns the 10 traps. |
| **Convention 11 — Knowledge-Augmented OVs (OKF data plane)** | KNOWLEDGE-MOUNT (Step 4.6); boot-time re-verification (`08-KNOWLEDGE-RETRIEVAL.md` Rule 4) | C15, C16 | F14 | Vendored, pinned, OKF-conformant mounts. |
| **Convention 13 — Traceability maintenance** | This file updated in the same change as any `P`/`F`/`C`/`Convention` edit | C18 | — | Prevents the untraced-requirement / silent-orphan drift. |
| **Convention 14 — Grows-Through-Use Zone** | Declared zone (`_portfolio/`) in manifest + `CONTRIBUTING.md`; seeded at release; operator-appended; merge-not-clobber on `git pull` | C19 | — | Fifth content zone for use-grown catalogs. First instance: Baseplate's portfolio failure catalog (v2.7.0). |

## Cross-cutting disciplines (F-codes / C-checks without a numbered P or Convention)

| Principle / Convention / Discipline | Enforcement mechanism | Validator check | Failure mode(s) prevented | Notes |
|---|---|---|---|---|
| **Bootstrap ↔ engine mirror** | Root file thin-pointer; engine canonical (`AI-BOOTSTRAP.md` ↔ `00-START-HERE.md`); release-time agreement | C6 | F6 | Tier-1 file lists must match; engine wins. |
| **Cross-reference integrity** | REVIEW link-resolution pass | C5 | F2 (fabricated file refs) | See Orphans O-1: enforced but not stated as a first-class principle. |
| **Writing style (AI is the reader)** | Opening-directive scan in REVIEW (`05-WRITING-FOR-AI.md`) | manual-only | F7 | Style is not mechanically detectable. |
| **Activity ordering (SCHEMA → CARTRIDGE → DRAFT)** | Decision-algorithm ordering (`03-DESIGN-PROTOCOL.md`) | manual-only | F8 | Prevents drafting before deciding. |
| **OV form-fit check** | CQ6 (`BOOTSTRAP-NEW-OV.md`); F9 diagnostic during design | manual-only | F9 | "Is this actually an OV?" — surfaced, operator decides. |
| **Sandbox-mode honesty** | Phase 0 writability check; sandbox announcement in readiness statement (`00-START-HERE.md`) | manual-only | F12 | Read-only substrate must be declared, not absorbed. |
| **Voice / client-promise discipline** | Vocabulary Audit (Phase 3.9); `ove_Audience_Prose_Register` | C13 | — | Deliverable-promise nouns + register violations. |
| **Golden-session execution** | Golden Session (`_meta/GOLDEN-SESSION.md`); ship gate (Phase 3.11) | C17 | F15 | Executes the OV before ship, not just audits its form. Added v2.6.0 (CR-1). |

## Orphans

Goal: empty. Each entry is a requirement that reaches this matrix without a complete `principle → enforcement → check → failure` chain, or an ID reserved but not yet enforced. Disposition is one of `gap — needs enforcement`, `gap — needs principle`, or `intentional (reason)`.

- **O-1 · Cross-reference integrity has a check (C5) but no first-class principle.** Link-resolution is enforced by C5 and implied by F2/P8, but "every cross-reference must resolve" is not stated as its own `P`-code. Disposition: **gap — needs principle** (low priority; C5 already gates it mechanically).
- **O-2 · P12 (write before you end) has no mechanical check.** The session-end quality gates are manual; nothing in `validate.py` proves a session actually wrote its log + state. Disposition: **gap — needs enforcement** (a `C`-check that a session directory grew a log file could close it; v-next backlog).
- **O-3 · Convention 12 (Registry Sync) is reserved but not shipped.** The design note (`_proposals/Convention-12-Registry-Sync-Design-Note.md`) was trimmed from the distribution in HEAD; the slot is named only in front-door/historical docs, not in `CONVENTIONS.md`, so it is not swept by C18. Disposition: **intentional (reserved — Registry Sync; see `_upgrade/QUESTIONS.md` Q1)**.
- **O-4 · Master tests + Traps are enforced without their own IDs.** The Displacement and Absorption tests and Traps 1–10 (`02-DESIGN-PRINCIPLES.md`) carry no `P`/`F` code; they are enforced through Convention 10 → C14. Disposition: **intentional (enforced via Convention 10; not ID-swept because they match no `P`/`F`/`C`/`Convention` pattern)**.

**Gap count reported to operator: 2** (O-1, O-2). Both are low-priority v-next backlog, not ship blockers. O-3 and O-4 are intentional.

## Maintenance (Convention 13)

This matrix is only as trustworthy as its currency. Convention 13 (`_meta/CONVENTIONS.md`) makes updating it non-optional: **any change that adds or amends a `P`-code, `F`-code, `C`-check, or `Convention` must update this file in the same change**, and must re-evaluate the Orphans section. Validator check **C18** (`validate.py`; prose fallback in `VALIDATION-CHECKLIST.md`) mechanically confirms that every ID defined in the authority files appears here and that the Orphans section exists — it verifies the *ritual happened*, not that the chains are correct. Verifying the chains live is audit-mode's job (`03-DESIGN-PROTOCOL.md` §4).
