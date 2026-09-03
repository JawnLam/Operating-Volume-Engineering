---
type: Fleeting
timestamp: "2026-08-28T00:00:00Z"
Item_ID: ove-meta-specialists
title: "OVE Meta — Specialist Registry & Detection Triggers"
Date_Added: 2026-08-28
Date_Modified: 2026-08-28
Needs_Processing: false
doc_type: design-engine-meta
role: specialist-registry
scope: subject-agnostic
updated: 2026-08-28
---

# Specialist Registry — who OVE delegates to, and how it knows when

> **OVE designs institutions; it does not design every artifact an institution contains.** Some parts of a host OV's work belong to a different form with a different engineering discipline, owned by a **specialist OV**. Under Convention 16, OVE's knowledge of each specialist's craft is deliberately restricted to two things: the **detection trigger** (recognizing that the specialist's class of need is present) and the **requisition interface** (specifying the need without designing the solution). This file is the registry of specialists and the canonical home of their detection triggers. It is loaded during SCHEMA-DESIGN (the Q7 sweep), during BOOTSTRAP-NEW-OV's specialist sweep, during Audit Mode, and at SHIP-PREP Phase 3.13.

## Registry entry format

Each specialist entry declares:

- **Specialist OV** — name and, when it exists, location.
- **Sub-artifact class** — what it builds inside host OVs.
- **Status** — `planned` (requisitions bank per Convention 16 until it exists) or `exists` (requisitions route to a design engagement of that OV).
- **Detection trigger** — the complete criterion the designing/auditing AI applies. This is the *only* craft knowledge OVE holds about the specialist's domain.
- **Requisition notes** — anything class-specific the requisition template needs beyond its general fields.
- **Mount convention** — where fulfilled sub-artifacts live in a host OV and how they are versioned.

The sweep discipline, common to all entries: every candidate activity or deliverable surfaced during design is classified **`ov-native` | `requisition` | `hybrid-split`** against every registered trigger, and the classification — including every *negative* one — is logged in the engagement's design record. A shipped pipeline-shaped activity must always be a *decided* thing, never a default.

---

## Specialist 1 — Interpretable Context Methodology Engineering (ICME)

- **Specialist OV:** Interpretable-Context-Methodology-Engineering. **Status: `planned`** — not yet built. All detection hits requisition-and-bank: write the requisition, declare the placeholder mount, ship the host functional, record what capability is deferred.
- **Sub-artifact class:** ICM workspaces — staged, terminating, filesystem-orchestrated pipelines in the sense of Van Clief & McDermott (the factory form: numbered stages, stage contracts, run-scoped state, deliverable per run).
- **Mount convention:** fulfilled ICMs are vendored under the host OV's `_pipelines/<pipeline-name>/`, declared in the host manifest's `Sub_Artifact_Mounts`, pinned to an ICME fulfillment version, and updated only by ICME re-engagement — never hand-edited by the host's operator or AI (Convention 16).

### Detection trigger — when a piece of a host OV's work wants an ICM

Apply this to every candidate activity, deliverable, or recurring procedure surfaced during design (and, advisorily, during audit). The criterion is domain-blind: it tests the *shape* of the work, never its subject.

**The factory signature — all five structural marks must hold:**

1. **Terminating.** The work is a *run* with a defined deliverable; done-ness is structural (the output exists), not judged. If completion requires a judgment call, the mark fails.
2. **Spec-completable in advance.** Inputs, steps, and pass conditions can be enumerated before the run starts. The run consumes *parameter values*; it never needs to discover mid-run what it should have asked for.
3. **Linear or near-linear.** Fixed stage order; no dispatch on case state, no reentry into an earlier stage as a normal path, branching at most trivial (a skip, not a router).
4. **Consistency-preferred.** Run N should resemble run 1. Learning from prior runs' outputs inside the process is unwanted or dangerous — the spec, not precedent, is the standard.
5. **Run-scoped state.** Nothing generated inside the run needs to survive into the host OV's memory except the deliverable itself and its filing record. The run can be forgotten once its output is filed.

**Counter-indicators — any single one routes the candidate back to OV-native design:**

- **Answer-dependent elicitation.** The next question depends on the last answer — conversational judgment is happening inside the process. (An up-front parameter form is fine; an interview is not.)
- **Cross-run state accumulation inside the process.** The process itself is supposed to get wiser, track history, or carry balances forward — that is host-OV state wearing a pipeline costume.
- **State-driven dispatch or branching.** Which step runs next depends on the case; the "pipeline" is actually a dispatcher.
- **Mid-process cross-session resume.** "Where were we?" must be answerable *inside* the process across sessions — the work has a memory-worthy middle, which is institution work by definition.
- **In-process normative walls or refusal behavior.** Decision lines, confidentiality walls, and refusal contracts are institution features. Their presence does not necessarily kill the pipeline — it relocates the wall: the host owns the norm and imposes it on the requisition as an **output constraint** the deliverable must satisfy (e.g., "the produced document carries no values from file X"), while the judgment of edge cases stays host-side.

**The hybrid-split rule — where most real candidates land.** When a candidate mixes judgment and production, do not classify it whole: **split it**. The elicitation/judgment half remains an OV-native activity; the production half is requisitioned; the seam is that the host activity *parameterizes and invokes* the pipeline — it gathers and decides what the factory consumes, and files what the factory produces. A candidate that seems to fail marks 1–2 only because an interview precedes the production is a hybrid, not a rejection.

**The acid test (when the marks feel arguable):** *would run-fresh amnesia be malpractice for this piece of work?* If forgetting everything between runs is harmless — even hygienic — it is factory work: requisition it. If forgetting between occasions would be negligence, it is institution work: keep it OV-native.

**Design-time markers — where to look during an engagement:**

- **Q1** answers weighted toward *operational* / *procedural* knowledge kinds.
- **CQ10** deliverables produced repeatedly to a stable template ("every deal gets a …", "each quarter we produce a …").
- **Q7** candidate activities whose descriptions reduce to a fixed step list, or to the form "generate X from Y" — a noun-pipeline hiding in an activity name.
- Any activity the operator describes with assembly-line vocabulary: *standard*, *always the same way*, *batch*, *turn the crank*.

**Classification output.** For each candidate: `ov-native` (counter-indicator present, or signature incomplete), `requisition` (full signature, no counter-indicators), or `hybrid-split` (record both halves: the retained host activity and the requisitioned pipeline). Log every classification with a one-line reason in `_design-decisions.md`. What OVE must **never** do at a `requisition` or `hybrid-split` hit is design the pipeline: no stages, no folder layout, no context budgets, no stage contracts — that is ICME's craft, and its appearance in OVE output is failure mode **F18**.

### Requisition notes (ICM-specific fields)

Beyond the general template: name the invoking host activity and its trigger; enumerate the host Items/files the run consumes and the host Type its deliverable is filed as; state the consistency posture explicitly (ICM's native stance is no-learning-from-precedent — if the host *wants* precedent sensitivity, say so in the requisition and let ICME judge whether the need is still ICM-shaped); state cadence and expected run volume.
