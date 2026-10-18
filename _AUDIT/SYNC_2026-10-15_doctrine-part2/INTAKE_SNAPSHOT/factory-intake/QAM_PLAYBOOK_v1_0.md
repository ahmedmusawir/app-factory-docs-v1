# QAM PLAYBOOK v1.0
## Mandatory module packaging and two-shot independent QA

**Date:** 2026-10-14 · **Authoring seat:** QA Lead / JARVIS · **Director:** Tony Stark  
**Audience:** Factory Doc Sync Architect, module-writing Architects, Engineers and QA Executors.  
**Status:** QA Lead-authored v1.0 for Factory synchronization under the Director's current instruction. This document does not claim that other Factory documents or repositories have already been updated.

## 1. The rule every Architect must understand

**Every new Factory module MUST contain a complete, module-specific `QAM/` from initial authoring.** This applies to RRM, FFM, BIM, TRM, FIX, FEAT, ABM, APBM and future module types. The module's scope changes the tests; it does not remove QAM.

**Every ordinary QA engagement has TWO planned execution shots:**

1. **Q1 — independent recon and test planning.** The QA Executor checks readiness, reads the contract, challenges the Engineer's claims and writes the proposed test plan. It returns one indexed review package and stops for the QA Lead.
2. **Q2 — independent QA execution.** After the QA Lead approves that specific plan and the Director releases the candidate, the QA Executor executes the approved work continuously and returns one indexed result package.

**Repair and retest are conditional, after findings.** They are not mandatory extra shots. QA Lead adjudication, cleanup, certification, Architect closeout and Director Git actions still exist. Two-shot QA does not mean two messages from module creation through merge, and it never means ignoring a genuine stop condition.

The practical Director experience is: place one complete module pack, let Engineering finish its handoff, establish the QA branch, point the QA Executor to QAM, upload its Q1 ZIP, relay the QA Lead's approval, release Q2, and upload its result ZIP. The Director should not assemble QA documents, compose a new test campaign prompt, or perform repetitive browser matrices.

## 2. What QAM is

QAM is the module's self-contained QA assignment, operating instructions, readiness checks, planning workspace and evidence record. It is a real folder inside the parent module, not merely a renamed empty QA folder or a reference to another chat.

The folder contains enough information for a fresh authorized agent to identify its role, determine the current phase, locate the governing contract, explain missing prerequisites and do the next permitted work. Module-relative links to the parent's canonical acceptance spec are acceptable; duplicate acceptance contracts are not required. External governing bodies must be available through a versioned local snapshot with provenance or an explicitly approved accessible source.

The Architect ships a prepared skeleton. The Engineer supplies factual completion inputs. The QA Executor independently drafts and executes tests. The QA Lead owns approval, adjudication and certification. A folder does not transport itself between applications: indexed ZIP export remains the predictable handoff when the QA Lead is in a separate chat.

## 3. Authority and the five seats

| Seat | Responsibility | Boundary |
|---|---|---|
| Director | Approves scope/targets and risk decisions; controls credentials, Git, release and destructive authority | Does not have to perform every repeatable UI check |
| Architect | Defines frozen acceptance contract, module scope and protections; instantiates QAM from this playbook; resolves contract ambiguity; directs closeout | Does not substitute an engineering-green result for independent QA |
| Engineer | Implements approved scope, self-verifies, completes manifest and engineering handoff; repairs only ruled scope | Does not approve the QA plan, fill independent QA results or issue a certificate |
| QA Lead | Owns this playbook and standing risks; amends/approves Q1 plan; adjudicates findings; approves cleanup/retention and certifies | Does not invent missing evidence or silently repair the product |
| QA Executor | Performs Q1, drafts plan, executes approved Q2, records findings, executes approved retests and cleanup, exports packages | Does not self-approve, self-certify, mutate Git or make unauthorized product changes |

Names and models are interchangeable; authority follows the seat. The agent that engineered a candidate must not independently certify its own work. When one runtime changes seats, record the handoff and preserve an independent verification assignment and QA Lead review.

The Architect owns or validates acceptance criteria before implementation. The Engineer may propose clarifications during planning; approval and frozen-contract rules still apply. The Engineer's handoff reports what was built, not what the acceptance criteria ought to become after building it.

## 4. How this fits existing doctrine

