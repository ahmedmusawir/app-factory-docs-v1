# Phase 2 review handoff — approval-ready (Fable, QA Lead, 2026-10-17T19:07:09+06:00)

**QA verdict: AMENDED-v1 ownership amendment CONFIRMED; QA-AF01 CLOSED (PASS) on independent retest of the corrected patch. No concrete unresolved blocker.** Gate 2 (amendment) and Gate 3 (matching specification) remain Tony's decisions, in that order. Phase 3 NOT RELEASED. No canonical implementation or Git mutation has occurred; no approval is claimed.

## 1. Verdict and matching specification

- Retest verdict: `QA_RETEST_AF01/QA_AF01_RETEST_VERDICT.md` — PASS, 12 checks, fresh BASE exports, own replay/hash/blob/lint evidence (`RETEST_VERIFICATION.json`, `RETEST_COMMANDS.json`).
- Matching specification: `QA_RETEST_AF01/DOCSET_SYNC_ACCEPTANCE_SPEC_AMENDED_V1_R1.md` — SHA-256 `2a3867cacef11c6bb0419a4c71229479efe703cee9fbcc1e4f71c0ac8e63f0fc`; 38 ACs, scope, exclusions, AC6 corrected-ownership wording and AC37 source-derived actor labels unchanged from AMENDED-v1; changes limited to the patch identity, QA-AF01 status, seat attribution and approval ledger (`SPEC_REVISION_R1.diff`).
- Seat attribution corrected: Cody Engineer (content amendment, serialization repair); Fable QA Lead (this verdict and specification). The 16:06 review's source-based evidence is carried forward; its "Cody, QA Lead" claim is withdrawn. No settled review was restarted.

## 2. Exact identities

| Object | Path | SHA-256 |
|---|---|---|
| Amendment record | `AMENDED_V1/AMENDMENT_V1.md` | `655e24edf2c53b8ca89563a66ada54ab6df09b930eb80a7a2743216dc1153764` |
| Amendment edits E373–E380 | `AMENDED_V1/AMENDMENT_V1_EDITS.json` | `274df38cbf0b2cefd91e05d505e71fc35d91f09cb16ca885234e80a300364893` |
| Ordered edits (380) | `AMENDED_V1/SELECTED_EXACT_EDITS.json` | `2675ffc148f49a95b688e9f252527950ce9c3f1fd61df3fb0ffb067fcc7ff687` |
| Amended index (101 paths) | `AMENDED_V1/EXECUTION_PROPOSAL_INDEX.json` | `69244f4edc347b30b81ed6a909bae4fbb5130864319e9f8cd84b5d5c22e59ba6` |
| **Corrected patch (executable)** | `REPAIR_QA_AF01/EXECUTION_PROPOSAL.corrected.patch` | `cf6413c9340c80f5c1bf53a55385876470e9b3aad364bc8963f52a68580f2a6d` |
| Submitted patch (history, not for execution) | `AMENDED_V1/EXECUTION_PROPOSAL.patch` | `ce4528d8db1183699ea8a90aaed266e91c991fe59b01747d4aa51e70acb3d58c` |
| **Specification AMENDED-v1-R1** | `QA_RETEST_AF01/DOCSET_SYNC_ACCEPTANCE_SPEC_AMENDED_V1_R1.md` | `2a3867cacef11c6bb0419a4c71229479efe703cee9fbcc1e4f71c0ac8e63f0fc` |
| Specification AMENDED-v1 (preserved) | `QA_AMENDED_V1/DOCSET_SYNC_ACCEPTANCE_SPEC_AMENDED_V1.md` | `103c7ede8a03e7bd0ea64f482e9d0b5a646b7720b8ae7f07729ea3482c9b8bd3` |
| Specification v1.0 (preserved) | `DOCSET_SYNC_ACCEPTANCE_SPEC.md` | `3910a62c34ff28acf1f9b956c5650deecae4ebd36872cc0072fd83e35ca19fa0` |
| Frozen approved map | `UPDATE_MAP.md` | `cd291270bb6c8e537bcb050685c6464d326254f0d2a703c21f7f304dfe286931` |

Amended documents: Blueprint `df17ac84…`, ARCHITECT_PLAYBOOK `3ec6bc37…`, ENGINEER_PLAYBOOK `b0f74569…` (full values in `FINAL_IDENTITIES.json`). BASE `9c179392…`.

## 3. Ordered Director decision block

Record in `QA_RETEST_AF01/DIRECTOR_DECISIONS.md`: **(1) Gate 2** — amendment AMENDED-v1 with the corrected patch `cf6413c9…` as executable representation; **(2) Gate 3** — specification R1 `2a3867ca…`, only after (1); **(3)** preservation commit, remote-baseline, worktree and explicit Phase 3 release receipts.

## 4. Preservation and setup

`QA_RETEST_AF01/OPERATOR_INSTRUCTIONS_FINAL.md` with `COMPLETE_PRESERVATION_PATHS.txt` (865 paths; extends the 846-path repair list with this handoff, its receipt and response). Tony retains all Git actions.
