# PART_05 — correction mapping draft

DRAFT FOR REVIEW — no execution approval. Source outcomes are not relabeled approved.

### FC-050 — Public order-status mutation accepts the caller's assertion that payment succeeded

**Proposed disposition:** BLOCKED. **Authority:** certified correction YES; package outcome remains proposed. CONDITIONAL: DEC-05 guest capability (required authorization still applies). 

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/05_api_commerce_corrections.md:43`):

- **Certified record:** CF-08 · Severity BLOCKER · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C05-D03 · Fable none
- **Evidence:** Astra C05 §7 C05-D03; Sol C05 §3 ("Reusable Factory payment doctrine must never teach that a browser-selected payment state can directly cause authoritative paid-order state").
- **Defect surfaces (`0a787cb`):** `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md`, §3 "Handling Payment Results", §5 "Order Status Updates" and its service implementation, §11 "Order Security".
- **Defect:** the browser posts `orderId`, `status: 'processing'` and any `paymentIntentId`. The route sets `set_paid = true` and forwards the change through server WooCommerce credentials with:
  - no authentication
  - no ownership check
  - no Stripe retrieval
  - no amount/currency comparison
  - no transition check
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - Payment-derived order status changes come only from verified server-side payment evidence bound to the stored order and payment attempt. The browser never chooses payment truth.
  - Every non-webhook order mutation authenticates and authorizes, including an explicit guest-order capability where guest checkout is supported, and validates legal transitions.
- **Preserve:** server-side WooCommerce credentials. Sol: holding server credentials is not authorization to use them on a caller's behalf.
- **Likely affected docs / consumers:** ECOM §3/§5/§11; FC-051 (quote binding), FC-054 (transitions), FC-063 (forged-status negative case), FC-036 (operation-local authorization).
- **Verification intent:**
  - No live recipe sets a paid or processing state from a client-supplied status or `paymentIntentId`.
  - The client success path only displays or polls.
  - The negative matrix (FC-063) includes a forged status call that produces no state change.
- **Open decision:** DEC-05, the guest-order capability model (Jarvis). DEC-04, the operation-local authorization invariant.
- **Proposed route:** `SYNC`. **Wave 1 BLOCKER.**

**Mapping proposal — ENGINEER-PROPOSED:** The browser may display or poll payment status; it may not choose paid or processing state. A payment-derived transition requires verified server-side evidence bound to the stored order and payment attempt, including amount and currency. Non-webhook mutations authenticate and authorize the operation and target, including an explicitly approved guest capability where supported, then validate the state transition.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:181` — ## 3. PaymentIntent Flow; MANIFEST ← 3: API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:661` — ## 5. Order Management; MANIFEST ← 3: API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:1722` — ## 11. Security Checklist; MANIFEST ← 3: API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.

**Touch proposal:** C-050. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-050` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-051 — PaymentIntent amount is computed from client-supplied prices, shipping and discount despite "never trust client"

**Proposed disposition:** BLOCKED. **Authority:** certified correction YES; package outcome remains proposed. CONDITIONAL: DEC-05 design only (certified behavior remains required). 

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/05_api_commerce_corrections.md:67`):

- **Certified record:** CF-08 · Severity BLOCKER · Review CONFIRMED · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C05-D04 · Fable FBL-D019 (primary)
- **Evidence:** Astra C05 §7 C05-D04; Sol C05 §3 ("Server-side arithmetic does NOT transform untrusted values into authoritative values"); Fable §7 FBL-D019, §9 rows 8–9, §2 row 2.
- **Defect surfaces (`0a787cb`):**
  - `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md`: §1 principles, §3 PaymentIntent creation, §5 order creation, §6 totals helper, §9 success handler, §11 checklist
  - `03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md`: §1.8, §4.3 (generic error message)
- **Defect:**
  - Under the comment "Recalculate total on server – never trust client", the route feeds `body.items[].price`, `body.shipping.cost` and `body.coupon.discount` into `calculateOrderTotal`.
  - The order ID is caller-set in metadata, and the WooCommerce total is ignored.
  - The success webhook marks the metadata-selected order paid without an amount/currency binding.
  - The handler returns Stripe `error.message` to the client, contrary to TESTING §4.3.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - **Required: what the certified finding needs (server-authoritative pricing and payment/order binding).**
    - The server derives the charge amount from authoritative sources:
      - catalog prices for validated products, variations and quantities;
      - a server-validated shipping selection;
      - server-validated coupon eligibility;
      - the applicable tax policy.
    - It never uses client-supplied prices, shipping cost or discount amounts.
    - The payment is bound to an authorized order. The order is not selected by caller-set metadata alone, and amount, currency and order association are verified before any paid transition.
    - Client totals are display-only.
    - Errors return a generic client message, with a redacted server-side log (FC-021).
  - **Architectural recommendation: awaiting approval (DEC-05). Not a certified-finding requirement.**
    - Implement the requirement through one persisted, versioned server quote on the authorized order.
    - The PaymentIntent is created or reused from that quote, and its ID is bound to it.
    - Other designs that satisfy every "Required" bullet stay open for Jarvis/Tony.
- **Preserve:** the §1 "never trust client" principle and the §11 checklist, which are already correct; correct Stripe usage.
- **Likely affected docs / consumers:** ECOM; TESTING §4.3; FC-060 (checkout contract), FC-067 (coupon), FC-021 (log redaction), FC-063 (tampered-totals negative case).
- **Verification intent (tests the required behavior; independent of the quote design):**
  - The PaymentIntent recipe reads no price, shipping cost or discount amount from the request body; only identifiers and selections.
  - The server-side pricing computation it relies on is defined in the manual, not an undocumented import.
  - The success path verifies amount, currency and order association before marking an order paid, and does not trust caller metadata to select the order.
  - The error path returns a generic message.
  - The negative matrix includes tampered totals (FC-063).
  - Additional checks if the recommendation is approved: the quote is persisted and versioned, and the PaymentIntent ID is bound to it.
