# PART_03 — correction mapping draft

DRAFT FOR REVIEW — no execution approval. Source outcomes are not relabeled approved.

### FC-020 — TESTING webhook recipe acknowledges success unconditionally, without durable processing or recovery

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/03_build_method_corrections.md:30`):

- **Certified record:** CF-05 · Severity BLOCKER · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C03-D05 · Fable none
- **Evidence:** Astra C03 §7 C03-D05; Sol C03 §3 ("Accept as BLOCKER"; keep separate from the Chunk 05 finding until synthesis because the doctrine owners differ) and §9.A.
- **Defect surfaces (`0a787cb`):**
  - `03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md`: Part 6 G5, §2.2
  - `03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md` §7
  - `03_BUILD_METHODOLOGY/QA_PLAYBOOK.md` §§13, 18
- **Defect:** G5 tells the webhook handler to always return 200 to prevent retries. Processing tests check call shape, not persistence outcome. Nothing requires durable capture, processing success or reconciliation before acknowledging, so a valid event whose business write fails is acknowledged and can be lost.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - TESTING no longer prescribes unconditional success acknowledgment.
  - Acknowledgment follows the approved event-processing contract (DEC-03), which separates two failure phases:
    - **Before durable acceptance.** The handler acknowledges success only after the required state transition has completed, or the event/work has been durably captured or enqueued. If that fails, the response is a retryable non-success, so the provider redelivers.
    - **After durable acceptance.** Once the event is durably accepted, the acknowledgment is lawful. A later worker or processor failure does not retroactively invalidate it. That failure is handled by durable retry/recovery: bounded retries, failed-job visibility, reconciliation and a named recovery owner. Idempotency covers both phases.
  - Webhook tests assert response status and persisted outcome for both phases, plus duplicate delivery and recovery, not only call shape.
- **Preserve:**
  - Signature-failure rejection.
  - "Tests that pass for the wrong reason are worse than tests that fail."
  - BIM §7 per-module failure policy.
  - The testing-tier preservation note above.
- **Likely affected docs / consumers:**
  - TESTING G5 and §2.2.
  - **FC-052** (same mechanism in the ECOM/STRIPE manuals, CF-09, brief 05). Both corrections must converge on one contract.
  - FC-059, FC-062 (CF-09).
  - QA §13/§18 as consumers of the evidence.
- **Verification intent:**
  - A live-corpus search for unconditional-acknowledgment phrasing ("always return 200", "Always return 200") is fully dispositioned, together with FC-052's STRIPE §6 instance.
  - The G5 recipe includes both failure phases:
    - **Failure before durable acceptance** (the capture, enqueue or required write fails) expects a retryable non-success response, and nothing is acknowledged.
    - **Failure after durable acceptance** (the worker fails on an already-accepted event) expects the success acknowledgment to stand, and the test asserts the durable retry/recovery evidence (retry or failed-job state, recovery path) rather than a changed response.
  - A duplicate-delivery case shows idempotent handling.
  - TESTING and the CF-09 manuals state the same acknowledgment contract.
- **Open decision:** DEC-03, the Factory webhook acknowledgment contract, shared with FC-052, FC-059 and FC-062. Jarvis designs; Tony approves. Recommend Sol's synthesis candidate (C05 §7.B): "success must mean the required state transition was completed or durably accepted for recovery."
- **Proposed route:** `SYNC`. **Wave 1 BLOCKER.**

**Mapping proposal — ENGINEER-PROPOSED:** A webhook acknowledges success only after checked completion of the required state transition or checked durable capture/enqueue. Failure before that boundary returns a retryable non-success. Failure after durable acceptance is recovered through bounded durable retries, visible failed work, reconciliation and a named recovery owner; it does not retroactively invalidate the acknowledgment. Test status and persisted outcome for pre-acceptance failure, post-acceptance failure, duplicates and recovery.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:823` — ## 3.8 Run-verification rituals (promoted from Run 001); MANIFEST ← 11: SOFTWARE_FACTORY_PLAYBOOK, ENGINEER_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, API_AND_SERVICES_MANUAL, DATABASE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.

**Touch proposal:** C-020. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-020` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-021 — Payment-error recipe moves sensitive error content into server logs

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/03_build_method_corrections.md:66`):

- **Certified record:** CF-05 · Severity HIGH · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C03-D06 · Fable none
- **Evidence:** Astra C03 §7 C03-D06; Sol C03 §4 ("define an approved structured error record rather than simply suppressing diagnostics").
- **Defect surfaces (`0a787cb`):**
  - `03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md` §4.3
  - `03_BUILD_METHODOLOGY/QA_PLAYBOOK.md` §13 (D7), §29
