# SYNC_HANDOFF — test-b-large — 2026-09-15

> **Engineering → QA claim package** (`QA_PLAYBOOK` §6: a handoff is claims to verify, never proof). Authored by Claudy (Engineer seat) AFTER the last approved content commit exists and BEFORE Gate 4. It references **CONTENT_SHA** and does not claim the SHA of the commit that contains this file. Cody records **QA_START_SHA** independently from the remote after the Gate 4 push.
>
> **TEST B — disposable LARGE-path validation.** Merge target NONE: no PR, no merge (map §0 / §K-2).

## 0. Identity

| Field | Value |
|---|---|
| Run ID | `SYNC_2026-09-15_test-b-large` |
| Branch | `test/docset-sync-v07-large-001` (local only; **not pushed** at time of writing; `git ls-remote --heads origin test/docset-sync-v07-large-001` empty) |
| BASE_SHA | `dd6d496a3b269a6bf83ce4e85101d8e0e6e785b9` (approved in UPDATE_MAP §0). The branch was reused, not created: HEAD was at BASE_SHA with 0 commits after it (`git log dd6d496..HEAD` empty) |
| **CONTENT_SHA** | **`4971a6133a9b93a456726de0940add5ed7908b8d`**: the last commit containing approved canonical content (`git rev-parse HEAD` immediately after the ENGINEER_PLAYBOOK commit, before any metadata commit) |
| Approved artifacts | UPDATE_MAP `APPROVED (Gate 2, 2026-09-15)` + `AMENDED-v1 (Gate 2, 2026-09-15)`; SHA-256 `98a033eeddd7a00cf21e34dc986645c335b3234698079d35a7506724eced6cba`, equal to the hash recorded in spec §0 before Phase 4 (map unaltered). DOCSET_SYNC_ACCEPTANCE_SPEC `APPROVED (Gate 3, 2026-09-15 20:22:59 Asia/Dhaka)`, FROZEN, 23 ACs; SHA-256 at Phase 4 start `8468df2011b2557e2e690fd7f47720c1919ff21a9862d36acca77baccc95f221` |
| Path | LARGE |
| Phase 4 execution date (`<EXEC_DATE>`) | `2026-09-15` |

## 1. Candidate files

| Path | Kind | Version live → new | Contributing IDs | Commit |
|---|---|---|---|---|
| `03_BUILD_METHODOLOGY/APP_FACTORY_SKILLS_PLAYBOOK.md` | canonical edit (§C 1a, 1b) | 1.1 → 1.2 | TB-CP-001, IN-2026-09-15-01 (TB-CP-003 cited, NO-CHANGE) | `0e88561` docs(APP_FACTORY_SKILLS_PLAYBOOK): v1.2 - TEST B synthetic validation sentences [TB-CP-001, TB-CP-003, IN-2026-09-15-01] |
| `_ARCHIVE/APP_FACTORY_SKILLS_PLAYBOOK_v1_1.md` | archive | (snapshot of 1.1) | same | `0e88561` |
| `MANIFEST.md` row :39 | infra | row 1.1/2026-07-08 → 1.2/2026-09-15 | same | `0e88561` |
| `CHANGELOG.md` row :35 | infra | +1 row | TB-CP-001, TB-CP-003, IN-2026-09-15-01 | `0e88561` |
| `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md` | canonical edit (§C 2a, 2b, 2c) | 1.2 → 1.3 | TB-CP-002, TB-CP-004 | `4971a61` docs(ENGINEER_PLAYBOOK): v1.3 - TEST B synthetic sentence and no self-approval of required gates [TB-CP-002, TB-CP-004] |
| `_ARCHIVE/ENGINEER_PLAYBOOK_v1_2.md` | archive | (snapshot of 1.2) | same | `4971a61` |
| `MANIFEST.md` row :31 + header :3 Date | infra | row 1.2/2026-07-07 → 1.3/2026-09-15; header Date 2026-07-12 → 2026-09-15 (Version 1.0 unchanged) | TB-CP-002, TB-CP-004 (header date clears DRIFT-04) | `4971a61` |
| `CHANGELOG.md` row :36 + header :3 Date | infra | +1 row; header Date 2026-07-12 → 2026-09-15 | TB-CP-002, TB-CP-004 (header date clears DRIFT-05) | `4971a61` |

## 2. Intake / correction disposition table (equals UPDATE_MAP §A)

