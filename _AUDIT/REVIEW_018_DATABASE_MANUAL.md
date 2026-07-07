# REVIEW 018: 4_MANUAL-DATABASE_MANUAL.md

> **Review Series:** Stark Industries App Factory — Full Doc Stack Audit
> **Reviewer:** Architect Jarvis
> **Date:** 2026-07-06
> **Doc Version Reviewed:** UNVERSIONED (F-018 roster)
> **Tier:** 4 — Reference Manuals
> **Verdict:** KEEP — needs v1.1 with CONTENT SURGERY on the roles section (security-classed) + methodology bridge

---

## 1. What This Doc Is

The Supabase PostgreSQL doctrine: schema-first workflow, schema design patterns, data types reference, relationships/FKs, RLS, indexing, JSONB, TypeScript type generation, query patterns, migration workflow, integrity, performance.

## 2. Strengths

- Comprehensive reference coverage; schema-first rationale table is clear.
- §5 RLS section correctly uses `user_roles` in policies.
- Hygiene clean: zero mojibake, zero Stitch, zero versioned refs.
- Practical query-pattern quick reference.

## 3. Findings

| ID | Severity | Finding |
|----|----------|---------|
| F-041 | HIGH — security-classed content conflict | §2's user-creation example WRITES `role` into `user_metadata` (line ~169) and mirrors to an `app_users.role` column — a pattern the factory itself forbids (kit law: roles in `user_roles` table via `handle_new_user` trigger, resolved server-side via `get_user_role()`; `user_metadata` roles are the forbidden smell recon Q3.4 greps for — client-tamperable in common configs). **The manual would fail its own factory's security grep.** Internally split: §5 RLS uses `user_roles` correctly while §2 teaches the metadata pattern — same doc, two contradictory role doctrines. Fix: rewrite §2 user-sync to the kit pattern + forbidden-pattern warning box. |
| F-040 | MEDIUM — methodology fork unbridged | Schema-first declared universal ("before writing ANY application code... THEN build service layer and UI") with ZERO frontend-first/mock acknowledgment — the factory's flagship methodology inverts this order. Both orders legitimate per context (schema-first: backend phases/conversions; frontend-first: discovery builds). F-030's cousin at build-order level. Fix: "When Schema-First Applies" note + pointer to FRONTEND_FIRST §2. |
| F-018 (roster) | MEDIUM | Unversioned — third consecutive Tier 4 manual with no version/date/history. |
| F-035 (roster) | LOW | Outbound island — zero factory cross-refs. |
| Cleanup note | LOW | `ghl_qr_orders` + 6 GHL mentions — the year-old QR-project fossil (recon Q8.5's target) used as doctrine examples. Scrub to neutral examples in v1.1. |

## 4. Required Changes for v1.1

1. **Roles section surgery (F-041):** replace §2 user-sync with the kit pattern (`user_roles` + `handle_new_user` + `get_user_role()`); add ⛔ forbidden box ("never store/read roles from user_metadata — recon Q3.4 smell"); reconcile with §5 so the doc speaks one role doctrine.
2. "When Schema-First Applies" note + FRONTEND_FIRST §2 pointer (F-040).
3. Standard header block + version-history table; cross-references section (STARTER_KIT_HANDBOOK DB section, AUTH_MANUAL, API_AND_SERVICES_MANUAL, FRONTEND_FIRST_PLAYBOOK).
4. Scrub GHL fossil examples.

## 5. Cross-Doc Dependencies Noted

Conflicts with: kit role architecture + AUTH doctrine + RECON Q3.4 (F-041), FRONTEND_FIRST methodology (F-040 — unacknowledged, not contradicted). Internal conflict: §2 vs §5 role patterns. Inbound: SFP manual roster. Outbound: none (finding). Cross-check at Review 019: AUTH_MANUAL's role doctrine (expected to be the correct source to align §2 against).

---

*Part of the Factory Doc Stack Audit series. See FINDINGS_LOG.md for the running catch list.*
