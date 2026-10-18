# Deployment, identity and independent Gate D

> **Version:** 1.0 · **Date:** 2026-10-16 · **Status:** Proposed — pending verified publication
> **Governed by:** `DEPLOYMENT_PLAYBOOK.md`, `SOFTWARE_FACTORY_PLAYBOOK.md` §2, `RRM_PLAYBOOK.md` §2, `QAM_PLAYBOOK.md`, `DEPLOYMENT_PLAYBOOK.md`.

This revised workflow supersedes the August diagram `SRC-W03_FFM_DEPLOYMENT.png` for current instructions when this proposed sync is approved, landed and verified. The [unaltered original](../../_AUDIT/SYNC_2026-10-15_doctrine-part2/INTAKE_SNAPSHOT/factory-intake/SOURCES/Workflow/SRC-W03_FFM_DEPLOYMENT.png) remains historical evidence; it grants no current role, Git or cloud permission. This derivative follows RUL-01…15 and Tony’s explicit workflow/diagram correction assignment of 2026-10-16.

![Revised stick-actor workflow](../_assets/workflows/FFM_DEPLOYMENT.svg)

## Sequence

1. **Architect:** Declare target, permissions, exclusion and recovery.
2. **QA Lead:** Required product QA verdict remains distinct.
3. **Director:** Release the verified candidate for deployment.
4. **Authorized operator:** Deploy within existing context-specific permissions.
5. **QA Executor:** Verify deployed identity, exclusions and behavior at Gate D.
6. **QA Lead:** Issue deployed-environment verdict.
7. **Director:** Release decision or authorized recovery.
8. **Architect:** Record follow-ups; release is separate from review.

## Review and release checkpoints

- Review checkpoint 1: after FFM build and its independent QA finish.
- Review checkpoint 2: Engine 2 independent system review after all Engine 1 phases/modules and their QA are closed.
- At either checkpoint, disposition findings; RRM only for approved findings requiring repairs. A clean review requires no RRM.
- Review, Gate Q, required cleanup and certification, Gate D and Director release remain separate responsibilities.

## Entry, handoff and evidence

Boot/resume through the module’s declared entry file: Engineering routes to its released implementation assignment; QA routes to `QAM/` as QA Executor. Read-only Git inspection and declared reporting writes are permitted; Tony performs all Git mutations. Requirements/acceptance freeze while declared handoff and QA evidence lanes remain writable. Preserve actual candidate, test-plan, repair/retest, cleanup and closeout identities; never prefill a verdict or planned commit SHA. Deployment additionally requires verified exclusion from build inputs and the actual artifact; a folder name is insufficient. Existing modules in flight keep their recorded sequence unless explicitly amended.

## Version History

| Version | Date | Change | Authority |
|---|---|---|---|
| 1.0 | 2026-10-16 | Revised workflow and stick diagram; original retained; review checkpoints and seat boundaries reconciled | MC-06; W01–W23; RUL-01–RUL-15; Tony 2026-10-16 correction assignment |
