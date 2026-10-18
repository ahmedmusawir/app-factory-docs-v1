# QAM_MANIFEST — `<<MODULE_ID>>` (Engineer's factual completion record)

> TEMPLATE SET v0.3 — QA LEAD ACCEPTED WITH EXACT AMENDMENTS (Fable, 2026-10-14); AMENDMENTS ARCHITECT-VERIFIED; INSTALLATION REQUIRES THE APPROVED DOCSET SYNC. Template `QAM/QAM_MANIFEST.md` v0.3-draft (2026-10-14), from `QAM_PLAYBOOK_v1_0.md` §7 ("As Engineering finishes") and §5. **Owner: Engineer**, written as part of the original engineering assignment and **before the Director commits**. Facts and labeled **CLAIMs** only. This file contains no test plan, no risk order, no expected value other than the Engineer's own measurements, each marked CLAIM. It contains no Q1 finding, no Q2 result, no QA Lead decision and no certification.

**Engineer (seat, runtime):** `<<…>>` · **Recorded at:** `<<YYYY-MM-DD HH:MM TZ>>` · **Working directory for every command below:** `<<REPO_ROOT or subdir>>`

## 1. Identity (facts)

| Field | Value |
|---|---|
| Baseline (full SHA) | `<<BASELINE_SHA>>` |
| Implementation identity | `PENDING` — the candidate commit does not exist until the Director commits the completed engineering work; this manifest is written before that commit. After the commit, the Q1 entry resolves the candidate from the Director's receipt / read-only Git evidence and **reconciles it against the inventory in §2**. If this manifest needs a factual amendment afterwards, the Engineer records it, dated, in §8; the Executor records independent identity in recon. No documentation commit is made just to embed its own SHA. |
| Engineering branch | `<<MODULE_BRANCH>>` |
| Intended QA branch | `qa/<<MODULE_BRANCH>>` — the Director creates it at the completed engineering candidate commit, after this handoff |
| HEAD at handoff (last commit on `<<MODULE_BRANCH>>`, may predate the candidate) | `<<HEAD_AT_HANDOFF_SHA>>` |

## 2. Complete change inventory at handoff (facts; captured before the Director commits)

The baseline→HEAD diff alone misses uncommitted implementation work, so all four parts are recorded, with the exact command and its output path.

| Part | Command (working dir) | Output stored at | Count |
|---|---|---|---|
| 2.1 Committed since baseline | `git diff --name-status <<BASELINE_SHA>>..HEAD` (+ `git log --oneline <<BASELINE_SHA>>..HEAD`) | `<<evidence path>>` | `<<n>>` |
| 2.2 Staged, not committed | `git diff --cached --name-status` | `<<evidence path>>` | `<<n>>` |
| 2.3 Unstaged modifications | `git diff --name-status` | `<<evidence path>>` | `<<n>>` |
| 2.4 Untracked files | `git ls-files --others --exclude-standard` | `<<evidence path>>` | `<<n>>` |
| 2.5 Snapshot of the whole tree state | `git status --porcelain` | `<<evidence path>>` | — |

Consolidated inventory (one row per path across 2.1–2.4):

| Path | Where (committed / staged / unstaged / untracked) | Status (A/M/D) | What changed | Authorized by |
|---|---|---|---|---|
| `<<path>>` | `<<…>>` | `<<…>>` | `<<…>>` | `<<contract AC / ruling ID>>` |

Paths outside the authorized scope: `<<none / list with the authorizing ruling>>`. Paths the Engineer expects the Director to leave uncommitted (e.g. local-only files): `<<none / list>>`. Q1 compares the Director's committed candidate against this table and records every difference as a GAP in recon.

## 3. Claimed behavior and self-verification (CLAIMs)

| Claim (what was built) | Self-verification command (working dir) | Engineer result | Evidence link | AC(s) |
|---|---|---|---|---|
| `<<…>>` | `<<…>>` | CLAIM: `<<…>>` | `<<path>>` | `<<AC-nnn>>` |

The Engineer's handoff reports what was built, not what the acceptance criteria ought to become after building it (§3).

## 4. Reproduction (facts — exact commands, no interpretation)

| Step | Command | Working directory |
|---|---|---|
| Install | `<<…>>` | `<<…>>` |
| Build | `<<…>>` | `<<…>>` |
| Serve | `<<…>>` | `<<…>>` |
| Tests / board | `<<…>>` | `<<…>>` |
| Reproduce claim `<<n>>` | `<<…>>` | `<<…>>` |

## 5. Environment the QA body needs (facts; no secret values)

| Item | Value |
|---|---|
| Environments / targets | `<<…>>` |
| Services and external prerequisites | `<<…>>` |
| Migrations / fixtures / seed state | `<<…>>` |
| Roles and identities required | `<<by role name only>>` |
| Credentials needed (key names only) | `<<KEY_NAMES>>` — the Director creates `<<QA_CREDENTIAL_FILE>>`; values are never written here |
| Ports / resources | `<<…>>` |
| Runtime and tool versions used by the Engineer | `<<…>>` |

## 6. Known limitations, unresolved issues, preserved paths, rollback (facts)

| Item | Detail |
|---|---|
| Known limitations | `<<…>>` |
| Unresolved issues | `<<…>>` |
| Preserved / untouched paths relevant to QA | `<<…>>` |
| Rollback dependencies | `<<…>>` |
| Not done by engineering | `<<…>>` |

## 7. Meaning of each engineering evidence item (CLAIMs)

| Evidence path | What it shows (CLAIM) | How QA can independently re-derive it |
|---|---|---|
| `<<path>>` | `<<…>>` | `<<…>>` |

## 8. Factual amendments after handoff (dated; Engineer only)

| Date | Owner | Field amended | Old → new | Reason |
|---|---|---|---|---|
| | | | | |

*TEMPLATE SET v0.3 — QA LEAD ACCEPTED WITH EXACT AMENDMENTS (Fable, 2026-10-14); AMENDMENTS ARCHITECT-VERIFIED; INSTALLATION REQUIRES THE APPROVED DOCSET SYNC.*
