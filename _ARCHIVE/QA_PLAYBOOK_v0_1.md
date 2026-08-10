# QA PLAYBOOK

> **Version:** 0.1 · **Date:** 2026-08-04 · **Status:** DRAFT — Validate through real FFM, BIM, FIX, and FEAT runs before promotion to v1.0
> **Tier:** 3 — Build Methodology  
> **Pairs with:** `BUG_FIX_PLAYBOOK.md`, `TESTING_PLAYBOOK.md`, `SOFTWARE_FACTORY_PLAYBOOK.md`, `ENGINEER_PLAYBOOK.md`, `FFM_PLAYBOOK.md`, `RECON_QUESTIONNAIRE.md`  
> **Owner:** Stark Industries App Factory  
> **Purpose:** Define how the factory plans, executes, records, and approves quality verification before and after cloud deployment.

---

## 1. Core Principle

QA exists to reduce uncertainty.

Engineering asks:

> Did we implement the requested change?

QA asks:

> What evidence shows the system can be trusted?

A green build is evidence.

It is not the whole verdict.

A release is complete only when:

1. the revision satisfies its acceptance criteria before deployment, and
2. the deployed system behaves correctly in its real environment.

---

## 2. Position in the Factory

This playbook orchestrates quality across:

- FFM modules,
- BIM modules,
- FIX modules,
- FEAT modules,
- prototypes promoted to the mothership,
- staging deployments,
- production releases.

It does not replace `TESTING_PLAYBOOK.md`.

`TESTING_PLAYBOOK.md` remains the source of truth for:

- unit testing,
- integration testing,
- E2E testing,
- manual smoke testing,
- test isolation,
- fixture strategy,
- retries,
- backend-specific mocking,
- diagnostic patterns.

This QA playbook defines:

- who verifies,
- what evidence is required,
- when gates run,
- how verdicts are issued,
- how defects route back to engineering,
- when deployment and release are complete.

---

## 3. Quality Flow

```text
Recon / Ground Truth
  ↓
Scope and Acceptance Criteria
  ↓
QA Risk Review
  ↓
Engineer Plan
  ↓
Implementation
  ↓
Engineer Self-Verification
  ↓
Gate Q — Pre-Deployment QA
  ↓
Deploy Approved Revision
  ↓
Gate D — Deployed-Environment Verification
  ↓
Production Confirmation when applicable
  ↓
Retrospective and Doctrine Promotion
  ↓
Release Complete
```

No module begins without acceptance criteria.

No deployment begins without Gate Q.

No deployment is complete without Gate D.

---

## 4. Roles and Authority

### Operator / Final Approver

- Owns final product and release authority.
- Approves scope, risk acceptance, and exceptions.
- May override a QA recommendation only with a written acknowledgment of the risk.

### Architect

- Defines or validates scope and acceptance criteria.
- Identifies forbidden zones and risks.
- Ensures the QA plan tests the intended product behavior, not an invented behavior.
- Reviews structural lessons for doctrine promotion.

### Engineer

- Implements the approved scope.
- Runs targeted and full required test suites.
- Supplies reproducible evidence.
- Does not self-approve release.

### QA Lead

- Produces or reviews the QA plan.
- Traces every acceptance criterion to evidence.
- Independently reviews engineering claims.
- Executes or coordinates manual verification.
- Classifies and routes defects.
- Issues Gate Q and Gate D verdicts.

### DevOps / Deployment Operator

- Deploys the approved revision.
- Records commit SHA, image digest, service revision, environment, and timestamp.
- Maintains rollback capability.
- Supports environment-specific diagnostics.

QA owns the verdict.

The operator owns the final release decision.

---

## 5. Evidence Discipline

QA reports must distinguish:

### EVIDENCE

Direct observation from tests, logs, screenshots, network traces, database state, revision metadata, or manual walkthroughs.

### INFERENCE

A conclusion supported by evidence but not directly proven.

### CLAIM

A statement from a person or document that QA has not independently verified.

### GAP

Required evidence that is missing.

### QUESTION

