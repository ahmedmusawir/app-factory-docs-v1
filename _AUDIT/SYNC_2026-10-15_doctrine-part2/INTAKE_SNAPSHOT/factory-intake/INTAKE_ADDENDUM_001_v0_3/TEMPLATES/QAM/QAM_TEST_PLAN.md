# QAM_TEST_PLAN — `<<MODULE_ID>>`

> DRAFT v0.3 — QA LEAD ACCEPTED WITH EXACT AMENDMENTS (Fable, 2026-10-14); AMENDMENTS APPLIED AND ENGINEER-VERIFIED; ARCHITECT AMENDMENT VERIFICATION PENDING. Template `QAM/QAM_TEST_PLAN.md` v0.3-draft (2026-10-14), from `QAM_PLAYBOOK_v1_0.md` §8 (drafting), §9 (approval and exact amendments), §10 (execution order), §11 (retest scope), §12 (browser matrix). **Owner: QA Executor drafts independently in Q1; the QA Lead amends and approves.** The approval itself is recorded in `QAM_APPROVAL.md`, a separate file, so this plan's hash is not self-referential. Plan edits never modify the frozen contract (RUL-04).

| Field | Value |
|---|---|
| Plan status | `DRAFT (Q1)` → `AMENDED PER QA LEAD` → `BOUND` (SHA-256 recorded in `QAM_APPROVAL.md`) |
| Drafted by / at | `<<QA Executor seat>>` / `<<YYYY-MM-DD HH:MM TZ>>` |
| Inputs | contract `<<version/hash>>` + rulings `<<IDs>>`; `QAM_RISK_REQUIREMENTS.md` (standing `<<ver>>` + module section); source; `QAM_RECON_REPORT.md` attempt `<<n>>`; Engineer claims (`QAM_MANIFEST.md`, `HANDOFFS/ENGINEERING_HANDOFF.md`) |
| Candidate the plan binds to | `<<CANDIDATE_SHA>>` (from recon §1) |
| Target / environment identity | `<<…>>` |
| Amendment record | §8 (exact edits the QA Lead supplied; diff preserved) |

## 1. Scope and applicability

| AC | In scope | Test ID(s) | If not testable: applicability ruling needed from |
|---|---|---|---|
| `<<AC-nnn>>` | `<<Y/N>>` | `<<T-nn>>` | `<<Architect / Director>>` |

Every AC has a test or a separately authorized applicability ruling. Items that cannot yet be tested are listed in §6.

## 2. Tests (risk / dependency order)

| Test ID | AC(s) | Objective | Independently derived expected result (source of the reference) | Procedure (command · working dir / steps) | Negative control | Evidence to capture | Depends on | Human check? |
|---|---|---|---|---|---|---|---|---|
| T-01 | `<<…>>` | `<<…>>` | `<<value — derived from: spec / source / registry / own build>>` | `<<…>>` | `<<…>>` | `evidence/<<area>>/<<file>>` | — | `<<N / Y: what, when>>` |

## 3. Required board and regression scope

| Suite / check | Command (working dir) | Why required | Evidence |
|---|---|---|---|
| `<<type check / lint / unit / build>>` | `<<…>>` | `<<…>>` | `evidence/board/` |
| Regression suite `<<name>>` | `<<…>>` | `<<nearest regressions to the changed behavior>>` | `evidence/regression/` |

Fresh-build evidence comes from a QA-controlled build when a claim depends on compilation. Still-valid Q1 instrument evidence may be reused with provenance; setup is repeated when reproducibility, changed inputs or this plan require it.

## 4. Browser / API / data coverage matrix (if applicable)

| Role | Route / workflow | Data / filter state | Viewport | Theme | Checks (rendered behavior, effective theme, keyboard/focus, errors, loading/stale/rejection, access denial) | Test ID |
|---|---|---|---|---|---|---|
| `<<…>>` | `<<…>>` | `<<…>>` | `<<…>>` | `<<…>>` | `<<…>>` | `<<…>>` |

Reductions and why: `<<…>>`. Sign-in strategy: one in-memory authenticated context per role where safe; roles and tenants separated; actual sign-in counts recorded. Credential handling per `QAM_RISK_REQUIREMENTS.md` SR-5.

## 5. Stop conditions for execution

The `STOP-*` table in `QAM_PLAYBOOK` §11 applies. Module-specific triggers: `<<…>>`. An isolated product FAIL is recorded and unaffected checks continue unless a trigger here says otherwise.

## 6. Cannot yet be tested

| AC / area | Reason | Enabler | Owner |
|---|---|---|---|
| `<<…>>` | `<<…>>` | `<<…>>` | `<<…>>` |

## 7. Conditional Q4 retest scope (filled only if a repair is ruled; drafted by the Executor after the Director's repair commit exists, approved by the QA Lead in `QAM_APPROVAL.md` §4; executed only in state `RELEASED FOR Q4`)

| Repair ruling ID | Repair diff (paths) | Affected ACs | Full required regression suite | Carried-forward evidence (with original SHA / attempt) | Live validation reserved for the final candidate |
|---|---|---|---|---|---|
| NOT RECORDED | | | | | |

## 8. Amendments (QA Lead)

| # | Exact edit (before → after) | Supplied by / date | Applied by / date | Material? (material new tests or interpretation changes return to the QA Lead) |
|---|---|---|---|---|
| none | | | | |

*DRAFT v0.3 — QA LEAD ACCEPTED WITH EXACT AMENDMENTS (Fable, 2026-10-14); AMENDMENTS APPLIED AND ENGINEER-VERIFIED; ARCHITECT AMENDMENT VERIFICATION PENDING.*
