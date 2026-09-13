# SYNC_SKILL_REVIEW — factory-docs-update — Stage A

> **Reviewer:** Fable 5.1, independent Factory Process Architect · **Run:** fable-sync-review/run-001
> **Date:** 2026-09-13 18:37 BST · **Stage:** A — REVIEW / DESIGN ONLY (no skill rewrite, no doctrine edit, no sync performed)
> **Branch reviewed:** `factory-docs-sync-process-001` · **Baseline SHA:** `0a787cb826118b4a010765d60e41a449df3ce746`
> **Companion:** `SYNC_PROCESS_PROPOSAL.md` (same folder)

Label key used throughout: **[FACT]** observed on disk (path cited) · **[INFERENCE]** reasoned from facts (basis stated) · **[REC]** recommendation · **[UNKNOWN]** could not be determined · **[NEEDS-TONY-DECISION]** requires the Operator.

---

## 1. STATUS

- **Review complete.** Both Stage-A reports written. Nothing else created or changed.
- **Version note [FACT]:** the mission refers to "v0.2". The copy on disk is **v0.3-DRAFT (2026-08-10)** in `_SKILLS/factory-docs-update/CLAUDE.md` line 4 and `SKILL.md` line 172. The 0.2 → 0.3 delta is the `_INBOX/` cargo bay, D15a resume protocol, and D16 cargo triage. This review covers the on-disk v0.3-DRAFT and calls it "v0.3" below; every finding was checked against that copy, not memory of v0.2.
- **Independence [FACT]:** no `astra-review/` folder exists on this branch; no prior Astra, Sol, whole-corpus Fable, disposition, or synthesis files were opened. The only historical run material consulted was the skill's own run evidence (`session_2026-08-05.md`, `session_2026-08-10.md`, `agent_docs/RESPONSES/response_2026-08-10_203000_run-summary.md`, `_AUDIT/DOCTRINE_PROMOTION_2026-08-04_NAVBAR_SAGA.md`) because it is the field record of the skill under review.
- **Constraint conflict, disclosed [FACT]:** the repo `CLAUDE.md` mandates a session file, `RECOVERY.md` updates, and `agent_docs/RESPONSES/` logging. The mission authorizes creating ONLY the two report files and forbids modifying existing files. I followed the mission. No session file, no RECOVERY.md edit, no RESPONSES copy. If Tony wants those, it is a one-line follow-up.
- **Lints [FACT]:** `py lints/run_all.py` run read-only on the baseline: ENCODING PASS, RETIRED-TERMS PASS, VERSIONED-REFS FAIL (8 hits), HEADER-PRESENCE FAIL (1 miss) — 9 pre-existing stragglers, all in `STARTER_KIT_HANDBOOK.md`, `DATABASE_MANUAL.md`, `UI_UX_BUILDING_MANUAL.md`. Matches the "9 pre-existing stragglers" the 08-10 run recorded. Working tree clean after the run.

## 2. SCOPE

**In scope:** the eight files of `_SKILLS/factory-docs-update/` as the DocSet synchronization mechanism; its fitness for the Part-2 mission (approved corrections, journals/lessons, new/revised process docs, diagrams/images, other approved intake); its conformance to `APP_FACTORY_SKILLS_PLAYBOOK`, `QA_PLAYBOOK`, `SOFTWARE_FACTORY_PLAYBOOK` §2.5, `ENGINEER_PLAYBOOK` §15, `MANIFEST.md`, `_ARCHIVE/README.md`, `lints/`, and CI.

**Out of scope:** the content quality of any doctrine document; Part-1 examiner findings; the starter kit; other repos; lint code changes (observed only).

## 3. CURRENT V0.2 PROCESS — PLAIN ENGLISH

What the skill actually does today, as written in v0.3 [FACT unless marked]:

1. **Activation.** Tony says "go read `_SKILLS/factory-docs-update/CLAUDE.md` and follow it." Claudy reads CLAUDE.md, then SKILL.md, runs environment discovery (`pwd`, `ls`, `git remote -v`, pull main), scans `_INBOX/` (root as legacy fallback), looks for a project lessons file, checks whether the GitHub MCP exists, reads MANIFEST.md. No question is asked that discovery could answer.
2. **Phase 1 — Intake.** Every `_INBOX/` file is classified aloud as PACK (promotion/patch entries editing existing docs), NEW DOC, or SUPERSEDING DOC. Anything unclassifiable is a QUESTION. Cross-repo entries are parked as SPLIT CANDIDATES; entries citing docs the Hub lacks are GAPs. Claudy presents scope. **Stop Gate 1:** Tony approves scope.
3. **Phase 2 — Ripple analysis.** Using MANIFEST's ← dependency map, Claudy lists each target doc's referencing docs, verifies each pack entry's stated placement against the live doc's real section structure, and fills `templates/RIPPLE_MAP.md` (touch list, new docs, consistency ripples, structural flags, write-load tally). **Stop Gate 2:** Tony approves the ripple map, which becomes the single source of truth for execution.
4. **Phase 3 — Route decision.** Claudy presents local git (standing primary since the 2026-08-05 ruling) versus GitHub MCP (exception), with estimates, in a fixed shape. **Stop Gate 3 (hard):** Tony chooses.
5. **Phase 4 — Execute.** Per doc, lightest ← first: archive the live doc to `_ARCHIVE/<NAME>_v<X_Y>.md` stamped from its header; edit and bump the header plus Version History row; update MANIFEST row; append CHANGELOG line. Local route: branch `docs/<topic>-<date>` off pulled main, one commit per doc. Lints must pass for Claudy's changes; pre-existing reds are reported, never fixed or exempted. **Stop Gate 4:** Claudy presents CHANGES / DIDN'T TOUCH / CONCERNS plus verification evidence and asks for approval "to push and hand off."
6. **Phase 5 — PR & handoff.** Claudy reports the compare URL; Tony clicks it, creates the PR, reviews, and merges with rebase-and-merge. Claudy predicts CI outcome.
7. **Phase 6 — Close-out sweep.** After merge: pull main, delete the branch, ensure `_INBOX/` is empty (landed, parked, or returned), commit session artifacts, mark pack entries ENCODED with the PR number, deliver the run summary and skill-refinement notes.

