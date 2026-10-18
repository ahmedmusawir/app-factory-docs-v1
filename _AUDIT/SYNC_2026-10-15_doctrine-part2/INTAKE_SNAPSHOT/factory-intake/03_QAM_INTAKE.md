# QA Modules — Consolidated Intake Brief

Version: 0.1 · Date: 2026-10-13, Asia/Dhaka · Author: JARVIS, intake Architect

**Status: PROPOSED ADOPTION. Latest supplied synthesis remains an experimental draft; this document does not promote it into production doctrine.**

Common authority and decisions: [00_MASTER_INDEX.md](00_MASTER_INDEX.md). Source identities: [SOURCE_REGISTER.md](SOURCE_REGISTER.md). RRM contract interface: [02_RRM_INTAKE.md](02_RRM_INTAKE.md).

## 1. Purpose and source hierarchy

QAM is a prepared QA subpackage attached to a bounded engineering assignment and candidate. Its purpose is to remove repeated startup prompts, environment surprises, manual regression matrices and file hunting while preserving independent judgment and declared approvals.

SRC-Q05 is Tony's original two-scenario brain-dump. SRC-Q01 proposes the skeleton/facts/plan split. SRC-Q04 is the older 29 September pilot plan. SRC-Q02 records subsequent Architect-side rulings and outcomes. SRC-R04 records QA-side Director requirements and Q1 observations. SRC-Q03, the 2 October QA Lead master draft, is the most complete supplied synthesis. It incorporates later rules but explicitly remains experimental. Read it alongside the journals; newer date alone is not an authority rule.

The preferred preparation pattern in the later synthesis is: QA Lead maintains standing QA doctrine; Architect includes its skeleton in the module pack; Engineer fills factual handoff fields; QA Executor performs Q1 and drafts the independent plan; QA Lead approves before Q2. This resolves the original “who drops the folder?” question without making Engineering author the independent test plan.

## 2. Supersession and unresolved-scope register

| Topic | Earlier material | Later supplied record | Intake treatment |
|---|---|---|---|
| Folder name | Keep `QA/` for RRM-004 | QA Lead ruling adopted `QAM/` during the pilot via recorded overlay | New QAM proposal uses `QAM/`; preserve old pack paths as history |
| Plan authoring | QA Lead alone, possibly in parallel with build | Executor drafts at Q1; Lead amends/approves | Proposed common split; do not allow Engineer to grade itself |
| Entry filenames | CLAUDE-only proposal, then AGENTS-only ruling | 1 October Director requirement: both files, same role/common instructions | Carry dual-entry requirement with source attribution |
| Handoff transport | Director asks for individual reports | Indexed review package automatically at checkpoints | Preserve `QAM/HANDOFFS/` as later recorded destination |
| Authentication | Director browser entry in old pilot | Authorized temporary QA credential file in revised pilot | Keep as supported adapter with target/tool-policy boundaries, not universal requirement |
| Certification/cleanup | Gate Q then cleanup | Approved RRM-004 Q5 credential cleanup before final certification | Propose explicit sequence; preserve historical ordering in original sources |
| Success | Initial intended continuous run | Product PASS; pilot PARTIAL SUCCESS due to Q1 scope stop | Never rewrite the historical score |
| Applicability | Pilot class lists include RRM/BIM/FFM/ABM/APBM | Master draft calls for validation and explicit wider adoption | ND-01 remains open; ABM/APBM-specific adoption stays 10X |

## 3. Proposal ledger

### QAM-01 — Definition and adoption boundary

**Sources:** SRC-Q03 §§1–3/17–20; SRC-Q04 §2. **Status:** proposed adoption ND-01.

QAM packages QA readiness, independent planning, execution, evidence, repair routing, cleanup and review transport. It does not replace the product acceptance contract, invent release authority, or turn every module into an unattended task.

RRM-004 was a specifically approved Cyber Pharma experiment. A report of its success is not blanket authorization for future client migrations, commerce writes or deployments. Propose the reusable playbook now and make its scope/adoption status explicit. Carry experimental state/export/runtime mechanisms as proposals until implemented and evidenced.

**Verify:** the adopted document states who may use which parts, what remains experimental and which governing project contract wins at a live run.

### QAM-02 — Authorship and five seats

**Sources:** SRC-Q03 §§4–5; SRC-Q01 §0/1; SRC-R03 authorship opinion. **Correction interface:** FC-006/025, DEC-07/13.

