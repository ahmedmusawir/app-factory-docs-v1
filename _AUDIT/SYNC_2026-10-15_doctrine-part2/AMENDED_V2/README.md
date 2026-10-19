# AMENDED-v2 review package

1. HUMAN_SUMMARY.md — short handback and status.
2. AMENDMENT_V2.md / AMENDMENT_V2_EDITS.json — exact E381–E409 old/new spans, authority and evidence.
3. PROPOSED_CONTENT/ — exactly seven canonical files; EXECUTION_PROPOSAL.patch is the complete candidate-to-proposal delta.
4. EXECUTION_PROPOSAL_INDEX.json / BOUND_EXECUTION_INDEX.json — identical, date-bound 101-path successors; candidate before hashes; 94 unchanged paths.
5. VERIFICATION.json, COMMANDS.json, PATH_VERIFICATION.json, PROTECTED_PATHS.json, EXPORT_HASHES.json, METADATA_VERIFICATION.json, CLOSEOUT_TRANSITIONS.json, WITHDRAWAL_ROWS.json, LINT_OUTPUT.txt and PROPAGATION.tsv — Engineer evidence.
6. JARVIS_FABLE_HANDOFF.md — exact identity handoff and R1–R12 accounting corrections; future Gate 2/landing/retest boundary.
7. INPUTS/ — original handback ZIP and exact source copies; AMENDMENT_IDENTITIES.json pins them. SELECTED_EXACT_EDITS.json preserves all 380 original records and appends 29.
8. scratchpad/generators/ at ZIP root — generation and verification helpers. SHA256SUMS.txt at ZIP root covers every other member.

## Reproduction in the review repository

The helpers require local Git access to the pinned candidate in `/home/moose/Documents/app-factory-docs-sync-execution` and the original source handback/review records. They use only Python standard-library modules and Git; no application dependency installation or network calls.

Run from the review repo (writes only proposal records and temporary exports):

```bash
python3 -B -I _AUDIT/SYNC_2026-10-15_doctrine-part2/scratchpad/generators/cody_amend_v2.py
python3 -B -I _AUDIT/SYNC_2026-10-15_doctrine-part2/scratchpad/generators/cody_amend_v2_verify.py
```

Generation rebuilds draft artifacts; reseal the inventory and regenerate the delivery ZIP after any change. Verification timestamps and scratch paths naturally differ. Do not regenerate an approved sealed package in place.

For a standalone patch check, export `git archive 20f71ee932ed21c0878cb3a0f39c6fbe90d0a793` to a fresh disposable directory and run `git apply --check -p0 <absolute-path-to-EXECUTION_PROPOSAL.patch>` there. Never run apply on the execution worktree before Tony’s recorded Gate 2. The diff generator emits no-newline markers when a changed diff line lacks a terminal newline; this delta does not need any, and exact output bytes were verified.

Verify inventory after extracting the ZIP with `sha256sum -c SHA256SUMS.txt`. The delivery receipt inside the ZIP pins payload identities and excludes its enclosing ZIP hash to avoid self-reference; the external review-repo receipt records the delivered ZIP hash.
