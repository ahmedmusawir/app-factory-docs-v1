# ABM PLAYBOOK — APPLICATION BUILD MODULE

**Version:** 1.0  
**Date:** 2026-10-17 · Asia/Dhaka  
**Authoring seat:** JARVIS / Architect  
**Director:** Tony Stark  
**Audience:** Module-writing Architects, Engineers, QA Leads, QA Executors and the Factory Doc Sync Architect  
**Status:** Complete authoring baseline for Factory integration. This file does not claim that existing repositories, skills or Factory manuals have already been synchronized.  
**Pilot evidence:** Web Factory scraper: scoped Gate Q PASS, cleanup accepted and integrated into main. Director ride and final product acceptance remain pending.

## 1. The operating promise

An ABM packages one bounded application or tool outcome so an Engineer can implement it continuously, verify it and hand it to independent QA without the Director managing every internal task.

The normal path is:

**Prepare a complete contract → approve one engineering plan → build and self-verify continuously → QAM Q1 → Lead approves the plan and Director releases Q2 → QAM Q2 → conditional repair/retest → certification and required cleanup → Architect closeout → Director integration and acceptance.**

The objective is fewer coordination steps with dependable results. Internal tasks, tests and progress records remain. They do not become separate human approval rounds unless a real decision or explicit gate requires it.

“One shot” means one coherent authorized engineering assignment, including its self-checks and factual QA handoff. It does not promise one model response, one context window, no failures or no recovery.

“Two-shot QA” means two planned independent execution assignments: Q1 planning and Q2 execution. Lead adjudication, Director release, conditional repairs, cleanup and Git handling remain distinct responsibilities.

This playbook owns ABM packaging and engineering orchestration. **QAM_PLAYBOOK_v1_0.md owns the independent QA process.** Reuse that process; do not invent an ABM-specific competing QA framework.

## 2. When to use ABM

Use ABM when the intended outcome can be expressed as one coherent contract, its major dependencies are understood, and an independent QA campaign can meaningfully judge the integrated result.

| Situation | Routing |
|---|---|
| Small application or standalone tool with bounded inputs/outputs | ABM |
| Existing tool being substantially completed within a clear boundary | ABM with brownfield baseline and preserved-behavior contract |
| Large application needing separately approved, certified phases | APBM / phase-based application delivery |
| Narrow defect, feature or rework assignment | Existing FIX/FEAT/RRM route, as defined by the Factory |
| Uncertain feasibility or unresolved architecture | Bounded investigation/prototype before freezing implementation |
| UI/full-stack outcome | Approved design and frontend contract, with any required FFM gate explicitly declared |
| Backend-only outcome | Mark UI/design requirements not applicable with rationale; do not manufacture an FFM |

The September v0.1 ABM drafts bundled application-wide phase plans and per-phase modules into ABM. This edition separates the single bounded outcome from the phase-based APBM route. That clarifies new authoring; it does not rename or rewrite historical campaigns.

Do not create independently governed child modules merely to break an implementation checklist into chunks. If genuine child modules exist, each requires QAM, and the parent ABM/APBM also needs QAM for integration scope. Child certificates can support parent planning; they do not prove integration.

ABM does not authorize deployment by default. A deployment requirement must name the environment, authority and separate Gate D obligations. Local product QA does not certify a deployed revision.

## 3. Roles follow seats, not model names

| Seat | Owns | Must not do |
|---|---|---|
| Director | Product intent, scope/risk decisions, credentials, Git mutation, release and final acceptance | Become the courier assembling missing QA records or the default executor of repeatable checks |
| Architect | Contract, acceptance criteria, ABM pack, integration boundaries, engineering-plan review, bounded repairs and closeout instructions | Replace independent QA with engineering-green claims |
| Designer, when applicable | Approved visual direction, tokens, canonical screens, states and component contracts | Leave required product behavior implied |
| Engineer | Implementation, self-verification, recovery records, factual QAM handoff and authorized repairs | Approve independent QA results, rewrite acceptance to match code, certify itself or mutate Git |
| QA Executor | Independent Q1, approved Q2, evidence, conditional retest and authorized cleanup | Self-approve its plan, self-certify or repair product code during QA |
| QA Lead | Standing risk requirements, Q1 approval/amendment, finding adjudication, retention/cleanup decisions and Gate Q | Invent missing evidence or silently change the product contract |
| Specialist reviewer, when specified | A named independent review question and report | Create a new unbounded build/review loop |

Cody may be Engineer and Opy/Claudy QA, as in the scraper pilot. Another project may reverse them. Record the assignment. Using a different model name alone does not establish independence; the verification assignment and evidence must actually be independent.

The QA Lead need not approve every engineering packet or implementation plan. The Architect and Director own engineering preparation. Candidate-specific QA approval occurs after Q1. Seek early specialist input only when an actual risk requires it.

## 4. Prepare the work before releasing the Engineer

The Architect consolidates existing product decisions, relevant reconnaissance, runtime evidence and design inputs into one executable assignment.

The pack must answer:

