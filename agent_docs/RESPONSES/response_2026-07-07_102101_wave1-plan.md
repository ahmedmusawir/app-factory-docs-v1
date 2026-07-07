# 📋 WAVE 1 PLAN — The Pipeline Story (3 docs)

> Status at write time: PENDING_APPROVAL · Session: 2026-07-07 · Mirrors CLI presentation.

## Required reading completed

1. `_AUDIT/GRAND_AUDIT_SUMMARY.md` §3 (findings themes) + §5 (Wave 1 scope) ✓
2. `_AUDIT/FINDINGS_LOG.md` — F-002, F-003, F-008, F-009, F-010, F-011, F-012, F-018, F-026, F-029, F-030, F-035 ✓
3. `_AUDIT/REVIEW_001` (Blueprint), `REVIEW_002` (SFP), `REVIEW_009` (Handoff) ✓
4. `3_METHOD-FFM_PLAYBOOK.md` §4 — router source, READ ONLY ✓
5. Full reads of all three target docs ✓

## Cross-cutting (all three docs)

- **Standard header block** at very top: `# <DOC TITLE>` + `> **Version:** X.Y · **Date:** 2026-07-07 · **Status:** Active` + `> **Tier:** <N — Category> · **Pairs with:** <canonical names>` (F-018).
- **Canonical-name cross-refs** — strip every `_vX.Y` suffix from doc references (F-011).
- **Mojibake sweep** — fix `â–º`, `â–¼`, `â—„`, `âœ…` and any other `â` artifacts; clean UTF-8, no smart quotes (F-012).
- **Version History** table gains a new logged row with finding IDs (D-018).

## DOC 1 — BLUEPRINT → v2.1 (`1_CONSTITUTION-APP_FACTORY_BLUEPRINT_v2_0.md`)

| # | Change | Finding |
|---|--------|---------|
| 1 | Internal title "AI App Factory" → "App Factory" everywhere. Stray line-1 bold title + H1 replaced by the standard header; "The Stark Protocol" kept as subtitle line | F-008 |
| 2 | New tight section **PHASE 0: RECON** before THE FULL WORKFLOW + `PHASE 0` block prepended in the workflow diagram. Engineer ground-truths the target repo per RECON_QUESTIONNAIRE / stark-recon; Architect consumes the Recon Report before authoring | F-003 |
| 3 | New section **WHICH PIPELINE AM I IN?** right after THE BIG PICTURE: CONVERSION (Brain Drain → 4-file handoff package → Engineer; no Designer; visuals = source-app screenshots) vs GREENFIELD (Architect → Designer → Engineer; token file primary). Condensed FFM §4 router questions (de-Stitched). Ownership statement: HANDOFF_PACKAGE_PLAYBOOK owns conversion detail; agent playbooks own greenfield detail | F-030 |
| 4 | Same section, one paragraph: DATA_CONTRACT ownership — conversion = Architect pre-authors from Brain Drain evidence; greenfield = Engineer authors from APP_BRIEF + UI_SPEC | F-029 |
| 5 | De-Stitch: only surviving hits are two Changelog history rows — reworded to "the external UI-generation tool" so the 0-hit gate passes while history stays intelligible | F-002 |
| 6 | One-line Karpathy Protocol pointer placeholder after the PLAYBOOK DOCS table (NO import this wave) | D-011 |
| 7 | "Changelog" heading → "Version History"; add v2.1 row citing F-003/F-008/F-011/F-018/F-029/F-030 | D-018 |

## DOC 2 — SOFTWARE_FACTORY_PLAYBOOK → v1.2

