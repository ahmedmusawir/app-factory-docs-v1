# ONE-SHOT ENGINEERING

## Architect's Field Note from RRM-003

**For:** the 10x Lab Master Architects, Stark Industries
**From:** Cyber Pharma Project Architect
**Date:** 2026-09-29
**Companion to:** the QA Lead's field note "Agentic One-Shot Build & QA — Production Field Note from RRM-002" (2026-09-28), already submitted. That note covers the QA seat. This one covers the Engineering seat and the Architect's preparation that made the single session possible.
**Evidence source:** Cyber Pharma RRM-003 production engineering, 2026-09-28. Not a simulation.
**Status vocabulary:** EVIDENCE (observed on disk or in a report) · INFERENCE (my reading of why) · PROPOSAL (not yet proven twice).

---

## Executive summary

On 2026-09-28 the Cyber Pharma Engineer completed a bounded four-part module — keyboard accessibility on three UI primitives, a cache-header repair, a hygiene pass, and a documentation quarantine — in **one continuous session of twelve minutes**, with **zero Director interventions, zero stop conditions, seventeen-for-seventeen preflight, and a green board** (34 suites / 164 tests, two clean builds, zero type or lint errors). The Director's involvement between "go" and "done" was nil. He committed once.

The same Engineer, working for the same Director on the same repository, needed six prompts and six Director commits for RRM-001 eight days earlier.

Nothing about the Engineer changed. What changed was the **authority package** he was handed. This note describes what went into that package, what the preparation cost, what Plan Mode still caught even in one-shot form, and what I would and would not carry forward.

The lesson in one sentence:

> One-shot is not a property of the agent. It is a property of the preparation. When every decision the agent could face has already been made, written down, and placed where the agent will read it, the agent does not need to stop.

---

## 1. The lineage: three modules, one campaign

| | RRM-001 (20 Sep) | RRM-002 (23 Sep) | RRM-003 (28 Sep) |
|---|---|---|---|
| Scope | Remove two starter-kit surfaces; prove unreachability | Summary-tab disclosure + fixture audit | Keyboard/focus, cache header, hygiene, docs quarantine |
| Prompts to the Engineer | 6 (P1, P2-S1, P2-S2, P3, plus two docs-only) | 5 (P1, P1b, P2-S1, P2-S2, P3) | **3 (P1, P1b, P2)** |
| Director commits during engineering | 6 | 5 | **2** (P1b, then one at the end) |
| Director touches between build start and handoff | ~4 (stage commits + one ruling) | ~3 | **0** |
| Stop conditions | described in prose | described in prose | **enumerated, eight, numbered** |
| Preflight | none (baseline check only) | none (baseline check only) | **17 machine-checkable rows, run at P1 and P2** |
| Director checkpoints | discovered as we went | discovered as we went | **declared in a file before the run** |
| Contradictions caught at Plan Mode | 11 | 2 + one material fixture finding | 10 (two would have broken the run) |
| Build wall-clock (engineering only) | ~3 hours across stages | ~1.5 hours across stages | **12 minutes** |

**EVIDENCE:** pack folders `agent_docs/ACTIONS/RRM-00{1,2,3}-CYBER-PHARMA/`, the Engineer's completion reports in `agent_docs/RESPONSES/`, `EXECUTION_LOG.md` §Metrics in RRM-003.

**INFERENCE:** the reduction is not linear in scope. RRM-003 touched more files (25 modified, 15 added, 1 deleted) than RRM-002 (6 product files). The time fell because the *decisions* were pre-made, not because the work was smaller.

---

## 2. What the RRM-003 authority package contained that the earlier ones did not

Every RRM pack already had the factory's standard shape: a front door (`CLAUDE.md`), a brief, a frozen acceptance spec with an erratum lane, staged prompts, an addendum file, and QA/evidence lanes. RRM-003 added four things.

### 2.1 `ENVIRONMENT_PREFLIGHT.md` — a gate, not a checklist

Seventeen rows, each with a read-only command and a literal pass condition. Branch, baseline identity, ancestry, docs-only-above-baseline, clean tree, runtimes, dependencies present without installing, env key *names* present (never values), port free, evidence lane writable, disk headroom, **a full baseline build and test run**, a standalone-server boot, **the "before" header capture for the cache-header repair**, the governing-doctrine source, the legacy files that the docs stage would touch, and a check that no Director checkpoint falls inside the run.

