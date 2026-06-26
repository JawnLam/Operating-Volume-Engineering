---
Item_Prototype: OVE_Design_Decisions
Item_ID: "kaov-demo-decisions"
Title: "Knowledge-Augmented-Demo — Design Decisions Log"
Date_Added: 2026-06-25
Date_Modified: 2026-06-25
Needs_Processing: false
ove_OV_Name: "Knowledge-Augmented-Demo"
---

# Knowledge-Augmented-Demo — Design Decisions Log

## Decisions

### 2026-06-25 — Decision 1: knowledge_augmented with a single vendored mount

**Decided:** This OV declares `ove_Knowledge_Source: knowledge_augmented` and mounts exactly one OKF bundle (`_knowledge/demo-catalog`). `ship_disposition: vendored` — the bytes ship with the OV, preserving self-containment per Convention 11.

### 2026-06-25 — Decision 2: data-plane claims cite the source concept (Rule 3)

**Decided:** Any drafted claim drawn from the catalog carries a file-relative markdown link to the source concept. Worked example of the citation form:

> The orders fact table is one row per completed order and joins to widgets on `widget_id`, per the catalog's [orders table](_knowledge/demo-catalog/tables/orders.md) and [widgets dataset](_knowledge/demo-catalog/datasets/widgets.md).

This is the OKF-conformant form (file-relative markdown links). The `[Source: …]` pseudo-syntax is never used (C16).