1. What result must exist, for whom, and why?
2. What is in scope, excluded and intentionally deferred?
3. What actual repository, branch, baseline and existing dirty work are involved?
4. What inputs, outputs, APIs, schemas and integration seams govern the result?
5. Which existing behaviors must remain intact?
6. How will each acceptance criterion be verified, in which environment and with what evidence?
7. What may the Engineer change or run, and where must it stop?
8. What factual handoff must Engineering supply to QAM?
9. Who owns each later decision, and where do artifacts go?

Reuse relevant existing recon. Refresh only facts that are stale or necessary to resolve a concrete unknown. For brownfield behavior, a bounded baseline run can provide information static inspection cannot. Do not repeat full recon for a routine handoff.

Acceptance criteria must be literal and testable. Distinguish:

- Implemented versus independently verified.
- Local fixtures versus native integration versus external live behavior.
- Source content versus derived presentation.
- Exact limits versus estimates.
- Partial results versus complete selected scope.
- Product success versus cleanup success.
- Required human judgment versus repeatable automated checks.

If a resource limit is estimated, say so before implementation. If a helper requires an agent review step, include that step in the product contract and test the final reviewed result.

## 5. The frozen contract and change rule

Freeze approved requirement text, protected boundaries and required design/integration contracts before implementation. Mutable status and append-only evidence remain outside that frozen text.

| Record class | Rule |
|---|---|
| Frozen contract | Preserve approved text; change through a dated amendment/erratum with authority and impact |
| Mutable control | Update concise current state and pointers; retain provenance of transitions |
| Historical evidence | Preserve failed attempts, original observations, approved plans, decisions and exports; append corrections |
| Generated working output | May be revised within authority; retain initial/final versions when the claim depends on that comparison |
| Disposable execution material | Retain only as required; remove through declared ownership and cleanup authority |

A scope reduction must list what was superseded, what remains open and what the current acceptance basis is. Do not convert removed obligations into PASS.

A QA plan cannot silently amend the acceptance contract. A documentation successor cannot silently extend certification to changed product, tests, configuration or dependencies.

Retiring an implementation path is a scope decision. It does not prove its old failures were repaired.

## 6. Minimum ABM package

Use the actual repository's established module root. For new packs using the scraper convention:

~~~text
agent_docs/ACTION/<module-id>/
~~~

Do not rename an existing ACTION/ACTIONS layout as a side task. Record the actual path.

### Parent files

| Path relative to module | Required content |
|---|---|
| README.md | Human orientation, scope, file index and entry points |
| CLAUDE.md and AGENTS.md | Matching role routing and references to the canonical entry |
| ABM_ENTRY.md | Read order, engineering/resume dispatch, limits and next-action rules |
| ABM_BRIEF.md | Objective, inputs/outputs, exclusions, dependencies and acceptance boundary |
| ABM_ACCEPTANCE_SPEC.md | Frozen ACs, methods, environments, expected evidence and blocking rules |
| ABM_EXECUTION_PLAN.md | Engineer's evidence-based plan, internal dependencies/checks, approval reference |
| ABM_STATE.md | Small current-state index; next owner; writer; identities; pointers into QAM |
| ABM_ACCEPTANCE_LEDGER.md | Engineering claims and references to independent QA dispositions |
| ABM_JOURNAL.md | Meaningful implementation/checkpoint records; no transcript dump |
| ABM_RULINGS.md | Scope changes, errata, deviations and authority |
| ABM_SKILLS_MANIFEST.md | Actual skill locations, versions, activation and scope |
| CONTRACTS/ | Data/integration/design/no-break protections when separate documents are useful |
| EVIDENCE/ | Engineering records needed to reproduce or review claims |
| QAM/ | Complete module-specific QAM from initial authoring |
| RETROSPECTIVE.md | Lessons and measured process results, populated as work progresses |

Small contracts can live in clearly named sections of ABM_BRIEF.md or ABM_ACCEPTANCE_SPEC.md and be referenced from the index. Do not create empty duplicates to satisfy a decorative tree.

### Required QAM structure

Instantiate the current approved QAM template, with module-specific paths and instructions. Its v1.0 locations are:

| Path | Owner/use |
|---|---|
| QAM/CLAUDE.md, QAM/AGENTS.md | Architect-generated matching entry routing |
| QAM/QAM_ENTRY.md | QA identity, read order and phase dispatch |
| QAM/QAM_STATE.md | QA state, identities, decision pointers and next owner |
| QAM/QAM_MANIFEST.md | Engineer's factual completion/environment record |
| QAM/HANDOFFS/ENGINEERING_HANDOFF.md | Engineer claims, commands, limitations and reproduction |
| QAM/QAM_PREFLIGHT.md | Readiness checks, expected results and resolution owners |
| QAM/QAM_RISK_REQUIREMENTS.md | Standing Lead requirements and module risks |
| QAM/QAM_RECON_REPORT.md | Independent Q1 observations |
| QAM/QAM_TEST_PLAN.md | Executor plan; QA Lead approval/amendments |
| QAM/QAM_APPROVAL.md | Exact approval and candidate/plan/release binding |
| QAM/QAM_EXECUTION_REPORT.md | Independent measurements |
| QAM/AC_EVIDENCE_MATRIX.md | AC-to-test/evidence/disposition mapping |
| QAM/FINDINGS.md | Findings and attributed dispositions |
| QAM/QAM_CLEANUP_REPORT.md | Authorized cleanup evidence |
| QAM/QAM_CERTIFICATION.md | Exact or directly linked QA Lead verdict with attribution |
| QAM/GOVERNING/ | Versioned governing sources and provenance |
| QAM/AUTOMATION/, QAM/evidence/ | Approved instruments, measurements and attempts |
| QAM/HANDOFFS/ | Review packages, receipts and reviewer entry notes |

