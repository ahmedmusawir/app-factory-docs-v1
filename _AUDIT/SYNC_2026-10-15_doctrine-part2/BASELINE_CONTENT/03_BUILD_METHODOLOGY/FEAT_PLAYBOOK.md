# FEAT PLAYBOOK
## Feature Modules — Adding Capability to Working Systems

> **Version:** 1.0 · **Date:** 2026-08-10 · **Status:** Active
> **Tier:** 3 — Build Methodology
> **Pairs with:** `SOFTWARE_FACTORY_PLAYBOOK.md` › Module Identity & QA Handoff (Factory-level shared doctrine), `BIM_PLAYBOOK.md` (module mechanics reference — this playbook only states deltas), `BUG_FIX_PLAYBOOK.md`, `QA_PLAYBOOK.md`, `TESTING_PLAYBOOK.md`
> **Owner:** Stark Industries App Factory
> **Provenance:** FEAT-001 (ADK-HARNESS, legacy — read-aloud + copy-everywhere) and the Agent-Home polish pattern from the same pilot campaign.

---

## 1. What a FEAT Is

A **Feature Module** adds user-facing capability to a system that already works. Nothing is broken (that's a FIX), no backend seam changes hands (that's a BIM) — the system gains an ability it didn't have.

Typical FEATs: accessibility features, UI capabilities (copy, read-aloud, panels, home pages), UX polish promoted from QA findings, capability rollouts behind existing plumbing. If implementing the feature forces a contract change or a new backend integration, it's a BIM wearing a costume — reclassify it.

## 2. Shared Doctrine (inherited from the FACTORY level — not restated)

**Module identity and the QA-handoff contract are Factory-wide doctrine** (SOFTWARE_FACTORY_PLAYBOOK › Module Identity & QA Handoff): `<TYPE>-<NNN>-<APP-SLUG>` IDs, the mandatory `ACCEPTANCE_SPEC.md` with `AC*` requirements, the Engineering/QA separation, and QA verdict ownership (QA verdict → Operator final authority → Architect advisory). FEAT inherits these from the Factory level — never from BIM. Module *mechanics* shared with BIM (one-folder package, one CLAUDE.md manager, stage-gate lifecycle, freeze rule, Plan Mode, verify-first, git-zero/cloud-zero, baseline-first regression, per-module failure policy, anti-patterns, Definition of Done) are documented in `BIM_PLAYBOOK.md` §4–§12 and apply to FEATs by reference. Below are the FEAT-specific deltas.

## 3. FEAT-Specific Doctrine

### 3.1 Launch conditions are first-class
Features ride on top of moving systems. Every FEAT manager declares its launch condition in the status line AND in the Operator launch line itself (field pattern: *"Operator launch line (ONLY after BIM-002 closes)"*) — so even if future-you forgets, the manager remembers. Features never share a lane with a risky module: the riskiest module of a campaign carries zero passengers.

### 3.2 Version doctrine: v1 now, v2 seeded, NOT built
Ship the simplest capable version using what the platform already provides (field example: browser-native speech before premium TTS). The upgrade path is designed in — the capability isolated behind ONE swap point (a utility, a service function) — and the v2 design lives as a **seed note in the retrospective**, not as built code, not as new dependencies, not as env vars. Garnish (LLM-generated titles, premium voices, optimistic locking) is named as garnish and deferred out loud.

### 3.3 Scope discipline against feature gravity
Features attract siblings ("while we're adding copy, let's also…"). The manager's OUT-of-scope section says it loud, including: adjacent icons that stay decorative, input modalities not in scope (voice OUT ≠ dictation IN), and restyling beyond wiring what exists. QA-finding-born features cite their finding IDs and carry ONLY the adjudicated findings — rejected findings never smuggle in.

### 3.4 Mode parity — where both modes support the feature
When the application's modes (e.g., mock and live) both support a feature's surface, the feature must behave consistently in both — proven by a gate, not assumed. Some features are legitimately mode-specific; the manager declares mode scope explicitly. A feature that *secretly* depends on a live backend while claiming mode-agnosticism is a misclassified BIM.

### 3.5 Accessibility is not a garnish
When a feature IS the accessibility path (audio-first operators, keyboard paths), it carries normal-priority scheduling and its gates test the accessible experience itself (field gate: *"if it reads markdown symbols aloud, it fails"*).

## 4. FEAT Gates (typical shape)

Numbered `V1…Vn` in the manager: capability works as specified · capability is interruptible/reversible where relevant (stop, undo, revert) · **failure behavior matches the module's declared failure policy** (safe degradation only where losing the capability is explicitly safe — e.g., SSR/missing-API guards on a convenience feature; fail-closed where security, privacy, financial integrity, authorization, tenant isolation, or data integrity demands it) · mock/live parity · zero regression on the surrounding surface — the law: **regression assertions are never weakened merely to accommodate the feature; changes to existing tests must be justified by changed accepted behavior**, each edit listed in the report · green board · `ACCEPTANCE_SPEC.md` delivered.

## 5. Definition of Done — delta only

BIM_PLAYBOOK §12 applies, plus: the v2 seed recorded in the retrospective; any deferred garnish named in the acceptance spec's known-follow-up section so QA doesn't file it as a defect.

## 6. Version History

| Version | Date | Change |
|---|---|---|
| 1.0-DRAFT | 2026-08-10 | Initial playbook from FEAT-001 (ADK-HARNESS, legacy) field experience. |
| 1.0-DRAFT-R2 | 2026-08-10 | QA AMEND pass: inheritance re-pointed to Factory-level doctrine (never BIM-as-constitution); mode-parity rule scoped to features both modes support; byte-unmodified test rule replaced with the no-weakened-assertions law. |
| 1.0 ACTIVE | 2026-08-10 | Finalization pass (F1 registry ref removed; F4 per-module failure-policy wording). Promotion provenance: field campaign → QA engagements → R1 → R2 → final pass. |
