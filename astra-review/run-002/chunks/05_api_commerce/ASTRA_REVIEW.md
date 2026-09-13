# CHUNK 05 — API / COMMERCE REVIEW

## 1. STATUS

COMPLETE

Branch verified: `factory-docs-review-astra-w-chunks`. Initial working tree clean. The complete Run 002 Chunk Review Contract and only the Chunk 05 execution-plan definition govern this examination. This report is the only authorized write target.

All three primary sources were fully examined; the single supporting authority reference is logged in §11. The report was written incrementally, then checked for the required 12-section structure, complete defect evidence fields, stable unique IDs, severity ordering, integer scores, coverage, and finding counts. Whitespace/diff checks passed. Only this report was modified; no Factory doctrine changed, no commit or push occurred, no other chunk began, and no synthesis was performed. Examination stops here.

## 2. SCOPE

Objective: examine the current API, service-integration, commerce, payment, subscription, and webhook doctrine for correctness, security, consistency, and executable recovery controls.

Primary files selected by principal subject from discovery of `04_REFERENCE_MANUALS/`:

- `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md` — APIs, services, and external integrations.
- `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md` — commerce, checkout, and payments.
- `04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md` — Stripe subscription integration.

Other discovered files are classified by filename and excluded from substantive primary review: `AUTH_MANUAL.md` (authentication/security), `DATABASE_MANUAL.md` (data), `APP_ARCHITECTURE_MANUAL.md` (architecture), and `STATE_MANAGEMENT_MANUAL.md` (state management). Security/data sources may be consulted narrowly to verify a specific security or authority dependency, with each access logged below.

Out of scope: other chunks' substantive reviews, Run 001, all Fable/Sol/disposition artifacts, synthesis material, Factory-wide conclusions, implementation, doctrine changes, commits, and pushes.

## 3. DOMAIN MODEL

The API manual puts project-specific fetching, normalization, and errors in services, with credential-bearing requests behind server routes. Kit auth primitives are consumed directly; browser Supabase operations depend on RLS. Public catalog data can be cached, while private or current operational data should not be shared-cached. Webhooks and explicit sync jobs update local records and external CRM fields.

The commerce manual specializes this model to WooCommerce catalog/orders plus Stripe one-time payments. It prescribes an unpaid order before a PaymentIntent, a client cart storing cents, server validation of totals, Stripe Elements confirmation, and a webhook updating order status. Coupons, shipping, and checkout state feed that flow. Its examples also allow a browser-triggered status update, creating a second authority path that the findings examine.

The subscription playbook assigns money truth to Stripe and the local subscription mirror to Supabase. It separates roles from commercial tiers. Authenticated checkout resolves a tier to a configured Price, creates/reuses a Customer, creates a subscription or changes an existing one, and relies on signed webhooks to write the mirror through a service-role client. Users can read their own subscription, but cannot directly write it. Success-page polling waits for mirror propagation; the Customer Portal manages cancellation and payment details. Developer/DevOps schema handoff is stated; periodic reconciliation and several failure-handling features are deferred.

## 4. FIVE-DIMENSION SCORECARD

| Dimension | Score | Evidence-based justification |
|---|---:|---|
| Correctness | 2 | Sound money-authority and raw-signature principles coexist with a forged paid-status path, untrusted pricing inputs, and erroneous acknowledgment/deduplication examples (D03/D04/D05/D01). |
| Consistency | 2 | Explicit rules conflict with executable examples: server trust versus caller-supplied payment truth, raw bodies versus reconstructed JSON, and the subscription schema versus bootstrap/UPSERT instructions (D03/D04/D09/D10). |
| Completeness | 2 | Core happy paths are documented, but retry identity, event convergence, durable follow-up, refund/dispute completion, and local API negative acceptance criteria are materially incomplete (D02/D06/D07/D18/D16). |
| Executability | 2 | A competent implementer must repair checkout field/helper mismatches and subscription lifecycle persistence, then invent several failure/authority controls before safe execution (D11/D10/D05/D08). |
| Maintainability | 3 | Domain territories and service/normalization ownership provide useful structure; duplicated quick references and incompatible same-name examples create meaningful drift risk (D12, S01/S03). |

Scores apply only to this chunk's doctrine, not to deployed applications or the Factory as a whole.

## 5. WHAT IS STRONG