Future-state templates identify their owner and “not yet executed” status. **Never prefill a QA result, approval or certificate with PASS.**

Existing pilots may have earlier filenames such as STATE.md or MANIFEST.md. Map those explicitly instead of migrating certified history merely to match this table.

ABM_STATE.md indexes QAM state; it does not maintain a second full QA report. The acceptance ledger links the independent matrix rather than copying contradictory verdicts.

## 7. Skill activation and runtime portability

The module must have a usable execution method discoverable from its entry files. Reuse an existing versioned builder skill when one satisfies the contract. Otherwise author the missing skill as a separately identified pack deliverable; do not claim a manifest entry is an installed or tested skill.

Record in ABM_SKILLS_MANIFEST.md:

- Skill name, purpose, actual path and version.
- Authoritative doctrine source.
- Entry file and supported runtime/launch directory.
- Read/write scope, tool/environment requirements and outputs.
- Activation-check evidence or explicit NOT VERIFIED status.

Follow APP_FACTORY_SKILLS_PLAYBOOK.md for any actual skill authoring. Keep entry/doctrine in the manager file and methodology in SKILL.md. References point to canonical contracts; do not fork acceptance requirements into the skill.

Engineering automation is an Agent Skill use case. Internal planning and verification remain mandatory; already authorized routine work should not repeatedly request permission. Operator-driven deployment/migration skills retain their own applicable interaction requirements.

CLAUDE.md and AGENTS.md are runtime adapters to the same module rules. Validate actual activation from the documented launch location. A file's existence does not prove the runtime reads it. Provide one stable fallback: read ABM_ENTRY.md or QAM/QAM_ENTRY.md.

This playbook does not install a builder skill, modify a runtime's permissions or guarantee tool availability. A blocked tool must be reported accurately. Changing from one harness to another preserves the contract, role, evidence and writer handoff.

Do not print credential files as an environment-discovery shortcut. Check necessary configuration without emitting secret values. Follow the current QAM credential/privacy rules for QA.

## 8. Engineering: plan once, execute the whole assignment

### Planning

The Engineer reads actual state and the contract, resolves discoverable facts, and returns one complete plan with:

- Intended behavior and affected paths.
- Internal task/dependency order.
- Required self-checks and regression.
- Resource/side-effect authority.
- Existing work to preserve.
- Genuine ambiguities or blockers, collected together.
- The factual QAM handoff it will produce.

The Architect reviews the plan against the contract; the Director authorizes execution. Existing explicit authorization carries forward. Do not create a new approval round for an unchanged plan, a context reset or a routine continuation.

### Continuous execution

After release, the Engineer:

1. Implements the entire approved boundary.
2. Runs meaningful checks as dependencies become available.
3. Repairs in-scope implementation failures.
4. Performs the required final engineering regression.
5. Updates the acceptance ledger, concise journal and recovery pointers.
6. Completes the factual QAM manifest and engineering handoff.
7. Returns one coherent engineering completion package and Git reminder.

Engineering self-tests precede independent QA; they do not replace it.

Internal milestones are checkpoints for the agent, not automatic stopping points for Tony. Do not split a released build into “Chunk A complete—say go for Chunk B” without an explicit dependency, required decision or hard stop.

At handoff, identify uncommitted work honestly. The final candidate SHA does not exist until Tony commits. Record the known HEAD plus changed-path/source identity and “candidate pending Director commit.” Q1 later binds the committed candidate using read-only evidence. Do not create an endless commit cycle to embed a commit's own SHA inside its own files.

## 9. Authority, stop and recovery rules

### Allowed inside the released assignment

Read-only repository/Git inspection; approved product edits; declared local builds/tests/services; bounded fixture use; in-scope corrections; engineering records; factual QA handoff.

### Director-controlled or separately scoped

Git mutation; deployment; new external targets or spending; credentials/identity changes; destructive data or cleanup; protected architecture; unapproved schema/dependency changes; material acceptance changes.

Approval can preauthorize precise actions and boundaries. Do not ask again when that authority already applies. A tool policy denial is still a real limitation; wording such as “go” does not bypass it.

### Stop only where necessary

Stop the affected operation for:

- Wrong candidate/branch/target or unexplained product drift.
- Material contract contradiction.
- Missing prerequisites that prevent trustworthy execution.
- Required work outside the authorized write/effect boundary.
- Untrustworthy test instrument or inability to preserve evidence.
- Secret/protected-data exposure.
- A required product decision that cannot be inferred safely.

