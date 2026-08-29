---
type: Fleeting
timestamp: "2026-08-28T00:00:00Z"
Item_ID: ove-engine-09-close-out
title: "OVE Engine — 09 Close-Out"
Date_Added: 2026-08-28
Date_Modified: 2026-08-28
Needs_Processing: false
doc_type: design-engine
role: close-out-protocol
scope: subject-agnostic
updated: 2026-08-28
---

# 09 — CLOSE-OUT (release lifecycle: ship records, upgrades, registry sync, graduation)

> **A cleared gate is not a finished release.** An OVE-designed OV is born in handoff shape (P3: the folder bootstraps a stranger), so unlike a working document stack it needs no restructuring — what it needs is everything *after* the gate: the immutable ship record, the install choreography that never destroys operator state, the ecosystem indexes updated in the same change, and the records closed with their timestamps true. Until v2.9.0 that ritual lived only in precedent — reconstructed from prior session logs at each release, with nothing to catch a dropped step (F17, shipped-by-precedent). This chapter is that ritual, codified. First-ship engagements reach it through `07-SHIPPING-CHECKLIST.md` Phase 9; **subsequent releases (version N → N+1) run this chapter's upgrade choreography in addition to the Phase gauntlet** — the first-ship checklist alone does not cover an upgrade.

## The three copies

Every OV under OVE stewardship exists in up to three places, and each is truth for something different:

1. **The working tree** — `<Cartridge>/Artifacts/<OV-Name>-v<major>.<minor>/` inside the design cartridge. Truth for *what the next release will contain*. Edited freely between releases.
2. **The ship record** — `<Cartridge>/_shipped/<OV-Name>-v<major>.<minor>/`, a full snapshot taken at the moment of release. Truth for *what each release actually contained*. **Written once, never edited after.** Every prior release's record is untouchable — editing a ship record, for any reason including fixing a typo, is a defect (it falsifies history the golden logs and changelogs cite). A defect found in a ship record is fixed in the working tree and shipped forward.
3. **The live install** — the copy the operator actually runs, wherever Convention 7 installed it. Truth for *operator state*: the filled Operator-Private files, the grown Convention-14 zones, any documented local overrides. The engine content inside it is a replaceable projection of a ship record; the operator state inside it is irreplaceable and is what the upgrade choreography exists to protect.

## Upgrade re-ship choreography (version N → N+1 of an installed OV)

Runs after the new release clears its gates (the Phase gauntlet, including the golden session and any Convention-15 sampling plan). Order matters.

1. **Snapshot first.** Copy the cleared working tree to `_shipped/<OV-Name>-vNEW/`. The record exists before anything touches the install, so a botched overlay can always be re-run from it.
2. **Walk the preservation list — before overlaying anything.** Enumerate, from the *install*, everything the overlay must not destroy:
   - **Operator-Private Zone** files (Convention 8): the filled `_USER.md`, filled policy/config files, live cartridges — anything the shipped `.gitignore` marks operator-private, whether or not this install's git actually ignores it.
   - **Grows-Through-Use Zones** (Convention 14): merge-not-clobber, always — the release's seed entries merge *into* the operator's grown file, never over it.
   - **Documented local overrides**: blocks the operator has added to shipped files and marked as local policy (e.g., a monorepo `.gitignore` override block). These survive verbatim.
   - **One-time setup blocks** still pending (an un-run registration block, an un-finished install step): carried forward into the new install with internal paths retargeted to the new folder name — **instruction content unchanged**. A pending block that silently vanishes in an upgrade strands the step it existed to trigger.
3. **Rename and overlay.** Rename the install folder per Convention 7 (`git mv <OV>-vOLD <OV>-vNEW` where the install is version-controlled — history preserved), then overlay the new release in full: stale engine files deleted, new files added. The overlay replaces engine content; the preservation list is what it must route around.
4. **Verify preservation.** After the overlay, confirm each item from step 2 survived: private files present and unmodified, grown zones containing both the operator's entries and any new seeds, override blocks intact, pending one-time blocks present with retargeted paths. **An upgrade that loses one preserved item is a failed upgrade** — restore from the pre-upgrade state and re-run; do not hand-patch the damage forward.
5. **Registry sync** (next section), then **records** (last section).

## Registry sync (Convention 12)

Where the destination ecosystem keeps any index of OVs, **every index updates in the same change as the ship — or the ship is not done.** Two kinds of index exist, and they are separate obligations:

