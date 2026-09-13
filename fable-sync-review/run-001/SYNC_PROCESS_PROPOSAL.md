# SYNC_PROCESS_PROPOSAL — DocSet Synchronization vNext

> **Author:** Fable 5.1, independent Factory Process Architect · **Run:** fable-sync-review/run-001
> **Date:** 2026-09-13 18:37 BST · **Stage:** A — DESIGN ONLY. Nothing here is implemented.
> **Branch:** `factory-docs-sync-process-001` · **Baseline SHA:** `0a787cb826118b4a010765d60e41a449df3ce746`
> **Companion:** `SYNC_SKILL_REVIEW.md` (defect IDs FSR-D01…D18, suggestions FSR-S01…S15 referenced below)

Label key: **[FACT]** observed on disk · **[INFERENCE]** reasoned · **[REC]** recommendation · **[NEEDS-TONY-DECISION]**.

Design stance: the smallest coherent evolution of v0.3-DRAFT. Every mechanism the review marked SOUND is kept. Additions are limited to what the Part-2 mission cannot run without. Where the mission's proposed lifecycle was challenged, the challenge and the outcome are stated.

---

## 1. DESIGN GOALS

1. **One skill family, two paths.** A one-document lesson runs in the same phases as a Factory-wide correction sync; the large path adds a QA seat and a spec, nothing else.
2. **Authority never moves silently.** The Correction Package says WHAT must become true; Claudy proposes WHERE and HOW; Tony approves before edits; Sol derives the acceptance contract; Cody verifies; Sol issues Gate Q; Tony merges. No seat adjudicates for another.
3. **Completeness is proven, not asserted.** Every intake ID is dispositioned; every approved change is traceable to a hunk; every hunk is traceable to an approved map row; propagation is searched, not remembered.
4. **One sequencing contract.** Commits local → Gate 4 → push → QA at a recorded SHA → Gate Q → PR → merge → sweep.
5. **Minimal ceremony.** Six Tony touchpoints on the large path (scope, map, spec, push, PR, merge); four on the tiny path (scope, map with waiver, push, merge). The route stop disappears at a clone.
6. **Nothing floats.** One durable package per run; a named debris list; `_INBOX/` empty at close.
7. **Playbook-compliant.** Every structural change is checked against `APP_FACTORY_SKILLS_PLAYBOOK` (§20 lists the checks).

## 2. ROLES / AUTHORITY BOUNDARIES

Names below map onto Factory seats already in doctrine [FACT: `QA_PLAYBOOK` §4, `SOFTWARE_FACTORY_PLAYBOOK` §2.5, `BIM_PLAYBOOK` §2]. "Sol" and "Cody" appear nowhere in doctrine [FACT]; the skill must define them as seat labels, not new roles.

