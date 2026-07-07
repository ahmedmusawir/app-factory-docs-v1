# REVIEW 017: 4_MANUAL-API_AND_SERVICES_MANUAL.md

> **Review Series:** Stark Industries App Factory — Full Doc Stack Audit
> **Reviewer:** Architect Jarvis
> **Date:** 2026-07-06
> **Doc Version Reviewed:** UNVERSIONED (F-018 roster)
> **Tier:** 4 — Reference Manuals
> **Verdict:** KEEP — needs v1.1 (Lesson-2 exception box + metadata + cross-refs)

---

## 1. What This Doc Is

The service-layer bible: "Components render. Services fetch." Four-layer flow (UI → services → API routes → external services), server-vs-client decision tree, integration patterns (WooCommerce, Stripe, Supabase), data transformation, error handling strategy, performance patterns, quick-reference tables.

## 2. Strengths

- The law is clean and quotable; the server-vs-client decision tree is genuinely good agent-routing doctrine.
- Credential-security rationale explicit (keys never reach the client; API routes as secure proxy).
- Hygiene spotless: zero mojibake, zero Stitch, zero versioned refs.
- Pattern quick-reference (webhooks, field mapping, upsert sync, fire-and-forget) — liftable.

## 3. Findings

| ID | Severity | Finding |
|----|----------|---------|
| F-039 | HIGH — unamended root of Lesson 2 | The manual teaches the blanket rule (ALL API calls through `src/services/`) with ZERO kit-capability carve-out — no Kit Audit mention, no auth exception. This is the exact doctrine that produced the Run 001 authService near-miss. Every downstream doc got the antibody (Frontend-First §0, RECON §3, handbook verdict table); the source doc never did. An agent citing this manual can still justify the wrapper. Fix: prominent exception box — "Kit primitives are consumed directly; the kit's auth IS the service layer; service layer = project-specific domain logic; run the Kit Audit (FRONTEND_FIRST §0) before authoring any service." |
| F-018 (roster) | MEDIUM | Completely unversioned: no version block, date, or history. Second consecutive Tier 4 manual refusing to testify. Standard header + v1.0 "(original, date unknown)" history entry. |
| F-035 (roster) | LOW | Outbound half-island: zero factory cross-refs — and this is the doc MOST in need of pointing at FRONTEND_FIRST §0 and the handbook's verdict table (same disease as F-039). Inbound exists via SFP roster. |
| Enrichment note | — | snake_case-wire / camelCase-UI convention (HANDOFF_PACKAGE_PLAYBOOK DATA_CONTRACT discipline) belongs in §7 Data Transformation; currently only file-naming covered. |

## 4. Required Changes for v1.1

1. Add the Lesson-2 exception box (F-039) near the top of §1 — one paragraph closes a two-month-old vulnerability.
2. Standard header block + version-history table.
3. Cross-references section: FRONTEND_FIRST_PLAYBOOK (§0 Kit Audit + service-layer gates), STARTER_KIT_HANDBOOK (verdict table + kit auth), ECOMMERCE_AND_PAYMENTS_MANUAL, DATABASE_MANUAL, TESTING_PLAYBOOK (service unit-testing).
4. Enrichment: wire-format conventions in §7.

## 5. Cross-Doc Dependencies Noted

Inbound: SOFTWARE_FACTORY_PLAYBOOK (manual roster). Outbound: none (finding). Doctrinal relationship: ROOT of Lesson 2 — downstream antibodies live in FRONTEND_FIRST §0, RECON §3, STARTER_KIT_HANDBOOK §11; source never amended (F-039).

---

*Part of the Factory Doc Stack Audit series. See FINDINGS_LOG.md for the running catch list.*
