# REVIEW 010: 3_METHOD-FFM_PLAYBOOK.md

> **Review Series:** Stark Industries App Factory — Full Doc Stack Audit
> **Reviewer:** Architect Jarvis
> **Date:** 2026-07-06
> **Doc Version Reviewed:** v1.1 (2026-06-18; Gate M added after RUN_002)
> **Tier:** 3 — Build Methodology (TIER OPENER; largest doc in the factory, 107KB)
> **Verdict:** KEEP — needs v1.2 (recon Stage 0 + Role 1 modernization + de-Stitch); §4 promoted upward

---

## 1. What This Doc Is

The FFM authoring manual: what a Frontend-First Module is, the four-role factory pattern (Designer → Extractor → Architect → Engineer), FFM folder anatomy, the two variants (Conversion vs Greenfield) with a decision router, one-FFM-per-phase scoping, a 14-step authoring sequence, file-by-file authoring guides for every artifact, Brain Drain integration, kit bridging, stumbles, checklists, evolution/versioning rules, worked examples, boot prompts, and template stubs. The factory's operational centerpiece.

## 2. Strengths

- **Exemplary header hygiene:** version block at TOP (F-018-correct), canonical-name cross-references (F-011-correct). The hygiene model for Tier 3.
- **§4 Two FFM Variants — the F-030 fix already written.** Conversion vs Greenfield fully specified: per-variant `_design/`/`_extraction/` contents, DATA_CONTRACT/UI_SPEC sourcing, failure modes, and a 3-question operator router. Promote this upward into the Blueprint (and Handoff Playbook preamble).
- **§19 Evolution loop (D-013):** structural-vs-project lesson split — structural lessons promote to playbook/skill updates; project-specific lessons stay in the retrospective. The routing rule the Doctrine Hub PR flow needs.
- Gate M changelog (v1.1) — Rule Zero as an enforced gate after RUN_002 shipped without a mobile shell; lessons → gates in action.
- Sub-Phase vocabulary ("Sub-Phase 0 Discovery") cleanly disambiguates from project Phases — the best phase-naming pattern in the stack; candidate convention for the canonical phase map (F-010).
- Vendor-neutral entry points (CLAUDE.md / AGENTS.md / GEMINI.md → one navigation contract).

## 3. Carried-Check Results

| Check | Result |
|---|---|
| F-015 (Vitest lie in FFM CLAUDE.md template) | ✅ **RESOLVED** — zero test-runner claims anywhere in the doc. The lie was removed rather than corrected: the honest fix (the runner is recon's job to verify, not doctrine's to assert). |
| F-024 (recon pairing) | ❌ **CONFIRMED + WIDENED** — zero recon references in the entire doc; §7 authoring sequence starts at "scaffold," no recon step. Recon Questionnaire claims to be "Stage 0 of the four-role pattern"; the FFM has never heard of it. One-directional pairing, in a doc updated June 18 (recon was law by June 7). |

## 4. Findings

| ID | Severity | Finding |
|----|----------|---------|
| F-031 | HIGH — stale role contract | Role 1 (Designer) + `_design/` contract are pre-Designer-v2.0: outputs listed as brand tokens, style tile, wireframes, "Stitch output" (4 Stitch references, 9 days post-retirement). No token file as primary deliverable, no token-driven HTML, no Playwright PNG, no Canonical Page Method. Downstream update never happened when Designer v2.0 shipped. |
| F-024 (widened) | HIGH | See carried-check result. Fix: §7 gains "Step 0 — Recon" (stark-recon / RECON_QUESTIONNAIRE, current report required before authoring); four-role diagram gains the recon input. |
| F-029 (instance) | — | §7 step 4: Architect authors DATA_CONTRACT — aligned with Handoff Playbook, conflicts with Engineer Playbook/Blueprint. Per-pipeline resolution (F-029) covers this; FFM sits on the conversion side. |
| F-002 (instance) | — | 4 Stitch references (lines 79, 95, 103, 406). Fold into F-031's Role 1 rewrite. |

## 5. Required Changes for v1.2

1. Add Step 0 — Recon to §7 (current Recon Report required; cite RECON_QUESTIONNAIRE + stark-recon); add recon to the four-role diagram flow.
2. Rewrite Role 1 + `_design/` guides to Designer Playbook v2.0 deliverables (token file primary, style tile HTML+PNG, screen HTML+PNG, component manifest); remove all Stitch references.
3. Add per-pipeline DATA_CONTRACT ownership note (coordinate F-029 resolution).
4. Coordinate upward promotion of §4 variant logic into Blueprint v2.1 / Handoff Playbook v1.1 (F-030) — FFM keeps the detailed version; constitution gets the router summary.

## 6. Cross-Doc Dependencies Noted

Pairs with (header, canonical names ✓): HANDOFF_PACKAGE_PLAYBOOK, APP_FACTORY_SKILLS_PLAYBOOK, SOFTWARE_FACTORY_PLAYBOOK, ARCHITECT_PLAYBOOK, ENGINEER_PLAYBOOK. Missing link: RECON_QUESTIONNAIRE (F-024). Stale link era: DESIGNER_PLAYBOOK pre-v2.0 (F-031). Feeds: F-030 fix (§4 promotion), F-010 fix (Sub-Phase convention).

---

*Part of the Factory Doc Stack Audit series. See FINDINGS_LOG.md for the running catch list.*
