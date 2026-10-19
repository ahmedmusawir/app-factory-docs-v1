# AMENDED-v2 — F01–F05 complete proposal

Status: ENGINEER-PROPOSED; Tony Gate 2 PENDING. Preparation only.

QA Lead verdict F01–F05; Jarvis correction directions confirmed by Tony in current preparation assignment. Exact proposed bytes remain subject to Tony Gate 2; no approval inferred.

Candidate: `20f71ee932ed21c0878cb3a0f39c6fbe90d0a793`; landing date 2026-10-18. FU-1/FU-2 excluded.

## Accounting correction (current Director assignment)

R6: seven changed canonical paths (six documents plus CHANGELOG.md), 94 unchanged paths in the 101-path index. R12: only those seven canonical paths plus new run records and normal bookkeeping are allowed. CHANGELOG is included in contents, patch and verification. This clarifies the repair prompt only; frozen spec R1 is byte-unchanged. The 39 current-run CHANGELOG rows retain their count; six existing rows gain the QA clause.

## Replay semantics

SELECTED_EXACT_EDITS preserves E001–E380 exactly as provenance and appends E381 onward. Replay the new suffix against candidate bytes (already metadata/date-bound); do not replay the concatenated provenance list directly against BASE without the original metadata/date binding stages. EXECUTION_PROPOSAL.patch is the complete seven-path delta against git archive 20f71ee932ed21c0878cb3a0f39c6fbe90d0a793, applied with -p0 only to a disposable verification export before approval. Both successor indices cover all 101 paths using candidate before hashes.

## Exact old-to-new spans

### E381 — F01 — 02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:176

Evidence: pinned candidate span; QA verdict §2 and repair prompt §1/§2.

Old:
````text
> Same artifact name — different author, different moment. Router: APP_FACTORY_BLUEPRINT, "Which Pipeline Am I In?".
````

New:
````text
> The Architect authors `DATA_CONTRACT.md` in both runs; only the evidence base and moment differ: conversion uses Brain Drain evidence and is pre-authored; greenfield uses the approved APP_BRIEF before Design. Router: APP_FACTORY_BLUEPRINT, "Which Pipeline Am I In?".
````

### E382 — F02 — 02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:1385

Evidence: pinned candidate span; QA verdict §2 and repair prompt §1/§2.

Old:
````text
When code is complete and tested, Engineer hands off to Operations/Deployment.
````

New:
````text
When code is complete and self-verified, the Engineer hands the candidate and factual QAM engineering handoff to independent QA on the Director-created QA branch; Operations/Deployment receives the package only after QA Lead certification and Director release (see QAM_PLAYBOOK §3 and DEPLOYMENT_PLAYBOOK §3).
````

### E383 — F02 — 02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:1392

Evidence: pinned candidate span; QA verdict §2 and repair prompt §1/§2.

Old:
````text
├── APP_BRIEF.md (from Architect)
├── UI_SPEC.md (from Designer)
├── DATA_CONTRACT.md
├── Working Code (tested)
├── README.md (setup instructions)
└── Deployment Guide
````

New:
````text
├── APP_BRIEF.md (from Architect)
├── UI_SPEC.md (from Designer)
├── DATA_CONTRACT.md
├── ACCEPTANCE_SPEC.md (from Architect)
├── Working Code (tested)
├── QAM/ (module QA pack: ENGINEERING_HANDOFF, approved plan, results, certificate)
├── README.md (setup instructions)
└── Deployment Guide
````

### E384 — F03 — 02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:255

Evidence: pinned candidate span; QA verdict §2 and repair prompt §1/§2.

Old:
````text
   Read the handbook, treat it as ASPIRATIONAL — verify every load-bearing
   claim against disk (RECON_QUESTIONNAIRE §0). Where handbook and
   filesystem disagree, the filesystem wins.
````

