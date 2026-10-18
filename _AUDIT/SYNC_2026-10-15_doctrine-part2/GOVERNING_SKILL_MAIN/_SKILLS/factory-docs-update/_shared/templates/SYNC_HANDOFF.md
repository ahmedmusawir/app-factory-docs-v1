# SYNC_HANDOFF — <run slug> — <YYYY-MM-DD>

> **Engineering → QA claim package** (`QA_PLAYBOOK` §6: a handoff is claims to verify, never proof). Authored by Claudy AFTER the last approved content commit exists and BEFORE Gate 4. References **CONTENT_SHA**; never claims the SHA of the commit that will contain this file. Cody records **QA_START_SHA** independently from the remote after the Gate 4 push (`_shared/references/SHA_AND_PUSH_CONTRACT.md`). Lives at `_AUDIT/SYNC_<YYYY-MM-DD>_<slug>/SYNC_HANDOFF.md`. On the TINY path this file is not required; the equivalent fields (CONTENT_SHA, Gate 4 record, pushed tip) go in RUN_SUMMARY.md — never into the map, which is frozen at Gate 2.

## 0. Identity

| Field | Value |
|---|---|
| Run ID | `SYNC_<YYYY-MM-DD>_<slug>` |
| Branch | `<run branch>` (local; not yet pushed at the time of writing) |
| BASE_SHA | `<sha>` (approved in UPDATE_MAP §0) |
| **CONTENT_SHA** | `<sha>` = last commit containing approved canonical content (`git rev-parse HEAD` immediately after that commit; recorded before any metadata commit). **This row is the authoritative record of CONTENT_SHA** — the UPDATE MAP is frozen at Gate 2 and is never written to for it (D18). |
| Approved artifacts | UPDATE_MAP `APPROVED (Gate 2 <date/time>)` [+ `AMENDED-v<n>`]; DOCSET_SYNC_ACCEPTANCE_SPEC `APPROVED (Gate 3 <date/time>)` |
| Intake snapshot | `_AUDIT/SYNC_<run>/INTAKE_SNAPSHOT/` — committed in `<commit short SHA>` (this handoff commit at the latest); unmodified since Gate 1 (`git log --diff-filter=M -- <run>/INTAKE_SNAPSHOT` empty). Cody reads the intake from here, not from `_INBOX/`. |
| Path | LARGE |

## 1. Candidate files

| Path | Kind (canonical edit / new canonical / archive / infra / asset) | Version live → new | Contributing IDs | Commit (short SHA, subject) |
|---|---|---|---|---|
| | | | | |

## 2. Intake / correction disposition table (must equal UPDATE_MAP §A at CONTENT_SHA)

| ID | Class | Disposition (CHANGE / NO-CHANGE / SPLIT / BLOCKED / DEFERRED) | Where it landed (paths) or ruling reference |
|---|---|---|---|
| | | | |

## 3. Claims (each labeled; QA verifies every one)

- **Lints at CONTENT_SHA** — command: `<…>`; result: `<verbatim summary lines>`; new findings: `0`; baseline: `<count>` unchanged — `<paths>` [EVIDENCE: pasted output]
- **Archive fidelity** — for each archived doc (one per §C "Archive expected: YES" row): `git rev-parse <CONTENT_SHA>:_ARCHIVE/<NAME>_v<X_Y>.md` = `git rev-parse <BASE_SHA>:<path>` (same blob SHA; Git-object method, EOL-safe — never `git show … | diff -`, AP-21) [EVIDENCE per doc: both SHAs pasted]
- **MANIFEST derived fields** — fields this run changed (map §G): live-doc count on disk `<n>` = MANIFEST rows `<n>` = stated `<n>` (or: unchanged, no doc added/removed); rows for `<docs>` equal headers; ← map recomputed for `<docs>`; baseline drift `<DRIFT IDs / none>` unchanged from BASE_SHA; MANIFEST/CHANGELOG headers Date-bumped, not archived [EVIDENCE]
- **CHANGELOG** — rows added = one per bumped / new doc in §1 above (count taken from those rows), IDs in last column [EVIDENCE: lines]
- **Diff scope** — `git diff --name-status <BASE_SHA>..<CONTENT_SHA>` = `<list>`; equals map §C ∪ §D ∪ §E ∪ §G [EVIDENCE]
- **Propagation** — the §B searches were re-run by Claudy at CONTENT_SHA: `<n>` active hits, all dispositioned [CLAIM — Cody re-runs independently]
- **References / assets** — §H items resolve [CLAIM — Cody verifies]
- **Commit hygiene** — `<n>` doc commits, shape verified, no Co-Authored-By [EVIDENCE: `git log --format`]
- **Working tree** — `git status --porcelain` empty at CONTENT_SHA [EVIDENCE]

## 4. Deviations from the approved map

`NONE` — or: `<row> — <what differed> — <amendment reference AMENDED-v<n>, re-approved <date/time>>`. A deviation without an amendment reference is a defect; do not hand off.

## 5. Known limitations

- `<e.g. NO-CHANGE rows approved: IDs; parked XB items: IDs; anything the Operator accepted>`

## 6. Explicitly unverified claims (what Claudy did NOT check)

- `<e.g. consistency of §F dependents beyond the quoted lines; case-exact asset paths on a case-sensitive filesystem; …>` — QA owns these.

## 7. Repair cycles (appended per cycle, after each repair content commit exists)

| Cycle | Findings addressed (QA-F…) | REPAIR_CONTENT_SHA | Files touched (must be ⊆ approved touch list) | Repair summary (CHANGES / DIDN'T TOUCH / CONCERNS) | Pushed at |
|---|---|---|---|---|---|
| 1 | | | | | |

## 8. Gate 4 record (filled by Claudy at the moment of approval; committed BEFORE the push)

The sequence is deliberate and always the same (D18, `SHA_AND_PUSH_CONTRACT.md`): CONTENT_SHA → this handoff committed (`chore(sync): handoff for CONTENT_SHA <short> [<run-id>]`) → ⛔ Gate 4 → this section filled → **`chore(sync): gate 4 approval record [<run-id>]`** (a metadata-only commit; it is expected to sit after CONTENT_SHA and Cody's post-CONTENT diff allowance names it) → `git push -u origin <branch>` → Cody independently records QA_START_SHA.

- Gate 4 APPROVED by Operator at `<date/time>` · approval record committed as `<short SHA>` · pushed `<date/time>` · (QA_START_SHA is Cody's to record — not here)
