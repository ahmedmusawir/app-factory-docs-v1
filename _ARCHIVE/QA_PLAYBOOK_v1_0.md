# QA PLAYBOOK

> **Version:** 1.0 · **Date:** 2026-08-10 · **Status:** Active — field-tested (ADK Harness BIM/FIX verification)
> **Tier:** 3 — Build Methodology  
> **Pairs with:** `BUG_FIX_PLAYBOOK.md`, `TESTING_PLAYBOOK.md`, `SOFTWARE_FACTORY_PLAYBOOK.md`, `ENGINEER_PLAYBOOK.md`, `FFM_PLAYBOOK.md`, `RECON_QUESTIONNAIRE.md`  
> **Owner:** Stark Industries App Factory  
> **QA Lead:** App Factory QA Lead  
> **Purpose:** Define how the App Factory independently verifies BIM, FIX, FEAT, FFM, prototype, deployment, and release work before it is trusted.

---

# 0. Why This Playbook Exists

The App Factory already had testing doctrine before it had a QA department.

That distinction matters.

Testing answers:

> Does this code behave as expected under a defined test?

QA answers:

> Do we have enough independent evidence to trust the engineer's claim that this module, fix, feature, or release is complete?

Those are not the same job.

The Engineer builds and self-verifies.

QA independently verifies the engineer's completion claim against the accepted contract, the real system, the real environment, and the expected user behavior.

A green test suite is evidence.

A clean build is evidence.

A successful deployment is evidence.

An engineer completion report is a claim package.

None of those alone are the QA verdict.

This playbook was promoted to v1.0 only after hands-on verification of the ADK Next.js Harness, where QA manually exercised:

- agent-selection persistence,
- hard refresh behavior,
- loading states,
- user-facing failure wording,
- localStorage persistence boundaries,
- mock-mode regression,
- live-mode recovery,
- slow-network behavior,
- browser-profile differences,
- session contamination across mock/live modes,
- Jest regression,
- TypeScript validation,
- production build,
- and final environment state.

That run proved the Factory needs an independent QA seat, not just more tests.

---

# 1. Core Principle

## QA exists to reduce uncertainty through evidence.

Engineering asks:

> Did we implement the requested change?

QA asks:

> What evidence proves the requested behavior works, regressions were avoided, the environment is correct, and the release can be trusted?

The QA Lead does not certify effort.

The QA Lead certifies evidence.

---

# 2. Position in the App Factory

QA is an independent verification function.

It sits **after Engineer self-verification and before release approval**.

```text
Recon / Ground Truth
        ↓
Scope + Acceptance Criteria
        ↓
Architect / Operator Approval
        ↓
Engineer Plan
        ↓
Implementation
        ↓
Engineer Self-Verification
        ↓
ENGINEER HANDOFF PACKAGE
        ↓
QA Intake + Contract Extraction
        ↓
Gate Q — Pre-Deployment QA
        ↓
Approved Revision Deploys
        ↓
Gate D — Deployed-Environment QA
        ↓
Production Confirmation when applicable
        ↓
QA Acceptance Report
        ↓
Operator Release Approval
        ↓
Retrospective + Doctrine Promotion
```

QA does not replace:

- `TESTING_PLAYBOOK.md`,
- Engineer unit/integration/E2E work,
- Architect acceptance criteria,
- operator product judgment,
- DevOps deployment verification.

QA orchestrates and independently validates all of them.

---

# 3. The Separation Law

## Blue Team builds. Red Team verifies.

The Engineer may:

- implement,
- write tests,
- fix failures,
- prepare evidence,
- explain design decisions,
- provide reproduction steps.

The QA Lead may:

- inspect,
- reproduce,
- execute test plans,
- challenge assumptions,
- verify evidence,
- classify findings,
- issue gate verdicts.

The QA Lead does **not** silently repair implementation defects while verifying them.

If QA finds a code defect:

1. evidence is captured,
2. the defect is classified,
3. the defect returns to Engineering,
4. Engineering fixes it,
5. QA retests it,
6. affected regression is rerun.

The same agent may technically be capable of both jobs.

The Factory still treats the jobs as separate roles.

---

# 4. Authority

## Operator / Final Approver

The Operator:

- owns product judgment,
- approves scope,
- accepts or rejects risk,
- approves release,
- may override a QA recommendation only with written acknowledgment.

## Architect

The Architect:

- defines or validates scope,
- owns acceptance-criteria clarity,
- protects forbidden zones,
- resolves product ambiguity,
- promotes structural lessons into doctrine.

## Engineer

The Engineer:

- implements approved scope,
- self-verifies,
- runs required automated tests,
- provides the completion handoff,
- does not self-approve release.

## QA Lead

The QA Lead:

- treats the handoff as claims to verify,
- authors or reviews the QA plan,
- traces acceptance criteria to evidence,
- executes or coordinates manual QA,
- performs exploratory verification,
- classifies findings,
- issues Gate Q and Gate D verdicts,
- protects the boundary between in-scope defects and follow-up findings.

## DevOps / Deployment Operator

DevOps:

- deploys the approved revision,
- records deployment identity,
- maintains rollback capability,
- supports environment diagnostics.

**QA owns the verification verdict.**

**The Operator owns the release decision.**

---

# 5. Source-of-Truth Order

QA must know what wins when sources disagree.

Use this order unless a module explicitly overrides it:

1. **Current accepted scope / acceptance specification**
2. **Current filesystem and running system**
3. **Current data contracts / architecture contracts**
4. **Current recon report**
5. **Current environment configuration**
6. **Engineer completion report**
7. **Prior documentation**
8. **Conversation history / recollection**

Important:

> The Engineer report is never higher authority than the acceptance contract or the running system.

If docs and disk disagree:

> Disk wins, and the documentation drift becomes a finding.

If acceptance criteria and implementation disagree:

> Acceptance criteria win until the Operator or Architect changes the contract.

---

# 6. The Engineer Handoff Is a Claim Package

Every BIM, FIX, FEAT, FFM, prototype promotion, or release should hand QA a completion package.

At minimum:

1. module / issue identifier,
2. accepted scope,
3. acceptance specification or acceptance criteria,
4. files changed,
5. behavior claimed complete,
6. tests added or changed,
7. commands run,
8. test results,
9. build/typecheck results,
10. manual checks already performed,
11. known limitations,
12. environment/setup requirements,
13. migrations or secret/env changes,
14. rollback notes when relevant,
15. open risks or follow-up items.

QA reads this package as:

```text
CLAIM:
"The engineer says X is complete."

CONTRACT:
"The acceptance spec requires A, B, C."

JOB:
"Independently prove or disprove A, B, C and check for obvious collateral damage."
```

A detailed engineer report increases QA efficiency.

It does not reduce QA independence.

---

# 7. Acceptance Spec = QA Contract

The acceptance spec is the center of the engagement.

Before running tests, QA extracts every testable requirement into a traceability matrix.

Example:

| ID | Acceptance Criterion | Evidence Type | Environment | Status |
|---|---|---|---|---|
| X1 | Selected agent survives refresh | Manual + browser state | Local live | Pending |
| X2 | Loading state appears during delayed response | Manual | Local throttled | Pending |
| X3 | User-facing error says Agent Service | Failure injection | Local live | Pending |
| X4 | No transcript content persists in localStorage | Storage inspection | Browser | Pending |
| X5 | Mock mode still works | Regression manual | Local mock | Pending |
| X6 | Automated suite remains green | Jest | Local | Pending |
| X7 | TypeScript + build remain clean | CLI | Local | Pending |

If a requirement cannot be tested because the acceptance spec is ambiguous:

> QA issues a QUESTION or BLOCKED state.

QA does not invent product behavior.

---

# 8. Evidence Discipline

Every QA statement belongs to one of five evidence classes.

## EVIDENCE

Directly observed.

Examples:

- command output,
- screenshot,
- browser behavior,
- localStorage contents,
- network payload,
- HTTP status,
- database row,
- cloud revision,
- log entry.

## INFERENCE

A conclusion strongly supported by evidence but not directly observed.

Example:

> The 502 is likely caused by a mock session ID being sent to the live endpoint because the network payload shows the mock ID and the stored map contains the same value.

## CLAIM

A statement from Engineering, documentation, or a stakeholder that QA has not independently verified.

## GAP

Evidence that should exist but does not.

## QUESTION

A fact or decision required from the Operator, Architect, Engineer, or stakeholder.

### Rules

- Never convert CLAIM into PASS.
- Never bury GAP inside prose.
- Never say "tests pass" without the command and result.
- Never say "deployment works" without identifying the deployed revision.
- Never expose secrets, PHI, PII, credentials, or protected identifiers in QA artifacts.
- Never infer root cause when the evidence only proves a symptom.

---

# 9. QA Engagement Lifecycle

Every meaningful QA engagement follows this sequence.

---

## Stage 1 — Intake

QA receives:

- acceptance spec,
- engineer completion report,
- changed-file summary,
- environment/setup requirements,
- relevant contracts,
- relevant test commands,
- target environment.

QA first answers:

> What exactly am I being asked to certify?

---

## Stage 2 — Contract Extraction

Convert the acceptance spec into a test matrix.

No manual testing begins until the acceptance criteria are visible and numbered.

This prevents:

- forgotten criteria,
- improvised testing,
- over-focus on whatever looks interesting first,
- false completion.

---

## Stage 3 — Environment Readiness

Before blaming application code, verify the environment.

Check, when relevant:

