# ASTRA FACTORY CORE REVIEW — RUN 001, PART 1

Status: IN PROGRESS — corpus discovery completed; examination and judgments incomplete.

Review date: 2026-09-11. Branch: `astra-factory-doc-review`. Repository: `/home/moose/Documents/app-factory-docs-v1`. Governing packet: `astra-review/packets/ASTRA_FACTORY_DOCTRINE_REVIEW_PACKET_001.md` (read completely). Only this report is writable. No incoming/candidate doctrine, intake, synchronization, or Part 2 material is in scope.

## 1. EXECUTIVE ASSESSMENT

INCOMPLETE — pending examination and evidence synthesis.

## 2. TOP 10 — IF ONLY TEN THINGS GET FIXED

INCOMPLETE — pending examination and evidence synthesis.

## 3. RECONSTRUCTED FACTORY OPERATING MODEL

This reconstruction is grounded in the current constitution, agent playbooks, FFM, BIM, FEAT, frontend methodology, and QA playbook. Technical-reference and support examination remains in progress.

### Purpose and routing

The Factory translates approved human intent into reproducible, testable applications using explicit contracts, reusable starter-kit capabilities, bounded modules, and human gates. APP_FACTORY_BLUEPRINT owns the conversion/greenfield router and canonical lifecycle: Phase 0 Recon → 1 Ignition → 2 Design → 3 Engineering → 4 Fabrication → 5 Deployment. SOFTWARE_FACTORY_PLAYBOOK §2 maps its nine execution phases inside that lifecycle. Engineer §5/§13 separates the Next.js kit track from the Python/backend/local-first track. Frontend-first is a selected strategy with eligibility restrictions (FRONTEND_FIRST §2); it defers domain backend implementation behind a service contract.

Conversion preserves a source application's evidenced behavior: Brain Drain extracts → Architect-authored four-file package → Engineer. Greenfield uses Architect → Designer → Engineer, with the Engineer authoring DATA_CONTRACT from approved brief and UI_SPEC. FFM §7 explicitly allows a greenfield contract shell at authoring time. The exact handoff that converts that shell into a fully approved contract is AMBIGUOUS against the package's complete-before-launch rules.

### Roles, authority, and independent action

| Seat | Defined responsibility | Human boundary / unresolved point |
|---|---|---|
| Operator / Tony | Product scope, approval of deliverables, risk acceptance, final release adjudication | QA §4 requires written acknowledgment for overriding a QA recommendation; QA verdict remains QA-owned. |
| Architect | Consumes recon, authors scope and modules, reviews plans, advises on architectural classification | Blueprint calls Architect an agent; SOFTWARE_FACTORY §1 also uses “Human (Architect).” BIM clarifies the seats may be combined but responsibilities remain separate. Product decisions belong to the human. |
| Designer | Tokens, canonical HTML and PNG, UI_SPEC, component manifest; clone-and-adapt after canonical lock | Operator locks tokens/canonical screen/screen set. Conversion ordinarily skips this seat. UI_SPEC draft ownership differs between role tables and package instructions. |
| Engineer / Claudy | Recon, specifications appropriate to pipeline, approved implementation, tests, completion evidence | BIM/FEAT permit deterministic auto-mode only after approved plan; git/cloud actions belong to Coordinator. Engineer §15's generic inline-plan default proceeds unless redirected; its relationship to explicit approval gates is not fully reconciled. |
| Extractor | Evidence-labeled source analysis for conversions or related-repo context | Produces evidence, not new scope or product decisions. Tool distribution is an external dependency. |
| Independent QA Lead | Turns accepted claims into independent checks, attacks seams, classifies findings, issues verdict | Cannot silently repair the code being judged. Operator releases; Architect advises. QA authority text concerning changes to acceptance criteria needs reconciliation with Factory-level ownership. |
| DevOps / Operations | Deploys approved revision, records identity, maintains rollback and environment readiness | QA §4 and Engineer §17 establish the seat; Blueprint Phase 5 assigns deployment to Tony. No single general branch/promotion runbook is established. |

### Work and evidence flow