A failing product assertion is a finding, not automatically a reason to abandon every unaffected check. Continue independent safe checks when the plan permits; aggregate blockers so Tony receives a useful return.

Record the stop, evidence, owner, exact resolution and safe resume point. Resume there after resolution. Do not automatically restart recon, reinstall everything or repeat passed checks.

One active writer means one seat owns repository writes at a time. Record owner, scope, relevant identity, acquisition/release and next owner. The handoff includes owned process/temp-path information where relevant. A read-only reviewer is not another writer.

## 10. Engineering handoff and Director candidate

Engineering completion includes QA readiness. It is not a separate later assignment to “write the QA handoff.”

The factual handoff contains:

- Full baseline/current HEAD; changed paths; known dirty/untracked work.
- Build/serve/test/reproduction commands with working directories.
- Actual environment, configuration prerequisites and test-data requirements.
- Per-AC engineering claims linked to evidence.
- Known failures, limitations, exclusions and unverified areas.
- Actual interface/data boundaries and independent QA needs.
- Owned temporary paths/processes and retention requirements.
- Exact review package location and next owner.

Tony stages and commits intended changes, establishes the QA branch and reports the candidate. Agents may prepare exact scoped commands after checking actual state, but may not run Git mutations.

Do not prescribe blanket staging to capture “everything.” Shared workspaces may include another seat's records or unrelated outputs.

The default QA branch is qa/<module-id>, created from the completed engineering candidate under Tony's control. Approved repairs can occur on that QA line with a writer handoff and a new committed candidate. Preserve existing repository branch policy when explicitly different.

## 11. QAM: two planned shots

### Q1 — independent reconnaissance and test plan

Point the QA Executor at QAM and ask it to start. That authorizes Q1 within its declared scope, not Q2 or product repair.

The Executor verifies actual identity/state, contract and governing sources, environment, target, instruments, test data, permitted effects and evidence/export readiness. Q1 is read-only toward product and business data; bounded setup/probes require the preflight's authority.

Then it independently drafts the full plan from the contract, risks, source and Engineer's claims. Every AC gets a check or explicit applicability ruling. Expected results must have an independent basis.

Return one indexed Q1 package containing actual recon, draft plan, identities, contradictions and supporting sources. Stop for Lead review. Do not return after each minor missing document if useful independent work can safely continue.

### The approval checkpoint

The QA Lead reviews the actual package and approves, amends or holds the specific plan. Record the candidate, plan hash, contract/ruling identity, environment, exact changes and release conditions.

Exact delegated edits can be applied with a preserved diff and finalized plan identity. They do not automatically create a new general approval round. Material changes or unresolved contradictions return to the Lead. Q1b amendment bookkeeping is not a mandatory third shot.

Tony releases Q2 under the established Git policy. Distinguish the tested product candidate from a later documentation-only execution HEAD. Prove a successor's complete changed-path scope; a commit message is insufficient.

### Q2 — independent execution

At release, verify the approved plan, candidate, current HEAD, target and applicable readiness. Execute continuously in risk/dependency order.

Preserve failures and partial results. Correct authorized disposable QA helpers with a record and validated instrument; do not alter product code, weaken assertions or silently retry failures to obtain green.

Return one result package with execution report, matrix, findings, identities, instruments, measurements and remaining gaps. The Executor reports observations; the Lead certifies.

Required human checks are planned and grouped where possible. Authentication/MFA or real product judgment may require Tony. Record such interventions honestly; never fake unattended execution.

## 12. Conditional findings, repairs and independent retest

The Lead classifies findings and requests only the appropriate next work. The Architect produces one consolidated repair handoff for accepted implementation changes.

A bounded repair identifies:

- Finding IDs and precise failing mechanism.
- Inputs and reproduction evidence.
- Expected behavior and acceptance/ruling references.
- Allowed implementation/test paths and preserved boundaries.
- Required regression and affected independent checks.
- Handback directory, candidate-binding method and next owner.

The Engineer repairs and self-verifies. Tony commits. Independent QA re-pins the candidate and retests the repair, affected ACs and the full regression required by the approved plan. Reuse unaffected evidence only with stated applicability and original provenance.

Evidence-only completion is not a product rebuild. A packaging correction is not a reason to rerun passed tests. A QA helper defect is not automatically a product defect. Keep those categories distinct.

Specialist architecture/code reviews are included when the frozen contract or a concrete risk requires them. Name the question, reviewer, evidence and blocking rules before execution. Do not automatically append Astra → GLM → another final review to every small tool.

The older drafts' RBM label is not introduced as a new Factory module type here. Use bounded repair instructions or the existing applicable RRM/FIX route. Any already frozen independent-review obligation still requires fulfillment or an explicit authorized disposition; this edition does not waive it retroactively.

## 13. Evidence that is sufficient and reviewable

Every important claim needs the relevant input, expected result, observation, method, environment and identity.

Examples from the scraper:

- “Heading preserved” needs the actual source and final reviewed output, not just a count.
- “REST bytes preserved” needs independently defined source bytes and the saved body/checklist/result chain.
- “Literal source remains inert” needs suitable parsing/rendering evidence, not only an escape-string assertion.
- “Limit enforced” must distinguish observed triggering, estimate accounting and true hard-cap behavior.
- “All tests pass” needs actual result records and unique case counts, not repeated executions added together.