Doctrine always in effect: D1 narrate aloud; D2 Plan Mode first; D3 Operator owns routing, local git primary; D4 mid-flight checkpoint (MCP); D5 Claudy owns all git, Operator owns merge; D6 main is PR-only; D7 four-step dance; D8 MCP mechanics; D9 lint conduct; D10 read-only boundary; D11 close-out sweep; D12 evidence labels; D13 no invention; D14 minimal diff by blast radius; D15 Hub law over cargo conventions; D15a resume protocol; D16 cargo triage.

**Field record [FACT]:** two live runs. PR #8 (2026-08-05, four-entry pack + two new docs) and PR #10 (2026-08-10, seven cargo files incl. the first superseding-doc dance). Both merged. Refinement notes from both runs are recorded but only the 08-10 `_INBOX`/D15a/D16 set was encoded; the six 08-05 notes are still pending (`session_2026-08-05.md` lines 74–81; run summary lines 45–53).

## 4. WHAT IS STRONG / PRESERVE

Each mechanism on the mission's preserve list was checked against the text and the field record. Verdict per item:

| Mechanism | Where | Verdict | Basis |
|---|---|---|---|
| Discovery before questions | CLAUDE.md §2 step 3; SKILL.md Phase 1 step 5 | **SOUND — preserve** | [FACT] Matches Skills Playbook §9 activation flow exactly; 08-10 run asked four questions, all genuinely non-discoverable. |
| Plan Mode before writes | D2 | **SOUND — preserve** | [FACT] Playbook §10 verbatim spirit; partial approval honored. |
| Human approval gates | Gates 1–4 | **SOUND — preserve; re-sequence** | [FACT] Four gates fired in both runs. See D01 for the push ambiguity. |
| Promotion-pack / lessons discovery | Phase 1 step 2–3; AP-11 | **SOUND for packs; too narrow for Part 2** | [FACT] Finds `DOCTRINE_PROMOTION*`/`*PATCH*` and lessons files. See D06. |
| Ripple analysis | Phase 2; RIPPLE_MAP template | **SOUND — preserve; extend** | [FACT] Header-declared ← map used both runs. Incomplete for body-mention propagation (D04). |
| MANIFEST dependency use | Phase 2 step 1–2; D14 | **SOUND — preserve** | [FACT] The ← map is the right blast-radius instrument; it needs a recompute step (D14). |
| Placement verification against live docs | Phase 2 step 3; D13 | **SOUND — preserve** | [FACT] Caught a naming mismatch in the worked example and a real one in run 08-05 ("phase-close checklist" vs "Stage 7 Completion Checklist"). |
| Operator ownership of approvals | D2, D3, D5, README | **SOUND — preserve** | [FACT] |
| Local git as primary route | D3; TOOL_ROUTING | **SOUND — preserve** | [FACT] Standing ruling 2026-08-05; both runs local. |
| Main protected / PR-only | D6; §6 last paragraph | **SOUND — preserve; the one non-waivable rule** | [FACT] AP-4 incident; branch protection enforces. |
| Minimal-diff discipline | D14 | **SOUND — preserve** | [FACT] Run 08-10 used a fractional-section insert on a Tier-1 doc to keep the diff surgical. |
| Archive/version discipline | D7 step 1; AP-6; `_ARCHIVE/README.md` | **SOUND — preserve; add a fidelity check** | [FACT] Seven archives exist, all stamped from headers. No check that an archive is byte-equal to the pre-change live file (S07). |
| MANIFEST / CHANGELOG maintenance | D7 steps 3–4 | **SOUND in shape; derived fields drift** | [FACT] MANIFEST says "29 live docs" (lines 6, 12, 76); disk has 31 tier-folder `.md` files and MANIFEST's own tables have 31 rows. Appendix still says "27 bodies" (line 114). See D14. |
| Evidence labels | D12 | **SOUND — preserve** | [FACT] Same five labels as QA_PLAYBOOK §8 and Skills Playbook §11. |
| No-invention rule | D13 | **SOUND — preserve** | [FACT] |
| Cross-repo split handling | Phase 1 step 2, Phase 6 step 4, README gotchas | **SOUND — preserve; give splits IDs** | [FACT] Two splits parked 08-05 and restated 08-10 by name only; no ID survives across runs. |
| Lint / validation discipline | D9; AP-5 | **SOUND — preserve; encode lint-before-commit** | [FACT] Run 08-05 needed a fixup commit because lints ran after commits; run 08-10 ran them per doc. The doctrine text still says "throughout." |
| Interruption / recovery handling | D15a; README resume line | **SOUND — preserve; add QA-phase resume + RECOVERY.md pointer** | [FACT] Never exercised live [INFERENCE from session logs]. |
| Final cleanup sweep | D11; Phase 6 | **SOUND — preserve; define debris** | [FACT] Sweep fired both runs; what counts as debris was decided by Operator ruling mid-run (71 RESPONSES files deleted). |
| Audio-friendly Operator interaction | D1; §2 preamble | **SOUND — preserve** | [FACT] |

