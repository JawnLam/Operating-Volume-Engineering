---
type: Fleeting
timestamp: "2026-08-28T00:00:00Z"
Item_ID: ove-release-v2-9-0-plan
title: "OVE v2.9.0 — Release Plan (pre-registered)"
Date_Added: 2026-08-28
Date_Modified: 2026-08-28
Needs_Processing: false
---

# OVE v2.9.0 — Release Plan (pre-registered before build)

**Operator directive (2026-08-28):** codify for OVE what Baseplate's `06-CLOSE-OUT` codifies for product stacks — the working artifact restructured and ready as a self-contained handoff, plus everything after the golden gate that today lives only in precedent. Documented basis: five Spreadwright releases (v1.1.0 → v1.4.0) whose ship rituals — `_shipped/` snapshot, install `git mv` + overlay with preservation, Console re-registration, records close — were reconstructed from session logs each time, codified nowhere in `_design-engine/`. Committed before build per Convention 15; companion eval: `release-v2.9.0-eval.md`.

**What already exists (not rebuilt, only wired to):** Phase 3.12 owns central *schema* registration (Master_Schema); Phase 9 owns a thin design-cartridge close; Convention 7 owns install/update from the operator's side; Convention 14 owns merge-not-clobber for the Grows-Through-Use Zone; P3/Convention 10 imply but do not check independence.

## What ships (scope)

A **minor, additive** release: **v2.9.0**.

