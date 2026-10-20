# Phase 4 QA readiness — installed doc-sync candidate

**Seat:** Fable (QA Lead) · **Recorded:** 2026-10-19T10:56:22+06:00 · **Run:** `_AUDIT/SYNC_2026-10-15_doctrine-part2/` (RUN)
**Purpose:** establish that the candidate and its records satisfy the specification's §1 preconditions so an independent QA Executor can run the full 38-AC assignment in one pass. **This is readiness, not the product verdict.** The verdict is issued by Fable only after the Executor's evidence package is adjudicated.

## 1. Identities (verified read-only this session)

| Object | Identity | Verified how |
|---|---|---|
| Handoff ZIP | `/home/moose/Downloads/FACTORY_PHASE3_ENGINEERING_HANDOFF_2026-10-18_212938.zip` · SHA-256 `d12d0ff80c90090b16800bbd8b7c315dd2ebc4712d2dabf6cb67e75ad7c577ea` · 17,210,480 B | sha256sum; CRC clean; 786/786 inventory hashes; 782 payload members byte-equal to `git show 20f71ee:<path>` |
| Remote tip = QA_START_SHA (remote-read) | `20f71ee932ed21c0878cb3a0f39c6fbe90d0a793` on `refs/heads/docs/sync-doctrine-part2-2026-10-15` | `git ls-remote --heads origin` from the execution worktree (no fetch) |
| Implementation commit CONTENT_SHA | `ef35d26d82f1904da6ed33663ad647e4ee16fe98` · committed 2026-10-18 21:28:07 +0600 | ancestor of tip; BASE ancestor of it |
| BASE_SHA | `9c179392f79b70da099121fc357d3107ad3bb86e` | `git ls-remote origin refs/heads/main` still equals BASE |
| Chain BASE..tip | `356206a` checkpoint → `4ec73a4` 10x (2 files) → `2e714b6` setup record → `ef35d26` implementation → `20f71ee` handoff | `git log --format='%H %P'`; 5 commits, author Ahmed Musawir |
| Execution worktree | `/home/moose/Documents/app-factory-docs-sync-execution` @ `20f71ee`, clean before and after lint | `git worktree list`, `git status --porcelain` |
| Approved spec (Gate 3) | `RUN/QA_RETEST_AF01/DOCSET_SYNC_ACCEPTANCE_SPEC_AMENDED_V1_R1.md` · `2a3867cacef11c6bb0419a4c71229479efe703cee9fbcc1e4f71c0ac8e63f0fc` | hash equal on disk and at `ef35d26` |
| Gate 2 / Gate 3 records | `RUN/QA_RETEST_AF01/DIRECTOR_DECISIONS.md` §1/§2 APPROVED 2026-10-17 19:23:09 +06:00, naming corrected patch `cf6413c9…` and spec `2a3867ca…` | read at candidate |
| Phase 3 release + Git authorization | `RUN/PHASE3_EXECUTION/DIRECTOR_RELEASE.md`; `RUN/EXECUTION_SETUP/GIT_AUTHORIZATION_2026-10-18.md` | read at candidate |
| Setup receipts | `RUN/EXECUTION_SETUP/SETUP_RECEIPT.json`: preservation `e7b4a6f…`, fetched BASE `9c17939…`, checkpoint `356206a…`, setup HEAD `2e714b6…`, content `ef35d26…` | read at candidate |
| Standalone 10x references | `10x Lab/ABM_PLAYBOOK_v1_0.md` `21f8344812a3…` (47,242 B); `10x Lab/APBM_PLAYBOOK_v1_0.md` `c12ff3f9bc43…` (25,765 B) | equal to `/home/moose/Documents/` sources and to `EXECUTION_SETUP/STANDALONE_10X_AUTHORIZATION.json` |

## 2. Precondition checks (spec §1 "Preconditions") — 24/24 PASS

Reproducible: `python3 -B -I qa_readiness.py` in this directory → `QA_READINESS.json` (results) and `QA_READINESS_RAW.json` (24 commands with cwd/exit/output). Summary:

