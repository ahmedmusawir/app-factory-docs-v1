# Architect / Engineering Report to the 10X Lab — RRM Campaign

**From:** Architect, Cyber Pharma v1 · **Date:** 2026-10-02 · **Campaign:** RRM-001…004 (Review Rework Modules), repo `cyber-pharma-dev-v1-phase-3`
**Status:** Findings and proposals. Nothing here is production doctrine until the Lab reviews it. The QA Lead files the QA-side findings and the QAM Playbook separately.
**Bundle:** this report sits on top of four companion documents (§8). Read this first; open the others for evidence.

---

## 1. The finding in one paragraph

A prepared module can be built and handed off by an AI Engineer in one continuous session, with no human touch between "go" and "here is your staging block". That held twice in a row on real production modules (RRM-003: 11m54s; RRM-004: 11m15s; zero stops, zero Director touches both times). The same discipline applied to QA (the QAM pilot) took Director touches inside the QA run from 8 to 0. The time saved is not in the agent; it is in the pack. **Every interruption we saw across four modules traced back to something the pack asserted without measuring.** The one-shot works when the Architect measures first and the pack declares everything a human will ever be asked for.

---

## 2. Metrics across the campaign

| Module | Shape | Engineering session | Checks | Stops | Self-repairs | Director touches (eng) | QA | Director touches (QA) | Gate Q |
|---|---|---|---|---|---|---|---|---|---|
| RRM-001 Removal | staged, multi-prompt | not measured | — | — | — | several per stage | manual matrix | Director-heavy | PASS 2026-09-22, 0 rework |
| RRM-002 Ledger truth | staged, multi-prompt | not measured | — | — | — | several per stage | agent browser QA; one environment interruption (paused replica, drifted identities) | credentials + resumption | PASS 2026-09-28, 0 defects, 0 rework |
| RRM-003 Access/Cache/Hygiene/Docs | **one-shot engineering pilot** | **11m54s** | 67 | 0 | 3 (all new test code) | **0** | 74m55s active, two segments; pack named QA accounts that did not exist | 8 (1 ruling + 7 human sign-ins) | PASS 2026-09-29, 26/26, 0 rework |
| RRM-004 Dependencies | **one-shot engineering + QAM pilot** | **11m15s** | 80 | 0 | 0 | **0** | Q2 body 10m08s (17m21s release); Q1 raised one scope stop, resolved before Q2 | **0 inside Q2**; credentials by file | PASS 2026-10-02, 31 product ACs, 0 rework |

Campaign: four modules, four Gate Q passes, zero repair rounds. Evidence paths are in each module's `EXECUTION_LOG.md` §Metrics and, for RRM-004, `QAM/QAM_PILOT_RESULTS.md`.

What the numbers do and do not say: two one-shot runs is a pattern, not a law. Neither run hit a hard product problem; the pattern has not yet been tested by a module where the right fix is unclear. RRM-004's QA did not exercise a repair loop. Both are open questions (§7).

---

## 3. The one-shot engineering recipe (proven twice)

The Architect does these before the Engineer sees the pack:

