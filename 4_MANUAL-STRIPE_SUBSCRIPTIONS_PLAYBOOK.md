# STRIPE SUBSCRIPTIONS PLAYBOOK

> **Version:** 1.0
> **Date:** 2026-04-28
> **Author:** Architect (Claude) for Tony Stark
> **Origin:** Distilled from the StarkReads Subscription v1 build (Phase 1 + Phase 2)
> **Purpose:** Reusable recipe for adding Stripe subscription billing to any Next.js + Supabase application
> **Prerequisite:** A working Next.js App Router app with Supabase Auth already integrated

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

**Customer** — a person in Stripe's system. One Stripe Customer per user in your app. Store the `stripe_customer_id` on your user/subscription record. This is the bridge between your world and Stripe's.

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

### The Subscriptions Table

```sql
CREATE TABLE public.subscriptions (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  stripe_customer_id TEXT,
  stripe_subscription_id TEXT,
  tier TEXT NOT NULL CHECK (tier IN ('starter', 'pro', 'enterprise')),
  status TEXT NOT NULL DEFAULT 'active' CHECK (status IN ('active', 'canceled', 'past_due', 'incomplete', 'trialing', 'unpaid')),
  current_period_start TIMESTAMPTZ,
  current_period_end TIMESTAMPTZ,
  cancel_at_period_end BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- One subscription per user
ALTER TABLE public.subscriptions
  ADD CONSTRAINT subscriptions_user_id_unique UNIQUE (user_id);

-- Prevent duplicate webhook processing
ALTER TABLE public.subscriptions
  ADD CONSTRAINT subscriptions_stripe_subscription_id_unique UNIQUE (stripe_subscription_id);

-- Fast lookups
CREATE INDEX idx_subscriptions_user_id ON public.subscriptions(user_id);
CREATE INDEX idx_subscriptions_stripe_sub_id ON public.subscriptions(stripe_subscription_id);
```

### RLS Policies

```sql
ALTER TABLE public.subscriptions ENABLE ROW LEVEL SECURITY;

-- Users can read their own subscription
CREATE POLICY "Users can read own subscription"
  ON public.subscriptions FOR SELECT
  USING (auth.uid() = user_id);

-- Block all direct writes (webhook handler uses service role to bypass)
CREATE POLICY "No direct user inserts"
  ON public.subscriptions FOR INSERT WITH CHECK (FALSE);

CREATE POLICY "No direct user updates"
  ON public.subscriptions FOR UPDATE USING (FALSE);

CREATE POLICY "No direct user deletes"
  ON public.subscriptions FOR DELETE USING (FALSE);
```

### Auto-Update Trigger

```sql
CREATE OR REPLACE FUNCTION public.update_updated_at()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER subscriptions_updated_at
  BEFORE UPDATE ON public.subscriptions
  FOR EACH ROW EXECUTE FUNCTION public.update_updated_at();
```

### Column Reference

| Column | Purpose | Who Writes It |
|--------|---------|---------------|
| `id` | Primary key | Auto-generated |
| `user_id` | Links to Supabase auth user | Checkout route (on first subscribe) |
| `stripe_customer_id` | Bridge to Stripe Customer object | Checkout route (on first subscribe) |
| `stripe_subscription_id` | Bridge to Stripe Subscription | Webhook handler |
| `tier` | Current subscription tier string | Webhook handler |
| `status` | Stripe subscription status | Webhook handler |
| `current_period_start` | Billing period start | Webhook handler |
| `current_period_end` | Billing period end (check this + status for access) | Webhook handler |
| `cancel_at_period_end` | User canceled but still has access until period ends | Webhook handler |
| `created_at` | Row creation timestamp | Auto |
| `updated_at` | Last modification timestamp | Auto (trigger) |

### The "No Subscription" Convention

Users who never subscribed have NO row in this table. The service layer treats absence as `tier: 'free'`:

```typescript
const { data } = await supabase.from('subscriptions').select('*').eq('user_id', userId).single();
if (!data) return { tier: 'free', status: 'none', renewal_date: null, started_at: null };
```

Components never deal with null — the service layer always returns a valid `Subscription` object.

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

### Architecture

