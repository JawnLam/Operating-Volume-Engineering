---
type: Fleeting
timestamp: "2026-06-25T00:00:00Z"
Item_ID: ove-proposal-okf-conformance
title: "OKF v0.1 Conformance Notes — implementation contract for KAOV"
Date_Added: 2026-06-25
Date_Modified: 2026-06-25
Needs_Processing: false
Status: REFERENCE — distilled from Google's real OKF spec + reference code. Source of truth for KAOV format compliance.
Cited_by: _design-engine/08-KNOWLEDGE-RETRIEVAL.md, _design-engine/_meta/CONVENTIONS.md
---

# OKF v0.1 Conformance Notes

> **Purpose.** This is the grounded, verified record of what Google's **Open
> Knowledge Format (OKF) v0.1** actually requires — read directly from the
> normative spec AND the reference implementation (not from any summary). It is
> the format contract any KAOV producer/consumer must satisfy to stay
> interoperable with the broader OKF ecosystem. Where Gemini's source PRD
> diverged from real OKF, the divergence is
> flagged here.

## 0. What was read (provenance)

All from `github.com/GoogleCloudPlatform/knowledge-catalog`, `okf/`, `main`,
fetched 2026-06-25:

- `okf/SPEC.md` — the normative spec (v0.1 Draft, 11 sections + Appendix A). **Authoritative.**
- `okf/README.md` — overview + reference-agent/visualizer docs.
- `okf/src/reference_agent/bundle/document.py` — concept parse/serialize/validate.
- `okf/src/reference_agent/bundle/index.py` — `index.md` generation.
- `okf/src/reference_agent/bundle/paths.py` — concept-id ↔ path + segment rules.
- `okf/src/reference_agent/prompts/reference_instruction.md` — the producing-agent contract.
- `okf/bundles/crypto_bitcoin/**` — a real, shipped, conformant bundle.

## 1. Terminology (use these exact terms — Gemini's did not)

| OKF term | Meaning | Gemini PRD used (WRONG) |
|---|---|---|
| **Knowledge Bundle** | Self-contained hierarchical collection of concepts. The unit of distribution. | "OKF Bundle" (ok) |
| **Concept** | One unit of knowledge = **one markdown document**. | "**Node File**" / "concept_A.md" ❌ |
| **Concept ID** | The concept file's path within the bundle, **`.md` removed**. `tables/users.md` → `tables/users`. | (absent) |
| **Frontmatter** | YAML metadata block, `---`-delimited, at file top. | ok |
| **Body** | Everything after the frontmatter. | ok |
| **Link** | A standard markdown link between concepts (a relationship edge). | ok |
| **Citation** | A link to an external source backing a body claim. | mis-specified (see §6) |

**Action for KAOV:** purge "node" / "Node File" from all KAOV prose. The unit is a
**Concept**, addressed by **Concept ID**.

## 2. Bundle structure (SPEC §3)

```
bundle_root/
├── index.md          # OPTIONAL. Directory listing for progressive disclosure. (§6)
├── log.md            # OPTIONAL. Chronological update history. (§7)
├── <concept>.md      # A concept at bundle root.
└── <subdir>/         # Subdirectories group concepts.
    ├── index.md
    ├── <concept>.md
    └── <subdir>/ …
```

- Directory layout is **domain-independent** — producers organize however suits the
  knowledge.
- A bundle MAY ship as a git repo (recommended), a tarball/zip, or a subdirectory of
  a larger repo. **A bundle is just a directory.**

### 2.1 Reserved filenames (SPEC §3.1) — MUST NOT be concept docs

| Filename | Purpose |
|---|---|
| `index.md` | Directory listing (§6). Carries **no frontmatter**, except the bundle-root `index.md` MAY carry `okf_version` (§11). |
| `log.md` | Update history (§7). Date-grouped, newest first, ISO `YYYY-MM-DD` headings. |

Every **other** `.md` file is a concept document. *(Gemini's PRD never mentioned
`log.md` or the reserved-filename rule.)*

## 3. Concept frontmatter — THE compliance crux (SPEC §4.1 vs reference code)

> **Spec ⊥ reference implementation. Read both.**

- **SPEC §4.1 + §9 conformance:** the **only REQUIRED field is `type`** (a free-form
  string; not centrally registered; consumers MUST tolerate unknown values).
  `title`, `description`, `resource`, `tags`, `timestamp` are *recommended/optional*.
- **Reference code `document.py`:**
  `REQUIRED_FRONTMATTER_KEYS = ("type", "title", "description", "timestamp")` — and
  `validate()` raises if ANY of the four is missing/empty.

**KAOV resolution (satisfies BOTH):**

- **As a producer:** always emit `type` + `title` + `description` + `timestamp`, plus
  `resource` whenever the concept maps to a real asset/source. This passes the strict
  reference validator and the permissive spec simultaneously.
- **As a consumer:** be permissive per §9 — accept any doc with a non-empty `type`;
  never reject on missing optional fields, unknown `type`, unknown extra keys, or
  broken links.

Canonical frontmatter block:

```yaml
---
type: <short free-form string>      # REQUIRED. e.g. "BigQuery Table", "Metric", "Playbook", "Reference"
title: <human display name>         # spec-optional; reference-validator-required → always emit
description: <ONE sentence>          # used verbatim in generated index.md → keep tight
resource: <canonical URI>           # recommended when the concept maps to a real asset
tags: [<tag>, <tag>]                # optional
timestamp: <ISO 8601 datetime>      # spec-optional; reference-validator-required → always emit
# producer-defined extra keys allowed; consumers preserve & tolerate them
---
```

*Gemini's PRD claimed frontmatter is "type, tags, **dependencies**" — `dependencies`
is **not an OKF field**; it was invented. Do not emit it.*