1. **Measure before writing a single acceptance criterion.** For RRM-004 the Architect cloned `main`, applied the upgrade in a scratch copy, ran install, build, tsc, eslint, jest, served the build and probed it. Every number the Engineer later produced matched to the decimal (41 + 18 lockfile moves, 17 routes, 34/164). An AC written against a measured system is an AC the Engineer can meet without a ruling.
2. **Read facts from the source of truth, never from conversation.** Versions from the registry and the lockfile; advisories from `npm audit`; installed library versions from the package's own metadata. Memory is where stale numbers come from.
3. **A preflight that is a gate, not a checklist.** Machine-checkable rows, run at Plan Mode and again at the start of the build. A failed row stops the run before anything expensive. Every row should exist because something real failed once (the bare standalone server that 404'd static files; the build-time font fetch).
4. **Enumerated stop conditions.** Eight, numbered, specific. "If unsure whether it is a stop, it is." The Engineer stops only on a number, never on nerves.
5. **Declared checkpoints, none inside the build.** Every human touch is listed before the run. The Director knows exactly when he is needed and is never needed mid-session.
6. **Plan Mode stays.** It caught real pack errors in every module (an instrument path that throws, a preflight that measured a 404). It is the cheapest stop in the process.
7. **Rulings land on disk before the build.** Decisions the Director makes at Plan Mode are written as addendum rows by the Engineer in a docs-only step. The build prompt cites them; it never carries a decision in prose.
8. **Three prompts, one staging block.** Plan, rulings, build. The build ends with every path explicit, one `git add` per line group, and the commit message. The Director commits once.
9. **Metrics are part of the contract.** Timestamps, checks, self-repairs, touches, stops — an AC, not an afterthought. Without them there is nothing to bring to the Lab.

---

## 4. The Architect's half of the QAM (counterpart to the QA Lead's playbook)

The QA Lead owns what a QA Module must contain. The Architect owns generating it into every pack so nobody builds folders by hand. Checklist for any RRM/BIM/ABM/APBM pack:

- [ ] `QAM/` ships in the pack zip from day one. No overlay, no rename, no mid-flight move.
- [ ] `QAM/QAM_ENTRY.md` — model-neutral first file; points to the law and the prompts.
- [ ] `QAM/AGENTS.md` — the QA Executor's law, copied from the playbook canon; module-specific stops appended, never edited into the canon.
- [ ] `QAM/QAM_PREFLIGHT.md` — canon rows plus module rows; **the QA target and its identities are named and verified at authoring**, not discovered in the run.
- [ ] `QAM/QAM_PROMPTS.md` — Q1 recon + plan draft, Q1b, Q2 one-shot, Q4 retest, Q5 cleanup.
- [ ] `QAM/QAM_CHECKPOINTS.md` — every Director touch, with the exact command line to give.
- [ ] `QAM/QAM_RISK_REQUIREMENTS.md` — §A the QA Lead's standing doctrine (from the playbook), §B the Architect's module risk notes, §C left for the QA Lead.
- [ ] `QAM/QAM_MANIFEST.md` — template only; the Engineer fills it at handoff. The build prompt names it.
- [ ] `QAM/QAM_TEST_PLAN.md` — placeholder that says who drafts (QA Executor) and who approves (QA Lead). The Architect writes no part of the plan.
- [ ] Output templates: evidence matrix, execution report, repair proposal, inventory, cleanup report, pilot/process results.
- [ ] **Scope exceptions pre-ruled.** Anything the QA run will see that looks out of contract (predecessor docs hunks, archive moves) is an addendum row before Q1. RRM-004's only QA stop was this exact gap.
- [ ] Credentials protocol: the env file name, keys, proof rows, and deletion step are in the pack; the Director creates the file at the declared checkpoint.
- [ ] Two verdicts: product ACs gate certification; process ACs are graded separately and never rescue or block it.

---

## 5. Anti-patterns, each caught for real

| Anti-pattern | What happened | Fix (now practice) |
|---|---|---|
| Literal SHAs in a pack | Pack commit moved HEAD; the P1 check failed against a hard-coded baseline (RRM-001) | Refer to "the previous module's merge commit"; the Engineer records the SHA at Plan Mode |
| Preflight that asserts instead of measures | "Before" header capture measured a 404, not the defect (RRM-003) | Every capture records its status line; rows come from real failures |
| Checkpoint names an environment nobody verified | QA accounts on a scratch project did not exist; 7 human sign-ins followed (RRM-003) | QA target and identities verified at authoring; credentials by env file with proof rows |
| Package export-map trap | `require('…/versions.json')` threw at P1; a QA helper hit the same trap on `sharp/package.json` in Q2 (RRM-004) | Read the package's `exports` before scripting against it; use the exported subpath or read the file from disk |
| Shell pipe inside a Markdown table cell | `\|` read as an escape, not a pipe (RRM-004 v1.0) | Commands with pipes are written as plain lines, never in table cells |
| Scope exception left for QA to find | Q1 stopped on predecessor docs hunks and `_OLD/` moves; resolved by A-15 (RRM-004) | Pre-rule known out-of-contract diffs in the pack |
| "Transcribe verbatim" without the text | The closeout prompt referred to the QA Lead's letter but did not carry it; the Engineer refused to reconstruct a certificate from a summary — correctly (RRM-004 P5) | A prompt that says "transcribe" contains the text between markers |
| Hand-editing rows the Engineer can write | Director pasting addendum rows by hand (RRM-002) | All rulings go to the Engineer as docs-only prompts |
| Long one-liner git commands | Director could not follow or recover a failed line (RRM-002) | One command per block, numbered |

---

## 6. Precedent: the frozen contract beat the pilot

The QA Lead's QAM rulings arrived while the Engineer's build was running. The clean way to adopt them would have been to rewrite the pack. The factory's rule says the contract freezes at engineering handoff and changes only by appended rows. The rule won: the QA folder was moved with a tracked `git mv`, the new QA files were placed as an overlay after the candidate commit, and the frozen engineering files took their changes as four addendum rows and erratum entries through a docs-only Engineer prompt. Cost: one prompt and four commands. Benefit: the certified candidate's contract was never edited after the fact, and the audit trail shows exactly when and why each change arrived. **Recommend this as standing precedent:** a mid-flight process change is recorded against a frozen contract, never written into it.

---

## 7. Proposals for the Lab (not doctrine until reviewed)

1. **Adopt the one-shot engineering recipe (§3) as the default module shape** for RRM/BIM/ABM/APBM, with Plan Mode retained.
2. **Adopt the Architect's QAM checklist (§4)** as the Architect-side companion to the QA Lead's QAM Playbook; both reviewed together.
3. **Make "measure before AC" mandatory for any module that touches dependencies, configuration or infrastructure**, where the Architect can run the change in a scratch copy at authoring time.
4. **Make the anti-pattern table (§5) a pre-publish checklist** the Architect runs over every pack before handing it to the Director.
5. **Adopt the §6 precedent** for all future mid-flight process changes.
6. **Open questions to answer with the next module:** does the one-shot hold when the right fix is unclear and Plan Mode must surface a real design choice? Does the QAM repair loop (proposal → scope ruling → repair → targeted retest) run as cleanly as the happy path? Is zero Director touches inside a QA run repeatable when authentication meets MFA or rate limits?

---

## 8. Bundle and evidence

| Document | What it is |
|---|---|
| `ARCHITECT_ENGINEERING_10X_LAB_REPORT_RRM_CAMPAIGN.md` | This report — findings, metrics, proposals |
| `ONE_SHOT_ENGINEERING_ARCHITECT_FIELD_NOTE_RRM003.md` | The first one-shot run, written up the day after |
| `ARCHITECT_OPINION_QAM_QA_MODULE.md` | Why whoever built the candidate does not write the plan that tests it |
| `QAM_OPERATING_MODEL_PROPOSAL_v0_1.md` | The QAM model the QA Lead accepted and ruled on |
| `QAM_PILOT_ARCHITECT_JOURNAL.md` | The day-by-day record of decisions, corrections and reasons |

In-repo evidence: `agent_docs/RRM_CAMPAIGN_MAP_v1_0.md` §0 (scoreboard), `agent_docs/RRM_CAMPAIGN_JOURNAL.md` (each seat's entries), `agent_docs/RRM_FINDINGS_DISPOSITION_LEDGER.md`, and each `agent_docs/ACTIONS/RRM-00N-CYBER-PHARMA/EXECUTION_LOG.md` §Metrics; RRM-004 `QAM/QAM_CERTIFICATION.md` and `QAM/QAM_PILOT_RESULTS.md`.

— Architect, Cyber Pharma v1
