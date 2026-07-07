# TESTING PLAYBOOK

> **Version:** 2.0
> **Date:** 2026-05-11
> **Author:** Architect (Claude) — synthesis of v1.0 (StarkReads, 2026-05-03) + Dockbloxx field notes (Blocks 2/3/4, May 8–11)
> **Origin:** Distilled from two production Next.js apps:
>
> - StarkReads (Subscription v1) — Supabase + Stripe, 136 tests across 3 layers
> - Dockbloxx (Headless WooCommerce) — REST + Stripe + Playwright, 182 tests across 4 layers
>   **Purpose:** Reusable recipe for adding a complete testing strategy to any Next.js application with **any** backend (SDK-mediated like Supabase, or REST-mediated like WooCommerce, or both)
>   **Prerequisite:** A working Next.js App Router app. Stripe, Supabase, and external REST APIs are all optional — the patterns adapt.

---

## How v2.0 differs from v1.0

v1.0 codified the four-layer testing strategy from a single Supabase + Stripe app (StarkReads). v2.0 generalizes those patterns to be **backend-agnostic** at the principle level, while preserving concrete implementations as appendix examples drawn from real apps.

New in v2.0:

- **Layered document architecture** — concise principles up top, deep appendices below.
- **REST-backend integration patterns** (fetch-mock) alongside SDK-mediated patterns (Supabase chain mock).
- **Stripe SDK mocking decision tree** — wrapper-mock vs constructor-mock based on the app's import pattern.
- **Fixture discovery** — test data sourced from the live backend per environment instead of hardcoded.
- **Diagnostic principles** — meta-principles for diagnosing test failures and avoiding false coverage.
- **Companion artifacts** — `CHANGELOG.md`, `SECURITY_FINDINGS.md`, `CLEANUP_BACKLOG.md` as standard project documents.

v1.0's specific patterns (Supabase chain mock, Stripe wrapper-mock, E2E user lifecycle, etc.) are preserved verbatim where they're correct; promoted to backend-agnostic principles where they generalize; supplemented with REST-equivalent patterns where they don't.

---

## Table of Contents

**Part 1 — Principles (quick reference)**

1. Four layers, not one
2. Write the cheapest test that catches the bug
3. Tests that pass for the wrong reason are worse than tests that fail
4. `retries: 0` is non-negotiable
5. Environment drift first
6. Source recon before test writing
7. Test data discovered, not declared
8. Defensive error message assertions for security-sensitive endpoints
9. Don't test features you're killing
10. Shadow implementations are false coverage

**Part 2 — The Four Layers**

- 2.1 Layer 1: Unit Tests (Jest)
- 2.2 Layer 2: Integration Tests (Jest)
- 2.3 Layer 3: E2E Tests (Playwright)
- 2.4 Layer 4: Manual Smoke Test

**Part 3 — Diagnostic Principles**

- 3.1 Environment drift first (the diagnostic order)
- 3.2 Tests that pass for the wrong reason (assertion specificity)
- 3.3 Source recon catches more than test plan mismatches
- 3.4 Audit-then-add when joining an existing project
- 3.5 Limits of seed-and-wait
- 3.6 Skip-and-document as a Factory pattern
- 3.7 The strict-vs-lenient validator pair pattern

**Part 4 — Backend Examples (deep appendix)**

- 4.1 Supabase-backed apps — chain mocks, RLS-aware testing
- 4.2 REST-backed apps — fetch mocks, header-based pagination, WooCommerce patterns
- 4.3 Stripe — wrapper-mock vs constructor-mock decision tree
- 4.4 Test data sourcing — discovered vs declared
- 4.5 E2E framework specifics — Playwright config, strict-mode, trace viewer
- 4.6 Testing in regulated environments (HIPAA / SOC2 / PCI / GDPR) — stub

**Part 5 — Companion Artifacts**

- 5.1 `CHANGELOG.md` — Keep a Changelog + SemVer discipline
- 5.2 `SECURITY_FINDINGS.md` — severity-graded discovery tracker
- 5.3 `CLEANUP_BACKLOG.md` — deferred technical debt tracker

**Part 6 — Gotchas & Generalizable Failure Modes**

**Appendix: Quick Reference Card**

---

# Part 1 — Principles

## Principle 1.1 — Four layers, not one

Every production app needs **four layers** of testing. Each layer catches what the others can't — unit tests are fast but can't test HTTP handlers; integration tests mock external services so they can't prove the real integration works; E2E tests run in a browser but can't automate third-party hosted pages; manual smoke covers the rest. **Each layer fills the blindspots of the others.**

| Layer       | Tool       | What It Proves                           | Speed        | Network?           |
| ----------- | ---------- | ---------------------------------------- | ------------ | ------------------ |
| Unit        | Jest       | Pure functions are correct               | ~3s for 100+ | No                 |
| Integration | Jest       | Route handlers orchestrate services      | <1s for 20+  | No (mocked)        |
| E2E         | Playwright | UI flows work in a real browser          | ~40s for 18+ | Yes (real backend) |
| Manual      | Human      | Real third-party integration round-trips | ~5 min       | Yes (real Stripe)  |

See Part 2 for layer-specific guidance.

## Principle 1.2 — Write the cheapest test that catches the bug

Unit tests are cheapest (fastest, no deps). Integration tests are medium (need mocks). E2E tests are expensive (need browser + running app + backend). Manual tests are most expensive (need a human). **Don't write an E2E test for something a unit test can catch. Don't mock what you can test purely.** Reach for the lowest-cost layer that actually verifies the claim.

## Principle 1.3 — Tests that pass for the wrong reason are worse than tests that fail

Prefer assertions that are **impossible to satisfy by accident.** A test that fails sends a clear signal — something is broken, investigate. A test that passes for the wrong reason sends a fraudulent signal: claims coverage that doesn't exist, hides the moment when the real claim broke. Targeted selectors (`getByRole`, distinctive regex, `data-testid`) beat full-page text searches. Setup dependencies must be enforced in the test body, not assumed.

See Section 3.2 for the diagnostic story behind this principle.

## Principle 1.4 — `retries: 0` is non-negotiable

Flaky tests **are bugs**, not inconveniences. The moment you set `retries: 1`, you create a class of bugs that hide forever — the ones that fail 50% of the time. Two failures in a row = retry passes = green CI = silent regression. When a test flakes, fix the root cause (or skip with documentation, per Section 3.6); never paper over with a retry budget.

## Principle 1.5 — Environment drift first

When debugging E2E flakes that don't reproduce in production, **check for environment drift before diagnosing test or code issues.** Dev environments accumulate scripts, debug tooling, and config overrides that prod doesn't have — any of them can break tests for reasons unrelated to the code under test. Environment-side fixes are usually one line; test-side workarounds compound.

See Section 3.1 for the full diagnostic order.

## Principle 1.6 — Source recon before test writing

Always read the source before writing the test. Match the real signature, validation behavior, and error shape — skipping recon costs 5–10 minutes per shape mismatch. Recon also surfaces issues beyond the test plan (security concerns, dead code, undocumented branches) that belong in tracker docs, not absorbed into the test.

See Section 3.3 for the full case study.

## Principle 1.7 — Test data discovered, not declared

When testing against a real backend, hardcoded record references (specific product IDs, coupon codes, category slugs) create brittle coupling between test logic and dataset state. A **discovery script** connects to whichever backend is configured in `.env.local`, pulls live records (the first published product, a populated category, a valid coupon), merges them with static fixtures, and writes a JSON file all E2E tests read at module top. Tests reference _roles_ (the populated category) rather than _records_ (`accessories-id-7`).

See Section 4.4 for the implementation.

## Principle 1.8 — Defensive error message assertions for security-sensitive endpoints

For routes handling money, identity, or PII, the catch-block test asserts two things: the expected user-facing error IS present, and the internal/upstream error is NOT. This catches a class of security regressions where someone "improves" error messages by including the original and accidentally leaks card digits, customer emails, or internal request IDs.

See Section 4.3 for the implementation pattern. `SECURITY_FINDINGS.md` tracks real-world examples.

## Principle 1.9 — Don't test features you're killing

When deprecated code stays in the codebase for deferred-removal reasons, do NOT write tests to lock in its behavior. Tests have maintenance cost; protecting regressions in features you don't care about is **negative ROI.** Document the decision in `CLEANUP_BACKLOG.md`, and test the shape of related output if other consumers depend on it — but skip feature-specific content assertions.

## Principle 1.10 — Shadow implementations are false coverage

