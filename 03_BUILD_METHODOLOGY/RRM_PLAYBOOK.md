# RRM PLAYBOOK
## Review Rework Modules — Adjudicated Review Findings into Bounded Repair and Independent Verification

> **Version:** 1.0 · **Date:** 2026-10-18 · **Status:** Active
> **Tier:** 3 — Build Methodology · **Pairs with:** `SOFTWARE_FACTORY_PLAYBOOK.md` › Module Identity & QA Handoff (Factory-level shared doctrine), `QAM_PLAYBOOK.md`, `QA_PLAYBOOK.md`, `BIM_PLAYBOOK.md` (module mechanics reference), `BUG_FIX_PLAYBOOK.md`, `FEAT_PLAYBOOK.md`, `FFM_PLAYBOOK.md`, `ARCHITECT_PLAYBOOK.md`, `ENGINEER_PLAYBOOK.md`, `HANDOFF_PACKAGE_PLAYBOOK.md`, `TESTING_PLAYBOOK.md`, `DEPLOYMENT_PLAYBOOK.md`
> **Owner:** Stark Industries App Factory
> **Provenance:** Authored for the Factory DocSet from the RRM pilot playbook v0.1 (17 September 2026; harvest source SRC-R01, preserved as received in INTAKE_SNAPSHOT/factory-intake/) and the RRM-001…004 field results (SRC-R03), reconciled to the Director rulings of 2026-10-14 (RUL-01 mandatory QAM, RUL-02 continuing QA branch, RUL-03 required cleanup, RUL-04 frozen contract with writable lanes, RUL-05 two review checkpoints, RUL-06 placement). The pilot playbook's persona names were replaced by seats; every departure from the pilot text is listed in the Version History. The pilot records themselves are unchanged.

---

## 1. What an RRM Does

A **Review Rework Module** converts adjudicated review findings into bounded engineering work and independent verification. Its scope comes from approved dispositions, not raw report counts. It can repair completed frontend, backend, cross-cutting or release work. It does not consume the identity of the next BIM, FIX or FEAT and it does not change a product's phase numbering.

Success means: the accepted repair objectives are verified, required existing behavior remains green, unresolved items have explicit dispositions, and the certified QA branch is properly closed out and merged. No RRM automatically proves an entire phase or application production-ready.

**Module identity** follows the Factory-level rule (`SOFTWARE_FACTORY_PLAYBOOK.md` › Module Identity & QA Handoff): `RRM-<NNN>-<APP-SLUG>`, uppercase canonical ID, lowercase-kebab branch. Mechanics shared with every module type — one folder, one manager file, Plan Mode, verify-first, Engineer read-only Git inspection, Director-only Git mutations, and existing context-specific cloud restrictions, baseline-first regression, per-module failure policy, Definition of Done — are documented in `BIM_PLAYBOOK.md` §4–§12 and apply by reference. **Every RRM includes a module-specific `QAM/`** (`QAM_PLAYBOOK.md`; Director ruling RUL-01 and RUL-05).

## 2. When an RRM Is Launched — the Two Review Checkpoints

The Factory has two planned independent-review checkpoints (Director ruling RUL-05, 2026-10-14):

1. **Review after FFM build and its independent QA finish**; disposition findings and authorize RRM only when approved findings require repair.
2. **Engine 2 review after all Engine 1 implementation phases and their QA are closed**, followed by approved RRM work. (Definitions and lifecycle vocabulary: `SOFTWARE_FACTORY_PLAYBOOK.md` §2, “Phase Vocabulary — One Canonical Map”.)

At each checkpoint: review findings require disposition (§5); approved findings determine the bounded RRM work; **a clean review produces no RRM** — repair work is never manufactured to fill a checkpoint. Review timing follows the approved project workflow; a review "both PASS" result defines neither Gate Q, Gate D nor release authority. Module QA certification (Gate Q), review completion and deployed-system verification (Gate D) remain distinct claims.

Revised workflow references: [FFM creation](_workflows/FFM_CREATION.md), [FFM execution and post-FFM review](_workflows/FFM_EXECUTION.md), [deployment and Gate D](_workflows/FFM_DEPLOYMENT.md), and [BIM through Engine 2](_workflows/BIM_WORKFLOW.md). Each includes a revised stick diagram and links its superseded original as history. The source diagrams are not current instructions.

## 3. Inputs and Entry Conditions

The project Architect gathers:

- the original review reports, prompts, evidence and specimen identities;
- the current application state and project instructions/contracts;
- completed module records, known limitations and already-approved decisions;
- the intended use/release context, relevant environments and permitted actions;
- this playbook, the reviewer guidance (§11) and the governing QA doctrine (`QA_PLAYBOOK.md`, `QAM_PLAYBOOK.md`).

