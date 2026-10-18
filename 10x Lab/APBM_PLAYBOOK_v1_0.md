# APBM PLAYBOOK v1.0

**Application Phase Build Module**  
**Date:** 18 October 2026, Asia/Dhaka  
**Authoring seat:** JARVIS Master / Architect · **Director:** Tony Stark  
**Status:** Final authored v1.0, delivered under Tony's instruction to finalize the APBM method. Repository installation and Factory-wide synchronization are separate actions; neither is claimed here.

## 1. The operating promise

Build a useful, bounded application phase with one well-prepared engineering assignment and one well-prepared independent QA assignment. Give the Director clear decisions and usable returns. Keep routine implementation, test execution, evidence collection and packaging with the agents.

The target is **two engineering passes plus two QA passes**:

| Pass | Work | Exit |
|---|---|---|
| E1 — engineering recon and approval | Investigate the real repository, runtime, dependencies and integration contracts; return consolidated facts and a proposed approach | Architect resolves findings, freezes the phase contract and assembles the implementation-ready module; Director approves scope and effects |
| E2 — engineering execution | Build the complete approved phase, self-verify, prepare the factual QAM handoff and review package | Architect accepts engineering readiness; authorized Git owner commits the candidate; checkout ownership transfers explicitly |
| Q1 — independent QA recon and plan approval | Challenge the claims, check readiness and prepare the exact independent test plan | QA Lead approves the plan/candidate; Director releases execution |
| Q2 — independent QA execution | Run the approved campaign continuously, preserve evidence, return findings and results | QA Lead adjudicates; required cleanup, certification and closeout follow |

E1/E2 are planning labels introduced by this playbook, not additional Factory gates. Q1/Q2 retain their QAM meanings. The original pilot did not consistently use the E1/E2 labels.

**Accuracy outranks pass count.** Recon can take additional exchanges when evidence requires them. The improvement is to investigate predictable questions together before execution. E2 and Q2 should then run continuously through routine work within their approved boundaries. Four passes does not mean four chat messages, four approvals, no repairs, or no closeout.

## 2. When to use APBM

ABM means **Application Build Module**: one bounded whole-app assignment. APBM means **Application Phase Build Module**: one bounded phase in a planned application campaign. A campaign is the coordinated sequence of phases; an individual APBM is not the entire campaign.

Use APBM when work benefits from independently useful checkpoints, different dependency readiness, a meaningful risk boundary, or sequential integration. Use ABM when the whole app can be built and independently checked as one coherent assignment. A small app may deliberately use APBM to pilot the method, as Stark Agent Workspace did.

Do not split a phase just because the task is long or because an agent prefers small prompts. A phase should deliver a user-visible outcome or a verifiable enabling capability. Internal implementation stages belong inside the same E2 assignment unless a real approval, dependency or acceptance boundary requires a separate phase.

For a defect discovered after closure, use the smallest appropriate Factory repair module, usually FIX/BIM/RRM according to the actual scope and installed doctrine. ABM/APBM are available for broader work; neither is mandatory for every bug.

## 3. Always start with a phase map

Create a short campaign map before authoring build modules. It must show the overall outcome, phases, prerequisites, acceptance boundary, current status, next owner and deferred work. Use plain statuses such as PLANNED, RECON, BUILDING, QA, BLOCKED and CLOSED, with factual detail in the module records.

Plan ahead enough to expose dependencies. Do not pretend every future phase has a frozen design. Detail the next phase, outline later phases and version the map when evidence changes the plan. Never silently move a failed requirement into a later phase to make the current one pass.

The map must distinguish:

- phase engineering and Gate Q;
- integration into the main line;
- Director hands-on acceptance, when required or deliberately deferred;
- whole-app/integration review required by the campaign;
- deployment and Gate D.

A phase certificate proves its stated scope. Several child certificates do not prove their combined workflow. An independently authored aggregate module also receives its own QAM, referencing valid child evidence and testing the actual seams without gratuitously repeating unchanged work.

## 4. Seats and authority

