# QAM_RECON_REPORT — `<<MODULE_ID>>` (Q1, attempt `<<n>>`)

> TEMPLATE SET v0.3 — QA LEAD ACCEPTED WITH EXACT AMENDMENTS (Fable, 2026-10-14); AMENDMENTS ARCHITECT-VERIFIED; INSTALLATION REQUIRES THE APPROVED DOCSET SYNC. Template `QAM/QAM_RECON_REPORT.md` v0.3-draft (2026-10-14), from `QAM_PLAYBOOK_v1_0.md` §8. **Owner: QA Executor.** Independent Q1 observations, contradictions and readiness. Q1 is not the full QA campaign and produces no verdict. A successful login during recon does not satisfy the later acceptance walk.

**Executor:** `<<seat / runtime>>` · **Start:** `<<YYYY-MM-DD HH:MM TZ>>` · **End:** `<<…>>` · **Working directory:** `<<…>>` · **Preflight results:** `evidence/preflight/<<attempt>>/`

## 1. Identity resolved independently

| Field | Value | Evidence |
|---|---|---|
| Repository / branch | `<<…>>` / `qa/<<MODULE_BRANCH>>` | `<<path>>` |
| Full HEAD at recon | NOT RECORDED | |
| Baseline | `<<BASELINE_SHA>>` | |
| Candidate (the Director's committed candidate, from the receipt / read-only Git evidence; `qa/<<MODULE_BRANCH>>` created at it) | NOT RECORDED | |
| Candidate → HEAD classification, from review of the **complete** diff (`git diff <<CANDIDATE>>..HEAD`, not `--stat`) | NOT RECORDED (docs-only successor / product change → `STOP-IDENTITY`) | |
| Committed candidate reconciled against the handoff inventory (manifest §2: committed, staged, unstaged, untracked at handoff) | NOT RECORDED (every difference listed as a GAP in §4) | |
| Tracked / untracked state | NOT RECORDED | |

## 2. Contract, scope and governing versions as read

| Item | Identity read | Notes |
|---|---|---|
| Frozen acceptance spec | `<<version / hash>>` | AC count `<<n>>` |
| Ruling / erratum lane entries in force | `<<IDs>>` | pre-ruled exceptions: `<<…>>` |
| Protected paths | `<<…>>` | |
| Governing bodies (from `GOVERNING/README.md`) | `<<…>>` | all resolved? `<<Y / GAP>>` |
| Engineer handoff completeness | `<<complete / gaps listed in §4>>` | |

## 3. Readiness results (summary of `QAM_PREFLIGHT.md`)

| Section | Rows | Passed | Failed | Not run | Blocking? |
|---|---|---|---|---|---|
| 1 Repository / identity | | NOT RECORDED | | | |
| 2 Contract / handoff | | | | | |
| 3 Runtime / tools | | | | | |
| 4 Target / data / roles | | | | | |
| 5 Browser / instruments / auth | | | | | |
| 6 Packaging / recovery | | | | | |

Distinguish "endpoint reachable" from "service ready for the required operation" in every row that touches a service.

## 4. Unresolved details, contradictions and challenged claims

| # | Type (GAP / QUESTION / BLOCKED / CONTRADICTION) | Detail | Sources in conflict | Owner | Exact resolution needed | Blocks |
|---|---|---|---|---|---|---|
| R-1 | `<<…>>` | `<<…>>` | `<<e.g. manifest §3 vs spec AC-nnn>>` | `<<seat>>` | `<<…>>` | `<<Q1 planning / Q2 / nothing>>` |

Engineer claims challenged (claim → what recon observed → consequence for the plan): `<<…>>`

## 5. Stops raised in Q1

| Stop ID | Phase / time | Identity | Affected checks | Evidence | Owner | Required resolution | Safe resume point |
|---|---|---|---|---|---|---|---|
| none | | | | | | | |

## 6. What cannot yet be tested, and why

| AC / area | Reason | What would enable it | Owner |
|---|---|---|---|
| `<<…>>` | `<<…>>` | `<<…>>` | `<<…>>` |

## 7. Readiness statement and decision requested

Readiness for Q2 planning approval: NOT RECORDED (`READY — plan drafted` / `READY WITH GAPS` / `BLOCKED`).
Decision requested from the QA Lead: review `QAM_TEST_PLAN.md` (draft, SHA-256 `<<…>>`) and the Q1 package `HANDOFFS/<<MODULE_ID>>_Q1_REVIEW_<<n>>.zip`; approve, approve with exact amendments, or hold with specific blockers.

*TEMPLATE SET v0.3 — QA LEAD ACCEPTED WITH EXACT AMENDMENTS (Fable, 2026-10-14); AMENDMENTS ARCHITECT-VERIFIED; INSTALLATION REQUIRES THE APPROVED DOCSET SYNC.*