**Bottom line [INFERENCE]:** the bones are good. Every preserved mechanism maps to a real incident (AP-1 to AP-11) and both live runs succeeded. The skill's weakness is not what it does; it is what it cannot yet see (intent-level corrections, body-level propagation, assets) and what it cannot yet prove (completeness, independent verification).

## 5. DEFECTS / CONTRADICTIONS

Severity: BLOCKER / HIGH / MEDIUM / LOW. **No BLOCKER found:** nothing in v0.3 makes it unsafe for its current pack-landing job. HIGH items are those that prevent safe use for the Part-2 campaign.

### FSR-D01 — Push sequencing is contradictory (HIGH)
- [FACT] `SKILL.md` line 100 (Phase 4 route mechanics, local) lists `git push -u origin <branch>` as an execution step. Line 107 (Stop Gate 4) says "Awaiting your APPROVED to push and hand off." Line 109 says the phase output is "a pushed branch, fully verified, no PR yet." `references/TOOL_ROUTING.md` line 66 says "Push with -u origin <branch>; hand the Operator the compare URL" with no gate. `README.md` lines 66–67 say "Say APPROVED; he pushes the branch."
- [FACT] Practice resolved it the safe way: run 08-10 held seven commits unpushed until Gate 4 approval (`session_2026-08-10.md` lines 56–65).
- [INFERENCE] A fresh session following SKILL.md line 100 literally would push before Gate 4. The remote branch is not main, so no doctrine is broken, but "await approval before push" becomes theatre.
- **One executable contract [REC]:** commits are local during execution; **push happens once, after Gate 4 approval, as the Engineering → QA handoff action.** Remove push from the Phase 4 mechanics list; state it as the Gate 4 exit action in SKILL.md, TOOL_ROUTING, and README identically. Rework pushes (Cody loop) are sub-cases of the same rule: each retest cycle pushes only after Claudy's repair summary is acknowledged.

### FSR-D02 — Git-ownership and skill-type conflict with current Factory doctrine (HIGH)
- [FACT] D5: "Claudy owns all git; the Operator owns the merge." Current module doctrine says the opposite for Engineers: `BIM_PLAYBOOK.md` §2 line 29 ("runs zero git and zero cloud commands"), §7 line 110 ("Git-zero / cloud-zero"); `BUG_FIX_PLAYBOOK.md` §3 line 72 ("The Engineer runs zero git and zero cloud commands... hands the Coordinator suggested commit messages").
- [FACT] `CLAUDE.md` line 3 labels the skill "Stark Skill (semi-execution class, Brain Drain precedent)". `APP_FACTORY_SKILLS_PLAYBOOK.md` §2 lines 88–95: "Operator pastes commands → Stark Skill. Agent executes the task → Agent Skill. If a skill blurs this line, split it." Brain Drain is listed as a Stark example with the same semi-execution caveat (line 72), so precedent exists but is thin.
- [FACT] The Operator's standing ruling supports Claudy running git in the Hub (`RECOVERY.md`: "operator merges everything; pull-only on main; never write to main"; `session_2026-08-05.md` lines 103–109).
- [INFERENCE] The conflict is real but scoped: git-zero is code-module doctrine born from app repos; the Hub sync is docs-only under an explicit Operator ruling. The skill never says so, so a future examiner or a Claudy session that has read BIM/BUG_FIX first will see a contradiction.
- **[REC]** The skill states the carve-out explicitly in D5 with its provenance (2026-08-05 ruling) and declares its type honestly. **[NEEDS-TONY-DECISION]** whether the label stays "Stark (semi-execution)" or becomes "Agent Skill with Operator gates"; either is defensible, silence is not.

