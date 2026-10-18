# QAM_STATE — `<<MODULE_ID>>`

> NEWLY AUTHORED DRAFT — QA LEAD REVIEW REQUIRED. Template `QAM/QAM_STATE.md` v0.2-draft (2026-10-14), from `QAM_PLAYBOOK_v1_0.md` §15 (and §6, §13). **Owner: Architect creates; each seat appends dated entries for its own transitions.** A small index into authoritative records: it references authority and never grants it. Do not duplicate reports here. Immutable exports keep their historical statements; later entries supersede stale "pending" summaries with dated provenance. This file is read by the arriving agent; it is not a dispatcher.

## State vocabulary (the only values the Phase field may hold; dispatch in `QAM_ENTRY.md` §5)

`READY FOR ENGINEERING` → `ENGINEERING COMPLETE — AWAITING QA BRANCH` → `READY FOR RECON` → `Q1 COMPLETE — AWAITING QA LEAD REVIEW` → (`Q1 AMENDMENTS REQUESTED` → `Q1 AMENDED — AWAITING QA LEAD BINDING`) | `HOLD` → `APPROVED — NOT RELEASED` → `RELEASED FOR Q2` → `Q2 COMPLETE — AWAITING ADJUDICATION` → (conditional: `REPAIR RULED — AWAITING COMMIT` → `RETEST SCOPE APPROVED — NOT RELEASED` → `RELEASED FOR Q4` → `Q4 COMPLETE — AWAITING ADJUDICATION`) → `VERDICT ISSUED — CLEANUP PENDING` → `CLEANUP EXECUTED — AWAITING ACCEPTANCE` → `CLEANUP ACCEPTED — RELEASED TO CLOSEOUT` → `CLOSED`. `STOPPED (STOP-*)` may interrupt any phase and records its safe resume point.

## Current state (latest entry wins)

| Field | Value |
|---|---|
| Phase | `READY FOR ENGINEERING` ← set by the Architect at packaging. `READY FOR RECON` is recorded by the Director only after the engineering handoff is complete **and** `qa/<<MODULE_BRANCH>>` exists at the completed engineering candidate commit |
| Attempt | `<<n>>` (Q1 attempt / Q2 attempt / Q4 attempt counted separately) |
| Engineering branch / QA branch | `<<MODULE_BRANCH>>` / `qa/<<MODULE_BRANCH>>` (`NOT RECORDED` until the Director creates it) |
| Baseline | `<<BASELINE_SHA>>` |
| Candidate (tested product SHA) | `PENDING` |
| QA execution HEAD (branch HEAD when the shot ran) | `NOT RECORDED` |
| Evidence / closeout commit | `NOT RECORDED` |
| Contract identity (spec version/hash + accepted errata) | `<<…>>` |
| Plan identity (SHA-256 of the bound `QAM_TEST_PLAN.md`) | `NOT RECORDED` |
| Approval record | `NOT RECORDED` (→ `QAM_APPROVAL.md`) |
| Release reference (Director) | `NOT RECORDED` |
| Latest package (path, member count) | `NOT RECORDED` (→ `HANDOFFS/`) |
| Latest package SHA-256 (from the external receipt) | `NOT RECORDED` — see "Package snapshots" below |
| Active stop | none |
| Next owner | `<<SEAT>>` |
| Next permitted action | `<<ACTION, e.g. "Engineer: implement; complete manifest + handoff">>` |

Rule before any resumed instruction (§15): compare its prerequisites to disk and to the identities above. A cleanup or test that already completed is reported, not rerun. A stale instruction requiring obsolete bytes goes back to its owner. Docs-only identity changes need a scope check (from the complete diff); product changes need a new candidate and a retest decision. An unknown or inconsistent state is reported with the exact discrepancy and next owner; nobody guesses.

## Package snapshots (playbook §13; expected difference between archived and live state)