When tests are hard to write against the real code, the common shortcut is to copy the logic into the test file and test the copy. The copy diverges; tests stay green; **coverage is illusion.** Extract the testable logic into a shared lib that BOTH the route and tests import — detection heuristic: a test-file function whose name matches a source function is a strong smell.

See Section 3.4 for detection + Section 2.2 for the fix pattern.

---

# Part 2 — The Four Layers

## 2.1 Layer 1: Unit Tests (Jest)

### What to unit test

Pure functions with no side effects, no async, no external dependencies. If a function takes inputs and returns outputs without touching the network, database, or filesystem — unit test it.

Typical targets (backend-agnostic):

| Function type                                                    | What to assert                                                    | Why                                     |
| ---------------------------------------------------------------- | ----------------------------------------------------------------- | --------------------------------------- |
| Tier/permission hierarchy (`meetsTier`)                          | All N×N combinations of the matrix                                | Cumulative gates are easy to get wrong  |
| Validation functions (`safeRedirect`, `validateCoupon`)          | Each rule fires when violated; each rule passes when not violated | Validation is the first line of defense |
| Mapping/resolution (`resolveTierFromPriceId`, `parseCouponMeta`) | Known inputs → expected outputs; unknown input → safe default     | Lookup tables drift                     |
| Formatters/cleaners (`cleanPriceHtml`, `formatDateString`)       | Happy path + edge cases (null, empty, malformed input)            | Cosmetic functions are bug magnets      |

### Example pattern: validation function with multiple rules

```typescript
describe("safeRedirect", () => {
  it("accepts valid internal paths", () => {
    expect(safeRedirect("/pricing")).toBe("/pricing");
    expect(safeRedirect("/members-portal/pro")).toBe("/members-portal/pro");
  });

  it("returns null for null, undefined, and empty string", () => {
    expect(safeRedirect(null)).toBeNull();
    expect(safeRedirect(undefined)).toBeNull();
    expect(safeRedirect("")).toBeNull();
  });

  it("rejects protocol-relative URLs", () => {
    expect(safeRedirect("//evil.com")).toBeNull();
  });

  it("rejects schemed URLs", () => {
    expect(safeRedirect("https://evil.com")).toBeNull();
    expect(safeRedirect("javascript:alert(1)")).toBeNull();
  });
});
```

Pattern: one `describe` per function, one `it`/`test` per rule. Names describe the rule, not the implementation.

### The strict-vs-lenient validator pair pattern

When a feature needs both **rigid validation** (one path) and **permissive validation** (another path), build two validators with a shared core rather than parameterizing one function with a "skip these rules" flag.

Concrete example from Dockbloxx:

