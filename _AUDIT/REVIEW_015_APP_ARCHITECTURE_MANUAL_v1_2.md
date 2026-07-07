# REVIEW 015: 4_MANUAL-APP_ARCHITECTURE_MANUAL_v1_2.md

> **Review Series:** Stark Industries App Factory — Full Doc Stack Audit
> **Reviewer:** Architect Jarvis
> **Date:** 2026-07-06
> **Doc Version Reviewed:** v1.2 (2026-06-28, Kit Hardening Gate 10)
> **Tier:** 4 — Reference Manuals (TIER OPENER)
> **Verdict:** KEEP — needs v1.3 (version de-pinning + recon pointer, mojibake sweep, canonical refs)

---

## 1. What This Doc Is

The Next.js architecture reference: monolithic-frontend + external-services philosophy, project structure, routing architecture, layout system, rendering strategies, data flow, component architecture (§11 co-location per Lesson 7), server/client boundary (§12 per Lesson 8), external service integration, performance, security.

## 2. Strengths

- Header at top with version/date/born-from ✓; version history table with lesson provenance ✓ ("preserve lesson, swap actor" v1.2 entry).
- Run 001 lessons landed: co-location pattern present with worked ProductPageContent examples; server/client boundary section added v1.1.
- Practical, code-first reference style; architecture-benefit tables; clean layered ToC.
- Zero Stitch, zero recon-era anachronisms (appropriately — it's a stack reference).

## 3. Findings

| ID | Severity | Finding |
|----|----------|---------|
| F-038 | HIGH — stale stack pins | **Manual pins Next.js 15 throughout (6+ instances: subtitle, stack table, §3, code comments) while the kit runs Next.js 16.** This is the exact offender RECON_QUESTIONNAIRE §1 was written about ("global doctrine pins versions that age; package.json is the only truth" — the Cyber Pharma 15-vs-16 conflict is its first table entry). An Architect consuming this manual replays that Discovery-gate conflict. v1.3: de-pin where version-irrelevant ("App Router"); label version-sensitive facts ("params-as-Promise, Next 15+"); add "verify per repo — recon Q1.1" pointer; verify middleware guidance vs Next 16's `src/proxy.ts` (recon Q2.5). |
| F-012 (3rd instance — SYSTEMIC) | MEDIUM | 16 mojibake chars (diagram arrows `â–¼`) in a Gate-10 doc whose v1.1 changelog claims the UTF-8 fix. Third doc with claimed-but-persistent corruption (SFP, Frontend-First, this). **Diagnosis: the editing/export pipeline itself is the corruption source — fixes get re-broken on save.** Identify the tool before the rewrite phase or sweeps repeat forever. |
| F-032 (extended) | MEDIUM | Line 1482 cites `STARTER_KIT_HANDBOOK_v1.0.md` — stale v1.0 reference in a June-28 Gate-10 doc; same zero-hour drift class as Frontend-First §0. Canonical-name rule evidence grows. |

## 4. Required Changes for v1.3

1. Version de-pinning pass (F-038) + recon Q1.1 pointer + proxy/middleware verification.
2. Mojibake sweep (and report the editing-tool diagnosis to the operator).
3. Canonical-name cross-references (STARTER_KIT_HANDBOOK, no suffix).
4. Adopt standard header block when F-018 lands (already close).

## 5. Cross-Doc Dependencies Noted

References: ECOMMERCE_AND_PAYMENTS_MANUAL (canonical ✓), STARTER_KIT_HANDBOOK (stale versioned ref — F-032). Conflicts with: kit reality on Next version (F-038, recon §1 evidence). Should reference: RECON_QUESTIONNAIRE Q1.1/Q2.5 (version ground-truthing).

---

*Part of the Factory Doc Stack Audit series. See FINDINGS_LOG.md for the running catch list.*
