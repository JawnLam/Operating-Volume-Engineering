---
Item_Prototype: Fleeting
Item_ID: ove-proposal-kaov
Title: "Design Note — Knowledge-Augmented Operating Volume (KAOV)"
Date_Added: 2026-06-25
Date_Modified: 2026-06-25
Needs_Processing: false
Status: DRAFT — for operator review. NOT adopted canon. No engine edits made.
Supersedes: nothing
Source_PRD: _proposals/KAOV-PRD-source.md
Conformance_ref: _proposals/OKF-conformance-notes.md
---

# Design Note — Knowledge-Augmented Operating Volume (KAOV)

> **Status: DRAFT for review.** This note proposes integrating Google Cloud's
> Open Knowledge Format (OKF) into OVE as a runtime *data plane*. It is a design
> proposal, not adopted convention. Nothing in `_design-engine/` has been changed.
> Decide the open questions in § 7 before any rule/schema edits.

## 0. Provenance

The substance originates in a PRD ("The Knowledge-Augmented Operating Volume (KAOV)
Architecture") authored in a Gemini session and captured verbatim at
`_proposals/KAOV-PRD-source.md`. Two external claims were independently verified
before drafting this note:

- **OKF is real.** Google Cloud's Open Knowledge Format, **v0.1 Draft** — a
  vendor-neutral markdown spec (one `type` frontmatter field required by the spec;
  directory of **concept** documents; producers may add keys, consumers tolerate
  unknown keys). Repo: `GoogleCloudPlatform/knowledge-catalog`, `okf/SPEC.md`.
  **The full spec + reference implementation were read directly and distilled into
  `_proposals/OKF-conformance-notes.md`** — which is the binding format contract for
  this work and corrects four format errors in the source PRD (see § 8 below).
- **The PRD reads OVE accurately.** Its references to F13 (`_meta/FAILURE-MODES.md`),
  P11 Propose-don't-decide (`02-DESIGN-PRINCIPLES.md` §140), `03-DESIGN-PROTOCOL.md`,
  `_ov-manifest.md`, and `_design-state.md` / `_design-decisions.md` all resolve to
  real surfaces. The `08-` engine slot it proposes is genuinely the next free number
  (engine is currently 00–07).

The PRD's supporting citations (Liu et al. "Lost in the Middle" arXiv:2307.03172;
Yao et al. "ReAct" arXiv:2210.03629) are both real, peer-known papers.

## 1. The one-sentence abstraction

**A KAOV is an OV that, instead of baking all source knowledge into its static
corpus at design time, mounts one or more external OKF bundles as a read-only data
plane and retrieves from them at session runtime under a bridge protocol that
preserves OVE's provenance discipline.**

In OVE's own terms: OVE is the control plane (state machine, lifecycle, propose-don't-decide,
F13 source discipline); OKF is the data plane (progressively-disclosed knowledge graph).
The bridge is a new, *opt-in* engine chapter that governs how the control plane is
permitted to touch the data plane.

## 2. Why this is a foundational change, not a feature

OVE today has a single, load-bearing model of what an OV *is*: a **self-contained,
shippable markdown corpus** (README tagline: "self-contained markdown corpora").
The entire F13 pipeline exists to make sources *baked-in and verified by ship time*:

- INTERVIEW captures sources → `_source-inventory.md`
- ARTIFACT-DRAFT is gated until every source is located + read (`03-DESIGN-PROTOCOL.md`
  Step 4.5)
- SHIP-PREP Phase 3.7/3.8 manually verifies every cite against canonical source and
  logs `_citation-audit-log.md`

KAOV breaks that model in one specific place: **sources move from design-time inputs
that get verified once and frozen, to a runtime data plane the *shipped* OV queries
live.** That is not a new template or a new check — it changes the provenance
guarantee OVE makes. This is exactly the class of change `02-DESIGN-PRINCIPLES.md`
and Convention 10 are built to gatekeep, which is why it gets a design note first.

## 3. Coexistence with existing surfaces

### 3.1 Convention 10 (Standalone Sufficiency) — the crux