- expected env vars exist,
- expected mode is active,
- target services are reachable,
- required migrations are applied,
- correct Supabase project is in use,
- expected bundle URL is configured,
- mock/live switch is intentional,
- browser session is valid,
- localStorage/session state is understood,
- required cloud permissions exist.

### Field lesson

A fast 500 may be missing configuration rather than an upstream failure.

A missing panel may be a missing table rather than missing code.

A failed history call may be a stale session pointer rather than a connector regression.

**Environment triage comes before defect accusation.**

---

## Stage 4 — Automated Evidence Review

Run or independently verify the required automated checks.

Typical sequence:

1. targeted tests,
2. affected integration tests,
3. full regression suite,
4. TypeScript,
5. production build,
6. lint if part of project doctrine.

QA records:

- command,
- environment,
- result,
- relevant counts,
- failures,
- pre-existing failures,
- deviations from the engineer report.

Automated evidence should normally be collected before long exploratory manual work unless the acceptance spec requires a reproduction-first sequence.

---

## Stage 5 — Operator Manual QA

Manual QA is run **one test at a time**.

Do not dump a 25-step checklist on the Operator unless explicitly requested.

For each test:

1. QA explains the purpose briefly.
2. QA gives the exact action.
3. Operator performs it.
4. Operator reports or shows the result.
5. QA records PASS / FAIL / OBSERVATION.
6. Only then does QA move to the next test.

This is both more reliable and more accessible.

It prevents:

- skipped steps,
- ambiguous evidence,
- checklist fatigue,
- loss of sequence,
- accidental environment changes.

---

## Stage 6 — Exploratory QA

Passing the acceptance criteria is necessary.

It is not always sufficient.

After contract verification, QA deliberately probes adjacent risk.

Examples:

- switch mock → live without clearing state,
- switch agents repeatedly,
- hard refresh during loading,
- open a different browser profile,
- throttle network,
- force an upstream failure,
- test stale localStorage,
- clear one persisted pointer but not others,
- test rapid navigation,
- repeat the action after a cold start.

Exploratory QA must remain disciplined.

It is not permission for random wandering.

Probe the seams most likely to break:

- state boundaries,
- mode boundaries,
- auth boundaries,
- browser persistence,
- environment boundaries,
- timing,
- retries,
- external services,
- multi-tenant isolation.

---

## Stage 7 — Finding Classification

Every observation must be classified before action.

Possible classifications:

### A. Acceptance Failure

The module does not satisfy its accepted requirement.

Result:

> Current gate may FAIL.

### B. Regression

Previously working behavior broke because of this change.

Result:

> Current gate normally FAILS.

### C. Environment / Setup Issue

Behavior is caused by missing or incorrect configuration, migration, credentials, permissions, or target environment.

Result:

> Fix environment first; do not file a code defect until reproduced under correct setup.

### D. Pre-Existing Defect

The issue existed before this module and is proven unrelated.

Result:

> Record separately; do not falsely fail the module unless the current release policy requires it.

### E. Follow-Up Finding

A real issue discovered during exploratory QA that is outside the module's accepted scope and does not invalidate its acceptance criteria.

Result:

> Module may PASS WITH FOLLOW-UP FINDINGS.

### F. Architecture Enhancement

A better future design, not a current defect.

Result:

> Route to backlog / Architect. Do not reopen the module.

### G. Observation

Interesting behavior with insufficient evidence to call a defect.

Result:

> Record; investigate only if risk justifies it.

---

# 10. The Scope Protection Rule

One of QA's most important jobs is preventing a successful module from being reopened by unrelated discoveries.

During the ADK Harness verification, exploratory QA found that:

```text
Mock mode session state
        ↓
persisted in shared browser storage
        ↓
mode switched to Live
        ↓
mock session ID sent to live history endpoint
        ↓
502
```

That was real.

It was reproducible.

It deserved a follow-up FIX.

But it was **not** evidence that the original persistence fix had failed.

Therefore the correct disposition was:

> PASS WITH FOLLOW-UP FINDINGS

This distinction protects velocity without hiding defects.

QA must never use exploratory success as an excuse for scope creep.

QA must never use scope protection as an excuse to hide a dangerous defect.

---

# 11. Verdict Model

QA uses the following verdicts.

## PASS

All accepted criteria are independently verified.

No release-blocking defect remains.

## PASS WITH FOLLOW-UP FINDINGS

All accepted criteria pass.

QA discovered one or more real, non-blocking findings outside the module's acceptance scope.

Requirements:

- findings are documented,
- severity is assigned,
- owner or routing is known,
- no Critical or release-blocking High issue remains.

## PASS WITH KNOWN RISK

The accepted scope passes, but a known risk remains inside or adjacent to the release boundary.

Use sparingly.

Requires explicit Operator acceptance when the risk is meaningful.

