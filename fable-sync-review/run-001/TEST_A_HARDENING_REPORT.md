# TEST_A_HARDENING_REPORT — factory-docs-update v0.6-DRAFT → v0.7-DRAFT

> **Pass:** bounded hardening after TEST A (TINY) passed · **Date:** 2026-09-14 · **Not a redesign.**
> **Candidate status:** **IMPLEMENTED — AWAITING INDEPENDENT VALIDATION.** Not certified. Nothing committed, nothing pushed.

Labels: **[FACT]** seen on disk or in command output · **[INFERENCE]** reasoned.

## 1. Starting SHA

| Item | Value [FACT] |
|---|---|
| Branch | `factory-docs-sync-process-001` (verified before and after) |
| HEAD | `a311924040026f5cd7b4c35017c2283e30f09eda` (unchanged at end) |
| Working tree at start | clean (`git status --porcelain` empty) |
| Lint baseline at start | ENCODING PASS · RETIRED-TERMS PASS · VERSIONED-REFS FAIL 8 · HEADER-PRESENCE FAIL 1 (33 live docs) |

## 2. Fixes applied

| Fix | What changed | Where |
|---|---|---|
| **1 — Pre-existing drift** | Derived fields are *checked* against disk every run, but *updated* only when the approved run changes the underlying value. A value already stale at BASE_SHA that the intake does not authorize repairing is **PRE-EXISTING / BASELINE DRIFT**: recorded with a `DRIFT-<run>-<NN>` ID and BASE evidence in map §G, parked, never added to the touch list, left byte-unchanged. Adding or removing a doc still requires the count update (the map says if that clears a recorded drift). Drift never escalates TINY. QA grades drift only as "unchanged from BASE". | CLAUDE.md §2 discovery, D7, D16 · engineer SKILL P0, P1.6, P2.6, P4.4, P9.7, worked example, AP-9 · UPDATE_MAP §0, §G (new drift table), §M · INTAKE_TAXONOMY ID table · STANDING_INVARIANTS AC-I · sync-qa AC-I · SYNC_HANDOFF claims · ACCEPTANCE_SPEC AC8 + out-of-scope · route-selection note · ANTI_PATTERNS AP-12 rule + new AP-18 · README gotcha |
| **2 — BASE_SHA is the execution base** | BASE_SHA is proposed from discovery (launch/intake-named commit, tag or branch tip, else the clean discovered HEAD), recorded in map §0 **before Gate 2**, approved with the map, and never assumed to be main. P4: if already on the approved run branch at BASE_SHA or a lawful descendant (only this run's commits since BASE), no new branch; otherwise `git switch -c <run-branch> <BASE_SHA>`. Changing BASE after Gate 2 = amendment. Compare URL and post-merge pull use map §0 `<merge-target>`. | CLAUDE.md §2, D6, D18 · engineer SKILL P0, P1.6, P2.1, Gate 2 line, P3, P4.1, P5 push, P8.1, P9.1, example, AP-13 · TOOL_ROUTING local branch step + MCP step 1 · SHA_AND_PUSH_CONTRACT BASE_SHA row · STANDING_INVARIANTS notation · UPDATE_MAP §0 (run branch, BASE_SHA, merge target) · SYNC_HANDOFF §0 · README gotcha |
| **3 — Engineer-proposed wording** | Exact intake wording is preserved unless Tony approves otherwise. Every added heading, wrapper, transition, label, explanation or normalization is written out in the §C row and marked **ENGINEER-PROPOSED** before Gate 2 (spans marked INTAKE-VERBATIM / ENGINEER-PROPOSED). No new artifact, no new gate. | CLAUDE.md D15 · engineer SKILL P2.4, Gate 2 line, example, AP-2 · UPDATE_MAP §C column · README gotcha |
| **4 — Conflict vs mechanical clarification** | **DOCTRINE / AUTHORITY CONFLICT** (incompatible governing requirements, or an approved request that cannot coexist with doctrine) → BLOCKED → Tony, §K type CONFLICT, counts for A7. **MECHANICAL CLARIFICATION** (non-doctrinal detail) → resolve from evidence first; only then the smallest question, §K type CLARIFICATION; not BLOCKED; does not affect the route. | CLAUDE.md D17, §2 (base disagreement example) · engineer SKILL P1.6, P2.5, AP-14 · UPDATE_MAP §K (Type column), §P A7 row · route-selection A7 · INTAKE_TAXONOMY class 11 "Not this class" · README gotcha |
| **5A — Content-first classification** | Class decided by status, contents, intent, target, provenance, authority, semantic form (+ counterpart match); filename is supporting evidence only; contents win on disagreement, stated aloud. Root-fallback name patterns only locate candidates. | CLAUDE.md §2 cargo scan, D16 · engineer SKILL P1.1, example, AP-15 · INTAKE_TAXONOMY "Cargo units" + class 2 recognition |
| **5B — Run-state vs canonical writes** | **RUN-STATE / PLANNING WRITE** (session file, RECOVERY.md, RESPONSES, durable-folder drafts such as the DRAFT UPDATE MAP and draft RUN_SUMMARY) may precede canonical execution approval. **CANONICAL WRITE** (tier docs, MANIFEST, CHANGELOG, `_ARCHIVE/`, assets, other skills, lints, CI, production files) only in P4 after Gate 2 (+ Gate 3 on LARGE). | CLAUDE.md D2, D10, §2 steps 3 and 6 · engineer SKILL P2.1 |

**Version / status:** the family's evolution principle (CLAUDE.md §6) requires a Version History row for meaningful changes, so the candidate moved to **0.7-DRAFT**: header in CLAUDE.md and README; Version History rows in CLAUDE.md, `sync-engineer/SKILL.md`, `sync-qa/SKILL.md`. Status everywhere: IMPLEMENTED — AWAITING INDEPENDENT VALIDATION.

## 3. Files changed

All under `_SKILLS/factory-docs-update/` [FACT: `git status --porcelain`; `git diff --stat` = 13 files, +91 / −66]:

`CLAUDE.md` · `README.md` · `_shared/references/ANTI_PATTERNS.md` · `_shared/references/INTAKE_TAXONOMY.md` · `_shared/references/SHA_AND_PUSH_CONTRACT.md` · `_shared/references/STANDING_INVARIANTS.md` · `_shared/templates/DOCSET_SYNC_ACCEPTANCE_SPEC.md` · `_shared/templates/SYNC_HANDOFF.md` · `_shared/templates/UPDATE_MAP.md` · `sync-engineer/SKILL.md` · `sync-engineer/decision-trees/route-selection.md` · `sync-engineer/references/TOOL_ROUTING.md` · `sync-qa/SKILL.md`

Created: this report. Untouched family files: `sync-engineer/templates/LESSONS_LEARNED.md`, `sync-qa/templates/QA_MATRIX.md`, `sync-qa/templates/GATE_Q_REPORT.md`. No files added or removed in the skill.

## 4. TESTA-F03 — DEFERRED

Version-bump magnitude (PATCH / MINOR / MAJOR) is **DEFERRED**. No governing Factory rule currently authorizes this skill to define bump magnitude, so no rule was invented. D22's "one version bump per canonical doc per unmerged run" is unchanged. Recorded in the CLAUDE.md 0.7-DRAFT Version History row.

## 5. Consistency checks

| Check | Result |
|---|---|
| No branch-from-main execution instruction remains | PASS [FACT] — grep `checkout main\|checkout -b\|origin/main\|from main`: remaining hits are discovery "distance from main" (informational), "never blindly from main" rules, the BASE_SHA row "never assumed to be origin/main", post-merge `git checkout <merge-target> && git pull`, and Version History text. The two `git checkout main && git pull && git checkout -b …` branch steps (engineer P4.1, TOOL_ROUTING) are gone |
| BASE_SHA meaning consistent | PASS — same definition in D18, SHA contract, UPDATE_MAP §0, STANDING_INVARIANTS notation, SYNC_HANDOFF, engineer P2.1/P4.1, TOOL_ROUTING. "Pending until branch creation" removed (it contradicted §C/§H/§L "verified at BASE_SHA" before Gate 2) |
| Pre-existing drift never silently absorbed | PASS — D7 rule; P4.4 leaves drift values as at BASE; AC-I requires drift byte-unchanged unless authorized; AC-S still requires every hunk to map to an approved row. Worked example no longer "fixes" 29 → 31 inside an unrelated LARGE run |
| Engineer-added wording requires Gate-2 visibility | PASS — D15, P2.4, §C column, Gate 2 line, AP-2 |
| Conflict and clarification distinct | PASS — D17 definitions; §K Type; A7 counts only CONFLICT; taxonomy class 11 excludes clarifications; "placement that does not exist" removed from class 11 recognition (it is D13 mechanics) |
| Intake classification content-first | PASS — D16, §2, P1.1, taxonomy "Cargo units" and class 2 |
| Run-state writes vs canonical writes | PASS — D2 definitions; D10 surface split; §2 steps 3 and 6 no longer contradict session-file creation before approval |
| TINY remains lightweight | PASS — no new gate, artifact, or seat; drift explicitly excluded from A2/A7/A8; clarifications don't flip A7 |
| LARGE flow intact | PASS — P3, P6, S1–S5, Gate 3/4/Q, SHA sequences unchanged; only AC-I wording (drift) and a "before starting Phase 4" phrasing changed |
| No canonical doctrine or infrastructure changed | PASS [FACT] — no path outside `_SKILLS/factory-docs-update/` in `git status` besides this report; MANIFEST, CHANGELOG, tiers, lints, `.github/`, `_AUDIT/`, session, RECOVERY untouched |
| Lint baseline not worsened | PASS [FACT] — after: ENCODING PASS · RETIRED-TERMS PASS · VERSIONED-REFS FAIL 8 · HEADER-PRESENCE FAIL 1 — identical to start |
| Single CLAUDE.md; no commit; no push | PASS [FACT] — HEAD still `a311924`; nothing staged |

## 6. Parked items

| ID | Item | Why parked |
|---|---|---|
| TESTA-F03 | Version-bump magnitude rules | DEFERRED — no authorizing Factory rule (§4) |
| HP-01 | Repo `CLAUDE.md` session-file / RECOVERY.md / RESPONSES protocol and Plan-Mode ceremony not executed for this pass | This pass's authorized surface excluded session files; the task directive itself served as the approved plan. Same pattern as Stage-B PB-02 |
| HP-02 | `DRIFT-<run>-<NN>` is a new ID form | Minimal addition needed so parked drift is traceable like `XB-`/`GAP-`; validate in LARGE run |
| HP-03 | MANIFEST derived-field drift (Stage-B PB-04) still exists in the Hub | Canonical/infra — now exactly the kind of item a run records as `DRIFT-…` and parks; needs its own authorized job |
| HP-04 | LF → CRLF warnings on the 13 edited files | Informational; same as Stage-B PB-09 |
| HP-05 | `examples/` still absent | Populate from the first validated run (Stage-B PB-03) |

## 7. Ready / not ready for LARGE independent validation

**READY.** [INFERENCE] The five fixes are consistent across the family, TINY is not heavier, and the LARGE lane is structurally unchanged. The LARGE test should probe the new seams specifically: (a) a stale-at-BASE MANIFEST value alongside a run that does *not* add a doc — expect a `DRIFT-…` row, no touch-list repair, Cody grading it "unchanged"; (b) a run that *does* add a doc — expect the count recomputed and the drift row marked CLEARED at Gate 2; (c) a BASE_SHA that is not main (branch ahead of main) and a resume on an existing run branch — expect no redundant branch; (d) an intake sentence plus an Engineer lead-in — expect ENGINEER-PROPOSED marking and AC-S hunk mapping; (e) one mechanical clarification and one real conflict — expect only the conflict to be BLOCKED and to affect routing; (f) a misleadingly named intake file — expect content-first classification.

---
*TEST A hardening complete. Candidate awaits LARGE-path independent validation.*
