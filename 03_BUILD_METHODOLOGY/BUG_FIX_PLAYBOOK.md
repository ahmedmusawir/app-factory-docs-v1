# BUG FIX PLAYBOOK

> **Version:** 0.1  
> **Date:** 2026-08-04  
> **Status:** DRAFT — Validate through real FIX modules before promotion to v1.0  
> **Tier:** 3 — Build Methodology  
> **Pairs with:** `QA_PLAYBOOK.md`, `TESTING_PLAYBOOK.md`, `ENGINEER_PLAYBOOK.md`, `RECON_QUESTIONNAIRE.md`, `FFM_PLAYBOOK.md`  
> **Owner:** Stark Industries App Factory  
> **Purpose:** Standardize how defects are investigated, corrected, verified, documented, and permanently retired.

---

## 1. Core Principle

The purpose of a bug fix is not to make the symptom disappear.

The purpose is to:

1. identify the mechanism that produced the defect,
2. correct that mechanism with the smallest safe change,
3. prove the defect is gone,
4. prove existing behavior still works,
5. verify the fix in the environment where the defect matters,
6. preserve the lesson so the factory does not rebuild it.

A bug that “stopped happening” is not necessarily fixed.

A bug is closed only when the evidence supports closure.

---

## 2. Position in the Factory

This playbook governs **FIX modules** and any defect discovered during an FFM, BIM, FEAT, deployment, prototype, or production-support run.

It does not replace:

- `TESTING_PLAYBOOK.md` — the source of truth for test-layer implementation.
- `QA_PLAYBOOK.md` — the source of truth for independent quality gates and release verdicts.
- `RECON_QUESTIONNAIRE.md` — the source of truth for ground-truth inspection before authoring.
- Project-specific acceptance criteria — the definition of intended behavior.

This playbook defines the defect lifecycle that connects those documents.

---

## 3. Roles

### Operator / Final Approver

- Owns the final scope and release decision.
- Approves changes to doctrine and risk acceptance.
- Decides whether a known risk may ship.

### Architect

- Protects scope.
- Clarifies intended behavior and acceptance criteria.
- Reviews whether the proposed fix addresses the real mechanism.
- Identifies structural lessons that should move into factory doctrine.

### Engineer

- Performs ground-truth recon.
- Reproduces the defect.
- identifies and documents the root cause.
- Implements the smallest safe fix.
- Adds regression protection.
- Runs targeted and full regression suites.
- Produces evidence.

### QA Lead

- Reviews the reproduction, root-cause claim, test plan, and evidence independently.
- Verifies the fix against acceptance criteria.
- Issues Gate Q and Gate D verdicts under `QA_PLAYBOOK.md`.
- Rejects closure when evidence is missing, ambiguous, or non-reproducible.

### DevOps / Deployment Operator

- Deploys the approved revision.
- Records the deployed commit, image, or revision identity.
- Supports rollback if Gate D fails.

One person may fill multiple roles, but the responsibilities remain distinct.

---

## 4. The Bug Lifecycle

```text
Intake
  ↓
Triage and Classification
  ↓
Reproduction
  ↓
Read-Only Recon
  ↓
Root-Cause Mechanism
  ↓
Fix Plan and Approval
  ↓
Implementation
  ↓
Targeted Regression Protection
  ↓
Full Regression Suite
  ↓
Gate Q — Pre-Deployment QA
  ↓
Deploy Approved Revision
  ↓
Gate D — Deployed-Environment Verification
  ↓
Doctrine / Tracker Promotion
  ↓
Closure and Retrospective
```

No stage may be silently skipped.

A stage may be marked **Not Applicable** only with a written reason.

---

## 5. Rule 1 — Reproduce Before Repair

Do not start by editing code.

First establish:

- the exact symptom,
- the environment where it occurs,
- the shortest reliable reproduction path,
- expected behavior,
- actual behavior,
- whether the issue is deterministic, intermittent, or environment-dependent.

For intermittent defects, capture frequency and suspected timing conditions.

Examples:

