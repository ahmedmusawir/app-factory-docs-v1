# STARK QAM — Evidence-backed operating model and playbook draft

**Version:** 0.1 · **Date:** 2026-10-02, Asia/Dhaka  
**Author:** JARVIS / QA Lead · **Director:** Tony Stark  
**Audience:** Master Jarvis, Architects, Engineers and QA seats in the 10X Lab  
**Status:** EXPERIMENTAL DRAFT FOR INTERNAL LAB VALIDATION. No production doctrine is amended by this document.

## 1. The decision this document asks the Lab to make

Build and test a reusable QAM package that preserves the five-seat factory while removing repeated preparation, manual browser matrices, document hunting and missing handoff inputs. Use RRM-004 as field evidence, including its friction. Validate the proposed template on an internal app before proposing wider adoption.

The desired Director experience is straightforward: place one Architect-authored module pack; let the Engineer build and prepare the handoff; commit the candidate and create its QA branch; point the QA Executor at QAM; review recon with the QA Lead; authorize one continuous QA run; handle only declared human checkpoints; receive an indexed result package; route any ruled repairs; receive certification; close out and merge.

Tony wants to remain involved in scope, evidence, Git and important judgment. Success is less repetitive work with equally strong verification. It is not removal of the Director, elimination of independent review, or a claim that every job finishes while unattended.

**Field result:** RRM-004 Gate Q PASS, cleanup accepted, 31 product criteria passing. Q2 executed with zero observed Director interventions. The pilot verdict remains PARTIAL SUCCESS because Q1 stopped for a contract correction. Read `01_EVIDENCE_DOSSIER.md` for provenance, exact numbers, limitations and current closeout state.

## 2. Plain-language definitions

| Term | Meaning |
|---|---|
| Engineering module | The bounded build assignment: RRM, BIM, FFM, ABM or one APBM phase |
| QAM | A self-contained QA subpackage for that assignment and its candidate; it is not a second product implementation |
| Acceptance contract | What the product must do, frozen before build with an explicit correction lane |
| Engineering handoff | What was built, how to run it and what the Engineer claims to have checked |
| Test plan | How independent QA will challenge the candidate, including failure cases, reference values and instruments |
| One-shot execution | One authorized continuous execution attempt between planned checkpoints, subject to enumerated stops |
| Gate Q | QA Lead's evidence-based product certification before deployment/integration steps specified by the project |
| Cleanup acceptance | Confirmation that retained records are deliberate, temporary sensitive state is removed, and the QA branch can leave QA |
| Pilot verdict | A separate judgment about how well the experimental workflow performed |
| Gate D | Deployed-system verification where required; local Gate Q does not imply it |

One-shot does not mean one prompt for the entire lifecycle. Recon, plan approval, execution, adjudication, cleanup and Git decisions remain distinct. A correct stop is useful information, not an agent failure to conceal.

## 3. Status and authority of this draft

This package contains three kinds of material:

1. **Existing requirements:** five-seat separation, frozen acceptance with errata, literal grading, evidence ownership, Director Git authority and the applicable project cleanup rules.
2. **Director design requirements for future packaging:** both CLAUDE.md and AGENTS.md, simple folder entry, useful wrong-folder guidance, automatic indexed review packages directly under QAM/HANDOFFS/, main-dev authorization for the current Cyber Pharma pilot, and no automatic promotion of Lab experiments into production doctrine.
3. **Proposals needing validation:** the generic state record, completeness checks, resume protocol, broader runtime portability, reusable exports and the adaptation of this process to larger apps and backend writes.

A template must never override a live module's frozen contract just because it is newer. Each authored pack states its governing versions, precedence and permitted exceptions. A genuine conflict is routed to the responsible seat and recorded; an agent does not invent its own hierarchy.

The supplied QA_PLAYBOOK v1.1 and doctrine journal v0.3 contain historical rules. J-11 replaces the older disposable-QA-branch model with a forward certification line. J-19 supersedes blanket retention with bounded cleanup. RRM-004's approved Q5 sequence places credential cleanup before final certification. Future packs must state their sequence explicitly, preserving both product certification and cleanup obligations; do not blindly paste conflicting historical sequences together.