- **Open decision:** DEC-05 (Jarvis → Tony): the server pricing sources, the tax policy, and whether to adopt the persisted/versioned quote recommendation. **Containment note:** marking the current sample unsafe contains the risk but does not close FC-051. Closure needs the "Required" behavior landed and verified.
- **Proposed route:** `SYNC`. **Wave 1 BLOCKER.**

**Mapping proposal — ENGINEER-PROPOSED:** Accept product/variation identifiers, quantities, shipping selection and coupon code, never caller prices, shipping costs or discount amounts. Validate quantities and product eligibility; load authoritative catalog prices; validate the shipping selection and coupon eligibility; apply the declared tax policy; calculate currency-safe totals on the server. Bind the payment to the authorized order and verify payment identity, amount, currency and order association before marking paid. Client totals are display-only. Return generic failures and redact logs. A persisted versioned quote is a proposed design, not a certified requirement.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:181` — ## 3. PaymentIntent Flow; MANIFEST ← 3: API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:661` — ## 5. Order Management; MANIFEST ← 3: API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:877` — ## 6. Cart Logic; MANIFEST ← 3: API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:1511` — ## 9. Webhook Handling; MANIFEST ← 3: API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:1722` — ## 11. Security Checklist; MANIFEST ← 3: API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.

**Touch proposal:** C-051. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-051` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-052 — Commerce and subscription webhook acknowledgment conceals failed business persistence

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/05_api_commerce_corrections.md:149`):

- **Certified record:** CF-09 · Severity HIGH · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C05-D05 · Fable none
- **Evidence:** Astra C05 §7 C05-D05; Sol C05 §4 (HIGH minimum; a BLOCKER candidate depending on architecture). Certified closure: HIGH, 2026-09-27.
- **Defect surfaces (`0a787cb`):**
  - `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md` §9
  - `04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md` §6, §14
- **Defect:**
  - The ECOM §9 handlers catch WooCommerce update errors and still return `{ received: true }`.
  - The STRIPE §6 UPSERT result is never inspected, and the guidance says "Always return 200".
  - Reconciliation is only a roadmap item.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - Supported events are acknowledged only after checked durable completion or checked durable enqueue (durable acceptance).
  - **Failure before durable acceptance** (the required write or the enqueue fails or is unconfirmed) returns a retryable failure, not `{ received: true }`.
  - **Failure after durable acceptance** (a worker fails on an already-accepted event) does not retroactively invalidate the lawful acknowledgment. It is handled by durable retry/recovery: bounded retries, failed-job visibility, alerting, a replay/reconciliation procedure and a recovery owner.
  - Unknown event types are distinguished from failed known events.
  - Missing order or user mappings become actionable records instead of silent returns.
- **Preserve:** signature rejection; ignoring unsupported events.
- **Likely affected docs / consumers:** ECOM §9, STRIPE §6/§14; **FC-020** (the same mechanism in TESTING G5, brief 03), FC-059, FC-062, FC-054.
- **Verification intent:**
  - No unconditional "Always return 200" remains.
  - The handlers inspect write and enqueue results before acknowledging.
  - A documented pre-acceptance failure yields a retryable non-success response.
  - A documented post-acceptance worker failure leaves the acknowledgment standing and produces a durable retry or failed-job record with a recovery path.
  - Reconciliation is a defined procedure, not a roadmap note.
  - TESTING G5 and these manuals state the same two-phase contract.
- **Open decision:** DEC-03, the Factory acknowledgment contract (shared with FC-020). Sol's conditional BLOCKER is noted under DEC-22.
- **Proposed route:** `SYNC`. Wave 1 companion to BLOCKER FC-020.

**Mapping proposal — ENGINEER-PROPOSED:** For supported events, check business persistence or durable enqueue before acknowledging. Pre-acceptance failure returns a retryable failure. After durable acceptance, worker failures enter bounded durable retries and visible failed-work reconciliation with an alert and recovery owner. Unsupported events are explicitly distinguished from failed supported events. Missing order/user mappings create actionable recovery records, not silent success.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:1511` — ## 9. Webhook Handling; MANIFEST ← 3: API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:391` — ## 6. The Webhook Handler; MANIFEST ← 1: ECOMMERCE_AND_PAYMENTS_MANUAL.
- `04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:840` — ## 14. Phase 3 Roadmap; MANIFEST ← 1: ECOMMERCE_AND_PAYMENTS_MANUAL.

**Touch proposal:** C-052. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-052` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-053 — Checkout creation lacks the retry and concurrency identity its invariants require

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/05_api_commerce_corrections.md:179`):

- **Certified record:** CF-09 · Severity HIGH · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C05-D06 · Fable none
- **Evidence:** Astra C05 §7 C05-D06; Sol C05 §4.
- **Defect surfaces (`0a787cb`):**
  - `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md` §§1, 3–5, 11
  - `04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md` §§5, 7
- **Defect:**
  - Every initialization creates a new order and a new PaymentIntent, with no idempotency key.
  - The subscription flow creates Customers and Sessions without a stable identity and diverts only when the status is exactly `active`.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - A stable, authorized checkout attempt persists across retries, and concurrent attempts are coordinated atomically.
  - External objects are reused or retrieved rather than recreated.
  - The idempotency-key scope and unknown-outcome recovery are specified.
  - Customer identity is persisted independently of activation.
  - Every existing subscription state is handled, not only `active`.
- **Preserve:** the one-order/customer/subscription intentions the manuals already state.
- **Likely affected docs / consumers:** ECOM, STRIPE; FC-055, FC-056.
- **Verification intent:**
  - The recipes show idempotency-key usage and an attempt lookup.
  - The existing-subscription guard covers `past_due` and other nonterminal states.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Persist one authorized checkout-attempt identity across retries and claim it atomically against concurrent requests. Scope provider idempotency keys to that attempt and operation, reuse or retrieve existing external objects after an unknown outcome, and reconcile before creating a replacement. Persist customer identity independently of paid activation. Handle every documented subscription state, not only active.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:181` — ## 3. PaymentIntent Flow; MANIFEST ← 3: API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:412` — ## 4. Checkout Implementation; MANIFEST ← 3: API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:661` — ## 5. Order Management; MANIFEST ← 3: API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:1722` — ## 11. Security Checklist; MANIFEST ← 3: API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:319` — ## 5. The Checkout Flow; MANIFEST ← 1: ECOMMERCE_AND_PAYMENTS_MANUAL.