1. **Explicit money authority and separation from roles.** Subscription §§1 and 6 (lines 39–58, 92, 395, 489–503) distinguish Stripe truth, the Supabase mirror, structural permission, and commercial entitlement. Preserve these separate authorities and composed gate helpers; they prevent a paid tier from becoming administrative privilege.
2. **A restricted subscription write boundary.** Subscription §3 (lines 205–223) establishes owner-only reads and blocked user writes, with a server-only service-role writer in §6. Preserve this defense against users granting themselves subscriptions, while resolving checkout's bootstrap exception explicitly (C05-D10).
3. **Raw-body Stripe verification before dispatch.** Commerce §9 (lines 1524–1549, 1616–1633) and subscription §6 (lines 399–422) demonstrate the correct ordering and reject invalid signatures. Preserve this as a separate control from processing reliability; a valid signature alone cannot establish durable completion.
4. **Explicit scope and reuse boundaries.** Commerce scope declaration (lines 11–18), subscription territory declaration (line 10), and API §1 kit exception (lines 34–35) define one-time versus recurring territory and forbid redundant wrappers around completed kit primitives. Preserve these boundaries when consolidating examples.
5. **Useful service and data-boundary principles.** API §§1, 4, 7 (lines 72–110, 522–538, 1000–1005) separate secrets from browsers, private data from public caching, and wire shapes from UI types. Subscription §8 (lines 581–589) makes server/client imports explicit. Preserve the principles while repairing the inconsistent contracts and error examples below.
6. **Concrete negative cases and operational checks already exist.** Subscription §§11–12 (lines 717–721, 738–759) require redirect rejection cases, complete tier-comparison combinations, unknown Price mapping checks, and confirmation that upgrades retain one subscription. Commerce §10 covers declines and authentication challenges. Preserve these checks and extend them to the API trust and failure cases missing from the local recipes (C05-D16).

## 6. PRIORITY FINDINGS

1. **C05-D03 — BLOCKER:** the order-status route can turn an arbitrary caller assertion into a privileged paid-order mutation.
2. **C05-D04 — BLOCKER:** Stripe collection is not bound to an authorized order and trusted server quote.
3. **C05-D05 — HIGH:** webhook success acknowledgment can conceal failure to persist the business result.
4. **C05-D06 — HIGH:** checkout retries and concurrent requests lack stable creation identity despite one-order/customer/subscription intentions.
5. **C05-D07 — HIGH:** distinct delayed or replayed events can overwrite newer order or entitlement state.

Defect totals: **18 — BLOCKER 2; HIGH 10; MEDIUM 6; LOW 0.** Suggestions: **3**. Full findings below are ranked by severity and operational impact; IDs remain stable from their first incremental write.

## 7. RANKED DEFECTS

### C05-D03 — Public order-status mutation accepts the caller's assertion that payment succeeded

- Classification: DEFECT. Severity: BLOCKER.
- Affected file/location: `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md`, §3 “Handling Payment Results,” lines 381–405; §5 “Order Status Updates” and service implementation, lines 786–807 and 830–866; §11 “Order Security,” lines 1750–1753.
- Evidence: the browser posts `orderId`, `status: 'processing'`, and `paymentIntentId`. The route sets `set_paid = true` whenever that status and any truthy paymentIntentId are supplied, then forwards the mutation through a WooCommerce client using server credentials. No caller authentication, order ownership, Stripe retrieval, amount/currency comparison, or permitted-transition check occurs.
- Why this establishes a defect: a direct request with a chosen order ID and an arbitrary nonempty paymentIntentId reaches the paid mutation without proof of payment. Keeping WooCommerce credentials on the server does not authorize callers to exercise them. A webhook in parallel does not secure this alternative route.
- Operational consequence: unpaid orders can be marked paid; arbitrary orders can also be completed, cancelled, or failed by callers who know their IDs.
- Recommended resolution: reserve payment-derived status changes for verified server payment evidence, bound to the stored order and payment attempt. Authenticate and authorize every non-webhook mutation, including an explicit guest-order capability where supported. Validate legal transitions and prevent the browser from choosing payment truth.

### C05-D04 — The payment amount is not bound to a trusted order quote

- Classification: DEFECT. Severity: BLOCKER.
- Affected file/location: `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md`, §1 security principles, lines 101–107; §3 PaymentIntent creation, lines 199–255; §5 order creation, lines 740–765; §6 totals helper, lines 1193–1218; §9 success handler, lines 1573–1586; §11 input validation, lines 1740–1746.
- Evidence: beneath “never trust client,” PaymentIntent creation accepts item `price`, shipping `cost`, and coupon `discount` from JSON and passes them directly to `calculateOrderTotal`. It neither fetches nor checks the referenced order, sets its ID from the caller in metadata, and ignores the WooCommerce total returned by order creation. Order shipping cost is also copied from the request. The success webhook marks that metadata-selected order paid without checking its expected amount/currency/payment binding.
- Why this establishes a defect: doing arithmetic on the server does not establish the authority of its inputs. The imported `calculateOrderTotal` implementation is absent from this manual (the provided helper is `calculateCartTotals`, which multiplies supplied prices); therefore an undocumented trusted lookup cannot be credited. The displayed route and webhook leave no enforced connection between the purchased order and collected amount.
- Operational consequence: a copied implementation can accept reduced prices, shipping, or invented discounts and mark the selected order paid after a smaller payment succeeds. Legitimate totals can also diverge between checkout, WooCommerce, and Stripe.
- Recommended resolution: derive one authoritative, versioned server quote from validated products/variations/quantities, shipping selection, coupon eligibility, and tax policy; persist it on an authorized order. Create/reuse the intent from that order, bind the intent ID, and verify amount, currency, and order association before any paid transition. Treat client totals as display-only.