## 4. Five seats, five responsibilities

| Seat | Owns | Required output | Authority limit |
|---|---|---|---|
| Architect | Scope, pre-build acceptance, package skeleton, scope rulings and closeout instruction | Complete module with QAM, gradable ACs, bounded repair/closeout instructions | Does not turn engineering claims into independent QA evidence |
| Engineer | Implementation and factual readiness | Engineering report, handoff, manifest, reproduction and changed-file facts | Does not approve the QA plan, grade independent QA or self-certify |
| QA Lead | Standing risks, plan approval, findings adjudication, retention judgment and certification | Approved plan, ruled findings, certificate and separate pilot verdict | Does not quietly rewrite product requirements or claim unrun tests |
| QA Executor | Recon, plan draft, independent measurements, evidence and authorized cleanup | Checkpoint packages, matrix, findings, metrics and cleanup record | Does not repair product code, self-adjudicate, self-certify or mutate Git |
| Director | Scope decisions, access, designated human judgment, Git and release | Approvals, commits, environment authority, rotation/merge records | No obligation to perform repetitive mechanical QA when agents can verify it |

These are roles, not models. In a QAM folder, both CLAUDE.md and AGENTS.md assign QA Executor responsibilities. The same filenames at the engineering module root assign the engineering role and point to the separate QAM entry. Provider substitution changes neither approval state nor permission.

The Engineer may write engineering tests and improve testability within authorized build scope. QA may use those tests, inspect them and add independent probes. Independence means that QA derives expected results, checks scope and challenges failure cases; it does not require discarding useful engineering tests or duplicating every test.

## 5. Who creates QAM, and when

Use **Scenario One with explicit authorship**. The QA Lead authors this playbook and standing risk requirements. The Architect authors the QAM skeleton inside the same module pack before engineering begins. The Engineer fills factual fields as the build proceeds and completes its handoff in the same assignment. After the Director commits, QA recon resolves the actual immutable identity and drafts the test plan. The QA Lead reviews and approves that plan before Q2.

The QAM folder is ready for recon when the Engineer finishes. It is not yet approved for the main QA execution. This distinction avoids asking the Engineer to predict the final independent plan or a future commit hash.

The Architect owns canonical acceptance text. The Engineer can identify ambiguity and propose corrections through the designated lane. It must not manufacture new acceptance criteria after seeing what the implementation happens to do. QAM links to the enclosing contract rather than copying it into a competing authority file.

The default new pack must include handoff authoring in its definition of engineering completion. There should be no extra trip to the Architect for a prompt whose only purpose is “now write the QA handoff.”

## 6. Package layout and ownership

These are relative paths from the engineering module root. Actual filesystem layouts are provided under `TEMPLATES/`; there are no hidden runtime assumptions in this table.

