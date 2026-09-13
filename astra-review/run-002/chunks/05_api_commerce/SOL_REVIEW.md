# SOL REVIEW — ASTRA CHUNK 05
# API / COMMERCE
# ASTRA FACTORY DOCTRINE REVIEW — RUN 002

## 1. REVIEW STATUS

COMPLETE

Reviewer:
Sol

Reviewed artifact:

astra-review/run-002/chunks/05_api_commerce/ASTRA_REVIEW.md

Scope:

This is a secondary review of Astra's Chunk 05 examination.

It is NOT:

- a fresh whole-domain audit,
- an implementation review of a deployed application,
- a final Factory disposition,
- a doctrine repair,
- or Factory-wide synthesis.

Astra's findings remain examiner claims until Factory disposition.

---

## 2. OVERALL ASSESSMENT

Astra's Chunk 05 review is strong.

The report is especially valuable because it distinguishes three different
integration concerns that are often incorrectly collapsed into one:

1. AUTHORITY
   Who is allowed to cause a money/order/subscription state transition?

2. TRUSTED INPUT
   What data is authoritative when computing or accepting money state?

3. DELIVERY / CONVERGENCE
   What happens when external events arrive twice, late, out of order, or while
   local persistence is unavailable?

The current Factory doctrine contains strong high-level principles in all three
areas.

Examples include:

- Stripe owns money truth.
- Local application state mirrors external payment truth.
- Roles and paid tiers remain separate authorities.
- Webhook signatures are verified.
- Server-side routes protect credentials.
- Client totals should not be trusted.

However, several executable recipes violate those principles.

This makes Chunk 05 more serious than a simple documentation-consistency issue.

The Factory is supplying code-shaped examples that can directly teach unsafe
payment and integration behavior.

Astra correctly limits its claims to doctrine as written and does not claim that
a deployed Stark application currently contains these defects.

---

## 3. BLOCKER REVIEW

### C05-D03 — Public order-status mutation accepts caller assertion of payment success

ASTRA:
BLOCKER

SOL PRELIMINARY ASSESSMENT:
ACCEPT — BLOCKER

Reasoning:

This is a direct authority-boundary failure in reusable payment doctrine.

The documented browser flow can submit:

- an order ID,
- a desired status,
- and a nonempty paymentIntentId,

and the server-side path can translate that assertion into a privileged
WooCommerce paid-state mutation.

The problem is not that WooCommerce credentials are exposed.

They are correctly server-side.

The problem is that possession of server credentials is being confused with
authorization to exercise them on behalf of the caller.

The recipe does not establish:

- caller authority,
- ownership of the target order,
- validity of the Stripe payment,
- amount/currency match,
- binding between the payment and order,
- or a legal state transition.

A signed webhook operating elsewhere does not secure this alternative mutation
path.

SOL POSITION:

Accept as BLOCKER.

Reusable Factory payment doctrine must never teach that a browser-selected
payment state can directly cause authoritative paid-order state.

---

### C05-D04 — Payment amount is not bound to a trusted order quote

ASTRA:
BLOCKER

SOL PRELIMINARY ASSESSMENT:
ACCEPT — BLOCKER

Reasoning:

This is the second independent money-authority defect.

The doctrine says not to trust client totals.

The executable PaymentIntent path nevertheless accepts price-bearing inputs
from the request and performs server-side arithmetic on them.

Server-side arithmetic does NOT transform untrusted values into authoritative
values.

The missing trust step is the important part.

The server must obtain authoritative:

- product/variation price,
- quantity rules,
- shipping price,
- coupon eligibility,
- tax behavior,
- currency,
- and expected total,

from trusted sources.

That trusted quote must then be bound to the order/payment attempt.

The written flow does not establish that binding.

SOL POSITION:

Accept as BLOCKER.

This is precisely the kind of example that could result in underpayment while
appearing superficially secure because Stripe itself is used correctly.

---

## 4. HIGH-SEVERITY REVIEW

### C05-D05 — Webhook success acknowledgment conceals failed persistence

