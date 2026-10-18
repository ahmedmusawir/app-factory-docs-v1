# QA Lead Decision — 2026-10-14 — QAM template set v0.2-draft: ACCEPT WITH EXACT AMENDMENTS

> **QA LEAD DECISION RECORD — preserved verbatim.** The text in the block below is the QA Lead's (Fable's) own decision on the QAM template set v0.2-draft, supplied to the Engineer seat on 2026-10-15 by the Director's instruction "CLAUDY — RECORD ARCHITECT VERIFICATION AND FINALIZE INTAKE READINESS" for verbatim preservation. The Engineer seat adds, infers or reconstructs nothing.
>
> **Provenance correction (2026-10-15).** From 2026-10-14 20:40 this file reproduced a different text, the Director-relayed Architect implementation instruction "CLAUDY — APPLY QA LEAD'S EXACT AMENDMENTS", and labeled it the QA Lead's verbatim decision. That attribution was wrong. The instruction text is preserved unchanged, correctly attributed, in `ARCHITECT_IMPLEMENTATION_INSTRUCTION_2026-10-14.md`. The amendments it conveyed (AM-1, AM-2, AM-3, the QAM-SR v1.0 adoption) match this decision; nothing applied in v0.3-draft changes as a result of the correction, and no template file was edited for it. The copy of this file inside `QAM_TEMPLATES_v0_3_AMENDED_FOR_ARCHITECT_2026-10-14_204903.zip` carries the earlier, mis-attributed content; that ZIP is preserved unchanged as historical evidence and the Architect's verification of it stands (`ARCHITECT_VERIFICATION_2026-10-14.md`).

| Field | Value |
|---|---|
| Decision | **ACCEPT WITH EXACT AMENDMENTS** on `TEMPLATES/QAM/` v0.2-draft; `QAM_RISK_REQUIREMENTS.md` §1 **ADOPT** as QAM-SR v1.0 |
| Decider | QA Lead (Fable) |
| Decision date | 2026-10-14 |
| Package reviewed | `QAM_TEMPLATES_QA_LEAD_REVIEW_v0_2` (`QAM_TEMPLATES_QA_LEAD_REVIEW_v0_2_2026-10-14_192019.zip`, SHA-256 `bffd05c6566fed627be0b00bd58fc290dae71e2b4f2c88f0bd3ab96bc75d21d4`; preserved) |
| Supplied to the Engineer seat | 2026-10-15, by the Director (Tony), for verbatim preservation |
| Recorded by | Claudy (documentation Engineer seat), 2026-10-15 12:03 +0600, transcription only |
| Applied in | `TEMPLATES/QAM/` **v0.3-draft** — `TEMPLATE_CORRECTION_RECORD_002.md` (AM-1, AM-2, AM-3, standing-requirements adoption); Engineer-verified (`ENGINEER_VERIFICATION_v0_3.md`); Architect-verified (`ARCHITECT_VERIFICATION_2026-10-14.md`: the amendments are accepted under this decision; no further QA Lead review is required for these exact edits) |
| What this record is not | Not a second QA Lead decision; not a decision on v0.3-draft as such (the Lead decided on v0.2-draft with these amendments, and the Architect verified their application); not intake approval; not sync authorization; not an installation |

## Decision text (verbatim, as supplied)

```text
QA LEAD DECISION — QAM template set v0.2-draft
Seat: QA Lead (Fable) · Date: 2026-10-14 · Package: QAM_TEMPLATES_QA_LEAD_REVIEW_v0_2
(all member hashes verified against HASH_MANIFEST; governing playbook SHA confirmed 97e111e2…5c897)

DECISION: ACCEPT WITH EXACT AMENDMENTS — the Engineer seat applies ONLY these three
edits and records them in a v0.3-draft correction record:

AM-1 — QAM_CLEANUP_REPORT.md §1: add column "Done at Q4 exit (if Q4 ran)" to the
routine phase-exit hygiene table. Rationale: Q4 is conditional, but when it runs it
is a real phase exit with owned browsers/servers/auth state.

AM-2 — QAM_PACKAGING.md §3, QAM_TEST_PLAN.md row, STOP column: replace "✔" with
"as relevant (a stop may precede the plan draft)". Rationale: a STOP raised during
preflight predates any plan; the current mark is unsatisfiable.

AM-3 — QAM_RISK_REQUIREMENTS.md §1, SR-3: insert "exit code" so it reads "cites an
evidence path with the command, working directory, exit code and unfiltered output".
Rationale: aligns SR-3 with evidence/README.md; the stricter form governs.

RISK REQUIREMENTS §1: ADOPT — as standing QA Lead requirements, version QAM-SR v1.0,
adopted by QA Lead (Fable) 2026-10-14, with AM-3 applied. Record the adoption in the
§1 header ("adopted by" line). SR-1…SR-11 are now my standing requirements and are
reusable across modules without per-module re-review.

REVIEW ANSWERS R-1 through R-7: all satisfied; no finding beyond the three amendments.
No seat-boundary leak, no sequence shortcut, no prefilled result, no path for an
engineering-green substitute. Verified mechanically: routing bodies byte-identical,
zero stray SHAs, state vocabulary ↔ dispatch table row-for-row.

Nothing in this decision installs the set; landing remains with the DocSet Sync run
at 03_BUILD_METHODOLOGY/_templates/QAM/ per AD-01, with explicit template
verification in that run's acceptance scope.
```

Transcription note: reproduced character-for-character from the text as supplied between the Director's `--- BEGIN QA LEAD DECISION ---` and `--- END QA LEAD DECISION ---` markers (the markers themselves are the Director's framing and are omitted). No word, number, identifier or line was changed, added or omitted.

## Where each element landed (pointer only; the Engineer seat's record of application is `TEMPLATE_CORRECTION_RECORD_002.md`)

| Element | Applied in |
|---|---|
| AM-1 | `TEMPLATES/QAM/QAM_CLEANUP_REPORT.md` §1 — column "Done at Q4 exit (if Q4 ran)" added; cells `NOT RECORDED` (unfilled) |
| AM-2 | `TEMPLATES/QAM/QAM_PACKAGING.md` §3 — `QAM_TEST_PLAN.md` row, STOP column: "as relevant (a stop may precede the plan draft)" |
| AM-3 | `TEMPLATES/QAM/QAM_RISK_REQUIREMENTS.md` §1, SR-3 — "… command, working directory, exit code and unfiltered output …" |
| RISK REQUIREMENTS §1: ADOPT | `TEMPLATES/QAM/QAM_RISK_REQUIREMENTS.md` §1 — heading "reusable; version QAM-SR v1.0; adopted by: QA Lead (Fable), 2026-10-14" and the STANDING REQUIREMENTS ADOPTION RECORD (SR-1…SR-11 with AM-3; reusable across modules without per-module re-review); §2 (Architect) and §3 (Executor) untouched |
| R-1…R-7 satisfied; no further finding | No template change required; recorded here and in the planning clarifications |
| "Nothing in this decision installs the set" | The set remains in intake staging; landing is the DocSet Sync run's, at `03_BUILD_METHODOLOGY/_templates/QAM/` (AD-01), with explicit template verification in that run's acceptance scope |

*QA LEAD DECISION RECORD — verbatim supplied text; transcription by the Engineer seat; provenance corrected 2026-10-15; no decision of the Engineer seat is contained here.*
