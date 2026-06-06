---
Item_Prototype: Fleeting
Item_ID: ove-meta-conventions
Title: "OVE Meta — Universal Conventions for OV-Designed Output"
Date_Added: 2026-06-06
Date_Modified: 2026-06-06
Needs_Processing: false
type: design-engine-meta
role: conventions
scope: subject-agnostic
updated: 2026-06-06
---

# OVE Meta — Universal Conventions for OV-Designed Output

> **An OV designed via OVE produces files that conform to a small set of universal conventions out of the box. The operator should not need to post-process the output to make it vault-compatible. This file is the canonical statement of those conventions. Reference from `04-SCHEMA-DESIGN.md`, `05-WRITING-FOR-AI.md`, and `BOOTSTRAP-NEW-OV.md`.**

## Why these conventions exist

A new OV designed by OVE produces files that live alongside the operator's other notes — in an Obsidian vault, a folder of markdown, a Hugo content directory, etc. If the new OV's files don't conform to the operator's existing conventions (frontmatter shape, property naming, prototype declarations), the operator does cleanup work after every design engagement. The operator hired OVE to *avoid* that work, not generate it.

These conventions are not platform-specific. They work in any tool that reads YAML frontmatter. They are minimum-friction defaults; an operator who has different conventions can override them per-OV in the schema design.

## Convention 1 — Universal Core fields on every shipped note

Every `.md` file that ships in an OV designed via OVE declares these six fields in YAML frontmatter:

```yaml
---
Item_Prototype: <Prototype_Name>      # See Convention 4
Item_ID: <slug-or-uuid>
Title: "<Human-readable title>"
Date_Added: YYYY-MM-DD
Date_Modified: YYYY-MM-DD
Needs_Processing: false
---
```

OV-specific properties live below these. `Item_Prototype` is the discriminator that tells humans, queries, and automation which schema the note follows.

## Convention 2 — Case conventions for property names

Five rules govern frontmatter property naming. They apply universally to every OV designed via OVE.

| Position | Convention | Example |
|----------|------------|---------|
| **Core keys** (`Item_ID`, `Title`, `Date_Added`, etc.) | `Title_Snake_Case` | `Publication_Date`, `Item_ID` |
| **Domain prefix** (the namespace) | `lowercase_snake_case` | `lll_`, `lfw_`, `ove_`, `cook_` |
| **Domain-prefixed property body** (after the prefix) | `Title_Snake_Case` | `lll_Status`, `lfw_Item_Type`, `ove_OV_Name` |
| **Acronyms in either position** | Fully capitalized | `URL`, `ISBN`, `POV`, `OV` |
| **Enum identifiers** (under `enums:` in schema) | `lowercase_snake_case` (typically plural) | `lll_statuses`, `lfw_item_types`, `ove_design_phases` |

These rules ensure cross-namespace consistency. They are also documented at the top of any published `Master_Schema.yaml` (case rules 1–5).

## Convention 3 — One namespace per OV

Every OV chooses a short lowercase namespace prefix at design time (e.g., `cook_` for a cooking OV, `negotiation_` for a negotiation-prep OV). All OV-specific frontmatter properties carry that prefix.

Per Convention 2, the prefix is `lowercase_snake_case` and the body after the prefix is `Title_Snake_Case`. The namespace + Title_Snake_Case body pattern is what makes a property name belong to a particular OV.

## Convention 4 — Every Prototype gets its own `Item_Prototype` value

Every Prototype in the OV is declared with an `Item_Prototype` value, named `<NAMESPACE_UPPER>_<TypeName>`. Every Item in a cartridge carries the value of the Prototype it conforms to. Examples from existing OVs:

| OV | Prototype names |
|----|-----------------|
| LLL | `LLL_Unit`, `LLL_Subject_Manifest`, `LLL_Session`, … |
| LFW | `LFW_Character_Bible`, `LFW_Motif`, `LFW_Scene`, … |
| OVE | `OVE_OV_Manifest`, `OVE_Design_State`, `OVE_Session`, … |

For non-Item files (front-door docs, engine prose, meta), use `Item_Prototype: Fleeting`. This is the universal "this is a note but not an instance of any OV-specific Prototype" value.

## Convention 5 — Schema-of-namespace declaration

The new OV's `_<purpose>-engine/_meta/SCHEMA-OF-SCHEMAS.md` declares its namespace, Prototypes, enum identifiers, and properties in YAML — ready to be lifted into a `Master_Schema.yaml` if the operator maintains one. Even if no `Master_Schema.yaml` exists, the per-OV schema declaration is the canonical source for that OV's structural rules.

## Convention 6 — Each OV ships its own `_Prototypes/` folder

Every OV bundles a top-level `_Prototypes/` folder containing one `.md` file per Prototype in its namespace. Each file is a self-contained declaration of that Prototype: its frontmatter shape, required body sections, and an example. The structure of each file follows `_design-engine/_templates/TEMPLATE-Prototype.md`.

**This folder is the canonical home for the OV's Prototype definitions.** A reader who clones the OV without any surrounding infrastructure can open `_Prototypes/<NAMESPACE>_<TypeName>.md` and learn what an Item of that Prototype is supposed to look like, what frontmatter fields it carries, and what its body should contain.

