# CHUNK 03 — BUILD METHOD REVIEW

## 1. STATUS

COMPLETE — all nine primary doctrine files examined; findings, scores, coverage, and handoff finalized. Branch verified as `factory-docs-review-astra-w-chunks`. Written incrementally and completed on 2026-09-12.

Session limitation: the requested brand-new Astra High session/model setting cannot be independently verified or changed from inside this thread. The limitation was disclosed before examination; the user directed continuation after a network interruption. This status certifies completion of the bounded review, not the external session setting.

## 2. SCOPE

Objective: determine whether the current Factory build/change/QA methodology can take bounded approved work through recon, implementation, verification, independent QA, remediation, deployment handoff, and closure.

Primary scope: every current substantive Markdown doctrine file in `03_BUILD_METHODOLOGY/`: `APP_FACTORY_SKILLS_PLAYBOOK.md`, `BIM_PLAYBOOK.md`, `BUG_FIX_PLAYBOOK.md`, `FEAT_PLAYBOOK.md`, `FFM_PLAYBOOK.md`, `FRONTEND_BUILD_PHASE_PLAYBOOK.md`, `FRONTEND_FIRST_PLAYBOOK.md`, `QA_PLAYBOOK.md`, and `TESTING_PLAYBOOK.md`.

Only permitted supporting references: `01_CONSTITUTION/` and `02_PIPELINE_AGENTS/`, when necessary to verify authority or ownership. Excluded: Run 001 material, other reviewers' findings, disposition and synthesis material, other chunk reviews, implementation, doctrine changes, commits, pushes, and Chunk 04. References embedded in current doctrine are evidence about that doctrine, not permission to open excluded artifacts.

Review controls read: the complete `astra-review/run-002/packets/CHUNK_REVIEW_CONTRACT.md` and only the Chunk 03 entry of `astra-review/run-002/packets/EXECUTION_PLAN.md`. The only authorized write target is this report.

## 3. DOMAIN MODEL

The intended process is evidence-first and supervised:

1. **Select and bound the work.** FFM packages frontend work against contracts/mocks; BIM makes a backend real behind a seam; FIX repairs a named defect mechanism; FEAT adds user-facing capability without taking over a new backend seam. The Architect and Operator define scope, forbidden paths, gates, and acceptance requirements. FEAT inherits BIM mechanics, while shared identity and QA authority live above both.
2. **Recon before commitment, verify again at the point of change.** BIM/FFM require current recon before executable authoring. FIX adds reproduction and mechanism evidence. The kit audit and source-before-test rules check facts again before writing. Future phases remain seeds until prior closure/lessons and fresh recon exist.
3. **Execute only the approved stage.** BIM/FIX/FEAT use a manager, Plan Mode, bounded writable surfaces, baseline/final regression, and explicit stops. FFM supplies discovery, contract/type, service, mock, component, and verification work; the frontend-stage playbook supplies layout through demo refinement. Their unresolved inner mapping is C03-D10.
4. **Separate Engineering claims from independent verification.** Acceptance criteria are seeded before implementation. Engineering finalizes the handoff; QA extracts ACs, verifies setup, checks automated evidence, conducts manual and exploratory probes, and owns the verdict. The Operator adjudicates scope/risk and release decisions; the Architect advises on routing.
5. **Deploy and close with evidence.** Gate Q precedes deployment; deployment-dependent work requires Gate D against an identified revision, plus bounded production confirmation when applicable. QA restores test-altered configuration. FIX/BIM closure includes regression, findings routing, retrospectives, and lessons. BIM explicitly permits a documented Gate D N/A when deployment is outside scope.
6. **Make the procedure repeatable.** Skill doctrine separates a manager from methodology, provides single/family organization, requires context discovery and appropriate approval, and tests activation in a fresh context. The testing playbook supplies the test layers and evidence recipes.

These are the written intended mechanics, not a claim that every recipe implements them consistently. The defects below identify where execution diverges.

## 4. FIVE-DIMENSION SCORECARD

| Dimension | Score | Evidence-based justification |
|---|---:|---|
| Correctness | 3 | Service seams, layered testing, negative paths, environment triage, and independent QA are sound. Unconditional webhook acknowledgment, full-error logging, and defective helper/fixture examples materially weaken the operational recipes (D05–D06, D11–D12). |
| Consistency | 2 | Scope exceptions, folder freeze versus spec maintenance, greenfield authoring, auth wrapping, and competing scope authorities give incompatible instructions (D01–D04, D07, D13). |
| Completeness | 3 | Recon through Q/D, failure investigation, rollback readiness, final-state restoration, and closure are substantially covered. Acceptance-artifact integration, greenfield sequencing, safe E2E targets, and the inner execution crosswalk remain incomplete (D03, D07–D08, D10). |
| Executability | 2 | Boot prompts, numbered gates, templates, and manual QA sequencing help execution. A competent agent still needs unstated exceptions to update frozen artifacts, fulfill a greenfield shell, interpret overlapping phases, or use several test recipes reliably. |
| Maintainability | 2 | Canonical homes, version histories, and FEAT's delta-only inheritance help. FFM copies rules into guides, trees, checklists, and stubs; demonstrated mismatches and stale gate pointers show manual synchronization is already failing (D02–D03, D07, D10, D13–D14). |

