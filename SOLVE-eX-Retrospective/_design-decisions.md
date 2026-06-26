---
type: OVE_Design_Decisions
timestamp: "2026-06-01T00:00:00Z"
Item_ID: "solve-ex-retrospective-decisions"
title: "SOLVE-eX — Retrospective Decisions Log"
Date_Added: 2026-06-01
Date_Modified: 2026-06-01
Needs_Processing: false
ove_OV_Name: "SOLVE-eX"
---

# SOLVE-eX — Retrospective Decisions Log

> **Decisions reverse-engineered from the shipped artifact. Annotations explain why each choice was made and what alternative was rejected.**

## Decisions

### 2026-04 (approx.) — Decision 1: The cartridge analog is a Case File

**Decided:** Each engagement = one Case File. Active case files live in `06-Case-Files/_ACTIVE/`; archived ones in `_ARCHIVED/`. A `_TEMPLATE.md` ships with the OV; user case files are gitignored by default.

**Alternatives considered:**
- One folder per project (rejected: doesn't match how the user actually engages — problems are case-shaped, not project-shaped)
- Single rolling state file (rejected: loses case-by-case isolation; multiple concurrent cases would collide)

**Rationale:** Decision-making and problem-solving are inherently case-shaped. The user brings a specific problem; the AI works through it; the case closes. The Case File metaphor matches the work.

**Implications:** Schema design centers on the Case File structure. Sessions are recorded within case files, not in a separate `Sessions/` folder at the cartridge level.

---

### 2026-04 — Decision 2: Personas as switchable operating modes

**Decided:** Five named personas (Partner, Counselor, Therapist, Guide, Consultant) with explicit switching rules in chapter 07.

**Alternatives considered:**
- Single fixed voice (rejected: doesn't match the range of needs — pure decision support is different from emotional support is different from teaching)
- User-selectable personas only (rejected: AI needs to be able to switch when context warrants, not wait for user)
- Many personas (rejected: cognitive overhead; five is at the edge of useful)

**Rationale:** Different problems need different operating modes. The user wants substantive help across the range. Personas with explicit switching rules + safety routing give the AI a structured way to adapt.

**Implications:** Chapter 07 needs to specify the switching rules formally. Sample sessions need to demonstrate persona transitions. This is heavier than most OVs need.

---

### 2026-04 — Decision 3: Frozen schema with explicit version policy

**Decided:** Schema is v1.14.0 FROZEN. Any schema change requires a master-plan version bump + a documented migration crosswalk + a migration script.

**Alternatives considered:**
- Loose schema, "we'll update as needed" (rejected: produces silent breakage in downstream tools)
- External schema service / API (rejected: breaks substrate-agnostic principle)

**Rationale:** SOLVE-eX is shipped publicly under CC-BY 4.0. Downstream forks and adopters depend on schema stability. The institutional discipline of a frozen schema with explicit migration policy is the only way to make the OV trustworthy as a base.

**Implications:** Adds release-engineering overhead. Sprint cycles required for any spec change. But pays off in adopter trust.

---

### 2026-04 — Decision 4: Voice-neutrality lint via regex

**Decided:** Chapter 13 defines forbidden voice patterns (Class A composition-meta, Class B voice projection, Class C readiness-statement leaks, Class D adjective injection). A `voice-neutrality-lint.py` script enforces them on sample sessions and tool entries.

**Alternatives considered:**
- Prose-only style guide (rejected: not enforceable; AI drifts back to default failures)
- Manual review at every release (rejected: doesn't scale; misses regressions)

**Rationale:** Voice failures are some of the most damaging in OV use — they break the peer register and feel like the AI is performing for the user instead of helping. Regex enforcement catches the most common failures automatically.

**Implications:** Maintenance burden on the regex patterns themselves (Sprint 19 includes the "do NOT propose more regex patterns to close L1 leaks" discipline). The technique has limits but is genuinely useful within them.

---

### 2026-04 — Decision 5: 677 thinking-tool entries

**Decided:** Ship the corpus with 677 individually-schema-validated tool entries in `01-Tools/Tool Entries/`. Each entry conforms to v1.14.0.

**Alternatives considered:**
- Smaller curated set (~50 tools) (rejected: too thin; users would hit gaps quickly)
- Tools as a separate downloadable add-on (rejected: breaks self-contained-folder principle)
- AI generates tool entries on demand (rejected: quality drift; fabrication risk)

**Rationale:** Comprehensive coverage of structured-thinking techniques. 677 is the result of a long curation effort. The schema validation guarantees consistency.

**Implications:** Folder size is substantial. AI must search efficiently rather than reading all tools at every session start. Tool discovery is a real design challenge addressed by the question banks.

---

### 2026-05-26 — Decision 6: Operator-private separation in .gitignore

**Decided:** `06-Case-Files/_ACTIVE/` and `99-Archive/` are gitignored. Public release ships only the template + sample sessions.

**Alternatives considered:**
- Track all case files in public repo (rejected: privacy concern — case files contain personal-decision detail)
- Don't ship case file template at all (rejected: users wouldn't know the shape)

**Rationale:** Personal-decision content is private by default. Public users get the template and can create their own active case files locally.

**Implications:** `.gitignore` carries operational meaning, not just hygiene. The README and INSTALL need to explain the default.

---

### 2026-05-29 — Decision 7: v2.1.0 ADAPT Loop integration as minor release

**Decided:** Add the ADAPT Loop integrative-session-design pattern as an additive content extension. v2.0 → v2.1.0. No schema change.

**Alternatives considered:**
- Hold ADAPT for v3.x (rejected: ready content, no schema impact, minor release is the right slot)
- Bake into chapter content directly (rejected: belongs in `04-Application-Patterns/` as a distinct pattern entry)

**Rationale:** Demonstrates that v3.0 STABLE permits additive content within its constraint. Models the patch / minor / major distinction explicitly.

**Implications:** None — additive only.

---

## Patterns worth surfacing for future OVs

1. **Schema discipline pays off later.** Up-front investment in versioning and migration policy makes the OV trustworthy as a public artifact.
2. **Personas are powerful but heavy.** Five personas is at the top of the useful range. Most OVs need fewer.
3. **Regex enforcement of voice has limits.** Useful within bounds; don't chase every new failure shape with more regex.
4. **Case-shaped cartridges work for decisional/episodic domains.** Pattern transfers to negotiation-prep, legal-case-work, medical-conversation OVs.
5. **Operator-private separation in .gitignore is a real architectural choice.** Worth thinking about per OV.
