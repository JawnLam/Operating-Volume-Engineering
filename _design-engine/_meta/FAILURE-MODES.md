---
type: Fleeting
timestamp: "2026-06-06T00:00:00Z"
Item_ID: ove-meta-failure-modes
title: "OVE Meta — Failure Modes"
Date_Added: 2026-06-01
Date_Modified: 2026-06-06
Needs_Processing: false
doc_type: design-engine
role: failure-catalog
scope: subject-agnostic
updated: 2026-06-01
---

# Failure Modes — Canonical Catalog

> **Documented failure modes that OV design sessions are known to produce. Each entry: name, trigger pattern, why it matters, fix, prevention. The AI should guard against every entry actively.**

## F1 — Multi-bullet questionnaire

**Trigger pattern:** When opening a clarifying interview (CQ1–CQ10 in `BOOTSTRAP-NEW-OV.md`), the AI's natural failure is to dump all the questions in one message as a numbered list.

**Why it matters:** Bulk questions get bulk answers. The user fills them in like a form, and you lose the nuance that comes from probing one answer at a time. The resulting design is generic.

**Fix:** Stop the conversation. Reset: *"I'll ask you one question at a time, conversationally. Probe your answers. We'll get to the others as we go."*

**Prevention:** The protocol in `BOOTSTRAP-NEW-OV.md` and `03-DESIGN-PROTOCOL.md` both explicitly state "one question at a time." Triple-redundant in the engine because this failure recurs.

## F2 — Fabrication of tools, frameworks, people, facts

**Trigger pattern:** When designing the OV needs a reference (a methodology to extend, a framework to integrate, a thinker to cite), the AI invents plausible-sounding names that aren't real.

**Why it matters:** The user discovers the fabrication later — sometimes by trying to look up the cited thing. Trust collapses. The OV gets poisoned with false references that have to be ripped out.

**Fix:** When you're not certain something exists, say so. Acceptable: *"I'm not sure that framework exists in the form you describe. Can you confirm, or should we treat it as something to verify before locking?"*

**Prevention:** `05-WRITING-FOR-AI.md` codifies the fabrication discipline. Default to "I don't know" over "I'll guess."

## F3 — Identity inference from indirect signals (recurrence)

**Trigger pattern:** When the AI needs to put a name into a shipped artifact (LICENSE, README attribution, signature blocks), it parses a username string, file path, or git config into a guessed real name and writes the guess as if it were fact.

**Why it matters:** This is one of the most embarrassing categories of error because it's visible — it gets into shippable files. Documented historical recurrence: the username `jawnlam` was parsed as "John Lam" in multiple deliverables. Operator corrections happen with increasing force each time.

**Fix:** Use a placeholder (`[USER_NAME]`, `<author>`, etc.) until the user provides their name in their own words. Flag the placeholder as a TODO before shipping.

**Prevention:** `02-DESIGN-PRINCIPLES.md` P7 makes this a load-bearing principle. Every template with a name field uses a placeholder.

## F4 — Engine drift into domain specifics

**Trigger pattern:** While writing an engine file, the AI slips in a domain-specific example as if it were canonical: "*for cybernetics, you should…*" instead of "*for any conceptual-thinker subject, you should…*".

**Why it matters:** Engine files must be subject-agnostic (Layer 1, per `_meta/SCHEMA-OF-SCHEMAS.md`). Domain bleed pollutes the engine and makes the OV harder to reuse.

**Fix:** Refactor. Move domain-specific guidance to a cartridge's `_schema.md` or to a worked-example cartridge. Keep the engine general.

**Prevention:** When citing examples in an engine file, frame them as "*for example*" or "*in OV X, …*" — never as the canonical case. Use multiple examples to make the abstraction explicit.

## F5 — Schema implicit in prose

**Trigger pattern:** A section of engine prose *implies* a schema constraint without making it explicit. (E.g., "the session log should include Items-engaged" without that being listed as a required field in the schema.)

**Why it matters:** Implicit schema produces drift. Different sessions implement the constraint differently. The schema validator can't catch the violation.

**Fix:** Lift any structural rule from prose to the schema document. The schema is the source of truth for structure.

**Prevention:** During REVIEW sessions, check: every rule the AI must enforce should appear in `_meta/SCHEMA-OF-SCHEMAS.md` or the OV's `_schema.md`.

## F6 — Root mirror / engine canonical drift

**Trigger pattern:** OVs that maintain both a root-level `AI-BOOTSTRAP.md` and an `00-START-HERE.md` inside the engine can let the two drift out of sync over time.

**Why it matters:** AI behavior depends on whichever file the bootstrap loads. If they say different things, sessions become inconsistent.

