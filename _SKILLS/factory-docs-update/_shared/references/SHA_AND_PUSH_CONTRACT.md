# SHA_AND_PUSH_CONTRACT.md — One Push, Recorded SHAs, No Self-Reference (D18)

> Shared reference. Claudy reads it before Gate 4 and before every repair push; Cody reads it at Stage 1 and at every retest. This file is the single executable statement of WHEN a push happens and WHICH commits QA tests. Every other file in this family defers to it. Any instruction anywhere in this family that says "push during execution" is a defect to be reported.

## The rule in one sentence

**Implementation commits stay local; the branch is pushed exactly once, after Tony's Gate 4 approval; every later push is a bounded QA-repair push; QA tests only what is on the remote and records the remote SHA itself.**

## The four recorded SHAs

| Name | Definition | Recorded by | Recorded where |
|---|---|---|---|
| **BASE_SHA** | The approved execution base: the commit the UPDATE MAP was planned and verified against, proposed from discovery (the Operator- or intake-named commit / tag / branch tip, else the clean discovered HEAD), approved at Gate 2. Never assumed to be `origin/main`. The run branch is created FROM it — or, when already on the approved run branch at BASE_SHA or a lawful descendant, reused (D18). A change after Gate 2 is a map amendment. | Claudy | UPDATE_MAP §0 (before Gate 2); SYNC_HANDOFF |
| **CONTENT_SHA** | The exact commit containing the LAST approved canonical content change of the implementation phase (the last `docs(<DOC>): …` commit). Everything after it on the branch is durable-folder metadata (handoff, intake snapshot, the Gate-4 approval record), session, RECOVERY, or response logs. | Claudy | **Authoritative:** SYNC_HANDOFF §0 (LARGE) / RUN_SUMMARY.md (TINY), written after the commit exists; later mirrored into QA_MATRIX and GATE_Q_REPORT. **Never** written into UPDATE_MAP after Gate 2 — the map is frozen and §O holds only the pre-freeze pointer "recorded in SYNC_HANDOFF §0 / RUN_SUMMARY" (TEST B). |
| **QA_START_SHA** | `git rev-parse origin/<branch>` at the moment Cody begins the first QA cycle — the actual remote tip Cody checks out. | Cody | QA_MATRIX header; GATE_Q_REPORT |
| **REPAIR_CONTENT_SHA** (per cycle n) | The last repair commit touching canonical content in rework cycle n. | Claudy | SYNC_HANDOFF "Repair cycles" appendix (written after the commit exists) |
| **QA_RETEST_SHA** (per cycle n) | `git rev-parse origin/<branch>` at the start of retest cycle n. | Cody | QA_MATRIX cycle header |

No document ever records the SHA of the commit that contains that document. A handoff that "contains its own final SHA" is impossible and is not attempted.

## Sequence — normal LARGE run

```
P4  (if the commit plan §N requires it) chore(sync): run-state checkpoint [<run-id>]   ← approved run-state set
    (map, INTAKE_SNAPSHOT/, session/recovery, response logs); tree clean before the first per-doc sequence
P4  Claudy implements: one local commit per canonical doc … last content commit = CONTENT_SHA
    Claudy records CONTENT_SHA (git rev-parse HEAD) — no push; written into SYNC_HANDOFF §0, NOT the map
P5  Claudy writes <run>/SYNC_HANDOFF.md referencing CONTENT_SHA, plus run metadata
    Claudy commits: chore(sync): handoff for CONTENT_SHA <short> [<run-id>]   ← metadata-only commit(s);
    <run>/INTAKE_SNAPSHOT/ is committed by this commit at the latest (a fresh QA workspace needs it)
⛔  GATE 4 — Tony approves publication (evidence: handoff, lints, fidelity, derived fields, diff stats)
    Claudy records the approval time in SYNC_HANDOFF §8 and commits:
      chore(sync): gate 4 approval record [<run-id>]                          ← metadata-only Gate-4 commit,
                                                                              deliberate, always after CONTENT_SHA
    → only then:  git push -u origin <branch>                                ← THE push
P6  Cody (fresh session):  git fetch; QA_START_SHA = git rev-parse origin/<branch>; git checkout QA_START_SHA
    Cody verifies:
      git merge-base --is-ancestor CONTENT_SHA QA_START_SHA                 → must succeed
      git diff --name-only CONTENT_SHA..QA_START_SHA                         → only _AUDIT/SYNC_<run>/**
                                                                              (handoff, INTAKE_SNAPSHOT/,
                                                                              the Gate-4 record), RECOVERY.md,
                                                                              session_*.md, agent_docs/RESPONSES/*
      (any 0?_*/ , MANIFEST.md, CHANGELOG.md, _ARCHIVE/ path in that diff)  → BLOCKED: unapproved change after CONTENT_SHA
      test -d <run>/INTAKE_SNAPSHOT at QA_START_SHA                          → missing → BLOCKED (intake not portable)
```

