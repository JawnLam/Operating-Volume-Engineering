---
type: Fleeting
timestamp: "2026-06-25T00:00:00Z"
Item_ID: ove-engine-08-knowledge-retrieval
title: "OVE Engine — 08 Knowledge Retrieval (the OKF bridge)"
Date_Added: 2026-06-25
Date_Modified: 2026-06-25
Needs_Processing: false
doc_type: design-engine
role: knowledge-retrieval
scope: subject-agnostic
updated: 2026-06-25
---

# 08 — KNOWLEDGE RETRIEVAL (the OKF bridge)

> **How a knowledge-augmented OV is permitted to touch its data plane. The control plane (this engine, the lifecycle, the rules of engagement) governs what the AI *does*; the data plane (a vendored OKF knowledge bundle) is what the AI *knows*. This chapter is the bridge between them — and the discipline that keeps the bridge from re-introducing the two failures OVE exists to prevent: context exhaustion and fabrication.**

## When this chapter applies

Only when the OV's manifest declares `ove_Knowledge_Source: knowledge_augmented` (Convention 11). The default is `self_contained`: all knowledge is baked into the OV's own corpus at design time and verified by ship (the F13 source pipeline, `02-DESIGN-PRINCIPLES.md` + `07-SHIPPING-CHECKLIST.md` Phase 3.7). A self-contained OV mounts nothing and may skip this chapter entirely.

A **knowledge-augmented OV (KAOV)** additionally mounts one or more **OKF v0.1 bundles** as a read-only data plane and retrieves from them at session runtime under the protocol below.

## Why the data plane is separate from the control plane

Large domains break the "bake everything into the corpus" model: you cannot load a 5,000-concept enterprise catalog into a session and still reason well. Research on long-context degradation (the "Lost in the Middle" effect — recall accuracy collapses when relevant facts are buried in a large flat context) makes the flat-load approach actively harmful, not merely expensive. The fix is **progressive disclosure**: keep the knowledge in a structured, hierarchical bundle and pull only the slice a task needs.

OVE adopts Google Cloud's **Open Knowledge Format (OKF)** for that bundle rather than inventing a format. The reason is integration, not convenience: an OKF bundle is plain markdown that *any* OKF-speaking producer, consumer, browser, or graph viewer can use. A KAOV's knowledge is therefore a portable asset, not a lock-in. The binding format facts live in `_proposals/OKF-conformance-notes.md`; the ones a session must obey are restated below.

## What a mount is

Each mount is one **vendored** OKF bundle living under the OV's `_knowledge/` zone:

```
<OV root>/
├── _ov-manifest.md            ← declares ove_Knowledge_Source + Knowledge_Mounts
└── _knowledge/
    └── <bundle-slug>/         ← one vendored OKF bundle = one mount
        ├── index.md           ← OKF directory listing (progressive disclosure)
        ├── log.md             ← optional OKF update history
        ├── <concept>.md       ← OKF concept documents
        └── <subdir>/ …
```

**Vendored is mandatory** (Convention 11): the bundle's bytes are copied into the OV and ship with it. A KAOV is still a self-contained corpus — the data plane is a curated, version-pinned part of that corpus, not a live external dependency. This is what preserves Convention 10's Absorption story: the moat is the control-plane discipline plus the curated/vetted mount, never bare access to public bytes.

The manifest's `Knowledge_Mounts` array records, per mount: `bundle_root`, `okf_version`, `provenance`, `ship_disposition: vendored`, and `pin` (the git SHA and/or per-concept `timestamp` baseline the bundle was vetted against).

## OKF facts a session must obey

These are Google's spec, not OVE's invention. Matching them is what keeps the bundle interoperable.

- **The unit is a Concept** — one markdown document — addressed by its **Concept ID** (file path within the bundle, `.md` removed: `tables/users.md` → `tables/users`). Never call it a "node."
- **`index.md` and `log.md` are reserved.** `index.md` is a directory listing (no frontmatter, except an optional `okf_version` at the bundle root); `log.md` is update history. Every other `.md` is a concept.
- **Required frontmatter:** every concept has a non-empty `type`. Well-formed concepts also carry `title`, `description`, `timestamp` (and `resource` when they map to a real asset). Be **permissive on read**: never reject a concept for missing optional fields, unknown `type`, unknown extra keys, or broken links.
- **Links and citations are standard markdown links, written file-relative** (`../tables/blocks.md`), never leading-slash. Citations go under a `# Citations` heading and/or inline-link the source concept. The `[Source: <path>]` pseudo-syntax is **not OKF** — never emit it.

## The bridge protocol — four rules

### Rule 1 — Progressive disclosure (read the index before any concept)