The supplied QA Playbook v1.1 remains the source for evidence discipline, finding severity, gate verdicts and independence. The supplied Doctrine Journal v0.3 contributes QA-branch ownership, bounded repair/retest, errata, evidence retention and cleanup rules. This QAM playbook specifies packaging and execution around those responsibilities.

The latest Director instruction makes QAM mandatory for future module authoring. Earlier pilot-only or optional-QAM language is historical and must be reconciled by the Factory Doc Sync Architect. Preserve the original RRM-004 records and their dates; do not rewrite the pilot as if v1.0 existed then.

Conflicts affecting scope, permissions or grading must be surfaced with the two sources and owner. A folder-level instruction cannot erase higher-priority tool restrictions or repository authority. Documentation synchronization must settle a real conflict rather than tell an agent to ignore it.

Frozen AC text remains unchanged. Record approved corrections in the append-only ruling/erratum lane with original observation, exact corrected interpretation, approving authority, date and affected ACs. Plan amendments alone cannot modify a contract.

## 5. Package structure and ownership

Instantiate `TEMPLATES/QAM/` inside each module directory. The template's unfilled fields are authoring prompts, not a launch-ready pack. Resolve paths and module-specific choices before declaring it ready.

| Location | Contents and owner |
|---|---|
| Parent module | Canonical scope, acceptance spec, rulings, implementation instructions and Engineer evidence |
| `QAM/CLAUDE.md` and `QAM/AGENTS.md` | Matching QA entry instructions, generated by Architect |
| `QAM/QAM_ENTRY.md` | Module identity, role routing, read order and phase dispatch |
| `QAM/QAM_STATE.md` | Current workflow state, identities, latest receipts and next owner; references authority, never grants it |
| `QAM/QAM_MANIFEST.md` | Engineer's factual completion record and environment needs |
| `QAM/HANDOFFS/ENGINEERING_HANDOFF.md` | Engineer's claims, commands, evidence, limitations and reproduction |
| `QAM/QAM_PREFLIGHT.md` | Executable readiness checks with expected results and owners |
| `QAM/QAM_RISK_REQUIREMENTS.md` | QA Lead standing requirements, Architect risk input, module-specific risks |
| `QAM/QAM_RECON_REPORT.md` | Executor's independent Q1 observations, contradictions and readiness |
| `QAM/QAM_TEST_PLAN.md` | Executor draft, amended and approved by QA Lead |
| `QAM/QAM_APPROVAL.md` | Exact QA Lead decision, approved plan identity and Director release references |
| `QAM/QAM_EXECUTION_REPORT.md` and `AC_EVIDENCE_MATRIX.md` | Executor measurements and per-AC evidence |
| `QAM/FINDINGS.md` | Findings, classification proposals, Lead dispositions and conditional repair routing |
| `QAM/QAM_CLEANUP_REPORT.md` and `QAM_CERTIFICATION.md` | Cleanup evidence and separately attributed QA Lead verdict |
| `QAM/GOVERNING/` | Applicable bodies and source/version/hash provenance |
| `QAM/AUTOMATION/` and `QAM/evidence/` | Approved helpers, instrument controls, durable measurements and attempt history |
| `QAM/HANDOFFS/` | Indexed checkpoint ZIPs, external receipts and review entry notes |

Future QA handoffs belong under QAM. Do not leave the real handoff scattered between root documents, temporary directories and chat. Repository-required response/session records may remain at their governed paths; the QAM package must include or clearly index the records required for review. Do not add write access to protected session or recovery files merely to satisfy a template.

## 6. Reliable entry through either runtime

Both `QAM/CLAUDE.md` and `QAM/AGENTS.md` must assign the QA Executor seat and refer to the same canonical `QAM_ENTRY.md`. Keep their routing text identical. At the parent module, both entry conventions must route Engineering to the implementation assignment and QA to QAM.

A user pointing an agent to QAM and asking it to start authorizes Q1 within the declared scope. A folder path by itself never authorizes Q2, product repair, certification, Git mutation or deployment. The agent reads persisted state before acting:

- Ready for recon: introduce the QA role briefly and perform Q1.
- Q1 already complete, awaiting review: return the existing package and decision needed; do not rerun automatically.
- Approved but unreleased: identify the missing Director release.
- Released for Q2: verify the approval/candidate binding and run Q2.
- Stopped or interrupted: report the recorded stop and resume only after its resolution.
- Already completed/certified: show the result and next owner; do not restart testing or cleanup.
- Wrong folder/role: explain the correct module-relative entry and ask only when intent remains ambiguous.

