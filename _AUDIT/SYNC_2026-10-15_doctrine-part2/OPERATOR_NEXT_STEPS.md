# Operator next steps — corrected Phase 2 map

Tony performs ALL Git mutations. Cody performed read-only inspection and proposal/report writes. Current review branch: factory-docs-review-astra-w-chunks at 626da8d70f4db22987dc7fcc86765492072360cd. Local main/origin-main: 9c179392f79b70da099121fc357d3107ad3bb86e; no fetch by Cody. The review branch and its older skill copy must not be merged into main.

## 1. Preserve the corrected preparation

Inspect before staging. OPERATOR_PRESERVATION_PATHS.txt lists only observed authorized review/intake/run/bookkeeping changes. The matching NUL pathspec list excludes the local _INBOX drop, caches and unrelated work. It preserves existing root AGENTS.md as earlier review-branch work; it does not implement root-instruction corrections or transfer that file into the execution worktree. Stop for an unexplained path.

```sh
cd /home/moose/Documents/app-factory-docs-v1
git status --short
git diff --stat
git diff --cached --stat
git rev-parse HEAD main origin/main
```

After reviewing the named path list and staged diff:

```sh
git add --pathspec-from-file=_AUDIT/SYNC_2026-10-15_doctrine-part2/OPERATOR_PRESERVATION_PATHS.nul --pathspec-file-nul
git diff --cached --name-status
git diff --cached --stat
git commit -m "chore(sync): preserve corrected phase 2 map and review evidence"
git rev-parse HEAD
```

Return the observed full preservation SHA. If Jarvis/Fable or Tony subsequently amend/approve files, preserve those later exact bytes before transfer; do not reuse an older receipt that lacks the approved map/spec. This commit preserves review material; it does not approve the map or implement canonical changes.

## 2. Confirm the remote baseline

```sh
git fetch origin
git rev-parse main origin/main
git worktree list --porcelain
```

If origin/main differs from 9c179392f79b70da099121fc357d3107ad3bb86e, return its actual SHA and reconcile placements/before-hashes before freezing or applying the map. No automatic reset, rebase, merge or replacement base.

## 3. Prepare the isolated execution worktree

After baseline confirmation, check the proposed directory is absent and branch unused. The original worktree and all review work remain intact.

```sh
git worktree add -b docs/sync-doctrine-part2-2026-10-15 /home/moose/Documents/app-factory-docs-sync-execution 9c179392f79b70da099121fc357d3107ad3bb86e
```

Transfer only the durable run from the actual preservation commit that contains the approved map and Fable-finalized/approved spec. Replace the placeholder with the observed full SHA:

```sh
SYNC_PRESERVATION_SHA='REPLACE_WITH_OBSERVED_FULL_SHA'
git -C /home/moose/Documents/app-factory-docs-sync-execution restore --source="$SYNC_PRESERVATION_SHA" -- _AUDIT/SYNC_2026-10-15_doctrine-part2
git -C /home/moose/Documents/app-factory-docs-sync-execution status --short
```

Cody verifies transferred snapshot hashes, approved identities, baseline and exact dirty set. Tony checkpoints only the transferred run on the execution branch before canonical execution, so the approved implementation starts from a clean worktree. Review-branch preservation and the execution-branch checkpoint are separate identities; the latter carries the durable intake into the implementation ancestry. No review-branch canonical tiers, root instructions or _SKILLS are transplanted.

## 4. Gates before Phase 3

Jarvis reviews MC_CORRECTION_DISPOSITIONS and the corrected exact map. Tony approves Gate 2, including 101 paths, 372 edits, the workflow/diagram publications, date binding, exclusions and the conditional closeout plan. Fable re-anchors/finalizes her preserved DRAFT specification; Tony approves Gate 3. Cody verifies setup receipts and the actual release before applying any canonical proposal. Current source-template acceptance is settled and is not repeated.

At authorized implementation, bind only LANDING_DATE_PLAN.json’s named current fields to the actual landing date. Record it in execution evidence and generate separate BOUND_EXECUTION_INDEX.json and BOUND_STATUS_TRANSITIONS.json/pre-post hashes. Preserve the reviewed/frozen map and review-time indexes; do not blanket-replace historical approval dates.

## 5. Later bounded closeout — purpose and evidence, no action now

POST_VERIFICATION_STATUS_TRANSITIONS.json names Tony’s intended closeout commit: activate verified new doctrine/workflow references and installed-template provenance. Its SHA is PENDING. Required actual installation verification, independent product verdict, required cleanup acceptance and Architect closeout instruction must exist first. Tony then commits only the nine declared transition paths plus the named durable evidence/receipt lanes. Record the actual SHA after it exists in a subsequent receipt. Independent bounded retest covers AC25/27/31/32/33, all twelve spans, exact diff, templates and workflow references; QA Lead accepts the resulting candidate. Any unrelated change needs a properly authorized repair or map/spec amendment.

No Git action above is performed by Cody. No canonical implementation, push, PR, merge, release tag or future evidence is claimed in Phase 2.
