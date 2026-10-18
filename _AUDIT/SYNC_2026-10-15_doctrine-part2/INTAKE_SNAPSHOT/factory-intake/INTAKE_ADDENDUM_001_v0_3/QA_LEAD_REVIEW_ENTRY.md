# QA LEAD REVIEW — start here (QAM template set v0.2-draft)

> **REVIEW RETURNED (2026-10-14).** The QA Lead (Fable) decided **ACCEPT WITH EXACT AMENDMENTS** on the v0.2-draft set and adopted the standing requirements as **QAM-SR v1.0** — decision preserved verbatim in `QA_LEAD_DECISION_2026-10-14.md`. The exact amendments (AM-1, AM-2, AM-3) and the adoption record are applied in `TEMPLATES/QAM/` **v0.3-draft** (`TEMPLATE_CORRECTION_RECORD_002.md`; Engineer verification in `ENGINEER_VERIFICATION_v0_3.md`). The Architect's amendment verification is the next step. The text below is retained unchanged as the record of what the v0.2 review asked; it is no longer a pending request.

> **REVIEW ENTRY — for the QA Lead.** This package asks for three things: (1) a review of the **actual template files** in `TEMPLATES/QAM/` (25 files), (2) adoption or amendment of the standing requirements drafted in `TEMPLATES/QAM/QAM_RISK_REQUIREMENTS.md` §1, and (3) an explicit **ACCEPT** or **HOLD** decision on the set's QA behavior. Nothing in this package is QA-approved yet; no execution result, approval or certificate is filled anywhere, and none should be filled during this review.

| Field | Value |
|---|---|
| Package | `QAM_TEMPLATES_QA_LEAD_REVIEW_v0_2_<timestamp>.zip` — members and hashes in `FILE_INDEX.json` (every member except itself) and `HASH_MANIFEST.sha256`; the ZIP's own SHA-256 is recorded outside the package (response file, session, `RECOVERY.md`) |
| Prepared by | Claudy (documentation Engineer seat), 2026-10-14, at the Architect's instruction relayed by the Director |
| Set under review | `TEMPLATES/QAM/` **v0.2-draft** (governing playbook QAM_PLAYBOOK v1.0); drafted by the Engineer seat from the Director-approved playbook; corrected per the Architect's review (`TEMPLATE_CORRECTION_RECORD_001.md`) |
| Decided home (not installed) | `03_BUILD_METHODOLOGY/_templates/QAM/` — Architect decision AD-01 under Director delegation (`ARCHITECT_DECISIONS_2026-10-14.md`) |
| Authority for the QA behavior | `QAM_PLAYBOOK_v1_0.md` (unchanged, SHA-256 `97e111e2a495f9a3fe65f50213e6f2ba68c8e5e963f3d23493b1ee99ad35c897`) and the Director rulings RUL-01…RUL-07 (`DIRECTOR_RULINGS_2026-10-14.md`) |
| Decision requested | **ACCEPT** (set may be instantiated once landed by the sync run) · **ACCEPT WITH EXACT AMENDMENTS** (list each edit; the Engineer seat applies only those) · **HOLD** (blockers with owner and required resolution) — plus **ADOPT / AMEND / REPLACE** for `QAM_RISK_REQUIREMENTS.md` §1 |

## Read in this order

