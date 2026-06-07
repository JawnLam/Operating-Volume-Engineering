---
Item_Prototype: Fleeting
Item_ID: ove-operator-guide
Title: "Operating-Volume-Engineering — Operator Guide"
Date_Added: 2026-06-01
Date_Modified: 2026-06-06
Needs_Processing: false
---

# Operating-Volume-Engineering — Operator Guide

This guide is for the human running OVE day-to-day: how design sessions actually work, common failure modes, how to recover, and how to keep your design cartridges healthy through a multi-session design engagement.

If you're setting up for the first time, read [`INSTALL.md`](INSTALL.md) first.

---

## 1. How a design session actually works

1. **READ** — AI reads `AI-BOOTSTRAP.md` → `_design-engine/` → your cartridge's manifest/state/recent sessions
2. **DIAGNOSE** — AI inspects state for open threads, decisions pending, schema gaps
3. **PROPOSE** — AI proposes a session activity (one of the activities defined in `_design-engine/03-DESIGN-PROTOCOL.md`)
4. **WAIT** — AI waits for your confirmation or override
5. **EXECUTE** — the actual design conversation
6. **CAPTURE** — AI records decisions, schema updates, artifact drafts
7. **WRITE session log** — new file in `<Cartridge>/Sessions/`
8. **UPDATE `_design-state.md`** — overwritten with new state
9. **END with Open Threads** — explicit seed for the next session

If a session ends without phases 6–9, tell the AI to finish.

## 2. Reading the cartridge state

`<Cartridge>/_design-state.md` is the single source of truth for the design engagement. Useful sections:

- **Design phase** — where the design currently sits (interview / schema-drafting / artifact-drafting / scrubbing-and-shipping)
- **Decided** — choices that are locked
- **Open** — questions still unresolved
- **Artifact status** — which shipping files have drafts, which don't
- **Open Threads** — what next session is supposed to address

## 3. Common failure modes and how to fix them

### AI dumps a multi-bullet questionnaire

**Symptom:** During cartridging or early interview, the AI sends a single message with seven or eight questions in a list.

**Fix:** Stop. Say *"Ask one question at a time. Probe my answers. This is a conversation, not an assignment."* The protocol in `_design-engine/03-DESIGN-PROTOCOL.md` and the failure-mode entry in `_design-engine/_meta/FAILURE-MODES.md` both explicitly forbid this — refresh the AI on it if it keeps happening.

**Prevention:** The very first sentence of `BOOTSTRAP-NEW-OV.md` says "one question at a time, conversationally." Some models default to bulk-questioning anyway. Watch for it.

### AI fabricates a tool, framework, or method

**Symptom:** The AI cites a "framework" or "method" or "standard practice" you've never heard of, and it doesn't quite ring true.

**Fix:** Stop and ask the AI to verify. If fabricated, say *"That isn't real. From now on, if you're not sure something exists, say so."* The discipline is in `_design-engine/05-WRITING-FOR-AI.md`.

### AI uses a guessed name for you

**Symptom:** The AI calls you by a name you haven't provided (often parsed from your username or file path).

**Fix:** Stop and correct. *"That's not my name. Use a placeholder until I tell you."* This is in the failure-modes catalog as a *recurrence pattern* — this specific error has been triggered multiple times historically, which is why it's a load-bearing principle in `02-DESIGN-PRINCIPLES.md`.

### AI proposes a schema that doesn't fit the domain

**Symptom:** The schema feels generic — Items that don't naturally exist in your domain, relationships that don't map to how you actually think about the work.

**Fix:** Stop and walk through `_design-engine/04-SCHEMA-DESIGN.md` Q1–Q8 again, this time more carefully. The schema should *come out of* the domain, not be retrofitted to it.

### `_design-state.md` is corrupted or stale

**Symptom:** AI says it can't read your state, or the state contradicts the session logs.

**Fix:** Open the most recent session log in `<Cartridge>/Sessions/`. Reconstruct `_design-state.md` from it using `_design-engine/_templates/TEMPLATE-design-state.md`. If multiple sessions back are unrecoverable, walk the `_design-decisions.md` log to rebuild the picture.

### AI starts implementing artifacts before design decisions are locked

**Symptom:** AI begins drafting `AI-BOOTSTRAP.md` for the new OV before the schema is settled.

**Fix:** Stop. The design protocol has an explicit ordering: interview → schema → cartridge shape → state-persistence model → bootstrap → engine → templates → root docs. Drafting before deciding produces artifacts you'll throw away. Tell the AI to back up and finish the design phase first.

### Self-similarity fails — the OV-being-designed can't be designed by THIS OV

**Symptom:** While walking through `_design-engine/04-SCHEMA-DESIGN.md`, you realize the design you're proposing for the new OV doesn't fit into the cartridge-and-engine pattern this OVE is built on.

**Diagnostic:** This usually means one of three things:
1. The new "OV" isn't actually an OV — it's a smaller artifact (a skill, a prompt pack, a Custom GPT)
2. The new OV is significantly different in shape from existing OVs and requires extending OVE itself (a v1.x update)
3. You're trying to shoehorn a non-OV-shaped need into the OV pattern when a different pattern would serve better

Treat this as a strong signal. Don't suppress it.

## 4. Cartridge health over time

A design cartridge can drift over weeks. Periodic check:

- **Every ~5 sessions:** ask the AI to do a state-audit pass — list everything decided, everything open, every artifact's status. Surfaces drift.
- **At schema-lock:** ask the AI to run the schema through the audit checklist in `_design-engine/_meta/SCHEMA-OF-SCHEMAS.md`.
- **Before shipping:** run the full scrubbing + verification checklist in `_design-engine/07-SHIPPING-CHECKLIST.md`.

