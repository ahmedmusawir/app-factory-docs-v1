# APP FACTORY — BIM OPERATING MODEL
## Loop 2: BIM Set Planning → Execution → Independent QA → Close

> **Version:** 1.0 · **Date:** 2026-08-24
> **Status:** REVIEW — Operator rulings ratified; full operating-model text pending final Operator approval.
> **Tier:** 1 — Factory Operating Model · **Owner:** Stark Industries App Factory
> **Provenance:** Field-derived from the ADK Harness BIM campaign (BIM-001…005, FIX-001…003, FEAT-001 — origin of the factory's independent QA model) and the Cyber Pharma Phase 3 BIM set (ongoing), where the Codex-executed QA model was proven in live runs: manual CLI under QA Lead direction → scripted CLI → QA-Engineer-authored and -executed scripts. Ratified inputs: four Operator rulings issued 2026-08-24 against the BIM Workflow diagram.
> **Companion visual:** APP FACTORY: BIM WORKFLOW diagram (Whimsical). The diagram is a simplified process map; **this document is the full contract. Diagram omission does not mean process omission.** Where they differ, this document wins.
> **Sibling doc:** `APP_FACTORY_FFM_OPERATING_MODEL_v1.0.md` (Loop 1). Shared laws are stated once there where noted.

---

## 1. Executive Explanation — What a BIM Is

A **BIM — Backend Integration Module** — is the factory's vehicle for making backend reality exist behind an established contract: databases, APIs, integrations, auth wiring, external services, business logic.

BIMs live primarily in **Loop 2 — MATURE**: the loop that answers *"Can we transform the approved product shell into the secure, integrated, production-capable system?"* Where the FFM builds the frontend against a service seam with mock data, the BIM makes the seam real — the mock implementations are replaced by genuine backend implementations **without rewriting the UI**, because both sides honor the same approved contract.

The BIM's center of gravity is therefore the **seam/contract**, not the screen. Its truth is textual — contracts, schemas, endpoint shapes, command output — which is why the BIM package is denser and leaner than the FFM package, and why its QA execution is machine-verifiable rather than browser-visual.

BIMs ship in **sets**: a named, sequenced campaign of scoped modules (BIM000, BIM001, BIM002…) advancing one backend concern at a time. No mega-modules.

---

## 2. The Human Control Model — Teams and Seats

**Blue Team** (builds) is the combination of three functions: **Architecture + Engineering/Development + Design**. **Red Team** (verifies) is **QA**. *(Ruled 2026-08-24.)*

> Terminology, ruled: **"Engineering" and "Development" are interchangeable** — the Director of Engineering and the Director of Development are the same chair.

```text
BLUE TEAM — builds                      RED TEAM — verifies

Director of Engineering                 Director of QA
        +                                       +
BIM Architect (AI advisory)             QA Lead (AI advisory)
        ↓                                       ↓
Engineer (AI execution)                 QA Engineer (AI execution)
        ↓                               runs scripts + commands via CLI
BUILD                                           ↓
                                        evidence → QA Lead → VERDICT
```

**Seats over models — ruled.** Seats are defined by responsibility; models are variables. The current occupants (Engineer: Claude Code "Claudy"; QA Lead: GPT-class "Sol"; QA Engineer: Codex) are deployment choices, not doctrine. The Operator assigns the best available model to each seat; the contracts between seats survive model changes. Diagram labels naming specific models describe current occupants only.

In BIM work, unlike canonical FFM QA, the QA department runs at **full three-seat configuration**: human Director, AI QA Lead, AI QA Engineer. BIM evidence is predominantly CLI/script/database-verifiable — exactly the terrain where an AI execution seat outperforms manual operation.

The Director remains the human authority: approves scope and plans, adjudicates, owns git and cloud actions, and can personally execute work. **An Engineer is never unleashed unsupervised.**

---

## 3. Stage 0 — Fresh Recon (per module)

Factory law (shared with Loop 1; see sibling doc §3): **no current Recon Report → no authoring.** For BIMs this is per-module: each BIM begins with a **fresh recon** of the repo's current state, because the previous module changed that state.

- Recon is read-only; the Engineer is the ground-truth instrument.
- Where docs and disk disagree, **disk wins**.
- The Architect authors the module from the current Recon Report, never from memory of the last one.

---

## 4. The BIM Set — planning and authoring patterns

A BIM campaign begins with the Architect and Director of Engineering defining the **set**: named modules in sequence (BIM000…BIMnnn), each scoped to one backend concern.

**Two authoring patterns are permitted — ruled:**

1. **Author-all-upfront:** the full set is authored before execution begins. Suited to short, well-understood sets.
2. **Plan-names / author-just-in-time:** the set is planned and named upfront; each module is authored one at a time, after the prior module's retrospective lands. Suited to longer or discovery-heavy campaigns — the next module inherits the last module's lessons.

The Operator chooses the pattern per campaign. In both patterns, execution is strictly **one module at a time**, and every module closes with a retrospective before the next executes.

---

## 5. The BIM Package (per module)

```text
<project>_bim_<nnn>/
├── CLAUDE.md                    ← module manager (always required)
├── MODULE_BRIEF.md              ← larger modules
├── DATA_CONTRACT_AMENDMENT.md   ← only when wire contracts change
├── ACCEPTANCE_SPEC.md           ← always required
├── RETROSPECTIVE.md             ← always required at close
└── (stage artifacts as ruled)
```

Small modules may fold the brief and contract amendment into the manager — **manager, acceptance spec, and retrospective are never optional.**

The manager (CLAUDE.md) carries the module's full informed state: status, mission, verified ground with provenance, rulings, TO-VERIFY-FIRST items, scope, forbidden zones, numbered engineering gates, Plan Mode requirements, definition of done, and stop condition. Density substitutes for folder breadth: the living repo is the BIM's visual ground truth.

---

## 6. Execution Flow (Blue Team)

```text
Fresh Recon (Stage 0)
   ↓
Architect authors the FINAL module package
   ↓
Director of Engineering approves scope
   ↓
Engineer — Plan Mode (no build yet)
   ↓
Architect plan-QA (advisory verification)
   ↓
Director approves the plan
   ↓
Engineer implements — one module, narrow scope, zero git/cloud commands
   ↑ supervision throughout: Director (approvals & directions) + Architect (verification & advisory)
   ↓
Engineer self-verifies
   ↓
ACCEPTANCE_SPEC.md finalized (AC-numbered claims; prerequisites first)
   ↓
Module handoff to QA
```

Internal stage gates are Development gates — supervision instruments, never Gate Q. The acceptance contract rules are shared law with Loop 1 (sibling doc §6): seeded from the approved module contract, Engineer-finalized, never silently weakened. *The Engineer does not grade his own paper, and does not write his own exam either.*

---

## 7. Independent QA — the canonical BIM QA flow

**Canonical QA source:** `QA_PLAYBOOK.md` (independence, Gate Q §12, Gate D §13, verdict vocabulary). BIM applies that doctrine within its module class.

### 7.1 Flow — full three-seat Red Team

```text
ACCEPTANCE_SPEC.md
   ↓
QA Lead designs the independent attack:
   test plan · test cases · happy paths · negative paths · transitions · environment reality
   ↓
QA ENGINEER (AI execution seat) authors and runs the attack:
   scripts · CLI commands · database checks · machine-verifiable evidence
   ↓
Test results return via CLI evidence to the QA Lead
   ↓
QA Lead adjudicates and issues the verdict + QA report
   ↓
FAIL → Engineering (FIX loop, under Development supervision) → QA retest
PASS → GATE Q → module certified
```

The Director of QA drives the run, provisions environment/access, approves the QA plan's execution, and may execute steps personally where judgment or physical access demands it. The QA Lead owns the verdict. **Verdict vocabulary:** PASS / PASS WITH FOLLOW-UP FINDINGS / PASS WITH KNOWN RISK / FAIL / BLOCKED.

### 7.2 Provenance of this model (evidence, not theory)

The three-seat model was reached through field iteration on Cyber Pharma Phase 3: (1) the QA Lead walked the Director through manual CLI testing; (2) repeatable operations were converted to scripts to save time; (3) the QA Engineer seat was introduced to author and run the scripts directly — and it worked. The QA department found its execution seat the same way the QA department itself was found: through real BIM friction. This is the canonical BIM QA configuration going forward.

---

## 8. QA Branch Doctrine — disposable by design (ruled 2026-08-24)

QA execution happens on a **dedicated QA branch**. That branch is scaffolding, not product.

**Default: ABANDON the QA branch after the QA report is issued. Do not merge. Do not clean up for merge.** Cleanup labor buys nothing; test debris never belongs in the product tree.

Three guardrails must be satisfied before the branch dies:

1. **Harvest the scripts.** QA-Engineer-authored test scripts are regression assets for future BIMs, FIX runs, and eventually TRM. They are copied out of the branch into the designated QA assets location before abandonment (location: open item — §13).
2. **Record the tested identity.** The QA report records the exact commit SHA the attack ran against. **Certified-revision law:** the revision QA certified must be the revision that ships. The QA branch must be product-identical to the target branch (product code unchanged; scaffolding only) — verify this each run. If product code diverged, the branch cannot simply be abandoned.
3. **Fixes never die with the branch.** Any defect fixed during the QA run lands on the product branch through the FIX loop — never stranded on the disposable branch.

Merge becomes the exception, used only when the branch deliberately carries product-bound changes — at which point it is no longer a QA branch and normal review applies.

---

## 9. Gate Q, Gate D, and Release Authority

- **Gate Q** (per `QA_PLAYBOOK.md` §12): sits after Engineer self-verification, before release approval. Mandatory for all code-bearing modules; QA reviews completed, frozen work; symmetric evidence bar; a Gate D plan exists before any deployment.
- **Gate D** (per `QA_PLAYBOOK.md` §13): deploy-requiring modules verify the actual deployed revision — QA Lead designs the verification, execution per module class (QA Engineer for machine-verifiable checks; Director for manual/environment checks), DevOps supplies the release identity chain and rollback path, QA Lead adjudicates. No deployment in scope → recorded "Gate D: N/A — reason." A deploy-requiring module is never CLOSED before its Gate D.
- **Release authority** (shared law; sibling doc §9): QA owns the verification verdict; human authority owns the release decision; departmental approval is not final release authorization.

Module close requires: verdict issued → Gate D satisfied or N/A → RETROSPECTIVE.md written → lesson candidates flagged for doctrine promotion.

---

## 10. Full Role Roster (BIM)

| Seat | Kind | Team | Duty |
|---|---|---|---|
| Director of Engineering (= Development) | Human | Blue | Approves set, scope, and plans; directs the run; owns git; carries context |
| BIM Architect | AI advisory | Blue | Fresh-recon-based module authoring; plan-QA; verification & advisory throughout |
| Engineer | AI execution | Blue | Plan Mode → build → self-verify → ACCEPTANCE_SPEC → retrospective; zero git/cloud |
| Director of QA | Human | Red | Drives the QA run; provisions environment/access; approves attack execution; manual steps where required |
| QA Lead | AI advisory | Red | Independent attack design; evidence adjudication; owns the verdict |
| QA Engineer | AI execution | Red | Authors and runs scripts/CLI/database checks under the QA Lead's strategy |
| Operator (final release authority) | Human | Factory | Authorizes release beyond departmental approvals; final adjudication |

Current occupants (variables, not doctrine): Engineer — Claude Code "Claudy"; QA Lead — GPT "Sol"; QA Engineer — Codex.

---

## 11. Artifact Registry (BIM)

| Artifact | Canonical filename | Produced by | Consumed by |
|---|---|---|---|
| Recon Report | `agent_docs/recon/RECON_<project>_<phase>_<date>.md` | Engineer (read-only) | Architect, Director |
| Module manager | `CLAUDE.md` (in module folder) | Architect | Engineer |
| Module brief | `MODULE_BRIEF.md` (larger modules) | Architect | Engineer |
| Contract amendment | `DATA_CONTRACT_AMENDMENT.md` (only when wire contracts change) | Architect | Engineer, QA |
| Acceptance contract | `ACCEPTANCE_SPEC.md` | Seeded by contract; Engineer finalizes | QA Lead |
| QA plan / test cases | `QA_PLAN.md` + test case set | QA Lead | QA Engineer, Director of QA |
| QA scripts | harvested per §8 (location: open item) | QA Engineer | Future QA runs, regression |
| QA verdict/report | Per `QA_PLAYBOOK.md` | QA Lead | Directors, Operator |
| Retrospective | `RETROSPECTIVE.md` | Engineer | Next module's Architect |

---

## 12. Amendment Ledger

**A — Existing doctrine already aligned**

- A-1 · Module lifecycle, package anatomy, small-module folding, fresh-recon-per-module, plan-QA chain — `BIM_PLAYBOOK.md` §§2–8.
- A-2 · QA doctrine: independence, gates, verdicts — `QA_PLAYBOOK.md` (canonical), BIM as implementing class.
- A-3 · Engineer conduct: Plan Mode, zero git/cloud, narrow scope — `ENGINEER_PLAYBOOK.md`.

**C — Operator rulings that clarify**

- C-1 · **"Engineering" = "Development"** — interchangeable department names, one chair. New Tier-1 docs may use either; this doc pair uses both with the equivalence stated.
- C-2 · **Blue Team composition** — Architecture + Engineering/Development + Design collectively constitute the Blue Team.
- C-3 · **Seats over models** — seat responsibilities are doctrine; model assignments (Claudy, Sol, Codex) are variables chosen by the Operator.
- C-4 · **BIM set authoring patterns** — author-all-upfront and plan-names/author-just-in-time are both sanctioned; Operator chooses per campaign; one-module-at-a-time execution and retrospective-before-next are invariant.

**D — Newly introduced doctrine**

- D-1 · **QA Engineer as canonical BIM QA execution seat** (§7) — three-seat Red Team is the standard BIM configuration. Extends the sibling doc's D-2 (where Codex was reserve-only for FFM).
- D-2 · **QA Branch Doctrine** (§8) — disposable QA branches, abandon-by-default, three guardrails (script harvest, tested-identity record + certified-revision law, fixes via FIX loop). New; no prior playbook covers QA branch lifecycle.

**F — Open items** → §13.

---

## 13. Open Items (fenced — NOT v1.0 doctrine)

- F-1 · **QA script harvest location** — canonical destination for harvested QA scripts (`qa/` folder in repo vs module folder vs factory-level QA assets repo). Needs ruling.
- F-2 · **BIM package upgrades** (carried from factory ledger): standing `verification/` folder and example payload/fixture battery as package elements — `BIM_PLAYBOOK` v1.1 candidates; evidence pass over BIM-001…005 + Cyber Pharma Phase 3 set first.
- F-3 · **Gate D execution split for BIM** — precise boundary between QA-Engineer-executed and Director-executed Gate D checks; current text states the principle, mechanics to be hardened from the next deploy-requiring BIM.
- F-4 · **TRM routing** — production tickets routing into BIM (integration-class issues) awaits DockBloxx evidence; out of scope here.

---

## 14. Definition of Done — per BIM

- [ ] Fresh Recon Report obtained and reviewed before authoring
- [ ] Module package authored FINAL by the Architect; scope approved by the Director
- [ ] Engineer Plan Mode → Architect plan-QA → Director plan approval → build
- [ ] Engineer self-verification recorded; `ACCEPTANCE_SPEC.md` finalized
- [ ] QA Lead designed the attack; QA Engineer executed; evidence returned; verdict issued
- [ ] **Gate Q: PASS**
- [ ] QA branch: scripts harvested · tested SHA recorded · certified-revision law verified · fixes landed via FIX loop · branch abandoned
- [ ] Gate D satisfied for deploy-requiring modules (or recorded N/A with reason)
- [ ] `RETROSPECTIVE.md` written honestly; lesson candidates flagged for promotion
- [ ] Next module authored only after this retrospective lands (just-in-time pattern) or next module in the pre-authored set released for execution

**Done looks like:** a reader who has never seen our conversations can trace a backend concern from set planning through fresh recon, module authoring, supervised engineering, a three-seat independent QA attack, and a disposable QA branch — to a certified, retrospected module close, knowing who owns every decision and which artifact crosses every boundary.

---

## 15. Version History

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-08-24 | Initial operating model. Consolidates the BIM Workflow diagram, four Operator rulings (seats-over-models, Engineering=Development + Blue Team composition, dual set-authoring patterns, QA branch abandonment doctrine), the field-proven three-seat Red Team, and `BIM_PLAYBOOK.md`/`QA_PLAYBOOK.md` alignment into one Tier-1 document. Status REVIEW pending Operator ratification. |
