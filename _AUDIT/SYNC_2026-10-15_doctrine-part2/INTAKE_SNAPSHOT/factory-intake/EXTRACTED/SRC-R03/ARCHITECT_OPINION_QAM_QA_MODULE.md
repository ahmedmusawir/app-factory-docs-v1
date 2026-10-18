# QAM — The QA Module

## Architect's Opinion for the QA Lead

**From:** Cyber Pharma Project Architect
**To:** QA Lead, Cyber Pharma v1
**Date:** 2026-09-29
**Status:** Opinion, not doctrine. Forward-looking. Nothing here changes the RRM campaign in flight.
**Evidence base:** RRM-001 (manual QA matrix, one repair-free pass), RRM-002 (agent-driven browser QA, environment interruption, one repair-free pass), RRM-003 (one-shot Engineering pilot, now entering QA).

---

## 1. The idea as I understand it

The QA Lead writes a **QAM handbook** — the rules for what a QA Module must contain. For each engineering candidate, a **QAM folder** is authored to that handbook. The Director then points the QA Executor at the folder and says go. The Executor runs the whole QA body in one session, and returns either a **QA execution report** for the QA Lead to certify, or — when something is wrong — a drafted **rework package** (the "RBM") so the repair loop starts with a bounded instruction instead of a conversation.

I like it. Most of it already exists in pieces across our last three modules. The QAM gives those pieces one shape, one folder, one command. What follows is where I think the idea is right, where I would change one authority line, and what would break it if we're careless.

---

## 2. What is already proven (do not re-argue these)

| Piece | Where it was proven | What it showed |
|---|---|---|
| A frozen acceptance spec graded literally, with an append-only erratum lane | RRM-001, RRM-002, RRM-003 | The QA Executor never had to guess what "pass" meant. Every ambiguity went to a ruling row, never to improvisation. |
| Independent derivation of expected values | RRM-002 ($20.27 derived from fixtures, not read from the handoff) | The Executor did not trust the Engineer's number and was right not to. That is the whole point of an independent seat. |
| Agent-driven browser QA with credential entry by the Director only | RRM-002 (16-state authenticated matrix) | The manual role × viewport × theme grid is gone. The Director types a password once and steps back. |
| Environment as a first-class failure class | RRM-002 (paused replica, drifted identities) | The only interruption in three modules was the environment, not the product and not the agent. |
| Machine-checkable preflight before the run | RRM-003 Engineering (17 rows, PASS at P1 and P2) | Zero mid-run surprises. The one thing the preflight itself got wrong (bare standalone server not serving static files) was caught at P1, fixed in the preflight, and never seen again. |
| Governing doctrine copied into the repo with provenance | RRM-001 (Director copy), RRM-002 and RRM-003 (Engineer copy with chain) | The Executor never needs an outside-repo read. |
| Enumerated stop conditions and declared checkpoints | RRM-003 Engineering | Twelve minutes, zero Director touches, zero stops. The agent knew exactly when it was allowed to keep going. |

The QAM should be built out of these. It should not reinvent any of them.

---

## 3. The one authority line I would move

The proposal as stated has **the Engineer author the QAM**. I would not do that, and I want to be precise about why, because the mechanical parts are fine for the Engineer to produce and the judgment parts are not.

**What the Engineer may produce for the QAM** (mechanical, factual, already in `QA_HANDOFF.md` today):
- candidate identity, baseline, branch, provenance chain
- the reproduction map: build commands, serve method, placeholder env, fixture derivation formulas
- the changed-file inventory and product-only diff
- the environment manifest: services, ports, required test identities and roles, tools
- the evidence schema the Executor must fill
- the governing-doctrine snapshot with provenance

