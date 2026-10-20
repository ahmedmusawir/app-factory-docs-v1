# QA_PHASE4 — Phase 4 independent QA of the installed doc sync

Owner: Fable (QA Lead). Created 2026-10-19. Candidate: branch `docs/sync-doctrine-part2-2026-10-15` @ `20f71ee9…` (CONTENT_SHA `ef35d26d…`), approved spec R1 `2a3867ca…`.

| File | Purpose |
|---|---|
| `QA_READINESS_RECORD.md` | Fable's precondition evidence (24 checks PASS) and observations R-1…R-7; readiness decision READY |
| `qa_readiness.py` → `QA_READINESS.json`, `QA_READINESS_RAW.json` | reproducible readiness checks (read-only Git) and their raw command record |
| `OVERRIDES_AND_ALIGNMENT.md` | QA Lead alignment of the frozen spec with Tony's recorded rulings (O-1…O-8); no spec bytes change |
| `AC_EXECUTION_CHECKLIST.md` | the complete QA Executor assignment, AC1…AC38 + 10X-COPY, with commands, reads and the evidence layout |
| `QA_EXECUTOR_PROMPT.md` | the ready-to-run prompt for the fresh QA Executor session (Tony launches it) |
| `EXECUTOR_EVIDENCE/` | QA Executor package (Codex, fresh session, 2026-10-19T05:41Z): 31 PASS / 8 FAIL, findings F01–F07; byte-identical to `/home/moose/Downloads/QA_PHASE4_EXECUTOR_20f71ee_2026-10-19.zip` (SHA-256 `64ec4aca…`) |
| `qa_adjudicate.py` → `ADJUDICATION_EVIDENCE.json` | Fable's independent span checks (BASE vs candidate, map dispositions) for F01–F07 |
| `QA_LEAD_VERDICT.md` | **FAIL** — F01–F05 confirmed (AC5, AC6, AC9, AC15, AC16, AC18); F06/F07 rejected → follow-ups FU-1/FU-2; 33 PASS / 6 FAIL |
| `REPAIR_QA_P4/ENGINEER_REPAIR_PROMPT.md`, `REPAIR_FINDINGS.json` | one bounded repair assignment for Cody (AMENDED-v2, six documents, content-only) with acceptance criteria R1–R12 and the bounded retest list |

Nothing here modifies the candidate worktree, frozen records, `main`, or any Git state.

## AMENDED-v2 retest adjudication (2026-10-19 19:30)
Candidate `8dff354`: **FAIL on R4 only** (AC16 / FC-066); 11 PASS preserved. RV2-F01 CONFIRMED (narrowed): unlabelled `fetchProducts` consumers in APP_ARCHITECTURE_MANUAL §5 and STATE_MANAGEMENT_MANUAL §7 contradict API §3:172–174. Repair = AMENDED-v3 labels (`RETEST_AMENDED_V2/JARVIS_REPAIR_RECOMMENDATION.md`). Verdict: `RETEST_AMENDED_V2/QA_LEAD_VERDICT_V2.md`. Handback ZIP: `/home/moose/Downloads/FACTORY_QA_AMENDED_V2_VERDICT_HANDBACK_2026-10-19_193051.zip` (SHA-256 `7d8b58b747b952de0c1f573fc9c37219b9bf739c2ab274edc2fbb0460c6ae925`).

## AMENDED-v3 retest adjudication — Phase 4 product QA gate CLOSED (2026-10-20 16:50)
Candidate `26b050f`: **PASS WITH FOLLOW-UP FINDINGS**; 38/38 ACs met; AC16/FC-066 resolved by four labels. Verdict `RETEST_AMENDED_V3/QA_LEAD_VERDICT_V3.md`; handback `RETEST_AMENDED_V3/ARCHITECT_HANDBACK.md` (Jarvis: cleanup and closeout; 12 transitions still pending; PR/merge Tony-only). Handback ZIP `/home/moose/Downloads/FACTORY_QA_PHASE4_GATE_CLOSED_ARCHITECT_HANDBACK_2026-10-20_165031.zip` (SHA-256 `fbcabacdd39d74fc7fc63daf3f512cac42dafa0c0d8ab17306d980f842084dff`).