- **Defect:** TESTING §4.3 acknowledges that payment errors can carry card details, emails and request IDs, then mandates `console.error("Stripe Error:", error)` with no redaction. Its test checks only the response body, while QA forbids PII or secrets in logs.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - TESTING §4.3 prescribes a structured, redacted error record with approved fields instead of logging the raw provider error.
  - Its defensive test asserts both the client response and the log content, using synthetic sensitive markers.
- **Preserve:**
  - The generic-client-message rule and the test that card fragments never reach the client.
  - Enough sanitized context for diagnosis.
- **Likely affected docs / consumers:** TESTING §4.3; ECOM §3 error path (FC-051, response side) and API §3/§6 (FC-064), which belong to the same leakage family; QA §29 evidence redaction.
- **Verification intent:**
  - No live recipe logs a raw provider error object; every `console.error(..., error)`-style hit in recipes is dispositioned.
  - The §4.3 test includes a log assertion.
- **Open decision:** the approved field list (Jarvis). No Director decision is needed.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Return a generic client error. Log only an allow-listed structured record: correlation ID, operation, normalized failure class and safe provider code. Exclude raw exceptions, request bodies, credentials, payment details and personal data. A negative test plants synthetic sensitive markers and asserts that neither client output nor retained logs contain them.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:1089` — ## 4.3 Stripe — wrapper-mock vs constructor-mock decision tree; MANIFEST ← 11: SOFTWARE_FACTORY_PLAYBOOK, ENGINEER_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, API_AND_SERVICES_MANUAL, DATABASE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.
- `03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:1105` — ### 4.3a — Wrapper-mock pattern (StarkReads / v1.0); MANIFEST ← 11: SOFTWARE_FACTORY_PLAYBOOK, ENGINEER_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, API_AND_SERVICES_MANUAL, DATABASE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.
- `03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:1152` — ### 4.3b — Constructor-mock pattern (Dockbloxx); MANIFEST ← 11: SOFTWARE_FACTORY_PLAYBOOK, ENGINEER_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, API_AND_SERVICES_MANUAL, DATABASE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.

**Touch proposal:** C-021. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-021` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-022 — Mutating E2E helpers lack an enforced test-environment boundary

**Proposed disposition:** BLOCKED. **Authority:** certified correction YES; package outcome remains proposed. CONDITIONAL: DEC-14 diagnostic authority. 

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/03_build_method_corrections.md:88`):

- **Certified record:** CF-05 · Severity HIGH · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C03-D08 · Fable none
- **Evidence:** Astra C03 §7 C03-D08; Sol C03 §4 ("fail closed unless the target environment is positively identified as authorized for mutation").
- **Defect surfaces (`0a787cb`):**
  - `03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md` §4.1, §4.4 (and §4.5 fixture regeneration)
  - `03_BUILD_METHODOLOGY/QA_PLAYBOOK.md` §§12, 29–30
- **Defect:** the E2E recipe registers users, seeds subscriptions through an admin client and deletes records against whatever Supabase URL and privileged key are loaded. Nothing checks that the target is an approved test project before mutating.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - Privileged E2E setup and cleanup positively verify the approved test project and test identity before any mutation, and fail closed otherwise.
  - Production confirmation is a separate, bounded, non-destructive procedure.
  - Cleanup is limited to identities the run created and recorded.
- **Preserve:**
  - Synthetic identities and cleanup ordering.
  - Read-only fixture discovery across environments.
  - QA's final-environment-reset rule.
- **Likely affected docs / consumers:** TESTING §4.1/§4.4/§4.5; QA §§12, 29–30; FC-069 (environment-variable naming, CF-07), on which the check may depend.
- **Verification intent:**
  - The recipe contains a pre-mutation target-identity assertion that refuses an unapproved project.
  - The documentation separates mutating E2E from production confirmation.
- **Open decision:** how a test project is positively identified, e.g. an allow-listed project reference vs a marker (Jarvis).
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Before privileged test setup or cleanup, verify the target project reference against the Director-approved test-project allowlist and verify the authorized test identity. Fail closed on mismatch, missing identity or unknown target. Record every run-created identity; cleanup may act only on that set. Production verification is a separately authorized, bounded, non-destructive procedure.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:847` — ## 4.1 Supabase-backed apps (StarkReads example); MANIFEST ← 11: SOFTWARE_FACTORY_PLAYBOOK, ENGINEER_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, API_AND_SERVICES_MANUAL, DATABASE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.