Scores apply only to this chunk. A strong QA policy does not make an inconsistent lower-level recipe safe automatically.

## 5. WHAT IS STRONG

| Practice | Evidence | Operational value and what to preserve |
|---|---|---|
| **Acceptance is agreed before implementation; QA designs its own attack.** | BIM §8; FEAT §2; BUG_FIX §18; QA §§3, 6–8. | Prevents implementation from redefining success and keeps green tests separate from a verdict. Preserve pre-implementation criteria, independent traceability, and approval for requirement changes. |
| **Recon and just-in-time authoring constrain assumptions.** | BIM §§5–6; FFM §§6–7; FRONTEND_FIRST §0; BUG_FIX §§5–7. | Prevents executable plans from being authored against a future or imagined repository. Preserve evidence provenance, TO VERIFY FIRST, defect reproduction, and explicit uncertainty. |
| **Regression evidence must prove behavior rather than a copy.** | TESTING §§1.2–1.3, 1.10, 2.2, 3.4, 3.8; BUG_FIX §§10–11; FEAT §4. | Cheapest-effective-layer selection, call/argument assertions, baseline checks, and no weakened assertions reduce false confidence. Preserve them while correcting the contradictory workaround and webhook recipes. |
| **QA tests environment, state, and failure boundaries.** | QA §§9, 13–16, 26–30. | Setup triage avoids false code accusations; mode switches, persistence checks, timing probes, and final-state restoration catch failures a happy-path suite misses. Preserve controlled injection, negative paths, and one-test-at-a-time operator-assisted checks. |
| **Deployment identity and rollback readiness are part of done.** | BIM §§6, 10, 12; BUG_FIX §§12–13, 20; QA §§12–14, 32–33. | Prevents a passing local build or anonymous URL from standing in for a verified release. Preserve deployed identity, environment-sensitive verification, tested BIM fallback switches, and migration-recovery decisions. |
| **Frontend mobile checks execute with the screen.** | FFM §13.1; FRONTEND_BUILD_PHASE §§4, 9. | Gate M catches missing mobile access before work advances; desktop-frame checks catch a separate class of layout failures. Preserve same-stage gates, reachable navigation, both themes, and concrete viewport checks. |
| **Scope protection distinguishes defects from enhancements.** | BUG_FIX §§3, 9; FEAT §§3–4; QA §§9–11, 18, 34. | Keeps nonblocking discoveries from reopening accepted work while retaining Critical-risk blocking. Preserve per-finding routing, the five QA verdicts, and Operator risk ownership. |
| **Reusable skill managers are tested as entry points.** | APP_FACTORY_SKILLS §§3–7, 9, 12, 15–16. | Single/family management, explicit discovery, versioned behavior, and fresh-context activation testing reduce dependence on remembered prompts. Preserve the distinction between operator-guided and delegated work, including compressed interaction for Agent Skills. |

## 6. PRIORITY FINDINGS

1. **C03-D05 — BLOCKER:** unconditional webhook success acknowledgment lacks a durable-processing/recovery requirement.
2. **C03-D06 — HIGH:** payment-error logging retains the sensitive information the response tests exclude.
3. **C03-D08 — HIGH:** privileged E2E setup/cleanup lacks a verified test-project boundary.
4. **C03-D04 — HIGH:** post-action ratification and inline-fix recipes bypass the prior scope-approval rule.
5. **C03-D09 — HIGH:** production-script suppression can turn an unverified integrated flow into apparently passing E2E evidence.

Totals: **14 defects — 1 BLOCKER, 8 HIGH, 4 MEDIUM, 1 LOW.** **3 suggestions**, separately ranked below.

## 7. RANKED DEFECTS

Ranked by severity, then operational impact. IDs retain the order in which findings were first persisted; they are not rank numbers. All short doctrine filenames in findings resolve under `03_BUILD_METHODOLOGY/` unless an explicit cross-reference path is given.

### C03-D05 — Webhook recipe acknowledges failure without requiring durable recovery

