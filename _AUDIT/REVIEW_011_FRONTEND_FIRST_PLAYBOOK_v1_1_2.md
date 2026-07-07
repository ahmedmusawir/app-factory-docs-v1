# REVIEW 011: 3_METHOD-FRONTEND_FIRST_PLAYBOOK_v1_1_2.md

> **Review Series:** Stark Industries App Factory — Full Doc Stack Audit
> **Reviewer:** Architect Jarvis
> **Date:** 2026-07-06
> **Doc Version Reviewed:** v1.1.2 (2026-06-28, Kit Hardening Gate 10)
> **Tier:** 3 — Build Methodology
> **Verdict:** KEEP — v1.1.3 micro-patch only (canonical-name refs + mojibake sweep)

---

## 1. What This Doc Is

The when-and-why of frontend-first: §0 mandatory Pre-Authoring Kit Audit (Lesson 2), allowed/forbidden contexts, three mandatory gates (App Brief, Data Contract, Service Layer skeleton), data-contract + service-layer law, ranked mock strategies, transition-to-backend criteria, §12 page co-location pattern (Lesson 7), §13 Pre-Write Check Protocol (four mobile-first JSDoc questions), §14 pointer to the execution sibling (FRONTEND_BUILD_PHASE_PLAYBOOK).

## 2. Strengths

- **§14 is the MODEL for the F-017 fix.** Lesson 9 caught duplicated doctrine in retrospective; v1.1.1 relocated it to its proper home and left a summary + pointer, explicitly citing the Doctrine Pairing Principle and explaining the split. The exact surgery the Architect Playbook/Questionnaire twins need — already performed successfully once in this stack.
- **§0 Kit Audit** — three questions, 30 seconds, kills the redundant-authoring failure family. "The kit's auth IS the service layer."
- **§13 Pre-Write Check** — four answerable questions gate every UI file; refusal condition built in ("If you cannot answer all four, do not author the file").
- **Version history with lesson provenance** — including v1.1.2's "preserve lesson, swap actor" maintenance doctrine (re-point examples to living actors when the original is deleted; keep the lesson).
- Service-layer rules are enforceable absolutes; mock strategies ranked with removal discipline.

## 3. Findings

| ID | Severity | Finding |
|----|----------|---------|
| F-032 | MEDIUM — same-campaign drift (new record: zero hours) | §0 references `STARTER_KIT_HANDBOOK_v1.0.md` and `COMPONENT_REGISTRY_v1.0.md` — both stale. The SAME Gate 10 that produced this v1.1.2 bumped the handbook and registry to v1.1 the same day. One campaign updated three docs and left two pointing at retired versions of each other. Fix = F-011 cure: canonical names, no version suffixes (§0 + §14's versioned refs). |
| F-012 (instance) | LOW — pattern confirmed | §3 gate headers contain mojibake (`Gate 1 "”`) in a doc whose v1.1 changelog claims the UTF-8 fix. Second confirmed doc (after SFP) where the declared encoding fix didn't stick. Lint-bot candidate confirmed as stack-wide. |
| Minor note | — | No recon pointer; §0's Kit Audit is a mini-recon but the upstream recon gate could be referenced in one line (optional, coordinate with F-024 fixes). |

## 4. Required Changes for v1.1.3 (micro-patch)

1. §0 + §14: strip version suffixes from cross-references; canonical names only.
2. Mojibake sweep (§3 headers, full-file pass).
3. Optional: one-line recon pointer in §0.

## 5. Cross-Doc Dependencies Noted

References: STARTER_KIT_HANDBOOK (stale v1.0 ref — F-032), COMPONENT_REGISTRY (stale v1.0 ref — F-032), FRONTEND_BUILD_PHASE_PLAYBOOK (§14 sibling), SOFTWARE_FACTORY_PLAYBOOK §1.5 (D-001 cited). Model for: F-017 de-duplication surgery. Project-specific example: CYBERBUGS_DATA_CONTRACT (acceptable as worked example).

---

*Part of the Factory Doc Stack Audit series. See FINDINGS_LOG.md for the running catch list.*
