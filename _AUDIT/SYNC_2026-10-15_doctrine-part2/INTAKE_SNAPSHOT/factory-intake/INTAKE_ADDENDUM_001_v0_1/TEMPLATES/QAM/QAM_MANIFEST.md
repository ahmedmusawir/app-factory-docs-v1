# QAM_MANIFEST — `<<MODULE_ID>>` (Engineer's factual completion record)

> NEWLY AUTHORED DRAFT — QA LEAD REVIEW REQUIRED. Template `QAM/QAM_MANIFEST.md` v0.1-draft (2026-10-14), from `QAM_PLAYBOOK_v1_0.md` §7 ("As Engineering finishes") and §5. **Owner: Engineer**, written as part of the original engineering assignment. Facts and labeled **CLAIMs** only. This file contains no test plan, no risk order, no expected value other than the Engineer's own measurements, each marked CLAIM. It contains no Q1 finding, no Q2 result, no QA Lead decision and no certification.

**Engineer (seat, runtime):** `<<…>>` · **Recorded at:** `<<YYYY-MM-DD HH:MM TZ>>` · **Working directory for every command below:** `<<REPO_ROOT or subdir>>`

## 1. Identity (facts)

| Field | Value |
|---|---|
| Baseline (full SHA) | `<<BASELINE_SHA>>` |
| Implementation identity | `PENDING` — the final commit SHA does not exist until the Director commits; after the commit the Q1 entry resolves it from the Director's receipt / read-only Git evidence. If this manifest needs a factual amendment afterwards, the authorized owner records it (dated) below; the Executor records independent identity in recon. No documentation commit is made just to embed its own SHA. |
| Engineering branch | `<<MODULE_BRANCH>>` |
| Intended QA branch | `qa/<<MODULE_BRANCH>>` (Director creates at the same starting commit) |
| Working tree at handoff | `<<clean / list of intentionally uncommitted paths>>` (`git status --porcelain` output in `<<evidence path>>`) |

## 2. Changed paths and authorized exceptions (facts)

| Path | Status (A/M/D) | What changed | Authorized by |
|---|---|---|---|
| `<<path>>` | `<<…>>` | `<<…>>` | `<<contract AC / ruling ID>>` |

Diff command: `git diff --name-status <<BASELINE_SHA>>..HEAD` (output stored at `<<evidence path>>`). Paths outside the authorized scope: `<<none / list with the authorizing ruling>>`.

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

## 8. Factual amendments after handoff (dated; authorized owner only)

| Date | Owner | Field amended | Old → new | Reason |
|---|---|---|---|---|
| | | | | |

*NEWLY AUTHORED DRAFT — QA LEAD REVIEW REQUIRED.*
