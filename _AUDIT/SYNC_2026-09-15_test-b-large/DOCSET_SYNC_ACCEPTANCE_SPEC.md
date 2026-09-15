# DOCSET_SYNC_ACCEPTANCE_SPEC — test-b-large — 2026-09-15

> **Gate 3 APPROVED — FROZEN.** Approved by Tony on **2026-09-15 at 20:22:59 Asia/Dhaka (UTC+06:00; 14:22:59 UTC)**. Phase 3 derivation only, authored by Jarvis acting as **Sol (QA Lead)**. Every acceptance criterion derives from approved intake, an approved UPDATE MAP row, or a standing sync invariant. This document records the contract for later independent verification; it does not report candidate PASS results or authorize Phase 4.

## 0. Header and derivation sources

| Field | Value |
|---|---|
| Run ID | `SYNC_2026-09-15_test-b-large` |
| Repository / working copy | `app-factory-docs-v1`; the Operator-designated existing working copy |
| Branch | `test/docset-sync-v07-large-001` — verified with `git rev-parse --abbrev-ref HEAD` |
| BASE_SHA / verified HEAD at derivation | `dd6d496a3b269a6bf83ce4e85101d8e0e6e785b9` — verified with `git rev-parse HEAD` |
| Approved map | [UPDATE_MAP.md](UPDATE_MAP.md), APPROVED at Gate 2 on 2026-09-15, **AMENDED-v1 APPROVED at Gate 2 on 2026-09-15**, frozen; approval record §O |
| Map SHA-256 at derivation | `98a033eeddd7a00cf21e34dc986645c335b3234698079d35a7506724eced6cba` (local, uncommitted source bytes) |
| Approved correction package | `_INBOX/TEST_B_CORRECTION_PACKAGE/INDEX.md` and `CORRECTION_001.md` through `CORRECTION_004.md`; TB-CP-001 through TB-CP-004 |
| Approved lesson | `_INBOX/odd_payload.md`; `IN-2026-09-15-01`, classification and approval in MAP §A |
| Standing source | `_SKILLS/factory-docs-update/_shared/references/STANDING_INVARIANTS.md`, the ten families supplied by skill v0.7-DRAFT |
| Method | Family `CLAUDE.md` D20; `sync-qa/SKILL.md` Stage S1; shared acceptance-spec template |
| Author / date | Jarvis acting as Sol, QA Lead; 2026-09-15 |
| Status / amendments | **Gate 3 APPROVED; FROZEN** — Tony, 2026-09-15 20:22:59 Asia/Dhaka (UTC+06:00; 14:22:59 UTC); approved exactly as derived; no spec amendments |
| AC count | **23**, numbered AC1–AC23; all ten standing families represented |
| Verdict vocabulary for later QA | PASS / PASS WITH FOLLOW-UP FINDINGS / PASS WITH KNOWN RISK / FAIL / BLOCKED |

**Source discipline.** Run-specific derivation inputs were limited to the approved package, `odd_payload.md`, and AMENDED-v1 UPDATE MAP. The skill reading path supplies methodology and standing invariants. No previous validation report, Astra review, unrelated reviewer artifact, or content under `fable-sync-review/` was read. Canonical anchors and baseline claims below are taken from the approved map for contract derivation; Cody must independently verify them later. Recovery/session narratives are not derivation evidence. The local intake and map remain valid sources despite being intentionally uncommitted.

**Notation.** `MAP` means the approved AMENDED-v1 map above. `STANDING AC-X` means the corresponding row in STANDING_INVARIANTS.md. `SKILLS` means `03_BUILD_METHODOLOGY/APP_FACTORY_SKILLS_PLAYBOOK.md`; `ENGINEER` means `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md`. Other filenames in MAP §B/§F retain their map locations. Line anchors below are **BASE_SHA anchors**, not a demand that candidate line numbers stay fixed. `<EXEC_DATE>` is the actual Phase 4 date in YYYY-MM-DD, consistently substituted as MAP §C requires. It is not fixed to this spec's authoring date.

## 1. Objective and scope

