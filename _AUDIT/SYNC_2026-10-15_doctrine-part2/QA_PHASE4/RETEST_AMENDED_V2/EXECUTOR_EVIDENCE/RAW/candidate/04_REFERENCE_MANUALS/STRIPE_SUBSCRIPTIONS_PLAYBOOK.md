# STRIPE SUBSCRIPTIONS PLAYBOOK

> **Version:** 1.2 · **Date:** 2026-10-18 · **Status:** Active
> **Tier:** 4 — Reference Manuals · **Pairs with:** ECOMMERCE_AND_PAYMENTS_MANUAL, API_AND_SERVICES_MANUAL, TESTING_PLAYBOOK, AUTH_MANUAL

> **Author:** Architect (Claude) for Tony Stark
> **Origin:** Distilled from the StarkReads Subscription v1 build (Phase 1 + Phase 2)
> **Purpose:** Reusable recipe for adding Stripe subscription billing to any Next.js + Supabase application
> **Prerequisite:** A working Next.js App Router app with Supabase Auth already integrated
> **Territory:** RECURRING billing only. One-time payments / WooCommerce commerce → `ECOMMERCE_AND_PAYMENTS_MANUAL.md` (the territory pair — zero overlap by design).

---

## Table of Contents

1. [Architecture Overview](#1-architecture-overview)
2. [Stripe Setup Recipe](#2-stripe-setup-recipe)
3. [Supabase Schema Recipe](#3-supabase-schema-recipe)
4. [Environment Variables](#4-environment-variables)
5. [The Checkout Flow](#5-the-checkout-flow)
6. [The Webhook Handler](#6-the-webhook-handler)
7. [The Tier Upgrade Pattern](#7-the-tier-upgrade-pattern)
8. [The Service Layer Swap Pattern](#8-the-service-layer-swap-pattern)
9. [Success Page Polling Pattern](#9-success-page-polling-pattern)
10. [Stripe Customer Portal Integration](#10-stripe-customer-portal-integration)
11. [Common Gotchas & Lessons Learned](#11-common-gotchas--lessons-learned)
12. [Testing Strategy](#12-testing-strategy)
13. [Deployment Checklist](#13-deployment-checklist)
14. [Phase 3 Roadmap](#14-phase-3-roadmap)

---

## 1. Architecture Overview

### The Core Mental Model

Three sentences that govern everything:

**Stripe owns the truth about money.** Whether a subscription is active, what was charged, when the next renewal is — Stripe is always the authoritative source.

**Supabase owns the cache.** Your app reads subscription state from Supabase for speed and convenience. This is a local mirror, not a source of truth.

**Webhooks keep them in sync.** Stripe sends events to your webhook endpoint whenever subscription state changes. Your webhook handler writes those changes to Supabase. One-way street: Stripe speaks, Supabase listens.

### The Two Systems That Must Stay Separate

**RBAC (Role-Based Access Control)** answers: "Who are you structurally?" — superadmin, admin, member. This is about identity and permission within the app.

**Subscriptions** answer: "What have you paid for?" — free, starter, pro, enterprise. This is about commercial state.

These are orthogonal. They cross at right angles. Never implement subscription tiers as roles. A superadmin with no subscription still has full admin power. A member with an Enterprise subscription gets premium content but can't touch admin routes.

**Gate helpers compose, they never replace each other:**
- `requireUser()` — checks login only
- `requireRole(role)` — checks structural permission
- `requireSubscriptionTier(tier)` — checks commercial state

A page can require any combination of these.

### The Stripe Object Model

Five nouns you need:

**Product** — the abstract thing you sell. "Pro Plan." No price attached.

**Price** — a specific amount on a Product. "$15/month." A Product can have multiple Prices (monthly, annual, different currencies). Old subscribers stay on their original Price forever — you change prices without breaking existing subscriptions.

**Customer identity:** use the project-approved ownership and storage contract. Do not prescribe universal storage on a subscription row; universal subscription-schema design is deferred.

**Subscription** — the live recurring relationship between a Customer and a Price. Has a status: `active`, `past_due`, `canceled`, `incomplete`, `trialing`, `unpaid`.

**Checkout Session** — a temporary, single-use payment page hosted by Stripe. You redirect users there; they pay; Stripe redirects them back. You never see card numbers. No PCI burden.

### The Data Flow

```
User clicks "Subscribe to Pro"
    ↓
Your server creates a Stripe Checkout Session
    ↓
User redirected to checkout.stripe.com (enters card, pays)
    ↓
Stripe processes payment → TWO things happen simultaneously:
    A. Browser redirected to your success URL
    B. Webhook event fires to your server
    ↓
Webhook handler verifies signature → writes to Supabase
    ↓
App reads subscription from Supabase → gates content accordingly
```

**Critical:** The browser redirect (A) is cosmetic. The webhook (B) is the source of truth. Never trust the redirect alone to confirm payment.

---

## 2. Stripe Setup Recipe

### Step 1 — Create a Sandbox

Log into Stripe Dashboard. If you have multiple accounts, switch to the one with the appropriate business address. Click your account name → Switch to sandbox → Create sandbox. Name it after the project (e.g., "ProjectName Subscription v1").

**Why sandboxes over test mode:** Complete isolation. Separate products, prices, customers, webhook secrets, API keys. No cross-contamination between projects. One sandbox per project.

### Step 2 — Collect API Keys

Inside the sandbox, the dashboard shows your API keys (usually in a panel or under Developers → API Keys):
- **Publishable key** (`pk_test_...`) — safe for browser, goes in `NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY`
- **Secret key** (`sk_test_...`) — server-only, NEVER in browser, goes in `STRIPE_SECRET_KEY`

### Step 3 — Create Product + Prices

Go to Product Catalog → Create Product.
- **Product name:** "YourApp Subscription"
- **Description:** Brief description of the subscription offering
- Stripe's UI forces you to create the first Price during product creation — that's fine

For each tier, add a Price:
- **Pricing model:** Recurring
- **Amount:** The monthly price (e.g., $5, $15, $49)
- **Billing period:** Monthly
- **Currency:** USD (or your target currency)
- **Description:** Tier name (e.g., "Starter", "Pro", "Enterprise")

**Important:** One Product with multiple Prices, NOT multiple Products. This keeps Stripe's data model clean and allows tier upgrades via `subscriptions.update()` without creating new subscriptions.

After creation, click into each Price to get its Price ID (`price_...`). Store these in env vars.

### Step 4 — Install Stripe CLI

```bash
# Ubuntu/Debian
curl -s https://packages.stripe.dev/api/security/keypair/stripe-cli-gpg/public | gpg --dearmor | sudo tee /usr/share/keyrings/stripe.gpg > /dev/null
echo "deb [signed-by=/usr/share/keyrings/stripe.gpg] https://packages.stripe.dev/stripe-cli-debian-local stable main" | sudo tee /etc/apt/sources.list.d/stripe.list
sudo apt update && sudo apt install stripe -y

# macOS
brew install stripe/stripe-cli/stripe

# Verify
stripe version
```

### Step 5 — Log In and Start Listener

```bash
stripe login
# Opens browser for OAuth — authorize, confirm pairing code

stripe listen --forward-to localhost:3000/api/webhooks/stripe
# Prints: Ready! Your webhook signing secret is whsec_...
```

Copy the `whsec_...` value into `STRIPE_WEBHOOK_SECRET` in `.env.local`.

**Key facts about the listener:**
- Keep it running in a dedicated terminal tab — close it and webhooks stop arriving
- The `whsec_` secret changes every time you restart the listener — update `.env.local` and restart your dev server
- This is dev-only tooling — production uses a permanent webhook endpoint URL registered in Stripe Dashboard

### Step 6 — Activate Customer Portal

Stripe Dashboard → Settings → Billing → Customer Portal → Toggle on.

Configure which actions customers can take:
- ✅ Cancel subscription
- ✅ Update payment method
- ✅ View invoices

This gives you a free, hosted subscription management page. Your app just redirects to it — zero UI to build.

---

## 3. Supabase Schema Recipe

**Executable example withdrawn.** The previous example is not an approved implementation. The outgoing archived document preserves it as history. Replacement code requires the project’s approved contract, verified dependency interfaces and behavioral evidence. This withdrawal contains the misleading recipe; it does not certify the underlying finding resolved.

Subscription bootstrap, customer identity and resubscription must agree with the project’s approved schema. Universal subscription-schema design is deferred; no runnable replacement is supplied here. Preserve owner-only reads and server-only subscription writes. Keep this finding open until the project contract and recovery behavior are verified.

---

## 4. Environment Variables

### Complete List

```env
# Stripe (from Stripe Dashboard → API Keys)
NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=pk_test_...    # Safe for browser
STRIPE_SECRET_KEY=sk_test_...                      # Server-only, NEVER in browser
STRIPE_WEBHOOK_SECRET=whsec_...                    # Server-only, from Stripe CLI

# Stripe Price IDs (from Product Catalog → each Price)
STRIPE_PRICE_STARTER=price_...
STRIPE_PRICE_PRO=price_...
STRIPE_PRICE_ENTERPRISE=price_...

# Supabase (from Supabase Dashboard → Settings → API)
NEXT_PUBLIC_SUPABASE_URL=https://xxx.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJ...               # Safe for browser, RLS enforced
SUPABASE_SERVICE_ROLE_KEY=eyJ...                    # Server-only, bypasses RLS
```

### Naming Convention

**In your app:** Generic names. No project suffix. Code reads `process.env.STRIPE_SECRET_KEY` everywhere.

**In GCP Secret Manager:** Project-prefixed names.
```
starkreads-stripe-secret-key → sk_test_...
mothership-stripe-secret-key → sk_live_...
```

**In Cloud Run:** Map GCP secrets to generic env vars at deploy time.
```bash
gcloud run deploy starkreads \
  --set-secrets=STRIPE_SECRET_KEY=starkreads-stripe-secret-key:latest
```

Same env var name in code, different secret in GCP per project. Clone the repo, point at different secrets, deploy. No code changes.

### Security Rules

- `NEXT_PUBLIC_` prefix = browser-safe. Only the Stripe publishable key and Supabase URL/anon key get this prefix.
- Everything else = server-only. Never imported in `"use client"` components.
- `.env.local` is gitignored. Never committed.
- Rotate keys immediately if accidentally exposed (Stripe Dashboard → Roll key).

---

## 5. The Checkout Flow

**Executable example withdrawn.** The previous example is not an approved implementation. The outgoing archived document preserves it as history. Replacement code requires the project’s approved contract, verified dependency interfaces and behavioral evidence. This withdrawal contains the misleading recipe; it does not certify the underlying finding resolved.

Persist one authorized checkout-attempt identity across retries and claim it atomically against concurrent requests. Scope provider idempotency keys to that attempt and operation, reuse or retrieve existing external objects after an unknown outcome, and reconcile before creating a replacement. Use the project-approved customer-identity contract without assuming paid activation; universal subscription schema design is deferred. Handle every documented subscription state, not only active.

Subscription bootstrap, customer identity and resubscription must agree with the project’s approved schema. Universal subscription-schema design is deferred; no runnable replacement is supplied here. Preserve owner-only reads and server-only subscription writes. Keep this finding open until the project contract and recovery behavior are verified.

---

## 6. The Webhook Handler

**Executable example withdrawn.** The previous example is not an approved implementation. The outgoing archived document preserves it as history. Replacement code requires the project’s approved contract, verified dependency interfaces and behavioral evidence. This withdrawal contains the misleading recipe; it does not certify the underlying finding resolved.

For supported events, check business persistence or durable enqueue before acknowledging. Pre-acceptance failure returns a retryable failure. After durable acceptance, worker failures enter bounded durable retries and visible failed-work reconciliation with an alert and recovery owner. Unsupported events are explicitly distinguished from failed supported events. Missing order/user mappings create actionable recovery records, not silent success.

Converge each order or subscription aggregate using authoritative provider retrieval or explicit freshness and legal-transition rules. Reject stale transitions; check zero-row updates and repair missing mappings. A late event for an old subscription may not overwrite its replacement. Define reconciliation of the local mirror independently of inbound deduplication.

Subscription bootstrap, customer identity and resubscription must agree with the project’s approved schema. Universal subscription-schema design is deferred; no runnable replacement is supplied here. Preserve owner-only reads and server-only subscription writes. Keep this finding open until the project contract and recovery behavior are verified.

Distinguish optional telemetry from required follow-up. Complete required work retry-safely or durably enqueue it before acknowledgment. Failed or unconfirmed enqueue returns retryable failure. A later worker failure uses bounded durable retry, visible failed-work state and a named recovery owner. Inspect non-success HTTP responses from follow-up targets; a resolved fetch is not proof of success.

---

## 7. The Tier Upgrade Pattern

**Executable example withdrawn.** The previous example is not an approved implementation. The outgoing archived document preserves it as history. Replacement code requires the project’s approved contract, verified dependency interfaces and behavioral evidence. This withdrawal contains the misleading recipe; it does not certify the underlying finding resolved.

Persist one authorized checkout-attempt identity across retries and claim it atomically against concurrent requests. Scope provider idempotency keys to that attempt and operation, reuse or retrieve existing external objects after an unknown outcome, and reconcile before creating a replacement. Use the project-approved customer-identity contract without assuming paid activation; universal subscription schema design is deferred. Handle every documented subscription state, not only active.

Poll the server-authorized payment attempt and expected target tier with its qualifying subscription status. A pre-existing paid tier is not evidence of this upgrade. A timeout shows pending or unknown and its recovery/support path; it never claims payment receipt. Redirects remain cosmetic.

---

## 8. The Service Layer Swap Pattern

### The Principle

Build your UI against a service layer with clean method signatures. Mock the internals in Phase 1. Swap to real backend in Phase 2. UI code never changes.

### How It Worked In Practice

**Phase 1 (mock):**
```typescript
getCurrentSubscription: async () => {
  const tier = readMockTierFromCookie();
  return buildSubscriptionFromTier(tier);  // fake data
}
```

**Phase 2 (real):**
```typescript
getCurrentSubscription: async () => {
  const { data } = await supabase.from('subscriptions').select('*').eq('user_id', userId).single();
  if (!data) return { tier: 'free', status: 'none', renewal_date: null, started_at: null };
  return mapRowToSubscription(data);  // real data
}
```

**Components in both phases:**
```typescript
const subscription = await subscriptionService.getCurrentSubscription();
// Doesn't know or care if data is mock or real
```

### The Turbopack Server/Client Split

Next.js App Router + Turbopack traces ALL imports in a module, even dynamic ones. If a service file imports anything server-only (like `next/headers` or the Supabase admin client), it can't be imported by a client component — even if the client component only calls a method that doesn't use the server import.

**The fix:** Split the service into two files:
- `subscriptionService.ts` — server-only, handles `getCurrentSubscription()` (queries Supabase)
- `checkoutService.ts` — client-safe, handles `subscribe()` (POSTs to `/api/checkout`)

Components import from the appropriate file. The API boundary (`/api/checkout`) is the bridge between client and server.

### What Moves, What Stays

| File | Phase 1 | Phase 2 | Signature Changed? |
|------|---------|---------|-------------------|
| `subscriptionService.getCurrentSubscription()` | Cookie/store → mock object | Supabase query → real object | ❌ No |
| `checkoutService.subscribe(tier)` | Flip cookie → return `/subscribe/success` | POST to `/api/checkout` → return Stripe URL or success URL | ❌ No |
| `userService.getCurrentUser()` | Mock user + mock subscription | Real auth + real role + real subscription join | ❌ No |
| `requireSubscriptionTier()` | Calls userService (which read cookie) | Calls userService (which queries Supabase) | ❌ No |
| All components | Use service methods | Use same service methods | ❌ No |

**Zero UI files changed during the backend swap.** That's the payoff.

---

## 9. Success Page Polling Pattern

### The Problem

After paying on Stripe Checkout, the user's browser is redirected to your success page. But the webhook that writes the subscription to Supabase fires independently — it might arrive before, after, or at the same time as the redirect.

If the success page reads the subscription immediately and the webhook hasn't arrived yet, it shows "free" instead of "pro." Bad UX.

### The Solution

Poll for subscription status with three visual states:

**State 1 — Polling (spinner):**
"Activating your subscription..." with a spinning icon. Check every 2 seconds.

**State 2 — Confirmed (green check):**
"Your subscription change is confirmed." with a Continue button. Show only after the server-authorized payment attempt resolves to its expected target tier and qualifying subscription status; an existing non-free tier is insufficient.

**State 3 — Timeout (amber info):**
"Your subscription change is still pending or could not be confirmed." with Refresh and the approved support/recovery path. Show after 5 failed polls (10 seconds); timeout does not establish payment receipt.

### Implementation Notes

- The success page must be a Client Component (`"use client"`) for the polling `useEffect`
- Use `useState` for `currentTier`, `isPolling`, `pollCount`
- The `?next=` parameter handling stays — "Continue" button still respects intent-aware redirects
- Max 5 polls at 2-second intervals = 10 seconds total wait
- In practice, the webhook usually arrives within 1-3 seconds

---

## 10. Stripe Customer Portal Integration

### The 20-Line Shortcut

Instead of building a custom subscription management UI (cancel, update payment, view invoices), use Stripe's hosted Customer Portal. It's free, maintained by Stripe, PCI-compliant, and handles edge cases you don't want to build.

### The API Route

**Dependent executable example withdrawn.** Use a project-approved state/payment contract with explicit hydration errors, server-authoritative pricing, authenticated ownership and recovery. The removed example’s missing contract is still tracked; no universal quote/subscription schema is introduced.

### The Frontend

```typescript
// Account page "Manage Subscription" button:
const handleManageSubscription = async () => {
  const response = await fetch('/api/customer-portal', { method: 'POST' });
  const data = await response.json();
  window.location.href = data.redirect_url;
};
```

### What The Portal Gives You For Free

- Cancel subscription (with confirmation)
- Update payment method (new card)
- View invoice history
- Resume canceled subscription (if within period)

All hosted by Stripe. All PCI-compliant. Zero UI for you to build or maintain.

---

## 11. Common Gotchas & Lessons Learned

### Gotcha 1: The Double-Subscription Bug

**What happens:** User subscribes to Starter, then clicks Subscribe on Pro. Two active subscriptions, double charge.
**Root cause:** Checkout route always creates a new subscription instead of checking for an existing one.
**Fix:** Check for active `stripe_subscription_id` before creating a new Checkout Session. If exists, use `stripe.subscriptions.update()`. See Section 7.
**Lesson:** Always check for existing state before creating new state.

### Gotcha 2: Webhook Secret Rotation

**What happens:** You restart `stripe listen` and the webhook secret changes. Your app still has the old secret in `.env.local`. Webhooks arrive but signature verification fails silently (returns 400).
**Symptom:** User pays successfully but subscription never appears in Supabase. Success page shows "Activating..." forever.
**Fix:** After restarting `stripe listen`, copy the new `whsec_...` value into `.env.local` and restart `npm run dev`.
**Lesson:** When debugging "webhook isn't working," check the secret first.

### Gotcha 3: `request.text()` Not `request.json()`

**What happens:** You parse the webhook body as JSON before verifying the signature. The signature check fails because it needs the raw bytes.
**Symptom:** Every webhook returns 400 "signature verification failed."
**Fix:** Use `request.text()` for the body, pass raw string to `constructEvent()`.
**Lesson:** Stripe signature verification is byte-sensitive. Parse AFTER verification.

### Gotcha 4: Stripe SDK v22 Period Dates

**What happens:** You read `subscription.current_period_start` and get `undefined`.
**Root cause:** Stripe SDK v22 moved period dates to `subscription.items.data[0]`.
**Fix:** Read from `subscription.items.data[0].current_period_start` and `.current_period_end`.
**Lesson:** Check the SDK version's changelog when upgrading.

### Gotcha 5: Turbopack Server/Client Import Tracing

**What happens:** You import a service that uses `next/headers` into a file that's in a client component's dependency chain. Turbopack throws a build error.
**Root cause:** Turbopack traces ALL imports, even dynamic ones. If any import path reaches a server-only module, the whole chain is flagged.
**Fix:** Split services into server-only and client-safe files. Use API routes as the bridge.
**Lesson:** In Next.js App Router, the server/client boundary is enforced at the import level, not the runtime level.

### Gotcha 6: The `?next=` Open Redirect

**What happens:** Without validation, `?next=https://evil.com` becomes an open redirect through your trusted domain.
**Fix:** Validate all `next` values: must start with `/`, no `//`, no `:`, no `\`.
**Lesson:** Every user-controlled redirect target needs validation. Build a `safeRedirect()` helper and use it everywhere.

### Gotcha 7: Free Tier Supabase Pauses

**What happens:** Your Supabase free-tier project pauses after 7 days of inactivity. Webhooks hit a paused database and silently fail.
**Symptom:** Users pay but subscriptions never activate.
**Fix:** Use a paid Supabase plan ($25/mo Pro, $10/mo per additional project) for anything with webhooks.
**Lesson:** Webhook-driven systems need always-on infrastructure.

---

## 12. Testing Strategy

The Architect includes the API trust-boundary matrix in the acceptance contract; the Engineer supplies engineering results, the QA Executor derives independent checks, and the QA Lead approves and grades them. Cover unauthenticated/wrong-role/wrong-owner calls, forged payment status, tampered totals, duplicate and concurrent requests, invalid signatures, pre-acceptance persistence failure, post-acceptance worker failure, and stale/out-of-order events. Each case records status, absence of unauthorized effects, persisted final state and retry/recovery evidence. TESTING_PLAYBOOK owns the matrix; commerce, subscription and API manuals refer to it.

### Pure Function Unit Tests (High Value, Low Effort)

These functions are pure (no side effects, no async, no mocking needed) and critical:

**`meetsTier(current, required)`** — Test all 16 combinations (4 tiers × 4 tiers). Verify cumulative hierarchy: Enterprise ≥ Pro ≥ Starter ≥ Free.

**`safeRedirect(next)`** — Test valid paths, paths with query strings, null, undefined, empty string, protocol-relative URLs (`//evil.com`), schemed URLs (`https://evil.com`), backslash paths, non-slash starts.

**`tierDisplayName(tier)`** — Test all 4 tiers produce correct capitalized names.

**`resolveTierFromPriceId(priceId)`** — Test valid Price IDs return correct tiers, unknown ID returns null. Requires setting env vars before import.

**`resolvePriceIdFromTier(tier)`** — Test valid tiers return correct Price IDs, 'free' returns null.

### Manual Smoke Test Checklist

Run after every backend change:

```
□ Register new user → default tier is "free"
□ Subscribe to Starter → Stripe Checkout → test card → success page → tier updates
□ Verify Supabase row: tier=starter, status=active, subscription ID present
□ Verify Stripe: ONE subscription, ONE customer
□ Upgrade to Pro (from pricing page) → no new Checkout page → instant upgrade
□ Verify Supabase: same row, tier=pro, same subscription ID
□ Verify Stripe: ONE subscription (updated), not two
□ Check gating: Pro + Starter content accessible, Enterprise locked
□ Check article paywall: Pro articles unlocked, Enterprise articles show paywall
□ Check navbar badge: shows "Pro"
□ Close browser → reopen → log in → tier persists (reads from Supabase)
□ Account page → "Manage Subscription" → Stripe Customer Portal opens
□ Stripe CLI terminal → webhook events visible for all operations
```

### Future: E2E Testing with Playwright

Automate the manual checklist. Playwright handles multi-page flows including redirects to Stripe Checkout. Set up as a separate mini-lab:

```bash
npm install -D @playwright/test
npx playwright install
```

Each user flow from the APP_BRIEF becomes a Playwright test. ~20-40 lines per flow. Runs in ~2-3 minutes. Catches regressions automatically.

---

## 13. Deployment Checklist

### GCP Cloud Run Deployment

**Step 1 — Create Secrets in GCP Secret Manager:**
```bash
gcloud secrets create projectname-stripe-secret-key --data-file=-
gcloud secrets create projectname-stripe-webhook-secret --data-file=-
gcloud secrets create projectname-stripe-price-starter --data-file=-
gcloud secrets create projectname-stripe-price-pro --data-file=-
gcloud secrets create projectname-stripe-price-enterprise --data-file=-
gcloud secrets create projectname-supabase-service-role-key --data-file=-
```

**Step 2 — Deploy Cloud Run with Secret Mappings:**
```bash
gcloud run deploy projectname \
  --set-secrets=STRIPE_SECRET_KEY=projectname-stripe-secret-key:latest \
  --set-secrets=STRIPE_WEBHOOK_SECRET=projectname-stripe-webhook-secret:latest \
  --set-secrets=STRIPE_PRICE_STARTER=projectname-stripe-price-starter:latest \
  --set-secrets=STRIPE_PRICE_PRO=projectname-stripe-price-pro:latest \
  --set-secrets=STRIPE_PRICE_ENTERPRISE=projectname-stripe-price-enterprise:latest \
  --set-secrets=SUPABASE_SERVICE_ROLE_KEY=projectname-supabase-service-role-key:latest \
  --set-env-vars=NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=pk_test_... \
  --set-env-vars=NEXT_PUBLIC_SUPABASE_URL=https://xxx.supabase.co \
  --set-env-vars=NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJ...
```

Note: `NEXT_PUBLIC_*` vars can be plain env vars (they're browser-safe). Secret vars use `--set-secrets`.

**Step 3 — Register Webhook Endpoint in Stripe Dashboard:**

After deployment, your Cloud Run service has a URL like `https://projectname-abc123.run.app`.

Go to Stripe Dashboard → Developers → Webhooks → Add endpoint:
- **URL:** `https://projectname-abc123.run.app/api/webhooks/stripe`
- **Events:** Select `checkout.session.completed`, `customer.subscription.updated`, `customer.subscription.deleted`

Copy the new webhook signing secret and update the GCP secret.

**Step 4 — Verify:**
```
□ Visit the Cloud Run URL — app loads
□ Register a user — auth works
□ Subscribe — Stripe Checkout works
□ Webhook fires — subscription appears in Supabase
□ Content gating works
```

### DevOps Handoff Note

Schema design and migration SQL are the developer's responsibility. Running migrations against production and managing database access/backups is DevOps. Hand them:
- The migration SQL (Section 3 of this playbook)
- The RLS policy explanation (webhook handler writes via service role, users read only)
- The env var list (Section 4)
- The secret naming convention (project-prefixed in Secret Manager, generic in app)

---

## 14. Phase 3 Roadmap

Items explicitly deferred from the StarkReads build. Each is a self-contained enhancement:

### Payment Failure Handling (Dunning)

Handle `invoice.payment_failed` webhook event. Update subscription status to `past_due`. Show a banner: "Your payment failed. Please update your payment method." Link to Customer Portal. After N failures, Stripe automatically cancels — handle `customer.subscription.deleted`.

### Trial Periods

Add `trialing` status support. Create Checkout Sessions with `subscription_data.trial_period_days`. Handle `customer.subscription.trial_will_end` webhook (3 days before trial ends). Show trial countdown in UI.

### Annual Billing

Add yearly Prices to existing Product ($50/year for Starter, $150/year for Pro, $490/year for Enterprise). Update pricing page to show monthly/annual toggle. The checkout and webhook flows are identical — only the Price ID changes.

### Multi-Tenant Subscriptions (Mothership)

Subscription attaches to an organization, not a user. Add `organization_id` to subscriptions table. Gate helper checks "does the user's org have an active subscription?" instead of "does the user have an active subscription?" Same webhook handler, same Stripe flows — different foreign key.

### Reconciliation Job

Periodic background job that fetches subscription state from Stripe API and compares to Supabase mirror. Flags and repairs any drift (missed webhooks, manual changes in Stripe Dashboard). Run daily or weekly. Catches the edge cases webhooks miss.

### Custom Transactional Emails

Replace Stripe's built-in emails with branded transactional emails (welcome, renewal confirmation, payment failure, cancellation confirmation). Use Resend, SendGrid, or Supabase Edge Functions.

---

## Appendix: Quick Reference Card

**Test card:** `4242 4242 4242 4242` (any future expiry, any CVC)

**Stripe CLI listener:** `stripe listen --forward-to localhost:3000/api/webhooks/stripe`

**Tier hierarchy:** Enterprise (3) > Pro (2) > Starter (1) > Free (0)

**Cumulative access check:** `TIER_LEVELS[current] >= TIER_LEVELS[required]`

**Key files:**
- Checkout route: `src/app/api/checkout/route.ts`
- Webhook handler: `src/app/api/webhooks/stripe/route.ts`
- Customer portal: `src/app/api/customer-portal/route.ts`
- Stripe init: `src/lib/stripe/stripe.ts`
- Tier resolver: `src/lib/stripe/tierResolver.ts`
- Admin client: `src/lib/supabase/admin.ts`
- Gate helper: `src/lib/auth/requireSubscriptionTier.ts`
- Tier logic: `src/lib/tiers.ts`
- Safe redirect: `src/lib/safeRedirect.ts`

---

## Cross-References (Factory Doctrine)

- **`ECOMMERCE_AND_PAYMENTS_MANUAL.md`** — the territory pair: one-time payments, WooCommerce commerce, carts/checkout.
- **`API_AND_SERVICES_MANUAL.md`** — the service-layer law behind §8's swap pattern (incl. the Kit Exception).
- **`TESTING_PLAYBOOK.md`** — §12's testing strategy in full: the StarkReads provenance sibling (Stripe boundary-stop, webhook tests, four layers).
- **`AUTH_MANUAL.md`** — the auth/role side of the gate helpers (`requireUser`/`requireRole` compose with `requireSubscriptionTier`; roles ⊥ tiers — never implement tiers as roles).

---

## Version History

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-04-28 | Initial playbook, distilled from StarkReads Subscription v1: object model, setup + schema recipes, checkout flow, webhook handler, tier upgrades, service-layer swap, success polling, customer portal, gotchas, testing, deployment, roadmap. |
| 1.1 | 2026-07-08 | **Wave 4 micro (audit sync).** Territory declaration added (recurring only; one-time/WooCommerce → ECOMMERCE_AND_PAYMENTS_MANUAL — completes the pair's two-way declaration). Cross-References section added — island ended: §8 ↔ API_AND_SERVICES, §12 ↔ TESTING_PLAYBOOK (provenance siblings introduced at last), gate helpers ↔ AUTH_MANUAL (F-035). Standard header (F-018); this history table (D-018). Content untouched — the D-016 money-truth model + RBAC ⊥ subscriptions doctrine is promoted gold. |
| 1.2 | 2026-10-18 | Factory DocSet sync: approved workflow/security/reference corrections; preserved original; explicit exclusions per doctrine-part2 map. IDs: FC-047, FC-052, FC-053, FC-054, FC-055, FC-059, FC-063, FC-065, FC-065-confirmed, FC-065-timeout, FC-067, FC-068, RUL-11 |

---

**END OF STRIPE SUBSCRIPTIONS PLAYBOOK**