### C05-D05 — Webhook acknowledgment conceals failed business persistence

- Classification: DEFECT. Severity: HIGH.
- Affected files/locations: `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md`, §9, lines 1552–1607; `04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md`, §6, lines 416–423 and 455–476; §14, lines 860–862.
- Evidence: commerce success/failure handlers catch WooCommerce update errors and return normally; the endpoint then returns `{ received: true }`. The subscription UPSERT awaits a result without inspecting its error, while its guidance says “Always return 200” and its handler sketch ends in 200. Reconciliation is a future roadmap item.
- Why this establishes a defect: the commerce failure path demonstrably reports successful receipt after failed required work. The subscription recipe provides no checked write/acknowledgment contract and conflates ignoring unsupported events with acknowledging failed supported events. An awaited call by itself does not establish successful database persistence. Signature rejection is present and is not the missing control.
- Operational consequence: a customer can pay while order or entitlement state stays stale, with retries suppressed by the success response and no defined recovery owner.
- Recommended resolution: acknowledge supported events only after checked durable completion or durable enqueue. Return a retryable failure for transient processing faults, distinguish unknown event types from failed known events, and provide alerting plus a replay/reconciliation procedure for unresolved events. Missing order/user mappings must become actionable records rather than silent returns.

### C05-D06 — Checkout creation does not implement the retry and concurrency identity its invariants require

- Classification: DEFECT. Severity: HIGH.
- Affected files/locations: `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md`, §§1, 3–5, 11, lines 82–107, 238–255, 444–477, 708–758, 1753; `04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md`, §§5 and 7, lines 327–335, 349–376, 515–534.
- Evidence: every commerce initialization creates another order and another PaymentIntent; neither creation carries a stable idempotency key or persisted payment-attempt lookup. The subscription flow creates Customers/Sessions without such identity and only diverts an existing subscription when the local status is exactly `active`.
- Why this establishes a defect: after creation succeeds but its response is lost, retrying repeats creation. Two initial checkout requests can both observe no active subscription before either completion webhook arrives. A nonterminal existing subscription such as the playbook's own `past_due` state also falls through the active-only guard. A database unique user row cannot prevent creation of multiple external Customers or subscriptions.
- Operational consequence: duplicate orders, payment attempts, customers, or subscriptions; possible duplicate collection and manual billing cleanup. This is outbound creation identity, distinct from inbound delivery deduplication in C05-D01.
- Recommended resolution: define a stable, authorized checkout attempt across retries; atomically coordinate concurrent attempts and reuse/retrieve existing external objects. Specify customer identity persistence independently of successful subscription activation, idempotency-key scope, unknown-outcome recovery, and handling for every existing subscription state before allowing new billing relationships.

### C05-D07 — Event handlers can regress newer commerce or subscription state

- Classification: DEFECT. Severity: HIGH.
- Affected files/locations: `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md`, §9, lines 1573–1607; `04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md`, §6, lines 430–476; §14, lines 860–862.
- Evidence: commerce applies `processing` or `failed` directly from each delivered event. Subscription updates write the event object's tier/status/dates by subscription ID; deletion sets `canceled`; checkout completion retrieves current Stripe state, but later update events use their own snapshots. No transition, freshness, or per-aggregate ordering rule is given.
- Why this establishes a defect: consider a failed attempt followed by successful payment, delivered success-first and failure-last: the written commerce handler finishes at `failed`. Likewise, an old active subscription update delivered after deletion can restore an older active mirror. Replaying a formerly valid event after a newer state change is not covered by “same event twice = same final state.” An update arriving before a subscription row exists can affect zero rows without a repair path.
- Operational consequence: paid orders regress, cancelled access can be restored, or entitlement changes disappear. Deduplicating event IDs alone cannot resolve ordering among distinct events.
- Recommended resolution: define aggregate-level convergence using authoritative retrieval and coordinated application or another explicit freshness/transition strategy. Reject stale transitions, check zero-row writes, recover missing mappings, and specify how the mirror is repaired. Keep this separate from signature verification and duplicate delivery handling.

### C05-D10 — Subscription bootstrap and resubscribe writes conflict with the prescribed schema

