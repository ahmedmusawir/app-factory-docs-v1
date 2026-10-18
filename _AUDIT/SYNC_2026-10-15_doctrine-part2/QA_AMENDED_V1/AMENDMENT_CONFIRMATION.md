# Consolidated AMENDED-v1 confirmation — Cody, QA Lead

Prepared 2026-10-17T16:06:55+06:00 under Tony’s current assignment. This session did not author or modify the amendment. The historical Engineer’s name is also Cody; independence here comes from fresh checks against source bytes and pinned Git blobs, without executing the Engineer’s generators or accepting their verification output as evidence. Tony explicitly assigns the current QA Lead seat. This is Phase 2 proposal review, not Gate Q on an installed candidate.

**Ownership amendment: CONFIRMED. Execution package recommendation: FAIL on QA-AF01 only.** No remaining acceptance failure was found in D-1, D-2, OBS-1 or P-1…P-4. Both Tony decisions remain pending; implementation is not released.

## Independent evidence

| Check | Result |
|---|---|
| Current 14:58 source ZIP | SHA-256 `711914a986cd64071f4372e0c428249ba27c6eba8ace160918c312d098b34f60`; CRC and member safety verified |
| Inventory | 27/27 hashes and local counterparts match; 28 ZIP members |
| Ordered edits | Original 372 preserved exactly; E373–E380 appended; 380/380 spans apply uniquely in order from BASE |
| Composed proposal | 101/101 hashes and sizes match; 33 before-hashes match BASE; only three target files differ from frozen proposal |
| Eight amendment edits | Independently applied to the frozen proposed files; exact equality with all three amended documents |
| Metadata/evidence | 31/31 replay residuals unchanged; 8 regenerated record pairs and 13 unaffected record hashes match |
| Ownership sweep | All 39 dispositions read; 31 retained live hits reproduced, locations and contexts checked; zero additional hits with the recorded query |
| Workflow actors/steps | Eight actor labels derived from unchanged plan; 7/18/8/24 steps agree with SVG and prose; prohibited persona/authority text absent |
| Lints | Full pinned suite PASS: 36 live docs, zero hits; no lint edits |
| Distributed patch | **FAIL: 99/101 outputs match; two archive EOF boundaries corrupted; Git check rejects** |
| Preservation | 797 protected source/run/canonical/skill/lint/intake files unchanged; Git refs and staging unchanged |

Verification command: `python3 -B -I _AUDIT/SYNC_2026-10-15_doctrine-part2/QA_AMENDED_V1/verify_amendment.py`, repository root; exit 1 represents the recorded patch fidelity failure. Full stdout is `VERIFICATION_RAW.txt`, structured checks in `VERIFICATION.json`; patch and lint command/cwd/exit/output are separately recorded. Two preliminary checker runs stopped while handling SVG visual line wrapping; the final checker normalizes whitespace and hyphen wraps, retaining exact words/order. No product failure was inferred from those harness assertions.

## Ownership judgments

| Items | Evidence in composed proposal | Judgment |
|---|---|---|
| D-1 / E373 | Blueprint:140–142 | Architect assembles approved contract artifacts for Engineering implementation; before-Design and optional-FILE_TREE rules preserved |
| D-2 / E374 | ENGINEER:746 | DATA_CONTRACT template author is Architect |
| OBS-1 / E375–E376 | ARCHITECT:63/67 | Engineer implements approved schemas and API contracts |
| P-1/P-2 / E377–E378 | Blueprint:87/88 | DB_SCHEMA and API_SPEC owner is Architect |
| P-3 / E379 | ENGINEER:86 | Implements approved contracts; changes return to Architect |
| P-4 / E380 | ENGINEER:998 | Database-schema implementation wording agrees with OBS-1 |

`OWNERSHIP_REVIEW.tsv` records the QA judgment for every supplied disposition. SFP database-phase headings/checklists describe a build discipline; Architect Engineer-Focus rows list implementation subjects. STRIPE:535 is the developer/DevOps operational split (OBS-2), not a Factory seat ownership grant. No new acceptance failure is asserted for those retained statements.

## Sole remaining acceptance failure

**QA-AF01:** executable patch serialization corrupts `_ARCHIVE/FRONTEND_BUILD_PHASE_PLAYBOOK_v1_2_2.md` and `_ARCHIVE/FRONTEND_FIRST_PLAYBOOK_v1_1_3.md`. The source payloads are correct. This defect is also reproduced in the frozen original patch. See `QA_AF01_PATCH_FIDELITY.md` for exact lines, hashes, route and bounded retest. Engineer correction and independent retest are required before implementation release. No repair was made in the QA seat.

## Matching specification and limits

`DOCSET_SYNC_ACCEPTANCE_SPEC_AMENDED_V1.md` preserves 38 AC IDs and the original exclusions. AC6 grades all eight corrected spans; AC37 derives the eight labels including Reviewers and Authorized operator from WORKFLOW_PUBLICATION_PLAN.json, retaining historical-persona and authority prohibitions. Counts/identities/reference paths and named session-preservation lanes are aligned. `SPEC_REVISION.diff` exposes every change.

D-3 stays a readability follow-up. D-4 records existing approved bytes and adds no content change. Template acceptance and intake were not restarted. Original map, original specification, exact source amendment and unaffected evidence remain intact. Jarvis’s acceptance and reported checks are attributable to Tony’s current assignment; the independent evidence above is separately generated.

Tony receives the exact amendment and matching spec together: Gate 2 amendment decision first; Gate 3 decision second. Neither is prefilled. Current instructions and a complete preservation list are included; setup remains gated by QA-AF01 resolution, actual approval records and operator receipts.
