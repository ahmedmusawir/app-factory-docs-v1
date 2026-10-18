# AC_EVIDENCE_MATRIX — `<<MODULE_ID>>` (QA Executor; attempt `<<n>>`)

> NEWLY AUTHORED DRAFT — QA LEAD REVIEW REQUIRED. Template `QAM/AC_EVIDENCE_MATRIX.md` v0.1-draft (2026-10-14), from `QAM_PLAYBOOK_v1_0.md` §10–§11. **Owner: QA Executor** (per-AC evidence). The QA Lead's adjudication is recorded in `FINDINGS.md` and the verdict in `QAM_CERTIFICATION.md`, never here.

**Executor:** `<<seat / runtime>>` · **Recorded at:** `<<YYYY-MM-DD HH:MM TZ>>` · **Candidate:** `<<CANDIDATE_SHA>>` · **QA execution HEAD:** `<<…>>` · **Executor platform:** `<<…>>` · **Plan SHA-256:** `<<…>>`

Status vocabulary (observations, not release decisions): **PASS** (independently proven, literal AC) · **FAIL** (demonstrated miss) · **BLOCKED** (prerequisite unavailable; name it) · **NOT RUN** (not attempted; say why) · **ADJUDICATE** (contract question for the QA Lead; cite the row). Every PASS or FAIL cites an evidence path. An unresolved discrepancy never becomes PASS by relabeling.

## Product acceptance criteria (Gate Q input)

| AC | Test ID(s) | Status | Evidence path(s) | Independently derived reference | Note / limitation |
|---|---|---|---|---|---|
| `<<AC-nnn>>` | `<<T-nn>>` | NOT RUN | | | |

One row per AC in the frozen contract, including ACs covered by an applicability ruling (status per the ruling, citing it).

## Carried-forward evidence (only where applicability is demonstrated)

| AC | Original attempt / SHA | Why still applicable | Evidence path |
|---|---|---|---|
| none | | | |

## Totals

| PASS | FAIL | BLOCKED | NOT RUN | ADJUDICATE | Total ACs |
|---|---|---|---|---|---|
| NOT RECORDED | | | | | `<<n>>` |

*NEWLY AUTHORED DRAFT — QA LEAD REVIEW REQUIRED.*
