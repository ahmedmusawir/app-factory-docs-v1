# factory-docs-update — OPERATOR RUNBOOK

> **Stark Skill · v0.2-DRAFT · Home:** `_SKILLS/factory-docs-update/` in the Doctrine Hub
> (`ahmedmusawir/app-factory-docs-v1`). Droppable anywhere.
>
> **THIS FILE IS FOR THE OPERATOR (Tony).** Read it cold after any amount of time away
> and you can run a doctrine update start to finish without a briefing. Agent doctrine
> lives in CLAUDE.md; methodology in SKILL.md — you never need to read those.

---

## What this skill does (30 seconds)

When lessons from any project need to go INTO the factory doctrine docs, this skill makes
Claudy conduct the whole ceremony: read the lessons/patch pack → map blast radius via
MANIFEST → confirm the route with you → execute the per-doc update dance → push a branch
→ hand you a one-click PR link. You approve gates and click Merge. That's your whole job.

**Standing rules baked in:** local git is the PRIMARY route (operator ruling 2026-08-05 —
the MCP is the exception you must explicitly choose) · main is PR-only, no agent ever
merges · Claudy runs ALL git, you never type a git command · red CI from known pre-existing
findings does not block your merge.

---

## THE PROCESS — start to finish

**Step 0 — You have cargo.** An Architect handed you a doctrine promotion pack
(`DOCTRINE_PROMOTION_<date>_<name>.md`) or a project's lessons file has FLAGGED entries.

**Step 1 — Get a current Hub clone.** Fresh box: `git clone` the Hub. Existing clone:
just open a terminal there — Claudy pulls latest as part of his own discovery.
(You don't run git; being IN the folder is enough.)

**Step 2 — Check the skill is present** at `_SKILLS/factory-docs-update/`. If missing
or outdated, drop the latest skill folder in (it ships as a zip; the folder lands as-is).

**Step 3 — Drop the cargo in the clone ROOT:**
- the promotion pack file itself
- any NEW doc files the pack introduces to the Hub (e.g. a QA_PLAYBOOK the entries cite)

Claudy's intake scans the root for `DOCTRINE_PROMOTION*` and `*PATCH*` files
automatically — in the root, the cargo cannot be missed.

**Step 4 — Launch Claudy.** The activation line is always the same:

    Go read _SKILLS/factory-docs-update/CLAUDE.md and follow it.

That alone is enough — he discovers the rest. Optionally add scope rulings (which
entries are in or out this run, cross-repo splits). Template at the bottom of this file.

**Step 5 — Ride the gates.** He narrates aloud and STOPS at each; nothing happens
without your word:
- **Gate 1 — Scope:** he reports the pack/lessons found and what's in this run. Say APPROVED.
- **Gate 2 — Ripple map:** the exact docs to touch, blast radius from MANIFEST. Say APPROVED.
- **Gate 3 — Route:** he presents local git (primary) vs MCP with honest estimates.
  Your call — the standing default answer is local git.
- **Gate 4 — Diffs:** per-doc change summary + verification evidence. Say APPROVED;
  he pushes the branch and gives you the compare URL.

**Step 6 — YOUR move: the merge.** Click the compare URL → Create pull request →
review → **Merge via REBASE-AND-MERGE** (doctrine law — preserves per-doc history).
Squash only for trivia.

**Step 7 — Tell him it's merged.** He sweeps: syncs main, deletes the branch, marks
the pack/lessons ENCODED with the PR number, delivers the run summary. Done when he
says the tree is clean.

---

## Rules you occasionally need (the gotchas)

- **Cross-repo entries split out.** If a pack entry targets another repo (a skill folder,
  the starter kit), it does NOT ride this Hub run — separate mini-task and PR in that
  repo. Claudy flags these; you just confirm the split.
- **Hub law beats pack conventions.** Inside the Hub: canonical filenames only; versions
  live in headers + MANIFEST + `_ARCHIVE/` — even if the pack says otherwise.
- **New docs entering the Hub** get the standard header, a MANIFEST row, and a CHANGELOG
  line in the same PR. Claudy handles it; the files just need to be in the root (Step 3).
- **Red ❌ on CI:** if it's from pre-existing known findings, merge anyway — Claudy will
  have named them. He fixes reds HIS change caused; he never touches the rest.
- **He may stop mid-job and ask you to re-choose the route** (time overrun, repeated
  errors). Switching is normal — the ripple map, not the half-done work, is truth.

## What you NEVER do

Run git commands · merge from an agent session · let anyone push main directly ·
hand-copy doctrine between projects (everything flows through this process).

---

## Launch prompt template (copy, edit the bracketed bits, paste)

    Go read _SKILLS/factory-docs-update/CLAUDE.md and follow it.

    Intake: the lessons input is [PACK_FILENAME] in the repo root.
    Scope: [all entries | entries X,Y only — entry Z targets another repo, park it].
    New docs riding in: [none | FILE1, FILE2 — in the repo root].
    Route: local git (standing primary).
    Merge style: rebase-and-merge.

---

*Skill anatomy: CLAUDE.md (agent doctrine) · SKILL.md (phases & gates) · references/
(routing + anti-patterns) · decision-trees/ (route logic) · templates/ (lessons file,
ripple map). Authored per the App Factory Skills Playbook.*