The Architect must validate discovery in each supported runtime. Merely creating a file does not prove the runtime loads it. If a runtime does not auto-discover the entry, the documented fallback is one stable instruction to read `QAM_ENTRY.md`; there must be no long custom kickoff prompt containing missing operating rules.

## 7. Architect authoring and Engineer completion

### Before engineering

The Architect includes QAM with the module ZIP. It resolves the actual repo/module identity, acceptance references, baseline, protected paths, intended QA branch, target environment, test data, role requirements, toolchain and permitted effects. It specifies evidence outputs, blocking rules, browser coverage inputs, completion duties and handoff destinations.

QA Lead standing requirements are reusable. The QA Lead need not review every engineering packet before work begins. The independent, candidate-specific plan approval happens after Q1. Specialist risks can be supplied earlier when requested.

### As Engineering finishes

Completing the factual QAM handoff is part of the original engineering assignment, not another trip to the Architect for a handoff-writing prompt. The Engineer records:

- baseline and implementation identity; all changed paths and authorized exceptions;
- claimed behavior, self-verification commands/results and evidence links;
- install/build/serve/reproduction commands and working directory;
- environments, prerequisites, migrations, fixtures, roles and credentials needed, without secret values;
- known limitations, unresolved issues, preserved paths and relevant rollback dependencies;
- the meaning of each engineering evidence item, clearly labeled as a claim for independent QA.

The Engineer does not fill Q1 findings, Q2 results, the QA Lead decision, or a passed certification template.

The final commit SHA does not exist until the Director commits. Before that, use an explicit pending identity, not an invented SHA. After commit, the Q1 entry resolves the candidate from the Director's receipt/read-only Git evidence, checks it against the handoff and records the full SHA. If the manifest needs a factual amendment, the authorized owner records it; the Executor records independent identity in recon. No repeated documentation commit is required just to embed its own SHA in its own bytes.

## 8. Shot 1 — Q1 recon and test plan

Q1 is read-only toward product and live business data, with writes only to the declared QA lane and approved transient setup. It may install/build/serve or perform bounded login/logout probes when the preflight explicitly authorizes them. Q1 is not the full QA campaign.

Execute the complete permitted readiness assessment in one run. Aggregate independent blockers instead of returning after each missing document when safe work remains possible. Stop immediately before a forbidden or unsafe action; do not continue through a compromised instrument or wrong target.

Check:

1. Repository, branch, full baseline/candidate/HEAD, tracked and untracked state, candidate ancestry and complete changed-path inventory.
2. Contract, errata, scope, protected paths, pre-ruled exceptions, governing versions and Engineer handoff completeness.
3. Runtime/tool versions, dependency setup, external build prerequisites, free ports, resources and evidence-lane permissions.
4. Actual resolved target, configuration precedence, service readiness, role/account availability and suitable test data. A target label alone is insufficient.
5. Browser driver and basic interactions, privacy instrumentation and permitted auth probes where relevant.
6. Ability to produce a safe review package and recover after interruption.

Record unresolved details as GAP/QUESTION/BLOCKED, with owner and exact resolution. Distinguish “endpoint reachable” from “service ready for the required operation.” An HTTP response of any status proves connectivity only. Main-dev, scratch and replica are module-specific approvals; never choose one by habit.

Then independently draft the plan from the contract, risk requirements, source, recon and Engineer claims. Every AC gets a test or a separately authorized applicability ruling. Specify expected results, independently derived references, negative controls, evidence, regression scope, ordering and dependencies. Identify what cannot yet be tested.

Return one Q1 ZIP under `QAM/HANDOFFS/`, including the recon response, draft plan, identity evidence, contradictions, governing references and relevant supporting records. Stop for QA Lead review. A successful login during recon does not automatically satisfy the later acceptance walk.

## 9. Approval between the shots

The QA Lead reviews the actual Q1 package, not just the Executor's summary. The Lead may approve, approve exact amendments, or hold with specific blockers. This is the module-specific steering point: risk order, negative tests, references, browser matrix and regression coverage become final here.

Record approval in `QAM_APPROVAL.md` with full product candidate, plan SHA-256, contract/ruling identity, environment identity, limitations, exact amendments, approval source/date and required release conditions. Use a separate approval file to avoid a self-referential plan hash.

