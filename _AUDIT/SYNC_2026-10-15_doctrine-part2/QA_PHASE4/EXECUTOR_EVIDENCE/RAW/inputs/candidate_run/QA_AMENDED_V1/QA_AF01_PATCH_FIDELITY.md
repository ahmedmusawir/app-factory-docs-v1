# QA-AF01 — execution patch fails exact archive fidelity

**Classification:** Acceptance Failure in the executable proposal artifact; pre-existing in the frozen proposal serialization and carried into AMENDED-v1. Not introduced by E373–E380. **Severity:** High — blocks use of this patch for implementation. **Requirements:** AC2 exact indexed bytes, AC23 archive fidelity; MAP §C/§L; standing AC-S/AC-A.

**Expected:** applying the distributed `AMENDED_V1/EXECUTION_PROPOSAL.patch` to BASE reproduces all 101 indexed files exactly, including the original no-final-newline archive bytes.

**Actual:** GNU `patch --batch --fuzz=0 -p0` exits 0 but only 99/101 outputs match. In both affected archives the text `--- /dev/null` from the following patch header is appended to the last source line, followed by a newline. `git apply --check -p0` rejects the amended patch with exit 128: `patch fragment without header at line 29750`; it rejects the frozen original at line 29699.

**Exact locations:** amended patch lines 29748 and 30197; frozen patch lines 29697 and 30146. Both contain `+🥄 *Part of Stark Industries — App Factory doctrine.*--- /dev/null`.

| Output path | Expected bytes | Actual bytes | Expected SHA-256 | Actual SHA-256 |
|---|---:|---:|---|---|
| `_ARCHIVE/FRONTEND_BUILD_PHASE_PLAYBOOK_v1_2_2.md` | 23578 | 23592 | `362609b6551bd585c5f3c57ce5b751285871335d154ad2a8c97ca62b28a20702` | `731454ea6e8893ec9754f74c5b55f7fac5fa50335440e5ebdac3b631493282fe` |
| `_ARCHIVE/FRONTEND_FIRST_PLAYBOOK_v1_1_3.md` | 15043 | 15057 | `2516dcbd50f525328db955592c6c14eafa971c02d4dec722130a87505248a422` | `76ae7dc8984abdd70ef02333c6a2e36aef010300647a5e78165b32e8800d3c53` |

**Evidence:** `PATCH_MISMATCHES.json` (exact byte hashes and diffs), `PATCH_REPLAY_RAW.txt` (command, cwd, exit and full output), `PATCH_PROVENANCE.json` (both `git apply --check` outputs and original-patch replay), `VERIFICATION_RAW.txt`. Source archive payloads in PROPOSED_CONTENT and the amended index are correct; this is patch serialization, not an approved-content change.

**Route:** Engineer corrects no-final-newline handling in the patch serializer under an explicit bounded assignment, preserves all 101 target bytes and the 380 edits, records old/new patch identity and regenerates the affected packaging/identity records. QA does not repair the Engineer’s patch. Tony approves the exact resulting amendment identity; no silent replacement of this submission.

**Retest:** GNU patch replay AND `git apply --check` on a fresh BASE tree; compare all 101 outputs with the amended index; prove the two archive blob IDs equal BASE originals; recheck scope, preserved map/spec/source bytes and lint. The eight ownership corrections need no wording change. Until resolution, no Phase 3 implementation release.
