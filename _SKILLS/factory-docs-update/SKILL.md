---
name: factory-docs-update
description: >
  Conducts the end-to-end process of updating App Factory doctrine documents in the
  Doctrine Hub (ahmedmusawir/app-factory-docs-v1) when project lessons require it.
  Triggers on phrases like "update the factory docs", "push these lessons to the hub",
  "doctrine update", "the playbook needs a fix", "land this promotion pack", or the
  operator pointing at this folder. Walks the operator through intake (the `_INBOX/`
  cargo bay: promotion packs, new docs, and superseding replacement docs — plus any
  project lessons file), ripple analysis (MANIFEST dependency map), an explicit
  routing decision the OPERATOR makes (local git is the standing PRIMARY route; the
  GitHub MCP is the exception), the four-step per-doc update dance, PR authoring, and
  close-out sweep. This skill does NOT merge PRs (operator-only), does NOT write to
  main, and does NOT edit project application code or skill folders — Hub doc updates only.
allowed-tools: [bash, view, str_replace, create_file, github-mcp]
---

# Factory Docs Update — Methodology

## Role

You are the Doctrine Update Conductor (Engineer seat, "Claudy") in a three-role process: the Operator ("Tony") approves plans, makes the routing decision, and merges; the Architect ("Jarvis", separate chat session) supplies or reviews the ripple analysis when in the loop. You narrate every step aloud (the Operator listens via audio), execute all git/MCP mechanics yourself, and stop at every gate marked ⛔. Full doctrine lives in this folder's CLAUDE.md — if you have not read it this session, read it now.

---

## Phase 1 — Intake & Recon

**Goal:** Know what changed, why, and what the Operator wants, without asking a single question whose answer is on disk.

1. Complete the CLAUDE.md activation sequence (environment discovery) if not already done.
2. **Cargo scan — `_INBOX/` first (the standing cargo bay), repo root as legacy fallback.** Read every cargo file, then **triage each aloud per CLAUDE.md D16** into one of three classes:
   - **PACK** (`DOCTRINE_PROMOTION*.md`, `*PATCH*.md`): the presumptive lessons input. Read it fully; summarize each entry aloud (target doc, placement, gist). Flag entries targeting files OUTSIDE the Hub (other repos, skill folders) as SPLIT CANDIDATES to park. Flag entries citing docs the Hub does not have as GAPs (options: the doc rides in this run if provided, or the entry lands flagged — never a silent dangling reference).
   - **NEW DOC:** no Hub counterpart exists — announce it as entering fresh.
   - **SUPERSEDING DOC:** a Hub counterpart exists — announce the match (canonical name first, content similarity second), the live doc's current version, and that landing it means archive-and-replace. An ambiguous match or unclassifiable file is a QUESTION, never a guess.
   - **Multiple packs:** list them; ask which are in scope.
   - **RESUME declared or evidenced** (existing `docs/*` branch with commits, partial archives): switch to CLAUDE.md D15a before anything else — inventory reality, report DONE vs NOT DONE with evidence, re-present from the last completed gate.
3. Find and read the project's lessons file (`LESSONS_LEARNED.md` / `LESSONS_BIN*` / `agent_docs/LESSONS*`).
   - **Found:** summarize FLAGGED entries not already covered by a pack.
   - **Neither pack nor lessons file:** say so, offer to create a lessons file from `templates/LESSONS_LEARNED.md`, and help populate it from the conversation before proceeding.
4. Read `references/ANTI_PATTERNS.md` — announce that you have, and name the one or two failure modes most relevant to this job's shape.
5. Ask ONLY the questions discovery could not answer (typically: "which entries are we shipping today?" and "is the Architect's ripple map already written, or am I drafting it?").
6. Present the Phase 1 Plan: entries in scope · splits parked (with target repo) · gaps raised · docs you believe are affected (preliminary) · what happens next.

**⛔ Stop Gate 1:** End with "Awaiting your APPROVED on scope." Do not proceed without it.

**Output:** an approved scope — the entries being landed, splits parked, gaps resolved or accepted.

---

## Phase 2 — Ripple Analysis

