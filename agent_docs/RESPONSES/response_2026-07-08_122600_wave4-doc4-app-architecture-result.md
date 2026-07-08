# ✅ WAVE 4 — DOC 4 COMPLETE: APP_ARCHITECTURE_MANUAL → v1.3

**Files:** `4_MANUAL-APP_ARCHITECTURE_MANUAL_v1_2.md` + one authorized line in `2_AGENTS-ARCHITECT_PLAYBOOK_v2_1.md`

## CHANGES MADE

| # | Change | Finding |
|---|--------|---------|
| 1 | Standard header (v1.3 · 2026-07-08 · Tier 4) + **the version rule**: this manual pins no framework version — `package.json` is the only truth (recon Q1.1) | F-038, F-018 |
| 2 | De-pins: subtitle + stack table + §3 intro → "Next.js App Router"; version-sensitive facts LABELED — "Async Route Params (Next.js 15+)", "From Next.js 15 onward", code comments "Next.js 15+" ×2; "(Next.js 14 and earlier)" kept as historical context. The GDSH verify-then-fork shape: version-irrelevant facts de-pinned, version-sensitive facts labeled, verification pushed to recon | F-038 |
| 3 | §10 Route Protection: `src/middleware.ts` vs **`src/proxy.ts` (Next 16 kit convention)** note + verify-on-disk pointer (recon Q2.5); code comment annotated | F-038 |
| 4 | Encoding repair: 21 mojibake (▼×11, ►×8, ✅×2) + **17 invisible U+0090 C1 controls** stripped byte-safe (UTF-8, no BOM). **F-012 systemic diagnosis reconfirmed a third time** — a Gate-10 doc whose v1.1 changelog claimed the UTF-8 fix; the corruption signature (U+0090 after `┐` + â-sequences) matches SFP exactly. The editing/export pipeline is the source; the Wave 6 lint must gate on all three classes | F-012 |
| 5 | Handbook cross-ref canonical (line 1482) | F-032 |
| 6 | v1.3 Version History row (existing table extended) | D-018 |
| 7 | **Authorized exception (work-order item 5):** ARCHITECT_PLAYBOOK Example A "Frontend: Next.js 14 (App Router)" → "Next.js (App Router — verify version per repo, recon Q1.1)" — the Wave 2A carry-forward, explicitly named in your order; one line, logged here | F-038 |

## GATES

3-class encoding **0/0/0** · unlabeled `Next.js 15` pins **0** · `_v` live **0** · header + history ✓ · ARCHITECT_PLAYBOOK `Next.js 14` **0**

## THINGS I DIDN'T TOUCH

§§2, 4–9, 11–12 content; the co-location + server/client boundary lessons; Tailwind/TS minor-version rows in the stack table (stack-table versions beyond the framework were not in scope — flagged below).

## CONCERNS

1. Stack table still pins "TypeScript 5" / "Tailwind CSS 3.4" — same F-038 family, milder (kit may run Tailwind 4 per recon Q1.3's token-mechanic note). Not in the work order; queue with the kit-verification touch.
2. F-012 tooling: three docs now show identical re-corruption signatures post-"fix" — identifying Tony's editing tool remains the Wave 0 leftover; every sweep is provisional until then.

## Suggested commit

wave4(app-architecture): v1.3 — de-pin + version rule, proxy note, 3-class encoding repair, F-012/F-032/F-038
