# evidence/ — durable measurements and attempt history

> DRAFT v0.3 — QA LEAD ACCEPTED WITH EXACT AMENDMENTS (Fable, 2026-10-14); AMENDMENTS APPLIED AND ENGINEER-VERIFIED; ARCHITECT AMENDMENT VERIFICATION PENDING. Template `QAM/evidence/README.md` v0.3-draft (2026-10-14), from `QAM_PLAYBOOK_v1_0.md` §5, §10, §12, §14. **Owner: QA Executor** (writes); the Architect declares the lane and the expected evidence outputs at packaging; the QA Lead decides retention at cleanup.

## Layout (attempt-scoped; prior attempts are never overwritten)

```
evidence/
├── preflight/<attempt>/        PREFLIGHT_RESULTS.txt and raw outputs per row
├── identity/<attempt>/         HEAD, status, ancestry, change inventory reconciliation, complete candidate→HEAD diff
├── board/<attempt>/            QA-controlled builds, type checks, lint, unit/integration runs
├── <area>/<attempt>/           per-test evidence as named in the plan's "Evidence to capture" column
├── browser/<attempt>/          readiness, per-role matrices, cropped screenshots, sanitized traces, sign-in counts
├── regression/<attempt>/
├── privacy/<attempt>/          scanner validation (fixture + control) and scan reports (counts/locations only)
└── INVENTORY.md                the table below, kept current
```

## Rules

- Every PASS or FAIL in the matrix cites a path here with the command, its working directory, exit code and unfiltered output (or a cropped screenshot / sanitized trace for the browser). "Verified" without a path is NOT RUN.
- Raw authenticated traces can contain sensitive state even after login: retain only approved sanitized evidence. Image bodies: keep a short hex prefix, not the body, unless the plan requires it.
- **Write scope.** Measurement files go only here, in `AUTOMATION/` and `HANDOFFS/`. The Executor's report updates go to the Executor-owned files and Executor-recorded cells listed in `QAM_ENTRY.md` §3 (recon report, execution report, matrix, findings records, preflight result cells, risk observations, exact plan amendments, state entries, package records). Never to product, tests, contract files, `QAM_MANIFEST.md` or the Engineer's evidence.
- Carried-forward evidence from an earlier attempt is referenced with its original SHA and attempt, never silently reused.

## Inventory

| Path | Attempt | Test ID / AC | What it shows | Produced by (command / helper) | Sanitized? | Retention (QA Lead) |
|---|---|---|---|---|---|---|
| none yet | | | | | | NOT RECORDED |

*DRAFT v0.3 — QA LEAD ACCEPTED WITH EXACT AMENDMENTS (Fable, 2026-10-14); AMENDMENTS APPLIED AND ENGINEER-VERIFIED; ARCHITECT AMENDMENT VERIFICATION PENDING.*
