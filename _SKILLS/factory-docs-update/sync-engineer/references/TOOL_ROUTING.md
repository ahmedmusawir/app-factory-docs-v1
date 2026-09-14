# TOOL_ROUTING.md — Local Git at a Hub Clone (the execution environment) vs the GitHub MCP (exception)

> Engineer-child reference. The Hub clone with local git is the execution environment (family CLAUDE.md D3; Operator ruling 2026-08-05). This file exists for the rare session with no clone (`decision-trees/route-selection.md` Decision B) and for the local-git mechanics every run uses. **Push timing is NOT decided here:** the single push rule is `_shared/references/SHA_AND_PUSH_CONTRACT.md` (D18) — there is exactly one push, after Gate 4, plus bounded QA-repair pushes on LARGE.

## Why this file exists (the war story)

On 2026-07-12, Wave 6 Job 1 — renaming 27 doctrine docs into tier folders — was launched over the GitHub MCP. Each rename required: fetch file → push add-side → delete old path → SHA-verify. Over an hour in, with 100+ API calls spent and no end in sight, the Operator killed the task. The same job, redone in a local clone: `git mv` ×27, one commit, one push, one PR — **minutes**. Three weeks later the Operator promoted the lesson from threshold to default: the clone is home base; the MCP is reserved for the rare touch where a clone genuinely is not at hand.

## The two routes

| | Local git at a Hub clone (execution environment) | GitHub MCP (exception) |
|---|---|---|
| Works from | A clone of the Hub | Any session, no clone |
| Cost model | Flat: branch + commits + one push after Gate 4 | ~2–4 API calls per file touched (read + write + verify; +1 SHA fetch for existing files) |
| Renames / moves / new docs / assets | native | two-commit compose per rename — expensive; new docs and assets → local git, no exception discussion |
| Verification | git-native (diff, status, `git show <base>:<path>` fidelity) | mandatory per call (blob SHA compare) |
| When | always, at a clone | Operator-chosen exception: genuine 1–2 doc content-only touch, no clone obtainable |

## Local git mechanics (every run)

- Discovery: `git fetch origin`; report distance from `origin/main`; **do not pull** during discovery (D9 of the review: a pull is a write and is ambiguous off-main).
- Branch: from the approved BASE_SHA (UPDATE MAP §0; D18), never blindly from main. Already on the approved run branch at BASE_SHA or a lawful descendant (`git merge-base --is-ancestor <BASE_SHA> HEAD`, only this run's commits in `git log <BASE_SHA>..HEAD`) → stay. Otherwise → `git switch -c <run-branch> <BASE_SHA>`.
- One commit per canonical doc: `docs(<DOC>): v<X.Y> - <summary> [<IDs>]`; repairs: `docs(<DOC>): v<X.Y> - repair QA-F<nn> [<IDs>]`; metadata: `chore(sync): … [<run-id>]`. Plain hyphens. No `Co-Authored-By` trailer, ever — strip it if injected (D22).
- Type commands by hand — a pasted invisible C1 control character and, later, an em-dash in a commit message each broke a command inexplicably (AP-10).
- Archive fidelity per doc before commit: `git show <BASE_SHA>:<path> | diff - _ARCHIVE/<NAME>_v<X_Y>.md` → empty.
- Lints per doc before commit: `py lints/run_all.py` (or the rig's Python) — new findings fixed, baseline untouched, no exemptions (D9).
- **Push: only after Gate 4 approval** — `git push -u origin <branch>`; then report `git rev-parse origin/<branch>`. Repair pushes only inside Phase 6. Never before Gate 4, never on main.
- On main: PULL, never push. Post-merge "ahead of origin" confusion = reset/pull, never force.
- PR number after merge: `git ls-remote origin 'refs/pull/*/head'` matched to the pushed tip (no MCP needed).

## MCP mechanics & gotchas (exception route only)

1. **Branch first, always.** `create_branch` from the approved BASE_SHA before any write. Never write to main; never call `merge_pull_request`.
2. **Existing-path updates need the current blob SHA.** Fetch before every `create_or_update_file` on an existing file.
3. **`push_files` cannot delete.** Renames = two commits: `push_files` (new path) then `delete_file` (old path). Announce the compose.
4. **Verify-after-write, always.** A call that errored may have partially succeeded server-side. Re-read; compare blob SHAs.
5. **Transient 50x "Unicorn" errors are real.** Announce, retry once. Second failure on the same call → D4 checkpoint.
6. **Gate 4 still applies.** On the MCP the "push" is the moment writes land on the remote branch; that moment is after Gate 4 too — draft everything locally in the session, present Gate 4 evidence, then write. The compare URL comes after.
7. **The mid-flight switch (D4 aftermath):** if the Operator rules "switch to local" mid-job: stop MCP writes; list exactly what landed (verified files only); announce the branch for deletion — never build on a half-done branch; restart Phase 4 locally from the approved UPDATE MAP, which remains the single source of truth.

## Estimate math (present honestly when Decision B reaches B3)

- Local: minutes ≈ 2 + docs touched.
- MCP: calls ≈ (files touched × 3) + renames × 2 + 2; minutes ≈ calls × 1–2, more with 50x retries. Count the FULL write load: archives, MANIFEST, CHANGELOG, assets are writes too.
