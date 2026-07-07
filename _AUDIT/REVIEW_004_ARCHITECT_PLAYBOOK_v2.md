# REVIEW 004: ARCHITECT_PLAYBOOK_v2.md

> **Review Series:** Stark Industries App Factory — Full Doc Stack Audit
> **Reviewer:** Architect Jarvis
> **Date:** 2026-07-02
> **Doc Version Reviewed:** 2.1 per footer (⚠️ filename says v2 — see F-016)
> **Tier:** 2 — Pipeline Agents
> **Verdict:** KEEP — needs v2.2

---

## 1. What This Doc Is

The Architect Agent's definitive manual: role definition, required inputs, the Ignition Questionnaire, the App Type Router (Full-Stack Web / Backend Bundle / Local-First Tool), the universal APP_BRIEF template, type-specific considerations, approval criteria, Designer handoff protocol, anti-patterns, and three worked examples.

## 2. Strengths

- **Recon Mode (§2, added v2.1)** — doctrine done right: rationale (docs drift; stale docs → "correct artifact built on wrong data"), absolute rule (no authoring without a current `stark-recon` report; filesystem wins over docs), recovery path ("No Recon Report? Stop."), and full integration (first Core Responsibility, mantra clause, anti-pattern #1, checklist Step 0). Traced to the Cyber Pharma v1 run lesson.
- **Anti-Patterns §9** — Bad/Good/Test triplet format; every anti-pattern ships a self-check. Teaching format worth standardizing (pairs with D-004).
- **App Type Router** — decision tree + implications tables for Designer AND Engineer per type.
- **Appendix worked examples** (one per app type) — complies with D-001 Doctrine Pairing.
- Clear "What the Architect Does NOT Do" ownership table.

## 3. Findings

| ID | Severity | Finding |
|----|----------|---------|
| F-002 (detailed) | HIGH — stale tool + deliverable | Stitch in FOUR places: §1 pipeline diagram ("UI_SPEC + Stitch" as Designer deliverable), §2 No-Vibe-Design protocol ("Suggest using Google Stitch"), §3 Phase 6 checkbox ("Stitch output attached"), APP_BRIEF template Appendix A. Pipeline diagram also misstates Designer's primary deliverable (should be token file per Blueprint v2.0; HTML/PNG as QC). Fix is a sweep + diagram redraw, not find-replace. |
| F-016 | MEDIUM — version mismatch | Filename `ARCHITECT_PLAYBOOK_v2.md` vs footer "Version: 2.1". Filename lies about currency. Reinforces F-011: versions belong inside the doc + MANIFEST, never in filenames. |
| F-017 | MEDIUM — content duplication | §3 embeds the full Ignition Questionnaire and §5 the full APP_BRIEF template — same material as the standalone ARCHITECT_QUESTIONNAIRE_v2_1 doc. Two homes = guaranteed divergence. Proposal: standalone doc is single source; playbook shrinks §3/§5 to summary + pointer. Divergence check due at REVIEW_005. |
| F-018 | LOW — convention | Version block at footer; other docs (SFP, Starter Kit) put it at top. Standardize a parseable header block (name, version, date, status) stack-wide — MANIFEST generator input. |

## 4. Required Changes for v2.2

1. Stitch sweep: §1 diagram, §2, §3 Phase 6, template Appendix A → "style tile / reference screenshot / Figma link" per Blueprint v2.0.
2. Redraw §1 pipeline diagram with correct Designer deliverables (token file primary; HTML/PNG QC).
3. De-duplicate: questionnaire + APP_BRIEF template point to ARCHITECT_QUESTIONNAIRE as single source (coordinate with REVIEW_005).
4. Move version block to standardized top header; align filename to canonical (unversioned) name per F-011 rule when the delivery system lands.

## 5. Cross-Doc Dependencies Noted

References: stark-recon skill (`_SKILLS/stark-recon/CLAUDE.md`), recon reports (`agent_docs/recon/`), RECON_QUESTIONNAIRE (implicit), ARCHITECT_QUESTIONNAIRE (duplicated content — F-017), APP_FACTORY_BLUEPRINT (pipeline), DESIGNER_PLAYBOOK (handoff §8), Claude Code / Windsurf (Engineer tooling). Conflicts with: Blueprint v2.0 (F-002 Stitch + Designer deliverable).

---

*Part of the Factory Doc Stack Audit series. See FINDINGS_LOG.md for the running catch list.*