## FAIL

An acceptance criterion fails, a regression is introduced, or a release-blocking defect exists.

## BLOCKED

QA cannot issue a verdict because required evidence, access, setup, data, credentials, decisions, or environments are unavailable.

---

# 12. Gate Q — Pre-Deployment Quality Gate

## Purpose

Prove the release candidate is fit to deploy.

Gate Q occurs after implementation and Engineer self-verification.

Gate Q is the QA umbrella.

Existing specialist gates remain valid inputs.

Example:

- Gate M = mobile/UI shell requirement
- Gate Q = full pre-deployment QA verdict

Gate Q does not rename Gate M.

---

## Gate Q Required Checks

### Scope + Contract

- [ ] Acceptance criteria exist.
- [ ] Each acceptance criterion is traceable to evidence.
- [ ] Forbidden zones were respected.
- [ ] No undocumented scope was added.
- [ ] Documentation/contracts match implementation where required.

### Ground Truth

- [ ] Test runner verified from disk.
- [ ] Relevant file paths / exports / routes verified.
- [ ] Environment names verified.
- [ ] Required recon exists or exception is documented.
- [ ] Engineer report was treated as claims, not proof.

### Automated Tests

- [ ] Targeted tests pass.
- [ ] Affected integration tests pass.
- [ ] Full required regression suite passes.
- [ ] TypeScript passes.
- [ ] Production build passes.
- [ ] No retry was added merely to obtain green.
- [ ] No test shadows source logic.
- [ ] Pre-existing failures are separated and evidenced.

### Manual Acceptance

- [ ] Each manual acceptance criterion was independently exercised.
- [ ] Expected and actual behavior match.
- [ ] Relevant browser persistence was checked.
- [ ] Relevant loading / error / recovery states were checked.
- [ ] Original bug reproduction was rerun for FIX modules.

### Security / Data

- [ ] Auth is server-enforced where required.
- [ ] Negative permission paths were tested where required.
- [ ] Tenant isolation was tested where applicable.
- [ ] Service-role paths remain isolated.
- [ ] Secrets are not in browser bundles or evidence.
- [ ] PHI/PII test handling is approved.
- [ ] Error responses do not leak protected internals.

### UI / Accessibility

When applicable:

- [ ] Gate M passes.
- [ ] 375 / 768 / 1024 behavior verified.
- [ ] shell remains stable.
- [ ] loading / empty / error / success states verified.
- [ ] keyboard-critical path checked.
- [ ] no global overlay blocks navigation unexpectedly.

### Deployment Readiness

- [ ] Approved commit/artifact is identified.
- [ ] Required env changes are documented.
- [ ] Required migrations are documented.
- [ ] Setup order is documented.
- [ ] rollback path is documented.
- [ ] Gate D plan exists before deployment.

---

# 13. Gate D — Deployed-Environment Verification

## Purpose

Prove the deployed system works in its real target environment.

A successful deploy command is not Gate D.

A healthy container is not Gate D.

A green build is not Gate D.

Gate D verifies the actual deployed revision.

---

## Step D1 — Identify the Deployment

Record:

- repository,
- branch,
- commit SHA,
- build ID,
- image digest when available,
- Cloud Run revision or equivalent,
- environment,
- URL,
- deployment time.

Do not QA an unidentified deployment.

---

## Step D2 — Availability

- [ ] DNS resolves.
- [ ] HTTPS is valid.
- [ ] expected URL loads.
- [ ] correct service/revision serves traffic.
- [ ] health endpoint passes when present.

---

## Step D3 — Auth + Session

When applicable:

- [ ] login works,
- [ ] correct role resolves,
- [ ] navigation renders,
- [ ] navigation survives route changes,
- [ ] session survives hard refresh,
- [ ] protected routes reject unauthorized users,
- [ ] logout clears access,
- [ ] back-button behavior is safe,
- [ ] incognito behavior is correct.

---

## Step D4 — Core Workflow

Walk the shortest critical production-like path.

Examples:

- user opens agent and receives reply,
- history restores,
- pharmacy reads its own claims,
- tenant A cannot read tenant B,
- Liberty import reaches expected staging state,
- PDF generates and stores,
- signed URL authorizes correctly,
- subscription state updates.

---

## Step D5 — Environment Dependencies

Verify affected dependencies:

- Secret Manager,
- Supabase,
- GCS,
- service account IAM,
- Cloud Run env vars,
- custom domains,
- OAuth callbacks,
- external APIs,
- webhooks,
- scheduled jobs,
- email,
- CORS,
- timeout limits,
- file-size limits.

---

## Step D6 — Timing + Race Conditions

Where relevant:

- repeat hard refresh,
- test cold start,
- throttle network,
- delay upstream responses,
- navigate rapidly,
- switch agents,
- switch sessions,
- inspect loading behavior,
- inspect failed network calls,
- verify shell remains usable.