The Gate-4 approval commit is not an anomaly and not a contradiction of "CONTENT_SHA is the last content commit": it contains no canonical path, it exists so the approval is durable before publication, and Cody's post-CONTENT diff allowance names it explicitly (TEST B).

## Sequence — rework cycle n (LARGE only, after Gate 4)

```
Sol routes accepted in-scope finding(s) QA-Fnn to Claudy (bounded: cited AC, cited map row)
Claudy repairs ONLY inside approved map scope; commits docs(<DOC>): v<X.Y> - repair QA-Fnn [<IDs>]
Claudy records REPAIR_CONTENT_SHA(n) = last repair content commit
Claudy appends the cycle to <run>/SYNC_HANDOFF.md ("Repair cycles" table) and commits the metadata
Claudy announces the repair summary (CHANGES / DIDN'T TOUCH / CONCERNS) — Gate 4 does NOT repeat
Claudy pushes: git push origin <branch>                                    ← bounded repair push
Cody: git fetch; QA_RETEST_SHA(n) = git rev-parse origin/<branch>; checkout; verify ancestry as above
Cody retests the failed AC(s) + mandatory regression families AC-S, AC-L, AC-H (+ AC-A if any archive touched)
```

Scope expansion during repair (a file outside the touch list, wording outside an approved placement, a new ID, a changed disposition, a deletion) is NOT a repair: stop, return to Gate 2 as a map amendment (and Gate 3 if ACs change), then resume. Three FAIL cycles on the same AC → BLOCKED → Tony (the map or the spec is wrong, not the execution).

## Sequence — TINY run

```
P4  Claudy implements … last content commit = CONTENT_SHA; records it in RUN_SUMMARY.md (never in the frozen map)
    Claudy runs the mechanical checks of the standing invariants himself (waiver recorded at Gate 2)
    Claudy commits metadata: chore(sync): run metadata for CONTENT_SHA <short> [<run-id>]   (incl. INTAKE_SNAPSHOT/)
⛔  GATE 4 — Tony approves publication
    Claudy records the approval time in RUN_SUMMARY.md; commits: chore(sync): gate 4 approval record [<run-id>]
    → git push -u origin <branch>                                            ← THE push
P8  Tony: compare URL → PR → review → rebase-and-merge
```

There is no QA_START_SHA on TINY; the PR review is Tony's, on the pushed tip, and the run summary records the pushed tip AFTER the push (`git rev-parse origin/<branch>`), never inside a commit it describes.

## Sequence — after merge (both paths)

The Phase 9 close-out may push a separate housekeeping branch (`chore/sync-closeout-<slug>-<date>`: session file, RECOVERY.md, RESPONSES dispositions, final durable-folder stamps). It is outside the implementation contract above: it is announced to Tony before the push, it never contains canonical content (no tier doc, MANIFEST, CHANGELOG, or `_ARCHIVE/` change), and Tony merges it like any PR. It is not a repair push and needs no QA cycle.

## Forbidden

- Pushing before Gate 4 approval, for any reason ("so Tony can look at it on GitHub" is not a reason — the compare URL is produced after the push, which is after Gate 4).
- Rebasing, amending, squashing, or force-pushing any commit that a QA seat has already recorded (`QA_START_SHA` or any `QA_RETEST_SHA`). History that QA tested must remain reachable.
- A QA seat pushing anything. Cody's evidence is committed by Claudy at closeout into the durable folder, or by Cody into the durable folder only — never touching canonical files — and the branch push remains Claudy's act after Sol's Gate Q. (If Cody commits evidence locally, the commit contains only `<run>/**` and the QA session file.)
- Writing to main. Ever.

## Why

The v0.3 text listed `git push` inside the execution steps and, three lines later, asked for approval "to push." Practice held the push until Gate 4 both times; the text did not. A fresh session reading literally would have published before approval. Separately, a handoff "containing the final SHA" cannot exist, because committing the handoff moves the SHA; the CONTENT_SHA / QA_START_SHA split makes the contract executable and lets QA prove that nothing canonical moved after the content was frozen.
