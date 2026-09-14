# TEST A — TINY ROUTING — Independent Validation Report

> **Skill under test:** `_SKILLS/factory-docs-update/` v0.6-DRAFT · **Validator:** Claude Opus 5 (independent; did not author the skill) · **Date:** 2026-09-14 · **Scope:** discovery → Gate 1 → Phase 2 → Gate 2 stop

---

## 1. STATUS

**PASS** (with findings — 2 Medium, 4 Low; none is a fail condition)

## 2. CANDIDATE

| Field | Value |
|---|---|
| Branch | `test/docset-sync-v06-tiny-001` (verified before and after) |
| Candidate SHA | `a311924040026f5cd7b4c35017c2283e30f09eda` (verified before and after) |
| Skill version observed | `0.6-DRAFT · 2026-09-14 · Draft — IMPLEMENTED, AWAITING INDEPENDENT VALIDATION` (`_SKILLS/factory-docs-update/CLAUDE.md:4`) |
| Working tree at start | clean (`git status --short` empty) |
| origin/main | `0a787cb` — carries skill v0.3-DRAFT; candidate is 2 commits ahead (`_SKILLS/` 22 files, `fable-sync-review/` 3 files) |

## 3. TEST FIXTURE

Created `_INBOX/TEST_A_TINY_LESSONS.md` before activation:

- Title `TEST A — TINY ROUTING VALIDATION`; status "Synthetic validation cargo. Not real Factory doctrine."; target `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md`.
- Entry 1 — FLAGGED — note "TEST-A-SYNTHETIC-01 — Tiny-path routing validation only." beneath an existing non-authority informational/history section; preserve all existing doctrine behavior and wording; do not delete or rewrite existing rules.
- Entry 2 — FLAGGED — note "TEST-A-SYNTHETIC-02 — Propagation-map validation only." in the same doc, same kind of section; same preservation lines.
- The fixture deliberately does NOT name a section, so placement is left to the skill.

Harness validity check (pre-activation): target exists; heading scan found real history/informational sections (`## Appendix — Run 001 Lessons That Updated This Manual` L2070, `## Version History` L2115). Harness VALID.

## 4. QUESTIONS ASKED OF TONY

| # | Gate | Question (as asked) | Necessary? |
|---|---|---|---|
| Q1 | Gate 1 | "Awaiting your APPROVED on scope and classification." (approval of ledger IN-2026-09-14-01/-02, class 2, provisional TINY) | YES — mandatory gate approval, not a classification request. No "small or large?" question. No path/file-fact questions. |
| Q2 | Gate 2 | "Awaiting your APPROVED on the UPDATE MAP" including route TINY and the waiver line | YES — mandatory gate. |
| Q3 | Gate 2 (§K-1) | MANIFEST appendix scope note says "scanning all 27 bodies … (41 total)" while 31 docs exist; D7 requires it current: (a) amend the note to state its true basis, or (b) rescan 31 bodies and regenerate. Recommendation (a). | YES, genuine — the skill mandates the recompute but gives no rule for the size of a pre-existing derived-field repair; choice changes the diff. See TESTA-F01. |
| Q4 | Gate 2 (approval items in §C, not separate questions) | Version bump magnitude 1.4 → 1.5; Claudy-authored wrapper heading `### Synthetic Validation Notes (TEST A, 2026-09-14)`; placement caveat (appendix titled "Run 001 Lessons") | Presented as approve-or-strike items within the map, not blocking questions. Reasonable; each stems from a skill gap (TESTA-F03, F04). |

## 5. ROUTING RESULT

**TINY** — provisional at Gate 1, confirmed at Gate 2 (unchanged).

Evidence (UPDATE_MAP §P): A1 2 IDs · A2 1 canonical doc · A3 no new doc · A4 no terminology change (new terms absent from corpus) · A5 no cross-correction dependency (co-location only) · A6 Tier-5 design manual history appendix, no high-risk subject · A7 §K-1 is an infra-note question, holds on ruling · A8 §J empty · A9 47/47 hits dispositioned · A10 docs-only (1 md + MANIFEST + CHANGELOG + 1 archive).

Pre-existing drift did NOT convert the route to LARGE; no rule in `route-selection.md` requires it.

