# 📋 WAVE 4 PLAN — Manual Tier Sync (7 docs) + ROLE-PAIR BEFORE/AFTERS

> Status: PENDING_APPROVAL · 2026-07-08 · Mirrors CLI presentation. The AUTH+DATABASE before/afters below are the security-classed approval gate.

## Required reading status

FINDINGS F-038–F-042, F-035, F-018, F-011, F-012 + D-016 ✓ · REVIEW_015–021 ✓ · RECON Q3.4 v0.5 ✓ (authored it in Wave 2A) · **⚠️ _AUDIT/RECON_WAVE0.md DOES NOT EXIST in this repo** (glob-verified). Proceeding on two consistent sources for the Q1 verdict: the FINDINGS_LOG F-042 resolution row + the work order's own summary (kit TABLE-BASED; `user_roles` = source of truth; `get-user-role.ts` canonical; post-creation LOCKED; metadata = creation-time transport via protected channel; signup-vector = separate KIT ticket). **If the file should exist, drop it in before approving.**

## Pre-plan scan (3-class encoding + refs)

| Doc | C1 | moji | badDash | `_v` refs |
|---|---|---|---|---|
| AUTH | 0 | 0 | 0 | 3 (lines 106–108) |
| DATABASE | 0 | 0 | 0 | 0 |
| API | 0 | 0 | 0 | 0 |
| APP_ARCH | **17** | **21** | 0 | 1 (line ~1482) |
| STATE | 0 | 0 | 0 | 0 |
| ECOMMERCE | 0 | 0 | 0 | 0 |
| STRIPE | 0 | 0 | 0 | 0 |

APP_ARCH is worse than REVIEW_015's "16 chars" — it carries U+0090-class C1 controls too (the SFP disease). F-012 systemic diagnosis reconfirmed.

## ⚠️ The speculative-authoring boundary (governs Docs 1–2)

I do not have the kit's actual `get-user-role.ts` / `setup.sql` on disk. Fabricating "kit code" into kit-authoritative manuals = the Lesson 9 violation. Therefore:

- **Doctrine statements** — rewritten fully (that's the F-042 correction).
- **SQL examples** — written as clearly-labeled generic PATTERN SQL ("pattern — the kit's `supabase/setup.sql` is the ground truth; verify on disk, recon Q3.2/Q5.3"), never presented as kit copies.
- **The manual's stale TS code samples** (metadata-reading `getUserRole`, `is_qr_*` store flags) — replaced with interface-level descriptions + read-the-kit-on-disk pointers, NOT invented implementations.
- **Full code-sample resync against the real kit** = queued kit-verification touch (CONCERNS).

---

## DOC 1 — AUTH_MANUAL → v1.3 (F-042 correction) — BEFORE/AFTER GATE

Discovery: the metadata doctrine runs THROUGH the manual, not just line 154 — §8's `getUserRole()` sample reads `user.user_metadata`; §5's store shape uses legacy `is_qr_superadmin/admin/member` metadata flags (QR-project fossils); §10 Pattern 4 + §11 troubleshooting reference metadata roles; a "Role Flags in Metadata" storage section exists.

### A. Key Principles #5 (line 154)

BEFORE:
> 5. **Metadata-driven roles** - Roles stored in `user_metadata`, not separate tables

AFTER:
> 5. **Table-driven roles** - The `user_roles` table is the single source of truth for authorization (kit: `supabase/setup.sql`), resolved server-side via the kit's `get-user-role.ts`. `user_metadata` may carry a role ONLY as a creation-time transport through the protected admin channel — authorization is NEVER read from it.

### B. Role storage section ("Stored in Supabase auth.users.user_metadata", ~line 959)

BEFORE: describes `user_metadata` flag storage (`is_qr_*: 1/0`), "only one flag should be 1."

AFTER (rewrite):
> **Where roles live:** the `user_roles` table (one row per user; source of truth; post-creation changes go through the locked admin path). **Creation-time transport:** the admin creation flow writes the intended role into `user_metadata` for the Mark IV `handle_new_user()` trigger to apply INTO `user_roles` at creation — transport, not storage. **⛔ FORBIDDEN:** reading `user_metadata` for any authorization decision (client or server) — this is the recon Q3.4 smell. **Hardening note:** a kit-side hardening ticket exists for the creation-time transport channel; apply the kit's current hardening — this manual does not document the vector.

### C. §8 RBAC `getUserRole()` sample (lines ~884–893) — currently reads `user.user_metadata`

AFTER: keep the `AppRole` type line; replace the metadata-reading body with the canonical-path description: "`src/utils/get-user-role.ts` resolves the role from the `user_roles` table (server-side). **The kit file on disk is the ground truth — read it there (recon Q3.2); this manual intentionally does not carry a copy that can drift.**" (No fabricated implementation.)

### D. §5 store / §10 Pattern 4 / §11 troubleshooting (legacy `is_qr_*` metadata reads)

One advisory box at §5 (referenced from §10/§11): "⚠️ The store snippets below show a legacy shape (`is_qr_*` metadata flags — QR-era naming). The current kit resolves roles from `user_roles` via `get-user-role.ts` and the store shape differs — **verify on disk (recon Q3.6) before consuming**; do not copy these snippets into new code." Samples marked, not rewritten (speculation boundary). Full resync = queued.

### E. Rest

Canonical refs (lines 106–108, F-032) · changelog → full Version History table (v1.0 "(original)" / v1.1 / v1.2 / v1.3 rows) · §0 anti-authService antibody + `src/proxy.ts` currency untouched · standard header (v1.3 · 2026-07-08 · Tier 4).

## DOC 2 — DATABASE_MANUAL → v1.1 (content surgery) — BEFORE/AFTER GATE

### A. §2 "User Mirror Table Pattern" (lines ~132–192)

BEFORE: `app_users` mirror with a `role TEXT` column + `createUserWithProfile()` writing `role` into BOTH `user_metadata` and `app_users.role`.

AFTER:
- **Roles:** the kit pattern — `user_roles` table (labeled PATTERN SQL: `user_id UUID REFERENCES auth.users, role TEXT, one row per user`) + `handle_new_user()` trigger applying the creation-time metadata transport INTO the table + server-side resolution via `get_user_role()` / the kit's `get-user-role.ts`. Labeled: "pattern — the kit's `supabase/setup.sql` is the ground truth (recon Q5.2/Q5.3)."
- **Profile mirror:** `app_users` keeps display fields (display_name, avatar_url, preferences) — **role column REMOVED** (roles have one home).
- **⛔ Forbidden box:** "Never store or READ roles for authorization from `user_metadata` (recon Q3.4 smell). Metadata is a creation-time transport only, via the protected admin channel."
- Sync example rewritten accordingly (auth create with metadata transport → trigger populates `user_roles` → profile insert without role).

### B. §5 RLS reconciliation — the review UNDERSTATED this

The first "Admins see all" policy example reads `raw_user_meta_data->>'is_admin'` — the forbidden pattern, presented as a peer option next to the `user_roles` version. AFTER: the metadata-reading policy is removed and replaced by a ⛔ marker ("do not write policies that read roles from `raw_user_meta_data` — Q3.4 smell"); the `user_roles` policy stands as THE pattern.

### C. Rest

F-040 "When Schema-First Applies" note + FRONTEND_FIRST §2 pointer (schema-first: backend phases/conversions; frontend-first mock-first: discovery builds) · GHL/`ghl_qr_orders` fossils → neutral examples (`orders`, `external CRM`, system_name `'crm'`) · standard header + v1.0-baseline history · Cross-References section (STARTER_KIT_HANDBOOK, AUTH_MANUAL, API_AND_SERVICES_MANUAL, FRONTEND_FIRST_PLAYBOOK, TESTING_PLAYBOOK) (F-035).

## DOC 3 — API_AND_SERVICES → v1.1

Lesson-2 exception box near §1 top (F-039, work-order wording) · standard header + v1.0-baseline history · Cross-References (FRONTEND_FIRST §0, STARTER_KIT_HANDBOOK, DATABASE, ECOMMERCE, TESTING) · §7 wire-format enrichment (snake_case wire / camelCase UI, per HANDOFF DATA_CONTRACT discipline).

## DOC 4 — APP_ARCHITECTURE → v1.3

F-038 de-pin: subtitle/stack-table/§3 "Next.js 15" → "Next.js App Router" where version-irrelevant; version-sensitive facts labeled ("params are a Promise — Next 15+"); recon Q1.1 verify-per-repo pointer · §10 `src/middleware.ts` guidance aligned/noted vs Next 16 `src/proxy.ts` (recon Q2.5; AUTH manual is the currency model) · 21 moji + 17 C1 swept (report: F-012 tool diagnosis reconfirmed — third Gate-10 doc) · line-1482 handbook ref canonical (F-032) · standard header + history row.

## DOC 5 — STATE_MANAGEMENT → v1.1 (metadata only)

Standard header + v1.0 "(original, date unknown)" history · Cross-References (STARTER_KIT_HANDBOOK auth-store ground truth, AUTH_MANUAL, FRONTEND_FIRST service-layer law, APP_ARCHITECTURE data flow) · ZERO content changes (review-verified clean).

## DOC 6 — ECOMMERCE → v1.1

Scope declaration at top (headless WooCommerce + Stripe ONE-TIME commerce; recurring → STRIPE_SUBSCRIPTIONS_PLAYBOOK; Supabase-native commerce → extend, F-040) · `apiVersion: '2023-10-16' // Use latest` → verify-per-repo pattern (F-038) · standard header + v1.0-baseline history · territory cross-ref.

## DOC 7 — STRIPE_SUBSCRIPTIONS → v1.1 (micro)

Territory declaration (one-time/WooCommerce → ECOMMERCE manual) · cross-refs: API_AND_SERVICES (§8), TESTING_PLAYBOOK (§12), AUTH_MANUAL (gate-helper composition) · standard header · D-016 content untouched.

## Order, gates, boundaries

Order: AUTH → DATABASE → API → APP_ARCH → STATE → ECOMMERCE → STRIPE; one suggested commit per doc, stop each time. Gates per doc + wave: role doctrine singular (user_roles) in AUTH+DATABASE; zero metadata-authz-read examples surviving unmarked; 3-class encoding 0 ×7; `_v` live refs 0; headers + history rows 7/7; Lesson-2 box present; de-pin verified; per-doc CHANGES/DIDN'T TOUCH/CONCERNS. NOT touched: everything outside the seven. The signup exploit is NOT documented anywhere — only "a kit hardening ticket exists."
