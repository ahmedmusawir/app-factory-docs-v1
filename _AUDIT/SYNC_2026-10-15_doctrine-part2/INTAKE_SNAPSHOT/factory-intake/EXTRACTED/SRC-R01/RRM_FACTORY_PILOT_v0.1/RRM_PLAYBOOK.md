# Review Rework Module Playbook

**Version 0.1 · 17 September 2026 · Pilot procedure**  
**Owner:** JARVIS Master HQ for reusable method; project Architect for each executable RRM; Tony for approval.

## 1. What an RRM does

An RRM converts adjudicated review findings into bounded engineering work and independent verification. Its scope comes from approved dispositions, not raw report counts. It can repair completed frontend, backend, cross-cutting or release work. It does not consume the identity of the next BIM or change a product's phase numbering.

Success means accepted repair objectives are verified, required existing behavior remains green, unresolved items have explicit dispositions, and the certified branch is properly closed out. No RRM automatically proves an entire phase or application production-ready.

## 2. Inputs and entry conditions

The project Architect gathers:

- Original review reports, prompts, evidence and specimen identities.
- Current application state and project instructions/contracts.
- Completed module records, known limitations and already-approved decisions.
- Intended use/release context, relevant environments, and permitted actions.
- This pilot playbook, reviewer guidance and established engineering/QA doctrine.

Current-source recon is mandatory before writing the executable packet. A report about old code cannot establish a defect in today's candidate by itself. For a Git-free review, compare pertinent source bytes/excerpts with current source; record unresolved equivalence. Missing equivalence does not invalidate all findings, but it prevents pretending that reviewer disagreement is controlled comparison.

## 3. Lifecycle and ownership

| Stage | Owner and action | Required exit evidence |
|---|---|---|
| Intake | Architect inventories reviews, specimens and limitations | Intake record and current-source reconciliation |
| Disposition | Architect proposes; Director rules | Every material finding has a reasoned disposition |
| Contract | Architect authors; Director approves | Brief, frozen acceptance requirements, bounded engineering prompts |
| Plan/build | Claudy plans, Tony approves, Claudy implements | Execution log, engineering checks, candidate identity |
| QA entry | Director opens qa/<module>; SOL plans; Cody executes | Independent test matrix and results |
| Repair loop | Architect rules when needed; Claudy repairs; Cody retests | New candidate identity and bounded repair/regression evidence |
| Certification | SOL adjudicates and issues Gate Q | Acceptance and repair trace, limitations and verdict |
| Cleanup | SOL selects durable package; authorized executor performs hygiene; Tony controls Git | Durable records retained; debris handled; clean tree |
| Closeout | Architect writes prompt; Claudy executes; Director reviews and commits | Closeout report, updated project status, clean tree |
| Merge/return | Director merges/pushes; Architect returns lessons | Merge identity, journal inputs, deferred follow-ups |

SOL/Cody enter at QA handoff, not as routine approvers of the Architect's engineering packet. HQ may advise on factory method without taking over project scope authority.

## 4. Disposition before repair

Use one primary disposition for every material source finding:

- **ACCEPT REPAIR:** current applicable problem with an approved objective.
- **NEEDS DECISION/EVIDENCE:** unresolved requirement, deployment fact or contradictory evidence; name owner and resolving question.
- **DEFER / FUTURE GATE:** retain with reason, owner and concrete trigger; state whether current approved use is affected.
- **REJECT / NOT APPLICABLE / ALREADY RESOLVED:** attach current evidence and reason.
- **DUPLICATE:** map to the retained finding while preserving original IDs and distinct evidence.

Record accepted risk only through a Director decision, with conditions and follow-up. Reviewer severity does not automatically approve a repair or a deferral. Both reviewers agreeing is not proof; one reviewer finding something alone is not a reason to dismiss it.

Raw reports stay unchanged. Corrections and rulings append in the disposition/errata lane. The ledger must distinguish a source observation from a current-project decision.

## 5. Author the engineering contract

Use RRM_MODULE_KIT. Choose a project-consistent identity, for example <app>-p<phase>-rrm<NNN>, only after verifying existing numbering. The example is not a mandated Cyber Pharma ID. Folder, branch and packet names should align. Prefer the established agent_docs/ACTION/<module>/ convention where the project confirms it.

The Architect's packet contains a front door, brief, disposition ledger, acceptance specification and engineering prompts. Requirements are settled before build. Claudy delivers the acceptance artifact with his completion handoff, but may not redefine success after implementation. Separate required behavior from engineering claims and QA verdicts.