| ID | Class | Disposition | Where it landed (paths) or ruling reference |
|---|---|---|---|
| TB-CP-001 | 1 APPROVED CORRECTION PACKAGE | CHANGE | `APP_FACTORY_SKILLS_PLAYBOOK.md:1149` (§17 v1.2 row); CHANGELOG :35 |
| TB-CP-002 | 1 | CHANGE | `ENGINEER_PLAYBOOK.md:1597` (Version History v1.3 row); CHANGELOG :36 |
| TB-CP-003 | 1 | NO-CHANGE (approved Gate 2, 2026-09-15) | Map §B TB-CP-003 evidence; cited in `APP_FACTORY_SKILLS_PLAYBOOK.md:1149` and CHANGELOG :35 only |
| TB-CP-004 | 1 | CHANGE (K-3; AMENDED-v1 wording) | `ENGINEER_PLAYBOOK.md:97` (§1 table row), `:1597` (v1.3 row sentence); CHANGELOG :36 |
| IN-2026-09-15-01 | 2 DOCTRINE JOURNAL / LESSON | CHANGE | `APP_FACTORY_SKILLS_PLAYBOOK.md:1149` (§17 v1.2 row); CHANGELOG :35 |

Candidate line numbers are shown; BASE anchors are in the map. Final stamps (ENCODED / NO-CHANGE) are applied at close-out, not here.

## 3. Claims (each labeled; QA verifies every one)

**Lints at CONTENT_SHA.** EVIDENCE: working tree canonical content = CONTENT_SHA.
- Command: `py lints/run_all.py` → exit 1, `=== RESULT: FAIL ===` from baseline only.
- `[ENCODING] PASS — 0 hits across 33 live docs` · `[RETIRED-TERMS] PASS — 0 hits across 33 live docs` · `[VERSIONED-REFS] FAIL — 8 hit(s)` · `[HEADER-PRESENCE] FAIL — 1 miss(es)`.
- Findings: STARTER_KIT_HANDBOOK :258 :261 :688 :690 :692 [VERSIONED-REFS]; DATABASE_MANUAL :8 :156 [VERSIONED-REFS]; UI_UX_BUILDING_MANUAL :2092 [VERSIONED-REFS]; STARTER_KIT_HANDBOOK :1 [HEADER-PRESENCE].
- New findings: **0**. Baseline **9, unchanged** (same paths, lines, IDs). Lints were also run before each doc commit, with the same result.
- `git diff --name-only dd6d496..4971a61 -- lints .github` → empty.

**Archive fidelity.** EVIDENCE, run on committed blobs because `core.autocrlf=true` makes working-tree bytes CRLF.
- `git rev-parse dd6d496:03_BUILD_METHODOLOGY/APP_FACTORY_SKILLS_PLAYBOOK.md` = `ba8d795b651eb61b650af580cef24c94048b9d1a` = `git rev-parse 4971a61:_ARCHIVE/APP_FACTORY_SKILLS_PLAYBOOK_v1_1.md`; `git show BASE:… | cmp - <(git show CONTENT:_ARCHIVE/…)` → byte-equal. Archive header L3: `> **Version:** 1.1 ·`.
- `git rev-parse dd6d496:02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md` = `2be9f7787481018b5ddafa721eea1220e88aff7e` = `git rev-parse 4971a61:_ARCHIVE/ENGINEER_PLAYBOOK_v1_2.md`; cmp → byte-equal. Archive header L3: `> **Version:** 1.2 ·`.
- Pre-commit, the working-tree `git hash-object` of each archive also equalled the BASE blob.
- No MANIFEST/CHANGELOG archive was created.

**MANIFEST derived fields.** EVIDENCE.
- Live docs at CONTENT_SHA (`git ls-tree` `0[1-5]_*/*.md`) = 31; MANIFEST table rows = 31; stated "29" **unchanged** (no doc added or removed; DRIFT-01 parked).
- Rows vs headers (recomputed from disk): APP_FACTORY_SKILLS_PLAYBOOK header `1.2 / 2026-09-15 / Active` = row :39; ENGINEER_PLAYBOOK header `1.3 / 2026-09-15 / Active` = row :31. The other row-vs-header differences reported by the recompute are the pre-existing observations recorded in map §G (STARTER_KIT footnote; abbreviated long statuses), unchanged.
- `git diff -U0 dd6d496..4971a61 -- MANIFEST.md` hunks: `@@ -3 +3 @@`, `@@ -31 +31 @@`, `@@ -39 +39 @@` only.
- DRIFT lines L6, L12, L76, L83, L114: line-hash comparison BASE vs CONTENT → all **unchanged**. `diff` of the whole `## Dependency Map` section through end-of-file, BASE vs CONTENT → identical (← map incl. DRIFT-03 and appendix incl. DRIFT-02 untouched).
- No Pairs-with changed, so no ← recompute was needed. Target rows recompute from disk as before: SKILLS ← {FFM_PLAYBOOK}; ENGINEER ← 7.
- MANIFEST/CHANGELOG header Dates bumped to 2026-09-15 (clears DRIFT-04/-05 as approved); Version 1.0 unchanged; not archived.

