# Engineer Verification — `TEMPLATES/QAM/` v0.3-draft (amendments applied)

> **ENGINEER SEAT VERIFICATION — not QA, not Architect verification.** Read-only self-checks run by the authoring seat (Claudy) after applying the QA Lead's exact amendments, so that Jarvis (Architect) can verify the amendments against a stated baseline. The QA Lead's decision is in `QA_LEAD_DECISION_2026-10-14.md`; the change inventory is in `TEMPLATE_CORRECTION_RECORD_002.md`. Nothing here approves anything.

| Field | Value |
|---|---|
| Verified set | `TEMPLATES/QAM/` v0.3-draft, 25 files (hashes in §4; also in `ADDENDUM_FILE_INDEX.json` and the package `FILE_INDEX.json` / `HASH_MANIFEST.sha256`) |
| Baseline | `../INTAKE_ADDENDUM_001_v0_2/TEMPLATES/QAM/` v0.2-draft — the set the QA Lead reviewed, as packaged in `QAM_TEMPLATES_QA_LEAD_REVIEW_v0_2_2026-10-14_192019.zip` (SHA-256 `bffd05c6566fed627be0b00bd58fc290dae71e2b4f2c88f0bd3ab96bc75d21d4`) |
| Run by / when | Claudy (documentation Engineer seat), 2026-10-14 20:47 +0600, repository branch `factory-docs-review-astra-w-chunks`, HEAD `626da8d` (unchanged), nothing staged |
| Method | Python checks run with `-I` from the session scratchpad against the working tree; `diff -r` between the v0.2 and v0.3 sets; `sha256sum`; the repository lints (`lints/run_all.py`) compared with the day's baseline output |
| Result | **0 problems** on the v0.3 checks (§1–§3); the two "problems" reported by the older v0.1-era checker are known false positives, listed in §5 so they are not mistaken for findings |

## 1. Scope of difference against v0.2 (the "only authorized amendments and bookkeeping" check)

Every one of the 25 files differs from v0.2 in its version line and status label (bookkeeping B-1/B-2 of the correction record). After removing those pure label/version swaps, the complete `diff -r` leaves **35 lines in 4 files**, all accounted for:

| File | Lines | Accounted for by |
|---|---|---|
| `QAM_CLEANUP_REPORT.md` | 10 (5 −, 5 +) | **AM-1** — the §1 table gains the column "Done at Q4 exit (if Q4 ran)"; its three cells are `NOT RECORDED` (unfilled) |
| `QAM_PACKAGING.md` | 2 (1 −, 1 +) | **AM-2** — `QAM_TEST_PLAN.md` row, STOP column: "as relevant (a stop may precede the plan draft)" |
| `QAM_RISK_REQUIREMENTS.md` | 17 (3 −, 14 +) | **AM-3** (SR-3 wording with "exit code") and **SRA** (§1 heading and the STANDING REQUIREMENTS ADOPTION RECORD replacing the "NOT APPROVED" notice) |
| `README.md` | 6 (3 −, 3 +) | **B-3** (header status sentence and revision chain; footer "not approved" → "not installed") and **B-4** (§2 row for the risk file) |

Checks that bound the change:

| Check | Result |
|---|---|
| SR-1…SR-11 rows (11) compared row-by-row with v0.2 | only SR-3 differs (AM-3) |
| `QAM_RISK_REQUIREMENTS.md` §2 (Architect) and §3 (Executor) compared with v0.2 | identical (footer label aside) |
| Dual-entry routing region (`CLAUDE.md` ↔ `AGENTS.md`, start marker to end marker) | byte-identical to each other **and** to v0.2 |
| Stale text anywhere in the set: `QA LEAD REVIEW REQUIRED`, `v0.2-draft (2026-10-14)`, `<<STANDING_VERSION>>`, `DRAFT WORDING FOR QA LEAD ADOPTION`, `NOT APPROVED`, "start(ing) commit" | none |
| Exact amendment strings present exactly once each (AM-1 header + 3 rows; AM-2 row; AM-3 row; adoption heading, version, adopter, date, scope, reuse) | yes |
| Files added / removed in the set | none (25 → 25; stable filenames) |

## 2. Structural and unfilled-field checks (unchanged behavior)

