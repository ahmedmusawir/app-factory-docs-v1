# Fable — Gate 2 recorded, corrections confirmed, specification finalized for Gate 3 (2026-10-17)

## Outcome

**Gate 2 is recorded in the map. Cody's MC-01…14 corrections are confirmed. The acceptance specification is finalized as v1.0 and returned for Gate 3. Two retained contradictions (D-1, D-2) need a bounded map amendment before Phase 3 release.**

## Package and map identities

| Object | Result |
|---|---|
| Corrected review ZIP (…184920.zip) | SHA-256 matches Tony's brief; 510 of 510 payload hashes OK; every payload file byte-identical to the run directory |
| UPDATE_MAP.md before approval | `fae29812…09ae` matches the brief |
| EXECUTION_PROPOSAL_INDEX.json | `84337dcd…da39` matches the brief |
| Gate 2 record | written to map §O at 2026-10-17T11:19:57+06:00; only a 9-line insertion; reviewed wording preserved |
| Approved map identity | `cd291270bb6c8e537bcb050685c6464d326254f0d2a703c21f7f304dfe286931` |

## Independent confirmation (my replay, not Cody's evidence)

- 101 of 101 index hashes match; all 33 before-hashes equal pinned main.
- 372 of 372 edits apply once each; residual is header bump plus one history row, except the STARTER_KIT metadata normalization noted as D-4.
- 25 of 25 template translations replay exactly; 32 archives byte-exact; QA v1.0 restore equals the historical blob.
- 39 CHANGELOG rows sit inside the Ongoing table; MANIFEST's 34 rows equal their headers with suffixes preserved.
- 12 transitions on 9 paths resolve; 151 landing-date spans resolve; actual date and closeout SHA remain null.
- Four workflow documents and four SVGs: well-formed, step sequences match the publication plan, linked from owners.
- Lints pass on the approved tree with scripts identical to the repo's.

## MC dispositions

All fourteen confirmed as Cody dispositioned them. MC-07 is confirmed for its named sites, but two same-family sentences were never reached:

- **D-1** `APP_FACTORY_BLUEPRINT.md` lines 140–142 still read "ENGINEER AGENT: WHAT IT PRODUCES / The Engineer's full output list" with DATA_CONTRACT first. Contradicts RUL-09 and the corrected Phase 3 heading.
- **D-2** `ENGINEER_PLAYBOOK.md` line 746, inside the canonical DATA_CONTRACT template, still says "Author: Engineer Agent", ten lines under the new Architect-ownership note.

Both fail AC6 of the finalized spec as the approved tree stands. Bounded correction: two or three ENGINEER-PROPOSED spans on two paths, proposed by Cody, reviewed by Jarvis, approved by Tony as AMENDED-v1. No policy is reopened. D-3 (punctuation at five historical-pointer sites) and D-4 (generator-applied STARTER_KIT header normalization not written out as a span) are optional riders. I did not amend the approved map.

## Specification v1.0

38 ACs. Re-anchored to 101 paths, 372 edits, 39 CHANGELOG rows, 12 transitions on 9 paths, 89 selected FC rows plus 5 outside and 3 NO with the 94 YES / 3 NO register preserved, FC/W/RUL/AD traceability, preserved status suffixes and bump guidance, landing-date binding, both review checkpoints with conditional RRM routing. AC28 now permits exactly the four SVGs and four workflow documents with linkage checks. New AC37 grades the workflow documents and diagrams; new AC38 grades template installation verification. AC6 explicitly grades D-1 and D-2.

## Status

- **Phase 2 of 6:** Engineer preparation COMPLETE; Gate 2 APPROVED and recorded; Fable confirmation COMPLETE; specification FINAL, Gate 3 PENDING Tony; Phase 3 NOT RELEASED.
- **Correction confirmation result:** CONFIRMED WITH TWO RETAINED CONTRADICTIONS (D-1, D-2).
- **Gate 3 ZIP:** `/home/moose/Downloads/FACTORY_GATE3_FABLE_SPEC_REVIEW_2026-10-17_112715.zip` — SHA-256 `2a74128efa596080360d5ea011cf0ac39bcb8d847a1f47fab7d785fb297a0571`, 8 files, inventory verified after re-extraction.
- **Remaining blockers:** AMENDED-v1 for D-1/D-2 before Phase 3 release; Tony's preservation commit (add the paths in `FABLE_GATE3_PRESERVATION_SUPPLEMENT.txt`), remote-baseline and worktree receipts; Gate 3 approval.
- **Next operator action after spec approval:** Tony records Gate 3 in spec §7, runs the preservation commit with the supplemented pathspec, then the fetch/baseline check and the execution worktree checkpoint per `OPERATOR_NEXT_STEPS.md` §1–§3. Cody then proposes AMENDED-v1 for D-1/D-2; once Tony approves it, I issue spec AMENDED-v1 (count cells only) and Phase 3 can be released.

No canonical edits. No Git mutation. Files in the run: `DOCSET_SYNC_ACCEPTANCE_SPEC.md`, `FABLE_CORRECTION_CONFIRMATION_2026-10-17.md`, `GATE2_APPROVAL_RECORD_2026-10-17.md`, `FABLE_GATE3_PRESERVATION_SUPPLEMENT.txt`, `DELIVERY/GATE3_DELIVERY_RECEIPT.json`, `UPDATE_MAP.md` §O.

Response: `agent_docs/RESPONSES/response_2026-10-17_112715_gate3-spec-finalized.md`