## 5. Sharing or transporting a cartridge

A design cartridge is a self-contained folder. Zip and send. The recipient drops it into their own OVE folder. Cartridges are user-specific (the decisions and the schema reflect *your* domain framing), so the recipient should treat it as reference rather than as a head start on their own design.

## 6. Multiple cartridges in parallel

No limit. You can have several OVs in design at once. When starting a session, name the cartridge in your first message.

## 7. When something breaks and you can't fix it

- Open `CONTRIBUTING.md` and see if your case is a bug worth reporting upstream.
- Worst case: archive the cartridge as `99-Archive-<Name>/`, open a fresh cartridge with the AI, and import the decisions and schema by hand.

## 8. Engine vs your work — the four content zones (Convention 8)

Your installed OVE folder has four content zones. Knowing which is which prevents the operator-pulls-and-loses-work failure mode.

### Engine Zone — release-owned; updated by `git pull`

| Path | Notes |
|------|-------|
| `README.md`, `INSTALL.md`, `OPERATOR-GUIDE.md`, `CONTRIBUTING.md`, `LICENSE.md`, `VERSION.md`, `CHANGELOG.md` | Front-door docs |
| `_design-engine/` | The full design protocol — engine chapters, templates, meta |
| `_Prototypes/` | OVE's own Prototype definitions (Convention 6) |
| `_USER.md.template` | The template, not your filled-in `_USER.md` |
| `.gitignore` | Engine-zone file; its patterns define your Operator-Private Zone |

**Do not edit Engine Zone files directly.** Updates from `git pull` overwrite them. Customizations belong in the Operator-Extension Zone or in `_USER.md` overrides where supported.

### Operator-Private Zone — gitignored; never tracked

The `.gitignore` excludes these so they never get pushed and never get touched by `git pull`:

- `_USER.md` (your operator profile)
- `<Cartridge>/_design-state.md` (cartridge state)
- `<Cartridge>/Sessions/*.md` (session logs)
- Anything else you `git add -f` then later `git rm --cached` — those go in `.gitignore` too

If you want to track your own design history, see `INSTALL.md § 3a — Tracking your own design history` for the opt-in recipe.

### Operator-Extension Zone — your design cartridges; survives `git pull`

This is where your work lives. Every design cartridge you open through OVE (a new OV being designed, an audit-in-progress, your own evolution of a worked example) becomes a folder at the OVE root.

`<Cartridge>/` folders are not in OVE's release, so `git pull` never touches them. They're yours.

### Shipped Examples Zone — release-owned; updated by `git pull`

The five worked-example cartridges that demonstrate OVE:

- `Long-Form-Writing/`
- `LifeLong-Learning-Retrospective/`
- `Negotiation-Preparation/`
- `Relationship-Cultivation/`
- `SOLVE-eX-Retrospective/`

**Do not edit Shipped Examples directly.** If you want to riff on an example, copy it into an Extension Zone cartridge (`mv Long-Form-Writing My-LFW-Variant`) and customize there.

## 9. Updates and troubleshooting

The canonical update workflow lives in `INSTALL.md § 7`. Common scenarios:

### Clean fast-forward (no local engine modifications)

```bash
cd ~/Operating-Volumes/Operating-Volume-Engineering-v<your-major>.<minor>
git fetch origin
git log --oneline HEAD..origin/main          # what's incoming
git pull --ff-only origin main
```

### Fast-forward fails because you have local engine modifications

```bash
git status                                    # see what's modified
git stash push --include-untracked -m "pre-update state"
git pull --ff-only origin main
git stash pop                                 # may produce conflicts on engine files you edited
```

If `git stash pop` reports conflicts, the conflict is between *your local edit* of an engine file and *the upstream release's version*. You almost always want the upstream version (engine evolution generally improves what's there):

```bash
git checkout --theirs <conflicting-file>
git add <conflicting-file>
# OR — abandon your local edits entirely:
git checkout origin/main -- <conflicting-file>
```

If your local edit was load-bearing, copy it to a side file before checkout, then reconcile.

### Update lost a file you cared about

`git pull` only updates tracked paths. If a file disappeared, either: (a) the release explicitly removed it (the `CHANGELOG.md` will say so), or (b) it was a gitignored file you forgot was ignored. For (a), the file is recoverable via `git log --all --oneline -- <path>`. For (b), check whether the file matched a `.gitignore` pattern.

### Major.minor folder transition

When the release notes say to rename your folder:

```bash
cd ~/Operating-Volumes/
mv Operating-Volume-Engineering-v<old> Operating-Volume-Engineering-v<new>
cd Operating-Volume-Engineering-v<new>
git status   # should show clean
```

The folder rename doesn't affect git; the rename is for your filesystem clarity.

### Contributing back upstream

To contribute back (open a PR against the upstream OVE), re-enable push to *your own fork* (never to upstream):

```bash
# Replace with your fork's URL
git remote set-url --push origin https://github.com/<your-username>/Operating-Volume-Engineering.git

# Make a branch, commit, push to your fork, open a PR on GitHub
git checkout -b my-contribution
# ... your changes ...
git commit -m "..."
git push origin my-contribution
```

When you're done contributing, re-disable push to protect your private work going forward:

```bash
git remote set-url --push origin DISABLED_TO_PREVENT_ACCIDENTAL_PUSH_OF_PERSONAL_WORK
```

## Version

This operator guide ships with Operating-Volume-Engineering v1.0.0.