- `04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:507` — ## 7. The Tier Upgrade Pattern; MANIFEST ← 1: ECOMMERCE_AND_PAYMENTS_MANUAL.

**Touch proposal:** C-053. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-053` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-054 — Event handlers can regress newer commerce or subscription state

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/05_api_commerce_corrections.md:204`):

- **Certified record:** CF-09 · Severity HIGH · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C05-D07 · Fable none
- **Evidence:** Astra C05 §7 C05-D07; Sol C05 §4.
- **Defect surfaces (`0a787cb`):**
  - `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md` §9
  - `04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md` §6, §14
- **Defect:** handlers apply each event's snapshot directly, with no transition, freshness or ordering rule. Out-of-order delivery can end a paid order at `failed` or restore a cancelled subscription.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - State converges per aggregate, through authoritative retrieval or explicit freshness and transition rules.
  - Stale transitions are rejected.
  - Zero-row writes are checked and missing mappings recovered.
  - Mirror repair is specified.
- **Preserve:** the separation from signature verification and duplicate-delivery handling.
- **Likely affected docs / consumers:** ECOM §9, STRIPE §6/§14; FC-052, FC-056.
- **Verification intent:** the documented scenarios converge correctly: success-then-failure delivered in reverse order ends paid, and a late update after deletion does not restore access.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Converge each order or subscription aggregate using authoritative provider retrieval or explicit freshness and legal-transition rules. Reject stale transitions; check zero-row updates and repair missing mappings. A late event for an old subscription may not overwrite its replacement. Define reconciliation of the local mirror independently of inbound deduplication.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:1511` — ## 9. Webhook Handling; MANIFEST ← 3: API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:391` — ## 6. The Webhook Handler; MANIFEST ← 1: ECOMMERCE_AND_PAYMENTS_MANUAL.

**Touch proposal:** C-054. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-054` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-055 — Subscription bootstrap and resubscribe writes conflict with the prescribed schema

**Proposed disposition:** BLOCKED. **Authority:** certified correction YES; package outcome remains proposed. CONDITIONAL: K-SUBSCRIPTION-MODEL. 

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/05_api_commerce_corrections.md:224`):

- **Certified record:** CF-09 · Severity HIGH · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C05-D10 · Fable none
- **Evidence:** Astra C05 §7 C05-D10; Sol C05 §4.
- **Defect surfaces (`0a787cb`):** `04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md` §3 (schema), §5, §6.
- **Defect:**
  - `tier` is required with no default, `status` defaults to `active`, and `user_id` is unique.
  - Checkout must save the customer ID before payment, but no unpaid bootstrap state is defined.
  - The webhook UPSERT conflicts only on `stripe_subscription_id`, so the first-subscribe and resubscribe paths collide.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - The customer-link storage model and an explicit unpaid bootstrap state are decided, with narrowly authorized checkout writes.
  - Webhook persistence reconciles the user and the current subscription atomically and is protected against late events for replaced subscriptions.
  - Four lifecycle examples satisfy every constraint: first subscribe, abandoned checkout, cancellation, resubscribe.
- **Preserve:** the restricted write boundary and the money-authority separation.
- **Likely affected docs / consumers:** STRIPE §3/§5/§6; FC-053.
- **Verification intent:** the schema plus the documented write paths satisfy NOT NULL, the defaults and the unique constraints in all four lifecycle examples.
- **Open decision:** the customer-link storage model (Jarvis).
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Store provider customer identity independently of paid entitlement. Represent an unpaid checkout bootstrap explicitly and permit only narrowly authorized server writes. Reconcile user/current-subscription identity atomically; reject stale updates for replaced subscriptions. Before publishing a recipe, verify first subscribe, abandoned checkout, cancellation and resubscribe against every schema constraint.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:173` — ## 3. Supabase Schema Recipe; MANIFEST ← 1: ECOMMERCE_AND_PAYMENTS_MANUAL.
- `04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:319` — ## 5. The Checkout Flow; MANIFEST ← 1: ECOMMERCE_AND_PAYMENTS_MANUAL.
- `04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:391` — ## 6. The Webhook Handler; MANIFEST ← 1: ECOMMERCE_AND_PAYMENTS_MANUAL.

**Touch proposal:** C-055. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-055` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-056 — Webhook deduplication neither excludes concurrent execution nor identifies events reliably

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/05_api_commerce_corrections.md:244`):

- **Certified record:** CF-09 · Severity HIGH · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C05-D01 · Fable none
- **Evidence:** Astra C05 §7 C05-D01; Sol C05 §4.
- **Defect surfaces (`0a787cb`):** `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md` §11, "Idempotency for Webhooks".
- **Defect:** the handler reads `processed_webhooks`, does the work, then inserts a marker without checking the result, keyed on `webhookId || order._id`. This is non-atomic, and the key identifies an aggregate rather than an event.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - A stable provider event identity is used.
  - Claims are atomic, with in-progress, completed and retryable states, and persistence results are checked.
  - Effects are idempotent or coordinated transactionally.
  - Recovery for abandoned claims and partial external success is defined.
- **Preserve:** the intent of idempotent webhook handling.
- **Likely affected docs / consumers:** API §11; FC-053, FC-054.
- **Verification intent:** the recipe's claim is atomic and checked, two concurrent deliveries cannot both execute, and a later event for the same order is not suppressed.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Use the provider’s stable event ID, never a random fallback. Atomically claim each event with in-progress, completed and retryable states; inspect persistence results. Make effects idempotent or transactional. A bounded lease/recovery process reclaims abandoned work and reconciles partial external success without duplicating completed effects.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:1564` — ## 11. Webhook Integration Patterns; MANIFEST ← 5: APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, DATABASE_MANUAL, ECOMMERCE_AND_PAYMENTS_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.