| # | Check | Result |
|---|---|---|
| 1–4 | ZIP SHA, CRC, 786 inventory hashes, payload == committed tip | PASS |
| 5–8 | remote tip == expected HEAD; origin/main == BASE; worktree HEAD == tip on the named branch; porcelain empty | PASS |
| 9–10 | CONTENT_SHA ancestor of tip and BASE ancestor of CONTENT_SHA; implementation commit date == 2026-10-18 | PASS |
| 11–15 | spec R1 SHA at candidate; Gate 2/3 APPROVED naming patch+spec; release + agent Git authorization recorded; setup receipt identities; SYNC_HANDOFF §0 names CONTENT_SHA | PASS |
| 16–17 | AC1 set over BASE..tip: 101 sync (33 M / 68 A) + 2 `10x Lab/` + 664 `RUN/**` + 8 bookkeeping = 775, nothing else; `lints`, `.github`, `_SKILLS`, root `CLAUDE.md`/`AGENTS.md`, `factory-corrections`, `factory-intake`, `_INBOX` unchanged | PASS |
| 18–19 | `BOUND_EXECUTION_INDEX.json`: 101/101 committed hashes and byte counts at `ef35d26`; review hashes equal the amended index; 101 paths unchanged between `ef35d26` and tip | PASS |
| 20 | 12 conditional transitions on 9 paths still at pre-transition wording (`BOUND_STATUS_TRANSITIONS.json` old spans present at declared occurrences; new absent) | PASS |
| 21 | `INTAKE_SNAPSHOT/` 189/189 files equal `INTAKE_SNAPSHOT_INDEX.json` (paths relative to the snapshot dir); no modifying commit BASE..tip | PASS |
| 22–23 | two 10x files exact copies; `_ARCHIVE/QA_PLAYBOOK_v1_0.md` blob `bb41260f6b6f94372a682f04b313a451f2b3c4b1` | PASS |
| 24 | pinned lint suite at the worktree: exit 0, `=== RESULT: PASS ===`, 36 live docs, 0 hits × 4 lints; worktree clean afterwards | PASS |

The remaining §1 precondition, "the QA Executor was launched in a fresh session by Tony", is satisfied when Tony launches `QA_EXECUTOR_PROMPT.md`.

## 3. Observations carried into the assignment (not failures)

- **R-1 Spec self-reference.** The frozen R1 text still says "this file at `QA_AMENDED_V1/DOCSET_SYNC_ACCEPTANCE_SPEC_AMENDED_V1.md`". `DIRECTOR_DECISIONS.md` §2 already rules that the R1 path/hash is the authoritative selection. Executor uses R1.
- **R-2 `STANDING_INVARIANTS.md`** (spec §0 "Derived from") is not at RUN root; it resolves at `RUN/GOVERNING_SKILL_MAIN/_SKILLS/factory-docs-update/_shared/references/STANDING_INVARIANTS.md` (and `_SKILLS/...` at BASE, unchanged).
- **R-3 AC3 "filled" disposition table.** No separately named filled file exists at the candidate. `SYNC_HANDOFF_DISPOSITIONS.template.md` carries the full 97-row ledger copy, and `SELECTED_SCOPE_LEDGER.md` carries 97 FC rows. Executor grades set identity across ledger, template and `UPDATE_MAP.md` §A and reports whether a distinct filled handoff table is required; Fable adjudicates.
- **R-4 Bound index shape.** Every `BOUND_EXECUTION_INDEX.json` entry carries `landing_date: "2026-10-18"`; field-level binding authority remains the 151 spans in `AMENDED_V1/LANDING_DATE_PLAN.json` (AC30).
- **R-5 ENGINEER_PLAYBOOK fence parity.** Nested template fences invert markdown_it fence parity from §12 on (pre-existing at BASE; fence count 82 unchanged). Container checks there use line structure, not markdown_it (recorded at AMENDED-v1 verification).
- **R-6 Bookkeeping paths in the candidate (8).** `RECOVERY.md` (M) and seven files under `agent_docs/SESSIONS/`, `agent_docs/RESPONSES/` (A). Allowed by AC1's named housekeeping set.
- **R-7 Git actor.** All five commits are authored "Ahmed Musawir" and were executed under Tony's 2026-10-18 agent-Git authorization. AC32's historical Tony-only wording is superseded (see `OVERRIDES_AND_ALIGNMENT.md` O-1).

## 4. Readiness decision

**READY.** Preconditions hold; the candidate is at its deliberate pre-closeout stage; the assignment in `AC_EXECUTION_CHECKLIST.md` and the prompt in `QA_EXECUTOR_PROMPT.md` are issued. No Git mutation, no implementation edit, no candidate-tree write occurred during readiness.
