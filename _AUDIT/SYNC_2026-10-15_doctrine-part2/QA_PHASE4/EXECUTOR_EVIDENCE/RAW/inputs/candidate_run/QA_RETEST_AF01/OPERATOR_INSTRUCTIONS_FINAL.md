# Operator instructions — final Phase 2 handoff (2026-10-17T19:07:09+06:00)

Tony performs every Git mutation. These supersede the sequencing in `QA_AMENDED_V1/OPERATOR_INSTRUCTIONS.md` and `REPAIR_QA_AF01/OPERATOR_SUPPLEMENT.md` (both preserved). Nothing here is an approval or a Phase 3 release.

## 1. Decide, in order (`QA_RETEST_AF01/DIRECTOR_DECISIONS.md`)

1. Gate 2: approve AMENDED-v1 naming the amended index `69244f4e…`, the 380 edits and the **corrected patch `cf6413c9…`** as the executable representation. QA-AF01 is closed; no blocker remains on the amendment.
2. Gate 3: approve the matching specification `QA_RETEST_AF01/DOCSET_SYNC_ACCEPTANCE_SPEC_AMENDED_V1_R1.md`, SHA-256 `2a3867cacef11c6bb0419a4c71229479efe703cee9fbcc1e4f71c0ac8e63f0fc`, only after Gate 2.

## 2. Preserve the exact reviewed state

Use `QA_RETEST_AF01/COMPLETE_PRESERVATION_PATHS.txt` (865 paths) and its NUL companion. It extends the 846-path repair list with this handoff's files, receipt and response. Inspect the list, the working tree and the staged set first; the list grants no permission to stage unrelated work. `_INBOX/`, caches and Downloads ZIPs are excluded. Root `session_*.md` entries in the list record the already-performed relocation to `agent_docs/SESSIONS/`.

```sh
cd /home/moose/Documents/app-factory-docs-v1
git status --short
git diff --cached --name-status
git add --pathspec-from-file=_AUDIT/SYNC_2026-10-15_doctrine-part2/QA_RETEST_AF01/COMPLETE_PRESERVATION_PATHS.nul --pathspec-file-nul
git diff --cached --name-status
git diff --cached --stat
git commit -m "chore(sync): preserve amended map, QA-AF01 retest and matching specification R1"
git rev-parse HEAD
```

Record the observed SHA in `DIRECTOR_DECISIONS.md` §3. Any later decision records go in a later named commit.

## 3. Verify the remote baseline, then create the isolated execution worktree

```sh
git fetch origin
git rev-parse main origin/main
git worktree list --porcelain
git branch --list docs/sync-doctrine-part2-2026-10-15
```

Expected BASE `9c179392f79b70da099121fc357d3107ad3bb86e`. If `origin/main` differs, stop and return the actual SHA; before-hashes must be reconciled by an attributable amendment. Then follow the preserved `OPERATOR_NEXT_STEPS.md` §3 for the worktree and checkpoint, and record the SHAs.

## 4. Phase 3 (only after an explicit release)

Content authority: the amended index and 380 edits. Executable representation: the corrected patch, applied with `-p0` from the worktree root, followed by the declared landing-date binding and separately generated bound indexes. Future serialized bound patches must use standard no-final-newline markers and repeat exact replay-to-index verification. No bound patch or landing date exists yet. Do not apply the submitted `AMENDED_V1/EXECUTION_PROPOSAL.patch`.
