# REVIEW 002: SOFTWARE_FACTORY_PLAYBOOK_v1_1.md

> **Review Series:** Stark Industries App Factory — Full Doc Stack Audit
> **Reviewer:** Architect Jarvis
> **Date:** 2026-07-02
> **Doc Version Reviewed:** 1.1 (Last Updated 2026-05-31, born from Cyberize Run 001)
> **Tier:** 1 — Constitution
> **Verdict:** KEEP — needs v1.2 (see Required Changes)

---

## 1. What This Doc Is

The process spine. Distinct from the Blueprint: the Blueprint defines the *agent pipeline* (Architect → Designer → Engineer, project lifecycle); this playbook defines the *feature build sequence* (9 phases: Planning → Design → Database → API → State → UI → Auth → Testing → Deployment). Includes the Human-Architect/AI-Builder philosophy, per-phase templates, feature spec template, and execution checklists.

## 2. Strengths

- **§1.5 Doctrine Pairing Principle — the strongest doctrine in the stack.** Playbook + worked example, always paired, with an explicit example lifecycle (born → refined → canonical → archived) and post-run sync rules. Should be promoted to constitution level.
- "Why This Order?" dependency table — teaches the reasoning, not just the sequence.
- §13 checklists (feature dev, code review, QA) — directly executable by agents.
- User story format + worked example (§3) follows its own pairing principle.
- Version history with run lineage ("born from Cyberize Run 001").

## 3. Findings

| ID | Severity | Finding |
|----|----------|---------|
| F-009 | HIGH — stale process | Phase 2 (Design System) shows `User Story → Google Stitch or Figma → Design Output` and describes a design-spec-doc workflow. This is not just a stale tool name — it is a competing design process that contradicts the Blueprint v2.0 / Designer Playbook method (token-driven HTML → Playwright PNG, Canonical Page Method). Phase 2 needs a rewrite that defers to DESIGNER_PLAYBOOK. |
| F-010 | HIGH — structural ambiguity | Two phase systems with no bridge: Blueprint's 5 project-lifecycle phases vs this doc's 9 feature-build phases. Compatible in practice (9-phase sequence ≈ inside Blueprint's Fabrication), but neither doc states the relationship. One bridging paragraph in each doc resolves it. |
| F-011 | MEDIUM — reference hygiene | §1.5 pairing table cross-references docs by versioned filename (`UI-UX-BUILDING-MANUAL_v1.1.md`, `FRONTEND_FIRST_PLAYBOOK_v1.1.md`); stack now holds v1.4 and v1.1.1. Proposal (stack-wide rule): cross-reference by canonical name only; MANIFEST owns versions. |
| F-012 | LOW — cosmetic/regression | UTF-8 mojibake still present throughout diagrams (`──â–º`, `â–¼`, `âœ…`) despite v1.1 changelog claiming the encoding fix. Candidate for automated lint later. |
| (F-004 confirm) | — | Knowledge-base diagram lists 7 manuals; §14 lists 7; stack has ~27 docs. Master-index gap pattern repeats. Already filed. |

## 4. Required Changes for v1.2

1. Rewrite Phase 2 to defer to DESIGNER_PLAYBOOK (token-driven HTML → Playwright PNG); remove Stitch/Figma workflow diagram.
2. Add "Phase System Bridge" paragraph: Blueprint phases = project lifecycle; these 9 phases = per-feature build sequence within Fabrication. (Mirror paragraph goes into Blueprint v2.1 — coordinate with REVIEW_001 changes.)
3. Strip version suffixes from all cross-references; adopt canonical-name rule.
4. Full mojibake sweep.
5. Consider extracting §1.5 (Doctrine Pairing) into a top-level constitution doc or into the Blueprint — it governs the whole factory, not just this playbook.

## 5. Cross-Doc Dependencies Noted

References: all 7 core manuals (§1, §14), HANDOFF_PACKAGE_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, UI-UX-BUILDING-MANUAL, AUTH_MANUAL, APP_ARCHITECTURE_MANUAL, DATABASE_MANUAL, API_AND_SERVICES_MANUAL, STATE_MANAGEMENT_MANUAL, ECOMMERCE_AND_PAYMENTS_MANUAL. Conflicts with: APP_FACTORY_BLUEPRINT v2.0 (F-009, F-010).

---

*Part of the Factory Doc Stack Audit series. See FINDINGS_LOG.md for the running catch list.*