A decision or fact needed from the operator, architect, engineer, or stakeholder.

Rules:

- Never turn a CLAIM into a PASS.
- Never hide a GAP inside narrative prose.
- Never call a test “passing” without the command, environment, and result.
- Never test a deployed URL without recording the deployed revision identity.
- Redact secrets, credentials, PHI, PII, and protected log content from evidence.

---

## 6. QA Inputs Required

Before QA planning begins, the module should provide:

- approved scope,
- acceptance criteria,
- forbidden zones,
- current recon report,
- affected file or component map,
- affected services and external integrations,
- data and security boundaries,
- test runner and commands verified from disk,
- target environments,
- deployment plan,
- rollback plan or rollback limitations,
- known pre-existing failures,
- known risks and open questions.

If a required input is missing, QA may issue **BLOCKED** rather than guess.

---

## 7. Risk-Based QA Planning

QA depth should match risk.

Evaluate:

- user impact,
- security and privacy,
- financial or calculation impact,
- data integrity,
- tenant isolation,
- reversibility,
- external dependencies,
- environment sensitivity,
- concurrency and timing,
- frequency of use,
- blast radius.

### Low-Risk Example

Copy change or isolated visual correction.

Possible test depth:

- targeted visual verification,
- responsive check,
- full existing regression suite if code changed,
- deployed smoke on affected route.

### High-Risk Example

RLS, reimbursement math, Liberty imports, payment, PDF/PHI delivery, authentication, or scheduled data pipelines.

Required test depth may include:

- unit,
- integration,
- E2E,
- database assertions,
- negative authorization cases,
- multi-tenant isolation,
- failure injection,
- idempotency,
- rollback,
- deployed verification,
- logs and monitoring.

Risk determines depth.

Schedule pressure does not erase risk.

---

## 8. The Four Test Layers

QA plans must use the lowest-cost layer that proves each claim, following `TESTING_PLAYBOOK.md`.

### Layer 1 — Unit

Proves pure logic.

Examples:

- reimbursement formulas,
- formatters,
- validators,
- role hierarchy,
- mapping logic.

### Layer 2 — Integration

Proves modules orchestrate dependencies correctly.

Examples:

- route handler and service behavior,
- database query composition,
- webhook validation,
- Edge Function parsing,
- storage metadata.

### Layer 3 — E2E

Proves user workflows in a real browser or full system path.

Examples:

- login to protected page,
- pharmacy A sees only pharmacy A,
- submit and confirm workflow,
- upload and process file.

### Layer 4 — Manual Smoke

Proves real third-party and deployed-environment behavior.

Examples:

- Cloud Run custom domain,
- real cookie round trip,
- email delivery,
- signed storage URL,
- OAuth redirect,
- production-only integration.

Do not write an E2E test for a claim a unit test can prove.

Do not mock the only behavior the test claims to verify.

Do not add retries to hide flakes. Flaky tests are defects.

---

## 9. Gate Q — Pre-Deployment Quality Gate

### Purpose

Prove the release candidate is fit to deploy.

Gate Q runs after implementation and engineer self-verification, but before cloud deployment of that revision.

### Required Checks

#### Scope and Traceability

- [ ] Every acceptance criterion has a test or explicit verification step.
- [ ] Forbidden zones were respected.
- [ ] No unrelated scope was added.
- [ ] Documentation and data contracts match the implementation.

#### Ground Truth

- [ ] Test runner and commands were verified from disk.
- [ ] A current recon report exists or the operator approved a documented exception.
- [ ] Claimed file paths, exports, routes, policies, and environment names were verified.

#### Tests

- [ ] Targeted tests pass.
- [ ] Directly affected integration tests pass.
- [ ] Full required regression suite passes.
- [ ] No retries were introduced to create a green result.
- [ ] Pre-existing failures are separated and evidenced.
- [ ] Tests do not duplicate source logic as shadow implementations.
- [ ] Deprecated behavior is not being preserved accidentally.

#### Security and Data

