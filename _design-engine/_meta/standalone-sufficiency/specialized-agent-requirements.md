# Specialized AI Agent — Loyalty & Retention Requirements

**A field-agnostic requirements specification for any specialized AI agent that must defeat the objection:**
> *"Why should I use your specialized AI agent over a general-purpose LLM like Claude, ChatGPT, or Gemini?"*

*Revision 1.2 — adds **REQ-J4** (Value Attribution / ROI Surfacing), folds an interactive-surface clause into REQ-C1, and states the spec's explicit position on boundary governance (§3 note + §17 traps). Earlier 1.1 added REQ-E4, REQ-H4, REQ-M4. Each addition was run through the two master tests in §1 before inclusion.*

*This narrative spec is the conceptual master. The per-requirement registry (`requirements.yaml`) is the single source of truth from which two operational views are generated — an internal **build standard** (pass/fail gates) and a client-facing **vetting rubric** (weighted scoring). Edit the registry, regenerate the views; never hand-edit the views.*

---

## 0. Governing Premise

This specification assumes the agent is **already** imbued with the focused expertise of the best thinkers in its field. Therefore:

**Expertise is the entry ticket, not the differentiator.** It is *assumed*, not *required*, because the frontier general models already hold most of the field's public knowledge, and the rest can be retrieved. If the agent's only advantage is that it "knows the domain better," the customer is correct to walk — they can prompt a general model toward the same knowledge.

Every requirement below therefore addresses the **delivery system around the expertise** — the state, workflow, action, accountability, and compounding value that a raw chat session structurally cannot provide. Each requirement exists to neutralize a specific version of *"I'll just use Claude."*

---

## 1. The Two Master Tests

A capability only counts as a genuine loyalty driver if it survives **both** tests. Every requirement in this document is written to pass them.

### The Displacement Test
> *Can a competent user reproduce this capability in under ten minutes with a good prompt in a general-purpose LLM?*

If **yes**, it is not a loyalty driver — it is a prompt, and it should be given away as a lead magnet, not sold. A persona, a tone, a clever system prompt, and raw domain knowledge all fail this test.

### The Absorption Test
> *Will the underlying platform (the lab) plausibly ship this natively within ~12 months?*

If **yes**, it may be table stakes but it is **not a durable moat**. Basic memory, simple connectors, and persona-prompting are being absorbed by the platforms quarter over quarter. Durable value must rest on proprietary data, real integration, accountability, or a compounding outcome record the lab will never build for your specific niche.

### The Loyalty Equation
> **Loyalty = (Friction removed + Outcome owned + State compounded) − (Capability lost vs. the general model)**

A specialized agent loses the customer the moment the final term goes positive — i.e., the moment it feels *worse* than the thing it replaces. Several requirements below exist solely to keep that term at or below zero.

---

## 2. How to Read This Spec

Each requirement carries:

- **ID** — stable reference (e.g., `REQ-D3`).
- **Requirement** — a `SHALL` statement.
- **Neutralizes** — the specific customer objection it kills.
- **Acceptance test** — the condition under which it is verifiably met.

Priority tiers (mapped in §16):

| Tier | Meaning |
|---|---|
| **T0 — Parity** | If absent, the customer instantly defaults to the general model. Non-negotiable. |
| **T1 — Differentiator** | The active reason to *choose* the specialist over the default. |
| **T2 — Retention/Moat** | The reason to *stay*, and the reason the value *can't be absorbed*. |
| **TG — Trust-Gated** | Required to *enter* a high-stakes or regulated domain at all. |

---

## 3. Category A — Foundational Parity & Scope Integrity
*If the specialist feels dumber or more caged than the general model, no other feature matters.*

| ID | Requirement | Neutralizes | Acceptance test |
|---|---|---|---|
| **REQ-A1** | The agent SHALL be at least as capable and fluent as a frontier general model on any task that overlaps both. | "The specialist is just a worse, narrower Claude." | Blind A/B on overlapping tasks: specialist rated ≥ general model on usefulness. |
| **REQ-A2** | The agent SHALL handle adjacent or out-of-scope requests gracefully — answering competently or redirecting transparently — never dead-ending in a refusal wall. | "It can't do the other ten things I also need, so I'll just keep one tab for everything." | Out-of-scope probes yield useful handling, not brittle failure. |
| **REQ-A3** | Specialization SHALL add only constraints that serve the user; it SHALL NOT strip useful general capability to force a workflow. | "It won't just answer my question — it makes me jump through hoops." | The user can still obtain a direct answer on demand. |

