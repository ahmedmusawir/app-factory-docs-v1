# 05 — API / Commerce / Payments — Correction Brief

> **DRAFT — CORRECTION INTAKE / NOT APPROVED FOR SYNC**

- **Package:** Factory Doctrine Correction Package 001. Index: `FACTORY_DOCTRINE_CORRECTION_INDEX_001.md`.
- **Prepared by:** Claudy (documentation Engineer seat), 2026-10-11. This is not a QA product and certifies nothing.
- **Primary entries:** FC-050 … FC-070 (21), the certified register §5.E. **Contains 2 BLOCKERs: FC-050, FC-051.**
- **Authority:** every outcome is **PROPOSED** for Jarvis (Architect) review and Tony (Director) approval. Nothing here is approved policy.
- **Nature:** these are documentation findings about payment and API recipes. Astra did not claim, and this package does not claim, that any deployed Stark application is exploitable or that vendor runtime behavior was verified. No replacement doctrine text is written.

## Pinned sources

| Ref | Revision | Path |
|---|---|---|
| Certified register / QA | `c6210c3` = `c6210c32480558b343a27726a26822e8d959d0f7` | `astra-review/run-002/synthesis/PART1_FINDINGS_DISPOSITION.md`, `astra-review/run-002/synthesis/QA/PART1_CONVERGENCE_QA.md` |
| Astra chunk 05 / Sol chunk 05 | `c6210c3` | `astra-review/run-002/chunks/05_api_commerce/ASTRA_REVIEW.md`, `astra-review/run-002/chunks/05_api_commerce/SOL_REVIEW.md` |
| Fable (blind) | `39a1c6114d72b22d3550d7ff65234ec0f01418f6` (`origin/factory-docs-review-fable-001`) | `fable-review/run-001/reviews/FABLE_FACTORY_DOCTRINE_REVIEW_001.md` |
| Review baseline | `0a787cb` = `0a787cb826118b4a010765d60e41a449df3ce746` | defect surfaces named per entry |
| Current main | `9c17939` = `9c179392f79b70da099121fc357d3107ad3bb86e` | every surface in this brief is blob-identical to `0a787cb` (QA-4) |

Route codes are as in the index. Short names: ECOM = `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md`; STRIPE = `04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md`; API = `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md`.

**Domain preservation (Astra C05 §5; applies to every entry below):**
- explicit money authority kept separate from roles (Stripe truth, Supabase mirror, permission, entitlement)
- the restricted subscription write boundary (owner reads, blocked user writes, server-only writer)
- raw-body Stripe signature verification before dispatch
- the scope and kit-reuse boundaries
- service/data-boundary principles: secrets server-only, private data uncached, wire types separate from UI types
- the negative checks that already exist

Sol C05 §8: keep these concepts separate in every correction:
- authentication vs operation authorization
- server execution vs trusted input
- authenticity vs successful processing
- deduplication vs ordering
- outbound vs inbound idempotency
- mirror vs provider truth

---

## CF-08 — Commerce money authority / checkout contract (FC-050, 051, 060, 067)

### FC-050 — Public order-status mutation accepts the caller's assertion that payment succeeded
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

### FC-051 — PaymentIntent amount is computed from client-supplied prices, shipping and discount despite "never trust client"
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
  - One authoritative, versioned server quote is persisted on an authorized order. It is derived from validated products, variations and quantities, the shipping selection, coupon eligibility and the tax policy.
  - The PaymentIntent is created or reused from that order, with its ID bound to it.
  - Amount, currency and order association are verified before any paid transition.
  - Client totals are display-only.
  - Errors return a generic client message, with a redacted server-side log (FC-021).
- **Preserve:** the §1 "never trust client" principle and the §11 checklist, which are already correct; correct Stripe usage.
- **Likely affected docs / consumers:** ECOM; TESTING §4.3; FC-060 (checkout contract), FC-067 (coupon), FC-021 (log redaction), FC-063 (tampered-totals negative case).
- **Verification intent:**
  - The PaymentIntent recipe reads no price, shipping cost or discount from the request body.
  - The quote function it calls is documented in the manual.
  - The success path checks the amount/currency/order binding.
  - The error path returns a generic message.
  - The negative matrix includes tampered totals.
