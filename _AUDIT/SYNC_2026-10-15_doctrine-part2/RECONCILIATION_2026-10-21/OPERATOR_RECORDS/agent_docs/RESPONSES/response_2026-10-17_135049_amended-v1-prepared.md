# Cody (Engineer) — AMENDED-v1 prepared for D-1 / D-2 (2026-10-17)

**Outcome:** the bounded amendment is prepared, verified and packaged. It is a proposal that re-enters Gate 2. Not approved. Gate 3 pending Tony. Phase 3 NOT RELEASED. No canonical edits, no Git mutation, no edits to Fable's specification.

## Delivered

- ZIP: `/home/moose/Downloads/FACTORY_AMENDED_V1_REVIEW_2026-10-17_135049.zip`
- SHA-256: `4feb45de9818397b4ac18167f0f0e69a74f3aeb65bb38b1ef2860cfa5ecbd07e` (1,061,624 bytes; 26 members; 25 inventoried files; inventory self-check and payload-vs-run-directory comparison OK)
- Receipt: `_AUDIT/SYNC_2026-10-15_doctrine-part2/DELIVERY/AMENDED_V1_DELIVERY_RECEIPT.json`
- Run records: `_AUDIT/SYNC_2026-10-15_doctrine-part2/AMENDED_V1/` (frozen Gate 2 records untouched)

## The amendment

| Edit | Document | Old → New |
|---|---|---|
| E373 / D-1 | APP_FACTORY_BLUEPRINT.md lines 140–142 | `## 📋 ENGINEER AGENT: WHAT IT PRODUCES` + `The Engineer's full output list:` → `## 📋 ENGINEERING PACKAGE: APPROVED CONTRACT ARTIFACTS` + Architect-assembly lead sentence (exact brief text) |
| E374 / D-2 | ENGINEER_PLAYBOOK.md line 746 (§12 template fence) | `> **Author:** Engineer Agent` → `> **Author:** Architect` |

Each old span occurs exactly once at BASE, in the frozen proposed file and in the replay. IDs: D-1/MC-07/RUL-09/FC-008/FC-017/FC-027 and D-2/MC-07/RUL-09/FC-027. Authority: Architect text via Tony's brief; applies existing RUL-09; no new policy.

## Actual counts

| Item | Gate 2 | AMENDED-v1 |
|---|---:|---:|
| Ordered edits | 372 | 374 |
| Paths | 101 | 101 (2 hashes changed, 99 identical) |
| CHANGELOG rows / MANIFEST rows | 39 / 34 | 39 / 34 |
| Landing-date spans | 151 | 151 (identical) |
| Closeout spans / paths | 12 / 9 | 12 / 9 (unaffected) |
| Templates / archives / workflows / SVGs | 25 / 32 / 4 / 4 | unchanged |
| Certified findings | 97 (94 YES / 3 NO) | unchanged |

Identities: Blueprint `de0321e3…` → `5ac27e0d…` (14,634 B); ENGINEER `72477ec8…` → `ef3826c9…` (50,873 B); index `84337dcd…` → `c35406fe…`; frozen map `cd291270…` unchanged. Full table: `AMENDED_V1/AMENDMENT_IDENTITIES.json`.

## Verification result (Engineer checks — PASS; independent acceptance pending)

374-edit replay over pinned `9c17939` blobs with per-document residual equal to the frozen residual; 101/101 index hashes and before-hashes; header/history/MANIFEST cells unchanged for both docs; 151 date spans each once; 12 transitions still apply; RUL-09 traceability gains E373/E374; unchanged lint suite PASS on an overlay copy; two generator runs byte-identical; HEAD 626da8d, main = origin/main = 9c17939, nothing staged, empty canonical diff. Evidence: `AMENDED_V1/VERIFICATION.json`, `VERIFICATION_RAW.txt`.

D-4 recorded as an already-approved byte transformation (`D4_STARTER_KIT_METADATA_NORMALIZATION.json`); no content change. D-3 left out as instructed.

## Concrete blocker for Jarvis — OBS-1

`ARCHITECT_PLAYBOOK.md` lines 63 and 67, table "What the Architect Does NOT Do": `| Define data schemas | Engineer Agent |` and `| Define API contracts | Engineer Agent |` (retained BASE text). Same ownership family as D-1/D-2; after E373 the Blueprint says the Architect assembles those artifacts. Not in Fable's §5 table or the brief, so **not amended**. Needs an Architect decision before the amendment is frozen: fold into AMENDED-v1, defer to AMENDED-v2, or rule RETAIN with rationale. Nine ownership hits dispositioned in `AMENDMENT_V1.md` §7.

## Fable handoff

`AMENDED_V1/FABLE_HANDOFF_AMENDED_V1.md`: confirm D-1/D-2 on the amended tree; re-anchor only affected cells (372→374, two document hashes, index identity after approval, AC6(c)/(d) wording); derive the AC37 whitelist from `WORKFLOW_PUBLICATION_PLAN.json` — eight labels including **Reviewers** and **Authorized operator** — while keeping the persona/authority prohibitions. Specification untouched by Cody.

## Operator

`AMENDED_V1/OPERATOR_NEXT_STEPS_SUPPLEMENT.md` (gate order: Jarvis review incl. OBS-1 → Fable confirmation → Tony approves amendment at Gate 2 and spec at Gate 3 → preservation incl. `PRESERVATION_SUPPLEMENT.txt` paths → baseline → worktree → explicit Phase 3 release). Tony retains all Git operations.

## Files changed this assignment

New: `AMENDED_V1/` (21 files), `scratchpad/generators/cody_amend_v1.py`, `cody_amend_v1_verify.py`, `DELIVERY/AMENDED_V1_DELIVERY_RECEIPT.json`, this response. Updated: `session_2026-10-17.md`, `RECOVERY.md`. Nothing else.
