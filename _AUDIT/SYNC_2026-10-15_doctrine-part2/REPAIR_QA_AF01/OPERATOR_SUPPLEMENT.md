# Operator supplement — QA-AF01-R1 serialization repair

Tony retains ALL Git mutations. This supplements the preserved `QA_AMENDED_V1/OPERATOR_INSTRUCTIONS.md`; no command here is an approval or implementation release. Cody is Engineer; Fable is QA Lead.

1. Send the one repair ZIP for independent QA retest. Review `REPAIR_IDENTITIES.json` and `INDEPENDENT_RETEST_HANDOFF.md`. The proposed executable replacement is `REPAIR_QA_AF01/EXECUTION_PROPOSAL.corrected.patch`; do not replace the submitted original on disk. The frozen historical comparison patch is not the amended execution route.
2. After independent retest, QA Lead prepares the matching specification identity update. Record exact successor decisions in order: Gate 2 amendment/transport identity, then Gate 3 QA specification. Record actual retest evidence; do not reuse approval by implication. Existing original map remains frozen.
3. Preserve this repair, receipt/response and later actual QA/decision records together with the existing preparation. `COMPLETE_PRESERVATION_PATHS.txt` and its NUL companion in this repair directory extend the prior 817-path list. Inspect the lists and staged set first; later QA/approval files must be added explicitly before the final preservation commit. Do not use the older incomplete list alone.

Tony's scoped staging command, only after reviewing the path list:

```sh
cd /home/moose/Documents/app-factory-docs-v1
git status --short
git diff --cached --name-status
git add --pathspec-from-file=_AUDIT/SYNC_2026-10-15_doctrine-part2/REPAIR_QA_AF01/COMPLETE_PRESERVATION_PATHS.nul --pathspec-file-nul
git diff --cached --name-status
git diff --cached --stat
```

Then follow the preserved operator instructions for the actual preservation commit, remote baseline, isolated execution worktree and checkpoint. Preserve the exact approved run and successor spec/patch; transfer no review-branch canonical/root/old-skill files. Do not merge the review branch into main. Return observed full SHAs, never placeholders as completed receipts.

4. At a later explicit implementation release, the approved amended index and 380 edits remain the content authority. Use the corrected serialized patch with the declared landing-date binding procedure and separately generated bound indexes. Future serialized bound patches must use standard no-final-newline markers and repeat exact replay-to-index verification. No future bound patch or landing date has been produced by this repair.
5. No operator Git action is needed to perform the independent repair retest in disposable copies. Canonical installation, actual independent candidate QA, cleanup, closeout, publication and merge remain later phases.