| Path | Owner / purpose |
|---|---|
| CLAUDE.md and AGENTS.md | Architect; engineering entry and role routing |
| ACCEPTANCE_SPEC.md | Architect/Director; frozen product contract with correction lane |
| RULINGS_ADDENDUM.md | Authorized rulings, exact scope, approval provenance |
| QA_HANDOFF.md, EXECUTION_LOG.md, evidence/ | Engineer facts and claims; existing project locations may remain |
| QAM/CLAUDE.md and QAM/AGENTS.md | Matching QA entry files for supported tools |
| QAM/QAM_ENTRY.md | Common orientation, read order, role, state and next-action routing |
| QAM/QAM_MANIFEST.md | Engineer facts with candidate resolved after commit |
| QAM/QAM_RISK_REQUIREMENTS.md | QA Lead standing risks, Architect input clearly attributed, module-specific review |
| QAM/QAM_PREFLIGHT.md | Concrete environment, identity, instrumentation and permission gates |
| QAM/QAM_TEST_PLAN.md | Executor draft; QA Lead amendment and approval |
| QAM/QAM_STATE.json | Proposed durable phase, identity and approval pointers; no credentials |
| QAM/QAM_PROMPTS.md | Phase procedures and recovery instructions; default entry dispatches here |
| QAM/QAM_CHECKPOINTS.md | Declared Director/QA Lead decisions, evidence and actual status |
| QAM/AC_EVIDENCE_MATRIX.md | Executor measurements; QA Lead adjudication recorded separately |
| QAM/QAM_EXECUTION_REPORT.md | Attempts, commands, result summaries, findings and limitations |
| QAM/REPAIR_PROPOSAL.md | Executor's proposed repair scope, only if needed; not authorization |
| QAM/QAM_CLEANUP_REPORT.md | Executor cleanup evidence and retention decisions |
| QAM/QAM_CERTIFICATION.md | QA Lead-issued verdict; attributed transcription allowed |
| QAM/QAM_PILOT_CHARTER.md | Pre-approved experimental goals, metrics and verdict rules |
| QAM/QAM_PILOT_RESULTS.md | Experimental metrics, QA Lead process verdict, Director adoption decision |
| QAM/ARTIFACT_INVENTORY.json | Evidence purpose, retention, provenance, size and hash at stated cutoff |
| QAM/GOVERNING/ | Required local bodies with version/provenance and source hashes |
| QAM/AUTOMATION/ | Authorized QA-only helpers, not product runtime dependencies |
| QAM/evidence/ | Attempt-scoped raw/sanitized measurements with protected historical records |
| QAM/HANDOFFS/ | Obvious review-package destination; never buried under evidence/ |

A physically separate QA Lead chat receives an indexed ZIP. A QA Lead with access to the same immutable repository can consume the same index in place. Transport is an access question, not a reason to alter the approval boundary.

Templates must not ship fabricated PASS statuses, completed results, a pre-issued certificate, private credentials or a fixed SHA copied from this case study. Blank fields must say NOT RUN, NOT RECORDED or NEEDS AUTHORING as appropriate.

## 7. Self-sufficient entry and recovery

Every independently launched folder must tell the arriving agent:

1. What this module is and which role it is occupying.
2. Where the repository root and canonical authority live.
3. Which phase has completed and which action is next.
4. Which branch/candidate/plan approval to verify.
5. Which paths it may write and which operations need another seat.
6. Where to save output and how to return it.
7. How to stop or resume without losing evidence or rerunning everything.

Keep both entry files aligned through one common instruction body. Neither may contain a conflicting second copy of the rules. Test actual discovery in every supported runtime: filenames do not guarantee automatic loading. If a runtime needs an explicit bootstrap, package it so the Director still supplies only the folder pointer.

A fresh session must report, for example: “I am the QA Executor for module X. Recon is complete; plan approval is pending. I can prepare the Q1 review package, but cannot start Q2 yet.” It must not pretend to remember the previous agent session.

Wrong folder, wrong branch, missing approval or a completed module gets a short explanation and an exact next location/checkpoint. No automatic branch switching, reset, repair or restart. Within a shared repository, use one active writer at a time; the Engineer and Executor may both have sessions, but ruled repair and QA measurement must not race on the same worktree.

## 8. The operating sequence

### Before engineering: author a ready assignment

The Architect checks scope against the actual baseline and known preparation commits. Historical docs and archive relocations receive precise treatment now, not a blanket exemption later. Define permitted product files, protected files, engineering/QA documentation lanes and explicit build/runtime dependencies. All ACs must have observable pass/fail rules.

The QA Lead contributes mandatory risk questions and evidence classes. The Architect may flag risks but does not dictate how independent QA must declare them satisfied. Freeze the acceptance contract and record version/provenance.

### Engineering execution and handoff

The Engineer follows the approved build plan, self-checks and records artifacts as claims. It fills the manifest and reproduction instructions, including environment, roles, required services and any known limitations. Missing values stay explicit. It returns selective staging commands; the Director owns the commit.

The Director commits the candidate and creates the QA branch. QAM resolves the full SHA from Git and reconciles it with the handoff. A pre-commit phrase such as “Director's P2 commit” must not silently remain the certified identity. A documentation successor is allowed only when compared and classified; `src/` alone is not enough to establish product identity when lockfiles, config or migrations matter.

