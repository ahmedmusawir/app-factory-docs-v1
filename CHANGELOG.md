# CHANGELOG — App Factory Doctrine

> **Version:** 1.0 · **Date:** 2026-07-12 · **Status:** Active
> **Tier:** none — repository infrastructure · **Pairs with:** MANIFEST, _ARCHIVE/README

> Gate-ledger style change feed (D-007 pattern): one line per campaign wave / doc bump, newest last. Every entry cites finding IDs from the 2026-07 Grand Audit (`_AUDIT/FINDINGS_LOG.md`).

## The Rewrite Campaign (2026-07 Grand Audit → Waves 1–6)

| Date | Wave | Scope | Finding IDs |
|---|---|---|---|
| 2026-07-07 | W1 — Pipeline Story | APP_FACTORY_BLUEPRINT v2.1 (Phase 0 recon + pipeline router) · SOFTWARE_FACTORY_PLAYBOOK v1.2 (Phase 2 defers to Designer, phase map) · HANDOFF_PACKAGE_PLAYBOOK v1.1 (pipeline preamble, greenfield variant) | F-002, F-003, F-008, F-009, F-010, F-011, F-012, F-018, F-029, F-030, F-035 |
| 2026-07-07 | W2A — Agent Tier Sync | ARCHITECT_QUESTIONNAIRE v2.2 (F-017 single-source merge) · ARCHITECT_PLAYBOOK v2.2 (§3/§5 → pointers, diagram fix) · RECON_QUESTIONNAIRE v0.5 (tombstones, Q3.4 nuance) · DESIGNER_PLAYBOOK v2.1 (F-025 token-file ruling) | F-002, F-011, F-016, F-017, F-018, F-023, F-024, F-025, F-042 |
| 2026-07-07 | W2B — Engineer Rewrite | ENGINEER_PLAYBOOK v1.2 (two-track restructure, recon-executor role, handoff inputs fix, Karpathy marked all-agent) | F-018, F-026, F-027, F-028, F-029; D-011 |
| 2026-07-07/08 | W3 — Method Tier Sync | FFM_PLAYBOOK v1.2 (Step 0 recon, Role 1 → Designer v2.0) · FRONTEND_FIRST v1.1.3 · FRONTEND_BUILD_PHASE v1.2.1 (F-034 character repair) · TESTING_PLAYBOOK v2.1 (isolation ended) · SKILLS_PLAYBOOK v1.1 (de-Stitch, CWD rule) | F-002, F-010, F-011, F-012, F-024, F-029, F-031, F-032, F-033, F-034, F-035, F-036, F-037 |
| 2026-07-08 | W4 — Manual Tier Sync | AUTH_MANUAL v1.3 (F-042 table-role correction) · DATABASE_MANUAL v1.1 (F-041 surgery) · API_AND_SERVICES v1.1 (Kit Exception) · APP_ARCHITECTURE v1.3 (de-pin) · STATE v1.1 · ECOMMERCE v1.1 (scope declaration) · STRIPE_SUBSCRIPTIONS v1.1 (territory) | F-011, F-012, F-018, F-032, F-035, F-038, F-039, F-040, F-041, F-042 |
| 2026-07-08 | W5 — Design Tier Sync | GDSH v1.1 (--role-* into the contract) · TOKEN_FILE v1.2 (role values minted) · THEMING v1.2 (v1.1 entry restored, phantom killed) · UI_UX v1.4 (phantom extinct) · THEME_LIBRARY v1.2 · COMPONENT_REGISTRY v1.1-tag | F-011, F-012, F-013a, F-018, F-025, F-032, F-033, F-043 |
| 2026-07-10/12 | W6 — Doctrine Hub | Step 0 rename-primitive proof · 27 renames + tier folders (canonical live names) · _ARCHIVE snapshot rule · MANIFEST + CHANGELOG + dependency map · RECON_WAVE0 archived to _AUDIT/ · lints (Job 4, pending) | F-004, F-007, F-011, F-018 |

## Ongoing entries

> On every doc bump, append: `| date | doc vX.Y | one-line change | finding/lesson IDs |` — and archive the outgoing version per `_ARCHIVE/README.md`.

| 2026-08-05 | QA_PLAYBOOK v0.1 | New doc entering Hub: QA doctrine — evidence discipline, risk-based planning, Gate Q/D, defect routing, release-complete criteria | navbar-saga |
| 2026-08-05 | BUG_FIX_PLAYBOOK v0.1 | New doc entering Hub: bug-fix doctrine — evidence-first lifecycle, root-cause mechanism rule, regression protection, Gate Q/D, scope control | navbar-saga |
| 2026-08-05 | STATE_MANAGEMENT_MANUAL v1.2 | Navbar Saga promotion — Division of Labor subsection appended to §1 (server props vs. client stores hard rule); cross-ref to AUTH_MANUAL Navbar Law added | navbar-saga |
| 2026-08-05 | FRONTEND_BUILD_PHASE_PLAYBOOK v1.2.2 | Navbar Saga promotion — Gate Q/D checklist items appended to §9 (pointers to QA_PLAYBOOK + BUG_FIX_PLAYBOOK; never duplicated doctrine) | navbar-saga |
| 2026-08-05 | AUTH_MANUAL v1.4 | Navbar Saga promotion — new § "Server-Resolved Identity for UI (The Navbar Law)" inserted after Server-Side Protection (RBAC); four hard rules | navbar-saga |
| 2026-08-10 | BIM_PLAYBOOK v1.0 | New doc entering Hub: Backend Integration Module doctrine — module identity & package anatomy, stage-gate lifecycle, ACCEPTANCE_SPEC handoff, QA engagement, contracts/seams, anti-patterns. From the ADK Harness pilot campaign | factory-module-doctrine |
| 2026-08-10 | FEAT_PLAYBOOK v1.0 | New doc entering Hub: Feature Module doctrine — launch conditions, v1-now/v2-seeded, scope discipline, mode parity, accessibility gates; mechanics inherited from BIM_PLAYBOOK by reference | factory-module-doctrine |
| 2026-08-10 | QA_PLAYBOOK v1.0 | Field-tested supersession of v0.1 (archived) — claim-package handoff, contract extraction, one-test-at-a-time protocol, environment triage, exploratory seam testing, finding classification, verdict model, scope protection, 10 field lessons. Header translated to Hub single-line; history reordered newest-last | factory-module-doctrine |
| 2026-08-10 | QA_PLAYBOOK v1.1 | AC-numbering sync (Finalization F6): AC*/gate-ID distinct-families note at §7; legacy gate-ID labels on FIX-002 field-evidence examples (§7, §15); no renumbering — historical evidence stays historically true | factory-module-doctrine |
| 2026-08-10 | BUG_FIX_PLAYBOOK v1.0 | Seamless merge of the field amendments kit (v0.1 archived): role additions (git-zero Engineer, QA verdict ownership, Architect-advises), cross-module repair commits, ACCEPTANCE_SPEC as required artifact, app-suffixed BUG_REPORT header, new §16 FIX Module Anatomy + §17 Module Identity + §22 Field Case Studies (FIX-001/002/003) | factory-module-doctrine |
| 2026-08-10 | SOFTWARE_FACTORY_PLAYBOOK v1.3 | New §2.5 "Module Identity & QA Handoff" (Factory-wide — governs BIM, FIX, FEAT, and future module types): app-suffixed IDs, ACCEPTANCE_SPEC contract, AC* numbering, QA verdict ownership + Operator final authority. Fractional section number follows the file's own §1.5 precedent (v1.2 archived) | factory-module-doctrine |

---

🥄 *Part of Stark Industries — App Factory doctrine.*
