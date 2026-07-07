# REVIEW 009: 2_AGENTS-HANDOFF_PACKAGE_PLAYBOOK.md

> **Review Series:** Stark Industries App Factory — Full Doc Stack Audit
> **Reviewer:** Architect Jarvis
> **Date:** 2026-07-06
> **Doc Version Reviewed:** 1.0 (2026-05-31, born from Cyberize Run 001)
> **Tier:** 2 — Pipeline Agents (TIER CLOSER)
> **Verdict:** KEEP — needs v1.1 (pipeline-duality preamble + ownership resolution + Designer integration)

---

## 1. What This Doc Is

The authoring manual for the 4-file handoff package: APP_BRIEF, DATA_CONTRACT, UI_SPEC, `_project/CLAUDE.md` — with required sections per file, authoring order + rationale, evidence-traceability rules, approval gates, mistake catalog, and a lessons-promotion loop. Written from the Run 001 conversion (Streamlit → Next.js, 121 tests, 3 days).

## 2. Strengths

- **Numbered forbidden zones doctrine** — "if they're explicit and numbered, Claudy holds the line"; enforceability as the test of a good hard gate. Pairs with the Architect Questionnaire's ⛔ Hard Gate.
- **Evidence traceability (§7)** — every claim traces to Brain Drain extraction or a recorded operator decision; "if you can't trace it, surface — don't invent." Recon-ethos before recon existed.
- **Authoring order with WHY (§6)** — brief → contract → spec → spine, each dependency explained.
- **§9 mistake catalog** — battle-paid; each mistake has the ❌/✅ enforceable form.
- **§11 lessons promotion** — the playbook evolves through use (D-010 family).
- **§13 cross-references use canonical unversioned names** — F-011-correct (second doc to manage it, after the Starter Kit Handbook).
- Explicit D-001 compliance: "instruction set + worked example" named as the strategic move.

## 3. Findings

| ID | Severity | Finding |
|----|----------|---------|
| F-030 | HIGH — structural (audit's deepest catch) | **The factory has TWO pipelines no doc acknowledges.** Conversion pipeline (this doc): Brain Drain → operator/Architect-authored 4-file package → Claudy executes 8 phases; Designer absent; visuals = source-app screenshots. Greenfield pipeline (Blueprint + agent playbooks): Architect → Designer → Engineer; token file primary. Both real, both proven — but they share artifact names (UI_SPEC, DATA_CONTRACT, APP_BRIEF) with different authors and contents, and nothing routes between them. Explains F-026 and part of F-010. Fix: a pipeline-selection preamble here + matching section in the Blueprint ("Conversion runs use the Handoff Package flow; greenfield runs insert the Designer between brief and build"). |
| F-029 | HIGH — ownership conflict | DATA_CONTRACT authorship contradiction: this doc authors it pre-handoff (2nd in order, from Brain Drain evidence); ENGINEER_PLAYBOOK + Blueprint name it the Engineer's deliverable. Same artifact, two authors, two moments. Resolve per-pipeline (conversion: pre-authored from evidence; greenfield: Engineer-authored from APP_BRIEF+UI_SPEC) and state it in all three docs. |
| F-026 (tiebreak) | — | Third package confirmed: no token file / style tile / HTML+PNG anywhere in the package definition. Resolution folds into F-030's greenfield section: for greenfield runs, the package includes the Designer deliverables per DESIGNER_PLAYBOOK §10. |
| F-010 (instance) | — | "8 supervised phases" + "Phase 0 Discovery" — another phase vocabulary. Confirms the canonical phase map need. |
| Doctrine tension (delivery-system note, not a numbered finding) | — | §5.4 "intentional redundancy is a feature" (CLAUDE.md repeats forbidden zones) vs the single-source rule (F-017). Both correct in domain: doctrine docs = single source + pointers; project runtime artifacts = reinforcement redundancy legitimate. Encode the distinction in the delivery system. |

## 4. Required Changes for v1.1

1. Add "Which Pipeline Am I In?" preamble (conversion vs greenfield; router criteria); coordinate a mirror section in Blueprint v2.1 (bundle with F-003/F-008 changes).
2. Resolve DATA_CONTRACT ownership per-pipeline (F-029); sync with ENGINEER_PLAYBOOK v1.2 (§2/§10) and Blueprint.
3. Add greenfield variant of the package contents: Designer deliverables (token file, style tile, HTML+PNG, component manifest) per DESIGNER_PLAYBOOK §10 — closes F-026.
4. Add recon reference (package authoring presupposes a current Recon Report — post-dates this doc).
5. Consider pinning the worked-example pointer (`agent_docs/CURRENT_APP/...` is a moving path; name the module explicitly).

## 5. Cross-Doc Dependencies Noted

Conflicts with: ENGINEER_PLAYBOOK + Blueprint (F-029), DESIGNER_PLAYBOOK §10 (F-026/F-030). References (canonical names ✓): FRONTEND_FIRST_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, STARTER_KIT_HANDBOOK, COMPONENT_REGISTRY, SOFTWARE_FACTORY_PLAYBOOK. Related doctrine: ARCHITECT_QUESTIONNAIRE Hard Gate, RECON_QUESTIONNAIRE (absent — pre-dates it).

---

## TIER 2 CLOSING SUMMARY (Reviews 004–009)

Six docs, six KEEPs, zero rewrites-from-scratch. The Council's docs are individually strong but were written in different eras (Feb → June 2026) and never re-synchronized: Stitch ghosts (F-002), a divergent questionnaire twin (F-017), a mismatched handshake (F-026), a frozen Engineer manual (F-027), and an unacknowledged two-pipeline split (F-030). Gold promoted: Recon Mode (D-005), anti-pattern triplets (D-006), Planning State (D-009), recurrence promotion (D-010), Karpathy Protocol (D-011), session memory (D-012). The rewrite phase's Tier 2 theme: one pipeline story, one questionnaire, one handshake.

---

*Part of the Factory Doc Stack Audit series. See FINDINGS_LOG.md for the running catch list.*