New:
````text
   Read the handbook, treat it as ASPIRATIONAL — verify every load-bearing claim against disk (RECON_QUESTIONNAIRE §0).
   Disk establishes implementation facts; approved briefs govern scope and governing documents control their subjects.
   Record handbook drift; route genuine requirements conflicts to the Director.
````

### E385 — F04a / FC-022 — 03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:891

Evidence: pinned candidate span; QA verdict §2 and repair prompt §1/§2.

Old:
````text
```typescript
export async function seedSubscription(userId: string, tier: TestTier) {
  const { error } = await supabaseAdmin.from("subscriptions").upsert(
    {
      user_id: userId,
      tier,
      status: "active",
      stripe_customer_id: `cus_test_${userId.slice(0, 8)}`,
      stripe_subscription_id: `sub_test_${userId.slice(0, 8)}`,
      current_period_start: new Date().toISOString(),
      current_period_end: new Date(
        Date.now() + 30 * 24 * 60 * 60 * 1000,
      ).toISOString(),
      cancel_at_period_end: false,
    },
    { onConflict: "user_id" },
  );
  if (error) throw new Error(`Failed to seed subscription: ${error.message}`);
}
```
````

New:
````text
**Executable example withdrawn.** The previous example is not an approved implementation. The outgoing archived document preserves it as history. Replacement code requires the project’s approved contract, verified dependency interfaces and behavioral evidence. This withdrawal contains the misleading recipe; it does not certify the underlying finding resolved.

Privileged seeding and admin-client construction in test helpers run only behind the Director-approved test-project allowlist and authorized-test-identity guard above; fail closed on mismatch, missing identity or unknown target.
````

### E386 — F04a / FC-022 — 03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:918

Evidence: pinned candidate span; QA verdict §2 and repair prompt §1/§2.

Old:
````text
```typescript
import { createClient } from "@supabase/supabase-js";
import * as dotenv from "dotenv";

// Playwright runs outside Next.js — must load .env.local manually
dotenv.config({ path: ".env.local" });

export const supabaseAdmin = createClient(
  process.env.NEXT_PUBLIC_SUPABASE_URL!,
  process.env.SUPABASE_SECRET_KEY!,
  { auth: { autoRefreshToken: false, persistSession: false } },
);
```
````

New:
````text
**Executable example withdrawn.** The previous example is not an approved implementation. The outgoing archived document preserves it as history. Replacement code requires the project’s approved contract, verified dependency interfaces and behavioral evidence. This withdrawal contains the misleading recipe; it does not certify the underlying finding resolved.

Privileged seeding and admin-client construction in test helpers run only behind the Director-approved test-project allowlist and authorized-test-identity guard above; fail closed on mismatch, missing identity or unknown target.
````

### E387 — F04b / FC-038 — 04_REFERENCE_MANUALS/DATABASE_MANUAL.md:420

Evidence: pinned candidate span; QA verdict §2 and repair prompt §1/§2.

Old:
````text
When using the service role key (server-side), RLS is bypassed. This is appropriate for:
- API routes
- Background jobs
- Admin operations
````

New:
````text
A service-role client bypasses RLS and is appropriate only inside an independently authorized elevated operation:
- Background jobs with operation-local authorization
- Admin operations with operation-local authorization

An API route is not itself a reason to bypass RLS; never use a service-role client as the default route client (see AUTH_MANUAL, Service-Role Capability Boundary).
````

### E388 — F04b / FC-038 — 04_REFERENCE_MANUALS/DATABASE_MANUAL.md:426

Evidence: pinned candidate span; QA verdict §2 and repair prompt §1/§2.

Old:
````text
// Server-side: Service role bypasses RLS
````

New:
````text
// Construct only inside an independently authorized elevated operation, never as a default route client.
````

### E389 — F04b / FC-038 — 04_REFERENCE_MANUALS/DATABASE_MANUAL.md:431

Evidence: pinned candidate span; QA verdict §2 and repair prompt §1/§2.