The Engineer runs it twice: at Plan Mode (report) and at the start of the one-shot (gate). Any FAIL at the gate is stop condition 1. The run does not begin.

**EVIDENCE:** `evidence/PREFLIGHT_P1.txt`, `evidence/PREFLIGHT_P2.txt` — 17/17 both times.

**What it caught:** PF-14 itself. At P1 the Engineer discovered that the bare standalone server does not serve `.next/static`, so the "before" capture was measuring Next's own 404 header, not ours. He re-measured with the static directory copied in (the normal standalone deploy step), proved the defect was real, and proposed an amendment to the preflight row. Without the preflight, this would have surfaced in the middle of S2 as a confusing pass, or a confusing fail, and cost a stop.

### 2.2 Enumerated stop conditions

Eight, numbered, in the front door:

1. Any preflight check fails.
2. Any edit needed outside the allowed files.
3. An existing test fails and the only fix is to modify that test.
4. The cache-header fix cannot be achieved inside `next.config.js` alone.
5. A keyboard fix would require touching the frozen column definitions, the admin group, or a kit primitive's exported API.
6. The board is still red after two in-scope self-repair attempts on the same failure.
7. Disk and contract disagree on a point not already covered by a ruling.
8. Anything would require a live database, dashboard, credential, or Git mutation.

Followed by one sentence: *"If you are unsure whether something is a stop condition, it is — stop and report."*

**INFERENCE:** earlier packs described stop conditions in prose ("stop on any scope contradiction"). Prose invites judgment; judgment invites either a nervous stop or a rationalized continue. A numbered list turns the question into a lookup. The Engineer's completion report cites stop condition numbers when explaining why he did *not* stop on the one anomaly he found (an AC path list that overlapped another AC's required change — "there was only one correct action, so I recorded this instead of stopping").

### 2.3 `DIRECTOR_CHECKPOINTS.md` — the human stops, declared before the run