**Touch proposal:** C-056. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-056` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-057 — Manual sync exposes a privileged mutation as an unprotected GET

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/05_api_commerce_corrections.md:318`):

- **Certified record:** CF-10 · Severity HIGH · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C05-D08 · Fable none
- **Evidence:** Astra C05 §7 C05-D08; Sol C05 §4 and §7.A.
- **Defect surfaces (`0a787cb`):**
  - `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md` §13
  - `04_REFERENCE_MANUALS/AUTH_MANUAL.md`: Security Best Practices
- **Defect:** `/api/sync` exports `GET()` with no identity or role check and upserts database records, contrary to AUTH's every-request validation rule.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - A non-safe-method mutation endpoint, authenticated and role-authorized, with explicit tenant scope.
  - CSRF protection where applicable, plus concurrency and rate controls for bulk jobs.
  - Job acceptance and progress access follow the same authorization boundary.
- **Preserve:** the manual-sync capability itself.
- **Likely affected docs / consumers:** API §13; FC-036 (DEC-04 invariant).
- **Verification intent:** the recipe uses a non-GET method with operation-local authorization, and an unauthenticated invocation is rejected in the documented checks.
- **Open decision:** DEC-04.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Manual synchronization is an authenticated, role-authorized POST operation with explicit tenant scope. Apply the context’s CSRF protection, rate and concurrency controls. Job acceptance, progress reads and retries enforce the same authorization boundary. GET is read-only and cannot initiate synchronization.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:1831` — ## 13. Data Synchronization Patterns; MANIFEST ← 5: APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, DATABASE_MANUAL, ECOMMERCE_AND_PAYMENTS_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.

**Touch proposal:** C-057. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-057` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-058 — Generic webhook verification signs reconstructed JSON and chains supposedly alternative schemes

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/05_api_commerce_corrections.md:337`):

- **Certified record:** CF-10 · Severity HIGH · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C05-D09 · Fable none
- **Evidence:** Astra C05 §7 C05-D09; Sol C05 §4.
- **Defect surfaces (`0a787cb`):**
  - `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md` §11 (validator)
  - `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md` §9 (correct raw-body Stripe pattern)
  - `04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md` §6 (correct raw-body Stripe pattern)
- **Defect:** the API §11 validator hashes `JSON.stringify(payload)` after parsing rather than the raw body. It also runs "Option 1" (shared-secret header) and "Option 2" (HMAC) in sequence, though they are meant as alternatives.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - Each provider's signature, header and encoding contract is explicit.
  - The raw body is captured once and authenticated before parsing.
  - One documented scheme is selected, using the provider's verifier or a specified HMAC comparison.
  - Verification cases include whitespace-bearing signed payloads and absent or invalid headers.
- **Preserve:** the Stripe raw-body recipes.
- **Likely affected docs / consumers:** API §11.
- **Verification intent:** no recipe signs re-serialized JSON, the options are presented as alternatives, and the documented verification cases exist.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Capture the raw request body once. Select exactly one provider-specific signature scheme with its documented header and encoding, verify before parsing, and reject missing or invalid headers. Do not sign reconstructed JSON or chain alternative schemes as cumulative requirements. Test signed whitespace-bearing bodies and malformed or absent signatures.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:1564` — ## 11. Webhook Integration Patterns; MANIFEST ← 5: APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, DATABASE_MANUAL, ECOMMERCE_AND_PAYMENTS_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.

**Touch proposal:** C-058. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-058` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-059 — Required webhook follow-up has no durable acceptance or recovery boundary

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/05_api_commerce_corrections.md:262`):

- **Certified record:** CF-09 · Severity HIGH · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C05-D02 · Fable none
- **Certified severity note:** "HIGH (Sol: HIGH when the follow-up is required business work)".
- **Evidence:** Astra C05 §7 C05-D02; Sol C05 §4.
- **Defect surfaces (`0a787cb`):** `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md` §11, endpoint and "Async Follow-Up Pattern (Fire-and-Forget)"; final cheat sheet.
- **Defect:** the fire-and-forget `triggerAsyncFollowUp` is not awaited. The handler returns success, failures are only logged, and there is no durable job or retry.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - Optional telemetry is distinguished from required work.
  - Required follow-up is durably enqueued before acknowledgment, or completed in a retry-safe handler.
    - **If the enqueue fails or is unconfirmed (before durable acceptance),** the webhook returns a retryable failure instead of acknowledging.
    - **If the follow-up worker fails after the work was durably enqueued,** the webhook acknowledgment stays lawful and is not retroactively invalidated. The failure goes to durable retry/recovery.
  - Retry limits, failed-job visibility and recovery ownership are specified, and HTTP failure responses from the follow-up target are checked.
- **Preserve:** fire-and-forget for genuinely optional telemetry.
- **Likely affected docs / consumers:** API §11 and its cheat sheet; FC-020, FC-052 (DEC-03).
- **Verification intent:**
  - No required follow-up is shown fire-and-forget.
  - A failed enqueue produces a non-success webhook response.
  - A failed follow-up after durable enqueue produces a durable, visible retry or failed-job record with a recovery owner, while the original acknowledgment stands.
- **Open decision:** DEC-03.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Distinguish optional telemetry from required follow-up. Complete required work retry-safely or durably enqueue it before acknowledgment. Failed or unconfirmed enqueue returns retryable failure. A later worker failure uses bounded durable retry, visible failed-work state and a named recovery owner. Inspect non-success HTTP responses from follow-up targets; a resolved fetch is not proof of success.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:1564` — ## 11. Webhook Integration Patterns; MANIFEST ← 5: APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, DATABASE_MANUAL, ECOMMERCE_AND_PAYMENTS_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.

**Touch proposal:** C-059. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-059` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-060 — The displayed checkout caller cannot satisfy its order endpoint contract

