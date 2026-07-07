# ✅ WAVE 1 — DOC 1 COMPLETE: BLUEPRINT → v2.1

**File:** `1_CONSTITUTION-APP_FACTORY_BLUEPRINT_v2_0.md` (filename unchanged per Wave 1 rules)

## CHANGES MADE

| # | Change | Finding |
|---|--------|---------|
| 1 | Standard header block at top (Version 2.1 · 2026-07-07 · Active · Tier 1 — Constitution · Pairs-with canonical names). Stray line-1 bold title + old H1 folded in; "The Stark Protocol" preserved as subtitle | F-018, F-008 |
| 2 | Title "AI App Factory" → "App Factory" everywhere (remaining instance lives only in the v2.1 history row describing the rename) | F-008 |
| 3 | New section **🔀 WHICH PIPELINE AM I IN?** after THE BIG PICTURE: Conversion-vs-Greenfield comparison table, condensed FFM §4 operator router (3 questions, de-Stitched), hybrid note, ownership split (HANDOFF_PACKAGE_PLAYBOOK = conversion detail; agent playbooks = greenfield detail) | F-030 |
| 4 | DATA_CONTRACT ownership paragraph in the router section: conversion = Architect pre-authors from Brain Drain evidence; greenfield = Engineer authors from APP_BRIEF + UI_SPEC | F-029 |
| 5 | New section **🔎 PHASE 0: RECON (BEFORE ANY AUTHORING)** + `PHASE 0` block prepended in THE FULL WORKFLOW diagram | F-003 |
| 6 | One-line Karpathy Protocol pointer placeholder after the PLAYBOOK DOCS table (no import) | D-011 |
| 7 | Bottom block reworked: "Changelog" → "## Version History"; version/date moved to header; new v2.1 row with finding IDs | D-018 |

## VERIFICATION GATES

| Gate | Result |
|---|---|
| `grep -ri stitch` (live doctrine) | **0** — 2 hits remain, both inside Version History rows (exempt per approved amendment, D-018) |
| `grep -n "_v[0-9]"` | **0** |
| `grep -c "â"` | **0** |
| Standard header present | ✓ |
| New Version History entry | ✓ |

## THINGS I DIDN'T TOUCH

- Workflow Phases 1–5 content, BIG PICTURE diagram, Engineer output examples (Pepper's Rig), Blind Spots table — all as-is.
- Version History rows for (unversioned) and 2.0 — Stitch mentions preserved as historical record.
- All other repo files.

## CONCERNS

- F-004 (Blueprint indexes ~8 of 27 docs) intentionally NOT addressed — MANIFEST work, Wave 6.
- The doc's filename still carries `_v2_0` while content is v2.1 — expected; renames land at MANIFEST time (Wave 6).

## Suggested commit

wave1(blueprint): v2.1 — pipeline router, Phase 0 recon, F-003/F-008/F-029/F-030
