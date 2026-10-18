Copied both finalized files from Documents into [10x Lab/](</home/moose/Documents/app-factory-docs-v1/10x Lab>). Both source/destination hashes match. The separate authorization and commit plan are recorded; the frozen sync map and specification are unchanged.

The execution worktree is still pending. **Run this updated scoped staging step**, which now includes the two references and setup records:

```bash
cd /home/moose/Documents/app-factory-docs-v1
git add --pathspec-from-file=_AUDIT/SYNC_2026-10-15_doctrine-part2/EXECUTION_SETUP/PRESERVATION_PATHS.nul --pathspec-file-nul
git diff --cached --stat
```

Tell me when it finishes; I’ll verify the staged scope before your commit. The two references will receive a separate commit in the execution worktree.

[Saved response](/home/moose/Documents/app-factory-docs-v1/agent_docs/RESPONSES/response_2026-10-18_182605_standalone-10x-added.md)