ASTRA:
HIGH

SOL PRELIMINARY ASSESSMENT:
ACCEPT — HIGH MINIMUM
BLOCKER CANDIDATE DEPENDING ON FINAL PAYMENT ARCHITECTURE

Reasoning:

A valid signature proves who sent the event.

It does not prove that required business processing succeeded.

If:

payment succeeds
→ webhook arrives
→ local order/subscription persistence fails
→ handler still returns success

then the provider may stop retrying while local truth remains stale.

For an entitlement or fulfillment system where the webhook is the sole trusted
state transition and there is no durable queue/reconciliation mechanism, this
can become catastrophic.

SOL POSITION:

The defect is unquestionably valid.

Keep HIGH as the preliminary severity.

Allow final disposition to elevate it to BLOCKER when the webhook is the only
authoritative transition mechanism and no durable recovery path exists.

---

### C05-D06 — Checkout retry/concurrency identity is missing

SOL ASSESSMENT:
ACCEPT — HIGH

The doctrine expresses invariants such as one intended payment/order/customer
relationship but does not define a stable request identity capable of preserving
those invariants across:

- retry,
- timeout,
- duplicate submit,
- concurrent checkout,
- or unknown response outcome.

A database uniqueness constraint alone cannot prevent duplicate external
resources from being created.

This is a real integration-lifecycle defect.

---

### C05-D07 — Delayed/out-of-order events can regress newer state

SOL ASSESSMENT:
ACCEPT — HIGH

Webhook deduplication and webhook ordering are different problems.

Preventing the same event from running twice does not prevent an older distinct
event from arriving after a newer event.

A payment/subscription mirror therefore needs a convergence or transition rule.

Without one, later delivery can move authoritative local state backward.

This finding is technically strong.

---

### C05-D10 — Subscription bootstrap/resubscribe conflicts with schema

SOL ASSESSMENT:
ACCEPT — HIGH

The schema, checkout bootstrap rules, webhook-writer rule, unique user
constraint, and UPSERT conflict target do not form one executable lifecycle.

A competent Engineer must invent missing semantics for:

- customer creation before subscription,
- unpaid bootstrap state,
- first subscription,
- canceled subscription,
- resubscription,
- and replacement subscription events.

That is a doctrine defect, not simply missing implementation detail.

---

### C05-D01 — Webhook deduplication does not provide atomic event claiming

SOL ASSESSMENT:
ACCEPT — HIGH

The check-then-process-then-insert sequence has a race.

Two deliveries can both observe "not processed" and both execute.

Using an order ID as event identity also risks treating multiple legitimate
events for one aggregate as duplicates.

A durable event-processing design needs:

- provider event identity,
- atomic claim,
- completion state,
- retry/recovery state,
- and effect-level idempotency where required.

Astra correctly distinguishes this from outbound checkout idempotency.

---

### C05-D08 — Privileged sync mutation exposed as unprotected GET

SOL ASSESSMENT:
ACCEPT — HIGH

This repeats an important authority lesson already visible elsewhere in the
Factory:

UI placement is not authorization.

An "admin button" does not authorize the route it calls.

The route itself must authenticate and authorize the operation.

Using GET for a mutation also creates incorrect HTTP semantics and makes
unintentional invocation easier.

This is a local API defect even if downstream database RLS may still reduce some
effects.

---

### C05-D09 — Webhook verification reconstructs signed JSON and combines alternatives

SOL ASSESSMENT:
ACCEPT — HIGH

This finding is well supported.

The generic API example labels secret-header and HMAC checks as alternatives but
executes them sequentially.

The HMAC is also calculated over JSON.stringify(payload) after parsing.

That is not equivalent to verifying the exact bytes originally delivered unless
the provider explicitly defines a canonicalized representation.

The Stripe-specific doctrine correctly teaches raw-body verification.

Therefore the generic example conflicts with the stronger provider-specific
rule.

---

### C05-D02 — Required webhook follow-up uses fire-and-forget execution