- **Classification:** DEFECT
- **Severity:** BLOCKER
- **Affected files / locations:** `TESTING_PLAYBOOK.md` Part 6, G5, lines 1594–1596; §2.2, lines 264–272; `BIM_PLAYBOOK.md` §7, line 113; `QA_PLAYBOOK.md` §§13, 18.
- **Evidence:** G5 prescribes that the webhook handler always returns 200 to prevent retries; processing tests check database-call shape instead of response status, except signature failures. No condition requires successful processing, durable event capture, or a separate retry/reconciliation mechanism before acknowledging. The same testing playbook requires expected- and unexpected-upstream-failure coverage at service boundaries. BIM requires the contract to decide failure behavior for financial and data-integrity dependencies; QA treats corrupted financial state as Critical.
- **Why this is a defect:** a database write can fail after a valid webhook arrives. The stated recipe still sends its success acknowledgment and tests only that a call was made. Successful acknowledgment can be sound after durable capture, but the rule does not require that prerequisite or test recovery. This finding concerns the unconditional doctrine, not an assertion that either example application has lost an event.
- **Operational consequence:** payment/subscription state can remain wrong after a transient processing failure while the handler and its tests appear successful. Required recovery may be lost at the event boundary.
- **Recommended resolution:** define acknowledgment per the approved event-processing contract. Require proven processing or durable acceptance before success, with idempotency and recovery/reconciliation for deferred or failed work. Test persistence failure, duplicate delivery, and recovery as well as call shape. Remove the universal always-200 rule.

### C03-D06 — Payment-error recipe moves sensitive data into logs

- **Classification:** DEFECT
- **Severity:** HIGH
- **Affected files / locations:** `TESTING_PLAYBOOK.md` §4.3, lines 1217–1248; `QA_PLAYBOOK.md` §13/D7, lines 893–901, and §29, lines 1488–1503.
- **Evidence:** TESTING explicitly says payment errors can contain card details, customer emails, and internal request IDs, then mandates logging the full error server-side and demonstrates `console.error("Stripe Error:", error)`. Its defensive test checks only the response body. QA requires no secret or PHI/PII leakage in logs and redaction in evidence.
- **Why this is a defect:** moving the original sensitive error from the response into persistent logs does not satisfy the written leakage boundary. The recipe contains no redaction or approved-field restriction and its test does not exercise that boundary.
- **Operational consequence:** the user-visible response is safe while protected information enters log storage and later diagnostics or QA evidence. No actual sensitive log contents were inspected in this review.
- **Recommended resolution:** define an approved structured error record, redact sensitive fields before logging, and assert both response and log behavior with synthetic sensitive markers. Preserve enough sanitized context for diagnosis.

### C03-D08 — Mutating E2E helpers lack an enforced test-environment boundary

- **Classification:** DEFECT
- **Severity:** HIGH
- **Affected files / locations:** `TESTING_PLAYBOOK.md` §4.1, lines 876–950; §4.4, lines 1258–1363; `QA_PLAYBOOK.md` §§12, 29–30.
- **Evidence:** the E2E recipe registers users, seeds subscriptions using an admin client, and deletes subscription/role/user records. The admin client uses whatever Supabase URL and privileged key are loaded from `.env.local`; no target-identity or dedicated-test-project check precedes mutation. Fixture doctrine likewise follows whichever configured backend is present and expressly describes dev → staging → prod regeneration. QA requires approved test-data handling and bounded, non-destructive production confirmation.
- **Why this is a defect:** read-only fixture discovery and an admin-powered mutation suite have different permissible environments, but the executable helper makes no such distinction. Synthetic email names and cleanup order help isolate records; they do not prove the backend is an approved mutation target. The finding does not claim fixture fetching itself writes production data.
- **Operational consequence:** switching environment configuration can direct account creation, synthetic subscription writes, and deletion into a production project. A localhost browser target does not establish where the admin client writes.
- **Recommended resolution:** require positive verification of the approved test project and test identity before privileged setup/cleanup; fail closed on unapproved targets. Separate production confirmation from mutating E2E execution, and retain cleanup restricted to identities created and recorded by the run.

### C03-D04 — Local exceptions permit implementation before scope approval

- **Classification:** DEFECT
- **Severity:** HIGH
- **Affected files / locations:** `BIM_PLAYBOOK.md` §7, line 111; `FEAT_PLAYBOOK.md` §2; `BUG_FIX_PLAYBOOK.md` §3, line 72; `TESTING_PLAYBOOK.md` §3.3, lines 629–637; `APP_FACTORY_SKILLS_PLAYBOOK.md` §13, Anti-Pattern 8.
- **Evidence:** BIM allows “any step outside the enumerated writable surface” when the Engineer considers it genuinely required, followed by ratification in the report; the parenthetical example is limited to test/build configuration, but the operative sentence is not. FEAT imports that rule and FIX repeats ratification language. TESTING says newly discovered HIGH security findings should be fixed inline in the same session. Conversely, the skills manual permits only explicitly authorized modifications; BUG_FIX §§3, 9 require adjudicated, approved work and prohibit unrelated cleanup. `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md` §2.5, line 250, routes accepted findings to Engineering only as approved module content; `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md` §15 requires resolution before acting on conflicts.
- **Why this is a defect:** importance or implementation convenience becomes an alternate source of authority. Neither local exception requires confirmation that the additional source change was already approved. Reporting an action afterward cannot supply the prior approval other rules require.
- **Operational consequence:** a test-writing or FEAT session can modify protected configuration or adjacent security behavior before the Operator evaluates its scope and regression impact.
- **Recommended resolution:** allow execution only within explicitly approved conditional surfaces. For newly necessary changes, stop the affected work, present evidence and the minimal amendment, obtain approval, then proceed. Keep urgent security escalation prompt without treating severity as automatic implementation permission.

