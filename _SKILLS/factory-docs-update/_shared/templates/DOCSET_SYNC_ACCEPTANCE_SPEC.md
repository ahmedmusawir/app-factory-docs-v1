# DOCSET_SYNC_ACCEPTANCE_SPEC — <run slug> — <YYYY-MM-DD>

> **The QA contract for a LARGE synchronization run.** Authored by **Sol (QA Lead)** after Gate 2 under the **derivation-only rule** (D20): every AC below names its source — an approved Correction / Intake ID, an approved UPDATE MAP row, or a standing invariant family in `_shared/references/STANDING_INVARIANTS.md`. Sol transforms approved intent into testable criteria; Sol does NOT invent doctrine requirements. Approved by **Tony at Gate 3**; FROZEN thereafter — any material change re-enters Gate 3. Consumed by **Cody** (verification at `QA_START_SHA`), by **Claudy** (read-only — the bar he is measured against; he may not edit it), and by **Sol** (Gate Q). Lives at `_AUDIT/SYNC_<YYYY-MM-DD>_<slug>/DOCSET_SYNC_ACCEPTANCE_SPEC.md`. Not a QA test plan: HOW each AC is attacked is Cody's matrix.

## 0. Header

| Field | Value |
|---|---|
| Run ID | `SYNC_<YYYY-MM-DD>_<slug>` |
| Derived from | UPDATE_MAP status `APPROVED (Gate 2, <date/time>)` at `<path>`; approved package `<path>`; STANDING_INVARIANTS.md (skill v0.7) |
| Author (Sol) | `<session / date>` |
| Status | DRAFT → APPROVED (Gate 3, Operator, `<date/time>`) → FROZEN · Amendments: `<none / AMENDED-v1 re-approved <date/time>>` |
| Verdict vocabulary | PASS / PASS WITH FOLLOW-UP FINDINGS / PASS WITH KNOWN RISK / FAIL / BLOCKED (Factory QA vocabulary; no other) |

## 1. Objective and scope

- **Objective:** prove that the candidate branch makes every approved intake item true in the DocSet, changes nothing else, and leaves the Hub's indexes, archives, references, lints, and working tree in the approved state.
- **In scope:** the IDs in UPDATE_MAP §A with disposition CHANGE or NO-CHANGE; the touch list §C; new files §D; infra §G; assets §H; preservation §L.
- **Explicitly out of scope (QA will not use these to fail the run):** items dispositioned SPLIT / DEFERRED / BLOCKED (listed by ID); pre-existing lint findings in the recorded baseline; baseline drift recorded in map §G (`DRIFT-…`, graded only as "unchanged"); any observation outside the approved scope — these become Follow-Up Findings, not failures (`QA_PLAYBOOK` §10 scope protection).
- **Preconditions (BLOCKED, not FAIL, if unmet):** CONTENT_SHA recorded in SYNC_HANDOFF and an ancestor of QA_START_SHA; only approved audit/handoff artifacts between them; map APPROVED and this spec APPROVED present in `<run>/` at the candidate; lint runner executes on the QA rig.

## 2. Acceptance criteria

One row per AC. Numbering `AC1, AC2, …` (Factory decision 2026-08-10); the family tag is carried in the Family column. Every row's **Derived-from** cell is mandatory and must be one of: `CP-<id> invariant <n>` · `CP-<id> preserve <n>` · `IN-<run>-<nn> disposition` · `MAP §C#<n>` / `§D` / `§F#<n>` / `§H#<n>` / `§J#<n>` / `§L#<n>` · `STANDING <family tag>`. An AC without a lawful source is invalid and must be removed before Gate 3.

