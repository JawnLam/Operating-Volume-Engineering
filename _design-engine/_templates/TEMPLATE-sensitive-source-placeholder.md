---
type: Fleeting
Item_ID: "<source-slug>-placeholder"
title: "<Source Identifier> — Source Access Request"
Date_Added:
Date_Modified:
Needs_Processing: false
ove_Source_Slug: "<source-slug>"
ove_Source_Sensitivity: ship-by-reference   # Per Convention 9 in OVE _meta/CONVENTIONS.md
---

# `<Source Identifier>` — Source Access Request

> **This file is a placeholder for a sensitive source material that the `<OV Name>` Operating Volume cites as substrate but does not redistribute. The canonical source file stays local in the Methodology Author's working copy and is excluded from this repository per Convention 9 (`_design-engine/_meta/CONVENTIONS.md` in OVE). Anyone who needs access to the canonical source contacts the Methodology Author directly per the contact information below.**

## What this source is

*One paragraph describing the source: author, year, title, publication / dissertation venue, brief description of contents.*

*Example:*

> *`Lam 2018 Pepperdine dissertation` is the Methodology Author's doctoral dissertation, "The Accumulation, Utilization, And Protection of Political Capital" (Pepperdine University, 2018). The dissertation is the foundational substrate for this OV's framework for political capital, the 9-type resource taxonomy, Table 3's tactical move catalogue, and the ADAPT Loop coaching framework. 294 pages.*

## Why this source ships by reference, not in full

The Methodology Author retains the canonical source as personal academic work. The OV cites the source as substrate (specific page numbers, structural elements, theoretical concepts) but does not redistribute the source itself. This is the Convention 9 (`_design-engine/_meta/CONVENTIONS.md` in OVE) ship-by-reference pattern:

- Physical source file: held local in the Methodology Author's working copy
- This placeholder `.md`: ships publicly, points to the contact below
- `_source-inventory.md` in this OV: lists the source with sensitivity `Ship-by-reference (Convention 9)`
- `.gitignore` in this OV: excludes the physical source file at its canonical path
- LICENSE language: acknowledges the sacred-source distinction if the OV uses restrictive licensing

## How to request access

Contact the Methodology Author directly:

- **Methodology Author:** `<Methodology Author Name>`
- **Contact:** `<Contact Method — typically an email address the author publishes for this purpose>`
- **What to mention:** which OV brought you here (`<OV Name>`), what kind of access you need (read-only review, scholarly citation, academic archival), and your context (academic researcher, peer practitioner, etc.).

The Methodology Author responds case-by-case. Common outcomes:

- **Academic researchers** working on related scholarship: typically granted read-only access for fair-use citation in scholarly work.
- **Peer practitioners** evaluating the OV's substrate: typically granted read-only access during evaluation periods.
- **Commercial / redistribution requests:** require explicit written permission and are typically declined.

## What you can do without the source

The OV itself ships freely (per its `LICENSE.md`). You can:

- Read this OV's engine, templates, and worked examples to understand how the source's ideas are operationalized
- Read this OV's `_source-inventory.md` for the source's structural metadata (page count, sections, etc.)
- Read this OV's `_frameworks/` documentation (or equivalent) for the OV's own digestion of the source's ideas (citations are present; the source itself is not)

If your goal is *using* the OV (not republishing the source), the OV alone is sufficient.

## Related references in this OV

- `<list of OV files that cite this source, e.g.>:`
- `_source-inventory.md` — the inventory entry for this source
- `_frameworks/<framework-doc-citing-this-source>.md`
- `<other related references>`
