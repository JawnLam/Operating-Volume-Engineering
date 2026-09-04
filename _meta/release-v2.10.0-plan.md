---
type: Fleeting
timestamp: "2026-08-28T00:00:00Z"
Item_ID: ove-release-v2-10-0-plan
title: "OVE v2.10.0 — Release Plan (pre-registered)"
Date_Added: 2026-08-28
Date_Modified: 2026-08-28
Needs_Processing: false
---

# OVE v2.10.0 — Release Plan (pre-registered before build)

**Operator directive (2026-08-28):** upgrade OVE to be better at what it does best — the institution side — by teaching it to *delegate the factory side*. When OVE designs any new OV, it must identify which parts of that OV's work are ICM-shaped (staged, terminating, spec-completable pipelines per Van Clief & McDermott's Interpretable Context Methodology, arXiv 2603.16021) and **requisition** a future specialist OV ("Interpretable Context Methodology Engineering," ICME — to be built later) to create those parts, rather than designing them itself. The **only** ICM knowledge OVE may hold is the skill of identifying *when* an ICM is needed; that detection criterion is therefore the release's paramount deliverable and must be clear and comprehensive. Operator's four scoping answers (recorded via question round, 2026-08-28): the motivating example was a rhetorical placeholder — detection must be domain-blind; the mechanism ships as a **general cross-OV specialist-delegation convention** with ICME as its first registered instance; pre-ICME detection hits **requisition and bank** (host OVs ship functional with declared placeholder mounts); this is a **single-purpose release** (the banked ICM-inspired efficiency trio does not ride along).

**Design thesis (recorded for the changelog):** the formal relation established in this engagement is OV ⊇ ICM in expressive power, with ICM epistemically superior on its home ground (guarantees-by-construction vs. discipline-by-governance). A superset that knows where its subsets excel should *stop building them* — focus-by-delegation. F9 already teaches OVE to say "this whole thing isn't an OV"; v2.10.0 teaches the finer-grained version: "this *part* of an OV isn't OV-work."

## What ships (scope)

A **minor, additive** release: **v2.10.0**.

1. **`_meta/CONVENTIONS.md` — Convention 16: Specialist Delegation.** The general mechanism, subject-agnostic: a **specialist OV** is an OV whose product is a class of sub-artifact mounted inside other (host) OVs; a **detection trigger** is the criterion a designing or auditing OV applies to recognize that specialist's class of need; a **requisition** is the formal handoff artifact specifying the need; a **mount** is the declared location where the fulfilled sub-artifact lives in the host; **fulfillment** is a specialist-OV engagement consuming a requisition and producing the mount. The load-bearing **boundary rule**: the generalist knows *only* the detection trigger and the requisition interface — a requisition specifies WHAT/WHY/constraints, never internal design (for ICM: never stages, folder layouts, or context budgets); writing specialist-internal content into a requisition is failure mode F18. Mount contract modeled on Convention 11's precedent: declared in the host manifest, vendored in a declared folder, versioned/pinned, updated only by specialist re-engagement. Pre-fulfillment state: declared placeholder mount + banked requisition; the host ships functional, with the requisition recording what capability is deferred. Registry of specialists lives in `_design-engine/_meta/SPECIALISTS.md`.
2. **NEW `_design-engine/_meta/SPECIALISTS.md`** — the specialist registry and the release's centerpiece. General entry format (specialist name, sub-artifact class, status `planned | exists`, detection trigger, requisition notes, mount convention), followed by the first entry — **ICME (status: `planned`)** — carrying the **canonical ICM detection criterion**, comprehensive and domain-blind:
   - **The factory signature** (all five structural marks must hold): (a) *terminating* — a run with a defined deliverable; done-ness is structural, not judged; (b) *spec-completable in advance* — inputs, steps, and pass conditions enumerable before the run starts, with no mid-run elicitation beyond parameter values; (c) *linear or near-linear* — fixed stage order, no state-driven dispatch or mid-run reentry; (d) *consistency-preferred* — run N should resemble run 1; learning-from-precedent inside the process is unwanted; (e) *run-scoped state* — nothing inside the run needs to survive into host memory except the deliverable and its filing record.
   - **Counter-indicators** (any one routes the candidate back to OV-native design): conversational elicitation whose next question depends on the last answer; state accumulating across runs inside the process; dispatch or branching on case state; the need for mid-process cross-session resume ("where were we?" must be answerable inside the process); normative walls or refusal behavior *inside* the process — walls belong to the host, which imposes them on the requisition as output constraints.
   - **The hybrid-split rule** (where most real candidates land): when a candidate mixes judgment and production, split it — the elicitation/judgment half stays an OV-native activity that *parameterizes and invokes* the pipeline half; the pipeline half is requisitioned. Host-side activity gathers what the factory consumes; the factory produces what the host files.
   - **The acid test:** would run-fresh amnesia be malpractice for this piece of work? If forgetting between runs is harmless, it is factory work; if forgetting is the failure mode, it is institution work.
   - **Design-time markers** (where to look during an engagement): Q1 answers weighted operational/procedural; CQ10 deliverables produced repeatedly to a template; Q7 candidate activities whose descriptions reduce to fixed step lists or "generate X from Y."
   - **Classification output:** every candidate activity is classified `ov-native | requisition | hybrid-split`, and the classification is logged in the design record — including negative classifications, so a shipped pipeline-shaped activity is always a *decided* thing, never a default.