| Seat | Owns | Must not do under that seat |
|---|---|---|
| Architect | Approved scope, pre-build acceptance, module/QAM skeleton, scope rulings, closeout instructions | Pre-issue independent QA results |
| Engineer | Product implementation, self-tests, factual handoff and manifest | Approve QA plan, grade independent results or certify |
| QA Lead | Standing risks, plan approval, finding classification, retention judgment, certification | Quietly redefine product scope or claim unrun tests |
| QA Executor | Q1 recon, plan draft, independent checks, evidence, review packages and authorized cleanup | Repair product, self-certify or mutate Git without applicable authorization |
| Director | Scope/access decisions, approvals, Git, release and meaningful human judgment | No requirement to perform repetitive agent-capable matrices |

QA may reuse useful engineering tests while deriving independent expectations, inspecting instruments and challenging failure cases. Independence does not require redundant copies of every test. Tool/provider replacement preserves role, approval state and candidate identity. The same worktree has one active writer during repair and measurement.

### QAM-03 — Package readiness and ownership

**Source:** SRC-Q03 §§5–6; SRC-R03 report §4. **Status:** proposed template contract under ND-05.

Architect ships the QAM skeleton with the original engineering pack. Engineer completes factual readiness in the build assignment. The folder becomes ready for recon, not automatically approved for execution. Link to the enclosing frozen acceptance contract instead of creating a second authoritative copy.

Proposed common files: matching CLAUDE.md/AGENTS.md, QAM_ENTRY.md, QAM_MANIFEST.md, QAM_RISK_REQUIREMENTS.md, QAM_PREFLIGHT.md, QAM_TEST_PLAN.md, QAM_PROMPTS.md, QAM_CHECKPOINTS.md; evidence matrix, execution report, cleanup report, artifact inventory and certification record; GOVERNING/, AUTOMATION/, evidence/ and HANDOFFS/ lanes. REPAIR_PROPOSAL.md appears when needed. Pilot charter/results are required for experiments, not gratuitous paperwork on every routine run. QAM_STATE.json is a proposed routing aid, not a delivered runtime or new authority.

Actual generic templates were not included with SRC-Q03 (GAP-03). If authoring them here is approved, label them newly authored and validate pointers/ownership; do not claim byte identity with missing templates.

**Verify:** no fabricated PASS, pre-issued certificate, real credentials or historical fixed candidate in a blank kit; required missing fields are explicit.

### QAM-04 — Folder-only startup and safe resume

**Sources:** SRC-R04 Observation 004; SRC-Q03 §§6–7/14. **Status:** source-reported Director requirement plus proposed implementation.

Both CLAUDE.md and AGENTS.md at each independently launched module entry provide the same role and route to a common instruction body. At the engineering root they assign engineering; under QAM they assign QA Executor. Filename or model name does not change authority.

Entry explains module, repository root, current phase, completed work, candidate, governing versions, approval pointers, permitted paths, next action and output location. A fresh session reads durable records rather than pretending to remember its predecessor. Wrong folder/branch/phase produces useful guidance without automatic switching, resetting or restarting.

Test actual discovery in supported tools. If a runtime needs bootstrap instructions, package them explicitly. A folder pointer starts the permitted recon/resume step; it does not approve all later phases, repair, certification or Git.

**Verify:** first launch, resume, completed module, wrong folder and provider substitution preserve the same role and pending approvals.

### QAM-05 — Explicit checkpoint sequence

**Sources:** SRC-Q03 §8/15; later SRC-Q02/R04 rulings. **Status:** proposed adopted sequence under ND-04.

| Stage | Work | Exit/approval |
|---|---|---|
| Engineering handoff | Facts, diff, reproduction, limitations, manifest | Director commits candidate; QA resolves full identity |
| Q1 | Readiness, independent recon, scope contradictions, draft plan | One review package; QA Lead review |
| Q1b | Record approved plan and any authorized errata | Bind approval to candidate, plan and ruling set; Director releases Q2 |
| Q2 | Continuous approved verification and evidence collection | One package; Lead adjudication |
| Repair/Q4 if needed | Ruled Engineer repair, commit, re-pin, targeted and required regression checks | Lead re-adjudication |
| Q5 | Authorized retention/credential cleanup, identity proof, final package | Lead accepts cleanup/evidence |
| Certification/closeout | Exact Lead certificate, separate pilot result, Architect instructions, Engineer bookkeeping | Director integration/release actions |

