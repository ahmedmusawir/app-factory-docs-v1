# Fable — Phase 2 independent acceptance specification and map review — 2026-10-16 17:55 +0600

## Outcome

Package verified; Engineer counts confirmed; acceptance specification authored (DRAFT, derived against the unapproved map); 14 map corrections identified, 7 blocking-class; recommendation: Phase 3 NOT READY, Gate 2 should wait for the corrections.

## Engineer counts (all CONFIRMED independently)

| Claim | Check |
|---|---|
| 93 paths | 31 revised + 3 new playbooks + 25 templates + 32 archives (31 outgoing + restored QA v1.0) + MANIFEST + CHANGELOG |
| 31 revised | before-hashes = pinned main = worktree |
| 25 templates | translations replayed from the snapshot: 25/25 hashes match |
| archives | 31 byte-exact to baseline; QA v1.0 = blob bb41260f (SHA-256 32d17ef5…) |
| 334 edits | sequential replay 334/334; residual = header + one history row |
| lints | proposal tree PASS (36 docs) using scripts byte-identical to repo lints |

## Blocking map corrections (MC, full list in FABLE_MAP_REVIEW_2026-10-16.md)

- MC-01 FC-009 "historical pointer" label breaks markdown at 13 sites (table row, blockquotes, bullets).
- MC-02/13 duplicate "## Version History" sections in RECON_QUESTIONNAIRE and HANDOFF_PACKAGE_PLAYBOOK (rows appended after the footer).
- MC-03 CHANGELOG's 35 new rows sit after the footer, outside the table.
- MC-04 Blueprint lifecycle phases removed while SFP Phase Vocabulary, RECON:8, ENGINEER:123 and the MANIFEST FFM row still cite "Phase 5 — Deployment" / "four-role pattern".
- MC-06 FFM_PLAYBOOK and BIM_PLAYBOOK carry zero statements of Tony's two review checkpoints (post-FFM review; Engine 2 after all Engine 1 phases and QA).
- MC-07 retained contradictions: ENGINEER §12 "output the Engineer produces"; BIM §6 "[folder FREEZES here]" and §9 freeze line vs RUL-04; BIM §6 lifecycle lacks QA-branch/Q1/Q2/cleanup steps.
- MC-08 conditional status transitions lack the three MANIFEST row edits, a named commit, and the evidence files they cite.

Gate 2 questions: MC-05 Engine rows in the vocabulary table; MC-09 stripped status suffixes; MC-10 MANIFEST bump-procedure sentence removed; MC-12 ledger lacks W/RUL rows; MC-14 superseded template plan.

## Questions for Tony

- Q-1 Stick diagrams (SRC-W01…W04) stay historical and unreferenced; want a one-line supersession note (new content)?
- Q-2 Which commit applies the five status transitions (recommend: Tony closeout commit after Gate Q, then bounded retest)?
- Q-3 Keep or drop status suffixes (MC-09) and the MANIFEST bump sentence (MC-10)?

## Current phase, blockers, next action

Phase 2 (prepare execution) — Engineer preparation complete; Gate 2 NOT approved; spec DRAFT; Gate 3 pending; Phase 3 NOT released.
Blockers: MC-01…04, 06, 07, 08; Tony preservation commit + remote-baseline + worktree receipts; Gate 2; Gate 3.
Next action: Cody regenerates the proposal applying MC-01…MC-08 (and answers MC-12/14); Jarvis reviews; Tony rules Q-1…Q-3 and approves Gate 2; Fable re-anchors the spec for Gate 3.

Files: `_AUDIT/SYNC_2026-10-15_doctrine-part2/DOCSET_SYNC_ACCEPTANCE_SPEC.md`, `_AUDIT/SYNC_2026-10-15_doctrine-part2/FABLE_MAP_REVIEW_2026-10-16.md`.