- **The schema registry** (e.g., a vault `Master_Schema.yaml`) — owned by Phase 3.12 at first ship. On an upgrade it re-fires **only if the schema version moved**; an additive prose release leaves it untouched, and saying so in the release notes is part of the sync.
- **The catalog** (e.g., an OV console: adapter files, a registry table, open-threads, a session ledger) — this chapter's obligation, first ship and every upgrade alike: the OV's directory name, version, activity list, and description current; the catalog's narrative surfaces (open threads, upgrade notes) reflecting the release; the engagement's ledger entries appended.

Like Phase 3.12, this is **conditional and substrate-agnostic**: a destination with no registry and no catalog makes the whole section `n-a` — log that and proceed. A destination with either makes it a gate.

## The independence sweep

A shipped OV may **attribute** OVE — a category statement, a link to the OVE repository in `VERSION.md` or `README.md` — but may not **functionally depend** on it: no shipped file's instructions may require the reader to open OVE's engine, the design cartridge, or any file outside the shipped folder in order to execute. (This is Baseplate's "the builder never needs Baseplate," generalized: *the operator never needs OVE.*)

Mechanical recipe (run on the ship candidate before snapshot):

```bash
# From the working-tree root — hits are candidate defects, judged by the rule below:
grep -rn "_design-engine/\|Operating-Volume-Engineering" . --include="*.md" | grep -v "_meta/"
```

Judge each hit: a **link or category attribution** (README/VERSION provenance lines) passes; an **instruction that points the OV's operator or AI into OVE to complete a task** fails and is rewritten to be self-contained. Design-record files the OV legitimately ships in `_meta/` (golden logs citing the engagement) may reference history freely — the rule binds the files that *operate*.

## Graduation (leaving OVE stewardship)

Some OVs outgrow the design cartridge: they acquire their own repository, their own release cadence, their own contributors. Graduation is the deliberate handoff of stewardship — not a copy operation, a **status change with a record**.

**Maturity criteria** (all should hold; the operator may waive any explicitly, recorded in the departure record):

1. Schema frozen with a stated freeze policy (P13) and a version/migration discipline in its own docs.
2. Passes its own audit — the OV's validation checklist or equivalent runs clean against the shipped tree.
3. Golden-gate clearance history — at least one gated release with its log and transcripts shipped or referenced.
4. Demonstrated use — real sessions run by the operating persona, not only design-side tests.
5. Its own governance loop — `CONTRIBUTING.md`, versioning docs, and an update path that does not route through OVE's design cartridge.

**The departure record** (all three, in the same change):

1. A final entry in the design cartridge's `_design-decisions.md`: graduated, date, destination (repo/location), criteria met or waived.
2. The ecosystem catalog's status for the OV set to **`graduated`** with a pointer to the new home (Convention 12 — the index must not go stale at the moment of departure).
3. The design cartridge itself **retained in place, closed** — `_design-state.md` phase set to `graduated`, a final session log written. The cartridge is the permanent record of how the OV came to be; it is never deleted and never migrates with the OV.

**After graduation:** upgrades run in the OV's own repository under its own process; OVE's engine no longer gates them. If the OV later returns for OVE-level rework (a redesign, a schema break), that is a new engagement in a new or reopened cartridge, recorded as such.

## Records discipline (every release, graduation included)

- **Timestamps are part of the change.** Every file edited in a release gets its frontmatter `Date_Modified` synced in the same change — a body edit with a stale timestamp is a defect (Convention 1's time-sync, enforced here at the moment it historically drifts).
- **Release-identity surfaces regenerate together.** The `VERSION.md` identifiers table — including sub-identifier rows (engine, templates, validator, and their like) — and `CHANGELOG.md` are regenerated in the same change and must agree; a sub-identifier row that no longer matches the surfaces that actually changed is a defect.
- **The design cartridge closes per Phase 9**: state file phase updated, decision entry appended, final session log written, next-session thread opened.

## Checklist (all boxes before the release is called done)

- [ ] Ship record snapshotted to `_shipped/` before the install was touched; no prior record edited
- [ ] Preservation list walked before overlay; post-overlay verification confirmed every item survived
- [ ] Install renamed per Convention 7 and fully overlaid (stale files removed)
- [ ] Pending one-time blocks carried forward, paths retargeted, instruction content unchanged
- [ ] Registry sync complete — schema registry (if the schema moved) and catalog (always, where one exists) — or logged `n-a`
- [ ] Independence sweep run on the ship candidate; every hit judged; no functional dependence shipped
- [ ] `Date_Modified` synced on every edited file; VERSION identifiers (sub-identifier rows included) and CHANGELOG agree
- [ ] Design cartridge closed per Phase 9
- [ ] *(Graduation only)* all three departure-record entries written in the same change; cartridge retained and closed
