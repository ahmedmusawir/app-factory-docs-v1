# ✅ WAVE 4 — DOC 7 COMPLETE: STRIPE_SUBSCRIPTIONS_PLAYBOOK → v1.1 (WAVE 4 CLOSED)

**File:** `4_MANUAL-STRIPE_SUBSCRIPTIONS_PLAYBOOK.md` (micro — the D-016 gold untouched)

## CHANGES MADE

| # | Change | Finding |
|---|--------|---------|
| 1 | Standard header (v1.1 · 2026-07-08 · Tier 4) + **Territory line**: RECURRING only; one-time/WooCommerce → ECOMMERCE_AND_PAYMENTS_MANUAL — the pair's two-way declaration is now complete | F-018, F-040 pair |
| 2 | Cross-References ×4: ECOMMERCE (pair), API_AND_SERVICES (§8 swap pattern + Kit Exception), TESTING_PLAYBOOK (§12 — the StarkReads provenance siblings finally introduced), AUTH_MANUAL (gate-helper composition; roles ⊥ tiers) | F-035 |
| 3 | Version History table (1.0 + 1.1); stale "v1.0" END label fixed | D-018 |
| 4 | Content untouched — money-truth model + RBAC ⊥ subscriptions (D-016) preserved verbatim | — |

## FULL-WAVE VERIFICATION (all 7 Tier 4 manuals)

| Gate | AUTH | DB | API | ARCH | STATE | ECOM | STRIPE |
|---|---|---|---|---|---|---|---|
| 3-class encoding (C1/moji/dash) | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `_v` live refs | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Standard header | ✓1.3 | ✓1.1 | ✓1.1 | ✓1.3 | ✓1.1 | ✓1.1 | ✓1.1 |
| Wave 4 history row | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

Doctrine gates: **AUTH + DATABASE speak ONE role doctrine** (table-based; metadata authz-reads forbidden in both; DB §2↔§5 reconciled) ✓ · API carries the Lesson-2 exception at the root ✓ · ARCH de-pinned + recon-pointed ✓ · scope/territory pair declared two-way ✓ · F-035 bridges on all seven ✓

## THINGS I DIDN'T TOUCH (wave-wide)

D-016 doctrine; STATE content; all §§ not named in the plan; every file outside the seven + the one authorized Example A line.

## CONCERNS (wave-level, all tracked in RECOVERY)

1. **Kit-verification touch (pairs with the signup-vector ticket):** AUTH §5/§10 samples + `is_qr_*` naming, DB `user_roles` pattern-SQL, ARCH TS/Tailwind minor pins — all to confirm against the kit on disk.
2. API manual's pre-existing duplicate "§10 Quick Reference" — numbering decision queued.
3. F-012 editing-tool identification still open — three docs now show identical post-"fix" re-corruption signatures.
4. RECON_WAVE0.md to be added to `_AUDIT/` by operator (worked around via F-042 log row).

## Suggested commit

wave4(stripe-subs): v1.1 — territory declaration, cross-refs, F-035