*Boundary-governance position: scope discipline is **not** brittleness. The agent should preserve its identity and methodology (L2, I5), abstain outside grounded competence (D4), and escalate on high-stakes scope-breach (I3) — but it must absorb benign adjacent requests gracefully rather than refusing them to "reinforce authority." In viable-system terms, rigid refusal lowers requisite variety and makes the agent less viable, not more; it is also the precise behavior that keeps a general-model tab open. The right line is "won't issue sign-off it can't stand behind," not "won't answer anything off-script." (See §17.)*

---

## 4. Category B — Memory & Statefulness
*The single biggest structural gap between a service and a chat window.*

| ID | Requirement | Neutralizes | Acceptance test |
|---|---|---|---|
| **REQ-B1** | The agent SHALL retain a persistent user model (profile, constraints, goals, history) across sessions without re-priming. | "I have to re-explain everything every time." | Zero re-entry of previously supplied facts across sessions. |
| **REQ-B2** | The agent SHALL reference and build upon prior interactions, drafts, and decisions. | "A general chat loses the thread." | The agent invokes specific prior-session artifacts unprompted. |
| **REQ-B3** | Accumulated context SHALL make output measurably better over time — state must *appreciate*. | "Switching away is free; nothing is lost." | Output quality/tailoring improves as a function of usage history. |

---

## 5. Category C — Workflow Orchestration & Guided Process
*Sells the knowledge of how to extract value, not the value itself. Kills the "prompting deficit."*

| ID | Requirement | Neutralizes | Acceptance test |
|---|---|---|---|
| **REQ-C1** | The agent SHALL drive a structured expert intake — using interactive surfaces (forms, selectors, guided steps) rather than a bare prompt box — so the user need not know what to ask. | "I don't know how to prompt for genuinely good advice." | A novice reaches expert-grade output without writing an expert prompt. |
| **REQ-C2** | The agent SHALL chain and execute multi-step processes end-to-end from a single initiation. | "I'd have to run each step manually myself." | A multi-stage job completes without per-step hand-holding. |
| **REQ-C3** | The agent SHALL track where the user is in a longer journey and resume correctly. | "A chat has no concept of *where we are*." | The agent reports current stage and the next action. |
| **REQ-C4** | The agent SHALL offer an opinionated default path, eliminating the blank page. | "I'm staring at an empty box not knowing where to start." | The user always has a clear, recommended next step. |

---

## 6. Category D — Proprietary Knowledge & Grounding
*Anchors the reasoning engine to data the general model never saw and cannot guess.*

| ID | Requirement | Neutralizes | Acceptance test |
|---|---|---|---|
| **REQ-D1** | The agent SHALL ground answers in a curated, authoritative corpus (RAG), not internet averages. | "The general model already knows the public stuff." | Material answers derive from non-public or curated sources. |
| **REQ-D2** | The agent SHALL maintain domain data current to a known date, refreshed on a stated cadence. | "An LLM's training is stale." | The agent holds post-cutoff domain facts the base model lacks. |
| **REQ-D3** | The agent SHALL make claims traceable to authoritative sources. | "I can't trust a confident guess." | Material claims carry verifiable citations. |
| **REQ-D4** | The agent SHALL abstain or flag uncertainty outside its grounded knowledge rather than fabricate. | "It'll just hallucinate in a high-stakes spot." | Ungrounded queries return calibrated uncertainty, not invention. |

---

## 7. Category E — Integration, Action & Simulation
*The verb matters more than the noun. Advice is commoditized; doing the thing — and forecasting the thing — is not.*

| ID | Requirement | Neutralizes | Acceptance test |
|---|---|---|---|
| **REQ-E1** | The agent SHALL connect to the user's real systems of record and read/write actual data. | "The general model is a sealed box." | The agent performs a real read/write in an external system. |
| **REQ-E2** | The agent SHALL complete tasks, not merely describe them. | "ChatGPT gives me a wall of text I still have to action." | A real-world side effect is produced, not just text. |
| **REQ-E3** | The agent SHALL ingest the results of its own actions and adapt. | "Its advice is static and one-shot." | The agent adjusts based on outcome data it retrieved. |
| **REQ-E4** | The agent SHALL run methodology-bounded, quantified what-if and counterfactual simulations against the user's *actual* data ("retire three years earlier," "switch strategy," "change the diet"), returning a forecasted impact rather than generic pros and cons. | "It can only hand-wave at 'what if I did X instead.'" | A scenario yields a quantified, user-specific forecast traceable to the stated methodology. |