**Current-source recon is mandatory before writing the executable packet** (`RECON_QUESTIONNAIRE.md`). A report about old code cannot establish a defect in today's candidate by itself. For a review that was performed without Git access, compare the pertinent source bytes or excerpts with current source and record unresolved equivalence. Missing equivalence does not invalidate all findings, but it prevents pretending that reviewer disagreement is a controlled comparison.

## 4. Lifecycle and Ownership

| Stage | Owner and action | Required exit evidence |
|---|---|---|
| Intake | Architect inventories reviews, specimens and limitations | Intake record and current-source reconciliation |
| Disposition | Architect proposes; Director rules | Every material finding has a reasoned disposition (§5) |
| Contract | Architect authors; Director approves; Architect instantiates `QAM/` from the Hub template set | Brief, frozen acceptance requirements, bounded engineering prompts, QAM skeleton |
| Plan / build | Engineer plans (Plan Mode), Director approves, Engineer implements and self-verifies | Execution log, engineering checks, factual `QAM/` handoff (`QAM_MANIFEST.md`, `HANDOFFS/ENGINEERING_HANDOFF.md`) |
| Candidate | Director commits/pushes the completed engineering work and creates `qa/<module-branch>` at that commit | Candidate SHA recorded by the QA Executor in Q1 |
| Q1 | QA Executor performs independent recon and drafts the test plan; QA Lead reviews and approves (with exact amendments if any); Director releases | Q1 review package; `QAM_APPROVAL.md` |
| Q2 | QA Executor executes the approved plan continuously on the QA branch | Evidence matrix, execution report, findings, result package |
| Repair loop (conditional) | QA Lead classifies; Architect/Director rule scope; Engineer repairs on the QA branch; Director commits; QA Executor re-pins and retests (Q4) | New candidate identity; bounded repair and regression evidence |
| Certification | QA Lead adjudicates and issues the Gate Q verdict | Acceptance and repair trace, limitations, verdict |
| Cleanup | QA Lead decides retention; authorized executor performs the required cleanup checkpoint (`QAM_PLAYBOOK.md` §14) | Cleanup report; durable records retained; debris handled |
| Closeout | Architect writes the closeout instruction; Engineer performs bounded closeout; Director reviews and commits | Closeout report, updated project status, clean tree |
| Merge / return | Director merges `qa/<module-branch>` into `main` and pushes; Architect returns lessons | Merge identity, journal inputs, deferred follow-ups |

The QA Lead and QA Executor enter at the QA handoff; they are not routine approvers of the Architect's engineering packet. One person may hold several seats; the responsibilities never merge (`QAM_PLAYBOOK.md` §3).

## 5. Disposition Before Repair

Use one primary disposition for every material source finding:

- **ACCEPT REPAIR** — a current, applicable problem with an approved objective.
- **NEEDS DECISION / EVIDENCE** — an unresolved requirement, deployment fact or contradictory evidence; name the owner and the resolving question.
- **DEFER / FUTURE GATE** — retained with reason, owner and a concrete trigger; state whether current approved use is affected.
- **REJECT / NOT APPLICABLE / ALREADY RESOLVED** — with current evidence and reason.
- **DUPLICATE** — mapped to the retained finding while preserving original IDs and distinct evidence.

Record accepted risk only through a Director decision, with conditions and follow-up. Reviewer severity does not automatically approve a repair or a deferral. Both reviewers agreeing is not proof; one reviewer finding something alone is not a reason to dismiss it. Separate severity, origin and approved scope: an inherited issue may be severe and still require an explicit disposition.

Raw reports stay unchanged. Corrections and rulings append in the disposition/errata lane. The ledger must distinguish a source observation from a current-project decision. No raw review item silently becomes an authorized edit.

## 6. Author the Engineering Contract

The Architect's packet contains a front door (the module manager, `BIM_PLAYBOOK.md` §5), the brief, the disposition ledger, the acceptance specification (`ACCEPTANCE_SPEC.md`, `SOFTWARE_FACTORY_PLAYBOOK.md` §2.5), the engineering prompts and the instantiated `QAM/`. Requirements are settled before the build. The Engineer delivers the acceptance artifact with the completion handoff but may not redefine success after implementation. Separate required behavior from engineering claims and from QA verdicts.

Each accepted objective maps to numbered ACs, preserved behavior, allowed surfaces, forbidden scope, verification level/environment and required evidence. **The contract is frozen at handoff; declared lanes inside the module (engineering handoff, recon, plans, evidence, findings, approved rulings) stay writable by their owners; contract changes require an attributable approved amendment in the append-only errata lane** (Director ruling RUL-04). No unresolved blocking decision enters implementation as an invented assumption.

