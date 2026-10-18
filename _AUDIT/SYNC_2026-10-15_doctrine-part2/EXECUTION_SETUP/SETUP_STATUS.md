# Execution setup — in progress

Cody Engineer; Tony performs all Git mutations. Gate2 and Gate3 already approved and now recorded. Fable closed QA-AF01 PASS. The exact R1 specification is selected by path/hash, not its retained older self-reference.

Next: Tony stages the scoped preservation list; Cody checks the staged set; Tony commits. Then Tony fetches; Cody compares actual origin/main with expected BASE before worktree creation. No actual Git/setup SHAs or clean-tree claim yet. Consolidated receipt is SETUP_RECEIPT.json and will be updated with observed facts. One review ZIP for Jarvis is produced after setup completes, not prematurely. No canonical implementation before Phase3 release.

Only the approved run plus specifically named setup bookkeeping will transfer. Root instructions, obsolete canonical/skill changes, raw intake/drop and unrelated review history outside the run must not transfer. Transfer policy/list is prepared below; actual preservation commit identity is bound only after Tony creates it.

## Additive 10x delivery — approved separately

The two finalized references are copied and hash-verified in the original review worktree. They are not yet in an execution worktree, which has not been created. See STANDALONE_10X_AUTHORIZATION.json for exact identities and Director authorization. The preservation list includes both files. TRANSFER_PATHS remains the run/bookkeeping checkpoint set; REFERENCE_TRANSFER_PATHS contains exactly the two reference files. Do not blend the reference files into the canonical sync implementation commit.

After Tony creates/preserves the approved execution-run checkpoint, transfer the two reference files from the observed review preservation commit. These are future Tony-only commands; replace the placeholder with the actual verified preservation SHA. Cody verifies both transferred hashes before the dedicated commit.

```bash
git -C /home/moose/Documents/app-factory-docs-sync-execution restore --source=ACTUAL_PRESERVATION_SHA -- '10x Lab/ABM_PLAYBOOK_v1_0.md' '10x Lab/APBM_PLAYBOOK_v1_0.md'
git -C /home/moose/Documents/app-factory-docs-sync-execution add -- '10x Lab/ABM_PLAYBOOK_v1_0.md' '10x Lab/APBM_PLAYBOOK_v1_0.md'
git -C /home/moose/Documents/app-factory-docs-sync-execution diff --cached --name-status
git -C /home/moose/Documents/app-factory-docs-sync-execution commit -m "docs(10x): add standalone ABM and APBM reference playbooks"
```

Record reference-commit SHA separately from the run checkpoint SHA in the consolidated receipt; verify both intended copies and a clean execution tree at the final setup HEAD. Canonical implementation still awaits Phase3 release. No README, MANIFEST, CHANGELOG, integration or specification changes.
