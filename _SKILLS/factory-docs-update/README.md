# factory-docs-update — OPERATOR RUNBOOK

> **Skill family · v0.6-DRAFT (AWAITING INDEPENDENT VALIDATION) · Home:** `_SKILLS/factory-docs-update/` in the Doctrine Hub (`ahmedmusawir/app-factory-docs-v1`). Runs at a Hub clone.
>
> **THIS FILE IS FOR THE OPERATOR (Tony).** Read it cold after any time away and you can run a doctrine sync start to finish without a briefing. Agent doctrine lives in CLAUDE.md; methodology in the two children's SKILL.md — you never need to read those.

---

## What this skill does (30 seconds)

When approved material needs to go INTO the factory doctrine — a correction package, project lessons, a new or replacement playbook, a diagram — this family makes Claudy conduct the whole ceremony: read the cargo → classify it and give every item an ID → search the whole corpus for everything the change touches → put WHERE and HOW into one UPDATE MAP → you approve the map → he executes locally → you approve publication → he pushes → you review the PR and merge → he sweeps. On big jobs an independent QA lane (Sol, then Cody) proves the sync is complete before you merge. You approve gates and click Merge. That is your whole job.

**Standing rules baked in:** the Hub clone with local git is the execution environment (your ruling 2026-08-05) · main is PR-only, no agent ever merges · in this Hub only, Claudy runs all git and pushes exactly once after your Gate 4 word — you never type a git command (this is a Hub-only exception; app-module Engineers stay git-zero) · red CI from the recorded pre-existing lint findings does not block your merge · no doctrine release tag is cut by the skill.

**Small or large? You don't decide that up front.** Claudy inspects the cargo and the repo and routes the job himself: **TINY** (a few IDs, at most three docs, nothing new, no renames, no risky rules, clean search) runs the fast path with a recorded docs-only QA waiver; anything else is **LARGE** and gets the QA lane. He tells you the route and the evidence at Gate 2. You can always escalate to LARGE. Downgrading to TINY needs your explicit ruling, recorded.

---

## THE PROCESS — start to finish

**Step 0 — You have cargo.** An approved Correction Package (folder), a promotion pack or lessons file, a new or replacement doc, a diagram, a run record.

**Step 1 — Open a terminal at a current Hub clone.** Claudy fetches and checks distance from main himself; you run no git.

**Step 2 — Check the family is present** at `_SKILLS/factory-docs-update/` (one CLAUDE.md, `sync-engineer/`, `sync-qa/`, `_shared/`).

**Step 3 — Drop ALL cargo in `_INBOX/` at the clone root.** One folder, every run. A package goes in as its folder. You do NOT label what is what — Claudy classifies every unit aloud at Gate 1 (correction package / lesson / new doc / superseding doc / process doc / image / supporting / historical / cross-boundary / no-change / blocked) and asks only if something genuinely cannot be classified from disk.

**Step 4 — Launch Claudy.** The activation line is always the same:

    Go read _SKILLS/factory-docs-update/CLAUDE.md and follow it.

Optionally add scope rulings. Template at the bottom.

**Step 5 — Ride the gates.** He narrates aloud and STOPS at each; nothing happens without your word:

- **Gate 1 — Scope:** the intake ledger (every item with an ID and a class), parked items, blocked questions, the provisional route. Say APPROVED.
- **Gate 2 — UPDATE MAP:** the exact docs to touch, the verified placements, the proposed wording, every search hit and what it means, any NO-CHANGE proposals, the final route. On TINY he also reads you the QA-waiver line for your approval. Say APPROVED.
- **Gate 3 — Acceptance spec (LARGE only):** you launch **Sol** in a fresh session (line below); Sol derives the acceptance criteria from the approved map and package only, reads them to you. Say APPROVED. Then tell Claudy Gate 3 passed.
- **Gate 4 — Publication:** per-doc changes, lint result against the baseline, archive fidelity, index counts, the CONTENT_SHA. **Nothing has been pushed yet.** Say APPROVED; he pushes the branch once.
- **QA (LARGE only):** you launch **Cody** in a fresh session (line below). Cody verifies the pushed branch and reports to Sol; Sol routes any accepted finding back to Claudy for a bounded repair, Claudy pushes the repair, Cody retests. Sol issues **Gate Q** — PASS / PASS WITH FOLLOW-UP FINDINGS / PASS WITH KNOWN RISK / FAIL / BLOCKED. Anything BLOCKED comes to you.

