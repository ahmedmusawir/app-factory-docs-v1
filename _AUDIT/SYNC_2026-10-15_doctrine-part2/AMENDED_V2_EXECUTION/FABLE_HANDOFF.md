# Fable — independent bounded retest R1–R12

Engineering is complete and pushed. Launch a fresh QA Executor against `8dff354937bc7baf739370a9886497d9d5359186` on `docs/sync-doctrine-part2-2026-10-15`, pinned by `PUSH_RECEIPT.json`. Fable owns adjudication and successor verdict. This package is engineering evidence, not independent acceptance.

## Governing identities

- Start candidate/parent: `20f71ee932ed21c0878cb3a0f39c6fbe90d0a793`.
- Repaired candidate: `8dff354937bc7baf739370a9886497d9d5359186` (one child commit; exact subject in COMMIT_RECEIPT).
- Gate 2 approval: `QA_PHASE4/REPAIR_QA_P4/DIRECTOR_DECISIONS_V2.md` (committed before push; approval recorded before application).
- Successor index: `AMENDED_V2/BOUND_EXECUTION_INDEX.json`, SHA-256 `b4fe406963b13b650f11d7d688026c88ff37fb1698d6191cdec420247c156bc9`.
- Patch: `AMENDED_V2/EXECUTION_PROPOSAL.patch`, SHA-256 `86fbfe6f3787c55332bb5d0c741d7ed3296c1f872e3ce26bc4af01b29a0282fd`.
- Frozen spec: `QA_RETEST_AF01/DOCSET_SYNC_ACCEPTANCE_SPEC_AMENDED_V1_R1.md`, SHA-256 `2a3867cacef11c6bb0419a4c71229479efe703cee9fbcc1e4f71c0ac8e63f0fc`.

All relative run paths are below `_AUDIT/SYNC_2026-10-15_doctrine-part2/`. The original root BOUND_EXECUTION_INDEX remains historical; use the AMENDED_V2 successor for this retest. The sealed proposal’s PENDING labels remain unchanged as provenance; the additive Director decision now governs those exact identities. FU-1/FU-2 excluded.

## Retest scope

| Check | Required independent verification |
|---|---|
| R1 | AC5/6 ownership searches, both runs Architect-authored, eight AMENDED-v1 spans unchanged. |
| R2 | AC9 QA-branch routing, certification/release ordering, ACCEPTANCE_SPEC + QAM in eight-entry tree; Operations Needs and Verbal Brief unchanged. |
| R3 | AC15 zero active filesystem-wins/disk-wins hits, including fences; RUL-12 drift/requirements routing. |
| R4 | AC16 FC-022/038/066 containment; other 28 withdrawal rows preserved. Underlying implementation closure is not implied. |
| R5 | AC18 browser-contact-storage default in all four manuals; no new persistence recipe. |
| R6 | AC2 all 101 successor hashes; seven changed and **94 unchanged** against parent. |
| R7 | AC25–27 unchanged headers/MANIFEST; 39 run CHANGELOG rows with six amended; one amended existing run-history row per document. |
| R8 | AC29/31 unchanged lint suite passes with zero hits; lints/.github unchanged. |
| R9 | AC22–24/37 archives/templates/workflows/assets and protected files byte-identical. |
| R10 | AC33 all 12 closeout transitions on nine paths remain pending. |
| R11 | AC32 one repair commit after attributable Tony Gate 2; proper parent/subject; pushed working branch; clean tree; no main/merge/force push. |
| R12 | AC1 exactly seven canonical paths (six docs plus CHANGELOG), plus 61 additive run records; inspect full 68-path commit against STAGED_SCOPE. |

R6/R12 reflect Tony’s explicit prompt-accounting correction; the frozen spec is unchanged. The original 101-path set is not expanded by audit records.

## Evidence and limitations

`VERIFICATION.json` and `COMMANDS.json` are actual installed-worktree engineering checks; `INSTALLED_101_HASHES.json` records every successor hash. `COMMIT_RECEIPT.json` and `PUSH_RECEIPT.json` prove the final commit, remote SHA and clean tree; 68 committed path hashes were checked against staged bytes. Full existing-path before/after hashes and protected-path hashes are included. PROPAGATION contains 164 dispositioned hits. LINT_OUTPUT records the unchanged suite result.

The full staged whitespace diagnostic found preserved blank context lines in the patch, original source quotations and CRLF TSV evidence. Approved evidence was kept exact; the seven canonical-path whitespace check passed. See STAGING_WHITESPACE_NOTE/DIAGNOSTIC. No approved text was normalized or altered to silence this extra diagnostic.

Post-commit receipts live in the review repo and this handoff, not inside the commit they identify; the committed pre-commit evidence remains exact. No self-referential commit hash was inserted into the execution worktree. Do not run the engineering apply helper without --verify; independent QA should use its own read-only procedures under Fable’s original prompt and this bounded scope.

Keep closeout transitions pending through this retest. No QA verdict, cleanup acceptance, release, deployment or Architect closeout is asserted here.
