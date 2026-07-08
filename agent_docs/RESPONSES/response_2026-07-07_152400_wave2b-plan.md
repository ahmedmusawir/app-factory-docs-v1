# 📋 WAVE 2B PLAN — ENGINEER_PLAYBOOK → v1.2 + BEFORE→AFTER SECTION MAP

> Status at write time: PENDING_APPROVAL · Session 2026-07-07 · Mirrors CLI presentation.

## Required reading completed

FINDINGS F-026/F-027/F-028/F-029/F-002/F-018/F-035 + D-011/D-012 ✓ · REVIEW_008 ✓ · DESIGNER_PLAYBOOK §10 (the package) ✓ · HANDOFF_PACKAGE_PLAYBOOK v1.1 (preamble + §5.5) ✓ · BLUEPRINT v2.1 (router + Karpathy placeholder) ✓ · RECON_QUESTIONNAIRE v0.5 (executor role) ✓ · Full read of ENGINEER_PLAYBOOK v1.1 (1,405 lines) ✓

## Pre-plan findings

- Doc is **encoding-clean**: 0 mojibake, 0 C1, LF-only. **0 Stitch hits** (F-002 already satisfied here). 0 versioned refs. The work is purely structural.
- Numbering constraint honored: **D-011/D-012 cite §15/§16** — the new structure is engineered so Karpathy stays §15 and Session Memory stays §16 (same stable-ID principle approved for Recon in 2A).

## BEFORE → AFTER SECTION MAP (the approval gate)