- `validateCoupon` — strict path, runs at checkout. All rules fire: email required, zip required, allow-list checked, expiry checked, etc.
- `validateCouponForDealer` — lenient path, runs on dealer landing page. Skips email/zip/allow-list/per-user-limit (data isn't available yet); keeps the remaining rules (expiry, min/max spend, products, etc.).

Both call a shared private helper (`validateCouponSharedRules`) with the common rules. The two exported validators add their own rule sets around the shared core.

**Test the two validators through their public API, not the private helper.** This:

- Avoids exporting internals just for tests.
- Naturally exercises the shared rules via both paths.
- Makes the test pairing pattern explicit: every skip-list test in the lenient block is paired with a rule-firing test in the same block. Together they prove BOTH "the lenient path skips what it should" AND "the lenient path still fires what it shouldn't skip."

See Section 3.7 for the detailed treatment of this pattern.

### Shadow-implementation smell detection

Before writing new unit tests in an existing file, scan for shadow implementations — local function definitions in the test file that mimic source functions. Detection grep patterns:

```bash
# Find test-file functions whose names appear in source.
grep -rn "^function build" tests/ src/
grep -rn "// mimics\|// same as\|// copy of" tests/
```

If found, the right move is **not** to add more tests around the shadow — it's to extract the logic to a lib both source and tests import (Section 3.4).

### File location convention

Two valid conventions, pick one and stick with it:

- **`tests/` at project root** — Dockbloxx convention. Tests live outside `src/`. Easier when E2E also lives at root (`e2e/`).
- **`src/__tests__/`** — v1.0 / StarkReads convention. Tests colocate with source under `src/`. Requires `roots: ['<rootDir>/src']` in Jest config to exclude `e2e/`.

Either works. Switching from one to the other is mechanical. What matters is **consistency within a project** and matching `jest.config.js` to the choice.

---

## 2.2 Layer 2: Integration Tests (Jest)

### What to integration test

API route handlers — the server-side functions that orchestrate external services (Supabase, Stripe, REST APIs). These tests mock all external dependencies and verify the orchestration logic: "given this input and these mock responses, does the route produce the correct output and make the correct calls?"

### The 4-canonical-test shape per route

Every route handler integration test file should cover four behavior categories:

1. **Happy path** — upstream returns ok + valid body. Assert response status + body shape, and **assert what arguments/URL the route passed to the upstream** (catches "right response, wrong call" regressions).
2. **Upstream not-ok** — upstream returns ok:false (404, 5xx). Assert route's mapped status code + error body shape.
3. **Validation rejection** — required input missing. Assert 400 + error body. **Critically: assert the upstream was NOT called** — invalid input should never hit the external service.
4. **Upstream throw** — `mockRejectedValueOnce(new Error(...))`. Assert route returns 500 + **generic** error message that does NOT leak the upstream error text (defensive assertion — see Principle 1.8).

This 4-test minimum catches the four behavior categories at any service boundary: success, expected-failure, input-rejection, unexpected-failure.

### Backend-agnostic mocking — what to mock at which boundary

The cleanest mock target depends on how the route talks to the upstream:

| Route imports...                             | Mock target                                      | See  |
| -------------------------------------------- | ------------------------------------------------ | ---- |
| Project wrapper (`@/lib/stripe/stripe`)      | The wrapper module                               | §4.3 |
| SDK directly (`import Stripe from "stripe"`) | The SDK package itself                           | §4.3 |
| Native fetch (`await fetch(...)`)            | `global.fetch`                                   | §4.2 |
| Supabase client                              | The chain (`from().select().eq().maybeSingle()`) | §4.1 |

**Mock at the cleanest boundary, not the deepest one.** Mocking deeper than necessary means more setup, more brittleness, more "passes for the wrong reason" risk.

### The `@jest-environment node` docblock

Next.js's `next/server` import (used by route handlers for `NextResponse`) requires global `Request` and `Response` constructors at module-load time. Jest's default `jsdom` environment doesn't provide them — first run of any route-handler test fails with `ReferenceError: Request is not defined`.

Fix is one line at the top of the test file:

```ts
/**
 * @jest-environment node
 */
```

Node 18+ provides Request/Response globally. Per-file override is the right granularity — your React component tests still run in jsdom (correct for their needs); only route-handler tests need node env.

### File location convention

```
tests/api/                              ← integration tests target this
├── checkout.test.ts
├── webhook.test.ts
├── place-order.test.ts
└── create-payment-intent.test.ts
```

Plus an npm script that targets the directory:

```json
"test:integration": "jest tests/api --testPathPatterns=tests/api"
```

The positional `tests/api` is a path filter; `--testPathPatterns=tests/api` is the regex pattern. Both narrow Jest's discovery to the integration suite. Belt-and-suspenders.

### Single jest.config.js — no premature split

One Jest config for both unit and integration. Run all together with `npm test`; run integration-only with `npm run test:integration`. Splitting configs is premature optimization until the suite is slow enough to matter (Dockbloxx runs 166 tests in ~3s with one config).

---

## 2.3 Layer 3: E2E Tests (Playwright)

### What to E2E test

User-facing flows that span multiple pages, require browser interaction (form fills, clicks, navigation), and verify that the full stack works together. E2E tests are the closest thing to a real user.

### Minimum-viable `playwright.config.ts`

```ts
import { defineConfig } from "@playwright/test";

export default defineConfig({
  testDir: "./e2e",
  timeout: 30000,
  retries: 0, // Principle 1.4 — non-negotiable
  use: {
    baseURL: "http://localhost:3000",
    trace: "on-first-retry",
  },
  projects: [{ name: "chromium", use: { browserName: "chromium" } }],
  webServer: {
    command: "npm run dev",
    url: "http://localhost:3000",
    reuseExistingServer: true, // critical for local iteration speed
    timeout: 120000,
  },
});
```

Three knobs that matter most:

- **`retries: 0`** — flaky tests are bugs, not inconveniences.
- **`reuseExistingServer: true`** — if `npm run dev` is already running, Playwright uses it (massive speedup during local iteration). Otherwise it spawns one.
- **`webServer.command`** — auto-starts dev server if not running.

### Two-runner shell wrappers

```bash
scripts/run_e2e_tests_headless.sh    # CI / verification mode
scripts/run_e2e_tests_ui.sh          # Local development / debugging
```

Both wrap the corresponding `npm run test:e2e[:ui]` script. Same tests, same code, two runners. Headless for verification (fast, scriptable, no GUI). UI mode for debugging (time-travel, DOM inspection, see what the test sees).

All shell wrappers in `scripts/` must `cd` to project root:

```bash
#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
npm run test:e2e
```

Without the `cd`, running `./run_e2e_tests_headless.sh` from inside `scripts/` causes commands like `playwright test` to look in the wrong directory.

### Module-top fixture loading

Load fixtures **once at module top**, not per test:

```ts
const FIXTURES_DIR = path.join(__dirname, "fixtures");
const liveData = JSON.parse(
  fs.readFileSync(path.join(FIXTURES_DIR, "live-data.json"), "utf-8"),
);
const dealersData = JSON.parse(
  fs.readFileSync(path.join(FIXTURES_DIR, "dealers.json"), "utf-8"),
);

test.describe("Some flow", () => {
  test("...", async ({ page }) => {
    // use liveData / dealersData
  });
});
```

Two reasons:

1. **Performance** — no per-test filesystem cost.
2. **Fail-fast** — if a fixture file is missing or malformed, the spec fails at import time with a clear stack trace pointing at the JSON file. Tests don't even start.

### Test data discovery vs declaration

Hardcoded fixture data ages badly. The recommended pattern is a **discovery script** that fetches live data from the configured backend and writes it to a gitignored JSON file. Tests then reference _roles_ (the populated category, the first published product) rather than _records_ (specific IDs).

```
e2e/fixtures/
├── dealers.json         (static, committed — stable knowns the script can't infer)
└── live-data.json       (gitignored, regenerated by `npm run fixtures:fetch`)
```

See Section 4.4 for the full pattern.

### localStorage + UI dual-verification

For tests touching persistent client state (Zustand, Redux with localStorage, IndexedDB), assert against **both** the source of truth AND the UI:

```ts
await expect(page.getByText(/Coupon Applied:/)).toBeVisible(); // user-facing claim

const stored = await page.evaluate(() =>
  localStorage.getItem("checkout-storage"),
);
expect(JSON.parse(stored!).state.checkoutData.coupon.code).toBe(expectedCode); // ground truth
```

The UI proves the user sees the right thing. The persistent state proves the system actually did the right thing. UIs can lie (e.g., showing optimistic state that doesn't match the store).

### Playwright `getByText` strict-mode awareness

When multiple legitimate elements share text (very common), `getByText(/SomePattern/)` matches all of them and the assertion fails with "strict mode violation: resolved to N elements."

Three handling options, ranked best to worst:

1. **Best — assert each variant separately.** If both elements are real signals, name them both:

   ```ts
   await expect(page.getByText(/Coupon Applied \(\w+\):/i)).toBeVisible(); // order summary
   await expect(page.getByText(/Coupon Applied:\s*\w+/i)).toBeVisible(); // applied-state UI
   ```

   Stronger test — catches regressions in either component.

2. **Acceptable — narrow the regex** so it matches exactly one element. Works when one variant is distinctive enough.

3. **Last resort — `.first()`.** Hides the multiplicity rather than acknowledging it. A future engineer reading `.first()` won't know whether it was thoughtful (one of N is enough) or sloppy (just made the error go away).

### Stripe boundary stop pattern

E2E coverage of Stripe checkout ends at the Stripe boundary. Beyond that point, Stripe's hosted UI is out of scope (their DOM changes frequently, breaking selectors). The pattern:

```ts
test("submit checkout reaches Stripe boundary", async ({ page }) => {
  // ... fill checkout form ...
  await page.getByRole("button", { name: /place order/i }).click();

  // Wait for either Stripe-domain navigation OR a Stripe Elements iframe.
  await Promise.race([
    page.waitForURL(
      /checkout\.stripe\.com|hooks\.stripe\.com|js\.stripe\.com/,
      { timeout: 15000 },
    ),
    page.waitForSelector('iframe[src*="stripe"]', { timeout: 15000 }),
  ]);
  // End test here. Don't try to fill Stripe's form.
});
```

The real Stripe round-trip is covered by manual smoke (§2.4) and the integration layer (§4.3).

### File location convention

```
e2e/
├── helpers/                       (when patterns stabilize across specs)
├── fixtures/
│   ├── dealers.json               (committed)
│   └── live-data.json             (gitignored)
├── flow-1.spec.ts
├── flow-2.spec.ts
└── ...
```

E2E tests live **outside `src/`** and outside `tests/` (which is for Jest). Three separate roots: `src/` (source), `tests/` (Jest), `e2e/` (Playwright). Avoid Jest/Playwright collision (see §6).

### When to extract helpers

**Inline first.** Three tests with identical setup duplicated inline beats premature DRY. When you find yourself writing the same 20-line setup for the fourth time, extract to `e2e/helpers/`. Premature helper extraction obscures what each test actually does.

---

## 2.4 Layer 4: Manual Smoke Test

### When no automation can replace a human

Some flows cross into territory that's technically automatable but practically too brittle:

- Stripe Checkout (hosted page, frequent DOM changes)
- OAuth flows (third-party login pages)
- Real webhook round-trips (need external trigger + propagation time)
- Real email delivery
- Real SMS / push notifications

The manual smoke test covers these. Run before every production deploy. Takes ~5–10 minutes.

### Template — adapt per app

```markdown
# Manual Smoke Test — [App Name]

Run before every production push. Approximately 5–10 minutes.

## Why this exists

E2E tests stop at the [Stripe / OAuth / webhook] boundary. Integration
tests cover the [external-service-talking] route handlers with mocked
SDK. This checklist covers the gap: real [service] sandbox, real
[round-trip], the things only a human can verify.

## Payment Flow (or auth flow, or...)

- [ ] Add product to cart
- [ ] Go to /checkout, fill billing/shipping
- [ ] Apply a coupon (verify discount appears)
- [ ] Submit order
- [ ] On Stripe page, use test card `4242 4242 4242 4242`
- [ ] Confirm redirect to /thankyou
- [ ] Verify order in [backend] admin: status correct
- [ ] Verify [Stripe / webhook / event] log shows expected event

## [Feature]-Specific Flow (CONDITIONAL)

- [ ] Check if [feature flag / external script / config] is active
- [ ] If ACTIVE: walk through the user path, assert end-state
- [ ] If NOT ACTIVE: skip this section

## Regression Spot-Check

- [ ] [Surface 1] renders
- [ ] [Surface 2] works
- [ ] [Surface 3] doesn't error
```

### Why the conditional sections matter

Feature plumbing that's currently dormant (e.g., a deprecated attribution integration) should still appear in manual smoke with a **conditional check** at the top: "is this feature live right now?" If yes, do the full walk-through. If no, skip. Keeps the checklist useful as features come and go without rewrites.

---

# Part 3 — Diagnostic Principles

Meta-principles for diagnosing test failures and avoiding false coverage. Lessons from the field, not framework rules.

## 3.1 Environment drift first

When debugging E2E flakes that don't reproduce in production, **check for environment drift before diagnosing test or code issues.**

### The diagnostic order

1. **Is this script / config / dependency present in production?**
2. If not — align dev with prod (remove the dev-only thing) BEFORE writing test-side workarounds.
3. Only after the environments match should you investigate test code, app code, or framework behavior.

### Why this matters

Test-side workarounds for environment-drift problems compound. Each new spec needs the same workaround. Workarounds drift across specs as they're copy-pasted. Over time the test suite becomes a mirror of "things we did to fight dev-only weirdness" rather than "things that prove the app works."

The fix is almost always cheaper at the environment layer:

- Empty an ACF / CMS feature flag field
- Remove a dev-only `<script>` tag
- Strip a debug query-param injector
- Disable a mock service worker that prod doesn't have

vs. the test-side workaround:

- Pre-seed sessionStorage in every test
- Add `page.route` aborts to a fixture
- Override `history.replaceState` in setup scripts
- Introduce timing-based waits that assume the workaround landed

### Real-world case (Dockbloxx)

Spent several hours diagnosing a "race condition" in Playwright clicks. The race was real — third-party script `history.replaceState` was clobbering Link navigations. But the script only existed on dev (someone had populated a WordPress ACF field for a one-off integration that never shipped to prod). Empty the field, drift gone, tests pass. The right first question would have been "is this script even running in prod?" — one-line check; would have saved the entire debugging session.

## 3.2 Tests that pass for the wrong reason

A test that **fails** sends a clear signal: something is broken, investigate. A test that **passes for the wrong reason** sends a fraudulent signal: claims coverage that doesn't exist, hides the moment when the real claim broke.

### The diagnostic signature

The signature of a "passes for the wrong reason" test is that it **starts failing after an unrelated change.** Example from Dockbloxx:

A test asserted `page.locator("body").toContainText("aham10")` to verify a coupon code appeared on `/checkout`. The test passed for weeks. Then a third-party script was removed from dev (Section 3.1) — unrelated to the coupon flow. The test started failing.

Investigation revealed: `/checkout` silently redirects to `/shop` when the cart is empty. The test never seeded a product. The redirect happens client-side after a brief render — so the checkout body IS visible for a small window before being replaced. `body.toContainText` was racing the redirect, sometimes catching the brief render, sometimes not. The third-party script had added enough page-load latency to widen the catching window. With the script gone, the redirect won the race and the test failed honestly.

**The test was never correct.** It coincidentally passed because of unrelated timing.

### Three corollaries

1. **Targeted selectors > full-page text searches.** When asserting that a UI element rendered, name the element: `getByRole`, `getByText` with a distinctive regex, `data-testid`. Avoid `body.toContainText` unless you genuinely don't care which element holds the text.

2. **Setup dependencies must be enforced in the test body, not assumed.** If `/checkout` requires a non-empty cart, the test must seed the cart. Don't assume environment quirks (cached state, slow scripts, prior-test pollution) will provide the precondition.

3. **Tests that pass on retry but fail on first run** are a special case of this. The retry hid an accidental-pass condition that the first run revealed. Don't paper over with `retries: 1` (Principle 1.4).

### How to detect them proactively

Grep test files for "confession language" — comments where the author admits the test doesn't fully verify the claim:

- `// depends on ...`
- `// note that ...`
- `// verifies X, not Y`
- `// however ...`

If a test needed a paragraph to explain what it doesn't cover, it's probably weak by design.

## 3.3 Source recon catches more than test plan mismatches

When writing integration tests for security-sensitive endpoints (payment, auth, PII handlers), the source recon phase should explicitly look for:

1. **Error handling patterns** — what gets logged vs what gets returned. Look for `{ message: error.message }` patterns or anything that passes through upstream errors verbatim.
2. **Input validation gaps** — what's destructured vs what's validated. If `const { x, y, z } = await request.json()` is followed immediately by use of those values without a schema check, that's a finding.
3. **Implicit trust assumptions** — does the route trust the caller? Trust the upstream service? Where does the trust boundary live, and does the code enforce it?

### Where findings should land

Findings discovered during recon belong in a dedicated `SECURITY_FINDINGS.md`, **NOT** quietly absorbed into the test code as "test it as-is." The recon phase is a security audit opportunity; treating findings as test scope creep would silently bake the vulnerabilities into the test suite (e.g., "Test 4: assert the leak happens" is a regression test FOR a bug, not a fix).

The right pattern:

- **HIGH-severity findings** — fix inline in the same session (small, contained source change + test that locks in the fix).
- **MEDIUM / LOW findings** — document in `SECURITY_FINDINGS.md` with severity, recommended fix, and mitigation-until-fix.
- **Tests assert the CORRECT post-fix behavior** (defensive assertions), not the buggy pre-fix state.

### Real-world case (Dockbloxx, Block 4)

Source recon on `/api/create-payment-intent` revealed:

1. **SDK-direct import (no wrapper)** — changed the mocking approach. Test plan adjusted.
2. **Multi-step customer flow** (list customers → maybe create → PaymentIntent) — added two more tests for the branch coverage.
3. **Error message leak in catch block** — HIGH-severity finding, fixed inline (`{ message: error.message }` → generic message + server-side logging).
4. **No input validation** — MEDIUM-severity finding, documented as open item in `SECURITY_FINDINGS.md` Finding #2.

Two of those were test-plan adjustments. **Two were production security issues that recon happened to surface.** Without recon, both would have shipped untested.

## 3.4 Audit-then-add when joining an existing project

Before writing new tests in an existing test file, **audit what's already there.** The audit catches:

- **Shadow implementations** — local function in the test file that mimics a source function (Principle 1.10).
- **Drifted fixtures** — fixtures that no longer match the source's expected shape.
- **Weak assertions** — tests that pass via accidental conditions (Section 3.2).
- **Duplicate test files** — same function tested in two places, one will rot.
- **Skipped tests with no documentation** — `.skip` without explanation; either the reason is forgotten or the test is dead.

The audit costs ~30 minutes per test file. Saves hours of debugging when the new tests interact weirdly with old ones, or when an "obvious" assertion fails because the old code did something the audit would have surfaced.

### Audit checklist

```
□ Read the full test file
□ Read the full source file it tests
□ Grep for shadow-implementation smell (function-name match between test and source)
□ Check fixture factories — do they match current types?
□ Check assertion style — distinctive selectors, or generic text searches?
□ Note any .skip tests + their documentation status
□ Note any duplicate test names across the suite
□ Flag findings to SECURITY_FINDINGS.md or CLEANUP_BACKLOG.md as appropriate
```

## 3.5 Limits of seed-and-wait

When a third-party script mutates client-side state on page load, the seed-and-wait pattern controls **inputs and timing** but not **DOM side effects.**

- **Pre-seeding storage** controls a third-party script's _inputs._ (E.g., set `sessionStorage.utm_source` so the script uses your test value, not its "direct/(none)" fallback.)
- **Waiting for a deterministic signal** proves the script has _run._ (E.g., wait for the seeded UTM to appear in the URL after the script's `replaceState`.)
- **Neither addresses the script's DOM side effects.** If the script re-renders or re-routes during/after its work, click interactivity may remain broken regardless of seed/wait.

### Decision tree

```
Third-party script mutating page state during E2E?
│
├── Is the script ALSO present in production?
│   │
│   ├── No → Environment drift. Remove from dev. (Section 3.1)
│   │
│   └── Yes → Continue down the tree.
│
├── Does the script have DOM side effects beyond URL/storage writes?
│   │
│   ├── No → seed-and-wait works. Pattern:
│   │        seed → goto → waitForURL(deterministic-signal) → click → assert
│   │
│   └── Yes → seed-and-wait won't fully work. Consider:
│             (a) page.route to abort the script's network request
│             (b) addInitScript to neutralize history.replaceState etc.
│             (c) skip-and-document (Section 3.6) until architectural fix
```

## 3.6 Skip-and-document as a Factory pattern

When a test can't be made reliable due to an architectural issue outside the test layer, use `test.skip` with a deliberate comment block. The skip isn't a hack — it's a documented coverage decision.

### The comment block carries five things

1. **Why skipped** — the specific failure modes observed.
2. **What was tried** — including the things that didn't work.
3. **Real-user impact assessment** — "real users don't reliably hit this" is the load-bearing claim that justifies the skip.
4. **Investigation paths** — concrete options for the next person.
5. **Coverage mitigation** — what else covers the same surface.

### Example shape

```ts
/**
 * SKIPPED: [one-line reason — include in test name too]
 *
 * Failure mode: [what happens when this runs]
 * What was tried: [list options attempted]
 * Real-user impact: [why this doesn't hit production]
 * Investigation paths:
 *   - [option A — architectural fix]
 *   - [option B — different approach]
 * Coverage mitigation: [what else exercises this surface]
 */
test.skip("clicking [X] does [Y] (skipped: [one-line reason])", async ({
  page,
}) => {
  /* full body preserved — runnable when investigation resolves */
});
```

### Why this is better than deleting the test

The test body is **preserved verbatim** under `test.skip(...)`. When the architectural fix lands, swap `test.skip` → `test`, and you have a working regression test ready to go. The investment in writing the test isn't lost — just deferred.

The test name itself encodes the skip reason. Even without reading the comment, anyone running the suite sees `(skipped: [reason])` next to the test ID.

### Companion: mitigation test that exercises the same surface via a different path

When skipping a click-flow test, add a **direct-navigation companion** that hits the destination URL directly:

```ts
test("[destination page] renders when navigated to directly", async ({
  page,
}) => {
  await page.goto(`/path/to/destination`);
  await expect(page.getByRole("button", { name: /key cta/i })).toBeVisible();
});
```

This doesn't prove the click works, but it proves the destination is correct. Manual smoke fills the seam (the click flow itself).

## 3.7 The strict-vs-lenient validator pair pattern

When a feature needs two validation paths — a rigid one (full rules) and a permissive one (subset of rules) — build two validators with a shared private helper.

### Anti-pattern: one validator with a flag

```ts
// DON'T do this
validateCoupon(coupon, checkoutData, { isDealer: true });
```

Problems:

- The flag invites every future rule to gain a "skip in dealer mode?" decision.
- Test names become awkward: "validates X in non-dealer mode", "validates X in dealer mode" — every rule duplicates.
- Adding a new mode (e.g., admin override) doubles the matrix again.

### Pattern: two validators + shared core

```ts
// shared helper (private to lib)
function validateCouponSharedRules(coupon, data, meta) {
  // rules 2-5 — the rules both paths run
}

export function validateCoupon(coupon, data) {
  // rules 0, 0.1, 1 (gate rules)
  const sharedResult = validateCouponSharedRules(coupon, data, meta);
  if (!sharedResult.isValid) return sharedResult;
  // rule 6 (per-user usage limit — needs userEmail)
}

export function validateCouponForDealer(coupon, data) {
  const meta = parseCouponMeta(coupon);
  return validateCouponSharedRules(coupon, data, meta);
}
```

### Test pairing pattern

For the lenient validator, every test falls into one of three categories:

1. **Skip-list proofs** — "passes when X is invalid" (proves rule X is skipped in lenient mode).
2. **Rule-firing proofs** — "rejects when Y is invalid" (proves rule Y still fires in lenient mode).
3. **Happy path** — "returns isValid:true for a clean valid input."

Every skip-list proof in the lenient block should be paired with a rule-firing proof in the strict block (which exercises the gate rules the lenient mode skips). Together they prove BOTH:

- The lenient path skips what it should.
- The strict path still fires what the lenient path skips.

### Why this generalizes

This pattern appears in:

- **Permission systems** — strict (full ACL) vs admin-override (skip some checks).
- **Feature flag rollouts** — strict (full validation) vs early-access (relaxed for beta testers).
- **Multi-tenant apps** — strict (tenant-scoped) vs cross-tenant admin (global).
- **API versions** — v2 (strict) vs v1 (legacy permissive).

In every case, "one function with a flag" is the wrong shape. Two functions with a shared core is the right shape.

---

# Part 4 — Backend Examples

The principles above are backend-agnostic. This part shows real implementations for each backend pattern.

## 4.1 Supabase-backed apps (StarkReads example)

### The Supabase chain mock pattern

Supabase client uses method chaining: `supabase.from('x').select('y').eq('z', v).maybeSingle()`. Each method returns a new object with the next method. Mocking this chain requires nested `jest.fn()` returns.

```typescript
// For SELECT chains: from().select().eq().maybeSingle()
const maybeSingle = jest.fn().mockResolvedValue({ data: row });
const eq = jest.fn(() => ({ maybeSingle }));
const select = jest.fn(() => ({ eq }));
const from = jest.fn(() => ({ select }));

// For UPSERT: from().upsert()
const upsert = jest.fn().mockResolvedValue({ error: null });
const from = jest.fn(() => ({ upsert }));

// For UPDATE chains: from().update().eq()
const eqAfterUpdate = jest.fn().mockResolvedValue({ error: null });
const update = jest.fn(() => ({ eq: eqAfterUpdate }));
const from = jest.fn(() => ({ update }));

// Wire into the mock client
createClientMock.mockReturnValue({ from } as any);
```

### The `as any` cast

Constructing fully-typed mocks of Supabase response shapes is prohibitively verbose. Use `as any` for mock-shape casts in tests. This is a pragmatic trade-off: marginal type safety loss vs significant code reduction. Standard practice in every TypeScript test suite that mocks complex external APIs.

### E2E user lifecycle (Supabase apps)

```
uniqueEmail()
→ "test-1714768800000-x4q2@e2e.test"
        │
        ▼
registerUser(page, email)
→ fills /auth Register tab → clicks Signup
→ waits for /members-portal redirect
        │
        ▼
getUserId(email)
→ supabaseAdmin.auth.admin.listUsers() → find by email → UUID
        │
        ▼
seedSubscription(userId, tier)
→ UPSERT into subscriptions table with synthetic Stripe IDs
        │
        ▼
TEST RUNS
        │
        ▼
deleteTestUser(email) [afterAll]
1. DELETE from subscriptions (FK first)
2. DELETE from user_roles
3. supabaseAdmin.auth.admin.deleteUser
```

### Direct DB seeding to bypass Stripe in E2E

E2E tests need users with specific subscription tiers. Automating Stripe Checkout in a browser is brittle (Stripe changes their DOM). Solution: insert subscription rows directly into Supabase via the admin client, as if the webhook had already fired.

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

Synthetic Stripe IDs (`cus_test_*`, `sub_test_*`) work because the gating logic only reads `tier` and `status` from the row — it never calls the Stripe API to verify the subscription ID.

**Trade-off:** E2E doesn't cover the actual Stripe round-trip. That's what integration tests (mocked) validate at the route level, and what manual smoke tests validate end-to-end. Each layer covers what it's good at.

### Supabase admin client in E2E helpers

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

The `dotenv` import is required because Playwright runs in its own Node process, not inside Next.js. Without it, env vars from `.env.local` aren't available to the helpers.

---

## 4.2 REST-backed apps (Dockbloxx / WooCommerce example)

### The fetch-mock pattern

When a route uses native `fetch` to talk to an external REST API, the cleanest mock surface is `global.fetch`:

```ts
function mockOkResponse(body: unknown, headers: Record<string, string> = {}) {
  return {
    ok: true,
    status: 200,
    json: () => Promise.resolve(body),
    headers: new Headers(headers),
  } as unknown as Response;
}

function mockNotOkResponse(status: number) {
  return {
    ok: false,
    status,
    json: () => Promise.resolve({}),
    headers: new Headers(),
  } as unknown as Response;
}

describe("GET /api/some-route", () => {
  const originalFetch = global.fetch;

  beforeEach(() => {
    global.fetch = jest.fn();
  });
  afterEach(() => {
    global.fetch = originalFetch;
    jest.resetAllMocks();
  });

  test("happy path", async () => {
    (global.fetch as jest.Mock).mockResolvedValueOnce(mockOkResponse(payload));
    const response = await GET(request);
    // assertions
  });

  test("upstream throws", async () => {
    (global.fetch as jest.Mock).mockRejectedValueOnce(
      new Error("network failure"),
    );
    // assertions
  });
});
```

### Asserting the URL the route built

This is the most useful structural assertion for REST routes:

```ts
expect(global.fetch).toHaveBeenCalledTimes(1);
const fetchUrl = (global.fetch as jest.Mock).mock.calls[0][0] as string;
expect(fetchUrl).toContain("/coupons?");
expect(fetchUrl).toContain("code=TESTCOUPON");
```

Catches: missing query params, wrong endpoint path, accidentally appending the user input twice, off-by-one path constructions. Without this assertion, a route that builds the wrong URL but returns the correct response by accident (mock returns canned data regardless) would pass — a "passes for the wrong reason" trap.

### REST APIs often return counts in HEADERS, not body

A frontend that paginates needs a total count to compute "how many pages exist?" If the API returns only the current page and no total, the frontend either renders 1 page (if it falls back to `items.length`) or renders no pagination at all.

Common patterns across REST APIs:

| API                                                          | Where total / pagination lives                                                            |
| ------------------------------------------------------------ | ----------------------------------------------------------------------------------------- |
| **WordPress / WP REST API / WooCommerce / WPGraphQL bridge** | `X-WP-Total` + `X-WP-TotalPages` HTTP headers                                             |
| **GitHub REST**                                              | `Link` header with `rel="next" / rel="last"` cursor URLs (derive total from `rel="last"`) |
| **Stripe**                                                   | `has_more: boolean` in body (cursor-style)                                                |
| **Shopify**                                                  | `Link` header with cursor pagination                                                      |
| **Generic Laravel API pagination**                           | `meta.total` in body                                                                      |

**Always read the upstream API docs for pagination shape before writing the proxy.** Always test with the real third page of data, not just page 1 — page 1 will lie to you. The first time you set `page=2` is the first time you find out your total is wrong.

### Concrete Dockbloxx case — fix for `X-WP-Total`

```ts
// In the route's POST handler, after fetching products:
const total = parseInt(productsResponse.headers.get("X-WP-Total") || "0", 10);
return NextResponse.json({ products, total }, { status: 200 });
```

Mock pattern in the test:

```ts
mockFetch.mockResolvedValueOnce(
  mockOkResponse(products, { "X-WP-Total": "23" }),
);
// ...
expect(data.total).toBe(23);
```

### WooCommerce-specific gotcha — auth via query params

```ts
const url = `${BACKEND_URL}/wp-json/wc/v3/coupons?code=${code}&consumer_key=${CK}&consumer_secret=${CS}`;
```

Most REST APIs use Authorization headers. WooCommerce uses query strings. Implication: **never include the URL in error messages** — it has credentials baked in.

```ts
// WRONG — leaks credentials
throw new Error(`Failed to fetch from ${url}`);

// RIGHT — log endpoint path + status, never the full URL
throw new Error(
  `Woo REST ${resp.status} ${resp.statusText} for endpoint ${endpoint}`,
);
```

### Key-absent vs empty-value distinction

When parsing sparse metadata (WordPress meta, JSON columns, document store extras), distinguish "this key doesn't exist on the record" from "this key exists but its value is empty/zero/null":

```ts
function pickMeta(
  record: { meta_data: Array<{ key: string; value: unknown }> },
  key: string,
): unknown {
  const entry = record.meta_data?.find((m) => m.key === key);
  return entry ? entry.value : null; // null = absent; falsy value = present-but-empty
}
```

If the function returned `null` for either case, callers couldn't tell whether to use a feature at all or just had no restriction.

---

## 4.3 Stripe — wrapper-mock vs constructor-mock decision tree

### Two patterns, one decision

```
Route imports Stripe via...
│
├── Project wrapper module (e.g., import { stripe } from "@/lib/stripe/stripe")
│   → Use the WRAPPER-MOCK pattern (Section 4.3a)
│
└── Direct SDK import (import Stripe from "stripe"; new Stripe(...))
    → Use the CONSTRUCTOR-MOCK pattern (Section 4.3b)
```

**If you control the codebase and want easier testability, introduce a thin wrapper.** The wrapper pattern is cleaner — no class-constructor mock dance, no `mock*` prefix dance. But when you don't have a wrapper, the constructor mock works fine — just verbose.

### 4.3a — Wrapper-mock pattern (StarkReads / v1.0)

Singleton wrapper file:

```ts
// src/lib/stripe/stripe.ts
import Stripe from "stripe";
export const stripe = new Stripe(process.env.STRIPE_SECRET_KEY!, {
  typescript: true,
});
```

Routes import the wrapper, not the SDK:

```ts
import { stripe } from "@/lib/stripe/stripe";
```

Test mocks the wrapper, not `'stripe'`:

```ts
jest.mock("@/lib/stripe/stripe", () => ({
  stripe: {
    customers: { create: jest.fn() },
    checkout: { sessions: { create: jest.fn() } },
    subscriptions: { retrieve: jest.fn(), update: jest.fn() },
    webhooks: { constructEvent: jest.fn() },
    billingPortal: { sessions: { create: jest.fn() } },
  },
}));
```

Per-test configuration:

```ts
(stripe.checkout.sessions.create as jest.Mock).mockResolvedValue({
  url: "https://checkout.stripe.com/test-session",
});
```

Why this works:

- No need to mock the Stripe constructor or prototype.
- The mock shape only includes methods the route actually calls.
- The `STRIPE_SECRET_KEY!` assertion doesn't blow up at module load.
- Test failures point to your singleton, not SDK internals.

### 4.3b — Constructor-mock pattern (Dockbloxx)

Route imports Stripe directly:

```ts
import Stripe from "stripe";
const stripe = new Stripe(process.env.STRIPE_SECRET_KEY!, { ... });
// route handler uses stripe.customers.list(), stripe.paymentIntents.create(), etc.
```

Test mocks the `stripe` package itself. The factory returns a constructor that hands back a persistent instance whose methods are top-level `jest.fn()`s:

```ts
process.env.STRIPE_SECRET_KEY = "sk_test_fake_key";

const mockCustomersList = jest.fn();
const mockCustomersCreate = jest.fn();
const mockPaymentIntentsCreate = jest.fn();

jest.mock("stripe", () => {
  return jest.fn().mockImplementation(() => ({
    customers: { list: mockCustomersList, create: mockCustomersCreate },
    paymentIntents: { create: mockPaymentIntentsCreate },
  }));
});

import { POST } from "@/app/api/create-payment-intent/route";
```

Per-test:

```ts
beforeEach(() => {
  mockCustomersList.mockReset();
  mockCustomersCreate.mockReset();
  mockPaymentIntentsCreate.mockReset();
});

test("...", async () => {
  mockPaymentIntentsCreate.mockResolvedValue({
    id: "pi_test",
    client_secret: "pi_test_secret",
  });
  // call POST, assert
});
```

### Why top-level `mock*` constants

Two reasons:

1. **Jest's hoisting check.** `jest.mock(...)` factory functions can't reference outer-scope variables UNLESS they're prefixed with `mock` (case-insensitive). Top-level `const mockX = jest.fn()` satisfies this.

2. **Module-load capture.** The route instantiates `const stripe = new Stripe(...)` at MODULE LOAD time — once, when the test file's `import { POST }` runs. After that, the route's `stripe` variable is permanently bound to whatever the mock returned during that one call. The constructor mock returns a stable object containing references to top-level `jest.fn()`s, so per-test we configure those fns without losing the binding.

### Multi-step flow assertion pattern

When a route makes multiple SDK calls in a branchy sequence (e.g., `list customers → maybe create customer → create PaymentIntent`), each branch deserves a test:

- **Skip path:** input that bypasses an early step entirely. Assert that step was NOT called (`expect(mock).not.toHaveBeenCalled()`).
- **Reuse path:** input that triggers branch A. Assert A was called, B was NOT.
- **New path:** input that triggers branch B. Assert B was called with the right args.

Absence + presence assertions together catch both "accidentally always-calling" and "wrong args" regressions.

### Defensive error message assertions (Stripe + any payment processor)

Stripe errors can contain card details, customer emails, internal request IDs. The catch block of any payment route must:

1. Log the full error server-side (for debugging).
2. Return a **generic** message to the client.
3. Have a test that asserts the leak doesn't happen.

```ts
// Route source:
} catch (error: any) {
  console.error("Stripe Error:", error);
  return NextResponse.json(
    { message: "Failed to process payment. Please try again." },
    { status: 500 }
  );
}

// Test:
test("returns 500 with generic message when Stripe SDK throws (no internal details leaked)", async () => {
  mockPaymentIntentsCreate.mockRejectedValue(
    new Error("Your card ending 4242 was declined. Internal ID abc-secret-leaked")
  );

  const response = await POST(makeRequest({ amount: 5000, currency: "usd" }));
  const data = await response.json();

  expect(response.status).toBe(500);
  expect(data.message).toBe("Failed to process payment. Please try again.");

  // Defensive — none of the upstream leaks through.
  expect(data.message).not.toMatch(/4242/);
  expect(data.message).not.toMatch(/abc-secret-leaked/);
  expect(data.message).not.toMatch(/declined/i);
});
```

---

## 4.4 Test data sourcing — discovered vs declared

### The fixture discovery script

When testing against a real backend, hardcoded record references create brittle coupling between test logic and dataset state. The fix: a discovery script that connects to whichever backend is configured in `.env.local`, pulls live records, and writes a JSON file that all E2E tests read at module top.

### Static + live fixture split

| File                          | Source                  | Committed?      | When it changes                                          |
| ----------------------------- | ----------------------- | --------------- | -------------------------------------------------------- |
| `e2e/fixtures/dealers.json`   | manually maintained     | YES             | when team adds/removes dealer pages                      |
| `e2e/fixtures/live-data.json` | discovery script output | NO (gitignored) | regenerated per environment via `npm run fixtures:fetch` |

Static fixtures are for things the script can't infer (e.g., which dealer slugs the team has agreed to keep stable). Live fixtures are for everything else — let the script figure it out fresh each time.

### Discovery script architecture

```ts
#!/usr/bin/env tsx
import * as dotenv from "dotenv";
import * as fs from "fs";
import * as path from "path";

dotenv.config({ path: ".env.local" });

const BACKEND_URL = process.env.NEXT_PUBLIC_BACKEND_URL;
const CK = process.env.WOOCOM_CONSUMER_KEY;
const CS = process.env.WOOCOM_CONSUMER_SECRET;

function fail(msg: string): never {
  console.error(`❌ ${msg}`);
  process.exit(1);
}

// Fail loud on missing env vars BEFORE any network call.
if (!BACKEND_URL) fail("NEXT_PUBLIC_BACKEND_URL is not set in .env.local");
if (!CK) fail("WOOCOM_CONSUMER_KEY is not set in .env.local");
if (!CS) fail("WOOCOM_CONSUMER_SECRET is not set in .env.local");

async function wooFetch<T>(endpoint: string): Promise<T> {
  const sep = endpoint.includes("?") ? "&" : "?";
  const url = `${BACKEND_URL}/wp-json/wc/v3${endpoint}${sep}consumer_key=${CK}&consumer_secret=${CS}`;
  const resp = await fetch(url);
  if (!resp.ok) {
    // Never include the URL in error messages — it has credentials.
    throw new Error(
      `Woo REST ${resp.status} ${resp.statusText} for endpoint ${endpoint}`,
    );
  }
  return (await resp.json()) as T;
}

async function main() {
  // Pull live data
  const products = await wooFetch<any[]>(
    "/products?per_page=20&status=publish",
  );
  const categories = await wooFetch<any[]>("/products/categories?per_page=20");
  const coupons = await wooFetch<any[]>("/coupons?per_page=20");

  // Read static fixtures
  const dealers = JSON.parse(
    fs.readFileSync("e2e/fixtures/dealers.json", "utf-8"),
  );

  // Compose
  const liveData = {
    generated_at: new Date().toISOString(),
    backend_url: BACKEND_URL,
    products: {
      first_published: products[0],
      general_pool: products.slice(0, 5),
    },
    categories: { populated: categories.find((c) => c.count > 0) },
    coupons: {
      valid: coupons.find(
        (c) => !c.date_expires || new Date(c.date_expires) > new Date(),
      ),
    },
    dealers,
  };

  // Atomic write — temp file + rename. Prevents partial files on crash.
  const tmpPath = `e2e/fixtures/live-data.json.tmp`;
  const finalPath = `e2e/fixtures/live-data.json`;
  fs.writeFileSync(tmpPath, JSON.stringify(liveData, null, 2), "utf-8");
  fs.renameSync(tmpPath, finalPath);

  console.log(`✅ Fixtures written to ${finalPath}`);
}

main().catch((err: Error) => fail(`Fixture fetch failed: ${err.message}`));
```

### Four principles enforced by the script

1. **Fail loud on missing env vars before any network call** — clear one-line error instead of downstream "fetch failed" stack trace.
2. **Atomic write or no write** — temp file + rename. Prevents consumers from reading partial state if the script crashes mid-write.
3. **Credentials never appear in error messages** — log endpoint + status, never the URL with auth params.
4. **Key-absent vs empty-value distinction** — the script captures meta keys that ARE present even when their value is empty, so test code can decide what to do.

### npm script + per-environment regeneration

```json
"fixtures:fetch": "tsx scripts/fetch_e2e_fixtures.ts"
```

Run on every environment switch (dev → staging → prod), and before any test run where the backend dataset may have changed. The output JSON is gitignored — each environment regenerates its own.

---

## 4.5 E2E framework specifics — Playwright

### `npx playwright test --list` printing "Error" while exiting 0

Empty `e2e/` folder triggers `Error: No tests found` in stdout but exit code is still 0. Use exit code as ground truth, not the word "Error" in output. **Playwright-specific.**

### `webServer.reuseExistingServer` semantics

When `true`: Playwright uses an existing server on the URL if responsive; spawns one if not. Massive speedup during local iteration — no waiting for dev server cold start on every test run.

When `false`: Playwright always spawns its own server, fails if port is busy. Use in CI for hermetic runs.

### `getByText` strict-mode (recap)

See §2.3. Default is strict — multiple matches fail the assertion. Assert-each-variant > narrow regex > `.first()`.

### Trace viewer

`trace: 'on-first-retry'` (in config) captures a full trace on the first retry of a failed test. Open with `npx playwright show-trace <path>` to see DOM snapshots, network log, console output, and timeline. **Indispensable for diagnosing flakes.** With `retries: 0`, this only fires when manually re-running a failed test with `--retries=1` for the diagnostic.

### Conditional `test.skip` with runtime reason

For tests that depend on data conditions (e.g., a category needs >12 products for pagination):

```ts
test("category pagination works", async ({ page }) => {
  test.skip(
    liveData.categories.populated.product_count <= 12,
    "skipped: populated category has <13 products, can't test pagination",
  );
  // ... actual test ...
});
```

The skip reason appears in the test output. Different from `test.skip(...)` at the declaration level (no reason shown).

---

## 4.6 Testing in regulated environments

Patterns specific to regulated environments (HIPAA, SOC2, PCI, GDPR) will be added after the first regulated-environment project ships v1.0, at which point this section gains real case studies grounded in production experience. Until then, Principle 1.8 (defensive error message assertions) is the closest existing analog — applicable to PHI/PII protection in error responses. See Section 4.3 for the implementation pattern.

---

# Part 5 — Companion Artifacts

Every Factory app maintains three documents alongside the code. **Every new Factory app scaffolds with all three from day one.** If there are no findings or items yet, the file is just a template — but it exists, which makes adding entries frictionless when needed. Each costs ~10 minutes to set up and returns hours of investigation time over the project lifetime.

## 5.1 `CHANGELOG.md`

Follows [Keep a Changelog](https://keepachangelog.com/) format and [Semantic Versioning](https://semver.org/).

### Maintenance flow

- All in-flight changes accumulate under `[Unreleased]`.
- At deploy time, promote `[Unreleased]` → versioned section, date-stamp it (ISO 8601: `YYYY-MM-DD`), git-tag the commit (`v1.2.0`).
- Sections: `Added`, `Changed`, `Fixed`, `Security`, `Deprecated`, `Removed`.
- Skip: typo fixes, dep bumps, internal refactors, doc-only changes, test additions.
- **Inclusion test:** "would a stakeholder care this changed?"

### Semantic versioning rules

- **MAJOR** for breaking changes / required user action.
- **MINOR** for new features (backward compatible).
- **PATCH** for bug fixes (backward compatible).

### Template

```markdown
# Changelog — [App Name]

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.0.0] - YYYY-MM-DD

[Optional intro paragraph describing the release boundary.]

### Added

- ...

### Changed

- ...

### Fixed

- ...

### Security

- ...

### Deprecated

- ...

### Known Open Items (Not Blockers)

- ...
```

### When to start a changelog

Almost always immediately, but no later than the first production deploy. Starting late is worse than starting now.

## 5.2 `SECURITY_FINDINGS.md`

Authoritative tracker for security issues discovered outside the test/fix cycle. Maintained at project root in `agent_docs/`.

### Status key

- 🔴 **OPEN** — confirmed issue, not yet addressed
- 🟡 **IN PROGRESS** — fix planned or in flight
- ✅ **FIXED** — addressed and verified

### Template (per finding)

```markdown
## Finding #N — [Short title]

**Status:** [🔴 OPEN / 🟡 IN PROGRESS / ✅ FIXED YYYY-MM-DD]
**Severity:** [LOW / MEDIUM / HIGH / CRITICAL] ([what's exposed])

### Problem

[1-2 paragraphs describing the issue concretely.]

### Discovery

[When/where surfaced, e.g., during recon of /api/X in Block 4 Step 4C.1]

### Fix (if applicable)

[What was changed; pointer to the test that locks it in.]

### Risk (if OPEN)

[What an attacker could do.]

### Recommended Fix (if OPEN)

[Concrete proposed change, with code snippet if appropriate.]

### Mitigation Until Fix (if OPEN)

[Workarounds at infrastructure or process layer.]

### Files

- `src/path/to/file.ts` (specific lines or function)
```

### When findings should land here vs in tests

Recon-phase findings (Section 3.3) belong here. Tests should assert the **correct** post-fix behavior, not document the buggy state. If a test would have to be named "assert the leak happens," the finding belongs in this document and the fix is the priority.

## 5.3 `CLEANUP_BACKLOG.md`

Non-urgent items tracked for future cleanup sessions. Not bugs, not security issues — technical debt with known fix paths.

### Template (per item)

```markdown
### [Short title]

- Location: `src/path/to/file.ts` (or "various — see below")
- Current state: [what exists today]
- Fix: [what to change]
- Risk: [low / medium / high if you defer it]
- [Optional: blocker list if there's a dependency before this can be done]
```

### What belongs here vs in SECURITY_FINDINGS.md

- **Security issues** (data exposure, auth gaps, injection vectors): `SECURITY_FINDINGS.md`.
- **Tech debt without security impact** (dead code, deprecated dependencies, lint warnings, format inconsistencies): `CLEANUP_BACKLOG.md`.

If in doubt, file in `SECURITY_FINDINGS.md` with severity LOW — easier to recategorize down than to surface a missed security issue later.

### What belongs here vs in CHANGELOG.md `### Deprecated`

- **Deprecated feature plumbing that ships with the release** (code is in production but the feature is dead): note in `CHANGELOG.md ### Deprecated` AND in `CLEANUP_BACKLOG.md` for the eventual removal.
- **Pure tech debt** (no behavior change, no feature deprecation): `CLEANUP_BACKLOG.md` only.

---

# Part 6 — Gotchas & Generalizable Failure Modes

Augmented list from v1.0 plus new failure modes discovered.

## Carried forward from v1.0

### G1: Jest 30 flag rename

`--testPathPattern` (singular) → `--testPathPatterns` (plural). If your `package.json` script uses the old flag, Jest 30 will error. CLI flag only — not available in `jest.config.js`.

### G2: Env vars at module scope must be set before import

If a module reads `process.env.X` at import time (module scope), setting `process.env.X` after importing is too late. The module already captured `undefined`.

```ts
// In test file:
process.env.STRIPE_PRICE_STARTER = "price_test_starter";
import { resolveTierFromPriceId } from "@/lib/stripe/tierResolver";
//      ↑ MUST come AFTER the env assignment
```

Order matters. ts-jest compiles to CommonJS where assignment statements interleave with `require()` calls in source order. In integration tests, this is usually sidestepped by mocking the resolver module entirely.

### G3: Stripe SDK v22 — period dates moved to SubscriptionItem

`current_period_start` and `current_period_end` moved from `Subscription` to `SubscriptionItem` (`subscription.items.data[0]`). Mock fixtures must place them on the item, not the subscription root.

> **Note:** Accurate as of Stripe SDK v22+ (verified 2026-05-11). Check your installed version with `npm list stripe` if behavior differs.

### G4: `clearMocks` doesn't reset implementations

`clearMocks: true` in `jest.config.js` clears `mock.calls` and `mock.results`, NOT `mockImplementation` or `mockReturnValue`. A return value set via `.mockReturnValue()` persists across tests unless explicitly reset.

For per-test configuration that varies, prefer `mockReset()` (clears history + implementation) over `clearMocks`.

### G5: Webhook handler always returns 200

By design, to prevent Stripe from infinitely retrying. Tests assert the database call shape, not the response status, for event-processing tests. Only signature-verification tests (missing/invalid) check for 400.

### G6: Console output in passing tests is normal

Route handlers log events via `console.log` / `console.error`. Jest reprints these under each test. Seeing `console.error` under a `PASS` line is not a failure. To silence: `jest.spyOn(console, 'error').mockImplementation(() => {})` per test, or `silent: true` globally in config.

### G7: DNS failures break E2E but not unit/integration

E2E tests talk to real backends (Supabase admin client, fixture-discovery fetches). If DNS is down on your dev machine, E2E fails but unit/integration (which mock everything) pass fine. Fix DNS first if you see `getaddrinfo EAI_AGAIN` errors.

### G8: `as any` is acceptable in test mocks

Constructing fully-typed mocks of Supabase/Stripe response shapes adds hundreds of lines for marginal safety. Use `as any` for mock-shape casts. Standard practice in every TypeScript test suite that mocks complex external APIs.

## New in v2.0

### G9: Jest `testPathIgnorePatterns` matters when mixing test runners

A project using both Jest and Playwright has two test-file populations: `*.test.ts` for Jest, `*.spec.ts` for Playwright. Jest's default file discovery matches BOTH globs. Unless you tell Jest to skip the Playwright directory, Jest will scoop up the `.spec.ts` files, attempt to load them, and fail at module-load time when `@playwright/test`'s runtime detects it's been imported by Jest.

**The symptom — and why it's confusing:** `npm test` reports `Test Suites: 5 failed, 12 passed, 17 total. Tests: 146 passed, 146 total.` Five SUITES fail, but zero TESTS fail. That mismatch is the tell.

**The fix:** one line in `jest.config.js`:

```js
testPathIgnorePatterns: ["/node_modules/", "/e2e/"],
```

### G10: Playwright `getByText` strict-mode

`getByText(/SomePattern/)` matches all elements containing the text. If multiple match, strict mode fails the assertion. See §2.3 for the assert-each-variant pattern.

### G11: Third-party scripts at root layout race E2E click navigation

Scripts loaded in the root layout (analytics, attribution, A/B testing frameworks) run on every page. If they call `history.replaceState` or similar URL mutations on load, they can race Playwright clicks across **all** routes that have links.

Diagnostic signal: the same click-navigation flake reproduces on multiple unrelated routes that share only a layout-level script. If the routes have nothing in common except the script, the script is the cause.

Fixes, in priority order:

1. **Environment drift first** (Section 3.1) — is the script even present in production? If not, remove from dev.
2. If yes — use `page.route()` to abort the script's network request during E2E tests, OR `addInitScript()` to neutralize the specific DOM-side-effect method.
3. If neither works — `test.skip` with documentation (Section 3.6) until architectural fix.

Common culprits: GA4, GTM, Segment, Mixpanel, Amplitude, GHL, Optimizely, LaunchDarkly client SDKs with URL targeting, session-replay tools (FullStory, Hotjar), and custom in-house trackers.

### G12: Hard-waits vs deterministic signals in E2E

`page.waitForTimeout(N)` is a smell most of the time — replace with `waitForURL`, `waitForSelector`, `waitForLoadState`, or an explicit assertion that polls.

Acceptable uses for `waitForTimeout`:

- **Settling time for client-side state** (e.g., Zustand store update after a button click that triggers async storage write). 500ms is usually enough.
- **Brief gaps after async non-DOM effects** (e.g., service worker registration).

If you find yourself reaching for `waitForTimeout(N)` where N > 500, that's almost always a hidden race condition. Switch to a deterministic signal.

### G13: `@jest-environment node` docblock for App Router route tests

Next.js's `next/server` requires global `Request`/`Response` constructors. Jest's default `jsdom` doesn't provide them.

Symptom: `ReferenceError: Request is not defined` at module-load time when the test imports a route handler that uses `NextResponse`.

Fix: per-file docblock at the top of the test file:

```ts
/**
 * @jest-environment node
 */
```

Node 18+ provides Request/Response globally. Only the route-handler test files need node env; React component tests still run in jsdom.

### G14: WooCommerce auth via query params

WooCommerce REST authenticates via `consumer_key` + `consumer_secret` query parameters, not headers. Implication: never include the full URL in error messages — it has credentials baked in. Log the endpoint path and status code instead.

### G15: Dev environment drift accumulates silently

Dev environments collect scripts, debug tooling, mock services, and config overrides that prod doesn't have. If you have a feature flag in the CMS / WordPress / config layer, set up a periodic audit: "what's enabled on dev that isn't enabled on prod?" Drift is the canonical source of "works on dev, breaks in tests, fine in prod."

---

# Appendix: Quick Reference Card

**Run all unit + integration tests:** `npm test`

**Run only integration tests:** `npm run test:integration`

**Run E2E tests (headless):** `npm run test:e2e`

**Run E2E tests (UI / debug mode):** `npm run test:e2e:ui`

**Regenerate E2E fixtures from current backend:** `npm run fixtures:fetch`

**Test card for Stripe sandbox:** `4242 4242 4242 4242` (any future expiry, any CVC)

**Defensive error assertion shape:**

```ts
expect(data.message).toBe("Generic user-facing message");
expect(data.message).not.toMatch(/internal-leak-pattern/);
```

**Module-top fixture loading:**

```ts
const liveData = JSON.parse(fs.readFileSync(".../live-data.json", "utf-8"));
```

**Stripe boundary stop:**

```ts
await Promise.race([
  page.waitForURL(/checkout\.stripe\.com|hooks\.stripe\.com|js\.stripe\.com/, {
    timeout: 15000,
  }),
  page.waitForSelector('iframe[src*="stripe"]', { timeout: 15000 }),
]);
```

**Key files:**

- Jest config: `jest.config.js`
- Jest setup: `jest.setup.js` (or `src/__tests__/jest.setup.ts`)
- Playwright config: `playwright.config.ts`
- Integration tests: `tests/api/` (or `src/__tests__/api/`)
- E2E specs: `e2e/`
- E2E fixtures: `e2e/fixtures/`
- Shell wrappers: `scripts/`
- Security findings: `agent_docs/SECURITY_FINDINGS.md`
- Cleanup backlog: `agent_docs/CLEANUP_BACKLOG.md`
- Changelog: `CHANGELOG.md`

---

**END OF TESTING PLAYBOOK v2.0 DRAFT**