**Q1b is amendment bookkeeping within this approval checkpoint, not a mandatory third QA shot.** If no amendments are needed, record that and proceed to release. If the Lead supplies exact edits, the Executor applies only those edits and binds the finalized plan; a delegated exact-edit approval must identify the authorized changes and preserve the diff. Material new tests, interpretation changes or unresolved contradictions return to the Lead. Contract errata follow their separate Architect/Director authority.

The Director commits the required records and releases Q2 using the established Git policy. A documentation-only successor must be proved from the complete diff, not assumed from its commit message. New product/config/test changes invalidate the earlier candidate binding and require Lead review of the changed scope. Do not confuse tested product SHA, QA execution HEAD and evidence/closeout commit.

## 10. Shot 2 — Q2 continuous QA

At entry, verify the approved plan, current full HEAD, product identity, target and release. Recheck readiness items that could have changed. Reuse still-valid Q1 instrument evidence with provenance; repeat setup when reproducibility, changed inputs or the plan requires it. The RRM-004 fresh-install-per-phase rule was module-specific, not an automatic requirement to reinstall everything for every future module.

Execute the approved plan in risk/dependency order: independent assertions, required board/regression, browser/API/data checks, negative paths and bounded exploratory checks. Fresh-build evidence must come from a QA-controlled build when the claim depends on compilation. Commands must state their working directory; existence checks prevent empty diffs or greps over nonexistent paths from passing vacuously.

Maintain one coherent run. Repair disposable QA helpers within the authorized lane, preserving the failed attempt and verifying the corrected instrument. Never weaken assertions, add hidden retries, skip tests, or change product code to obtain green. An isolated product FAIL is recorded and unaffected checks continue unless the plan's stop conditions require otherwise.

Return the matrix, execution report, findings, evidence inventory, helper corrections, remaining untested areas and safe indexed ZIP automatically. Capture start/end times, full identities and the final changed-file inventory. No self-certification.

Human judgment remains available. Automate repetitive role/tab/filter/viewport/theme coverage where feasible. Declare required human checks beforehand and group independent ones near the end. If authentication, MFA or a required decision is a prerequisite, request it when needed; never fake an unattended run. Count those touches accurately.

## 11. Stops, findings and repairs

Use `STOP-*` identifiers for stops so they cannot be confused with phase names Q1/Q2/Q4/Q5. Each stop records phase, time, identity, affected checks, evidence, owner, required resolution and safe resume point.

| Stop | Trigger |
|---|---|
| STOP-IDENTITY | Wrong branch/candidate, unexpected product change or HEAD moved |
| STOP-CONTRACT | Grading depends on unresolved conflicting requirements or authority |
| STOP-ENV | Required target/data/tool/service unavailable or target mismatch |
| STOP-AUTH | Missing/invalid permitted credentials, unexpected identity, or auth outside authorization |
| STOP-AUTHORITY | Required action exceeds approved mutations, cost, data, Git or write-lane scope |
| STOP-INSTRUMENT | Measurement/helper control is untrustworthy; evidence cannot establish the claim |
| STOP-EVIDENCE | Evidence cannot be saved or exported with integrity |
| STOP-PRIVACY | Secret/protected-data exposure or unsafe retained artifact |

Do not use a stop as a reason to hide completed evidence. Supply a safe partial package when possible; withhold unsafe exports. Resume from preserved state after resolution rather than silently repeating the campaign.

Executor result labels are observations, not release decisions. Normalize PASS, FAIL, BLOCKED, NOT RUN and ADJUDICATE against the local governing vocabulary; where the governing documents use UNTESTED or PASS-PENDING-ADJUDICATION, preserve an explicit mapping. An unresolved discrepancy cannot become PASS through relabeling.

The QA Lead classifies acceptance failure, regression, environment/setup issue, instrument issue, contract gap, proven pre-existing defect, follow-up finding, enhancement or observation. Severity follows impact. Inherited conditions require evidence; neither charge them to a new module nor waive a release-blocking issue without the governing disposition.

For a genuine product defect: Lead disposition → Architect ruling/bounded repair instruction → Engineer repairs approved paths on the QA line → Director commits → Executor re-pins and performs Q4. Retest covers the repair diff, affected ACs and the full required regression suite. Carry forward only evidence whose applicability is demonstrated and whose original SHA/attempt remains visible. Live validation that the governing policy reserves for the final repaired candidate runs on that candidate. Preserve all prior attempts.