**Touch proposal:** C-022. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-022` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-023 — Local exceptions permit implementation before scope approval

**Proposed disposition:** BLOCKED. **Authority:** certified correction YES; package outcome remains proposed. CONDITIONAL: DEC-14. 

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/03_build_method_corrections.md:170`):

- **Certified record:** CF-03 · Severity HIGH · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C03-D04 · Fable none
- **Evidence:** Astra C03 §7 C03-D04; Sol C03 §4 ("STOP affected work → present evidence → request minimal amendment → receive approval → continue"; emergency procedures must be "explicit and bounded") and §9.B.
- **Defect surfaces (`0a787cb`):**
  - `03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md` §7
  - `03_BUILD_METHODOLOGY/FEAT_PLAYBOOK.md` §2 (imports BIM)
  - `03_BUILD_METHODOLOGY/BUG_FIX_PLAYBOOK.md` §3
  - `03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md` §3.3
  - Contrary rules: `03_BUILD_METHODOLOGY/APP_FACTORY_SKILLS_PLAYBOOK.md` §13 (Anti-Pattern 8), `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md` §2.5, `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md` §15
- **Defect:**
  - BIM §7 lets the Engineer step outside the enumerated writable surface when they judge it genuinely required, with ratification afterwards. FEAT imports this and FIX repeats it.
  - TESTING §3.3 says to fix HIGH security findings inline.
  - Both conflict with the prior-approval rules.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - No doctrine permits implementation outside the approved writable surface with after-the-fact ratification.
  - A newly necessary change follows: STOP the affected work → evidence → minimal amendment → approval → continue.
  - A newly found HIGH security issue is escalated promptly, not fixed inline without approval.
  - Any emergency path is explicit and bounded.
- **Preserve:**
  - Urgency of security escalation.
  - Explicitly approved conditional surfaces.
  - BUG_FIX scope protection.
- **Likely affected docs / consumers:** BIM §7, FEAT §2, BUG_FIX §3, TESTING §3.3; Engineer and Coordinator seats; FC-012.
- **Verification intent:**
  - A live-corpus search for ratification-after-action language and "fix inline" guidance is fully dispositioned, with none authorizing pre-approval action.
  - The BIM §7 writable-surface clause contains no open-ended exception.
- **Open decision:** DEC-14, whether to define a bounded emergency procedure now or defer it (Tony).
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** A newly necessary change outside the approved writable surface stops the affected work. Record evidence, propose the smallest scope amendment, obtain approval, then continue. Escalate a newly discovered high-severity security issue promptly; do not implement it under after-the-fact approval. No emergency implementation exception is created here.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:1139` — ## 15. Agentic Coding Constitution (Karpathy Protocol); MANIFEST ← 7: APP_FACTORY_BLUEPRINT, DESIGNER_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, FFM_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:650` — ## 3.4 Audit-then-add when joining an existing project; MANIFEST ← 11: SOFTWARE_FACTORY_PLAYBOOK, ENGINEER_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, API_AND_SERVICES_MANUAL, DATABASE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:616` — ## 8. File-By-File Authoring Guide — Root Files; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:620` — ### 8.1 — Root `CLAUDE.md`; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:659` — ### 8.2 — Root `README.md`; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:693` — ### 8.3 — `AGENTS.md`; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:713` — ### 8.4 — `GEMINI.md`; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.

**Touch proposal:** C-023. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-023` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-024 — E2E workaround recipe can remove a shipped failure from the system under test

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/03_build_method_corrections.md:112`):

- **Certified record:** CF-05 · Severity HIGH · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C03-D09 · Fable none
- **Evidence:** Astra C03 §7 C03-D09; Sol C03 §4 ("Any dependency-disabled run must be labeled as diagnostic/isolated evidence").
- **Defect surfaces (`0a787cb`):**
  - `03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md` §§3.5–3.6, Part 6 G11
  - `03_BUILD_METHODOLOGY/QA_PLAYBOOK.md` §§11–12, 19, 34
- **Defect:** TESTING recommends aborting or neutralizing a production-present script during E2E and presents that as a fix. It requires neither a reduced-coverage label nor verification with the script enabled, so the suite can go green while users still hit the failure.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - Dependency-disabled runs are labeled diagnostic or isolated evidence.
  - The full-environment flow stays FAILED or BLOCKED until it is fixed or covered by an approved compensating verification.
  - The coverage limitation is carried into the Gate Q evidence.
