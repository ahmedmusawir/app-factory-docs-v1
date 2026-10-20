# AUTOMATION/ — approved QA helpers and instrument controls

> TEMPLATE SET v0.3 — QA LEAD ACCEPTED WITH EXACT AMENDMENTS (Fable, 2026-10-14); AMENDMENTS ARCHITECT-VERIFIED; INSTALLATION REQUIRES THE APPROVED DOCSET SYNC. Template `QAM/AUTOMATION/README.md` v0.3-draft (2026-10-14), from `QAM_PLAYBOOK_v1_0.md` §5, §10, §12. **Owner: QA Executor writes helpers within this lane; the Architect declares the lane and its limits at packaging; the QA Lead approves retention at cleanup.** Helpers here are QA-only instruments, never product runtime dependencies. Promotion of a helper into maintained product tests is a separate authorized engineering change.

## Lane rules

- Helpers read credentials only from the declared ignored QA credential file (`<<QA_CREDENTIAL_FILE>>`) into process memory; values never reach commands, logs, exceptions, screenshots, traces, JSON or ZIPs.
- Every helper states its working directory and performs existence checks before diffs, greps or counts so that nothing passes vacuously.
- A helper that cannot fail is not an instrument: at least one deliberate attack (corrupted input, synthetic leak fixture) is recorded per instrument class, with the non-zero failure preserved.
- Repair of a helper is logged in `QAM_EXECUTION_REPORT.md` §3 with the failed attempt preserved and the corrected instrument re-verified. Never weaken an assertion, add a hidden retry or skip a test to obtain green.
- Avoid persistent browser storage; if unavoidable, declare its temporary path here and its cleanup step in `QAM_CLEANUP_REPORT.md`.

## Helper inventory

| Helper | Purpose | Inputs (by name) | Working directory | Instrument control (how it was attacked) | Retained after cleanup? (QA Lead) |
|---|---|---|---|---|---|
| none yet | | | | | NOT RECORDED |

*TEMPLATE SET v0.3 — QA LEAD ACCEPTED WITH EXACT AMENDMENTS (Fable, 2026-10-14); AMENDMENTS ARCHITECT-VERIFIED; INSTALLATION REQUIRES THE APPROVED DOCSET SYNC.*