RRM-004 demonstrated no product repair round. This repair protocol carries forward the supplied governing doctrine; it is not a capability proved by that pilot.

## 12. Browser work and credentials

The approved plan must define role × route/workflow × data/filter state × viewport × theme coverage and explain reductions. Do not hardcode Cyber Pharma's ADMIN/MEMBER or 375px into every app; use the actual contract. Check rendered behavior, effective theme, keyboard/focus, errors, loading/stale/rejection states and relevant access denials. Screenshots supplement assertions; neither screenshots alone nor green jsdom tests prove all browser behavior.

Reuse one in-memory authenticated context per role where safe. Separate roles and tenants. Record actual sign-in counts. Reusable regression tests are preferred when applicable; temporary module helpers are valid evidence tools. Promotion into maintained product tests is a separate authorized engineering change.

Credential automation is permitted only when the target, identities, runtime and tool policy allow it. The Director creates the declared ignored QA credential file, normally `.env.qa.local`, with module-specific keys. Do not reuse public `NEXT_PUBLIC_*` variables for QA passwords. Prove the file is ignored AND untracked, validate its schema without emitting values, and have only the authorized local helper read values into process memory. Keep credentials out of the app build/server environment, commands, logs, exceptions, screenshots, traces, JSON and ZIPs. A service-role/admin API key is not a substitute for proving a user's login and authorization.

If browser tooling requires human credential entry, use that supported flow and record the checkpoint. No automation plan overrides tool restrictions, MFA or access controls. Login/logout can create session/audit activity even when the business test is read-only. Backend, commerce and agent tests can mutate state or trigger costs; specify permitted effects and test targets before execution.

Privacy scanners must be validated with synthetic leak fixtures and clean controls. Scan selected export contents and expanded archive members; report safe counts/locations without echoing secrets. Raw authenticated traces can contain sensitive state even after login. Retain only approved sanitized evidence. Avoid persistent browser storage; if unavoidable, declare its temporary path and cleanup before use.

## 13. Automatic review packages

Every Q1 return, Q2 return, material stop and repair/retest return must produce a predictable package, subject to privacy. The Director should never ask “which files?” or search temporary folders.

Canonical destination: `QAM/HANDOFFS/<MODULE>_<PHASE>_REVIEW_<ATTEMPT>.zip`. Return its absolute upload path, count, SHA-256 and exact decision requested. A byte-identical convenience copy in the Director's Downloads folder is allowed when requested; the module copy remains canonical. Never nest previous ZIPs by default.

Each package includes `REVIEW_START_HERE.md`, current identities/state, phase reports, plan and approval as applicable, frozen contract/rulings, necessary governing sources, findings and supporting evidence. Include the actual recon response files, not only a plan or manifest. Include exact certification/approval text when someone is instructed to transcribe it. No reconstructing a missing letter from another seat's summary.

Use an explicit inclusion list. `FILE_INDEX.json` records archive path, source path, purpose, byte size and SHA-256 for every member except itself. Verify exact index membership, hashes, safe paths, duplicates, archive integrity and privacy coverage. The external receipt hashes the completed ZIP to avoid circular hashing. Exclude env/credential files, auth state, browser profiles, dependencies, builds, Git internals, disposable mirrors and unreviewed raw sensitive logs. Missing items are listed honestly. Packaging does not require rerunning passed tests.

## 14. Cleanup, certification and closeout

Two-shot QA preserves the distinction between product evidence, cleanup readiness and release. Routine safe hygiene—closing owned browsers, stopping owned QA servers, removing declared transient auth state—belongs in the phase's preauthorized exit steps. The final Q5 retention/cleanup decision remains governed by the QA Lead and the applicable cleanup policy, including J-19 where supplied. It is a closure operation, not another full planning/testing campaign. This kit does not silently replace a required post-Gate-Q cleanup checkpoint.

At the approved cleanup point: scan values while the credential source exists; resolve/quarantine actual leaks without publishing them; delete the QA credential file and owned auth state under the declared authority; verify removal; pattern-scan retained outputs and the final export. Do not preserve credential values or hashes as evidence. After deletion, do not claim a new value scan happened; record the actual sequence and earlier source hashes. Active editor recovery files and unrelated processes are not automatically deleted. Director password rotation is separate and must be recorded as Director-reported unless independently evidenced.