### Q1: readiness, independent recon and plan draft

The Executor reads the package, pins identity and checks readiness before the expensive test body. It inspects scope, current rules and available evidence, challenges the proposed instruments, and drafts the independent plan. It measures authorized authentication readiness as specified, rather than asking the Director for a manual matrix.

Q1 returns exactly one review package and stops for the QA Lead. A blocker includes its classification, failed check, evidence path, owner and smallest next action. Gather independent safe findings where permitted; do not loop through a failing environment or keep attempting credentials without a stated retry policy.

### Q1b: record the reviewed plan and any rulings

The QA Lead amends or approves the plan. The Architect/Director resolves contract scope where required; the Engineer records authorized errata without rewriting frozen history. The Executor records exact approval attribution and verifies the resulting pointers. A plan draft is never upgraded to approved merely because it exists.

The Director commits the approved instructions and recon outputs, then releases Q2. Bind approval to the candidate, plan version/hash and ruling set. A substantive plan edit requires review; document-only state bookkeeping does not warrant a new full test cycle.

### Q2: continuous independent QA execution

Revalidate identity and readiness affected by elapsed time. Run the approved checks, gather evidence, update the AC matrix and export the review package in the same assignment. Continue through ordinary passing checks and authorized helper correction. Stop on a defined condition when trust, access, scope or safety is no longer established.

No periodic “may I continue?” prompts for already authorized stages. No omission of checks to claim one-shot success. Independent checks may run concurrently if they do not share mutable build output, fixtures, ports or sessions; sequential dependencies stay sequential.

### Adjudication and Q4 when needed

The QA Lead determines whether a finding is an implementation defect, contract gap, environment failure, invalid instrument or informational observation. Only a product defect with a ruled scope goes to the Engineer as repair work. Follow the repair process in section 12. No Q4 occurs just because a helper needed correction.

### Q5: cleanup and final review package

After evidence adjudication permits it, perform authorized cleanup in the specified credential order. Preserve durable evidence and failed attempts, remove only identified disposable/sensitive artifacts, verify product identity, update inventories and produce the Q5 package. Q5 is not an excuse to repeat the test board.

### Certification, Architect closeout and integration

The QA Lead issues the exact certificate and the separate pilot verdict. The Architect receives a self-contained closeout handoff including that text, current identities, pending Director items and evidence references. The Engineer can transcribe the verdict but must not create or reinterpret it.

The Director commits closeout, merges the active QA line according to the project rule, pushes and supplies resulting SHAs. A final bounded documentation touch records those SHAs where required. A commit cannot contain its own final hash; do not create an endless “one more SHA” loop. Gate D remains a separate deployed verification obligation when applicable.

## 9. Preflight that catches real blockers

Preflight must be small enough to run routinely and specific enough to prove readiness. RRM-004 used 18 QF rows; that number is not a universal standard.

| Group | Required question | Example evidence |
|---|---|---|
| Identity | Is this the intended repo, branch and candidate? Are intervening changes classified? | Full SHAs, ancestry, product/config diff, entry tree state |
| Authority | Can the Executor read the actual spec, rulings, plan requirements and governing bodies? | Resolved paths, versions, hashes, conflicts list |
| Runtime | Are package manager, runtime, browser and native libraries usable? | Versions and minimal functional probe |
| Network | Can the authorized install/build dependencies be reached? | Bounded probe or relevant build failure evidence |
| Environment | Is the selected target the authorized one, available and configured? | Resolved target comparison without secrets, health result |
| Accounts | Do the dedicated identities exist and have the required server-resolved roles? | Login/role/logout result, no tokens or passwords |
| Browser | Can automation actually interact and collect safe evidence? | Small known-behavior control, capture location |
| Instrument | Does the check fail when deliberately given an invalid safe input? | Positive, negative and boundary control results |
| Evidence | Can outputs be written, indexed, privacy-checked and exported? | Writable lane, tool availability, scanner controls |
| Side effects | Which state can tests change, and how will it be restored? | Authorized operation and cleanup plan |