- **Preserve:** isolation as a diagnostic tool; the §3.6 documented skip path with a verified manual replacement, which is not the defect.
- **Likely affected docs / consumers:** TESTING §3.5, §3.6, G11; QA Gate Q (§12); FC-063.
- **Verification intent:**
  - G11 no longer presents neutralization as an unlabeled fix.
  - The recipe requires a coverage-limitation note in the Gate Q evidence.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** A run with a dependency disabled is diagnostic or isolated evidence. The full-environment flow remains FAILED or BLOCKED until repaired or covered by an explicitly approved compensating verification. Carry the omitted dependency, affected claims and coverage limitation into Gate Q evidence.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:705` — ## 3.6 Skip-and-document as a Factory pattern; MANIFEST ← 11: SOFTWARE_FACTORY_PLAYBOOK, ENGINEER_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, API_AND_SERVICES_MANUAL, DATABASE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.

**Touch proposal:** C-024. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-024` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-025 — FFM (and combined-artifact allowances) omit the mandatory `ACCEPTANCE_SPEC.md` lifecycle and QA handoff

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/03_build_method_corrections.md:223`):

- **Certified record:** CF-04 · Severity HIGH · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C03-D03 · Fable none
- **Evidence:** Astra C03 §7 C03-D03; Sol C03 §4 (a generic "equivalent artifact" allowance cannot override the Factory-wide filename and lifecycle rule; reinforces C01-D02/C02-D01 but should not be merged).
- **Defect surfaces (`0a787cb`):**
  - `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md` §§2–3, 12–13, 18, Appendix A
  - `03_BUILD_METHODOLOGY/QA_PLAYBOOK.md` §§6, 20
  - `03_BUILD_METHODOLOGY/BUG_FIX_PLAYBOOK.md` §18
  - `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md` §2.5
  - `03_BUILD_METHODOLOGY/FRONTEND_BUILD_PHASE_PLAYBOOK.md` §9 (correct)
- **Defect:**
  - FFM's folder trees, file guides, handoff diagram and authoring checklist have no `ACCEPTANCE_SPEC.md` creation or finalization step and no QA intake.
  - QA §§6/20 accept "equivalent" artifacts and BUG_FIX §18 allows combined documents, both against SFP §2.5's exact-filename mandate.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - FFM's anatomy, authoring sequence, boot/verification instructions and completion checklist include, by reference to the shared contract:
    - `ACCEPTANCE_SPEC.md` creation from a pre-implementation approved basis
    - its maintenance and finalization
    - the QA handoff
  - QA's "equivalent artifact" and BUG_FIX's combined-document allowances are limited to contexts the Factory rule actually exempts.
- **Preserve:**
  - SFP §2.5's exact-filename rule and mandatory Gate Q.
  - FBP §9's correct Gate Q/D requirement.
  - Proportional ceremony for small fixes within the rule (backlog C03-S02).
- **Likely affected docs / consumers:** FFM, QA §6/§20, BUG_FIX §18; FC-002, FC-013, FC-026 (sequence together).
- **Verification intent:**
  - The FFM Appendix A checklist contains the ACCEPTANCE_SPEC steps.
  - QA §6/§20 no longer admit a non-exempt substitute.
  - BUG_FIX §18 keeps the filename even when combining content.
- **Open decision:** whether a BUG_FIX small fix may carry all its acceptance content inside one `ACCEPTANCE_SPEC.md` (Jarvis).
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Every newly authored module includes ACCEPTANCE_SPEC.md based on the approved pre-implementation contract. The Architect prepares acceptance requirements; Engineering records factual completion without changing success criteria; independent QA evaluates them. Finalize the factual handoff before the engineering stop. A small FIX may combine supporting records, but it still supplies ACCEPTANCE_SPEC.md; runtime modules do not inherit a documentation-only waiver.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:261` — ## 3. FFM Anatomy — The Folder Structure; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:541` — ## 7. Authoring Sequence; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:616` — ## 8. File-By-File Authoring Guide — Root Files; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:620` — ### 8.1 — Root `CLAUDE.md`; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:659` — ### 8.2 — Root `README.md`; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:693` — ### 8.3 — `AGENTS.md`; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:713` — ### 8.4 — `GEMINI.md`; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1367` — ## 13. File-By-File Authoring Guide — `verification/`; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1371` — ### 13.1 — `verification/PHASE_GATES.md`; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1400` — ### 13.2 — `verification/BUILD_CHECKLIST.md`; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1414` — ### 13.3 — Authoring Discipline; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1828` — ## 18. The Authoring Checklist; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:2065` — ## 21. Appendix A — Skeleton Folder Tree; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:2141` — ## 22. Appendix B — Boot Prompts; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/BUG_FIX_PLAYBOOK.md:573` — ## 18. Required FIX Artifacts; MANIFEST ← 3: QA_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.
- `03_BUILD_METHODOLOGY/QA_PLAYBOOK.md:260` — # 6. The Engineer Handoff Is a Claim Package; MANIFEST ← 3: BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.

