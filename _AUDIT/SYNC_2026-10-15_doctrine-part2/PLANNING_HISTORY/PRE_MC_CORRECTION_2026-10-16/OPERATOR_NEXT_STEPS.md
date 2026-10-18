# Operator setup — Phase 2, Tony executes Git

Current reviewed baseline: HEAD 626da8d70f4db22987dc7fcc86765492072360cd on factory-docs-review-astra-w-chunks; local main/origin-main 9c179392f79b70da099121fc357d3107ad3bb86e. No fetch was performed. Only the original worktree exists. Keep all work; do not reset, discard, merge the review branch, or transplant its older skill family.

## 1. Preserve the reviewed scope

Engineer preparation is saved for review. Run this checkpoint after inspecting the handoff; subsequent review amendments require another scoped preservation checkpoint before transfer. Read the exact status/diff first:

```sh
cd /home/moose/Documents/app-factory-docs-v1
git status --short
git diff --stat
git diff --cached --stat
git branch --show-current
git rev-parse HEAD main origin/main
```

Stage only this work’s named paths. Review the response directory changes against the saved status before including it; stop for an unexplained path. _INBOX is a local drop, not a substitute for the durable snapshot under _AUDIT.

```sh
git add -- AGENTS.md RECOVERY.md session_2026-10-12.md session_2026-10-13.md session_2026-10-14.md session_2026-10-15.md session_2026-10-16.md factory-corrections factory-intake _AUDIT/SYNC_2026-10-15_doctrine-part2 agent_docs/RESPONSES
git diff --cached --stat
git diff --cached --name-only
git commit -m "chore(sync): preserve doctrine-part2 phase 2 preparation"
git rev-parse HEAD
```

Return the full preservation SHA. This is NOT the implementation commit or a map/spec approval. One implementation commit is approved for this run; preservation/QA repair/closeout commits remain possible.

## 2. Verify remote baseline, then prepare isolated worktree

```sh
git fetch origin
git rev-parse main origin/main
git worktree list --porcelain
```

If origin/main differs from 9c179392f79b70da099121fc357d3107ad3bb86e, return its SHA for baseline reconciliation before using these proposals. Do not automatically rebase, merge or substitute the new base.

After baseline confirmation and completed preparation, this proposed destination must be absent and the branch unused:

```sh
git worktree add -b docs/sync-doctrine-part2-2026-10-15 /home/moose/Documents/app-factory-docs-sync-execution 9c179392f79b70da099121fc357d3107ad3bb86e
```

Transfer only the durable run folder from the actual preservation SHA. Substitute the observed full SHA for the placeholder; never copy the review branch’s _SKILLS, canonical tiers or Git internals:

```sh
SYNC_PRESERVATION_SHA=REPLACE_WITH_OBSERVED_FULL_SHA
git -C /home/moose/Documents/app-factory-docs-sync-execution restore --source="$SYNC_PRESERVATION_SHA" -- _AUDIT/SYNC_2026-10-15_doctrine-part2
git -C /home/moose/Documents/app-factory-docs-sync-execution status --short
```

No canonical files should change at this step. Execution setup must be rechecked in that worktree, including immutable snapshot hashes and governing skill identity. Fable’s independent specification and Tony’s executable-map/spec approvals are still required before Phase 3; do not apply EXECUTION_PROPOSAL.patch now. No tag, push, PR or merge command is authorized by these setup instructions.