Place the module under the project's established `agent_docs/` module convention; its QA records live in the module's `QAM/` structure (Director ruling RUL-03). Use staged prompts when dependency changes, schema work or distinct risks require checkpoints. Small related findings may share one RRM; split when independence, rollback or verification needs justify it.

## 7. Engineering and Branch Flow

The Director starts from the approved current `main` baseline under project Git discipline. The Engineer performs Plan Mode inspection and reports conflicts before writes; the Director approves the plan and checkpoint progression; the Engineer implements only allowed work, verifies it, and logs changes, commands, outcomes, limitations and affected ACs. The Engineer may inspect Git read-only; the Director performs every Git mutation. Existing context-specific cloud restrictions remain in force; this document grants no new cloud permission.

**Branch flow (Director ruling RUL-02):** the module has a numbered engineering branch (for example `rrm-001-<app>`). After Engineering, the Director commits and pushes the completed engineering work and creates the matching `qa/<module-branch>` **at that same commit** — the completed engineering candidate. The Engineer performs authorized rework on that QA branch; the QA Executor independently tests on that same branch; role boundaries are preserved and conflicting simultaneous writes are avoided (one active writer when sessions share a worktree). The QA Lead certifies the governed candidate; the Architect issues the closeout instruction; the Engineer performs bounded closeout; the Director commits, merges the QA branch into `main` and pushes `main`. **Repairs are not transferred back to the engineering branch and the QA branch is not abandoned as the normal workflow.** Product, execution, evidence and closeout identities are preserved separately.

Review-only exports are separate input artifacts; their lack of `.git` does not change engineering's Git discipline. This is project-module policy; the Doctrine Hub's own synchronization Git rules are separate (`DEPLOYMENT_PLAYBOOK.md` §3).

## 8. QA Handoff and Verification (the QAM interface)

Every RRM includes QAM: the Architect instantiates `QAM/` from the Hub template set at packaging; the Engineer completes the factual manifest and engineering handoff as part of the engineering assignment; the QA Executor performs Q1 (independent recon and test plan) and, after QA Lead approval and Director release, Q2 (continuous execution); the QA Lead adjudicates findings and certifies (`QAM_PLAYBOOK.md` §§5–14). The handoff supplies the approved spec and execution log plus references to the brief, the disposition ledger, the exact candidate commit, the repair diff, engineering results, fixtures/environment setup, limitations and the governing QA instructions (carried in `QAM/GOVERNING/` with version and hash provenance).

Tests must reach the boundary claimed: a direct function probe is not automatically a framework HTTP test; a synthetic database substitute is not deployed RLS evidence. Browser, SQL and deployment checks are required only where the approved contract or the QA risk plan needs them; report gaps instead of claiming success.

**Trace:** source finding ID → disposition → AC → repair → test/evidence → final disposition. Required regression establishes that protected existing behavior still works. Targeted re-review by the original reviewer can strengthen the evidence; the QA Lead specifies when it is required and who can satisfy it. A closed reviewer session does not invalidate the report or require resuming the same model instance.

The QA Executor records PASS, FAIL, BLOCKED, NOT RUN or ADJUDICATE with evidence; its recommendation is not the QA Lead's certificate. Verdict vocabulary is the Factory set in `QA_PLAYBOOK.md` §11; outstanding mandatory checks cannot be relabeled passed.

## 9. Repair / Retest Loop (conditional)

QA Executor reports → QA Lead classifies → Architect/Director resolve scope or contract questions and issue a bounded repair instruction → Engineer executes the approved repair on the QA branch → Director commits → QA Executor re-pins and retests (Q4) → QA Lead re-adjudicates (`QAM_PLAYBOOK.md` §11).

A repair instruction names the affected findings/ACs, allowed files, prohibited changes and required engineering checks. Retest covers the diff, the impacted ACs and the required regression. Unchanged evidence may carry forward with explicit specimen provenance and impact reasoning. Do not restart the entire campaign without a concrete reason. New material issues require a disposition; no quiet scope expansion and no moving acceptance criteria to fit the implementation. Required final live validation runs against the final candidate after outstanding failures are resolved and the QA Lead authorizes it.

The RRM-001…004 campaign did not exercise a product repair round; this loop carries forward the governing doctrine and is not a capability proved by that pilot.

## 10. Certification, Cleanup, Closeout and Merge