### FSR-D03 — Stale root-versus-`_INBOX/` statements (MEDIUM)
- [FACT] `references/ANTI_PATTERNS.md` AP-11 lines 68–70: packs "in the repo root are discovered automatically... The Operator's runbook puts them in the root." `templates/LESSONS_LEARNED.md` lines 8–9: "the skill's cargo scan finds those by name in the Hub clone root." `README.md` line 87: "the files just need to be in the root (Step 3)" while Step 3 (line 38) says `_INBOX/`.
- [INFERENCE] Three files contradict the v0.3 cargo-bay law. Non-fatal (root is a legacy fallback) but exactly the drift class the skill exists to prevent.
- **[REC]** Fix all three when v0.4 lands; add "skill's own files are consistent with its current doctrine" to the Stage-B done criteria.

### FSR-D04 — No completeness mechanism: propagation is header-declared only (HIGH for Part 2)
- [FACT] Phase 2 uses MANIFEST's ← map, which is "computed by inverting the Pairs-With → lists" (MANIFEST line 77), i.e., header declarations. Body mentions are tracked only in the MANIFEST appendix (lines 112–133), computed once for "27 bodies" and never recomputed (run summary line 60 parks it).
- [FACT] Cross-references in live docs are backtick canonical names (`SOFTWARE_FACTORY_PLAYBOOK.md` etc.), not markdown links; zero `](...md)` links exist in the five tier folders. Grep-based propagation search is therefore feasible and cheap.
- [FACT] Derived-field drift already occurred under the current mechanism: MANIFEST "29 live docs" vs 31 on disk and 31 rows in its own tables.
- [INFERENCE] For a one-entry pack, the header map plus placement verification is adequate. For a Factory-wide correction ("rule X must become true everywhere"), header declarations cannot find every checklist, example, quick reference, or role instruction that restates the old rule. The skill has no step that searches the corpus for the rule's terms and dispositions each hit.
- **[REC]** See proposal §7 (UPDATE MAP schema: search terms + hit dispositions) and §14 (Cody re-runs the same searches).

### FSR-D05 — Self-certification only; no independent verification and no recorded waiver (MEDIUM)
- [FACT] Gate 4 evidence is produced by the same seat that made the changes. `QA_PLAYBOOK.md` §34 names "Engineer Self-Certification" an anti-pattern. `SOFTWARE_FACTORY_PLAYBOOK.md` §2.5 item 6 permits "a recorded Operator QA waiver" for documentation-only changes; the skill records no waiver.
- [INFERENCE] For tiny lessons this is acceptable under the waiver clause if the waiver is recorded. For a campaign-scale sync it is not: the person who wrote 20 diffs is the wrong person to prove nothing was missed.
- **[REC]** Add the QA seat for the large path; record an explicit waiver line at Gate 2 for the tiny path (proposal §19).

### FSR-D06 — Intake taxonomy cannot classify the Part-2 cargo (HIGH for Part 2)
- [FACT] D16 admits exactly three classes: PACK, NEW DOC, SUPERSEDING DOC. Anything else is a QUESTION at Gate 1.
- [INFERENCE] A Correction Package (master index + domain briefs stating intent, not edits), a doctrine journal, an image, an archive-only record, or a "no canonical change" note would each stall as a QUESTION. Safe, but the skill would be asking Tony to classify every file, which the Skills Playbook §1 calls "a checklist with extra steps."
- **[REC]** Extend the taxonomy (proposal §3) with explicit routing per class and keep "unclassifiable = QUESTION" as the backstop.

### FSR-D07 — "Apply EXACTLY as written" assumes edit-level cargo (HIGH for Part 2)
- [FACT] Phase 4 step 2: "apply the approved changes EXACTLY as written in the pack." D15: "Land the pack's CONTENT exactly as written; translate its MECHANICS." The 08-04 pack (`_AUDIT/DOCTRINE_PROMOTION_2026-08-04_NAVBAR_SAGA.md` lines 13–16) was authored that way: "Claudy lands each into its target file EXACTLY as written."
- [FACT] The mission states the Correction Package "will NOT prescribe exact line edits."
- [INFERENCE] The skill has no model for who drafts the words when cargo is intent-level. If Claudy drafts silently in Phase 4, Tony approves a map but never sees the prose; if Claudy refuses, the campaign stalls.
- **[REC]** Claudy drafts the proposed wording (or a precise placement-level intent where prose is trivial) inside the UPDATE MAP; Tony approves the map; Phase 4 then applies the approved map EXACTLY. D13/D15 survive unchanged; the map becomes the "pack." Claudy still never adjudicates whether a correction is valid (proposal §4).

### FSR-D08 — D5 wording versus Phase 5 actions (LOW)
- [FACT] D5: the Operator's "ONLY git-adjacent action is clicking Merge." Phase 5 step 3 and README Step 6: open compare link, create the PR, review, merge. Two actions, not one.
- **[REC]** Reword D5: "creates the PR from the compare link and merges."

### FSR-D09 — Activation pulls main before any plan, and the instruction is ambiguous off-main (LOW)
- [FACT] CLAUDE.md §2 step 3: "If inside a clone, `git pull` main current before anything else." D2 forbids branch creation and writes before approval; a pull mutates the working tree. This review session is on a feature branch, where "pull main current" has no single meaning.
- **[REC]** Discovery does `git fetch` and reports main's distance; the pull happens at branch creation in Phase 4 (already `git checkout main && git pull`).