**Proposed disposition:** BLOCKED. **Authority:** certified correction YES; package outcome remains proposed. CONDITIONAL: DEC-05. 

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/05_api_commerce_corrections.md:107`):

- **Certified record:** CF-08 · Severity HIGH · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C05-D11 · Fable none as primary
- **Evidence:** Astra C05 §7 C05-D11; Sol C05 §4.
- **Defect surfaces (`0a787cb`):** `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md`, §4 initialization and billing schema, §5 `PlaceOrderRequest` and route, §3 pricing import, §6 helper.
- **Defect:**
  - `initializePayment` omits the required `shippingMethod`, which the route dereferences.
  - Email is sent as `customerEmail`, but the route reads `billing.email`.
  - Coupon state reaches neither order creation nor intent creation.
  - `calculateOrderTotal` does not match the exported `calculateCartTotals`.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - One validated request/response contract and one server quote interface (FC-051).
  - Caller, form/state mapping, route and helper are aligned.
  - Email, shipping selection, coupon code, failure responses and permitted checkout revisions are defined.
  - The documented happy path is verified with those exact contracts.
- **Preserve:** the scope declaration (one-time vs recurring territory).
- **Likely affected docs / consumers:** ECOM §§3–6; FC-068 (checkout store shape), FC-051.
- **Verification intent:** a contract-level consistency check across the linked snippets:
  - `shippingMethod` is present;
  - the email location agrees;
  - the coupon is delivered;
  - the helper name and signature match.
- **Open decision:** none beyond DEC-05.
- **Proposed route:** `SYNC`. Wave 1, paired with FC-051.

**Mapping proposal — ENGINEER-PROPOSED:** Use one validated checkout contract across form, state, route and service. The request carries billing.email, validated line identifiers/quantities, shippingMethod and couponCode; it carries no authoritative monetary values. The response identifies the authorized order/payment attempt or a typed generic failure. The server pricing operation from the same contract supplies totals. Revisions to items, shipping or coupon invalidate the old payment binding before a new attempt is released.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:181` — ## 3. PaymentIntent Flow; MANIFEST ← 3: API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:412` — ## 4. Checkout Implementation; MANIFEST ← 3: API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:661` — ## 5. Order Management; MANIFEST ← 3: API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:877` — ## 6. Cart Logic; MANIFEST ← 3: API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.

**Touch proposal:** C-060. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-060` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-061 — Revalidation secret comparison fails open when the environment variable is absent

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/05_api_commerce_corrections.md:358`):

- **Certified record:** CF-10 · Severity MEDIUM · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C05-D13 · Fable none
- **Evidence:** Astra C05 §7 C05-D13; Sol C05 §4 (MEDIUM by default; HIGH when invalidation scope or cost is material). Certified closure: MEDIUM, 2026-09-27.
- **Defect surfaces (`0a787cb`):** `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md` §9, "ISR and Revalidation".
- **Defect:** the route rejects only when `secret !== process.env.REVALIDATION_SECRET`, so when both are undefined the check passes.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - A non-empty configured secret is validated at startup.
  - Missing or invalid supplied credentials are rejected before comparison.
  - Invalidation targets are bounded, and the unset-secret case is verified.
- **Preserve:** the revalidation capability.
- **Likely affected docs / consumers:** API §9; other secret-comparison recipes (propagation search).
- **Verification intent:** the documented checks include the unset-secret case, and it is rejected.
- **Open decision:** none. Sol's conditional HIGH is noted under DEC-22.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Validate a nonempty revalidation secret at startup. Reject missing or invalid supplied credentials before comparing; an absent environment value never authenticates an absent request value. Authorize and bound invalidation targets. Verify the unset-secret case causes no invalidation.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:1328` — ## 9. Performance Patterns; MANIFEST ← 5: APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, DATABASE_MANUAL, ECOMMERCE_AND_PAYMENTS_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.

**Touch proposal:** C-061. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-061` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-062 — Refund and dispute events are advertised but acknowledged without their required work

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/05_api_commerce_corrections.md:285`):

- **Certified record:** CF-09 · Severity MEDIUM · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C05-D18 · Fable none
- **Evidence:** Astra C05 §7 C05-D18; Sol C05 §5 (placeholders must be unmistakably non-production).
- **Defect surfaces (`0a787cb`):** `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md` §9 (event table, `handleRefund`, dispute fall-through, production checklist).
- **Defect:** the event table requires order updates and notifications for refunds and disputes. `handleRefund` only logs, disputes fall through to an unhandled-event log, and both are acknowledged as successful.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - The minimum refund (partial vs full) and dispute state changes are defined, or these handlers are explicitly marked INCOMPLETE / not for production until implemented.
  - Notification and failure owners are named.
  - Acknowledgment comes only after the required local work is safely accepted.