- Classification: DEFECT. Severity: HIGH.
- Affected file/location: `04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md`, §3, lines 178–198, 215–223, 244–264; §5, lines 327–335, 365–376; §6, lines 448–473, 489–491.
- Evidence: `tier` is mandatory and has no default; `status` defaults to `active`; `user_id` is unique. Checkout must save the new customer ID before payment, but the playbook supplies no unpaid bootstrap tier/status or authorized write exception to “the webhook is the only trusted writer.” Webhook UPSERT conflicts only on `stripe_subscription_id`. Cancellation retains the old row, and subsequent subscription creation is allowed by the active-only branch.
- Why this establishes a defect: saving only the stated customer/user link cannot satisfy the required tier. Guessing a paid tier while accepting the default status creates premature active state. If an unpaid placeholder is supplied by undocumented convention, the first webhook with a new subscription ID attempts an insert that conflicts on the already-present unique user. Resubscribing with a different subscription ID hits the same conflict against the cancelled user's retained row. The written conflict target does not reconcile either lifecycle.
- Operational consequence: first-time or returning paid users can fail to acquire an entitlement record; different implementers may bypass RLS or invent premature paid state to unblock checkout.
- Recommended resolution: decide a customer-link storage model and explicit unpaid bootstrap state, with narrowly authorized checkout writes. Make webhook persistence reconcile the intended user and current subscription atomically, while protecting against late events for replaced subscriptions. Supply first-subscribe, abandoned-checkout, cancellation, and resubscribe examples compatible with all constraints.

### C05-D01 — Webhook deduplication neither excludes concurrent execution nor identifies events reliably

- Classification: DEFECT. Severity: HIGH.
- Affected file/location: `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md`, §11 “Idempotency for Webhooks,” lines 1692–1717.
- Evidence: the handler chooses `payload.webhookId || payload.order?._id`, reads `processed_webhooks`, performs the work, then inserts a marker without checking the insert error.
- Why this establishes a defect: two concurrent deliveries can both read “absent” and execute before either marker exists. A crash after the effect and before the marker repeats the effect on retry. An order ID also identifies an aggregate, not each distinct event concerning that order; subsequent legitimate events can be suppressed. A unique marker added after the work alone does not repair these interleavings.
- Operational consequence: duplicate external effects or silently skipped order transitions despite following the prescribed duplicate-handling pattern.
- Recommended resolution: require a stable provider/event identity, atomic claiming with explicit in-progress/completed/retryable states, checked persistence results, and effect-level idempotency or transactional coordination. Define recovery for abandoned claims and partial external success.

### C05-D08 — Manual sync exposes a privileged mutation as an unprotected GET

- Classification: DEFECT. Severity: HIGH.
- Affected files/locations: `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md`, §13, lines 1835–1887, 1892–1907, 1961–1963; supporting `04_REFERENCE_MANUALS/AUTH_MANUAL.md`, “Security Best Practices,” lines 1516–1519, 1567–1570, 1597.
- Evidence: `/api/sync` exports `GET()` with no request identity or role check, fetches all items to sync, and invokes a function that upserts database records. The admin button uses an ordinary GET. Auth doctrine explicitly requires user validation in API routes and role checks on every request.
- Why this establishes a defect: the example does not enforce its apparent admin boundary at the server; placing the button under an admin component does not authorize the route. It also assigns mutating semantics to a read request. No documented outer guard is identified in this example.
- Operational consequence: callers reaching the route can trigger repeated integration writes and external API work. Browser or intermediary GET behavior can also initiate work unexpectedly. Exact data privilege depends on the omitted Supabase client, so this is not a claim that every possible deployment bypasses RLS.
- Recommended resolution: require an authenticated, role-authorized mutation endpoint, explicit tenant scope and applicable CSRF protection, plus concurrency/rate controls appropriate to a bulk job. Make job acceptance and progress access obey the same authorization boundary.

### C05-D09 — Generic webhook verification signs reconstructed JSON and combines supposedly alternative schemes

- Classification: DEFECT. Severity: HIGH.
- Affected files/locations: `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md`, §11, lines 1582–1586 and 1651–1671; `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md`, §9, lines 1624–1628; `04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md`, §6, lines 399–422.
- Evidence: the generic endpoint parses JSON before validation; its validator hashes `JSON.stringify(payload)`. It labels the shared-secret header “Option 1” and HMAC “Option 2,” but executes both checks in sequence. Both Stripe recipes explicitly require raw-body verification.
- Why this establishes a defect: reserialization can remove whitespace or alter numeric representation, producing different signed bytes for a valid delivered payload. Providers using only the described HMAC option are rejected by the preceding shared-secret-header requirement. No provider-specific canonical JSON contract is specified to justify the reconstruction.
- Operational consequence: copying the general-purpose recipe can reject legitimate webhooks, stopping order or CRM synchronization; implementers must invent how to select authentication schemes.
- Recommended resolution: make each provider's signature/header/encoding contract explicit; capture the raw body once, authenticate it before parsing, select one documented verification scheme, and use the provider's supported verifier or a carefully specified HMAC comparison. Include valid signed payloads with whitespace and both absent/invalid headers in verification cases.

### C05-D02 — Required webhook follow-up has no durable acceptance or recovery boundary