| Seat | Owns | Does not self-authorize |
|---|---|---|
| Director | Product direction, scope/risk decisions, credentials, release and Git authority; may explicitly delegate bounded operations | Unsupported claims of production readiness |
| Architect | Phase map, recon assignment, accepted contracts, design reconciliation, module/QAM assembly, repair scope and closeout | A QA certificate in place of the independent Lead |
| Engineer | Recon, implementation, self-verification, factual handoff and authorized repairs | Independent QA approval or certification |
| QA Executor | Independent recon, draft plan, approved testing, evidence and authorized cleanup | Product fixes, waived failures, raised hard limits or Gate Q |
| QA Lead | Standing risk requirements, plan approval, findings adjudication, cleanup disposition and certification | Silent changes to the product contract |
| Designer, when needed | Approved visual direction, tokens, canonical screens, states and responsive behavior | Runtime/persistence claims from mockups |

Names and models can change. Authority follows the seat. Record the actual tool/model when verifiable; otherwise say it is unknown. Changing an agent's label does not establish independent verification of its own implementation.

Maintain **one active writer per checkout**. The outgoing owner stops owned services and browsers, records release, and pauses. The incoming owner verifies identity and explicitly accepts ownership in `QAM/HANDOFFS/QA_HANDOFF.md`. Record any later return to engineering for repair. The Director may perform the declared Git steps while agents are idle.

Do not make the Director run routine read-only commands simply because they are Git commands. Recon agents may inspect status, history and diffs under their assignment. Mutating Git operations follow current authorization. A delegated local commit does not imply permission for push, merge, branch deletion or history rewriting.

## 5. E1: comprehensive recon before implementation

The Architect supplies one written mission containing all foreseeable questions, their evidence sources, permitted actions and conditional follow-ups. Read the actual code and runtime evidence before deciding the implementation. Existing documentation is an input, not proof that the deployed system matches it.

Use `TEMPLATES/RECON_ASSIGNMENT.md`. Cover these areas as applicable:

| Area | Questions to settle |
|---|---|
| Repository and instructions | Actual root, branch, full HEAD, dirty files, installed instructions, protected paths, placement rules and existing skills |
| Existing behavior | What already works? What is missing? Where are the actual callers, state stores and rendering boundaries? |
| Runtime and build | Versions, dependency lock/install match, build prerequisites, fonts/assets, ports, production versus development behavior |
| Identity and access | Where is identity resolved? What browser input is trusted? Which frontend and upstream boundaries are protected? |
| API and data contracts | Actual request casing, response shapes, error codes, title/state/timestamp behavior, ownership and authority of each data source |
| Persistence | What survives reload, sign-out and reconnect? What restart/deployment durability is demonstrated versus unknown? |
| Async behavior | Cancellation, late responses, navigation, target/user/agent/session changes, retries and uncertain writes |
| Design | Current theme sources, approved screens, existing usable UI, responsive breakpoints, keyboard behavior and states |
| External effects | Logins, refreshes, reads, creates, sends, deletes, cost-bearing tools, test namespace and cleanup permissions |
| Validation | Maintained tests, fixture limits, live checks, missing instruments, human checks and evidence export |
| Delivery | Deployment inputs, excluded files, unresolved public access, migration/rollback needs and phase boundaries |

Trace the whole request path. A login may invoke middleware, role reads and session checks in addition to a password request. Budgets derived from guesses produce false stops and tempt unauthorized overrides.

Plan bounded capability probes inside E1 when necessary: exact target, identity, harmless input, maximum effects, timeouts, no-retry policy where required, and stop/retention behavior. Read-only business work can still create auth sessions or audit records. An agent message can trigger tools, cost and writes; select the test agent accordingly.

Conditional branches prevent avoidable back-and-forth. Example: “If the list omits titles, inspect the authorized history response and report a fallback; do not add a metadata database.” Missing old data is an observation, not automatic proof of a broken persistence engine. Ten-day retention does not prove restart durability.

Aggregate independent blockers and continue safe investigation. Stop dependent work at a genuine boundary. Return one evidence package with EVIDENCE, INFERENCE, CLAIM, GAP and QUESTION clearly distinguished. Include proposed scope, alternatives, dependency decisions and what is still unverified.