Convention 10 demands every OV defeat *"would a general LLM be better for this work?"*
via the Displacement and Absorption master tests, with ≥1 moat commitment from
{REQ-E4, M1, M2, M3, M4}.

KAOV cuts **both ways** here, and the design must resolve the cut deliberately:

- **Strengthens the moat.** A mounted enterprise OKF graph is, almost by definition,
  a proprietary-knowledge-integration moat. KAOV could become a *first-class
  mechanism* for satisfying the M-series moat items — "this OV is bound to a curated
  knowledge graph a general LLM cannot see." That is a genuine Displacement win.
- **Threatens self-containment.** A general LLM pointed at the same mounted OKF folder
  gets the same data. If the OV's only value is "it reads the folder," it fails
  Absorption — the substrate's anti-trap against "raw-memory-as-permanent-distinction"
  applies directly. The moat has to live in the *control-plane discipline* (the
  retrieval protocol, the state machine, the provenance contract), not in mere access
  to the bytes.

**Disposition required:** a KAOV's `posture.yaml` must claim its moat on the
control-plane + curation, and explicitly disclaim "access to the mount" as the moat.
A new validator sub-check (see § 6) should flag any KAOV whose sole moat commitment
reduces to data access.

### 3.2 Convention 8 (four content zones) — where do mounts live?

Convention 8 partitions every OV into four zones (engine / operator-content /
operator-private / generated). An OKF mount is a **fifth kind of thing**: external,
read-only, not authored by the OV, possibly not shipped with it. The note's
recommendation (§ 5) is to make mounts an explicit new zone — "Mounted Data Plane
(read-only, external)" — with its own `.gitignore` posture (mounts are typically
*referenced, not vendored*, echoing Convention 9).

### 3.3 Convention 9 (ship-by-reference) — KAOV is its generalization

Convention 9 already handles "source material we cite but do not ship" (sensitive
sources, ship-by-reference). KAOV's `Knowledge_Mounts` is the structured,
runtime-queryable generalization of exactly this. **Reuse, don't reinvent:** the
mount declaration should extend the Convention 9 reference pattern rather than stand
up a parallel mechanism. A Convention-9 sensitive source and a KAOV mount are the
same species (external, referenced, provenance-tracked) at different fidelities.

### 3.4 F13 / source-inventory — FR 3.2 is F13 at runtime, but weaker

The PRD's FR 3.2 (every drafted claim cites its OKF source) is F13 extended to the
data plane. The natural fit is real — with **two corrections from the real spec**
(see `OKF-conformance-notes.md` §6):

- **Citation form.** The PRD appended `[Source: okf/network/firewall_rules.md]` to
  claims. That is **not** OKF. OKF citations are markdown links — inline file-relative
  links to the source **concept**, and/or a numbered `# Citations` section (SPEC §8).
  KAOV's sourcing rule must use the real convention, or it produces non-interoperable
  bundles. The "claim → source" tie still holds; only the syntax changes.
- **Unit name.** The thing cited is a **concept** (one markdown doc, addressed by its
  **concept ID** = path minus `.md`), not a "node file."

The deeper, honest gap the note must not paper over:

> F13's guarantee is *"verified against canonical source at ship time."* KAOV's
> guarantee is *"links the concept that was read at draft time."* Because the data
> plane is **external and mutable** — and OKF concepts carry a `timestamp` and live
> under git/`log.md` precisely because they change — a concept can change *after* the
> OV ships. The runtime citation proves *where* a claim came from, not that it still
> matches the source. That is strictly weaker than F13's ship-time verification. **And
> OKF itself is v0.1 Draft (§11 permits breaking changes), so the format can shift too.**

This is the single biggest correctness question in the proposal. Options to close it
(for § 7 decision), now sharper given what OKF actually provides: pin each cited
concept by its frontmatter `timestamp` and/or the mount's git SHA at draft time;
record `okf_version` per mount; declare KAOV citations as "provenance pointers, not
verified cites" with the downgrade documented; or require a boot-time re-verification
pass over the concepts a session depends on (diff `timestamp`/SHA, re-confirm if changed).

