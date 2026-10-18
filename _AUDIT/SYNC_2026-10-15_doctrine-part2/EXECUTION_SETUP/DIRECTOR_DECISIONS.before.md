# Ordered Director decisions — AMENDED-v1 (final handoff, 2026-10-17T19:07:09+06:00)

**Neither decision is recorded.** QA verdict: ownership amendment CONFIRMED; QA-AF01 CLOSED (PASS) on the corrected patch. This form supersedes `QA_AMENDED_V1/ORDERED_GATE_DECISIONS.md` for recording; that file is preserved as history. Nothing here approves anything until Tony writes the decision.

## 1. Gate 2 — amendment AMENDED-v1 with corrected executable patch

- Decision: `<PENDING Tony>` · wording / timestamp: `<pending>`
- Amendment record: `AMENDED_V1/AMENDMENT_V1.md` — `655e24edf2c53b8ca89563a66ada54ab6df09b930eb80a7a2743216dc1153764`
- Amendment edits E373–E380: `AMENDED_V1/AMENDMENT_V1_EDITS.json` — `274df38cbf0b2cefd91e05d505e71fc35d91f09cb16ca885234e80a300364893`
- Ordered edits (380): `AMENDED_V1/SELECTED_EXACT_EDITS.json` — `2675ffc148f49a95b688e9f252527950ce9c3f1fd61df3fb0ffb067fcc7ff687`
- Amended index (101 paths): `AMENDED_V1/EXECUTION_PROPOSAL_INDEX.json` — `69244f4edc347b30b81ed6a909bae4fbb5130864319e9f8cd84b5d5c22e59ba6`
- **Executable patch (successor): `REPAIR_QA_AF01/EXECUTION_PROPOSAL.corrected.patch` — `cf6413c9340c80f5c1bf53a55385876470e9b3aad364bc8963f52a68580f2a6d`**
- Superseded submitted patch (history only): `AMENDED_V1/EXECUTION_PROPOSAL.patch` — `ce4528d8db1183699ea8a90aaed266e91c991fe59b01747d4aa51e70acb3d58c`
- Independent retest: `QA_RETEST_AF01/QA_AF01_RETEST_VERDICT.md` — PASS, 2026-10-17T19:07:09+06:00
- Frozen original map stays approved and unchanged: `UPDATE_MAP.md` — `cd291270bb6c8e537bcb050685c6464d326254f0d2a703c21f7f304dfe286931`

## 2. Gate 3 — matching specification (only after 1)

- Decision: `<PENDING Tony>` · wording / timestamp: `<pending>`
- File: `QA_RETEST_AF01/DOCSET_SYNC_ACCEPTANCE_SPEC_AMENDED_V1_R1.md` — **`2a3867cacef11c6bb0419a4c71229479efe703cee9fbcc1e4f71c0ac8e63f0fc`**
- Previous versions preserved: AMENDED-v1 `103c7ede8a03e7bd0ea64f482e9d0b5a646b7720b8ae7f07729ea3482c9b8bd3`; v1.0 `3910a62c34ff28acf1f9b956c5650deecae4ebd36872cc0072fd83e35ca19fa0`
- Gate 2 decision relied on: `<pending>`

## 3. Setup / release receipts (after 1 and 2)

- Preservation commit SHA: `<pending>` · remote BASE verification (`origin/main` = `9c17939…`) and timestamp: `<pending>` · execution worktree/branch checkpoint SHA: `<pending>` · explicit Phase 3 release: `<pending>`

If any identity above changes, a new attributable successor must be named; approval never transfers silently.