**Touch proposal:** C-025. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-025` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-026 — Whole-folder module freeze conflicts with required in-folder working artifacts

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/03_build_method_corrections.md:255`):

- **Certified record:** CF-04 · Severity MEDIUM · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C03-D01 · Fable none
- **Evidence:** Astra C03 §7 C03-D01; Sol C03 §5 (provisional MEDIUM, closed MEDIUM 2026-09-27; distinguish "IMMUTABLE APPROVED INPUTS from AUTHORIZED WORKING / EVIDENCE OUTPUTS").
- **Defect surfaces (`0a787cb`):**
  - `03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md` §§4, 6–8
  - `03_BUILD_METHODOLOGY/BUG_FIX_PLAYBOOK.md` §§16, 18
  - `03_BUILD_METHODOLOGY/FEAT_PLAYBOOK.md` §2
  - `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md` §2.5
- **Defect:** BIM freezes the whole module folder from Plan Mode to STOP ("nothing inside may be added or edited"), yet requires the Engineer to maintain and finalize `ACCEPTANCE_SPEC.md`, which lives inside that folder. FIX repeats this; FEAT imports it.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):** the freeze rule distinguishes immutable approved inputs from authorized working and evidence outputs. It states:
  - which files stay writable during the hold, and by whom;
  - where updates are staged and who admits them;
  - when the spec is finalized relative to STOP.
  Requirement changes still need approval.
- **Preserve:**
  - The freeze's purpose: no scope drift during execution (Fable §6 item 4).
  - Approval for requirement changes.
- **Likely affected docs / consumers:** BIM, BUG_FIX, FEAT (inherits); QA §20 artifact home (FC-013).
- **Verification intent:**
  - Following BIM literally, an Engineer can maintain and finalize the spec without violating any freeze sentence.
  - FIX and FEAT inherit the same rule.
- **Open decision:** DEC-13, the freeze model (Jarvis), joint with FC-013.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Freeze requirements and acceptance criteria at handoff. Declare owner-specific writable lanes inside the module for engineering handoff, recon, plans, evidence, findings and attributable rulings. QA records belong in the module’s QAM under agent_docs/. Contract changes require an approved amendment; neither a test-plan edit nor a new evidence file silently amends the contract.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md:46` — ## 4. The Module Package (one folder, self-contained); MANIFEST ← 1: FEAT_PLAYBOOK.
- `03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md:77` — ## 6. Lifecycle (the stage-gate chain); MANIFEST ← 1: FEAT_PLAYBOOK.
- `03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md:150` — ## 11. Anti-Patterns (block these); MANIFEST ← 1: FEAT_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:541` — ## 7. Authoring Sequence; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/QA_PLAYBOOK.md:1185` — # 20. QA Deliverables; MANIFEST ← 3: BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.

**Touch proposal:** C-026. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-026` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-027 — Greenfield DATA_CONTRACT authorship and timing are not executable as written

**Proposed disposition:** BLOCKED. **Authority:** certified correction YES; package outcome remains proposed. CONDITIONAL: DEC-11. 

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/03_build_method_corrections.md:311`):

- **Certified record:** CF-02 · Severity HIGH · Review PARTIAL · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C03-D07 · Fable FBL-D014 (primary)
- **Severity divergence (recorded):** Astra HIGH vs Fable MEDIUM. The certified HIGH stands.
- **Evidence:** Astra C03 §7 C03-D07; Sol C03 §4 (reinforces C02-D03) and §9.C; Fable §7 FBL-D014, §11 decision 6.
- **Defect surfaces (`0a787cb`):**
  - `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md` §§7, 9.2, 12.4, 14, 18
  - `03_BUILD_METHODOLOGY/FRONTEND_FIRST_PLAYBOOK.md` §3
  - `01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md` Phase 3/4
  - `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md` §§1–3, §12 ("Author: Engineer Agent")
