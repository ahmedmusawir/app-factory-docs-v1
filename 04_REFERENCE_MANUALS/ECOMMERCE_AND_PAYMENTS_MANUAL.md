# ECOMMERCE AND PAYMENTS MANUAL

> **Version:** 1.2 · **Date:** 2026-10-18 · **Status:** Active
> **Tier:** 4 — Reference Manuals · **Pairs with:** STRIPE_SUBSCRIPTIONS_PLAYBOOK, STATE_MANAGEMENT_MANUAL, API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL

> **Stark Industries Software Factory**
> *E-commerce doctrine: Stripe integration, WooCommerce backend, cart logic, and checkout flows.*

---

## Scope Declaration (read first)

**This manual covers ONE commerce shape: headless WooCommerce backend + Stripe ONE-TIME payments** (the Dockbloxx pattern — PaymentIntents, carts, checkout, orders, coupons).

- **Recurring billing / subscriptions** → `STRIPE_SUBSCRIPTIONS_PLAYBOOK.md` (Next.js + Supabase; the territory pair — zero overlap by design).
- **Supabase-native commerce** (products/orders in Supabase instead of WooCommerce) → not yet covered; extend this manual's service-layer patterns rather than assuming WooCommerce shapes apply.

The architecture patterns (Order-First, webhook verification, checkout store) generalize; the WooCommerce API shapes do not.

---

## Table of Contents