**Fix:** Decide which is canonical. SOLVE-eX uses the pattern "root mirrors engine; engine wins on divergence." LLL uses the pattern "root file is a thin pointer; engine file is canonical." Both work; pick one and document it.

**Prevention:** Add a check at every release: do the two files agree on the substantive content?

## F7 — Writing for human readers when AI is the audience

**Trigger pattern:** Engine prose opens with meta-commentary: *"In this section we will discuss…"* or *"This document covers…"*. That's textbook prose for a human reader, not operational instructions for an AI.

**Why it matters:** The AI doesn't need to know what's coming. It needs to know what to do. Meta-prose burns context-window space without producing behavior.

**Fix:** Cut all meta-prose. Open with the operational directive.

**Prevention:** During REVIEW, scan each section's opening. If the first sentence is meta, delete and rewrite.

## F8 — Drafting before deciding

**Trigger pattern:** The AI starts drafting `AI-BOOTSTRAP.md` for the new OV before the schema is locked. Drafts get thrown away when the schema changes.

**Why it matters:** Wasted work, sometimes wasted multiple times. Each schema change cascades into artifact rewrites.

**Fix:** Stop drafting. Return to SCHEMA-DESIGN or CARTRIDGE-SHAPE. Don't draft artifacts until both are locked.

**Prevention:** The decision algorithm in `03-DESIGN-PROTOCOL.md` orders activities deliberately: SCHEMA-DESIGN before CARTRIDGE-SHAPE before ARTIFACT-DRAFT.

## F9 — OV form-fit failure (the thing isn't an OV)

**Trigger pattern:** Late in design, you realize the thing being designed doesn't really need multi-session state, doesn't really need cartridges, doesn't really need substrate-agnosticism. It would be better served as a Custom GPT, a skill, or a prompt pack.

**Why it matters:** Sunk-cost fallacy. The user may have invested significant design effort. Continuing produces a heavy OV for what should be a light artifact.

**Fix:** Surface the diagnostic. *"This may not be an OV. Here are three reasons why, and here's what I'd suggest instead."* The user decides.

**Prevention:** CQ6 in `BOOTSTRAP-NEW-OV.md` is specifically the OV-form check. Take it seriously the first time.

## F10 — Self-similarity violation

**Trigger pattern:** While walking Q1–Q13 from `04-SCHEMA-DESIGN.md`, the AI realizes the proposed design can't be expressed in OVE's own design protocol.

**Why it matters:** Either OVE has a gap or the proposed design has a gap. Both are worth flagging.

**Fix:** Stop. Investigate which is true:
- Is the proposed design actually an OV? (Maybe not.)
- Is OVE missing a feature this OV needs? (Maybe — flag as v1.x backlog.)
- Is the design wrong? (Maybe — go back to schema design.)

**Prevention:** P9 in `02-DESIGN-PRINCIPLES.md` makes self-similarity an explicit check during schema design.

## F11 — Premature lock

**Trigger pattern:** The AI locks a decision in `_design-decisions.md` after one round of conversation, without giving the user a chance to push back or explore alternatives.

**Why it matters:** Lock-in produces brittle designs. The user might have a different intuition that the AI's proposal didn't surface.

**Fix:** Treat the first proposal as a draft. Surface the alternative. Wait for explicit user confirmation before recording the decision as locked.

**Prevention:** The propose-don't-decide principle (P11). Every decision-recording line in `_design-decisions.md` should be the result of an explicit user "yes, lock this."

## F12 — Sandbox-mode misuse

**Trigger pattern:** In a sandbox environment (no file write), the AI continues acting as if state is being persisted to disk.

**Why it matters:** State is lost at session end. The user thinks work is being saved; it isn't.

**Fix:** At Phase 0 pre-flight, detect read-only mode and declare sandbox explicitly. All state lives inline in the conversation; user is told this.

**Prevention:** Phase 0 environment checks in `AI-BOOTSTRAP.md` include writability verification.

## F13 — Source-grounding skipped (F2 vector specific to source-grounded OVs)