| AC | Family | Requirement (testable, observable) | Derived-from | Verification expectation (evidence type Cody must produce) | Gate / phase |
|---|---|---|---|---|---|
| AC1 | AC-T | Every ledger ID `<list>` has exactly one final disposition and is grep-traceable through map, doc Version History rows, commits, CHANGELOG, handoff, and this spec | STANDING AC-T; MAP §A | `grep -rn` chain per ID; three disposition tables identical | Gate Q |
| AC2 | AC-S | Changed paths at the candidate equal MAP §C ∪ §D ∪ §E ∪ §G ∪ `<run>/**` ∪ root session/RECOVERY files; every hunk in each canonical file maps to a §C row; no canonical change after CONTENT_SHA | STANDING AC-S; MAP §C, §D, §E, §G | `git diff --name-status BASE..cand`; hunk-by-hunk read; `git diff --name-only CONTENT_SHA..QA_START_SHA` | Gate Q |
| AC3 | AC-P | Preservation constraint §L#1 "<verbatim>" is present unaltered at `<path>` | CP-<id> preserve 1; MAP §L#1 | `grep -n` / read; path:line | Gate Q |
| AC4 | AC-C | The propagation searches for `<ID>` (terms `<…>`, scope `<…>`) re-run at the candidate return zero undispositioned active hits; §F dependents `<…>` are CONSISTENT | CP-<id> invariant 1; MAP §B (<ID>) hits table; MAP §F | verbatim re-run output reconciled row-by-row against §B; §F locations read | Gate Q |
| AC5 | AC-C | The approved wording for MAP §C#<n> is present at the verified placement in `<doc>` and no active guidance in scope contradicts invariant "<verbatim>" | CP-<id> invariant 1; MAP §C#<n> | read at placement; contradiction grep | Gate Q |
| AC6 | AC-R | Every reference in MAP §H resolves case-exactly at the candidate; no orphan under `<tier>/_assets/` | STANDING AC-R; MAP §H | `test -f` / `git ls-files`; orphan cross-check | Gate Q |
| AC7 | AC-N | Terms `<canonical list>` are used and `<retired list>` are absent from live scope outside history sections | STANDING AC-N; MAP §M term lists | grep with lint-mirroring exemptions | Gate Q |
| AC8 | AC-I | MANIFEST rows equal headers for `<docs>`; derived fields this run changed are correct (live-doc count `<n>` = disk = rows, if a doc was added/removed; ← map recomputed for `<docs>`); baseline drift `<DRIFT IDs>` unchanged from BASE; CHANGELOG has `<n>` rows with IDs; MANIFEST/CHANGELOG not archived | STANDING AC-I; MAP §G | counts and header/row diffs | Gate Q |
| AC9 | AC-A | `_ARCHIVE/<NAME>_v<X_Y>.md` byte-equal to `git show BASE:<path>` for each of `<docs>`; suffix = archived header version; live header bumped once | STANDING AC-A; MAP §C archive column | `git show … \| diff -` empty; header reads | Gate Q |
| AC10 | AC-L | Lints at the candidate: zero new findings; baseline `<count>` unchanged; `lints/`, `.github/` untouched | STANDING AC-L; MAP §M baseline | lint output diffed against baseline | Gate Q |
| AC11 | AC-H | Commit shape `docs(<DOC>): v<X.Y> - … [<IDs>]`, no Co-Authored-By, one bump per doc; no push before Gate 4; `_INBOX/` dispositioned; no debris; tree clean; durable folder contains exactly the required set | STANDING AC-H; MAP §N, §O | `git log` scan; timestamps; `git status`; `ls <run>/` | Gate Q |
| AC<n> | … | (one AC per approved NO-CHANGE row: "the intent of `<ID>` is true at `<path:line>` as approved at Gate 2, and nothing was changed for it") | IN-…/CP-… NO-CHANGE; MAP §B | read; `git diff` shows no change for that ID | Gate Q |

*(Rows above are the shape. Sol instantiates one AC per approved ID-invariant, per approved preservation line, per §C row cluster, per NO-CHANGE row, and one per standing family. Sol may merge closely related IDs into one AC and may split a family into several ACs; Sol may not add a requirement with no Derived-from source.)*

## 3. Gates ↔ AC mapping

| UPDATE MAP row / gate | ACs |
|---|---|
| §C#1 … | AC… |
| §D … | AC… |
| §L#… | AC… |
| Gate 4 self-checks presented by Claudy (informational for QA; never a substitute) | AC8, AC9, AC10 |

## 4. Regression expectations

- Pre-existing lint baseline: `<count>` findings at `<paths>` — must be unchanged, never "fixed" by this run.
- Every doc NOT on the touch list: byte-identical to BASE_SHA (`git diff --name-only BASE..cand` shows none of them).
- Mandatory regression families on every retest cycle: AC-S, AC-L, AC-H (+ AC-A if an archive was touched by a repair).

## 5. Manual-only points

`<none>` — or list the judgment reads (consistency, preservation) that cannot be reduced to a command, each with the path:line Cody must cite.

## 6. Known limitations / follow-up outside this contract

- Items dispositioned SPLIT / DEFERRED / BLOCKED: `<IDs>` — not graded here.
- `<any accepted limitation, with the Operator ruling that accepted it>`

## 7. Approvals

- Sol (QA Lead), derivation complete, every AC sourced: `<date/time>`
- Tony (Operator), Gate 3 APPROVED — spec FROZEN: `<date/time>`