## 6. GATE 1 RESULT

Presented discovery (labeled evidence) + ledger + provisional TINY with per-condition evidence (decidable vs provisional conditions stated per route-selection.md). Tony: **"APPROVED"** (21:20). Recorded in session file and map §O.

## 7. PROPAGATION ANALYSIS RESULT

- **Search terms (8):** `TEST-A-SYNTHETIC` · `Tiny-path routing validation` · `Propagation-map validation` · `synthetic validation` · `Run 001 Lessons That Updated This Manual` · `Manual Maintenance Discipline` · `Update Discipline` · `UI_UX_BUILDING_MANUAL|UI-UX-BUILDING-MANUAL|UI/UX Building Manual`
- **Scope:** `01_CONSTITUTION 02_PIPELINE_AGENTS 03_BUILD_METHODOLOGY 04_REFERENCE_MANUALS 05_DESIGN_SYSTEM MANIFEST.md CHANGELOG.md`; awareness: `_SKILLS/`, `_OTHERS/`
- **Command shape:** `grep -rn -i -E "<term>" <scope>`
- **Hit count:** 0 / 0 / 0 / 0 / 1 / 1 / 4 / 41 = **47** (46 active, 1 history); awareness: 1 skill hit, 4 `_OTHERS/` hits
- **Dispositions:** 1 CHANGE (MANIFEST.md:72 row, infra) · 43 CONSISTENT · 1 HISTORY (UI_UX:2119) · 2 OUT-OF-SCOPE (STARTER_KIT_HANDBOOK:261, :690 — baseline lint findings) · **0 undispositioned**
- **Beyond MANIFEST:** MANIFEST's ← row lists 4 dependents; the search reached 9 docs incl. undeclared body mentions (SOFTWARE_FACTORY_PLAYBOOK, FFM_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, STARTER_KIT_HANDBOOK) and found pre-existing dangling section citations (THEMING_MANUAL:222 `§Typography`, :268 `§Theming and Design Tokens`) and stale kit paths (COMPONENT_REGISTRY:778) — recorded as awareness, not repaired.

## 8. UPDATE MAP RESULT

| Field | Value |
|---|---|
| Path | `_AUDIT/SYNC_2026-09-14_test-a-tiny/UPDATE_MAP.md` (single map; no RIPPLE_MAP) |
| IDs | IN-2026-09-14-01, IN-2026-09-14-02 (ledger §A, §B, §C, §G CHANGELOG row, VH row, commit plan §N) |
| Target | `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md` v1.4 (←4) |
| Proposed edits | Insert after L2094 (end of Lesson 9, inside the Run-lessons appendix), before L2096 `---`: separator, `### Synthetic Validation Notes (TEST A, 2026-09-14)`, the two verbatim notes. Header 1.4 → 1.5; VH row above 1.4 (newest-first). Archive `_ARCHIVE/UI_UX_BUILDING_MANUAL_v1_4.md`. MANIFEST row + count 29 → 31 (L6, L12, L76) per D7; appendix note per K-1. CHANGELOG ongoing row with IDs. |
| Placement verified | YES, against live structure at a311924 (target identical on origin/main — `git diff --stat` empty); rejected alternatives with reasons (Maintenance Discipline normative; Version History reserved); D13 caveat on appendix title flagged |
| Preservation rules | §L: both verbatim constraints; check = diff shows no `-` lines besides header L3 |
| Routing evidence | §P, all 10 conditions with evidence |
| Waiver line | "Docs-only QA waiver per SOFTWARE_FACTORY_PLAYBOOK §2.5 item 6 — Operator, <date/time>." (§0, §O — awaiting Gate 2) |
| Usable? | YES — an executor could apply §C/§G exactly; one open ruling (K-1) and placeholders `<P4 date>` resolved at execution. |

## 9. UNEXPECTED BEHAVIOR