| Check | Result |
|---|---|
| Template completeness (22 playbook-named items + `README.md`, `QAM_PACKAGING.md`, `PARENT_ENTRY_ROUTING.md`) | 25/25 present; no unexpected file |
| Status label and `v0.3-draft (2026-10-14)` version line | 25/25 |
| State vocabulary (`QAM_STATE.md`) ↔ dispatch table (`QAM_ENTRY.md` §5) | 19 states ↔ 19 rows; no state without a row, no row without a state |
| Result rows (`QAM_PREFLIGHT.md` 27, `QAM_EXECUTION_REPORT.md` 1, `AC_EVIDENCE_MATRIX.md` 1) | all `NOT RUN` |
| `QAM_APPROVAL.md` Decision · `QAM_CERTIFICATION.md` Verdict · cleanup acceptance · identities | `NOT RECORDED` / `PENDING`; no `PASS` cell outside vocabulary headers |
| Hash-like literals (40/64 hex) other than the playbook hash; credential-like strings | none |
| "QA-approved" wording | appears only negated or as the rule "never labeled QA-approved"; the new label states the Lead's recorded decision, not an approval of v0.3 |
| Encoding: CRLF, BOM, single H1 per Markdown file; JSON files parse (`HANDOFFS/FILE_INDEX.template.json`, `ADDENDUM_FILE_INDEX.json`) | clean |
| Path tokens in the addendum and planning documents | 453 checked; all resolve or are declared missing/known-not-yet-existing (see §5 for the checker's own whitelist gaps) |

## 3. Preservation checks (nothing else moved)

| Item | Result |
|---|---|
| `../INTAKE_ADDENDUM_001_v0_2/` (the reviewed set + records) | 30/30 files unchanged against its `ADDENDUM_FILE_INDEX.json` |
| `../INTAKE_ADDENDUM_001_v0_1/` | 28/28 unchanged |
| `~/Downloads/QAM_TEMPLATES_QA_LEAD_REVIEW_v0_2_2026-10-14_192019.zip` | present; SHA-256 unchanged (`bffd05c6…21d4`) |
| `~/Downloads/CONSOLIDATED_INTAKE_001_2026-10-14_184845.zip` | present; SHA-256 unchanged (`4c9d8e5b…2671`) |
| `QAM_PLAYBOOK_v1_0.md` | SHA-256 `97e111e2a495f9a3fe65f50213e6f2ba68c8e5e963f3d23493b1ee99ad35c897`, unchanged |
| Harvest `FILE_INDEX.json` · `SOURCE_INVENTORY.json` | 75/75 · 22/22 unchanged |
| Correction Package 001 (9 files) | 9/9 unchanged |
| 100 protected canonical/CI files (`protected_after.sha256` baseline) | 100/100 unchanged |
| Repository lints (`lints/run_all.py`: encoding, retired terms, versioned refs, header) | output identical to the day's baseline (9 known findings, all pre-existing, unrelated) |
| `DIRECTOR_RULINGS_2026-10-14.md`, `ARCHITECT_DECISIONS_2026-10-14.md`, `TEMPLATE_PLACEMENT_RECOMMENDATION.md`, `TEMPLATE_CORRECTION_RECORD_001.md` | byte-identical to v0.2 copies |
| Git | HEAD `626da8d`; nothing staged; no Git write command run |

## 4. Hashes of the v0.3-draft set (SHA-256; paths relative to `TEMPLATES/QAM/`)

```text
ce619971ec58604e09f768de64337367cafec29ca30367b019e475c7ebf70883  AC_EVIDENCE_MATRIX.md
13c5be461a00bd6239da3b5a247bd91130c85dcf519da59b231fcc421e62eced  AGENTS.md
76d5fb29a0f2ee90e7281f091894e1f04c394a3cacea9606a5aa51438d5fcc45  AUTOMATION/README.md
bf7d4ff22b5d8c14d8f370cc128bc23553a1d95ddb41545700e64a9d080ad535  CLAUDE.md
385ad08e235c77b50a62ab78c5976e00df4f2167fc40f814f0300646a532d6df  evidence/README.md
c17a149be9a6bea8aaac720c3de47ea9e7b5402bb86792b466c8e5a6f2156385  FINDINGS.md
b11da26e2793bd9bf816b51840f007922b3e4028a6298be7494e834ce28aee20  GOVERNING/README.md
ccb15192ecccfd1dceae95fa2e7f0b2fa6bd9e19f4956e1295964a89eaa7391f  HANDOFFS/ENGINEERING_HANDOFF.md
fa5705561225dc1b108c2e2173121f6949f0d9141d6b5010b577cb5d15e5e2fb  HANDOFFS/FILE_INDEX.template.json
82876906ba38d2d57506e934e645c38675768d5d76a66089b343d31273ecaba0  HANDOFFS/README.md
a7dc1fcac42b30ce6dd270078f5e9202d22aa011e2e531871acb0f5086d37633  HANDOFFS/REVIEW_START_HERE.md
769345f5dc96fd52a654b65f663d51cacfa2ac65dd5b4f275afba01be9c38eb1  PARENT_ENTRY_ROUTING.md
caa2c0f8080bfdecdd48a5c11830ad3ea162c1dd309d87738045a63b58fa6538  QAM_APPROVAL.md
b2e7db8d3b27c064914bb30f269bd7ab46276eaef92ed3cfeb973c0abe144d19  QAM_CERTIFICATION.md
0a2eb83607a81870031d96190263531afed26745fffc8218a3a004293c92a4c1  QAM_CLEANUP_REPORT.md
bc15f3c613a144be5a50c811752f00905a9585c6c4eb87300b7ee105da2c01fa  QAM_ENTRY.md
723afabf776deddae595dfda5f1bca70dfc2c5616da32fe63de9dcf45e5b7177  QAM_EXECUTION_REPORT.md
2dc5ebb4dd8d257047b4f72b53122ad67953372106ddb7f2662a6858c5948c62  QAM_MANIFEST.md
1a9a61ae19b2ee98cc481368d46ec0403895225f51afaec293e440d3ccc84ea7  QAM_PACKAGING.md
a887e728a817b51944583c30d89a285820fb680c80c2568459ba32ea374f97c6  QAM_PREFLIGHT.md
977fb2630ac38727936abc0770e748a705d377b31850a875beb841563eb9b764  QAM_RECON_REPORT.md
6e8cfb4e2df064b5eb8c2402654b66dec774b10c173a76134c04c65e854a4d76  QAM_RISK_REQUIREMENTS.md
487b60e8bb7c45f1f246fa9d22e276a6498b1fdd2ddb90fd99d847e8a6d78a1e  QAM_STATE.md
2df20cbd259a76d4bb58759478c30ce21e2774cfff64e8a796b142c1e7020dc7  QAM_TEST_PLAN.md
8ccc80f3f2f89549bd4a29260f236a33fe4eee5b3f08933ca62fb08e5bcbd0c3  README.md
```

## 5. Known false positives of the older checker (not findings)

| Reported | Why it is not a finding |
|---|---|
| `QAM_CERTIFICATION.md` missing "never write this file"; `QAM_APPROVAL.md` missing "QA Executor never writes this file" | v0.1-era phrase checks. Those sentences were deliberately replaced in v0.2 (correction C-8: the Executor may transcribe exact supplied text only when expressly instructed, attributed). The v0.2 copies do not contain them either. |
| Unresolved `HANDOFFS/FILE_INDEX.template.json` in the correction records; `SOURCES/RRM/SRC-R02_RRM004_ORIGINAL_PACK_v1_0.zip` in the clarifications | Both files exist (relative to `TEMPLATES/QAM/` and to `factory-intake/`); the checker resolves only against the citing document's folder and the repository root. |
| Unresolved `ENGINEER_VERIFICATION_v0_3.md` | This file; the check ran before it was written. Re-run after writing: resolves. |

## 6. Package (built after this file; verified after re-extraction)

The ZIP for Jarvis contains: the 25 v0.3-draft templates under `TEMPLATES/QAM/`; the governing sources `QAM_PLAYBOOK_v1_0.md` (byte-identical, hash above), `DIRECTOR_RULINGS_2026-10-14.md` (R1.2) and `ARCHITECT_DECISIONS_2026-10-14.md`; `QA_LEAD_DECISION_2026-10-14.md` (verbatim decision); `TEMPLATE_CORRECTION_RECORD_001.md` and `TEMPLATE_CORRECTION_RECORD_002.md`; this file; `FILE_INDEX.json` (every member except itself: archive path, source path, bytes, SHA-256) and `HASH_MANIFEST.sha256` (every member except itself). Membership is exact (no extra, no missing), paths are safe, and the archive is integrity-tested after re-extraction. The ZIP's own SHA-256 is recorded **outside** the package (response file, session log, `RECOVERY.md`), per the snapshot rule the set itself prescribes (`QAM_PACKAGING.md` §6).

*ENGINEER SEAT VERIFICATION — results of read-only self-checks; the Architect's amendment verification and the QA Lead's authority are not replaced by this file.*
