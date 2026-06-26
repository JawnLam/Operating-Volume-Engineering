---
type: Fleeting
timestamp: "2026-06-06T00:00:00Z"
Item_ID: ove-engine-06-state-persistence
title: "OVE Engine — 06 State Persistence"
Date_Added: 2026-06-01
Date_Modified: 2026-06-06
Needs_Processing: false
doc_type: design-engine
role: state-persistence
scope: subject-agnostic
updated: 2026-06-01
---

# 06 — STATE PERSISTENCE

> **What gets written when, by whom, with what durability. The state-persistence contract is what makes an OV multi-session-capable. Get it wrong and the AI either loses continuity or overwrites your work.**

## Why this chapter is load-bearing for Convention 10

State persistence design IS how this OV implements the **Memory & Statefulness** category of the Standalone Sufficiency substrate (`_design-engine/_meta/standalone-sufficiency/requirements.yaml`, Category B). Three of the 47 requirements map directly to the decisions in this chapter:

- **REQ-B1 — Persistent User Model** (T0 hard gate, weight 5). The agent SHALL retain a persistent user model (profile, constraints, goals, history) across sessions without re-priming. This is non-negotiable; if the state-persistence design fails to make this real, the OV cannot ship.
- **REQ-B2 — Longitudinal Continuity** (T2). The agent SHALL reference and build upon prior interactions, drafts, and decisions. Mode A append-only logs + Mode B overwrite-with-history are the two patterns that realize this.
- **REQ-B3 — Compounding Context Value** (T2). Accumulated context SHALL make output measurably better over time — state must appreciate. This is the durability claim that turns Mode B from a recordkeeping pattern into a moat. REQ-M2 (Legitimate Switching Cost) often rests on B3 being designed in.

When designing the OV's state model below, design *toward* these three requirements explicitly. The Memory & Statefulness category is the single biggest structural gap between a service and a chat window — Convention 10's framing — and this chapter is where OVE closes it. The OV's `_meta/posture.yaml` must mark REQ-B1 as `met` with an evidence pointer into this chapter's decisions (typically: name the state file Mode and the bootstrap re-read protocol that satisfies B1).

## The five durability modes

Every file in an OV has one of these modes. Choose deliberately.

### Mode A — Append-only

Once written, never edited. New entries are appended at the bottom.

**Examples:** session logs, decision logs, quiz results, SR performance logs, sprint archives.

**Why:** historical record. Editing breaks the record. The chronology is part of the data.

### Mode B — Overwrite-with-history

The current state lives at the top; history accumulates below.

**Examples:** none in OVE v1.0, but possible — e.g., a "current opinion" file that keeps prior versions below for audit.

**Why:** when the current view matters but the history is also useful.

### Mode C — Full overwrite

Rewritten in full each session. No history within the file.

**Examples:** state files (`_state.md` in LLL, `_design-state.md` in OVE). The state is by definition current; the session log is the history.

**Why:** scannable, single source of truth, no merging.

### Mode D — Append-friendly with sections

Mostly stable; specific named sections are appended within the session.

**Examples:** Item notes that grow as mastery increases (the body sections accumulate notes; the frontmatter overwrites).

**Why:** mixed mode for documents that have both stable structure and accumulating content.

### Mode E — Immutable after creation

Written once; never touched.

**Examples:** archived case files, shipped synthesis pieces, license files.

**Why:** these represent finished work; editing them retroactively changes history.

## The state-persistence contract for OVE itself

| File | Mode | Owner | Read at | Written at |
|------|------|-------|---------|------------|
| `_ov-manifest.md` (cartridge) | C — overwrite | AI | Session start | Sessions that change scope/goals |
| `_design-state.md` (cartridge) | C — overwrite | AI | Session start | Every session end |
| `_design-decisions.md` (cartridge) | A — append-only | AI | When needed for context | Sessions that lock a decision |
| `_schema-draft.md` (cartridge) | D — append-friendly | AI | When designing schema | SCHEMA-DESIGN sessions |
| `Sessions/YYYY-MM-DD_NNN_*.md` | E — immutable | AI | When needed for context | At session end |
| `Artifacts/*.md` (drafts) | D — append-friendly | AI | ARTIFACT-DRAFT, REVIEW sessions | ARTIFACT-DRAFT, REVIEW sessions |
| `_USER.md` | C — overwrite | User | Session start | When user updates |
| `_design-engine/*.md` | C — overwrite | OVE maintainers | Reference only | Patch / minor / major releases |
| `_design-engine/_meta/*.md` | C — overwrite | OVE maintainers | Reference only | Patch / minor / major releases |
| `LICENSE.md`, `VERSION.md`, `CHANGELOG.md` | C/A — see file | OVE maintainers | Reference | Release events |

## The "what gets written when" decision

For any data the OV needs to remember, decide three things:

1. **Granularity** — per session? per Item? per cartridge? per OV?
2. **Lifecycle** — does it accumulate? get overwritten? get archived?
3. **Owner** — who writes it (AI, user, both, maintainer)?

The combination determines the durability mode and the file.

Examples:

- **A user's current state in a long-running engagement** → granularity: cartridge; lifecycle: overwritten; owner: AI. → Mode C, lives in a `_state.md`-style file.
- **A historical record of decisions** → granularity: per-decision; lifecycle: accumulates; owner: AI. → Mode A, lives in a `_decisions.md`-style log.
- **A specific deliverable being worked on** → granularity: per-artifact; lifecycle: edited until shipped, then immutable; owner: AI. → Mode D during work, Mode E after ship.
- **User identity and preferences** → granularity: global; lifecycle: overwritten when user updates; owner: user. → Mode C, lives in `_USER.md`.

## Source-of-truth rule

For any single piece of state, exactly one file is the source of truth. Other files may *reference* it but must not *duplicate* it.

If you find yourself writing the same value into two files, stop. Pick one as the source; have the other reference it. Duplication produces drift; drift produces corruption.

## State recovery

If a state file is corrupted, missing, or stale, the recovery procedure is:

1. **Read the most recent session log.** It contains the state changes from that session.
2. **Walk backward through session logs** until the state can be reconstructed.
3. **For decision-locked state,** the decision log is authoritative.
4. **Rewrite the state file** using the template.

The session log is the durable record. The state file is a rollup. If the rollup is lost, the record can rebuild it. This is why session logs are Mode E (immutable) — they're the foundation.

## Anti-patterns to flag

- **AI memory features as load-bearing.** Don't depend on ChatGPT Memory or Claude's memory tool for state. They're not portable, not auditable, not in the user's control.
- **Inline state in the conversation.** Don't track state in the chat transcript alone. Sandbox mode is the exception, not the rule.
- **State only in the bootstrap file.** AI-BOOTSTRAP must be stateless across users; it's the runtime, not the data.
- **No state at all.** If the OV can be used in a single session and never again, it's not an OV — it's a Custom GPT or a sophisticated prompt.

## Quality checks

For the OV being designed:

- [ ] Every piece of state has exactly one source-of-truth file
- [ ] Every file has a defined durability mode
- [ ] The "write before you end" contract is explicit in the protocol
- [ ] The recovery procedure for the state file is documented
- [ ] No state lives only in AI memory or only in the conversation
