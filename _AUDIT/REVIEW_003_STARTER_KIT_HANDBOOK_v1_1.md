# REVIEW 003: STARTER_KIT_HANDBOOK_v1_1.md

> **Review Series:** Stark Industries App Factory — Full Doc Stack Audit
> **Reviewer:** Architect Jarvis
> **Date:** 2026-07-02
> **Doc Version Reviewed:** 1.1 (v3 reconciliation pass, 2026-06-08)
> **Tier:** 1 — Constitution
> **Verdict:** KEEP — MODEL DOC (no rewrite; two pending operator decisions)

---

## 1. What This Doc Is

The canonical answer to "what does the kit already provide?" — the anti-redundancy gate read in Phase 0 of every run. Covers auth, RBAC/RLS, DB patterns, component inventory, routing conventions, state, tests, gotchas, and the "Should I Author This?" verdict table. Born from Run 001's near-miss (agent almost authored a redundant authService.ts).

## 2. Strengths (several are stack-wide models)

- **v1.1 reconciliation pass** — admits v1.0 was partially aspirational, closes every handbook-vs-disk gap with inline 🔧 RECONCILED tags traced to lesson numbers. Auditable healing.
- **D-002 doctrine:** "The handbook is a contract, not an aspiration. Every file/flag/path named must exist on disk. Ground-truth before trust."
- **⚑ operator-decision flags** — pending human calls surfaced in-doc, not lost in chat logs. Pattern worth standardizing stack-wide.
- **"Should I Author This?" table (§11)** — most agent-effective artifact in the stack; binary verdicts per temptation.
- **Cross-references by canonical unversioned names (§13)** — the only doc so far that does references the F-011-correct way. The model for the stack-wide fix.
- §12 maintenance triggers + update discipline ("obsolete gets marked, not deleted — history is doctrine").
- Gotchas section encodes hard-won, disk-verified failures (PostgREST sibling selects, directive-case typo, trigger double-insert).

## 3. Findings

| ID | Severity | Finding |
|----|----------|---------|
| F-013 | MEDIUM — pending decisions | Two ⚑ OPERATOR DECISIONS open since 2026-06-08: (a) role colors as `--role-*` semantic tokens vs numbered-color exception; (b) canonical name `ThemeToggle` vs `ThemeToggler`. Jarvis recommendation: tokens + `ThemeToggle`. Needs Tony's call; then remove ⚑ flags in a patch rev. |
| F-014 | LOW — missing referenced doc | §13 references `STARTER_KIT_FEEDBACK.md` — not present in the 27-doc stack. Determine: repo-side-only by design, or missing from factory doc set (F-001 pattern). |
| F-010+ | HIGH — pattern escalation | Third phase vocabulary: "Phase 0" (handbook read) and "Phase 8 retrospective" don't map to Blueprint's 5 phases or SFP's 9 (SFP Phase 8 = testing). Phase numbering is now a confirmed stack-wide ambiguity → one canonical phase map required. |
| F-015 | LOW — carry-forward check | Changelog: "doctrine says Vitest" lie lives in FFM project CLAUDE.md template; fix assigned there (L8). Verify fix landed when reviewing FFM_PLAYBOOK (Tier 3). |

## 4. Required Changes

None structural. Patch rev after Tony's two ⚑ decisions; resolve F-014 status; participate in the canonical phase map (owned at Tier-1 level).

## 5. Cross-Doc Dependencies Noted

References (canonical names): AUTH_MANUAL, DATABASE_MANUAL, UI-UX-BUILDING-MANUAL, STATE_MANAGEMENT_MANUAL, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEME_LIBRARY, COMPONENT_REGISTRY, STARTER_KIT_FEEDBACK (absent — F-014). Referenced by: FFM CLAUDE.md template (L8 linkage), Factory Phase 0 doctrine.

---

*Part of the Factory Doc Stack Audit series. See FINDINGS_LOG.md for the running catch list.*
