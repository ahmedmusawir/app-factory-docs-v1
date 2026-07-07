# REVIEW 008: 2_AGENTS-ENGINEER_PLAYBOOK_v1_1.md

> **Review Series:** Stark Industries App Factory — Full Doc Stack Audit
> **Reviewer:** Architect Jarvis
> **Date:** 2026-07-06
> **Doc Version Reviewed:** 1.1 (February 2026 — see F-027)
> **Tier:** 2 — Pipeline Agents
> **Verdict:** KEEP core doctrine — needs v1.2 STRUCTURAL update (largest change list in Tier 2)

---

## 1. What This Doc Is

The Engineer Agent's manual: role, inputs, systems-discipline philosophy, CLI-first pattern, file-based state contracts, build sequence, testing strategy, cloud-native engineering (GCS/ADC), provider abstraction, DATA_CONTRACT template, handoff, anti-patterns, plus §15 Karpathy Protocol (agentic behavior constitution) and §16 Session Memory Protocol.

## 2. Strengths

- **§15 Karpathy Protocol — best agent-behavior doctrine in the stack (D-011).** Assumption surfacing, confusion management (STOP on ambiguity), push-back duty + anti-sycophancy, simplicity enforcement, Tony's Rule (scope discipline), dead-code hygiene, output standards (CHANGES/DIDN'T TOUCH/CONCERNS). Applies to ALL agents — extraction to constitution level recommended.
- **§16 Session Memory Protocol (D-012)** — tool-agnostic session files; ancestor of the Gate-ledger change-feed pattern (D-007).
- Timeless systems core: explicit/testable/swappable pillars, files-as-contracts, "orchestration comes last," clean-venv truth-test, provider abstraction with registry pattern, cloud limits as design inputs.

## 3. Findings

| ID | Severity | Finding |
|----|----------|---------|
| F-026 | HIGH — handoff protocol mismatch | Engineer §2 inputs: APP_BRIEF, UI_SPEC, screen screenshots, gating, checkpoints. Designer v2.0 §10 ships: token file (PRIMARY), style tile, HTML+PNG artifacts, UI_SPEC, component manifest. The receiving side omits the token file and HTML build references — the load-bearing items. Two halves of one handshake describe different packages. Cross-check HANDOFF_PACKAGE_PLAYBOOK at Review 009 for a third opinion. |
| F-027 | HIGH — doc frozen pre-modern-factory | v1.1 dated February 2026. Missing everything defining Claudy's current job: recon-executor role (Claudy ANSWERS the Recon Questionnaire — absent from his own manual), Phase-0 handbook read, Kit Audit, FFM execution mode (his primary work per FRONTEND_BUILD_PHASE_PLAYBOOK), all Run 001 / Cyber Pharma lessons. Designer + Architect went through June v2.x cycles; Engineer stayed at February. |
| F-028 | MEDIUM — center-of-gravity mismatch | Spine (§6–§9) is Python/pytest/venv/CLI-pipeline. Correct for Backend Bundle + Local-First types, but the factory's dominant lane (Next.js/TS starter kit) gets one sentence. v1.2 restructure: common doctrine (systems discipline + §15 + §16) + two tracks — Kit Track (recon → Phase 0 → FFM; points at METHOD playbooks) and Pipeline Track (existing Python material, retained). |
| F-018 (instance) | LOW | Version block at footer. Standard top header in v1.2. |

## 4. Required Changes for v1.2

1. Rewrite §2 inputs to match the Designer v2.0 handoff package verbatim (token file, style tile, HTML+PNG, UI_SPEC, component manifest) — resolve jointly with F-026/Review 009.
2. Add the Engineer's recon-executor role (answers RECON_QUESTIONNAIRE read-only, produces Recon Report) + Phase-0 handbook read + Kit Audit references.
3. Add FFM-execution as the primary Kit-Track work mode; cross-reference FFM_PLAYBOOK + FRONTEND_BUILD_PHASE_PLAYBOOK.
4. Restructure into common doctrine + Kit Track / Pipeline Track (F-028).
5. Extract §15 (Karpathy Protocol) to constitution level (or Blueprint), leaving a pointer — it governs all agents.
6. Standard top header; fold Run 001 / Cyber Pharma lesson references where relevant.

## 5. Cross-Doc Dependencies Noted

Conflicts with: DESIGNER_PLAYBOOK §10 (F-026). Missing links to: RECON_QUESTIONNAIRE, STARTER_KIT_HANDBOOK, FFM_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK §0. References: APP_BRIEF, UI_SPEC, DATA_CONTRACT (template owner). Check at Review 009: HANDOFF_PACKAGE_PLAYBOOK's description of the same handshake.

---

*Part of the Factory Doc Stack Audit series. See FINDINGS_LOG.md for the running catch list.*