```
PlanCard (client) → checkoutService.subscribe(tier)
    ↓ POST /api/checkout { tier, next? }
Checkout Route (server):
    1. Authenticate user from Supabase session
    2. Validate tier against known values
    3. Look up existing subscription row
    4. If active subscription exists → UPGRADE path (Section 7)
    5. If no subscription → NEW SUBSCRIBER path:
       a. Create Stripe Customer (if needed)
       b. Save stripe_customer_id to Supabase
       c. Create Checkout Session (mode: 'subscription')
       d. Return { redirect_url: session.url }
    ↓
PlanCard: window.location.href = redirect_url
    ↓
User on Stripe Checkout → pays → redirected to success URL
```

### Why `window.location.href` Not `router.push()`

Stripe Checkout lives on `checkout.stripe.com` — an external domain. Next.js `router.push()` only handles internal routes. For external URLs, use `window.location.href` for a full browser redirect. This also works for internal URLs (upgrade path returns `/subscribe/success`), so one code path handles both cases.

### The Checkout Session Configuration

```typescript
const session = await stripe.checkout.sessions.create({
  mode: 'subscription',
  customer: stripeCustomerId,
  line_items: [{ price: priceId, quantity: 1 }],
  success_url: `${origin}/subscribe/success${next ? `?next=${encodeURIComponent(next)}` : ''}`,
  cancel_url: `${origin}/pricing${next ? `?next=${encodeURIComponent(next)}` : ''}`,
  metadata: { supabase_user_id: user.id, tier },
});
```

