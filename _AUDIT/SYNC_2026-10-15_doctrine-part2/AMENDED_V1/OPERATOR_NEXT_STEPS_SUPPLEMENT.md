# Operator next steps — supplement for AMENDED-v1 (2026-10-17, complete ownership correction)

Tony performs ALL Git mutations. This supplement sits on top of `../OPERATOR_NEXT_STEPS.md` (corrected Phase 2 map) and Fable's `../FABLE_GATE3_PRESERVATION_SUPPLEMENT.txt`; it changes the order of the gates, not the commands.

## Where we are

- Gate 2 APPROVED and recorded (map §O, approved identity `cd291270…6931`). Fable confirmed MC-01…14 with two retained contradictions (D-1, D-2). Her spec v1.0 (`3910a62c…9fa0`) is returned for Gate 3.
- **AMENDED-v1** (this directory) proposes the eight-span ownership repair (D-1, D-2, OBS-1 folded in per Jarvis, four sweep resolutions) on three documents. Per the map's freeze rule it **re-enters Gate 2**: Jarvis reviews, Fable confirms D-1/D-2, Tony approves the amendment. Until then the frozen Gate 2 identities remain the approved ones.
- **OBS-1 is resolved** inside this draft (Jarvis's rows, E375/E376). No open Architect decision remains; OBS-2 (`AMENDMENT_V1.md` §7) is an observation with no change proposed.
- Gate 3 (spec) is pending Tony; Fable will issue spec AMENDED-v1 re-anchoring only the affected cells (`FABLE_HANDOFF_AMENDED_V1.md`).
- Phase 3 is NOT RELEASED. Nothing in this package authorizes implementation.

## Order of operations

1. Upload `/home/moose/Downloads/FACTORY_AMENDED_V1_REVIEW_<timestamp>.zip` (path and SHA-256 in the response and `../DELIVERY/AMENDED_V1_DELIVERY_RECEIPT.json`) to Jarvis; forward `FABLE_HANDOFF_AMENDED_V1.md` to Fable.
2. Receive: Jarvis review (confirming the Engineer-worded P-1…P-4 under his rule), Fable confirmation (D-1/D-2 + OBS-1/P-1…P-4), Fable spec AMENDED-v1 (incl. the AC37 whitelist correction).
3. Approve the amendment at Gate 2 (and Gate 3 for the spec). Record the approval in run records as Fable did for Gate 2 (`GATE2_APPROVAL_RECORD_2026-10-17.md` pattern); Cody will then fold `AMENDED_V1/` records into the current executable map on an explicit instruction — not before.
4. Only after 3: preservation commit (§1 of `../OPERATOR_NEXT_STEPS.md`) **including** the paths in `PRESERVATION_SUPPLEMENT.txt` and Fable's supplement; remote baseline check (§2); execution worktree (§3); explicit Phase 3 release.

## Guards (unchanged)

Inspect `git status --short` before staging; never blanket-stage; `_INBOX/` stays out; do not merge the dirty review branch into main; no reset/rebase/stash. If `origin/main` ≠ `9c179392f79b70da099121fc357d3107ad3bb86e`, stop and return the actual SHA — before-hashes must be reconciled before any freeze or apply.
