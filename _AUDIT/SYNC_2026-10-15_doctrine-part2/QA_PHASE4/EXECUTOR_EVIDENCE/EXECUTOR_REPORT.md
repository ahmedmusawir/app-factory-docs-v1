# Phase 4 — independent QA Executor evidence

QA Executor: Codex; fresh user-launched session. Reporting to Fable, QA Lead. Start: 2026-10-19T05:41:06Z. This report records criterion results, not a product verdict.

Candidate / QA_START_SHA: `20f71ee932ed21c0878cb3a0f39c6fbe90d0a793` (matches expected tip, local HEAD and remote branch). Branch: `docs/sync-doctrine-part2-2026-10-15`. BASE: `9c179392f79b70da099121fc357d3107ad3bb86e`. CONTENT_SHA: `ef35d26d82f1904da6ed33663ad647e4ee16fe98`. Landing: 2026-10-18.

## Results

39 items: **31 PASS / 8 FAIL / 0 BLOCKED / 0 OBSERVATION**. Separate observations below do not replace criterion outcomes. Git remained read-only; candidate files and pending closeout transitions were not changed.

| Item | Result | Independent evidence |

|---|---|---|

| AC1 | PASS | 101 scope paths (33 M/68 A), two authorized 10x files, 664 run records, eight bookkeeping paths; protected diff empty. RAW/ac1_classification.json. |

| AC2 | PASS | 101 installed/content/bound hash matches; 380 exact edits; 31 metadata residuals reconciled. RAW/ac2_installed_hashes.json; RAW/ac2_edit_replay.json; RAW/supplement_checks.json. |

| AC3 | PASS | 97 IDs in each table; 89 selected/5 outside/3 NO; 94 YES/3 NO; W01–23/RUL01–15/AD01 covered. RAW/ac3_ledger_tables.json; RAW/reconciled_checks.json. O-7 applied. |

| AC4 | PASS | No blanket closure/verified-kit/rescore claim; NO rows have no edit IDs. RAW/supplement_claims.txt; RAW/inputs/candidate_run/SELECTED_SCOPE_LEDGER.md. |

| AC5 | FAIL | F01; MANUAL_READS.md AC5; RAW/finding_excerpts.txt. |

| AC6 | FAIL | F01; eight exact amendments pass, surrounding ownership contradiction remains. RAW/supplement_checks.json. |

| AC7 | PASS | Two checkpoint/clean-review/gate distinctions agree. MANUAL_READS.md AC7 and AC37; RAW/read_governance.txt. |

| AC8 | PASS | Canonical vocabulary/lifecycle references agree. MANUAL_READS.md AC8; RAW/read_ownership.txt. |

| AC9 | FAIL | F02; QAM prose present but Operations package tree omits artifacts. RAW/finding_excerpts.txt. |

| AC10 | PASS | Director Git/QA-branch sequence coherent. MANUAL_READS.md AC10; RAW/read_new.txt. |

| AC11 | PASS | Immutable contracts with writable evidence lanes. MANUAL_READS.md AC11. |

| AC12 | PASS | Cleanup and three exclusion surfaces; Q9.1–3 unchanged, Q9.4 new. MANUAL_READS.md AC12; RAW/final_checks.json. |

| AC13 | PASS | Seat duties distinct; no persona-based grant. MANUAL_READS.md AC13; RAW/supplement_personas.txt. |

| AC14 | PASS | Bounded boot/resume prompts and three entry templates agree. MANUAL_READS.md AC14; RAW/reconciled_checks.json. |

| AC15 | FAIL | F03; active filesystem-wins instruction. RAW/finding_excerpts.txt. |

| AC16 | FAIL | F04; 31 withdrawal rows reviewed; FC022/038/066 retain dependent recipes. MANUAL_READS.md withdrawal table. |

| AC17 | PASS | Domain invariants preserved; six distinctions explicit. MANUAL_READS.md AC17; RAW/ac17_preservation.json. |