*REQ-E4 clears both master tests: a rigorous, data-constrained forecast is not reproducible by a ten-minute chat prompt (Displacement), and it rests on the user's proprietary data plus the house methodology rather than promptable behavior the platform ships natively (Absorption).*

---

## 8. Category F — Structured Deliverables & Artifacts
*A coach produces a roadmap and a scorecard. A chatbot produces text you must assemble yourself.*

| ID | Requirement | Neutralizes | Acceptance test |
|---|---|---|---|
| **REQ-F1** | The agent SHALL produce finished, domain-standard deliverables (plans, reports, scorecards, dashboards). | "I get prose I still have to turn into the actual thing." | Output is a usable artifact in the field's expected format. |
| **REQ-F2** | Deliverables SHALL follow a reliable, consistent, professional template every time. | "A general LLM's formatting is inconsistent." | Outputs are reproducibly structured. |
| **REQ-F3** | Artifacts SHALL be exportable in usable, portable formats. | "The output is trapped in a chat window." | Export to PDF/CSV/etc. functions on demand. |

---

## 9. Category G — Personalization & Adaptive Tailoring
*Generic advice is the tell of a wrapper. Constrained, situation-specific advice is the product.*

| ID | Requirement | Neutralizes | Acceptance test |
|---|---|---|---|
| **REQ-G1** | The agent SHALL constrain all output to the user's real situation (budget, constraints, context, history). | "It gives generic advice that ignores my specifics." | Output automatically reflects the user's known constraints. |
| **REQ-G2** | The agent SHALL adapt recommendations based on what has and hasn't worked for *this* user. | "Static advice that never learns." | Recommendations shift after logged outcomes. |
| **REQ-G3** | The agent SHALL learn and honor the user's preferences, depth, and cadence without re-asking. | "I have to re-specify how I want things every time." | Learned preferences are applied without re-prompting. |

---

## 10. Category H — Proactivity & Lifecycle Management
*A general LLM only acts when you open it. A service drives the cadence.*

| ID | Requirement | Neutralizes | Acceptance test |
|---|---|---|---|
| **REQ-H1** | The agent SHALL initiate check-ins, reminders, and nudges aligned to the user's journey. | "It only responds when I remember to ask." | The agent reaches out at the right moments unprompted. |
| **REQ-H2** | The agent SHALL surface relevant issues and opportunities before the user asks. | "It's purely reactive." | The agent flags pertinent items proactively. |
| **REQ-H3** | The agent SHALL track time-bound domain milestones and deadlines. | "I have to manage the whole timeline myself." | The agent enforces and reports against deadlines. |
| **REQ-H4** | The agent SHALL engineer a tangible, personalized "first win" within the opening session and the first week — a diagnostic finding, a revealed blind spot, or a completed deliverable — by design, not by chance. | "I'll try it, see nothing a free model can't do, and churn in week one." | A measurable activation event lands within 7 days for a defined majority of new users. |

*REQ-H4 is a design mandate rather than a standalone moat: its job is to surface the Category B/D/F advantages fast enough that the user feels them before the free-model habit reasserts. It clears Absorption (the win rides on proprietary state and deliverables) and is the explicit gate on the Trial→Retention transition the §16 sequencing guidance warns about.*

---

## 11. Category I — Trust, Safety, Accountability & Calibration
*In high-stakes domains, a confident wrong answer is worse than no answer.*