### 3.5 Progressive disclosure (FR 3.1) — already native to OVE

The index→concept discipline mirrors how the engine already routes itself
(`00-START-HERE` → numbered chapters; parent-child skill structure). Applying it to
*data* is new but idiomatic. Low risk. The "must read `index.md` before any concept"
rule is a clean, enforceable invariant — **but note** OKF makes `index.md` *optional*
and consumer-synthesizable (SPEC §6), so this is an **OVE-imposed discipline stricter
than OKF requires**, not an OKF mandate. Frame it that way.

## 4. Mapping the PRD's three FRs onto OVE mechanisms

| PRD requirement | Closest existing OVE surface | Verdict |
|---|---|---|
| FR 3.1 Progressive disclosure (index→concept) | Engine self-routing; parent-child disclosure | **New surface, idiomatic.** Adopt as bridge-protocol invariant (stricter than OKF — index.md is optional in OKF). |
| FR 3.2 Explicit sourcing (link the source concept) | F13 / `_source-inventory.md` / Phase 3.7 cite audit | **Extension, but weaker guarantee.** Adopt with § 3.4 resolution + OKF `# Citations`/markdown-link form (not `[Source: …]`). |
| FR 3.3 `Knowledge_Mounts` in manifest | Convention 9 ship-by-reference; `_ov-manifest.md` schema | **New schema field, reuses Convention 9 pattern.** Adopt. |

## 5. Core-vs-archetype recommendation

**Recommendation: ship KAOV as an opt-in capability layer (a new "knowledge-augmented"
archetype dimension), NOT a core engine convention.**

Rationale:

1. **Convention 10 says "every OV, no exceptions."** Folding KAOV into core would
   force *every* OV — most of which are and should remain self-contained corpora — to
   reckon with an external data plane. Wrong default. The README identity ("self-contained")
   should remain the default; KAOV is the deliberate exception.
2. **The archetype-fork precedent already exists** (v2.0). The manifest already carries
   `ove_OV_Archetype` (`finite_horizon | practice`). KAOV is naturally a *second,
   orthogonal* axis — `knowledge_source: self_contained | knowledge_augmented` — that
   an OV opts into, leaving the lifecycle and the static-corpus default untouched.
3. **Blast radius containment.** As an opt-in layer, the new `08-KNOWLEDGE-RETRIEVAL.md`
   chapter and the `Knowledge_Mounts` schema are read/enforced *only* when an OV
   declares `knowledge_augmented`. Self-contained OVs never load the bridge protocol —
   no context cost, no behavior change, no new failure surface for the 99% case.

The alternative (Convention 11, every OV becomes KAOV-capable) is documented in § 7
as Option B for completeness, but I do not recommend it: it raises the floor for every
OV to satisfy a data-plane discipline most will never use, and it muddies the
self-contained identity that Convention 10 just spent v2.2.0 hardening.

## 6. Anticipated downstream verification surface

If adopted as the recommended opt-in layer, the work touches:

- **New engine chapter:** `_design-engine/08-KNOWLEDGE-RETRIEVAL.md` — the bridge
  protocol (FR 3.1/3.2/3.3 as enforceable rules + the read-index-before-concept invariant
  + the provenance-pointer contract from § 3.4). Must encode the OKF conformance facts
  from `OKF-conformance-notes.md` (concept/concept-ID terms, `# Citations`/markdown-link
  citation form, file-relative links, permissive consumption).
- **Manifest schema:** add `ove_Knowledge_Source` flag + a `Knowledge_Mounts` array to
  `TEMPLATE-ov-manifest.md`. Each mount: `bundle_root`, `index_path` (optional — OKF
  index.md is optional), `okf_version`, `provenance`, `ship_disposition: vendored |
  referenced`, optional `pin` (git SHA or per-concept `timestamp`).
- **Conventions:** extend Convention 8 with the "Mounted Data Plane" zone; cross-link
  Convention 9 as the parent pattern; add a Convention 10 disposition rule (moat may
  not reduce to mount access).
