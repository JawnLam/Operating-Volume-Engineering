---
type: Fleeting
timestamp: "2026-06-25T00:00:00Z"
Item_ID: ove-proposal-kaov-prd-source
title: "Source PRD — Knowledge-Augmented Operating Volume (KAOV)"
Date_Added: 2026-06-25
Date_Modified: 2026-06-25
Needs_Processing: false
Status: SOURCE CAPTURE — verbatim. Cited by _proposals/KAOV-design-note.md.
Origin: Gemini session (shared link), captured 2026-06-25
---

> **Capture note.** This is the source PRD that `_proposals/KAOV-design-note.md`
> analyzes. Captured verbatim from a Gemini session for provenance (OVE's F13
> discipline applied to OVE's own proposals — never lose the source). The original
> share URL was JS-gated and could not be machine-fetched; the operator pasted the
> text. Bracketed `[n]` markers are the author's inline citation anchors, expanded in
> § 5.
>
> **Format-conformance flags.** This PRD's *architecture* is sound, but several
> *format* details do not match real OKF v0.1 (e.g. "Node File" should be "Concept";
> the `[Source: …]` citation syntax and the invented `dependencies` frontmatter field
> are non-conformant). Do NOT implement from this file's format directly — see
> `_proposals/OKF-conformance-notes.md` for the corrected, binding format contract and
> `_proposals/KAOV-design-note.md` § 8 for the full audit. This capture is left
> verbatim on purpose; corrections live in those two files, not here.

---

# Product Requirements Document (PRD)

## The Knowledge-Augmented Operating Volume (KAOV) Architecture

### Integrating Operating-Volume-Engineering (OVE) with Open Knowledge Format (OKF)

## 1. Executive Summary

Current LLM agent implementations suffer from a dichotomy: they either possess strict
behavioral guardrails but lack deep, scalable domain knowledge (the OVE paradigm) [1],
or they possess massive, structured knowledge graphs but lack deterministic
operational workflows to act upon them (the OKF paradigm) [2].

This PRD outlines an integrated architecture—the Knowledge-Augmented Operating Volume
(KAOV). It uses OVE as the Control Plane (state machine, session loops, rules of
engagement) and OKF as the Data Plane (scalable, progressively disclosed knowledge
graph).

Goal: Enable an AI to execute long-running, complex workflows across massive
enterprise datasets without suffering from context-window degradation or
hallucination.

## 2. Core Architectural Components

The system consists of two distinct but interacting directory structures, glued
together by a new bridging protocol.

### 2.1 The Control Plane: OVE Engine (The "CPU")

The OVE architecture dictates how the AI behaves. It remains strictly quarantined from
raw data, containing only operational logic.

- **AI-BOOTSTRAP.md:** The entry point. Forces the AI to load the rules of engagement
  before taking any action.
- **_design-engine/:** The immutable rulebook containing the event-loop protocol
  (03-DESIGN-PROTOCOL.md), anti-hallucination rules, and strict formatting
  guidelines [1].
- **\<Cartridge\>/_design-state.md:** The mutable, persistent memory of the current
  session's state.

### 2.2 The Data Plane: OKF Bundles (The "Hard Drive")

The OKF architecture dictates what the AI knows. It acts as a static, read-only graph
of the domain.

- **YAML Frontmatter:** Every file contains structured metadata (type, tags,
  dependencies) establishing semantic meaning [2].
- **index.md Files:** High-level directories that summarize the nodes within a
  specific domain concept, preventing the need to load all data at once.
- **Node Files (e.g., concept_A.md):** Deep-dive files containing the actual raw data,
  referenced explicitly via markdown links from the index files [2].

## 3. The Integration: "The Bridge Protocol"

To make OVE and OKF work together, a new instruction file must be added to the OVE
Control Plane: `_design-engine/08-KNOWLEDGE-RETRIEVAL.md`.

This protocol dictates exactly how the AI is permitted to interact with the OKF Data
Plane.

### Functional Requirement 3.1: Progressive Disclosure (Anti-Context Exhaustion)

**Rule:** The AI is strictly forbidden from requesting or reading a raw OKF Node File
directly if it has not first read its parent index.md file.

**Justification:** Normative AI research demonstrates that LLMs suffer from a "Lost in
the Middle" phenomenon; injecting massive amounts of unsorted context degrades
reasoning accuracy [3]. OKF's index files serve as a table of contents, allowing the
AI to filter relevance before consuming token budget.

### Functional Requirement 3.2: Explicit Sourcing (Anti-Hallucination)

**Rule:** When the OVE engine executes an ARTIFACT-DRAFT or writes to
_design-decisions.md, every factual claim MUST include a markdown link citation
pointing directly to the OKF Node File that provided the fact.

**Justification:** OVE's existing F13 failure mode explicitly forbids inventing
sources [1]. By tying OVE's "Never invent" rule directly to OKF's standard file paths,
we create a mathematically verifiable chain of provenance.

### Functional Requirement 3.3: Workspace Isolation

**Rule:** The OVE Cartridge manifest (_ov-manifest.md) must include a Knowledge_Mounts
array. This array defines exactly which OKF index.md files are relevant to the current
project. The AI may not traverse outside these mounted paths.

**Justification:** Constraining the search space limits the LLM's tendency to draw
irrelevant connections across massive enterprise graphs [4].

## 4. Example Session Workflow

1. **Boot:** User types: "Start session. Draft the network architecture based on the
   enterprise catalog."
2. **State Load (OVE):** AI reads AI-BOOTSTRAP.md and the cartridge's _design-state.md.
   It determines the current phase is ARTIFACT-DRAFT.
3. **Knowledge Query (Bridge):** AI notes that the Network_Architecture OKF bundle is
   mounted. It reads okf/network/index.md.
4. **Targeted Retrieval (OKF):** The AI identifies that okf/network/firewall_rules.md
   contains the specific constraints needed. It loads only that file.
5. **Execution (OVE):** AI drafts the artifact, appending
   [Source: okf/network/firewall_rules.md] to the relevant claims.
6. **Propose (OVE):** AI presents the draft to the user and waits for confirmation
   (adhering to OVE's "Propose, don't decide" rule [1]).
7. **State Save (OVE):** Upon user approval, AI updates _design-decisions.md and
   _design-state.md.

## 5. Citations and Justifications

- **[1] Operating-Volume-Engineering (OVE) Specification:** Jawn Lam (2026).
  Operating-Volume-Engineering. Sourced from AI-BOOTSTRAP.md and 03-DESIGN-PROTOCOL.md.
  Specifically validates the use of deterministic, stateful event loops (Step 1-9
  Lifecycle) and the "Propose, don't decide" constraint. GitHub Repository.
- **[2] Open Knowledge Format (OKF) Specification:** Google Cloud Platform (2024).
  Knowledge Catalog Tools and Samples. Sourced from the okf toolset. Validates the use
  of Markdown as an AI-native data transfer format, relying on directory structures
  and frontmatter to represent graph nodes. GitHub Repository.
  *(Verifier note 2026-06-25: OKF was in fact published 2026-06-12, not 2024; repo
  `GoogleCloudPlatform/knowledge-catalog`, `okf/SPEC.md`.)*
- **[3] Context Window Degradation:** Liu, N. F., et al. (2023). "Lost in the Middle:
  How Language Models Use Long Contexts." Establishes the normative requirement for
  Progressive Disclosure (Section 3.1). arXiv:2307.03172.
- **[4] ReAct (Reasoning and Acting) Paradigm:** Yao, S., et al. (2022). "ReAct:
  Synergizing Reasoning and Acting in Language Models." Justifies separating the OVE
  logic loop from the OKF data retrieval step. arXiv:2210.03629.