Six checkpoints, each with when, what the Director does, and a status column. DC-1 (approve the plan, rule contradictions) before the run. DC-2 (one commit) after. DC-3 (cut the QA branch). DC-4 (type credentials into the QA Executor's browser — the QA seat's checkpoint, not Engineering's). DC-5 (rule a scope question if QA raises one). DC-6 (merge).

And one line that matters more than the table: **"No checkpoint falls between the start of P2 and the staging block."** The Engineer knew, before he started, that nothing he would encounter required a human. That is what let him keep going.

### 2.4 Three prompts instead of six

P1 plans (read-only; the one stop that has earned its keep three times running). P1b applies the Director's rulings as documentation rows — a step the Engineer performs, never the Director pasting by hand. P2 is the entire build plus the QA handoff in one session, ending in a single selective staging block. The Director commits once.

The P2 prompt itself is long — every stage's allowed work, exit criteria, and evidence file are spelled out — but it is *one* prompt. The Engineer reads it once and executes it top to bottom.

---

## 3. What the Architect's preparation actually consisted of

This is the part I want the 10x Lab to weigh, because it is where the cost moved. The Engineer's twelve minutes were bought with roughly two hours of Architect time spread over two days, plus one Director sitting to rule the plan. Concretely:

**a. Resolve every known ambiguity before writing the pack.** RRM-003's scope came from the campaign map, two carried observations from RRM-001, and one docs-cleanup rider. Before authoring, I re-read the recon report's sections on each finding, the two reviews' original claims, the prior module's addendum rows, and the Director's standing rulings. Every "what should happen if…" I could think of became either an allowed-files entry, a forbidden-work entry, or a stop condition.

**b. Verify every fact the pack asserts against the last known disk state.** File paths, line numbers where cited, which tests exist, which helpers are exported. RRM-001's pack had cited a literal baseline SHA that was wrong by the time the Engineer read it; RRM-002's had assumed a helper was exported when it was private. RRM-003's pack cites the baseline as "the merge commit of the previous module, SHA recorded at P1" and asks the Engineer to confirm every helper's export status in Plan Mode. Verify-then-write, applied to the pack itself.

**c. Write the preflight as executable rows, not as advice.** Each row has a command a human could paste and a pass condition a script could evaluate. The Engineer proposed one amendment (PF-14, above); it was ruled and applied before the run.

**d. Enumerate the stops.** I wrote them by asking, for each stage, "what is the one thing that would make a careful engineer want to ask someone?" and turning each answer into a numbered line.

**e. Declare the checkpoints.** Then I checked the list against the stages and confirmed none fell inside the build. If one had, the module would not have been a one-shot candidate — it would have been a two-shot with a declared pause.

**f. Keep Plan Mode.** P1 is read-only and produces a plan the Director approves. In RRM-003 the plan surfaced ten contradictions or risks, and two of them (the standalone-static issue and the nested-Escape event-order issue in production vs. test) would have produced either a false pass or a stop mid-run. Ten rulings, written by the Architect, applied by the Engineer as documentation rows, committed by the Director, and the run began on a clean tree with every one of them on disk.

**g. Make the rulings the Engineer's job to file.** The Director never edits a file by hand. Rulings go to the Engineer as a documentation-only prompt; he appends rows, verifies IDs are unique, returns a staging block. This kept the Director's role to reading, deciding, and typing git.

**EVIDENCE:** the pack itself (`agent_docs/ACTIONS/RRM-003-CYBER-PHARMA/`), the P1 plan (`agent_docs/RESPONSES/response_2026-09-28_210200_rrm003-p1-plan.md`), `RULINGS_ADDENDUM.md` A-01…A-14.

---

## 4. What the run looked like from the Director's chair

**EVIDENCE**, from the Director's own account and the Engineer's timestamps:

- 21:16 — Director pastes P1b (rulings). Engineer applies. Director commits and pushes. Tree clean.
- 21:29 — Director pastes P2 and leaves.
- 21:29–21:41 — Preflight 17/17. S1: three components, three new test suites, twenty tests, three self-repairs (all in new test code, none in product). S2: one-line config change, five header captures, chunk now `public, max-age=31536000, immutable`, every page still `no-store`. S3: two debug strings, one orphan deleted, three SQL banners, five doc edits, one baseline record, counts corrected, full board rerun. Handoff assembled. Metrics filled. Staging block returned.
- 21:41 — Engineer stops. "Waiting for the Director."
- Next morning — Director stages, commits once, pushes, cuts the QA branch.

Director touches during the run: **0**. Stop conditions hit: **0**. Self-repairs: **3**, all in test code, each with the attempt recorded.

The Engineer's own summary line: *"Not committed. Not self-certified."*

---

## 5. What Plan Mode still caught — the argument for keeping it

The temptation after a run like this is to fold Plan Mode into the one-shot too. I would not, and RRM-003 is the evidence.

The plan surfaced:

- **C-2:** bare `node .next/standalone/server.js` does not serve static assets. The cache-header "before" capture and the AC-202 "after" capture would both have been measuring 404 headers. The Engineer found it, proved the defect on a static-copied server, and proposed the preflight amendment. **This would have made S2 either falsely pass or stop.**
- **C-6:** in production Next.js hydrates against `document`, so React's root listener and the drawer's Escape listener sit on the same node and plain `stopPropagation` does not order them; in Jest the root is a `<div>`, so a naive test passes either way. The Engineer proposed two mechanisms; I ruled the order-independent one (a `defaultPrevented` guard). **A one-shot without this ruling would have shipped a test that passed in Jest and a picker that closed the drawer in the browser.**
- **C-3:** a spec file the pack cited as authority had been deleted in the Director's own pack commit (two folders removed "without thinking"). Restored before P1b.
- **C-5:** the spec said "(preventDefault)" on Space; a native `<button>` already consumes Space, and an explicit handler would either double-fire or suppress activation. Ruled: native semantics, no handler.
- Six more of the ordinary kind: a file named at the wrong path, a docs section the brief's allowed-list did not quite cover, an unsafe claim in a doc outside the grep's scope.

**INFERENCE:** the one-shot succeeded *because* Plan Mode ran, not despite it. Plan Mode is where the Engineer's disk-level knowledge meets the Architect's contract and the Director's authority. Removing it would move those ten rulings into the run as stops — or worse, as silent guesses.

**PROPOSAL:** the doctrine should read "one plan stop, then one-shot," not "one-shot." The plan stop is cheap (read-only, ~15 minutes of agent time, one Director sitting) and it is where every material catch in three modules has happened.

---

## 6. What I would not carry forward unchanged

Honest list, because the 10x Lab should hear the limits from the seat that hit them.

- **Per-stage rollback is gone.** With one commit at the end, a problem found in QA in S1's work cannot be reverted without also reverting S2 and S3. For RRM-003 the stages are independent enough that a targeted repair on the QA line is cheaper than a revert. For a module where stages build on each other, the Architect should consider a declared checkpoint between them — which makes it a two-shot by design, and that is fine.
- **The P2 prompt is long.** Roughly 900 words. The Engineer handled it, but a future harness with a smaller context window, or a less disciplined agent, might not. The obvious mitigation is to move the per-stage detail into the pack files (it mostly already lives in the brief) and make P2 a pointer: "execute `RRM_BRIEF.md` §Stages under `CLAUDE.md` stop conditions." I did not do that for the pilot because I wanted the prompt to be self-contained evidence. Next module I would.
- **One Engineer, one session, one harness.** This is a single observation on a single model. The QA Lead's note makes the same caveat about QA. Two observations across two seats is a pattern; it is not yet doctrine.
- **The preflight row that was wrong was the Architect's.** PF-13/14 assumed a serve method that does not work standalone. The Engineer caught it. A preflight is only as good as the person who wrote it; the doctrine should require the Engineer to *challenge* the preflight at P1, not just run it.
- **The AC overlap the Engineer chose not to stop on** (an AC's "nothing under `supabase/` changed" versus another AC's required banner on `supabase/setup.sql`) was the right call, and he documented it, but it was a judgment. A tighter spec would have had no overlap. Verify-then-write applies to the spec's own path lists.

---

## 7. The shared principle, from the Engineering side

The QA Lead's note states the principle for both seats. From the Engineering side it reads:

- The Architect decides everything decidable before the run, verifies every claim the pack makes against disk, and writes the stops and checkpoints as lists.
- The Director rules the plan, files nothing by hand, commits once.
- The Engineer runs preflight as a gate, plans once, builds continuously, writes evidence after every stage, self-repairs inside scope with the attempts recorded, stops only on a numbered condition, and returns one staging block with the words "not committed, not self-certified."
- Independent QA follows on its own line. Nothing here touches that.

What moved is not the amount of governance. It is *when* the governance happens: before the run instead of during it.

---

## 8. Proposed doctrine seeds (for the 10x Lab to weigh)

1. **One plan stop, then one-shot.** Plan Mode remains mandatory and read-only; the build runs continuously after the plan's rulings are on disk.
2. **Preflight is a gate.** Machine-checkable rows, run at plan and at build start; any FAIL stops before cost. The Engineer challenges the preflight at plan time.
3. **Stops are enumerated, not described.** A numbered list with a "when unsure, it is" clause.
4. **Checkpoints are declared, not discovered.** A file listing every human stop with its trigger; the Architect confirms none falls inside the run before calling it a one-shot candidate.
5. **Rulings are filed by the Engineer.** The Director rules; the Engineer writes the rows; the Director commits. No hand edits.
6. **Verify-then-write applies to the pack.** Paths, line numbers, exports, path lists in ACs. The pack is code the Engineer executes; it should be reviewed like code.
7. **Metrics are part of the deliverable.** Timestamps per stage, checks run, self-repairs, Director touches, stops hit. Without them the next module cannot say whether it did better.
8. **Eligibility is a property of the module, not the agent.** Bounded scope, no mid-run credential or destructive step, independent stages or a declared pause between dependent ones, and a QA plan on a separate line. Modules that fail this test are two-shots by design, and that is a fine answer.

---

## 9. What is next

- **RRM-004** (dependency remediation) will run on the same shape. It is the harder test: higher blast radius, a lockfile change, and a full board rerun as the only proof. If the one-shot holds there, the pattern has held on a removal module, a feature module, a repair module, and an upgrade module.
- **RRM-003 QA** is entering now on the QA Lead's line. Its outcome is the other half of this note's evidence — a twelve-minute build that fails certification would be a different story than one that passes.
- The QA Lead's proposed **QAM** (QA Module) is the natural pair to this: the same authority-package discipline on the QA seat, so the Director's command becomes "point the Executor at the folder." My opinion on it is filed separately.

---

*Filed to the RRM campaign journal as a doctrine-harvest seed. Every number above is on disk in the RRM-003 pack and the Engineer's reports. Nothing here is certified until the QA Lead says so.*

— Architect, Cyber Pharma v1
