# QA-AF01-R1 — independent retest handoff

From Cody, Engineer, to the independent QA seat assigned by Tony / QA Lead Fable. **No acceptance is issued here.** Tony authorizes this repair and reports Jarvis independently reproduced QA-AF01 and confirmed the eight ownership corrections.

## Fixed inputs

- BASE: `9c179392f79b70da099121fc357d3107ad3bb86e`.
- Corrected patch: `REPAIR_QA_AF01/EXECUTION_PROPOSAL.corrected.patch`, SHA-256 `cf6413c9340c80f5c1bf53a55385876470e9b3aad364bc8963f52a68580f2a6d`.
- Expected outputs: unchanged `AMENDED_V1/EXECUTION_PROPOSAL_INDEX.json`, SHA-256 `69244f4edc347b30b81ed6a909bae4fbb5130864319e9f8cd84b5d5c22e59ba6`; 101 paths.
- Ordered edits: unchanged `AMENDED_V1/SELECTED_EXACT_EDITS.json`, 380 entries, SHA-256 `2675ffc148f49a95b688e9f252527950ce9c3f1fd61df3fb0ffb067fcc7ff687`.
- Source copies in this ZIP are under `CONTEXT/`; originals remain in the existing run. Corrected patch applies from the root of a disposable BASE tree with `-p0`.

## Independent acceptance work requested

1. Verify ZIP inventory and exact input identities. Inspect `SERIALIZATION_REPAIR.diff`: only two standard missing-newline boundary sequences, no intended target changes. Confirm old/new marker mechanics directly; do not rely on a successful patch exit.
2. Export two **fresh disposable BASE copies** using read-only Git blobs, without branch/worktree/index mutations. Run `git apply --check -p0 <absolute-corrected-patch>` on one. Run `patch --batch --fuzz=0 -p0 -i <absolute-corrected-patch>` on the other. Record full command, cwd, exit and unfiltered safe output. Check 0 exits and no rejected/fuzzy hunks.
3. Independently compare every one of the 101 resulting files to the unchanged amended index, including byte size. Compare exact changed/added file set against 33 modifications/68 additions; catch stray patch rejects/backups/cache files. The Engineer's self-check helper is supplied for reproducibility, not as an independent oracle.
4. For `_ARCHIVE/FRONTEND_BUILD_PHASE_PLAYBOOK_v1_2_2.md`, compare with BASE:`03_BUILD_METHODOLOGY/FRONTEND_BUILD_PHASE_PLAYBOOK.md`; expected Git blob `3edb88c3149a9a6d9a7c760471f30956053c9d60`, 23,578 bytes. For `_ARCHIVE/FRONTEND_FIRST_PLAYBOOK_v1_1_3.md`, compare with BASE:`03_BUILD_METHODOLOGY/FRONTEND_FIRST_PLAYBOOK.md`; expected blob `c8516c8b8b3950e4b2d08d0bb2c112d7136d8f30`, 15,043 bytes. Both **lack final LF**. Use `git rev-parse BASE:<source>` and read-only `git hash-object --no-filters <replayed-archive>`, without `-w`, plus byte/EOF comparison.
5. Run the pinned unchanged lint suite on the replayed tree: `PYTHONDONTWRITEBYTECODE=1 python3 -B -I lints/run_all.py`. Verify zero lint changes. Check map/spec/source/template/diagram identities remain unchanged; no settled template acceptance is reopened.
6. Review other-patch audit: amended selected-content diff and conditional closeout patch are unchanged and pass their replay/checks. Frozen original execution has the same historical defect; its separate corrected fixture is for comparison only. Do not substitute its 372-edit content for the current amended 380-edit route.
7. Record the independent retest verdict with exact corrected patch/index identity. Route failure if any output differs. Only the independent QA Lead can accept that result; Cody's PASS does not close QA-AF01.

## Remaining gates and boundaries

QA Lead updates affected specification identities/status references separately; exact locations are listed in `QA_LEAD_REFERENCE_UPDATES.md`. No AC content change is proposed by this serialization repair. Preserve all old submitted bytes and identify any successor spec explicitly. Tony decides Gate 2 amendment/successor executable identity, then Gate 3 matching spec. Both remain pending. Operator preservation, actual remote-baseline/worktree receipts and explicit Phase 3 release still follow; no canonical implementation has occurred.

Original exclusions, D-3 readability follow-up, D-4 existing-byte record, 12 conditional closeout spans and actual date/evidence gates remain unchanged. No new content amendment, release tag, skill rewrite or policy approval is requested.
