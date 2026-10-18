# QAM_APPROVAL — `<<MODULE_ID>>` (QA Lead decisions and Director releases)

> NEWLY AUTHORED DRAFT — QA LEAD REVIEW REQUIRED. Template `QAM/QAM_APPROVAL.md` v0.2-draft (2026-10-14), from `QAM_PLAYBOOK_v1_0.md` §9 and §13. **Owners: §1, §2 and the QA Lead columns of §4 — QA Lead only (the decision); §3 and the Director columns of §4 — Director (release references).** Kept separate from the plan so the plan's hash is not self-referential. **Ownership vs transcription:** the decision belongs to the QA Lead and the release to the Director. The QA Executor may **transcribe** the exact supplied text into this file only when expressly instructed to, attributing it (author, source, date) — it never composes, infers or reconstructs a decision or release. **An empty decision means no approval exists.**

## 1. QA Lead review of the Q1 package

| Field | Value |
|---|---|
| Q1 package reviewed (path, SHA-256 from the external receipt, member count) | NOT RECORDED |
| Reviewed the actual package, not only the Executor's summary | NOT RECORDED |
| Decision | NOT RECORDED — one of `APPROVED` · `APPROVED WITH EXACT AMENDMENTS` · `HOLD (blockers listed)` |
| Blockers (if HOLD; each with owner and required resolution) | |
| Exact amendments (if any; each is an exact edit the Executor applies verbatim and records as a diff in `QAM_TEST_PLAN.md` §8) | |
| Q1b bookkeeping | `<<no amendments needed → proceed to release / amendments applied by the Executor; finalized plan re-bound in §2>>` |
| Decision source (QA Lead seat, runtime, date, time zone) | NOT RECORDED |
| Transcribed by (only if the QA Lead's exact text was transcribed on instruction) and source of the text | n/a |

## 2. Binding (what exactly is approved)

| Field | Value |
|---|---|
| Product candidate (full SHA) | NOT RECORDED |
| Plan identity: `QAM_TEST_PLAN.md` SHA-256 after amendments | NOT RECORDED |
| Contract identity (spec version/hash) and rulings in force | NOT RECORDED |
| Environment / target identity | NOT RECORDED |
| Limitations accepted at approval | NOT RECORDED |
| Required release conditions (what the Director must do before Q2) | NOT RECORDED |

A new product/config/test change after this binding invalidates it and requires QA Lead review of the changed scope. A documentation-only successor is proved by reviewing the **complete** candidate→HEAD diff (file contents, not a `--stat` summary), never assumed from a commit message. Tested product SHA, QA execution HEAD and evidence/closeout commit are recorded as three different identities.

## 3. Director release (Q2)

| Field | Value |
|---|---|
| Records committed (which files, commit SHA on `qa/<<MODULE_BRANCH>>`) | NOT RECORDED |
| Release statement (Q2 released for candidate `<<…>>` under plan `<<SHA-256>>`) | NOT RECORDED |
| Credential file created (`<<QA_CREDENTIAL_FILE>>`; keys by name only) | NOT RECORDED |
| Release source (Director, date, time zone) | NOT RECORDED |

## 4. Later decisions in the same engagement (append-only; Q4 retest scope, repaired candidates)

| Date | QA Lead decision (retest scope approved; plan §7 SHA-256) | Repaired candidate (full SHA, from the Director's commit receipt) | Director release for Q4 (reference, date) | Recorded by (seat; "transcribed" if applicable) |
|---|---|---|---|---|
| | NOT RECORDED | | NOT RECORDED | |

`RELEASED FOR Q4` requires all three: the repaired candidate identity, the QA Lead's retest-scope approval and the Director's release (`QAM_ENTRY.md` §5).

*NEWLY AUTHORED DRAFT — QA LEAD REVIEW REQUIRED.*