The AI MUST read a directory's `index.md` before reading any concept beneath it, descending one level at a time: bundle-root `index.md` → subdirectory `index.md` → the specific concept. It MUST NOT open a concept it reached by guessing a path.

> OKF makes `index.md` *optional* and consumer-synthesizable. OVE makes **reading the index first mandatory** — a discipline stricter than OKF requires, because the whole point of mounting (rather than flat-loading) is to filter relevance before spending context. If a directory genuinely has no `index.md`, the AI synthesizes one in working memory by listing the directory before reading concepts; it does not skip the filtering step.

### Rule 2 — Workspace isolation (stay inside declared mounts)

The AI may retrieve only from bundles declared in `Knowledge_Mounts`. It may not traverse outside a mounted `bundle_root`, follow a link out of the mount, or read arbitrary files in `_knowledge/` that no mount declares. Constraining the search space is what stops the model from drawing spurious connections across a large graph.

### Rule 3 — Explicit sourcing (every data-plane claim is cited)

Any factual claim drawn from the data plane that lands in a drafted artifact or in `_design-decisions.md` MUST carry an OKF-conformant citation back to the concept that supplied it: a **file-relative markdown link** to the source concept at the point of claim, and/or a numbered entry under a `# Citations` heading. This is **F13 extended to the data plane** — the same "never invent a source" discipline, now pointing at concept IDs instead of an inventory entry.

What this rule forbids, explicitly: the `[Source: _knowledge/...]` pseudo-tag; bare paths that are not markdown links; and citing a concept the AI did not actually read this session.

### Rule 4 — Boot-time re-verification (provenance is not currency)

A runtime citation proves *where* a claim came from, not that the claim still matches the source. Because a vendored bundle can be re-vendored to a newer version — and because OKF is itself v0.1 Draft and may change — at **session start**, for every mount the session depends on, the AI:

1. compares each depended-on concept's current `timestamp` (and the bundle's git SHA / `okf_version`) against the `pin` recorded in `Knowledge_Mounts`;
2. surfaces any drift to the operator (concept changed, version bumped, or pin missing);
3. re-confirms the affected claims against the current concept before reusing them, and updates the `pin` once the operator accepts the new baseline.

This closes failure mode **F14** (stale/format-drift mount — `_meta/FAILURE-MODES.md`).

## Lifecycle integration

The bridge protocol is wired into `03-DESIGN-PROTOCOL.md` as the **KNOWLEDGE-MOUNT** state: a KAOV cannot enter ARTIFACT-DRAFT until its declared mounts resolve under `_knowledge/`, pass OKF conformance, and have a recorded `pin`. The re-verification of Rule 4 runs as part of the bootstrap re-read every session, alongside the state re-read described in `06-STATE-PERSISTENCE.md`.

## Worked session (the canonical loop)

1. **Boot.** AI re-reads `AI-BOOTSTRAP.md`, the manifest, and `_design-state.md`. It sees `ove_Knowledge_Source: knowledge_augmented` and runs Rule 4 (re-verify pins for the mounts this session will use).
2. **Disclose.** Task needs network constraints. AI reads `_knowledge/enterprise-catalog/index.md`, then `_knowledge/enterprise-catalog/network/index.md` (Rule 1).
3. **Retrieve.** AI identifies `network/firewall_rules.md` as relevant and reads only that concept (Rule 2 — inside the declared mount).
4. **Draft + source.** AI drafts the artifact; each claim from the concept carries a file-relative link, e.g. *"…egress is default-deny per the [firewall rules](../_knowledge/enterprise-catalog/network/firewall_rules.md)…"* (Rule 3).
5. **Propose.** AI presents the draft and waits for the operator's decision (P11 — propose, don't decide).
6. **Persist.** On approval, AI updates `_design-decisions.md` (carrying the citations) and `_design-state.md`.

## Validator coverage

- **C15** — mounts resolve under `_knowledge/`, vendored bytes present, `okf_version` + `pin` set, and each bundle passes OKF v0.1 §9 conformance (every non-reserved `.md` has parseable frontmatter with a non-empty `type`).
- **C16** — no `[Source: …]` pseudo-citations in shippable content; data-plane citations are real markdown links resolving into a declared mount.

## Related references

- `_design-engine/_meta/CONVENTIONS.md` § Convention 11 — the convention this chapter implements
- `_proposals/OKF-conformance-notes.md` — the full OKF v0.1 format contract (spec + reference implementation)
- `_design-engine/02-DESIGN-PRINCIPLES.md` — the F13 source-grounding contract this extends
- `_design-engine/03-DESIGN-PROTOCOL.md` § KNOWLEDGE-MOUNT — the lifecycle state
- `_design-engine/_meta/FAILURE-MODES.md` § F14 — the stale-mount failure mode
