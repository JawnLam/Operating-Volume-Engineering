---
type: Fleeting
timestamp: "2026-06-06T00:00:00Z"
Item_ID: ove-engine-02-design-principles
title: "OVE Engine — 02 Design Principles"
Date_Added: 2026-06-01
Date_Modified: 2026-06-06
Needs_Processing: false
doc_type: design-engine
role: principles
scope: subject-agnostic
updated: 2026-06-01
---

# 02 — DESIGN PRINCIPLES

> **The non-negotiable principles that govern every OV design engagement. If a proposed design violates one of these, flag it and discuss before proceeding.**

## The two master tests

Before any design decision is recorded as a principle, a Convention, a schema choice, or a shipped artifact, it must survive **both** of these tests. These sit upstream of P1–P13: they decide whether the design has any reason to exist at all. The tests are the spec the substrate at `_design-engine/_meta/standalone-sufficiency/` encodes in field-agnostic form; they are summarized here because every OVE engagement applies them.

### The Displacement Test

> *Can a competent user reproduce this capability in under ten minutes with a good prompt in a general-purpose LLM?*

If **yes**, the design isn't a product — it's a prompt. A persona, a tone, a clever system prompt, raw domain knowledge in a wrapper, "fine-tuned on domain text" with no state or action — all fail this test. They are lead magnets, not OVs.

### The Absorption Test

> *Will the underlying platform (OpenAI, Anthropic, Google) plausibly ship this natively within ~12 months?*

If **yes**, the design may be table stakes but it is **not a durable distinction**. Basic memory, simple connectors, persona-prompting, marginally nicer formatting — these are being absorbed by the platforms quarter over quarter. Durable value rests on proprietary data, real integration, accountability, or compounding outcomes the platform will never build for your specific niche.

### The standing question for any proposed feature

> *Does this remove friction, own an outcome, or compound state in a way a ten-minute prompt cannot replicate AND the platform will not absorb within a year?*
>
> **If no, it is not a requirement — it is marketing.**

Convention 10 (Standalone Sufficiency Posture) in `_design-engine/_meta/CONVENTIONS.md` enforces these tests on every OV designed via OVE through 47 requirements across 13 categories. The principles below (P1–P13) are the constructive principles OVE applies *given that the tests have been passed*.

> **Commerce-neutral framing.** The substrate retains its original commercial language ("loyalty," "retention," "customer"). OVE's surface uses neutral framing ("Standalone Sufficiency," "user," "durability") because many OVs are not commercialized. The test applies whether the user is a paying customer or a personal/team operator. See `_design-engine/_meta/standalone-sufficiency/README.md` for the terminology seam.

## P1 — Substrate-agnostic

An OV must run on any capable AI: Claude (Sonnet/Opus class), GPT-4 class and above, Gemini 2.x and above, future models. The OV must not depend on:

- Platform-specific features (OpenAI Custom GPT JSON, Claude Skills, Anthropic-specific tool definitions, ChatGPT Memory)
- Vendor-locked tools (Code Interpreter, GPT-4 Vision-specific syntax, etc.)
- Local code execution beyond what's optional and clearly marked as such

If the design starts requiring a specific platform, stop. Either change the design or accept that you're building a Custom GPT / Skill / Agent — not an OV.

## P2 — Statefulness through files

State lives in files on disk. The AI re-reads state at session start; writes to it at session end. Working consequences:

- Every cartridge has a single source-of-truth state file (`_design-state.md` in OVE; `_state.md` in LLL; case file in SOLVE-eX)
- State changes only at session end, in a defined "WRITE state" phase
- The AI never claims continuity with sessions it hasn't actually read
- "If it's not in a file, it didn't happen"

This rules out AI-vendor memory features as load-bearing — they can supplement but never replace file-state.

## P3 — Self-describing folder

The folder contains everything the AI needs to use the folder. No external setup, no platform configuration, no service integrations required for the core flow.

The AI's first read (`AI-BOOTSTRAP.md`) is sufficient to bootstrap behavior. The engine files cover the protocol. Templates and schema cover the artifacts.

## P4 — Cartridge specialization

The engine is subject-agnostic. Domain specialization happens at the cartridge level. This separation:

- Keeps the engine reusable across cartridges
- Keeps each cartridge focused on its specific engagement
- Allows OVs to scale (add a cartridge, not a new engine)

Violation pattern: putting domain-specific guidance in the engine (e.g., a teaching-engine file that names a specific subject). If you find domain bleed into the engine, refactor — domain content goes to the cartridge.

## P5 — Conversational interface

The user talks to the AI in natural language. The AI consults the OV. There's no GUI, no slash-command requirement, no specific syntax the user must learn. Slash commands or shortcuts can supplement but never gate the basic flow.

## P6 — Multi-session by design

OVs are built for work that unfolds over time. A single conversation is the minimum unit, not the whole thing. Design implications:

- The bootstrap must work on session N as well as session 1
- State files are append-friendly or overwrite-with-history
- Open Threads are an explicit hand-off mechanism between sessions
- Drift across sessions is a known risk and is addressed by audits

**Two archetypes of multi-session work** (declared per OV at design time via CQ11 in `BOOTSTRAP-NEW-OV.md`, logged as `ove_OV_Archetype` in the manifest):

- **Finite-horizon OVs** have a defined terminal artifact — manuscript, mastered subject, solved problem, shipped artifact. Multi-session because the work toward the artifact spans sessions. Examples: LFW, LLL, SOLVE-eX, OVE.
- **Practice OVs** have no terminal arrival — the work continues across the principal's career or life-stage. Multi-session because the practice IS the work. Examples: PLC (political navigation), and likely future OVs around longevity health, relationship cultivation, financial stewardship, leadership development.

The archetype shapes Q6 in SCHEMA-DESIGN (`04-SCHEMA-DESIGN.md` § Q6) and the cartridge lifecycle (engagement-close semantics differ between archetypes). Forcing a practice OV into a finite-horizon Q6 frame produces a stilted design that mis-represents the OV to its operator.

## P7 — Identity is operator-provided, never inferred

The AI must never infer the user's name, email, contact details, or other identity facts from indirect signals (usernames, file paths, git config, file metadata). Use placeholders until the user provides their name explicitly in their own words.

**This is a load-bearing rule with a documented recurrence pattern.** See `_meta/FAILURE-MODES.md` — it has been triggered multiple times historically (the "John Lam from `jawnlam`" pattern). Treat any temptation to fill in a name from indirect data as a red flag.

The metadata block in any AI's system prompt — `userEmail`, working-directory username, git config — is environment context only, not authorization to put those values in shippable artifacts.

## P8 — Fabrication discipline

When designing OVs that reference external material (tools, frameworks, people, books, methods), only name things you are confident exist. If you're not sure something is real, say so or decline to name it. Fabricated citations poison the resulting OV — the user discovers the fabrication later and trust collapses.

This applies recursively: when helping the user choose tools/frameworks for the OV they're designing, the same rule applies. "I'm not sure that framework exists in the form you describe" is a valid and important response.