| ID | Requirement | Neutralizes | Acceptance test |
|---|---|---|---|
| **REQ-I1** | The agent SHALL communicate calibrated confidence and flag risk, avoiding confident wrongness. | "An LLM is confidently wrong, and I can't tell when." | Uncertainty is signaled and proportionate to the stakes. |
| **REQ-I2** | The agent SHALL enforce domain guardrails and a defensible point of view, refusing unsafe or non-compliant guidance. | "Free advice could be dangerous or flat wrong." | Known-bad inputs are caught and constrained. |
| **REQ-I3** | The agent SHALL recognize its limits and escalate to a human or expert when warranted. | "Who do I turn to when the AI is out of its depth?" | Escalation triggers fire at appropriate thresholds. |
| **REQ-I4** | The agent SHALL be auditable and explainable, producing a reasoning/source trail. | "It's a black box I can't defend to a regulator/board." | A decision trail exists for material outputs. |
| **REQ-I5** | A named entity or methodology SHALL stand accountably behind the output. | "Nobody is accountable for an LLM's guess." | Outputs carry a consistent, attributable point of view. |

---

## 12. Category J — Outcome Orientation & Measurement
*A general model answers questions. A coach owns the result with you.*

| ID | Requirement | Neutralizes | Acceptance test |
|---|---|---|---|
| **REQ-J1** | The agent SHALL establish the user's measurable objective at the outset. | "It's an aimless conversation." | A tracked goal exists for each user. |
| **REQ-J2** | The agent SHALL measure and report progress toward that objective over time. | "I have no sense of whether I'm getting anywhere." | A visible progress metric is maintained. |
| **REQ-J3** | The agent SHALL frame itself as accountable to the *outcome*, not merely the response. | "It answers, but it doesn't own anything." | Success is defined by user outcome, not response quality alone. |
| **REQ-J4** | The agent SHALL quantify and surface *its own* contribution — hours saved, errors caught, decisions accelerated, dollar impact — on a recurring cadence, reframing the subscription from expense to ROI. | "Why pay $100 when ChatGPT is $20?" | A periodic, user-specific value report ties measurable impact to the agent's own actions. |

*REQ-J4 is the only requirement that attacks the **price** objection head-on, and it is distinct from J2: J2 tracks the user's progress toward their goal; J4 tracks the agent's contribution to it. It clears Displacement (a chat cannot meter its own longitudinal ROI) and clears Absorption conditionally — the telemetry rides on the agent's own workflow, which the platform does not see.*

---

## 13. Category K — Data Governance, Privacy & Ownership
*Privacy is only a differentiator if it genuinely exceeds what the base provider already offers.*

| ID | Requirement | Neutralizes | Acceptance test |
|---|---|---|---|
| **REQ-K1** | The agent SHALL offer data-handling guarantees that demonstrably **exceed** the base provider's defaults — otherwise this is not claimed as a differentiator. | "My data is just as safe typing into ChatGPT directly." | Documented handling is stricter or clearer than the base API default. |
| **REQ-K2** | The user SHALL own their data and be able to export or delete it on demand. | "I'm afraid of getting locked in." | Export and deletion function on request. |
| **REQ-K3** | The agent SHALL meet the regulatory bar of its domain (e.g., HIPAA, FERPA, financial, legal) where applicable. | "Can I even legally use a general LLM for this?" | Relevant compliance attestations exist and hold. |

---

## 14. Category L — Reliability, Consistency & Methodological Integrity
*A general model is brilliant but variable. A professional tool has a quality floor.*

| ID | Requirement | Neutralizes | Acceptance test |
|---|---|---|---|
| **REQ-L1** | The agent SHALL deliver consistent-quality output for equivalent inputs — a guaranteed quality floor. | "Sometimes the general model is great, sometimes useless." | Repeated runs stay within an acceptable tolerance band. |
| **REQ-L2** | The agent SHALL apply its named "house" methodology consistently, not ad hoc. | "I get generic, eclectic answers with no through-line." | Outputs trace to the stated framework/methodology. |
| **REQ-L3** | The methodology SHALL be versioned and deliberately improved, not silently drifting. | "What changed, and why is it different today?" | The active methodology version is identifiable. |

---

## 15. Category M — Compounding Moat & Retention (Durability)
*The requirements that make the value un-absorbable and switching genuinely costly.*

