# QAM_PREFLIGHT — `<<MODULE_ID>>` (executable readiness checks)

> NEWLY AUTHORED DRAFT — QA LEAD REVIEW REQUIRED. Template `QAM/QAM_PREFLIGHT.md` v0.1-draft (2026-10-14), from `QAM_PLAYBOOK_v1_0.md` §5 and §8 (Q1 checks 1–6). **Owner: Architect authors the rows (expected result, owner, authorization); the QA Executor records the results in Q1 and rechecks changeable rows at Q2 entry.** Rows measure real prerequisites for this module; there is no universal minimum row count. Every result starts as `NOT RUN`.

**Executor:** `<<seat / runtime>>` · **Run at:** `<<YYYY-MM-DD HH:MM TZ>>` · **Working directory:** `<<…>>` · **Results file:** `evidence/preflight/<<attempt>>/PREFLIGHT_RESULTS.txt`

Q1 is read-only toward product and live business data; writes go only to the declared QA lane and approved transient setup. Install/build/serve and bounded login/logout probes are allowed only where a row below authorizes them. Execute the complete permitted assessment in one run; aggregate independent blockers instead of returning after each one; stop immediately before a forbidden or unsafe action.

## Section 1 — Repository and identity (playbook §8 check 1)

| # | Check | Command (working dir) | Expected | Authorized effect | Result | Evidence |
|---|---|---|---|---|---|---|
| PF-1.1 | Repository and branch | `git rev-parse --abbrev-ref HEAD` | `qa/<<MODULE_BRANCH>>` | read-only | NOT RUN | |
| PF-1.2 | Full HEAD, baseline, candidate | `git rev-parse HEAD`; `git log --oneline <<BASELINE_SHA>>..HEAD` | candidate per Director receipt; recorded in `QAM_RECON_REPORT.md` §1 | read-only | NOT RUN | |
| PF-1.3 | Tracked and untracked state | `git status --porcelain` | `<<expected: empty / listed paths>>` | read-only | NOT RUN | |
| PF-1.4 | Candidate ancestry | `git merge-base --is-ancestor <<CANDIDATE>> HEAD` | exit 0 | read-only | NOT RUN | |
| PF-1.5 | Complete changed-path inventory vs baseline | `git diff --name-status <<BASELINE_SHA>>..<<CANDIDATE>>` | matches `QAM_MANIFEST.md` §2 | read-only | NOT RUN | |
| PF-1.6 | Candidate → HEAD diff is docs-only (if HEAD ≠ candidate) | `git diff --stat <<CANDIDATE>>..HEAD` | only `QAM/**` and governed bookkeeping paths; else `STOP-IDENTITY` | read-only | NOT RUN | |

## Section 2 — Contract and handoff (check 2)

| # | Check | How | Expected | Result | Evidence |
|---|---|---|---|---|---|
| PF-2.1 | Frozen contract present, version/hash as in `QAM_ENTRY.md` §2 | `sha256sum <<spec path>>` | match | NOT RUN | |
| PF-2.2 | Ruling / erratum lane read; pre-ruled exceptions listed | read | list in recon §2 | NOT RUN | |
| PF-2.3 | Protected paths and scope understood | read `QAM_ENTRY.md` §3 | — | NOT RUN | |
| PF-2.4 | Governing bodies resolve with version + hash | `GOVERNING/README.md` rows | all resolve | NOT RUN | |
| PF-2.5 | Engineer manifest and handoff complete (every AC has a row; no secret values) | read | complete, or GAP rows in recon | NOT RUN | |

## Section 3 — Runtime, tools, resources (check 3)

| # | Check | Command (working dir) | Expected | Authorized effect | Result | Evidence |
|---|---|---|---|---|---|---|
| PF-3.1 | Runtime versions | `<<e.g. node --version; npm --version>>` | `<<…>>` | read-only | NOT RUN | |
| PF-3.2 | Dependency setup from lockfile (QA-controlled, never the Engineer's install) | `<<install command>>` | exit 0 | `<<authorized: Y/N>>` | NOT RUN | |
| PF-3.3 | External build prerequisites reachable | `<<…>>` | `<<…>>` | read-only | NOT RUN | |
| PF-3.4 | Free ports / resources | `<<…>>` | `<<…>>` | read-only | NOT RUN | |
| PF-3.5 | Evidence-lane permissions (`QAM/evidence/`, `QAM/AUTOMATION/`, `QAM/HANDOFFS/` writable; protected paths not) | `<<…>>` | writable / protected | QA lane only | NOT RUN | |

## Section 4 — Target, configuration, service readiness, roles, data (check 4)

| # | Check | How | Expected | Authorized effect | Result | Evidence |
|---|---|---|---|---|---|---|
| PF-4.1 | Actual resolved target (not a label): URL / project / database identity | `<<…>>` | `<<TARGET>>` per `QAM_ENTRY.md` §4 | read-only | NOT RUN | |
| PF-4.2 | Configuration precedence (env files, overrides) | `<<…>>` | documented | read-only | NOT RUN | |
| PF-4.3 | Service **ready for the required operation** (an HTTP status proves connectivity only) | `<<operation-level probe>>` | `<<…>>` | `<<…>>` | NOT RUN | |
| PF-4.4 | Role / account availability (by role name; existence verified by the Director) | `<<…>>` | roles `<<…>>` exist | `<<…>>` | NOT RUN | |
| PF-4.5 | Suitable test data present | `<<…>>` | `<<…>>` | read-only | NOT RUN | |
| PF-4.6 | Credential file declared, **ignored and untracked**, schema valid, no values echoed | `git check-ignore -v <<QA_CREDENTIAL_FILE>>`; `git ls-files --error-unmatch <<QA_CREDENTIAL_FILE>>` (expect failure); key-name schema check | ignored; untracked; keys `<<KEY_NAMES>>` present | read-only; no values printed | NOT RUN | |

## Section 5 — Browser, instrumentation, auth probes (check 5; only where relevant)

| # | Check | How | Expected | Authorized effect | Result | Evidence |
|---|---|---|---|---|---|---|
| PF-5.1 | Browser driver launches; basic interaction works | `<<…>>` | `<<…>>` | local only | NOT RUN | |
| PF-5.2 | Privacy instrumentation validated with a synthetic leak fixture **and** a clean control | `<<…>>` | fixture detected, control clean | local only | NOT RUN | |
| PF-5.3 | Permitted auth probe (bounded login/logout) | `<<…>>` | `<<…>>` | `<<authorized: Y/N; session/audit activity acknowledged>>` | NOT RUN | |

## Section 6 — Packaging and recovery (check 6)

| # | Check | How | Expected | Result | Evidence |
|---|---|---|---|---|---|
| PF-6.1 | Can produce a safe review package (`QAM_PACKAGING.md` dry run, exclusion list honored) | `<<…>>` | index + hashes verified | NOT RUN | |
| PF-6.2 | Can recover after interruption (state file readable; evidence lane durable) | read `QAM_STATE.md` | — | NOT RUN | |

## Outcome

| Field | Value |
|---|---|
| Blockers (GAP / QUESTION / BLOCKED rows with owner and exact resolution) | NOT RECORDED |
| Readiness for Q1 planning | NOT RECORDED |
| Rows to recheck at Q2 entry (changeable items) | `<<PF-1.x, PF-4.x, …>>` |

*NEWLY AUTHORED DRAFT — QA LEAD REVIEW REQUIRED.*
