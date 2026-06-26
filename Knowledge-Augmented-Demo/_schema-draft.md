---
type: OVE_Schema_Draft
timestamp: "2026-06-25T00:00:00Z"
Item_ID: "kaov-demo-schema-draft"
title: "Knowledge-Augmented-Demo — Schema Draft"
Date_Added: 2026-06-25
Date_Modified: 2026-06-25
Needs_Processing: false
ove_OV_Name: "Knowledge-Augmented-Demo"
ove_Schema_Status: locked
---

# Knowledge-Augmented-Demo — Schema Draft

## Q1 — Kinds of knowledge or work

- **Declarative/factual** (high) — the catalog of datasets and tables (held in the OKF data plane, not the corpus)
- **Procedural** (medium) — how to retrieve from the mount under the bridge protocol

## Data plane vs control plane

The factual knowledge lives in the mounted OKF bundle (`_knowledge/demo-catalog`), addressed by OKF **Concept ID** (e.g. `tables/orders`). The control plane (this engine) holds only the retrieval discipline. This split is the whole point of Convention 11.

## Namespace

`kaov_` (demonstration only; the OV ships no Prototypes of its own beyond the OVE backbone).