Keep engineering claims separate from independent measurements. Hash integrity proves identity; it does not prove evidence completeness, correctness or useful behavior.

Package Q1, Q2, material stops and repair/retest returns under:

~~~text
QAM/HANDOFFS/<MODULE>_<PHASE>_REVIEW_<ATTEMPT>.zip
~~~

Each package includes REVIEW_START_HERE.md, relevant identities/state, actual reports, governing contract/rulings, plan/approval as appropriate, findings and sufficient supporting evidence.

Use an explicit inclusion list and FILE_INDEX.json with each member's path, source, purpose, size and SHA-256, excluding the index itself. Verify membership, hashes, safe paths, duplicates and ZIP integrity. An external receipt hashes the finished archive. Avoid circular/self hashes and nested prior ZIPs by default.

Exclude credentials, auth/browser state, dependency/build trees, Git internals and unsafe raw logs. Apply QAM privacy requirements proportionately to the actual surfaces. Preserve synthetic fixtures as labeled test data; do not silently exempt real credential leaks.

Return exact filename, full upload path, archive hash, member count and the decision needed. A byte-identical Downloads copy is useful when requested. Missing evidence must be named, not invented.

## 14. Certification, cleanup, integration and Director acceptance

These are separate recorded facts:

| Fact | Meaning / owner |
|---|---|
| Engineering complete | Engineer claims approved implementation and self-checks are complete |
| Gate Q | QA Lead's scoped independent verdict on a bound product candidate |
| Cleanup accepted | Required retention and owned-debris handling accepted under the governing policy |
| Integrated | Tony committed, merged, pushed and synchronized the intended repository state |
| Director accepted | Tony completed the required product ride/manual checks and made the acceptance decision |
| Gate D, when applicable | Separately scoped verification of the deployed system |

Follow the governing module's order for Gate Q and cleanup. Some contracts require cleanup before the final certificate; others issue a product verdict then require cleanup before closeout. Do not reorder a frozen campaign to fit a generic diagram.

Routine preauthorized hygiene belongs in execution. Final retention/cleanup uses exact owned paths and the required Lead/Director authority. Retain the smallest durable package that explains the verdict and supports reproduction. Preserve failed attempts and useful helpers when justified; do not retain all disposable runtime material by habit.

Before destructive cleanup, verify actual current ownership/state. Already absent means verified absent, not newly deleted. Preserve unrelated work and other seats' processes.

Install the exact QA Lead decision unchanged. A certificate may correctly describe pending records at issuance. Later commit/clean-tree/integration facts go in a successor record, not an edited certificate.

Architect closeout verifies accepted scope, limitations, frozen history, required cleanup and records, then prepares scoped Git steps based on actual branch/HEAD/diffs. Tony executes Git mutations.

Director ride timing is declared by the contract. It may be an earlier required visual gate or a final usability check after integration. Do not invent a second ride where the required check already occurred. Do not call an ABM fully accepted while its required Director check remains pending.

## 15. Definition of complete

An ABM is fully complete for its declared scope when:

- The approved outcome exists and every AC has an explicit final disposition.
- Required engineering checks and independent QA are complete.
- Required specialist reviews and risk decisions are fulfilled or explicitly dispositioned.
- Gate Q identifies the product, evidence, scope and limitations.
- Required cleanup and durable record handling are accepted.
- Architect closeout is complete.
- Tony's integration and required repository state are verified.
- Required Director checks are complete and his acceptance is recorded.
- Deployment is either explicitly excluded/deferred or fulfilled through its separate authorized process.
- The retrospective states lessons and evidence limits honestly.

A useful demonstration can be accepted without meeting full module completion. Label it as a demonstration. Likewise, “certified and integrated; Director ride pending” is a valid precise status.

Do not use “closed” as shorthand for whatever milestone happened most recently.

## 16. Reusable authoring templates

These are shapes to fill from actual project evidence. Angle-bracket fields are authoring placeholders; resolve them before delivery. Do not fabricate unknown future SHAs or prefill later verdicts.

### A. ABM brief

~~~text
Module ID and actual module path:
Repository / working directory:
Director / Architect / Engineer / QA Lead / QA Executor:
Objective and intended user:
Approved inputs and outputs:
In scope:
Out of scope / deferred:
Existing baseline and work to preserve:
Data / integration / UI contracts:
Critical end-to-end path:
Protected behaviors and files:
Allowed product / evidence / temporary write locations:
Allowed local/external effects, resources and limits:
Required engineering checks:
Required independent QA environments:
Required Director checks and timing:
Required specialist reviews, or not required with rationale:
Deployment status:
Engineering release / governing decision:
QAM location:
Expected engineering handoff and review destination:
~~~

### B. Acceptance row

~~~text
AC ID:
Requirement, stated as observable behavior:
Input / precondition:
Expected result and independently derived reference:
Verification method:
Required environment:
Evidence required:
No-break / negative cases:
Blocking severity:
Allowed applicability/erratum decision owner:
~~~