Prove that a later candidate implements the approved five-ID ledger with the exact approved wording, preserves existing doctrine, and satisfies the standing sync invariants within this disposable TEST B run.

### 1.1 Intake coverage

| Approved ID | Approved disposition → expected final disposition | Implementation / verification source | ACs |
|---|---|---|---|
| TB-CP-001 | CHANGE → ENCODED | MAP §B invariant 1; §C 1a/1b | AC1–AC5, AC10–AC12, AC14–AC23 as applicable |
| TB-CP-002 | CHANGE → ENCODED | MAP §B invariant 1; §C 2a/2c | AC1–AC4, AC7, AC10–AC11, AC13–AC23 as applicable |
| TB-CP-003 | Approved NO-CHANGE → NO-CHANGE | MAP §B invariants 1/2 and approved NO-CHANGE evidence | AC1–AC4, AC9, AC12; approved audit citations in AC10/AC17/AC21 |
| TB-CP-004 | CHANGE → ENCODED | MAP §B invariant 1; §C 2a/2b/2c; §K-3; §O AMENDED-v1 | AC1–AC4, AC8, AC10, AC13–AC23 as applicable |
| IN-2026-09-15-01 | CHANGE → ENCODED | MAP §A approved content-first lesson disposition; §B invariant 1; §C 1a/1b | AC1–AC4, AC6, AC10–AC12, AC14–AC23 as applicable |

In scope: the two canonical docs, five enumerated §C rows (1a, 1b, 2a, 2b, 2c), two archive additions, MANIFEST/CHANGELOG changes in §G, §B searches, §F dependents, §H references, and §L preservation. §D has no new canonical files; §E has no approved deletion or supersession; §J has no parked cross-boundary item.

Explicitly excluded from repair requirements:

- No ledger ID is SPLIT, DEFERRED, or BLOCKED. `DRIFT-2026-09-15-01`, `-02`, and `-03` are parked; QA grades their preservation, not their correction. `DRIFT-2026-09-15-04` and `-05` are cleared only by the approved infrastructure date updates.
- The nine pre-existing lint findings in §4 are retained. Unrelated canonical docs, `_SKILLS/**`, `_OTHERS/**`, `lints/**`, `.github/**`, governance, and other repositories have no authorized edits.
- MAP §E's APP_FACTORY_BLUEPRINT stale forward-reference and §I's historical versioned filenames remain follow-up observations. Unrelated findings cannot expand the acceptance contract.
- The synthetic brief-completeness waiver and K-1 version choices apply only to TEST B. Missing waived fields supply no additional invariants, evidence requirements, or production doctrine. Intent comes from the actual briefs and approved rows.
- Merge target is **NONE**, per MAP §K-2/§O: no PR, merge, compare URL, or PR-number prerequisite is required for this run. ENCODED records implementation on the test candidate, not a production merge.

### 1.2 Preconditions for Cody's later verification

These are **BLOCKED, not FAIL**, if unmet at QA entry; they are not additional ACs and are not expected to be complete at Gate 3:

- Approved map and Gate 3-approved spec are present at the candidate SHA; referenced approved intake is available.
- Handoff records CONTENT_SHA, which exists on the run's remote branch and is an ancestor of QA_START_SHA. Only approved run audit/handoff files, `RECOVERY.md`, `session_*.md`, or `agent_docs/RESPONSES/*` changed after CONTENT_SHA; no canonical change follows it.
- Cody independently records QA_START_SHA from `origin/test/docset-sync-v07-large-001` at QA entry. Retest uses the corresponding REPAIR_CONTENT_SHA and independently recorded QA_RETEST_SHA; a moved tip invalidates prior PASS rows.
- Lints execute on the QA rig; no unresolved MAP §K decision or ambiguous/untestable AC prevents verification.

Source: STANDING preconditions and AC-S; MAP §0/§K/§M/§N/§O; skill SHA_AND_PUSH_CONTRACT and sync-qa Stages S2/S4. No candidate verification is performed during this derivation.

## 2. Acceptance criteria