SOL ASSESSMENT:
ACCEPT — HIGH WHEN THE FOLLOW-UP IS REQUIRED BUSINESS WORK

The defect depends on the nature of the follow-up.

Fire-and-forget may be acceptable for optional telemetry.

It is NOT sufficient for required business processing.

The displayed example represents synchronization work as part of webhook
handling while providing no:

- durable queue,
- retry record,
- recovery owner,
- or checked HTTP result.

SOL POSITION:

Accept the defect as HIGH for required integration work.

The final doctrine should explicitly distinguish optional side effects from
required durable work.

---

### C05-D11 — Checkout caller and endpoint contracts do not match

SOL ASSESSMENT:
ACCEPT — HIGH

This is an executability defect.

The documented client/server flow disagrees on:

- shipping method presence,
- email location,
- coupon propagation,
- and pricing helper interface.

The important point is that these examples describe one supposed checkout path,
not unrelated alternatives.

A competent Engineer cannot assemble them literally into a reliable flow.

HIGH is reasonable because the defect affects the Factory's principal payment
example.

---

### C05-D13 — Revalidation secret fails open when configuration is missing

ASTRA:
HIGH

SOL PRELIMINARY ASSESSMENT:
ACCEPT DEFECT — MEDIUM BY DEFAULT; HIGH WHEN INVALIDATION SCOPE/COST IS MATERIAL

Reasoning:

The logic defect is real.

If both:

request.secret === undefined

and

process.env.REVALIDATION_SECRET === undefined

then:

secret !== process.env.REVALIDATION_SECRET

is false.

The request therefore passes the intended secret check.

However, this primarily exposes cache invalidation / regeneration capability,
not payment authority or direct data modification.

SOL POSITION:

Accept defect.

Preliminary severity MEDIUM.

HIGH remains reasonable when:

- arbitrary paths/tags can be invalidated,
- regeneration is expensive,
- the endpoint can be abused for substantial resource consumption,
- or cached security-sensitive behavior depends on invalidation.

Final severity should depend on the intended endpoint scope.

---

## 5. MEDIUM-SEVERITY REVIEW

### C05-D18 — Refund/dispute handlers acknowledge incomplete business work

SOL ASSESSMENT:
ACCEPT — MEDIUM

The doctrine describes required behavior but the example does not perform or
durably delegate it.

If these handlers are intentionally placeholders, the documentation must make
their non-production status unmistakable.

The current presentation risks treating an incomplete example as production
doctrine.

---

### C05-D16 — Local validation does not require trust-boundary negative cases

SOL ASSESSMENT:
CONDITIONALLY ACCEPT — DEFER FULL CLASSIFICATION TO TESTING-DOMAIN REVIEW

The concern is legitimate.

Payment/API doctrine should not call itself production-safe if its local
acceptance path never exercises:

- forged paid-state calls,
- tampered totals,
- foreign order IDs,
- failed persistence,
- duplicate/reordered events,
- checkout concurrency,
- and resubscription.

However, the report explicitly did not inspect TESTING_PLAYBOOK.md.

Therefore it is not yet established whether the broader Factory testing doctrine
already supplies these requirements.

SOL POSITION:

Retain as a valid Chunk 05 concern.

Do not finalize this as a standalone Factory defect until the testing domain is
cross-checked.

Possible final outcomes:

- CONFIRMED DEFECT,
- DUPLICATE OF TESTING DEFECT,
- or DEPENDENCY already satisfied elsewhere.

---

### C05-D14 — Service errors collapse unavailable into successful absence/client error

SOL ASSESSMENT:
ACCEPT — MEDIUM

Unavailable data, confirmed empty data, unauthorized data, and not-found data
have different semantics.

Returning the same successful-looking empty/null representation destroys that
distinction.

The subscription example is particularly important because a failed entitlement
lookup should not masquerade as confirmed absence.

---

### C05-D15 — Success polling can confirm stale tier / unknown payment

SOL ASSESSMENT:
ACCEPT — MEDIUM

The success page predicate is not tied to the requested transition.