- Classification: DEFECT. Severity: HIGH.
- Affected file/location: `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md`, §11 endpoint and “Async Follow-Up Pattern (Fire-and-Forget),” lines 1597–1607 and 1675–1688; final cheat sheet, line 2068.
- Evidence: the handler calls `triggerAsyncFollowUp` without awaiting it and returns success; the follow-up posts an order sync, parses any response as JSON, and only logs rejection.
- Why this establishes a defect: successful webhook acknowledgment is independent of successful follow-up acceptance. There is no durable job, failure record, retry, or reconciliation path. HTTP failure responses are not checked before logging completion. Process termination or an unavailable sync endpoint can therefore leave an acknowledged order unsynchronized.
- Operational consequence: integration work disappears without a provider retry trigger; operators have no defined recovery record.
- Recommended resolution: distinguish optional telemetry from required work. Durably enqueue required sync before acknowledgment, or complete it under a retry-safe handler; specify retry limits, failed-job visibility, and recovery ownership.

### C05-D11 — The displayed checkout caller cannot satisfy its order endpoint contract

- Classification: DEFECT. Severity: HIGH.
- Affected file/location: `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md`, §4 initialization, lines 444–477; billing schema, lines 567–577; §5 `PlaceOrderRequest` and route, lines 671–705, 718–749; §3 pricing import/call, lines 199 and 223–228; §6 helper, lines 1193–1218.
- Evidence: `initializePayment` omits the required `shippingMethod`, while the route unconditionally dereferences `body.shippingMethod.id`. It sends email as `customerEmail`, while the endpoint reads `billing.email` and the billing form has no email field. Selected coupon state is sent to neither order creation nor intent creation. The payment route calls `calculateOrderTotal({ ... })`, but the provided pricing module exports `calculateCartTotals(items, options)` instead.
- Why this establishes a defect: even an honest request produced by the shown client reaches an undefined shipping-method dereference; the snippets disagree on field placement, coupon delivery, and helper name/signature. These are linked examples for the same paths/modules, not merely unspecified visual components.
- Operational consequence: checkout can fail before payment begins, omit receipts or selected discounts, or fail compilation when assembled from the manual. Correcting only price authority does not fix the request-shape break.
- Recommended resolution: define one validated request/response contract and a single server quote interface; align the caller, form/state mapping, route, and helper. Explicitly define email, shipping selection, coupon code, failure responses, and permitted checkout revisions. Verify the documented happy path using those exact contracts.

### C05-D13 — Revalidation secret comparison fails open when the environment variable is absent

- Classification: DEFECT. Severity: HIGH.
- Affected file/location: `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md`, §9 “ISR and Revalidation,” lines 1343–1364.
- Evidence: the route destructures `secret` from JSON and rejects only when `secret !== process.env.REVALIDATION_SECRET`. It never requires the configured secret to exist.
- Why this establishes a defect: with the environment variable unset and the request omitting `secret`, both sides are `undefined`; the rejection condition is false. A request containing a path or tag passes the supposed authorization check. This follows from the displayed equality test without assuming framework-specific behavior.
- Operational consequence: a deployment configuration error converts the endpoint into unauthenticated cache invalidation, allowing disruption or excessive regeneration.
- Recommended resolution: validate a nonempty configured secret at startup and reject missing/invalid supplied credentials before comparison. Bound allowed invalidation targets and verify the unset-secret case explicitly.

### C05-D18 — Refund and dispute actions are advertised but acknowledged without their required work

- Classification: DEFECT. Severity: MEDIUM.
- Affected file/location: `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md`, §9, lines 1552–1570, 1610–1613, 1638–1643; production checklist, lines 1777–1786.
- Evidence: the event table requires a refund to update the order and notify the customer, and a dispute to flag the order and notify an admin. `handleRefund` only logs “Refund processed”; disputes fall into the unhandled-event log; both paths reach success acknowledgment. The production checklist asks for dispute notifications but supplies no event-processing handoff.
- Why this establishes a defect: the shown handler reports acceptance without implementing or durably delegating the promised business action. A placeholder for refund logic is visible, but there is no explicit readiness condition preventing that stub from being treated as a complete webhook integration.
- Operational consequence: order/payment records or operator awareness can remain incorrect after a reversal or dispute. External dashboard/email configuration might supply some notification, but it is not evidence that the documented order updates occur.
- Recommended resolution: define the minimum refund/dispute state changes, including partial versus full refunds, or explicitly mark these integrations incomplete until implemented and checked. Establish who handles notifications and failures, and acknowledge only after the required local work is safely accepted.

### C05-D16 — Local validation recipes do not require API trust-boundary and event-failure negative cases