Latency is not only a performance concern.

Latency exposes race conditions hidden by localhost.

---

## Step D7 — Logs + Observability

- [ ] no new Critical / High errors,
- [ ] no secret leakage,
- [ ] no PHI/PII leakage,
- [ ] expected audit/log events exist,
- [ ] failures are diagnosable,
- [ ] alerting works when in scope.

---

## Step D8 — Regression Smoke

Minimum:

- [ ] auth,
- [ ] navigation,
- [ ] primary read,
- [ ] primary write when applicable,
- [ ] one negative authorization path,
- [ ] one error path,
- [ ] original bug reproduction for FIX work.

---

## Step D9 — Rollback Readiness

- [ ] prior stable revision identified,
- [ ] rollback action known,
- [ ] database compatibility understood,
- [ ] destructive migration recovery approved.

---

# 14. The Final Environment Reset Rule

QA must not leave the system in a test-only or broken state.

Before issuing the final verdict, verify the final operating configuration.

Examples:

- mock mode returned to live,
- temporary broken URL restored,
- throttling disabled,
- test-only feature flag reset,
- temporary credentials removed,
- browser storage cleaned only where intended,
- dev server restarted with production-intended local settings,
- no temporary bypass remains.

The final environment state is itself a QA criterion.

### Field lesson

After mock-mode and failure-injection testing, QA explicitly verified:

```text
NEXT_PUBLIC_CHAT_MODE=live
ADK_BUNDLE_URL=<expected live bundle>
```

That final check prevented a technically passing QA run from handing back a broken workstation.

---

# 15. Manual QA Protocol — One Test at a Time

The standard operator-assisted loop:

```text
QA Lead:
"Test X1. Select Jarvis, refresh, tell me which agent returns."

Operator:
"Jarvis returned."

QA Lead:
"X1 PASS. Now X2..."
```

Rules:

- explain purpose before action,
- give one action set,
- wait for result,
- classify immediately,
- record before moving on,
- never assume what the Operator saw,
- request screenshots/logs only when they add evidence,
- avoid huge command dumps unless explicitly requested.

This protocol is the default for accessibility and evidence quality.

---

# 16. Exploratory Probe Catalog

Use only the probes relevant to the module.

## Persistence

- refresh,
- hard refresh,
- browser restart,
- new browser profile,
- incognito,
- localStorage inspection,
- stale session pointer.

## Mode Boundaries

- mock → live,
- live → mock,
- feature flag on → off,
- local → cloud.

## Timing

- slow 3G,
- delayed upstream,
- cold start,
- rapid repeated action,
- double click,
- quick navigation.

## Failure Injection

- invalid URL,
- unavailable upstream,
- expired session,
- denied permission,
- malformed response,
- missing env var.

## Auth / Security

- wrong role,
- logged out,
- direct protected URL,
- cross-tenant request,
- stale cookie,
- cleared browser storage.

## State Isolation

- agent A → agent B,
- session A → session B,
- tenant A → tenant B,
- user A → user B.

## Recovery

- restore config,
- refresh,
- retry,
- logout/login,
- clear only affected state,
- redeploy known-good revision.

Exploration should target seams.

Not random UI wandering.

---

# 17. Defect Report Standard

Every real defect must include:

1. ID
2. title
3. module / release
4. severity
5. classification
6. environment
7. preconditions
8. exact reproduction
9. expected result
10. actual result
11. evidence
12. suspected cause — only if labeled INFERENCE
13. scope impact
14. gate impact
15. owner
16. retest requirement

Example:

```markdown
## QA-F09 — Mock session pointer contaminates Live mode

**Severity:** Medium  
**Classification:** Follow-Up Finding  
**Environment:** Local Next.js harness  
**Precondition:** Calc Agent has an active mock session persisted

**Reproduction**
1. Run app in mock mode.
2. Use Calc Agent.
3. Switch app to live mode without clearing persisted agentSessions.
4. Open Calc Agent.

**Expected**
Live mode creates or resolves a live-compatible session.

**Actual**
The app sends a `mock-session-*` ID to the live history endpoint and receives 502.

**Evidence**
- localStorage contains `mock-session-*`
- live history request payload contains same ID
- request returns 502

**Scope Impact**
Does not invalidate FIX-002 acceptance criteria.

**Gate Impact**
Non-blocking follow-up.

**Route**
Dedicated FIX recommended.
```

---

# 18. Defect Severity

## Critical

Always blocks Gate Q and Gate D.

Examples:

- unauthorized PHI/PII access,
- privilege escalation,
- corrupted claims,
- wrong reimbursement totals,
- broken payments,
- destructive cross-tenant writes,
- system-wide outage.

## High

Normally blocks release.

