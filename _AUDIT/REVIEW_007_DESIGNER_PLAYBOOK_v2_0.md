# REVIEW 007: 2_AGENTS-DESIGNER_PLAYBOOK_v2_0.md

> **Review Series:** Stark Industries App Factory — Full Doc Stack Audit
> **Reviewer:** Architect Jarvis
> **Date:** 2026-07-06
> **Doc Version Reviewed:** 2.0 (9 June 2026)
> **Tier:** 2 — Pipeline Agents
> **Verdict:** KEEP — cleanest agent playbook; needs v2.1 micro-patch only (§13 reference hygiene + standard header)

---

## 1. What This Doc Is

The Designer Agent's manual: role definition, required inputs, Demo/Production modes, the Canonical Page Method, the token-driven HTML + Playwright production method, screen-by-screen discipline, deliverables + UI_SPEC template, type-specific considerations, handoff protocol, anti-patterns, field lessons. The doc that closed F-001.

## 2. Strengths

- **Only doc in the stack that fully completed its Stitch retirement.** The v2.0 changelog is the model for documenting a doctrine sweep (what was removed, what replaced it, why). Its §1 pipeline diagram (token file primary, HTML+PNG QC) is the reference implementation for the F-002 Architect Playbook fix.
- **Core thesis** — "concrete artifacts survive, abstract intentions decay" — constitution-grade; the design-side twin of D-002.
- **Canonical Page Method** — build one screen, lock at a human gate, clone-and-adapt; explicitly tool-agnostic, survives generator churn.
- **§13 conflict rule** — "if this playbook and a doctrine doc disagree, the doctrine doc wins — surface the conflict and update this playbook." Self-aware hierarchy placement.
- Deliverables table aligned with Blueprint v2.0 (token file = primary). Handoff protocol lists exactly what Claudy needs and why.
- Field lesson 4 ("Tokens Are the Real Deliverable") — the design system in one paragraph.

## 3. Findings

| ID | Severity | Finding |
|----|----------|---------|
| F-025 | MEDIUM — internal + cross-doc inconsistency | The doc argues with itself about where token values live. §5 correctly names `globals.css`/`globals.scss` as the live token file (aligned with THEME_LIBRARY v1.1's 2026-06-08 correction + GDSH §8). §13 still lists `TOKEN_FILE.md` as "the live token values for the current project" — the exact reference retired one day earlier. 24-hour drift incubation. Rewrite-phase decision needed: define TOKEN_FILE doc's official role (values catalog/reference) vs `globals.css` (live values), then align all Tier 5 docs + this §13. |
| F-011 (instance) | LOW | §13 cites `THEMING_MANUAL_v1.0.md` by versioned name; current is v1.1. Canonical-name rule applies. |
| F-018 (instance) | LOW | Version block at footer (same as Architect Playbook). Standard top header in v2.1. |

## 4. Required Changes for v2.1 (micro-patch)

1. §13: `TOKEN_FILE.md` reference → align to the settled token-file terminology (post F-025 decision); drop version suffix from THEMING_MANUAL reference.
2. Move version/changelog block to standard top header.
3. Nothing else — structure and content are the Tier 2 gold standard.

## 5. Cross-Doc Dependencies Noted

References: GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEME_LIBRARY, THEMING_MANUAL (stale version ref), TOKEN_FILE (F-025), COMPONENT_REGISTRY, APP_BRIEF (input), UI_SPEC (output), HANDOFF package. Model for: ARCHITECT_PLAYBOOK §1 diagram fix (F-002), SOFTWARE_FACTORY_PLAYBOOK Phase 2 rewrite (F-009 — Phase 2 should simply defer here).

---

*Part of the Factory Doc Stack Audit series. See FINDINGS_LOG.md for the running catch list.*