| Seat | Doctrine role | May | Must not |
|---|---|---|---|
| **Tony** | Operator / Coordinator / Final Approver | Approve scope, UPDATE MAP, acceptance spec, push; adjudicate BLOCKED and CONFLICT items; grant a recorded QA waiver (tiny path); create PR; merge | Be asked to run git; be asked to classify what discovery can classify |
| **Claudy** | Engineer (Doctrine Update Conductor) | Discover, classify, propose the UPDATE MAP incl. proposed wording, execute approved edits, run lints, commit, push after Gate 4, repair within the approved map, sweep | Decide whether an approved correction is valid; resolve conflicts between corrections; write outside the approved map; alter the acceptance spec; issue any verdict |
| **Sol** | QA Lead (independent seat) | Derive `DOCSET_SYNC_ACCEPTANCE_SPEC.md` from approved artifacts; author/approve the QA plan; adjudicate finding classification; issue Gate Q verdict; sign closeout | Add requirements not traceable to an approved ID or standing invariant; edit canonical files; alter the spec after Tony approval without re-approval |
| **Cody** | QA executor (under the QA Lead) | Extract the contract into a matrix; verify each AC at the recorded SHA; record findings with evidence; retest | Edit canonical files, MANIFEST, CHANGELOG, `_ARCHIVE/`, the map, or the spec; propose doctrine wording; read Claudy's session context |
| **Jarvis** | Architect | Part 1: author the Correction Package. Part 2: **[NEEDS-TONY-DECISION]** none / map reviewer / preservation-constraint author | Own the map (it is Claudy's) |

**Challenges to the mission's authority model, and outcomes:**

- *Sol derives acceptance criteria.* Doctrine says the acceptance spec is "the contract from Engineering to QA... never the QA test plan," seeded by Architect/Operator and finalized by the Engineer (`SFP` §2.5.2, `BIM` §8) [FACT]. Having QA author the spec inverts that. **Outcome [REC]:** acceptable for the sync campaign **only under a derivation rule**: every AC must cite an approved correction/intake ID, an approved UPDATE MAP row, or a standing campaign invariant (the fixed list in §8). Sol may not introduce requirements. Claudy must not author it (he would write his own exam, `BIM` §8 line 120). Tony's approval makes it "Operator-defined" in the doctrinal sense. The alternative (Tony or Jarvis authors, Sol reviews) is listed as decision 8.
- *Claudy produces "no-change" dispositions.* That is adjudication-adjacent. **Outcome [REC]:** Claudy may PROPOSE `NO-CHANGE` with evidence (the rule is already true at path:line); it is valid only once Tony approves the map row. A correction Claudy believes is wrong or conflicts with another is dispositioned `CONFLICT → BLOCKED`, never `NO-CHANGE`.
- *Cody findings go straight to Claudy.* `BUG_FIX` §3 line 81 and `BIM` §9: findings reach the Engineer "only as approved module content; rejected findings never land on the Engineer's desk." **Outcome [REC]:** in-scope acceptance failures (an AC not met) route to Claudy directly, as doctrine allows ("an in-scope acceptance failure needs no one's permission to be a FAIL"). Anything else (scope expansion, conflict, new doctrine question) routes to Tony via Sol.
- *No post-QA Astra review.* Agreed. Gate Q plus Tony's PR review is the control.
- *Two Tony approvals before edits (map, then spec).* Kept for the large path because the spec adds campaign invariants the map does not carry. Merged into one approval on the tiny path (§19).

## 3. INTAKE MODEL

Extends D16's three classes to the mission's list. Every cargo unit in `_INBOX/` (a file, or a folder treated as one unit) is classified aloud at Phase 1 and receives an ID. Unclassifiable remains a QUESTION.

| Class | Recognition (discovery, not Tony) | Route |
|---|---|---|
| **APPROVED CORRECTION** | A correction package: master index + domain briefs carrying confirmed problem, evidence/finding IDs, approved intent, invariants, preserve list, likely files, constraints; status APPROVED on the index | One map section per correction ID; propagation search mandatory |
| **DOCTRINE JOURNAL / LESSON** | `LESSONS*`, `*JOURNAL*`, `DOCTRINE_PROMOTION*`, `*PATCH*`, lesson entries with FLAGGED status | Pack model (existing D16 PACK) — entries with placements; verify placements; may be edit-level or intent-level |
| **NEW CANONICAL DOCUMENT** | No Hub counterpart by canonical name or content | Existing NEW DOC dance (header, tier, MANIFEST row, CHANGELOG, dependency map) |
| **UPDATE TO EXISTING CANONICAL DOCUMENT** | Hub counterpart exists; cargo is a full replacement | Existing SUPERSEDING DOC dance (archive, replace, version from live header) |
| **PROCESS DOCUMENT** | A doc describing Factory process that is not a tier doc (e.g., a runbook, a gate procedure) | **[NEEDS-TONY-DECISION]** tier placement rule; default: it is a canonical doc in the tier Tony names, else `_OTHERS/` as non-canonical |
| **DIAGRAM / IMAGE** | Binary or SVG asset, or a doc that embeds one | §15 |
| **SUPPORTING / NONCANONICAL ASSET** | Reference material, examples, run records, reports | `_AUDIT/` or `_OTHERS/`; no header, no MANIFEST row, no CHANGELOG line; noted in the map |
| **ARCHIVE / HISTORICAL MATERIAL** | Explicitly marked historical, or a superseded version arriving late | `_ARCHIVE/` only if it is a versioned snapshot of a live doc; else `_AUDIT/`; never a live tier |
| **CROSS-REPO CHANGE** | Targets a path outside the Hub, or `_SKILLS/*` and `lints/` (per D16 decision) | Parked split with ID and target repo; restated at close-out |
| **NO CANONICAL CHANGE REQUIRED** | Claudy's evidence shows the intent is already true, or the item is informational | `NO-CHANGE` proposal in the map with path:line evidence; valid only when Tony approves |
| **BLOCKED / NEEDS OPERATOR DECISION** | Ambiguous class, conflicting corrections, missing referenced doc, placement that does not exist, constraint that cannot be met | `BLOCKED` row with the exact question; never guessed |

**IDs [REC]:** yes, explicit. Corrections keep the package's own IDs (whatever Part 1 mints, e.g. `CP-07`); all other cargo gets `IN-<run>-<NN>` at Gate 1. Splits and gaps get IDs too. The ID is the join key across map, spec, commits, CHANGELOG, QA report, and the ENCODED stamp (§14). Reason [INFERENCE]: the 08-05 splits are still tracked by prose ("Entry 3 → stark-frontend-first") across three session files; a Factory-wide sync will have dozens of such items.

**Intake ledger:** one table at the top of the UPDATE MAP (§7) — ID · class · source file · one-line gist · disposition · gate status. This replaces the separate "Entries in scope" and "Splits parked" tables of RIPPLE_MAP.

## 4. CORRECTION PACKAGE HANDLING

How the package enters and what Claudy does with it:

1. **Whole-package intake.** The package folder (or file) is one cargo unit; each correction inside is one intake row. Claudy reads the master index first, then each brief, and reports: N corrections, their status field, the domains they name, and any brief whose required fields (problem, evidence IDs, intent, invariants, preserve list) are missing → `BLOCKED` for that ID, not for the package.
2. **Authority reading.** The package defines WHAT must become true. Claudy does not re-argue the problem or the intent. If Claudy has evidence the problem statement is factually wrong (e.g., the cited doc no longer says that), he records it under the correction ID as `CONFLICT` with evidence and moves on; Tony rules.
3. **Propagation.** For each correction: (a) start from "likely affected files" in the brief; (b) MANIFEST ← map for each; (c) **propagation search** — grep the live scope (five tier folders + MANIFEST + CHANGELOG, plus `_SKILLS/` and `_OTHERS/` read-only for awareness) for the rule's key terms: the old wording, the retired term, role/gate/module/artifact names touched, section titles cited, file names cited; (d) disposition every hit: `CHANGE` (goes on the touch list) / `CONSISTENT` (already agrees, path:line) / `HISTORY` (Version History or CHANGELOG, exempt) / `OUT-OF-SCOPE` (another repo or a non-canonical file, becomes a split or a note).
4. **Drafting.** For every `CHANGE` hit, the map row carries the verified placement and the **proposed wording** (full text for new or replaced sentences; "delete lines a–b" for removals; a precise intent line only when the edit is mechanical, e.g. a rename). This is what Tony approves. D13 and D15 apply to the drafting: no invented facts, Hub header and naming law.
5. **Invariants and preserve list.** Each correction's "rules that must become true" and "behavior to preserve" become candidate ACs (Sol derives them in §8); Claudy lists them verbatim under the correction in the map so the derivation is mechanical.
6. **Cross-correction conflicts.** If two corrections' invariants collide on the same passage, the row is `CONFLICT → BLOCKED` with both IDs; Tony rules before Gate 2 closes.
7. **Status stamping.** After merge, the package index rows are stamped `ENCODED (PR #n)` / `NO-CHANGE (approved Gate 2)` / `SPLIT → <repo>` / `DEFERRED (Operator, date)`, and the package is retained in the durable folder (§18), matching the 08-04 pack precedent [FACT].

## 5. PROPOSED PHASE / STATE MACHINE

The mission's lifecycle, challenged and adjusted. Changes from the mission's draft: route decision folded into the map; an explicit handoff artifact; QA loop bounded by SHA; sweep kept as the last phase (the mission's draft ended at merge).

```
P0  ACTIVATION & DISCOVERY        (Claudy)  seat declared in the launch line; fetch, inventory, _INBOX/ scan,
                                             MANIFEST read, RECOVERY.md read, RESUME detection (D15a)
P1  INTAKE & CLASSIFICATION       (Claudy)  ledger with IDs, classes, splits, gaps, BLOCKED questions
     ⛔ GATE 1  — Tony approves scope + classification
P2  PROPAGATION ANALYSIS          (Claudy)  MANIFEST ← map + propagation search + placement verification
                                             + proposed wording + dispositions + route line  →  UPDATE MAP
     ⛔ GATE 2  — Tony approves the UPDATE MAP (incl. NO-CHANGE rows, route, and — tiny path — the QA waiver)
P3  ACCEPTANCE CONTRACT           (Sol)     derives DOCSET_SYNC_ACCEPTANCE_SPEC.md from package + ledger + map
     ⛔ GATE 3  — Tony approves the spec (large path only; skipped under a recorded waiver)
P4  EXECUTE                       (Claudy)  four-step dance per doc, lint-before-commit, one commit per doc [ID],
                                             archive fidelity check, derived-field recompute; NO PUSH
     ⛔ GATE 4  — Tony approves execution evidence → Claudy pushes (the only push)
P5  ENGINEERING → QA HANDOFF      (Claudy)  SYNC_HANDOFF.md: SHA, files, per-ID disposition, lint state, deviations
P6  QA CYCLE                      (Cody)    contract extraction → verification at SHA → findings → recommendation to Sol
     ↺ REWORK LOOP: FAIL → Claudy bounded repair (within map) → push → Cody retest at new SHA → until PASS,
       or BLOCKED → Tony; scope expansion → back to GATE 2 (map amendment)
P7  GATE Q CLOSEOUT               (Sol)     verdict, GATE_Q_REPORT.md, cleanup verified, durable package complete
     ⛔ GATE Q  — Sol issues PASS / PASS WITH FOLLOW-UP FINDINGS / PASS WITH KNOWN RISK / FAIL / BLOCKED
P8  PR & MERGE                    (Tony)    compare URL → PR → review → rebase-and-merge
P9  CLOSE-OUT SWEEP               (Claudy)  pull main, delete branch, verify merge landed, stamp ENCODED,
                                             _INBOX/ empty, tag decision, run summary, refinement notes
```

**Tiny path** = P0, P1, P2 (with waiver line), P4, GATE 4, push, P8, P9. Identical to v0.3 minus the route stop.

## 6. STOP / APPROVAL GATES

| Gate | Owner | Input | Approval means | Exit action |
|---|---|---|---|---|
| 1 Scope | Tony | Intake ledger | The IDs in scope, the splits, the BLOCKED questions answered | P2 begins |
| 2 Map | Tony | UPDATE MAP | Every row's placement + wording + disposition; NO-CHANGE rows; route line; tiny-path waiver line ("QA waived per SFP §2.5.6, Operator, date") | P3 (large) or P4 (tiny); branch may be created |
| 3 Spec | Tony | DOCSET_SYNC_ACCEPTANCE_SPEC | The AC list is the contract; frozen | P4 begins |
| 4 Push | Tony | CHANGES / DIDN'T TOUCH / CONCERNS + evidence (diff stats, lint output, archive fidelity, derived fields) | Push authorized | `git push -u origin <branch>`; SYNC_HANDOFF written; Tony launches Cody |
| Q | Sol | GATE_Q_REPORT | Verdict issued | Tony creates PR (PASS family) or loop continues (FAIL) or Tony rules (BLOCKED) |
| Merge | Tony | PR | Merged, rebase-and-merge | P9 |

Partial approvals are honored exactly (D2). Re-approval triggers (return to Gate 2): any file added to the touch list; any wording change outside an approved row; any disposition change; any new correction; any deletion beyond archive-and-replace. Silence is never approval.

**The route decision (FSR-S01):** the map carries one line — "Route: local git (standing ruling 2026-08-05)." At a clone, that line is the decision and Tony approves it with the map. Only when no clone is available does Claudy present both routes with estimates before Gate 2 (the existing decision tree, Q3 branch). D3's ownership is intact: Tony still approves; the ceremony is proportional.

## 7. UPDATE MAP SCHEMA

**RIPPLE_MAP → UPDATE_MAP: one artifact [REC].** Reasons [INFERENCE]: v0.3 already makes the ripple map "the single source of truth for Phase 4"; a second planning artifact would split that truth; the ripple analysis remains an *activity* whose output is a section of the map. RIPPLE_MAP's tables all survive inside the new schema.

Minimum useful schema (one file per run, `UPDATE_MAP.md`):

```
# UPDATE MAP — <run slug> — <date>
Run ID · Branch · Base SHA · Route line · Path: TINY (waiver) | LARGE
Status: DRAFT | APPROVED (Gate 2, date) | AMENDED-vN (Gate 2, date)

## A. Intake ledger
| ID | Class | Source artifact | Gist | Disposition (CHANGE / NO-CHANGE / SPLIT / BLOCKED / DEFERRED) | Gate |

## B. Per-ID sections (one per correction or intake item)
### <ID> — <title>
- Approved intent (verbatim from package)            [CLAIM: package]
- Invariants / must-become-true (verbatim)           → AC candidates
- Preserve (verbatim)                                → AC candidates
- Propagation search: terms searched · scope · hit count · hits table:
  | Path:line | Hit | Disposition (CHANGE / CONSISTENT / HISTORY / OUT-OF-SCOPE) | Evidence label |
- Touch list rows (see C) that implement this ID
- NO-CHANGE evidence (if proposed)
- Open questions / CONFLICT (→ BLOCKED)

## C. Touch list (execute lightest ← first)
| # | Doc (canonical) | ← count | Placement (VERIFIED against live structure) | Proposed wording / edit | IDs | New version | Archive? | Structural (rename/move/new)? |

## D. New canonical files            | File | Tier | Header | MANIFEST row | Pairs-with | IDs |
## E. Stale / superseded material    | Path | Action (archive / delete-with-approval / mark historical) | IDs |
## F. Dependents checked, unchanged  | Doc | Why checked (dependent example / checklist / template / quick ref / role instruction) | Verdict CONSISTENT + path:line |
## G. Infra & indexes                | MANIFEST rows · live-doc count (computed) · ← map recompute · appendix · CHANGELOG rows · README/index files |
## H. Links, paths, assets           | Reference | Resolves at base? | Resolves after? | IDs |
## I. Skill references               | Skill file | Reference to a doc/section being changed | Disposition (in-scope? per D16 decision) |
## J. Cross-repo / parked            | ID | Target repo / path | Why parked |
## K. Unresolved Operator decisions  | ID | Question | Blocking what |
## L. Preservation constraints       | Constraint (verbatim) | Where it lives | How QA will check |
## M. Expected validation            | Lints (4) expected state · pre-existing straggler baseline (count + paths) · grep gates to re-run · derived-field assertions |
## N. Write-load tally + commit plan | one commit per doc, message template `docs(<doc>): v<X.Y> - <summary> [<IDs>]`
## O. Approval                       | Gate 2 APPROVED by Operator at <time> · amendments log |
```

Everything the mission's list asked for maps onto A–O. What was deliberately left out: per-row time estimates (only needed for the MCP exception), separate "checklists/templates/quick references/role instructions" tables (they are rows in F with the reason column stating which kind), and any narrative rationale (belongs in the CLI narration, not the artifact).

## 8. DOCSET_SYNC_ACCEPTANCE_SPEC LIFECYCLE

**Where it enters:** after Gate 2, before Gate 3 (P3). It cannot exist earlier because ACs for propagation depend on the approved map; it must exist before execution so Claudy is not tested against criteria written after the fact (`BIM` §8: "never reverse-engineered afterward").

**Author:** Sol (QA Lead). **Approver:** Tony (Gate 3). **Consumers:** Cody (verification), Claudy (knows the bar, may not edit), Sol (Gate Q). **Maintainer:** Sol, but frozen after Gate 3; any change re-enters Gate 3. **Home:** the durable run folder (§18); it rides the branch so QA state survives session death.

**Derivation rule (the authority guard):** each AC carries a "Derived from" field: a correction ID's invariant or preserve line, an intake ID's disposition, a map row, or one of the standing invariants below. An AC with no derivation is invalid. Sol may split or merge but not invent.

**Standing campaign invariants (the fixed list, candidates from the mission's 15, refined):**

| AC family | Requirement | Mission item(s) | Change from mission list |
|---|---|---|---|
| **AC-T (traceability)** | Every ledger ID has exactly one final disposition: ENCODED (with hunks), NO-CHANGE (Tony-approved), SPLIT (repo named), DEFERRED/BLOCKED (Tony ruling cited). Every changed canonical file cites at least one ID in its Version History row and commit. | 1, 2, 10 | Merged into one family; "explicitly approved" is checked by the map's approval log |
| **AC-S (scope)** | Diff scope equals map scope: every changed path is a touch-list or infra row; within changed files, every hunk maps to an approved row; no other file changed. Pre-existing lint stragglers: same count, same paths. | 3, 14 | 14 ("regression review") made concrete: for docs, regression = scope equality + preservation checks + straggler equality |
| **AC-P (preservation)** | Every "preserve" statement from the package is still present at the cited location. | 14 | New explicit form |
| **AC-C (consistency)** | For each modified rule, the dependents listed in map §F were checked and either changed or recorded CONSISTENT with path:line; the propagation searches re-run at the candidate SHA return zero undispositioned hits; no active guidance within the approved scope contradicts the approved intent. | 4, 5, 20 | 4 and 5 kept separate as two checks inside one family; "search terms are part of the contract" |
| **AC-R (references)** | Backtick file names, folder paths, section citations, and image/diagram links in changed files resolve on disk; assets referenced exist at canonical paths; no orphaned new asset. | 6, 9 | Merged |
| **AC-N (naming)** | Role, module, gate, lifecycle, artifact names in changed files match the campaign's canonical term list; retired terms absent outside history sections. | 7 | Term list supplied by the package or Tony; applied as grep |
| **AC-I (indexes)** | MANIFEST rows equal headers (version/date/status); live-doc count equals disk; ← map recomputed; CHANGELOG has one row per bumped doc with IDs; README/index files updated where the map says so. | 8 | Adds derived-field equality (the 29-vs-31 case) |
| **AC-A (archive)** | Each bumped doc has an `_ARCHIVE/` copy byte-equal to `git show <base>:<path>`, suffixed from that copy's own header; new docs have none; header bumped; Version History row present in the doc's own ordering. | (implicit in 14) | New; closes AP-6 mechanically |
| **AC-L (lint)** | `lints/run_all.py` at the candidate SHA: zero new findings; pre-existing findings listed and unchanged; no exemptions added. | 11 | Kept |
| **AC-H (hygiene)** | One commit per doc; messages carry IDs; no Co-Authored-By; no push before Gate 4; `_INBOX/` dispositioned; no debris in the branch (per §18 list); working tree clean at handoff. | 13, 15 | Merged; adds the commit rules from the pending refinements |
| **Precondition (not an AC)** | Candidate SHA recorded in SYNC_HANDOFF and matches `origin/<branch>`; else BLOCKED. | 12 | Reclassified: a missing SHA blocks QA rather than failing it |

Removed nothing outright; items 12, 13, 15 changed kind. Added AC-A and AC-P because they are the two things a docs sync can silently get wrong that no lint catches.

**Format:** the Factory's `AC1, AC2, …` numbering (`SFP` §2.5.3) with a family tag in the title, and a gates↔AC mapping to the map rows. Filename exact: `DOCSET_SYNC_ACCEPTANCE_SPEC.md`.

## 9. ENGINEERING EXECUTION MODEL

Unchanged in mechanics (D7 four-step dance, one commit per doc, lightest ← first, D14 minimal diff), with these additions (all field-validated or closing a review finding):

- **Branch:** `docs/sync-<slug>-<date>` off pulled main, created only after Gate 2/3 (D2).
- **Per-doc checklist before commit:** archive copy → edit per approved row(s) EXACTLY → header bump + Version History row in the doc's own order citing IDs → MANIFEST row from the header → CHANGELOG row with IDs → `py lints/run_all.py` (or the platform's Python; the 08-10 rig needed `py`) → archive fidelity check `git show <base>:<path>` vs archive → commit `docs(<doc>): v<X.Y> - <summary> [<IDs>]` (plain hyphens; no Co-Authored-By).
- **After the last doc:** recompute live-doc count and the ← map from disk; write CHANGELOG rows in the exact row format; record straggler baseline.
- **Unexplained working-tree changes are a STOP** (08-10 note 4): inventory, evidence, Operator ruling; intentional deletions become named housekeeping commits.
- **Writable surface (D10, restated):** files on the approved touch list, approved new files, `MANIFEST.md`, `CHANGELOG.md`, `_ARCHIVE/` additions, the durable run folder, RECOVERY.md and the session file. Nothing else.
- **No push in P4.** The only push is the Gate 4 exit action (FSR-D01).

## 10. ENGINEERING → QA HANDOFF

Doctrine: the handoff is a claim package (`QA_PLAYBOOK` §6). Artifact: `SYNC_HANDOFF.md` in the durable folder, committed on the branch, pushed with it.

Contents (minimum): run ID · branch · **candidate SHA** · base SHA · files changed with old→new versions · per-ID disposition table (mirrors ledger) · lint output verbatim with straggler baseline · archive fidelity results · derived-field values · deviations from the map (must be none, or an amendment reference) · known limitations · what Claudy did NOT verify.

Sequence: Gate 4 approved → push → handoff written and pushed (one more commit, `chore(sync): handoff <SHA>` — or included in the same push if written before) → Claudy stops → Tony launches Cody in a fresh session with the launch line for the QA seat. Claudy makes no further commits until a finding is routed to him.

## 11. CODY QA / REWORK / RETEST LOOP

Cody's inputs, and only these: the approved Correction Package, the approved UPDATE MAP, the approved spec, SYNC_HANDOFF, the branch at the recorded SHA, the Hub clone. Not Claudy's session file, not the CLI transcript, not the map's drafting rationale beyond what the map states.

**Cycle n:**
1. **Contract extraction** (`QA_PLAYBOOK` §9 stage 2): matrix `| AC | Check | Method (grep / diff / script / read) | Result | Evidence |`, written to the durable folder as `QA_MATRIX.md` (or inside GATE_Q_REPORT for small runs).
2. **Precondition:** `git rev-parse origin/<branch>` equals the handoff SHA; else BLOCKED.
3. **Verify** every AC at that SHA. Mechanical checks are commands whose output is pasted (lint run, diff scope `git diff --stat <base>..<sha>`, archive fidelity, propagation greps, reference resolution, derived-field recount). Judgment checks (consistency, preservation) cite path:line.
4. **Classify** each observation with the Factory classes: Acceptance Failure / Regression / Pre-Existing / Follow-Up Finding / Observation (`QA_PLAYBOOK` §9 stage 7). No "environment" class applies; "pre-existing" covers the straggler set and anything provable at base SHA.
5. **Record findings** `QA-F<nn>` with the §17 defect standard (ID, AC, severity, exact location, expected, actual, evidence, retest requirement).
6. **Recommend** to Sol: PASS / PASS WITH FOLLOW-UP FINDINGS / FAIL / BLOCKED with the matrix. Cody does not issue the verdict; Sol does (`QA_PLAYBOOK` §4: QA Lead "issues Gate Q").

**Rework (on FAIL):**
- Sol routes in-scope acceptance failures to Claudy as a finding list (no adjudication needed); routes anything requiring a scope, wording, or doctrine decision to Tony.
- **Claudy may change:** only files already on the approved touch list, only to satisfy the cited finding, keeping every other approved row intact. Each repair is a commit `docs(<doc>): v<X.Y> - repair QA-F<nn> [<IDs>]` (version bumps only if the doc's content changed after its prior bump in this run — [REC] no second bump within one unmerged run; the Version History row is amended).
- **Scope expansion** = any of: a file not on the touch list; wording outside an approved row's placement; a new ID; a changed disposition; a deletion. It returns the run to Gate 2 as `UPDATE_MAP` amendment vN (Tony approves), then Gate 3 if ACs change.
- **Claudy pushes** the repair after presenting the repair summary (Gate 4 does not repeat; Tony's Gate 4 approval covers the branch, and the QA loop is the control). Handoff appended with the new SHA.
- **Cody retests** the failed ACs plus AC-S, AC-L, AC-H (the scope/lint/hygiene families are always re-run because a repair can break them). Cycle count and SHAs are logged.
- **Loop bound [REC]:** three FAIL cycles on the same AC escalate to Tony as BLOCKED (something in the map or spec is wrong, not the execution).

**BLOCKED, not FAIL, when:** SHA mismatch or unpushed work; an AC is ambiguous or untestable; a referenced intake artifact is missing; the lint runner cannot execute on the QA rig; a Tony decision listed in map §K is unresolved; two corrections conflict; Cody would need to modify a canonical file to proceed.

**Cody may modify:** `QA_MATRIX.md`, `GATE_Q_REPORT.md` draft, findings, and its own session file. **Cody must not modify:** any live doc, `MANIFEST.md`, `CHANGELOG.md`, `_ARCHIVE/`, `_INBOX/`, the map, the spec, the handoff, lints, CI, or branch history (no rebase, no amend, no force).

## 12. SOL GATE Q / CLOSEOUT

Sol: reviews the matrix and findings for evidence sufficiency (findings without evidence are returned unread, `BIM` §9 line 140), confirms classification, checks the cleanup list (§18) at the final SHA, and issues the verdict in Factory vocabulary. `GATE_Q_REPORT.md` follows the `QA_PLAYBOOK` §22 template minus the deployment sections (Gate D: N/A — documentation-only; reason recorded), plus: tested SHAs per cycle, the final AC matrix, findings with routing, pre-existing set, and the closeout checklist. Sol signs; Tony's approval line stays empty until merge.

PASS WITH FOLLOW-UP FINDINGS is expected to be common: things Cody notices outside the approved scope (a stale example in an untouched doc) are routed as future intake, not fixed (`QA_PLAYBOOK` §10 scope protection).

## 13. TONY PR / MERGE RESPONSIBILITY

Unchanged from v0.3 in mechanics: compare URL → Create pull request → review → **rebase-and-merge** (per-doc history preserved). Additions: the PR description is drafted by Claudy after Gate Q and includes the Gate Q verdict, the IDs encoded, splits, NO-CHANGE rows, lint status with stragglers named, and the durable folder path. Tony merges only on a PASS-family verdict or with a written acceptance of a KNOWN RISK. CI red from the 9 stragglers does not block, as today.

## 14. TRACEABILITY MODEL

The Hub already has three hooks [FACT]: commit messages carry `[<origin>]`, CHANGELOG's last column is "finding/lesson IDs", packs are stamped ENCODED with the PR number. vNext uses them and adds two.

| Stage | Where the ID appears | Who writes it |
|---|---|---|
| Intake | Ledger row (map §A) | Claudy |
| Map | Every touch-list row and hit table | Claudy |
| Spec | "Derived from" on every AC | Sol |
| Commit | `[<IDs>]` suffix | Claudy |
| Doc | Version History row text | Claudy |
| CHANGELOG | last column | Claudy |
| Handoff | per-ID disposition table | Claudy |
| QA | matrix rows and findings cite AC and ID | Cody |
| Gate Q report | final per-ID disposition | Sol |
| Package / cargo | ENCODED (PR #n) stamp | Claudy at sweep |
| Splits | ID + target repo, restated in the run summary and RECOVERY.md | Claudy |

A run is traceable when `grep -r "<ID>"` over the durable folder, the branch's commit log, CHANGELOG, and the changed docs' Version History rows returns the full chain. Cody runs exactly that grep for AC-T.

## 15. IMAGE / DIAGRAM HANDLING

[FACT] No image files and no markdown image references exist anywhere in the Hub today. Everything below is forward design; keep it small until the first image arrives.

- **Canonical location [NEEDS-TONY-DECISION, low stakes]:** recommend one folder per tier, `0N_<TIER>/_assets/`, with canonical names (no version suffix) — mirrors the live-doc law. Alternative: a single root `_ASSETS/`.
- **Versioning:** images have no header block. On replacement, the outgoing file is copied to `_ARCHIVE/` as `<NAME>_<YYYY-MM-DD>.<ext>` (date, not version, because there is no header to read). MANIFEST gets an "Assets" table: name · path · referenced by · date.
- **Validation (AC-R):** every `![...](path)` and every HTML `<img src>` in live scope resolves to a file; every file in an assets folder is referenced by at least one live doc (orphan check); paths are relative and case-exact (Linux CI). Lints do not cover this [FACT]; it runs as a Cody grep gate now and becomes a fifth lint in a separate infra PR if Tony wants it.
- **Source files** (draw.io, Mermaid text, Excalidraw) are supporting assets: they ride next to the rendered image, are named identically with the source extension, and are not referenced from doctrine.
- **Diagrams as text** (ASCII or Mermaid inside a doc) are doc content, not assets; nothing changes.

## 16. CROSS-REPO HANDLING

Unchanged in principle (park with target repo, restate at close-out), with: an ID per split; a `SPLIT` disposition in the ledger and Gate Q report; the split's approved intent copied verbatim into the run summary so the receiving repo's run does not re-derive it; RECOVERY.md's parked list keyed by ID. In-repo but out-of-scope targets (`_SKILLS/*`, `lints/`, CI) are handled the same way pending the D16 decision — they are "cross-boundary," not cross-repo, but the mechanism is identical.

## 17. INTERRUPTION / RECOVERY

D15a stays and gains three things:

1. **Read RECOVERY.md and the day's session file first**, then verify against git (`git branch -a`, `git log`, `git status`, `_INBOX/`, `_ARCHIVE/` additions, the durable folder). Disk wins on disagreement.
2. **Phase-aware resume points.** The durable folder tells the truth: no map → resume P1; map DRAFT → P2; map APPROVED, no spec → P3; spec APPROVED, commits on branch but no handoff → P4 (inventory per touch-list row, DONE/NOT DONE with evidence); handoff present → P6 (Cody resumes from the last recorded matrix row at the same SHA); GATE_Q_REPORT with verdict → P8/P9.
3. **QA-seat resume.** A dead Cody session re-verifies the SHA precondition, then continues the matrix; already-recorded PASS rows are re-run only if the SHA changed.
4. **Adopt-or-abandon** the half-done branch remains Tony's explicit call (D15a step 4). The map, not the branch, is the truth.

## 18. CLEANUP / DURABLE ARTIFACTS

**Durable (rides the PR, one folder per run):** `_AUDIT/SYNC_<YYYY-MM-DD>_<slug>/` containing `UPDATE_MAP.md` (approved, with amendment log), `DOCSET_SYNC_ACCEPTANCE_SPEC.md` (large path) or the waiver line inside the map (tiny path), `SYNC_HANDOFF.md`, `QA_MATRIX.md` + findings, `GATE_Q_REPORT.md`, the intake package as received with status stamps, and the run summary. [NEEDS-TONY-DECISION] on `_AUDIT/` vs a new folder; `_AUDIT/` is recommended because it is lint-exempt by scope [FACT: `lints/lint_common.py` line 4] and already holds the 08-04 pack and 08-10 finalization report.

**Debris (removed before Gate Q closeout, verified by Sol at the final SHA):** per-cycle scratch files; duplicate copies of the durable artifacts under `agent_docs/RESPONSES/` (the RESPONSES protocol may still log them during the run; the sweep deletes the duplicates in a named housekeeping commit, matching the 08-10 ruling); temporary grep output files; abandoned branches (local and remote); `_INBOX/` contents (landed, parked, or returned); any `__pycache__` outside `lints/.gitignore` scope; editor backups.

**Session files and RECOVERY.md** remain outside the durable folder (repo root, per the repo `CLAUDE.md`), committed in the housekeeping commit as today.

## 19. TINY-CHANGE FAST PATH VS LARGE-SYNC PATH

| Aspect | TINY (e.g. one lesson into one doc) | LARGE (Factory-wide correction sync) |
|---|---|---|
| Trigger | Ledger ≤ 3 IDs, ≤ 3 touch-list docs, no new docs, no term changes, no cross-correction dependencies | Anything else, or Tony says so |
| Map | Full schema, short (most sections "none") | Full schema |
| Route | Line in map | Line in map (ceremony only without a clone) |
| QA | **Recorded Operator waiver at Gate 2** (SFP §2.5.6 permits for docs-only); Claudy's Gate 4 evidence includes AC-S, AC-A, AC-L, AC-I checks run by himself | Sol spec, Cody verification, Gate Q |
| Gates | 1, 2 (+waiver), 4, merge | 1, 2, 3, 4, Q, merge |
| Durable folder | Map + handoff-lite (SHA, evidence) + run summary | Full set |
| Same skill? | Yes: the path is a field in the map, chosen at Gate 1 by rule, overridable by Tony | Yes |

The tiny path is v0.3's proven flow with the route stop folded in and a waiver line added. It must not grow ceremony; if it does, the fast path has failed.

## 20. PROPOSED STAGE-B SKILL CHANGES

**Shape [REC]: family skill** `_SKILLS/DOCSET_SYNC_SKILLS/` with one `CLAUDE.md` and two children: `docset-sync-engineer/` (Claudy: P0–P5, P9) and `docset-sync-qa/` (Cody/Sol: P6–P7). Basis: Skills Playbook §6 family criteria fit exactly — distinct activation contexts (different sessions, different seats), a phase re-run independently (retest), and one CLAUDE.md preventing doctrine drift between seats; Cody's SKILL.md then contains no execution mechanics he must not use. **Fallback if Tony prefers not to rename:** single skill `factory-docs-update` with a seat line in the launch prompt and a `workflow/` folder split by seat; smaller migration, weaker isolation. **[NEEDS-TONY-DECISION 1.]**

**Files to modify (either shape):**
- `CLAUDE.md`: D5 carve-out with provenance (FSR-D02); D7 gains lint-before-commit, single-line header law, Version History ordering rule, archive fidelity, derived-field recompute; D10 writable surface incl. durable folder; D11 durable/debris definition; D15a + RECOVERY.md and phase-aware resume; D16 taxonomy extended (§3); new D17 "Authority: package defines WHAT, Claudy proposes WHERE/HOW, Tony approves, QA verifies"; new D18 "One push, after Gate 4"; new D19 "Commit hygiene: IDs, no Co-Authored-By, hyphens"; §2 activation gains the seat declaration and fetch-not-pull; §3 folder tree updated; Version History row.
- `SKILL.md` (engineer): Phase 1 ledger + IDs; Phase 2 becomes Propagation Analysis → UPDATE MAP with the search step and drafting; Phase 3 route folded (exception-only ceremony); Phase 4 push removed, per-doc checklist inserted; new Phase 5 handoff; Phase 6/9 sweep gains ENCODED stamping by ID, merge verification, PR-number discovery, tag decision, debris removal; worked example updated to a correction-package run; anti-patterns 9–12 (drafting in Phase 4; adjudicating a correction; pushing before Gate 4; repairing outside the map).
- `README.md`: two launch lines (engineer, QA seat), the tiny/large rule, the waiver sentence, `_INBOX/` package-folder note, line 87 fix.
- `references/ANTI_PATTERNS.md`: AP-11 root→`_INBOX/`; AP-12 derived-field drift (the 29/31 case); AP-13 self-certification on a large sync; AP-14 QA writing doctrine via ACs.
- `references/TOOL_ROUTING.md`: push line moved under "after Gate 4"; header notes it is the exception reference.
- `decision-trees/route-selection.md`: entry condition "only when no clone"; otherwise "route line in map."
- `templates/RIPPLE_MAP.md` → renamed/rewritten as `templates/UPDATE_MAP.md` (schema §7).
- `templates/LESSONS_LEARNED.md`: lines 8–9 root→`_INBOX/`; Status gains `SPLIT` and `NO-CHANGE`.

**Genuinely necessary new files:**
- `templates/DOCSET_SYNC_ACCEPTANCE_SPEC.md` (AC families §8, derivation field, gates↔AC map).
- `templates/SYNC_HANDOFF.md` (§10).
- `templates/GATE_Q_REPORT.md` (docs-only variant of QA_PLAYBOOK §22) — or reference the playbook template and add only the sync-specific sections, to avoid forking doctrine (Skills Playbook §14 Exemplar 3: "keep the doc as the single source"). [REC] the latter: a short overlay template.
- `docset-sync-qa/SKILL.md` (family shape) or `workflow/06-qa-cycle.md` (single shape).
- `decision-trees/intake-classification.md` (the §3 table as a tree) — optional; the table may suffice inside SKILL.md.
- `examples/factory-module-doctrine-2026-08-10/` (FSR-S14) — a copy of the run's map, session extract, and summary; Playbook §15 step 10.

**Removable / consolidated:** none deleted. `RIPPLE_MAP.md` is superseded by `UPDATE_MAP.md` (keep the old file one version as a pointer or delete after Tony confirms). The "Location variants" block in CLAUDE.md §2 shrinks to two lines (FSR-D18).

**Playbook compliance checks for Stage B:** two-file core per skill or family; single CLAUDE.md; SKILL.md under 500 lines each (the engineer SKILL.md is at 174 and will grow; if it passes ~400, move phase detail to `workflow/NN-*.md`); frontmatter `name` equals folder; Version History rows in both files; no pre-created empty folders; the operator launch line remains one sentence plus optional scope; Operator Override protocol retained. **Change that would violate the Playbook if done carelessly:** a per-child CLAUDE.md in the family shape (Anti-Pattern 4) — must not be created.

## 21. MIGRATION PATH FROM v0.2

1. **v0.4-DRAFT (Stage B):** encode the twelve pending refinements + the review's D01, D03, D08, D09, D12, D13, D17, D18 fixes into the existing single skill. No shape change. This alone makes v0.3's tiny path fully executable from the text.
2. **v0.5-DRAFT:** intake taxonomy + IDs + UPDATE_MAP template + propagation search + drafting rule + push contract (D04, D06, D07, S03, S05, S06). Still one seat. Run one tiny lesson through it as the validation run.
3. **v0.6-DRAFT / family split:** QA seat (spec, handoff, Cody loop, Gate Q, durable folder, debris) — the shape decision applies here. Validate on the first Part-2 domain brief (a bounded large run), then promote toward v1.0 after a full Correction Package sync.
4. **Carry-forward:** every run before v1.0 stays a test of the skill (existing rule); refinements batch into the next version with Version History rows.

If Stage B time is short, steps 1 and 2 can land together; step 3 must not land untested.

## 22. DONE LOOKS LIKE FOR THE EVENTUAL SKILL REWRITE

- A fresh session given only the launch line classifies a Correction Package folder in `_INBOX/` without asking Tony what it is.
- The UPDATE MAP for a three-correction brief shows, for every correction, the search terms, every hit with a disposition, the proposed wording, and at least one CONSISTENT dependent — and Tony can approve it by listening.
- Gate 4 evidence includes archive fidelity, derived-field equality, lint output with the straggler baseline, and no push has occurred.
- Cody, in a fresh session with only the spec, handoff, map, package, and SHA, produces a matrix where every AC has a command or path:line, and finds a seeded defect (a deliberately unpropagated hit) — the acceptance test for AC-C.
- One FAIL → repair → retest cycle completes with only touch-list files changed, two SHAs logged, and Gate Q PASS issued by Sol.
- After merge and sweep: `_INBOX/` empty, one `_AUDIT/SYNC_*/` folder, no RESPONSES duplicates, every ID grep-traceable end to end, MANIFEST count equals disk, RECOVERY.md points at the next step.
- The same skill runs a one-line lesson into one doc with four Tony touchpoints and a recorded waiver, in about the time v0.3 takes today.
- Both skill files carry Version History rows for every change; `examples/` holds at least one validated run; the Skills Playbook checks in §20 all pass.

---

## CONSOLIDATED: UNKNOWN / NEEDS-TONY-DECISION

**UNKNOWN:** MCP availability or desire (irrelevant on the primary route) · whether Sol and Cody are separate model sessions · the Correction Package's physical layout.

**NEEDS-TONY-DECISION:**
1. Skill shape: family (recommended) or single with seat switch.
2. Skill type label and the explicit git-ownership carve-out.
3. Jarvis's seat in Part 2 (proposal assumes none beyond authoring the package).
4. Whether `_SKILLS/*` (other than this skill) and `lints/` are writable in Part 2 (proposal: no; park with IDs).
5. Durable folder location (`_AUDIT/SYNC_<date>_<slug>/` recommended).
6. Whether close-out cuts the first `doctrine-YYYY.MM` tag.
7. Infra-doc versioning rule for MANIFEST/CHANGELOG (Date bump only, never archived, recommended).
8. Spec authorship: Sol under the derivation rule (recommended) or Tony/Jarvis with Sol reviewing.
9. Asset folder convention when the first image arrives (per-tier `_assets/` recommended).
10. PROCESS DOCUMENT tier placement rule.

---
*Stage A proposal. No skill file, doctrine file, or existing file was modified. Stage B not begun.*
