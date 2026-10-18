# Template Correction Record 002 — `TEMPLATES/QAM/` v0.2-draft → v0.3-draft (QA Lead's exact amendments)

> **CORRECTION RECORD — concise, for the Architect (amendment verification) and the QA Lead.** Lists everything that differs between the v0.2-draft set (the set the QA Lead reviewed; preserved byte-for-byte in `../INTAKE_ADDENDUM_001_v0_2/TEMPLATES/QAM/` and in `~/Downloads/QAM_TEMPLATES_QA_LEAD_REVIEW_v0_2_2026-10-14_192019.zip`, SHA-256 `bffd05c6566fed627be0b00bd58fc290dae71e2b4f2c88f0bd3ab96bc75d21d4`) and the v0.3-draft set in this folder. The substantive changes are exactly the QA Lead's amendments AM-1, AM-2, AM-3 and the standing-requirements adoption record; everything else is version/status bookkeeping, itemized below so the Architect can verify that nothing else moved.

| Field | Value |
|---|---|
| Authority | QA Lead (Fable) decision **ACCEPT WITH EXACT AMENDMENTS** on v0.2-draft, 2026-10-14 — preserved verbatim in `QA_LEAD_DECISION_2026-10-14.md`; relayed by the Director's instruction "CLAUDY — APPLY QA LEAD'S EXACT AMENDMENTS" |
| Applied by | Claudy (documentation Engineer seat), 2026-10-14 |
| Set version | v0.3-draft (governing playbook: QAM_PLAYBOOK v1.0, SHA-256 `97e111e2…5c897`, unchanged; standing requirements QAM-SR v1.0) |
| Placement | `03_BUILD_METHODOLOGY/_templates/QAM/` (AD-01); **not installed** |
| Files in the set | 25 (unchanged count; stable filenames; no file added or removed) |
| Status | QA Lead accepted with exact amendments; amendments applied and Engineer-verified (`ENGINEER_VERIFICATION_v0_3.md`); Architect amendment verification pending. **No second QA Lead decision exists or is implied.** |

## A. Exact amendments (substantive; authorized by the QA Lead)

