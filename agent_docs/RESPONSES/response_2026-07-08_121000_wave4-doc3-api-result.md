# ✅ WAVE 4 — DOC 3 COMPLETE: API_AND_SERVICES_MANUAL → v1.1

**File:** `4_MANUAL-API_AND_SERVICES_MANUAL.md`

## CHANGES MADE

| # | Change | Finding |
|---|--------|---------|
| 1 | Standard header (v1.1 · 2026-07-08 · Tier 4 · Pairs-with) | F-018 |
| 2 | **🛑 THE KIT EXCEPTION** box directly under "Components render. Services fetch." — kit primitives consumed directly; the kit's auth IS the service layer; service layer = project-specific domain logic; Kit Audit (FRONTEND_FIRST §0) + handbook verdict table before authoring ANY service; AUTH §0 pointer. The two-month-old root of Lesson 2 is amended at the source | F-039 |
| 3 | §7 "Wire-Format Conventions": snake_case wire / camelCase UI; service layer owns the case boundary; tied to the HANDOFF DATA_CONTRACT discipline (the section's own normalize examples now have their stated convention) | enrichment |
| 4 | Cross-References ×6 (FRONTEND_FIRST, STARTER_KIT_HANDBOOK, AUTH, DATABASE, ECOMMERCE, TESTING) — outbound-zero ended | F-035 |
| 5 | Version History (v1.0 "(original, date unknown)" + v1.1) | F-018, D-018 |

## GATES

3-class encoding **0** · `_v` refs **0** · kit-exception box ✓ · wire-format section ✓ · header + history ✓

## THINGS I DIDN'T TOUCH

§§2–6, 8–13 content; the four-layer diagram; the decision tree.

## CONCERNS

- **Pre-existing defect, left alone (outside work order):** the doc contains TWO "## 10. Quick Reference" headings (original §10 at ~line 1440, a second at ~1990, with §§11–13 Webhooks/CRM/Sync between them). Queue a numbering decision (tombstone vs renumber — D-019 applies) for a later touch.

## Suggested commit

wave4(api): v1.1 — Lesson-2 kit exception at the root, wire-format conventions, F-035/F-039
