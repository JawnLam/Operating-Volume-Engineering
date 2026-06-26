---
type: Dataset
title: Widgets
description: The product catalog — one row per sellable widget.
tags: [product, catalog, reference]
timestamp: 2026-06-25T00:00:00Z
---

The widgets dataset is the canonical list of sellable products. It is referenced
by the [orders table](../tables/orders.md) via the `widget_id` foreign key.

# Schema

| Column      | Type    | Description                          |
|-------------|---------|--------------------------------------|
| `widget_id` | STRING  | Globally unique widget identifier.   |
| `name`      | STRING  | Human-readable widget name.          |
| `unit_usd`  | NUMERIC | List price per unit, in US dollars.  |

# Citations

[1] [Demo catalog README](../index.md)