Old:
````text
process.env.SUPABASE_SERVICE_ROLE_KEY! // Bypasses RLS
````

New:
````text
process.env.SUPABASE_SERVICE_ROLE_KEY! // Operation-local authorization is required before construction.
````

### E390 — F04c / FC-066 — 04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:613

Evidence: pinned candidate span; QA verdict §2 and repair prompt §1/§2.

Old:
````text
export const fetchProducts = async (): Promise<Product[]> => {
````

New:
````text
// Independent normalization-step example: fetchProducts() returns Promise<Product[]>.
// This array-returning step is not the typed-outcome service used by the route below.
export const fetchProducts = async (): Promise<Product[]> => {
````

### E391 — F04c / FC-066 — 04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:783

Evidence: pinned candidate span; QA verdict §2 and repair prompt §1/§2.

Old:
````text
### Graceful Degradation Pattern

````

New:
````text
### Graceful Degradation Pattern

This caller uses the §3 typed-outcome contract: `fetchProducts()` returns a discriminated outcome with `status` equal to `success`, `not-found`, `unavailable`, `invalid` or `forbidden`; only `success` carries `items: Product[]`. This example assumes a project-approved public-catalog failure policy permitting the generic empty-state UI on non-success; this is not an entitlement decision or a cached successful result. It does not call the independent array-returning normalization example.

````

### E392 — F04c / FC-066 — 04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:793

Evidence: pinned candidate span; QA verdict §2 and repair prompt §1/§2.

Old:
````text
  const { items: products, error } = await fetchProducts();

  // Graceful degradation: show empty state instead of crashing
  if (error || products.length === 0) {
````

New:
````text
  const outcome = await fetchProducts();

  // Apply the declared public-catalog failure policy; do not treat failure as success.
  if (outcome.status !== 'success' || outcome.items.length === 0) {
````

### E393 — F04c / FC-066 — 04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:809

Evidence: pinned candidate span; QA verdict §2 and repair prompt §1/§2.

Old:
````text
  return <ProductList products={products} />;
````

New:
````text
  return <ProductList products={outcome.items} />;
````

### E394 — F04c / FC-066 — 04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:852

Evidence: pinned candidate span; QA verdict §2 and repair prompt §1/§2.

Old:
````text
### ISR and Revalidation

````

New:
````text
### ISR and Revalidation

Independent ISR example: this `fetchProducts()` returns the endpoint’s raw JSON payload, with no normalization or typed-outcome envelope; it is not the §3 service or the caller above. The project must declare and validate that endpoint’s wire contract and failure/cache policy before implementation; this example only illustrates the revalidation option.

````

### E395 — F05 / RUL-13 — 04_REFERENCE_MANUALS/AUTH_MANUAL.md:1122

Evidence: pinned candidate span; QA verdict §2 and repair prompt §1/§2.

Old:
````text
2. **Don't store sensitive data in localStorage**
   - Accessible via JavaScript
   - Use secure cookies instead
````

New:
````text
2. **Don't store sensitive data in localStorage**
   - Accessible via JavaScript
   - Use secure cookies instead
   - No persistent raw contact information is stored in browser storage by default; any approved exception names the fields, purpose, retention period and owner, with clearing/invalidation behavior.
````

### E396 — F05 / RUL-13 — 03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:426

Evidence: pinned candidate span; QA verdict §2 and repair prompt §1/§2.

Old:
````text
expect(JSON.parse(stored!).state.couponCode).toBe(expectedCode); // approved non-sensitive project fixture only
```
````

New:
````text
expect(JSON.parse(stored!).state.couponCode).toBe(expectedCode); // approved non-sensitive project fixture only
```

No persistent raw contact information is stored in browser storage by default; any approved exception names the fields, purpose, retention period and owner, with clearing/invalidation behavior.
````

### E397 — F05 / RUL-13 — 04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:205

Evidence: pinned candidate span; QA verdict §2 and repair prompt §1/§2.

Old:
````text
Personal fields follow the approved account-transition and retention policy.
````

New:
````text
Personal fields follow the approved account-transition and retention policy in STATE_MANAGEMENT_MANUAL. No persistent raw contact information is stored in browser storage by default; any approved exception names the fields, purpose, retention period and owner, with clearing/invalidation behavior.
````

### E398 — HISTORY / F01–F05 — 02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:1602

Evidence: pinned candidate span; QA verdict §2 and repair prompt §1/§2.

Old:
````text
| 1.3 | 2026-10-18 | Factory DocSet sync: approved workflow/security/reference corrections; preserved original; explicit exclusions per doctrine-part2 map. IDs: FC-004, FC-005, FC-008, FC-014, FC-015, FC-017, FC-018, FC-027, MC-06, MC-07, RUL-01, RUL-05, RUL-09, RUL-12, W19, W23 |
````

New:
````text
| 1.3 | 2026-10-18 | Factory DocSet sync: approved workflow/security/reference corrections; preserved original; explicit exclusions per doctrine-part2 map. IDs: FC-004, FC-005, FC-008, FC-014, FC-015, FC-017, FC-018, FC-027, MC-06, MC-07, RUL-01, RUL-05, RUL-09, RUL-12, W19, W23; QA-P4 repair: F01–F05 (AC5/6/9/15/16/18) |
````

### E399 — CHANGELOG / F01–F05 — CHANGELOG.md:43

Evidence: pinned candidate span; QA verdict §2 and repair prompt §1/§2.

Old:
````text
| 2026-10-18 | ENGINEER_PLAYBOOK v1.3 | Factory DocSet sync; preserved outgoing original; MC correction pass | FC-004, FC-005, FC-008, FC-014, FC-015, FC-017, FC-018, FC-027, MC-06, MC-07, RUL-01, RUL-05, RUL-09, RUL-12, W19, W23 |
````

New:
````text
| 2026-10-18 | ENGINEER_PLAYBOOK v1.3 | Factory DocSet sync; preserved outgoing original; MC correction pass; QA-P4 repair: F01–F05 (AC5/6/9/15/16/18) | FC-004, FC-005, FC-008, FC-014, FC-015, FC-017, FC-018, FC-027, MC-06, MC-07, RUL-01, RUL-05, RUL-09, RUL-12, W19, W23 |
````

### E400 — HISTORY / F01–F05 — 03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:1655

Evidence: pinned candidate span; QA verdict §2 and repair prompt §1/§2.

Old:
````text
| 2.2 | 2026-10-18 | Factory DocSet sync: approved workflow/security/reference corrections; preserved original; explicit exclusions per doctrine-part2 map. IDs: DEC-03, FC-020, FC-021, FC-022, FC-023, FC-024, FC-030, FC-031, FC-040, FC-063, RUL-11, RUL-12, RUL-13 |
````

New:
````text
| 2.2 | 2026-10-18 | Factory DocSet sync: approved workflow/security/reference corrections; preserved original; explicit exclusions per doctrine-part2 map. IDs: DEC-03, FC-020, FC-021, FC-022, FC-023, FC-024, FC-030, FC-031, FC-040, FC-063, RUL-11, RUL-12, RUL-13; QA-P4 repair: F01–F05 (AC5/6/9/15/16/18) |
````

### E401 — CHANGELOG / F01–F05 — CHANGELOG.md:54

Evidence: pinned candidate span; QA verdict §2 and repair prompt §1/§2.

Old:
````text
| 2026-10-18 | TESTING_PLAYBOOK v2.2 | Factory DocSet sync; preserved outgoing original; MC correction pass | DEC-03, FC-020, FC-021, FC-022, FC-023, FC-024, FC-030, FC-031, FC-040, FC-063, RUL-11, RUL-12, RUL-13 |
````

New:
````text
| 2026-10-18 | TESTING_PLAYBOOK v2.2 | Factory DocSet sync; preserved outgoing original; MC correction pass; QA-P4 repair: F01–F05 (AC5/6/9/15/16/18) | DEC-03, FC-020, FC-021, FC-022, FC-023, FC-024, FC-030, FC-031, FC-040, FC-063, RUL-11, RUL-12, RUL-13 |
````

### E402 — HISTORY / F01–F05 — 04_REFERENCE_MANUALS/DATABASE_MANUAL.md:1161

Evidence: pinned candidate span; QA verdict §2 and repair prompt §1/§2.

Old:
````text
| 1.2 | 2026-10-18 | Factory DocSet sync: approved workflow/security/reference corrections; preserved original; explicit exclusions per doctrine-part2 map. IDs: FC-001, FC-003/096, FC-033, FC-034, FC-036, FC-037, FC-038, FC-039, FC-045, RUL-11 |
````

New:
````text
| 1.2 | 2026-10-18 | Factory DocSet sync: approved workflow/security/reference corrections; preserved original; explicit exclusions per doctrine-part2 map. IDs: FC-001, FC-003/096, FC-033, FC-034, FC-036, FC-037, FC-038, FC-039, FC-045, RUL-11; QA-P4 repair: F01–F05 (AC5/6/9/15/16/18) |
````

### E403 — CHANGELOG / F01–F05 — CHANGELOG.md:58

Evidence: pinned candidate span; QA verdict §2 and repair prompt §1/§2.

Old:
````text
| 2026-10-18 | DATABASE_MANUAL v1.2 | Factory DocSet sync; preserved outgoing original; MC correction pass | FC-001, FC-003/096, FC-033, FC-034, FC-036, FC-037, FC-038, FC-039, FC-045, RUL-11 |
````

New:
````text
| 2026-10-18 | DATABASE_MANUAL v1.2 | Factory DocSet sync; preserved outgoing original; MC correction pass; QA-P4 repair: F01–F05 (AC5/6/9/15/16/18) | FC-001, FC-003/096, FC-033, FC-034, FC-036, FC-037, FC-038, FC-039, FC-045, RUL-11 |
````

### E404 — HISTORY / F01–F05 — 04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:1206

Evidence: pinned candidate span; QA verdict §2 and repair prompt §1/§2.

Old:
````text
| 1.2 | 2026-10-18 | Factory DocSet sync: approved workflow/security/reference corrections; preserved original; explicit exclusions per doctrine-part2 map. IDs: FC-021, FC-056, FC-057, FC-058, FC-059, FC-061, FC-063, FC-064, FC-066, FC-070, RUL-11 |
````

New:
````text
| 1.2 | 2026-10-18 | Factory DocSet sync: approved workflow/security/reference corrections; preserved original; explicit exclusions per doctrine-part2 map. IDs: FC-021, FC-056, FC-057, FC-058, FC-059, FC-061, FC-063, FC-064, FC-066, FC-070, RUL-11; QA-P4 repair: F01–F05 (AC5/6/9/15/16/18) |
````

### E405 — CHANGELOG / F01–F05 — CHANGELOG.md:55

Evidence: pinned candidate span; QA verdict §2 and repair prompt §1/§2.

Old:
````text
| 2026-10-18 | API_AND_SERVICES_MANUAL v1.2 | Factory DocSet sync; preserved outgoing original; MC correction pass | FC-021, FC-056, FC-057, FC-058, FC-059, FC-061, FC-063, FC-064, FC-066, FC-070, RUL-11 |
````

New:
````text
| 2026-10-18 | API_AND_SERVICES_MANUAL v1.2 | Factory DocSet sync; preserved outgoing original; MC correction pass; QA-P4 repair: F01–F05 (AC5/6/9/15/16/18) | FC-021, FC-056, FC-057, FC-058, FC-059, FC-061, FC-063, FC-064, FC-066, FC-070, RUL-11 |
````

### E406 — HISTORY / F01–F05 — 04_REFERENCE_MANUALS/AUTH_MANUAL.md:1373

Evidence: pinned candidate span; QA verdict §2 and repair prompt §1/§2.

Old:
````text
| 1.5 | 2026-10-18 | Factory DocSet sync: approved workflow/security/reference corrections; preserved original; explicit exclusions per doctrine-part2 map. IDs: FC-001, FC-021, FC-033, FC-034, FC-035, FC-036, FC-038, FC-039, FC-041, FC-042, FC-043, FC-044, FC-063, FC-066, RUL-11 |
````

New:
````text
| 1.5 | 2026-10-18 | Factory DocSet sync: approved workflow/security/reference corrections; preserved original; explicit exclusions per doctrine-part2 map. IDs: FC-001, FC-021, FC-033, FC-034, FC-035, FC-036, FC-038, FC-039, FC-041, FC-042, FC-043, FC-044, FC-063, FC-066, RUL-11; QA-P4 repair: F01–F05 (AC5/6/9/15/16/18) |
````

### E407 — CHANGELOG / F01–F05 — CHANGELOG.md:57

Evidence: pinned candidate span; QA verdict §2 and repair prompt §1/§2.

Old:
````text
| 2026-10-18 | AUTH_MANUAL v1.5 | Factory DocSet sync; preserved outgoing original; MC correction pass | FC-001, FC-021, FC-033, FC-034, FC-035, FC-036, FC-038, FC-039, FC-041, FC-042, FC-043, FC-044, FC-063, FC-066, RUL-11 |
````

New:
````text
| 2026-10-18 | AUTH_MANUAL v1.5 | Factory DocSet sync; preserved outgoing original; MC correction pass; QA-P4 repair: F01–F05 (AC5/6/9/15/16/18) | FC-001, FC-021, FC-033, FC-034, FC-035, FC-036, FC-038, FC-039, FC-041, FC-042, FC-043, FC-044, FC-063, FC-066, RUL-11 |
````

### E408 — HISTORY / F01–F05 — 04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:563

Evidence: pinned candidate span; QA verdict §2 and repair prompt §1/§2.

Old:
````text
| 1.2 | 2026-10-18 | Factory DocSet sync: approved workflow/security/reference corrections; preserved original; explicit exclusions per doctrine-part2 map. IDs: FC-047, FC-050, FC-051, FC-052, FC-053, FC-054, FC-055, FC-059, FC-060, FC-062, FC-063, FC-067, FC-068, RUL-11 |
````

New:
````text
| 1.2 | 2026-10-18 | Factory DocSet sync: approved workflow/security/reference corrections; preserved original; explicit exclusions per doctrine-part2 map. IDs: FC-047, FC-050, FC-051, FC-052, FC-053, FC-054, FC-055, FC-059, FC-060, FC-062, FC-063, FC-067, FC-068, RUL-11; QA-P4 repair: F01–F05 (AC5/6/9/15/16/18) |
````

### E409 — CHANGELOG / F01–F05 — CHANGELOG.md:59

Evidence: pinned candidate span; QA verdict §2 and repair prompt §1/§2.

Old:
````text
| 2026-10-18 | ECOMMERCE_AND_PAYMENTS_MANUAL v1.2 | Factory DocSet sync; preserved outgoing original; MC correction pass | FC-047, FC-050, FC-051, FC-052, FC-053, FC-054, FC-055, FC-059, FC-060, FC-062, FC-063, FC-067, FC-068, RUL-11 |
````

New:
````text
| 2026-10-18 | ECOMMERCE_AND_PAYMENTS_MANUAL v1.2 | Factory DocSet sync; preserved outgoing original; MC correction pass; QA-P4 repair: F01–F05 (AC5/6/9/15/16/18) | FC-047, FC-050, FC-051, FC-052, FC-053, FC-054, FC-055, FC-059, FC-060, FC-062, FC-063, FC-067, FC-068, RUL-11 |
````