**Why this matters.** Without Convention 6, an OV's Prototypes live only by reference. A cartridge note declares `Item_Prototype: COOK_Recipe` — that's a name pointer. If the reader has no `COOK_Recipe.md` definition available, the name is meaningless. Operators with a vault-wide central registry (e.g., a Master_Schema and an `_Infrastructure/_Prototypes/` folder) get the definition from the central registry, but operators without such infrastructure are stranded. Convention 6 makes the OV portable: the Prototype definitions travel with it.

**The vault-wide central registry, if any, is a downstream union view.** Operators who run multiple OVs may choose to maintain a central registry that aggregates Prototypes across all of their OVs (the user's `_Infrastructure For All Vaults/_Prototypes/` is one example). That central registry is convenience, not authority — the canonical home of each Prototype is still the OV's local `_Prototypes/` folder. If the two disagree, the OV's local folder wins.

**Concretely:**

- `_Prototypes/COOK_Recipe.md`
- `_Prototypes/COOK_Technique.md`
- `_Prototypes/COOK_Ingredient.md`
- *(one file per Prototype declared in the OV's namespace)*

Non-Item file types (Fleeting, the universal "this is a note but not a recurring Prototype") do not need to be redeclared in the OV's `_Prototypes/` folder — Fleeting is a vault-universal Prototype with no OV-specific behavior.

**Materialization happens during ARTIFACT-DRAFT.** As the AI walks `04-SCHEMA-DESIGN.md` and locks the OV's Prototype list (Q4, Q9, Q12), it materializes one `_Prototypes/<NAMESPACE>_<TypeName>.md` file per Prototype, conforming to `TEMPLATE-Prototype.md`. The shipping checklist gates whether all declared Prototypes have a corresponding file in `_Prototypes/` before the OV ships (`07-SHIPPING-CHECKLIST.md` Phase 3.5).

**Validator coverage.** The optional `validate.py` includes a check (C7 — Prototype coverage) that scans every cartridge for `Item_Prototype:` values and confirms each has a matching `<NAMESPACE>_<TypeName>.md` in either the OV root's `_Prototypes/` or, if present, an enclosing cartridge's `_Prototypes/`. Missing files fail with a precise file:line pointer.

## How to apply during a new-OV design

The AI walking `BOOTSTRAP-NEW-OV.md` asks the operator one question early:

> *"What namespace prefix will this OV use? (Three to six lowercase letters ending in underscore. Example: `cook_` for a cooking OV.)"*

From that single answer, everything else follows:

- Prototype names: `COOK_<TypeName>`
- Property names: `cook_<Title_Snake_Case_Body>`
- Enum identifiers under `enums:`: `cook_<lowercase_plural>`
- `Item_Prototype` values on each Item: `COOK_<TypeName>`
- `Item_Prototype: Fleeting` on non-Item files
- `_Prototypes/` folder at the OV root with one `COOK_<TypeName>.md` per Prototype, each following `_design-engine/_templates/TEMPLATE-Prototype.md`

When drafting templates, Prototype declarations, and example Items, the AI applies these conventions throughout. The operator does not post-process the output.

## When the operator wants different conventions

If the operator has different conventions (e.g., they prefer all-lowercase property bodies for backwards-compatibility with a legacy schema), they say so during INTERVIEW or SCHEMA-DESIGN. The AI then applies the operator's conventions instead — but documents the choice in `_design-decisions.md` so future sessions know which conventions apply.

**The default is the conventions above. Override only on explicit operator request.**

## Verifying the output

After ARTIFACT-DRAFT and during REVIEW, the AI checks every drafted file for:

- [ ] Six Universal Core fields present and non-empty (Convention 1)
- [ ] Property bodies in Title_Snake_Case (Convention 2)
- [ ] Acronyms fully capitalized (Convention 2)
- [ ] Namespace prefix consistent across all properties (Conventions 2, 3)
- [ ] `Item_Prototype` value matches a Prototype defined in the OV's `_meta/SCHEMA-OF-SCHEMAS.md` (Convention 4)
- [ ] Non-Item files declare `Item_Prototype: Fleeting` (Convention 4)
- [ ] Schema declaration exists at `_<purpose>-engine/_meta/SCHEMA-OF-SCHEMAS.md` (Convention 5)
- [ ] `_Prototypes/` folder exists at the OV root with one `<NAMESPACE>_<TypeName>.md` per Prototype declared in the OV's namespace (Convention 6)
- [ ] Each `_Prototypes/<NAMESPACE>_<TypeName>.md` conforms to `TEMPLATE-Prototype.md` and matches the Prototype's `_meta/SCHEMA-OF-SCHEMAS.md` declaration (Convention 6)

These checks are also covered by the optional `validate.py` (`C1` backbone presence, `C2` frontmatter presence, `C3` placeholder leakage — the wider scrub, `C7` Prototype coverage) and by walking `VALIDATION-CHECKLIST.md` for markdown-only environments.

## Related references

- `_design-engine/04-SCHEMA-DESIGN.md` § "Convention compliance" — points back to this file when designing the new OV's schema
- `_design-engine/05-WRITING-FOR-AI.md` § "Property-naming conventions" — points back to this file when drafting any property-bearing prose
- `_design-engine/BOOTSTRAP-NEW-OV.md` — the namespace CQ that triggers the convention cascade
