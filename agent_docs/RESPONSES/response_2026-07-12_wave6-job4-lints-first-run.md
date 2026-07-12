# ✅ WAVE 6 JOB 4 — THE FOUR LINTS + FIRST RUN (the free final audit)

> **Date:** 2026-07-12 · Branch `wave6/lints`, commits `bd6745d` + `addbd7e` · PR: https://github.com/ahmedmusawir/app-factory-docs-v1/pull/new/wave6/lints
> Built: `lints/` (common lib + 4 lints + runner + README + .gitignore) + `.github/workflows/doctrine-lint.yml` (push + PR to main).

## FULL LINT OUTPUT (local run, py -3, exit 1)

```
[ENCODING] PASS — 0 hits across 29 live docs
[RETIRED-TERMS] PASS — 0 hits across 29 live docs
01_CONSTITUTION/STARTER_KIT_HANDBOOK.md:258: [VERSIONED-REFS] versioned filename reference 'COMPONENT_REGISTRY_v1.1.md'
01_CONSTITUTION/STARTER_KIT_HANDBOOK.md:261: [VERSIONED-REFS] versioned filename reference 'UI-UX-BUILDING-MANUAL_v1_3.md'
01_CONSTITUTION/STARTER_KIT_HANDBOOK.md:688: [VERSIONED-REFS] versioned filename reference 'AUTH_MANUAL_v1.2.md'
01_CONSTITUTION/STARTER_KIT_HANDBOOK.md:690: [VERSIONED-REFS] versioned filename reference 'UI-UX-BUILDING-MANUAL_v1_3.md'
01_CONSTITUTION/STARTER_KIT_HANDBOOK.md:692: [VERSIONED-REFS] versioned filename reference 'COMPONENT_REGISTRY_v1.1.md'
04_REFERENCE_MANUALS/DATABASE_MANUAL.md:8: [VERSIONED-REFS] versioned prose reference 'AUTH_MANUAL v1.3' — canonical names only
04_REFERENCE_MANUALS/DATABASE_MANUAL.md:156: [VERSIONED-REFS] versioned prose reference 'AUTH_MANUAL v1.3' — canonical names only
05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:2092: [VERSIONED-REFS] versioned filename reference 'THEMING_MANUAL_v1.0.md'
[VERSIONED-REFS] FAIL — 8 hit(s)
01_CONSTITUTION/STARTER_KIT_HANDBOOK.md:1: [HEADER-PRESENCE] missing standard 'Version / Date / Status' header line in the first 10 lines
[HEADER-PRESENCE] FAIL — 1 miss(es)
=== RESULT: FAIL ===
```

## THE 9 FINDINGS (reported, NOT fixed — per operator ruling; content frozen this wave)

| # | File:Line | Lint | Offending text | Class / remedy |
|---|---|---|---|---|
| 1 | STARTER_KIT_HANDBOOK:258 | VERSIONED-REFS | `COMPONENT_REGISTRY_v1.1.md` | F-022 — rides the handbook redo |
| 2 | STARTER_KIT_HANDBOOK:261 | VERSIONED-REFS | `UI-UX-BUILDING-MANUAL_v1_3.md` | F-022 |
| 3 | STARTER_KIT_HANDBOOK:688 | VERSIONED-REFS | `AUTH_MANUAL_v1.2.md` (stale — AUTH is v1.3) | F-022 |
| 4 | STARTER_KIT_HANDBOOK:690 | VERSIONED-REFS | `UI-UX-BUILDING-MANUAL_v1_3.md` | F-022 |
| 5 | STARTER_KIT_HANDBOOK:692 | VERSIONED-REFS | `COMPONENT_REGISTRY_v1.1.md` | F-022 |
| 6 | STARTER_KIT_HANDBOOK:1 | HEADER-PRESENCE | pre-standard header (no Version/Date/Status line) | F-022 (predicted in the plan) |
| 7 | DATABASE_MANUAL:8 | VERSIONED-REFS | `AUTH_MANUAL v1.3` (header banner) | Wave-4 straggler, pre-flagged — de-version in follow-up PR |
| 8 | DATABASE_MANUAL:156 | VERSIONED-REFS | `AUTH_MANUAL v1.3` (§2 ⛔ box) | same |
| 9 | UI_UX_BUILDING_MANUAL:2092 | VERSIONED-REFS | `THEMING_MANUAL_v1.0.md` (Lesson-appendix narrative) | de-version OR relocate under a history heading — follow-up PR |

**Reading:** 6 of 9 findings are the STARTER_KIT_HANDBOOK — the one doc Waves 1–5 never touched. The lint independently re-derived the F-022 case on its first run. ENCODING and RETIRED-TERMS pass 29/29 — the campaign's byte-repair and de-Stitch work held.

## Lint-CODE fixes during build (not doctrine edits)

1. UTF-8 stdout reconfigure (Windows cp1252 console crashed printing `→` in a report line).
2. `CHANGELOG.md` file-level exemption for the section-based lints (a change ledger is all-history by nature; its own heading structure ended the section exemption early). Documented in `lints/README.md`. ENCODING + HEADER-PRESENCE still apply to it.
3. Housekeeping: `__pycache__` artifact dropped from the index + `lints/.gitignore` added (commit `addbd7e`).

## ⚠️ CI note for the operator

`doctrine-lint.yml` runs on this very PR — **it will FAIL with exactly these 9 findings. That is by design** (the watchdog works). Merge judgment is yours: merge with the red check and clear the findings via (a) the small de-version follow-up PR (items 7–9) and (b) the F-022 handbook redo (items 1–6).

## Suggested PR title

Wave 6 Job 4: four doctrine lints + CI (first run: 9 findings reported)
