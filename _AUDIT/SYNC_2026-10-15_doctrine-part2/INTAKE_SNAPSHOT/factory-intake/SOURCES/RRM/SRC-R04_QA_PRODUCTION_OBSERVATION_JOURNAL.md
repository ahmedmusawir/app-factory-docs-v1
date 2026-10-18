# JARVIS QA 10X — Production Observation Journal

**Owner:** JARVIS Master / QA Lead  
**Director:** Tony Stark  
**Started:** 2026-09-28  
**Status:** Private working journal · outside production repositories

## Purpose

Capture evidence-based lessons from real production QA so the 10X Lab can design a one-shot QA method for ABM and APBM work. This journal records how the process behaves, where human intervention is actually necessary, which evidence is durable, and which handoffs create avoidable delay.

## Production-integrity rules

- Production acceptance criteria always outrank the experiment.
- QA never reduces coverage merely to make a run “one shot.”
- Experimental helpers stay inside the authorized QA lane.
- No product repair, Git mutation, credential capture, database mutation, or destructive cleanup is authorized by this journal.
- The QA Lead may veto or stop the experiment whenever module risk, evidence quality, or a contract conflict requires the normal process.
- Observations are copied here after the fact; this journal is not governing authority for the active module.

## Working hypothesis

A well-prepared module can complete independent QA in one uninterrupted Executor run when the candidate is immutable, the contract is frozen, rulings are already recorded, governing documents are local, repeatable checks are automated, Director checkpoints are explicit, and the evidence/cleanup outputs are specified before execution.

## Observation 001 — RRM-001 closeout

### What happened

- The first RRM combined module design, review reconciliation, contract correction, QA execution, live authentication, evidence packaging, cleanup and playbook discovery.
- Missing governing documents and a mistaken logout destination created avoidable handoffs.
- A successful manual login was initially mistaken for completion of the full authenticated journey.
- The Director was asked to repeat a role × viewport × theme matrix manually.
- Gate Q eventually passed with no product rework after the contract erratum and full authenticated walk were completed.

### Lessons

- Repeated authenticated UI matrices belong in Playwright.
- The Director should enter credentials only in the browser and perform one ADMIN and one MEMBER visual spot-check.
- A bounded post-Gate-Q cleanup prompt is valuable: preserve cited evidence, remove disposable helpers and runtime debris, rebuild the artifact inventory, write cleanup/certification records, and return an exact Director commit block.
- QA governing documents must be present inside the module before execution begins.
- Frozen criteria must have an append-only ruling lane for drafting errors.
- Passing evidence should never be rerun without a concrete invalidation reason.

## Observation 002 — RRM-002 one-shot trial authorization

### Module profile

- Small, bounded frontend disclosure plus fixture/copy audit.
- Six intended source files.
- No service, type, certified-wrapper, Supabase or script changes.
- No live database mutation.
- One authenticated Summary-tab acceptance check.
- Primary risks are stale filter pairing, rounding, hidden-state behavior and accidental money-value changes.

### QA Lead ruling

RRM-002 is suitable for a controlled one-shot QA execution. The Executor may perform intake, write the test plan, run static/runtime/browser/regression checks, and return one evidence package without pausing for ordinary observations. The normal process resumes immediately if candidate identity changes, the frozen contract contradicts itself, a release-blocking failure appears, required authentication is unavailable, or an unapproved destructive/live operation would be necessary.

### Experiment measures

- Number of Director interventions.
- Number of QA prompts from release to evidence handoff.
- Number and cause of Executor stops.
- Repeated checks caused by incomplete evidence.
- Time spent on testing versus document discovery and coordination.
- Whether Playwright eliminates the manual viewport/theme matrix.
- Whether the first evidence package is sufficient for SOL adjudication.
- Whether post-Gate-Q cleanup completes without loss of cited evidence.

## QAM design seed

### Core judgment