**What the Engineer must not author** (judgment, and the source of QA's independence):
- the risk ranking — which claims to attack first
- the test plan — how to attack them
- the negative controls — what must *still* be true
- the reference values — what "correct" looks like, derived independently
- the finding classification and the verdict

If the Engineer writes the attack plan for the candidate he built, the Executor is running the Engineer's exam. Three modules of zero-defect passes look exactly the same whether the QA was independent or not — which is precisely why independence has to be structural, not assumed.

**Recommended split:** the Engineer assembles the QAM's *manifest and reproduction* half at handoff (he does this already). The QA Lead — or a QA-seat agent working from the handbook — authors the *plan and reference* half at QA entry. The Executor consumes both. The handbook defines both halves so neither seat has to think about the boundary each time.

---

## 4. On the "RBM" — the Executor drafting a rework package

Good instinct, with one guardrail.

The Executor is the best-placed seat to *draft* a repair instruction: it has the failing evidence, the exact path:line, the reproduction, and the affected ACs in front of it. Making it write that draft saves the QA Lead and the Architect a round of reconstruction.

But a repair package carries **scope authority** — which files may change, which may not, which ACs are affected, whether the contract needs an erratum. In our factory that authority sits with the Architect and the Director, adjudicated through the QA Lead. So:

- The Executor **drafts** `REPAIR_PROPOSAL.md`: finding IDs, evidence, affected ACs, a *suggested* allowed-file list, a suggested retest scope.
- The QA Lead **classifies** it (implementation defect vs contract gap vs environment vs instrument).
- The Architect **rules scope** and issues the P4 repair prompt; the Director approves and commits.

Name it what you like — "RBM" is fine — but treat it as a proposal, not a work order. The Engineer receives it only after the Architect's scope ruling, exactly as today. Otherwise the QA seat starts writing engineering contracts, and that is the same independence problem in the other direction.

---

## 5. What the QAM folder should contain

Aligned with the field note, tightened by what we have actually needed:

| File | Author | Purpose |
|---|---|---|
| `AGENTS.md` | QA Lead (handbook-derived, mostly static) | The Executor's operating law: seat boundaries, no repair, no self-verdict, no git mutation, evidence-not-narration, stop rules. |
| `QAM_MANIFEST.md` | Engineer at handoff | Module, candidate, baseline, branch, environment, tools, required outputs. The factual half. |
| `ACCEPTANCE_SPEC.md` + `RULINGS_ADDENDUM.md` | Architect (frozen) + append-only | The contract. Copied or linked, never rewritten. |
| `QA_HANDOFF.md` | Engineer | Claims and reproduction. Every line is a claim. |
| `ENVIRONMENT_PREFLIGHT.md` | QA Lead template, Executor runs | Services awake, identities exist with correct roles, browser tooling present, ports free, evidence lane writable. **Gate, not checklist.** Fail = stop before the expensive body. |
| `DIRECTOR_CHECKPOINTS.md` | QA Lead | Declared human stops: credential entry, destructive authorization, visual spot-checks. Nothing discovered mid-run. |
| `QA_TEST_PLAN.md` | **QA Lead** (or QA-seat agent) | Risk-ranked attacks, negative controls, reference values with derivation rules. The judgment half. |
| `AUTOMATION/` | Executor | Disposable browser helpers; a promotion list for anything worth keeping. |
| `evidence/` | Executor | Commands, calculations, diffs, screenshots, safe traces. |
| `AC_EVIDENCE_MATRIX.md` | Executor | One row per AC: PASS / FAIL / BLOCKED / UNTESTED / adjudication-needed, with evidence path. |
| `QA_EXECUTION_REPORT.md` | Executor | What actually happened, including environment events, self-repairs to helpers, and anything unexpected. |
| `REPAIR_PROPOSAL.md` | Executor, *only when a FAIL exists* | Draft for the QA Lead → Architect → Director chain. |
| `ARTIFACT_INVENTORY.json` · `QA_CLEANUP_REPORT.md` · `QA_CERTIFICATION.md` | Executor · Executor · **QA Lead** | Retention, cleanup, verdict. |

The Director's command is then genuinely one line: point the Executor at the folder. The folder already knows its candidate, its environment, its stops, its plan, and its outputs.

---

## 6. What would break it

These are the failure modes I would design against in the handbook, in order of how likely they are to bite:

1. **A stale test identity.** RRM-002's only interruption. The preflight must query the accounts, not assume them. Until BIM-004's seed script owns test users, this is the most fragile row in the whole module.
2. **A vague stop rule.** "Stop if something seems wrong" is the same as no rule. Enumerate them. RRM-003 Engineering used eight; the Executor probably needs six: preflight fail, credential needed, destructive action needed, contract contradiction not covered by a ruling, instrument cannot be trusted, evidence lane cannot be written.
3. **The Executor trusting its own instrument.** BIM-003's lesson: attack the oracle before trusting its green. The plan should require at least one deliberate corruption of any derived reference value or helper, with the expected non-zero failure recorded.
4. **A reproduction that only works on the Engineer's machine.** RRM-003 caught "bare standalone doesn't serve static" at Plan Mode. The manifest must carry the exact serve method, and the Executor must build the candidate itself — never reuse the Engineer's `.next/`.
5. **Evidence that leaks.** Screenshots and traces of authenticated sessions can carry cookies and tokens. RRM-002's evidence security scan should be a mandatory preflight row for cleanup, not an afterthought.
6. **The Executor drifting into repair.** A helper obstruction was fixed inside disposable tooling in RRM-002, correctly. The line is: anything under `AUTOMATION/` and `evidence/` is the Executor's; anything under `src/` is never. Put it in `AGENTS.md` in those words.
7. **The one-shot becoming a reason to skip the human read.** The QA Lead's adjudication is the certificate. A clean execution report is an input, not a verdict. The handbook should say plainly that the QA Lead reads the AC matrix and the evidence map before signing, every time, even when everything is green.

---

## 7. What I would pilot first

- **RRM-004 QA** as the first QAM run. It is the right shape: bounded (a dependency bump), high blast radius (so the regression plan matters), and every proof is mechanical (versions, audit, board, header re-capture, image walk). No new browser flows to invent.
- The Engineer supplies the manifest half at handoff, as he already does. The QA Lead writes the plan half from the handbook. The Director runs one command.
- Measure the same things the field note lists: wall-clock, Executor-active time, Director-active time, interruptions, preflight failures, product findings, repair rounds, helpers promoted. We now have RRM-002 and RRM-003 numbers to compare against.

---

## 8. Bottom line

Build it. The parts are proven, the folder shape is right, and the Director-as-authority-not-operator model has now held up across engineering and QA in real production modules.

Keep one line firm: **whoever built the candidate does not write the plan that tests it.** Let the Engineer hand over facts; let the QA seat decide how to attack them. Everything else in the proposal I would adopt as written.

— Architect, Cyber Pharma v1
