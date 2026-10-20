# Repair recommendation for Jarvis — AMENDED-v3 (RV2-F01 / AC16 / FC-066)

From Fable (QA Lead), 2026-10-19. Successor to `REPAIR_QA_P4/ENGINEER_REPAIR_PROMPT.md` F04c; same constraints apply. Candidate to repair: `8dff354937bc7baf739370a9886497d9d5359186`. Line numbers are at that candidate.

## 1. Required corrections (labels only; no new service code)

Standard (frozen): API_AND_SERVICES_MANUAL.md:174 — "A named operation uses one parameter signature and typed result envelope in its service, route and client examples. Any independent alternative is explicitly labelled with its own contract; callers do not silently mix array, paginated and wrapped results." Each container below must either be explicitly labelled as an independent illustration with its own stated return contract, or be rewritten to consume the §3 typed outcome. I recommend labels, mirroring the approved E390/E394 pattern, because the examples teach rendering and state placement, not the service contract.

| # | Document : lines | Container | Correction (Jarvis fixes exact wording) |
|---|---|---|---|
| V3-1 | `04_REFERENCE_MANUALS/APP_ARCHITECTURE_MANUAL.md:499–501` | §5 "Server Components (Default)" — the sentence before the fence | Add one sentence after line 499, before the fence at 501: *"Independent rendering illustration: the `fetchProducts()` used in this section returns `Promise<Product[]>` and is not the API manual §3 typed-outcome service; a project implementing the §3 contract narrows `status === 'success'` and passes `items` to the list."* Optionally add the comment `// Independent illustration: returns Promise<Product[]> (see note above §5 example)` as a fence line after 503. |
| V3-2 | `04_REFERENCE_MANUALS/APP_ARCHITECTURE_MANUAL.md:610–613` | §5 "Streaming and Suspense" — `ProductListAsync` | Covered by the V3-1 sentence if it says "in this section"; otherwise add a fence comment after 610: `// Same independent Promise<Product[]> illustration as the Server Component example above.` One of the two is required so the streaming fence is not an unlabelled second occurrence. |
| V3-3 | `04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:808–810` | §7 "Store + Service Layer", ✅ GOOD fence | Replace the comment at 809 (`// src/services/productServices.ts`) with two comment lines: `// src/services/productServices.ts — independent store/service-separation illustration` and `// this local fetchProducts() returns the route's raw JSON array; it is not the API manual §3 typed-outcome service`. Keep the code unchanged. |
| V3-4 | `04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:865–867` | §7 "Store + Server Components" — the sentence before the fence | Extend line 865 with one sentence: *"This illustration's `fetchProducts()` returns `Promise<Product[]>` (hence `initialProducts: Product[]`) and is not the API manual §3 typed-outcome service; under that contract, narrow `status === 'success'` and pass `outcome.items`."* |

Not acceptable: a caller silently consuming a shape the declared service does not return; a "GOOD/BAD" or section label standing in for a return-contract label; changing the import path or adding a new `productServices` implementation.

Leave as RETAIN (not contradictions): STATE:241 and API:183/985/1179 (naming vocabulary), STATE:798–806 (❌ BAD example), API:942–955 `fetchProductsByIds` (distinct operation).

## 2. Must not change

Identical to `ENGINEER_REPAIR_PROMPT.md` §2: headers (ARCH v1.4 / STATE v1.3, date 2026-10-18, Status Active) unchanged; no new history or CHANGELOG rows — amend the existing 2026-10-18 rows: ARCH:1286 and STATE:1110 history rows and CHANGELOG:56/60, appending the clause `; QA-P4 repair: RV2-F01 (AC16/FC-066 labels)` in the same style as the AMENDED-v2 rows (CHANGELOG:43/54/55/57). API_AND_SERVICES_MANUAL.md and the other four repaired documents unchanged. Archives, templates, workflows, SVGs, `10x Lab/`, `_SKILLS/`, lints, `.github/`, root files untouched. 12 closeout transitions pending. Frozen records (R1 spec, maps, Gate 2 records, Phase 4 verdict, AMENDED-v2 records) untouched; AMENDED-v3 records are additive under `RUN/AMENDED_V3/`.

## 3. Records to produce (`RUN/AMENDED_V3/`)

Same shape as AMENDED-v2: edits numbered E410+, `AMENDMENT_V3_EDITS.json`, `EXECUTION_PROPOSAL_INDEX.json` and `BOUND_EXECUTION_INDEX.json` (101 paths; three changed: ARCH, STATE, CHANGELOG; 98 unchanged byte-identical to `8dff354`), `-p0` patch passing `git apply --check` at `8dff354`, `PROPOSED_CONTENT/` for the three files, identities, verification, and a `PROPAGATION.tsv` sweep for `fetchProducts` / `services/productServices` over live scope with every hit dispositioned (expected: all API-manual hits RETAIN as labelled; ARCH 4 and STATE 7 hits RETAIN as labelled/negated/vocabulary after the fix).

## 4. Acceptance criteria for the bounded retest (fresh Executor)

- **R4′ (AC16, FC-066 row):** grep `fetchProducts` and `services/productServices` over live scope; every hit is (a) inside the labelled §3 typed-outcome examples, (b) inside an explicitly labelled independent illustration whose stated return shape matches its own consumer, (c) a ❌ negated example, or (d) naming vocabulary with no result shape. FC-022/FC-038 and the other 28 withdrawal rows unchanged from the AMENDED-v2 retest.
- **R6′ (AC2):** 101/101 = AMENDED-v3 bound index; 98 unchanged byte-identical to `8dff354`.
- **R7′ (AC25/26/27):** headers unchanged; MANIFEST unchanged; 39 CHANGELOG rows; one amended existing history row in each of ARCH and STATE.
- **R8′ (AC29/AC31):** lint suite PASS, 0 hits; lints/.github unchanged.
- **R10′ (AC33):** 12 transitions pending.
- **R11′ (AC32):** one non-merge commit `repair QA-P4 RV2-F01 (AMENDED-v3 <index sha>)` on `docs/sync-doctrine-part2-2026-10-15` after Tony's recorded Gate 2; no main write; clean tree.
- **R12′ (AC1):** changed paths = ARCH, STATE, CHANGELOG + additive `RUN/AMENDED_V3/**` and `RUN/AMENDED_V3_EXECUTION/**` records only.
- **Carry-forward:** R1, R2, R3, R5, R9 are not re-run; the Executor verifies that every document they graded is byte-identical to `8dff354` and records the carry-forward.

## 5. Sequence and stops

a. Jarvis confirms or edits the wording in §1 (no scope beyond the four containers). b. Cody prepares `RUN/AMENDED_V3/` in the review repo (no execution-worktree writes). c. **STOP** for Tony's Gate 2 record on AMENDED-v3 (additive `DIRECTOR_DECISIONS_V3.md`). d. Cody applies, verifies, commits and pushes the working branch under the existing Git authorization. e. Fresh Executor runs §4; Fable issues the successor verdict. No merge, closeout or release before that verdict.