For Cyber Pharma RRM-004 the authorized target was main development, not SCRATCH. For a future module, copy neither environment choice nor credentials blindly. Resolve the authorized configuration once and compare it at each relevant entry. Pause/resume changes, expired sessions and stale fixtures can invalidate readiness even with unchanged code.

Q1 readiness may involve builds or logins that are repeated as independent Q2 acceptance measurements. Declare this distinction; avoid duplication that answers no new question. RRM-004's approved Q2 deferred QF-16 authentication to its actual walk. Report that ordered exception faithfully rather than claiming every auth action happened before the body.

## 10. Browser QA and credentials

The QA Lead specifies observable outcomes and required risk coverage. The Executor owns the mechanical browser work, using existing tests or temporary helpers as appropriate. A scripted exploration is not automatically a permanent regression suite. Retain useful helpers with a reason; promote reusable tests only through a separate engineering change and review.

Test user behavior and resulting state. Prefer accessible roles/names and stable semantic selectors, verify the actual viewport/theme/role, and wait on relevant UI/network conditions. A screenshot is supporting visual evidence; it cannot by itself prove response freshness, session invalidation or correct authorization. Negative controls must demonstrate that the instrument could detect the failure it claims to exclude.

Coverage is a risk-based matrix, not an automatic multiplication of every role, tab, viewport and theme. The plan declares required cells and justifies omitted combinations. The agent performs repetitive regression; the Director may judge new designs, usability or a consequential full transaction. Put human judgment at the end where dependencies allow, while declaring early access needs honestly.

### Credential lifecycle adopted for the pilot

- Director creates a dedicated local QA credential file with the exact keys declared by the pack. Its filename is not itself protection: verify Git ignores it and it has never been tracked.
- Keep QA identities separate from personal accounts. Use the minimum roles required; do not invent or create users as an unapproved workaround.
- Load secrets into the authorized local browser/scanner helper process. No values in chat, command arguments, shell output, screenshots, artifacts or client bundles. Do not give credential variables a public frontend prefix.
- Confirm the resolved application target matches authorization. Do not rewrite app environment files silently or switch to a replica because a template says so.
- For tool runtimes requiring a browser-auth handoff, follow that mechanism. The file-based method is not permission to bypass tool authentication policy, MFA or captcha.
- A login may write session/audit state. “Frontend testing” does not imply zero backend side effects. Business-data writes, emails, payment events and destructive changes need their own explicit authorization.
- During cleanup, scan values and declared encodings while the credential source exists; then remove the credential file and identified auth state; then scan retained output for patterns. Do not retain credentials merely to simplify later exports.
- Director rotates passwords after the pilot as specified, and immediately upon an actual leak. Record attestation and date; never record old/new values.

If testing stops before completion, use the authorized pause cleanup policy to revoke/delete transient auth state. Later resumption may require fresh credentials. A halted experiment does not justify leaving private sessions indefinitely on disk.

## 11. Instruments, evidence and grading

An AC matrix row contains: AC ID, literal requirement/ruling pointer, expected outcome, actual observation, status, candidate/environment identity, evidence path and any qualification. A row without evidence is NOT RUN or BLOCKED, not PASS because the Engineer reported green.

Use independent references when possible: fixture-derived numbers, known encoded image signatures, baseline byte comparisons, isolated test identities or documented API behavior. Validate numeric/version boundaries and known bad cases. A failed instrumentation command invalidates that measurement until repaired and rerun; it is not proof of a product defect.

QA helpers may be corrected within their authorized lane. Record the failed attempt, cause, correction and affected measurements. A correction that changes the meaning of an AC or the coverage strategy goes to the QA Lead. Never change a selector or assertion merely to accept an unexpected product result.

Durable evidence should be enough to explain and reproduce the verdict without unnecessary bulk. Include safe helper source when it explains how a measurement was obtained. Preserve failed attempts rather than overwriting them. Do not automatically commit dependencies, builds, raw authenticated browser traces, profiles or every generated file.