QAM is a strong idea, but the Engineer must not invent acceptance criteria after seeing the completed implementation. The QAM needs two controlled halves:

1. **Pre-build authority half:** Architect and Director define scope, acceptance criteria, protected paths, test boundaries, required roles, live-service permissions and stop conditions. The QA Lead supplies the certification model and mandatory evidence classes.
2. **Post-build execution half:** The Engineer pins the candidate, maps each criterion to implementation evidence, supplies reproduction commands, identifies Director checkpoints, prepares automation and hands the immutable package to the QA Executor.

### Candidate QAM structure

```text
agent_docs/ACTIONS/<MODULE-ID>/QA/
├── AGENTS.md
├── QAM_MANIFEST.md
├── ACCEPTANCE_SPEC.md
├── RULINGS_ADDENDUM.md
├── QA_HANDOFF.md
├── QA_TEST_PLAN.md
├── DIRECTOR_CHECKPOINTS.md
├── AUTOMATION/
├── GOVERNING/
├── evidence/
├── QA_EXECUTION_REPORT.md
├── AC_EVIDENCE_MATRIX.md
├── ARTIFACT_INVENTORY.json
├── QA_CLEANUP_REPORT.md
└── QA_CERTIFICATION.md
```

### Role boundaries

- **Architect:** freezes the behavioral contract and adjudicates scope ambiguity.
- **Engineer:** completes the build-side handoff and prepares repeatable test entry points.
- **QA Lead:** designs risk-based independent testing, adjudicates findings and owns Gate Q.
- **QA Executor:** executes, probes, collects evidence and performs ruled cleanup; never repairs or certifies.
- **Director:** supplies credentials/authority, performs bounded visual judgment, controls Git and approves destructive/live operations.

## Open design questions for the 10X Lab

- Is QAM a standalone module type or the mandatory QA subpackage of every ABM/APBM phase?
- Which acceptance tests must Engineering author, and which probes must remain independently authored by QA?
- How should QAM declare reusable authenticated Playwright storage without retaining secrets?
- What is the minimum durable evidence set for Gate Q?
- Can the artifact inventory drive cleanup automatically without broad deletion rules?
- What schema can validate QAM completeness before Cody starts?
- What conditions promote a one-shot run back to the normal staged QA loop?

## Future entry template

### Observation NNN — module and date

- Module profile:
- Predicted QA shape:
- Actual execution:
- Director interventions:
- Stops and causes:
- Evidence defects:
- Automation wins:
- Cleanup result:
- Gate Q cycles:
- Keep:
- Change:
- Drop:
- QAM/playbook implication:

## Observation 003 — RRM-002 completed production trial, 2026-09-28

- **Module profile:** Six-path frontend disclosure/audit module; no service, type, database, or certified-wrapper change.
- **Predicted QA shape:** Controlled one-shot execution with one possible Director authentication checkpoint.
- **Actual execution:** Cody completed the static, fixture, race, build, regression, and browser-instrument work autonomously, then completed the authenticated matrix after the Director entered credentials.
- **Director interventions:** Environment authorization plus browser-only ADMIN and MEMBER credential entry. The Director did not manually execute the role × viewport × theme × filter matrix.
- **Stops and causes:** One material stop caused by the paused/drifted free replica environment; classified as setup, not product.
- **Evidence defects:** No missing acceptance evidence remained after the authenticated continuation. AC-402's historical clean-tree moment could not be independently recreated, but contemporaneous logs, exact ancestry, docs-only successor proof, and current tracked-tree evidence were sufficient.
- **Automation wins:** Independent $20.27 derivation; live slow-result race; double-clear path; 16 authenticated Summary states; 21 screenshots; three safe traces; 31 Jest suites/144 tests; two clean 17-route builds.
- **Cleanup result:** Pending the bounded post-Gate-Q cleanup/closeout pass; no reason to rerun passing product evidence.
- **Gate Q cycles:** One evidence adjudication cycle after the authenticated continuation; PASS, zero product defects, zero repairs.
- **Keep:** Adaptive Playwright, visible-browser credential handoff, sanitized traces, AC matrix, immutable candidate pin, evidence-only Executor role.
- **Change:** Mandatory preflight for service wakefulness, test identities, role availability, target environment, browser tooling, and Director checkpoints.
- **Drop:** Large manual browser matrices for the Director and redundant reruns after resolved environment/setup issues.
- **QAM/playbook implication:** QAM should validate readiness before Cody starts, then allow one continuous execution through static, runtime, race, browser, evidence, and cleanup stages. The QA Lead retains adjudication and certification; the Executor never self-certifies.