### C03-D09 — E2E workaround recipe can remove a shipped failure from the system being tested

- **Classification:** DEFECT
- **Severity:** HIGH
- **Affected files / locations:** `TESTING_PLAYBOOK.md` §§3.5–3.6 and Part 6/G11, especially lines 688–713 and 1634–1638; `QA_PLAYBOOK.md` §§11–12, 19, 34.
- **Evidence:** after confirming a troublesome script also exists in production, TESTING recommends aborting its network request or neutralizing its DOM-side-effect method during E2E. G11 presents these as prioritized fixes. Unlike §3.6's documented skip/mitigation path, that workaround path does not require an explicit reduced-coverage label or verification of the affected flow with the production script enabled. QA requires accepted behavior and regressions to pass and forbids treating green automation alone as completion.
- **Why this is a defect:** disabling a real production dependency can be useful for diagnosis or an isolated component test, but the resulting pass does not prove the integrated click flow. The recipe does not preserve that distinction when it calls the modification a fix for E2E failure. Documented skipping with a verified manual replacement is not itself the defect.
- **Operational consequence:** the automation goes green because the failure-producing behavior was removed from the test environment, while users still encounter it.
- **Recommended resolution:** label dependency-disabled runs as diagnostic/isolated evidence. Keep the original full-environment flow failed or explicitly blocked until fixed or independently verified through an approved compensating check, and carry the coverage limitation into Gate Q.

### C03-D03 — Handoff recipes do not consistently require the mandatory acceptance artifact

- **Classification:** DEFECT
- **Severity:** HIGH
- **Affected files / locations:** `FFM_PLAYBOOK.md` §§2–3, 12–13, 18, Appendix A; `QA_PLAYBOOK.md` §§6, 20; `BUG_FIX_PLAYBOOK.md` §18.
- **Evidence:** FFM's complete folder trees, required file guides, handoff diagram, and authoring checklist contain no `ACCEPTANCE_SPEC.md` creation/finalization step or QA intake handoff. The Engineer hands working code and a retrospective to the Operator (§2); verification ends in master sign-off (§13). QA §§6 and 20 accept acceptance criteria or an equivalent artifact. BUG_FIX §18 permits small fixes to combine artifacts into one document without preserving an explicit exception for the locked spec filename. In contrast, `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md` §2.5, lines 246–251, mandates the exact filename for every code-bearing module and mandatory Gate Q. `FRONTEND_BUILD_PHASE_PLAYBOOK.md` §9 does correctly require Q/D, so QA is not absent from frontend doctrine as a whole.
- **Why this is a defect:** an Architect can satisfy the self-described complete FFM authoring checklist without delivering a mandatory Factory artifact or establishing its pre-implementation ownership and finalization. QA's equivalent-artifact wording compounds the incompatible handoff paths. The explicit Factory-wide handoff rule establishes the governing requirement; it should not need to be rediscovered to repair the recipe.
- **Operational consequence:** FFM scope/gate files are improvised into a QA contract at completion, or QA rejects an otherwise checklist-complete module because the required contract is missing.
- **Recommended resolution:** add the acceptance-spec lifecycle and QA handoff to FFM's anatomy, authoring sequence, boot/verification instructions, and completion checklist. Reference the shared contract rather than copying its full contents; restrict equivalent/combined-artifact allowances to contexts the Factory rule actually exempts.

### C03-D01 — Whole-folder freeze conflicts with required working artifacts

- **Classification:** DEFECT
- **Severity:** HIGH
- **Affected files / locations:** `BIM_PLAYBOOK.md` §§4, 6–8; `BUG_FIX_PLAYBOOK.md` §§16, 18; `FEAT_PLAYBOOK.md` §2. Paths are under `03_BUILD_METHODOLOGY/`.
- **Evidence:** BIM places `ACCEPTANCE_SPEC.md` inside the module folder (§4, lines 48–55), freezes that folder at Engineer Plan Mode (§6, line 83), and says nothing inside may be added or edited by anyone from launch until STOP (line 103). Yet its Engineer must maintain the acceptance spec during implementation and finalize it at handoff (§8, lines 120–133). FIX likewise freezes the module folder while requiring a maintained spec (§§16, 18); FEAT imports these mechanics. The permitted authority check, `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md` §2.5, lines 246–249, confirms that maintenance/finalization is required.
- **Why this is a defect:** even an approved, criteria-preserving spec update violates the literal freeze. The outside-folder staging rule explicitly addresses Architect outputs; it does not define an Engineer working-artifact exception or a spec-finalization gate before handoff.
- **Operational consequence:** one Engineer edits the frozen folder; another delays required handoff artifacts or uses an undocumented staging convention. The claimed deterministic manager contract cannot be followed literally.
- **Recommended resolution:** decide which approved inputs are immutable and which evidence/output files remain writable. Define where Engineer updates are staged, who admits them, and when the spec is finalized relative to STOP. Preserve approval for requirement changes.