The Lead defines the smallest durable evidence package sufficient for certification, reproduction and audit. Retain failed attempts and useful helpers when justified; remove disposable generated debris. Record precise paths and exclusions. Check current state before cleanup: already absent is verified absent, not newly deleted. Protected recovery/session files require their own authority.

The QA Lead issues the governing verdict: PASS, PASS WITH FOLLOW-UP FINDINGS, PASS WITH KNOWN RISK, FAIL or BLOCKED, with scope, candidate and limitations. No accepted requirement may silently become optional; meaningful risk acceptance follows Director authority. Product Gate Q, pilot-process evaluation, cleanup acceptance and Gate D remain separate claims.

Release to Architect closeout requires the accepted product verdict, required cleanup, durable records committed and the governed clean-tree condition. The Architect then directs bounded Engineer closeout; the Director commits, merges and pushes. Verify documentation-only successors before extending the recorded identity. Gate Q does not certify a deployed revision; Gate D is separately scoped and authorized when required.

## 15. State and restart discipline

Maintain `QAM_STATE.md` as a small index into authoritative records: phase, attempt, candidate, execution HEAD, contract/plan/approval identity, latest package/receipt, stop, next owner and next permitted action. Do not duplicate entire reports. Immutable exports retain their historical statements; later state entries supersede stale “pending” summaries with dated provenance.

Before any resumed instruction, compare its prerequisites to disk and current identity. If a cleanup or test already completed, report that rather than running it twice. A stale instruction requiring obsolete bytes must be reconciled by its owner. Docs-only identity changes need a scope check; product changes need a new candidate and retest decision. This rule prevents both unsafe resumption and unnecessary restarts.

## 16. Adapting the QAM to module type

| Module | Architect must supply; QA plan must address |
|---|---|
| RRM | Finding/disposition-to-AC mapping, exact rework boundary, removed behavior and preserved paths |
| FFM | Canonical design/data contracts, frontend states, responsive/keyboard/access behavior; real auth/integrations where present |
| BIM | Actual service/schema/API contracts, environment parity, auth/RLS/tenant negatives, data fixtures, allowed writes, rollback and regression |
| TRM | Its explicit Factory definition and contracts; do not guess its expansion or assume a test profile from its acronym |
| FIX/FEAT | Original failure/feature contract, changed behavior and nearest regressions |
| ABM | Whole-app acceptance and integration seams; critical end-to-end paths; scoped data/cost/side-effect authority |
| APBM | Phase boundaries and prerequisite evidence; inherited guarantees; cross-module integration and explicit deployed/live requirements |

Every independently authored module gets QAM. An ABM/APBM containing child modules also has its own QAM for aggregate scope. Parent plans may reference child certificates with candidate provenance; they cannot treat child PASS as proof that integration works. Avoid repeating unchanged child coverage without reason, while preserving required parent regression. Large phases may have bounded internal stages under one approved Q2 plan; duration and genuine stops are not hidden to preserve a slogan.

## 17. Metrics and evidence limits

Measure preparation, Q1, review/wait, Q2 execution, packaging, repair and cleanup separately. Record Director touches by purpose; record helper corrections, product repairs, stops, retries, skipped checks and remaining gaps. Zero interventions is a target, not a reason to suppress an access problem.

RRM-004 provides evidence that Q2 ran continuously with zero Director interventions and automated role sign-ins. Its 10m08s measurement body and 17m21s reported release elapsed exclude earlier preparation and Q1 resolution. Its overall pilot was PARTIAL SUCCESS because Q1 raised a contract stop. Preserve all three facts.

This v1.0 generalizes the operating process under the Director's mandate. RRM-004 alone does not validate every BIM, TRM, ABM/APBM, runtime, destructive workflow, deployment or repair scenario. New module-specific checks are required; the five-seat process remains in force.

## 18. Definition of a conforming module pack

A module pack is ready when QAM is present from authoring; both runtime entry files route correctly; the authoritative contract and all required sources resolve; Engineer completion duties are explicit; target/effects/credentials and write lanes are declared; Q1 produces recon plus a draft plan and ZIP; QA Lead approval is mandatory before Q2; Q2 runs the approved plan and exports results; repair is conditional; cleanup and closeout have owners; no execution or certification result is prefilled; and the Director never has to assemble an ad hoc QA package.

The Factory Doc Sync Architect must reconcile older lifecycle diagrams, folder trees, role tables, prompts and handoff templates with this rule, using the companion synchronization brief. A new playbook sitting beside contradictory templates is not a completed synchronization.
