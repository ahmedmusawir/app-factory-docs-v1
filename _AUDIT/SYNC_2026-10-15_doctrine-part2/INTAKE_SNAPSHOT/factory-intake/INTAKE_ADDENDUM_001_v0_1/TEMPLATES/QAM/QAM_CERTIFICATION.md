# QAM_CERTIFICATION — `<<MODULE_ID>>` (QA Lead verdict)

> NEWLY AUTHORED DRAFT — QA LEAD REVIEW REQUIRED. Template `QAM/QAM_CERTIFICATION.md` v0.1-draft (2026-10-14), from `QAM_PLAYBOOK_v1_0.md` §14 and §13 ("Include exact certification/approval text when someone is instructed to transcribe it. No reconstructing a missing letter from another seat's summary"). **Owner: QA Lead only.** An attributed transcription of the QA Lead's exact text is allowed; a reconstruction is not. **An empty verdict means no certificate exists.** The QA Executor and the Engineer never write this file.

| Field | Value |
|---|---|
| Issued by (QA Lead seat, runtime) | NOT RECORDED |
| Date / time zone | NOT RECORDED |
| Transcribed by (if not written directly by the QA Lead) and source of the exact text | NOT RECORDED |

## 1. Verdict

| Field | Value |
|---|---|
| **Verdict** | NOT RECORDED — one of `PASS` · `PASS WITH FOLLOW-UP FINDINGS` · `PASS WITH KNOWN RISK` · `FAIL` · `BLOCKED` |
| Scope certified | NOT RECORDED |
| Certified candidate (full SHA) | NOT RECORDED |
| QA execution HEAD(s) | NOT RECORDED |
| Contract identity and accepted errata / rulings | NOT RECORDED |
| Approved plan (SHA-256) and approval record | NOT RECORDED (`QAM_APPROVAL.md`) |
| Limitations | NOT RECORDED |

## 2. Basis

| AC group / AC | Independent result (matrix) | Finding IDs and dispositions | Evidence / specimen | Limitation or ruling |
|---|---|---|---|---|
| `<<…>>` | NOT RECORDED | | | |

Evidence adequacy and rationale for the verdict: NEEDS AUTHORING (QA Lead).
Follow-up findings carried (if `PASS WITH FOLLOW-UP FINDINGS`): NOT RECORDED.
Known risk accepted (if `PASS WITH KNOWN RISK`): NOT RECORDED — Director authority reference: NOT RECORDED. No accepted requirement silently becomes optional.

## 3. Separate claims (each stated on its own; none implied by another)

| Claim | Status |
|---|---|
| Product Gate Q (this verdict) | see §1 |
| Required cleanup accepted (`QAM_CLEANUP_REPORT.md`) | NOT RECORDED |
| Pilot / process evaluation (only if this module was an experiment) | n/a unless declared |
| Gate D (deployed-system verification; separately scoped and authorized) | not covered by this certificate |
| Review completion (RRM checkpoints) | not covered by this certificate |

## 4. Release to Architect closeout

| Condition | Met? | Evidence |
|---|---|---|
| Accepted product verdict | NOT RECORDED | |
| Required cleanup complete under QA Lead authority | NOT RECORDED | |
| Durable records committed (Director) | NOT RECORDED | |
| Governed clean-tree condition | NOT RECORDED | |
| Released to Architect closeout (yes/no, date) | NOT RECORDED | |

After release: the Architect directs bounded Engineer closeout; the Director commits, merges `qa/<<MODULE_BRANCH>>` into `main` and pushes. A documentation-only successor is verified from the diff before the recorded identity is extended. This certificate does not certify a deployed revision.

*NEWLY AUTHORED DRAFT — QA LEAD REVIEW REQUIRED.*