### C03-D07 — Greenfield DATA_CONTRACT ownership is corrected in a note but not in the execution recipe

- **Classification:** DEFECT
- **Severity:** HIGH
- **Affected files / locations:** `FFM_PLAYBOOK.md` §§7, 9.2, 12.4, 14, 18; `FRONTEND_FIRST_PLAYBOOK.md` §3.
- **Evidence:** FFM §7, line 579, correctly assigns the greenfield contract to the Engineer and says the Architect delivers a shell. But §12.4, lines 1296–1305, makes Discovery read-only and immediately proceeds to creating types from DATA_CONTRACT §4, without an explicit contract-authoring/approval step. §14's greenfield-with-related-evidence branch assigns contract authoring to the Architect again (lines 1435–1439); §18 still checks for a fully populated contract without a greenfield exception. FRONTEND_FIRST §3 requires the contract before mock UI. `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md` §3, lines 168–172, confirms the per-pipeline author of record.
- **Why this is a defect:** ownership is known; the greenfield sequence for fulfilling it is not executable as written. Following the detailed branch assigns the wrong author, while following the corrected note leaves the Engineer consuming an unfinished contract. Conversion's complete pre-authored contract is a valid different path.
- **Operational consequence:** types can be invented from a shell, approval can happen at inconsistent points, or work stops for an undocumented contract-authoring phase.
- **Recommended resolution:** give conversion and greenfield explicit branches in the authoring and execution sequence. For greenfield, place Engineer contract authoring and the relevant approval before type/service implementation; make the checklist accept a shell only at the specified earlier handoff.

### C03-D02 — FFM prescribes the auth wrapper that kit-consumption doctrine forbids

- **Classification:** DEFECT
- **Severity:** HIGH
- **Affected files / locations:** `FFM_PLAYBOOK.md` §§9.2, 12.4; `FRONTEND_FIRST_PLAYBOOK.md` §0; `FRONTEND_BUILD_PHASE_PLAYBOOK.md` §1.6.
- **Evidence:** FFM's auth service contract describes wrapping starter-kit `getUser()` and `signInWithPassword()` (§9.2), and its service sub-phase instructs Claudy to wrap the kit's data access in `/src/services/` (§12.4). FRONTEND_FIRST §0, lines 30–41, explicitly prohibits redundant `authService.ts` wrappers because the kit's auth already is the service layer; FRONTEND_BUILD_PHASE §1.6 repeats that rule. The authority/ownership check in `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md` §5, lines 261–278, explicitly assigns FFM anatomy and frontend-stage execution to these playbooks and reserves the service layer for project-specific domain logic.
- **Why this is a defect:** the copyable contract and sub-phase recipe reintroduce the named failure the mandatory kit audit is supposed to prevent. This is not a demand to remove legitimate domain-specific auth enrichment; FFM fails to distinguish such approved additions from wrapping complete kit behavior.
- **Operational consequence:** the Architect can hand off a contract that directs duplicate auth plumbing, forcing Engineer improvisation or an avoidable approval stop and creating divergence from kit security behavior.
- **Recommended resolution:** make direct kit-auth consumption the default and require recon-backed justification for genuinely missing domain behavior. Synchronize the sample contract and service-sub-phase instructions with that boundary.

### C03-D13 — FFM gives two different documents final scope authority

- **Classification:** DEFECT
- **Severity:** MEDIUM
- **Affected file / locations:** `FFM_PLAYBOOK.md` §9.1, line 745; §9.4/Cross-File Consistency, lines 928–949; Appendix C.1, line 2296.
- **Evidence:** §9.1 calls APP_BRIEF the single source of truth for in/out of scope. The copyable root-manager stub instead says `_project/CLAUDE.md` wins on scope. Other sections require duplicated forbidden zones to match.
- **Why this is a defect:** duplicate copies agreeing is an invariant, not a precedence rule for when they drift. In the exact conflict case where authority is needed, one instruction makes the brief authoritative and another makes the spine authoritative. The stub's residual STOP rule does not remove its explicit winner instruction.
- **Operational consequence:** an outdated spine can override newly approved brief scope, or the same disagreement produces a stop in one session and implementation in another.
- **Recommended resolution:** select a single scope authority and make all managers and stubs defer to it. Require unresolved disagreements to stop the affected work rather than treating a copied summary as an alternate source of approval.

### C03-D10 — The two frontend execution maps lack an operational crosswalk

