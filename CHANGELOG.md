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

---

🥄 *Part of Stark Industries — App Factory doctrine.*