| AC18 | FAIL | F05; required default missing across manuals. RAW/personal_data_matches.txt. |

| AC19 | FAIL | F06; retained prescriptive platform checklist. RAW/finding_excerpts.txt. |

| AC20 | FAIL | F07; universal CURRENT_APP instructions remain; all 13 historical containers pass. RAW/ac20_markdown_containers.json; RAW/reconciled_checks.json. |

| AC21 | PASS | Three draft v1.0 playbooks, single rows, no archives; QAM permitted substitutions. RAW/ac21_qam_draft.diff; RAW/final_checks.json. |

| AC22 | PASS | 25 exact installed/source/translated files; 31 translation spans; AM1–3,11 SR rows,19 states; no populated results. RAW/ac22_template_hashes.json; RAW/ac22_classified_hits.json; RAW/reconciled_checks.json. |

| AC23 | PASS | 31 archive blobs byte-equal BASE; planned live bumps. RAW/ac23_blobs.json. |

| AC24 | PASS | Restored QA blob bb41260f6b6f94372a682f04b313a451f2b3c4b1; historical restoration wording. RAW/automated_checks.json. |

| AC25 | PASS | 34 tier docs; manifest header cells/reverse dependencies/appendix agree. RAW/ac25_manifest.json; RAW/final_checks.json. |

| AC26 | PASS | 39 contiguous run rows at CHANGELOG lines 37–75; IDs/templates/SVG coverage. RAW/ac26_rows.json. |

| AC27 | PASS | 31 single existing-table rows in required order; RECON fence closed; embedded histories unchanged. RAW/ac27_table_order.json; RAW/reconciled_checks.json. |

| AC28 | PASS | References resolve; eight canonical assets/workflow docs, embedded/linked; code JSON.stringify is not a Markdown link. RAW/ac28_links.json; RAW/asset_scope_resolution.json. |

| AC29 | PASS | Four lints pass; history-aware retired-label review. RAW/ac29_lints.txt; RAW/supplement_retired.txt. |

| AC30 | PASS | 151 exact landing substitutions, 101 bound hashes, immutable frozen records; future hashes recomputed in scratch only. RAW/automated_checks.json; RAW/reconciled_checks.json. |

| AC31 | PASS | Lint exit0/36 docs/zero hits each; lints/.github unchanged; nine-hit baseline preserved. RAW/ac29_lints.txt; RAW/protected_diff.txt. |

| AC32 | PASS | Five-commit chain, clean worktree, main unchanged, no merges/debris/snapshot modification/skill drift; preservation commit exists outside ancestry. RAW/ac32_*.txt; RAW/end_pin.json. |

| AC33 | PASS | Correctly pending: all12 old spans present/new absent; required records present, verdict/cleanup/Architect closeout pending, CLOSEOUT_VERIFICATION absent. RAW/ac33_bound_fields.json; RAW/automated_checks.json. |

| AC34 | PASS | Owners/triggers and exclusions visible; no excluded work graded as required completion. MANUAL_READS.md AC34 and External exclusions. |

| AC35 | PASS | All _SKILLS bytes unchanged; pinned guards unchanged and no attributed edit. RAW/ac35_guard_hashes.json; RAW/ac32_skills.txt. |

| AC36 | PASS | Outside/partial rows preserve owner+trigger with no closure claim. RAW/ac36_remainder_rows.json. |

| AC37 | PASS | 4 documents/SVGs; 7/18/8/24 steps exact; valid XML/actor vocabulary and historical PNG hashes. MANUAL_READS.md AC37; RAW/final_checks.json; RAW/snapshot_hashes.json. |

| AC38 | PASS | Engineering installation evidence inspected; independent25 hash/set/standing-row checks pass. Post-closeout README correctly pending. RAW/ac22_template_hashes.json; RAW/final_checks.json. |

| 10X-COPY | PASS | Both source/candidate SHA256 values exact; only4ec73a4 adds copies; zero integration hits. RAW/automated_checks.json; RAW/10x_commits.txt. |

## Findings

