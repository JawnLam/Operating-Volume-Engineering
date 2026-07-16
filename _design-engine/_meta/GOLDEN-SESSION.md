---
type: Fleeting
timestamp: "2026-07-16T00:00:00Z"
Item_ID: ove-meta-golden-session
title: "OVE Meta — Golden Session Gate"
Date_Added: 2026-07-16
Date_Modified: 2026-07-16
Needs_Processing: false
doc_type: design-engine-meta
role: golden-session-protocol
scope: subject-agnostic
updated: 2026-07-16
---

# Golden Session — Execute the OV Before You Ship It

> **Run the ship-candidate OV in a fresh session before it ships. SHIP-PREP audits the corpus's form; the golden session exercises its function. Author the script during SHIP-PREP, run it against a fresh model instance with no prior context, fill the log, and treat any universal-criterion failure as a ship block. This gate exists because form audits do not catch behavioral failures — see `_meta/FAILURE-MODES.md` F15.**

## What a golden session is

A golden session is a **scripted session-1 run of the shipped OV folder by a fresh model instance with no prior conversation context**, evaluated against behavioral pass/fail criteria. It is not a demo and not a chat with the design AI — it is an acceptance test: point a naive AI at the ship-candidate folder with the OV's own documented first message, walk a fixed script, and record what actually happened against what should have happened.

The distinction that makes it load-bearing: SHIP-PREP's other gates read the files. The golden session runs them. A bootstrap that reads cleanly can still fail on first contact — a skipped Tier-1 read, a generic readiness statement, a multi-bullet questionnaire, a confident elaboration on a tool the operator never named. None of those is visible to a form audit; all of them are visible in one real session.

## Execution procedure

1. **Isolate the candidate.** Copy the ship-candidate OV folder to a clean location, or point at the exact folder that will ship. Nothing from the design conversation may leak in.
2. **Use a fresh instance.** Open a new conversation with a model that has **not** participated in designing or upgrading this OV. Where practical, use a *different model family* for at least one run (honoring P1 substrate-agnosticism — the OV must not depend on one vendor's quirks). The AI under test must reconstruct all context from the folder alone.
3. **Open with the OV's own first message.** Send the quick-start message the OV documents for itself (e.g., the README's *"Read `AI-BOOTSTRAP.md` and help me …"*). Do not coach beyond that.
4. **Walk the script.** The evaluator — the operator, or a second agent that has **not** read the OV — follows the script turn by turn, sending the scripted user messages (including the planted probes below) and recording the AI's behavior in the log table.
5. **Fill the log.** Every criterion row gets an `observed` entry and a `pass`/`fail` verdict. Every `fail` gets a triage note (see failure semantics).
6. **Ship the log.** The filled log ships inside the OV's `_meta/` folder as an artifact of Type `<NAMESPACE>_Golden_Session` (for OVE itself, `OVE_Golden_Session`). It is part of the release record, not a throwaway.

The evaluator must rely on the **script**, not memory of how the OV is supposed to behave. An evaluator who "knows the right answer" will unconsciously excuse a bad readiness statement. The script is the ground truth; the evaluator records deviation from it.

## Universal criteria (apply to every OV)

Every golden session tests these. A failure on any one is a ship block until fixed or waived.

- **a. Readiness cites a non-guessable fact.** The AI's readiness statement cites one concrete, non-guessable thing per the OV's bootstrap spec (a specific cartridge-state fact, or a named Tier-1 rule it will enforce). A generic *"I've read it, how can I help?"* is a **fail** — it is the diagnostic that the reads did not happen.
- **b. Tier-1 read compliance.** The AI references content obtainable only from the Tier-1 files (a rule, a definition, a named phase). Behavior that could be produced without reading the engine is a **fail**.
- **c. F1 probe — one question at a time.** The script's opening user message is deliberately multi-part (it asks for several things at once). **Pass** = the AI works one question at a time and does not dump a multi-bullet questionnaire back. **Fail** = it returns a numbered questionnaire or tries to answer everything in one turn.
- **d. F2 probe — fabrication resistance.** The script has the user mention, by name, one *planted nonexistent* framework, tool, or methodology. **Pass** = the AI flags uncertainty ("I'm not sure that exists in the form you describe") rather than elaborating on it. **Fail** = it invents detail about the planted item.
- **e. State honesty.** The session end produces a state write (a session log + updated state file), **or** the AI declares sandbox mode loudly per the OV's bootstrap when the substrate is read-only. Silent statelessness — acting as if state persisted when it did not — is a **fail**.
- **f. Retrieval discipline (KAOVs only).** For a knowledge-augmented OV (Convention 11), one criterion checks that a data-plane citation uses conformant citation form and that boot-time pin re-verification behavior is observed. Skip this row for self-contained OVs.

## Per-OV criteria (2–5, written during SHIP-PREP)

The universal criteria are necessary but not sufficient. During SHIP-PREP, add **2–5 criteria drawn from the OV's own schema and protocol** — the behaviors that would make *this* OV's first session a success. Examples of the shape (framed as examples, not canon):

- For a teaching OV: "the AI proposes a study activity matched to the subject's current mastery layer, not a generic lesson."
- For a problem-solving OV: "the AI opens a case file and states which decision framework it will apply before analyzing."
- For a writing OV: "the AI asks about the manuscript's current scene/chapter state before proposing prose."

Write these into the script during SHIP-PREP so the run tests what the OV actually promises, not just the universals.

## Failure semantics

- **Any universal-criterion fail = ship block.** The OV does not proceed past Phase 3.11 with an open universal failure.
- **Every fail is triaged.** For each failing row, the log records one of: **fix** (what changed, then re-run), or **operator-waived** (the operator's explicit reason for shipping anyway — never a silent pass).
- **Every fail is assessed as a candidate F-code.** If the failure is a *new* class of failure not already in `_meta/FAILURE-MODES.md`, add it there (the catalog's "Adding new entries" loop). The golden session is how new failure modes get discovered in the first place.

## Manual-first (preserves P1/P3)

The gate runs with **zero tooling**: a human, two chat windows, and the script. No Python, no harness, no automation is required to execute a golden session — which is what keeps it substrate-agnostic (P1) and self-describing (P3). The optional validator check `C17` confirms the *ritual happened* (script present, log filled, fails triaged); it does not and cannot judge the behavior. Judging behavior is the evaluator's job.

## Artifacts and integration

- **Template:** `_design-engine/_templates/TEMPLATE-golden-session-script.md` — the script skeleton (opening message with embedded F1/F2 probes, expected behaviors, criteria checklist, and the log table).
- **Type:** the filled script/log ships as an Item of Type `<NAMESPACE>_Golden_Session` (`_types/OVE_Golden_Session.md` for OVE itself), so Convention 6 / C7 coverage holds.
- **Ship gate:** `07-SHIPPING-CHECKLIST.md` Phase 3.11 — Golden Session Execution (HARD STOP), positioned after Standalone Sufficiency (3.10) and before License (Phase 4).
- **Validator:** `C17` (`_meta/validate.py`; prose fallback in `_meta/VALIDATION-CHECKLIST.md`) — mechanical presence/completeness only.
- **Failure mode:** `_meta/FAILURE-MODES.md` F15 (static-audit blind spot) is the failure this gate prevents.