### FSR-D10 — Architect relay path is non-executable and the Architect seat is undefined for Part 2 (LOW)
- [FACT] Phase 2 step 5 and the RIPPLE_MAP preamble: the map is "authored by the Architect (Jarvis) when in the loop... present it as DRAFT for the Operator to relay." No artifact path, format, or handoff mechanism exists for that relay.
- [INFERENCE] In Part 2 the Architect's contribution is the approved Correction Package itself (Part 1 output). The map is Claudy's.
- **[NEEDS-TONY-DECISION]** Jarvis's seat in Part 2: none, reviewer of the update map, or author of preservation constraints. Proposal assumes "none beyond Part 1" (§2).

### FSR-D11 — Debris versus durable artifacts is undefined (LOW)
- [FACT] D10 allows writing "session artifacts"; D11 says commit them "into the PR or an immediate housekeeping PR." On 08-10 the Operator deleted 40 then 31 `agent_docs/RESPONSES/` files as merged-PR clutter, by ruling, mid-run (`session_2026-08-10.md` lines 77–80; commit b760588).
- [INFERENCE] Without a rule, every large sync will generate dozens of response logs whose fate is decided ad hoc.
- **[REC]** Proposal §18 defines the durable package and the debris list.

### FSR-D12 — Field-validated refinements are absent from the doctrine text (LOW, cumulative)
- [FACT] Six 08-05 notes (`session_2026-08-05.md` lines 74–81) and six 08-10 notes (run summary lines 47–53) are recorded, not encoded: lint-before-commit per doc; single-line header law for new docs; Version History ordering; NO Co-Authored-By; close-out cargo manifest; post-merge verification; deterministic PR-number discovery; kit-internal reference resolution; unexplained working-tree changes as a STOP; commit-message hyphen safety; fractional-section insert pattern.
- [INFERENCE] A fresh session following the current text would repeat the 08-05 failures (fixup commit, header lint miss). The 08-10 run avoided them because the same operator-and-agent pairing remembered.
- **[REC]** Encode as a batch in Stage B (S04). Three of them are QA-relevant (header law, ordering, no Co-Authored-By) and become acceptance checks.

### FSR-D13 — Gate 3 route ceremony is mandatory even when the answer is fixed (LOW)
- [FACT] `decision-trees/route-selection.md` Q1/Q2 short-circuit to "recommend local git" at a clone, yet SKILL.md Phase 3 still requires presenting both routes "in this exact shape" and a hard stop. Both live runs: "Local. Go."
- [INFERENCE] Ceremony that produces the same answer every time at a clone erodes attention for the gates that matter.
- **[REC]** S01: record the route as a line in the UPDATE MAP (approved at Gate 2); run the full both-routes ceremony only when the exception conditions hold (no clone). Operator ownership is preserved because Tony approves the map.

### FSR-D14 — MANIFEST maintenance rule omits derived fields; infra-doc versioning undefined (MEDIUM)
- [FACT] D7 step 3: "update the doc's row." Nothing says recompute the live-doc count, the ← dependency map, or the appendix. MANIFEST's own header is still v1.0 / 2026-07-12 (line 3) after content changes on 08-05 and 08-10; `_ARCHIVE/README.md` bump rule applies to "docs," and no rule says whether infrastructure files bump or archive.
- [FACT] Result: "29 live docs" stated three times; 31 on disk.
- **[REC]** S08: derived fields are computed from disk at every run and asserted by QA; decide infra-doc versioning (NEEDS-TONY-DECISION, low stakes; proposal recommends "infra files bump Date only, never archive").

### FSR-D15 — CHANGELOG append step has no format contract (LOW)
- [FACT] `CHANGELOG.md` "Ongoing entries" (lines 24–34) are pipe rows with no table header row, so they do not render as a table; each run appended in the same shape. Lints do not check CHANGELOG structure.
- **[REC]** Give the append step an exact row format and a header-row check in the sweep. Fixing the existing block is a Hub edit for the sync run, not for Stage B.

### FSR-D16 — Skill scope boundary versus Part-2 intake (MEDIUM)
- [FACT] CLAUDE.md §1 scope boundary and D10 exclude `_SKILLS/` folders, `lints/`, CI, and governance settings from writable scope. The mission's UPDATE MAP list includes "skill references" and the QA list includes terminology consistency that may require `lints/retired_terms_lint.py` changes.
- **[NEEDS-TONY-DECISION]** whether Part 2 may touch (a) `_SKILLS/*` content other than this skill, (b) `lints/`. Proposal recommends: (a) no — park as cross-repo-style splits with IDs even though they are in-repo; (b) no — QA applies campaign term lists as grep gates, lint promotion is a separate infra PR.

### FSR-D17 — Resume protocol ignores the repo's RECOVERY.md layer (LOW)
- [FACT] D15a inventories git state only. The repo `CLAUDE.md` mandates `RECOVERY.md` and session files, and run 08-10 used RECOVERY.md at Gate 4 as the merge-pending pointer.
- **[REC]** D15a step 1 reads RECOVERY.md and the day's session file first, then verifies against git.