No repeated “may I continue?” between already authorized passing checks. No skipped check to preserve one-shot claims. Q5 does not rerun the product board without a concrete reason. Existing approved live modules retain their own sequence until amended through the proper lane.

### QAM-06 — Preflight and concrete stops

**Sources:** SRC-Q03 §9; SRC-R03 report §5; SRC-Q04 stages F/G. **Correction interface:** FC-014/022/030, DEC-14.

Check identity/ancestry, authority pointers, runtime/browser, required network access, authorized target, test roles, trustworthy instruments, writable evidence lanes and permitted side effects. Use bounded probes that answer actual readiness questions. Eighteen historical rows are not a universal minimum.

Q1 may need explicitly authorized builds or login probes; describe these as diagnostics with effects, not magically write-free recon. Revalidate changed/time-sensitive prerequisites at Q2/resume. A failing environment produces a classified blocker with evidence, owner and smallest next action. Do not endlessly retry unavailable credentials or services.

Stop when candidate/approval identity, scope, access, evidence integrity or permitted operations no longer hold. Ordinary instrument correction may continue within its assigned lane and budget. New material uncertainty cannot be ignored merely because a numbered list omitted it.

### QAM-07 — Credential and browser lifecycle

**Sources:** SRC-Q05 Part 1; SRC-Q03 §10; SRC-Q02 later rulings. **Status:** reusable protocol proposal from a scoped pilot, not authorization for a new environment.

Director chooses the environment and supplies authorized dedicated identities. A temporary ignored QA credential file is one adapter; the pilot's exact five keys and ADMIN/MEMBER roles are project examples. Check ignored/untracked state, required key names, target match and authorized authentication without printing values. Respect the actual tool's credential-handling and browser-auth policy; do not bypass MFA or CAPTCHA.

Login can write session/audit state. Business-data writes, emails, payments, role changes and destructive operations need explicit scope. Keep credentials, cookies, tokens, browser storage and raw authenticated traces out of export/evidence. Load required secret values only inside the authorized process.

Under the proposed QAM cleanup sequence: run the applicable value/encoding scan while the credential source is available; remove authorized credential/auth state with evidence; rescan retained output for patterns. On a stopped run, apply the approved pause policy rather than retaining sessions indefinitely. Record Director rotation attestations separately from file deletion. Do not claim a new value scan after deleting the only value source.

### QAM-08 — Independent instruments and literal grading

**Source:** SRC-Q03 §11; SRC-R01 §7; SRC-Q04 §§6/12. **Correction interface:** CF-05, FC-024.

Each AC row links requirement/ruling, expected outcome, observed outcome, candidate/environment, evidence and qualification. Unrun/blocked evidence is not PASS because engineering reported green. Use independent reference derivations and relevant positive/negative/boundary controls. Retain failed instrument attempts and the correction history.

QA helpers may change within authorized lanes to repair measurement. Changes that alter coverage or acceptance meaning need Lead review. Do not change assertions merely to accept unexpected behavior. Direct function probes, synthetic fixtures, runtime HTTP checks, browser interaction and deployed checks support different claims; name the level actually exercised.

Human visual/product judgment remains where the approved plan needs it; repetitive browser matrices can be automated. Permanent regression tests should be selected for durable value rather than converting every exploratory click into a maintained test.

### QAM-09 — Finding classification and repair

**Source:** SRC-Q03 §12; SRC-Q01 §5; SRC-R01 §8.

Classify product defect, contract gap, environment blocker, instrument problem or observation before selecting the owner. Executor proposes; Lead adjudicates; Architect/Director scope product repair; Engineer edits; Director commits; Executor re-pins and measures. A helper fix is not a product repair round.

Retest affected ACs, the actual repair diff and regression required by the approved plan. Reuse unaffected evidence with explicit identity/environment reasoning. Preserve attempts. In a shared worktree, pause QA writes while engineering repairs. RRM-004's clean product run does not prove the Q4 path; later evidence may close this gap, otherwise state it as unvalidated.

### QAM-10 — Durable evidence and certification

**Sources:** SRC-Q03 §§11/15; SRC-R04; SRC-Q02 final entry. **Correction interface:** DEC-13.

Lead selects the smallest durable package that can explain/reproduce the verdict. Preserve issued decisions, necessary helper source, meaningful failed attempts, matrix and provenance. Remove only identified temporary or sensitive items; never blanket-delete a cited evidence tree or unknown process/profile. Prove product/config/test/contract identity is unchanged by cleanup.