- **Recon:** Engineer inspects the target repo and reports actual versions, kit capabilities, auth, schema, routes, environment names, compile scope, and surprises. Architect consumes the report before authoring. Re-run after phase closure, upgrades, or merges (ARCHITECT §2). Explicit conflict: recon says no file changes but also requires a report file and includes build commands; the permitted write surface is AMBIGUOUS.
- **Architect:** Questionnaire captures mission, user, scope exclusions, stack, success, decisions/assumptions/open questions. Human approval locks the brief; amendments require reapproval. APPROVED versus LOCKED state vocabulary is inconsistent across consumers and template.
- **Designer:** Confirm stack/token source, author tokens first, render canonical HTML in both themes, obtain lock, clone/adapt each screen, ship executable visual references and intent. Global design doctrine is explicitly delegated authority over tokens/method (DESIGNER §13).
- **Engineer:** Kit recon/read/audit before consumption or extension; greenfield contracts are authored by Engineer, conversion contracts arrive pre-authored. Python track builds independently executable stages and then orchestration/UI. Implementation is bounded by approved scope, forbidden zones, and stage gates.
- **FFM:** One module per project phase, portable navigation, project contracts, skill/workflow copies, design/evidence inputs, verification files, and retrospective. Subphases run Discovery → Types → Services → Mocks → Components → Verification → Retrospective. Six frontend build stages instead run shell → fidelity → polish → subpages → mock functionality → demo deployment. The exact nesting between these two execution maps is AMBIGUOUS. New Factory-wide acceptance-spec and identity requirements have not been fully integrated into the FFM authoring checklist.
- **BIM:** Fresh recon → just-in-time module → scope approval → Engineer plan → Architect plan-QA → Coordinator approval → build → full regression → acceptance handoff → Coordinator commits/setup → independent Gate Q → adjudication/remediation → authorized merge/deploy → Gate D if deployed → closure and retrospective (BIM §6). Existing service seams are preserved; amendments are numbered; rollback switches must be tested.
- **FEAT:** Adds user-facing capability to an already working system; new backend seam work routes to BIM. Inherits BIM mechanics, keeps v2 as a seed, tests declared mode parity and accessible behavior, and forbids weakening regression assertions merely to get green (FEAT §§2–5).
- **QA:** Receive claim package → extract acceptance matrix → verify environment → automated evidence → one-at-a-time human-assisted checks → exploratory seams → classify → verdict. Vocabulary: PASS / PASS WITH FOLLOW-UP FINDINGS / PASS WITH KNOWN RISK / FAIL / BLOCKED. Acceptance failures do not need permission to fail. Out-of-scope nonblocking findings are separately routed.
- **Deployment:** Gate Q certifies candidate readiness, Gate D tests identified deployed revision, bounded production confirmation follows staging/promotion where applicable. Record commit/build/revision/environment; check auth, core flow, negative access, dependencies, timing, logs, regression, rollback, and final configuration reset (QA §§12–14, §30). Full branch naming/base/merge/promotion semantics are project-dependent or UNKNOWN in the general doctrine; BIM only assigns actions and module-branch examples.
- **Support / bug fixing:** Detailed reconstruction pending BUG_FIX and technical-reference review; no separate support manual was discovered.

### Source-of-truth and regression rules

Explicit authorities exist by subject, not as one complete universal hierarchy. Blueprint owns the project router/lifecycle; SOFTWARE_FACTORY §2.5 governs shared module identity and QA handoff; Engineer §15 owns all-agent conduct; Designer defers token/method conflicts to design doctrine; QA §5 places accepted scope first. Recon gives disk precedence for factual claims. FFM Appendix C assigns data to DATA_CONTRACT, UI to UI_SPEC, scope to project CLAUDE, and structure to its navigation file. Root CLAUDE says code serves approved docs. Whether “disk wins” applies only to observed facts or also to approved intended behavior is AMBIGUOUS outside QA's more careful distinction.

Regression doctrine protects prior working behavior, requires baseline evidence and final full-suite checks for BIM/FEAT, forbids weakening assertions for green, treats flakes as defects, and separates proven pre-existing failures. Test counts and Engineer claims alone are insufficient certification. Scope changes, stage transitions, deployment, risk acceptance, and release require the documented human seat. No blanket autonomous release authority is established.

## 4. OVERALL FIVE-DIMENSION SCORECARD

INCOMPLETE — pending examination and evidence synthesis.

## 5. DOMAIN SCORECARDS

INCOMPLETE — pending examination and evidence synthesis.

## 6. WHAT THE FACTORY IS DOING WELL

The following practices have specific operating value and should survive corrective work.