### FSR-D18 — "Droppable anywhere" variants are inconsistent with `_INBOX/` law (LOW)
- [FACT] CLAUDE.md line 5 and §2 "Location variants" describe project-repo and bare-session activations; `_INBOX/` is a Hub-clone folder, lints and MANIFEST are Hub-local, and the standing ruling makes a clone the primary route.
- **[REC]** vNext declares "Hub clone is the execution environment"; the non-clone variants become a short "obtain a clone" instruction. TOOL_ROUTING stays as the exception reference, not deleted.

## 6. MISSING CAPABILITIES

For the Part-2 mission, v0.3 lacks (each cross-referenced to the proposal):

1. **Intake classes** for correction packages, journals, images/assets, archive-only material, no-change, blocked, cross-repo with IDs (D06 → proposal §3).
2. **Intent-to-edit drafting authority** with Operator approval of proposed wording before edits (D07 → §4, §7).
3. **Stable intake / correction IDs** carried from intake through commits, CHANGELOG, QA report, and ENCODED stamps. [FACT] The Hub already has the hooks: commit template `[<origin>]`, CHANGELOG's last column "finding/lesson IDs", pack ENCODED stamps. Nothing assigns IDs to non-pack cargo (→ §14).
4. **Propagation search** beyond header declarations, with per-hit disposition (D04 → §7, §14).
5. **Independent QA seat** with a campaign-level acceptance spec, traceability matrix, verdict vocabulary, bounded rework loop, and recorded waiver for tiny changes (D05 → §8, §11, §19).
6. **Completeness assertions** (every ID dispositioned; diff scope equals map scope; derived fields equal disk) as opposed to "edited files are valid" (→ §14, ACs in §8).
7. **Archive fidelity check**: archived copy byte-equal to the base-SHA live file (→ §9 checklist).
8. **Asset handling**: canonical location, reference resolution, orphan check, versioning without headers (no images exist today [FACT] → §15).
9. **Reference/path resolution check** for backtick file names, folder paths, and image links (→ §14, §15).
10. **Durable QA package location and debris list** (D11 → §18).
11. **QA-phase resume** (a dead Cody session) (→ §17).
12. **Handoff artifact** from Engineering to QA with the tested SHA (→ §10).

## 7. UNNECESSARY COMPLEXITY / SIMPLIFICATION

Suggestions (stable IDs):

- **FSR-S01** Fold the Phase 3 route stop into the UPDATE MAP approval; keep the full both-routes ceremony only when no clone exists (D13). Saves one gate per run without moving the decision away from Tony.
- **FSR-S02** Declare the Hub clone the execution environment; keep `references/TOOL_ROUTING.md` and D8 as the exception appendix rather than co-equal methodology (D18). Do not delete: AP-1 is the most expensive incident on record.
- **FSR-S03** One planning artifact, not two: RIPPLE_MAP evolves into UPDATE_MAP (see proposal §7 for the reasoning). Two maps would be two truths.
- **FSR-S04** Encode the twelve pending refinement notes as one batch (D12) rather than carrying them as tribal memory.
- **FSR-S05** Give every intake item an ID at Gate 1 and stop tracking splits and gaps by prose name.
- **FSR-S06** Add a propagation-search step to Phase 2 that records search terms and hit dispositions in the map; QA re-runs the same searches. Cheap (grep), high value.
- **FSR-S07** Archive fidelity: `git show <base-sha>:<path>` compared with the archive file. One command per doc.
- **FSR-S08** Derived fields (MANIFEST count, ← map, appendix) recomputed from disk every run; assert in QA.
- **FSR-S09** Durable package in one folder per run under `_AUDIT/` (existing precedent for run records: the 08-04 pack and the 08-10 finalization report live there [FACT]); everything else is debris.
- **FSR-S10** Tiny path = v0.3 flow plus a recorded QA waiver line. No new ceremony for a one-doc lesson.
- **FSR-S11** Link/path/image resolution as a QA grep gate now; promotion to a fifth lint later as a separate infra change.
- **FSR-S12** D15a reads RECOVERY.md first (D17).
- **FSR-S13** Version History ordering rule: follow the live doc's existing order; newest-last for new docs (08-10 note 1).
- **FSR-S14** Capture the 08-10 run as `examples/factory-module-doctrine-2026-08-10/` per Skills Playbook §15 step 10; none exists [FACT].
- **FSR-S15** Drop the "Architect relay" language; the Architect's Part-2 contribution is the Correction Package (D10).

Things I considered and rejected [INFERENCE]:
- **A mandatory post-QA Astra review.** Agree with the mission: none. Gate Q by an independent seat plus Tony's PR review is the control; a third review adds latency without a new evidence source.
- **Automating MANIFEST/CHANGELOG generation.** Parked in DOCTRINE_HUB_DESIGN §3 by design; out of scope for the skill.
- **A separate "large-sync" skill.** Two unrelated skills would drift; the mission forbids it and the fast-path/large-path split in one family covers both.

## 8. CONFLICTS WITH CURRENT FACTORY DOCTRINE