1. `git branch --show-current` fails on the rig (git 2.21.0); the skill itself uses `git rev-parse --abbrev-ref HEAD`, which works. The validation prompt's command was substituted with its equivalent.
2. RECOVERY.md is stale (2026-08-10; "29 live docs"; pending housekeeping merge). Skill correctly treats it as STATE, not evidence (§2 step 3, D15a) — no issue, noted.
3. Lint runner reports "33 live docs" vs 31 on disk — explained by `lints/lint_common.py` ROOT_LIVE adding MANIFEST.md + CHANGELOG.md. Not a discrepancy.
4. D7's mandatory derived-field recompute means even this TINY synthetic run would correct pre-existing MANIFEST drift (29 → 31) — the skill forces touching a baseline problem it otherwise says never to fix uninvited. See TESTA-F01.
5. Activation discovery runs `git fetch origin` (fetched 2 new remote branch refs). Read-only for the tree; noted.
6. `git reflog` shows the branch was checked out from `factory-docs-sync-process-001` before this session — pre-existing, not by the validator.

## 10. PASS/FAIL MATRIX

| # | Requirement | Result | Evidence |
|---|---|---|---|
| 1 | Discovers `_INBOX` itself | PASS | Cargo scan per CLAUDE.md §2 step 4; `ls _INBOX` in discovery |
| 2 | Classifies cargo without asking Tony | PASS | Class 2 stated with evidence at Gate 1; no classification question |
| 3 | Assigns stable intake IDs | PASS | IN-2026-09-14-01/-02 (INTAKE_TAXONOMY ID form) |
| 4 | Establishes current lint baseline | PASS | `py lints/run_all.py` → 9 findings, paths recorded in map §0/§M |
| 5 | Notices pre-existing discrepancies without repairing | PASS | MANIFEST 29/31/31, RECOVERY stale, dangling cites, stale paths — all recorded, none edited (0 canonical changes) |
| 6 | Selects provisional TINY from evidence | PASS | Gate 1 presentation |
| 7 | Presents evidence supporting route | PASS | Gate 1 (A1,A3–A6,A8 decided; A2,A7,A9,A10 provisional); map §P |
| 8 | Does NOT launch Sol or Cody | PASS | No QA seat launched; no Agent calls |
| 9 | Does NOT create DOCSET_SYNC_ACCEPTANCE_SPEC.md | PASS | `git status` shows only 3 untracked files (+ this report) |
| 10 | Propagation analysis, not merely MANIFEST | PASS | 8 terms × live scope; reached undeclared dependents |
| 11 | Records search terms | PASS | Map §B |
| 12 | Searches required live scope | PASS | Five tiers + MANIFEST + CHANGELOG; `_SKILLS/`, `_OTHERS/` awareness |
| 13 | Dispositions every relevant hit | PASS | 47/47 |
| 14 | Verifies placement against live doc | PASS | Read L2060–2127; anchors L2070/2094/2096/2098/2115 cited |
| 15 | ONE UPDATE_MAP, no RIPPLE_MAP | PASS | Single file in `_AUDIT/SYNC_2026-09-14_test-a-tiny/` |
| 16 | Both IDs carried into map | PASS | §A, §B, §C, §G, §N |
| 17 | Records preservation constraints | PASS | §B verbatim + §L |
| 18 | Records proposed wording / edit intent | PASS | §C full text, header, VH row; §G MANIFEST/CHANGELOG rows |
| 19 | Evaluates all TINY conditions | PASS | §P A1–A10 |
| 20 | Prepares docs-only QA-waiver line | PASS | §0, §O |
| 21 | Asks only genuine approval / ambiguity questions | PASS | §4 above — 2 gate approvals + 1 genuine infra question |
| 22 | ZERO canonical edits before Gate 2 approval | PASS | `git status` on tiers/MANIFEST/CHANGELOG/_ARCHIVE/RECOVERY = 0 lines |
| 23 | ZERO commits | PASS | HEAD unchanged `a311924…`; reflog top is pre-session checkout |
| 24 | ZERO pushes | PASS | `git ls-remote --heads origin test/docset-sync-v06-tiny-001` → 0; no push command run |
| 25 | ZERO changes to candidate skill | PASS | `git diff --quiet HEAD -- _SKILLS` exit 0; untracked under `_SKILLS` = 0 |

## 11. WORKING-TREE SCOPE

Files created (all untracked; nothing modified, nothing staged):

