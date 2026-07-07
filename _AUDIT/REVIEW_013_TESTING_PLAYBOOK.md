# REVIEW 013: 3_METHOD-TESTING_PLAYBOOK.md

> **Review Series:** Stark Industries App Factory — Full Doc Stack Audit
> **Reviewer:** Architect Jarvis
> **Date:** 2026-07-06
> **Doc Version Reviewed:** v2.0 (2026-05-11) — ⚠️ tail self-labels "DRAFT" (F-036)
> **Tier:** 3 — Build Methodology
> **Verdict:** KEEP — MODEL DOC content; v2.1 patch (status + history table + end the isolation)

---

## 1. What This Doc Is

The testing bible: ten quick-reference principles, the four-layer strategy (Jest unit → Jest integration → Playwright E2E → manual smoke), diagnostic principles (environment drift first, audit-then-add, skip-and-document, strict/lenient validator pairs), deep backend appendices (Supabase chain mocks, REST fetch mocks, Stripe wrapper-vs-constructor decision tree, discovered-not-declared fixtures), and companion artifacts. Distilled from two production apps with receipts (StarkReads 136 tests; Dockbloxx 182 tests).

## 2. Hygiene Scorecard (cleanest in the audit)

Stitch: 0 · Vitest: 0 / Jest: 59 (aligned with kit reality — never the L8 liar) · Mojibake: 0 · Versioned cross-refs: 0 · Header at top with provenance ✓

## 3. Strengths

- **Ten quotable principles** — esp. 1.3 "tests that pass for the wrong reason are worse than tests that fail" and 1.4 non-negotiable `retries: 0`.
- **Principle 1.6 "Source recon before test writing" (2026-05-11)** — the conceptual ancestor of the RECON_QUESTIONNAIRE, three weeks before it was law. The recon DNA fossil record.
- **D-015: honesty artifacts** — companion trio (CHANGELOG, SECURITY_FINDINGS, CLEANUP_BACKLOG as standard project docs) + skip-and-document as a Factory pattern (defer honestly, never fake or silently delete).
- **Layered document architecture** — principles up top, appendices below; the doc explains its own v1→v2 generalization method (preserve verbatim / promote to principle / supplement).
- Backend-agnostic at the principle level with concrete per-backend appendices — the D-001 pairing pattern at document scale.

## 4. Findings

| ID | Severity | Finding |
|----|----------|---------|
| F-035 | HIGH — orphaned doctrine | **The doc is an island.** Zero outbound factory references (no FFM, Build Phase, Starter Kit Handbook, SFP) AND zero inbound (per Reviews 002/010/012: SFP Phase 8, FFM verification/, Build Phase checklists — none point here). 75KB of testing doctrine undiscoverable by any agent executing the factory's testing phases. Fix: mutual pointers — SFP Phase 8 → here; FFM verification guides → here; Build Phase §9 → here; this doc → STARTER_KIT_HANDBOOK (kit runner/config ground truth). |
| F-036 | LOW — status ambiguity | Tail: "END OF TESTING PLAYBOOK v2.0 DRAFT" vs header "Version 2.0" (no status). Operating as doctrine; label is stale. Also missing a version-history table (provenance prose only). Per D-009, status ambiguity is not left lying around. |
| Enrichment note | — | Post-May verification rituals living in RECON_QUESTIONNAIRE §12 (grep-at-close L17, rm .next between batches L25, fresh baseline L26) are testing lessons; v2.1 here is their natural home (coordinate with RECON v0.5 so they're referenced, not duplicated). |

## 5. Required Changes for v2.1

1. Resolve status: drop DRAFT (or mark explicitly and route for approval); add a version-history table.
2. End the isolation (F-035): add cross-references both directions per above.
3. Absorb/reference the L17/L25/L26 verification rituals (single-source: pick home here, pointer from RECON).
4. Adopt standard header block when F-018 lands (already close to compliant).

## 6. Cross-Doc Dependencies Noted

Current: NONE (the finding). Should reference: STARTER_KIT_HANDBOOK, SOFTWARE_FACTORY_PLAYBOOK (Phase 8), FFM_PLAYBOOK (verification/), FRONTEND_BUILD_PHASE_PLAYBOOK (§9 checklist), RECON_QUESTIONNAIRE (Q1.7 runner check; §12 rituals). Should be referenced by: all of the above.

---

*Part of the Factory Doc Stack Audit series. See FINDINGS_LOG.md for the running catch list.*