- [ ] Authentication and authorization checks are server-enforced where required.
- [ ] RLS or tenant-isolation tests include negative cases.
- [ ] Service-role paths are isolated.
- [ ] Secrets are not exposed in client bundles, logs, or evidence.
- [ ] PHI/PII test data is synthetic, seeded, or explicitly approved.
- [ ] Error responses do not leak internal or protected data.

#### UI and Accessibility when applicable

- [ ] Existing Gate M requirements pass for UI-bearing work.
- [ ] Mobile, tablet, and desktop behavior is verified.
- [ ] Loading, empty, error, and success states are verified.
- [ ] Keyboard and accessibility-critical paths are checked.

#### Deployment Readiness

- [ ] Approved commit or artifact is identified.
- [ ] Environment variables and secrets required by the change are documented.
- [ ] Database migrations are ordered and reversible where practical.
- [ ] Rollback path is documented.
- [ ] Gate D checklist is prepared before deployment.

### Gate Q Verdicts

#### PASS

All required evidence is present. Deployment may proceed.

#### PASS WITH KNOWN RISK

Only permitted when:

- no Critical or High defect remains,
- the risk is documented,
- mitigation or workaround is documented,
- the operator explicitly accepts the risk.

#### FAIL

A requirement is unmet or a release-blocking defect exists. Deployment is blocked.

#### BLOCKED

QA cannot issue a verdict because required evidence, access, environment, or decisions are missing.

### Naming Protection

Gate M already means the FFM mobile-shell gate.

Gate Q does not replace or rename Gate M. Gate M becomes one input to Gate Q for UI-bearing work.

---

## 10. Gate D — Deployed-Environment Verification

### Purpose

Prove the deployed system—not merely the code—works in the target cloud environment.

Gate D runs on the deployed staging revision.

For a production release, repeat a minimal non-destructive production confirmation after promotion.

### Step 1 — Deployment Identity

Record:

- repository,
- branch,
- commit SHA,
- build ID,
- image digest when available,
- Cloud Run revision or equivalent,
- environment,
- URL,
- deployment timestamp.

Do not test an unidentified deployment.

### Step 2 — Availability

- [ ] DNS resolves.
- [ ] HTTPS certificate is valid.
- [ ] Expected URL loads.
- [ ] Health endpoint passes when present.
- [ ] Correct service and revision are serving traffic.

### Step 3 — Authentication and Session

When applicable:

- [ ] login works,
- [ ] correct role resolves,
- [ ] navigation is present,
- [ ] session survives navigation,
- [ ] session survives hard refresh,
- [ ] protected routes reject unauthorized users,
- [ ] logout clears access,
- [ ] incognito path behaves correctly.

### Step 4 — Core Workflow

Walk the shortest critical path for the deployed change.

Examples:

- OwedBook reads seeded rows,
- pharmacy A cannot see pharmacy B,
- reference job fetches and versions data,
- Liberty import reaches expected staging state,
- PDF generates and stores,
- signed link opens for authorized user,
- payment or subscription state updates.

### Step 5 — Environment-Specific Dependencies

Verify affected dependencies:

- Secret Manager,
- Supabase connectivity,
- storage permissions,
- Cloud Run service accounts,
- custom domains,
- OAuth callbacks,
- external APIs,
- scheduled jobs,
- email delivery,
- webhooks,
- CORS,
- file size and timeout behavior.

### Step 6 — Latency and Race Conditions

Where timing matters:

- hard refresh repeatedly,
- test cold start when practical,
- test slow or delayed responses,
- navigate quickly,
- verify shell stability during loading,
- confirm no global overlay blocks navigation,
- inspect network timing and failed requests.

### Step 7 — Logs and Monitoring

- [ ] no new Critical or High errors,
- [ ] no secret or PHI leakage,
- [ ] expected audit/log entries appear,
- [ ] failures are observable,
- [ ] alerting path works when in scope.

### Step 8 — Regression Smoke

At minimum:

- [ ] authentication,
- [ ] navigation,
- [ ] core read path,
- [ ] core write path when applicable,
- [ ] one negative permission path,
- [ ] one error path,
- [ ] original bug reproduction for FIX modules.

