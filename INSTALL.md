---
Item_Prototype: Fleeting
Item_ID: ove-install
Title: "Operating-Volume-Engineering — Install Guide"
Date_Added: 2026-06-01
Date_Modified: 2026-06-06
Needs_Processing: false
---

# Operating-Volume-Engineering — Install Guide

Once you have this folder on disk, the only things you need to use it are an AI assistant and the willingness to have a real design conversation. There is no code to run.

## 1. Install (recommended: git clone with push disabled)

This is the **canonical install pattern per OVE Convention 7** — git-tracked so you can `git pull` future releases; push disabled so you can't accidentally upload your design-cartridge work.

```bash
# Choose a parent folder. Anything works — Dropbox-synced, iCloud-synced, vault, etc.
# Example uses ~/Operating-Volumes/ as the parent.
mkdir -p ~/Operating-Volumes
cd ~/Operating-Volumes

# Clone into a folder named with the current major.minor.
# (Check VERSION.md or the GitHub releases page for the current version.)
git clone https://github.com/JawnLam/Operating-Volume-Engineering.git \
  Operating-Volume-Engineering-v1.2

# Disable push remote — protects your design-cartridge work against accidental upload.
cd Operating-Volume-Engineering-v1.2
git remote set-url --push origin DISABLED_TO_PREVENT_ACCIDENTAL_PUSH_OF_PERSONAL_WORK

# Verify
git remote -v
# Expect: origin fetch URL real; origin push URL = DISABLED_TO_PREVENT_ACCIDENTAL_PUSH_OF_PERSONAL_WORK
```

**Why the folder name has a version suffix.** The convention is `Operating-Volume-Engineering-v<major>.<minor>`. When a new major.minor ships (e.g., v1.3), `OPERATOR-GUIDE.md § Updates` walks you through renaming the folder so old and new can briefly coexist during the transition.

**Why push is disabled.** Almost everything you do in this folder beyond reading the engine is private design work — manifests, decision logs, session histories, schema drafts. The push-disabled default prevents the worst-case operator-error: `git push` accidentally uploading your in-progress design to the public OVE repo. You can re-enable push to your own fork if you want to contribute back upstream (see `OPERATOR-GUIDE.md § Contributing back`).

## 1a. Alternative install (no git tracking)

If you don't want git tracking — you'd rather treat this as a snapshot reference, no updates — you can also just download the folder:

- **Plain copy:** Download a release ZIP from the GitHub releases page; unzip anywhere your AI assistant can read.
- **Cloud-synced folder** (Dropbox, iCloud, OneDrive, Google Drive) — convenient if you want the same content available across devices.
- **Obsidian vault** — open as a vault if you want graph view across your designs-in-progress.

The folder is fully self-contained. No network fetch happens at runtime; no paths are hard-coded. The trade-off versus the git-tracked install: you don't get `git pull` updates — you have to re-download each release.

## 2. (Optional) Configure your user profile

If you want consistent personalization across every design session:

```
cp _USER.md.template _USER.md
```

Fill in your name (the spelling matters — see `_design-engine/_meta/FAILURE-MODES.md` for why), communication preferences, and any global notes.

## 3. (Optional) Initialize git

If you want version control on your designs-in-progress (recommended):

```
cd "Operating-Volume-Engineering"
git init
git add .
git commit -m "Initial install"
```

The shipped `.gitignore` excludes cartridge session content (`Sessions/*.md`, `_design-state.md`) by default so the folder can be shared without leaking your active design work. The trade-off is that **your own design history is not tracked unless you opt in** — the next section is the opt-in recipe.

## 3a. Tracking your own design history

The shipped `.gitignore` is privacy-safe by default — it excludes `_design-state.md` and `Sessions/*.md` so you can share the folder without leaking your in-progress conversations. The trade-off: the OV's core thesis is *"state lives in files,"* and that state isn't version-controlled unless you opt in.

To track your own cartridge in git despite the default ignore:

```
cd "Operating-Volume-Engineering"

# Replace <YourCartridge> with your actual cartridge folder name
git add -f <YourCartridge>/_design-state.md
git add -f <YourCartridge>/Sessions/
git commit -m "Track <YourCartridge> design history"
```

The `-f` flag forces git to add paths that match `.gitignore`. Once added, they'll be tracked normally on subsequent commits.

