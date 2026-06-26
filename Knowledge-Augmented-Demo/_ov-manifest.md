---
type: OVE_OV_Manifest
timestamp: "2026-06-25T00:00:00Z"
Item_ID: "kaov-demo-manifest"
title: "Knowledge-Augmented-Demo — KAOV Worked Example"
Date_Added: 2026-06-25
Date_Modified: 2026-06-25
Needs_Processing: false
ove_OV_Name: "Knowledge-Augmented-Demo"
ove_OV_Slug: "kaov-demo"
ove_Design_Phase: artifact-draft
ove_User_Name: "OVE engine maintainer"
ove_Bootstrapped: 2026-06-25
ove_Engagement_Kind: fresh-worked-example
ove_Knowledge_Source: knowledge_augmented
---

# Knowledge-Augmented-Demo — KAOV Worked Example

> **The dogfood for Convention 11.** A deliberately tiny knowledge-augmented OV that mounts one vendored OKF v0.1 bundle as its data plane and proves the bridge protocol end-to-end (`_design-engine/08-KNOWLEDGE-RETRIEVAL.md`). It exists to demonstrate the loop and to give validator checks C15/C16 a real, conformant target — not to be a serious OV.

## What this OV is

A minimal "data-catalog assistant" OV: it helps an operator draft data-integration notes grounded in a curated catalog of datasets and tables. The catalog is not baked into the corpus as prose — it is mounted as an OKF bundle under `_knowledge/demo-catalog/` and retrieved progressively (index → concept) at session time.

## Why this user is designing it

To dogfood Convention 11: the cleanest way to prove the data-plane discipline is to ship an OV that actually uses it. The catalog is small enough to read in one sitting, which makes the progressive-disclosure and explicit-sourcing rules easy to follow in the worked session.

## Who is this for

- [x] Self only (demonstration)

## OV Archetype

- [x] **Finite-horizon** — the demo's finish line is "the bridge protocol is shown working end-to-end."

## Knowledge mounts (Convention 11)

`ove_Knowledge_Source: knowledge_augmented`. One vendored OKF bundle, copied under `_knowledge/` so the OV stays self-contained.

```yaml
Knowledge_Mounts:
  - bundle_root: _knowledge/demo-catalog
    okf_version: "0.1"
    provenance: "Hand-authored demonstration bundle for the KAOV worked example; conformant to OKF v0.1; vetted 2026-06-25."
    ship_disposition: vendored
    pin:
      vetted_timestamp: "2026-06-25T00:00:00Z"
```

## Scope boundaries

Not a real catalog assistant. The bundle has two concepts. The point is the *protocol*, not the breadth of knowledge.

## Notes

The mounted bundle follows OKF terminology exactly (Concept / Concept ID, reserved `index.md`, file-relative links, `# Citations`). See `_proposals/OKF-conformance-notes.md` for the binding format contract this bundle was authored against.
