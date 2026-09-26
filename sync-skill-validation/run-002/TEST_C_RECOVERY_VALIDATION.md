# TEST C — Recovery / Resume Validation

> **Date:** 2026-09-26 · **Seat:** Claudy (Engineer) · **Status:** COMPLETE

## Run identity

| Field | Value |
|---|---|
| Candidate skill version | `factory-docs-update` v0.7-DRAFT |
| Branch | `test/docset-sync-v07-recovery-001` (disposable) |
| BASE_SHA | `dd6d496a3b269a6bf83ce4e85101d8e0e6e785b9` |
| Run ID | `SYNC_2026-09-26_test-c-recovery` |
| Route | TINY · merge target NONE · docs-only QA waiver |
| Stop point | After Gate 2 approval (2026-09-26 12:13 BST), before Phase 4 |

## TEST C1 — Graceful Resume

- **Result:** PASS [CLAIM: Operator]
- A fresh Engineer session rebuilt the run from the usual recovery and run-state files (RECOVERY.md, the session file, the UPDATE MAP).
- It correctly named Phase 4 as the next legal phase.

## TEST C2 — Hard-Crash Resume

- **Result:** PASS
- RECOVERY.md, `session_*.md`, `agent_docs/RESPONSES/**` and conversational memory were deliberately ignored.
- The run was recovered from git, disk, `_AUDIT/`, the approved UPDATE MAP and `_INBOX/` alone:
  - HEAD equals BASE_SHA. `git log dd6d496..HEAD` is empty, so there are no run commits.
  - The map status reads APPROVED and FROZEN. Gate 1 was approved at ~11:31 BST and Gate 2 at 12:13 BST.
  - The target doc, MANIFEST.md, CHANGELOG.md and `_ARCHIVE/` are identical to BASE. The target file's hash is `15780306…`, the same as the BASE version. The expected archive file is absent.
- It correctly named Phase 4 as the next legal phase, starting at map §N step 0.
- **No unexplained dirty files:** the 7 dirty paths (1 modified, 6 untracked) match the run-state list in map §N step 0 exactly.
- Caveat: those files were confirmed to exist, but their contents were not read (the test barred it). Their contents should be checked against the map before the step-0 run-state commit.

## Skill findings observed

| ID | Finding |
|---|---|
| R1 | The P4.2.5 archive-fidelity command (`git show <BASE>:<path> \| diff -`) reports false differences on `core.autocrlf=true` / CRLF worktrees. The map's M-1 blob-hash method (`git hash-object` against the BASE blob) is CRLF-safe. |
| R2 | The P4.1 clean-tree rule does not say how to handle legitimate uncommitted state left by an interrupted run. The map's M-2 handling (the dirty set must match the listed run-state paths exactly, then those paths are committed as run-state) filled the gap. |
| R3 | RECOVERY.md can be stale: at BASE it described 2026-08-10 and predated three skill commits. It must stay advisory, not authoritative. |
| — | Hard-crash recovery shows that git and disk, plus the approved durable files (UPDATE MAP, `_INBOX/`), must be enough without any recovery prose. D15a should treat the recovery files as optional hints, not a required first read. |

## Final verdict

**TEST C PASS**

## Recommendation

Carry the accepted findings (R1–R3 and the hard-crash sufficiency point) into the final bounded hardening pass of `factory-docs-sync-process-001` before merge.