## Observation 004 — Director ruling on self-sufficient module entry, 2026-10-01

**Authority:** Tony Stark, Director, in the Cyber Pharma QA lab at 13:24 Asia/Dhaka.  
**Recorded by:** QA Lead / JARVIS.  
**Status:** Explicit Director requirement for forthcoming factory templates and playbooks. Implementation and portability still need evidence. This journal entry does not claim those mechanisms already exist or silently amend the active frozen RRM-004 package.

### The Director's rule

Every factory module must be self-sufficient to enter, understand and continue. Pointing an agent at the module folder must be enough to discover its purpose, assigned role, current state, instructions and next permitted action. Tony must not reconstruct the module's instructions in a fresh custom prompt.

Both **CLAUDE.md** and **AGENTS.md** belong at each independently launched module entry, including the QAM subfolder. This applies to the factory's RRM, BIM, FFM, ABM and APBM packaging and to independently launched skill folders where those entry files are supported. Native skill entry requirements such as SKILL.md remain in place.

The reason for both files is operational continuity: one model or tool can be unavailable, and the Director must be able to continue through another without rebuilding the assignment. Role names are Architect, Engineer, QA Lead, QA Executor and Director; model names are not authority labels.

### What the two files must accomplish

1. **Explain the folder.** Identify the application, module ID and purpose; say whether this is an engineering module, a QA module or a skill; identify the role being performed here.
2. **Explain the next step.** Locate durable status, candidate identity, prior evidence, approved plan and outstanding checkpoint. Distinguish a first launch from a resumed or already completed run. Do not blindly restart work.
3. **Load the instructions.** Provide an unambiguous read order and working-directory rule; resolve every required local pointer. The folder can reference its enclosing module's frozen contract, provided that reference is available and explicit. Self-sufficiency does not require copying the contract into competing versions.
4. **Steer the Director when necessary.** Recognize the wrong folder, branch, module, role or phase when the available evidence makes that clear. Explain the mismatch in plain English and point to the correct location or next checkpoint. Do not guess, silently switch branches or begin unauthorized work.
5. **State boundaries.** Identify allowed operations, environment and credential handling, protected paths, stop conditions, deliverables, evidence locations, cleanup and who approves what. An unavailable prerequisite gets a specific blocker and owner.
6. **Preserve continuity across tools.** A replacement agent reads the recorded state and evidence, reports what is complete and pending, and resumes the permitted step. It must not claim access to an unavailable former session.

### One instruction set with two compatible entry files

CLAUDE.md and AGENTS.md must expose the same role, authority and workflow in a given folder. They may point to one common instruction body, but each must contain enough orientation and explicit routing for its supported tool to reach that body. Maintain both entries together so they cannot drift into conflicting instructions.

In a QAM folder, **both files assign the QA Executor role**. CLAUDE.md does not turn that agent into the Engineer. In an engineering module, both entries describe the engineering assignment and clearly identify the separate QA entry. The tool or model name never grants a different permission set.

This Director ruling supersedes the earlier proposed convention that CLAUDE.md is exclusively engineering and AGENTS.md exclusively QA in future packaging. Historical records remain unchanged. Do not interrupt an active RRM-004 run merely to retrofit filenames; any current-module change must follow its existing amendment process.