- Classification: DEFECT. Severity: MEDIUM.
- Affected files/locations: `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md`, §§10–11, lines 1663–1693 and 1740–1786; `04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md`, §12, lines 732–777, and deployment verification, lines 821–828; `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md`, testing cross-reference, line 2079.
- Evidence: commerce exercises successful cards, declines, and 3DS, followed by unchecked security statements. Subscription tests cover pure helpers and a sequential successful subscribe/upgrade path. Neither local test recipe requires direct forged order-status calls, cross-user object IDs, tampered totals, checkout concurrency, invalid signatures, failed persistence, reordered events, or resubscription. The API manual delegates testing through a generic service-testing reference.
- Why this establishes a defect: the local acceptance instructions can be followed without exercising the negative cases that distinguish the documented server controls from UI behavior, or durable processing from successful signature checks. These are material conditions of the supplied payment/API recipes, not optional visual tests.
- Operational consequence: the demonstrated authority and lifecycle defects can pass the stated local smoke checks and security checklists.
- Recommended resolution: make a minimum API-level negative matrix explicit, with expected status, absence of unauthorized effects, persisted final state, and retry/recovery evidence. Assign who produces and reviews it. The linked `TESTING_PLAYBOOK.md` was not opened under this chunk's reference boundary; this finding concerns local executable acceptance criteria, not a claim that the entire Factory lacks these tests.

### C05-D14 — Service error contracts collapse dependency failure into successful absence or client error

- Classification: DEFECT. Severity: MEDIUM.
- Affected files/locations: `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md`, §3, lines 200–217, 241–249, 315–367; §4, lines 409–417; §8, lines 1270–1283; §10, lines 1500–1506; `04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md`, §3, lines 260–267, and §8, lines 568–571.
- Evidence: product failures return the same empty list/null as absence, and the GET route responds with public-cache headers without a failure indicator. The generic route maps every returned service error to 400. Subscription lookup ignores the query error and treats any missing `data` as a free user. Elsewhere, API §3 explicitly demonstrates `{ data, error, success }` as a consistent result.
- Why this establishes a defect: an unavailable provider, a missing resource, and valid empty data have different recovery semantics. The shown defaults erase that distinction; upstream outages can be cached as empty catalogs, and a temporarily failed subscription read appears to be a known absence. Avoiding a UI crash does not require losing error identity.
- Operational consequence: misleading empty/free states, inappropriate client retries or no retries, and harder incident diagnosis. Denying access on a failed read can be a defensible fail-closed choice, but it must not be represented as confirmed commercial absence.
- Recommended resolution: adopt an explicit success/not-found/unavailable/invalid/forbidden contract, map it to appropriate HTTP and UI behavior, and keep failed results out of successful public caches. Preserve safe UI rendering while retaining machine-readable error and correlation information.

### C05-D15 — Success polling can confirm an old tier and claims receipt of unverified payment

- Classification: DEFECT. Severity: MEDIUM.
- Affected file/location: `04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md`, §1, line 92; §7, lines 525–530; §9, lines 615–631.
- Evidence: the upgrade path returns the same success page used for new subscriptions. That page is instructed to show confirmation whenever the tier is no longer `free`, and to say “Your payment was received!” after five unsuccessful polls. The playbook separately says the redirect is cosmetic and must never alone confirm payment.
- Why this establishes a defect: an existing Starter user upgrading to Pro already meets the non-free predicate before the upgrade webhook is applied. A timeout proves neither receipt nor activation; visiting the success URL alone can reach that message.
- Operational consequence: users are told an upgrade is complete while the old tier remains, or that payment was received when its status is unknown. This is a false UI confirmation, not evidence that the page itself grants unauthorized access.
- Recommended resolution: poll a server-authorized operation or expected subscription transition, including target tier and qualifying status, rather than generic non-free state. Use an honest pending/unknown timeout and a recovery/support path; preserve the rule that redirects do not establish payment truth.

### C05-D12 — API examples assign incompatible signatures and representations to the same service contracts

- Classification: DEFECT. Severity: MEDIUM.
- Affected file/location: `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md`, §3, lines 184–217, 273–286; §4, line 410; §7, lines 1000–1005, 1043–1048, 1083–1097; §8, line 1271.
- Evidence: the first `fetchProducts(page, perPage)` returns `ProductsResponse`; the route passes a third `category` argument; normalization redefines that same service as zero-argument `Promise<Product[]>`; the shop consumer destructures `{ items, error }`. `Product` in the same named type module is first a wire-shaped type with string prices and snake_case fields, then a normalized camelCase type with numeric prices. The rule says UI code never sees wire casing.
- Why this establishes a defect: these snippets name the same modules/functions without declaring versions, alternatives, or adapters. The documented consumer does not match either declared service return contract completely, and the route's category argument is not supported by the first signature. The ambiguity changes implementation and type-checking outcomes.
- Operational consequence: copied examples fail type checks, ignore requested filters, or propagate inconsistent data shapes into UI code; implementers must decide which example to rewrite.
- Recommended resolution: establish distinct wire and internal types, one service signature/result envelope, and explicit normalization ownership. Align route and component consumers, or label incompatible examples as independent alternatives with their own contracts.