The copy of this file inside a review ZIP is the **immutable pre-export snapshot**: it was written before the ZIP existed, so it cannot contain the ZIP's own hash. The completed ZIP's SHA-256 is recorded **only** in the external receipt (`HANDOFFS/README.md` table, the return message) and in the **subsequent live entry** of this file. The ZIP is never rebuilt merely to embed its own hash. When reading an archived snapshot, the missing hash and the later live entry are the expected, provenance-recorded difference, not an inconsistency.

## Transition log (append-only; newest last)

The rows below show the expected shape of each transition and are **not prefilled events**. Delete the example rows that did not happen; never record a transition that did not occur.

| Date / time | Seat | From → To | Identity touched | Record / receipt |
|---|---|---|---|---|
| `<<YYYY-MM-DD HH:MM TZ>>` | Architect | — → `READY FOR ENGINEERING` | baseline `<<BASELINE_SHA>>` | QAM instantiated from template set `<<SET_VERSION>>` (governing QAM_PLAYBOOK `<<VERSION>>`) |
| | Engineer | `READY FOR ENGINEERING` → `ENGINEERING COMPLETE — AWAITING QA BRANCH` | candidate `PENDING`; handoff inventory recorded (manifest §2) | `QAM_MANIFEST.md`, `HANDOFFS/ENGINEERING_HANDOFF.md` |
| | Director | → `READY FOR RECON` | completed engineering candidate committed on `<<MODULE_BRANCH>>` as `<<…>>`; `qa/<<MODULE_BRANCH>>` created at that commit | Director receipt `<<…>>` |
| | QA Executor | `READY FOR RECON` → `Q1 COMPLETE — AWAITING QA LEAD REVIEW` | candidate resolved `<<…>>` and reconciled against the handoff; execution HEAD `<<…>>` | package `HANDOFFS/<<MODULE_ID>>_Q1_REVIEW_<<n>>.zip` (members `<<n>>`); SHA-256 recorded in the next live entry |
| | QA Executor | (live entry after export) | — | external receipt: Q1 package SHA-256 `<<…>>` |
| | QA Lead | → `APPROVED — NOT RELEASED` / `Q1 AMENDMENTS REQUESTED` / `HOLD` | plan SHA-256 `<<…>>` | `QAM_APPROVAL.md` §1–§2 |
| | Director | → `RELEASED FOR Q2` | release ref `<<…>>`; records committed `<<…>>` | `QAM_APPROVAL.md` §3 |
| | QA Executor | → `Q2 COMPLETE — AWAITING ADJUDICATION` | execution HEAD `<<…>>` | `HANDOFFS/<<MODULE_ID>>_Q2_REVIEW_<<n>>.zip`; SHA-256 in the next live entry |
| | QA Lead | → (conditional) `REPAIR RULED — AWAITING COMMIT` | ruling `<<ID>>` | `FINDINGS.md` §2/§3.2 |
| | Director | → `RETEST SCOPE APPROVED — NOT RELEASED` → `RELEASED FOR Q4` | repaired candidate `<<…>>`; Q4 scope approval + release | `QAM_APPROVAL.md` §4 |
| | QA Lead | → `VERDICT ISSUED — CLEANUP PENDING` | certified candidate `<<…>>` | `QAM_CERTIFICATION.md` §1–§3 |
| | QA Executor | → `CLEANUP EXECUTED — AWAITING ACCEPTANCE` | — | `QAM_CLEANUP_REPORT.md` |
| | QA Lead / Director | → `CLEANUP ACCEPTED — RELEASED TO CLOSEOUT` | durable records commit `<<…>>` | `QAM_CERTIFICATION.md` §4 |
| | Architect / Engineer / Director | → `CLOSED` | closeout commit `<<…>>`; merge of `qa/<<MODULE_BRANCH>>` into `main` `<<…>>` | closeout instruction / Director receipt |

*NEWLY AUTHORED DRAFT — QA LEAD REVIEW REQUIRED.*