The Architect then resolves predictable questions together. A full new recon is unnecessary when a narrowly identified delta can refresh the evidence, subject to the installed recon policy. Do not bypass an applicable rule under the label of efficiency.

## 6. Assemble the implementation-ready phase

Each APBM contains its own populated `QAM/` from initial module authoring. The preliminary E1 mission is discovery, not a build module released without QAM. See the companion folder specification and the unchanged governing QAM reference.

The phase pack must establish:

1. The outcome, exclusions, prior-phase dependencies and approved scope decisions.
2. Actual baseline, intended branch, allowed/protected paths and owner.
3. One canonical acceptance specification with observable outcomes and negative cases.
4. Accepted data/API/identity contracts and design references.
5. Implementation strategy, relevant tests, regression obligations and completion duties.
6. Environment, credentials, effects, timeouts, budgets and stop/resume rules.
7. A module-specific QAM skeleton, with independent plans/results/approval unfilled.
8. Automatic review export, cleanup ownership, Git handoff and closeout expectations.

Acceptance criteria belong to the Architect-approved contract before code. Engineers can propose technical contracts; the Architect reconciles and freezes the accepted version. Do not rewrite criteria after seeing what implementation produced. Authorized changes go in the dated rulings lane with affected ACs and impact.

Preserve usable existing behavior and approved visual direction. A designer handoff needs actual source tokens and screens, not a verbal resemblance to another product. Reuse valid design approval; do not ask again without a material change.

Prefer the simplest architecture supported by evidence. In APBM001, ADK supplied conversation discovery and history. Deferring rename/archive avoided introducing metadata storage solely for two features. This is an example of a scope decision, not a universal ban on databases.

Avoid overprescribing a guessed file count. “Six files, no screen changes” is not a safe boundary if navigation or recovery behavior is part of acceptance. Declare real allowed areas and protections; seek a bounded amendment when work must cross them.

## 7. E2: one continuous engineering execution

The launch prompt points to the complete module. It should not carry operating rules missing from the files.

The Engineer validates the package, reads applicable instructions and checks the actual checkout before installation. Unpack outside the repository; install only the approved module path; preserve differing existing work. Then implement the entire released scope and self-verify without pausing for approval of each routine edit.

Engineering owns its maintained tests and the complete factual handoff. Return commands/results, failures, changed-path inventory, contract deviations, environment requirements, reproduction steps, known limits and evidence references. Preserve failed attempts. Distinguish fixture success from live behavior and engineering claims from independent QA.

Write engineering records to the governed engineering paths; general session records go under `agent_docs/SESSIONS/` in Tony's convention. QA records and recovery belong inside the module's QAM. Do not create root session files or root QA pointers. Resolve conflicting active instructions before launch.

Before the candidate commit exists, identify the result as uncommitted with a file inventory; never invent its SHA. After the authorized Git owner commits, use an external receipt or subsequent handoff record to pin the full SHA. Do not create endless documentation commits trying to put a commit's own hash inside itself.

Architect review may identify one bounded correction. Return one consolidated correction with its required verification. No new general recon or full live walk unless the changed risk or governing plan requires it. Exhausted effect budgets do not replenish automatically.

## 8. Q1/Q2: embed the established QAM process

`REFERENCES/QAM_PLAYBOOK_v1_0.md` governs packaging and the two-shot QA process; `REFERENCES/QA_PLAYBOOK_v1_1.md` supplies the referenced QA doctrine. They are preserved source snapshots, not new revisions authored here. Use the applicable adopted versions in each real repository and resolve material conflicts before execution.

Q1 checks readiness and independently plans tests across the full frozen scope. It can perform only the setup/probes explicitly allowed for Q1. It cannot spend Q2's session/message budget before release. Review the actual source, prior evidence, configured target and account needs; do not certify availability from an endpoint's HTTP response alone.

The plan must bind the candidate, contract/rulings, environment, effect limits, commands, expected outcomes, independent references, controls, browser matrix, regression and evidence outputs. The QA Lead approves the exact plan. The Director releases Q2. Approval and release may be conveyed in one handoff when both authorities are explicit; neither is inferred from a generic “go.”

