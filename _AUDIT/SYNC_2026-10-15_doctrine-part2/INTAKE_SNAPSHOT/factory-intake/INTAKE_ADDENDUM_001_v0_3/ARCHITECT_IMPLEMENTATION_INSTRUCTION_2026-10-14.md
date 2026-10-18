# Architect Implementation Instruction — 2026-10-14 — "CLAUDY — APPLY QA LEAD'S EXACT AMENDMENTS" (Director-relayed)

> **PROVENANCE-CORRECTED RECORD.** The text below is the **implementation instruction** that the Engineer seat received on 2026-10-14 for applying the QA Lead's amendments: an Architect (Jarvis) implementation prompt, relayed by the Director (Tony). It restates the QA Lead's decision elements (AM-1, AM-2, AM-3, the QAM-SR v1.0 adoption) but it is **not** the QA Lead's decision text. From 2026-10-14 20:40 until 2026-10-15 it was reproduced in `QA_LEAD_DECISION_2026-10-14.md` and labeled "the QA Lead's verbatim decision"; that attribution was wrong and was corrected on 2026-10-15 at the Architect's instruction. The actual QA Lead decision is now preserved verbatim in `QA_LEAD_DECISION_2026-10-14.md`. The text itself is unchanged here, character-for-character.

| Field | Value |
|---|---|
| What this is | Director-relayed Architect implementation instruction to the Engineer seat (2026-10-14) |
| Author of the instruction | Jarvis (Architect), relayed by Tony (Director) |
| Not | the QA Lead's decision (see `QA_LEAD_DECISION_2026-10-14.md`); not a Director ruling; not an Architect verification (see `ARCHITECT_VERIFICATION_2026-10-14.md`) |
| What it drove | `TEMPLATES/QAM/` v0.3-draft; `TEMPLATE_CORRECTION_RECORD_002.md`; `ENGINEER_VERIFICATION_v0_3.md`; the package `QAM_TEMPLATES_v0_3_AMENDED_FOR_ARCHITECT_2026-10-14_204903.zip` |
| Recorded by | Claudy (documentation Engineer seat): text captured 2026-10-14 20:40 +0600; attribution corrected and moved to this file 2026-10-15 12:03 +0600 |

## Instruction text (verbatim, as received 2026-10-14)

```text
CLAUDY — APPLY QA LEAD’S EXACT AMENDMENTS

QA Lead Fable issued ACCEPT WITH EXACT AMENDMENTS for QAM template set v0.2-draft on 2026-10-14.

Preserve the v0.2 review package. Prepare v0.3-draft with ONLY these substantive changes:

AM-1 — QAM_CLEANUP_REPORT.md §1
Add this column to the routine phase-exit hygiene table:
“Done at Q4 exit (if Q4 ran)”
Leave its execution results unfilled.

AM-2 — QAM_PACKAGING.md §3
In the QAM_TEST_PLAN.md row, replace the STOP-column “✔” with:
“as relevant (a stop may precede the plan draft)”

AM-3 — QAM_RISK_REQUIREMENTS.md §1, SR-3
Use:
“Evidence: every PASS/FAIL cites an evidence path with the command, working directory, exit code and unfiltered output; existence checks precede greps/diffs so vacuous passes are impossible”

STANDING REQUIREMENTS ADOPTION
Record in QAM_RISK_REQUIREMENTS.md §1:
- Standing requirements version: QAM-SR v1.0
- Adopted by: QA Lead (Fable)
- Date: 2026-10-14
- SR-1 through SR-11 adopted, with AM-3 applied.
- Reusable across modules without per-module re-review.

Replace the now-stale “NOT APPROVED” standing-requirements notice with the attributed adoption record. Preserve the separate Architect and Executor sections.

RECORDS AND VERIFICATION
- Preserve Fable's supplied decision verbatim as a separate QA Lead decision record.
- Record AM-1, AM-2, AM-3 and the standing-requirements adoption in the v0.3-draft correction record.
- Update version references, indexes and directly affected staging status records.
- Describe the status accurately: QA Lead accepted with exact amendments; amendments applied and Engineer-verified. Do not invent a second Lead decision.
- Compare against v0.2: only authorized amendments and necessary version/status/index bookkeeping may differ.
- Verify hashes, package membership, matching dual-entry routing and unfilled module execution/approval/certification fields.

Return one indexed ZIP containing the revised template set, governing sources, exact QA Lead decision, correction record and verification results. Include its absolute path, file count and SHA-256.

Keep canonical documents and _INBOX untouched. No Git actions or DocSet Sync activation.

Return the completed package to Jarvis, Factory Doc Sync Architect, for amendment verification and the next intake step.
```

Transcription note: reproduced character-for-character from the instruction as received, including its typographic quotation marks and apostrophe. No word, number, identifier or line was changed, added or omitted.

*ARCHITECT IMPLEMENTATION INSTRUCTION — provenance-corrected 2026-10-15; the QA Lead's own decision text is in `QA_LEAD_DECISION_2026-10-14.md`.*
