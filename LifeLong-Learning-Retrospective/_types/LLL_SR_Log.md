---
Item_ID: "UUID-OR-SLUG"
type: LLL_SR_Log
title: "SR Log"
lll_Subject: ""
lll_Phase: 
Date_Added: 
Date_Modified: 
Needs_Processing: false
AI_Instructions: ""
---

# Phase <N> SR Performance Log

*Append-only. Every SR quizzing session adds rows.*

| Date | Atom | Card | Result | Streak | Session |
|------|------|------|--------|--------|---------|

## Rules

- Result values: `again` | `hard` | `good` | `easy`
- Streak counts consecutive non-`again` results
- Any atom with two or more `again` results in its last three reviews gets flagged `lll_Status: weak` in `_state.md`
- No SR quizzing for atoms below mastery level 2
