# RIPPLE_MAP — factory-module-doctrine — 2026-08-10

> Phase 2 output of the `factory-docs-update` skill (v0.3-DRAFT run). Drafted by Claudy
> (Architect's intent carried by the FINALIZATION_REPORT manifest); INFERENCE rows labeled.
> Approved by the Operator at Stop Gate 2. This map — not memory, not the branch —
> is the single source of truth for Phase 4 execution.

## Entries in scope

| Entry/Lesson ID | One-line summary | Source |
|---|---|---|
| BIM-doctrine | BIM_PLAYBOOK v1.0 enters the Hub (new doc) | _INBOX/BIM_PLAYBOOK.md |
| FEAT-doctrine | FEAT_PLAYBOOK v1.0 enters the Hub (new doc) | _INBOX/FEAT_PLAYBOOK.md |
| QA-supersede | QA_PLAYBOOK v0.1 → v1.0 wholesale (field-tested) | _INBOX/QA_PLAYBOOK_v1.0_FIELD_TESTED.md |
| QA-AC-sync | AC-numbering sync patch on QA_PLAYBOOK → v1.1 | _INBOX/QA_PLAYBOOK_AC_SYNC_PATCH.md |
| BUGFIX-merge | Seamless merge v0.1 + amendments kit → BUG_FIX_PLAYBOOK v1.0 | _INBOX/BUG_FIX_PLAYBOOK_v1_0_AMENDMENTS.md |
| SFP-insert | "Module Identity & QA Handoff" section into SOFTWARE_FACTORY_PLAYBOOK → v1.3 | _INBOX/SFP_INSERT_KIT_MODULE_IDENTITY_QA_HANDOFF.md |
| (record) | FINALIZATION_REPORT → `_AUDIT/` marked ENCODED at close-out | _INBOX/FINALIZATION_REPORT.md |

## Splits parked

None — all cargo targets Hub doctrine. (`APP_REGISTRY.md` stays a proposed-only mention; separately approvable later, per FINALIZATION_REPORT item 3.)

## Touch list (execute lightest ← first, heaviest ← last)

| # | Doc | ← count | Placement (VERIFIED vs live) | Change summary | New version | Rename/move? |
|---|---|---|---|---|---|---|
| 1 | BIM_PLAYBOOK | 0 (new) | `03_BUILD_METHODOLOGY/` | New doc, content verbatim; status string translated (see flags) | 1.0 | NO |
| 2 | FEAT_PLAYBOOK | 0 (new) | `03_BUILD_METHODOLOGY/` | New doc, content verbatim; status string translated | 1.0 | NO |
| 3 | QA_PLAYBOOK | 1 — ← BUG_FIX (header-declared; also FBP §9 body pointer) [EVIDENCE] | Wholesale replacement under canonical name | Archive v0.1 → land field-tested content; header → single-line Hub format; Version History reordered newest-LAST | 1.0 (commit 1) | NO — cargo's versioned filename dies here (AP-9) |
| 4 | QA_PLAYBOOK | (same doc) | §7 (traceability definition), §15, §36 | AC-sync patch: clarifying line at §7; legacy labels on X1–X7 field-evidence examples (see Resolution R1); history row | 1.1 (commit 2) | NO |
| 5 | BUG_FIX_PLAYBOOK | 1 — ← QA (header-declared) [EVIDENCE] | A1→§3 (Engineer/QA Lead/Architect subsections VERIFIED) · A2→§9 · A3→§16 list · A4→§17 template · A5→§13 note · A6→history · N1,N2 inserted after §15 · N3 as appendix | Seamless merge per kit §D; 20 → 23 sections (see Structure S1) | 1.0 | NO |
| 6 | SOFTWARE_FACTORY_PLAYBOOK | 4 (MANIFEST map) — HEAVIEST | New top-level §2.5, after §2 (whose §216 "Phase Vocabulary" subsection the kit names as anchor), before §3 per-phase chapters [VERIFIED] | Insert kit section verbatim as §2.5 (fractional — follows the file's own §1.5 precedent; avoids renumbering 12 sections + ToC on a Tier-1 doc, D14) + history row | 1.3 | NO |

Plus per-doc MANIFEST + CHANGELOG updates (D7 steps 3–4) riding each doc's commit.

## New docs entering the Hub

| File | Standard header? | MANIFEST row | Notes |
|---|---|---|---|
| BIM_PLAYBOOK.md | Yes — already single-line; status normalized `ACTIVE — Factory doctrine` → `Active` | Add (03_BUILD_METHODOLOGY) | History table already newest-last ✓ |
| FEAT_PLAYBOOK.md | Yes — same normalization | Add (03_BUILD_METHODOLOGY) | History table already newest-last ✓ |

## Resolutions of pack ambiguities (Operator confirms at this gate)

- **R1 (QA AC patch item 1 vs item 2)** [INFERENCE]: the §7 example matrix (X1–X7) and §15 dialogue (X1/X2) in the v1.0 cargo ARE the historical FIX-002 (ADK-HARNESS, legacy) field record — item 2 governs: keep X*, add the "legacy/internal engineering gate IDs" label. Item 3's clarifying line lands at §7 where traceability is defined. The §21 QA-plan template's ID column is empty — nothing to renumber. Net: labels + one clarifying line, zero renumbering.
- **S1 (BUG_FIX merged structure)** [INFERENCE from kit §D "N1–N3 as §16-adjacent and appendix sections, renumber"]: §1–15 unchanged (A1/A2/A5 applied in place) · §16 FIX Module Anatomy (N1) · §17 Module Identity (N2) · §18 Required FIX Artifacts (old 16, per A3) · §19 BUG_REPORT Template (old 17, per A4) · §20 Definition of Done · §21 Anti-Patterns · §22 Field Case Studies (N3, appendix) · §23 Version History (+A6 row). §12/§13 self-references in amendment text stay valid (those sections don't move).

## Hub-law translations (D15 — each flagged)

1. QA v1.0 stacked header → single-line `> **Version:** 1.0 · **Date:** 2026-08-10 · **Status:** Active — field-tested (ADK Harness)`.
2. QA v1.0 cargo Version History is newest-FIRST → reordered newest-LAST; bold version markers normalized.
3. BIM/FEAT status `ACTIVE — Factory doctrine` → `Active`; BUG_FIX header DRAFT → `Active`, v1.0 (the kit's stated finalization outcome; A6's row label `1.0-DRAFT` lands as `1.0`).
4. SFP history row `vNEXT` → `1.3`; QA patch row `vNEXT` → `1.1`.
5. SFP ToC: §2.5 NOT added — the live ToC already omits fractional §1.5; following file precedent (alternative: add both, a wider diff).
6. BUG_FIX Pairs-with gains `SOFTWARE_FACTORY_PLAYBOOK.md` (N2 explicitly inherits from it). QA/BIM/FEAT pairs land as cargo declares.

## Consistency ripples (checked, NOT edited)

| Doc | Why checked | Verdict |
|---|---|---|
| FRONTEND_BUILD_PHASE_PLAYBOOK v1.2.2 | §9 Gate Q/D pointers to QA + BUG_FIX | CONSISTENT — Gate Q/D retained and strengthened in both v1.0s [EVIDENCE] |
| TESTING_PLAYBOOK v2.1 | QA/BIM/FEAT defer to it for test layers | CONSISTENT — deference restated, no contradiction [EVIDENCE: QA §2, BIM §7] |
| ENGINEER_PLAYBOOK v1.2 | BIM's git-zero Engineer doctrine | CONSISTENT — BIM scopes git-zero to module execution under a Coordinator; no Hub text contradicted. Noted as future candidate: module-track awareness [INFERENCE] |
| APP_FACTORY_BLUEPRINT v2.1 | Owns the pipeline router; BIM/FIX/FEAT are new module types | NO ENTRY TARGETS IT — router mention of module types listed under CONCERNS as a future candidate, not touched (D10) |

## MANIFEST scope (this run)

- Rows: SFP 1.2→1.3 · QA 0.1→1.1 · BUG_FIX 0.1→1.0 · + BIM 1.0, FEAT 1.0 rows.
- Doc count "27" → "29" (title line, §"The 27 Live Docs" heading, map preamble).
- Dependency map (← table): recompute additions from the five in-scope headers. This ALSO closes a pre-existing GAP: QA/BUG_FIX (landed 08-05) were never added to the ← map nor counted into TESTING/ENGINEER/etc. rows [EVIDENCE: map lists 27 docs only]. Flagged: this is the map obeying its own "computed by inverting" law, executed at this bump.

## Structural flags

- Renames/moves: NONE (cargo filenames die in `_INBOX/`; canonical names land).
- Heaviest doc: SOFTWARE_FACTORY_PLAYBOOK ←4, Tier-1 Constitution — minimal-diff form chosen (§2.5 fractional insert, no renumber).
- Placement mismatches: none — every kit anchor exists as stated. All ambiguities above are resolution choices (R1, S1), not missing anchors.

## Write-load tally

3 archive copies + 2 new docs + 4 live-doc edit sets (QA×2 commits) + MANIFEST + CHANGELOG ≈ **~12 file writes, 6 doc commits** (+ close-out housekeeping: skill folder rename/commit, pack → `_AUDIT/`, session artifacts).

## Approval

- [ ] Operator APPROVED at Stop Gate 2 on: ____