Q2 validates instruments before relying on them, checks current identity and executes the approved plan continuously. Routine local helper corrections are allowed only within the plan's lane; preserve failures and revalidate the helper. A helper change that expands effects, changes acceptance, raises limits or weakens the test needs the relevant authority.

Use actual application boundaries when the claim depends on them. A synthetic harness can prove only what it exercises. Race tests need distinct user/agent/target/session data, controlled response timing, and the real navigation action where that boundary is under test. Identical fixture content can hide cross-context contamination.

Static scanners must prove they find real callsites, including multiline calls and legacy paths. Empty matches are not a pass. Pair an expected-failure control with an allowed/clean control when needed to prove the instrument failed for the intended reason. Make state promises and request counters observable before spending the live budget.

Use risk-based browser coverage from the phase contract. Record the viewport/theme/role/workflow combinations and any omitted browser families. Screenshots complement assertions; neither alone proves the complete application. Do not sum overlapping suites into a fictional unique test count.

## 9. Effects, credentials and stop behavior

Define budgets per pass, target and attempt, with cumulative totals where applicable. Identify what each counter measures: UI submission, actual upstream dispatch, password login, refresh, role read, session creation, agent run or business mutation. Failed attempts and retries consume the corresponding allowance. Reset only by explicit authority.

Distinguish approved **hard limits** from nonblocking **observations** before execution. Hard limits fail closed. An Executor cannot convert a hard limit to a measurement because the application makes more requests than predicted. Where read traffic is uncertain, investigate it in authorized recon or seek an appropriate evidence-based envelope; do not guess a tiny cap and later ignore it.

Stop dependent work on wrong identity, invalid instruments, conflicting contracts, privacy exposure, missing authority, or unavailable required environment. Preserve useful completed evidence and report the owner, exact decision needed and safe resume point. Do not stop unrelated safe work merely to return one missing filename at a time.

Temporary credential automation may use a Director-supplied ignored and untracked `.env.qa.local` when supported and authorized. Use the login identity the UI expects, not a guessed database UUID. Validate schema without emitting values; keep credentials in the permitted helper's memory. Restrict local permissions where applicable. Do not read, hash or edit a protected `.env.local`; hashing is reading. An authorized application process loading its ordinary environment is a different operation and must be addressed explicitly by the plan.

Keep credentials, cookies, auth state and raw sensitive traces out of logs, screenshots and archives. Validate privacy scanners using synthetic controls. Run any authorized credential-value scan before deleting its source; later scans must accurately state that they are pattern scans or comparisons against previously scanned bytes. Never preserve secret values or hashes to enable later scanning.

Uncertain writes are not safe retry opportunities. Retain a returned session ID, show honest status, and use an authorized read/check-history path. Matching message text alone does not prove delivery or exactly-once semantics.

## 10. Findings, repair and proof boundaries

The QA Lead classifies product failures, environment issues, instrument defects, contract gaps and proven inherited findings. The Architect scopes product repairs; the Engineer implements them; the authorized Git owner commits; independent QA retests under an approved binding. An Executor does not repair the product to make its own campaign green.

Carry forward applicable evidence with its original candidate and limitations. Retest the changed behavior and required regression; repeat live work when the revised-candidate policy requires it. Do not rerun a successful suite simply to package an addendum, record a ruling, or move documents.

Record separately:

| Claim | Required basis |
|---|---|
| Product Gate Q | QA Lead certificate naming exact candidate, scope and limitations |
| Process compliance | Actual adherence to approvals, gates, privacy and effect limits |
| Cleanup acceptance | Verified approved actions, retention and remaining artifacts |
| Integration | Git merge/push receipt and resulting identity |
| Director acceptance | Actual personal review or explicit deferral |
| Gate D | Authorized verification of the deployed revision/environment |

A green product result cannot erase a process violation. A scoped demo pass cannot become a production-security or multi-user certificate. A future phase's evidence may resolve a historical finding through an explicit disposition; it must not silently rewrite old records.

## 11. Automatic returns and restart discipline

Each substantial E1/E2/Q1/Q2 return includes a short human summary, next owner, exact decision/action, and the required review package. Engineering exports live under the declared engineering lane; QA exports under `QAM/HANDOFFS/`. Provide a byte-identical Downloads copy when requested and the exact absolute upload path. The Director should not hunt through temporary directories or assemble evidence.

