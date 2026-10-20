# FACTORY QA FINAL HANDOFF — read in this order

1. `QA_RETEST_AF01/FINAL_HANDOFF.md` — verdict, identities, ordered decision block, preservation pointer.
2. `QA_RETEST_AF01/QA_AF01_RETEST_VERDICT.md` + `RETEST_VERIFICATION.json` / `RETEST_COMMANDS.json` / `REPLAY_101_HASHES.json` / `ARCHIVE_BLOBS.json` / `LINT_RAW.txt` — independent evidence (script `qa_retest_af01.py`).
3. `QA_RETEST_AF01/DOCSET_SYNC_ACCEPTANCE_SPEC_AMENDED_V1_R1.md` + `SPEC_REVISION_R1.diff` — the matching specification and its delta from AMENDED-v1.
4. `QA_RETEST_AF01/DIRECTOR_DECISIONS.md` — Tony's ordered form. `OPERATOR_INSTRUCTIONS_FINAL.md` + `COMPLETE_PRESERVATION_PATHS.txt/.nul` — setup.
5. `CONTEXT/` — byte-exact copies of the corrected patch, repair identities, amendment records, previous specifications and the 16:06 confirmation (unchanged; verify with `sha256sum -c SHA256SUMS.txt`).

Status: QA-AF01 CLOSED (PASS); Gate 2 amendment PENDING; Gate 3 PENDING; Phase 3 NOT RELEASED. Fable, QA Lead, 2026-10-17T19:07:09+06:00. Cody is Engineer. Tony retains all Git operations.
