# QAM_CERTIFICATION — `<<MODULE_ID>>` (QA Lead verdict)

> TEMPLATE SET v0.3 — QA LEAD ACCEPTED WITH EXACT AMENDMENTS (Fable, 2026-10-14); AMENDMENTS ARCHITECT-VERIFIED; INSTALLATION REQUIRES THE APPROVED DOCSET SYNC. Template `QAM/QAM_CERTIFICATION.md` v0.3-draft (2026-10-14), from `QAM_PLAYBOOK_v1_0.md` §14 and §13 ("Include exact certification/approval text when someone is instructed to transcribe it. No reconstructing a missing letter from another seat's summary"). **Owner: QA Lead only.** **Ownership vs transcription:** the verdict is the QA Lead's; an expressly instructed, attributed transcription of the QA Lead's exact text is allowed; a composed, inferred or reconstructed verdict is not. **An empty verdict means no certificate exists.** The Engineer never writes this file; the QA Executor writes it only as such a transcription.
>
> **Sequence (RUL-03; playbook §14):** adjudication → **§1–§3 product verdict** (issued on the adjudicated evidence; it does not depend on cleanup) → required cleanup (`QAM_CLEANUP_REPORT.md`) → cleanup acceptance and durable records committed → **§4 release to Architect closeout** (appended afterwards). Gate Q, cleanup acceptance and Gate D stay separate claims.

| Field | Value |
|---|---|
| Issued by (QA Lead seat, runtime) | NOT RECORDED |
| Date / time zone | NOT RECORDED |
| Transcribed by (only if transcribed on instruction) and source of the exact text | n/a |

## 1. Verdict (product; issued after adjudication, before cleanup)

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
| Product Gate Q (this verdict, §1) | see §1 |
| Required cleanup accepted (`QAM_CLEANUP_REPORT.md`) | NOT RECORDED — recorded in §4 after cleanup |
| Pilot / process evaluation (only if this module was an experiment) | n/a unless declared |
| Gate D (deployed-system verification; separately scoped and authorized) | not covered by this certificate |
| Review completion (RRM checkpoints) | not covered by this certificate |

## 4. Cleanup acceptance and release to Architect closeout (appended after cleanup; QA Lead)

| Condition | Met? | Evidence |
|---|---|---|
| Accepted product verdict (§1) | NOT RECORDED | |
| Required cleanup executed under QA Lead authority and **accepted** (`QAM_CLEANUP_REPORT.md` §4) | NOT RECORDED | |
| Durable records committed (Director; commit SHA) | NOT RECORDED | |
| Governed clean-tree condition | NOT RECORDED | |
| Released to Architect closeout (yes/no, date, QA Lead) | NOT RECORDED | |

After release: the Architect directs bounded Engineer closeout; the Director commits, merges `qa/<<MODULE_BRANCH>>` into `main` and pushes. A documentation-only successor is verified by reviewing the complete diff before the recorded identity is extended. This certificate does not certify a deployed revision.

*TEMPLATE SET v0.3 — QA LEAD ACCEPTED WITH EXACT AMENDMENTS (Fable, 2026-10-14); AMENDMENTS ARCHITECT-VERIFIED; INSTALLATION REQUIRES THE APPROVED DOCSET SYNC.*
