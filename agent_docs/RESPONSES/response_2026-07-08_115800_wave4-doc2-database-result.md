# ✅ WAVE 4 — DOC 2 COMPLETE: DATABASE_MANUAL → v1.1 (content surgery, F-041)

**File:** `4_MANUAL-DATABASE_MANUAL.md`

## CHANGES MADE

| # | Change | Finding |
|---|--------|---------|
| 1 | Standard header (v1.1 · 2026-07-08 · Tier 4) + role-doctrine banner aligned to AUTH v1.3 | F-018 |
| 2 | **NEW §2 "Roles Table Pattern":** `user_roles` = the single authorization home — labeled **PATTERN SQL** ("kit `setup.sql` is the ground truth, verify on disk Q5.2/Q5.3" — D-015/ruling 3); `handle_new_user()` creation-time transport explained; ⛔ forbidden box (no role storage or authz reads from `user_metadata`; no role columns on mirrors — "two homes for a role guarantees privilege drift") | F-041, F-042 |
| 3 | **Mirror-table pattern de-roled:** `role TEXT` column + its index removed; sync example rewritten — metadata carries the role as transport for the trigger, profile insert carries NO role | F-041 |
| 4 | **§5 RLS reconciled (ruling 4):** the `raw_user_meta_data->>'is_admin'` policy variant REMOVED (was shown as a peer option); `user_roles` policy stands alone + ⛔ marker naming the forbidden pattern | F-041 |
| 5 | "When Schema-First Applies" note: schema-first = backend phases/conversions; frontend-first mock-first = discovery builds; FRONTEND_FIRST §2/§8 pointers | F-040 |
| 6 | GHL/QR fossils neutralized ×5: naming-table example, mapping-table default `'ghl'`→`'crm'`, order-ID comment, contact/product-ID comments, `GoHighLevel` COMMENT string | recon Q8.5 class |
| 7 | Cross-References section (STARTER_KIT_HANDBOOK, AUTH, API, FRONTEND_FIRST, TESTING) | F-035 |
| 8 | Version History table (v1.0 "(original, date unknown)" + v1.1) | F-018, D-018 |

## GATES

ghl live **0** · mirror role column **0** · metadata role-write in mirror **0** · `raw_user_meta_data` live = the ⛔ marker only · `user_roles` ×13 · 3-class encoding **0** · header ✓ · **AUTH v1.3 + DATABASE v1.1 now speak ONE role doctrine** ✓

## THINGS I DIDN'T TOUCH

§§3–4, 6–12 (data types, relationships, indexing, JSONB, typegen, queries, migrations, integrity, performance) — content as-is.

## CONCERNS

- The `user_roles` DDL is labeled pattern-SQL, not a kit copy — the queued kit-verification touch covers confirming it against `setup.sql` on disk (tracked with the AUTH item; pairs with the signup-vector ticket).

## Suggested commit

wave4(database): v1.1 — user_roles surgery, RLS reconciled, schema-first bridge, F-035/F-040/F-041