**Step 6 — YOUR move: the PR and the merge.** Click the compare URL Claudy gives you → Create pull request → review → **Merge via REBASE-AND-MERGE** (doctrine law — preserves per-doc history). Squash only for trivia. On LARGE, merge only on a PASS-family verdict.

**Step 7 — Tell him it's merged.** He sweeps: syncs main, deletes the branch, stamps every intake item ENCODED with the PR number, empties `_INBOX/`, removes debris, leaves the run's durable folder in `_AUDIT/SYNC_<date>_<slug>/`, updates RECOVERY.md, delivers the run summary. Done when he says the tree is clean.

---

## Rules you occasionally need (the gotchas)

- **Claudy never judges a correction.** The approved package says what must become true; he proposes where and how; you approve. If something in the Hub contradicts an approved correction, it comes to you as BLOCKED — he does not resolve it. Jarvis is consulted only if you decide a blocked item needs him.
- **Other skills, lints, CI, other repos are read-only during a sync.** If the run finds one of them should change, Claudy parks it with an ID (`XB-…`) and a target; it gets its own approved job later.
- **Hub law beats cargo conventions.** Canonical filenames; single-line headers; versions only in headers, MANIFEST, and `_ARCHIVE/`; kit-internal references resolved on landing.
- **New docs** get the standard header, a MANIFEST row, a CHANGELOG line — in the tier that owns the subject. If ownership is unclear he asks; canonical doctrine never lands in `_OTHERS/`.
- **Images / diagrams** land in the owning tier's `_assets/` folder with a canonical name; the doc that uses one references it by relative path; replacements are archived by date.
- **MANIFEST and CHANGELOG** get their content and date updated, never archived. Their computed fields (doc count, dependency map) are recomputed every run and checked.
- **Red ❌ on CI** from the recorded pre-existing findings: merge anyway — they are named in the map and the PR. He fixes reds HIS change caused; he never touches the rest and never silences a lint.
- **A QA seat never edits doctrine.** Cody and Sol write only QA evidence in the run folder. If a QA session ever offers to "fix" a doc, that is a defect — say no.
- **Run died mid-flight?** Same first line plus: "This is a RESUME." Any seat reads RECOVERY.md and the session file for where it stopped, then checks git and disk, and re-presents from the last completed gate. A resumed Cody re-checks the branch tip before trusting any earlier PASS.
- **He may stop and ask you to re-choose the execution route** only if no clone exists (the MCP exception). At a clone there is no route question.

## What you NEVER do

Run git commands · merge from an agent session · let anyone push main directly · hand-copy doctrine between projects · let a QA session touch a doctrine file · cut a release tag from inside a run (that decision is yours, later, after a real merged sync).

---

## Launch prompt templates (copy, edit the bracketed bits, paste)

Engineer (the normal launch):

    Go read _SKILLS/factory-docs-update/CLAUDE.md and follow it.

    Intake: all cargo is in _INBOX/.
    Scope: [all of it | items X, Y only — park Z].
    [Optional: Route this LARGE regardless.]

QA Lead (LARGE, after Gate 2 — fresh session):

    Go read _SKILLS/factory-docs-update/CLAUDE.md and follow it.
    Seat: QA Lead (Sol). Run: SYNC_<date>_<slug>. Derive the acceptance spec.

QA executor (LARGE, after Gate 4 push — fresh session):

    Go read _SKILLS/factory-docs-update/CLAUDE.md and follow it.
    Seat: QA (Cody). Run: SYNC_<date>_<slug>. Verify the pushed candidate.

Resuming a dead run (any seat): same lines, plus:

    This is a RESUME — a prior session was interrupted. Inventory what landed
    and re-present from the last completed gate.

---

*Family anatomy: CLAUDE.md (the one doctrine + activation manager) · sync-engineer/ (Claudy: discovery, intake, map, execute, publish, sweep) · sync-qa/ (Sol: spec + Gate Q; Cody: verification + retest) · _shared/ (taxonomy, standing invariants, SHA/push contract, anti-patterns, map/spec/handoff templates). Authored per the App Factory Skills Playbook.*