| # | Change | Finding |
|---|--------|---------|
| 1 | Standard header (Tier 1 — Constitution) | F-018 |
| 2 | §4 Phase 2 rewrite: DELETE the Stitch/Figma workflow diagram + design-spec-doc process; replace with a short summary + defer: "Design execution is owned by DESIGNER_PLAYBOOK (token file primary, Canonical Page Method)". Phase numbering intact. §13 Phase-2 checklist items aligned to Designer deliverables | F-009 |
| 3 | De-Stitch the whole doc | F-002 |
| 4 | "Phase Vocabulary" note + mapping table in §2: Blueprint lifecycle (incl. new Phase 0 Recon) = canonical project-phase map; these 9 phases = execution breakdown within it; FFM Sub-Phases nest inside build phases. Map: 1→Ignition · 2→Design · 3→Engineering/Fabrication · 4–8→Fabrication · 9→Deployment. No renumbering | F-010 |
| 5 | Phase 8 (§10) gains `**Reference:** TESTING_PLAYBOOK.md` | F-035 |
| 6 | §1.5 pairing table: strip 5 versioned filenames (`FRONTEND_FIRST_PLAYBOOK_v1.1.md` etc.) | F-011 |
| 7 | Full mojibake sweep (known F-012 carrier: diagram arrows, summary checkmarks) | F-012 |
| 8 | Version History row v1.2 citing F-002/F-009/F-010/F-011/F-012/F-018/F-035 | D-018 |

## DOC 3 — HANDOFF_PACKAGE_PLAYBOOK → v1.1

| # | Change | Finding |
|---|--------|---------|
| 1 | Standard header (Tier 2 — Pipeline Agents) | F-018 |
| 2 | Unnumbered "Which Pipeline Am I In?" preamble before §1: this playbook = the CONVERSION pipeline's package doctrine; greenfield runs → agent playbooks; APP_FACTORY_BLUEPRINT router = entry point (cross-ref the new Blueprint section) | F-030 |
| 3 | New §5.5 "Greenfield Variant": package additionally carries Designer deliverables per DESIGNER_PLAYBOOK §10 — token file (PRIMARY), style tile HTML+PNG, screen HTML+PNG, component manifest; UI_SPEC drafted by Architect, revised by Designer | F-026 |
| 4 | §5.2 (DATA_CONTRACT) gains per-pipeline ownership one-liner + Blueprint pointer (no duplicated text) | F-029 |
| 5 | §4 Prerequisites table gains a "Recon Report (current)" row — package authoring presupposes Phase 0 recon | F-003 |
| 6 | §12 Versioning row v1.1 citing F-003/F-018/F-026/F-029/F-030 | D-018 |

## Verification gates (run after each doc / all at end)

- `grep -ri "stitch"` on the 3 docs → **0 hits**
- `grep -rn "_v[0-9]"` on the 3 docs → **0** versioned cross-refs (Version-History filenames describing past versions exempt)
- `grep -c "â"` per doc → **0**
- All 3 docs: standard header + new Version History entry present
- Final summary in CHANGES / DIDN'T TOUCH / CONCERNS format

## Files I will NOT touch

- `3_METHOD-FFM_PLAYBOOK.md` — read-only router source (edits land Wave 3)
- All other 24 doctrine docs, `_AUDIT/`, `_OTHERS/`, `CLAUDE.md`
- Filenames — unchanged this wave (renames at MANIFEST time, Wave 6)
- Git — zero operations; one suggested commit message output per doc

## Assumptions

1. **Stitch-in-changelog:** history rows naming Stitch are reworded ("the external UI-generation tool") — 0-hit gate wins over verbatim history.
2. **Suite-label footers** ("App Factory v1.1 doctrine") → "App Factory doctrine" (de-versioned) on edited docs only.
3. **Blueprint title:** doc title = "APP FACTORY BLUEPRINT"; "The Stark Protocol" survives as subtitle.
4. Emoji section markers (🏭 📚 🔄 etc.) in existing docs are house style — preserved, and new sections follow it.

## Risks

- SFP §4 deletion is the largest cut — the replacement must not orphan the §13 Phase-2 checklist or the ToC anchor (`#4-phase-2-design-system` — heading text stays "Phase 2: Design System" so anchors hold).
- Mojibake matching: edits must match the corrupted bytes exactly; verified by grep gate afterward.
- Editing-pipeline re-corruption (F-012 systemic) — post-edit grep verifies; operator should re-check after any external save.