Reports must distinguish historical engineering records from observed QA execution. A test result certifies only its candidate and environment scope. Registry audit results are dated observations, not promises about future vulnerability disclosures.

## 12. Finding and repair loop

| Finding class | Owner/action | Evidence required before continuation |
|---|---|---|
| Product defect | QA Lead adjudicates; Architect rules scope; Engineer repairs | Reproduction, mechanism, affected ACs, allowed files and regression plan |
| Contract gap | Architect/Director ruling; exact erratum recorded | Original text preserved, narrow correction and approval provenance |
| Environment blocker | Responsible environment owner/Director resolves | Actual readiness measurement against authorized target |
| Instrument issue | Executor fixes within bounds; QA Lead reviews material changes | Failed control, correction and repeat of affected measurement |
| Informational/inherited | QA Lead classifies; record owner/gate if deferred | Why outside current defect scope; no blanket inherited exemption |

A repair proposal is not authority to repair. It names the failed requirement, reproduction, evidence, suspected mechanism, suggested allowed-file list and retest coverage. The Architect/Director-approved repair package supplies the actual scope.

Use the same QA branch for the forward certification line when the governing project follows J-11. Pause Executor writes while Engineering repairs; Director commits; Executor re-pins and compares the repair. Retest the repair diff, affected criteria and the required full regression board. Carry unchanged evidence only when its identity, environment and dependency assumptions remain valid. Preserve all attempts and record why evidence was reused.

**Lab gap:** RRM-004 did not exercise this loop. Validate it with an intentionally defective internal fixture before claiming QAM handles repair end to end.

## 13. Review packages as a required output

Every checkpoint needing another seat ends with one indexed review package under QAM/HANDOFFS/. No extra Director request should be necessary to discover which files to upload.

| Checkpoint | Package contents | Decision requested |
|---|---|---|
| Q1 | Recon/stop report, preflight, draft plan, current contract/rulings, manifest, governing bodies and instrument controls | Resolve blockers and approve/amend plan |
| Q2 | Execution report, matrix, approved plan, findings, measurements, safe visual evidence, identity and inventory | Adjudicate; repair or progress to cleanup |
| Q4 | Repair scope/diff and new candidate, linked earlier finding, affected AC/regression results | Confirm repair or return a bounded finding |
| Q5 | Cleanup, privacy/removal proof, retained inventory, final matrix, execution/pilot records, earlier-package references | Certify and issue separate pilot verdict |
| Closeout | Exact QA Lead certificate, pilot verdict, Architect instructions, pending items, identity and record destinations | Execute documentation closeout, then Director Git |

`REVIEW_START_HERE.md` gives module/phase/attempt, code candidate, QA HEAD, tree state, environment label, time, outcomes, missing evidence, reading order and the exact owner decision requested. `FILE_INDEX.json` records each included file's relative path, original path, purpose, bytes and SHA-256. The index excludes its own hash; a receipt outside the ZIP records the final ZIP hash and integrity result.

An incremental package may reference a previously reviewed immutable package by hash when the receiving QA Lead has it. A new reviewer needs the full dependency set, supplied as sibling archives if appropriate. Do not create recursive archives or an unbounded chain of inaccessible references. Record completeness explicitly.

Export uses an explicit allowlist and privacy checks covering selected contents. No shell glob should casually zip the whole repository. Reject absolute/traversal archive paths and unexpected symlinks, verify inventory and archive integrity, and report an exact path. ZIP assembly never reruns QA or changes the verdict.

After credential deletion, preserve the provenance of the pre-deletion value scan and use pattern scanning for newly generated safe metadata. Do not claim a fresh credential-value scan on a final ZIP if it did not occur. RRM-004 recorded this limitation correctly.

## 14. State, staleness and checkpoints

The proposed QAM_STATE.json is a routing aid, not a new approval authority. It references the canonical plan approval, rulings and certificate. A field saying APPROVED without a resolvable owner record is invalid.

Record separately: product candidate, execution QA HEAD, evidence commit, certificate date/author, closeout commit and merge SHA. Also distinguish execution completion from review acceptance, credential deletion from password rotation, product PASS from pilot adoption and prepared closeout from merged integration.