An existing paid user upgrading tiers can already satisfy "not free" before the
upgrade succeeds.

A timeout also cannot prove payment receipt.

Astra correctly keeps this finding bounded to false UI confirmation rather than
claiming it grants unauthorized entitlement.

---

### C05-D12 — API examples use incompatible service/type contracts

SOL ASSESSMENT:
ACCEPT — MEDIUM

The examples reuse the same named modules/functions/types while assigning them
different signatures and data shapes.

This is executable documentation drift.

The repair should not merely make TypeScript compile.

It should establish one canonical:

wire shape
→ normalization boundary
→ service result contract
→ route contract
→ UI contract.

---

### C05-D17 — Fixed-product coupon calculator lacks product/quantity context

SOL ASSESSMENT:
ACCEPT — MEDIUM

A per-product discount cannot be computed correctly from subtotal alone.

The displayed function therefore advertises behavior its inputs cannot support.

This is a correctness problem in the worked example even if the final server
quote is eventually authoritative.

---

## 6. REVIEW OF SUGGESTIONS

### C05-S01 — One mechanically checked canonical example path

SOL ASSESSMENT:
ACCEPT — HIGH-VALUE SUGGESTION

This may be one of the most important maintainability lessons from Chunks 04 and
05.

The Factory pairs doctrine with executable examples.

Those examples therefore need stronger ownership than ordinary prose.

A canonical integration fixture that is type-checked and regression-tested would
greatly reduce doctrine/code drift.

---

### C05-S02 — Integration ownership and recovery record

SOL ASSESSMENT:
ACCEPT

External systems introduce operational ownership that application code alone
cannot define.

Provider/account/environment, retry owner, reconciliation owner, alerts,
credential owner, and correlation identifiers should be explicit.

---

### C05-S03 — Consolidate duplicate quick references / declare assumptions

SOL ASSESSMENT:
ACCEPT

This is a maintainability improvement rather than a correctness defect.

One indexed source plus explicit assumptions reduces future divergence.

---

## 7. CROSS-CHUNK OBSERVATIONS

These are NOT final synthesis conclusions.

They are preservation notes for later comparison.

### A. Operation-local authorization is becoming a repeated seam

Chunk 04 identified privileged operations that relied on outer UI/layout
protection.

Chunk 05 identifies sync/payment operations with similar boundary problems.

Potential synthesis invariant:

EVERY PRIVILEGED OPERATION AUTHORIZES ITS OWN INVOCATION.

Do not finalize this here; carry it forward.

### B. Durable persistence and recovery recur across domains

Chunk 04 identified incomplete compensation/recovery behavior.

Chunk 05 identifies webhook acknowledgment, retry identity, event ordering, and
durable follow-up issues.

Potential synthesis theme:

SUCCESS MUST MEAN THE REQUIRED STATE TRANSITION WAS COMPLETED OR DURABLY
ACCEPTED FOR RECOVERY.

Again, this is a synthesis candidate only.

### C. New principles coexist with old executable recipes

This is now strongly visible in two independent technical domains.

Examples include:

- "never trust client totals" beside client-authoritative pricing inputs,
- raw-body webhook law beside reconstructed-JSON HMAC,
- server/API security rules beside unprotected mutation routes,
- one subscription truth model beside incompatible lifecycle writes.

This appears to be a documentation-maintenance problem, not merely isolated
technical mistakes.

Carry forward for final synthesis.

---

## 8. WHAT ASTRA DID PARTICULARLY WELL

Astra separated several commonly conflated concepts:

- authentication versus operation authorization,
- server execution versus trusted input,
- webhook authenticity versus successful processing,
- event deduplication versus event ordering,
- outbound request idempotency versus inbound webhook idempotency,
- local mirror state versus provider truth.

That separation materially improves the usefulness of the review.

Astra also repeatedly bounded its conclusions.

It did not claim:

- that a deployed Stark application is exploitable,
- that vendor runtime behavior was verified,
- that unexamined testing doctrine lacks all relevant controls,
- or that roadmap features are necessarily defects.