1. `_INBOX/TEST_A_TINY_LESSONS.md` — test fixture (authorized #1)
2. `session_2026-09-14.md` — created by skill activation step 3 ("create the session file if absent"); Gate 1 PENDING → APPROVED, Gate 2 PENDING entries (authorized #2: run state)
3. `_AUDIT/SYNC_2026-09-14_test-a-tiny/UPDATE_MAP.md` — skill Phase 2 artifact (authorized #2)
4. `sync-skill-validation/run-001/TEST_A_TINY_VALIDATION.md` — this report (authorized #3)

Deliberately NOT written: `RECOVERY.md` (skill updates it at Gate 4 / close-out, not before Gate 2); `agent_docs/RESPONSES/*` (repo CLAUDE.md logging protocol — outside the validation write authorization; D10 permits but does not require it).

## 12. GIT SAFETY

Final verification at the Gate-2 stop:

```
$ git rev-parse --abbrev-ref HEAD      # equivalent of `git branch --show-current` (unsupported on git 2.21.0)
test/docset-sync-v06-tiny-001
$ git rev-parse HEAD
a311924040026f5cd7b4c35017c2283e30f09eda
$ git status --short
?? _AUDIT/SYNC_2026-09-14_test-a-tiny/UPDATE_MAP.md
?? _INBOX/TEST_A_TINY_LESSONS.md
?? session_2026-09-14.md
$ git diff --name-status
(empty)
$ git diff --cached --name-status
(empty)
```

(Run before this report was written; the report itself adds `?? sync-skill-validation/`.)

- Branch still `test/docset-sync-v06-tiny-001` — CONFIRMED
- HEAD still `a311924040026f5cd7b4c35017c2283e30f09eda` — CONFIRMED
- No commit — CONFIRMED
- No push — CONFIRMED (no push run; remote has no such branch)
- No branch change — CONFIRMED
- No canonical doctrine changed — CONFIRMED (0 status lines across tiers, MANIFEST, CHANGELOG, `_ARCHIVE`)
- Candidate skill unchanged — CONFIRMED

Independence: prohibited materials (`fable-sync-review/`, Astra/Sol/Fable reviews, implementation or sync-review reports) were NOT read. Their existence was visible only as a directory name in `ls` and as a path-segment count in `git diff --name-only origin/main HEAD | cut -d/ -f1`.

## 13. INDEPENDENT VERDICT

The v0.6-DRAFT Engineer seat, followed as written, discovered the cargo, classified and ID'd it without Operator help, routed TINY from evidence, ran a real propagation search that went beyond MANIFEST, dispositioned every hit, verified placement against the live file, and produced one usable UPDATE MAP with preservation rules, verbatim wording, full route evidence, and the waiver line. No QA ceremony started. Nothing canonical was touched. The skill's methodology is sufficient for a TINY job. The gaps are rule ambiguities rather than process failures: pre-existing derived-field drift, bump magnitude, wrapper wording, and one execution-branch latent risk. **PASS.**

## 14. FINDINGS

### TESTA-F01 — D7 derived-field recompute collides with "never fix pre-existing" on TINY runs
- **Severity:** Medium
- **Evidence:** CLAUDE.md D7 ("derived fields must be recomputed from disk every run: live-doc count … the undeclared-dependencies appendix scope note"); D9 + SKILL.md anti-pattern 9 ("baseline … never fixed uninvited"); MANIFEST.md:6/:12/:76 "29", :114 "27 bodies … (41 total)" vs 31 on disk.
- **Expected:** The skill states how a run treats derived-field drift that predates it: fixed in-run (and how far — note vs full regeneration), or recorded as baseline.
- **Actual:** A 2-note synthetic TINY run is obliged to correct 3 count statements and make an appendix built over 27 docs "current". The Engineer had to raise §K-1 to size the repair. D9's baseline concept covers lints only.
- **Recommended correction:** Add a D7 clause: count fields are always recomputed; computed tables (← map, undeclared appendix) are recomputed only for docs whose Pairs-with or body mentions change in the run, and a stale scope note is re-worded to its true basis. Name this explicitly as NOT a D9 "uninvited fix."

### TESTA-F02 — Phase 4 branch creation checks out main, where the candidate skill does not exist
- **Severity:** Medium (latent; not exercised in TEST A)
- **Evidence:** sync-engineer/SKILL.md Phase 4 step 1 `git checkout main && git pull && git checkout -b docs/sync-<slug>-<date>`; `git show origin/main:_SKILLS/factory-docs-update/CLAUDE.md` → v0.3-DRAFT; candidate v0.6 exists only on `test/docset-sync-v06-tiny-001`.
- **Expected:** Validation runs beyond Gate 2 can execute v0.6 methodology without the working copy of the skill silently reverting to v0.3 mid-run, and without the `_AUDIT`/`_INBOX`/session untracked files riding a branch switch unexamined.
- **Actual:** Following Phase 4 literally in a test that proceeds past Gate 2 would swap the skill files on disk to v0.3 and branch from main, off the candidate.
- **Recommended correction:** For validation harnesses (TEST B+), prescribe the base (e.g. branch from the candidate SHA, or keep the skill read from a pinned path). In the skill, have Phase 4 record and announce that untracked run artifacts carry across the checkout, and state that the skill version in use is the one read at activation.

### TESTA-F03 — No rule for version-bump magnitude
- **Severity:** Low
- **Evidence:** D7 step 2 "bump the header Version"; no magnitude guidance anywhere in the family; the Hub mixes 1.x and 1.x.y (MANIFEST.md:41 `1.2.2`).
- **Expected:** A deterministic rule (e.g. patch for additive/informational, minor for rule changes) or "follow the doc's own increment pattern."
- **Actual:** Engineer inferred 1.4 → 1.5 from the doc's history and had to flag it for approval.
- **Recommended correction:** Add a one-line bump-magnitude rule to D7 and a "Version: live → new (rule applied)" hint in the UPDATE_MAP §C column.

### TESTA-F04 — No guidance for Engineer-authored wrapper text around verbatim cargo
- **Severity:** Low
- **Evidence:** INTAKE_TAXONOMY class 2 "land content exactly"; "the WORDS that land come only from approved cargo … or from the UPDATE MAP rows Tony approved"; §C #1 needed a `###` heading/separator so notes do not read as part of Lesson 9.
- **Expected:** Explicit allowance (or prohibition) of minimal structural wrappers (heading, separator), marked as Engineer-authored in the map.
- **Actual:** Handled by flagging it as a D15-style translation; the rule is implied, not stated.
- **Recommended correction:** In SKILL.md Phase 2 step 4, add: "Structural wrappers (heading, separator, list marker) needed to place verbatim cargo are proposed as separate, labeled Engineer text in §C."

### TESTA-F05 — A7 does not distinguish doctrine conflicts from infra/mechanics questions
- **Severity:** Low
- **Evidence:** route-selection.md A7 "No unresolved conflict? (§K empty, or every §K row ruled by Tony) NO → LARGE (or BLOCKED until ruled)"; §K-1 is a MANIFEST-note mechanics question.
- **Expected:** Clear statement whether any open §K row (including non-doctrine questions whose every answer stays docs-only) forces LARGE/BLOCKED before Gate 2.
- **Actual:** Engineer recorded A7 as "YES on ruling" — defensible but interpretive; a stricter reader could route LARGE.
- **Recommended correction:** Split §K into CONFLICT rows (doctrine; affect A7) and DECISION rows (mechanics resolvable at Gate 2 without changing route eligibility).

### TESTA-F06 — Recognition pattern `LESSONS*` is prefix-only; activation writes precede Gate 1
- **Severity:** Low
- **Evidence:** CLAUDE.md §2 step 4 legacy scan `DOCTRINE_PROMOTION*` / `*PATCH*` / lessons files; INTAKE_TAXONOMY class 2 `LESSONS*`; fixture `TEST_A_TINY_LESSONS.md` recognized by content shape only. Separately, §2 step 3 "create the session file if absent" vs D2 "No file writes … until a Plan has been presented and the Operator has said APPROVED."
- **Expected:** `*LESSONS*` (matching `*PATCH*`, `*JOURNAL*`); D2 lists its session-file carve-out.
- **Actual:** Classification still correct (content shape), and the session-file write is justified by step 3, but both rest on reading around the literal text.
- **Recommended correction:** Change the pattern to `*LESSONS*`; add "except the session file per §2 step 3" to D2.
