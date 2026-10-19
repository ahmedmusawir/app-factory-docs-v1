# Ordered Director decisions — AMENDED-v1 (final handoff, 2026-10-17T19:07:09+06:00)

**Gate 2 and Gate 3 APPROVED, recorded in that order below.** Tony approved both in the Jarvis Architect conversation on **2026-10-17 at 19:23:09 Asia/Dhaka (UTC+06:00)**, replying **“YES!!”** to the explicit question approving the reviewed changes and matching QA specification. Attribution: Tony relayed this approval and instructed Cody to record it in the 2026-10-18 execution-setup assignment; Cody has not independently accessed that external conversation. QA-AF01 is CLOSED (PASS) by Fable; Jarvis reviewed and accepted the final handoff, as relayed by Tony. Prior decision forms remain history. This records approvals already issued by Tony; it is not an approval by Cody or a Phase 3 release.

## 1. Gate 2 — amendment AMENDED-v1 with corrected executable patch

- Decision: **APPROVED — Gate 2, recorded first.** Tony: **“YES!!”**, 2026-10-17 19:23:09 Asia/Dhaka, approving AMENDED-v1 including the corrected execution patch identified below.
- Amendment record: `AMENDED_V1/AMENDMENT_V1.md` — `655e24edf2c53b8ca89563a66ada54ab6df09b930eb80a7a2743216dc1153764`
- Amendment edits E373–E380: `AMENDED_V1/AMENDMENT_V1_EDITS.json` — `274df38cbf0b2cefd91e05d505e71fc35d91f09cb16ca885234e80a300364893`
- Ordered edits (380): `AMENDED_V1/SELECTED_EXACT_EDITS.json` — `2675ffc148f49a95b688e9f252527950ce9c3f1fd61df3fb0ffb067fcc7ff687`
- Amended index (101 paths): `AMENDED_V1/EXECUTION_PROPOSAL_INDEX.json` — `69244f4edc347b30b81ed6a909bae4fbb5130864319e9f8cd84b5d5c22e59ba6`
- **Executable patch (successor): `REPAIR_QA_AF01/EXECUTION_PROPOSAL.corrected.patch` — `cf6413c9340c80f5c1bf53a55385876470e9b3aad364bc8963f52a68580f2a6d`**
- Superseded submitted patch (history only): `AMENDED_V1/EXECUTION_PROPOSAL.patch` — `ce4528d8db1183699ea8a90aaed266e91c991fe59b01747d4aa51e70acb3d58c`
- Independent retest: `QA_RETEST_AF01/QA_AF01_RETEST_VERDICT.md` — PASS, 2026-10-17T19:07:09+06:00
- Frozen original map stays approved and unchanged: `UPDATE_MAP.md` — `cd291270bb6c8e537bcb050685c6464d326254f0d2a703c21f7f304dfe286931`

## 2. Gate 3 — matching specification (only after 1)

- Decision: **APPROVED — Gate 3, recorded after Gate 2.** Tony: **“YES!!”**, same approval event, 2026-10-17 19:23:09 Asia/Dhaka, approving the exact matching R1 specification identified below.
- File: `QA_RETEST_AF01/DOCSET_SYNC_ACCEPTANCE_SPEC_AMENDED_V1_R1.md` — **`2a3867cacef11c6bb0419a4c71229479efe703cee9fbcc1e4f71c0ac8e63f0fc`**
- Previous versions preserved: AMENDED-v1 `103c7ede8a03e7bd0ea64f482e9d0b5a646b7720b8ae7f07729ea3482c9b8bd3`; v1.0 `3910a62c34ff28acf1f9b956c5650deecae4ebd36872cc0072fd83e35ca19fa0`
- Gate 2 decision relied on: §1 above, AMENDED-v1 and corrected executable patch `cf6413c9340c80f5c1bf53a55385876470e9b3aad364bc8963f52a68580f2a6d`.
- Authoritative specification selection is the R1 path/hash above. Any retained older self-reference inside the frozen R1 text does not select the older AMENDED-v1 specification; no specification bytes were changed.

## 3. Setup / release receipts (after 1 and 2)

- Preservation commit SHA: `<pending>` · remote BASE verification (`origin/main` = `9c17939…`) and timestamp: `<pending>` · execution worktree/branch checkpoint SHA: `<pending>` · explicit Phase 3 release: `<pending>`

If any identity above changes, a new attributable successor must be named; approval never transfers silently.

## Recording provenance

Recorded by Cody, Engineer, at 2026-10-18T17:39:26+06:00. Original blank form preserved at `EXECUTION_SETUP/DIRECTOR_DECISIONS.before.md` and in the unchanged final QA handoff ZIP. Approval time above is Tony’s reported actual decision time, not this later recording time. §3 stays pending until operator Git actions produce actual receipts. No new approval is requested.

## 4. Director-approved additive scope — standalone 10x references

Tony explicitly authorizes `10x Lab/ABM_PLAYBOOK_v1_0.md` and `10x Lab/APBM_PLAYBOOK_v1_0.md` in his subsequent execution-setup instruction, with final source location `/home/moose/Documents/`. Recorded by Cody, Engineer, at 2026-10-18T18:26:05+06:00. These are byte-for-byte standalone references, not canonical Factory integration. No MANIFEST, CHANGELOG, cross-reference, template, skill or README changes; no new review campaign/repository. Future updates are separate. Exact source/destination identities and copy verification are recorded in `EXECUTION_SETUP/STANDALONE_10X_AUTHORIZATION.json`.

The approved101-path/380-edit sync map and specification remain frozen and unchanged; these two additional paths are explicitly authorized and verified separately. The references must transfer to the isolated execution worktree and receive their own scoped two-file commit, separate from the sync implementation commit. Tony retains all Git mutations. Existing Gate2/Gate3 decisions remain approved; no Phase3 canonical implementation release is implied.