### The short launch and the approval boundary

The intended launch is a folder reference plus a simple request to start or continue. The entry files supply the detailed instructions. In QAM, the default first step is recon and a draft test plan, followed by the QA Lead's approval checkpoint before the main QA execution. Pointing at the folder does not approve all later phases, repairs, certification or Git operations.

The five seats remain: Architect, Engineer, QA Lead, QA Executor and Director. QA independence remains required even if a different tool fills a vacant seat. An agent that built the candidate does not self-certify it. The Director retains Git and credential authority.

### Required proof before calling this complete

The 10X Lab should demonstrate the following with fresh sessions in each supported tool:

- A folder-only launch makes the agent explain its role and correct first action without a bespoke launch prompt.
- The agent follows all required pointers and identifies an unavailable tool or prerequisite accurately.
- A launch from the wrong folder or phase produces useful guidance without an unauthorized action.
- A tool/provider substitution preserves the role, evidence, candidate identity and pending approval state.
- Recon stops for QA Lead plan approval; completed steps are not automatically repeated.
- Both entry files remain consistent when the common instructions change.

Exact automatic file discovery is a runtime capability to verify, not a fact inferred from a filename. If a supported tool needs a launcher or explicit bootstrap to read the correct entry, package that mechanism with the module so the Director's experience remains a simple folder handoff.

### Ownership and lesson for the next playbook

The QA Lead carries this requirement into the QAM playbook. The Architect includes both compatible entries when authoring the module package. The Engineer completes the factual handoff and durable state. The QA Executor verifies readiness; the QA Lead approves the resulting plan and later judges the evidence.

**Keep:** five independent seats, declared checkpoints and evidence-based QA.  
**Change:** move launch knowledge and recovery guidance into the module itself; support both entry filenames.  
**Drop:** bespoke startup prompts, tool-name-based role assumptions and asking the Director to repeatedly explain the same module.

No new reminder from Tony is required to carry this ruling into the next template/playbook draft. The full QAM pilot remains experimental; recording this explicit design requirement is not a claim that the pilot has passed or that all experimental practices have been promoted into production doctrine.

## Observation 005 — Director requirement for automatic QA Lead review packages, 2026-10-01

**Authority:** Tony Stark, Director, in the Cyber Pharma QA lab at 14:34 Asia/Dhaka.  
**Recorded by:** QA Lead / JARVIS.  
**Status:** Requirement for the QAM handoff design; current RRM-004 receives a bounded export instruction. No claim that the active entry files already implement automatic export, and no frozen contract is amended by this journal.

### What was observed

The Director supplied two screenshots of the first RRM-004 QAM recon return. They show the active branch as `qa/phase-3-rrm004`, the Executor reporting HEAD `5362b79ca724e454011e77aeaf4b11101176d0b5`, a draft test plan and execution/stop report, and preflight/recon evidence. The Executor stopped for an AC-403 ruling and QA Lead plan approval. The full reports have not yet been supplied to the QA Lead, so neither the scope question nor the preflight outcome has been adjudicated. This is not evidence of a product defect or certification.

The Director then had to ask which files to collect. The folder entry had worked, but the return handoff still depended on another conversation and manual file selection.

### The Director's requirement

Whenever the QA Executor reaches a checkpoint requiring QA Lead review, the Executor prepares a single indexed review package as part of that checkpoint. It states the exact decision needed and supplies the documents and evidence needed to make it. The Director uploads one package instead of discovering and collecting individual files.

For the current chat-to-repository arrangement, a ZIP is the transfer format. If the QA Lead has direct access to the same repository in a future setup, the same index can point to the files without creating an unnecessary archive. File transport does not grant plan approval, repair authority or certification.

### Checkpoint contents