### C05-D17 — The per-product coupon calculator has no line-item information and applies one flat discount

- Classification: DEFECT. Severity: MEDIUM.
- Affected file/location: `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md`, §8, lines 1356–1406 and 1450–1459.
- Evidence: `calculateCouponDiscount(coupon, subtotal)` advertises `fixed_product`; that branch, explicitly commented “Per-product discount,” returns one `amount * 100`, exactly like `fixed_cart`. The function receives no product IDs, eligibility, or quantities. The UI stores this result as its applied discount.
- Why this establishes a defect: a per-product discount cannot distinguish one eligible unit from several using subtotal alone. For example, carts with the same subtotal and different eligible quantities must receive different per-unit discounts, but the function necessarily returns the same number. The comment that this is “handled differently” does not implement or name a separate path.
- Operational consequence: displayed coupon totals diverge from product/quantity-based eligibility and from the eventual authoritative order quote. C05-D04 separately addresses trusting those totals for collection.
- Recommended resolution: obtain the discount from an authoritative quote with eligible line items, or supply and validate the required line/quantity model for a display estimate. Do not advertise `fixed_product` support through the flat-cart branch.

## 8. RANKED SUGGESTIONS

### C05-S01 — Maintain one coherent, mechanically checked example path per integration

- Classification: SUGGESTION. Rank: 1.
- Evidence/location: API §§3–4 and 7 reuse the same modules/types with different contracts; commerce §§3–6 are a multi-file implementation recipe; subscription §§3, 5–7 require compatible schema and application behavior.
- Expected value: a small maintained example fixture checked for type compatibility, request/response agreement, and lifecycle invariants would catch future drift after the concrete defects are resolved.
- Recommendation: choose an owner for each canonical example, record its tested dependency versions, and derive or validate copied snippets from that fixture. This is an ongoing maintenance improvement, separate from correcting today's defects.

### C05-S02 — Attach an integration ownership and recovery record to each adopted recipe

- Classification: SUGGESTION. Rank: 2.
- Evidence/location: API §§11–13 cover webhook/CRM/sync operations; subscription §13 provides a concrete developer/DevOps migration handoff, while §14 defers reconciliation.
- Expected value: the existing handoff can be made more operationally useful without reconstructing other Factory domains.
- Recommendation: record provider/account/environment, credential and webhook owner, alert destination, retry/replay operator, mapping ownership, and a correlation identifier linking local and external objects. Include evidence locations for recovery drills. Required durable processing corrections remain C05-D01/D02/D05/D07.

### C05-S03 — Consolidate duplicate quick references and declare example limits beside the recipe

- Classification: SUGGESTION. Rank: 3.
- Evidence/location: API has two “§10 Quick Reference” sections (lines 1442 and 1993), while its contents list ends at §10 although webhooks/CRM/sync follow. Commerce declares one-time WooCommerce territory but uses USD/US examples throughout.
- Expected value: fewer independently maintained templates and clearer applicability reduce selection errors and future drift.
- Recommendation: keep one indexed quick reference; identify the currency, tax, shipping, inventory configuration, and provider-version assumptions of each worked example. Label illustrative placeholders and identify the required production behavior they stand for.

## 9. CROSS-DOMAIN DEPENDENCIES

| Classification | Boundary and evidence | Bounded handoff |
|---|---|---|
| DEPENDENCY | Auth/server authorization: API §13 sync and commerce §5 mutations exercise external or database authority; AUTH “Security Best Practices” requires user/role checks. | Preserve API-local authorization even when a page is protected. C05-D03/D08 are supported local example defects; the rest of the auth system is not assessed here. |
| DEPENDENCY | Data/RLS: API §6 profile and generic table services rely on the request-scoped Supabase client; subscription §§3/6 rely on schema constraints and a service-role writer. | Security/data review should establish table and column write permissions, tenant isolation, and bootstrap writer authority. The database manual was not opened; no broad RLS verdict is made. |
| DEPENDENCY | Testing: both payment sources explicitly point to `TESTING_PLAYBOOK.md`; API points to service tests. | The testing domain should verify how the negative matrix and persistence/recovery evidence in D16 attach to gates. Its source was not opened under this chunk's permitted-reference boundary. |
| DEPENDENCY | Delivery/operations: subscription §13 assigns schema design to developers and production migrations/access/backups to DevOps; §14 postpones reconciliation. | Assign concrete replay/reconciliation and incident ownership before relying on the integration in production. No DevOps or release doctrine was opened. |
| SYNTHESIS FLAG | The subscription playbook's money-truth model is strong, but its local recipes and the one-time commerce route do not consistently enforce that model. | Consider a shared payment-authority and durable-event acceptance invariant across the relevant domains. This is a handoff question, not a Factory-wide verdict. |
| SYNTHESIS FLAG | Multiple active manuals provide reusable snippets whose contracts or safeguards diverge from their own principles (D03/D04/D09/D10/D12). | Consider ownership and evidence requirements for executable doctrine examples. Do not infer the state of unexamined manuals. |

