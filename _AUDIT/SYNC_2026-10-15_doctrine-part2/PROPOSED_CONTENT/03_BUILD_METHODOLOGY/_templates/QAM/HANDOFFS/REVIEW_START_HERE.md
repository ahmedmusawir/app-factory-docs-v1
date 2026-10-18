# REVIEW_START_HERE — `<<MODULE_ID>>` `<<PHASE>>` review package, attempt `<<ATTEMPT>>`

> TEMPLATE SET v0.3 — QA LEAD ACCEPTED WITH EXACT AMENDMENTS (Fable, 2026-10-14); AMENDMENTS ARCHITECT-VERIFIED; INSTALLATION REQUIRES THE APPROVED DOCSET SYNC. Template `QAM/HANDOFFS/REVIEW_START_HERE.md` v0.3-draft (2026-10-14), from `QAM_PLAYBOOK_v1_0.md` §13. **Owner: QA Executor**, one copy per package (filled at packaging time; the template stays in `HANDOFFS/` unfilled). The first file a reviewer opens.

| Field | Value |
|---|---|
| Package | `<<MODULE_ID>>_<<PHASE>>_REVIEW_<<ATTEMPT>>.zip` — members `<<n>>` — SHA-256 recorded **outside** this package (external receipt in `HANDOFFS/README.md`, the return message, and the live `QAM_STATE.md` entry written after export). The `QAM_STATE.md` in this package is the immutable pre-export snapshot; its missing package hash is expected. |
| Produced by / at | `<<QA Executor seat / runtime>>` / `<<YYYY-MM-DD HH:MM TZ>>` |
| Reviewer and decision requested | `<<QA Lead: approve / amend / hold the plan>>` · `<<QA Lead: adjudicate findings>>` · `<<Director: resolve STOP-…>>` |
| Identities | candidate `<<…>>` · QA execution HEAD `<<…>>` · contract `<<…>>` · plan SHA-256 `<<…>>` · approval `<<…>>` · release `<<…>>` |
| Current state (`QAM_STATE.md`) | `<<…>>` |
| Active stop (if any) | `<<STOP-… / none>>` |

## Read in this order

1. `QAM_STATE.md` — where the engagement is.
2. `<<phase report: QAM_RECON_REPORT.md / QAM_EXECUTION_REPORT.md>>`
3. `<<QAM_TEST_PLAN.md (draft or bound)>>`, `<<QAM_APPROVAL.md if present>>`
4. `<<AC_EVIDENCE_MATRIX.md, FINDINGS.md (Q2/Q4)>>`
5. Contract and rulings, `GOVERNING/README.md`, Engineer manifest and handoff (claims).
6. `evidence/` as cited from the reports; `FILE_INDEX.json` for every member's purpose and hash.

## Summary (facts; no verdict)

`<<three to six lines: what was done, totals by label, stops, Director touches, what is untested>>`

## Not included (listed honestly)

| Item | Why | Where it is instead |
|---|---|---|
| `<<…>>` | `<<privacy / size / not produced>>` | `<<path or "not produced">>` |

*TEMPLATE SET v0.3 — QA LEAD ACCEPTED WITH EXACT AMENDMENTS (Fable, 2026-10-14); AMENDMENTS ARCHITECT-VERIFIED; INSTALLATION REQUIRES THE APPROVED DOCSET SYNC.*
