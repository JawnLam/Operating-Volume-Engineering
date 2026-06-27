---
type: Fleeting
timestamp: "2026-06-27T00:00:00Z"
Item_ID: ove-proposal-convention-12
title: "Convention 12 — Registry Sync (Design Note)"
Date_Added: 2026-06-27
Date_Modified: 2026-06-27
Needs_Processing: false
Status: DRAFT — for operator review. No engine edits made.
---

# Convention 12 — Registry Sync (Design Note)

> **Goal.** Every OV OVE designs carries baked-in instructions to keep the operator's
> central **registry** (an aggregate schema like the author's `_Infrastructure For All
> Vaults/` — `Master_Schema.yaml` + `_types/`) in sync with the OV's schema contribution —
> on **create/install** and on **upgrade** — and to **soft-retire** that contribution on
> uninstall. Path-independent (the registry is named differently, or absent, in a
> stranger's environment). Extends Conventions **5** (the OV declares its schema in
> `_meta/SCHEMA-OF-SCHEMAS.md`), **6** (the per-OV `_types/` is canonical; a central
> registry is a *downstream union view*), and **7** (install/update flow).
>
> Status: DRAFT. Nothing in the engine changed.

## 1. The model in one paragraph

The per-OV `_types/` is the source of truth for that OV's schema (C6). A central registry,
*if the operator maintains one*, is the **union** of every installed OV's schema. Convention
12 keeps that union current: the OV pushes its types/namespace/properties up; the registry
pushes *universal* conventions (the OKF Universal Core, case rules) down so the OV stays
conformant. All sync is **propose-and-confirm** — it edits the operator's schema and can
touch existing notes, so it never runs silently.

## 2. Discovery — path-independent (the crux)

On install/upgrade the OV locates the registry in this order:

1. **Operator pointer** — a marker the operator set (e.g. a line in `_USER.md` or a
   `.registry` file naming the registry root). Authoritative if present.
2. **Search** — look upward / across the vault for a registry by its minimal contract (§6).
3. **Ask** — prompt: *"where is your infrastructure registry, if any?"*
4. **Offer to build** — **most strangers have no registry.** If none is found, offer to
   scaffold a minimal one *from this OV's own `SCHEMA-OF-SCHEMAS.md`* as the seed.
5. **Record the decision** — the outcome is written to the OV's **`_meta/registry-link.yaml`**
   memory. If the operator **declines** a registry, that is recorded as `registry: none-declined`,
   and **all future upgrades touch only the OV's internals** — never hunting for a registry again.

## 3. Direction — bounded bidirectional (Option A, locked)

Each surface has an owner; both directions happen:

- **OV → registry** for the OV's *own* schema (namespace, types, properties, enums). The OV
  is canonical for its own types (C6 preserved).
- **Registry → OV** for *universal* conventions (the OKF Universal Core fields, case rules).
  When the universal core changes (e.g. a future OKF field rename), the registry is the
  source and **the OV is made aware** and brought into conformance.

## 4. Reconciliation — a 3-way merge

Because changes can arrive from both sides since the last sync, reconcile against the
**merge base** recorded in `registry-link.yaml` (`last_synced_registry_schema` +
`last_synced_ov_version`): compare the OV's current schema, the registry's current record,
and that baseline; surface each real divergence for an operator decision (git-style). Then
update the baseline.

## 5. What syncs (the registry update surface)

On register/upgrade: the OV's **namespace** (`<ns>_`), its **types** (`<NS>_*` + their
specific-keys), its **properties** (`<ns>_*`), its **enums** (`<ns>_*`), the **`_types/`
union view** (copy/refresh each `<NS>_<Type>.md`), the registry **`meta` version + changelog
+ Decision Log** entry, and a **cross-OV collision check** (no namespace/type-name clash). A
re-validation run (`schema-validator`) confirms green. *Not synced:* the OV's engine,
cartridges, or front-door — only its schema contribution.

## 6. The minimal "registry contract"

So the OV knows what it's syncing into, a registry is anything that provides: (a) a schema
file with a `namespaces`, `types`, `properties`, `enums` shape (a `Master_Schema.yaml` is the
reference), and (b) a `_types/` union folder. The OV degrades gracefully if either is absent.

## 7. No registry → graceful

If the operator has no registry and declines to build one, the OV is fully self-sufficient
(C6: the per-OV `_types/` is canonical). The sync **no-ops**, records `none-declined`, and
future upgrades are internal-only.

## 8. Retirement — soft by default, registry-side audit (locked)

De-registration is **not** the inverse of registration: an uninstalled OV's *notes outlive
it*, so hard-deleting its types would invalidate existing notes. And an absent OV can't run
its own de-registration. Therefore retirement is a **registry-side audit**, not OV-baked:

- **Detect** — the audit compares registered namespaces against currently-installed OVs; a
  namespace with no installed OV is **orphaned**.
- **Soft-retire (default)** — mark it `status: retired, retired: <date>, last_ov_version: <x>`
  and **keep the type definitions** so existing notes still validate. Re-installing the OV
  **un-retires** (clean merge).
- **Hard-purge (explicit, reference-checked GC only)** — a separate "clean the registry"
  action removes a retired type **only if zero notes reference it**, on operator confirm. If
  notes reference it: surface the count and offer to migrate, never delete. (Reuses the OKF
  migrator's note-scanning.)

## 9. What gets baked into every OV (the deliverable)

OVE emits, in every OV it designs:

- `_meta/SCHEMA-OF-SCHEMAS.md` — C5, exists; the thing reconciled.
- `_meta/registry-link.yaml` — **new memory:** `registry: <path>|none-declined|unset`,
  `last_synced_registry_schema`, `last_synced_ov_version`.
- `_meta/REGISTRY-SYNC.md` — **new:** the protocol the AI follows (discovery → reconcile →
  propose → record), restating §2–§5.
- Hooks in `INSTALL.md` (on-install) and `UPDATE-PROMPT.md` / `OPERATOR-GUIDE.md §Updates`
  (on-upgrade) that invoke the sync.

OVE's engine gains: **Convention 12** in `_meta/CONVENTIONS.md`; a `BOOTSTRAP-NEW-OV.md` step
that emits the artifacts and runs registration at ship; a **SHIP-PREP gate** ("registry-sync
artifacts present"); and a validator check. The registry-side **audit/GC** ships as a tool
(sibling to the OKF migrator).

## 10. Open items

None blocking. (Discovery=pointer→search→ask→offer→record; direction=bounded-bidirectional A;
retirement=soft + reference-checked GC — all locked by the operator.) Implementation lands as
the next OVE release, coordinated with the Prototype→Type terminology retirement.