1. [Payment Architecture Overview](#1-payment-architecture-overview)
2. [Stripe Setup](#2-stripe-setup)
3. [PaymentIntent Flow](#3-paymentintent-flow)
4. [Checkout Implementation](#4-checkout-implementation)
5. [Order Management](#5-order-management)
6. [Cart Logic](#6-cart-logic)
7. [Checkout Store](#7-checkout-store)
8. [Coupon System](#8-coupon-system)
9. [Webhook Handling](#9-webhook-handling)
10. [Testing Payments](#10-testing-payments)
11. [Security Checklist](#11-security-checklist)

---

## 1. Payment Architecture Overview

### The Payment Flow (High-Level)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           CUSTOMER JOURNEY                                   │
└─────────────────────────────────────────────────────────────────────────────┘

    ┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
    │  Browse  │ ──► │   Cart   │ ──► │ Checkout │ ──► │ Thank You│
    │ Products │     │   Page   │     │   Flow   │     │   Page   │
    └──────────┘     └──────────┘     └──────────┘     └──────────┘
                                            │
                                            ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                           CHECKOUT FLOW DETAIL                               │
└─────────────────────────────────────────────────────────────────────────────┘

    ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
    │   Contact    │ ──► │   Shipping   │ ──► │   Payment    │
    │    Info      │     │   Address    │     │   Details    │
    └──────────────┘     └──────────────┘     └──────────────┘
                                                     │
                                                     ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                           PAYMENT PROCESSING                                 │
└─────────────────────────────────────────────────────────────────────────────┘

    ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
    │ Create Order │ ──► │   Create     │ ──► │   Confirm    │
    │ (WooCommerce)│     │PaymentIntent │     │   Payment    │
    └──────────────┘     │   (Stripe)   │     │   (Stripe)   │
                         └──────────────┘     └──────────────┘
                                                     │
                                                     ▼
                                              ┌──────────────┐
                                              │Update Order  │
                                              │   Status     │
                                              └──────────────┘
```

### Key Principle: Order-First Pattern

**Always create the order BEFORE processing payment.**

This ensures:
1. Order exists in your system regardless of payment outcome
2. Order ID can be attached to PaymentIntent metadata
3. Failed payments can be retried against existing order
4. Inventory is reserved before payment

### System Components

| Component | Technology | Purpose |
|-----------|------------|---------|
| Product Catalog | WooCommerce REST API | Product data, inventory, pricing |
| Shopping Cart | Zustand (client-side) | Cart state, persistence |
| Checkout Form | React Hook Form + Zod | Form validation, data collection |
| Payment Processing | Stripe | Secure payment handling |
| Order Management | WooCommerce REST API | Order creation, status updates |
| Webhooks | Next.js API Routes | Async payment confirmations |

### Security Principles

1. **Never expose secret keys** - Stripe Secret Key stays server-side only
2. **Validate on server** - Never trust client-side totals
3. **Use HTTPS** - All payment pages must be HTTPS
4. **PCI Compliance** - Use Stripe Elements (never handle raw card data)
5. **Idempotency** - Use idempotency keys for retries

---

## 2. Stripe Setup

### Environment Variables

```bash
# .env.local

# Public key (safe for client-side)
NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=pk_test_xxx

# Secret key (server-side ONLY)
STRIPE_SECRET_KEY=sk_test_xxx

# Webhook secret (for verifying webhook signatures)
STRIPE_WEBHOOK_SECRET=whsec_xxx
```

### Dependencies

```bash
npm install stripe @stripe/stripe-js @stripe/react-stripe-js
```

| Package | Purpose | Environment |
|---------|---------|-------------|
| `stripe` | Server-side Stripe SDK | Server only |
| `@stripe/stripe-js` | Client-side Stripe.js loader | Client only |
| `@stripe/react-stripe-js` | React components (Elements) | Client only |

### Client-Side Initialization

```typescript
// src/lib/stripe/client.ts
'use client';

import { loadStripe, Stripe } from '@stripe/stripe-js';

let stripePromise: Promise<Stripe | null>;

export const getStripe = () => {
  if (!stripePromise) {
    stripePromise = loadStripe(
      process.env.NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY!
    );
  }
  return stripePromise;
};
```

### Server-Side Initialization

```typescript
// src/lib/stripe/server.ts

import Stripe from 'stripe';

if (!process.env.STRIPE_SECRET_KEY) {
  throw new Error('STRIPE_SECRET_KEY is not set');
}

export const stripe = new Stripe(process.env.STRIPE_SECRET_KEY, {
  // apiVersion: match the version your repo's Stripe SDK types expect —
  // verify per repo (package.json + the kit's existing stripe.ts), never
  // copy a pinned date from doctrine (F-038 stale-pin lesson).
  typescript: true,
});
```

---

## 3. PaymentIntent Flow

**Executable example withdrawn.** The previous example is not an approved implementation. The outgoing archived document preserves it as history. Replacement code requires the project’s approved contract, verified dependency interfaces and behavioral evidence. This withdrawal contains the misleading recipe; it does not certify the underlying finding resolved.

The browser may display or poll payment status; it may not choose paid or processing state. A payment-derived transition requires verified server-side evidence bound to the stored order and payment attempt, including amount and currency. Non-webhook mutations authenticate and authorize the operation and target, including an explicitly approved guest capability where supported, then validate the state transition.

Accept product/variation identifiers, quantities, shipping selection and coupon code, never caller prices, shipping costs or discount amounts. Validate quantities and product eligibility; load authoritative catalog prices; validate the shipping selection and coupon eligibility; apply the declared tax policy; calculate currency-safe totals on the server. Bind the payment to the authorized order and verify payment identity, amount, currency and order association before marking paid. Client totals are display-only. Return generic failures and redact logs. Universal quote-storage design is deferred; the required server pricing and payment binding still apply.

Persist one authorized checkout-attempt identity across retries and claim it atomically against concurrent requests. Scope provider idempotency keys to that attempt and operation, reuse or retrieve existing external objects after an unknown outcome, and reconcile before creating a replacement. Use the project-approved customer-identity contract without assuming paid activation; universal subscription schema design is deferred. Handle every documented subscription state, not only active.

Use one validated checkout contract across form, state, route and service. The request carries billing.email, validated line identifiers/quantities, shippingMethod and couponCode; it carries no authoritative monetary values. The response identifies the authorized order/payment attempt or a typed generic failure. The server pricing operation from the same contract supplies totals. Revisions to items, shipping or coupon invalidate the old payment binding before a new attempt is released.

---

## 4. Checkout Implementation

**Executable example withdrawn.** The previous example is not an approved implementation. The outgoing archived document preserves it as history. Replacement code requires the project’s approved contract, verified dependency interfaces and behavioral evidence. This withdrawal contains the misleading recipe; it does not certify the underlying finding resolved.

Accept product/variation identifiers, quantities, shipping selection and coupon code, never caller prices, shipping costs or discount amounts. Validate quantities and product eligibility; load authoritative catalog prices; validate the shipping selection and coupon eligibility; apply the declared tax policy; calculate currency-safe totals on the server. Bind the payment to the authorized order and verify payment identity, amount, currency and order association before marking paid. Client totals are display-only. Return generic failures and redact logs. Universal quote-storage design is deferred; the required server pricing and payment binding still apply.

Persist one authorized checkout-attempt identity across retries and claim it atomically against concurrent requests. Scope provider idempotency keys to that attempt and operation, reuse or retrieve existing external objects after an unknown outcome, and reconcile before creating a replacement. Use the project-approved customer-identity contract without assuming paid activation; universal subscription schema design is deferred. Handle every documented subscription state, not only active.

Use one validated checkout contract across form, state, route and service. The request carries billing.email, validated line identifiers/quantities, shippingMethod and couponCode; it carries no authoritative monetary values. The response identifies the authorized order/payment attempt or a typed generic failure. The server pricing operation from the same contract supplies totals. Revisions to items, shipping or coupon invalidate the old payment binding before a new attempt is released.

The checkout interaction contract includes shippingCost and couponDiscount as display estimates, couponCode, setCoupon(code) and clearCoupon(), alongside the existing checkout fields. The server revalidates shipping and coupons. STATE_MANAGEMENT_MANUAL owns the shared store shape; ECOMMERCE_AND_PAYMENTS_MANUAL refers to it. Personal fields follow the approved account-transition and retention policy.

---

## 5. Order Management

**Executable example withdrawn.** The previous example is not an approved implementation. The outgoing archived document preserves it as history. Replacement code requires the project’s approved contract, verified dependency interfaces and behavioral evidence. This withdrawal contains the misleading recipe; it does not certify the underlying finding resolved.

The browser may display or poll payment status; it may not choose paid or processing state. A payment-derived transition requires verified server-side evidence bound to the stored order and payment attempt, including amount and currency. Non-webhook mutations authenticate and authorize the operation and target, including an explicitly approved guest capability where supported, then validate the state transition.

Accept product/variation identifiers, quantities, shipping selection and coupon code, never caller prices, shipping costs or discount amounts. Validate quantities and product eligibility; load authoritative catalog prices; validate the shipping selection and coupon eligibility; apply the declared tax policy; calculate currency-safe totals on the server. Bind the payment to the authorized order and verify payment identity, amount, currency and order association before marking paid. Client totals are display-only. Return generic failures and redact logs. Universal quote-storage design is deferred; the required server pricing and payment binding still apply.

Persist one authorized checkout-attempt identity across retries and claim it atomically against concurrent requests. Scope provider idempotency keys to that attempt and operation, reuse or retrieve existing external objects after an unknown outcome, and reconcile before creating a replacement. Use the project-approved customer-identity contract without assuming paid activation; universal subscription schema design is deferred. Handle every documented subscription state, not only active.

Use one validated checkout contract across form, state, route and service. The request carries billing.email, validated line identifiers/quantities, shippingMethod and couponCode; it carries no authoritative monetary values. The response identifies the authorized order/payment attempt or a typed generic failure. The server pricing operation from the same contract supplies totals. Revisions to items, shipping or coupon invalidate the old payment binding before a new attempt is released.

---

## 6. Cart Logic

**Executable example withdrawn.** The previous example is not an approved implementation. The outgoing archived document preserves it as history. Replacement code requires the project’s approved contract, verified dependency interfaces and behavioral evidence. This withdrawal contains the misleading recipe; it does not certify the underlying finding resolved.

Keep hydration readiness outside the resettable business state. A normal reset preserves readiness. Hydration finishes in ready or error; an error exposes bounded recovery and never leaves an indefinite loading state. Verify reset after hydration, invalid stored data and unavailable storage.

The browser may display or poll payment status; it may not choose paid or processing state. A payment-derived transition requires verified server-side evidence bound to the stored order and payment attempt, including amount and currency. Non-webhook mutations authenticate and authorize the operation and target, including an explicitly approved guest capability where supported, then validate the state transition.

---

## 7. Checkout Store

See the `STATE_MANAGEMENT_MANUAL.md` for the full checkout store implementation. Key points:

### Checkout Data Structure

```typescript
interface CheckoutState {
  // Customer
  email: string;
  
  // Addresses
  billingAddress: Address | null;
  shippingAddress: Address | null;
  sameAsShipping: boolean;
  
  // Shipping
  shippingMethodId: string | null;
  shippingCost: number;
  
  // Payment
  paymentMethodId: string | null;
  
  // Coupon
  couponCode: string | null;
  couponDiscount: number;
  
  // Order
  customerNotes: string;
  
  // UI State
  currentStep: number;
  isProcessing: boolean;
  validationErrors: Record<string, string>;
}
```

### Totals Calculation

**Dependent executable example withdrawn.** Use a project-approved state/payment contract with explicit hydration errors, server-authoritative pricing, authenticated ownership and recovery. The removed example’s missing contract is still tracked; no universal quote/subscription schema is introduced.

---

## 8. Coupon System

### Coupon Validation

```typescript
// src/app/api/get-coupon-by-code/route.ts

import { NextRequest, NextResponse } from 'next/server';
import { validateCoupon } from '@/services/couponServices';

export async function GET(request: NextRequest) {
  const code = request.nextUrl.searchParams.get('code');

  if (!code) {
    return NextResponse.json(
      { error: 'Coupon code is required' },
      { status: 400 }
    );
  }

  try {
    const coupon = await validateCoupon(code);

    if (!coupon) {
      return NextResponse.json(
        { error: 'Invalid coupon code' },
        { status: 404 }
      );
    }

    // Check if coupon is expired
    if (coupon.date_expires && new Date(coupon.date_expires) < new Date()) {
      return NextResponse.json(
        { error: 'This coupon has expired' },
        { status: 400 }
      );
    }

    // Check usage limits
    if (coupon.usage_limit && coupon.usage_count >= coupon.usage_limit) {
      return NextResponse.json(
        { error: 'This coupon has reached its usage limit' },
        { status: 400 }
      );
    }

    return NextResponse.json({
      coupon: {
        code: coupon.code,
        discountType: coupon.discount_type,
        amount: coupon.amount,
        freeShipping: coupon.free_shipping,
        minimumAmount: coupon.minimum_amount,
        maximumAmount: coupon.maximum_amount,
      },
    });
  } catch (error) {
    console.error('Error validating coupon:', error);
    return NextResponse.json(
      { error: 'Failed to validate coupon' },
      { status: 500 }
    );
  }
}
```

### Discount Calculation

**Executable example withdrawn.** The previous example is not an approved implementation. The outgoing archived document preserves it as history. Replacement code requires the project’s approved contract, verified dependency interfaces and behavioral evidence. This withdrawal contains the misleading recipe; it does not certify the underlying finding resolved.

A fixed-product coupon uses validated eligible line items and quantities in the authoritative server pricing operation. Do not advertise fixed_product through a flat-cart subtotal branch. A client calculation is a display estimate only. Verify equal-subtotal carts with different eligible quantities; preserve valid fixed-cart and percentage behavior.

---

### Coupon UI Component

**Dependent executable example withdrawn.** Use a project-approved state/payment contract with explicit hydration errors, server-authoritative pricing, authenticated ownership and recovery. The removed example’s missing contract is still tracked; no universal quote/subscription schema is introduced.

---

## 9. Webhook Handling

### Webhook Endpoint Setup

**Executable example withdrawn.** The previous example is not an approved implementation. The outgoing archived document preserves it as history. Replacement code requires the project’s approved contract, verified dependency interfaces and behavioral evidence. This withdrawal contains the misleading recipe; it does not certify the underlying finding resolved.

For supported events, check business persistence or durable enqueue before acknowledging. Pre-acceptance failure returns a retryable failure. After durable acceptance, worker failures enter bounded durable retries and visible failed-work reconciliation with an alert and recovery owner. Unsupported events are explicitly distinguished from failed supported events. Missing order/user mappings create actionable recovery records, not silent success.

Converge each order or subscription aggregate using authoritative provider retrieval or explicit freshness and legal-transition rules. Reject stale transitions; check zero-row updates and repair missing mappings. A late event for an old subscription may not overwrite its replacement. Define reconciliation of the local mirror independently of inbound deduplication.

Distinguish optional telemetry from required follow-up. Complete required work retry-safely or durably enqueue it before acknowledgment. Failed or unconfirmed enqueue returns retryable failure. A later worker failure uses bounded durable retry, visible failed-work state and a named recovery owner. Inspect non-success HTTP responses from follow-up targets; a resolved fetch is not proof of success.

Refund and dispute handling is INCOMPLETE and not a production recipe until the module contract defines partial/full refund effects, dispute transitions, notification and recovery owners. Do not acknowledge a supported event until its required local work is completed or durably accepted under the webhook contract.

---

### Signature Verification

**Always verify webhook signatures.** This prevents attackers from sending fake events.

```typescript
// The signature verification happens in constructEvent()
// It uses your STRIPE_WEBHOOK_SECRET to verify the request came from Stripe

try {
  event = stripe.webhooks.constructEvent(
    body,           // Raw request body (must be string, not parsed JSON)
    signature,      // stripe-signature header
    webhookSecret   // Your webhook secret from Stripe Dashboard
  );
} catch (err) {
  // Invalid signature - reject the request
  return NextResponse.json({ error: 'Invalid signature' }, { status: 400 });
}
```

### Event Types

| Event | When It Fires | Action |
|-------|---------------|--------|
| `payment_intent.succeeded` | Payment completed | Update order to "processing" |
| `payment_intent.payment_failed` | Payment failed | Update order to "failed" |
| `charge.refunded` | Refund processed | Update order, notify customer |
| `charge.dispute.created` | Chargeback initiated | Flag order, notify admin |

---

## 10. Testing Payments

The Architect includes the API trust-boundary matrix in the acceptance contract; the Engineer supplies engineering results, the QA Executor derives independent checks, and the QA Lead approves and grades them. Cover unauthenticated/wrong-role/wrong-owner calls, forged payment status, tampered totals, duplicate and concurrent requests, invalid signatures, pre-acceptance persistence failure, post-acceptance worker failure, and stale/out-of-order events. Each case records status, absence of unauthorized effects, persisted final state and retry/recovery evidence. TESTING_PLAYBOOK owns the matrix; commerce, subscription and API manuals refer to it.

### Test Card Numbers

| Card Number | Scenario |
|-------------|----------|
| `4242 4242 4242 4242` | Successful payment |
| `4000 0000 0000 0002` | Card declined |
| `4000 0000 0000 9995` | Insufficient funds |
| `4000 0000 0000 9987` | Lost card |
| `4000 0000 0000 9979` | Stolen card |
| `4000 0027 6000 3184` | Requires authentication (3D Secure) |
| `4000 0000 0000 0077` | Charge succeeds, then disputed |

Use any future expiration date and any 3-digit CVC.

### Test Scenarios

```typescript
// Test file: __tests__/checkout.test.ts

describe('Checkout Flow', () => {
  it('should complete checkout with valid card', async () => {
    // 1. Add items to cart
    // 2. Fill checkout form
    // 3. Submit with test card 4242...
    // 4. Verify order created
    // 5. Verify redirect to thank you page
  });

  it('should handle declined card', async () => {
    // 1. Add items to cart
    // 2. Fill checkout form
    // 3. Submit with test card 4000 0000 0000 0002
    // 4. Verify error message displayed
    // 5. Verify order status is "pending" or "failed"
  });

  it('should handle 3D Secure authentication', async () => {
    // 1. Add items to cart
    // 2. Fill checkout form
    // 3. Submit with test card 4000 0027 6000 3184
    // 4. Verify 3DS modal appears
    // 5. Complete authentication
    // 6. Verify order completed
  });
});
```

### Error Simulation

```typescript
// Trigger specific errors for testing

// Insufficient funds
const testInsufficientFunds = async () => {
  // Use card: 4000 0000 0000 9995
  // Error code: insufficient_funds
};

// Expired card
const testExpiredCard = async () => {
  // Use any card with past expiration date
  // Error code: expired_card
};

// Invalid CVC
const testInvalidCVC = async () => {
  // Use card: 4000 0000 0000 0127
  // Error code: incorrect_cvc
};
```

---

## 11. Security Checklist

### API Key Security

- [ ] `STRIPE_SECRET_KEY` is in `.env.local` (not committed)
- [ ] `STRIPE_SECRET_KEY` does NOT have `NEXT_PUBLIC_` prefix
- [ ] Secret key is only used in server-side code (`src/app/api/`, `src/services/`)
- [ ] Publishable key (`pk_`) is used on client-side
- [ ] Webhook secret is stored securely

### PCI Compliance

- [ ] Using Stripe Elements (never handling raw card data)
- [ ] Not logging card numbers or CVCs
- [ ] Not storing card data in database
- [ ] HTTPS enabled on all payment pages
- [ ] Using `PaymentElement` or `CardElement` from Stripe

### Input Validation

- [ ] Server-side validation of all checkout data
- [ ] Server-side recalculation of totals (never trust client)
- [ ] Coupon validation on server
- [ ] Order amount validation (minimum $0.50)
- [ ] Email format validation

### Order Security

- [ ] Order created before payment (Order-First Pattern)
- [ ] Order ID in PaymentIntent metadata
- [ ] Order status updated via webhook (not just client callback)
- [ ] Idempotency keys for retries

### Webhook Security

- [ ] Signature verification enabled
- [ ] Webhook endpoint not publicly documented
- [ ] Raw body used for signature verification (not parsed JSON)
- [ ] Proper error handling without leaking info

### Environment Security

```bash
# .env.local (NEVER commit this file)

# Stripe
NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=pk_test_xxx  # OK to expose
STRIPE_SECRET_KEY=sk_test_xxx                    # NEVER expose
STRIPE_WEBHOOK_SECRET=whsec_xxx                  # NEVER expose

# WooCommerce
WOOCOM_CONSUMER_KEY=ck_xxx                       # NEVER expose
WOOCOM_CONSUMER_SECRET=cs_xxx                    # NEVER expose
```

### Production Checklist

- [ ] Switch from `sk_test_` to `sk_live_` keys
- [ ] Switch from `pk_test_` to `pk_live_` keys
- [ ] Update webhook endpoint in Stripe Dashboard
- [ ] Test with real (small) transaction
- [ ] Enable fraud protection in Stripe Dashboard
- [ ] Set up Stripe Radar rules
- [ ] Configure email receipts
- [ ] Set up dispute notifications

---

## Cross-References (Factory Doctrine)

- **`STRIPE_SUBSCRIPTIONS_PLAYBOOK.md`** — the territory pair: recurring billing, tiers, webhooks-as-sync (D-016 money-truth model).
- **`STATE_MANAGEMENT_MANUAL.md`** — the checkout store's Zustand doctrine.
- **`API_AND_SERVICES_MANUAL.md`** — the service-layer rules these integrations run on (incl. wire-format conventions).
- **`TESTING_PLAYBOOK.md`** — payment-flow testing (Stripe boundary-stop pattern, webhook tests).

---

## Version History

| Version | Date | Changes |
|---|---|---|
| 1.0 | (original, date unknown) | Initial manual: payment architecture, Stripe setup, PaymentIntent flow, checkout, orders, cart logic, checkout store, coupons, webhooks, testing, security checklist. Unversioned until the 2026-07 audit. |
| 1.1 | 2026-07-08 | **Wave 4 (audit sync).** Scope Declaration added at top — this manual = headless WooCommerce + Stripe ONE-TIME commerce; recurring → STRIPE_SUBSCRIPTIONS_PLAYBOOK; Supabase-native commerce = extend, don't assume (F-040 undeclared-jurisdiction fix; "THE E-commerce Module" framing dropped). Self-contradicting Stripe pin removed (`apiVersion: '2023-10-16' // Use latest`) → verify-per-repo note (F-038 pattern). Cross-References section (F-035); standard header (F-018); this history table (D-018). |
| 1.2 | 2026-10-18 | Factory DocSet sync: approved workflow/security/reference corrections; preserved original; explicit exclusions per doctrine-part2 map. IDs: FC-047, FC-050, FC-051, FC-052, FC-053, FC-054, FC-055, FC-059, FC-060, FC-062, FC-063, FC-067, FC-068, RUL-11 |

---

*This manual is part of the Stark Industries Software Factory documentation suite.*