This is good adversarial-review discipline.

---

## 9. WHERE SOL WOULD TEMPER ASTRA

Astra's technical defect discovery is strong.

Three classifications need restraint before final disposition.

### C05-D05

HIGH is clearly justified.

BLOCKER may ultimately be appropriate if webhook processing is the only trusted
payment/entitlement transition and there is no durable reconciliation path.

### C05-D13

The defect is real.

HIGH is context-sensitive.

MEDIUM is a better general default unless the invalidation endpoint has broad or
expensive impact.

### C05-D16

The concern is legitimate, but the testing corpus was deliberately not examined
in this chunk.

Final classification should wait until the testing domain is checked.

This preserves the examiner/reviewer separation:

ASTRA FINDS AND ARGUES.

SOL CHALLENGES AND CALIBRATES.

TONY / FACTORY DISPOSITION DECIDES.

---

## 10. PRELIMINARY SOL DISPOSITION

C05-D03:
ACCEPT — BLOCKER

C05-D04:
ACCEPT — BLOCKER

C05-D05:
ACCEPT — HIGH minimum; BLOCKER candidate depending on architecture

C05-D06:
ACCEPT — HIGH

C05-D07:
ACCEPT — HIGH

C05-D10:
ACCEPT — HIGH

C05-D01:
ACCEPT — HIGH

C05-D08:
ACCEPT — HIGH

C05-D09:
ACCEPT — HIGH

C05-D02:
ACCEPT — HIGH when follow-up is required business work

C05-D11:
ACCEPT — HIGH

C05-D13:
ACCEPT DEFECT — provisional MEDIUM; context may justify HIGH

C05-D18:
ACCEPT — MEDIUM

C05-D16:
CONDITIONALLY ACCEPT — defer final classification to testing cross-check

C05-D14:
ACCEPT — MEDIUM

C05-D15:
ACCEPT — MEDIUM

C05-D12:
ACCEPT — MEDIUM

C05-D17:
ACCEPT — MEDIUM

C05-S01:
ACCEPT AS SUGGESTION

C05-S02:
ACCEPT AS SUGGESTION

C05-S03:
ACCEPT AS SUGGESTION

These are preliminary reviewer assessments.

They are not final Factory disposition.

---

## 11. DEEPER FACTORY LESSON

Chunk 05 reinforces the same maintenance hazard visible in Chunk 04:

CORRECT PRINCIPLE
+
INCOMPATIBLE EXECUTABLE EXAMPLE
=
UNSAFE FACTORY GUIDANCE

The Factory intentionally teaches through worked examples.

That makes executable examples part of the doctrine's security surface.

A prose rule cannot safely compensate for a copy/paste-ready implementation that
violates it.

Future DocSet synchronization should therefore treat executable examples as
first-class governed artifacts.

When a governing rule changes, synchronization should locate and evaluate:

- code snippets,
- helper signatures,
- quick-reference sections,
- summaries,
- checklists,
- paired examples,
- and downstream recipes

that embody the superseded behavior.

This is a synthesis candidate, not yet approved Factory doctrine.

---

## 12. SOL VERDICT ON CHUNK 05

ASTRA REVIEW QUALITY:

STRONG

EVIDENCE DISCIPLINE:

STRONG

TECHNICAL DEPTH:

STRONG

DOMAIN BOUNDARY DISCIPLINE:

STRONG

SEVERITY CALIBRATION:

GOOD WITH THREE MATERIAL ADJUDICATION NOTES

VALUE TO FACTORY:

HIGH

FINAL SOL POSITION:

Chunk 05 is a successful Chunky Monkey artifact.

The two principal BLOCKER findings are credible doctrine-level payment security
failures.

The majority of HIGH findings identify concrete integration lifecycle,
authorization, or durability problems rather than stylistic preferences.

The review also exposes a recurring Factory-maintenance pattern in which sound
new principles coexist beside unsafe older executable examples.

Preserve this report as independent Astra evidence.

Do not repair Factory doctrine until disposition and cross-chunk synthesis are
complete.