**Trigger pattern:** The OV cites external source material (a dissertation, a published methodology, a field manual, a theorist's body of work) but the AI drafts artifacts from session-memory paraphrase of the source rather than verbatim quotes with verified page citations. Specific cite-prone failure cases:

- Citing "p. XX" of a source the AI has not actually located in its working environment
- Inventing structural counts ("the framework has N steps") not present in the source
- Misattributing concepts (assigning a label or category that doesn't exist in the canonical text)
- Hallucinating worked-example mappings ("character X → § Y.Z.W `<slot-id>`") without source-text verification
- Misstating publication metadata (wrong year, wrong publisher) of cited works

**Why it matters:** This is the F2 vector specifically triggered by source-grounded OVs. Once a fabricated citation lands in the shipped OV, every downstream cartridge inherits it. The operator discovers the fabrication later — often when trying to look up the cited page or verify a structural count — and trust collapses. Documented historical recurrence: the v1.0 build of Political Landscape Cartography (an OV citing a 294-page dissertation as substrate) hit this failure mode at high frequency — fabricated "N-step protocol" with false "p.XX-YY" cite, invented sub-section labels, multiple fabricated worked-example archetype assignments, wrong publication year. Most fabrications survived the SHIP-PREP gauntlet and only surfaced via operator spot-check, after substantial rework.

**Fix:** When you discover the source is not actually accessible in your working environment, **stop**. Don't paraphrase from memory. Either find the canonical source, ask the operator for it, or flag the cite as `[SOURCE-VERIFICATION-REQUIRED]` and route the question to the operator. Do not ship the cite as fact.

**Prevention:**

- CQ3 (`BOOTSTRAP-NEW-OV.md`) structurally captures each cited source with canonical location, page count, full-vs-excerpt status, and sensitivity.
- ARTIFACT-DRAFT (`03-DESIGN-PROTOCOL.md` Step 4.5) blocks until `_source-inventory.md` has every cited source's canonical location filled AND the AI has acknowledged reading the canonical source with a one-line per-source summary.
- SHIP-PREP Phase 3.7 (`07-SHIPPING-CHECKLIST.md`) — Citation Audit — every "p.XX / § X.Y / named theorist / verbatim quote" in shippable content is verified against source; unverified cite = ship block.
- SHIP-PREP Phase 3.8 — Worked-Example Slot-ID Verification — every worked-example reference to a Prototype slot ID carries a one-line source-justification; unjustified assignment = ship block.
- Validator checks C11 (source-inventory presence + completeness) and C12 (citation-audit-log presence) enforce the gates programmatically.

## F14 — Stale or non-conformant data plane (knowledge-augmented OVs)

**Trigger pattern:** A knowledge-augmented OV (Convention 11) mounts an OKF bundle and the AI treats a runtime citation as if it were a ship-time-verified fact. Two specific cases:

- **Staleness.** A cited concept's content changed after the bundle was vetted (the vendored bundle was re-vendored to a newer version, or the concept's `timestamp` advanced past the recorded `pin`), but the AI reuses the old claim because the citation path still resolves. The link proves *provenance*, not *currency*.
- **Non-conformance.** The mounted bundle drifts from OKF v0.1 — a concept loses its required `type`, citations get written as the `[Source: …]` pseudo-tag, or links use leading-slash paths that break GitHub rendering — and the data plane silently stops being interoperable with the wider OKF ecosystem.

**Why it matters:** F14 is the F13 vector relocated to the data plane. F13's guarantee is "verified against canonical source at ship." A mounted OKF bundle is external-in-origin and mutable by design (OKF concepts carry a `timestamp` and a `log.md` *because* they change), and OKF itself is v0.1 Draft and may make breaking changes. A KAOV that cites the data plane without re-verifying inherits exactly the trust-collapse F13 was built to prevent — now harder to spot because the citation looks valid.

**Fix:** When boot-time re-verification detects drift, **stop reusing the affected claims**. Re-read the current concept, re-confirm the claim against it, and surface the change to the operator before updating the `pin`. If a mount has fallen out of OKF conformance, repair the bundle (or re-vendor a conformant version) before drafting from it. Never emit `[Source: …]` or leading-slash links.

**Prevention:**

- KNOWLEDGE-MOUNT (`03-DESIGN-PROTOCOL.md` Step 4.6) blocks ARTIFACT-DRAFT until every declared mount is vendored, OKF-conformant, and pinned.
- The Rule 4 boot-time re-verification in `08-KNOWLEDGE-RETRIEVAL.md` runs every session for a KAOV: diff each depended-on concept's `timestamp` / git SHA / `okf_version` against the recorded `pin`; re-confirm on drift.
- Convention 11 requires `ship_disposition: vendored`, so the data plane is version-pinned and ships with the OV rather than floating as a live external dependency.
- Validator checks C15 (mount resolution + OKF v0.1 §9 conformance + pin present) and C16 (citation form — no `[Source: …]`, file-relative links into declared mounts only) enforce the gates programmatically.

## Adding new entries

When a new failure mode surfaces in real use, add it here with:

- Name (Fn)
- Trigger pattern
- Why it matters
- Fix
- Prevention

The catalog grows; the engine references it; the failure recurs less.
