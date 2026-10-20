# Operator next steps — proposals, not executed

1. Jarvis reviews UPDATE_MAP.md, especially §K, exact edits, template translations and preservation constraints. Tony records attributable rulings or explicit scoped deferrals. Source-template acceptance is settled; installation verification remains required.
2. Complete the remaining exact recipe replacements and semantic review of PROPAGATION.tsv before Gate 2 freezes an executable map. Its current classifications are preliminary search triage, not independently reviewed dispositions. Missing kit evidence blocks the named kit rows; it does not authorize guessed signatures.
3. Tony preserves the current review branch before any intake handling or branch/worktree changes. Review the exact status first; do not discard or reset anything. The following are read-only checks:

```sh
git status --short
git diff --stat
git diff --cached --stat
git branch --show-current
git rev-parse HEAD main origin/main
```

Proposed scoped preservation commands for Tony only, after checking status against RECOVERY_STATUS.txt and this run’s final report:

```sh
git add -- AGENTS.md RECOVERY.md session_2026-10-12.md session_2026-10-13.md session_2026-10-14.md session_2026-10-15.md factory-corrections factory-intake _AUDIT/SYNC_2026-10-15_doctrine-part2
```

Stage only the explicitly listed response files in the accompanying `PRESERVATION_RESPONSE_PATHS.txt`, after reviewing them. Do not use a repository-wide add. Then inspect staged content and commit the preserved planning/intake revision (Tony selects the message and records the resulting SHA). This is preservation, not a canonical implementation release. No merge is requested.

4. Gate 1 must approve the proposed PHASE1_LEDGER and actual cargo identities. Only then drop cargo into the agreed `_INBOX/` layout and verify it against the indexed originals. No cargo has been dropped here. Snapshot the actual approved drop using the governing main skill before implementation. Record paths, hashes, preservation SHA, baseline and gate evidence; do not relabel this proposed ledger as a completed intake record.
5. Tony selects the isolated execution worktree/branch based on main 9c179392f79b70da099121fc357d3107ad3bb86e, after preservation. Do not merge the review branch’s older `_SKILLS/` into main. Use the governing main skill and transfer only approved intake/planning artifacts. Exact worktree and drop commands depend on Tony’s selected destination and Gate 1 cargo layout; no guessed path is authorized here.
6. Gate 2 freezes the completed executable map. This LARGE run also requires the skill’s independent QA Lead acceptance-spec gate before canonical execution. Engineer implementation then follows only the approved map. Tony performs every Git mutation, final commit, merge and push.

No extra permission is needed for the already-authorized drafting; these gates concern intake and execution. No new ZIP or duplicate source review package is created.