- **Preserve:** the event table as the requirements statement.
- **Likely affected docs / consumers:** ECOM §9; FC-052, FC-020 (DEC-03).
- **Verification intent:** each advertised event either has its documented local effect or carries an unmistakable INCOMPLETE label, and the production checklist references the decision.
- **Open decision:** DEC-03.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Refund and dispute handling is INCOMPLETE and not a production recipe until the module contract defines partial/full refund effects, dispute transitions, notification and recovery owners. Do not acknowledge a supported event until its required local work is completed or durably accepted under the webhook contract.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:1511` — ## 9. Webhook Handling; MANIFEST ← 3: API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.

**Touch proposal:** C-062. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-062` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-063 — Local validation recipes do not require API trust-boundary or event-failure negative cases

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/05_api_commerce_corrections.md:426`):

- **Certified record:** CF-05 · Severity MEDIUM · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C05-D16 · Fable none
- **Evidence:** Astra C05 §7 C05-D16; Sol C05 §5 (conditional, pending a testing-domain cross-check). Certified closure: MEDIUM, 2026-09-27.
- **Defect surfaces (`0a787cb`):**
  - `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md` §§10–11
  - `04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md` §12 and deployment verification
  - `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md` (testing cross-reference)
  - `03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md`
- **Defect:** the local test recipes cover happy paths, declines and 3DS. They do not require these negative cases:
  - forged status calls
  - cross-user IDs
  - tampered totals
  - concurrency
  - invalid signatures
  - failed persistence
  - reordering
  - resubscription
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - A minimum API-level negative matrix covers those eight classes. Each case states the expected status, the absence of unauthorized effects, the persisted final state and the retry/recovery evidence.
  - The matrix has a named producer and reviewer.
  - Recommended placement: the Factory test owner (TESTING), referenced by ECOM, STRIPE and API rather than duplicated.
- **Preserve:** the existing negative checks:
  - STRIPE §§11–12: redirect rejection, tier combinations, unknown Price mapping, single-subscription upgrades
  - ECOM §10: declines and 3DS
- **Likely affected docs / consumers:** TESTING, ECOM, STRIPE, API. The expected behaviors come from the CF-08, CF-09 and CF-10 outcomes.
- **Verification intent:** all eight case classes appear with expected outcomes, and the ECOM, STRIPE and API recipes link to the matrix.
- **Open decision:** where the matrix lives, TESTING vs each manual (Jarvis).
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** The Architect includes the API trust-boundary matrix in the acceptance contract; the Engineer supplies engineering results, the QA Executor derives independent checks, and the QA Lead approves and grades them. Cover unauthenticated/wrong-role/wrong-owner calls, forged payment status, tampered totals, duplicate and concurrent requests, invalid signatures, pre-acceptance persistence failure, post-acceptance worker failure, and stale/out-of-order events. Each case records status, absence of unauthorized effects, persisted final state and retry/recovery evidence. TESTING_PLAYBOOK owns the matrix; commerce, subscription and API manuals refer to it.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:823` — ## 3.8 Run-verification rituals (promoted from Run 001); MANIFEST ← 11: SOFTWARE_FACTORY_PLAYBOOK, ENGINEER_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, API_AND_SERVICES_MANUAL, DATABASE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.
- `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:1647` — ## 10. Testing Payments; MANIFEST ← 3: API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:732` — ## 12. Testing Strategy; MANIFEST ← 1: ECOMMERCE_AND_PAYMENTS_MANUAL.
- `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:1564` — ## 11. Webhook Integration Patterns; MANIFEST ← 5: APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, DATABASE_MANUAL, ECOMMERCE_AND_PAYMENTS_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.

**Touch proposal:** C-063. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-063` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-064 — Service error-handling doctrine collapses or propagates dependency failures inconsistently with testing and module failure-policy doctrine

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/05_api_commerce_corrections.md:375`):

- **Certified record:** CF-10 · Severity MEDIUM · Review PARTIAL · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C05-D14 · Fable FBL-D022 (primary)
- **Evidence:** Astra C05 §7 C05-D14; Sol C05 §5; Fable §7 FBL-D022, §9 row 9.
- **Defect surfaces (`0a787cb`):**
  - `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md` §3 (Error Handling Template), §4, §6, §8, §10 (cheat sheet)
  - `04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md` §3, §8
  - `03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md` §1.8, §2.2, §4.3
  - `03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md` §7
- **Defect:**
  - Failure, absence and empty data are collapsed into one result.
  - Public caches can hold an empty catalog after an outage.
  - Every error is mapped to 400.
  - A failed subscription read is treated as a free user.
  - The template propagates raw upstream `error.message` to clients.
  - Degrade-by-default contradicts BIM §7's per-module failure policy.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - An explicit result contract (success, not-found, unavailable, invalid, forbidden) maps to HTTP and UI behavior.
  - Services return typed errors, and routes map them to generic client messages without raw upstream text.
  - Failed results are never served from successful public caches.
  - Degrade vs fail-closed follows BIM §7's per-module failure policy rather than a universal "return empty array".
  - A failed entitlement read is never represented as confirmed absence.
- **Preserve:** safe UI rendering; the `{ data, error, success }` envelope; machine-readable error and correlation information.
- **Likely affected docs / consumers:** API §3/§4/§6/§8/§10, STRIPE §3/§8; TESTING §2.2 test 4 (must be satisfiable); FC-021, FC-051.
- **Verification intent:**
  - The cheat-sheet "Graceful Degradation — return empty array on error" is removed or scoped by failure policy.
  - No route template forwards `error.message`.
  - TESTING §2.2 test 4 passes against the template.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Services return an explicit typed outcome: success, not-found, unavailable, invalid or forbidden. Routes map it to the approved HTTP/UI behavior with generic client messages and no upstream error text. Do not cache failures as successful public data. Degrade or fail closed according to the module’s approved failure policy; an unavailable entitlement read is not confirmed absence.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:166` — ## 3. Service Layer Implementation; MANIFEST ← 5: APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, DATABASE_MANUAL, ECOMMERCE_AND_PAYMENTS_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:1164` — ## 8. Error Handling Strategy; MANIFEST ← 5: APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, DATABASE_MANUAL, ECOMMERCE_AND_PAYMENTS_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:1328` — ## 9. Performance Patterns; MANIFEST ← 5: APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, DATABASE_MANUAL, ECOMMERCE_AND_PAYMENTS_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:550` — ## 8. The Service Layer Swap Pattern; MANIFEST ← 1: ECOMMERCE_AND_PAYMENTS_MANUAL.
- `03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:151` — ## Principle 1.8 — Defensive error message assertions for security-sensitive endpoints; MANIFEST ← 11: SOFTWARE_FACTORY_PLAYBOOK, ENGINEER_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, API_AND_SERVICES_MANUAL, DATABASE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.

**Touch proposal:** C-064. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-064` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-065 — Success polling can confirm an old tier and claims receipt of unverified payment

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/05_api_commerce_corrections.md:302`):