### F01 — AC5, AC6 — Retained contradictory DATA_CONTRACT ownership sentence

Both preceding branches assign the Architect, but the live router still says “different author”. The eight amended spans are installed exactly; the surrounding contradiction prohibition nevertheless fails.

```text

02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:174: > **CONVERSION:** the Architect **PRE-AUTHORS** `DATA_CONTRACT.md` from Brain Drain evidence — the Engineer consumes and honors it.
02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:175: > **GREENFIELD:** the Architect authors `DATA_CONTRACT.md` from the approved APP_BRIEF before Design. The Designer authors UI_SPEC; the Architect reconciles the assembled package. The Engineer consumes the approved contracts. The canonical DATA_CONTRACT template remains in §12.
02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:176: > Same artifact name — different author, different moment. Router: APP_FACTORY_BLUEPRINT, "Which Pipeline Am I In?".

```

### F02 — AC9 — Operations handoff anatomy omits mandatory QA artifacts

The mandatory QAM paragraph is present, but the immediately following handoff package tree lists the contracts/code/deployment guide without QAM/ or ACCEPTANCE_SPEC. AC9 explicitly covers folder trees and package anatomy, not only inserted prose.

```text

02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:1383: Every newly authored module includes a complete, module-specific `QAM/` prepared by the Architect from `03_BUILD_METHODOLOGY/_templates/QAM/`. QA Lead owns the reusable playbook and standing requirements. Engineer fills factual engineering records and handoff; QA Executor performs independent Q1 recon and test planning; QA Lead approves the plan; Director releases execution; QA Executor performs Q2 and authorized retest; QA Lead adjudicates and certifies. `QAM_PLAYBOOK.md` owns this packaging and sequence. Existing modules already in flight retain their recorded sequence until an attributable amendment.
02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:1384: 
02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:1385: When code is complete and tested, Engineer hands off to Operations/Deployment.
02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:1386: 
02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:1387: ### Handoff Package Contents
02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:1388: 
02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:1389: ```
02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:1390: 📦 ENGINEER → OPERATIONS HANDOFF
02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:1391: │
02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:1392: ├── APP_BRIEF.md (from Architect)
02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:1393: ├── UI_SPEC.md (from Designer)
02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:1394: ├── DATA_CONTRACT.md
02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:1395: ├── Working Code (tested)
02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:1396: ├── README.md (setup instructions)
02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:1397: └── Deployment Guide
02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:1398: ```

```

### F03 — AC15 — Active filesystem-wins rule survives in kit-track diagram

The diagram retains the explicitly forbidden “filesystem wins” authority rule. The corrected recon paragraph elsewhere does not remove this categorical instruction.

```text

02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:250: PHASE 0 — RECON (§2)
02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:251:    Answer RECON_QUESTIONNAIRE read-only → Recon Report → Architect authors
02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:252:         │
02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:253:         ▼
02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:254: KIT READ — STARTER_KIT_HANDBOOK
02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:255:    Read the handbook, treat it as ASPIRATIONAL — verify every load-bearing
02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:256:    claim against disk (RECON_QUESTIONNAIRE §0). Where handbook and
02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:257:    filesystem disagree, the filesystem wins.

```

### F04 — AC16 — Withdrawal coverage leaves dependent executable recipes

FC-022: seedSubscription still upserts through the .env.local admin client without an allowlisted target/test-identity guard. FC-038: Service Role Bypass still calls API routes an appropriate reason for RLS bypass. FC-066: fetchProducts returns Product[] while its page caller destructures {items,error}; the ISR variant has no separately named contract. These remain positive executable examples despite withdrawal/invariant paragraphs. No application code or external service was executed.