3. **NEW `_design-engine/_templates/TEMPLATE-specialist-requisition.md`** — the general requisition skeleton: host OV + engagement; specialist + sub-artifact class; the need (purpose, invoking host activity, trigger conditions, cadence/volume); the **interface contract** (inputs the host supplies — which Items/files/parameters; outputs the host receives — deliverable class, where filed, what host Type records it); **host-imposed constraints** (output requirements, confidentiality walls, provenance/tagging obligations the deliverable must carry); consistency posture; explicit out-of-scope declaration ("internal design — stages, structure, budgets — belongs to the specialist; content of that kind in this document is an F18 defect"); status ledger (`banked | fulfilled`, fulfillment version). One filled example rendered in a deliberately un-Polaris fiction.
4. **`_design-engine/04-SCHEMA-DESIGN.md` — Q7 extended with the specialist sweep:** after custom activities are defined, each is swept against every registry trigger and classified; classifications logged.
5. **`_design-engine/BOOTSTRAP-NEW-OV.md`** — the sweep wired into the execution plan: run after schema lock/cartridge shape (before ARTIFACT-DRAFT); requisitions and placeholder mounts added to the Step 5 artifact list; a quality-gate line (every pipeline-shaped candidate carries a logged classification; every `requisition` classification has a requisition document and a declared mount).
6. **`_design-engine/03-DESIGN-PROTOCOL.md` — §4 Audit Mode:** the audit walk gains a specialist-sweep step over an existing OV's activities — advisory findings ("candidate requisition") recorded, never auto-refactored.
7. **`_design-engine/07-SHIPPING-CHECKLIST.md` — Phase 3.13 (HARD STOP — conditional):** fires only when the engagement's design record contains specialist classifications; verifies every requisition is complete-per-template and HOW-free, every mount declared in the manifest, every placeholder honest about deferred capability; `n-a` logged otherwise.
8. **`_design-engine/01-WHAT-IS-AN-OV.md` — new section "Composed OVs":** the conceptual home — a host OV may contain mounted sub-artifacts built by specialist OVs; the institution/factory composition, stated subject-agnostically.
9. **`_design-engine/_templates/TEMPLATE-ov-manifest.md`** — gains a declared `Sub_Artifact_Mounts` list (name, class, specialist, status, mount path), empty by default, mirroring `Knowledge_Mounts`.
10. **`_design-engine/_meta/FAILURE-MODES.md` — F18: Specialist-boundary violation.** House format. Primary form: generalist overreach — the requisition (or the design conversation) contains specialist-internal design; OVE drafting stage structure is the canonical instance. Sibling form noted within the entry: missed detection — factory-shaped work force-fitted through institution categories (the fine-grained F9). Prevention: Convention 16's boundary rule, the sweep hooks, Phase 3.13's HOW-free check.
11. **Wiring and records:** `00-START-HERE.md` load-table row for `SPECIALISTS.md`; `TRACEABILITY.md` rows (Convention 16 and the sweep → manual walks → F18); `VERSION.md` + `CHANGELOG.md` at 2.10.0 with this governance record; `Date_Modified` synced on every edited file; identifiers table (release-date row included — the v2.9.0 banked drift gets corrected here as an in-scope records item).

## Out of scope (banked or elsewhere)

- **Building ICME** — a separate future design engagement; its registry entry ships `planned`.
- **Building any ICM** — nothing pipeline-internal ships; doing so would violate the release's own boundary rule.
- **The efficiency trio** (context budgets, Why-column, section routing) — stays banked per the operator's single-purpose answer.
- **Retrofitting existing OVs** (e.g., sweeping Spreadwright's activities) — audit-mode findings only, on each OV's next engagement.
- **Mechanical validator checks** for Convention 16 / Phase 3.13 — manual-first; banked with the C20/C21 class.
- **Folder rename `-v2.9` → `-v2.10`** — Convention 7 doctrine applies; execution is the operator's call, as with the prior two renames.

## QC plan (pre-registered)

- **Verification:** the companion eval (`release-v2.10.0-eval.md`) — mechanical criteria plus one behavioral probe — run post-build by an independent evaluator agent (fresh instance, no drafting role), binary verdicts with cited evidence.
- **The behavioral probe** uses a fresh fiction (not the operator's placeholder name, per instruction): a candidate-activity classification scenario mixing clear OV-native, clear factory, and hybrid cases.
- **No open-ended crucible.** Evaluator observations beyond the criteria bank to the next release's hopper.
- **Severity rubric:** any eval criterion FAIL = blocking (fix, re-run the eval in full); notes outside the criteria = banked.
- **Stopping rule:** the same criterion failing twice for distinct causes escalates to the operator.

## Definition of Done

All scope items 1–11 on disk; the eval run by an independent evaluator with every criterion PASS; 0 blocking; banked findings recorded in `release-v2.10.0-eval-results.md`; VERSION and CHANGELOG agree on 2.10.0; the plan/eval commit precedes the build commit in history; all work committed and pushed.