- **Classification:** DEFECT
- **Severity:** MEDIUM
- **Affected files / locations:** `FFM_PLAYBOOK.md` §§11.3, 12.4–12.6, 13; `FRONTEND_BUILD_PHASE_PLAYBOOK.md` §§1.5, 2–9.
- **Evidence:** FFM defines Discovery → Types → Services → Mocks → Components → Verification, followed by retrospective; its Components sub-phase is identified as 4 at line 1028 but as 5 in the reuse instructions at line 1362. FRONTEND_BUILD_PHASE says its six stages must run in order: Layout → Fidelity → Polish → Subpages → Mock Functionality → Demo Deployment. Its Stage 0/Discovery note maps only the starting point. `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md` §5 assigns FFM anatomy and frontend-stage execution to these two documents, while the permitted `SOFTWARE_FACTORY_PLAYBOOK.md` §2 note maps only the higher lifecycle/build layers.
- **Why this is a defect:** the higher-level nesting is acknowledged, but the actual inner execution relationship is not specified. Most frontend stages plausibly fit within FFM Components, while demo deployment overlaps FFM Verification. The written instructions do not say whether those gates are shared, nested, or repeated, and one numeric reference is internally wrong.
- **Operational consequence:** two competent authors create different gate placements or duplicate verification/deployment, and recovery instructions naming a phase can resume at the wrong point.
- **Recommended resolution:** add one compact crosswalk with namespaced stage identifiers, parent stage, entry/exit artifacts, and approval owner. Correct the Components index and state where demo deployment and Q/D sit. Preserve each map's useful level of detail.

### C03-D12 — Fixture discovery can publish unusable roles and its consumer reads a different count field

- **Classification:** DEFECT
- **Severity:** MEDIUM
- **Affected file / locations:** `TESTING_PLAYBOOK.md` §§2.3, 4.4–4.5, especially lines 1310–1352 and 1391–1398.
- **Evidence:** discovery labels `products[0]` as the first published product, `.find(c => c.count > 0)` as the populated category, and a coupon selected only by expiry as valid. It checks neither role existence nor all relevant coupon prerequisites before writing success. JSON serialization silently drops undefined role values. The pagination consumer then checks `.product_count`, although discovery selected and preserved a record using `.count`, without a normalization step.
- **Why this is a defect:** an empty dataset produces valid, successfully written JSON containing empty role objects; module-top JSON parsing does not detect that semantic failure. Direct evaluation also shows a `{count: 1}` category does not trigger the shown `product_count <= 12` skip. The playbook itself describes additional coupon rules in §§2.1 and 3.7, so expiry alone cannot establish the role “valid.”
- **Operational consequence:** setup fails later as a misleading application-test failure, the wrong pagination case runs, or a supposedly valid coupon fixture violates the scenario under test.
- **Recommended resolution:** define and validate a normalized fixture schema and scenario eligibility before publishing; use a single count property. Missing required roles should produce an explicit setup/BLOCKED result. Record optional role absence deliberately rather than emitting a successful but incomplete fixture.

### C03-D11 — Metadata helper cannot distinguish absence from present null

- **Classification:** DEFECT
- **Severity:** MEDIUM
- **Affected file / location:** `TESTING_PLAYBOOK.md` §4.2, “Key-absent vs empty-value distinction,” lines 1069–1085.
- **Evidence:** the guidance requires distinguishing a missing key from a present empty/zero/null value. The sample returns `entry ? entry.value : null`. A missing key returns `null`; a present `{ key: "x", value: null }` also returns `null`.
- **Why this is a defect:** direct evaluation confirms identical outputs for the two cases the helper claims to distinguish. Empty string and zero do survive; null does not.
- **Operational consequence:** tests or consumers using the recommended helper cannot determine whether metadata was omitted or explicitly cleared, and may apply the wrong default/restriction.
- **Recommended resolution:** return an explicit presence/value result or a distinct absence sentinel with a documented contract. Include separate absent, null, zero, and empty-string examples.

### C03-D14 — Frontend completion checklist points to the wrong QA gate sections

- **Classification:** DEFECT
- **Severity:** LOW
- **Affected files / locations:** `FRONTEND_BUILD_PHASE_PLAYBOOK.md` §9, lines 458–459; `QA_PLAYBOOK.md` §§9–10, 12–13.
- **Evidence:** the checklist points Gate Q to QA §9 and Gate D to QA §10. Those sections are now QA Engagement Lifecycle and Scope Protection. The actual gate checklists are §12 (line 684) and §13 (line 774).
- **Why this is a defect:** these are operational references to required verification criteria, and both destinations are incorrect in the current repository.
- **Operational consequence:** an operator following the declared references must search again or misses the detailed gate checks. The named gates and nearby summary text reduce the impact; Q/D are not absent.
- **Recommended resolution:** point to the actual gate headings, preferably using stable heading links, and include these references in synchronization checks.

## 8. RANKED SUGGESTIONS

### C03-S01 — Add a repeated-remediation escalation rule

