---
Item_Prototype: OVE_Design_Decisions
Item_ID: "lll-retrospective-decisions"
Title: "LifeLong-Learning — Retrospective Decisions Log"
Date_Added: 2026-06-01
Date_Modified: 2026-06-01
Needs_Processing: false
ove_ov_name: "LifeLong-Learning"
---

# LifeLong-Learning — Retrospective Decisions Log

> **Decisions reverse-engineered from the shipped artifact. Annotations explain rationale and rejected alternatives.**

## Decisions

### 2026-04 — Decision 1: Cartridge = one subject being studied

**Decided:** A cartridge represents a single subject of study (cybernetics, Roman Empire, Mandarin, baking, etc.). Each subject lives in its own folder with its own schema, curriculum, state, and atoms.

**Alternatives considered:**
- One global subject across all study (rejected: subjects are too structurally different to share state)
- Per-source cartridges (a cartridge per book) (rejected: study is subject-shaped, not source-shaped)

**Rationale:** Subjects have distinct shapes (cybernetics is canonical-thinker-heavy; cuisine is skill-based; languages have CEFR levels). One cartridge per subject lets each cartridge bring its own schema and curriculum.

**Implications:** Schema must be per-cartridge, not global. The teaching engine must be flexible enough to handle radically different subject shapes (canonical-thinker vs. skill-based vs. formal).

---

### 2026-04 — Decision 2: Six universal activities + per-subject custom activities

**Decided:** Standardize on six activities (TEACH, QUIZ-SR, QUIZ-SOCRATIC, REVIEW-WEAK, SYNTHESIZE, INTEGRATE) for all subjects. Allow per-subject custom activities for shapes that need them (e.g., COOK-ALONG for cuisine, SPEAK for languages, PROVE for math).

**Alternatives considered:**
- Fully fixed activity set (rejected: doesn't accommodate skill-based subjects)
- Fully custom per subject (rejected: loses the discipline of a standard protocol)

**Rationale:** Standardization where possible; flexibility where the subject demands it. The six universal activities are general enough to cover most cognitive learning patterns.

**Implications:** Schema design must include Q7 ("custom session activities") to surface subject-specific needs. The session protocol must be flexible enough to mix universal and custom activities.

---

### 2026-04 — Decision 3: Schema design via Q1–Q8 protocol

**Decided:** Each new subject's schema is designed via eight protocol questions before any atoms are created.

**Alternatives considered:**
- Generic universal schema for all subjects (rejected: forces all subjects into the same shape)
- AI improvises the schema on the fly (rejected: produces incoherent atom types and drifting structures)

**Rationale:** Schema is the most important creative work. Forcing eight explicit answers ensures the schema reflects the actual domain shape rather than retrofitting a template.

**Implications:** Cartridging takes longer (2–4 sessions just for schema). Pays off across the study's lifetime. Pattern adopted into OVE as Q1–Q13 at the meta level.

---

### 2026-04 — Decision 4: Universal atom types in templates, custom atoms in cartridges

**Decided:** Universal atom types (session, quiz, sr-log, synthesis, source) live as templates in `_teaching-engine/_templates/`. Custom atom types (concept, thinker, period, event, technique, etc.) are defined per cartridge in `<Subject>/_schema.md`.

**Alternatives considered:**
- All atoms universal (rejected: cybernetics needs "thinker"; cuisine doesn't)
- All atoms custom per subject (rejected: session logs and quizzes have the same shape across subjects)

**Rationale:** The line between universal and custom is the line between "always true of this kind of work" (session logs) and "depends on the domain" (atom types). This is the cleanest separation.

**Implications:** Two-layer schema (universal at the engine; custom at the cartridge). Pattern adopted into OVE's three-layer schema-of-schemas.

---

### 2026-04 — Decision 5: Synthesis at four time-scales

**Decided:** Four synthesis kinds with explicit cadence: weekly journal (every 3–5 sessions), monthly essay (every 12–18 sessions or on request), phase-end translation (at phase exit), quarterly public-facing draft (every ~40 sessions or on request).

**Alternatives considered:**
- Single synthesis kind (rejected: doesn't capture the different time-scales of integration)
- No structured synthesis (rejected: study without synthesis produces accumulated notes, not knowledge)

**Rationale:** Different time-scales of integration are genuinely different work. Weekly catches learning while it's fresh; monthly forces consolidation; phase-end translates theory to practice; quarterly forces external-audience writing.

**Implications:** Four templates needed. Four sub-folders in `<Subject>/Synthesis/`. Encourages a writing practice as part of study.

---

### 2026-04 — Decision 6: Bring-your-own SR tool

**Decided:** SR cards are embedded in atom notes using Obsidian SR plugin syntax by default, but the AI doesn't manage scheduling. Users can use Obsidian SR, Anki, Mochi, or any other tool — or skip SR entirely and fall back to Socratic quizzing.

**Alternatives considered:**
- Build SR scheduling into the engine (rejected: scope creep; existing tools do this well)
- Require a specific SR tool (rejected: locks the OV to a specific stack)

**Rationale:** Substrate-agnostic. The user's existing SR practice (if any) is more important than the OV's preference.

**Implications:** SR is genuinely optional. The QUIZ-SR activity is skipped if the user doesn't have an SR tool configured.

---

### 2026-05 — Decision 7: Personal name handling

**Decided:** The bootstrap protocol uses `_USER.md` (optional, user-created) and per-cartridge `_subject.md` user-context section for personalization. Engine files do NOT hardcode any user identity.

**Alternatives considered:**
- Hardcode "Jawn" in the engine (this was actually present in early drafts; corrected in the public release)
- Single global user profile required for use (rejected: too much setup friction)

**Rationale:** Substrate-agnostic + shareable + identity-safe. The `John-Lam-from-jawnlam` failure mode informed this choice (see OVE's `_meta/FAILURE-MODES.md` F3).

**Implications:** Bootstrap defaults to peer register / substantive critique without knowing the user's name. User can override via `_USER.md` or per-subject preferences.

---

### 2026-06-01 — Decision 8: Public release as v1.0.0 under CC-BY 4.0

**Decided:** Strip personal cartridges from the public release. Ship with one worked example (Roman Empire) demonstrating the four-atom-type schema. License CC-BY 4.0 matching SOLVE-eX.

**Alternatives considered:**
- Keep personal cartridges in the public repo (rejected: privacy + cleaner shipping)
- Ship without any example cartridge (rejected: users wouldn't know the shape)
- Multiple example cartridges (rejected: scope creep for v1.0)

**Rationale:** One full worked example demonstrates the pattern; users can bootstrap their own subjects from there.

**Implications:** `.gitignore` excludes personal cartridges by default. The Roman Empire cartridge is exemplary, not personal.

---

## Patterns worth surfacing for future OVs

1. **Two-layer schema (universal + per-cartridge custom) is generative.** Lets one OV serve many domain shapes.
2. **Q1–Q8 schema design is worth the up-front time.** Bad schemas can't be salvaged later.
3. **Synthesis at multiple time-scales is opinionated but powerful.** Pattern transfers to any long-running domain.
4. **Bring-your-own-tool for ancillary services (SR, calendar, etc.).** Keeps the OV substrate-agnostic.
5. **One worked example > zero examples > many shallow examples.** For v1.0 shipping.
