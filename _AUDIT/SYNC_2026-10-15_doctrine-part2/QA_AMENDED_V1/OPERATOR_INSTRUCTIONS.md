# Current operator instructions — consolidated AMENDED-v1 review

Tony performs every Git mutation. These instructions supersede the sequencing and pathspec examples in the preserved original OPERATOR_NEXT_STEPS.md and AMENDED_V1 supplement. They do not approve anything. The source amendment, original map and earlier specification remain unchanged. Current seat: Cody, QA Lead under Tony’s assignment; the next Engineer must be explicitly assigned.

## 1. Decide in order and resolve the concrete blocker

Read AMENDMENT_CONFIRMATION.md and QA_AF01_PATCH_FIDELITY.md. All eight ownership corrections are confirmed. The distributed patch has one High acceptance failure affecting two archives. The exact content/index is correct; the patch is not executable with byte fidelity.

1. Tony records his Gate 2 amendment decision in ORDERED_GATE_DECISIONS.md, identifying the exact package, amendment, index and patch. A decision on the ownership wording alone does not approve the defective patch for execution.
2. Tony records Gate 3 on DOCSET_SYNC_ACCEPTANCE_SPEC_AMENDED_V1.md only after Gate 2. The form pins the submitted specification hash. Both decisions are currently PENDING.
3. Route QA-AF01 to the Engineer for bounded serialization repair and regenerated patch-dependent identities/package records. Preserve the 380 edits, 101 target hashes, old patch and submitted review. QA independently retests all 101 patch outputs, both archive Git blob IDs, scope and lint. Record corrected identities and attributable decisions; a patch hash change must not silently reuse an earlier approval. Update only affected spec identity cells if the patch changes, with Gate 3 re-approval of that exact successor.
4. No Phase 3 release until the failure is resolved and the approval/setup receipts below exist. The instructions and preservation files needed for setup are already included; no intake restart or repeat template acceptance is needed.

The approved execution source is the separately identified amendment overlay plus original frozen proposal, as defined in the matching spec. Do not overwrite the frozen records. Any later Engineer folding into an active execution view requires explicit instruction and must preserve both reviewed versions and prove equality to the approved composed index.

## 2. Preserve the exact reviewed and approved state

Use COMPLETE_PRESERVATION_PATHS.txt and its NUL companion in this directory, not the original stale October 16 list. The consolidated list incorporates both earlier supplements, the actual relocated session paths, this review, the handoff and today’s responses/receipt. PRESERVATION_SUPPLEMENT.txt explains the additions and excludes caches, Downloads ZIPs and `_INBOX/`. Existing tracked root-session deletions and their relocated copies are preserved as earlier bookkeeping, not re-created or deleted by QA.

Inspect the list, working tree and staged set first. Every later repair/approval record must be added by exact path to this list before the final preservation commit; the list does not grant permission to stage unrelated work. If unexpected files are already staged, stop and reconcile them without reset/stash.

Tony runs:

```sh
cd /home/moose/Documents/app-factory-docs-v1
git status --short
git diff --stat
git diff --cached --name-status
git rev-parse HEAD main origin/main
```

After reviewing the named list, Tony stages only those paths, reviews the staged diff and commits:

```sh
git add --pathspec-from-file=_AUDIT/SYNC_2026-10-15_doctrine-part2/QA_AMENDED_V1/COMPLETE_PRESERVATION_PATHS.nul --pathspec-file-nul
git diff --cached --name-status
git diff --cached --stat
git commit -m "chore(sync): preserve amended map review and matching specification"
git rev-parse HEAD
```

Record the observed full SHA in ORDERED_GATE_DECISIONS.md. It must contain the exact approved records and resolution evidence; if those change later, preserve them in a later named commit and use its actual SHA. The receipt of a commit naturally lives in a later record; no self-referential commit SHA is invented.

## 3. Verify the actual remote baseline

Tony runs:

```sh
git fetch origin
git rev-parse main origin/main
git worktree list --porcelain
git branch --list docs/sync-doctrine-part2-2026-10-15
```

