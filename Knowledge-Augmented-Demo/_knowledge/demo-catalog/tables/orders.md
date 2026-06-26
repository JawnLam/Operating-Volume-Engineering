---
type: Table
title: Orders
description: One row per completed order; joins to widgets on widget_id.
tags: [orders, sales, fact]
timestamp: 2026-06-25T00:00:00Z
---

The orders table is the fact table for completed sales. Grain: one row per
completed order. Each order references a product in the
[widgets dataset](../datasets/widgets.md) via `widget_id`.

# Schema

| Column       | Type      | Description                              |
|--------------|-----------|------------------------------------------|
| `order_id`   | STRING    | Globally unique order identifier.        |
| `widget_id`  | STRING    | FK into [widgets](../datasets/widgets.md). |
| `quantity`   | INTEGER   | Units ordered.                           |
| `placed_at`  | TIMESTAMP | When the order was completed.            |

# Citations

[1] [Widgets dataset](../datasets/widgets.md)