**Key details:**
- `mode: 'subscription'` — not `'payment'` (that's for one-time charges like DockBloxx)
- `metadata` — carries your user ID and tier through the Stripe flow so the webhook can link back to your database
- `success_url` / `cancel_url` — preserve the `?next=` parameter so intent-aware redirects survive the Stripe round-trip
- `customer` — always pass the Stripe Customer ID; never let Stripe auto-create customers (you lose the link to your user)

### Stripe Customer Creation Strategy

One Stripe Customer per user, ever. Created on first subscribe:

```typescript
const customer = await stripe.customers.create({
  email: user.email,
  metadata: { supabase_user_id: user.id },
});
```

Store `stripe_customer_id` on the subscriptions row. On subsequent subscribes/upgrades, look it up instead of creating a new one. Never create duplicate customers — it causes billing confusion.

### Price ID Validation

Never trust the client to send a valid tier. Always validate server-side:

```typescript
const priceId = resolvePriceIdFromTier(tier);
if (!priceId) return NextResponse.json({ error: 'Invalid tier' }, { status: 400 });
```

The `resolvePriceIdFromTier()` helper reads from env vars — never hardcode Price IDs.

---

## 6. The Webhook Handler

### The Most Important File In The System

The webhook handler is where money becomes access. Get it wrong and either (a) people pay but don't get access, or (b) people get access without paying. Both are catastrophic.

### Signature Verification (Non-Negotiable)

```typescript
export async function POST(request: Request) {
  const body = await request.text();  // RAW body, NOT request.json()
  const signature = request.headers.get('stripe-signature')!;

  let event: Stripe.Event;
  try {
    event = stripe.webhooks.constructEvent(
      body,
      signature,
      process.env.STRIPE_WEBHOOK_SECRET!
    );
  } catch (err) {
    console.error('Webhook signature verification failed:', err);
    return new Response('Webhook signature verification failed', { status: 400 });
  }

  // Process event...
  return new Response('OK', { status: 200 });
}
```

**Critical details:**
- Read the body as `request.text()`, NOT `request.json()`. Signature verification needs the raw bytes. If you parse to JSON first, the signature won't match.
- Always return 200, even for unknown event types. Stripe retries on non-2xx responses for up to 3 days. Returning 400 for an event type you don't handle will cause endless retries.
- The `STRIPE_WEBHOOK_SECRET` changes every time you restart the Stripe CLI listener in development. Update `.env.local` and restart your dev server.

### Event Types (Happy Path)

Handle these three. Log and ignore everything else.

**`checkout.session.completed`** — User just paid for the first time.
```
1. Extract session.subscription (Stripe Subscription ID)
2. Retrieve full subscription: stripe.subscriptions.retrieve(subId)
3. Extract price ID from subscription.items.data[0].price.id
4. Resolve tier via resolveTierFromPriceId()
5. Extract customer ID and user ID from session metadata
6. UPSERT into subscriptions table
```

**`customer.subscription.updated`** — Subscription changed (upgrade, downgrade, renewal, pending cancellation).
```
1. Extract subscription object from event.data.object
2. Extract price ID → resolve tier
3. UPDATE subscriptions row WHERE stripe_subscription_id matches
4. Update: tier, status, period dates, cancel_at_period_end
```

**`customer.subscription.deleted`** — Subscription fully canceled (period ended).
```
1. Extract subscription object
2. UPDATE subscriptions row WHERE stripe_subscription_id matches
3. Set status to 'canceled'
```

### Idempotency via UPSERT

Webhooks can arrive multiple times (Stripe retries). Use Supabase UPSERT with conflict handling:

```typescript
await supabaseAdmin
  .from('subscriptions')
  .upsert({
    user_id: userId,
    stripe_customer_id: customerId,
    stripe_subscription_id: subscriptionId,
    tier,
    status,
    current_period_start,
    current_period_end,
    cancel_at_period_end,
  }, {
    onConflict: 'stripe_subscription_id',
  });
```

Same event twice = same final state. Idempotent by design.

### Stripe SDK v22 Gotcha

In Stripe SDK v22+, `current_period_start` and `current_period_end` moved from the Subscription object to the SubscriptionItem. Read them from:

```typescript
subscription.items.data[0].current_period_start
subscription.items.data[0].current_period_end
```

Not from `subscription.current_period_start` (which may be undefined or deprecated).

### The Admin Client

The webhook handler writes to Supabase using the **service role key**, which bypasses RLS. This is intentional — RLS blocks all user-level writes to the subscriptions table. The webhook is the only trusted writer.

```typescript
import { createClient } from '@supabase/supabase-js';

export const supabaseAdmin = createClient(
  process.env.NEXT_PUBLIC_SUPABASE_URL!,
  process.env.SUPABASE_SERVICE_ROLE_KEY!,
  { auth: { autoRefreshToken: false, persistSession: false } }
);
```

**Never import this client in client-side code.**

---

## 7. The Tier Upgrade Pattern

### The Bug That Caught Us

When a subscribed user clicked "Subscribe" on a different tier, the checkout route created a brand new Stripe Subscription. The user ended up with TWO active subscriptions and was double-charged. This is the #1 most common Stripe subscription bug in the wild.

### The Fix

Before creating a new Checkout Session, check if the user already has an active subscription:

```typescript
// In /api/checkout route handler:
if (existingSubscription?.stripe_subscription_id && existingSubscription?.status === 'active') {
  // UPGRADE PATH — modify existing subscription
  const stripeSubscription = await stripe.subscriptions.retrieve(existingSubscription.stripe_subscription_id);
  const existingItemId = stripeSubscription.items.data[0].id;
  const newPriceId = resolvePriceIdFromTier(tier);

  await stripe.subscriptions.update(existingSubscription.stripe_subscription_id, {
    items: [{ id: existingItemId, price: newPriceId }],
  });

  // No Checkout page needed — upgrade is instant
  return NextResponse.json({ redirect_url: '/subscribe/success' });
}

// NEW SUBSCRIBER PATH — create Checkout Session (existing flow)
```

### Why This Works

- `stripe.subscriptions.update()` swaps the Price ID on the existing subscription
- Stripe automatically prorates — credits unused time on old plan, charges difference for new plan
- Stripe fires `customer.subscription.updated` webhook event
- Your webhook handler already handles this event type — it updates the tier in Supabase
- ONE subscription in Stripe, ONE row in Supabase, correct tier reflected in your app

### Key Detail

The upgrade path returns an internal URL (`/subscribe/success`), not a Stripe URL. The user doesn't need to enter card details again — they already have a payment method on file. The PlanCard's `window.location.href` handles both internal and external URLs, so no client code changes needed.

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
"Welcome to Pro!" with a Continue button. Shown when the subscription tier is no longer "free."

**State 3 — Timeout (amber info):**
"Your payment was received! Your subscription will activate momentarily." with a Refresh button. Shown after 5 failed polls (10 seconds).

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

```typescript
// /api/customer-portal/route.ts
export async function POST(request: Request) {
  // 1. Authenticate user
  // 2. Look up stripe_customer_id from subscriptions table
  // 3. Create portal session:
  const session = await stripe.billingPortal.sessions.create({
    customer: stripeCustomerId,
    return_url: `${origin}/members-portal/account`,
  });
  // 4. Return { redirect_url: session.url }
}
```

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

**END OF STRIPE SUBSCRIPTIONS PLAYBOOK v1.0**
