# QAM_CLEANUP_REPORT — `<<MODULE_ID>>` (required closure operation)

> NEWLY AUTHORED DRAFT — QA LEAD REVIEW REQUIRED. Template `QAM/QAM_CLEANUP_REPORT.md` v0.2-draft (2026-10-14), from `QAM_PLAYBOOK_v1_0.md` §14 (preserved in full by RUL-03) and §12. **Owners: QA Lead records the cleanup point (§0), the retention decisions (§3, Decision column) and the acceptance (§4); the QA Executor executes under that recorded authority and records §1, §2 and the Executed?/Evidence columns.** Cleanup is a closure operation, not another planning or testing campaign. It is **required**; retention is never "keep everything". Only cleanup steps tied to abandoning the QA branch or transferring work back to the engineering branch do not exist here (RUL-02/RUL-03).
>
> **Sequence:** accepted product verdict (`QAM_CERTIFICATION.md` §1–§3, issued first and independent of cleanup) → required cleanup (this file) → cleanup acceptance (§4) and durable records committed by the Director → release to Architect closeout (`QAM_CERTIFICATION.md` §4).

## 0. Authority for this cleanup (QA Lead)

| Field | Value |
|---|---|
| Product verdict issued (reference to `QAM_CERTIFICATION.md` §1; verdict text is not repeated here) | NOT RECORDED |
| Cleanup point approved by / at | NOT RECORDED |
| Applicable cleanup policy (governing bodies; local rule names) | `<<QAM_PLAYBOOK §14; project policy …>>` |
| Director-reported items (e.g. password rotation) — recorded as reported, not evidenced | NOT RECORDED |

## 1. Routine phase-exit hygiene (preauthorized; done at each phase exit; Executor)

| Item | Done at Q1 exit | Done at Q2 exit | Evidence |
|---|---|---|---|
| Owned browsers closed | NOT RECORDED | NOT RECORDED | |
| Owned QA servers / processes stopped | NOT RECORDED | NOT RECORDED | |
| Declared transient auth state removed | NOT RECORDED | NOT RECORDED | |

## 2. Credential and auth-state cleanup (Executor; sequence matters; record the actual order)

| Step | Action | Result | Evidence |
|---|---|---|---|
| 1 | Value scan of retained outputs **while the credential source still exists** (scanner validated with a synthetic fixture and a clean control) | NOT RUN | |
| 2 | Resolve / quarantine actual leaks without publishing them (safe counts and locations only) | NOT RUN | |
| 3 | Delete `<<QA_CREDENTIAL_FILE>>` and owned auth state under the declared authority | NOT RUN | |
| 4 | Verify removal (already absent = verified absent, not newly deleted) | NOT RUN | |
| 5 | Pattern-scan retained outputs and the final export | NOT RUN | |

Do not preserve credential values or their hashes as evidence. After deletion, do not claim a new value scan happened; record the actual sequence and the earlier source hashes of the scan reports.

## 3. Retention decision (QA Lead) and execution (Executor)

| Item | Decision (KEEP / REMOVE / QUARANTINE) — QA Lead | Reason — QA Lead | Executed? — Executor | Evidence — Executor |
|---|---|---|---|---|
| Durable evidence package sufficient for certification, reproduction and audit (paths) | NOT RECORDED | | | |
| Failed attempts (preserved when justified) | NOT RECORDED | | | |
| Useful helpers under `AUTOMATION/` | NOT RECORDED | | | |
| Disposable generated debris (builds, dependencies, caches, raw traces, browser profiles, disposable mirrors) | NOT RECORDED | | | |
| Unrelated processes / active editor recovery files (not automatically deleted) | not touched | | | |
| Protected recovery/session files (require their own authority) | not touched | | | |

## 4. Final state and cleanup acceptance

| Field | Value | Owner |
|---|---|---|
| Product / tests / contract unchanged during cleanup (evidence: diff) | NOT RECORDED | Executor |
| Working tree after cleanup (`git status --porcelain`) | NOT RECORDED | Executor |
| Cleanup **accepted** (date, QA Lead) | NOT RECORDED | QA Lead |
| Durable records committed (Director; commit SHA) | NOT RECORDED | Director |
| Released to Architect closeout (recorded in `QAM_CERTIFICATION.md` §4) | NOT RECORDED | QA Lead |

*NEWLY AUTHORED DRAFT — QA LEAD REVIEW REQUIRED.*