| Old § | Old title | New § | Disposition |
|---|---|---|---|
| — | (title block) | header | Standard header block (v1.2 · 2026-07-07 · Tier 2 · Pairs-with); "AI App Factory" → "App Factory" |
| — | — | **PART I — COMMON DOCTRINE (ALL TRACKS)** | NEW part band |
| 1 | Role Definition | **1** | UPDATED: pipeline diagram → Designer v2.0 model (token file primary — same fix as Architect §1); Core Responsibilities gain "Ground-Truth Recon (Phase 0)" (first row) + "FFM Execution"; rest preserved |
| — | — | **2 — Phase 0: The Recon-Executor Role** | **NEW (F-027):** the Engineer ANSWERS RECON_QUESTIONNAIRE read-only from the filesystem, reports drift verbatim, produces the Recon Report (`agent_docs/recon/`) the Architect consumes. Blueprint Phase 0 / FFM Stage 0. Filesystem wins. Discipline rules (read-only, one pass, verbatim) |
| 2 | Inputs Required | **3** | **REWRITTEN (F-026/F-029):** route by Blueprint pipeline router. GREENFIELD = Designer §10 package verbatim: APP_BRIEF, **token file (PRIMARY)**, style tile HTML+PNG, screen HTML+PNG (locked set), UI_SPEC, component manifest + "what Claudy actually needs" (HTML to build from / PNG to verify / tokens to inherit). CONVERSION = 4-file handoff package (APP_BRIEF, DATA_CONTRACT pre-authored, UI_SPEC, `_project/CLAUDE.md`) + `_design/` screenshots + `_extraction/` Brain Drain. **F-029 ownership box**: conversion = Architect pre-authors from Brain Drain; greenfield = ENGINEER authors from APP_BRIEF + UI_SPEC. Pre-flight checklist per track. "Screen Screenshots" as greenfield input DIES (that was the F-026 bug) |
| 3 | Core Philosophy: Systems Discipline | **4** | Preserved; "Testable" pillar made track-aware (pytest-clean-venv = Pipeline expression; build+jest+tsc-clean = Kit expression) |
| — | — | **PART II — THE KIT TRACK (THE DOMINANT LANE)** | NEW part band — described FIRST per work order |
| — | — | **5 — Kit Track: Working the Starter Kit (FFM Execution Mode)** | **NEW (F-027/F-028):** sequence = Phase 0 recon (→§2) → kit handbook read (aspirational — verify per Recon §0) → Kit Audit (FRONTEND_FIRST §0) → **FFM execution as the primary work mode** (FFM_PLAYBOOK anatomy, FRONTEND_BUILD_PHASE_PLAYBOOK stages, approval gates). Kit-consumption rule: consume kit primitives directly — the kit's auth IS the service layer; no wrappers for what exists (Run 001 authService lesson). Pointers: FRONTEND_FIRST_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, FFM_PLAYBOOK, STARTER_KIT_HANDBOOK, TESTING_PLAYBOOK (F-035 bridge) |
| — | — | **PART III — THE PIPELINE TRACK (Backend Bundle / Local-First)** | NEW part band — existing material retained, framed as track 2 |
| 4 | The CLI-First Pattern | **6** | Moved verbatim |
| 5 | File-Based State as Contracts | **7** | Moved verbatim |
| 6 | The Build Sequence | **8** | Moved verbatim |
| 7 | Testing Strategy | **9** | Moved verbatim |
| 8 | Cloud-Native Engineering | **10** | Moved verbatim |
| 9 | Provider Abstraction | **11** | Moved verbatim |
| — | — | **PART IV — SHARED REFERENCE** | NEW part band |
| 10 | DATA_CONTRACT Template | **12** | Moved; + one-line F-029 ownership reminder atop; template body untouched |
| 11 | Type-Specific Considerations | **13** | Moved; + track-routing line per type (Full-Stack → Kit Track; Backend Bundle + Local-First → Pipeline Track) |
| 13 | Anti-Patterns to Avoid | **14** | Moved; + ONE new kit-track anti-pattern: "❌ Wrapping What the Kit Provides / Building on Unverified Kit Claims" (Run 001: authService trap + handbook lies; test = recon report + Kit Audit) |
| — | — | **PART V — AGENT CONDUCT (ALL AGENTS)** | NEW part band |
| 15 | Karpathy Protocol | **15 (PINNED)** | PRESERVED VERBATIM + banner atop: all-agent doctrine (D-011), governs Architect/Designer/Engineer; canonical home here; APP_FACTORY_BLUEPRINT holds the constitution-level pointer (connects to Wave 1 placeholder) |
| 16 | Session Memory Protocol | **16 (PINNED)** | PRESERVED VERBATIM |
| 12 | Handoff Protocol to Operations | **17** | Moved to end — chronologically last thing the Engineer does; content preserved |
| 14 | Appendix: Lessons from the Field | **Appendix A** | Retitled "Lessons from the Field (Pipeline Track — AI Video Pipeline)"; content preserved verbatim |
| — | Summary | Summary | Updated checklist: recon-executor step 0, per-track receive step, FFM mode; golden rules preserved + kit-track rule added |
| — | (footer version block) | Version History | Table: v1.2 row (finding IDs) + v1.1 row (from old changelog line) + v1.0 baseline |

## Nothing dies

No content deletion (doc has zero Stitch-era obsolescence). Everything moves or is preserved verbatim. Additions limited to: 2 new sections, part bands, per-track framing lines, 1 anti-pattern, Karpathy banner, ownership box, updated summary, header + history.

## Execution method

Single full-file Write (a restructure of this scale makes a whole-file diff unavoidable; content blocks carry over verbatim from the current file, so review can diff section-by-section against the map above).

## Verification gates

- Two clear tracks under common doctrine; Kit Track first ✓ (structure)
- Recon-executor present (§2); FFM mode present (§5)
- §3 inputs match Designer §10 / Handoff v1.1 (token file PRIMARY; no greenfield "screenshots")
- DATA_CONTRACT ownership per-pipeline (§3 box + §12 reminder)
- §15/§16 pinned + Karpathy all-agent banner
- stitch 0 · `_v[0-9]` 0 · mojibake/C1 0 · header + history row ✓
- CHANGES / DIDN'T TOUCH / CONCERNS summary

## Files I will NOT touch

Everything else. One file only.