Expected BASE is `9c179392f79b70da099121fc357d3107ad3bb86e`. If origin/main differs, return the actual SHA and reconcile the before-hashes/placements through an attributable amendment before execution. No automatic reset, merge, rebase or replacement base. QA has not fetched and cached origin/main is not current-remote evidence.

## 4. Create and checkpoint the isolated execution worktree

After the gates and blocker are resolved, verify that the proposed worktree path is absent and branch unused. Tony then runs:

```sh
test ! -e /home/moose/Documents/app-factory-docs-sync-execution
git worktree add -b docs/sync-doctrine-part2-2026-10-15 /home/moose/Documents/app-factory-docs-sync-execution 9c179392f79b70da099121fc357d3107ad3bb86e
```

If the test fails or the branch already exists, inspect and reconcile; do not overwrite it. Substitute the observed preservation SHA, then transfer only the durable run:

```sh
SYNC_PRESERVATION_SHA='REPLACE_WITH_OBSERVED_FULL_SHA'
git -C /home/moose/Documents/app-factory-docs-sync-execution restore --source="$SYNC_PRESERVATION_SHA" -- _AUDIT/SYNC_2026-10-15_doctrine-part2
git -C /home/moose/Documents/app-factory-docs-sync-execution status --short
```

The assigned verifier compares the 189-file snapshot with INTAKE_SNAPSHOT_INDEX.json, the exact original and approved amended map/spec identities, the resolved patch evidence and all 101 composed hashes; confirms BASE and that only the transferred run is dirty. Approval records must name the amendment overlay and matching spec rather than relying on the root historical v1.0 filename. Tony then checkpoints only that run:

```sh
git -C /home/moose/Documents/app-factory-docs-sync-execution add -- _AUDIT/SYNC_2026-10-15_doctrine-part2
git -C /home/moose/Documents/app-factory-docs-sync-execution diff --cached --stat
git -C /home/moose/Documents/app-factory-docs-sync-execution commit -m "chore(sync): checkpoint approved amended execution inputs"
git -C /home/moose/Documents/app-factory-docs-sync-execution rev-parse HEAD
git -C /home/moose/Documents/app-factory-docs-sync-execution status --porcelain
```

Record the checkpoint SHA separately from the review preservation SHA. The execution worktree must be clean before implementation. No root instructions, earlier review-branch canonical changes or old skill copy are transplanted; never merge the review branch into main.

## 5. Explicit Phase 3 release and date binding

Tony issues an attributable Phase 3 release only after all prior records and identities are verified. The Engineer is then assigned implementation. Nothing in this review, the approval form or these command blocks constitutes that release.

Use the approved AMENDED_V1 index/content view: 380 ordered edits, 101 paths, three amended documents. Bind only the 151 named current fields in AMENDED_V1/LANDING_DATE_PLAN.json to the actual landing date. Generate separate BOUND_EXECUTION_INDEX.json and BOUND_STATUS_TRANSITIONS.json. Preserve historical dates and all frozen review identities. Build the later full post-closeout index from the amended base plus the nine transition paths, carrying the three amended hashes forward. Existing root POST_VERIFICATION_PROPOSAL_INDEX.json has historical unaffected-file hashes and must not replace the amended index wholesale.

Record actual implementation CONTENT_SHA after Tony’s implementation commit exists. Publication, independent installed-candidate QA and subsequent release gates remain separate; no push/PR/merge is authorized by this review.

## 6. Later bounded closeout

The twelve status transitions on nine paths stay pending until actual template-install verification, the exact candidate’s independent product verdict, required cleanup acceptance, Architect closeout instruction and required evidence exist. Tony’s closeout commit activates verified doctrine/workflow references and installed-template provenance. Record its SHA after it exists. Retest AC25/27/31/32/33, all twelve spans, template hashes and workflow references (AC22/28); QA Lead accepts the post-closeout candidate separately. Preserve all exclusions and the D-3 readability follow-up. D-4 is existing approved metadata, not a new edit.