```text

03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:879: ### E2E user lifecycle (Supabase apps)
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:880: 
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:881: **Executable example withdrawn.** The previous example is not an approved implementation. The outgoing archived document preserves it as history. Replacement code requires the project’s approved contract, verified dependency interfaces and behavioral evidence. This withdrawal contains the misleading recipe; it does not certify the underlying finding resolved.
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:882: 
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:883: Before privileged test setup or cleanup, verify the target project reference against the Director-approved test-project allowlist and verify the authorized test identity. Fail closed on mismatch, missing identity or unknown target. Record every run-created identity; cleanup may act only on that set. Production verification is a separately authorized, bounded, non-destructive procedure.
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:884: 
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:885: ---
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:886: 
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:887: ### Direct DB seeding to bypass Stripe in E2E
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:888: 
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:889: E2E tests need users with specific subscription tiers. Automating Stripe Checkout in a browser is brittle (Stripe changes their DOM). Solution: insert subscription rows directly into Supabase via the admin client, as if the webhook had already fired.
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:890: 
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:891: ```typescript
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:892: export async function seedSubscription(userId: string, tier: TestTier) {
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:893:   const { error } = await supabaseAdmin.from("subscriptions").upsert(
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:894:     {
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:895:       user_id: userId,
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:896:       tier,
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:897:       status: "active",
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:898:       stripe_customer_id: `cus_test_${userId.slice(0, 8)}`,
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:899:       stripe_subscription_id: `sub_test_${userId.slice(0, 8)}`,
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:900:       current_period_start: new Date().toISOString(),
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:901:       current_period_end: new Date(
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:902:         Date.now() + 30 * 24 * 60 * 60 * 1000,
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:903:       ).toISOString(),
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:904:       cancel_at_period_end: false,
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:905:     },
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:906:     { onConflict: "user_id" },
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:907:   );
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:908:   if (error) throw new Error(`Failed to seed subscription: ${error.message}`);
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:909: }
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:910: ```
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:911: 
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:912: Synthetic Stripe IDs (`cus_test_*`, `sub_test_*`) work because the gating logic only reads `tier` and `status` from the row — it never calls the Stripe API to verify the subscription ID.
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:913: 
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:914: **Trade-off:** E2E doesn't cover the actual Stripe round-trip. That's what integration tests (mocked) validate at the route level, and what manual smoke tests validate end-to-end. Each layer covers what it's good at.
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:915: 
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:916: ### Supabase admin client in E2E helpers
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:917: 
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:918: ```typescript
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:919: import { createClient } from "@supabase/supabase-js";
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:920: import * as dotenv from "dotenv";
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:921: 
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:922: // Playwright runs outside Next.js — must load .env.local manually
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:923: dotenv.config({ path: ".env.local" });
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:924: 
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:925: export const supabaseAdmin = createClient(
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:926:   process.env.NEXT_PUBLIC_SUPABASE_URL!,
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:927:   process.env.SUPABASE_SECRET_KEY!,
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:928:   { auth: { autoRefreshToken: false, persistSession: false } },
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:929: );
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:930: ```

04_REFERENCE_MANUALS/DATABASE_MANUAL.md:418: ### Service Role Bypass
04_REFERENCE_MANUALS/DATABASE_MANUAL.md:419: 
04_REFERENCE_MANUALS/DATABASE_MANUAL.md:420: When using the service role key (server-side), RLS is bypassed. This is appropriate for:
04_REFERENCE_MANUALS/DATABASE_MANUAL.md:421: - API routes
04_REFERENCE_MANUALS/DATABASE_MANUAL.md:422: - Background jobs
04_REFERENCE_MANUALS/DATABASE_MANUAL.md:423: - Admin operations
04_REFERENCE_MANUALS/DATABASE_MANUAL.md:424: 
04_REFERENCE_MANUALS/DATABASE_MANUAL.md:425: ```typescript
04_REFERENCE_MANUALS/DATABASE_MANUAL.md:426: // Server-side: Service role bypasses RLS
04_REFERENCE_MANUALS/DATABASE_MANUAL.md:427: import { createClient } from '@supabase/supabase-js';
04_REFERENCE_MANUALS/DATABASE_MANUAL.md:428: 
04_REFERENCE_MANUALS/DATABASE_MANUAL.md:429: const supabase = createClient(
04_REFERENCE_MANUALS/DATABASE_MANUAL.md:430:   process.env.SUPABASE_URL!,
04_REFERENCE_MANUALS/DATABASE_MANUAL.md:431:   process.env.SUPABASE_SERVICE_ROLE_KEY! // Bypasses RLS
04_REFERENCE_MANUALS/DATABASE_MANUAL.md:432: );