- “Fails every attempt.”
- “Fails 1–2 times in 10 on deployed staging.”
- “Occurs only after hard refresh.”
- “Occurs only on Cloud Run, not localhost.”
- “Appears when the Supabase response exceeds approximately one second.”

If the defect cannot be reproduced, keep it open as **Unconfirmed** and define the next evidence-gathering step. Do not invent a cause.

---

## 6. Rule 2 — Separate Evidence from Hypothesis

Use the factory evidence discipline during investigation.

### EVIDENCE

Directly observed in code, logs, network traces, database state, screenshots, or repeatable behavior.

### INFERENCE

A reasoned conclusion supported by evidence, but not yet proven.

### CLAIM

Something stated by a person or document but not independently verified.

### GAP

Expected evidence that is missing.

### QUESTION

A decision or fact that requires operator or stakeholder input.

A hypothesis is not a root cause.

The fix plan may begin only when the proposed mechanism is either:

- confirmed by direct evidence, or
- explicitly approved as the safest bounded experiment when complete confirmation is impossible.

---

## 7. Rule 3 — Name the Mechanism

Every confirmed bug must answer:

1. What failed?
2. What mechanism caused it?
3. Why did the previous behavior allow it?
4. Why does the proposed change remove that mechanism?
5. What could still make the bug return?

Bad root-cause statement:

> The navbar randomly disappeared.

Good root-cause statement:

> The authenticated navigation depended on a client-side user fetch performed after mount. The shell rendered an empty navigation state while the request was unresolved. Real cloud latency widened that timing window enough for users to observe it.

“It stopped happening” is not a mechanism.

If the mechanism cannot be named, the bug is not ready to close.

---

## 8. Rule 4 — Classify the Defect

Assign one primary class and any relevant secondary classes.

### Build Defect

Implementation does not satisfy the intended behavior.

Examples:

- wrong business logic,
- broken UI,
- validation defects,
- missing states,
- role-check mistakes,
- incorrect calculations.

### Deployment Defect

The built code behaves incorrectly in a deployed environment.

Examples:

- baked environment values,
- cookies,
- DNS,
- SSL,
- Cloud Run configuration,
- secret mapping,
- OAuth callback URLs,
- storage permissions,
- external-service connectivity.

### Data-Integrity Defect

Stored, transformed, migrated, or calculated data is incorrect or inconsistent.

Examples:

- duplicate rows,
- wrong tenant ownership,
- stale reference data,
- migration loss,
- incorrect reimbursement values.

### Security / Privacy Defect

A defect can expose data, bypass authorization, leak secrets, or violate compliance boundaries.

Examples:

- RLS bypass,
- privilege escalation,
- PHI exposure,
- internal error leakage,
- service-role key exposure.

### Performance / Reliability Defect

The system is correct only under ideal timing or load.

Examples:

- race conditions,
- timeouts,
- memory growth,
- slow queries,
- retry storms,
- non-idempotent jobs.

### Usability / Accessibility Defect

The system technically functions but cannot be reliably or accessibly used.

Examples:

- unreachable mobile controls,
- missing keyboard path,
- unreadable states,
- misleading feedback.

Classification determines the required tests and the environment where closure must be proven.

---

## 9. Rule 5 — Protect Scope

A FIX module corrects the confirmed defect and the minimum required surrounding surface.

Do not use a bug as permission to:

- refactor unrelated code,
- replace frameworks,
- redesign nearby screens,
- clean unrelated warnings,
- change naming conventions,
- add features,
- “improve” behavior outside the accepted fix.

Unrelated discoveries must be routed to:

- another FIX,
- a FEAT module,
- `SECURITY_FINDINGS.md`,
- `CLEANUP_BACKLOG.md`,
- or a documented follow-up question.

The smallest correct fix is preferred over the broadest elegant rewrite.

---

## 10. Rule 6 — Every Bug Earns Regression Protection

Every confirmed defect must leave behind a repeatable way to detect its return.

Use the **cheapest effective layer** defined by `TESTING_PLAYBOOK.md`.

