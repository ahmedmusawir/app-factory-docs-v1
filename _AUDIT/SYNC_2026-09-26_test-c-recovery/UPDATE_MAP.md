# UPDATE MAP — test-c-recovery — 2026-09-26

> **The approved execution source of truth for this synchronization run** (supersedes RIPPLE_MAP since skill v0.6). Authored by Claudy (Engineer seat). Approved by Tony at Gate 2. Consumed by Sol (spec derivation), Cody (verification), and Claudy (execution, EXACTLY as approved). This file — not memory, not the branch — is what execution follows and what QA measures against. Lives at `_AUDIT/SYNC_2026-09-26_test-c-recovery/UPDATE_MAP.md`.
>
> Evidence labels on every non-trivial cell: EVIDENCE (path:line / SHA / command output) · INFERENCE (from what) · CLAIM (package / Operator says) · GAP (looked where) · QUESTION (needs Tony).
>
> **VALIDATION CONTEXT:** TEST C — recovery / resume validation of skill v0.7-DRAFT on disposable branch `test/docset-sync-v07-recovery-001`. Cargo is synthetic. This session stops after Gate 2 approval, BEFORE Phase 4; a fresh session resumes per D15a.

## 0. Run header

| Field | Value |
|---|---|
| Run ID | `SYNC_2026-09-26_test-c-recovery` |
| Run branch | `test/docset-sync-v07-recovery-001` — existing branch, named as-is; already at BASE_SHA, so D18 reuse applies (no new branch). Lawful descendants after BASE: only this run's own run-state and approved commits [EVIDENCE: `git rev-parse --abbrev-ref HEAD`; HEAD = BASE at map authoring] |
| BASE_SHA | `dd6d496a3b269a6bf83ce4e85101d8e0e6e785b9` — evidence: named by the Operator's TEST C launch line as the required starting SHA AND equal to the clean discovered HEAD on the run branch [EVIDENCE: `git rev-parse HEAD`; `git status --porcelain` empty at 11:07 BST]. Not main (`origin/main` = `0a787cb`, 3 behind). Change after Gate 2 = AMENDED-v<n>. |
| Merge target | **NONE** — Operator ruling at Gate 1: "NONE — disposable TEST C validation branch. No PR or merge is part of this run." [CLAIM: Operator, 2026-09-26 ~11:31 BST]. Phase 8 (PR) and the Phase 9 merge verification are N/A for this run. |
| Execution route | Local git at Hub clone (standing ruling 2026-08-05) [EVIDENCE: `git remote -v` → `ahmedmusawir/app-factory-docs-v1`] |
| **Path** | **TINY** — evidence in §P |
| QA arrangement | TINY: "Docs-only QA waiver per SOFTWARE_FACTORY_PLAYBOOK §2.5 item 6 — Operator, 2026-09-26 12:13 BST." (APPROVED at Gate 2) |
| Status | **APPROVED (Gate 2, 2026-09-26 12:13 BST) — FROZEN.** Any change = AMENDED-v1 re-entering Gate 2. Next legal phase: **Phase 4** (TINY skips Phase 3). |
| Lint baseline (pre-existing) | 9 findings, exit 1: `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md:258/261/688/690/692 [VERSIONED-REFS]`, `04_REFERENCE_MANUALS/DATABASE_MANUAL.md:8/156 [VERSIONED-REFS]`, `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:2092 [VERSIONED-REFS]`, `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md:1 [HEADER-PRESENCE]`; ENCODING PASS, RETIRED-TERMS PASS over 33 live files [EVIDENCE: `py lints/run_all.py`, 2026-09-26 ~11:08 BST] |
| Live-doc count on disk / MANIFEST rows / MANIFEST stated (at BASE_SHA) | 31 / 31 / **29** [EVIDENCE: `ls 0?_*/*.md \| wc -l` = 31; MANIFEST tables 3+6+9+7+6 = 31 rows; MANIFEST.md:6, :12, :76 say 29; MANIFEST.md:114 says "27 bodies"] → §G `DRIFT-2026-09-26-01` (pre-existing, parked) |