- **Lifecycle:** `03-DESIGN-PROTOCOL.md` gets a KAOV-only state (KNOWLEDGE-MOUNT, gating
  ARTIFACT-DRAFT until declared mounts resolve + are confirmed OKF-conformant per
  conformance-notes §9 — every concept has a non-empty `type`).
- **Validator:** new checks — `C15` (mounts resolve; each mounted bundle passes OKF §9
  conformance; `ship_disposition`/`okf_version` valid), `C16` (KAOV citations are real
  markdown links into declared mounts only — no `[Source: …]` pseudo-syntax;
  workspace-isolation per FR 3.3), and the Convention-10 moat-not-mere-access flag.
- **VALIDATION-CHECKLIST.md / FAILURE-MODES.md:** new failure mode (F14? — "stale mount:
  shipped OV cites a concept whose `timestamp`/SHA — or whose OKF format version — has
  since changed") tied to the § 3.4 gap.
- **Docs:** README + `01-WHAT-IS-AN-OV.md` get a "self-contained vs knowledge-augmented"
  paragraph so the identity stays honest.
- **Dogfood:** per the repo's habit of shipping a worked example per major feature, a
  minimal KAOV cartridge mounting a toy OKF bundle would prove the loop end-to-end.

Version implication: this is a **breaking minor at least** (new manifest fields, new
zone) — candidate **v2.3.0** if opt-in, or a major if any existing surface changes
semantics.

## 7. Open questions for operator decision

1. **Adopt the opt-in archetype recommendation (§ 5 Option A), or core Convention 11
   (Option B)?** — recommend A.
2. **Resolve the runtime-provenance gap (§ 3.4):** content-hash pin at draft time /
   provenance-pointers-not-verified-cites / boot-time re-verification — which contract?
3. **Mount ship-disposition default:** vendored (copied into the OV, self-contained
   preserved) or referenced (external, lighter, but breaks self-containment)?
4. **Scope of v1:** full bridge protocol + validator, or a minimal `08-` chapter +
   manifest field first, with validator/lifecycle deferred?
5. **Does KAOV need its own standalone-sufficiency sub-posture**, given it changes the
   Absorption story?

Once these are decided, the next thread can move from design to rule/schema edits with
a contained, reviewed blast radius.

## 8. OKF conformance corrections (audit of the source PRD)

The full OKF v0.1 spec **and** reference implementation were read directly (2026-06-25)
and distilled into `_proposals/OKF-conformance-notes.md` (the binding format contract).
The architecture in the source PRD is sound; its **format details were non-conformant
in four ways**, all corrected in this note and the conformance doc:

| # | Source PRD | Real OKF | Where corrected |
|---|---|---|---|
| 1 | "Node File" / `concept_A.md` | The unit is a **Concept**, addressed by **Concept ID** (path minus `.md`) | §§3.4–3.5, §4, §6 |
| 2 | Frontmatter "type, tags, **dependencies**" | Required = `type` (spec) / `type`+`title`+`description`+`timestamp` (reference validator). `dependencies` invented. | conformance §3 |
| 3 | Cite via `[Source: path]` appended to claims | `# Citations` section + numbered markdown links, and/or inline file-relative concept links (SPEC §8) | §3.4, §6, conformance §6 |
| 4 | Bundle-prefixed link paths | **File-relative** links (matches every real bundle + GitHub); SPEC §5.1 nominally recommends `/`-absolute but the reference tooling forbids `/` | conformance §5 |

**Two contradictions inside Google's own repo** (spec ⊥ reference code) are resolved by
producing the **stricter superset**: emit all four reference-required frontmatter keys,
and use file-relative links. That satisfies the permissive spec consumers *and* the
strict reference tooling simultaneously. See conformance-notes §3 and §5.

**Status caveat:** OKF is **v0.1 Draft** and §11 permits breaking changes at a major
bump. Each `Knowledge_Mounts` entry records `okf_version`; the § 3.4 provenance gap now
covers format drift, not just content drift.