- **Defect:** doctrine assigns the greenfield DATA_CONTRACT to the Engineer, yet the execution sequence either:
  - has the Engineer consume an unfinished "contract shell" (§12.4 goes straight to types); or
  - hands authorship back to another seat (§14).
  §18 checks for a fully populated contract, and the Blueprint names two Engineer actors.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - FFM's authoring and execution sequences have explicit conversion and greenfield branches.
  - Greenfield: Engineer authorship and approval of DATA_CONTRACT come before type and service implementation (before the freeze, if Fable's model is chosen).
  - §14 no longer reassigns authorship to the Architect, and §18 accepts a shell only at the specified earlier handoff.
  - The Engineer seat's identity is stated the same way everywhere.
- **Preserve:**
  - Conversion's complete pre-authored contract path.
  - ENGINEER §3's per-pipeline author of record.
  - FRONTEND_FIRST §3's contract-before-mock-UI rule.
- **Likely affected docs / consumers:** FFM, FRONTEND_FIRST §3, Blueprint, ENGINEER §12; FC-015 (pre-implementation approval), FC-006 (seat identity).
- **Verification intent:**
  - The FFM §12.4 greenfield branch has an authoring + approval step before Types.
  - §14 and §18 agree with it.
  - Blueprint Phase 3/4 name the same Engineer seat.
  - FRONTEND_FIRST §3 can be satisfied in sequence.
- **Open decision:** DEC-11 (Fable §11 decision 6). Is the Engineer Claudy in every context, and when is the greenfield DATA_CONTRACT completed? (Tony)
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Conversion consumes its approved extracted DATA_CONTRACT. Greenfield uses the Architect-prepared DATA_CONTRACT approved before Design and implementation. The Engineer verifies prerequisites and consumes that revision; a contract shell is not permission to implement types or services. Reopen a missing or conflicting contract through the amendment lane, not by silently changing authorship during execution.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:365` — ## 4. The Two FFM Variants — Conversion vs Greenfield; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:541` — ## 7. Authoring Sequence; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1422` — ## 14. The Extractor Question — When To Run Brain Drain; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1828` — ## 18. The Authoring Checklist; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:129` — ## 3. Inputs Required; MANIFEST ← 7: APP_FACTORY_BLUEPRINT, DESIGNER_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, FFM_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:540` — #### 3. Editable Installs Are Mandatory; MANIFEST ← 7: APP_FACTORY_BLUEPRINT, DESIGNER_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, FFM_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:1178` — #### 3. Push Back When Warranted; MANIFEST ← 7: APP_FACTORY_BLUEPRINT, DESIGNER_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, FFM_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `02_PIPELINE_AGENTS/ARCHITECT_PLAYBOOK.md:330` — ## 8. Handoff Protocol to Designer; MANIFEST ← 6: APP_FACTORY_BLUEPRINT, ARCHITECT_QUESTIONNAIRE, DESIGNER_PLAYBOOK, RECON_QUESTIONNAIRE, FFM_PLAYBOOK, BIM_PLAYBOOK.

**Touch proposal:** C-027. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-027` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-028 — FFM prescribes the auth-service wrapper that kit-consumption doctrine forbids

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/03_build_method_corrections.md:281`):

- **Certified record:** CF-04 · Severity HIGH · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C03-D02 · Fable none as primary
- **Evidence:**
  - Astra C03 §7 C03-D02.
  - Sol C03 §4: "preserve legitimate domain-specific enrichment while forbidding wrappers whose only purpose is to re-expose already complete kit behavior".
  - Register see-also: FBL-D001's APP_ARCHITECTURE §2 sub-claim, which FC-033 covers.
- **Defect surfaces (`0a787cb`):**
  - `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md` §9.2, §12.4
  - `03_BUILD_METHODOLOGY/FRONTEND_FIRST_PLAYBOOK.md` §0
  - `03_BUILD_METHODOLOGY/FRONTEND_BUILD_PHASE_PLAYBOOK.md` §1.6
  - `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md` §5
- **Defect:** FFM's auth-service contract and its service sub-phase tell the builder to wrap the kit's `getUser()` / `signInWithPassword()` in `/src/services/`. FRONTEND_FIRST §0 and FBP §1.6 prohibit redundant `authService.ts` wrappers.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - FFM's sample auth contract and service sub-phase default to direct kit-auth consumption.
  - A wrapper that only re-exposes complete kit behavior is not prescribed.
  - Genuinely missing domain auth behavior needs recon-backed justification.
- **Preserve:**
  - The Kit Exception and the "Should I Author This?" verdict table (Fable §6 item 2).
  - The service layer for project-specific domain logic (ENGINEER §5).