Security, privacy, financial, tenant-isolation, and data-integrity High defects should be treated as blockers unless the Operator explicitly accepts a tightly contained risk.

## Medium

May ship only when:

- impact is understood,
- workaround or containment exists,
- owner is assigned,
- follow-up is scheduled.

## Low

May ship when behavior is documented.

Severity is based on impact.

Not effort.

---

# 19. Regression Doctrine

The regression suite compounds with the product.

Rules:

- every confirmed defect earns regression protection when practical,
- every critical workflow keeps stable coverage,
- full required regression runs before Gate Q,
- flaky tests are defects,
- retries remain zero unless Factory doctrine changes,
- dead features do not deserve immortal tests,
- obsolete tests are removed only with documented feature retirement,
- assertions are never weakened merely to restore green,
- current-change failures must be fixed,
- pre-existing failures must be proven and separated.

A test suite should become more trustworthy over time.

Not merely larger.

---

# 20. QA Deliverables

Every meaningful BIM, FIX, FEAT, or release should produce or reference:

1. `ACCEPTANCE_SPEC.md` or equivalent acceptance criteria,
2. Engineer completion report,
3. `QA_PLAN.md`,
4. automated test evidence,
5. manual verification evidence,
6. exploratory findings,
7. `GATE_Q_REPORT.md`,
8. `GATE_D_CHECKLIST.md`,
9. `GATE_D_REPORT.md`,
10. defect reports,
11. known-risk / follow-up section,
12. retrospective input.

For small changes, multiple items may live in one file.

The file count may shrink.

The evidence may not disappear.

---

# 21. QA Plan Template

```markdown
# QA PLAN: [Module / Release]

## 1. Mission
What Engineering claims is complete.

## 2. Contract
Accepted scope and acceptance specification.

## 3. Out of Scope
What QA will not use to fail this module.

## 4. Sources of Truth
- Acceptance spec:
- Recon:
- Data contract:
- Relevant playbooks:
- Engineer handoff:

## 5. Environment Readiness
- Required env:
- Required migrations:
- Required services:
- Required accounts / roles:
- Required test data:

## 6. Risk Review
- Security:
- Privacy:
- Data integrity:
- Financial:
- Tenant isolation:
- Timing:
- External dependencies:
- Rollback:

## 7. Acceptance Traceability

| ID | Acceptance Criterion | Layer | Exact Check | Environment | Result |
|---|---|---|---|---|---|

## 8. Regression Scope
Existing behaviors that must remain green.

## 9. Automated Checks
Commands and expected evidence.

## 10. Manual Checks
One-test-at-a-time operator sequence.

## 11. Exploratory Probes
Only the seams relevant to this change.

## 12. Known Gaps
Missing access, data, environment, credentials, or decisions.

## 13. Exit Criteria
Evidence required for PASS.
```

---

# 22. QA Acceptance Report Template

```markdown
# QA ACCEPTANCE REPORT: [Module / Release]

## Executive Verdict

**Verdict:**  
[PASS | PASS WITH FOLLOW-UP FINDINGS | PASS WITH KNOWN RISK | FAIL | BLOCKED]

## Scope Verified

## Environment

- Repo:
- Branch:
- Commit:
- Build:
- Revision:
- URL:
- Mode:
- Date:

## Acceptance Results

| ID | Result | Evidence | Notes |
|---|---|---|---|

## Automated Evidence

| Command | Environment | Result | Evidence |
|---|---|---|---|

## Manual Evidence

| Test | Result | Observation |
|---|---|---|

## Exploratory Findings

| ID | Severity | Classification | Blocking? | Route |
|---|---|---|---|---|

## Pre-Existing Issues

## Environment / Setup Issues

## Known Risks

## Gaps / Untested Areas

## Gate Q Verdict

## Gate D Verdict

## Final Environment State

## Release Recommendation

## Approvals

QA Lead:  
Operator:
```

---

# 23. FIX Verification Protocol

FIX modules require one extra rule:

> Reproduce before repair whenever practical.

QA sequence:

1. confirm original bug behavior or evidence,
2. capture reproduction,
3. Engineering applies fix,
4. rerun original reproduction,
5. verify intended corrected behavior,
6. test nearest regression paths,
7. run required full suite,
8. perform exploratory probes around the mechanism,
9. issue verdict.

For a FIX, "the tests are green" is weaker evidence than:

> "The original failure mechanism was reproduced, the same path now passes, and regression remained green."

---

# 24. BIM / FEAT Verification Protocol

For BIM and FEAT work:

1. verify acceptance contract,
2. verify required environment setup,
3. verify primary path,
4. verify state persistence where applicable,
5. verify error path,
6. verify negative permission path where applicable,
7. verify mock/live or adapter boundaries where applicable,
8. verify regression,
9. probe adjacent seams,
10. restore final environment.