The QA Lead's Gate Q verdict certifies the implementation against the approved contract: it records the exact implementation SHA, accepted errata, results, preserved behavior, gaps and any Director-approved follow-ups. It does not certify deployment and it does not eliminate deferred findings.

**Sequence for every module with a `QAM/` (Director ruling RUL-03; `QAM_PLAYBOOK.md` §14):** accepted product verdict (QA Lead) → required cleanup under QA Lead authority, with records (credential and temporary auth-state hygiene; closing owned QA processes and browser contexts; authorized removal of disposable execution debris; retention of durable evidence, required attempts and useful helpers) → durable records committed (Director) → Architect closeout instruction → bounded Engineer closeout → Director merge of `qa/<module-branch>` into `main`. Product Gate Q, cleanup acceptance and Gate D remain separate claims. Verify that cleanup changed no product, test, configuration or contract bytes; a product change found at cleanup returns through QA, never buried in cleanup or closeout.

The closeout record distinguishes implementation, evidence, closeout and merge SHAs where they differ. Do not loop adding a commit's own hash to itself. After merge, the Director refreshes local `main` before any new branch starts. Required deployment and Gate D remain separate (`DEPLOYMENT_PLAYBOOK.md`; `QA_PLAYBOOK.md` §13).

## 11. Reviewer Guidance

Reviewer guidance belongs here under RUL-14 (2026-10-16). The reviewer guidance below governs review; pilot source records remain unchanged.

- **Freeze the specimen.** Name the exact revision, export or byte set reviewed; distinguish ordinary change review from broad or retrospective investigation.
- **Evidence levels.** Label every claim EVIDENCE / INFERENCE / CLAIM / GAP / QUESTION (`QA_PLAYBOOK.md` §8); state the conditions under which a finding holds and what would falsify it.
- **Origin ≠ severity.** Separate inherited origin from severity; disclose baseline failures without preventing security investigation; an inherited severe issue still needs a disposition.
- **No unsupported security claims.** A missing application-level filter is not a confirmed exposure when RLS or another effective boundary may apply; say what was and was not verified.
- **Calibrate.** State claim confidence and specimen equivalence; one severe, supported issue warrants correction — a repeated-incident threshold is not required.
- **Route, do not repair.** Reviewers propose; disposition is the Architect's proposal and the Director's ruling (§5). Original reports stay unchanged; dispositions and errata append.

## 12. Continuous Execution Within a Released Assignment

Under RUL-15 (2026-10-16), execute continuously within a released assignment, including routine checks, reporting and packaging. Stop for concrete blockers, authority changes or required independent verdicts. This is not permission to cross a release boundary.

Prepare measurable scope, prerequisites, writable lanes and enumerated stops before release. Once released, include routine checks, reporting and packaging in continuous execution. Preserve required independent verdicts and authority boundaries. Report the full lifecycle effort, interruptions, repairs and missing-package follow-ups; never omit a valid stop to claim uninterrupted success.

## 13. Return Learning

The project returns a concise retrospective: what was accepted, rejected or deferred and why; surprises in execution; the evidence needed to resolve disagreements; rework rounds and their causes; process friction; proposed doctrine changes. Attribute seat-authored lessons. Promote only supported lessons through the DocSet Sync process (`_SKILLS/factory-docs-update/`); a lesson is not doctrine until it lands in the Hub.

An RRM is complete only after actual delivery, QA and closeout evidence exists. Receipt of reviews and publication of a packet are preparation milestones, not a completed RRM.

## 14. Version History

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-10-18 | New doc entering Hub: Review Rework Module doctrine, authored from the RRM pilot playbook v0.1 (SRC-R01) and field results (SRC-R03) under the Director rulings of 2026-10-14. Departures from the pilot text: §1 module identity per SFP §2.5 and mandatory QAM (RUL-01/05); §2 new — two review checkpoints, clean review → no RRM (RUL-05); §4 lifecycle re-seated (Engineer / QA Lead / QA Executor / Director / Architect) with Q1/approval/release/Q2 and the RUL-03 sequence; §6 frozen contract with writable lanes (RUL-04), kit reference replaced by the Hub template set and the module's `QAM/`; §7 branch flow restated from RUL-02 (no `--no-ff` project policy as Hub policy); §8 QAM interface; §10 cleanup-before-closeout sequence (RUL-03) replacing the pilot's "Gate Q then cleanup" wording; §11 reviewer guidance as a section; §12 continuous execution within released scope (RUL-15); §13 promotion via DocSet Sync. [IN-2026-10-15-13 … IN-2026-10-15-22 (RRM-01…10); WF-11; WF-07; RUL-01…RUL-06]; current correction pass: MC-01…14; RUL-05, RUL-06, RUL-14, RUL-15 |