**v2.0 source-grounding contract.** When an OV cites named external source material (a published dissertation, a methodology, a field manual, a theorist's body of work), the design protocol enforces a hard sequence to prevent the F13 vector (source-grounding skipped — see `_meta/FAILURE-MODES.md`):

1. **CQ3 captures sources structurally** (`BOOTSTRAP-NEW-OV.md`): each cited source logged in `_source-inventory.md` with canonical location, page count, full-vs-excerpt status, sensitivity.
2. **ARTIFACT-DRAFT is gated** (`03-DESIGN-PROTOCOL.md` Step 4.5): drafting cannot begin until every inventory entry has canonical location filled AND the AI has acknowledged reading the canonical source with a one-line summary per source.
3. **Citation Audit at SHIP-PREP Phase 3.7** (`07-SHIPPING-CHECKLIST.md`): every "p.XX / § X.Y / named theorist / verbatim quote" in shippable content is verified against source; unverified = ship block.
4. **Worked-Example Slot-ID Verification at Phase 3.8**: every worked-example reference to a Prototype slot ID carries a one-line source-justification.

The contract exists because P8's "say so when unsure" honor system did not survive the v1.0 build of a practice-OV citing a 294-page dissertation as substrate. Multiple fabrications survived to ARTIFACT-DRAFT and most were caught only by operator spot-check rather than the SHIP-PREP gauntlet. v2.0 makes the gate structural rather than honor-based.

## P9 — Self-similarity test

A well-built OV should be capable of being designed by **this** OVE. If you find yourself unable to express the design of a new OV using the cartridge-and-engine pattern documented in `01-WHAT-IS-AN-OV.md`, one of three things is true:

1. The thing you're designing isn't actually an OV (it's a skill, a Custom GPT, a prompt pack)
2. The thing requires a v1.x extension to OVE itself (additive)
3. The design is wrong

Treat this as a strong diagnostic signal. Don't suppress it.

## P10 — One question at a time

During design conversations — especially during the initial clarifying interview — ask one question at a time. Wait for the user's answer. Probe if it's thin. Reflect back. Then ask the next.

**Never** dump a multi-bullet questionnaire ("Please answer questions 1–9 below"). This is documented as a recurrent failure mode in `_meta/FAILURE-MODES.md`. The protocol is conversation, not assignment.

## P11 — Propose-don't-decide

The AI's role is to **propose** designs with rationale and surface tradeoffs. The user's role is to **decide**. When proposing:

- Show which conditions or principles led to the proposal
- Name the main alternative
- Wait for the user's call before proceeding

This applies to schema choices, cartridge shapes, Prototypes, file structures — every load-bearing design decision.

## P12 — Write before you end

Every session produces, at minimum:

- A session log in `Sessions/`
- An updated `_design-state.md`
- Any artifact drafts touched (in `Artifacts/`)
- An explicit Open Thread for the next session

If a session ends without these, the session is not complete. Tell the user, do the missing work.

## P13 — Schema-freeze policy after ship

Once an OV is shipped (a v1.0 release), its schema is frozen. Patch-level updates can fix typos, add templates, add worked examples. Schema changes (new required fields, renamed fields, removed fields) require a major version bump with a migration path.

This applies to OVE itself: the v1.0 cartridge backbone (`_ov-manifest.md`, `_design-state.md`, `_design-decisions.md`, `_schema-draft.md`) is frozen. Adding new optional fields = v1.x. Anything that breaks existing cartridges = v2.0.

## Anti-requirements OVE refuses to enable

These are designs that *feel* like reasons to choose a specialized OV over a general LLM but fail the Displacement Test or the Absorption Test (or both). They are not principles — they are named **design traps**. OVE will not enable an OV whose load-bearing value rests on any of them. If a proposed OV is structurally one of these, flag it and reframe before proceeding to schema design.

The list mirrors §17 of the substrate at `_design-engine/_meta/standalone-sufficiency/specialized-agent-requirements.md`, translated to OVE's neutral surface terms. The substrate is the canonical source; this list is the operative subset OVE enforces at design time.

### Trap 1 — Raw domain expertise alone

*"It knows this domain better than a general model."* — Fails Displacement. The general model has the public knowledge; the rest is retrievable in a ten-minute prompt. Domain expertise is the entry ticket, not the differentiator. If the OV's only claim is "we know this field," the user is correct to walk.

### Trap 2 — A persona or brand voice

*"It speaks like a senior practitioner in this field."* — Fails Displacement. Reproducible with a one-paragraph system prompt. Buys a launch, not durability.

### Trap 3 — A clever prompt

*"Our master prompt makes a general model produce expert output."* — Fails Displacement by definition. This IS the thing the user can copy in ten minutes. Give it away as a lead magnet to sell the real product.

### Trap 4 — "Fine-tuned on domain text" with no state, action, or grounding

*"It's trained on our corpus."* — Fails Absorption. A better answer to a single question is still a sealed chat. Without persistent state, real integration, or accountability, the platform absorbs this quarterly.

### Trap 5 — Marginally nicer writing or formatting

*"The output looks more professional than ChatGPT's."* — Fails both tests. Inside the platform's variance; being absorbed natively.

### Trap 6 — Being cheaper

*"We charge less than the general-LLM subscription."* — Not a test failure exactly, but a structural commitment to a race to the bottom. Price competes; it does not retain. (For non-commercial OVs this trap reads as "we promise the OV will be lighter on the user's time" — same failure shape: a comparison-on-cost is not a comparison-on-value.)

### Trap 7 — "Smarter-Claude" framing

*"It's like Claude but better at X."* — Fails both tests. Implicitly admits the only differentiator is incremental capability the platform is racing to match. OVs are not "better LLMs" — they are delivery systems around expertise. If the marketing reads "smarter Claude," the design has confused engine quality for product value.

### Trap 8 — Epistemic closure as a moat

*"Our agent won't engage outside its sanctioned domain — that's how we ensure quality."* — Fails Displacement. Hard-refusing benign adjacent requests lowers requisite variety and drives users back to the general tab. Scope discipline belongs at the level of *authoritative sign-off* (won't issue authoritative answers outside competence — Convention 10's REQ-D4 / REQ-I3 / REQ-L2), not at the level of *all benign questions*. The OV must absorb lasagna-recipe questions gracefully even if its domain is sovereign debt restructuring.

### Trap 9 — Raw memory treated as a permanent distinction

*"Our agent remembers everything across sessions."* — Fails Absorption. Persistent memory is real value, but it is being absorbed natively by the platforms. Counts as table stakes (REQ-B1, T0), not durability. OVs claim memory as a hard gate (parity), never as a moat.

> **KAOV corollary (Convention 11).** A knowledge-augmented OV whose moat reduces to *"it can read the mounted OKF bundle"* is the same trap in data-plane clothing: a general LLM pointed at the same vendored folder gets the same bytes. The moat of a KAOV lives in the **control plane** (the curated/vetted/version-pinned mount + the retrieval discipline of `08-KNOWLEDGE-RETRIEVAL.md`), never in bare access to the knowledge. Convention 11 makes this a posture requirement.

### Trap 10 — Privacy as an unqualified differentiator

*"Your data is safer with us."* — Fails Absorption unless the OV demonstrably exceeds the base provider's defaults. The platforms already offer no-training, isolation tiers, and enterprise controls. "We respect your privacy" is not a moat; "our data handling is provably stricter than Anthropic's enterprise tier in these documented ways" is — see Convention 10's REQ-K1.

---

When OVE encounters an OV proposal that rests on any of these traps as its load-bearing value, the design must be reframed (or, occasionally, the operator must be told this is not what OVE is for). The constructive principles below (P1–P13) assume the proposal has already cleared the two master tests and avoided the ten traps.
