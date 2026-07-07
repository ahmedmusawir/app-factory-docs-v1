# REVIEW 006: 2_AGENTS-RECON_QUESTIONNAIRE.md

> **Review Series:** Stark Industries App Factory — Full Doc Stack Audit
> **Reviewer:** Architect Jarvis
> **Date:** 2026-07-06
> **Doc Version Reviewed:** v0.4 (2026-06-07, living document)
> **Tier:** 2 — Pipeline Agents
> **Verdict:** KEEP — MODEL DOC; needs v0.5 patch (internal renumbering + recon-doctrine cross-links)

---

## 1. What This Doc Is

The ground-truth gate: 13 sections of executable recon questions (bash per question) answered by the Engineer (Claudy) from the actual filesystem BEFORE the Architect authors anything. Includes the Day-1 Ground-Truth Sweep (Section 0), a structured Recon Report return format, and a Lessons Backlog with promotion rules. Born mid-Cyber-Pharma-v1 from conflicts at the Discovery gate; grew v0.1 → v0.4 in three days, each bump traced to numbered run lessons (L1–L34).

## 2. Strengths (multiple stack-wide models)

- **Question↔scar traceability:** the opening conflict table maps every question to the real failure it would have caught (app-role.ts ghost file → Q2.1-2.3; authService trap → Q3.1-3.4; posts-demo cascade → Q8.1-8.3). Doctrine Pairing at question granularity.
- **Section 0 meta-lesson** — "the handbook is aspirational, not literal... where any doc and the filesystem disagree, the filesystem wins — every time." The factory's sharpest doctrine sentence; consolidates L1/L5/L6/L7/L8/L9/L24/L32.
- **Executable, not prose** — agents can literally run the recon; zero interpretation gap.
- **Recon Report Format** — a return contract, so recon output is machine-consumable by the Architect.
- **Lessons Backlog + promotion rule (D-010):** new conflict → backlog question; recurrence across two runs → promoted numbered section. An explicit doctrine lifecycle; the Doctrine Hub PR flow should encode exactly this.
- Version history with lesson-numbered provenance — the living-document model done right.

## 3. Findings

| ID | Severity | Finding |
|----|----------|---------|
| F-023 | LOW — internal drift | Numbering inconsistencies from two rapid renumberings: no Section 7 exists (jumps 6→8); §13 "Open-Ended Sweep" still numbers questions Q10.1–Q10.4 (v0.2 relic); Recon Report Format references "Section 10 — Surprises" while the doc's surprises section is §13. Cheap v0.5 fix. |
| F-024 | MEDIUM — linkage gap | The two recon doctrines don't cross-reference: ARCHITECT_PLAYBOOK §2 formalizes Recon Mode via the `stark-recon` skill (`agent_docs/recon/` reports); this questionnaire describes the manual operator-mediated flow. Same gate, two automation levels, neither names the other. Fix: mutual pointers ("the skill automates this questionnaire" / "this questionnaire is the skill's source content"); verify the skill actually consumes this doc (skill lives repo-side — ties to F-021 scope decision). |

## 4. Required Changes for v0.5

1. Renumber: either restore a Section 7 or renumber 8–13 → 7–12; fix §13's Q10.x → matching section numbers; sync the Recon Report Format section labels.
2. Add two-way cross-references with ARCHITECT_PLAYBOOK §2 Recon Mode + `stark-recon` skill.
3. Nothing else — content is battle-tested; do not editorialize the scars away.

## 5. Cross-Doc Dependencies Noted

Pairs with: FFM_PLAYBOOK ("recon pass becomes Stage 0" — verify at Tier 3 FFM review), ARCHITECT_PLAYBOOK §2 (F-024), STARTER_KIT_HANDBOOK (the "aspirational vs literal" tension is ABOUT this doc — note the June-28 handbook edition post-dates most of these scars; some claims this doc calls lies may now be fixed, worth a one-pass re-verify during the rewrite phase), DATA_CONTRACT (project artifact), stark-recon skill (repo-side, F-021).

---

*Part of the Factory Doc Stack Audit series. See FINDINGS_LOG.md for the running catch list.*