| Checkpoint | Minimum review contents | QA Lead decision |
|---|---|---|
| Q1 recon or a recon stop | Recon/stop report, preflight outcomes, draft plan, current acceptance spec and rulings, manifest and engineering handoff labeled as claims, QA instructions/governing versions, evidence for each contradiction or blocker | Resolve or route the blocker; amend/approve the plan; authorize the next permitted step |
| Q2 execution return or a material execution stop | Execution report, AC evidence matrix, approved plan, findings and supporting evidence, candidate/change identity, current authority documents and inventory | Adjudicate findings; authorize bounded repair or the next closeout step |
| Q4 repair retest return | Repair identity/diff, prior finding links, affected-AC and required regression evidence, updated matrix; earlier attempts remain traceable | Determine whether the ruled repair resolves the finding |
| Q5 cleanup return | Cleanup report, privacy checks, retained-evidence inventory, final matrix and execution record, pilot results, links to any earlier reviewed package | Decide whether certification evidence is sufficient |

These packages reuse the existing reports and evidence. They do not create a second acceptance contract or require passing tests to run again for export. A stopped run is exported as stopped, with missing and not-run items explicit.

### Package rules

1. Include a short `REVIEW_START_HERE.md`: module, checkpoint/attempt, branch, full code-candidate SHA, full QA HEAD, baseline, export time, working-tree state, outcomes and exact questions/owners. Distinguish immutable candidate data from uncommitted QA outputs. Never label a draft plan approved.
2. Include an index of exported files with original repository paths, roles and SHA-256 hashes. Record missing requested files explicitly; do not invent empty evidence. Preserve relative paths so citations resolve. Exclude the index itself from its own hash list and report the final ZIP hash separately.
3. Include the current governing text needed to review the work, rather than assuming another chat has the same versions. Treat engineering measurements as claims, independent QA measurements as evidence, and rulings as authority. A later package may cite an already reviewed package for unchanged material if both sides retain it; a new reviewer receives a complete set.
4. Use an explicit file allowlist. Export relevant sanitized text, helper source and selected safe visual evidence where needed; omit environment files, credential values, tokens, cookies, authentication state, raw authenticated traces, dependency/build directories and Git internals. Use the existing privacy instrument on the export before release, with credentials confined to the local helper process. Record scan coverage and outcome without secret values.
5. Write within the authorized QA evidence lane. Keep export staging/ZIP files out of recursive evidence inclusion. Do not overwrite a prior attempt, delete original evidence, mutate Git, repair the product, rerun the QA board or begin the next phase merely to assemble a handoff. Archive integrity and member inventory must be checked.
6. End the Executor response with the package path, the decision required, any missing item, integrity/privacy outcomes and the next seat. A privacy-blocked export returns a safe blocker message and never releases the unsafe ZIP.

### Ownership and adoption

The QA Lead carries this return-package requirement into the QAM playbook. The Architect embeds the checkpoint and export instructions in the shared instruction body reached from both `CLAUDE.md` and `AGENTS.md`. The Engineer supplies factual build inputs; the QA Executor assembles its review package; the QA Lead adjudicates; the Director transports the package and retains Git authority.

For the running pilot, the QA Lead supplies a one-time export-only instruction under the existing QA evidence lane. This does not interrupt product work or reopen the frozen contract. Automatic packaging in future templates remains to be implemented and demonstrated.

**Keep:** recon before execution, independent QA Lead approval, visible blockers, one immutable candidate per evidence claim.  
**Change:** make the review package a required checkpoint output that the Executor assembles without another file-selection conversation.  
**Measure:** first-package sufficiency, missing-file follow-ups, Director handoff touches, package preparation time and privacy/integrity results.  
**Drop:** asking the Director to hunt for individual review documents and implying that a report path alone is an accessible handoff to a separate chat.

## Observation 006 — Q1 package reviewed; bounded scope correction, 2026-10-01

**Recorded by:** QA Lead / JARVIS. **Status:** Review of supplied evidence; Q2 has not run and no product certification is issued.