Do not hardcode scraper values, browser dimensions, user roles or test counts into unrelated applications. State the required behavior; choose the profile from the actual product.

### C. State and writer record

~~~text
As-of date/time and timezone:
Module state:
Current branch / HEAD:
Product candidate, or pending Director commit:
Contract version / approved plan reference:
Current writer and authorized write scope:
Latest engineering handoff:
QAM state / latest decision pointer:
Latest package / receipt:
Current stop, if any:
Next owner:
Next permitted action:
Actions already completed that must not repeat:
Writer release / owned process and temp-path handoff:
~~~

This is an index, not another report. Repository-mandated recovery/session files point here or summarize the same checkpoint without conflicting state.

### D. Engineering completion / QAM handoff

~~~text
Completed scope:
Baseline / current HEAD / working-tree identity:
Changed product, test, config and documentation paths:
AC claims with engineering evidence:
Exact commands, working directories and outcomes:
Environment, fixtures, target and permitted side effects:
Known limitations / failures / unverified areas:
Independent QA setup and reproduction:
Preserved existing work:
Owned services and temporary paths:
Package filename / absolute path / hash:
Git reminder: intended paths; candidate pending or Director receipt:
Next owner: Director for candidate, then independent QA for Q1.
~~~

### E. Bounded repair handoff

~~~text
Lead decision and exact finding IDs:
Candidate and contract:
Observed failure / independently expected behavior:
Reproduction and evidence:
Mechanism to address:
Allowed files and changes:
Forbidden / preserved scope:
Engineering regression:
Independent retest scope and required full regression:
New evidence lane / handback path:
Candidate re-pin after Director commit:
Writer handoff and next owner:
~~~

### F. Closeout record

~~~text
Accepted scope:
Certified product candidate:
Exact certificate filename / SHA-256 / installed location:
Accepted evidence and decision references:
Required cleanup result:
Preserved limitations and historical findings:
Documentation-successor identity and changed-path verification:
Current branch / HEAD / staged / unstaged / untracked state:
Intended closeout paths:
Tony's scoped commit / merge / push steps, based on actual state:
Final integration receipt:
Director check status and acceptance:
Deployment / Gate D status:
Retrospective and remaining follow-ups:
~~~

The final integration receipt is added after Tony supplies the result. It is not predicted during closeout authoring.

## 17. Entry and execution prompt patterns

The pack must contain the operating rules. Prompts select the seat and action; they must not supply missing contracts that exist only in chat. When delivering a prompt to Tony, show it on screen and name any required files first.

### Module-writing Architect

~~~text
Author one complete ABM for the agreed bounded outcome using ABM_PLAYBOOK_v1_0.md.
Use the current QAM playbook and instantiate a module-specific QAM from the start.
Read actual baseline evidence and existing skills before authoring.

Supply the frozen brief/acceptance contract, protected boundaries, execution
and recovery rules, skill references, internal check plan, and engineering
completion duties. Make one released engineering assignment cover the full
build, self-verification and factual QAM handoff.

Resolve module paths and prerequisites. Mark future candidate/QA fields
pending; do not fabricate results. Preserve existing work and Tony's Git
authority. Return one coherent pack and one entry instruction.
~~~

### Engineer: first entry

~~~text
You are the Engineer for <module-id>.
Read <absolute-module-path>/ABM_ENTRY.md and its declared sources.
Inspect the actual branch, HEAD, working tree and environment read-only.
Prepare the complete engineering plan and aggregate genuine blockers.
If the persisted record already contains my valid release for that exact
scope, continue from its recorded state; otherwise return the plan for release.
Do not mutate Git. Do not restart completed work.
~~~

### Engineer: release

~~~text
The engineering plan for <module-id>, identified by <plan version/hash>,
is approved. Execute the whole authorized assignment continuously:
implementation, in-scope corrections, required self-verification and
the factual QAM handoff. Continue across ordinary internal milestones.
Stop only for the declared hard-stop conditions. Preserve prior evidence,
maintain one active writer, and leave all Git mutations to Tony.
~~~

### Independent QA: Q1 entry

~~~text
You are the independent QA Executor for <module-id>.
Start Q1 from <absolute-module-path>/QAM/QAM_ENTRY.md.
Complete the authorized readiness/recon and independent test planning.
Return one indexed Q1 package at the declared handoff location, then stop
for QA Lead review. Do not repair the product or start Q2.
~~~

### Independent QA: Q2 release

~~~text
Run Q2 for <module-id> under the exact QA Lead approval at <approval-path>.
Approved product candidate: <full-SHA>.
Approved finalized plan SHA-256: <hash>.
Director release: <release-reference>.
Verify the bindings and current state, then execute the approved plan
continuously and return one indexed result package. Preserve failures,
observe stop rules, and leave certification to the QA Lead.
~~~

Replace placeholders with actual values and full paths. If a stopped or completed state is found, use its resolution or return its existing package; these prompts do not override persisted facts.

## 18. Worked example: Web Factory scraper

### Approved delivered boundary