## 4. Body conventions (SPEC §4.2)

- Standard markdown. Favor **structural** markdown (headings, tables, lists, fenced
  code) over freeform prose — aids both human reading and agent retrieval.
- No required sections. **Conventional** headings, used when applicable:
  `# Schema`, `# Examples`, `# Citations`. (Reference agent also uses
  `# Common query patterns`.)

## 5. Links between concepts (SPEC §5 vs reference code)

> **Second spec ⊥ reference-implementation conflict.**

- **SPEC §5.1:** bundle-relative **absolute** links (leading `/`, e.g.
  `/tables/customers.md`) are the **recommended** form ("stable when documents move").
- **Reference agent prompt + every real bundle:** **file-relative** links only
  (`../tables/blocks.md`, `users.md`); *"Never start a link with `/` (that breaks
  GitHub rendering)."*

**KAOV resolution:** use **file-relative** links. They match every shipped Google
bundle, render on GitHub (how OVE repos are browsed), and are what the reference
tooling emits. Note the divergence from SPEC §5.1's stated recommendation in
`_design-decisions.md` when implemented.

- Link semantics are **untyped**: a link asserts *a* relationship; the kind is
  conveyed by surrounding prose, not the link.
- Consumers **MUST tolerate broken links** (may be not-yet-written knowledge).

## 6. Citations (SPEC §8) — Gemini's biggest format error

OKF citations are **markdown links under a `# Citations` heading**, numbered:

```markdown
# Citations

[1] [BigQuery public dataset announcement](https://cloud.google.com/blog/...)
[2] [Internal data-quality runbook](/references/data-quality.md)
```

Citation targets MAY be absolute URLs, bundle-relative paths, or paths into a
`references/` subdirectory (external material mirrored as first-class concepts).

> **Gemini's PRD (FR 3.2 + example step 5) appended `[Source: okf/network/firewall_rules.md]`
> to each claim.** That is **not** OKF: it is neither a markdown link nor the
> `# Citations` convention. For KAOV's "every claim is sourced" rule, either:
>
> 1. inline a **file-relative markdown link** to the source concept at the point of
>    claim (`… per the [firewall rules](../okf/network/firewall_rules.md) …`), and/or
> 2. aggregate sources under a `# Citations` section per §8.
>
> Both are conformant; `[Source: …]` is not.

## 7. index.md (SPEC §6) — progressive disclosure

- **Optional** at every level (including bundle root). Consumers MAY synthesize one
  when absent. *(So KAOV's "read index before concept" is an OVE-imposed discipline,
  stricter than OKF — frame it that way, don't claim OKF mandates it.)*
- **No frontmatter** (sole exception: bundle-root `index.md` MAY carry `okf_version`).
- Format = sections, each a `#`-heading grouping entries:

```markdown
# <Group / Type heading>

* [Title](relative-link) - description from the concept's frontmatter

# Subdirectories

* [subdir](subdir/index.md) - synthesized description
```

- Reference `index.py` groups entries **by concept `type`** (heading per type) and
  lists subdirectories under a `Subdirectories` group; descriptions are pulled from
  each concept's `description` frontmatter. Confirmed in the real `crypto_bitcoin`
  bundle (`# Subdirectories`, `# BigQuery Table`).

## 8. log.md (SPEC §7) and okf_version (SPEC §11)

- `log.md`: date-grouped, newest first; ISO `YYYY-MM-DD` headings; entries are prose
  with a conventional leading bold word (`**Update**`, `**Creation**`,
  `**Deprecation**`).
- A bundle MAY declare `okf_version: "0.1"` in its **bundle-root `index.md`
  frontmatter** (the only frontmatter allowed in any index.md). Consumers that don't
  understand the version SHOULD best-effort consume, not refuse.

## 9. Conformance test (SPEC §9) — what "compliant" actually means

A bundle is **conformant with OKF v0.1** iff:

1. Every non-reserved `.md` file has a **parseable YAML frontmatter** block.
2. Every frontmatter has a **non-empty `type`**.
3. Reserved files (`index.md`, `log.md`) follow §6 / §7 structure when present.

Consumers **MUST NOT** reject a bundle for: missing optional fields; unknown `type`;
unknown extra keys; broken links; missing `index.md`. (Permissive-consumption is
load-bearing in OKF.)

## 10. Concept-ID segment rules (reference `paths.py`)

Each path segment must match `[A-Za-z0-9_][A-Za-z0-9_.\-]*` — i.e. start with
alphanumeric/underscore, then alphanumerics, underscore, dot, or hyphen. KAOV mount
declarations and any generated concept files must respect this.

## 11. Status caveat — OKF is v0.1 DRAFT

The spec header reads **"Version 0.1 — Draft."** §11 states a **major** bump "may make
breaking changes (renaming required fields, changing reserved filenames)." Committing
KAOV to OKF therefore means committing to a moving, pre-1.0 target. Implications:

- Every KAOV `Knowledge_Mounts` entry SHOULD record the `okf_version` it was authored
  against, so a future breaking bump is detectable.
- This compounds the design note's §3.4 runtime-provenance gap: not only can a *concept*
  change after ship, the *format itself* can. Pin both (concept `timestamp` / git SHA,
  and `okf_version`).

## 12. Net verdict on Gemini's PRD

**Architecture: sound.** Control-plane/data-plane split, progressive disclosure, and
explicit sourcing all map cleanly onto real OKF intent.

**Format details: non-conformant in four ways** that would have broken interoperability
— (1) "Node File" terminology, (2) invented `dependencies` field + wrong required-field
set, (3) `[Source: …]` citation pseudo-syntax, (4) bundle-prefixed link paths. All four
are corrected above.