Preferred order:

1. unit test,
2. integration test,
3. E2E test,
4. deterministic manual smoke step,
5. static check, grep, lint rule, schema assertion, or monitoring alert.

Automation is preferred, but not every environment defect is fully automatable.

When regression protection remains manual, document:

- why automation is not practical,
- the exact steps,
- the expected result,
- where the step lives in Gate Q or Gate D.

Do not create tests for deprecated behavior that is scheduled for removal. Record that decision in `CLEANUP_BACKLOG.md`.

A bug should be discovered once, not repeatedly rediscovered.

---

## 11. Rule 7 — Test in the Correct Order

After implementation:

### Step 1 — Targeted Test

Run the smallest test that proves the mechanism is corrected.

### Step 2 — Neighbor Tests

Run tests for directly affected modules, contracts, routes, policies, and flows.

### Step 3 — Full Regression Suite

Run all existing tests required by the repository.

No fix may declare success while hiding unrelated failures.

If failures were already present before the fix:

- prove they are pre-existing,
- report them,
- do not silently repair or suppress them,
- do not weaken assertions,
- do not add retries to create a green result.

### Step 4 — Manual or System Verification

Walk the user-visible or system-level path that originally exposed the defect.

### Step 5 — Gate Q

Submit evidence to QA for pre-deployment verdict.

---

## 12. Rule 8 — Environment Parity Matters

Different environments reveal different defect classes.

### Local Development

Useful for:

- implementation speed,
- logic,
- basic UI behavior,
- unit and integration tests.

It may hide:

- network latency,
- cookie-domain behavior,
- cloud IAM,
- CDN behavior,
- baked environment values,
- real external-service timing.

### Local Production Build

Useful for:

- production compilation,
- route generation,
- bundling,
- build-time environment behavior.

It still may hide deployed-network and cloud-runtime defects.

### Deployed Staging

Required for:

- authentication round trips,
- session persistence,
- latency-sensitive behavior,
- Cloud Run and Supabase connectivity,
- secret mapping,
- DNS and HTTPS,
- storage,
- external integrations.

### Production

Requires a minimal, non-destructive confirmation when a production release occurs.

Factory rule:

> Local development proves code behavior.  
> A production build proves packaging.  
> The deployed environment proves the system.

---

## 13. Rule 9 — Gate Q and Gate D Are Both Required

### Gate Q — Pre-Deployment Quality Gate

Gate Q proves the revision is fit to deploy.

Minimum evidence:

- reproduction confirmed,
- root cause named,
- fix implemented,
- targeted regression protection added,
- affected tests passed,
- full required test suite passed,
- acceptance criteria passed,
- security and data risks reviewed,
- rollback considerations documented.

A Gate Q failure blocks deployment.

### Gate D — Deployed-Environment Verification

Gate D proves the deployed revision behaves correctly in the real target environment.

Minimum evidence:

- expected revision is deployed,
- health checks pass,
- original reproduction no longer fails,
- auth and session paths pass when affected,
- core workflow passes,
- logs show no new critical errors,
- environment-specific integrations pass,
- rollback remains available.

A deployment is not complete until Gate D passes.

> **Naming protection:** Gate M remains the existing FFM mobile-shell gate. This playbook does not redefine it.

---

## 14. Rule 10 — Promote Lessons into the Right Home

A changelog records history. It does not enforce behavior.

After the fix, determine whether the lesson is:

### Project-Specific

Keep it in:

- the FIX retrospective,
- project docs,
- known-issues documentation,
- monitoring notes.

### Structural

Promote it into one or more of:

- playbook rule,
- `ANTI_PATTERNS.md`,
- QA checklist,
- verification gate,
- engineer prompt,
- template,
- lint rule,
- grep/static check,
- CI assertion,
- monitoring alert.

Do not promote every project-specific incident into global doctrine. Structural promotion is for lessons that can protect future projects.

---

## 15. Severity

### Critical

Release blocker. Active or credible risk of:

- unauthorized access,
- PHI/PII exposure,
- data corruption,
- financial miscalculation,
- system-wide outage,
- irreversible action.

### High

Core workflow is broken or unsafe for a meaningful user segment. No reasonable workaround.

### Medium

Important behavior is incorrect, but a safe workaround exists or impact is limited.

### Low

Minor functional, usability, or cosmetic defect with low operational risk.

Severity describes impact.

Priority describes when the team chooses to act.

Do not lower severity merely because a workaround exists.

---

## 16. Required FIX Artifacts

Every non-trivial FIX module should contain:

1. `BUG_REPORT.md`
2. `FIX_PLAN.md`
3. regression test or deterministic regression checklist
4. Gate Q evidence
5. Gate D evidence when deployed
6. retrospective / lessons entry
7. changelog entry
8. doctrine or tracker updates when applicable

Small fixes may combine these into one document, but no required information may disappear.

---

## 17. BUG_REPORT Template

```markdown
# BUG REPORT: [ID] — [Title]

## Status
[UNCONFIRMED | CONFIRMED | IN FIX | GATE Q | DEPLOYED | GATE D | CLOSED]

## Severity
[CRITICAL | HIGH | MEDIUM | LOW]

## Classification
Primary:
Secondary:

## Environment
- Local dev:
- Local production:
- Staging:
- Production:
- Browser/device:
- Commit/revision:

## Observed Symptom
What the user or system experienced.

## Expected Behavior
What should have happened.

## Reproduction
Exact shortest path and observed frequency.

## Evidence
Evidence-labeled findings with file paths, logs, screenshots, traces, or database queries.

## Root-Cause Mechanism
The confirmed mechanism. If not confirmed, mark it as INFERENCE and keep status open.

## Blast Radius
Affected users, modules, tenants, data, environments, and workflows.

## Fix Boundary
What may change.

## Forbidden Scope
What must not change.

## Regression Protection
Test or deterministic check that catches recurrence.

## Gate Q Evidence
Pre-deployment results.

## Gate D Evidence
Deployed-environment results.

## Doctrine / Tracker Promotion
Structural lesson, project-specific lesson, or no promotion with reason.

## Closure Verdict
Who approved closure, when, and on what evidence.
```

---

## 18. Definition of Done

A confirmed bug is **DONE** only when:

- [ ] symptom and environment documented,
- [ ] reproduction confirmed or evidence limitation explicitly recorded,
- [ ] root-cause mechanism named,
- [ ] scope boundary approved,
- [ ] smallest safe fix implemented,
- [ ] regression protection added,
- [ ] targeted tests passed,
- [ ] full required regression suite passed,
- [ ] Gate Q passed,
- [ ] deployed revision identity recorded,
- [ ] Gate D passed when deployment is part of the fix,
- [ ] security and data-integrity findings routed,
- [ ] changelog updated,
- [ ] structural lessons promoted where appropriate,
- [ ] operator or authorized owner approved closure.

A closed bug must be understandable by a future engineer without access to the original conversation.

---

## 19. Anti-Patterns

### Symptom Patch

Changing the visible behavior without removing the mechanism.

### Cannot Reproduce, Therefore Fixed

Absence of evidence in a friendly environment is not evidence of resolution.

### Test the Copy

Reimplementing source logic inside a test and proving only the duplicate.

### Green by Suppression

Skipping tests, weakening assertions, adding retries, swallowing errors, or ignoring red checks.

### Drive-By Refactor

Expanding the FIX into unrelated cleanup.

### Changelog Burial

Recording a structural lesson only in historical notes.

### Localhost Closure

Declaring an environment-sensitive defect closed without deployed verification.

### Unidentified Deployment

Testing a URL without proving which commit or Cloud Run revision is serving it.

---

## 20. Version History

| Version | Date | Change |
|---|---|---|
| 0.1 | 2026-08-04 | Initial draft. Defines evidence-first bug lifecycle, root-cause mechanism rule, regression protection, Gate Q and Gate D, scope control, environment parity, severity, required artifacts, doctrine promotion, and closure criteria. |
