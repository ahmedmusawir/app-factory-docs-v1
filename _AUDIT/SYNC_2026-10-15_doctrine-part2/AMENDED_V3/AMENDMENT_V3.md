# AMENDED-v3 — exact label-only proposal

ENGINEER-PROPOSED. Jarvis wording confirmed by Tony; exact-patch Gate 2 PENDING. Candidate `8dff354937bc7baf739370a9886497d9d5359186`. Four required containers, with explicit V3-2 streaming comment included. No optional V3-1 fence comment needed: its sentence directly precedes the fence.

Three canonical paths: ARCH, STATE, CHANGELOG; 98 unchanged of101. Eight new edits E410–E417. Existing headers/dates/imports/executable code preserved. Frozen records and all prior repairs untouched; twelve transitions pending. SELECTED_EXACT_EDITS retains409 historical records; replay only E410+ against this candidate, not the whole provenance list against BASE.

## E410 / V3-1 — 04_REFERENCE_MANUALS/APP_ARCHITECTURE_MANUAL.md:499

Old:
````text
By default, all components in the App Router are Server Components:
````

New:
````text
By default, all components in the App Router are Server Components:

Independent rendering illustration: the `fetchProducts()` used in this section returns `Promise<Product[]>` and is not the API manual §3 typed-outcome service; a project implementing the §3 contract narrows `status === 'success'` and passes `items` to the list.
````

## E411 / V3-2 — 04_REFERENCE_MANUALS/APP_ARCHITECTURE_MANUAL.md:610

Old:
````text
// Async component that fetches data
````

New:
````text
// Async component that fetches data
// Same independent Promise<Product[]> illustration as the Server Component example above.
````

## E412 / V3-3 — 04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:809

Old:
````text
// src/services/productServices.ts
````

New:
````text
// src/services/productServices.ts — independent store/service-separation illustration
// this local fetchProducts() returns the route's raw JSON array; it is not the API manual §3 typed-outcome service
````

## E413 / V3-4 — 04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:865

Old:
````text
Server Components cannot use hooks, but they can pass initial data to Client Components:
````

New:
````text
Server Components cannot use hooks, but they can pass initial data to Client Components: This illustration's `fetchProducts()` returns `Promise<Product[]>` (hence `initialProducts: Product[]`) and is not the API manual §3 typed-outcome service; under that contract, narrow `status === 'success'` and pass `outcome.items`.
````

## E414 / HISTORY — 04_REFERENCE_MANUALS/APP_ARCHITECTURE_MANUAL.md:1286

Old:
````text
| 1.4 | 2026-10-18 | Factory DocSet sync: approved workflow/security/reference corrections; preserved original; explicit exclusions per doctrine-part2 map. IDs: FC-001, FC-009, FC-021, FC-028, FC-033, FC-035, FC-036, FC-041, FC-042, FC-063, FC-066, FC-071, MC-01, RUL-11 |
````

New:
````text
| 1.4 | 2026-10-18 | Factory DocSet sync: approved workflow/security/reference corrections; preserved original; explicit exclusions per doctrine-part2 map. IDs: FC-001, FC-009, FC-021, FC-028, FC-033, FC-035, FC-036, FC-041, FC-042, FC-063, FC-066, FC-071, MC-01, RUL-11; QA-P4 repair: RV2-F01 (AC16/FC-066 labels) |
````

## E415 / CHANGELOG — CHANGELOG.md:56

Old:
````text
| 2026-10-18 | APP_ARCHITECTURE_MANUAL v1.4 | Factory DocSet sync; preserved outgoing original; MC correction pass | FC-001, FC-009, FC-021, FC-028, FC-033, FC-035, FC-036, FC-041, FC-042, FC-063, FC-066, FC-071, MC-01, RUL-11 |
````

New:
````text
| 2026-10-18 | APP_ARCHITECTURE_MANUAL v1.4 | Factory DocSet sync; preserved outgoing original; MC correction pass; QA-P4 repair: RV2-F01 (AC16/FC-066 labels) | FC-001, FC-009, FC-021, FC-028, FC-033, FC-035, FC-036, FC-041, FC-042, FC-063, FC-066, FC-071, MC-01, RUL-11 |
````

## E416 / HISTORY — 04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:1110

Old:
````text
| 1.3 | 2026-10-18 | Factory DocSet sync: approved workflow/security/reference corrections; preserved original; explicit exclusions per doctrine-part2 map. IDs: FC-035, FC-040, FC-046, FC-046-heading, FC-047, FC-048, FC-049, FC-055, FC-067, FC-068, RUL-11, RUL-13 |
````

New:
````text
| 1.3 | 2026-10-18 | Factory DocSet sync: approved workflow/security/reference corrections; preserved original; explicit exclusions per doctrine-part2 map. IDs: FC-035, FC-040, FC-046, FC-046-heading, FC-047, FC-048, FC-049, FC-055, FC-067, FC-068, RUL-11, RUL-13; QA-P4 repair: RV2-F01 (AC16/FC-066 labels) |
````

## E417 / CHANGELOG — CHANGELOG.md:60

Old:
````text
| 2026-10-18 | STATE_MANAGEMENT_MANUAL v1.3 | Factory DocSet sync; preserved outgoing original; MC correction pass | FC-035, FC-040, FC-046, FC-046-heading, FC-047, FC-048, FC-049, FC-055, FC-067, FC-068, RUL-11, RUL-13 |
````

New:
````text
| 2026-10-18 | STATE_MANAGEMENT_MANUAL v1.3 | Factory DocSet sync; preserved outgoing original; MC correction pass; QA-P4 repair: RV2-F01 (AC16/FC-066 labels) | FC-035, FC-040, FC-046, FC-046-heading, FC-047, FC-048, FC-049, FC-055, FC-067, FC-068, RUL-11, RUL-13 |
````