**CHANGELOG.** EVIDENCE.
- 2 rows added (hunk `@@ -34,0 +35,2 @@`) plus header Date (`@@ -3 +3 @@`).
- Row :35 last column `TB-CP-001, TB-CP-003, IN-2026-09-15-01`; row :36 last column `TB-CP-002, TB-CP-004`.
- The row strings equal map §G rows 1/2 with `<EXEC_DATE>` = 2026-09-15.

**Diff scope.** EVIDENCE.
- `git diff --name-status dd6d496..4971a61` = `M 02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md` · `M 03_BUILD_METHODOLOGY/APP_FACTORY_SKILLS_PLAYBOOK.md` · `M CHANGELOG.md` · `M MANIFEST.md` · `A _ARCHIVE/APP_FACTORY_SKILLS_PLAYBOOK_v1_1.md` · `A _ARCHIVE/ENGINEER_PLAYBOOK_v1_2.md`. That equals map §C ∪ §G ∪ archives; §D/§E empty.
- Tier docs changed: 2; every other canonical doc is byte-identical to BASE.
- Target-doc hunks: SKILLS `@@ -3 +3 @@` (1a), `@@ -1148,0 +1149 @@` (1b); ENGINEER `@@ -3 +3 @@` (2a), `@@ -96,0 +97 @@` (2b), `@@ -1595,0 +1597 @@` (2c). No pre-existing line deleted or modified except the two L3 headers.

**Exact wording landed.** EVIDENCE, `git diff` added lines.
- SKILLS :1149 `| 1.2 | 2026-09-15 | **TEST B synthetic validation (TB-CP-001, IN-2026-09-15-01; TB-CP-003 verified — no change).** TEST-B-SYNTHETIC-01 — LARGE-path synchronization validation only. TEST-B-SYNTHETIC-03 — Content-first intake classification validation only. |`
- ENGINEER :97 `| Self-approve a required human/Operator gate | Required human/Operator |`
- ENGINEER :1597 `| 1.3 | 2026-09-15 | **TEST B synthetic validation (TB-CP-002, TB-CP-004).** TEST-B-SYNTHETIC-02 — Independent Engineer-seat validation only. Clarified that a required human/Operator gate may not be self-approved by the Engineer. |`
- The struck "belongs to the Human" clause is not present. The existing ENGINEER :96 row `| Make product decisions | Human (Tony Stark) |` is unchanged.

**Propagation.** CLAIM, Claudy re-ran at CONTENT_SHA; Cody re-runs independently.
- `grep -rn "TEST-B-SYNTHETIC" <live scope>` → **4 lines**: ENGINEER :1597, SKILLS :1149, CHANGELOG :35, CHANGELOG :36. This equals the map §M expectation. `_SKILLS/`/`_OTHERS/` → 0.
- T3b `CLAUDE\.md` → 211 (BASE 210). The +1 is CHANGELOG :35 ("single-CLAUDE.md family rule verified", HISTORY), confirmed as the only added line containing the term.
- T4a `self[- ]?approv` → 4 (BASE 1); T4d → 25 (BASE 22). The +3 in each are the approved new lines ENGINEER :97, ENGINEER :1597, CHANGELOG :36, confirmed as the only added lines containing "operator gate".
- T4h hits are unchanged in content, shifted +1 by row 2b: ENGINEER :1162 "→ Correct me now or I'll proceed…" (BASE :1161), :1242 "→ Executing unless you redirect." (BASE :1241).
- Not re-run in full by Claudy: every individual T3a/T3c/T4b/T4c/T4e/T4f/T4g hit reconciliation (see §6).

**References / assets.** CLAIM.
- ENGINEER `### What the Engineer Does NOT Do` heading is unchanged (row 2b sits in its table; cited by CHANGELOG :36).
- SKILLS `## 17. Version History` is unchanged (cited by CHANGELOG :35).
- No filenames, paths, or images were added.

**Commit hygiene.** EVIDENCE.
- `git log --format="%h | %s | trailers:[%(trailers:only)]" dd6d496..4971a61` shows 2 doc commits in map §N order (SKILLS first, ENGINEER second), `docs(<DOC>): v<X.Y> - <summary> [<IDs>]` shape, plain hyphens, empty trailers (no Co-Authored-By).
- One version bump per doc.

**Working tree at CONTENT_SHA.** EVIDENCE, **not empty**. `git status --porcelain` right after the CONTENT_SHA commit showed only non-canonical run-state:
- `M RECOVERY.md`
- untracked `_AUDIT/SYNC_2026-09-15_test-b-large/` (map, spec)
- untracked `_INBOX/` (cargo, dispositioned at sweep)
- 4 untracked `agent_docs/RESPONSES/response_2026-09-15_*.md`
- untracked `session_2026-09-15.md`