### Step 9 — Rollback Readiness

- [ ] previous stable revision is known,
- [ ] rollback command or action is known,
- [ ] database compatibility is understood,
- [ ] destructive migrations have an approved recovery plan.

### Gate D Verdicts

#### PASS

The deployed revision is verified. Release may be declared complete.

#### PASS WITH KNOWN RISK

Only permitted with written operator acceptance and no unresolved Critical or High defect.

#### FAIL

The deployed system is unsafe or materially incorrect. Stop promotion or roll back.

#### BLOCKED

The environment, dependency, access, or evidence prevents verification.

A successful deployment command is not a Gate D PASS.

---

## 11. Production Confirmation

When staging passes and production is deployed, run a bounded, non-destructive subset of Gate D.

Minimum production confirmation:

- correct production revision,
- DNS and HTTPS,
- login,
- session persistence,
- navigation,
- one safe core read,
- one authorization-negative check when safe,
- logs free of new critical errors,
- external integration heartbeat when applicable.

Do not use real PHI or irreversible actions merely to prove deployment.

Use approved synthetic, seeded, or designated test records.

---

## 12. QA Deliverables Per Module

Every BIM, FIX, and FEAT should produce or reference:

1. `ACCEPTANCE_CRITERIA.md`
2. `QA_PLAN.md`
3. engineer test evidence
4. `GATE_Q_REPORT.md`
5. `GATE_D_CHECKLIST.md`
6. `GATE_D_REPORT.md` after deployment
7. bug reports for failures
8. known-risks section
9. retrospective input
10. changelog and doctrine/tracker updates when applicable

For small modules, these may be sections in fewer files.

The information may be compressed.

The evidence may not disappear.

---

## 13. QA Plan Template

```markdown
# QA PLAN: [Module / Release]

## Scope
What is being verified.

## Out of Scope
What is intentionally not being verified.

## Source of Truth
Approved brief, contract, design, recon report, and relevant playbooks.

## Risks
Security, data, financial, environment, dependency, timing, and rollback risks.

## Acceptance-Criteria Traceability
| ID | Acceptance Criterion | Test Layer | Test / Check | Environment |
|---|---|---|---|---|

## Regression Scope
Existing workflows that must remain green.

## Test Data
Synthetic, seeded, discovered, or approved fixtures.

## Gate Q Plan
Pre-deployment checks and commands.

## Gate D Plan
Deployed-environment checks and required access.

## Known Gaps
Missing environments, credentials, data, or automation.

## Exit Criteria
Evidence required for PASS.
```

---

## 14. QA Report Template

```markdown
# QA REPORT: [Module / Release]

## Verdict
[PASS | PASS WITH KNOWN RISK | FAIL | BLOCKED]

## Environment
- Repo:
- Commit:
- Build:
- Revision:
- URL:
- Date:

## Scope Verified

## Acceptance-Criteria Results
| ID | Result | Evidence | Notes |
|---|---|---|---|

## Tests Run
| Command / Check | Environment | Result | Evidence |
|---|---|---|---|

## Defects
| ID | Severity | Classification | Status | Owner |
|---|---|---|---|---|

## Known Risks

## Gaps / Untested Areas

## Gate Q Verdict

## Gate D Verdict

## Release Recommendation

## Approvals
QA Lead:
Operator:
```

---

## 15. Defect Routing

When QA finds a defect:

1. stop and record evidence,
2. assign severity and classification,
3. determine whether it blocks the current gate,
4. open or update a FIX module,
5. hand the report to engineering,
6. verify the correction under `BUG_FIX_PLAYBOOK.md`,
7. rerun the failed check,
8. rerun affected regression,
9. rerun the full required suite when code changed,
10. reissue the gate verdict.

QA does not silently fix implementation defects during verification.

QA may improve QA artifacts, but code changes return to engineering.

---

## 16. Severity and Release Rules

### Critical

Always blocks Gate Q and Gate D.

Examples:

- unauthorized PHI/PII access,
- privilege escalation,
- corrupted claims,
- wrong reimbursement totals,
- broken payments,
- system-wide outage.