DECIDE → explicit selected COLLECT → offline agent-assisted PREPARE.

The useful output is a selected, source-linked architect package. The workflow deliberately includes human selection and agent review. It is not a whole-site/media/iframe completeness promise.

The initial more complex controller direction was simplified. Historical obligations and failures were retained rather than silently marked PASS.

### Observed lifecycle

| Stage | Evidence-backed outcome |
|---|---|
| Engineering | Implemented the selected workflow and PREPARE skill; supplied readiness and handoff evidence |
| Independent QA | Q1 planning and Q2 execution exposed bounded repair/evidence work |
| LEAD-02 engineering | Fixed generic CTA title contamination and literal-source Markdown/HTML promotion |
| Independent retest/completion | Accepted 144 unique cases and C1–C3/O2 completion within the declared limits |
| Cleanup | Owned disposable roots removed; durable evidence retained and accepted |
| Gate Q | QA Lead issued scoped PASS on October 17 |
| Administration / integration | Certificate installed; records committed; module integrated and pushed to main |
| Director product ride | Pending at this playbook's publication |

Certified product candidate:

~~~text
0f98bcf095781a3ac7a231c276199224dc531f11
~~~

Certified source52 inventory fingerprint:

~~~text
6f35cf8dacf3aeecc17a89b1c96e3558ea52e3c03edf63c2e402a766a1e986f4
~~~

Recorded integrated main:

~~~text
7a47d7f5cc3d96ebf4fb0de34dc83519054b3b51
~~~

Certificate:

~~~text
WebFactory_GATE_Q_Certificate_2026-10-17.md
SHA-256: 6ecb6310938a0f2de4a3ffa1e87b8ad2befc2100d0f12ccc655598ab41874c31
~~~

The source52 fingerprint covers a defined inventory, not every repository file. Main's merge SHA differs from the product candidate and documentation commits. Those differences are expected; explain them rather than forcing equality.

### Lessons generalized into this playbook

1. **Choose a contract the implementation can honestly satisfy.** Planned calls and estimated persistence are different from exact browser-wire controls and hard resource ceilings.
2. **Test the behavior the consumer actually receives.** Initial helper output and final agent-reviewed output are distinct artifacts.
3. **Use independent expected results.** A plausible output or successful exit is not a correctness oracle.
4. **Include the actual evidence.** A summary saying “preserved” cannot replace the source/derived specimen required to verify preservation.
5. **Keep repair bounded.** Two concrete defects led to four product/test file edits, followed by independent retest; they did not require restarting the entire project.
6. **Package at the end of each assignment automatically.** The Director should receive the exact upload file without assembling it.
7. **Separate product and record identities.** A verified documentation-only successor should not be mistaken for changed product bytes.
8. **Recognize completed actions on resume.** Stale cleanup or closeout instructions must not trigger duplicate work.
9. **Preserve useful limits and open historical facts.** Certification of the revised scope does not erase retired-controller findings.
10. **Keep final acceptance visible.** QA and Git integration can be finished while the Director's real-world ride is still pending.

### Limits of the pilot evidence

The campaign demonstrates a scoped delivery/QA/repair/cleanup/integration chain. It does not establish a measured “10× faster” result, an intervention-free end-to-end build, or universal effectiveness across full-stack applications.

The certificate preserves unverified clean-install reproducibility, broad native cancellation/crash behavior, broad hostile-viewer behavior, media/hidden/deferred/image/iframe-child completeness and current external-site access. O5 remains an initial-helper limitation managed by review.

The historical media gap, unconfirmed late aborts, bootstrap/route mismatch and missing supervisor counters remain open for the retired controller history. They are not silently repaired by this playbook.

October 14 draft statements that QA had not run are historical. The October 17 certificate and integration receipts supersede those current-status statements without changing the old drafts.

The Director ride proceeds in the Web Factory product lab. Its findings return to the ABM retrospective and may inform a later playbook revision.

## 19. Measure whether ABM saves work

Record practical metrics when available; do not fabricate missing timestamps:

| Measure | What to capture |
|---|---|
| Preparation | Time to resolve scope, author pack and establish prerequisites |
| Engineering | Active implementation/check time; interruptions and their causes |
| Q1 | Readiness/planning work and avoidable missing-input returns |
| Review/release wait | Time waiting for decisions, separate from agent execution |
| Q2 | Execution duration and actual Director interventions |
| Repair | Product defects, helper defects and evidence-only corrections separately |
| Packaging/cleanup | Time spent exporting, correcting omissions and retaining/removing artifacts |
| Acceptance | Director ride result and usability friction |
| Overall | Elapsed delivery time, touches by purpose and usable accepted outcome |

Useful retrospective questions:

- Did the Engineer return for routine continuation when it could have proceeded?
- Did a complete initial pack prevent missing-input loops?
- Did Q1 catch real readiness problems before Q2?
- Did any missing evidence force a second package?
- Was a stop genuine, or caused by stale identity/state instructions?
- Did the delivered result solve the Director's task?
- What can be removed or automated next time without weakening the claim?

Do not optimize for a low message count by hiding failures, dropping requirements or misreporting human intervention.