No canonical path was dirty.

## 4. Deviations from the approved map

**NONE** in canonical content: every hunk equals an approved §C / §G row as amended by AMENDED-v1.

Process notes (not map deviations; for Tony and QA awareness):
1. **CONTENT_SHA is recorded here, not in UPDATE_MAP §O.** The skill (SKILL.md Phase 4 step 5) says to write it in map §O. The Operator's Phase 4 instruction said "Do not alter the UPDATE MAP", and the spec pins the map's SHA-256. The §O field therefore still reads `<pending Phase 4>`. The Operator's instruction takes precedence; this is flagged at Gate 4.
2. **Metadata commit contents.** The `chore(sync)` handoff commit after CONTENT_SHA carries only `_AUDIT/SYNC_2026-09-15_test-b-large/**` (map, spec, this handoff). RECOVERY.md, the session file, and RESPONSES logs are updated afterward as uncommitted run-state (SKILL.md Phase 5 step 2 order). `_INBOX/` stays untracked until the sweep.
3. The map §C summary says "6 edit rows"; the enumerated rows are five (1a, 1b, 2a, 2b, 2c). Execution followed the enumerated rows, consistent with spec §6 note 1.

## 5. Known limitations

- NO-CHANGE approved: TB-CP-003.
- Parked XB items: none. Parked drift: DRIFT-2026-09-15-01, -02, -03 (byte-unchanged). DRIFT-04/-05 cleared by the approved header-date updates.
- Operator test rulings (TEST B only; not doctrine): the Q1 brief-completeness waiver; K-1 versions 1.2 / 1.3 (TESTA-F03 remains deferred); K-2 merge target NONE.
- Engineer-noted CONCERN (map §B/§F, unchanged by design): ENGINEER §15 proceed-by-default phrasing at :1162 / :1242.
- Observation outside scope: `APP_FACTORY_BLUEPRINT.md:250` stale "pointer reserved" forward-reference (map §E).
- Environment: `core.autocrlf=true` on this rig. Working-tree files are CRLF, and byte comparisons should use git blobs (`git show` / `git rev-parse <sha>:<path>`).

## 6. Explicitly unverified claims (what Claudy did NOT check)

- Hit-by-hit reconciliation of every T3a/T3b/T3c and T4a–T4g hit at CONTENT_SHA against map §B. Claudy checked only totals and added-line deltas.
- Contextual consistency of every §F dependent at candidate line numbers.
- Case-exact reference resolution on a case-sensitive filesystem (Windows rig).
- Asset orphan checks across tier `_assets/` folders (no assets in scope).
- Any AC's verdict. Claudy issues none (D20); QA owns AC1–AC23.

## 7. Repair cycles (appended per cycle, after each repair content commit exists)

| Cycle | Findings addressed (QA-F…) | REPAIR_CONTENT_SHA | Files touched (must be ⊆ approved touch list) | Repair summary (CHANGES / DIDN'T TOUCH / CONCERNS) | Pushed at |
|---|---|---|---|---|---|
| — | none yet | — | — | — | — |

## 8. Gate 4 record (filled by Claudy at the moment of approval; the push happens only after this line exists)

- **Gate 4 APPROVED by Operator at 2026-09-15 20:52:06 Asia/Dhaka (UTC+06:00; 14:52:06 UTC)**. Operator instruction: "APPROVED — GATE 4. Authorize publication of the TEST B branch."
- Pushed `<recorded in Operator report after push — this file cannot contain the SHA or time of the commit that contains it>` · (QA_START_SHA is Cody's to record — not here)
- **Operator conditions for this publication:**
  - The commit carries only this Gate 4 handoff metadata.
  - No canonical doctrine, UPDATE_MAP.md, or DOCSET_SYNC_ACCEPTANCE_SPEC.md changes.
  - CONTENT_SHA unchanged (`4971a6133a9b93a456726de0940add5ed7908b8d`).
  - RECOVERY.md, session files, response logs, and `_INBOX/` cargo are excluded.
  - Single push of the current branch.
  - Merge target NONE: no PR, no merge.

## 9. Validation findings recorded for later review (TEST B; do not repair the skill during this run)

- **TESTB-F01** (Operator-recorded, 2026-09-15): UPDATE_MAP requires CONTENT_SHA to be recorded, but the map is frozen before CONTENT_SHA exists, and the acceptance spec relies on its fingerprint. During this run CONTENT_SHA was correctly recorded in SYNC_HANDOFF instead. Do not repair the skill during TEST B. (Cross-reference: §4 process note 1.)
