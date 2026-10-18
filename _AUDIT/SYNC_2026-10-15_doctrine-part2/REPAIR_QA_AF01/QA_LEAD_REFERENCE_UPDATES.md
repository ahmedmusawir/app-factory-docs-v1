# References requiring QA Lead / Director disposition — no specification edits by Engineer

The corrected patch path is `REPAIR_QA_AF01/EXECUTION_PROPOSAL.corrected.patch`; new SHA-256 `cf6413c9340c80f5c1bf53a55385876470e9b3aad364bc8963f52a68580f2a6d`, 1,906,921 bytes. Submitted path `AMENDED_V1/EXECUTION_PROPOSAL.patch`, old hash `ce4528d8db1183699ea8a90aaed266e91c991fe59b01747d4aa51e70acb3d58c`, 1,906,863 bytes, stays preserved.

| Existing record | Affected reference | Required owner action |
|---|---|---|
| QA_AMENDED_V1/DOCSET_SYNC_ACCEPTANCE_SPEC_AMENDED_V1.md:38 | §0.1 exact patch path/hash | QA Lead identifies the corrected execution representation in a separate matching successor revision, preserving submitted bytes |
| Same specification:9,40,177 | QA-AF01 outstanding status and release prerequisite | Update only after independent retest; cite actual verdict and corrected patch identity, never Engineer PASS as independent acceptance |
| QA_AMENDED_V1/REVIEW_IDENTITIES.json | amendment_records.EXECUTION_PROPOSAL.patch and known_failure | Preserve as historical reviewed identity; use REPAIR_IDENTITIES.json plus an attributable QA successor identity/verdict record |
| QA_AMENDED_V1/ORDERED_GATE_DECISIONS.md:13 | reviewed defective patch and pending resolution | Tony records the actual successor identity/retest receipt when deciding Gate 2, then exact QA-authored spec hash for Gate 3 |
| AMENDED_V1/AMENDMENT_IDENTITIES.json:62 | original transport patch amended_sha256 | Historical original is untouched. Repair overlay names only this replacement representation; all content/index/edits identities stay unchanged |
| QA_AMENDED_V1/OPERATOR_INSTRUCTIONS.md §1 and source amendment supplements | old-patch repair step and execution source | Use current repair operator supplement after independent retest and exact approvals; do not apply the old patch or infer release from new-file existence |

AC2 exact output hashes and AC23 archive fidelity retain their meaning. AC6 ownership, AC37 approved actor labels, all exclusions and unchanged content identities need no rewriting for this repair. QA Lead also reconciles the earlier erroneous Cody-QA-Lead authorship/independence assertions when issuing her own specification revision; this Engineer does not change those submitted records.

Gate 2 amendment/successor decision: PENDING. Gate 3 matching specification: PENDING. Independent QA acceptance: PENDING. Phase 3: NOT RELEASED.