- **Open decision:** DEC-05, the server quote source, tax policy and quote versioning scope (Jarvis → Tony).
- **Proposed route:** `SYNC`. **Wave 1 BLOCKER.**

### FC-060 — The displayed checkout caller cannot satisfy its order endpoint contract
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

### FC-067 — The per-product coupon calculator has no line-item information and applies one flat discount
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

## CF-09 — Webhook / event durability, idempotency and ordering (FC-052, 053, 054, 055, 056, 059, 062, 065)

### FC-052 — Commerce and subscription webhook acknowledgment conceals failed business persistence
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
  - Supported events are acknowledged only after checked durable completion or durable enqueue.
  - Transient processing faults return a retryable failure.
  - Unknown event types are distinguished from failed known events.
  - Alerting and a replay/reconciliation procedure exist.
  - Missing order or user mappings become actionable records instead of silent returns.
- **Preserve:** signature rejection; ignoring unsupported events.
- **Likely affected docs / consumers:** ECOM §9, STRIPE §6/§14; **FC-020** (the same mechanism in TESTING G5, brief 03), FC-059, FC-062, FC-054.
- **Verification intent:**
  - No unconditional "Always return 200" remains.
  - The handlers inspect write results.
  - Reconciliation is a defined procedure, not a roadmap note.
  - TESTING G5 and these manuals state the same contract.
- **Open decision:** DEC-03, the Factory acknowledgment contract (shared with FC-020). Sol's conditional BLOCKER is noted under DEC-22.
- **Proposed route:** `SYNC`. Wave 1 companion to BLOCKER FC-020.

### FC-053 — Checkout creation lacks the retry and concurrency identity its invariants require
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

### FC-054 — Event handlers can regress newer commerce or subscription state
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

### FC-055 — Subscription bootstrap and resubscribe writes conflict with the prescribed schema
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

### FC-056 — Webhook deduplication neither excludes concurrent execution nor identifies events reliably
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

### FC-059 — Required webhook follow-up has no durable acceptance or recovery boundary
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
  - Retry limits, failed-job visibility and recovery ownership are specified, and HTTP failure responses are checked.
- **Preserve:** fire-and-forget for genuinely optional telemetry.
- **Likely affected docs / consumers:** API §11 and its cheat sheet; FC-020, FC-052 (DEC-03).
- **Verification intent:** no required follow-up is shown fire-and-forget, and failed follow-up produces a durable, visible record.
- **Open decision:** DEC-03.
- **Proposed route:** `SYNC`.

### FC-062 — Refund and dispute events are advertised but acknowledged without their required work
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

### FC-065 — Success polling can confirm an old tier and claims receipt of unverified payment
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

## CF-10 — API trust boundaries / integration / failure semantics (FC-057, 058, 061, 064, 066)

### FC-057 — Manual sync exposes a privileged mutation as an unprotected GET
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

### FC-058 — Generic webhook verification signs reconstructed JSON and chains supposedly alternative schemes
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

### FC-061 — Revalidation secret comparison fails open when the environment variable is absent
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

### FC-064 — Service error-handling doctrine collapses or propagates dependency failures inconsistently with testing and module failure-policy doctrine
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

### FC-066 — API examples assign incompatible signatures and representations to the same service contracts
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

## CF-05 — Testing / evidence / environment fidelity (FC-063 here)

### FC-063 — Local validation recipes do not require API trust-boundary or event-failure negative cases
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

## CF-07 — Data / RLS / state correctness and privacy (FC-068, 069 here)

### FC-068 — ECOMMERCE defers to a checkout store the STATE manual does not define
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

### FC-069 — Supabase secret environment-variable names differ across manuals
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

## CF-13 — Cross-reference / locator / document-structure hygiene (FC-070 here)

### FC-070 — API_AND_SERVICES_MANUAL has two "§10 Quick Reference" sections
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

---

*End of brief 05. Primary entries: 21 (FC-050 … FC-070). DRAFT — CORRECTION INTAKE / NOT APPROVED FOR SYNC.*