### High

Normally blocks release.

An exception requires explicit operator risk acceptance and a clear containment plan. Security, privacy, data-integrity, and financial High defects should be treated as blockers.

### Medium

May ship only with documented impact, workaround, owner, and target fix window.

### Low

May ship when the behavior is understood and recorded.

Severity is based on impact, not effort.

---

## 17. Regression Doctrine

The regression suite should compound as the product matures.

It should not preserve dead features forever.

Rules:

- Every confirmed defect earns regression protection.
- Every high-value workflow keeps a stable regression path.
- All required tests run before Gate Q.
- Flakes are defects; retries remain zero unless the testing doctrine explicitly changes.
- Obsolete tests may be retired only when the feature is intentionally removed and the decision is documented.
- Test failures caused by the current change must be fixed.
- Pre-existing failures must be proved and reported, not silently absorbed.
- Never weaken assertions merely to restore green CI.

---

## 18. Security, Privacy, and Evidence Handling

For regulated or sensitive systems:

- use synthetic or de-identified test data by default,
- never paste secrets into reports,
- redact tokens, emails, patient details, and claim identifiers,
- avoid screenshots containing PHI,
- verify audit logging without exposing protected content,
- keep QA artifacts in approved storage,
- test least-privilege and negative access paths,
- confirm service-role credentials never reach the browser,
- treat unexpected access as a Critical defect until disproven.

For Cyber Pharma, tenant isolation, PHI boundaries, reimbursement accuracy, reference-data integrity, and auditability are release-critical.

---

## 19. Retrospective and Doctrine Promotion

After each meaningful run:

1. Engineer drafts the retrospective.
2. QA contributes:
   - escaped defects,
   - false positives,
   - missing acceptance criteria,
   - weak test evidence,
   - environment-only failures,
   - checks that caught real problems,
   - checks that added noise.
3. Operator reviews.
4. Architect separates:
   - project-specific lessons,
   - phase-specific lessons,
   - structural factory lessons.
5. Structural lessons promote into:
   - playbooks,
   - anti-patterns,
   - checklists,
   - templates,
   - static checks,
   - CI,
   - monitoring.

The factory compounds only when evidence changes future behavior.

---

## 20. Definition of Release Complete

A release is complete only when:

- [ ] approved acceptance criteria exist,
- [ ] QA plan exists,
- [ ] engineer self-verification is complete,
- [ ] all required tests pass,
- [ ] Gate Q passes,
- [ ] approved revision is deployed,
- [ ] deployed identity is recorded,
- [ ] Gate D passes,
- [ ] production confirmation passes when applicable,
- [ ] no unresolved Critical defect exists,
- [ ] High risks are resolved or explicitly accepted under policy,
- [ ] defects are routed,
- [ ] changelog is updated,
- [ ] retrospective inputs are captured,
- [ ] operator approves release completion.

---

## 21. Anti-Patterns

### QA at the End

Waiting until implementation is complete to define acceptance criteria.

### Engineer Self-Certification

Treating the implementer’s “works for me” as independent verification.

### Build Equals Release

Treating green CI or a successful deploy command as proof of system health.

### Unidentified Environment

Testing without recording the exact commit, build, revision, and URL.

### Happy-Path Only

Ignoring negative roles, error paths, stale data, timeouts, and failure recovery.

### Mocking the Claim

Mocking the external behavior the test claims to prove.

### Retry Green

Using retries to conceal flakes.

### PHI in Evidence

Leaking protected data into screenshots, logs, tickets, or chat.

### Gate Drift

Inventing new names that conflict with existing factory gates.

### Changelog-Only Learning

Recording lessons without promoting structural protections.

---

## 22. Version History

| Version | Date | Change |
|---|---|---|
| 0.1 | 2026-08-04 | Initial draft. Defines QA roles, evidence discipline, risk-based planning, Gate Q pre-deployment QA, Gate D deployed-environment verification, production confirmation, verdicts, deliverables, defect routing, regression doctrine, security/privacy handling, and release-complete criteria. Preserves existing Gate M meaning. |
