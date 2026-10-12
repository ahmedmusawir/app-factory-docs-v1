# 03 — Build Method / Testing / QA — Correction Brief

> **DRAFT — CORRECTION INTAKE / NOT APPROVED FOR SYNC**

- **Package:** Factory Doctrine Correction Package 001. Index: `FACTORY_DOCTRINE_CORRECTION_INDEX_001.md`.
- **Prepared by:** Claudy (documentation Engineer seat), 2026-10-11. This is not a QA product and certifies nothing.
- **Primary entries:** FC-020 … FC-032 (13), the certified register §5.C. **Contains 1 BLOCKER: FC-020.**
- **Authority:** every outcome is **PROPOSED** for Jarvis (Architect) review and Tony (Director) approval. Nothing here is approved policy.
- **Nature:** these are documentation findings about methodology and recipe text, not proof that any client application or test suite has the flaw. No replacement doctrine text is written.

## Pinned sources

| Ref | Revision | Path |
|---|---|---|
| Certified register / QA | `c6210c3` = `c6210c32480558b343a27726a26822e8d959d0f7` | `astra-review/run-002/synthesis/PART1_FINDINGS_DISPOSITION.md`, `astra-review/run-002/synthesis/QA/PART1_CONVERGENCE_QA.md` |
| Astra chunk 03 / Sol chunk 03 | `c6210c3` | `astra-review/run-002/chunks/03_build_method/ASTRA_REVIEW.md`, `astra-review/run-002/chunks/03_build_method/SOL_REVIEW.md` |
| Astra/Sol chunk 05 (FC-063 context) | `c6210c3` | `astra-review/run-002/chunks/05_api_commerce/ASTRA_REVIEW.md`, `astra-review/run-002/chunks/05_api_commerce/SOL_REVIEW.md` |
| Fable (blind) | `39a1c6114d72b22d3550d7ff65234ec0f01418f6` (`origin/factory-docs-review-fable-001`) | `fable-review/run-001/reviews/FABLE_FACTORY_DOCTRINE_REVIEW_001.md` |
| Review baseline | `0a787cb` = `0a787cb826118b4a010765d60e41a449df3ce746` | defect surfaces named per entry |
| Current main | `9c17939` = `9c179392f79b70da099121fc357d3107ad3bb86e` | every surface in this brief is blob-identical to `0a787cb` (QA-4) |

Route codes are as in the index. Short doctrine names in this brief resolve under `03_BUILD_METHODOLOGY/` unless a full path is given.

**Testing-tier preservation (applies to all CF-05 entries):** keep the field-earned truth principles Fable §6 item 6 asks to preserve verbatim: TESTING Principles 1.3, 1.4 and 1.10, `retries: 0`, shadow-implementation detection and defensive error assertions. Also keep QA's one-test-at-a-time protocol and final-environment-reset rule (Fable §6 item 3). The corrections below change recipes, not those principles.

---

## CF-05 — Testing / evidence / environment fidelity (FC-020, 021, 022, 024, 030, 031 here; FC-063 is in brief 05)

### FC-020 — TESTING webhook recipe acknowledges success unconditionally, without durable processing or recovery
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
  - Acknowledgment follows the approved event-processing contract (DEC-03): success only after proven processing or durable acceptance (capture or enqueue), with idempotency and recovery/reconciliation for deferred or failed work.
  - Webhook tests assert response status and persisted outcome, including persistence failure, duplicate delivery and recovery, not only call shape.
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
  - The G5 recipe includes a failed-persistence case that expects a non-success (retryable) response and a durable-acceptance case.
  - TESTING and the CF-09 manuals state the same acknowledgment contract.
- **Open decision:** DEC-03, the Factory webhook acknowledgment contract, shared with FC-052, FC-059 and FC-062. Jarvis designs; Tony approves. Recommend Sol's synthesis candidate (C05 §7.B): "success must mean the required state transition was completed or durably accepted for recovery."
- **Proposed route:** `SYNC`. **Wave 1 BLOCKER.**

### FC-021 — Payment-error recipe moves sensitive error content into server logs
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

### FC-022 — Mutating E2E helpers lack an enforced test-environment boundary
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

### FC-024 — E2E workaround recipe can remove a shipped failure from the system under test
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

### FC-030 — Fixture discovery can publish unusable roles, and its consumer reads a different count field
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

### FC-031 — Metadata helper cannot distinguish an absent key from a present null
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

## CF-03 — Recon / planning / scope-authority boundaries (FC-023, 029 here)

### FC-023 — Local exceptions permit implementation before scope approval
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

### FC-029 — FFM gives two different documents final scope authority
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

## CF-04 — FFM / module acceptance and freeze mechanics (FC-025, 026, 028 here)

### FC-025 — FFM (and combined-artifact allowances) omit the mandatory `ACCEPTANCE_SPEC.md` lifecycle and QA handoff
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

### FC-026 — Whole-folder module freeze conflicts with required in-folder working artifacts
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

### FC-028 — FFM prescribes the auth-service wrapper that kit-consumption doctrine forbids
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

## CF-02 — Artifact / handoff / template contracts (FC-027 here)

### FC-027 — Greenfield DATA_CONTRACT authorship and timing are not executable as written
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

## CF-13 — Cross-reference / locator / document-structure hygiene (FC-032 here)

### FC-032 — FRONTEND_BUILD_PHASE checklist points Gate Q / Gate D to the wrong QA_PLAYBOOK sections
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

---

*End of brief 03. Primary entries: 13 (FC-020 … FC-032). DRAFT — CORRECTION INTAKE / NOT APPROVED FOR SYNC.*
