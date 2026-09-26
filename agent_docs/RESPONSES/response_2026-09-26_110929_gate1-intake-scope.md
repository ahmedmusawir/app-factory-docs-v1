# GATE 1 — Scope & Classification — SYNC_2026-09-26_test-c-recovery

> TEST C (recovery / resume validation of factory-docs-update v0.7-DRAFT). Engineer seat (Claudy). Written 2026-09-26 11:09 BST, before on-screen display.

## Discovery (evidence-labeled)

| Item | Value | Label |
|---|---|---|
| Seat | Engineer (Claudy) — launch line names "Engineer seat" | EVIDENCE: launch line |
| Location | `/c/Users/user/GITHUB-REPOS/app-factory-docs-v1-testc`, remote `origin` = `ahmedmusawir/app-factory-docs-v1` → Hub clone | EVIDENCE: `pwd`, `git remote -v` |
| Branch | `test/docset-sync-v07-recovery-001` (no upstream; not on remote) | EVIDENCE: `git rev-parse --abbrev-ref HEAD`, `git ls-remote --heads` empty |
| HEAD | `dd6d496a3b269a6bf83ce4e85101d8e0e6e785b9` = required starting SHA | EVIDENCE: `git rev-parse HEAD` |
| Tree | clean at start | EVIDENCE: `git status --porcelain` empty |
| Distance from main | `origin/main` = `0a787cb`; HEAD is 3 ahead / 0 behind (the three skill commits fda59a8, a311924, dd6d496) | EVIDENCE: `git rev-list --left-right --count origin/main...HEAD` = `0 3` |
| Proposed BASE_SHA | `dd6d496a3b269a6bf83ce4e85101d8e0e6e785b9` — named by the launch line and equal to the clean discovered HEAD | EVIDENCE |
| RESUME detection | none: no `docs/sync-*` branch, no `_AUDIT/SYNC_*/`, `_INBOX/` absent at start, no "RESUME" in launch | EVIDENCE: `git branch -a`, `ls _AUDIT` |
| RECOVERY.md | stale — describes 2026-08-10 close-out; predates the three skill commits. Treated as state, not evidence | EVIDENCE: RECOVERY.md:3–8 vs `git log` |
| Session file | `session_2026-09-26.md` absent → created (run-state write) | EVIDENCE |
| Live docs | 31 on disk (`ls 0?_*/*.md`); MANIFEST tables 31 rows; MANIFEST states **29** (MANIFEST.md:6, :12, :76) and "27 bodies" (:114) | EVIDENCE |
| Baseline drift | `DRIFT-2026-09-26-01` — MANIFEST stated count 29 vs 31 on disk / 31 rows; appendix "27 bodies". Pre-existing at BASE; not authorized by intake → PARKED | EVIDENCE |
| Lint baseline | 9 findings, exit 1: VERSIONED-REFS ×8 (STARTER_KIT_HANDBOOK:258, 261, 688, 690, 692; DATABASE_MANUAL:8, 156; UI_UX_BUILDING_MANUAL:2092) + HEADER-PRESENCE ×1 (STARTER_KIT_HANDBOOK:1); ENCODING PASS, RETIRED-TERMS PASS over 33 live files | EVIDENCE: `py lints/run_all.py` |
| GitHub MCP | present (exception route only; not needed — clone exists) | EVIDENCE |
| Anti-patterns most relevant | AP-18 (absorbing baseline drift into an unrelated run) and AP-3 (floating files — this test deliberately leaves uncommitted run-state for a fresh session) | INFERENCE from job shape |

## Cargo scan

`_INBOX/` did not exist at BASE. Per the Operator's TEST C instruction, Claudy created ONE synthetic cargo unit: `_INBOX/TEST_C_RECOVERY_CARGO.md`. No legacy root cargo (`DOCTRINE_PROMOTION*`, `*PATCH*`, `LESSONS*`) found at the repo root.

## Intake ledger (draft §A)

| ID | Class | Source | Gist | Disposition (proposed) |
|---|---|---|---|---|
| IN-2026-09-26-01 | 2 — DOCTRINE JOURNAL / LESSON | `_INBOX/TEST_C_RECOVERY_CARGO.md` Entry 1 | Add the exact line "TEST-C-SYNTHETIC-01 — Recovery/resume validation only." to ARCHITECT_QUESTIONNAIRE `## Version History`, directly below the table | CHANGE |

**Classification evidence (content-first, D16):** status FLAGGED; one entry with a named target doc, a stated placement, exact required wording, and preservation lines = class 2 recognition. Semantic form: an edit-level lesson entry. Provenance/authority: synthetic, authored at the Operator's instruction for TEST C. Hub counterpart by canonical name: `02_PIPELINE_AGENTS/ARCHITECT_QUESTIONNAIRE.md` (header v2.2, 2026-07-07). The filename carries no "LESSONS"/"PATCH" marker — classification rests on contents alone.

**Placement pre-check (D13):** `## Version History` exists at ARCHITECT_QUESTIONNAIRE.md:170; table L172–176; blank L177; `---` L178. Placement exists as stated. Verified fully in Phase 2.

## Parked / gaps / conflicts / clarifications

- Cross-boundary (XB): none.
- Gaps (GAP): none.
- Baseline drift: `DRIFT-2026-09-26-01` (above) — PARKED, not on the touch list, does not affect route.
- CONFLICT: none.
- CLARIFICATION (smallest question; does not block Phase 4): **merge target.** The run branch would be the existing `test/docset-sync-v07-recovery-001` (already at BASE_SHA — D18 reuse). It carries 3 skill commits ahead of `origin/main` that are not part of this run, so a PR to `main` would carry them. Proposed default: merge target "none — disposable TEST C branch; Phase 8 not in this test's scope." Confirm or name a target.

## Provisional route — TINY

| Condition | Evidence now | Status |
|---|---|---|
| A1 ≤3 IDs | 1 ID | holds |
| A2 ≤3 docs | 1 likely doc (named TARGET) | provisional — confirmed after the Phase 2 search |
| A3 no new canonical doc | none | holds |
| A4 no Factory-wide rename | none | holds |
| A5 no cross-correction dependency | single ID | holds |
| A6 no high-risk rule change | synthetic note in a history section; no rule changes | holds |
| A7 no unresolved conflict | none | provisional |
| A8 no blocking cross-boundary | none | holds |
| A9 search bounded + complete | not yet run | provisional (Phase 2) |
| A10 docs-only waiver eligible | markdown + MANIFEST/CHANGELOG/_ARCHIVE only | provisional |

Provisionally TINY because every decidable condition holds; the touch-list count, conflicts, search completeness, and waiver eligibility are confirmed after the Phase 2 propagation search.

## Next

On APPROVED: create `_AUDIT/SYNC_2026-09-26_test-c-recovery/UPDATE_MAP.md` (DRAFT, run-state write), run the propagation search, verify placement, draft §C wording (Version History row text marked ENGINEER-PROPOSED), and stop at Gate 2.

**Awaiting your APPROVED on scope and classification.**
