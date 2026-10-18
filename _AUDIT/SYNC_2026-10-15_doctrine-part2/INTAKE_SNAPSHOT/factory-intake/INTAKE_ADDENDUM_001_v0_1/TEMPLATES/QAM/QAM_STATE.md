# QAM_STATE — `<<MODULE_ID>>`

> NEWLY AUTHORED DRAFT — QA LEAD REVIEW REQUIRED. Template `QAM/QAM_STATE.md` v0.1-draft (2026-10-14), from `QAM_PLAYBOOK_v1_0.md` §15 (and §6). **Owner: Architect creates; each seat appends dated entries for its own transitions.** A small index into authoritative records: it references authority and never grants it. Do not duplicate reports here. Immutable exports keep their historical statements; later entries supersede stale "pending" summaries with dated provenance.

## Current state (latest entry wins)

| Field | Value |
|---|---|
| Phase | `READY FOR RECON` ← set by the Architect at packaging; vocabulary in `QAM_ENTRY.md` §5 |
| Attempt | `<<n>>` (Q1 attempt / Q2 attempt / Q4 attempt counted separately) |
| Engineering branch / QA branch | `<<MODULE_BRANCH>>` / `qa/<<MODULE_BRANCH>>` |
| Baseline | `<<BASELINE_SHA>>` |
| Candidate (tested product SHA) | `PENDING` |
| QA execution HEAD (branch HEAD when the shot ran) | `NOT RECORDED` |
| Evidence / closeout commit | `NOT RECORDED` |
| Contract identity (spec version/hash + accepted errata) | `<<…>>` |
| Plan identity (SHA-256 of the bound `QAM_TEST_PLAN.md`) | `NOT RECORDED` |
| Approval record | `NOT RECORDED` (→ `QAM_APPROVAL.md`) |
| Release reference (Director) | `NOT RECORDED` |
| Latest package / external receipt | `NOT RECORDED` (→ `HANDOFFS/`) |
| Active stop | none |
| Next owner | `<<SEAT>>` |
| Next permitted action | `<<ACTION, e.g. "QA Executor: Q1 within declared scope">>` |

Rule before any resumed instruction (§15): compare its prerequisites to disk and to the identities above. A cleanup or test that already completed is reported, not rerun. A stale instruction requiring obsolete bytes goes back to its owner. Docs-only identity changes need a scope check; product changes need a new candidate and a retest decision.

## Transition log (append-only; newest last)

| Date / time | Seat | From → To | Identity touched | Record / receipt |
|---|---|---|---|---|
| `<<YYYY-MM-DD HH:MM TZ>>` | Architect | — → READY FOR ENGINEERING | baseline `<<BASELINE_SHA>>` | QAM instantiated from template set `<<SET_VERSION>>` |
| | Engineer | READY FOR ENGINEERING → ENGINEERING COMPLETE — MANIFEST + HANDOFF RECORDED | candidate `PENDING` | `QAM_MANIFEST.md`, `HANDOFFS/ENGINEERING_HANDOFF.md` |
| | Director | → READY FOR RECON | commit `<<…>>` on `<<MODULE_BRANCH>>`; `qa/<<MODULE_BRANCH>>` created at the same commit | Director receipt `<<…>>` |
| | QA Executor | READY FOR RECON → Q1 COMPLETE — AWAITING QA LEAD REVIEW | candidate resolved `<<…>>`; execution HEAD `<<…>>` | `HANDOFFS/<<MODULE_ID>>_Q1_REVIEW_<<n>>.zip` SHA-256 `<<…>>` |
| | QA Lead | → APPROVED — NOT RELEASED / HOLD | plan SHA-256 `<<…>>` | `QAM_APPROVAL.md` |
| | Director | → RELEASED FOR Q2 | release ref `<<…>>` | `QAM_APPROVAL.md` §3 |
| | QA Executor | → Q2 COMPLETE — AWAITING ADJUDICATION | execution HEAD `<<…>>` | `HANDOFFS/<<MODULE_ID>>_Q2_REVIEW_<<n>>.zip` |
| | QA Lead | → (conditional) REPAIR RULED / CLEANUP APPROVED | — | `FINDINGS.md` dispositions |
| | QA Lead | → CERTIFIED | certified candidate `<<…>>` | `QAM_CERTIFICATION.md` |
| | Architect / Engineer / Director | → CLOSED | closeout commit `<<…>>`; merge of `qa/<<MODULE_BRANCH>>` into `main` `<<…>>` | closeout instruction / Director receipt |

Rows above are the expected shape, not prefilled events. Delete the example rows that did not happen; never record a transition that did not occur.

*NEWLY AUTHORED DRAFT — QA LEAD REVIEW REQUIRED.*