- **Classification:** SUGGESTION
- **Affected locations:** BIM §6; BUG_FIX §§4, 6, 11; QA §§3, 23–24.
- **Evidence / opportunity:** the correction → retest → regression loop exists, and scope/approval gates bound what can change. The reviewed doctrine does not set a repeated-failure trigger for re-recon, revised mechanism analysis, or a fresh plan.
- **Recommendation:** let the approved module define a time/attempt checkpoint and escalation owner. Repeated failure should trigger a conscious replan, not another identical attempt. No universal numerical cap is needed.
- **Expected value:** reduces churn and context loss without weakening independent retesting or creating an artificial release deadline.

### C03-S02 — Scale document ceremony to risk and actual content

- **Classification:** SUGGESTION
- **Affected locations:** APP_FACTORY_SKILLS §4 (3,000–8,000-word manager guidance), §§5, 8; FFM §§8–13, 17–18.
- **Evidence / opportunity:** required section coverage is useful, but fixed length expectations, repeated scope text, and multi-thousand-line FFM packages can consume effort even for simple work. The skill manual itself favors progressive disclosure; BIM already permits brief/contract consolidation for small modules.
- **Recommendation:** prefer completeness checks and a small/standard/complex packaging choice over minimum prose volume. Keep the manager concise, link stable doctrine, and retain expanded detail only where the task's risk needs it.
- **Expected value:** lower authoring and synchronization cost while preserving executable boundaries. This is a process improvement, not a claim that every long document is defective.

### C03-S03 — Carry one candidate/evidence manifest through Q, remediation, and D

- **Classification:** SUGGESTION
- **Affected locations:** BIM §6; QA §§6, 12–13, 22.
- **Evidence / opportunity:** approved commit/artifact identity and deployed identity are already required, but the information is spread across handoff, gate reports, and deployment records.
- **Recommendation:** reuse a compact manifest connecting scope/spec version, candidate identity, setup/migrations, gate evidence, and deployed identity. State which changes after QA require renewed checks or approval, including merge-induced differences.
- **Expected value:** makes it easier to demonstrate that the candidate being promoted is the candidate whose evidence was accepted; preserves existing role ownership.

## 9. CROSS-DOMAIN DEPENDENCIES

| Classification | Boundary | Bounded handoff |
|---|---|---|
| DEPENDENCY | Factory authority and module handoff | SOFTWARE_FACTORY_PLAYBOOK §2.5 supplies the authoritative exact acceptance filename, pre-implementation ownership, QA verdict chain, and Q requirement. D03–D04 require downstream recipes to honor that contract; this review does not revise the constitution. |
| DEPENDENCY | Engineer / Architect ownership | ENGINEER_PLAYBOOK §§3, 5, 15 supplies greenfield-versus-conversion ownership, kit consumption, and conflict/scope conduct. D02 and D07 are supported local recipe defects, not a full review of either role. |
| DEPENDENCY | Recon, kit capabilities, design package | Fresh recon, the kit audit, and Designer artifacts are essential build inputs. Their manuals, questionnaire, and installed skills were not opened. Their existence/correctness in a particular app is outside this review. |
| DEPENDENCY | Release and deployment operations | QA names DevOps/Deployment Operator as deployer; BIM names the Coordinator as owner of all git/cloud actions. A launch package must identify who fills those seats and how approved candidates reach their target branches/environments. Deployment implementations were not examined. |
| SYNTHESIS FLAG | Financial event reliability and sensitive logging | D05–D06 warrant checks against the owning backend/security domains and actual event/logging implementations. This review establishes unsafe build/testing recipes; it does not claim a specific app lost events or exposed data. |
| SYNTHESIS FLAG | Approval and promotion continuity | D04 and S03 affect the authority/evidence chain across testing, module scope changes, merge, and deployment. Carry these findings forward; do not infer the unexamined operations rules. |
| CONTRADICTION CANDIDATE | FFM scope and identity across lifecycle maps | FFM §6 uses an FFM even for a schema/RLS phase; BIM §1 describes FFM as frontend-before-backend and BIM as making seams real. The shared identity heading explicitly names BIM/FIX/FEAT and future types, while FFM already has its own naming scheme. Whether later-phase FFM means a generic wrapper and whether existing FFM naming is an exception require an explicit Factory ruling. No FFM-ID defect is asserted from the ambiguous scope of that heading. |

## 10. AMBIGUITIES / UNKNOWNS

- **Launch provenance:** this thread cannot create or independently verify a brand-new Astra High session or the externally selected reasoning level. The initial limitation was disclosed, and the user directed continuation after the network interruption. Substantive completion is distinct from certification of the UI/session setting.
- **Deployment seats in FFM:** FFM §2 lists deployed services/URLs as Engineer outputs and §12.4 includes deployment; QA §4 assigns deployment to DevOps/Deployment Operator. BIM/FIX explicitly use git-zero/cloud-zero. FFM does not spell out the same handoff. A deliverable owner may differ from the command executor, so this is left as an ownership clarification rather than a proven unauthorized-deployment instruction.
- **Remediation limits:** authority and scope are bounded, but no attempt/time escalation threshold was found in the examined lifecycle loops. S01 proposes an improvement; no universal retry count is invented.
- **Coverage substitutions:** documented skipping with an independently verified manual alternative can be valid. D09 concerns suppressing production behavior without preserving the resulting evidence limitation, not a blanket prohibition on mocks, isolation, or skips.
- **Actual runtime consequences:** no application, deployment, installed skill, secret, provider account, or external framework documentation was examined. Runtime/version-specific claims not established by the permitted evidence remain unverified. Findings about recipes identify what the written method permits or fails to require, not incidents in a running app.
- **Cross-domain implementations:** approved artifact storage, release-branch protection, migration procedures, and backend event-recovery mechanisms may exist elsewhere. They were not presumed absent and were not opened outside the permitted authority/ownership checks.

