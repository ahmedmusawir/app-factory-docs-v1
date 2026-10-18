# FINDINGS — `<<MODULE_ID>>`

> NEWLY AUTHORED DRAFT — QA LEAD REVIEW REQUIRED. Template `QAM/FINDINGS.md` v0.1-draft (2026-10-14), from `QAM_PLAYBOOK_v1_0.md` §11 (findings, classification, repair protocol) and §5. **Owners: §1 QA Executor records findings and proposes a class; §2 QA Lead dispositions; §3 conditional repair routing — Executor proposes, QA Lead classifies, Architect rules scope, Engineer repairs on the QA branch, Director commits, Executor re-pins and retests.** A proposal here is never a work order.

## 1. Findings (QA Executor)

| ID | Phase / attempt | AC(s) | Observation (what was seen) | Expected (independently derived) | Reproduction (exact, with working dir) | Evidence path(s) | Proposed class | Proposed severity | Blocks other checks? |
|---|---|---|---|---|---|---|---|---|---|
| F-01 | | | | | | | `<<…>>` | `<<…>>` | |

Proposed class vocabulary (§11): acceptance failure · regression · environment/setup issue · instrument issue · contract gap · proven pre-existing defect · follow-up finding · enhancement · observation. Severity follows impact. A finding whose grading depends on an unresolved contract question is `ADJUDICATE` in the matrix and a `STOP-CONTRACT` if execution cannot continue safely.

Observations outside the plan ("while I'm here") are recorded here as **observation**, unranked, never widened into scope.

## 2. Dispositions (QA Lead only)

| Finding | Class (final) | Severity (final) | Disposition | Inherited condition evidence (if claimed pre-existing) | Affects verdict? | Routed to |
|---|---|---|---|---|---|---|
| F-01 | NOT RECORDED | | NOT RECORDED | | | |

Rules: inherited conditions require evidence; they are neither charged to a new module nor waived if release-blocking without the governing disposition. No accepted requirement silently becomes optional; meaningful risk acceptance follows Director authority and is recorded in `QAM_CERTIFICATION.md`.

## 3. Conditional repair routing (only when §2 dispositions a genuine product defect)

### 3.1 Repair proposal (QA Executor draft; a proposal, not a work order)

Created only when at least one product AC is FAIL with a product-defect disposition. No QA seat edits product code, tests, dependencies or contract files.

| Finding(s) | AC(s) | Evidence path(s) | Suggested allowed-file list (suggestion only) | Suggested retest scope (suggestion only) | Contract question, if any (spec row + ruling gap) |
|---|---|---|---|---|---|
| NOT RECORDED | | | | | |

### 3.2 Chain of authority (each step recorded with date and seat)

| Step | Seat | Record | Date |
|---|---|---|---|
| Disposition: product defect | QA Lead | §2 row | NOT RECORDED |
| Ruling / bounded repair instruction (exact allowed paths, forbidden paths, required checks) | Architect | `<<ruling ID in the parent's ruling lane>>` | NOT RECORDED |
| Repair on `qa/<<MODULE_BRANCH>>`, approved paths only; self-verification; amendment to `QAM_MANIFEST.md` §8 | Engineer | commit(s) `PENDING` | NOT RECORDED |
| Commit of the repair | Director | receipt `<<…>>` | NOT RECORDED |
| Re-pin repaired candidate; Q4 retest per `QAM_TEST_PLAN.md` §7 (repair diff + affected ACs + full required regression suite; carried-forward evidence with its original SHA/attempt; live validation reserved for the final repaired candidate runs on it) | QA Executor | `QAM_EXECUTION_REPORT.md` (Q4), new package | NOT RECORDED |
| Re-adjudication | QA Lead | §2 (appended rows) | NOT RECORDED |

Repairs stay on the QA branch; nothing is transferred back to the engineering branch (RUL-02). All prior attempts are preserved under `evidence/`.

*NEWLY AUTHORED DRAFT — QA LEAD REVIEW REQUIRED.*
