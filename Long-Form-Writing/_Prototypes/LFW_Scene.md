---
Item_Prototype: LFW_Scene
Item_ID: "<slug>"
Title: "<Scene title>"
lfw_Manuscript: ""
lfw_Item_Type: scene
lfw_Status: planned          # planned | drafting | drafted | revising | revised | final
lfw_Parent: ""               # wikilink to Chapter or Act
lfw_Order_In_Parent:
lfw_Setting: ""              # location / time
lfw_POV: ""                  # character or narrator
lfw_Characters_Present: []
lfw_Purpose: ""              # one-sentence: what this scene must do
lfw_Value_Shift_From: ""     # v1.2: starting value-state (e.g., "safe", "hopeful", "ignorant")
lfw_Value_Shift_To: ""       # v1.2: ending value-state (must differ from `from` for the scene to turn)
lfw_Scene_Type: scene        # v1.3.1: scene (value-shifting, default) | sequel (reactive-processing) | scene-sequel (compound)
lfw_First_Drafted: null
lfw_Word_Count: 0
Date_Added:
Date_Modified:
Needs_Processing: false
---

# <Scene title>

## Setting and Stakes

*Where. When. Who's present. What's at stake. POV.*

## Value-shift *(v1.2 — for lfw_Scene_Type: scene or scene-sequel)*

*The load-bearing fiction-craft discipline. Fill in before this scene is marked `drafted`. If `from` and `to` are identical, the scene doesn't turn — SCENE-AUDIT will flag. Omit this section entirely if lfw_Scene_Type is `sequel`.*

- **Whose want drives this scene:** *(character, what they want in this scene)*
- **What's the conflict:** *(what stands between the want and its satisfaction)*
- **Start-state (from):** *(value-state at the scene's opening — safe / hopeful / ignorant / connected / etc.)*
- **End-state (to):** *(value-state at the scene's close — must be different, or the scene doesn't turn)*
- **The turn — what changes:** *(one sentence: what is true at the end that wasn't at the start?)*
- **But / Therefore connector to the next scene:** *(the next scene happens because of this one — "therefore" — or despite it — "but." If "and then" is the only honest connector, the spine has gone slack here.)*

## Sequel *(v1.3.1 — for lfw_Scene_Type: sequel or scene-sequel)*

*The reactive-processing beat. Reaction → Dilemma → Decision. The decision becomes the NEXT scene's want. Omit this section entirely if lfw_Scene_Type is `scene`. See chapter 14 §1 for the scene-and-sequel discipline.*

- **Whose reaction this sequel carries:** *(POV character)*
- **Reaction (emotional, physical, immediate):** *(the first response to the prior scene's outcome)*
- **Dilemma (the new situation):** *(what new choice the prior outcome forces)*
- **Decision (the new want):** *(what the character decides to pursue next)*
- **Carry-forward connector to next scene:** *(the decision IS the next scene's want — make the linkage explicit)*

## Beats

*Ordered list of beats in this scene. Wiki-links to Beat atoms.*

1. [[Beat-slug-1]]
2. [[Beat-slug-2]]

## Prose

*The drafted scene. Or `*To be drafted*` if not yet.*

## Connections

- **Sets up:** *(future scene / payoff — these are `prefigures` relations and feed `_promises.md`; see chapter 11 §3)*
- **Pays off:** *(prior scene / setup)*
- **Parallels:** *(structural parallel scenes)*

## Open Notes

*Known weaknesses. Alternate versions considered. Things to revisit.*