## 11. COVERAGE MANIFEST

All nine substantive current Markdown files discovered in the primary directory were examined completely, including appendices, templates, and current in-file provenance/history. No separate historical run, prior review, disposition, or synthesis artifact was opened. Line counts below use logical lines, including an unterminated final line.

| Primary file | Status | Logical lines |
|---|---|---:|
| `03_BUILD_METHODOLOGY/APP_FACTORY_SKILLS_PLAYBOOK.md` | EXAMINED | 1166 |
| `03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md` | EXAMINED | 184 |
| `03_BUILD_METHODOLOGY/BUG_FIX_PLAYBOOK.md` | EXAMINED | 737 |
| `03_BUILD_METHODOLOGY/FEAT_PLAYBOOK.md` | EXAMINED | 53 |
| `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md` | EXAMINED | 2643 |
| `03_BUILD_METHODOLOGY/FRONTEND_BUILD_PHASE_PLAYBOOK.md` | EXAMINED | 583 |
| `03_BUILD_METHODOLOGY/FRONTEND_FIRST_PLAYBOOK.md` | EXAMINED | 447 |
| `03_BUILD_METHODOLOGY/QA_PLAYBOOK.md` | EXAMINED | 1829 |
| `03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md` | EXAMINED | 1742 |

Supporting references (limited inspection, not substantive whole-file review):

- **CROSS-REFERENCE — `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md`:** targeted heading/authority search; §2 phase-vocabulary note and §2.5, lines 216–251, read to verify lifecycle-map authority and Factory-wide module/QA handoff ownership. This establishes the governing requirement for D03–D04 and bounds the FFM identity ambiguity.
- **CROSS-REFERENCE — `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md`:** targeted heading/ownership search; §3 conversion inputs and DATA_CONTRACT ownership, lines 155–172; §5, lines 237–278; and §15 through Dead Code Hygiene, lines 1139–1223. Opened to verify greenfield authorship, kit-consumption ownership, and the authority governing scope/conflict handling for D02, D04, D07, and D10.

Review controls, not doctrine cross-references: the complete Chunk Review Contract and only the Chunk 03 Execution Plan entry. Ancestor/directory AGENTS.md existence checks found no applicable instruction files. Initial broad combined output was truncated; subsequent bounded reads covered all omitted primary content before any file was marked examined.

Verification: exact source locations were rechecked; the pure `pickMeta` and fixture-selection/consumer expressions were evaluated without network or file writes. These checks confirmed D11–D12. No application test suite, deployment, or doctrine implementation was run.

Final checks passed: all 12 required sections present; five integer scores; 9/9 primary files examined; two supporting references logged with reasons; 14 unique defect IDs in severity order (1 BLOCKER / 8 HIGH / 4 MEDIUM / 1 LOW); three unique suggestion IDs. Branch unchanged. A before/after size/mtime/ctime comparison across 143 workspace files found only `astra-review/run-002/chunks/03_build_method/ASTRA_REVIEW.md` changed; tracked and staged diffs were empty. No other file was modified by this review. The pre-existing untracked `astra-review/` directory remained untracked.

## 12. SYNTHESIS HANDOFF

- **Strongest conclusion:** this domain has a substantial evidence-first, independent-QA lifecycle, but it cannot yet be followed reliably without correcting unsafe testing recipes and conflicting execution instructions. This is a build-method conclusion only.
- **Most serious defect:** C03-D05 — always-successful webhook acknowledgment is prescribed without making durable processing/recovery a prerequisite.
- **Most important strength to preserve:** acceptance agreed before implementation, Engineer claims separated from independent QA evidence, and Q/D verification tied to the actual environment.
- **Unresolved issue most likely to affect another domain:** continuity of scope and candidate approval through remediation, merge, and deployment, including explicit role assignment for FFM deployment and the evidence linkage in S03.
- **Findings deserving Factory-wide consideration:** D04 (scope authority), D03 (exact acceptance handoff), D05–D06 (financial recovery and sensitive logging), D08–D09 (safe test targets and honest coverage), and D01/D07/D10 (executable module transitions). Route them to their owning review stages; no disposition or synthesis is made here.

No doctrine repairs, implementation changes, commits, pushes, merges, other chunks, or synthesis were performed.