Certification names full tested identity, authority versions, results, accepted rulings, package references/hashes, qualifications, cleanup outcome and remaining external actions. Engineer may transcribe the exact Lead text with attribution; a summary or a promise that “the letter was supplied” is insufficient.

### QAM-11 — Automatic checkpoint review packages

**Sources:** SRC-R04 Observations 005–006; SRC-Q03 §13. **Status:** source-reported Director requirement proposed for template propagation.

Each Q1/Q2/Q4/Q5 or material stop needing review produces one indexed package in `QAM/HANDOFFS/` as part of the assignment. Include REVIEW_START_HERE with module, phase/attempt, full candidate and QA HEAD, tree state, time, authorized target label, outcomes, missing material, read order and exact decision requested. Include current authority needed by the recipient, with engineering claims and QA evidence labeled.

Use an explicit file allowlist, preserve relative/original paths, record bytes and SHA-256, exclude the index from its own hash and record final ZIP hash separately. Verify archive paths/integrity and declared scan coverage. Avoid recursive handoffs and secrets/dependency/build/Git directories. Incremental references are acceptable only if the recipient actually has the referenced immutable package; a new reviewer needs the dependency set.

Shared-repository access can use an index in place instead of an unnecessary ZIP. Transport never grants approval. Export does not rerun QA, change a verdict or authorize the next phase.

### QAM-12 — Honest metrics and separate verdicts

**Sources:** SRC-Q03 §16; SRC-Q02 final entry; SRC-R03 campaign report. **Status:** proposed measurement standard.

Record preparation, Q1, review delay, Q2 body and release elapsed, repairs/Q4, cleanup/Q5, Director attention, planned vs unplanned touches, credential entries, instrument corrections and missing-package follow-ups. Mark unknowns and estimates. Measure total effort alongside attractive inner-loop timings.

RRM-004's reported product result is Gate Q PASS, 31 criteria and zero product repairs. Its process verdict remains PARTIAL SUCCESS; Q1 required A-15 scope reconciliation, while Q2 reported zero Director interventions. New experiments may use a clearer component rubric if approved before execution; never rescore the past to improve appearances.

### QAM-13 — Integration with current DocSet and tooling boundaries

**Sources:** SRC-Q03 §§6/18–20; existing correction package. **Status:** new owning playbook/kit proposal ND-05.

Propose one QAM_PLAYBOOK linked from QA_PLAYBOOK, Handoff, Architect, Engineer and applicable module playbooks. Existing QA doctrine remains the owner of Factory-wide independence, verdicts and Gate Q/Gate D unless an approved map explicitly reallocates ownership. Carry governing bodies locally with version/source provenance so the Executor can read what it must obey.

Keep templates aligned with the adopted playbook and module contracts. A generic validator, exporter, state dispatcher, browser adapter or skill implementation is a separately scoped tool deliverable; describing it in a draft is not proof it exists. Do not expand this sync into that engineering project by implication.

### QAM-14 — Portability, validation and promotion

**Source:** SRC-Q03 §§17–20; SRC-Q04 §2. **Status:** proposed promotion policy ND-01.

Reusable core can support RRM, FFM and BIM with different environment/side-effect needs. ABM/APBM adaptations stay on the 10X track. Cyber Pharma examples remain attributed pilot evidence. No module inherits main-dev targeting, login-only permissions or specific browser/runtime behavior from an example.

Proposed template checks include wrong folder/branch, missing authority, unapproved/stale plan, altered lockfile, unavailable target, planted-secret/clean controls, helper vs product defect routing, complete checkpoint exports, missing certificate, bounded cleanup and provider-resume continuity. The master's “two different internal profiles including repair” promotion threshold is a proposal, not an existing mandatory rule or a new blocker imposed here. Bring later validation evidence if available; otherwise distinguish adopted principles from unvalidated mechanisms.

## 4. Acceptance expectations for the eventual update

The approved map should leave a new agent able to identify its role, current phase, candidate, governing instructions and next permitted action from the package. QA handoff facts, independent plan, evidence and certification must have separate owners. Every checkpoint has a concrete return artifact. Stale plans and product identity changes are detected without restarting unrelated work. Cleanup and final certification ordering is unambiguous. Original pilot records remain unchanged and every broader adoption statement has explicit approval provenance.

This brief is ready for intake analysis. It is not a fresh QAM execution, a completed toolkit, a certification of the supplied archives or a Factory-wide adoption decision.