04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:613: export const fetchProducts = async (): Promise<Product[]> => {
04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:614:   const response = await fetch(API_ENDPOINTS.PRODUCTS);
04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:615:   const wooProducts: WooCommerceProduct[] = await response.json();
04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:616:   
04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:617:   // Transform each product to internal format
04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:618:   return wooProducts.map(normalizeProduct);
04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:619: };

04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:787: 
04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:788: import { fetchProducts } from '@/services/productServices';
04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:789: import { ProductList } from '@/components/shop/ProductList';
04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:790: import { EmptyState } from '@/components/common/EmptyState';
04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:791: 
04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:792: export default async function ShopPage() {
04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:793:   const { items: products, error } = await fetchProducts();
04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:794: 
04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:795:   // Graceful degradation: show empty state instead of crashing
04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:796:   if (error || products.length === 0) {
04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:797:     return (

04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:853: 
04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:854: ```typescript
04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:855: // Static generation with revalidation
04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:856: export const fetchProducts = async () => {
04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:857:   const response = await fetch(API_ENDPOINT, {
04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:858:     next: { 
04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:859:       revalidate: 3600, // Revalidate every hour
04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:860:     },
04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:861:   });
04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:862:   return response.json();

```

### F05 — AC18 — Browser-contact default is not stated across all four required manuals

STATE states the default. AUTH and TESTING do not state the required default against persistent raw contact information in browser storage; ECOMMERCE refers to an approved retention policy but does not state that default. Generic log-redaction or authorization-state restrictions are not the specified contact-storage rule. Full persist/contact matches are retained in RAW/personal_data_matches.txt.

```text

04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:501: **Never persist everything.** Use `partialize` to select only UX-critical state:
04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:502: 
04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:503: ```typescript
04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:504: export const useCheckoutStore = create<CheckoutState>()(
04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:505:   persist(
04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:506:     (set) => ({
04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:507:       // Persisted
04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:508:       billingAddress: null,
04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:509:       shippingAddress: null,
04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:510:       
04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:511:       // NOT persisted (transient)
04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:512:       isProcessing: false,
04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:513:       validationErrors: {},
04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:514:       paymentIntent: null,
04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:515:     }),
04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:516:     {
04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:517:       name: 'checkout-storage',
04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:518:       partialize: (state) => ({
04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:519:         // Raw contact information is not persisted by default.
04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:520:         // An approved exception must name fields, purpose, retention and owner.

04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:783: Do not persist raw contact details by default. Any approved personal-data persistence declares permitted fields, retention duration and user or guest scope. Sign-out and account transition reset and invalidate every affected store even when remote logout fails; a new account must not hydrate the previous account’s data. Payment and authorization state remain outside persistence. Storage readiness is separate from business-data reset.

04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:199: Accept product/variation identifiers, quantities, shipping selection and coupon code, never caller prices, shipping costs or discount amounts. Validate quantities and product eligibility; load authoritative catalog prices; validate the shipping selection and coupon eligibility; apply the declared tax policy; calculate currency-safe totals on the server. Bind the payment to the authorized order and verify payment identity, amount, currency and order association before marking paid. Client totals are display-only. Return generic failures and redact logs. Universal quote-storage design is deferred; the required server pricing and payment binding still apply.
04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:200: 
04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:201: Persist one authorized checkout-attempt identity across retries and claim it atomically against concurrent requests. Scope provider idempotency keys to that attempt and operation, reuse or retrieve existing external objects after an unknown outcome, and reconcile before creating a replacement. Use the project-approved customer-identity contract without assuming paid activation; universal subscription schema design is deferred. Handle every documented subscription state, not only active.
04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:202: 
04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:203: Use one validated checkout contract across form, state, route and service. The request carries billing.email, validated line identifiers/quantities, shippingMethod and couponCode; it carries no authoritative monetary values. The response identifies the authorized order/payment attempt or a typed generic failure. The server pricing operation from the same contract supplies totals. Revisions to items, shipping or coupon invalidate the old payment binding before a new attempt is released.
04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:204: 
04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:205: The checkout interaction contract includes shippingCost and couponDiscount as display estimates, couponCode, setCoupon(code) and clearCoupon(), alongside the existing checkout fields. The server revalidates shipping and coupons. STATE_MANAGEMENT_MANUAL owns the shared store shape; ECOMMERCE_AND_PAYMENTS_MANUAL refers to it. Personal fields follow the approved account-transition and retention policy.
04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:206: 
04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:207: ---

03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:418: For tests touching persistent client state (Zustand, Redux with localStorage, IndexedDB), assert against **both** the source of truth AND the UI:
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:419: 
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:420: ```ts
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:421: await expect(page.getByText(/Coupon Applied:/)).toBeVisible(); // user-facing claim
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:422: 
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:423: const stored = await page.evaluate(() =>
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:424:   localStorage.getItem("checkout-storage"),
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:425: );
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:426: expect(JSON.parse(stored!).state.couponCode).toBe(expectedCode); // approved non-sensitive project fixture only

```

### F06 — AC19 — Unqualified live platform deployment recipe remains

The deployment owner correctly says platform procedure is OPEN/not adopted, while the subscription manual retains a prescriptive GCP deployment checklist with create-secret/deploy commands and no historical/unadopted qualifier. This is an authority consistency finding, not a vendor-command correctness finding.

```text

04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:484: ## 13. Deployment Checklist
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:485: 
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:486: ### GCP Cloud Run Deployment
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:487: 
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:488: **Step 1 — Create Secrets in GCP Secret Manager:**
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:489: ```bash
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:490: gcloud secrets create projectname-stripe-secret-key --data-file=-
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:491: gcloud secrets create projectname-stripe-webhook-secret --data-file=-
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:492: gcloud secrets create projectname-stripe-price-starter --data-file=-
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:493: gcloud secrets create projectname-stripe-price-pro --data-file=-
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:494: gcloud secrets create projectname-stripe-price-enterprise --data-file=-
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:495: gcloud secrets create projectname-supabase-service-role-key --data-file=-
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:496: ```
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:497: 
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:498: **Step 2 — Deploy Cloud Run with Secret Mappings:**
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:499: ```bash
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:500: gcloud run deploy projectname \
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:501:   --set-secrets=STRIPE_SECRET_KEY=projectname-stripe-secret-key:latest \
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:502:   --set-secrets=STRIPE_WEBHOOK_SECRET=projectname-stripe-webhook-secret:latest \
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:503:   --set-secrets=STRIPE_PRICE_STARTER=projectname-stripe-price-starter:latest \
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:504:   --set-secrets=STRIPE_PRICE_PRO=projectname-stripe-price-pro:latest \
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:505:   --set-secrets=STRIPE_PRICE_ENTERPRISE=projectname-stripe-price-enterprise:latest \
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:506:   --set-secrets=SUPABASE_SERVICE_ROLE_KEY=projectname-supabase-service-role-key:latest \
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:507:   --set-env-vars=NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=pk_test_... \
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:508:   --set-env-vars=NEXT_PUBLIC_SUPABASE_URL=https://xxx.supabase.co \
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:509:   --set-env-vars=NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJ...
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:510: ```
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:511: 
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:512: Note: `NEXT_PUBLIC_*` vars can be plain env vars (they're browser-safe). Secret vars use `--set-secrets`.
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:513: 
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:514: **Step 3 — Register Webhook Endpoint in Stripe Dashboard:**
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:515: 
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:516: After deployment, your Cloud Run service has a URL like `https://projectname-abc123.run.app`.
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:517: 
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:518: Go to Stripe Dashboard → Developers → Webhooks → Add endpoint:
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:519: - **URL:** `https://projectname-abc123.run.app/api/webhooks/stripe`
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:520: - **Events:** Select `checkout.session.completed`, `customer.subscription.updated`, `customer.subscription.deleted`
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:521: 
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:522: Copy the new webhook signing secret and update the GCP secret.
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:523: 
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:524: **Step 4 — Verify:**
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:525: ```
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:526: □ Visit the Cloud Run URL — app loads
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:527: □ Register a user — auth works
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:528: □ Subscribe — Stripe Checkout works
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:529: □ Webhook fires — subscription appears in Supabase
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:530: □ Content gating works
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:531: ```

03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md:69: ## 7. Platform Profiles — OPEN
03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md:70: 
03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md:71: No platform procedure is Factory doctrine yet. The August DevOps operating model (SRC-W07) proposes a Cloud Run profile (`init-app.sh`, `cloudbuild.yaml`, `Dockerfile`, `deploy.sh`, a checklist) and two platform postures; `APP_FACTORY_SKILLS_PLAYBOOK.md` §14 names the deployment skill family. These are source claims and existing tools, not adopted rules: version-sensitive commands must be verified at implementation time, and profile-specific filenames are not imposed on Vercel or Python deployments. Adoption of any profile is the Director's decision (DEC-18 remainder).
03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md:72: 
03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md:73: ## 8. Open Items Register — OPEN (not doctrine)
03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md:74: 
03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md:75: | ID | Open item | Owner | Source of the gap |
03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md:76: |---|---|---|---|
03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md:77: | O-1 | DevOps authority: the cloud columns of the §3 matrix; "may the Engineer deploy to staging in FFM runs?"; Cloud Run as one platform profile | Director (Architect advises) | DEC-18 remainder; the reported DevOps Architect ruling of 2026-08-23 was not supplied (CL-13) |
03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md:78: | O-2 | DevOps Architect seat occupant | Director | SRC-W07 F-2 (deliberately unassigned) |
03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md:79: | O-3 | Staging → production promotion doctrine | Director | SRC-W07 F-1 |
03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md:80: | O-4 | Monitoring / incident detection after deploy | Director | SRC-W07 F-3 |
03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md:81: | O-5 | Non-Next.js deployment packages (Python / ADK services) | Director | SRC-W07 F-4 |
03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md:82: | O-6 | Gate D mapping on client platforms beyond Vercel | QA Lead / Director | SRC-W07 F-5 |
03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md:83: 
03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md:84: An OPEN item is closed only by a Director ruling recorded and landed through DocSet Sync; until then no module may cite this section as authority for a deployment action.

```

### F07 — AC20 — Universal CURRENT_APP landing instructions survive

Live FFM definition and handoff/bridging instructions prescribe agent_docs/CURRENT_APP despite the no-universal-landing-path requirement. Appendix B was repaired and passes its bounded AC14 checks. All 13 historical-pointer container checks separately pass.

```text

03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:38: ---
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:39: 
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:40: ## 1. What an FFM Is, In One Page
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:41: 
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:42: A **Frontend-First Module (FFM)** is a portable, self-contained folder dropped at `agent_docs/CURRENT_APP/<project>_<phase>_ffm/` inside a starter kit clone. It is the single source of truth that tells an AI coding tool (Claude Code, Codex CLI, Gemini CLI, etc.) **what to build, how to build it, and what not to touch.**
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:43: 
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:44: An FFM bundles:

03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:165: ### Role 3 — Architect
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:166: 
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:167: **Who:** You, Claude (in a chat session, NOT in the terminal as a coding agent).
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:168: **With:** Operator (you).
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:169: **Produces:** The complete FFM folder, ready to drop at `agent_docs/CURRENT_APP/`.
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:170: 
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:171: **Outputs:** Every file in the FFM folder structure (see [Section 3](#3-ffm-anatomy--the-folder-structure)).
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:172: 
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:173: **Handoff target:** The starter kit's `agent_docs/CURRENT_APP/` directory.
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:174: 

03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1637: ## 16. Bridging The FFM Into The Starter Kit
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1638: 
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1639: The FFM lives at `agent_docs/CURRENT_APP/<project>_<phase>_ffm/`. The starter kit's root `CLAUDE.md` needs to know it's there.
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1640: 
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1641: ### Two Bridging Patterns
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1642: 
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1643: **Pattern A — Edit Starter Kit Root `CLAUDE.md` (older convention)**
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1644: 
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1645: The operator adds a pointer paragraph to the starter kit's root `CLAUDE.md`:
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1646: 
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1647: ```markdown
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1648: ## Active Project Module
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1649: 
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1650: The current project's Factory module lives at `agent_docs/CURRENT_APP/<ffm_folder_name>/`. Read `CLAUDE.md` in that folder for project-specific direction, doctrine, and the phase-by-phase playbook. All work for the current project follows that module.
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1651: ```
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1652: 
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1653: Claudy reads root CLAUDE.md first on session start, sees the pointer, follows it to the FFM.
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1654: 
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1655: **Pattern B — `PROJECT_POINTER.md` (newer, cleaner convention)**
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1656: 
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1657: Create a separate file at the starter kit root called `PROJECT_POINTER.md`:
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1658: 
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1659: ```markdown
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1660: # PROJECT_POINTER.md — Active Project Module
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1661: 
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1662: The current project's Factory module lives at:
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1663: **`agent_docs/CURRENT_APP/<ffm_folder_name>/`**
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1664: 
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1665: On session start, read `CLAUDE.md` in that folder. That file is the project's navigation contract. It tells you which project we're building, what's in scope, what's forbidden, what phase we're in, and where to find the project handoff docs (APP_BRIEF, DATA_CONTRACT, UI_SPEC).

```

## Method and limits

Pristine BASE/CONTENT/candidate git-archive exports were graded. Installed hashes, exact edit/date/template replays, archive blobs, snapshot hashes, lints, XML/Markdown structure and manual surrounding-context checks were independently rerun. Engineering evidence was inspected as an object under test, not used as acceptance. COMMANDS.json preserves cited verification subprocess argv/cwd/exit/unfiltered output; RAW retains initial instrument outputs and corrected results. Manual quotations and all31 withdrawal judgments are in MANUAL_READS.md.

## Observations

- O-7: no separate filled handoff-disposition file; operative97-row tables agree. No failure added.

- D-3 historical-pointer punctuation and excluded kit/platform API implementation correctness are observations only.

- Initial script false negatives are preserved, not silently deleted: AM-marker substring vs row identity; Markdown numbered-step format; wrapped SVG hyphen; manifest Governed-by header; routing marker comments; mixed-case historical-site detector; code-expression pseudo-links; proposal copies counted as canonical assets. Corrected checks and semantic readings resolve these in final/reconciled/asset-scope records.

- AC13 follows the frozen spec’s no-permission-by-persona rule and no-mass-rename instruction. Raw tool-name hits alone are not failures.

- AC32 local graph and remote refs cannot prove the absence of every historical force-push. They establish the required current graph, stable main and start/end candidate; no broader historical claim is made.

- The user-supplied prompt path was absent in the execution tree. The exact expected-hash prompt was located in the review repo, where its own instructions place the assignment and evidence. No candidate mutation was needed.

- A prior-session BLOCKED note is retained only as RAW/prior_session_BLOCKED.md and does not describe this fresh session.

- Initial exploratory Python reads ran from review cwd; reproducible cited checks were rerun as python3 -B -I from scripts/. Inline exploratory snippets were not all retained verbatim; no such snippet is the sole basis of a result. This is a command-provenance limitation, not hidden evidence.

## Handoff

Fable owns adjudication. All12 conditional closeout transitions are correctly pending. No repair or closeout action was applied. SHA256SUMS.txt covers all other files in this package; its own hash is reported with the delivery ZIP.