Each phase updates only fields it owns. At closeout, reconcile all completed checkpoint rows against evidence, including earlier phases. Do not force the Engineer to infer authority from a green summary or leave known completed steps pending because the template forgot to allow bookkeeping. Scope the reconciliation explicitly in the closeout prompt.

Approval is tied to a candidate/plan/ruling set. Resume checks whether any of those changed and whether the environment still matches. Rerun only what is invalidated or explicitly required. If the state and evidence disagree, report the contradiction; do not erase history or restart blindly.

## 15. Cleanup, certification and closeout

The QA Lead defines the smallest durable certification package. The Executor lists each retained helper/artifact with purpose and each disposable item with deletion scope. Cleanup never means deleting protected files, unknown profiles, unrelated processes or an entire evidence tree.

Credential value scans precede deletion; recorded auth state is removed or verified absent; editor recovery files follow the approved name-only handling rule; post-deletion patterns are checked; QA server ownership is identified precisely. Preserve corrections to discovery scripts as evidence. Verify no product/config/test changes occurred.

A certificate includes the full tested identity, governing versions, outcome totals, accepted findings/rulings, evidence package hashes, coverage qualifications, cleanup outcome and remaining external actions. The QA Lead is the author even when the Engineer transcribes exact text into the repository.

The closeout package must carry that exact text or a verified accessible file, never merely say “the letter was supplied.” Include an explicit permission to reconcile checkpoint records, record Director attestations as attestations, and preserve two-seat journal authorship.

Director-owned actions remain with Tony: password rotation confirmation, adopt/amend/drop, commit, merge and push. No agent marks those complete without evidence. No closeout report should imply a finished merge when only its documentation is prepared.

## 16. Metrics and honest success criteria

Measure the complete lifecycle alongside uninterrupted Q2 execution. Record start/end/offset, source and whether each duration is measured elapsed time, attention time, estimate or unknown.

| Metric | Why it matters |
|---|---|
| Authoring/preparation time | Makes setup cost visible |
| Q1 body, return and approval interval | Separates execution from coordination delay |
| Q2 body and full release elapsed | Prevents reporting only the attractive inner loop |
| Q4 rounds and Q5 elapsed | Shows repair/cleanup cost |
| Director checkpoint touches vs in-run interventions | Keeps planned supervision distinct from interruption |
| Manual credential entries and browser matrix cells | Measures the work removed from the Director |
| Product, contract, environment and instrument findings | Shows where prevention effort belongs |
| First-package sufficiency and follow-up exports | Measures handoff quality |
| Helper corrections and promoted tests | Separates adaptive execution from production repair |
| Cleanup/privacy outcomes and retained bytes | Prevents speed gains from hiding unsafe retention |
| Final closeout/status corrections | Reveals the last-mile coordination debt |

For the existing RRM-004 charter retain PARTIAL SUCCESS. A future charter may separately grade preparation, Q2 autonomy, repair handling, cleanup and transport so a correctly handled recon stop is easy to interpret. Any new rubric is approved before the run; do not retrospectively redefine success to improve the pilot's score.

## 17. Carrying the pattern beyond RRMs

| Module | Reusable core | Additional preparation |
|---|---|---|
| RRM | Bounded scope, existing regression, preserved-path proof | Map review findings to dispositions and avoid unrelated repair |
| FFM | Browser execution, visual evidence and role coverage | Responsive/accessibility checks, realistic states and bounded human visual judgment |
| BIM | Recon, independent plan, contract evidence and repair cycle | Schema/migration identity, fixtures, authorization/RLS, idempotency, failure recovery and explicit data-write permission |
| ABM | One application assignment with one QAM package | Cross-feature journeys, integration boundaries, install/restart and full-app evidence map |
| APBM | One phase assignment with a QAM tied to its candidate | Prior phase contracts, integration regression, phase dependencies and accumulated evidence provenance |

One-shot execution does not imply one giant terminal command or simultaneous uncontrolled agents. Larger work may need bounded internal stages or a planned checkpoint. The Director-facing workflow can remain simple while the package carries that complexity.

