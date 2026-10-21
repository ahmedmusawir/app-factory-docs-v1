# Final local reconciliation — records-only publication

Baseline accepted branch: c69be638aca3bf3ec7610788e867c8428b3ec874. Both supplied paths share `/home/moose/Documents/app-factory-docs-v1/.git`; the complete worktree listing contains exactly the review worktree and execution worktree. No staged changes initially. Review:3 modified tracked files,1148 untracked files,3 ignored lint caches. Execution:clean tracked/untracked state,1 ignored lint cache. Exact initial paths and dispositions are in LOCAL_FILE_INVENTORY.json and LOCAL_STATUS_DISPOSITIONS.json. New reconciliation audit artifacts are identified by publication scope separately.

## 1. Publish missing durable records

88 exact-byte source records:21 missing run receipts at their original run paths and67 operator/session records archived under RECONCILIATION_2026-10-21/OPERATOR_RECORDS/ with their original relative paths. PUBLISH_RECORDS.json names every source, destination, SHA-256 and reason. Operator records cover completed-sync intake/planning, execution, amendments, QA and publication (October12–21); they are historical evidence, not active instructions. Source files remain untouched. The reconciliation inventories and this report are additional new audit records. Actual commit/push identity is observed only after creation in the external publication receipt; no self-referential SHA is invented here.

## 2. Already published

1729 compared review files already have exact content retained on the accepted branch (1722 run files plus7 operator records), sometimes at a different retained evidence path. ALREADY_PUBLISHED.json maps every source SHA to its accepted path(s). This includes the complete QA evidence, approved amendments, generators retained under their amendment records, and standalone10x files. No duplicate publication is needed. Final Fable QA manifest is verified from the run directory before and after publication; this is integrity verification, not a new QA cycle.

## 3. Kept local; no deletion or review-branch merge

KEPT_LOCAL.json gives17 specific unique files:6 delivery ZIPs,3 obsolete/conflicting setup/operator run records,4 unrelated/mixed operator records and4 ignored caches. All remain at their original absolute paths listed below. Already-published local copies also remain in place, so the review worktree intentionally remains dirty.

- `/home/moose/Documents/app-factory-docs-v1/_AUDIT/SYNC_2026-10-15_doctrine-part2/DELIVERY/FACTORY_AMENDED_V1_QA_SPEC_REVIEW_2026-10-17_160835.zip` — Local delivery ZIP; durable constituent records are retained separately; no new ZIP publication.
- `/home/moose/Documents/app-factory-docs-v1/_AUDIT/SYNC_2026-10-15_doctrine-part2/DELIVERY/FACTORY_AMENDED_V2_EXECUTION_HANDOFF_2026-10-19_150618.zip` — Local delivery ZIP; durable constituent records are retained separately; no new ZIP publication.
- `/home/moose/Documents/app-factory-docs-v1/_AUDIT/SYNC_2026-10-15_doctrine-part2/DELIVERY/FACTORY_AMENDED_V2_REVIEW_2026-10-19_135012.zip` — Local delivery ZIP; durable constituent records are retained separately; no new ZIP publication.
- `/home/moose/Documents/app-factory-docs-v1/_AUDIT/SYNC_2026-10-15_doctrine-part2/DELIVERY/FACTORY_AMENDED_V3_EXECUTION_HANDOFF_2026-10-20_104051.zip` — Local delivery ZIP; durable constituent records are retained separately; no new ZIP publication.
- `/home/moose/Documents/app-factory-docs-v1/_AUDIT/SYNC_2026-10-15_doctrine-part2/DELIVERY/FACTORY_AMENDED_V3_REVIEW_2026-10-19_203340.zip` — Local delivery ZIP; durable constituent records are retained separately; no new ZIP publication.
- `/home/moose/Documents/app-factory-docs-v1/_AUDIT/SYNC_2026-10-15_doctrine-part2/DELIVERY/FACTORY_QA_AF01_REPAIR_2026-10-17_173649.zip` — Local delivery ZIP; durable constituent records are retained separately; no new ZIP publication.
- `/home/moose/Documents/app-factory-docs-v1/_AUDIT/SYNC_2026-10-15_doctrine-part2/EXECUTION_SETUP/SETUP_RECEIPT.json` — Obsolete/conflicting review-branch setup or operator-state variant; preserve locally, do not overwrite accepted run.
- `/home/moose/Documents/app-factory-docs-v1/_AUDIT/SYNC_2026-10-15_doctrine-part2/EXECUTION_SETUP/SETUP_STATUS.md` — Obsolete/conflicting review-branch setup or operator-state variant; preserve locally, do not overwrite accepted run.
- `/home/moose/Documents/app-factory-docs-v1/_AUDIT/SYNC_2026-10-15_doctrine-part2/OPERATOR_NEXT_STEPS.md` — Obsolete/conflicting review-branch setup or operator-state variant; preserve locally, do not overwrite accepted run.
- `/home/moose/Documents/app-factory-docs-v1/RECOVERY.md` — Unrelated pre-sync session or mixed active recovery history; preserve locally on review branch.
- `/home/moose/Documents/app-factory-docs-v1/agent_docs/SESSIONS/session_2026-09-27.md` — Unrelated pre-sync session or mixed active recovery history; preserve locally on review branch.
- `/home/moose/Documents/app-factory-docs-v1/agent_docs/SESSIONS/session_2026-10-10.md` — Unrelated pre-sync session or mixed active recovery history; preserve locally on review branch.
- `/home/moose/Documents/app-factory-docs-v1/agent_docs/SESSIONS/session_2026-10-11.md` — Unrelated pre-sync session or mixed active recovery history; preserve locally on review branch.
- `/home/moose/Documents/app-factory-docs-v1/lints/__pycache__/header_lint.cpython-312.pyc` — Ignored regenerable lint cache from local checks; keep local.
- `/home/moose/Documents/app-factory-docs-v1/lints/__pycache__/lint_common.cpython-312.pyc` — Ignored regenerable lint cache from local checks; keep local.
- `/home/moose/Documents/app-factory-docs-v1/lints/__pycache__/versioned_refs_lint.cpython-312.pyc` — Ignored regenerable lint cache from local checks; keep local.
- `/home/moose/Documents/app-factory-docs-sync-execution/lints/__pycache__/lint_common.cpython-312.pyc` — Ignored regenerable lint cache from local checks; keep local.

