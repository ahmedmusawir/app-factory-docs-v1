# REVIEW 019: 4_MANUAL-AUTH_MANUAL_v1_2.md

> **Review Series:** Stark Industries App Factory — Full Doc Stack Audit
> **Reviewer:** Architect Jarvis
> **Date:** 2026-07-06
> **Doc Version Reviewed:** v1.2 (2026-06-28, Kit Hardening Gate 10)
> **Tier:** 4 — Reference Manuals
> **Verdict:** KEEP — kit-auth authority + F-039 antibody source; v1.3 (refs + history) PLUS F-042 adjudication required

---

## 1. What This Doc Is

The kit auth authority: complete guide to authentication, authorization, and Supabase integration for the Stark SaaS Starter Kit. Opens with the Lesson-2 antibody as §0 ("🛑 DO NOT AUTHOR authService.ts") + the 13-capability kit-provides inventory with consumption paths; covers signup/login flows, admin creation via server actions, protectPage/AppRole gating, the Mark IV handle_new_user trigger.

## 2. Strengths

- **Best header in Tier 4:** version/date/born-from/changelog at top.
- **The F-039 antibody, in the flesh:** the anti-authService doctrine leads the manual, with the anti-pattern shown and correct patterns per context (Server Component / protected route / Client Component). API_AND_SERVICES_MANUAL v1.1 points here.
- **Currency excellent:** `src/proxy.ts` (Next 16 convention) — the model App Architecture v1.3 should follow; zero mojibake.
- Has cross-references (unlike its Tier 4 siblings) — albeit stale-versioned (F-032).

## 3. Findings

| ID | Severity | Finding |
|----|----------|---------|
| F-042 | HIGH — security-classed, THREE-WAY doctrine conflict | **Role-storage doctrine contradiction across three docs:** (1) THIS manual, line 154, as design philosophy: "Metadata-driven roles — roles stored in `user_metadata`, NOT separate tables" (user_roles mentions: 0; get_user_role: 0; Mark IV trigger applies metadata role at creation). (2) RECON_QUESTIONNAIRE Q3.4: roles-in-user_metadata = THE forbidden security smell (named grep). (3) DATABASE_MANUAL: internally split (§2 metadata, §5 user_roles). Substance: metadata roles are safe ONLY with tamper protection (default Supabase updateUser can modify metadata → privilege-escalation vector — the reason the forbidden-smell doctrine exists). Two possible truths: (a) Mark IV deliberately adopted metadata roles WITH protections → RECON Q3.4 is stale and needs rewrite; (b) protections absent → this manual teaches the vulnerability recon hunts. **Operator ground-truth required: inspect Mark IV's metadata write-path (auth hooks / service-role-only writes / restricted claims).** F-041's Database Manual surgery is BLOCKED on this call. |
| F-032 (3rd extension) | MEDIUM | Lines 106–108: `STARTER_KIT_HANDBOOK_v1.0.md`, `COMPONENT_REGISTRY_v1.0.md`, `FRONTEND_FIRST_PLAYBOOK_v1.1.md` — stale versioned refs in a Gate-10 doc (both targets bumped the same day). Third doc in the zero-hour drift class. |
| F-018 (minor) | LOW | Header carries only the v1.2 changelog entry; no full version-history table. |

## 4. Required Changes for v1.3

1. **After F-042 adjudication:** either add the tamper-protection documentation (metadata write-path lockdown, making the doctrine defensible) OR align to a table-based model — and in BOTH cases coordinate the RECON Q3.4 + DATABASE_MANUAL §2 rewrites so the factory speaks ONE role doctrine.
2. Canonical-name cross-refs (strip versions, F-032/F-011).
3. Full version-history table.

## 5. Cross-Doc Dependencies Noted

Antibody target for: API_AND_SERVICES_MANUAL v1.1 (F-039 pointer). Conflicts with: RECON_QUESTIONNAIRE Q3.4 + DATABASE_MANUAL §5 (F-042). Referenced by: STARTER_KIT_HANDBOOK, FRONTEND_FIRST (Kit Audit chain). Currency model for: APP_ARCHITECTURE_MANUAL v1.3 (proxy.ts).

## 6. Open Question for Tony (blocking)

**F-042:** Does the Mark IV kit protect `user_metadata.role` from client-side modification (auth hook / service-role-only writes / restricted update)? One look at the kit's updateUser path settles which of the three doctrines is law.

---

*Part of the Factory Doc Stack Audit series. See FINDINGS_LOG.md for the running catch list.*