1. `QAM_PLAYBOOK_v1_0.md` — the approved source (if not already known).
2. `DIRECTOR_RULINGS_2026-10-14.md` — RUL-01 mandatory QAM and five-seat chain; RUL-02 continuing QA branch; RUL-03 cleanup retained; RUL-04 frozen contract / writable lanes; RUL-05 review checkpoints; RUL-06 placement; RUL-07 boundaries.
3. `ARCHITECT_DECISIONS_2026-10-14.md` — AD-00 assessment, AD-01 template home and versioning arrangement.
4. `TEMPLATE_CORRECTION_RECORD_001.md` — what changed from v0.1-draft and why (C-1…C-12).
5. `TEMPLATES/QAM/README.md` — the set: ownership, Architect preparation duties, Engineer completion duties, the engagement flow.
6. The templates, in the order a run uses them: `CLAUDE.md` / `AGENTS.md` → `QAM_ENTRY.md` → `QAM_STATE.md` → `QAM_MANIFEST.md` + `HANDOFFS/ENGINEERING_HANDOFF.md` → `QAM_PREFLIGHT.md` → `QAM_RISK_REQUIREMENTS.md` → `QAM_RECON_REPORT.md` → `QAM_TEST_PLAN.md` → `QAM_APPROVAL.md` → `QAM_EXECUTION_REPORT.md` + `AC_EVIDENCE_MATRIX.md` → `FINDINGS.md` → `QAM_CERTIFICATION.md` → `QAM_CLEANUP_REPORT.md` → `QAM_PACKAGING.md` + `HANDOFFS/*` → `GOVERNING/`, `AUTOMATION/`, `evidence/` READMEs → `PARENT_ENTRY_ROUTING.md`.
7. `FILE_INDEX.json` / `HASH_MANIFEST.sha256` — membership and hashes.

## What the QA Lead is asked to judge (QA behavior)

| # | Question | Where |
|---|---|---|
| R-1 | Do the five seats' boundaries match the playbook §3 and RUL-01 — in particular that the Executor never composes an approval, disposition, retention decision or verdict, and that transcription is only expressly instructed and attributed? | `QAM_ENTRY.md` §3, `QAM_APPROVAL.md`, `QAM_CERTIFICATION.md` |
| R-2 | Is Q1 → approval (with Q1b amendment bookkeeping) → release → Q2 → adjudication → conditional repair/retest preserved, with no shortcut that lets Q2 or Q4 start on a folder path alone? | `QAM_ENTRY.md` §5, `QAM_STATE.md`, `QAM_APPROVAL.md`, `FINDINGS.md` §3 |
| R-3 | Are the standing requirements in `QAM_RISK_REQUIREMENTS.md` §1 the QA Lead's own, or how should they be amended or replaced? | `QAM_RISK_REQUIREMENTS.md` §1 |
| R-4 | Does the cleanup/certification sequence match RUL-03 and playbook §14: product verdict → required cleanup → cleanup acceptance + durable records → release to closeout, with the verdict independent of cleanup? | `QAM_CERTIFICATION.md`, `QAM_CLEANUP_REPORT.md` |
| R-5 | Are the evidence, privacy, credential and packaging rules (§10, §12, §13) sufficient, including the pre-export snapshot rule for `QAM_STATE.md`? | `evidence/README.md`, `AUTOMATION/README.md`, `QAM_PACKAGING.md`, `HANDOFFS/*` |
| R-6 | Are the result vocabularies and the STOP-* usage correct, with no result, approval or certificate prefilled? | `AC_EVIDENCE_MATRIX.md`, `QAM_EXECUTION_REPORT.md`, `QAM_RECON_REPORT.md` |
| R-7 | Anything in the set that would let an engineering-green result substitute for independent QA, or let a template field be mistaken for an executed result? | whole set |

## What this review does not decide

The DocSet Sync run and its timing (Director); the intake approval of either package (Director); the kit/worked-example homes (DEC-19 remainder); any Git action. Accepting the set does not install it; the sync run lands it at the decided home with explicit template verification in its acceptance scope.

## How to return the decision

Record the decision in your own words (ACCEPT / ACCEPT WITH EXACT AMENDMENTS / HOLD, and ADOPT / AMEND / REPLACE for §1 of the risk requirements), with the date and seat, and return it to the Director. The Engineer seat will apply only exact amendments and record them in a v0.3-draft correction record; it will not relabel the set as approved on its own.

*REVIEW ENTRY — nothing in this package is QA-approved; all execution results and approvals are unfilled.*