- **Certified record:** CF-09 · Severity MEDIUM · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C05-D15 · Fable none
- **Evidence:** Astra C05 §7 C05-D15; Sol C05 §5.
- **Defect surfaces (`0a787cb`):** `04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md` §1, §7, §9.
- **Defect:** the success page confirms whenever the tier is no longer `free`, which an upgrading user already satisfies. After the polls time out it says "Your payment was received!".
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):** polling targets the server-authorized expected transition (target tier plus qualifying status). Timeouts show an honest pending/unknown state with a recovery or support path.
- **Preserve:** the rule that redirects are cosmetic and never confirm payment on their own.
- **Likely affected docs / consumers:** STRIPE §7/§9.
- **Verification intent:** an upgrade from Starter to Pro does not confirm before the Pro transition, and the timeout copy makes no payment claim.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Poll the server-authorized payment attempt and expected target tier with its qualifying subscription status. A pre-existing paid tier is not evidence of this upgrade. A timeout shows pending or unknown and its recovery/support path; it never claims payment receipt. Redirects remain cosmetic.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:507` — ## 7. The Tier Upgrade Pattern; MANIFEST ← 1: ECOMMERCE_AND_PAYMENTS_MANUAL.
- `04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:605` — ## 9. Success Page Polling Pattern; MANIFEST ← 1: ECOMMERCE_AND_PAYMENTS_MANUAL.

**Touch proposal:** C-065. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-065` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-066 — API examples assign incompatible signatures and representations to the same service contracts

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/05_api_commerce_corrections.md:407`):

- **Certified record:** CF-10 · Severity MEDIUM · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C05-D12 · Fable none
- **Evidence:** Astra C05 §7 C05-D12; Sol C05 §5.
- **Defect surfaces (`0a787cb`):** `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md` §3, §4, §7, §8.
- **Defect:** `fetchProducts` has three incompatible signatures and return shapes, and `Product` is both a wire-shaped and a normalized type in the same module.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - Wire and internal types are distinct.
  - One service signature and result envelope is used, with explicit ownership of normalization.
  - Consumers are aligned, or incompatible examples are labeled as independent alternatives with their own contracts.
- **Preserve:** the rule that UI code never sees wire casing.
- **Likely affected docs / consumers:** API; FC-070, best done in the same sync.
- **Verification intent:** every `fetchProducts` and `Product` occurrence matches one declared contract or a labeled alternative.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Declare wire and internal types separately and normalize once at the service boundary. A named operation uses one parameter signature and typed result envelope in its service, route and client examples. Any independent alternative is explicitly labeled with its own contract; callers do not silently mix array, paginated and wrapped results.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:166` — ## 3. Service Layer Implementation; MANIFEST ← 5: APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, DATABASE_MANUAL, ECOMMERCE_AND_PAYMENTS_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:383` — ## 4. API Route Patterns; MANIFEST ← 5: APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, DATABASE_MANUAL, ECOMMERCE_AND_PAYMENTS_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:998` — ## 7. Data Transformation; MANIFEST ← 5: APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, DATABASE_MANUAL, ECOMMERCE_AND_PAYMENTS_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:1164` — ## 8. Error Handling Strategy; MANIFEST ← 5: APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, DATABASE_MANUAL, ECOMMERCE_AND_PAYMENTS_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.

**Touch proposal:** C-066. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-066` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-067 — The per-product coupon calculator has no line-item information and applies one flat discount

**Proposed disposition:** BLOCKED. **Authority:** certified correction YES; package outcome remains proposed. CONDITIONAL: DEC-05 pricing interface. 

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/05_api_commerce_corrections.md:133`):

- **Certified record:** CF-08 · Severity MEDIUM · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C05-D17 · Fable none
- **Evidence:** Astra C05 §7 C05-D17; Sol C05 §5.
- **Defect surfaces (`0a787cb`):** `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md` §8.
- **Defect:** the `fixed_product` branch of `calculateCouponDiscount(coupon, subtotal)` returns the same flat amount as `fixed_cart`. It receives no product, eligibility or quantity input.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):** the discount comes from the authoritative quote with eligible line items, or a display estimate uses a validated line/quantity model. `fixed_product` is not advertised through the flat-cart branch.
- **Preserve:** coupon types that are correct.
- **Likely affected docs / consumers:** ECOM §8; FC-051 (quote).
- **Verification intent:** two carts with the same subtotal but different eligible quantities yield different documented discounts, or the `fixed_product` claim is withdrawn.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** A fixed-product coupon uses validated eligible line items and quantities in the authoritative server pricing operation. Do not advertise fixed_product through a flat-cart subtotal branch. A client calculation is a display estimate only. Verify equal-subtotal carts with different eligible quantities; preserve valid fixed-cart and percentage behavior.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:1285` — ## 8. Coupon System; MANIFEST ← 3: API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.

**Touch proposal:** C-067. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-067` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-068 — ECOMMERCE defers to a checkout store the STATE manual does not define

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/05_api_commerce_corrections.md:459`):

- **Certified record:** CF-07 · Severity LOW · Review UNIQUE (Fable) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra none · Fable FBL-D026
- **Evidence:** Fable §7 FBL-D026.
- **Defect surfaces (`0a787cb`):**
  - `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md` §4, §7, §8
  - `04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md` §6
- **Defect:** ECOM §7 points to STATE for "the full checkout store", then uses `shippingCost`, `couponCode`, `couponDiscount`, `setCoupon` and `clearCoupon`. None of these exist in STATE §6's template.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):** ECOM and STATE share one checkout store shape, and the cross-reference resolves to it.
- **Preserve:** whatever shape is chosen must also satisfy FC-040's personal-data lifecycle.
- **Likely affected docs / consumers:** ECOM §4/§7/§8, STATE §6; FC-060, FC-040.
- **Verification intent:** every store member ECOM uses exists in the STATE template, or ECOM defines it.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** The checkout interaction contract includes shippingCost and couponDiscount as display estimates, couponCode, setCoupon(code) and clearCoupon(), alongside the existing checkout fields. The server revalidates shipping and coupons. STATE_MANAGEMENT_MANUAL owns the shared store shape; ECOMMERCE_AND_PAYMENTS_MANUAL refers to it. Personal fields follow the approved account-transition and retention policy.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:412` — ## 4. Checkout Implementation; MANIFEST ← 3: API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:1224` — ## 7. Checkout Store; MANIFEST ← 3: API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:1285` — ## 8. Coupon System; MANIFEST ← 3: API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:745` — ## 6. Store Templates; MANIFEST ← 3: APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, ECOMMERCE_AND_PAYMENTS_MANUAL.