No additional cross-domain contradiction is asserted from an unexamined source. The narrow AUTH/API contradiction is already evidenced in C05-D08.

## 10. AMBIGUITIES / UNKNOWNS

- **Inventory reservation is asserted, not operationally established here.** Commerce §1 (lines 82–88) says Order-First reserves inventory; §5 creates a pending order. Required WooCommerce settings/plugins, reservation timing, expiration/release, concurrent stock handling, and recovery after abandoned checkout are not stated. Actual reservation behavior is UNKNOWN without the target integration/configuration; no vendor behavior has been invented to fill that gap.
- **Entitlement policy needs a concrete transition table.** Subscription §3 (line 253) says to check period end plus status, while §12/appendix emphasize tier comparison. Grace periods, past-due/unpaid access, trial behavior, expired periods, and how upgraded access relates to successful collection or extra authentication are not fully specified. Do not treat tier alone as payment confirmation. No undocumented provider default is credited as a policy.
- **Schema lifecycle decisions remain unresolved.** Is customer identity independent of subscriptions, what is the unpaid bootstrap state, and how should an old subscription's events interact with a replacement? D10 demonstrates the present incompatibility; deciding the intended model belongs to doctrine owners.
- **Target runtime and external versions are not supplied.** SDK-version claims, CLI-secret behavior, provider dashboard instructions, prices, and deployment-specific environment binding were read as current doctrine but not independently verified against a target repository or live vendor service. No version-dependent claim is classified as obsolete on recall alone.
- **Scope limits are real.** Supabase-native commerce is explicitly not covered; trials, annual billing, organization subscriptions, dunning enhancements, and reconciliation appear in the subscription roadmap. Their presence in a roadmap is not evidence of an implemented production control, and their absence is not automatically a separate defect.
- **The surrounding test and release gates remain unexamined.** Whether they already catch these local recipe defects is UNKNOWN. This report establishes what the assigned doctrine says, not the security or completeness of any deployed implementation.

## 11. COVERAGE MANIFEST

| Primary source | Status |
|---|---|
| `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md` | EXAMINED — all 2,092 lines, §§1–13, both Quick Reference sections, cross-reference list and history |
| `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md` | EXAMINED — all 1,808 lines, scope declaration, §§1–11, cross-reference list and history |
| `04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md` | EXAMINED — all 911 lines, §§1–14, appendix, cross-reference list and history |

| Supporting file | Access and reason |
|---|---|
| `04_REFERENCE_MANUALS/AUTH_MANUAL.md` | CROSS-REFERENCE — targeted heading/auth/route/RLS search to locate authority guidance; read only “Security Best Practices,” lines 1512–1601, to verify that API examples must validate users, roles, and inputs at the server boundary. Not fully reviewed. |

No other doctrine cross-reference opened. Discovery listed filenames only for the other excluded manuals. References to historical runs inside assigned current doctrine were read as part of those current files; no historical run artifacts or prior review opinions were opened.

Procedural inputs: complete `astra-review/run-002/packets/CHUNK_REVIEW_CONTRACT.md`; only the Chunk 05 definition in `astra-review/run-002/packets/EXECUTION_PLAN.md`. These are scope controls, not reviewed doctrine.

Examination method: complete line-numbered reads of all primary files, bounded cross-file contract tracing, and isolated in-memory JavaScript evaluations of selected conditions. Those evaluations confirmed the arbitrary payment-ID paid branch (D03), absent-secret equality (D13), and raw-versus-reserialized HMAC difference (D09); they also exposed the generic pagination guard's inability to reject `NaN`. No app code was created, no application/provider integration was executed, and no deployment correctness is claimed. No external sources, prohibited review artifacts, or synthesis material were opened.

## 12. SYNTHESIS HANDOFF

- **Strongest conclusion:** the assigned domain has useful architectural principles but cannot be used as a safely copyable payment/integration recipe without correcting its authority, lifecycle, and failure paths.
- **Most serious defect:** C05-D03 permits a caller's unverified fields to cause a paid-order mutation; C05-D04 independently leaves collected money unbound to the trusted order quote.
- **Most important strength to preserve:** Stripe owns money truth; the application mirrors it, separates commercial tiers from structural roles, and authenticates raw webhook bodies before processing.
- **Unresolved issue most likely to affect another domain:** the owner and gate for durable event completion, replay/reconciliation, and authoritative entitlement repair across API, data, testing, and operations.
- **Findings deserving cross-domain consideration:** D03/D04 (authority), D01/D02/D05/D06/D07 (durable and retry-safe integration), D10 (data/writer contract), and D16 (negative evidence expectations). These are inputs for later synthesis, not a synthesis performed here.