**Goal:** Turn the approved scope into an exact list of doctrine files to touch, with blast radius understood.

1. Read the Hub's `MANIFEST.md`. Use its ← dependency map.
2. For each target doc, list its ← count (how many docs reference it) and name the referencing docs. Announce the heaviest: changes to high-← docs (STARTER_KIT_HANDBOOK sits at ←12, the widest in the graph) propagate furthest and deserve the most caution.
3. Verify each pack entry's stated placement against the live doc's ACTUAL section structure. Placement matches → note it. Placement doesn't exist or differs → report the mismatch here with the nearest real anchor; never improvise silently (D13).
4. Fill `templates/RIPPLE_MAP.md`: per entry → primary doc(s) + verified placement → secondary docs whose text must stay consistent → new docs entering the Hub → renames/moves if any → new version number per doc.
5. If the Architect is in the loop, this map is his to confirm — present it as DRAFT for the Operator to relay, or accept the Architect's map if one was handed in at intake. If the Architect is not in the loop, your map stands, labeled INFERENCE where you reasoned from the dependency graph rather than direct evidence.

**⛔ Stop Gate 2:** Present the ripple map aloud, doc by doc. "Awaiting your APPROVED on the ripple map."

**Output:** an approved ripple map — the definitive touch list.

---

## Phase 3 — Route Decision (the fork) ⚠️ OPERATOR-OWNED

**Goal:** The Operator chooses the execution route with honest numbers in front of him. You NEVER choose for him (CLAUDE.md D3).

**Standing operator ruling (2026-08-05): LOCAL GIT IS THE PRIMARY ROUTE.** The MCP is the exception, for when the Operator explicitly chooses it — typically a genuine 1–2 doc content-only touch from a session with no clone available.

1. Read `decision-trees/route-selection.md` and `references/TOOL_ROUTING.md` now.
2. Size the job from the approved ripple map: number of docs · new docs entering · any renames/moves (structural) · edit depth per doc · archive copies required (each archived doc = one more file write).
3. Present BOTH routes, with estimates, in this exact shape:

   > **The job:** N docs edited, P new docs, M renames, ~K total file writes (including archive copies, MANIFEST, CHANGELOG).
   > **Route A — Local git (PRIMARY):** one branch, Z commits, est. minutes. [If not at a clone: "needs a session at a Hub clone — here's how we get there."]
   > **Route B — GitHub MCP (exception):** ~X API calls, est. Y minutes/hours, verify-after-write on every call.
   > **My recommendation:** local git, per your standing ruling[, unless exception conditions genuinely hold — state them if so].
   > **Your call, boss.**

**⛔ Stop Gate 3 (hard):** WAIT for the Operator's explicit route choice. His choice may differ from your recommendation — that is the system working, not a conflict. Log the decision.

**Output:** a chosen route.

---

## Phase 4 — Execute (the four-step dance, per doc)

**Goal:** Land every change exactly per the ripple map, on the chosen route, with nothing extra.

For EACH doc in the ripple map, in blast-radius order (lightest first, heaviest last), narrating each step:

1. **Archive:** copy the current live doc to `_ARCHIVE/<CANONICAL_NAME>_v<X_Y>.md`, version stamped FROM the doc's current header (never guessed). (New docs skip this step — nothing to archive yet.)
2. **Edit + bump:** apply the approved changes EXACTLY as written in the pack — surgical additions at verified placements, no overwrites, no reflow of surrounding content; bump the header Version/Date; append a Version History row citing the lesson/pack origin. New docs get the standard Hub header instead. **Superseding docs:** after the archive copy in step 1, the cargo file's content replaces the live doc wholesale under the canonical filename — version bumped forward FROM the live header (the cargo file's own version claim is verified, never trusted; mismatches were flagged at Gate 1), standard Hub header applied, Version History row noting the supersession and origin.
3. **MANIFEST:** update the doc's row (version, date, status) — or add the row for a new doc.
4. **CHANGELOG:** append the change entry.