| ID | Requirement | Neutralizes | Acceptance test |
|---|---|---|---|
| **REQ-M1** | The agent SHALL operate a data flywheel: anonymized outcome data makes it objectively better than any general model *for its specific goal*. | "The lab will just catch up and match this." | Measurable, niche-specific improvement attributable to usage data. |
| **REQ-M2** | The agent SHALL accumulate state, artifacts, and history such that it becomes the user's system of record. | "Switching is free." | Leaving means forfeiting real accumulated value. |
| **REQ-M3** | The agent's core value SHALL rest on proprietary data, real integration, or accountability — not on promptable behavior the platform can ship natively. | "Won't ChatGPT just add a feature for this?" | Core value passes the Absorption Test. |
| **REQ-M4** | Where the domain allows, the agent SHALL connect users into a gated cohort on the same methodology — privacy-preserved shared benchmarks, peer progress, and outcomes — so belonging compounds with use. | "A general LLM is a solitary tool; leaving costs me nothing social." | An active cohort exists and supplies benchmarks a solo user cannot self-generate. |

*REQ-M4 is the most absorption-resistant item in the spec: a platform can ship memory and connectors, but it cannot hand you the peer cohort assembled around your specific methodology. It clears Displacement trivially (no prompt produces a community) and Absorption structurally. **Caveat:** it is domain-gated — strong for fitness, admissions, and founder cohorts; weak or inappropriate where users are confidential or adversarial (e.g., competing M&A clients).*

---

## 16. Prioritization Matrix

Mapping every requirement to its tier and to the customer-journey stage it defends.

| Journey stage | Question the customer is asking | Tier | Requirements |
|---|---|---|---|
| **Trial** (overcome inertia) | "Is this even worth leaving my general model for?" | T0 | A1, A2, A3, B1, H4 |
| **Selection** (choose over default) | "What does this *do* that Claude doesn't?" | T1 | C1–C4, D1–D4, E1–E4, F1–F3 |
| **Retention** (why stay) | "Why not cancel and go back to the general model?" | T2 | B2, B3, G1–G3, H1–H3, J1–J4, L1–L3, M1, M2, M4 |
| **Trust gate** (enter the domain at all) | "Can I responsibly rely on this for something that matters?" | TG | I1–I5, K1–K3 |
| **Durability** (un-absorbable) | "Won't the platform just absorb this in a year?" | T2 | E4, M1, M2, M3, M4, and any T1 item that also clears the Absorption Test |

**Sequencing guidance:** A product that nails T1 but fails T0 dazzles in the demo and loses the user in week one. A product that nails T0+T1 but fails T2 wins the trial and churns at renewal. Win all three, and the trust gate, before claiming the domain.

---

## 17. Anti-Requirements (Common Traps)

These *feel* like reasons to choose a specialist but fail the Displacement or Absorption Test. They are not requirements, and a product resting on them is the thin wrapper the skeptical customer correctly rejects.

| Trap | Why it fails |
|---|---|
| **Raw domain expertise** | Assumed, not differentiating. The general model has the public knowledge; the rest is retrievable. Fails Displacement. |
| **A persona or brand voice** | Reproducible with a one-paragraph system prompt. Buys a launch, not retention. Fails Displacement. |
| **A clever prompt** | This *is* the thing the customer can copy in ten minutes. Give it away to sell the real product. Fails Displacement. |
| **"Fine-tuned on domain text"** with no state, action, or grounding | A better answer to a single question — still a sealed chat. Fails Absorption. |
| **Marginally nicer writing or formatting** | Inside the platform's variance, and being absorbed. Fails both. |
| **Being cheaper** | A race to the bottom, not loyalty. Price competes; it does not retain. |
| **Epistemic closure as a moat** (hard-refusing benign adjacent requests to "reinforce authority") | Lowers requisite variety and drives users back to the general tab. Scope discipline belongs in D4/I3/L2 — refuse *authoritative answers outside competence*, not *lasagna recipes*. |
| **Raw memory treated as a permanent moat** | Persistent memory is real value but is being absorbed natively by the platforms. Counts as table stakes, not durability. See M3. |
| **Privacy as an unqualified differentiator** | Base providers already offer no-training and isolation tiers. Only a differentiator if it demonstrably exceeds them. See K1. |

---

## 18. Master Acceptance Rule

> **A specialized AI agent is fit to compete against a general-purpose LLM only when its value lies in what the model cannot structurally provide on its own — and will not be able to next year either: persistent compounding state, executed action inside the user's systems, finished accountable deliverables, owned outcomes, and a defensible data and trust posture. Everything else is a prompt the customer can write themselves.**

The standing test for any proposed feature:
> *Does this remove friction, own an outcome, or compound state in a way a ten-minute prompt cannot replicate and the platform will not absorb within a year?*
> If not, it is not a requirement — it is marketing.
