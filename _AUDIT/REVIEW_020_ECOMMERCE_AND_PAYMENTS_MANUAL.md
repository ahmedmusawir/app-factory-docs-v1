# REVIEW 020: 4_MANUAL-ECOMMERCE_AND_PAYMENTS_MANUAL.md

> **Review Series:** Stark Industries App Factory — Full Doc Stack Audit
> **Reviewer:** Architect Jarvis
> **Date:** 2026-07-06
> **Doc Version Reviewed:** UNVERSIONED (F-018 roster)
> **Tier:** 4 — Reference Manuals
> **Verdict:** KEEP — v1.1 patch (scope declaration, API-pin fix, metadata, territory cross-ref)

---

## 1. What This Doc Is

The one-time-payments commerce doctrine: payment architecture, Stripe setup, PaymentIntent flow, checkout implementation, order management, cart logic, checkout store, coupons, webhook handling, payment testing, security checklist. Dockbloxx-pattern: headless WooCommerce backend + Stripe.

## 2. Strengths

- **Clean territory split with STRIPE_SUBSCRIPTIONS_PLAYBOOK:** zero subscription mentions — this doc owns one-time payments; the playbook owns recurring. No F-017-style duplication between the payment pair. (Split is real but undeclared — one cross-ref line each; verify at Review 021.)
- **Order-First pattern** — "always create the order BEFORE processing payment" — sound, quotable commerce doctrine with stated rationale.
- **Webhook security correct:** stripe-signature verification present; production-grade closing checklist (Radar, fraud protection, disputes, receipts).
- Encoding spotless; has a canonical-name cross-ref (STATE_MANAGEMENT_MANUAL — checkout store) — semi-connected, not an island.

## 3. Findings

| ID | Severity | Finding |
|----|----------|---------|
| F-038 (extended) | MEDIUM | Self-contradicting API pin: `apiVersion: '2023-10-16', // Use latest stable version` — a ~2.5-year-old pin whose own comment disagrees with it. Same stale-pin disease as the Next.js 15 case. Fix: reference the kit's actual pin or add verify-per-repo note. |
| F-040 (extended) | MEDIUM | Backend scope undeclared: 25 WooCommerce mentions, 0 Supabase, framed as "THE E-commerce Module." Agents on the dominant Supabase kit receive non-mapping doctrine. Fix: scope declaration paragraph ("this manual = headless WooCommerce + Stripe commerce; Supabase-native commerce → extend or see X"). |
| F-018 (roster) | MEDIUM | Unversioned — fourth Tier 4 manual with no version/date/history. |

## 4. Required Changes for v1.1

1. Scope declaration paragraph at top (F-040).
2. API-pin fix per F-038 pattern.
3. Standard header block + version-history table.
4. Territory cross-ref: "Recurring billing → STRIPE_SUBSCRIPTIONS_PLAYBOOK" (mirror line lands there at Review 021).

## 5. Cross-Doc Dependencies Noted

References: STATE_MANAGEMENT_MANUAL (canonical ✓). Territory pair: STRIPE_SUBSCRIPTIONS_PLAYBOOK (clean split, undeclared). Referenced by: APP_ARCHITECTURE_MANUAL (Stripe integration pointer). Backend scope: WooCommerce-only (F-040 extension).

---

*Part of the Factory Doc Stack Audit series. See FINDINGS_LOG.md for the running catch list.*