1. **Recon before invention.** APP_FACTORY_BLUEPRINT Phase 0, RECON_QUESTIONNAIRE, and ARCHITECT §2 require inspecting the actual target repository before authoring and distinguishing observations from assumptions. This reduces kit replacement, stale-version assumptions, and imaginary implementation claims. Preserve provenance and the conversion/greenfield distinction.
2. **A real independent QA seat.** QA_PLAYBOOK §§4–5, §§12–14 separates Engineer claims, independent evidence, QA verdict, and Operator release authority. Accepted scope leads; a passing test count is not certification. Preserve the ability to fail an acceptance claim without permission and the written risk-acceptance trail.
3. **Regression is protected behavior.** BIM §§6–8, FEAT §§4–5, BUG_FIX's regression-guard sections, and TESTING prohibit weakening assertions to obtain green. Baselines, final full-suite evidence, negative cases, and proven pre-existing failures are distinct. Preserve these safeguards while simplifying duplicated instructions.
4. **Backend work is bounded.** BIM's just-in-time authoring, tested rollback switches, explicit security/financial failure policies, and avoidance of speculative future modules are good constraints. Correct its freeze/write contradiction without losing the immutable approved-input intent.
5. **Bug fixing starts from mechanism.** BUG_FIX requires a reproducible symptom and confirmed mechanism, or an explicitly approved bounded experiment, before implementation. It routes larger seam replacement to BIM and protects existing behavior. Preserve that separation of diagnosis, hypothesis, and authorized change.
6. **Visual intent is executable.** DESIGNER and FRONTEND_BUILD require tokens, rendered canonical screens, screenshot evidence, component reuse, both themes, and explicit human locks. These provide observable acceptance inputs rather than prose-only aesthetic direction.
7. **Money authority is correctly stated.** STRIPE_SUBSCRIPTIONS §§1, 8, 10 separates Stripe money truth, Supabase's cached entitlement state, and orthogonal RBAC. ECOMMERCE §11 calls for trusted server totals and signed webhooks. Preserve these principles; several operational examples currently violate them.
8. **Evidence has context.** QA requires identified revisions/environments, environment reset, one-at-a-time human checks, exploratory seams, and explicit PASS / FAIL / BLOCKED variants. BIM and module doctrine require acceptance artifacts and retrospectives. Preserve evidence identity and independent ownership while repairing the incomplete FFM adoption.

Technical-reference and design examination continues; this section will be refined if later evidence changes a claim.

## 7. RANKED DEFECT FINDINGS

**Provisional ranking:** the following findings are already supported by current text. The complete ordered set and final identifiers will be consolidated after remaining technical-reference examination. These are defects in doctrine, not claims that a deployed application was tested or exploited.

### P-01 — The commerce mutation examples trust the caller with money authority

- **Classification:** DEFECT. **Severity:** BLOCKER.
- **Affected files / location:** `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md`, §3 PaymentIntent creation, §5 “Order Status Updates,” §11 “Input Validation” and “Order Security.”
- **Evidence:** The PaymentIntent route passes request-body items, shipping cost, and coupon discount into its total calculator. The order-status POST accepts `orderId`, `status`, and `paymentIntentId`; for caller-selected `processing` plus any truthy intent ID it sets `set_paid = true` using the privileged WooCommerce service. It neither authenticates/authorizes the target order nor retrieves and verifies the claimed Stripe payment. Section 11, conversely, says never trust client totals and requires server validation.
- **Why defective / consequence:** A server-side arithmetic operation does not establish trusted prices. A caller can request a paid state without proving payment. Copying the supplied route can enable underpayment or unauthorized paid-order mutation; a later signed webhook does not make this public mutation safe.
- **Recommended resolution:** Bind checkout to an authorized server-owned order; load authoritative catalog, shipping, discount, tax, and amount values; verify currency/amount/order/payment binding; derive paid state from verified processor evidence. Supply a safe example and negative tests for manipulated totals, foreign orders, and invented payment IDs. Do not rely on a checklist to reverse the example's executable behavior.

### P-02 — Privileged authorization still uses caller-editable metadata

