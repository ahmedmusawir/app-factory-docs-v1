# ✅ WAVE 2B COMPLETE: ENGINEER_PLAYBOOK → v1.2 (structural rewrite)

**File:** `2_AGENTS-ENGINEER_PLAYBOOK_v1_1.md` · 33,046 → 46,390 chars · assembled programmatically (moved blocks extracted from baseline, never retyped)

## CHANGES MADE (per approved BEFORE→AFTER map — honored exactly)

| Area | Change | Finding |
|---|---|---|
| Header | Standard block (v1.2 · 2026-07-07 · Tier 2 · 9 canonical pairs); App Factory rename; new part-structured ToC | F-018, F-008 |
| PART I | §1 updated (Designer v2.0 diagram + conversion-route note; +Ground-Truth Recon & FFM Execution responsibilities; recon mantra line) | F-026/F-027 |
| **NEW §2** | **Phase 0: Recon-Executor Role** — Engineer answers RECON_QUESTIONNAIRE read-only, verbatim drift reporting, produces the Recon Report at `agent_docs/recon/`; Blueprint Phase 0 / FFM Stage 0; filesystem wins | F-027 |
| §3 (rewritten) | Per-pipeline inputs: **greenfield = Designer §10 verbatim (token file PRIMARY, style tile + screen HTML/PNG, UI_SPEC, component manifest)** — "Screen Screenshots" input eliminated (the F-026 bug); conversion = 4-file package + `_design/` + `_extraction/`; **F-029 ownership box**; per-track pre-flight checklist | F-026, F-029 |
| §4 | Old §3 carried + track note (pytest-venv ↔ build/jest/tsc truth-tests) | F-028 |
| **NEW §5** | **Kit Track (PART II, described first):** recon → kit read (aspirational, verify) → Kit Audit (FRONTEND_FIRST §0) → **FFM execution as primary work mode**; kit-consumption rule (auth IS the service layer); discipline-per-pillar table; 5 doc pointers incl. TESTING_PLAYBOOK | F-027, F-028, F-035 |
| PART III | Old §4–§9 → §6–§11, **verbatim** (Pipeline Track framing via band only) | F-028 |
| PART IV | §12 DATA_CONTRACT (+ownership box, template verbatim); §13 Type-Specific (+track routing); §14 Anti-Patterns (+1 new: "Wrapping What the Kit Provides / Unverified Kit Claims" — Run 001, F-039 antibody) | F-029, F-028 |
| PART V | §15 Karpathy **PINNED at 15** + ALL-AGENT banner (D-011) connected to the Blueprint's Wave 1 placeholder; §16 Session Memory **PINNED at 16**, verbatim | D-011, D-012 |
| Ship | §17 = old §12 Ops handoff, verbatim | — |
| Appendix A | Old §14 lessons, verbatim, retitled "(Pipeline Track — AI Video Pipeline)" | F-028 |
| Tail | Summary updated (checklist w/ step 0 recon, per-pipeline receive; golden rules + 2 Run-001 rules); Version History table (1.2/1.1/1.0) | D-018 |

## THE REQUIRED GUARD — CARRY VERIFICATION

Section-by-section byte-comparison vs pre-edit baseline (`scratchpad/engineer_baseline.md`):

```
old4->new6 (CLI-First)      BYTE-FAITHFUL     old10->new12 (template)   BYTE-FAITHFUL
old5->new7 (File-State)     BYTE-FAITHFUL     old11->new13 (type-spec)  BYTE-FAITHFUL
old6->new8 (Build Seq)      BYTE-FAITHFUL     old13->new14 (anti-pat)   BYTE-FAITHFUL
old7->new9 (Testing)        BYTE-FAITHFUL     old15->new15 (Karpathy)   BYTE-FAITHFUL
old8->new10 (Cloud)         BYTE-FAITHFUL     old16->new16 (Session)    BYTE-FAITHFUL
old9->new11 (Providers)     BYTE-FAITHFUL     old12->new17 (Ops)        BYTE-FAITHFUL
old3->new4 (Sys Discipline) BYTE-FAITHFUL     old14->AppendixA          BYTE-FAITHFUL
```

**14/14 — zero drift.** Carried content moved; nothing was reworded or "improved."

## OTHER GATES

stitch live **0** (1 hit = v1.2 history row) · `_v[0-9]` **0** · `â`/C1 **0** · LF-only, no BOM · two tracks, Kit first ✓ · recon-executor ✓ · FFM mode ✓ · token-file-primary inputs ✓ · F-029 stated ✓ · §15/§16 pinned ✓

## THINGS I DIDN'T TOUCH

Every carried section's content (proven above); all other repo files.

## CONCERNS

- The ToC "Ship" grouping holds one section (§17) — cosmetic; kept for the chronology story.
- Karpathy extraction to a standalone constitution doc (REVIEW_008 option) deliberately NOT done — work order says canonical home stays here; Blueprint pointer connects it. Full extraction remains a Wave 6 / Doctrine Hub decision if wanted.
- Baseline snapshot + assembly/verify scripts preserved in scratchpad for your diff review.

## Suggested commit

wave2b(engineer): v1.2 — two-track restructure, recon-executor role, handoff inputs fix, F-026/F-027/F-028/F-029