| # | Skill text | Doctrine | Nature | Resolution |
|---|---|---|---|---|
| C1 | D5 Claudy owns all git | BIM §2/§7, BUG_FIX §3: Engineer git-zero | Real conflict, scoped to code modules | Explicit carve-out citing the 2026-08-05 ruling (D02) |
| C2 | "Stark Skill (semi-execution)" | Skills Playbook §2: agent-executes = Agent Skill; "split if blurred" | Classification tension | Tony decision (D02) |
| C3 | Gate 4 self-verification only | QA_PLAYBOOK §34 self-certification anti-pattern; SFP §2.5.6 waiver clause | Gap, not contradiction | Waiver for tiny path; QA seat for large (D05) |
| C4 | No ACCEPTANCE_SPEC-like contract | SFP §2.5.1: every code-bearing module handoff includes ACCEPTANCE_SPEC | Docs are non-code; clause does not bind | Campaign-level DOCSET_SYNC_ACCEPTANCE_SPEC for the large path (proposal §8) |
| C5 | No session file / RECOVERY.md mention | ENGINEER_PLAYBOOK §16 session memory; repo CLAUDE.md | Omission | S12 |
| C6 | `examples/` absent after two validated runs | Skills Playbook §15 step 10 | Omission | S14 |
| C7 | Skill Version History rows newest-first | Playbook §12 shows newest-last; Hub docs disagree among themselves [FACT: SFP newest-first, 03-tier newest-last] | Cosmetic inconsistency | S13 rule; leave existing order |

No conflict was found between v0.3 and `APP_FACTORY_SKILLS_PLAYBOOK` structural rules: two-file core present, frontmatter valid, SKILL.md under 500 lines (174), folder layout conforming, Version History present in both files, Operator Override protocol present with two worked examples.

## 9. RISK ASSESSMENT

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| **Incomplete propagation** in a Factory-wide sync: a corrected rule survives in a checklist, example, or role instruction somewhere (D04) | HIGH under v0.3 | HIGH — reintroduces exactly the audit's F-class contradictions | Propagation search in the map; QA re-runs; contradiction scan (proposal §7, §14) |
| **Claudy drifts into adjudication** when a correction brief is ambiguous or conflicts with another (D07) | MEDIUM | HIGH — authority model breaks silently | CONFLICT / BLOCKED dispositions require Tony; no-change proposals need Tony approval in the map (§4) |
| **Unapproved wording ships** because intent-level cargo is drafted in Phase 4 (D07) | HIGH under v0.3 | MEDIUM | Wording drafted in the map, approved at Gate 2 |
| **QA writes the doctrine** via acceptance criteria that add requirements not in the approved package (authority leak) | MEDIUM | HIGH | Derivation rule: every AC traces to an ID or a standing invariant; spec frozen after Tony approval (§8) |
| **Debris accumulation** across a multi-cycle QA loop (D11) | HIGH | LOW–MEDIUM | Durable package + debris list (§18) |
| **Derived-field drift** (MANIFEST count, ← map) compounds over 20 bumps (D14) | HIGH | MEDIUM | Recompute from disk; QA asserts (S08) |
| **Push-before-approval** by a literal reading of Phase 4 (D01) | MEDIUM | LOW (branch only) | One contract (§10) |
| **Seat contamination**: Cody reads Claudy's session or map rationale and inherits assumptions | MEDIUM | MEDIUM | Cody's inputs are limited to spec, handoff, candidate SHA, and the approved package (§11) |
| **Process weight kills tiny updates** | MEDIUM | MEDIUM | Fast path = today's flow + waiver line (§19) |
| **Over-reliance on `_INBOX/` for a package that arrives as a folder tree** | LOW | LOW | Intake accepts a package folder as one cargo unit (§3) |

## 10. COVERAGE MANIFEST

Files examined in full unless a line range is stated. Line counts from `wc -l` at baseline.

