---
type: Fleeting
Item_ID: prototype-NAMESPACE-typename
title: "<NAMESPACE>_<TypeName> Prototype"
Date_Added: YYYY-MM-DD
Date_Modified: YYYY-MM-DD
Needs_Processing: false
---

# `<NAMESPACE>_<TypeName>` — Prototype Definition

> **What this file is.** The canonical definition of the `<NAMESPACE>_<TypeName>` Prototype for the `<OV-NAME>` Operating Volume. Items (instances) in any cartridge that declare `type: <NAMESPACE>_<TypeName>` conform to the contract described below.

## Purpose

*One paragraph: what kind of thing this Prototype represents in the OV's domain. What does it model? Why does the OV need it? When does the operator create an Item of this Prototype?*

Example for `COOK_Recipe`:

> A Recipe is a structured cooking procedure: ingredients, technique, timing, and yield. It captures both the canonical form (what's written in the cookbook) and the operator's personal adaptations across attempts. Created whenever the operator decides a procedure is worth keeping, tagging, and iterating on.

## Required frontmatter

These fields MUST be present on every Item that declares `type: <NAMESPACE>_<TypeName>`:

### Universal Core (from CONVENTIONS.md Convention 1)

| Field | Type | Notes |
|-------|------|-------|
| `type` | string | Must equal `<NAMESPACE>_<TypeName>` |
| `Item_ID` | string | UUID or slug, unique within the cartridge |
| `Title` | string | Human-readable display title |
| `Date_Added` | date | When the Item was created |
| `Date_Modified` | date | When the Item was last changed |
| `Needs_Processing` | boolean | Whether the Item is waiting for the operator to refine it |

### Prototype-specific fields

*One row per OV-specific property this Prototype carries. Use the OV's namespace prefix and Title_Snake_Case body. Acronyms fully capitalized.*

| Field | Type | Required? | Notes |
|-------|------|-----------|-------|
| `<namespace>_<Field_Name>` | string / enum / list / date | yes / no | Brief description |
| … | … | … | … |

## Body structure

*The required and optional sections of an Item's body, in order. Headers should match exactly so the AI can navigate them when consulting an Item.*

```markdown
# <Item Title>

## Required Section A
*What goes here.*

## Required Section B
*What goes here.*

## Optional Section C
*When to include it.*
```

## Naming

- **Filename pattern:** `<descriptive-kebab-case-slug>.md`
- **Location:** `<Cartridge>/<Folder-for-this-Prototype>/`
- **Wikilink target:** the slug (Obsidian-native)

## Example Item

*A minimal example showing a complete, well-formed Item of this Prototype. Use a domain-appropriate concrete case, not a stub — examples should demonstrate the Prototype, not gesture at it.*

```markdown
---
type: <NAMESPACE>_<TypeName>
timestamp: "2026-06-06T00:00:00Z"
Item_ID: <slug>
title: "<Concrete example title>"
Date_Added: 2026-06-06
Date_Modified: 2026-06-06
Needs_Processing: false
<namespace>_<Field_Name>: <value>
---

# <Concrete example title>

## Required Section A
…

## Required Section B
…
```

## Relationships

*Which other Prototypes this one can point to or be pointed to by. Use the OV's relationship vocabulary from `04-SCHEMA-DESIGN.md` Q4.*

- `<NAMESPACE>_<OtherType>` — *relationship name (e.g., "originated-by", "prerequisite-of", "instantiates")*

## Notes

*Anything an operator or AI should know that doesn't fit above — edge cases, deprecation status, known sharp edges, evolution history.*
