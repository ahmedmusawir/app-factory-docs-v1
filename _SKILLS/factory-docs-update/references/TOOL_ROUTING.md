# TOOL_ROUTING.md — Local Git (PRIMARY) vs GitHub MCP (exception)

> Deep reference for SKILL.md Phase 3. Load before presenting the routing decision.
> The decision itself is the Operator's (CLAUDE.md D3). This file arms the recommendation.
> **Standing operator ruling (2026-08-05): local git is the PRIMARY route. The MCP is
> the exception the Operator must explicitly choose.**

## Why this file exists (the war story)

On 2026-07-12, Wave 6 Job 1 — renaming 27 doctrine docs into tier folders — was launched
over the GitHub MCP. Each rename required: fetch file → push add-side → delete old path →
SHA-verify. Sequentially, per file, with background agents. Over an hour in, with 100+ API
calls spent and no end in sight, the Operator killed the task. The same job, redone in a
local clone: `git mv` ×27, one commit, one push, one PR — **minutes**. GitHub even rendered
the proof: "27 changed files, 0 additions, 0 deletions."

Three weeks of live operation later, the Operator promoted the lesson from threshold to
default: per-file remote calls scale linearly and verification doubles them, while local
git batches everything into one push — so the clone is home base, and the MCP is reserved
for the rare touch where a clone genuinely isn't at hand.

## The two routes

| | Route A — Local git (PRIMARY) | Route B — GitHub MCP (exception) |
|---|---|---|
| Works from | A clone of the Hub | Any session, anywhere, no clone |
| Cost model | Flat: branch + commits + one push | ~2–4 API calls per file touched (read + write + verify; +1 SHA fetch for existing files) |
| Renames/moves | `git mv` — free | Two-commit compose per rename — expensive, fiddly |
| Verification | Git-native (diff, status, rename detection) | Mandatory per call (blob SHA compare) |
| When | The default, always available at a clone | Operator-chosen exception: genuine 1–2 doc content-only touch, no clone available |

## Recommendation rules (defaults for Phase 3)

1. **Recommend local git.** That is the standing ruling; it needs no justification beyond it.
2. The ONLY shape where the MCP earns a mention as viable: 1–2 docs, content-only edits,
   AND no clone session available or obtainable without real cost. Present it honestly;
   still recommend obtaining a clone unless the touch is truly trivial.
3. **ANY rename, move, folder restructure, or new-doc entry set → local git, no exception discussion.**
4. Count the FULL write load when estimating: each doc's archive copy, MANIFEST, and
   CHANGELOG are writes too. A "one-doc update" is really ~4 writes.

## Estimate math (present these numbers, honestly)

- Local: minutes ≈ 2 + docs touched. It is almost always minutes.
- MCP: `API calls ≈ (files touched × 3) + renames × 2 + 2 overhead`. Minutes ≈ calls × 1–2,
  more if 50x retries appear.

## MCP mechanics & gotchas (exception-route execution)

1. **Existing-path updates need the current blob SHA.** Fetch before every
   `create_or_update_file` on an existing file. `push_files` and `delete_file` do not need input SHAs.
2. **`push_files` cannot delete.** Renames = two commits: push_files (new path) then
   delete_file (old path). Announce the compose so a half-done rename is never mistaken for done.
3. **Verify-after-write, always.** A call that errored may have partially succeeded
   server-side. Re-read; compare blob SHAs. Match = byte-integrity proof.
4. **Transient 50x "Unicorn" errors are real.** Announce, retry once. Second failure on the
   same call → trip the D4 checkpoint.
5. **Branch first, always.** `create_branch` before any write. Never write to main; never
   call `merge_pull_request` (standing orders).

## Local git mechanics (primary-route execution)

- Fresh branch off up-to-date main: `git checkout main && git pull && git checkout -b docs/<topic>-<date>`.
- One commit per doc, message: `docs(<doc>): v<X.Y> — <summary> [<origin>]`.
- Type commands by hand — a pasted invisible C1 control char once broke a command (`\302\226git`).
- Push with `-u origin <branch>`; hand the Operator the compare URL.
- On main: PULL, never push. Post-merge "ahead of origin" confusion = reset/pull, never force.

## The mid-flight switch (D4 aftermath)

If the Operator rules "switch to local" mid-MCP-job: (1) stop all MCP writes; (2) list
exactly what landed on the remote branch (verified files only); (3) announce the branch
for deletion — do NOT build on a half-done branch; (4) restart Phase 4 on the local route
from the approved ripple map, which remains the single source of truth.