1. **New engine chapter `_design-engine/09-CLOSE-OUT.md`** — the release-lifecycle protocol, five sections:
   - **The three copies.** Working tree (`Artifacts/<OV>-vX.Y/` in the design cartridge), immutable ship record (`_shipped/<OV>-vX.Y/` — written once at ship, never edited after; prior records untouchable), and the live install. Which is truth for what; a defect class for editing a ship record.
   - **Upgrade re-ship choreography** (version N → N+1 of an already-installed OV): snapshot to `_shipped/`; install renamed per Convention 7 (`git mv`, history preserved) and overlaid in full; an explicit **preservation list** walked before overlay — Operator-Private Zone files, Grows-Through-Use Zone (merge-not-clobber per Convention 14), documented local override blocks (e.g., a monorepo `.gitignore` override), and one-time setup blocks carried forward with internal paths retargeted but instruction content unchanged; a post-overlay verification that each preserved item survived.
   - **Registry sync** (the ecosystem-catalog half; Convention 12's slot — see item 2): where the destination maintains an OV catalog/console (adapters, registry rows, open-threads, session ledgers) distinct from the Phase 3.12 schema registry, the catalog updates **in the same change** as the ship or the ship is not done; conditional and substrate-agnostic like 3.12 (`n-a` where no catalog exists, logged).
   - **The independence sweep.** A shipped OV may *attribute* OVE (links, category statements) but may not *functionally depend* on it: no shipped file's instructions may require reading OVE's engine or the design cartridge to execute. Greppable recipe included (sweep shipped files for `_design-engine/`, the design-cartridge path, and OVE-internal identifiers used load-bearingly); attribution-by-link is the stated exception.
   - **Graduation.** Criteria and procedure for an OV leaving OVE stewardship: maturity criteria (schema frozen with a P13 policy; passes its own audit; golden-gate clearance history; demonstrated operator use; its own governance loop — CONTRIBUTING and versioning docs — present), the **departure record** (final design-decision entry; registry/catalog status `graduated` with a pointer to the new home; design cartridge retained in place as the permanent record, never deleted), and what changes afterward (upgrades run in the OV's own repo under its own process; OVE's cartridge closes with a terminal state).
   - **Records discipline** (close-out hygiene): every file edited in a release gets its `Date_Modified` synced in the same change; the release-identity surfaces (VERSION identifiers table including sub-identifier rows, CHANGELOG) regenerate together and must agree.
2. **`_meta/CONVENTIONS.md` — Convention 12 claimed: Registry Sync.** Fills the deliberately reserved slot (numbering note at Convention 13; traceability orphan O-3): an OV that ships into an ecosystem keeping any index of OVs — a schema registry, a catalog/console, or both — updates every such index in the same change as the ship. Points at Phase 3.12 (schema half) and `09-CLOSE-OUT` (catalog half + re-sync on upgrade). The Convention-13 numbering note is updated to say the slot is now filled (historical note retained), and traceability O-3 is resolved.
3. **`_meta/FAILURE-MODES.md` — F17: Shipped by precedent.** House format. Trigger: post-gate ritual executed from memory of prior engagements rather than from the engine; a step silently drops (snapshot skipped, a preserved file clobbered, a catalog row stale, `Date_Modified` drift). Documented basis: five hand-executed Spreadwright ships plus the two v2.8.0 banked drifts. Fix/prevention: `09-CLOSE-OUT`, Convention 12, the Phase-9 rewire.
4. **`_design-engine/07-SHIPPING-CHECKLIST.md`** — Phase 9 rewired: retitled to make the design-cartridge close one part of close-out, with a checklist pointer into `09-CLOSE-OUT.md` (three copies, registry sync, records discipline) and an explicit line that **subsequent releases (N → N+1) run the Phase gauntlet plus the 09 upgrade choreography** — the first-ship checklist alone does not cover an upgrade.
5. **`_design-engine/00-START-HERE.md`** — the load-on-demand table gains the `09-CLOSE-OUT.md` row (SHIP-PREP, any re-ship, close-out, graduation).
6. **`_design-engine/03-DESIGN-PROTOCOL.md`** — the SHIP-PREP activity row notes that ship completion includes `09-CLOSE-OUT`; no new activity code (close-out is the tail of SHIP-PREP, as in Baseplate's NEW-STACK route — an eighth activity is not added).
7. **`_meta/TRACEABILITY.md`** — rows for Convention 12 and close-out execution (→ manual walk, no C-check → F17); O-3 removed from Orphans with a resolution note; file's own `Date_Modified` synced (absorbs v2.8.0 banked item 1).
8. **`VERSION.md` + `CHANGELOG.md`** — 2.9.0; the identifiers table's sub-identifier rows corrected per the new records discipline (Design engine → v2.9; Templates → v2.8, reflecting the v2.8.0 template edit; Validator unchanged at v2.7) — absorbs v2.8.0 banked item 2.

## Out of scope (banked or standing)

- Mechanical validator checks for close-out/independence (a C20/C21) — banked; 09's recipes are the manual equivalents per the tooling-posture doctrine.
- The vendored OVE folder rename — **executed by the operator mid-flight** (`-v2.7` → `-v2.8`, commit 9c34b24, 2026-08-28), so this item converts from banked to done-by-operator; the *doctrine* for such renames still lands in 09. Whether the folder later moves to `-v2.9` with this release remains the operator's call.
- Upstream-repo mirror of v2.8.0/v2.9.0 — operator-side or follow-up.
- The v2.8.0 banked multi-turn escalation probe — stays with the golden-session ratchet.
- Retrofitting shipped OVs' own docs to reference 09 — rides each OV's next scoped release.

## QC plan (pre-registered)

- **Verification:** the companion eval — mechanical criteria plus one behavioral probe — run after build by an independent evaluator agent (fresh instance, no drafting role), binary verdicts with cited evidence.
- **No open-ended crucible.** Evaluator observations beyond the criteria are banked, non-blocking.
- **Severity rubric:** any eval criterion FAIL = blocking (fix, re-run the eval in full); notes outside the criteria = banked to the next release's hopper via the results file.
- **Stopping rule:** the same criterion failing twice for distinct causes escalates to the operator.

## Definition of Done

All scope items 1–8 on disk; the eval run by an independent evaluator with every criterion PASS; 0 blocking; banked findings recorded in `release-v2.9.0-eval-results.md`; VERSION and CHANGELOG agree on 2.9.0; plan/eval commit precedes the build commit in history; all work committed and pushed.