Use internal apps such as Stark AI Workbench, Web Factory or Web Recon Scraper for wider experiments. For client work, retain the current proven five-seat process and adopt small improvements only through explicit project approval. Successful QAM on one dependency module is not authorization for unattended production migrations, live commerce writes or overnight deployments.

Unattended Lab runs need an authorized environment, bounded side effects, resource/time limits, a durable stop report, resumable state and a clear morning handoff. On external access controls or unavailable identities, stop; do not bypass safeguards to preserve autonomy.

## 18. Lab implementation backlog and promotion gate

| Priority | Deliverable | Owner | Proof needed |
|---|---|---|---|
| P0 | Complete template with both entry files and shared routing | Architect + QA Lead | Fresh sessions in both supported tools identify role/phase correctly |
| P0 | Package completeness checker | Lab Engineer | Missing spec, bad pointer, unresolved SHA and unapproved plan are detected |
| P0 | Checkpoint exporter | Lab Engineer + QA Executor | Q1/Q2/Q4/Q5/closeout return one reviewable package without Director file hunting |
| P0 | Evidence-linked state and checkpoint reconciliation | Lab Engineer | Resume after interruption; stale status caught without rerunning completed work |
| P0 | Credential lifecycle and safe browser adapter | QA Lead + Lab Engineer | Success, missing credentials and planted-secret cases; no actual secrets exported |
| P1 | Product repair/retest exercise | Architect + Engineer + QA seats | Bounded defect, ruled repair, new SHA, affected/full required regression and independent verdict |
| P1 | Runtime/provider substitution | Director + QA Lead | Handoff to a different supported tool preserves approvals and role boundaries |
| P1 | BIM integration pilot | Architect + QA Lead | Authorized data model/fixture/permission and rollback tests in a disposable internal environment |
| P2 | ABM/APBM pilots | Master Jarvis | Phase/app evidence complete with bounded Director involvement |

Recommended promotion review: repeat on at least two different internal module profiles, including one with a real repair round; demonstrate package/entry/cleanup failure cases; compare total Director effort rather than only Q2 time; obtain explicit Director decision before changing production doctrine. This threshold is proposed, not an existing factory rule.

## 19. Template acceptance tests for the Lab

The supplied templates are starting material, not an implemented validator. Test these scenarios before calling the packaging system complete:

1. Folder-only first launch in each supported tool identifies the QA role and stops after recon.
2. Wrong role/folder/branch explains the mismatch and performs no unauthorized action.
3. Missing governing body or broken relative pointer produces a specific blocker.
4. A committed candidate with a documentation successor is classified correctly; an altered lockfile invalidates product identity.
5. An unapproved or modified plan cannot start Q2.
6. Unavailable target, wrong target, missing role, expired credential or unexpected MFA returns a bounded access blocker.
7. A planted secret is detected, a clean control passes, and no secret appears in the report.
8. A helper defect is corrected with failed evidence preserved; a product defect is routed rather than repaired by QA.
9. Q1/Q2/Q4/Q5 exports are self-contained for their intended recipient and land in QAM/HANDOFFS/.
10. A missing certification letter prevents transcription before closeout begins.
11. Cleanup retains cited evidence, removes only authorized sensitive/transient items and preserves product identity.
12. Provider outage/resume preserves completed work and pending approvals.
13. Password rotation attestation and completed checkpoints reconcile without falsifying independent observation.
14. Product PASS, pilot result, deployment status and merge status remain distinct.

## 20. What the next Architect should do

Read the evidence dossier and preserved seat journals. Resolve the few genuine design decisions before creating an internal pilot pack. Use the template folder as a concrete starting point, author all module-specific fields and prepare the pre-build QA requirements. Build only the minimal mechanisms needed for folder entry, validation, export and resume. Keep client work unchanged while this Lab iteration runs.

The next win to seek is reproducibility: a second operator or a fresh agent should be able to follow the package without Tony re-explaining the factory. The result should still have five accountable seats, literal acceptance, independent evidence and a clear Director decision at the end.
