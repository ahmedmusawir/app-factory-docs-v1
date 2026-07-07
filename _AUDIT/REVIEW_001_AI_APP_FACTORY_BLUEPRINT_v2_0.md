# REVIEW 001: AI_APP_FACTORY_BLUEPRINT_v2_0.md

> **Review Series:** Stark Industries App Factory — Full Doc Stack Audit
> **Reviewer:** Architect Jarvis
> **Date:** 2026-07-02
> **Doc Version Reviewed:** 2.0 (Last Updated 9 June 2026)
> **Tier:** 1 — Constitution
> **Verdict:** KEEP — needs v2.1 (see Required Changes)

---

## 1. What This Doc Is

The constitution in miniature. One page answering: who does what (Architect → Designer → Engineer), what each produces, in what order, with human approval gates. v2.0 changelog shows real maintenance: Stitch retired, pipeline rebuilt around token-driven HTML → Playwright PNG.

## 2. Strengths

- 5-phase workflow with explicit human checkpoints at every gate.
- Designer deliverables unambiguous: token file is PRIMARY, HTML/PNG are QC artifacts.
- Concrete examples (Pepper's Rig DATA_CONTRACT + FILE_TREE) instead of abstract templates.
- "Blind Spots (Covered)" table — best section; the day-one FAQ for any new agent.
- Changelog discipline present (rare and valuable).

## 3. Findings (Red Flags)

| ID | Severity | Finding |
|----|----------|---------|
| F-002 | HIGH — cross-doc conflict | Blueprint v2.0 retired Stitch, but ARCHITECT_PLAYBOOK_v2 ("No Vibe Design? Stop" §2) and ARCHITECT_QUESTIONNAIRE_v2_1 (Phase 1, Q4) still reference Stitch as a live tool. Downstream agent docs cite a tool the constitution killed. |
| F-003 | HIGH — doctrine gap | Recon Mode (`stark-recon`, mandatory Step 0 per Architect Playbook v2.1) is entirely absent from the Blueprint. Phase 1 IGNITION starts at "You provide: Idea." A new agent reading only the Blueprint doesn't know recon exists. |
| F-004 | MEDIUM — structural | Blueprint indexes ~8 docs; the factory has 26. FFM, Testing, Frontend-First, Handoff, Skills, and all reference manuals are invisible from the top. Feeds the "central delivery system" work item. |
| F-007 | LOW | Versioning guidance covers project docs (`/docs` folder) but not factory-level doc versioning — the exact class of drift caught in this session (THEMING v1.0/v1.1 collision). |

## 4. Required Changes for v2.1

1. Add Recon Mode as Phase 0 (or as first line of Phase 1) with pointer to RECON_QUESTIONNAIRE / `stark-recon`.
2. Replace/expand the doc-structure tables with a pointer to a master MANIFEST (once it exists) — the Blueprint should not try to be the index itself.
3. Add a "Factory Doc Versioning" note or delegate it to the future manifest doc.
4. (Coordinated fix) Bump Architect Playbook + Questionnaire to remove Stitch references — tracked as F-002, owned by those docs' reviews.

## 5. Cross-Doc Dependencies Noted

References or is referenced by: ARCHITECT_PLAYBOOK, DESIGNER_PLAYBOOK, ENGINEER_PLAYBOOK, ARCHITECT_QUESTIONNAIRE (implicitly), TOKEN_FILE, UI_SPEC (project artifact), DATA_CONTRACT (project artifact).

---

*Part of the Factory Doc Stack Audit series. See FINDINGS_LOG.md for the running catch list.*