- **Likely affected docs / consumers:** FFM §9.2/§12.4; consistency with FRONTEND_FIRST §0, FBP §1.6, `04_REFERENCE_MANUALS/AUTH_MANUAL.md` §0, `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md` §1; FC-033 (APP_ARCHITECTURE §2 `authServices.ts`).
- **Verification intent:**
  - The FFM sample contract wraps no kit `getUser` or `signIn` primitive.
  - A live-corpus search for `authService` returns only prohibitions or justified domain enrichment.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Consume complete kit auth primitives directly. Do not create an auth service whose only purpose is to re-expose kit behavior. A genuinely missing domain capability requires recon evidence, a bounded approved contract and its own verification; it does not authorize replacing the kit’s auth authority.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:739` — ## 9. File-By-File Authoring Guide — `_project/`; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:743` — ### 9.1 — `_project/APP_BRIEF.md`; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:793` — ### 9.2 — `_project/DATA_CONTRACT.md`; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:854` — ### 9.3 — `_project/UI_SPEC.md`; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:900` — ### 9.4 — `_project/CLAUDE.md`; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1246` — ## 12. File-By-File Authoring Guide — `playbook/`; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1250` — ### 12.1 — Overall Structure; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1266` — ### 12.2 — `00-OVERVIEW.md`; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1283` — ### 12.3 — `01-DISCOVERY.md` Through `06-VERIFICATION.md` (And `07-RETROSPECTIVE.md`); MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1296` — ### 12.4 — Per-Sub-Phase Authoring Notes; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1338` — ### 12.5 — `RETROSPECTIVES/` Folder; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1356` — ### 12.6 — Playbook Reuse Discipline; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.

**Touch proposal:** C-028. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-028` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-029 — FFM gives two different documents final scope authority

**Proposed disposition:** BLOCKED. **Authority:** certified correction YES; package outcome remains proposed. CONDITIONAL: DEC-14 / DEC-06. 

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/03_build_method_corrections.md:201`):

- **Certified record:** CF-03 · Severity MEDIUM · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C03-D13 · Fable none as primary
- **Evidence:** Astra C03 §7 C03-D13; Sol C03 §6 ("One artifact should hold scope authority; derivative summaries should defer to it and STOP on disagreement").
- **Defect surfaces (`0a787cb`):** `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md` §9.1, §9.4 (Cross-File Consistency), Appendix C.1.
- **Defect:** §9.1 makes APP_BRIEF the single source of truth for scope, while the copyable root-manager stub says `_project/CLAUDE.md` wins on scope.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - One artifact holds scope authority. APP_BRIEF is recommended, per FFM §9.1.
  - The C.1 stub and every manager defer to it.
  - A disagreement stops the affected work.
- **Preserve:** the invariant that duplicated forbidden zones must match; the STOP rule.
- **Likely affected docs / consumers:**
  - FFM §9.1 and C.1.
  - `_project/CLAUDE.md` stubs already generated in downstream modules carry the old text (`XB-EXT` awareness only).
  - FC-005.
- **Verification intent:** the C.1 stub text defers to the chosen authority, and no "wins on scope" statement for another artifact remains.
- **Open decision:** DEC-14, the scope-authority artifact (Tony; APP_BRIEF recommended).
- **Proposed route:** `SYNC` (+ `XB-EXT` awareness).

**Mapping proposal — ENGINEER-PROPOSED:** APP_BRIEF is the module scope authority. Managers and startup stubs route to its approved revision; DATA_CONTRACT and UI_SPEC define their respective contracts within that scope. A disagreement stops the affected work for an attributable ruling. A manager’s summary never silently expands or overrides APP_BRIEF.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:739` — ## 9. File-By-File Authoring Guide — `_project/`; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:743` — ### 9.1 — `_project/APP_BRIEF.md`; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:793` — ### 9.2 — `_project/DATA_CONTRACT.md`; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:854` — ### 9.3 — `_project/UI_SPEC.md`; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:900` — ### 9.4 — `_project/CLAUDE.md`; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:2236` — ## 23. Appendix C — Template Files (Stubs To Copy); MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.

**Touch proposal:** C-029. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-029` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-030 — Fixture discovery can publish unusable roles, and its consumer reads a different count field

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/03_build_method_corrections.md:133`):

- **Certified record:** CF-05 · Severity MEDIUM · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C03-D12 · Fable none
- **Evidence:** Astra C03 §7 C03-D12; Sol C03 §6.
- **Defect surfaces (`0a787cb`):** `03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md` §§2.3, 4.4–4.5 (coupon rules at §§2.1, 3.7).
- **Defect:**
  - Discovery labels roles without checking that they exist or meet their prerequisites, so it can write "successful" JSON with empty roles.
  - The pagination consumer reads `.product_count`, but discovery preserved `.count`.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - Discovery validates a normalized fixture schema and scenario eligibility (role existence, coupon prerequisites) before reporting success, and uses one count property.
  - A missing required role yields an explicit setup BLOCKED result; optional absence is recorded deliberately.
