# QAM — Operating Model Proposal

**From:** Architect · **To:** QA Lead, Director · **Date:** 2026-09-30 · **Status:** proposal for the QA Lead to reconcile with the pilot plan v0.1; nothing here changes RRM-004 in flight.
**Answers the Director's brain-dump of 2026-09-30:** Part 1 (credentials automation) and Part 2 (who writes the QAM, and when).

---

## 0. The short answer

Neither scenario as written — a merge of the two, split along one line:

**The skeleton is authored with the pack. The facts are filled at handoff. The plan is written by the QA seat. The run is one command.**

| Half of the QAM | Who | When | Why there |
|---|---|---|---|
| **Law + skeleton** — Cody's front door, the QA preflight rows, the manifest template, the output templates, the stop list, the one command | Architect, generated from the QA Lead's **QAM Playbook** | while authoring the module pack (RRM/ABM/APBM zip) | mechanical, playbook-derived, belongs in one zip (Scenario One) |
| **Facts** — candidate identity, reproduction, changed files, environment needs, the Engineer's measurements labeled as claims | Engineer | at handoff, end of the one-shot build | only he knows what he built (both scenarios agree) |
| **Plan** — risk ranking, attack order, negative controls, reference values with derivation rules, the instrument to corrupt | **QA Lead** (or a QA-seat agent under the QA Lead) | drafted from the frozen `ACCEPTANCE_SPEC.md` while the Engineer builds; finalized in minutes once the manifest lands | whoever built the candidate does not write the plan that tests it (Scenario Two's instinct) |
| **Execution** — evidence, matrix, report, repair proposal, metrics | QA Executor (Cody) | Q1 recon → QA Lead thumbs up → Q2 one-shot | mirrors Claudy's P1 → P2 exactly |

And the thing the Director suspects is true: **RRM-004 already is this.** Its `QA/` folder holds Cody's operating law (`AGENTS.md`), the QF preflight, the manifest template, the plan placeholder marked "QA Lead only," the output templates, the Q-stops and the one-line Director command. It is a QAM in everything but the folder name and the playbook behind it. The playbook is what comes *out* of this pilot.

---

## 1. Where the Director's two scenarios agree, and where they don't

| Point | Scenario One | Scenario Two | Proposal |
|---|---|---|---|
| A QAM Playbook exists, QA Lead writes it | yes | yes | yes — `agent_docs/AUTHORITY/QAM_PLAYBOOK.md`, snapshotted into each module like `GOVERNING/` |
| Who lays down the QAM folder | Architect, inside the pack | QA Lead, handed to Director, dropped into the pack | **Architect**, inside the pack, *generated from the playbook*. One zip, one drop. The QA Lead's authorship shows up in the playbook and the plan, not in the folder scaffolding |
| Who fills it after the build | Claudy (handoff, execution report) | Claudy, on Architect instruction | Claudy fills **the manifest only** — facts and claims. He does not write the execution report (that is Cody's) and never the plan |
| Who writes the plan | *(not stated — the gap)* | *(not stated — the gap)* | **QA Lead.** This is the independence line and it is the one thing neither scenario names. Without it, Cody runs the Engineer's exam (or the Architect's, which is the same contract graded twice) |
| Cody recon mode | yes | yes | yes — **Q1**: QF preflight + contradiction report; QA Lead rules; Director commits the rows; then **Q2** one-shot |
| Rework | *(implied)* | Cody + Claudy on `qa/…`, QA Lead + Director supervise | yes — Cody drafts `REPAIR_PROPOSAL.md`; QA Lead classifies; Architect scopes; Claudy repairs on the QA branch; Cody re-pins and reruns only the retest scope |

The only real disagreement between the scenarios is *who drops the folder*. Both are fine; Scenario One is one fewer handoff and keeps the pack as the single artifact the Director places. Take it.

---

## 2. Lifecycle — one module, end to end

```
Architect authors pack  ──►  Director places pack, commits
        (incl. QAM skeleton
         from the playbook)
                                 │
                        Claudy P1 (plan)  ─►  Director + Architect rule  ─►  P1b rows
                                 │
                        Claudy P2 (one-shot build + handoff + QAM manifest)
                                 │                                    ║
                                 │                    QA Lead drafts the plan from the
                                 │                    frozen spec IN PARALLEL with P2
                                 ▼                                    ║
                        Director commits candidate  ◄─────────────────╝
                        Director cuts qa/<module>
                        QA Lead finalizes plan from the manifest (minutes), ratifies law
                        Director commits QA planning docs
                                 │
                        Director: ONE COMMAND ──►  Cody Q1 (recon: QF preflight + contradictions)
                                 │
                        QA Lead reads the recon, thumbs up (or rules; Director commits Q1b rows)
                                 │
                        Cody Q2 (one-shot QA body) ──► matrix + report + metrics (+ REPAIR_PROPOSAL on a FAIL)
                                 │
                        QA Lead certifies Gate Q (product) + pilot verdict (process)
                        [rework loop if needed — §5]
                        Cody closeout: cleanup, inventory, delete the QA env file (§4)
                        Architect closeout ─► Engineer closeout ─► Director merge --no-ff
```

The parallel step is the one that keeps the QA Lead's plan from adding wall-clock: the frozen `ACCEPTANCE_SPEC.md` exists before P2 starts, so the risk ranking and the reference-value derivation rules can be written while Claudy builds. The manifest only adds the candidate SHA, the exact probe lines and the Engineer's claims.

---

## 3. Folder shape (from the next module on)

Rename `QA/` → `QAM/`. Same place, same lifecycle, one name that says what it is.

```
agent_docs/ACTIONS/<MODULE>/
├── CLAUDE.md … ACCEPTANCE_SPEC.md … CLAUDY_PROMPTS.md      (Engineering pack, as today)
├── RULINGS_ADDENDUM.md                                     (shared, append-only)
├── evidence/                                               (Engineer)
└── QAM/
    ├── CLAUDE.md               Cody's front door — law, seat boundaries, order of work, Q-stops, the one command  [Architect from playbook; QA Lead ratifies]
    ├── QAM_PREFLIGHT.md        QF rows — a gate, run first in Q1                                                [Architect from playbook; QA Lead ratifies]
    ├── QAM_MANIFEST.md         the factual half                                                                  [template by Architect; Engineer fills at handoff]
    ├── QAM_TEST_PLAN.md        the judgment half                                                                 [QA Lead — only]
    ├── QAM_PROMPTS.md          Q1 recon · Q1b rulings · Q2 one-shot · Q4 retest · closeout                       [Architect from playbook]
    ├── GOVERNING/              playbook snapshot + PROVENANCE.md                                                 [Engineer copies at handoff]
    ├── AUTOMATION/             disposable drivers; promotion list                                                [Cody]
    ├── evidence/                                                                                                 [Cody]
    ├── AC_EVIDENCE_MATRIX.md · QAM_EXECUTION_REPORT.md · REPAIR_PROPOSAL.md (only on FAIL)                       [Cody]
    ├── ARTIFACT_INVENTORY.json · QAM_CLEANUP_REPORT.md · QAM_RESULTS.md (metrics)                                [Cody]
    └── QAM_CERTIFICATION.md                                                                                      [QA Lead]
```

Three prompts for Cody, mirroring Claudy's three: **Q1** (recon, read-only, one stop), **Q1b** (rulings, docs-only), **Q2** (one-shot). The Director's "point Cody at the folder" is Q1's first line.

---

## 4. Part 1 — credentials automation (agree, with the guardrails that make it safe)

The Director and QA Lead are right: seven browser sign-ins in RRM-003 is the cost of the human-in-the-loop model, and it is the wrong cost. A QA env file removes DC-5 from the run. Proposal:

| Rule | Detail |
|---|---|
| **File** | `.env.qa.local` at repo root. Keys: `QA_TARGET_LABEL`, `QA_ADMIN_EMAIL`, `QA_ADMIN_PASSWORD`, `QA_MEMBER_EMAIL`, `QA_MEMBER_PASSWORD`. No Supabase keys — those stay in `.env.local` as today. |
| **Ignored, proven** | `.gitignore` carries `.env.qa.local`. QF row: `git check-ignore -q .env.qa.local && echo ignored` → `ignored`. A file that is not ignored is a Q1 FAIL before anything runs. |
| **Created by** | Director, before Q1, for the target the DD ruling names. Accounts are **dedicated QA identities** (one ADMIN, one MEMBER) on that target — never a real user, never a Director login. Until BIM-004's seed owns test users, DA-5 creates them. |
| **Read by** | Cody's driver, from `process.env` after `dotenv.config({ path: '.env.qa.local', quiet: true })`. Values never logged, never written to a helper, never in a screenshot (the driver types into the field, the trace starts after login). |
| **Checked without reading** | QF row counts key names: `grep -cE '^QA_(ADMIN\|MEMBER)_(EMAIL\|PASSWORD)=' .env.qa.local` → `4`. Never `cat`. |
| **Login-only** | The driver logs in, walks, logs out. No data writes, no role changes, no settings — same as E-17. |
| **Privacy scan** | The existing evidence scan gains the four values as forbidden strings (read from env at scan time, compared by hash, never stored). Zero hits or the certification is blocked. |
| **Deleted by Cody at closeout** | `rm .env.qa.local` then `test ! -e .env.qa.local && echo gone` → `gone`, recorded in `QAM_CLEANUP_REPORT.md`. Also `git status --porcelain -- .env.qa.local` empty (it was never tracked). |
| **Rotated by the Director** | After each module, rotate the two QA passwords in the dashboard. Optional but cheap, and it makes a leaked file worthless within a day. |
| **What DC-5 becomes** | "Director creates `.env.qa.local` before Q1" — one touch, off the run clock, instead of N sign-ins inside it. Target Director touches during Q2: **zero**. |

One thing this does *not* change: the Director still decides the target (DD-3 today). The file just carries the decision to Cody without a human at the keyboard.

---

## 5. Rework loop

Same shape as today, now with names:

1. Cody records the FAIL, keeps going with everything it does not block, drafts `REPAIR_PROPOSAL.md` (finding, evidence, affected ACs, suggested files, suggested retest scope).
2. QA Lead classifies: implementation defect / contract gap / environment / instrument.
3. Architect rules scope and writes the P4 repair prompt (Claudy) and the Q4 retest prompt (Cody).
4. Claudy repairs on `qa/<module>`; Director commits.
5. Cody re-pins HEAD, reruns **only** the retest scope plus the regression rows the QA Lead names; matrix updated in place with the round number.
6. QA Lead re-adjudicates.

Claudy and Cody both sit on `qa/<module>`; neither touches the other's lane; the Director is the only committer. The proposal is a proposal — the scope ruling is the Architect's and the Director's, exactly as the QAM opinion said.

---

## 6. What the QA Lead owns (the playbook's table of contents, as I would draft it)

1. Purpose and the two verdicts (product Gate Q; process pilot verdict) — never mixed.
2. Seat boundaries and authorship — the table in §0 of this memo, as doctrine.
3. `QAM/CLAUDE.md` canonical text (Cody's law) — the static part every module copies.
4. QF preflight canon — the rows every module carries, plus how a module adds its own.
5. Q-stop canon — the enumerated list (Q1–Q7 from RRM-004), plus how a module adds one.
6. Manifest template — what the Engineer fills, and the "facts and claims only" rule.
7. Plan standard — what a QAM test plan must contain: risk ranking, negative controls, reference values with derivation rules, one deliberate instrument attack, finding classes, the retest rule.
8. Credentials protocol — §4 above.
9. Evidence standard — paths, exit codes, unfiltered output, hex-dump not binaries, sanitized traces, privacy scan.
10. Repair proposal standard and the rework loop — §5.
11. Metrics — the fixed list, with the RRM-002/003/004 baselines as the first rows.
12. Certification standard — the QA Lead reads the matrix and the evidence map before signing, every time, and says so in one line.

The Architect's side of the contract is §3–§6: I generate those into each pack from the playbook and never improvise them.

---

## 7. What changes, and when

| | RRM-004 (in flight) | BIM-004 and after |
|---|---|---|
| Folder name | `QA/` (leave it) | `QAM/` |
| Cody's law | `QA/AGENTS.md` | `QAM/CLAUDE.md` (same content, playbook-canonical) |
| Cody prompts | one command → Cody runs preflight + body in one go | Q1 recon → thumbs up → Q2 one-shot |
| Credentials | DC-5, Director in the browser, one per role | `.env.qa.local`, zero touches in-run |
| Plan | QA Lead authors after DC-3 (already the rule) | QA Lead drafts in parallel with P2, finalizes on the manifest |
| Playbook | none yet — the pilot produces it | `agent_docs/AUTHORITY/QAM_PLAYBOOK.md`, QA Lead, snapshotted per module |

Nothing in RRM-004 needs to move. Its pilot results (`QA/QAM_PILOT_RESULTS.md`) are the evidence the playbook is written from.

---

## 8. Two things I would push back on, gently

- **"Claudy fills the QAM folder with … execution report etc."** — no. Claudy fills the manifest. The execution report is Cody's. If the Engineer writes any part of the QA record, the record is no longer independent, and three zero-defect passes in a row is exactly the moment to be strict about that.
- **Point Cody at the folder and "he takes off"** — yes, but with the recon stop. Claudy's P1 caught real pack errors in every module. Cody's Q1 will too (RRM-003 QA would have stopped on "SCRATCH accounts do not exist" in thirty seconds instead of hours). The one command starts Q1; the QA Lead's thumbs up starts Q2. Two lines from the Director per module, not one — and both of them off the clock.

— Architect, Cyber Pharma v1