Each accepted objective maps to numbered ACs, preserved behavior, allowed surfaces, forbidden scope, verification level/environment, and required evidence. Leave an append-only errata lane for approved changes or interpretations. No unresolved blocking decision enters implementation as an invented assumption.

Use staged prompts when dependency changes, schema work or distinct risks require checkpoints. Small related findings may share one RRM; split when independence, rollback or verification needs justify it. Do not force every report item into this pilot.

## 6. Engineering and branch flow

Director starts from the approved current main baseline, following project Git discipline. Claudy performs Plan Mode inspection and reports conflicts before writes. Director approves the plan and checkpoint progression. Claudy implements only allowed work, verifies it, and logs changes, commands, outcomes, limitations and affected ACs. Tony performs or explicitly authorizes mutating Git/cloud operations.

Normal flow: main → RRM engineering branch → qa/<module> → main. After QA handoff the QA branch is the active certification line; the original engineering branch remains the historical handoff point. All approved QA-driven repairs happen on the QA line. Do not bounce between branches or create a disposable probe branch by default.

Review-only exports are separate input artifacts. Their lack of .git does not change engineering's Git discipline.

## 7. QA handoff and verification

Supply the approved spec and execution log, plus references to the brief/disposition ledger, exact candidate commit, repair diff, engineering results, fixtures/environment setup, limitations and governing QA instructions. Include the relevant QA playbook snapshot inside the repo so Cody need not depend on outside-repo access.

SOL prepares a risk-based test plan. Cody independently verifies implementation claims and accepted finding resolution, including required positive and negative controls. Tests must reach the relevant boundary: a direct function probe is not automatically a framework HTTP test; a synthetic database substitute is not deployed RLS evidence. Browser/SQL/deployment checks are required only where the approved contract or QA risk assessment needs them; report gaps instead of claiming success.

Trace: source finding ID → disposition → AC → repair → test/evidence → final disposition. Required regression establishes that protected existing behavior still works. Targeted re-review by the original reviewer can strengthen the evidence; SOL specifies when it is required and who can satisfy it. A closed reviewer session does not invalidate the report or require resuming the same model instance.

Cody records PASS, FAIL, BLOCKED, UNTESTED or adjudication-needed with evidence. Cody's recommendation is not SOL's certificate. Applicable QA verdict vocabulary remains governed by the project's QA playbook; outstanding mandatory checks cannot be relabeled passed.

## 8. Repair/retest loop

Cody reports → SOL classifies → Architect/Director resolve scope or contract questions → Claudy executes approved repair → Director commits → Cody re-pins and retests → SOL re-adjudicates.

A repair instruction names affected findings/ACs, allowed files, prohibited changes and required engineering checks. Retest covers the diff, impacted ACs and required regression. Unchanged evidence may carry forward with explicit specimen provenance and impact reasoning. Do not restart the entire campaign without a concrete reason.

New material issues require a disposition. No quiet scope expansion and no moving acceptance criteria to fit the implementation. Required final live validation runs against the final candidate, after outstanding failures are resolved and SOL authorizes it.

## 9. Certification, cleanup and closeout

Gate Q certifies the implementation against the approved contract. Record the exact implementation SHA, accepted errata, results, preserved behavior, gaps and any Director-approved follow-ups. This does not certify deployment or eliminate deferred findings.

Then perform QA Cleanup: preserve final reports, necessary reproducible evidence, adjudications and certification provenance; discard or intentionally exclude transient workspaces, caches and one-use debris. Review files deliberately before staging. Check for sensitive data, unintended large artifacts, escaped helpers and runtime dependencies on QA material. Do not delete required reproduction evidence merely because it is a script.

Verify no product/test/contract changes were introduced by cleanup, record durable evidence commits and ensure the working tree is clean. If a product change is needed, return it through QA; do not bury it in cleanup or closeout.

Only then does the Architect issue the final closeout prompt. Claudy updates the agreed project records and reports completion. Tony inspects, commits and merges the QA branch under project policy (currently --no-ff with a message), then pushes. The closeout record distinguishes implementation, evidence, closeout and merge SHAs where they differ. Required deployment and Gate D remain separate.

## 10. Return learning to HQ

The project returns a concise retrospective: what was accepted/rejected/deferred and why, surprises in execution, evidence needed to resolve disagreements, rework rounds and their causes, process friction, and proposed doctrine changes. Attribute seat-authored lessons. Promote only supported lessons via the controlled doc-set sync process.

This pilot is complete only after actual delivery/QA/closeout evidence exists. Receipt of two reviews and publication of this playbook are preparation milestones, not a completed RRM.
