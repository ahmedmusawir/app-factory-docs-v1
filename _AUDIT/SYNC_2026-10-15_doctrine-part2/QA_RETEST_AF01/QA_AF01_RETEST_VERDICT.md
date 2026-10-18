# QA-AF01 — independent retest verdict: **PASS — CLOSED**

Fable, QA Lead · 2026-10-17T19:07:09+06:00 · repository `/home/moose/Documents/app-factory-docs-v1`, run `_AUDIT/SYNC_2026-10-15_doctrine-part2/`.

**Verdict vocabulary:** PASS. QA-AF01 (patch serialization corrupting two archive outputs; High) is closed on my own passing evidence against the unchanged 101-path amended index. The Engineer's PASS and Jarvis's reported confirmation were not used as oracles.

## Independence statement

This session held the Engineer seat earlier today (AMENDED-v1 content, 13:50/14:58). The 16:06 QA review and the 17:36 repair were produced by other sessions. Every check below was re-run here from read-only Git blobs (`git archive 9c17939` into disposable scratch copies), the unchanged amended index and the pinned lint scripts. Script: `QA_RETEST_AF01/qa_retest_af01.py`; full command/cwd/exit/stdout/stderr: `RETEST_COMMANDS.json`; results: `RETEST_VERIFICATION.json`, `RETEST_RAW.txt`.

## Evidence

| # | Check | Result |
|---|---|---|
| 1 | Repair ZIP `9782260c…` | CRC clean; 45/45 inventory hashes; every payload byte-equal to its run-directory counterpart |
| 2 | Input identities | corrected patch `cf6413c9…` 1,906,921 B; submitted `ce4528d8…` 1,906,863 B; index `69244f4e…`; edits `2675ffc1…` |
| 3 | Serialization delta | exactly two `\ No newline at end of file` sequences at patch lines 29748 and 30199, each after the archive footer line and before the next `--- /dev/null`; removing them reproduces the submitted patch byte-for-byte (58 B) |
| 4 | `git apply --check -p0` (fresh BASE copy, no .git) | exit 0, empty stderr. Control on the submitted patch: exit 128, "patch fragment without header at line 29750" (QA-AF01 reproduced) |
| 5 | `patch --batch --fuzz=0 -p0` (second fresh BASE copy) | exit 0; 101 files patched; no rejects, fuzz or offsets; no `.rej`/`.orig`/cache files |
| 6 | 101 outputs vs amended index | 101/101 SHA-256 and byte sizes exact; changed set exactly 33 modified + 68 added; 33 before-hashes equal pinned blobs |
| 7 | Archive fidelity | `FRONTEND_BUILD_PHASE_PLAYBOOK_v1_2_2.md` blob `3edb88c3…` 23,578 B and `FRONTEND_FIRST_PLAYBOOK_v1_1_3.md` blob `c8516c8b…` 15,043 B equal BASE sources (`git hash-object --no-filters`, no `-w`); final LF absent in both; all 31 outgoing archives equal their BASE sources |
| 8 | Pinned lint suite on the replayed tree | `python3 -B -I lints/run_all.py` exit 0, RESULT: PASS; lint scripts byte-identical; no bytecode written |
| 9 | Other patch artifacts | conditional closeout patch `git apply --check -p0` on the replayed tree exit 0 and its 12 spans replay to the post-verification index; amended selected-content diff `git apply --check -p1` on BASE exit 0 |
| 10 | Carry-forward (ownership amendment) | 380 ordered edits replay from pinned blobs to the amended content index (31 docs); the three amended documents in the replayed tree equal `AMENDED_V1/PROPOSED_CONTENT/` with the standard header-bump + history-row residual |
| 11 | Identities unchanged | map `cd291270…`, spec v1.0 `3910a62c…`, spec AMENDED-v1 `103c7ede…`, AMENDMENT_V1.md `655e24ed…`, 23 AMENDED_V1 records, PRESERVATION_BASELINE, 101 frozen PROPOSED_CONTENT hashes |
| 12 | Git | HEAD 626da8d, main = origin/main = 9c17939 before and after; nothing staged; canonical diff vs BASE empty; no branch, worktree or index mutation |

## Disposition

- QA-AF01: **CLOSED (PASS)**. Executable representation = `REPAIR_QA_AF01/EXECUTION_PROPOSAL.corrected.patch`, SHA-256 `cf6413c9340c80f5c1bf53a55385876470e9b3aad364bc8963f52a68580f2a6d`. The submitted `AMENDED_V1/EXECUTION_PROPOSAL.patch` is preserved as history only.
- Frozen original execution patch: same defect, historical; its corrected fixture is comparison only and is not the execution route (380-edit amended route stands).
- No content amendment, template acceptance, intake restart or policy change occurred or is requested.
- Ownership corrections D-1, D-2, OBS-1, P-1…P-4: carried forward as CONFIRMED (16:06 source-based review, Jarvis confirmation via Tony, my carry-forward replay above).

Gate 2 amendment and Gate 3 remain Tony's decisions, in that order. Phase 3 NOT RELEASED.