- **Classification:** DEFECT. **Severity:** BLOCKER.
- **Affected files / location:** `04_REFERENCE_MANUALS/AUTH_MANUAL.md` §12 superadmin create/list/delete routes and §13 role mirroring; `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md` §2 role-trigger baseline; `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md` §9 metadata role guidance. Opposing rule: AUTH's role-table law and `04_REFERENCE_MANUALS/DATABASE_MANUAL.md` role storage restrictions.
- **Evidence:** Unlabelled privileged-route examples authorize with `requester.user_metadata.is_qr_superadmin`. The kit's auth-user insert trigger derives the application role from `raw_user_meta_data.role`, while public signup exists. New role-table guidance prohibits metadata as authorization truth. Some older snippets are explicitly marked advisory; this finding concerns remaining unqualified operational examples and the provisioning boundary, not those warnings alone.
- **Why defective / consequence:** Moving a role into a protected table does not protect it when the write source remains untrusted. Following the old checks or unchecked trigger can confer elevated authorization based on self-supplied data. The text does not supply an enforced privileged provisioning boundary for the metadata-to-role transition.
- **Recommended resolution:** Make public signup assign only a server-chosen nonprivileged role; require an independently authorized server path for elevation; retire unsafe metadata authorization examples and align consumers with the protected role table. Verify both reads and writes with adversarial role-assignment tests. The actual external starter kit was not available for implementation verification.

### P-03 — The user-creation Server Action relies on a layout for authorization

- **Classification:** DEFECT. **Severity:** BLOCKER.
- **Affected file / location:** `04_REFERENCE_MANUALS/AUTH_MANUAL.md`, “User Creation,” server-action example and authorization explanation.
- **Evidence:** The pattern places `protectPage` in an admin route-group layout and describes that as authorization for a service-role-backed user-creation action. The action itself has no equivalent caller/role authorization check.
- **Why defective / consequence:** A layout rendering gate is not the authorization boundary of a separately invocable server mutation. A privileged action must verify its own caller and permitted operation. A copied example can expose user creation independently of the protected screen.
- **Recommended resolution:** Authenticate and authorize inside every privileged action/route before using the admin client; centralize the reusable check and test direct unauthorized invocation, not only navigation redirects.

### P-04 — Payment webhook failure can be acknowledged as successful delivery

- **Classification:** DEFECT. **Severity:** BLOCKER.
- **Affected files / location:** `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md` §9 `handlePaymentSucceeded` / `handlePaymentFailed`; `04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md` §8 upsert handler; `03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md` webhook test guidance G5.
- **Evidence:** Commerce handlers catch failed order writes, log, and return to a route that sends success. Subscription code awaits an upsert without inspecting its returned error before acknowledging. Testing guidance prescribes always-200 responses to avoid retries. No durable event acceptance/recovery mechanism accompanies that blanket rule.
- **Why defective / consequence:** Valid signature proves origin, not successful processing. A database/order outage can lose the required entitlement or fulfillment update while telling the processor delivery succeeded. Duplicate and out-of-order delivery also need a defined policy; upsert alone does not prove lifecycle ordering correctness.
- **Recommended resolution:** Acknowledge only after durable acceptance or completed processing; return a retryable failure when neither occurs. Define replay/deduplication/order handling and reconciliation ownership. Test storage failure, redelivery, duplicate events, and stale lifecycle events. Unknown event types may be intentionally acknowledged; that is different from failed processing of a required event.

Remaining process and technical findings are incomplete. Primary technical documentation verification is pending and will be cited in the final entries.

## 8. RANKED SUGGESTIONS

INCOMPLETE — pending examination and evidence synthesis.

## 9. CROSS-DOCUMENT CONTRADICTIONS

INCOMPLETE — pending examination and evidence synthesis.

## 10. RECOMMENDED HUMAN DECISIONS

INCOMPLETE — pending examination and evidence synthesis.

## 11. FILE-BY-FILE REVIEW APPENDIX

INCOMPLETE — pending examination and evidence synthesis.

## 12. COVERAGE MANIFEST

Discovery found 31 Markdown documents in the five numbered doctrine directories: 3 constitution, 6 pipeline-agent, 9 build-methodology, 7 technical-reference, and 6 design-system documents. MANIFEST identifies these as live, although its headline says 29. Header tiers and explicit delegation will be respected; no additional hierarchy is assumed.

Repository-level agent instructions and the local factory-docs-update skill are operating instructions to examine, not authorization to perform their workflows. MANIFEST, CHANGELOG, lint tooling, and the archive maintenance README support doctrine governance. `_ARCHIVE/` superseded manuals, `_AUDIT/` prior audits, session logs, and existing response logs are historical/evidence material, not automatically current doctrine. `_OTHERS/` classification remains pending.

The per-file manifest and reading status will be completed during examination. `astra-review/` is experiment infrastructure, excluded from the health assessment. Its intake contents will not be accessed.

## 13. AMBIGUITIES / UNKNOWNS

INCOMPLETE — pending examination and evidence synthesis.

## 14. FINAL FACTORY HEALTH ASSESSMENT

INCOMPLETE — pending examination and evidence synthesis.