| File | Lines | Read |
|---|---|---|
| `_SKILLS/factory-docs-update/CLAUDE.md` | 162 | full |
| `_SKILLS/factory-docs-update/SKILL.md` | 174 | full |
| `_SKILLS/factory-docs-update/README.md` | 126 | full |
| `_SKILLS/factory-docs-update/references/ANTI_PATTERNS.md` | 70 | full |
| `_SKILLS/factory-docs-update/references/TOOL_ROUTING.md` | 74 | full |
| `_SKILLS/factory-docs-update/decision-trees/route-selection.md` | 46 | full |
| `_SKILLS/factory-docs-update/templates/LESSONS_LEARNED.md` | 43 | full |
| `_SKILLS/factory-docs-update/templates/RIPPLE_MAP.md` | 46 | full |
| `03_BUILD_METHODOLOGY/APP_FACTORY_SKILLS_PLAYBOOK.md` | 1166 | full |
| `03_BUILD_METHODOLOGY/QA_PLAYBOOK.md` | 1829 | full |
| `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md` | 1072 | full |
| `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md` | 1598 | full |
| `MANIFEST.md` | 137 | full |
| `_ARCHIVE/README.md` | 21 | full |
| `lints/README.md`, `run_all.py`, `lint_common.py`, `versioned_refs_lint.py`, `header_lint.py`, `retired_terms_lint.py`, `encoding_lint.py` | 36 + 6 scripts | full |
| `.github/workflows/doctrine-lint.yml` | 18 | full |
| `CHANGELOG.md` | 38 | full |
| `README.md` (repo) | 2 | full |
| `RECOVERY.md` | — | full |
| `CLAUDE.md` (repo) | — | full (system context) |
| `03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md` | 184 | lines 23–142 + heading scan |
| `03_BUILD_METHODOLOGY/BUG_FIX_PLAYBOOK.md` | 737 | lines 45–92, 300–327, 573–590 + heading scan |
| `01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md` | 282 | lines 122–166 + heading scan |
| `_OTHERS/DOCTRINE_HUB_DESIGN_v0_1.md` | — | heading scan + §2.3/§2.6/§3 lines |
| `_AUDIT/DOCTRINE_PROMOTION_2026-08-04_NAVBAR_SAGA.md` | — | lines 1–80 + headings (pack format evidence) |
| `session_2026-08-05.md` | — | lines 64–115 (refinement notes, standing rules) |
| `session_2026-08-10.md` | — | full |
| `agent_docs/RESPONSES/response_2026-08-10_203000_run-summary.md` | 60 | full |

Repository-level checks run read-only: `git rev-parse`, `git status`, `git log`, `git branch -a`, `git remote -v`, `git tag` (none exist [FACT]), `find` for images (none exist [FACT]), grep for markdown links (none in live scope [FACT]), grep for role names (Sol, Cody, Astra: zero hits in live doctrine and the skill [FACT]; Claudy 17 files, Jarvis 4, "QA Lead" 3), live-doc count (31), MANIFEST row count (31), `py lints/run_all.py`.

**Not consulted, by instruction:** `astra-review/` (absent anyway), prior Astra/Sol/Fable reports, disposition and synthesis files. **Not read:** the remaining 24 live doctrine docs beyond heading scans, `_AUDIT/REVIEW_*` and `FINDINGS_LOG`, `_OTHERS/MASTER_DOC_LIST`.

## 11. RECOMMENDATION

**EVOLVE SUBSTANTIALLY.** Not KEEP LARGELY INTACT, not REPLACE.

Why not KEEP: four HIGH findings (D01, D02, D04, D06/D07) mean the current text cannot ingest a Correction Package, cannot prove propagation completeness, and contradicts itself on the one sequencing point (push) that the QA handoff depends on.

Why not REPLACE: every preserved mechanism in §4 is sound and incident-backed; both live runs succeeded; the Hub already carries the traceability hooks (commit origins, CHANGELOG ID column, ENCODED stamps, `_AUDIT/` run records). The evolution is additive: an intake taxonomy, one planning artifact that carries proposed wording and search-based propagation, an independent QA seat with a derived acceptance spec and a bounded loop, an explicit debris rule, and one push contract. The tiny path stays what it is today plus one waiver line.

**Three most important changes, in order:**
1. UPDATE MAP as the single approved artifact carrying intent → placement → proposed wording → propagation search → dispositions (fixes D04, D07, S03).
2. Independent QA with a derived, frozen `DOCSET_SYNC_ACCEPTANCE_SPEC.md` and a bounded Claudy ↔ Cody loop (fixes D05; proposal §8–§12).
3. One sequencing contract: commits local → Gate 4 → push → QA at recorded SHA → Gate Q → PR → merge → sweep (fixes D01; proposal §5–§6).

**UNKNOWN**
- Whether the GitHub MCP is still installed or wanted for any Hub work (irrelevant on the primary route; noted because TOOL_ROUTING keeps it alive).
- Whether Sol and Cody are distinct model sessions or the same model in two sessions; the proposal treats them as two seats regardless.
- The Correction Package's actual file layout (folder vs single file); the intake design accepts either.

**NEEDS-TONY-DECISION** (consolidated; also listed at the end of the proposal)
1. Skill shape: family skill (engineer + QA children under one CLAUDE.md) or single skill with a seat switch (proposal §20 recommends family, with the fallback stated).
2. Skill type label and the explicit git-ownership carve-out (D02).
3. Jarvis's seat in Part 2 (D10).
4. Whether `_SKILLS/*` (other than this skill) and `lints/` are writable in Part 2 (D16).
5. Durable QA package location: `_AUDIT/SYNC_<date>_<slug>/` (recommended) or a new top-level folder.
6. Whether the sync close-out cuts the first `doctrine-YYYY.MM` release tag (none exists; MANIFEST line 10 promises one).
7. Infra-doc versioning (MANIFEST/CHANGELOG header Date bump only, never archived) — low stakes, needs a ruling.
8. Whether Sol authors the acceptance spec (as proposed) or Tony/Jarvis does with Sol reviewing; the proposal keeps Sol as author under a derivation-only rule.

---
*Stage A review. No files other than this and `SYNC_PROCESS_PROPOSAL.md` were created; no existing file was modified.*