| # | QA Lead amendment (as supplied) | Applied in v0.3 | File / location |
|---|---|---|---|
| AM-1 | Add the column "Done at Q4 exit (if Q4 ran)" to the routine phase-exit hygiene table; leave its execution results unfilled | Column added between "Done at Q2 exit" and "Evidence"; its three cells are `NOT RECORDED` (the set's unfilled marker, matching the existing Q1/Q2 cells); no result recorded | `QAM_CLEANUP_REPORT.md` §1 |
| AM-2 | In the `QAM_TEST_PLAN.md` row, replace the STOP-column "✔" with "as relevant (a stop may precede the plan draft)" | Replaced exactly; Q1 and Q2/Q4 cells unchanged | `QAM_PACKAGING.md` §3 |
| AM-3 | SR-3 wording: "Evidence: every PASS/FAIL cites an evidence path with the command, working directory, exit code and unfiltered output; existence checks precede greps/diffs so vacuous passes are impossible" | SR-3 row carries the supplied wording verbatim (adds "exit code"); playbook-basis and applies-to cells unchanged | `QAM_RISK_REQUIREMENTS.md` §1, SR-3 |
| SRA | Standing requirements adoption: version QAM-SR v1.0; adopted by QA Lead (Fable); date 2026-10-14; SR-1 through SR-11 adopted, with AM-3 applied; reusable across modules without per-module re-review. Replace the stale "NOT APPROVED" notice with the attributed adoption record; preserve the separate Architect and Executor sections | §1 heading now reads "reusable; version QAM-SR v1.0; adopted by: QA Lead (Fable), 2026-10-14"; the "DRAFT WORDING FOR QA LEAD ADOPTION OR AMENDMENT — NOT APPROVED" block is replaced by a STANDING REQUIREMENTS ADOPTION RECORD table (version, adopted by, date, scope SR-1…SR-11 with AM-3, reuse, decision source) and one sentence stating that the rows are the adopted text, that changes need a new adoption record, and that §2/§3 remain separate; SR-1, SR-2, SR-4…SR-11 text unchanged; §2 (Architect) and §3 (Executor) byte-identical to v0.2 | `QAM_RISK_REQUIREMENTS.md` §1 |

## B. Bookkeeping (version / status / index; no QA behavior changed)

| # | Change | Why | Files |
|---|---|---|---|
| B-1 | Version line `v0.2-draft (2026-10-14)` → `v0.3-draft (2026-10-14)` in every file's header (and the `_label` of `HANDOFFS/FILE_INDEX.template.json`) | Set version must be recorded in the set (AD-01) | all 25 |
| B-2 | Status label `NEWLY AUTHORED DRAFT — QA LEAD REVIEW REQUIRED` → `DRAFT v0.3 — QA LEAD ACCEPTED WITH EXACT AMENDMENTS (Fable, 2026-10-14); AMENDMENTS APPLIED AND ENGINEER-VERIFIED; ARCHITECT AMENDMENT VERIFICATION PENDING` in every header and footer where the old label appeared (header only in `CLAUDE.md` / `AGENTS.md`; the routing text between their markers is untouched and still byte-identical) | The old label described a review that has now been returned; the new label states the Lead's decision and the pending step without claiming a decision on v0.3 | all 25 |
| B-3 | `README.md` header: set version v0.3-draft with the revision chain (v0.1 → v0.2 → v0.3 and the two correction records); the sentence "**Not QA-approved.** The QA Lead reviews and accepts … never labeled QA-approved" replaced by the accurate status sentence (QA Lead accepted v0.2 with exact amendments; applied in v0.3, Engineer-verified; Architect verification and sync pending; no separate decision on v0.3); footer "not approved" → "not installed" | Status accuracy, as instructed | `README.md` header, footer |
| B-4 | `README.md` §2 row for `QAM_RISK_REQUIREMENTS.md`: "§1 … (draft wording for adoption or amendment)" → "(QAM-SR v1.0, adopted by the QA Lead 2026-10-14; reusable without per-module re-review)" | Mirrors SRA | `README.md` §2 |

Nothing else differs. The complete `diff -r` between the v0.2 and v0.3 sets, filtered of B-1/B-2 lines, shows only AM-1, AM-2, AM-3, SRA, B-3 and B-4 (`ENGINEER_VERIFICATION_v0_3.md` §2).

## C. Unchanged by design (verified, not merely asserted)

State vocabulary (19 states) and the dispatch table (19 rows); the single permission table (`QAM_ENTRY.md` §3); the dual-entry routing text (byte-identical between `CLAUDE.md` and `AGENTS.md` from the start marker to the end marker); Q1 → QA Lead approval → Director release → Q2; conditional repair/retest with `REPAIR RULED — AWAITING COMMIT` as a waiting state; the required §14 cleanup after the product verdict; the continuing `qa/<module>` branch at the completed engineering candidate commit (RUL-02); frozen contract and writable lanes (RUL-04); the pre-export snapshot rule; `<<…>>` placeholders; every result `NOT RUN`, every decision/verdict/acceptance `NOT RECORDED`, every identity `PENDING`; no SHA, credential, PASS, approval or certificate prefilled; no validators, exporters, dispatchers or runtime adapters (RUL-07). `TEMPLATE_CORRECTION_RECORD_001.md` (v0.1 → v0.2) is carried unchanged as history.

## D. Outside the template set (same addendum revision)

New: `QA_LEAD_DECISION_2026-10-14.md` (verbatim decision), this record, `ENGINEER_VERIFICATION_v0_3.md`. Updated: `00_ADDENDUM_INDEX.md` (v0.3; read order; status), `COMBINED_INTAKE_MANIFEST_001.md` (U3 v0.3; N-2(a) decision received; `_INBOX/` layout paths), `QA_LEAD_REVIEW_ENTRY.md` (one "review returned" paragraph prepended; body unchanged), `ADDENDUM_FILE_INDEX.json` (regenerated). Planning records in `../PLANNING_001/` revised to R4 only where they recorded N-2(a) as pending or cited the v0.2 folder as current. Not touched: `QAM_PLAYBOOK_v1_0.md`, `DIRECTOR_RULINGS_2026-10-14.md`, `ARCHITECT_DECISIONS_2026-10-14.md`, `TEMPLATE_PLACEMENT_RECOMMENDATION.md`, the v0.1 and v0.2 folders, the prior ZIPs, canonical doctrine, `_INBOX/`, skills, lints, CI; no Git action; no sync activation.

*CORRECTION RECORD 002 — the set is v0.3-draft: QA Lead accepted with exact amendments; amendments applied and Engineer-verified; Architect amendment verification pending.*