- **Preserve:** the fixture-discovery concept and environment-following read-only discovery.
- **Likely affected docs / consumers:** TESTING §§2.3, 4.4–4.5; consumers of the fixture JSON.
- **Verification intent:**
  - The documented empty-dataset case yields BLOCKED, not success.
  - Producer and consumer use the same count field.
  - Coupon eligibility checks reference the §2.1/§3.7 rules.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Fixture discovery returns one normalized record with role identities, scenario eligibility and a single count field named count. Validate role existence and coupon prerequisites before declaring readiness. A missing required role produces BLOCKED with the missing prerequisite; optional absence is recorded explicitly. Producers and consumers read count, not competing count aliases.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:1256` — ## 4.4 Test data sourcing — discovered vs declared; MANIFEST ← 11: SOFTWARE_FACTORY_PLAYBOOK, ENGINEER_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, API_AND_SERVICES_MANUAL, DATABASE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.

**Touch proposal:** C-030. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-030` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-031 — Metadata helper cannot distinguish an absent key from a present null

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/03_build_method_corrections.md:154`):

- **Certified record:** CF-05 · Severity MEDIUM · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C03-D11 · Fable none
- **Evidence:** Astra C03 §7 C03-D11; Sol C03 §6.
- **Defect surfaces (`0a787cb`):** `03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md` §4.2, "Key-absent vs empty-value distinction".
- **Defect:** §4.2 requires distinguishing a missing key from a present empty value, but the sample `entry ? entry.value : null` returns `null` in both cases.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):** the helper returns an explicit presence/value result, or a distinct absence sentinel, under a documented contract, with examples for absent, null, zero and empty string.
- **Preserve:** the absent-vs-empty requirement itself.
- **Likely affected docs / consumers:** TESTING §4.2 and tests built from it.
- **Verification intent:** evaluating the documented helper on {absent, null, 0, ""} yields four distinguishable results that match the documented contract.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Metadata lookup returns { present: false } for an absent key and { present: true, value } for a present key. Null, zero and the empty string remain present values. Test all four cases; never use null for both absence and a stored null.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:955` — ## 4.2 REST-backed apps (Dockbloxx / WooCommerce example); MANIFEST ← 11: SOFTWARE_FACTORY_PLAYBOOK, ENGINEER_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, API_AND_SERVICES_MANUAL, DATABASE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.

**Touch proposal:** C-031. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-031` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-032 — FRONTEND_BUILD_PHASE checklist points Gate Q / Gate D to the wrong QA_PLAYBOOK sections

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/03_build_method_corrections.md:346`):

- **Certified record:** CF-13 · Severity LOW · Review CONFIRMED · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C03-D14 · Fable FBL-D025 (primary)
- **Evidence:** Astra C03 §7 C03-D14; Sol C03 §7; Fable §7 FBL-D025, §9 row 20.
- **Defect surfaces (`0a787cb`):**
  - `03_BUILD_METHODOLOGY/FRONTEND_BUILD_PHASE_PLAYBOOK.md` §9
  - `03_BUILD_METHODOLOGY/QA_PLAYBOOK.md` §§9–10 (actual: §12 Gate Q, §13 Gate D)
  - Process evidence: `agent_docs/RESPONSES/response_2026-08-10_194109_phase2-ripple-map.md` (at `0a787cb`; deleted from the working tree by Director ruling and present in history).
- **Defect:** FBP §9 cites QA §9 for Gate Q and §10 for Gate D. In the live QA doc those are Engagement Lifecycle and Scope Protection.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - FBP §9 points to the live QA gate sections, preferably by stable heading name.
  - Inbound anchor checks become part of sync consistency checking. The process side is covered by DocSet Sync D19 and FC-087.
- **Preserve:** the Gate Q/D requirement in FBP §9.
- **Likely affected docs / consumers:** FBP §9; any other inbound QA anchor citations.
- **Verification intent:**
  - Both references resolve to the "Gate Q" and "Gate D" headings at the candidate SHA.
  - A propagation search for `QA_PLAYBOOK.md` §9/§10 citations is fully dispositioned.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Gate Q refers to QA_PLAYBOOK §12, “Gate Q”; Gate D refers to QA_PLAYBOOK §13, “Gate D”. These are distinct checks; frontend build success and demo deployment satisfy neither gate by themselves.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `03_BUILD_METHODOLOGY/FRONTEND_BUILD_PHASE_PLAYBOOK.md:417` — ## 9. UI Phase Completion Checklist; MANIFEST ← 4: ENGINEER_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, TESTING_PLAYBOOK, UI_UX_BUILDING_MANUAL.

**Touch proposal:** C-032. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-032` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.
