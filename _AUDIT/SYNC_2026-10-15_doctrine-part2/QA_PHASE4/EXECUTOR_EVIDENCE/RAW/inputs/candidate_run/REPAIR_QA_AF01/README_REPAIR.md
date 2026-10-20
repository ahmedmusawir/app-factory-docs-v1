# QA-AF01-R1 — patch serialization repair for independent retest

Prepared by **Cody, Engineer** under Tony's explicit QA-AF01 repair assignment. Fable is QA Lead. **Engineer checks PASS; independent QA acceptance PENDING.** This is a transport/serialization correction, not a content amendment. Phase 3 remains NOT RELEASED.

## Exact replacement proposed

Use `REPAIR_QA_AF01/EXECUTION_PROPOSAL.corrected.patch` only after the remaining retest/approval/release gates. It replaces the executable representation at `AMENDED_V1/EXECUTION_PROPOSAL.patch`; the submitted file remains unchanged as history.

| Identity | SHA-256 |
|---|---|
| Submitted amended patch | `ce4528d8db1183699ea8a90aaed266e91c991fe59b01747d4aa51e70acb3d58c` |
| Corrected amended patch | `cf6413c9340c80f5c1bf53a55385876470e9b3aad364bc8963f52a68580f2a6d` |
| Unchanged 101-path amended index | `69244f4edc347b30b81ed6a909bae4fbb5130864319e9f8cd84b5d5c22e59ba6` |
| Unchanged 380 ordered edits | `2675ffc148f49a95b688e9f252527950ce9c3f1fd61df3fb0ffb067fcc7ff687` |

`REPAIR_IDENTITIES.json` carries full source/map/spec/patch identities. No document wording, archive payload, template, diagram, rule, exclusion, date binding or approval has changed.

## Cause and bounded change

The prior generator joined `difflib.unified_diff` records verbatim. For a source file without a final LF, the final added line had no LF, so the next file's `--- /dev/null` header was concatenated to its content. The serializer now emits an LF-delimited patch record followed by the standard `\ No newline at end of file` marker for any unterminated added, removed or context line. Input content bytes are not changed.

This patch differs by exactly **58 bytes: two 29-byte boundary/marker insertions**. Removing only those two sequences reproduces the submitted patch byte-for-byte. See `SERIALIZATION_DELTA.json` and `SERIALIZATION_REPAIR.diff`. The new `repair_and_verify.py` contains the corrected serializer and checks. Existing submitted generators remain preserved; do not rerun them and deploy their defective patch output. Any future regeneration must use equivalent EOF-aware serialization and repeat patch-to-index fidelity checks.

## Engineer evidence

- Fresh disposable baseline copies: read-only `git apply --check -p0` exits 0; GNU patch replay exits 0; all **101/101** replayed bytes/sizes/SHA-256 values match the unchanged amended index.
- Both affected archives equal their original BASE bytes and Git blobs, with final-newline state **absent** in source and replay. See `ARCHIVE_FIDELITY.json`.
- Full unchanged lint suite on the replayed result: PASS, 36 live documents, zero hits.
- Exact replay scope: 33 modifications and 68 additions; no extra output files. All 380 ordered edits remain unchanged and their sequence replays successfully.
- All five current or historical patch artifacts audited. Both selected-content patches and the conditional-closeout patch are byte-valid already; each passed its own Git check and GNU replay. Original frozen execution patch has the same defect; `frozen_execution.corrected.patch` is a **historical comparison fixture only**, not the current execution route. The amended corrected patch is the sole proposed active replacement.
- Seven serializer cases pass both readers: unterminated addition/removal/change, adding/removing a final LF, unterminated context and CRLF. This checks EOF handling beyond the two observed archives.
- 1,148 pre-existing files unchanged, including submitted patches, map, specifications, canonical docs, templates, diagrams, intake, skills, lints and prior evidence. Refs, staging and worktrees unchanged.

`COMMANDS.json` records command arrays, working directories, environment override, exit codes, full stdout and stderr. Large `git show` outputs are deliberately retained unfiltered. `VERIFICATION.json`, `REPLAY_101_HASHES.json`, `REPLAY_SCOPE.json`, `PATCH_ARTIFACT_AUDIT.json`, `SERIALIZER_CASES.json` and `LINT_RESULT.json` provide bounded result indexes.

The first harness attempt caught a child-lint `__pycache__` in its disposable tree after the patch/hash/archive/lint checks passed. The harness now supplies `PYTHONDONTWRITEBYTECODE=1` to child interpreters. Source lints were not edited. `ATTEMPT_01_*` preserves that attempt; the final full verification passed with an exact clean replay scope.

## Review package layout

`REPAIR_QA_AF01/` holds the repair and evidence. `CONTEXT/` holds byte-exact copies of the unchanged source index/edits, submitted patch, original map/spec, previous review/specification and operator records needed to assess the repair. Its layout is relative to the existing run. `SHA256SUMS.txt` inventories every payload except itself. Original packages remain intact.

Read `INDEPENDENT_RETEST_HANDOFF.md` and `QA_LEAD_REFERENCE_UPDATES.md` next. The QA Lead owns specification revisions and independent verdicts. Tony retains all Git mutations and ordered amendment/specification decisions. The exact successor patch must be identified; no approval of the old defective patch is silently transferred.

## Seat provenance correction

Earlier `QA_AMENDED_V1` records incorrectly describe Cody as reassigned QA Lead. They are preserved as submitted history, not relied on as Cody's independent acceptance. Tony has explicitly confirmed Cody's Engineer seat; Fable is QA Lead. Jarvis's independent reproduction of QA-AF01 and confirmation of the eight ownership corrections are attributed to Tony's present routing. This repair claims Engineer verification only.