## 20. Adoption and synchronization notes

This edition consolidates the three September ABM drafts into one operating playbook with folder requirements and templates. Preserve those originals as dated history.

| Earlier draft convention | This edition's treatment |
|---|---|
| ABM includes every application phase by default | One bounded outcome; phase-based delivery routed to APBM |
| Named premium models own permanent seats | Role-based assignments with recorded independence |
| Separate generic QA/ folders | Mandatory module-specific QAM from authoring |
| Engineer returns for repeated chunk handoffs | One released assignment with internal automatic continuation |
| Handoff written as a later extra task | Factual QAM completion is part of engineering |
| Automatic Astra/GLM/final-review chain | Contract/risk-specific reviews; inherited obligations need explicit disposition |
| RBM as a new automatic repair module | Bounded repair or existing applicable Factory repair route |
| Many overlapping status documents | Concise state index, canonical contracts and linked evidence |
| Candidate/HEAD used interchangeably | Product candidate, execution HEAD, records commit and integration SHA distinguished |
| “Complete” used for any milestone | Engineering, QA, cleanup, integration and Director acceptance recorded separately |

For Factory integration, the Doc Sync Architect should reconcile applicable ABM/APBM definitions, module-authoring templates, engineering completion duties, QAM entry/routing, skill references, lifecycle diagrams and closeout vocabulary. Use the existing governed doc-sync process and installed capabilities; this playbook is not a request to build another doc-sync skill.

Known reconciliation points:

- The supplied Skills Playbook v1.1 distinguishes operator-driven Stark Skills from Agent Skills. Apply the Agent Skill execution model to released engineering; do not copy an operator checkpoint into every internal task.
- Its environment-discovery example must not be interpreted as permission to print secret configuration into reports.
- Runtime entry support must be demonstrated for the actual harness; do not assume Claude-specific discovery rules describe every tool.
- Existing approved campaigns retain their original contracts and explicit amendments. A new playbook does not retroactively remove required checks.
- The mandatory QAM structure is owned by the QAM playbook. Keep its current version/provenance visible rather than maintaining a competing ABM QA template.

No broad repository migration, additional QA campaign or new approval ceremony is authorized merely by publishing this file.

## 21. Source and authority ledger

| Source | Used for | Boundary |
|---|---|---|
| 00_ABM_VISION_AND_PROCESS_v0_1.md, 2026-09-16 | Original intent, speed model and prototype goals | Experimental historical proposal |
| 01_ABM_PLAYBOOK_v0_1.md, 2026-09-16 | Contract, execution, authority and completion baseline | Revised here; not treated as proof the pilot fulfilled every old proposal |
| 02_ABM_FOLDER_AND_TEMPLATE_SPEC_v0_1.md, 2026-09-16 | State classes, minimum fields and recovery shape | Consolidated; avoids mandatory empty/duplicate structures |
| APP_FACTORY_SKILLS_PLAYBOOK.md, supplied v1.1 dated 2026-07-08 | Skill/doctrine pairing, activation, evidence and evolution | This document does not update that source or claim a new skill was installed |
| QAM_PLAYBOOK_v1_0(1).md, retrieved 2026-10-17; document dated 2026-10-14 | Mandatory QAM, five seats, two shots, evidence, repair and cleanup | Latest located copy used for this authoring; filename suffix is not a version increment |
| WEB_FACTORY_P1_PHASE_MAP_v0_3.md, 2026-09-07 | Historical phase/role context | Predates October's approved simplified scope |
| WEB_FACTORY_P1_DOCTRINE_JOURNAL.md, v0.3 | Frozen contract/evidence distinction, Git, bounded repair and cleanup | Historical entries preserved, including their own corrections |
| WebFactory_ABM_Closeout_Assessment_and_Playbook_Draft_2026-10-14_134641.zip | Earlier concrete lessons and limitations | Pre-certification status is superseded by later evidence |
| WebFactory_GATE_Q_Certificate_2026-10-17.md | Final scoped QA and cleanup outcome | Product certification, not process-speed or Director-acceptance proof |
| Tony's October 17 Git terminal output | Integration SHA and clean local/remote-main state | Director-supplied evidence; no direct VM inspection by this authoring lab |
| Current Director instruction | Write the reusable ABM playbook; continue product ride separately | Does not imply that every Factory file has already been synchronized |

The source drafts are not overwritten. Proposed new operating defaults are explicit in this edition; historical decisions remain attributed to their original owners. A module's current approved contract, Director decisions and governing QA requirements must be reconciled before applying conflicting new defaults.

## 22. Version history

| Version | Date | Change |
|---|---|---|
| 0.1 | 2026-09-16 | Three experimental vision/playbook/folder documents proposed a larger automode campaign |
| 1.0 | 2026-10-17 | Consolidated bounded ABM method; mandatory existing QAM; continuous engineering; conditional repair; usable templates; separate candidate/record/integration identities; certification versus Director acceptance; scraper evidence and limitations |

**Current publication checkpoint:** the reusable playbook is written. Factory-wide synchronization and skill/template installation are separate work. The scraper's Director ride and final product acceptance are still pending.