Additional exact locations for local Downloads archives and known temporary task/export roots are in EXTERNAL_LOCAL_DELIVERIES_SCRATCH.json; these are outside repository publication and untouched. Run scratchpad/proposed exports whose bytes are already published are preserved; no new scratch or ZIP bytes are added. New /tmp/reconcile_* scripts remain local task tooling.

There are four local branches, all with same-name remote branches. main, astra-factory-doc-review and the accepted sync branch initially match their remotes. factory-docs-review-astra-w-chunks remains at local e7b4a6f33e1ae2442f71d82f7f3a9d694f50da36, one preservation commit absent from all live remote heads, whose same-name remote tip is626da8d70f4db22987dc7fcc86765492072360cd. Keep that commit/branch local; do not push or cherry-pick it. BRANCH_INVENTORY.json records all tips and LOCAL_COMMIT_DISPOSITIONS.json accounts for all1079 changed paths, including8 historical deletions/moves that are not replayed. Exact equivalent content is already retained or missing current durable records are separately copied; unrelated and old variants stay with that local commit. All prior remote branches remain untouched.

## Canonical comparison and approval

No dirty canonical path and no new unpublished canonical document change was discovered. The two10x additions in the preservation commit already match accepted published bytes. The review branch has33 existing canonical files differing from current accepted content because it predates the approved sync/repairs/activation. These obsolete variants are not proposed changes and receive no inferred approval. REVIEW_CANONICAL_DIFFERENCES.json lists identities. Exact accepted→obsolete-review diff is retained locally at `/home/moose/Documents/app-factory-docs-v1/_AUDIT/SYNC_2026-10-15_doctrine-part2/RECONCILIATION_2026-10-21/OBSOLETE_REVIEW_CANONICAL.diff`; the complete review working diff is alongside it as LOCAL_REVIEW_WORKING.diff. Both diff artifacts stay local and are excluded from publication. The branch path comparison is provided separately. No canonical bytes, frozen approvals, QA records, lint code, template, archive or standalone10x bytes are overwritten.

## 4. Merge readiness

No content blocker identified. Fable’s accepted closeout verdict is preserved; no QA round is reopened for this records-only publication. Verify all preexisting accepted tracked bytes, scoped staged/committed additions, final manifest, matching remote HEAD and clean execution worktree. Tony retains PR creation and merge. No main write, merge, deletion, force push or history rewrite.

Current reconciliation completion receipts, live RECOVERY.md and the live session log are operator bookkeeping outside the execution worktree; they are not inputs to or changes in the accepted canonical/QA set. Their final locations are reported with the final publication receipt, avoiding an endless self-referential commit cycle.
