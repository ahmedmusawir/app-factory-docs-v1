# QA Lead Successor Verdict — AMENDED-v2 retest, candidate `8dff354`

**Seat:** Fable, QA Lead. **Issued:** 2026-10-19 19:40 +06. **Authority:** Tony brief "FABLE — ADJUDICATE THE AMENDED-v2 RETEST" (2026-10-19).
**Candidate:** `8dff354937bc7baf739370a9886497d9d5359186` (parent `20f71ee…`, branch `docs/sync-doctrine-part2-2026-10-15`; remote tip and local worktree HEAD both `8dff354`; `main` unchanged at `9c17939…`).
**Evidence reviewed:** `/home/moose/Downloads/QA_AMENDED_V2_EXECUTOR_8dff354_2026-10-19.zip`, SHA-256 `907f8dabce8336955a936d953c0f4a20b08d703a2e5c801fe3d7bcfbc4ac4842`; 119 members, SHA256SUMS 0 mismatches; byte-identical to `RETEST_AMENDED_V2/EXECUTOR_EVIDENCE/`. The three candidate manual copies in the ZIP match the git blobs at `8dff354` (`76cc624c…`, `d661a820…`, `cac8f71f…`).
**Governing criteria:** frozen spec R1 (`2a3867ca…`) AC16; repair acceptance R1–R12 (`REPAIR_QA_P4/ENGINEER_REPAIR_PROMPT.md` §4); overrides O-1…O-8; Phase 4 verdict (preserved); Gate 2 AMENDED-v2 approval (`REPAIR_QA_P4/DIRECTOR_DECISIONS_V2.md`).

## 1. Verdict

**FAIL — on R4 (AC16, FC-066 row) only.** 11 of 12 repair checks PASS and are accepted as recorded. The five Phase 4 findings F01–F05 are repaired at their assigned sites; FC-022 and FC-038 are closed. One unlabelled-contract contradiction for the same named `fetchProducts` operation remains in two manuals that the Phase 4 repair did not list. This is a content amendment (AMENDED-v3, labels only, two documents), not an installation or process defect.

| Check | ACs | Executor | QA Lead | Note |
|---|---|---|---|---|
| R1 | AC5, AC6 | PASS | **PASS** | eight ownership spans present once; stale-assertion sweep zero |
| R2 | AC9 | PASS | **PASS** | §17 routes to QA first; tree lists `QAM/` and `ACCEPTANCE_SPEC.md` |
| R3 | AC15 | PASS | **PASS** | zero active "filesystem wins"/"disk wins" |
| R4 | AC16 | FAIL | **FAIL (narrowed)** | FC-022, FC-038 PASS; FC-066 FAIL — see §2 |
| R5 | AC18 | PASS | **PASS** | RUL-13 default in all four manuals |
| R6 | AC2 | PASS | **PASS** | 101/101 = bound index; 94 unchanged byte-identical |
| R7 | AC25/26/27 | PASS | **PASS** | headers unchanged; one amended history row per repaired doc |
| R8 | AC29/AC31 | PASS | **PASS** | lint suite PASS, 0 hits |
| R9 | AC22/23/24/37 | PASS | **PASS** | archives, templates, workflows, 10x byte-unchanged |
| R10 | AC33 | PASS | **PASS** | 12 transitions pending |
| R11 | AC32 | PASS | **PASS** | one non-merge commit after recorded Gate 2; clean tree; main unchanged |
| R12 | AC1 | PASS | **PASS** | seven canonical paths + additive records only |

## 2. Adjudication of RV2-F01 (R4 / AC16 / FC-066) — **CONFIRMED, narrowed**

**What the Executor found.** API_AND_SERVICES_MANUAL §3 (lines 172–174) declares the `fetchProducts` contract: a typed outcome (`success | not-found | unavailable | invalid | forbidden`, `items` only on success), and requires that "any independent alternative is explicitly labelled with its own contract; callers do not silently mix array, paginated and wrapped results." The service module is named at 582 (`// src/services/productServices.ts`) and the caller at 787–814 consumes the outcome correctly. Two other manuals import the same module and consume `fetchProducts()` as a bare `Product[]` with no label:

| Site (candidate lines) | Text | Why it contradicts 172–174 |
|---|---|---|
| APP_ARCHITECTURE_MANUAL.md:505–515 (§5 Server Components) | `import { fetchProducts } from '@/services/productServices'` … `const products = await fetchProducts(); <ProductList products={products} />` | same import path as the declared service; result used as an array without narrowing; no alternative label |
| APP_ARCHITECTURE_MANUAL.md:611–613 (§5 Streaming and Suspense) | `const products = await fetchProducts(); return <ProductList products={products} />` | same operation name in the same section; same unlabelled array use |
| STATE_MANAGEMENT_MANUAL.md:808–813 (§7 Store + Service Layer, ✅ GOOD) | `// src/services/productServices.ts` `export const fetchProducts = async () => { … return response.json(); }` | a second definition of the same module/function returning raw JSON; unlabelled; the "GOOD" label is about store/service separation, not the return contract |
| STATE_MANAGEMENT_MANUAL.md:869–876 (§7 Store + Server Components) | `import { fetchProducts } from '@/services/productServices'` … `<ProductList initialProducts={products} />` with `initialProducts: Product[]` (886) | the declared typed outcome is not a `Product[]`; no narrowing, no label |

Negated or vocabulary-only hits are not contradictions and stay RETAIN: STATE:241, STATE:801 (❌ BAD example), API:183/985/1179 (naming tables), `fetchProductsByIds` (distinct operation, explicit signature).

**Why it is in scope.** AC16's method is fixed by the frozen spec: "grep the withdrawn identifier/function name over live scope", and its requirement covers "every dependent reference (… helper signatures, cross-manual pointers) to the withdrawn recipe". The invariant that AC16(b) requires the replacement text to state is the very sentence at 174, and the frozen map's FC-066 verification intent reads "every occurrence matches one declared contract or a labelled alternative". In the Phase 4 verdict I confirmed F04c on exactly that standard for the API manual's own unlabelled occurrences. Applying a different standard to the same function name, imported from the same module path, in two sibling manuals would be rewriting the criterion to make the failure pass. The Gate 2 propagation rows for these spans were marked CONSISTENT with the explicit note "§F; final review required", so they were never settled; the AMENDED-v2 RETAIN rationale ("not asserted to implement the API typed service") does not hold against an identical `@/services/productServices` import.

**Why it is narrowed, not HIGH.** The Executor graded HIGH. I grade it a confirmed AC16 failure of the same class and size as the API-manual F04c fix: four containers in two documents, resolvable with labels and no new service code. Every span exists at BASE (ARCH 533/538/640, STATE 1103/1119/1162/1166 in BASE numbering), is unchanged through `20f71ee` and `8dff354` (blobs for both manuals identical parent→candidate), and was not among the F04c anchors I issued. The repair implemented the assignment exactly; the under-inclusion is in the Phase 4 anchor list, not in Cody's or Jarvis's work. I record that plainly.

**Rejected alternatives.** (i) Treat the ARCH/STATE examples as "generic project-local" illustrations: the import path names the declared service module; AC16 and line 174 require the label to be explicit, not inferred from a section heading. (ii) Treat them as RETAIN under O-6/O-7 or FU: no override or ruling excludes reference-manual examples from AC16, and the Phase 4 verdict used no such exclusion for the API manual.

## 3. What is preserved

- Phase 4 verdict and its adjudication (F01–F05 CONFIRMED, F06/F07 REJECTED → FU-1/FU-2) stand unchanged; FU-1/FU-2 remain optional and were correctly excluded from this retest.
- Gate 2 approvals (R1 spec, AMENDED-v1, AMENDED-v2) are not reopened; the frozen spec is unchanged.
- Installation and process: `8dff354` is the exact approved AMENDED-v2 patch (R6/R12), one attributable commit after Gate 2 (R11), lint PASS (R8), archives/templates/workflows/10x untouched (R9), 12 closeout transitions pending (R10). These results carry forward to the successor candidate for any document that stays byte-identical.
- No product document was edited, no Git mutation was run, no transition was activated in this adjudication.

## 4. Path to PASS

One bounded content amendment, **AMENDED-v3**, on `APP_ARCHITECTURE_MANUAL.md` and `STATE_MANAGEMENT_MANUAL.md` plus their existing CHANGELOG rows, specified in `JARVIS_REPAIR_RECOMMENDATION.md` (same folder): Jarvis confirms wording → Tony records Gate 2 on AMENDED-v3 → Cody applies, commits, pushes the working branch → fresh Executor runs the bounded retest (R4 FC-066 row; R6, R7, R8, R10, R11, R12 on the new commit; byte-identity check for every other document in place of R1, R2, R3, R5, R9) → Fable successor verdict. No new broad review cycle.

## 5. Independence

I did not author, apply or commit AMENDED-v2, and did not run the retest. All spans above were re-read from git objects at BASE, `20f71ee` and `8dff354` (`rv2_adjudicate.py` → `RV2_ADJUDICATION_EVIDENCE.json`, read-only), not from the Executor's copies alone.