**Touch proposal:** C-068. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-068` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-069 — Supabase secret environment-variable names differ across manuals

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/05_api_commerce_corrections.md:475`):

- **Certified record:** CF-07 · Severity LOW · Review UNIQUE (Fable) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra none · Fable FBL-D027
- **Evidence:** Fable §7 FBL-D027.
- **Defect surfaces (`0a787cb`):**
  - `03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md` §4.1
  - `04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md` §4
  - `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md` §5
  - `04_REFERENCE_MANUALS/DATABASE_MANUAL.md` §5
  - `02_PIPELINE_AGENTS/RECON_QUESTIONNAIRE.md` S0.6
- **Defect:** TESTING uses `SUPABASE_SECRET_KEY` while STRIPE, API and DATABASE use `SUPABASE_SERVICE_ROLE_KEY`, and RECON notes the newer publishable/secret naming. Fable rates the impact limited because RECON calls doc env names suggestive.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):** one environment-variable names table, including the newer publishable/secret naming, carries a "verify on disk" note, and the manuals reference it.
- **Preserve:** RECON's "doc env names are suggestive; disk wins".
- **Likely affected docs / consumers:** the surfaces above; FC-022 (the E2E target check may depend on these names).
- **Verification intent:** every Supabase key name in live recipes matches the table or cites it.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Verify credential names and capabilities on disk. SUPABASE_SERVICE_ROLE_KEY and SUPABASE_SECRET_KEY are server-only elevated-credential conventions, not interchangeable proof of project configuration; public anon/publishable keys are a separate capability class. RECON_QUESTIONNAIRE S0.6 owns the environment-name/capability table. Record the actual variable, provider key type and server-only exposure without printing values; manuals refer to that table.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `02_PIPELINE_AGENTS/RECON_QUESTIONNAIRE.md:63` — ## SECTION 0 — The Day-1 Ground-Truth Sweep (Run 001 Meta-Lesson); MANIFEST ← 13: APP_FACTORY_BLUEPRINT, ARCHITECT_PLAYBOOK, ARCHITECT_QUESTIONNAIRE, ENGINEER_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, APP_FACTORY_SKILLS_PLAYBOOK, FFM_PLAYBOOK, TESTING_PLAYBOOK, APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:847` — ## 4.1 Supabase-backed apps (StarkReads example); MANIFEST ← 11: SOFTWARE_FACTORY_PLAYBOOK, ENGINEER_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, API_AND_SERVICES_MANUAL, DATABASE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.
- `04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:271` — ## 4. Environment Variables; MANIFEST ← 1: ECOMMERCE_AND_PAYMENTS_MANUAL.
- `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:543` — ## 5. External API Integration; MANIFEST ← 5: APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, DATABASE_MANUAL, ECOMMERCE_AND_PAYMENTS_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/DATABASE_MANUAL.md:390` — ## 5. Row Level Security (RLS); MANIFEST ← 2: API_AND_SERVICES_MANUAL, AUTH_MANUAL.

**Touch proposal:** C-069. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-069` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-070 — API_AND_SERVICES_MANUAL has two "§10 Quick Reference" sections

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/05_api_commerce_corrections.md:496`):

- **Certified record:** CF-13 · Severity LOW · Review CONFLICT · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C05-S03 (SUGGESTION) · Fable FBL-D029
- **Sol adjudication (certified):** ACCEPT DEFECT (2026-09-27): "Duplicate §10 Quick Reference sections and an inconsistent ToC are objective documentation defects, albeit low impact."
- **Evidence:** Fable §7 FBL-D029; Astra C05 §8 (C05-S03, which cites the duplicates at baseline lines 1442 and 1993); register §7.1.
- **Defect surfaces (`0a787cb`):** `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md`, the ToC and both "## 10. Quick Reference" headings.
- **Defect:** "## 10. Quick Reference" appears twice, with overlapping content, before and after §§11–13, and the ToC lists only ten sections.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):** one Quick Reference section, consistent section numbering and a ToC listing every section. The overlapping content is merged, with recipe assumptions declared beside the recipes (C05-S03).
- **Preserve:** the content of both quick references, merged rather than dropped.
- **Likely affected docs / consumers:** API manual; FC-066 (same sync); inbound "§10"/"§11–13" citations (propagation search).
- **Verification intent:** exactly one `## 10.` heading exists, the ToC matches the headings, and inbound section citations resolve.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Maintain one Quick Reference after the numbered API sections. Merge both existing quick-reference bodies without dropping unique content. Keep sections 1–13 stable, number the merged Quick Reference 14, and update the table of contents and incoming references to the actual heading. Declare each recipe’s service contract beside it.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:11` — ## Table of Contents; MANIFEST ← 5: APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, DATABASE_MANUAL, ECOMMERCE_AND_PAYMENTS_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:1442` — ## 10. Quick Reference; MANIFEST ← 5: APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, DATABASE_MANUAL, ECOMMERCE_AND_PAYMENTS_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:1993` — ## 10. Quick Reference; MANIFEST ← 5: APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, DATABASE_MANUAL, ECOMMERCE_AND_PAYMENTS_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.

**Touch proposal:** C-070. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-070` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.