Backend modules often fail at seams rather than core logic.

QA should test the seams deliberately.

---

# 25. Environment Failure vs Code Failure

Before filing a code bug, ask:

1. Is the correct env var present?
2. Is the correct service URL configured?
3. Is the expected database migration applied?
4. Is the expected service account authorized?
5. Is the app in the intended mode?
6. Is stale browser state influencing the request?
7. Is the target upstream healthy?
8. Is the deployed revision the one we think it is?

Only after those are grounded should QA label the application defective.

This rule prevents false reds.

---

# 26. Browser State Is Part of the System

Modern web apps persist meaningful state in:

- cookies,
- localStorage,
- sessionStorage,
- IndexedDB,
- service workers,
- browser profiles.

QA must understand which state is:

- authoritative,
- a pointer,
- a cache,
- a convenience,
- safe to persist,
- unsafe to persist.

Example field lesson:

The ADK harness localStorage stored session pointers and selected agent state.

It did **not** store transcript content.

That distinction was itself an acceptance result.

Different browser profiles had different localStorage and therefore different visible session pointers.

That was an architectural observation, not automatically a defect.

---

# 27. Testing Mock Mode Is Mandatory When Mock Mode Ships

If the application contains a supported mock mode:

QA verifies it.

Why:

- frontend work depends on it,
- regression work depends on it,
- offline development may depend on it,
- deterministic testing may depend on it.

But QA also tests the mode boundary.

Mock and live state must not silently contaminate each other.

If the architecture intentionally shares state, the behavior must be documented and safe.

---

# 28. Failure Injection Is a First-Class QA Technique

QA should deliberately break dependencies when safe.

Examples:

- wrong bundle URL,
- missing env var,
- unavailable upstream,
- denied GCS permission,
- stale session,
- invalid auth,
- network delay.

Purpose:

- verify user-facing error wording,
- verify the shell survives,
- verify recovery is possible,
- verify logs are useful,
- verify failures are contained.

Failure injection is not chaos.

It is controlled evidence.

---

# 29. Security, Privacy, and Evidence Handling

For sensitive systems:

- synthetic or de-identified test data by default,
- never paste secrets into reports,
- redact tokens,
- redact emails where required,
- redact patient data,
- avoid PHI screenshots,
- verify audit logging without exposing protected content,
- store QA artifacts only in approved locations,
- test least privilege,
- test negative access,
- verify service-role credentials never reach browser code,
- treat unexpected cross-tenant access as Critical until disproven.

For Cyber Pharma specifically:

- tenant isolation,
- PHI boundaries,
- reimbursement correctness,
- reference-data integrity,
- auditability

are release-critical.

---

# 30. Production Confirmation

After staging passes and production is promoted, run a bounded non-destructive confirmation.

Minimum when applicable:

- correct production revision,
- DNS,
- HTTPS,
- login,
- session persistence,
- navigation,
- one safe core read,
- one safe negative authorization check,
- external integration heartbeat,
- logs free of new Critical errors.

Do not perform destructive actions merely to prove production works.

Do not use real PHI merely to prove deployment.

---

# 31. Retrospective + Doctrine Promotion

After a meaningful QA run, capture:

- escaped defects,
- false positives,
- weak acceptance criteria,
- missing environment setup,
- misleading engineer claims,
- tests that caught real bugs,
- tests that added noise,
- environment-only failures,
- exploratory probes that paid off,
- manual steps worth automating,
- repeated operator friction.

Then classify each lesson:

### Project-Specific

Keep in project docs.

### Module-Specific

Keep in module retrospective.

### Factory Structural

Promote into:

- QA playbook,
- testing playbook,
- bug-fix playbook,
- anti-patterns,
- templates,
- CI,
- static checks,
- deployment skills,
- monitoring.

The Factory compounds only when lessons change future behavior.

---

# 32. Definition of QA Complete

QA is complete only when:

- [ ] accepted criteria exist,
- [ ] QA plan exists,
- [ ] environment is ready,
- [ ] engineer claims are independently checked,
- [ ] automated evidence is captured,
- [ ] manual criteria are verified,
- [ ] relevant exploratory probes are complete,
- [ ] findings are classified,
- [ ] regressions are checked,
- [ ] Gate Q verdict is issued,
- [ ] Gate D verdict is issued when deployed,
- [ ] final environment state is restored and verified,
- [ ] Critical defects are zero,
- [ ] blocking High defects are zero,
- [ ] follow-up findings are routed,
- [ ] known risks are documented,
- [ ] QA acceptance report is written,
- [ ] Operator receives a clear release recommendation.

---

# 33. Definition of Release Complete

A release is complete only when:

- [ ] approved scope exists,
- [ ] acceptance criteria exist,
- [ ] Engineer self-verification is complete,
- [ ] Gate Q passes,
- [ ] approved revision is deployed,
- [ ] deployed identity is recorded,
- [ ] Gate D passes,
- [ ] production confirmation passes when required,
- [ ] no unresolved Critical defect exists,
- [ ] blocking High defects are resolved,
- [ ] accepted risks are documented,
- [ ] follow-up defects are routed,
- [ ] final environment state is correct,
- [ ] changelog is updated,
- [ ] retrospective inputs are captured,
- [ ] Operator approves completion.

---

# 34. QA Anti-Patterns

## Engineer Self-Certification

"The engineer says it works."

Not a QA verdict.

---

## Acceptance-by-Test-Count

"197 tests passed."

Useful evidence.

Not proof that the acceptance criteria were tested.

---

## Checklist Dump

Giving the Operator 30 manual steps at once.

Use one-test-at-a-time execution by default.

---

## Environment Blindness

Calling a code defect before verifying env, migrations, permissions, mode, and stale browser state.

---

## Happy Path Only

Ignoring:

- errors,
- wrong roles,
- stale state,
- slow network,
- recovery,
- mode changes.

---

## Mocking the Claim

Mocking the exact dependency the test claims to prove works.

---

## Retry Green

Adding retries to hide flakes.

---

## Scope Explosion

Reopening a passed module because exploratory QA found an unrelated enhancement.

Classify it.

Route it.

Protect the current contract.

---

## Scope Excuse

Calling a serious security or data-integrity issue "out of scope" to preserve a green verdict.

Critical risk overrides convenience.

---

## Root-Cause Theatre

Inventing a confident cause without enough evidence.

Label it INFERENCE.

---

## Build Equals Release

A successful build or deploy command is not release verification.

---

## Unidentified Deployment

Testing a URL without knowing the commit/revision behind it.

---

## Test-Mode Residue

Leaving the application in mock mode, broken env mode, throttled network, or temporary bypass state after QA.

---

## PHI in Evidence

Protected data in screenshots, logs, tickets, chat, or reports.

Automatic process failure.

---

# 35. Field Lessons That Promoted v0.1 → v1.0

The following lessons came from real App Factory QA work and are now doctrine.

## L-QA-001 — Engineer reports are claim packages

Detailed handoffs accelerate QA but never replace independent verification.

## L-QA-002 — Acceptance specs are executable contracts

Every acceptance criterion must map to a test or an explicit GAP.

## L-QA-003 — Manual QA works best one test at a time

Operator-assisted testing is clearer, more accessible, and produces better evidence when each check is closed before the next begins.

## L-QA-004 — Environment drift creates false reds

Verify config, migrations, services, mode, browser state, and permissions before blaming implementation.

## L-QA-005 — Exploratory QA must test seams

The most valuable finding in the ADK harness came from switching Mock → Live with persisted session state.

The acceptance spec alone did not reveal it.

## L-QA-006 — A real finding does not automatically reopen the module

Out-of-scope, non-blocking findings become follow-up work.

This preserves velocity without hiding defects.

## L-QA-007 — Browser persistence is architecture

localStorage, cookies, browser profiles, and session pointers must be understood as part of the runtime system.

## L-QA-008 — Failure injection belongs in QA

Breaking a dependency safely can verify error wording, recovery, shell stability, and observability faster than waiting for a natural failure.

## L-QA-009 — Final environment state must be verified

QA is not complete until temporary test configuration is removed and the intended operating mode is restored.

## L-QA-010 — Automated green is necessary, not sufficient

Jest, TypeScript, and production build all passed during the field run.

Manual and exploratory QA still found behavior worth fixing.

That is the reason the QA seat exists.

---

# 36. Version History

| Version | Date | Change |
|---|---|---|
| 0.1 | 2026-08-04 | Initial draft. Defined QA roles, evidence discipline, risk-based planning, Gate Q, Gate D, production confirmation, deliverables, defect routing, regression doctrine, security/privacy handling, and release-complete criteria. |
| 1.0 | 2026-08-10 | Promoted after hands-on ADK Next.js Harness QA. Adds Engineer Handoff as Claim Package, Acceptance Spec contract extraction, one-test-at-a-time manual protocol, environment-readiness triage, exploratory seam testing, explicit finding classifications, PASS WITH FOLLOW-UP FINDINGS, scope-protection doctrine, browser-state testing, mock/live boundary testing, failure injection, final environment reset verification, field-tested FIX/BIM protocols, and 10 promoted field lessons. |

---

# 37. Closing Doctrine

The App Factory does not need QA to prove that engineers make mistakes.

It needs QA because complex systems can be locally correct and globally wrong.

A component can pass.

A build can pass.

A deployment can succeed.

And the user can still be broken.

The QA department exists to independently close that gap.

**Engineering ships a claim.**

**QA ships the evidence.**

**The Operator decides whether the Factory releases.**
