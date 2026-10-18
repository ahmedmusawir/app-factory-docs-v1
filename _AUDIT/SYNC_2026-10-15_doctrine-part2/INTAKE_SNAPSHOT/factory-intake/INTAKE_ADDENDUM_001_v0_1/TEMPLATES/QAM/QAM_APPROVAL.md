# QAM_APPROVAL — `<<MODULE_ID>>` (QA Lead decision and Director release)

> NEWLY AUTHORED DRAFT — QA LEAD REVIEW REQUIRED. Template `QAM/QAM_APPROVAL.md` v0.1-draft (2026-10-14), from `QAM_PLAYBOOK_v1_0.md` §9. **Owners: §1–§2 QA Lead only; §3 Director release references.** Kept separate from the plan so the plan's hash is not self-referential. No field here is prefilled: an empty decision means **no approval exists**. The QA Executor never writes this file.

## 1. QA Lead review of the Q1 package

| Field | Value |
|---|---|
| Q1 package reviewed (path, SHA-256, member count) | NOT RECORDED |
| Reviewed the actual package, not only the Executor's summary | NOT RECORDED |
| Decision | NOT RECORDED — one of `APPROVED` · `APPROVED WITH EXACT AMENDMENTS` · `HOLD (blockers listed)` |
| Blockers (if HOLD) | |
| Exact amendments (if any; each is an exact edit, preserved as a diff in `QAM_TEST_PLAN.md` §8) | |
| Q1b bookkeeping | `<<no amendments needed → proceed to release / amendments applied by the Executor and the finalized plan re-bound below>>` |
| Approval source (seat, runtime, date, time zone) | NOT RECORDED |

## 2. Binding (what exactly is approved)

| Field | Value |
|---|---|
| Product candidate (full SHA) | NOT RECORDED |
| Plan identity: `QAM_TEST_PLAN.md` SHA-256 after amendments | NOT RECORDED |
| Contract identity (spec version/hash) and rulings in force | NOT RECORDED |
| Environment / target identity | NOT RECORDED |
| Limitations accepted at approval | NOT RECORDED |
| Required release conditions (what the Director must do before Q2) | NOT RECORDED |

A new product/config/test change after this binding invalidates it and requires QA Lead review of the changed scope. A documentation-only successor is proved from the complete diff, not assumed from a commit message. Tested product SHA, QA execution HEAD and evidence/closeout commit are recorded as three different identities.

## 3. Director release

| Field | Value |
|---|---|
| Records committed (which files, commit SHA on `qa/<<MODULE_BRANCH>>`) | NOT RECORDED |
| Release statement (Q2 released for candidate `<<…>>` under plan `<<SHA-256>>`) | NOT RECORDED |
| Credential file created (`<<QA_CREDENTIAL_FILE>>`; keys by name only) | NOT RECORDED |
| Release source (Director, date, time zone) | NOT RECORDED |

## 4. Later approvals in the same engagement (append-only)

| Date | QA Lead decision | Scope (e.g. Q4 retest plan §7, repaired candidate) | Candidate | Plan SHA-256 | Director release |
|---|---|---|---|---|---|
| | | | | | |

*NEWLY AUTHORED DRAFT — QA LEAD REVIEW REQUIRED.*
