# REVIEW 021: 4_MANUAL-STRIPE_SUBSCRIPTIONS_PLAYBOOK.md

> **Review Series:** Stark Industries App Factory — Full Doc Stack Audit
> **Reviewer:** Architect Jarvis
> **Date:** 2026-07-06
> **Doc Version Reviewed:** v1.0 (2026-04-28, StarkReads Subscription v1 distillation)
> **Tier:** 4 — Reference Manuals (TIER CLOSER)
> **Verdict:** KEEP — v1.1 micro-patch only (territory declaration + cross-refs)

---

## 1. What This Doc Is

The recurring-billing recipe for Next.js + Supabase: Stripe object model, setup + schema recipes, checkout flow, webhook handler, tier-upgrade pattern, service-layer swap, success-page polling, customer portal, gotchas (scar-tissue format), testing strategy, deployment checklist, Phase 3 roadmap.

## 2. Strengths (two promotions)

- **D-016a — the three-sentence mental model:** "Stripe owns the truth about money. Supabase owns the cache. Webhooks keep them in sync — one-way street: Stripe speaks, Supabase listens." An integration architecture in 27 words.
- **D-016b — RBAC ⊥ Subscriptions orthogonality:** "Never implement subscription tiers as roles... they cross at right angles" + composable gate helpers (requireUser / requireRole / requireSubscriptionTier). Boundary doctrine valuable to F-042's resolution regardless of outcome (defines what roles are NOT, independent of storage). Doc stays neutral on role storage — clean of the conflict.
- Gotchas in symptom/root-cause/fix/lesson format (double-subscription bug, webhook-secret rotation, request.text() not json()).
- Proper header at top ✓; no API pins (better than its sibling); zero mojibake/Stitch/stale refs.
- Key-files index at tail — liftable.

## 3. Territory Verdict (pair check with Review 020)

Clean from BOTH sides: zero PaymentIntent here; zero subscriptions in ECOMMERCE manual. The split is TWO-DIMENSIONAL — WooCommerce/one-time vs Supabase/recurring — which also fills the ecommerce manual's F-040 backend-jurisdiction gap. Undeclared: two mirror cross-ref lines complete the marriage (queued in both v1.1s).

## 4. Findings

| ID | Severity | Finding |
|----|----------|---------|
| F-035 (roster) | LOW | Island: zero cross-doc refs — §8 (Service Layer Swap) should link API_AND_SERVICES_MANUAL; §12 (Testing Strategy) should link TESTING_PLAYBOOK — its sibling by provenance (both StarkReads-distilled). Separated at birth, never introduced. |
| Territory (fold into F-040 fix) | — | Undeclared two-dimensional split with ECOMMERCE manual — mirror cross-ref line here. |

## 5. Required Changes for v1.1 (micro)

1. Territory declaration: "One-time payments / WooCommerce commerce → ECOMMERCE_AND_PAYMENTS_MANUAL."
2. Cross-refs: API_AND_SERVICES_MANUAL (§8), TESTING_PLAYBOOK (§12), AUTH_MANUAL (gate-helper composition).
3. Nothing else.

## 6. Cross-Doc Dependencies Noted

Territory pair: ECOMMERCE_AND_PAYMENTS_MANUAL (clean 2-D split). Provenance sibling: TESTING_PLAYBOOK (StarkReads). Doctrine boundary input to: F-042 (orthogonality rule). Outbound refs: none (finding).

---

## TIER 4 CLOSING SUMMARY (Reviews 015–021)

Seven manuals, seven KEEPs. The tier pattern: **content mostly sound, bookkeeping mostly absent** — four fully unversioned docs (F-018 roster: State, API, Database, Ecommerce), pervasive outbound isolation (F-035 roster), and stale pins (F-038: Next 15, Stripe 2023). Three substantive catches: F-039 (the unamended root of Lesson 2 in the API manual), F-041 (Database Manual's split role doctrine), and the tier's crown finding **F-042 — the three-way role-storage conflict (Auth Manual's metadata-driven philosophy vs Recon's forbidden smell vs Database's split), security-classed and BLOCKING on Tony's Mark IV ground-truth.** Gold promoted: D-016 (money-truth mental model + RBAC orthogonality). Tier 4 rewrite theme: *headers everywhere, bridges everywhere, one role doctrine.*

---

*Part of the Factory Doc Stack Audit series. See FINDINGS_LOG.md for the running catch list.*
