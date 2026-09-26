# GATE 2 — UPDATE MAP — SYNC_2026-09-26_test-c-recovery

> TEST C — RECOVERY VALIDATION · ENGINEER SEAT · CURRENT GATE: GATE 2 — UPDATE MAP APPROVAL
> Written 2026-09-26 11:33 BST, before on-screen display. Full map: `_AUDIT/SYNC_2026-09-26_test-c-recovery/UPDATE_MAP.md` (Status DRAFT).

## Run header
- BASE_SHA `dd6d496a3b269a6bf83ce4e85101d8e0e6e785b9` (launch-named = clean HEAD). Run branch: reuse `test/docset-sync-v07-recovery-001` (at BASE). Merge target: NONE (Gate 1 ruling). Route: local git at Hub clone.
- Lint baseline 9 (VERSIONED-REFS ×8, HEADER-PRESENCE ×1). Docs 31 disk / 31 rows / 29 stated → DRIFT-2026-09-26-01 parked.

## IDs
- IN-2026-09-26-01 (class 2) — CHANGE.

## Propagation search
- 6 terms (T1 `TEST-C-SYNTHETIC`, T2 `Recovery/resume validation`, T3 `synthetic validation`, T4 target + "Version History", T5 target + v2.2, T6 target name) over the five tiers + MANIFEST + CHANGELOG.
- 12 hit lines: 1 CHANGE (MANIFEST.md:29), 9 CONSISTENT, 2 HISTORY (ARCHITECT_PLAYBOOK.md:613, CHANGELOG.md:13). Zero undispositioned. New-wording terms: 0 hits.
- Awareness: `_OTHERS/MASTER_DOC_LIST_v1_0_FINAL.md:38` legacy filename — OUT-OF-SCOPE, untouched. `_SKILLS/`: 0 hits.

## Touch list — 1 doc: `02_PIPELINE_AGENTS/ARCHITECT_QUESTIONNAIRE.md` (← 1)
- 1a Header L3 → `> **Version:** 2.3 · **Date:** 2026-09-26 · **Status:** Active` — ENGINEER-PROPOSED (2.3 by Hub precedent; date = execution date).
- 1b New Version History row before L174 (newest-first) — ENGINEER-PROPOSED text; quoted note INTAKE-VERBATIM:
  `| 2.3 | 2026-09-26 | **TEST C synthetic validation (IN-2026-09-26-01).** Added the synthetic note "TEST-C-SYNTHETIC-01 — Recovery/resume validation only." below this table. No doctrine changed; questionnaire, APP_BRIEF template, ⛔ Hard Gate, 📌 Reality Rule, and Planning State untouched. |`
- 1c Note line after the table (after L177 blank, before `---` L178): `TEST-C-SYNTHETIC-01 — Recovery/resume validation only.` — INTAKE-VERBATIM text; plain-paragraph formatting ENGINEER-PROPOSED (not a blockquote).
- Archive: `_ARCHIVE/ARCHITECT_QUESTIONNAIRE_v2_2.md`.

## Infra (§G)
- MANIFEST.md:29 row 2.2/2026-07-07 → 2.3/execution date; MANIFEST L3 Date bumped. Count lines :6 :12 :76 :114 untouched (drift). ← map unchanged.
- CHANGELOG: +1 row after L34 — ENGINEER-PROPOSED: `| 2026-09-26 | ARCHITECT_QUESTIONNAIRE v2.3 | TEST C synthetic validation note added below the Version History table; no doctrine change (v2.2 archived) | IN-2026-09-26-01 |`; L3 Date bumped.

## Mechanical items resolved from evidence (approved with the map)
- M-1: this clone has `core.autocrlf=true` (worktree CRLF, blobs LF). The skill's literal `git show | diff` fidelity check gives a false DIFF. Method: `git hash-object <archive>` and staged `git rev-parse :<archive>` must equal BASE blob `15780306c6ad4dc2b5b3ab8d393d7d86a0643852`.
- M-2: at resume the tree holds this run's uncommitted run-state. The resumed session verifies the dirty set equals the §N step-0 list exactly, then commits it as `chore(sync): run-state through Gate 2 [SYNC_2026-09-26_test-c-recovery]` before the doc dance.

## Commit plan (Phase 4; none now)
0. run-state commit (above) · 1. `docs(ARCHITECT_QUESTIONNAIRE): v2.3 - TEST C synthetic recovery validation note [IN-2026-09-26-01]` → CONTENT_SHA · 2. `chore(sync): run metadata [SYNC_2026-09-26_test-c-recovery]`. No Co-Authored-By. No push before Gate 4.

## Route — TINY
A1–A10 all hold (1 ID, 1 doc, no new doc, no rename, no dependency, no high-risk rule, no conflict, no cross-boundary, search complete, waiver eligible). Unchanged from provisional.

Waiver line for approval: "Docs-only QA waiver per SOFTWARE_FACTORY_PLAYBOOK §2.5 item 6 — Operator, <date/time of approval>."

## Skill refinements observed
R1 EOL-unsafe fidelity command (M-1) · R2 P4.1 clean-tree rule vs uncommitted run-state (M-2) · R3 RECOVERY.md stale at BASE.

**Awaiting your APPROVED on the UPDATE MAP** (BASE_SHA, the three ENGINEER-PROPOSED spans plus the CHANGELOG row text, version 2.3, plain-paragraph formatting, parked drift, M-1/M-2 methods, route TINY, waiver line).