All rows require evidence at QA_START_SHA or the applicable QA_RETEST_SHA, except lifecycle evidence explicitly identified below. Commands and candidate path:line reads belong in Cody's matrix. Final Gate Q results are owned by Sol.

| AC | Family | Requirement (testable, observable) | Derived-from | Verification expectation | Gate / phase |
|---|---|---|---|---|---|
| AC1 | AC-T | Exactly the five §1.1 ledger IDs receive one final disposition each: four ENCODED and TB-CP-003 NO-CHANGE. Map, handoff, and final Gate Q disposition tables contain the identical ID set with reconciled approved/final dispositions. Each ENCODED ID traces through its approved touch row, changed doc Version History, commit, CHANGELOG, handoff, and spec. TB-CP-003 traces to its Gate 2 NO-CHANGE approval and the explicitly approved audit mentions; it requires no separate implementation edit or commit. | STANDING AC-T; MAP §A, §B TB-CP-003, §C, §G, §M, §N | Per-ID trace table, cited text and commit evidence; normalized disposition-set comparison. | Gate Q |
| AC2 | AC-S | The canonical/infra delta from BASE consists of SKILLS, ENGINEER, `_ARCHIVE/APP_FACTORY_SKILLS_PLAYBOOK_v1_1.md`, `_ARCHIVE/ENGINEER_PLAYBOOK_v1_2.md`, MANIFEST.md, and CHANGELOG.md. Every hunk implements the applicable §C/§G row or archive addition. Other allowed run-state paths are `_AUDIT/SYNC_2026-09-15_test-b-large/**`, RECOVERY.md, session_2026-09-15.md, and agent_docs/RESPONSES/*; cargo disposition follows the approved sweep. No extra canonical file, deletion, rename, or post-CONTENT_SHA canonical change occurs. Untouched canonical docs are byte-identical to BASE. | STANDING AC-S; MAP §C rows 1a/1b/2a/2b/2c, §D, §E, §G, §M scope assertion | Reconciled `git diff --name-status BASE..candidate`, every changed-doc hunk read against its row, and CONTENT_SHA-to-candidate path diff. | Gate Q; QA entry |
| AC3 | AC-P | Preserve “All existing governing rules.” and “Do not rewrite or weaken existing doctrine.” in both target docs. No pre-existing target line is deleted or modified except the two L3 header replacements; only the three approved lines are inserted. In particular preserve SKILLS :307, :318–327, :767–773 and §9–§10; ENGINEER's existing :90–97 table rows, :174–189 checklist, and §15 :1139–1276, including :1161 and :1241. | TB-CP-001 preserve 1/2; TB-CP-002 preserve 1/2; IN-2026-09-15-01 preserve; MAP §L rows 1/2 and §C; STANDING AC-P | Full target diffs and unchanged-passage comparisons to BASE, plus candidate path:line reads of the governing rules and inserted gate row in context. | Gate Q |
| AC4 | AC-P | Satisfy the intake constraints that Engineer-added headings, wrappers, transitions, explanations, or other wording be exposed separately before Gate 2. Every added target span matches MAP §C's INTAKE-VERBATIM, approved ENGINEER-PROPOSED, MECHANICAL, or explicitly approved OPERATOR-SPECIFIED span, including K-3 and AMENDED-v1. The “Do not guess.” constraints for TB-CP-003/004 are supported by their approved §B path:line rationale and independent candidate reads, without inventing missing brief fields. | TB-CP-001 preserve 3; TB-CP-002 preserve 3; TB-CP-003/004 intent “Do not guess.”; MAP §L rows 3–5, §C, §K-3, §O AMENDED-v1 | Added-span comparison to the approved rows and approval record; citations to §B rationale and the independently read rule locations. | Gate Q |
| AC5 | AC-C | SKILLS contains the exact sentence `TEST-B-SYNTHETIC-01 — LARGE-path synchronization validation only.` in the appended v1.2 data row of existing §17 Version History, after the BASE v1.1 row at :1148. It is historical/non-authority content at this approved location. | TB-CP-001 invariant 1; MAP §B TB-CP-001; §C 1b | Exact-string and contextual read at candidate path:line; placement comparison. | Gate Q |
| AC6 | AC-C | SKILLS contains the exact sentence `TEST-B-SYNTHETIC-03 — Content-first intake classification validation only.` in the same approved v1.2 §17 Version History row as AC5. Its ledger source remains IN-2026-09-15-01, the approved content-first DOCTRINE JOURNAL / LESSON from odd_payload.md. | IN-2026-09-15-01 approved disposition and invariant 1; MAP §A, §B, §C 1b | Exact-string/context read and ID-to-intake ledger trace. | Gate Q |
| AC7 | AC-C | ENGINEER contains the exact sentence `TEST-B-SYNTHETIC-02 — Independent Engineer-seat validation only.` in the new first Version History data row, v1.3, directly below the existing separator at BASE :1595 and above v1.2. It remains historical/non-authority content. | TB-CP-002 invariant 1; MAP §B TB-CP-002; §C 2c | Exact-string/context read and placement comparison. | Gate Q |
| AC8 | AC-C | ENGINEER §1, “What the Engineer Does NOT Do”, gains exactly the two-cell row `Self-approve a required human/Operator gate` / `Required human/Operator`, between BASE :96 “Make product decisions” and :97 “Operate production systems”. Its v1.3 history row includes exactly `Clarified that a required human/Operator gate may not be self-approved by the Engineer.` The struck “belongs to the Human” clause is not landed; the existing product-decisions owner `Human (Tony Stark)` is retained. | TB-CP-004 invariant 1; MAP §C 2b/2c, §K-3, §O AMENDED-v1 | Exact row and sentence comparison, table-context read, and diff showing the existing row unchanged. | Gate Q |
| AC9 | AC-P | TB-CP-003 remains approved NO-CHANGE: SKILLS doctrine still states both one manager CLAUDE.md at the family root and no separate CLAUDE.md in child skills. Preserve the governing statements at :307, :318–327 and :767–773, with the reinforcing examples/trees listed in MAP §B unchanged. No doctrinal edit is attributed to TB-CP-003; its approved verification mentions in Version History, CHANGELOG and the shared commit do not turn it into CHANGE. | TB-CP-003 invariants 1/2 and approved NO-CHANGE; MAP §B TB-CP-003, §C 1b, §G row 1, §N commit 1; STANDING AC-P | Independent reads with candidate path:line; BASE diff of the cited governing passages and examples; disposition evidence. | Gate Q |
| AC10 | AC-A | SKILLS L3 becomes the exact MAP §C 1a single-line header, Version 1.2, Date EXEC_DATE, Status Active; ENGINEER L3 becomes §C 2a, Version 1.3, same Date, Status Active. The entire new Version History rows equal §C 1b and amended §C 2c after date substitution, including approved bold lead-ins and IDs. Exactly one new row and one version bump per doc: newest-last for SKILLS, newest-first for ENGINEER. | MAP §C 1a/1b/2a/2c; §K-1 TEST B ruling; §O AMENDED-v1; STANDING AC-A, AC-H | Full header/row string comparison to map; row counts, ordering, and version comparison against BASE. | Gate 4 evidence / Gate Q |
| AC11 | AC-C | Re-run MAP §B/§M's synthetic-marker search across the full live scope. It returns exactly four matching lines: the SKILLS v1.2 row carrying markers 01 and 03, the ENGINEER v1.3 row carrying marker 02, and the two approved CHANGELOG rows. Re-run the recorded Version History placement searches in both targets; reconcile the TOC and fenced example as unchanged, and the actual history headings as the approved placements. | TB-CP-001/002 and IN-2026-09-15-01 invariants; MAP §B corresponding searches, §M searches 1; STANDING AC-C | Recorded searches and complete output reconciled against §B/§M; history-context reads. Include the approved awareness scope with OUT-OF-SCOPE disposition. | Gate Q |
| AC12 | AC-C | Re-run TB-CP-003 searches T3a/T3b/T3c with the terms, flags, and scopes in MAP §B. Every recorded hit retains its approved disposition; no active hit lacks a disposition or contradicts the single-manager/no-per-child rule. Read §F's FFM single-skill authoring example (:1114–1238) and the corresponding §B trees/templates to establish their continued consistency. | TB-CP-003 invariants 1/2; MAP §B TB-CP-003 hit tables/searches, §F FFM row, §M searches 2; STANDING AC-C | Verbatim approved search re-runs, hit-by-hit reconciliation, and independent path:line context reads, including distinction between single skills and skill families. | Gate Q |
| AC13 | AC-C | Re-run TB-CP-004 T4a–T4h using MAP §B's terms, flags, and scopes. The CHANGE hit is satisfied by §C 2b; all CONSISTENT hits remain present and consistent; no active hit remains undispositioned or contradicts the approved gate rule. Read every §F dependent location: FFM, APP_FACTORY_BLUEPRINT, DESIGNER, HANDOFF_PACKAGE, QA, BUG_FIX, BIM, ENGINEER checklists/§15, and both target TOCs. The existing assumption/inline-plan wording at ENGINEER BASE :1161/:1241 remains unchanged and is evaluated in its approved context. | TB-CP-004 invariant 1; MAP §B TB-CP-004 searches/hits, §C 2b, all §F rows, §M searches 3; STANDING AC-C | Verbatim search output reconciled per hit, independent dependent/context reads with candidate path:line, and BASE preservation diff. | Gate Q |
| AC14 | AC-R | References introduced by the approved edits resolve case-exactly. In particular ENGINEER's §1 “What the Engineer Does NOT Do” and SKILLS §17 Version History exist as cited by the approved CHANGELOG entries. No new filename, folder path, or image is authorized. Apply standing reference checks to added lines and the standing orphan check to any existing tier `_assets/` files; no new source/render asset pairing is required because §H lists none. Do not reinsert the removed §1 citation into the amended ENGINEER history sentence. | STANDING AC-R; MAP §H rows 1/2, §G CHANGELOG rows, §C 2c and §O AMENDED-v1 | Added-reference extraction, case-exact tracked-path checks where applicable, heading reads; asset inventory/reference check or evidence of no applicable assets. | Gate Q |
| AC15 | AC-N | The new gate row uses the approved terms `human/Operator gate` and `Required human/Operator`. The retained BASE product-decisions owner remains unchanged. The only recorded retired term, `stitch`, is absent from active live scope using the lint's history exemptions; no additional retired vocabulary is invented. | STANDING AC-N; MAP §M canonical/retired terms, §C 2b, §O | Exact-term reads; retired-term search with history-context handling matching the lint. | Gate Q |
| AC16 | AC-I | MANIFEST's ENGINEER row at BASE :31 matches Version 1.3 / EXEC_DATE / Active; its SKILLS row at :39 matches Version 1.2 / EXEC_DATE / Active. Other cells in those rows remain unchanged. MANIFEST L3 Date becomes EXEC_DATE with Version 1.0 unchanged; CHANGELOG L3 Date becomes EXEC_DATE without an infrastructure version bump. No infrastructure archive is added. | STANDING AC-I; MAP §G MANIFEST rows/header and CHANGELOG header; §C headers; §O drift rulings | Header-to-row comparisons and focused infrastructure diff; archive addition list. | Gate 4 evidence / Gate Q |
| AC17 | AC-I | Exactly two rows are appended to CHANGELOG “Ongoing entries” after BASE :34, equal to the two approved §G strings after EXEC_DATE substitution, in their approved order. Row 1 records SKILLS v1.2 and IDs TB-CP-001, TB-CP-003, IN-2026-09-15-01; row 2 records ENGINEER v1.3 and IDs TB-CP-002, TB-CP-004. All prior ledger rows remain unchanged. | STANDING AC-I, AC-T; MAP §G CHANGELOG exact rows 1/2, §N | Full-string comparisons, row count, ID-column check, and focused BASE diff. | Gate 4 evidence / Gate Q |
| AC18 | AC-I | Preserve DRIFT-2026-09-15-01 (MANIFEST :6/:12/:76 count wording), -02 (:114 appendix scope), and -03 (:83 dependency row) byte-for-byte from BASE; the entire dependency map and appendix remain unchanged as approved. No canonical doc is added/removed and no Pairs-with changes: recorded disk/row totals remain 31/31, while stated 29 remains parked. Clear -04 (MANIFEST :3) and -05 (CHANGELOG :3) only through the approved EXEC_DATE updates. Recomputed dependencies for the two changed docs agree with their unchanged approved rows. | STANDING AC-I; MAP §G derived fields and all five DRIFT rows; §M derived assertions; §O drift rulings | BASE/candidate count and dependency evidence; byte comparisons of parked fields, dependency map and appendix; date diffs tied to approved infra edits. | Gate 4 evidence / Gate Q |
| AC19 | AC-A | Exactly the two approved archives are added: `_ARCHIVE/APP_FACTORY_SKILLS_PLAYBOOK_v1_1.md` byte-equals BASE:SKILLS, and `_ARCHIVE/ENGINEER_PLAYBOOK_v1_2.md` byte-equals BASE:ENGINEER. Each suffix matches its archived header. Existing archives are unchanged; no MANIFEST/CHANGELOG or other infrastructure archive is created. | STANDING AC-A; MAP §C 1a/2a archive columns, §M archive fidelity | Binary-safe comparison or hashes of Git blob bytes versus archive bytes, plus archived header reads and archive delta inventory. | Gate 4 evidence / Gate Q |
| AC20 | AC-L | The four lints run successfully as tools at the candidate and report exactly the nine pre-existing findings in §4, with the same paths, lines, and lint IDs. There are zero findings on changed lines or new files. ENCODING and RETIRED-TERMS retain their passing baseline. No lint exemption changes, and `lints/` and `.github/` remain unchanged. A nonzero lint result due solely to the retained baseline does not fail this AC. | STANDING AC-L; MAP §0 lint baseline, §M lints | Candidate lint command/output, finding-by-finding baseline comparison, and empty BASE/candidate diff for lints and .github. | Gate 4 evidence / Gate Q |
| AC21 | AC-H | The initial implementation has the two per-doc commits in MAP §N order: SKILLS first, ENGINEER second, with the approved subjects/ID lists and associated doc/archive/infra changes. Metadata follows CONTENT_SHA in a separate sync commit. Commit messages use plain hyphens and have no Co-Authored-By trailer. Each doc is bumped once; any authorized repair cites `repair QA-F<nn>` and amends the same version-history entry. | STANDING AC-H; MAP §N commits 1–3, §C version/row choices | Commit subjects/bodies and per-commit path inventory, CONTENT_SHA identification, version/history comparison, repair history if applicable. | Gate Q |
| AC22 | AC-H | If the run reaches publication, implementation remains on the existing approved branch based at BASE_SHA; the initial implementation push follows a recorded Tony Gate 4 approval. Later implementation pushes are bounded QA repairs. Handoff identifies the prior content commit, not its own containing commit; QA records the remote tip independently. No PR or merge is created for TEST B. | STANDING AC-H, AC-S; MAP §0 branch/base/merge target, §K-2, §M publication, §N, §O | Branch/base ancestry and commit evidence; Gate 4 approval and remote-publication timing evidence; handoff/QA SHA records. Unsupported timing claims are not PASS evidence. | Gate 4 publication / Gate Q |
| AC23 | AC-H | At the applicable handoff/closeout milestone the working tree is clean, intake units have recorded dispositions, and debris is removed per the standing durable/debris definition. At Gate Q closeout the durable run folder contains the map, approved spec, handoff with any repair history, QA matrix/findings, Gate Q report, received intake snapshot with final disposition stamps (or permitted immutable-source reference), and RUN_SUMMARY. No scratch/grep dumps, duplicate debris, stray caches/backups, or abandoned branches remain. Required run artifacts are evaluated when their producing phase completes; this draft does not require future evidence at Gate 3. | STANDING AC-H; MAP §M scope/sweep and disposition assertions, §N hygiene, §K-2 no-merge ruling | Handoff/closeout status evidence, durable artifact and cargo inventory, disposition stamps, debris/branch checks; milestone-specific evidence in the matrix and closeout report. | Handoff / Gate Q closeout |

## 3. Gates and source rows mapped to ACs

| Approved source / gate | ACs |
|---|---|
| MAP §A ledger and §B per-ID invariants | AC1, AC5–AC9; propagation AC11–AC13 |
| MAP §C 1a | AC2–AC3, AC10, AC16, AC19, AC21 |
| MAP §C 1b | AC2–AC6, AC9–AC12, AC17, AC21 |
| MAP §C 2a | AC2–AC3, AC10, AC16, AC19, AC21 |
| MAP §C 2b | AC2–AC4, AC8, AC13, AC15, AC21 |
| MAP §C 2c, AMENDED-v1 | AC2–AC4, AC7–AC8, AC10–AC11, AC14, AC17, AC21 |
| MAP §D/§E no new files/deletions; §J no cross-boundary work | AC2; exclusions in §1 |
| MAP §F dependents and §I awareness | AC9, AC12–AC14; unchanged paths in AC2 |
| MAP §G infra and drift | AC16–AC19 |
| MAP §H references | AC14 |
| MAP §L preservation rows 1/2 | AC3; TB-CP-003 specifically AC9 |
| MAP §L preservation rows 3/4/5 | AC4 |
| MAP §M search/terms/lint/disposition expectations | AC1–AC2, AC11–AC20 |
| MAP §N/§O commit/publication and approvals | AC10, AC21–AC23; later QA preconditions |
| Gate 3 | Tony approves this derived contract; no candidate PASS/FAIL grading occurs here |
| Gate 4 self-checks from Engineer (claims for independent QA to verify) | AC10, AC16–AC20; publication boundary AC22 |
| Gate Q | All AC1–AC23 reconciled with independent evidence; Sol owns the verdict |
| Gate D | N/A — documentation-only disposable validation, no deployment |

Standing-family coverage: AC-T → AC1; AC-S → AC2; AC-P → AC3/AC4/AC9; AC-C → AC5–AC8/AC11–AC13; AC-R → AC14; AC-N → AC15; AC-I → AC16–AC18; AC-A → AC10/AC19; AC-L → AC20; AC-H → AC21–AC23.

## 4. Regression expectations

The approved lint baseline is **nine findings**, copied from MAP §0/§M for later independent comparison:

| Path | BASE and expected candidate line(s) | Lint ID | Count |
|---|---|---|---|
| `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md` | 258, 261, 688, 690, 692 | VERSIONED-REFS | 5 |
| `04_REFERENCE_MANUALS/DATABASE_MANUAL.md` | 8, 156 | VERSIONED-REFS | 2 |
| `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md` | 2092 | VERSIONED-REFS | 1 |
| `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md` | 1 | HEADER-PRESENCE | 1 |

ENCODING and RETIRED-TERMS pass in the recorded baseline. These files are untouched by the approved run, so their line anchors remain unchanged. Neither fixing nor suppressing these findings is authorized.

- Every canonical doc outside SKILLS and ENGINEER remains byte-identical to BASE_SHA. In both target docs, all pre-existing content except the approved headers remains unchanged.
- Parked DRIFT-01/-02/-03 stay byte-unchanged. The two authorized infrastructure header dates may change as AC16/AC18 require.
- Each repair retests the failed ACs plus mandatory **AC-S (AC2), AC-L (AC20), and AC-H (AC21–AC23)**. Add **AC-A (AC10/AC19)** if an archive is touched by the repair.
- Evidence must use the applicable retest SHA. In-scope acceptance failures and regressions route through Sol to the Engineer; scope/wording/doctrine ambiguity routes to Tony. Outside-scope observations remain follow-up findings, not newly invented ACs.

## 5. Manual-only points

Exact strings and searches are necessary but do not replace these contextual reads:

- **AC3/AC4/AC9:** read the preserved single-manager rule, Anti-Pattern 4, SKILLS §9–§10, ENGINEER role-limits table and §15. Cite candidate path:line and compare to BASE. Verify the approved additions do not weaken existing rules and every added span has approval provenance.
- **AC5–AC8/AC10/AC11:** read the actual history tables and new gate row. SKILLS' fenced “Version History” example at BASE :687 is not the placement. Verify marker content remains non-authority history and that amended wording is used.
- **AC12/AC13:** distinguish skill families, single skills, project managers, and module managers at the exact §B/§F locations. Read the assumption/inline-plan examples at ENGINEER BASE :1161/:1241 in context; preserve the map's scope and escalate an actual unresolved contradiction without rewriting doctrine.
- **AC14/AC18:** read referenced headings and the parked derived fields in context. Do not turn a deliberately retained baseline mismatch into a repair requirement.
- **AC22/AC23:** assess publication and lifecycle evidence at its proper milestone. Handoff statements alone are claims; commands, records, and observed state supply evidence.

## 6. Known limitations, mechanical notes, and approval readiness

**Derivation conclusion:** all 23 ACs have lawful sources; all five approved intake IDs and all ten standing families are covered. No unresolved doctrine ambiguity or BLOCKED issue prevents Gate 3 approval. No candidate verification result is asserted.

The following mechanical notes are settled by the explicit approved rows and amendment; they do not authorize edits to the map or add requirements:

1. **MAP §C total:** its summary says “6 edit rows”, but the enumerated set is 1a, 1b, 2a, 2b, 2c: five rows, comprising two header replacements and three inserted lines. This contract follows that explicit set and demands no sixth edit.
2. **MAP §H citation description:** §H row 1 still describes the ENGINEER §1 citation as inside history row 2c. AMENDED-v1 expressly replaced that history clause. The heading remains the row-2b target and is still cited in approved CHANGELOG row 2; AC14 checks the heading and actual approved references without restoring superseded wording.
3. **MAP §L span labels:** its checking shorthand lists INTAKE-VERBATIM, ENGINEER-PROPOSED, and MECHANICAL, while approved §C/§K/§O explicitly add OPERATOR-SPECIFIED owner/amendment spans. AC4 includes those expressly approved spans; it does not relabel them as Engineer-authored or reject them for the shorthand omission.

Remaining bounded limitations:

- MAP §B/§F's ENGINEER proceed-by-default concern is dispositioned CONSISTENT in assumption/inline-plan context and preserved. This spec does not extend the correction to §15 or adjudicate broader approval doctrine. Cody must still verify consistency within the approved scope.
- The BASE lint and corpus findings are approved-map inputs here, not independently rerun findings. Search patterns/scopes remain those in MAP §B/§M; Cody must execute and reconcile them at the candidate, including line shifts and the approved new hits.
- The synthetic waiver creates no production brief exception. The TEST B 1.2/1.3 version choices create no general version-bump rule; the map's deferred TESTA-F03 remains outside this contract.
- Gate 4, publication, candidate SHAs, QA evidence, and closeout are future phases. Their absence at this Phase 3 stop is expected. Any future inability to satisfy a precondition or test an AC routes BLOCKED to Tony rather than being silently waived.
- There is no PR/merge for this disposable run. Intake disposition and durable evidence remain required at their approved lifecycle milestones, without inventing a PR number.

## 7. Approvals and Gate 3 stop

- **Sol (QA Lead):** derivation complete, 2026-09-15. All **23/23 ACs traceable** to approved IDs/map rows or standing invariants. Ready for Tony's approval with the nonblocking mechanical notes in §6.
- **Tony (Operator), Gate 3 APPROVED:** **2026-09-15 20:22:59 Asia/Dhaka (UTC+06:00; 14:22:59 UTC)**. Operator instruction: “APPROVED — GATE 3.” Approved exactly as currently derived; this spec is **FROZEN**. All 23 ACs are unchanged. The three mechanical notes in §6 remain nonblocking observations.
- A later material change requires Gate 3 re-approval; an implementation scope change also requires the applicable Gate 2 amendment.
- **Current action: STOP. Gate 3 APPROVED / SPEC FROZEN.** Approval recording only; no Engineer execution, commit, or push.

TEST B — LARGE VALIDATION  
QA LEAD SEAT  
CURRENT GATE: GATE 3 — APPROVED / SPEC FROZEN