### Director correction: handoff location

Tony explicitly requires the handoff folder directly under the module's `QAM/` root. The canonical destination is `agent_docs/ACTIONS/RRM-004-CYBER-PHARMA/QAM/HANDOFFS/`, not `QAM/evidence/HANDOFFS/` or a remote response directory. This supersedes Observation 005's imprecise destination guidance. Future checkpoint exports must state the exact ZIP path. Historical packages/transcripts retain their original bytes and paths as provenance. A copied package is not recursively included in the next package.

### Evidence reviewed

Reviewed `RRM004_QAM_Q1_REVIEW.zip`, SHA-256 `34787660dd6c43c821e9ccf3689ebd7bd4762aec3f9c7b3f2128fe7c2161bc02`. Archive CRC passed; all 83 indexed members matched their sizes and SHA-256 values, with the index itself making 84 files. No requested file was reported missing. The QA Lead inspected the supplied reports, contract, rulings, plan, authorization history, preflight records and relevant helper source; this is not a fresh execution of the app or local credential scan.

Product candidate: `2fbc72f1f514049255f2b94054bd11cc77cbd158`. Q1 QA HEAD: `5362b79ca724e454011e77aeaf4b11101176d0b5`. Baseline: `649c36d0409c0b658cff14f779a09aad0c8e92b9`. Evidence separates pre-candidate changes, documentation-only successors, and uncommitted Q1 output.

Q1 evidence records 18/18 preflight rows passing, an independent install/build, one automated sign-in per role, both roles' protected-route access and logout denial, stopped server/removed browser state, and zero reported privacy hits. Q1 ran 13:29:22–13:42:29 UTC+06, with report timestamp 13:49:27. These are Executor-reported timestamps. The run stopped on a contract discrepancy, not a discovered product failure. Three helper corrections are recorded and must remain part of pilot metrics.

### QA Lead disposition

Q1 readiness evidence accepted. Q2 draft plan approved with the bounded AC-403 reconciliation and handoff-location amendment below; execution still requires Q1b, the Director's commit, clean-tree/candidate verification and the Q2 command.

AC-403's literal allowed-file list omitted five already-authorized predecessor closeout/journal edits. Authorization is documented by the archived SHA-record plan plus Director approval and the frozen P0 instructions. Resolve through an Engineer-recorded append-only A-15/AC-403 erratum identifying only the five observed hunks and their provenance. Retain the baseline, candidate, original AC text and all product protections. Twelve byte-identical response archive moves are historical Director archive activity under the governing J-09 rule; this grants no blanket `agent_docs/` exemption or new edits to closed modules. The Executor verifies the written ruling before closing Q1-C01 and recording plan approval. No application repair is indicated by this finding.

The independent Q2 plan retains dependency/native-library checks, instrument controls, image optimization and denial probes, cache regression, two environment builds, full required regression tests, preserved-path comparisons, and the authenticated viewport/theme image matrix. Q1 login proof does not substitute for Q2's image walk. Q5 cleanup and final QA Lead certification remain separate checkpoints.

### Lessons for the 10X Lab

- Preflight exposed a scope-accounting contradiction before the full QA body; retain that gate.
- Scope lists must reconcile approved preparation/closeout commits against the actual baseline before handoff. A docs-only successor does not by itself resolve older baseline-diff exceptions.
- One indexed, integrity-checked package enabled adjudication without asking the Director to collect more individual files.
- Packaging must be a checkpoint output in the module instructions, with `QAM/HANDOFFS/` as the obvious destination. The extra packaging prompts and folder relocation are pilot friction, not successful zero-touch automation.
- Automated credentials eliminated manual login work in the reported Q1 run; Q2 autonomy and final certification remain unproven at this checkpoint.

This entry records an experimental pilot outcome. It does not promote QAM changes into production QA doctrine or claim the RRM-004 campaign is complete.