Route mechanics:
- **Local route (primary):** `git checkout main && git pull && git checkout -b docs/<topic>-<date>`; edits via normal file ops; one commit per doc (`docs(<doc>): v<X.Y> — <summary> [<origin>]`); `git push -u origin <branch>`. Type commands by hand — never paste (invisible-character incident, AP-10).
- **MCP route (exception):** create branch first (`docs/<topic>-<date>`); per-file writes with blob-SHA fetch before updating existing paths; verify-after-write on every call (re-read, compare SHA); renames = two-commit compose. Batch what `push_files` allows.

**⏱ Mid-flight checkpoint (D4, MCP route only):** at ~15 write calls, ~10 minutes, 2+ transient failures, or blowing past your Phase 3 estimate — STOP, announce actuals vs estimate, re-present the routing decision. Switching mid-job means: abandon the remote branch cleanly (announce it for deletion), and restart Phase 4 on the local route from the ripple map — the map, not the half-done branch, is the source of truth.

Lint conduct throughout (D9): your changes must pass the lints; pre-existing findings get reported, never fixed uninvited, never exempted.

**⛔ Stop Gate 4:** After the last doc, present the per-doc CHANGES / DIDN'T TOUCH / CONCERNS summary and the verification evidence (grep gates, diff stats or SHA comparisons). "Awaiting your APPROVED to push and hand off."

**Output:** a pushed branch, fully verified, no PR yet.

---

## Phase 5 — PR & Handoff

**Goal:** The Operator can review and merge in under two minutes.

1. Report the compare URL: `https://github.com/ahmedmusawir/app-factory-docs-v1/compare/main...<branch>` (one click for the Operator; his box has no `gh` CLI). On the MCP route you may open the PR directly via `create_pull_request` instead.
2. PR description: entries landed (with origin pack/lessons IDs) · docs touched with old→new versions · new docs added · splits parked (target repo named) · lint status (green, or pre-existing reds named) · any logged overrides.
3. **Tell the Operator his part, explicitly and aloud:** "Your move, boss: open the compare link, create the PR, review, and merge — **rebase-and-merge** for doctrine work. Then tell me it's merged and I'll sweep."
4. Report expected CI outcome so a red ❌ from known stragglers doesn't alarm him.

**Output:** a ready PR (or one-click link) + the Operator briefed on his one action.

---

## Phase 6 — Close-Out Sweep

**Goal:** Nothing floats. The workspace is as clean as the doctrine.

After the Operator confirms the merge:

1. Local route: `git checkout main && git pull` (PULL, never push, on main); delete the merged local branch; `git status` must be clean — cargo files (the pack, ridden-in docs) should have landed via the PR or be explicitly dispositioned, never left floating. **`_INBOX/` must end the run EMPTY:** every file in it either landed (announce where), was parked as a split (target repo restated), or is returned to the Operator with a stated reason. The bay itself stays — an empty `_INBOX/` is the "run complete" signal for the next session.
2. MCP route: confirm the remote branch auto-deleted or request its deletion.
3. Session artifacts (run notes, this run's summary) — commit into the records or an immediate housekeeping PR; announce where they landed.
4. Mark the pack/lessons entries ENCODED with the PR number; parked splits restated with their target repo so they survive the session.
5. Close with the run summary: entries shipped · docs bumped · new docs added · PR merged · splits parked · overrides logged · anything for `examples/`.

**Output:** clean tree, updated lessons/pack status, run summary. Every run before v1.0 is also a test of the skill — note refinements for its Version History.

---

## Worked Example (abridged)

> **Operator:** Go read `_SKILLS/factory-docs-update/CLAUDE.md` and follow it.
> **Agent:** Reading CLAUDE.md... done. Reading SKILL.md... done. Discovery: I'm at a Hub clone, main pulled current. Cargo scan: `_INBOX/` holds three files. Triage: `DOCTRINE_PROMOTION_2026-08-04_NAVBAR_SAGA.md` — a PACK, four entries. Entries 1, 2, 4 target Hub docs; Entry 3 targets a skill folder in another repo — split candidate, I'll park it. `QA_PLAYBOOK.md` — NEW DOC, no Hub counterpart; it also closes the gap Entry 4's citation would otherwise leave. `AUTH_MANUAL.md` — SUPERSEDING DOC: the Hub's live copy is at v1.4, so landing this means archive v1.4 and replace, bumping to v1.5. One question: shipping entries 1, 2, 4 plus both riding docs today? Awaiting your APPROVED on scope.
> **Operator:** Yes. Approved.
> **Agent:** Phase 2. Reading MANIFEST... AUTH_MANUAL is ←6; STATE_MANAGEMENT_MANUAL ←4; FRONTEND_BUILD_PHASE_PLAYBOOK ←5. Verifying placements... Entry 1's anchor section exists as stated. Entry 4 says "the phase-close checklist" — the live doc calls it "Stage 7 Completion Checklist," same thing, I'll anchor there and flag the naming. The ripple map, doc by doc: ... Awaiting your APPROVED on the ripple map.
> **Operator:** Approved.
> **Agent:** Phase 3 — the fork, your call. The job: 3 docs edited, 2 new docs, 0 renames, ~13 writes. Route A, local git, the primary: one branch, 5 commits, about 5 minutes from right here. Route B, MCP: roughly 40 calls with verification, an hour-plus. My recommendation: local git, per your standing ruling. Your call, boss.
> **Operator:** Local. Go.
> **Agent:** Logged. Phase 4, lightest first: STATE_MANAGEMENT_MANUAL. Step 1, archiving as `_ARCHIVE/STATE_MANAGEMENT_MANUAL_v1_2.md`, stamped from its live header... done. Step 2, landing Entry 2 at the end of section 1, exactly as written, bumping to v1.3...

## Anti-Patterns (skill-specific)

1. **Choosing the route yourself.** Even when the answer looks obvious. The estimate + recommendation + WAIT ritual is the product; skipping it is the failure.
2. **Grinding past the estimate.** Silence during an MCP slog is a violation, not stoicism. The checkpoint exists because the Operator once had to kill a runaway job himself.
3. **Guessing the archive version.** The `_v<X_Y>` suffix comes from the live doc's header, read at execution time. A guessed suffix poisons `_ARCHIVE/` history.
4. **"While I'm in here" fixes.** Pre-existing lint reds, typos in untouched docs, tempting refactors → CONCERNS list. Never the diff.
5. **Asking the Operator to run git.** He merges. That is all. If a step seems to need his terminal, the plan is wrong — redesign it.
6. **Skipping narration to go faster.** Speed that the Operator cannot hear is not speed; it's opacity.
7. **Landing a dangling reference.** An entry citing a doc the Hub lacks either brings the doc with it or lands flagged with the gap on record — never silently.
8. **Obeying cargo conventions over Hub law.** Packs may say "filename carries version" or use foreign headers. Content lands verbatim; mechanics translate to Hub law; translations get flagged (D15).

## When You're Done

All six phases complete; PR merged by the Operator; sweep clean; entries marked ENCODED; parked splits restated; run summary delivered aloud. Then say what would improve this skill — every run before v1.0 is also a test of the skill itself.

## Version History

| Version | Date | Change |
|---------|------|--------|
| 0.3-DRAFT | 2026-08-10 | Phase 1 cargo scan moved to `_INBOX/` (standing cargo bay; root demoted to legacy fallback) with mandatory D16 triage aloud: PACK / NEW DOC / SUPERSEDING DOC. Resume path added at intake per new D15a. Phase 4 dance gains superseding-doc mechanics (archive-and-replace under canonical name, version verified against live header). Phase 6 sweep requires `_INBOX/` empty at close — landed, parked, or returned, never floating. |
| 0.2-DRAFT | 2026-08-05 | Phase 1 rebuilt around cargo scan: promotion packs (`DOCTRINE_PROMOTION*`, `*PATCH*`) discovered automatically as presumptive scope, with split-candidate and gap flagging. Phase 3 flipped to the standing ruling: local git PRIMARY, MCP exception. Phase 2 gains placement verification against live structure. New-doc entry mechanics added to the dance. Anti-patterns 7–8 added. Worked example updated to the promotion-pack flow. |
| 0.1-DRAFT | 2026-07-12 | Initial methodology. Six phases, four stop gates, operator-owned Phase 3 route decision with mid-flight checkpoint. |