## A. Intake ledger

| ID | Class (INTAKE_TAXONOMY #) | Source (file / package path) | Gist (one line) | Disposition | Gate state |
|---|---|---|---|---|---|
| IN-2026-09-26-01 | 2 — DOCTRINE JOURNAL / LESSON | `_INBOX/TEST_C_RECOVERY_CARGO.md` Entry 1 | Add the exact line "TEST-C-SYNTHETIC-01 — Recovery/resume validation only." to ARCHITECT_QUESTIONNAIRE `## Version History`, directly below the table | CHANGE | Gate 1 APPROVED 2026-09-26 ~11:31 BST |

Class evidence (content-first, D16): status FLAGGED; one entry with named target, stated placement, exact required wording, preservation lines → class 2 recognition. Filename carries no LESSONS/PATCH marker; classification rests on contents. Provenance: synthetic, authored by Claudy at the Operator's TEST C instruction (stated in the cargo). Hub counterpart by canonical name: `02_PIPELINE_AGENTS/ARCHITECT_QUESTIONNAIRE.md` (header v2.2, 2026-07-07). Entry is edit-level: wording and placement both supplied by the intake.

## B. Per-ID sections

### IN-2026-09-26-01 — TEST-C-SYNTHETIC-01 note

- **Approved intent** (verbatim): "Add one harmless synthetic validation note to the target document's existing `## Version History` section, directly below the version table. Non-authority placement only." [CLAIM: `_INBOX/TEST_C_RECOVERY_CARGO.md` Entry 1]
- **Required wording** (verbatim): "TEST-C-SYNTHETIC-01 — Recovery/resume validation only."
- **Must-become-true invariants:** none stated beyond the intent. Derived: the exact wording appears exactly once in the target doc, inside `## Version History`, below the version table [INFERENCE from intent text].
- **Preservation constraints** (verbatim; mirrored in §L): 1. "All existing doctrine behavior and wording." 2. "Do not delete or rewrite existing rules."
- **Likely affected files:** `02_PIPELINE_AGENTS/ARCHITECT_QUESTIONNAIRE.md` (named TARGET). MANIFEST ← row: ARCHITECT_QUESTIONNAIRE ← ARCHITECT_PLAYBOOK = **1** [EVIDENCE: MANIFEST.md:106].
- **Propagation search** (D19). The entry changes no governing rule; the search is still mandatory for class 2. It proves (a) the new wording does not already exist or collide, (b) nothing cites the placement section in a way the insertion breaks, (c) every live reference to the target doc and its version stays true or is on the touch list.
  - Terms:
    - T1 `TEST-C-SYNTHETIC` (new wording ID prefix)
    - T2 `Recovery/resume validation` (new wording)
    - T3 `synthetic validation` (intent phrase)
    - T4 `ARCHITECT_QUESTIONNAIRE.{0,40}Version History` (cross-references to the cited placement section)
    - T5 `ARCHITECT[_ -]QUESTIONNAIRE.{0,12}v?2\.2` (references to the live version that the bump would stale)
    - T6 `ARCHITECT[_ -]QUESTIONNAIRE` (target canonical name, hyphen/space variants)
  - Scope: `01_CONSTITUTION 02_PIPELINE_AGENTS 03_BUILD_METHODOLOGY 04_REFERENCE_MANUALS 05_DESIGN_SYSTEM MANIFEST.md CHANGELOG.md` (+ `_SKILLS/`, `_OTHERS/` read-only for awareness → §I)
  - Command shape: `grep -rn -i -E "<term>" 01_CONSTITUTION 02_PIPELINE_AGENTS 03_BUILD_METHODOLOGY 04_REFERENCE_MANUALS 05_DESIGN_SYSTEM MANIFEST.md CHANGELOG.md`
  - Hit count per term [EVIDENCE: run 2026-09-26 11:32 BST]: T1 0 · T2 0 · T3 0 · T4 0 · T5 2 · T6 12 → **12 distinct hit lines** (T5's two lines are also T6 lines): 10 active / 2 history.

  | # | Path:line | Hit (quoted, abridged) | Disposition | Drives | Label |
  |---|---|---|---|---|---|
  | 1 | 02_PIPELINE_AGENTS/ARCHITECT_PLAYBOOK.md:4 | `**Pairs with:** ARCHITECT_QUESTIONNAIRE, RECON_QUESTIONNAIRE, …` | CONSISTENT — header declaration; target's name, path, and Pairs-with unchanged | §F #1 | EVIDENCE |
  | 2 | 02_PIPELINE_AGENTS/ARCHITECT_PLAYBOOK.md:136 | `The Ignition Questionnaire lives in its single source: `ARCHITECT_QUESTIONNAIRE.md`.` | CONSISTENT — questionnaire untouched; still true | §F #1 | EVIDENCE |
  | 3 | 02_PIPELINE_AGENTS/ARCHITECT_PLAYBOOK.md:214 | `The canonical APP_BRIEF template lives in `ARCHITECT_QUESTIONNAIRE.md`` | CONSISTENT — template untouched; still true | §F #1 | EVIDENCE |
  | 4 | 02_PIPELINE_AGENTS/ARCHITECT_PLAYBOOK.md:613 | `\| 2.2 \| 2026-07-07 \| **Wave 2A (audit sync).** … relocated to ARCHITECT_QUESTIONNAIRE …` | HISTORY — under `## Version History` (ARCHITECT_PLAYBOOK.md:609) | — | EVIDENCE |
  | 5 | 02_PIPELINE_AGENTS/ARCHITECT_QUESTIONNAIRE.md:1 | `# 🏗️ ARCHITECT QUESTIONNAIRE` | CONSISTENT — title unchanged | — | EVIDENCE |
  | 6 | MANIFEST.md:28 | ARCHITECT_PLAYBOOK row (Pairs-with lists target) | CONSISTENT — not this doc's row | — | EVIDENCE |
  | 7 | MANIFEST.md:29 | `\| ARCHITECT_QUESTIONNAIRE \| 2.2 \| 2026-07-07 \| Active \| …` (T5 + T6) | **CHANGE** — Version/Date updated FROM the bumped header (D7 step 3) | §G row 1 | EVIDENCE |
  | 8 | MANIFEST.md:82 | ← row RECON_QUESTIONNAIRE (lists target) | CONSISTENT — target's Pairs-with unchanged → no ← recompute | §G ← map | EVIDENCE |
  | 9 | MANIFEST.md:83 | ← row APP_FACTORY_BLUEPRINT (lists target) | CONSISTENT (same reason) | §G ← map | EVIDENCE |
  | 10 | MANIFEST.md:88 | ← row ARCHITECT_PLAYBOOK (lists target) | CONSISTENT (same reason) | §G ← map | EVIDENCE |
  | 11 | MANIFEST.md:106 | `\| ARCHITECT_QUESTIONNAIRE \| ARCHITECT_PLAYBOOK \| 1 \|` | CONSISTENT — recomputed from headers: only ARCHITECT_PLAYBOOK.md:4 declares the target = 1 | §G ← map | EVIDENCE |
  | 12 | CHANGELOG.md:13 | `\| 2026-07-07 \| W2A — Agent Tier Sync \| ARCHITECT_QUESTIONNAIRE v2.2 (F-017 single-source merge) …` (T5 + T6) | HISTORY — CHANGELOG is an honest-history ledger (lints/lint_common.py:19 HISTORY_FILES); past row stays true | — | EVIDENCE |

  Zero undispositioned hits.

- **Touch-list rows implementing this ID:** §C #1 (rows 1a–1c).
- **NO-CHANGE proposal:** none — wording absent from live scope (T1–T3 = 0).
- **CONFLICT / open questions:** none.

## C. Touch list (execute lightest ← first, heaviest last)

One canonical doc. All placements verified against the live structure at BASE_SHA [EVIDENCE: `grep -n '^#'` and `awk NR 166–180` on the target, 2026-09-26 11:1x BST]. Line numbers are BASE_SHA line numbers.

| # | Canonical doc (path) | ← count (MANIFEST) | Placement — VERIFIED (anchor at BASE_SHA) | Proposed wording / exact edit (INTAKE-VERBATIM / ENGINEER-PROPOSED) | Contributing IDs | Version: live → new | Archive expected | Structural? | Minimal-form note (D14) |
|---|---|---|---|---|---|---|---|---|---|
| 1a | `02_PIPELINE_AGENTS/ARCHITECT_QUESTIONNAIRE.md` | 1 | Header line L3: `> **Version:** 2.2 · **Date:** 2026-07-07 · **Status:** Active` | Replace L3 with: `> **Version:** 2.3 · **Date:** 2026-09-26 · **Status:** Active` — **ENGINEER-PROPOSED** (version number and date). Date = the Phase 4 execution date; if Phase 4 runs on a later day, that day's date and nothing else changes (mechanics, D7). Version 2.2 → 2.3 follows Hub precedent for additive changes (QA_PLAYBOOK 1.0 → 1.1, SOFTWARE_FACTORY_PLAYBOOK 1.2 → 1.3); bump magnitude is not defined by any governing rule (TESTA-F03 deferred) — Tony approves or names another number. | IN-2026-09-26-01 | 2.2 → 2.3 | YES — `_ARCHIVE/ARCHITECT_QUESTIONNAIRE_v2_2.md` (suffix from live header L3; path absent at BASE) | NO | Single-line header format preserved (HEADER-PRESENCE lint) |
| 1b | same | 1 | `## Version History` L170; table header L172–173; newest-first order (2.2 at L174 above 2.1 at L175 above ≤2.0 at L176) → new row inserted as a new line immediately BEFORE L174 | Insert row: `\| 2.3 \| 2026-09-26 \| **TEST C synthetic validation (IN-2026-09-26-01).** Added the synthetic note "TEST-C-SYNTHETIC-01 — Recovery/resume validation only." below this table. No doctrine changed; questionnaire, APP_BRIEF template, ⛔ Hard Gate, 📌 Reality Rule, and Planning State untouched. \|` — **ENGINEER-PROPOSED** in full except the quoted note, which is INTAKE-VERBATIM. Date cell follows 1a's date. | IN-2026-09-26-01 | (same bump) | (same) | NO | One row, doc's own newest-first order (D7) |
| 1c | same | 1 | Below the version table: after L176 (`\| ≤2.0 \| — \| …`) and its following blank L177, before the `---` at L178 | Insert, as its own paragraph line with one blank line after it (so it stays outside the table and before `---`): `TEST-C-SYNTHETIC-01 — Recovery/resume validation only.` — text **INTAKE-VERBATIM**. Formatting **ENGINEER-PROPOSED**: rendered as a plain paragraph, not a `>` blockquote; the cargo's `>` is read as its quotation marker for the required wording, not as part of the wording [INFERENCE]. Strike this to land it as a blockquote instead. | IN-2026-09-26-01 | (same bump) | (same) | NO | Two added lines (note + blank); nothing else in the section moves |

Resulting tail of the target after execution (for Gate 2 listening; `…` = unchanged row text):

```
## Version History

| Version | Date | Change |
|---|---|---|
| 2.3 | 2026-09-26 | **TEST C synthetic validation (IN-2026-09-26-01).** Added the synthetic note "TEST-C-SYNTHETIC-01 — Recovery/resume validation only." below this table. No doctrine changed; questionnaire, APP_BRIEF template, ⛔ Hard Gate, 📌 Reality Rule, and Planning State untouched. |
| 2.2 | 2026-07-07 | … |
| 2.1 | 2026 (pre-audit, undated) | … |
| ≤2.0 | — | … |

TEST-C-SYNTHETIC-01 — Recovery/resume validation only.

---

🥄 *Part of Stark Industries — App Factory doctrine.*
```

## D. New canonical files

None.

## E. Stale / superseded material

| Path | Action | Evidence it is stale | IDs |
|---|---|---|---|
| `02_PIPELINE_AGENTS/ARCHITECT_QUESTIONNAIRE.md` v2.2 (outgoing) | Archive-and-bump: copy to `_ARCHIVE/ARCHITECT_QUESTIONNAIRE_v2_2.md` before editing (D7 step 1) | Superseded by v2.3 at execution | IN-2026-09-26-01 |

## F. Dependents checked, unchanged

| Doc / location (path:line) | Kind | Why checked | Verdict |
|---|---|---|---|
| 1. `02_PIPELINE_AGENTS/ARCHITECT_PLAYBOOK.md:4, :136, :214` | header declaration + pointer paragraphs (role instruction) | only ← dependent (MANIFEST.md:106); T6 hits | CONSISTENT — ":136 The Ignition Questionnaire lives in its single source: `ARCHITECT_QUESTIONNAIRE.md`" and ":214 The canonical APP_BRIEF template lives in `ARCHITECT_QUESTIONNAIRE.md`" stay true; no version, section, or placement of the target is cited |

## G. Infra and index effects

| Item | Expected change | Check at Gate 4 (AC-I) |
|---|---|---|
| MANIFEST rows | MANIFEST.md:29 ARCHITECT_QUESTIONNAIRE row: Version `2.2` → `2.3`, Date `2026-07-07` → execution date, FROM the bumped header; all other cells unchanged. MANIFEST header L3 Date `2026-07-12` → execution date (Version 1.0 and Status unchanged); NOT archived (Ruling 7) | row == header; only L3 and L29 differ from BASE |
| MANIFEST live-doc count | unchanged — no canonical doc added/removed. MANIFEST.md:6, :12, :76 ("29") and :114 ("27 bodies") left byte-identical to BASE (DRIFT-2026-09-26-01) | byte-equal to BASE on those lines |
| MANIFEST ← dependency map | unchanged — target's Pairs-with (L4) unchanged; no doc's Pairs-with changes; appendix scope unchanged | MANIFEST.md:74–133 byte-equal to BASE |
| CHANGELOG | Append ONE row at the end of the `## Ongoing entries` table, immediately after CHANGELOG.md:34 (last row at BASE), in the ledger format `\| date \| doc vX.Y \| one-line change \| finding/lesson IDs \|` (CHANGELOG.md:22): `\| 2026-09-26 \| ARCHITECT_QUESTIONNAIRE v2.3 \| TEST C synthetic validation note added below the Version History table; no doctrine change (v2.2 archived) \| IN-2026-09-26-01 \|` — **ENGINEER-PROPOSED** wording (date cell = execution date). CHANGELOG header L3 Date `2026-07-12` → execution date; NOT archived | +1 row; row count = 1 bumped doc |
| README / index files | none (`_ARCHIVE/README.md` unchanged — it states the rule, lists no files) | — |

**Pre-existing / baseline drift (D7)**

| ID | Location (path:line at BASE_SHA) | Stale value vs disk truth (EVIDENCE) | Caused by this run? | Disposition |
|---|---|---|---|---|
| DRIFT-2026-09-26-01 | MANIFEST.md:6 ("all 29 live doctrine docs"), :12 ("## The 29 Live Docs"), :76 ("inverting the 29 Pairs-With → lists"), :114 ("scanning all 27 bodies") | Disk: 31 live docs (`ls 0?_*/*.md \| wc -l`); MANIFEST tables: 31 rows | NO | PARKED → follow-up job; not on the touch list; left byte-unchanged |

## H. Paths, links, assets

| Reference (as written) | In doc | Resolves at BASE_SHA? | Resolves after? | Asset | IDs |
|---|---|---|---|---|---|
| none added | — | — | — | none | IN-2026-09-26-01 |

The change adds no link, path, or asset. The new archive file `_ARCHIVE/ARCHITECT_QUESTIONNAIRE_v2_2.md` is referenced by nothing (archive convention, `_ARCHIVE/README.md`).

## I. Skill references (read-only awareness)

| Skill / other file (path) | What it cites that this run changes | Disposition |
|---|---|---|
| `_OTHERS/MASTER_DOC_LIST_v1_0_FINAL.md:38` | `2_AGENTS-ARCHITECT_QUESTIONNAIRE_v2_1.md` (legacy pre-Hub filename) | OUT-OF-SCOPE — non-canonical historical list; already stale at BASE; not affected by this run; not edited (D10, D21) |
| `_SKILLS/**` | no hits for T1–T6 [EVIDENCE: `grep -rn -i -E "ARCHITECT[_ -]QUESTIONNAIRE\|TEST-C-SYNTHETIC" _SKILLS _OTHERS` = 1 hit, above] | CONSISTENT — nothing cites the target |

## J. Parked cross-boundary / cross-repo items

None.

## K. Unresolved Operator decisions

| ID | Type | Question | Evidence | What it affects | Ruling |
|---|---|---|---|---|---|
| K-1 | CLARIFICATION | Merge target? | Branch carries 3 skill commits ahead of `origin/main` not in this run | Phase 8 only | **RULED Gate 1:** "NONE — disposable TEST C validation branch. No PR or merge is part of this run." |

No CONFLICT rows. Mechanical items resolved from evidence (no question needed; approval of this map approves the method):

- **M-1 — Archive fidelity check on a CRLF checkout.** EVIDENCE: `core.autocrlf=true` (system, `C:\ProgramData/Git/config`), no `.gitattributes`; `git ls-files --eol` → `i/lf w/crlf` for the target, MANIFEST, CHANGELOG, and existing archives; the working-tree target has 180 CR bytes, the BASE blob has 0. The skill's literal command `git show <BASE_SHA>:<path> | diff - _ARCHIVE/<NAME>_v<X_Y>.md` therefore reports a false DIFF on this clone even for a perfect copy (trial: raw `diff` DIFFERS; `git diff --quiet dd6d496 -- <path>` identical). **Method used instead (same guarantee: byte-equal as committed):** `git hash-object _ARCHIVE/ARCHITECT_QUESTIONNAIRE_v2_2.md` (filtered, i.e. with the clone's EOL normalization) MUST equal `git rev-parse dd6d496:02_PIPELINE_AGENTS/ARCHITECT_QUESTIONNAIRE.md` = `15780306c6ad4dc2b5b3ab8d393d7d86a0643852`; after staging, `git rev-parse :_ARCHIVE/ARCHITECT_QUESTIONNAIRE_v2_2.md` MUST equal the same SHA. Proven at BASE: working-tree target filtered hash = `15780306…` = BASE blob. Recorded as a skill refinement (§O).
- **M-2 — Uncommitted run-state at Phase 4 start.** EVIDENCE: this stage is under an Operator no-commit instruction, so at resume the tree will contain the run-state files listed in §N step 0, all untracked or modified by this run. SKILL P4.1 says "confirm the tree is clean". Resolution: the resumed session verifies that the dirty set equals EXACTLY the §N step 0 list (any other change = D22 STOP), then commits them as the run-state commit in §N step 0 (a lawful descendant under D18), which makes the tree clean before the per-doc dance.

## L. Preservation constraints (all IDs, consolidated)

| Constraint (verbatim) | Source ID | Where it lives (path:line at BASE_SHA) | How checked (Gate 4 self-check, TINY) |
|---|---|---|---|
| "All existing doctrine behavior and wording." | IN-2026-09-26-01 | `02_PIPELINE_AGENTS/ARCHITECT_QUESTIONNAIRE.md` L1–L180 | `git diff dd6d496 -- <target>` shows only: L3 replaced; one row inserted before old L174; note + blank inserted after old L177. No `-` lines except old L3 |
| "Do not delete or rewrite existing rules." | IN-2026-09-26-01 | same | same diff: zero deleted lines other than the header line; Version History rows 2.2 / 2.1 / ≤2.0 byte-identical |

## M. Expected validation

- **Lints:** 4 lints; expected on the candidate: zero new findings; baseline unchanged at 9 — `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md:258/261/688/690/692 [VERSIONED-REFS]`, `04_REFERENCE_MANUALS/DATABASE_MANUAL.md:8/156 [VERSIONED-REFS]`, `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:2092 [VERSIONED-REFS]`, `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md:1 [HEADER-PRESENCE]`; ENCODING / RETIRED-TERMS PASS. (New wording is lint-safe: Version History sections and CHANGELOG are exempt from VERSIONED-REFS per `lints/lint_common.py:19, :33`; the only retired term is `stitch`, `lints/retired_terms_lint.py:11`.)
- **Propagation searches to re-run at the candidate** (verbatim from §B, same scope and command shape): T1 `TEST-C-SYNTHETIC` → **2 hits, both in the target under `## Version History`** (the §C 1b row, the §C 1c note line); the CHANGELOG row does not contain the prefix. T2 `Recovery/resume validation` → 2 (same two lines). T3 `synthetic validation` → target row 1b ("TEST C synthetic validation") + CHANGELOG new row → 2. T4 → 0. T5 `ARCHITECT[_ -]QUESTIONNAIRE.{0,12}v?2\.2` → 1 (CHANGELOG.md:13, HISTORY; MANIFEST.md:29 now reads 2.3). T6 → 13 (the 12 BASE lines, with MANIFEST.md:29 changed in place, + the new CHANGELOG row).
- **Canonical / retired term list (AC-N):** none supplied by the intake; the lint RETIRED-TERMS list applies.
- **Derived-field assertions:** MANIFEST count unchanged (29 stated; DRIFT-2026-09-26-01 lines byte-equal to BASE); rows 31; ← map unchanged (MANIFEST.md:74–133 byte-equal); MANIFEST.md:29 == target header; CHANGELOG +1 row.
- **Archive fidelity:** 1 archive expected, `_ARCHIVE/ARCHITECT_QUESTIONNAIRE_v2_2.md`; blob-equal to `git rev-parse dd6d496:02_PIPELINE_AGENTS/ARCHITECT_QUESTIONNAIRE.md` = `15780306c6ad4dc2b5b3ab8d393d7d86a0643852` by the §K M-1 method.
- **Diff scope (AC-S):** `git diff --stat dd6d496..CONTENT_SHA` limited to: the target, `_ARCHIVE/ARCHITECT_QUESTIONNAIRE_v2_2.md` (new), `MANIFEST.md` (L3, L29), `CHANGELOG.md` (L3, +1 row), plus §N step 0 run-state paths.
- **References/assets to resolve:** none.

## N. Write-load tally and commit plan

- Docs edited 1 + archives 1 + new docs 0 + MANIFEST + CHANGELOG (+ assets 0) = ~4 canonical writes.
- **Commits, in order (Phase 4 onward; none in this session):**
  0. **Run-state commit (resume step, before the per-doc dance; §K M-2):** first verify `git status --porcelain` lists exactly these paths and nothing else — `_INBOX/TEST_C_RECOVERY_CARGO.md`, `_AUDIT/SYNC_2026-09-26_test-c-recovery/UPDATE_MAP.md`, `session_2026-09-26.md`, `RECOVERY.md`, `agent_docs/RESPONSES/response_2026-09-26_*.md` (the Gate 1, Gate 2, and Gate 2-approval logs). Then commit them with explicit paths: `chore(sync): run-state through Gate 2 [SYNC_2026-09-26_test-c-recovery]`.
  1. `docs(ARCHITECT_QUESTIONNAIRE): v2.3 - TEST C synthetic recovery validation note [IN-2026-09-26-01]` — carries the archive, the target, MANIFEST (L3, L29), CHANGELOG (L3, +1 row). → **CONTENT_SHA** recorded in §O.
  2. `chore(sync): run metadata [SYNC_2026-09-26_test-c-recovery]` — map §O (CONTENT_SHA), draft `RUN_SUMMARY.md`, session file, RECOVERY.md.
- Hygiene: plain hyphens; **no Co-Authored-By trailer** on any of these commits (D22 — the skill's rule overrides a harness-injected trailer); one version bump per doc per run; explicit-path `git add`, never `git add -A`.
- Push: none before Gate 4. With merge target NONE, publication at Gate 4 is the Operator's call.

## O. Approval and amendments

- [x] Gate 1 — scope + classification APPROVED by Operator at 2026-09-26 ~11:31 BST (merge target ruled NONE)
- [x] Gate 2 — this map APPROVED by Operator at **2026-09-26 12:13 BST** ("Approve the UPDATE MAP exactly as proposed."). Route `TINY` confirmed; NO-CHANGE rows approved: none; TINY waiver line: "Docs-only QA waiver per SOFTWARE_FACTORY_PLAYBOOK §2.5 item 6 — Operator, 2026-09-26 12:13 BST."; LARGE → TINY downgrade ruling: none — route is TINY on evidence. Operator rulings (verbatim): "Route: TINY" · "Merge target: NONE — disposable TEST C branch" · "Version: 2.3 approved for this synthetic run only" · "Plain-paragraph placement approved" · "All ENGINEER-PROPOSED wording approved" · "DRIFT-2026-09-26-01 remains parked and untouched" · "M-1 CRLF-safe archive fidelity method approved" · "M-2 interrupted-run dirty-state handling approved" · "Docs-only QA waiver approved". Map FROZEN from this point.
- [ ] Gate 3 — N/A (TINY, waiver)
- Amendments: none
- Overrides logged: none
- Session interrupt (TEST C, Operator instruction): execution deliberately stopped after Gate 2 approval at 2026-09-26 12:13 BST, before Phase 4. No canonical write, no commit, no push. Resume via D15a: map APPROVED + no run commits after BASE → Phase 4, starting at §N step 0 (§K M-2).
- CONTENT_SHA (filled after the last content commit exists): `<pending — Phase 4>` · Gate 4 APPROVED at `<pending>` · pushed at `<pending / N/A>`
- Skill refinements observed (for the run summary): (R1) P4.2.5 fidelity command is EOL-unsafe on `core.autocrlf=true` clones — §K M-1; (R2) P4.1 "confirm the tree is clean" does not say how to treat uncommitted run-state from an interrupted pre-Phase-4 session — §K M-2; (R3) `RECOVERY.md` at BASE described 2026-08-10 and predated the three skill commits — the family's own evolution commits did not update it.

## P. Route evidence (TINY / LARGE decision record)

| Fast-path condition (route-selection.md) | Evidence | Holds? |
|---|---|---|
| A1 ≤ 3 intake IDs | 1 (§A) | YES |
| A2 ≤ 3 canonical touch-list docs (after §B search) | 1 — ARCHITECT_QUESTIONNAIRE (§C); MANIFEST/CHANGELOG are infra, `_ARCHIVE/` is an archive | YES |
| A3 no new canonical document | §D empty | YES |
| A4 no Factory-wide terminology rename / change | no role, gate, module, lifecycle, or artifact name changes; T1–T4 new-term hits = 0 | YES |
| A5 no cross-correction dependency | single ID | YES |
| A6 no high-risk governing-rule change | synthetic note in a Version History section; no rule changed; target subject (architect ignition questionnaire) is not auth / RBAC / tenant / PHI / payments / QA verdict / git governance | YES |
| A7 no unresolved conflict | §K: 0 CONFLICT rows; K-1 CLARIFICATION already ruled | YES |
| A8 no cross-boundary change required | §J empty | YES |
| A9 propagation search bounded and complete before Gate 2 | 6 terms, full live scope, 12 hit lines, all dispositioned (§B) | YES |
| A10 docs-only QA waiver eligible | changes confined to one live-scope markdown doc + MANIFEST + CHANGELOG + `_ARCHIVE/`; no assets, lints, CI, or skills; Operator has not disallowed waivers | YES |
| **Route** | ALL hold | **TINY** (unchanged from provisional; confirmed by Operator at Gate 2, 2026-09-26 12:13 BST) — Operator escalation / downgrade ruling: none |