An indexed ZIP includes the review entry, identities, reports, applicable contracts/rulings, needed authority and supporting evidence. Index every payload with path, purpose, bytes and SHA-256; exclude the index from its own entries. Put the completed ZIP's checksum in an external receipt. Check membership, duplicates, safe paths, hashes, integrity and privacy. Do not insert the receipt into the ZIP afterward or nest all previous archives by default.

Do not regenerate a valid archive just because its receipt had a minor administrative label. Preserve frozen packages. Link later corrections as dated successors. Packaging is not another test run.

Keep current state short: current phase/attempt, identities, latest package, active stop, owner and next permitted action. Preserve dated history below or by reference. On resume, compare the requested operation to the actual state. If already complete, report completion; do not repeat testing or deletion under an obsolete instruction.

## 12. Closeout in one administrative pass

Plan closeout during module authoring. When results are ready, combine the remaining recordkeeping, retention decisions, owner handoff and Git preparation into one bounded instruction wherever authority allows. Do not invent another recon or QA campaign.

1. QA Lead adjudicates and issues the exact scoped verdict; required cleanup follows the governing sequence.
2. Record that authority unchanged. Preserve qualifications, historical deviations, failed runs and justified instruments.
3. Current checkout owner prepares explicit durable commit paths and separately identifies unrelated work. Check credential exclusions and all tracked/untracked changes.
4. Director or authorized delegate commits approved records and resolves unrelated changes. Verify the complete successor diff: product/test/config/dependency identity is not inferred from a “docs” message.
5. Architect confirms closeout against certificate, cleanup and the governed clean-tree condition. Record follow-ups, owners, personal-acceptance status and deployment status.
6. Authorized Git owner integrates the exact branch, updates the target safely, handles conflicts explicitly, pushes, and records full merge SHA and final status. Preserve certified bytes; material integration changes require impact review.
7. Update the campaign map. Release the next phase only under its own scope and prerequisites.

Session relocation is housekeeping, not a product retest. Verify contents, stage explicit paths, and keep intentional deletions distinct from moves. Do not auto-delete old records or restore Director-owned changes. Git history may preserve deleted material, but that is not a reason to silently remove current evidence.

Git instructions must be prepared from current branch/HEAD/status and target ancestry. Prefer scoped staging and descriptive `--no-ff` merge commits under Tony's convention. Do not pull another branch into an active dirty QA checkout to satisfy a generic “pull first” habit. Do not force-push, reset or bypass branch protections without applicable authority.

## 13. KISS rules for speed

- Gather related recon questions and conditional probes before handing off E1.
- Give agents the complete assignment, including verification and packaging.
- Use one stable module entry per seat; keep prompts short and copyable.
- Resolve contract, environment and instruction conflicts before execution.
- Reuse valid evidence, approved design and existing project skills.
- Ask the Director for actual decisions, credentials or access—not routine file assembly.
- Keep reports human-readable; put detail in the evidence package.
- Run extra checks only for a real remaining risk or required gate.
- Bundle closeout decisions and avoid documentation-only approval loops.
- Preserve the truth about extra passes. Never optimize the reported count by hiding failures.

## 14. Definition of done and adoption

An APBM is closed when its approved engineering scope is complete; independent QA disposition and required cleanup exist; follow-ups have named owners; durable records are retained and committed; certified identity is reconciled through closeout; authorized integration is confirmed; and the campaign map accurately records outstanding Director acceptance/deployment work.

Optional personal comfort checks may be explicitly deferred. Required acceptance criteria cannot be waived by calling them comfort checks. Phase closure does not close the wider product roadmap.

This v1.0 is supported by the APBM000/001 pilot experience and the cited QAM doctrine. The pilot demonstrates a working UI and live single-user frontend, repair/retest and eventual integration. It does **not** demonstrate a clean four-pass process, all runtime combinations, Hermes integration, multi-user production security, or deployed durability.

Use the companion templates to author the next module. The Factory Doc Sync Architect installs this package through the existing sync process, reconciles conflicting active instructions and links the canonical QAM version. No new installable agent skill is created by this documentation package.