**Why the default excludes your own work.** The OV is designed to be portable — clone, fork, share. If your `_design-state.md` were tracked by default, anyone you shared the folder with would see your active design conversations. The opt-in pattern keeps the sharing case clean while letting you preserve your own history when you want it.

**If you prefer the inverse default** (track your own work; remove the ignore), edit `.gitignore` and remove the lines under the *"Personal design work"* comment block.

## 4. First session walkthrough

1. **Open the folder in your AI environment.**
2. **Send the AI a single message:**

   > Read `AI-BOOTSTRAP.md` and help me design a new operating volume.

   Or:

   > Read `AI-BOOTSTRAP.md` — I want to audit my existing OV at `[path]`.

   Or:

   > Read `AI-BOOTSTRAP.md` — what is an operating volume, exactly?

3. **Wait for the readiness statement.** The AI should respond with a short paragraph confirming it has read the design engine, plus either a clarifying question (new OV), a session-activity proposal (existing cartridge), an offer to audit (audit mode), or a direct conceptual answer (orientation).

   If the AI responds with a long explanation or generic greeting instead, it skipped Phase 0. Tell it: *"Read `AI-BOOTSTRAP.md` in full before responding."*

4. **Have the conversation.** Expect one question at a time. The AI guards against multi-bullet questionnaires — that's a documented failure mode.

## 5. What "done" looks like

A complete design engagement produces, inside your cartridge here:

- A filled-in `_ov-manifest.md`, `_design-decisions.md`, `_schema-draft.md`, `_design-state.md`
- Drafts in `Artifacts/` of every file the new OV will ship with (`AI-BOOTSTRAP.md`, `README.md`, the engine files, the templates, the bootstrap-new-cartridge prompt)
- A session log per design conversation in `Sessions/`

Once the artifacts in your cartridge are ready, the AI walks you through:

1. Creating the new OV's folder elsewhere on disk
2. Copying artifacts into place
3. Final scrubbing for personal data
4. License + version + README
5. `git init` and GitHub push (if desired)

See `_design-engine/07-SHIPPING-CHECKLIST.md` for the full shipping flow.

## 6. Troubleshooting

| Symptom                                                | Likely cause / resolution                                                                                                                          |
|--------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| AI dumps a multi-bullet questionnaire                  | It skipped or ignored the design protocol. Stop, say *"Ask one question at a time, conversationally."* This failure is in `_meta/FAILURE-MODES.md`. |
| AI starts designing without asking who the OV is for   | Same root cause. The clarifying interview is non-optional.                                                                                          |
| AI invents tools, frameworks, or methods that aren't real | Stop and correct. Fabrication discipline in `_design-engine/05-WRITING-FOR-AI.md`.                                                                |
| AI uses a guessed name for you (e.g., parsing a username) | Stop and correct with placeholder. See `_meta/FAILURE-MODES.md` — this is a documented recurrence pattern.                                       |
| AI never produces a readiness statement                | Re-send: *"Read `AI-BOOTSTRAP.md` in full before responding."*                                                                                       |
| `_design-state.md` is missing or stale                 | See `OPERATOR-GUIDE.md` recovery procedure.                                                                                                          |

For deeper guidance, see `OPERATOR-GUIDE.md`. To extend the engine itself, see `CONTRIBUTING.md`.

## 7. Updating (when a new release ships)

When OVE ships a new release on GitHub (announced in `CHANGELOG.md`):

```bash
cd ~/Operating-Volumes/Operating-Volume-Engineering-v<your-current-major>.<minor>

git fetch origin
git log --oneline HEAD..origin/main           # preview what's incoming

# If you have no local engine modifications: clean fast-forward
git pull --ff-only origin main

# If you have local engine modifications: stash → pull → pop
git stash push --include-untracked -m "pre-update state"
git pull --ff-only origin main
git stash pop                                  # resolve any conflicts
```

**When major.minor changes (e.g., v1.2 → v1.3 ships):**

```bash
cd ~/Operating-Volumes/
mv Operating-Volume-Engineering-v1.2 Operating-Volume-Engineering-v1.3
```

The CHANGELOG entry for the new major.minor will tell you whether folder rename is recommended or required. For pure-patch releases (e.g., v1.2.0 → v1.2.1), no folder rename is needed.

For troubleshooting common update issues (fast-forward conflicts, stash-pop merge conflicts, dirty working tree blocking pull), see `OPERATOR-GUIDE.md § Updates and troubleshooting`.

## Version

This install guide ships with Operating-Volume-Engineering v1.2.0. See `VERSION.md`.
