# Independent manual reads

Seat: QA Executor (Codex), fresh user-launched session; start 2026-10-19T05:41:06Z. Candidate 20f71ee932ed21c0878cb3a0f39c6fbe90d0a793. All citations below refer to pristine candidate export, not the mutable review tree. Exact candidate texts are in RAW/candidate_text/. Checks grade documentation; examples were read, not executed.

## Manual judgments by criterion

### AC5

Ownership agrees in amended tables but F01 remains. Read RAW/read_ownership.txt and RAW/read_ffm.txt; all four workflow texts in RAW/ac37_workflows.json.

```text

01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md:14: Phase 1 — Ignition: Architect authors APP_BRIEF and DATA_CONTRACT before Design; Director approves scope.
01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md:15: Phase 2 — Design: Designer authors UI_SPEC and the visual package; Architect reconciles assembly.
01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md:16: Phase 3 — Engineering (spec): Architect completes the module, ACCEPTANCE_SPEC and prepared QAM; FILE_TREE optional.
01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md:55: **Artifact ownership:** the Architect owns DATA_CONTRACT before Design. The Designer owns UI_SPEC. The Architect reconciles the assembled package and Engineering consumes its approved revision. Conversion evidence informs those contracts; greenfield does not transfer authorship to Engineering. FILE_TREE is optional; implementation structure and boundaries must remain explicit in the approved package.
01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md:89: | `FILE_TREE.md` (optional) | Supplementary structure view; approved package still states implementation structure and boundaries | Architect assembly |
01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md:120: Phase 1 — Ignition: Architect authors APP_BRIEF and DATA_CONTRACT before Design; Director approves scope.
01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md:121: Phase 2 — Design: Designer authors UI_SPEC and the visual package; Architect reconciles assembly.
01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md:122: Phase 3 — Engineering (spec): Architect completes the module, ACCEPTANCE_SPEC and prepared QAM; FILE_TREE optional.
01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md:142: The Architect assembles the approved contract artifacts below for the Engineer to implement. DATA_CONTRACT is authored before Design; FILE_TREE is optional when implementation structure and boundaries are otherwise explicit.
01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md:182: ### **FILE_TREE.md** (optional)
01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md:204: | "What does the Designer actually produce?" | Token file (primary) + style tile + per-screen HTML/PNG + UI_SPEC + component manifest |
01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md:217: 3. **Before Design:** Architect prepares DATA_CONTRACT. After the Designer authors UI_SPEC and the screen set is approved, the Architect reconciles the full package. FILE_TREE is optional; structure and boundaries remain explicit.
01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md:227: | 2.0 | 9 Jun 2026 | **Stitch retired.** Pipeline diagram, doc structure, and Phase 2 workflow rebuilt around token-driven HTML → Playwright PNG. Designer deliverables corrected (token file primary; `_design/` HTML+PNG; UI_SPEC; component manifest). `STITCH_PROMPTS/` folder replaced by `_design/`. Stale vendor parentheticals dropped from the diagram (agents shown role-only). Engineer tool labeled Claudy (Claude Code). Pepper's Rig example retained as illustration. |
01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md:228: | 2.1 | 7 Jul 2026 | **Wave 1 (audit sync).** Standard header block adopted, version/date moved to top (F-018). Title "AI App Factory" → "App Factory" (F-008). Phase 0 — Recon added to the lifecycle + workflow diagram: Engineer ground-truths per RECON_QUESTIONNAIRE / stark-recon, Architect consumes the Recon Report (F-003). "Which Pipeline Am I In?" router promoted from FFM_PLAYBOOK §4 — Conversion vs Greenfield, ownership split: HANDOFF_PACKAGE_PLAYBOOK = conversion detail, agent playbooks = greenfield detail (F-030). Per-pipeline DATA_CONTRACT ownership stated (F-029). Karpathy Protocol pointer placeholder reserved (D-011). Cross-references canonical-name only (F-011). |

```

### AC6

All eight E373–E380 replacements are exact; F01 fails the surrounding-text clause. RAW/supplement_checks.json records each replacement.

```text

02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:83: | **Ground-Truth Recon (Phase 0)** | Answer RECON_QUESTIONNAIRE read-only from the filesystem; produce the Recon Report the Architect authors from |
02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:111: **The Engineer is the factory's ground-truth instrument.** Before the Architect authors anything — brief, FFM, contract — the Engineer executes recon.
02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:174: > **CONVERSION:** the Architect **PRE-AUTHORS** `DATA_CONTRACT.md` from Brain Drain evidence — the Engineer consumes and honors it.
02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:175: > **GREENFIELD:** the Architect authors `DATA_CONTRACT.md` from the approved APP_BRIEF before Design. The Designer authors UI_SPEC; the Architect reconciles the assembled package. The Engineer consumes the approved contracts. The canonical DATA_CONTRACT template remains in §12.
02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:176: > Same artifact name — different author, different moment. Router: APP_FACTORY_BLUEPRINT, "Which Pipeline Am I In?".
02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:251:    Answer RECON_QUESTIONNAIRE read-only → Recon Report → Architect authors
02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:736: > **Ownership:** the Architect authors DATA_CONTRACT before Design, using the canonical template below. Conversion includes the approved extraction evidence. The Designer authors UI_SPEC; the Architect reconciles the assembled package. Engineering consumes the approved revisions; it does not create missing contracts during implementation.

```

### AC7

The two checkpoints, clean-review/no-RRM rule, and distinction from Gates Q/D agree. SFP owns the vocabulary; RRM cites it. Read governance, FFM, new-playbook and ownership packets.

```text

01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md:39: Keep lifecycle axes separate: Blueprint phases describe the Factory pipeline; SFP implementation phases describe build disciplines; FFM sub-phases and Frontend Build Phase stages describe execution within a module; roadmap phases describe product scope. Record each stage’s parent, entry artifacts, exit evidence and approver in the module contract. Demo deployment is not Gate Q or Gate D. Engine 1 is module engineering and module QA. Engine 2 is independent system review after all Engine 1 phases and their QA are closed. The separate post-FFM review occurs after FFM and its QA. Only dispositioned findings requiring repair produce RRM work.
01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md:45: Revised workflow documents and stick diagrams: [FFM creation](../03_BUILD_METHODOLOGY/_workflows/FFM_CREATION.md), [FFM execution and post-FFM review](../03_BUILD_METHODOLOGY/_workflows/FFM_EXECUTION.md), [deployment](../03_BUILD_METHODOLOGY/_workflows/FFM_DEPLOYMENT.md), [BIM and Engine 2](../03_BUILD_METHODOLOGY/_workflows/BIM_WORKFLOW.md). They supersede the historical August pictures when verified and published; originals are retained.
01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md:124: Engine 1 denotes module engineering and module QA across the implementation phases. Review occurs after FFM completion and its QA, and again at Engine 2 after all Engine 1 phase/module engineering and QA are closed. Findings require disposition; only approved findings needing repair produce bounded RRM work, and each RRM includes QAM. A clean review produces no RRM. Module QA certification, broader review completion and deployed-system Gate D remain distinct.
01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md:180: | Engine 1 | Module engineering and independent module QA, including required certification/cleanup/closeout; complete every scoped phase/module and its QA before Engine 2. |
01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md:181: | Post-FFM review (checkpoint 1) | Independent review after FFM build and its independent QA finish; findings require disposition. |
01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md:182: | Engine 2 (checkpoint 2) | Independent system review after all Engine 1 phases/modules and their QA are closed. |
01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md:183: | RRM | Repair work only for approved review findings requiring repair; a clean review requires no RRM. Review does not replace Gate Q, Gate D or Director release. |

```

### AC8

Blueprint phases 0–5 and deployment/Gate D exist; RECON and MANIFEST refer to existing lifecycle axes. Historical four-role mentions are not current rules.

```text

01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md:24:   Complete remaining Engine 1 phases/modules and their QA; include Gate D before closing deployment-requiring work.
01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md:25: Phase 5 — Deployment: authorized operator deploys only within existing context-specific permissions.
01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md:26:   QA independently verifies the deployed revision at Gate D; production confirmation/recovery as applicable.
01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md:29:   Review, Gate Q, cleanup acceptance, Gate D and Director release remain separate decisions.
01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md:32: Engine and review vocabulary: `SOFTWARE_FACTORY_PLAYBOOK.md` §2, “Phase Vocabulary — One Canonical Map”. Deployment requirements: `DEPLOYMENT_PLAYBOOK.md`; Gate D: `QA_PLAYBOOK.md` §13.
01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md:82: ### Phase 3: ENGINEERING (Architect Contract Assembly)
01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md:130:   Complete remaining Engine 1 phases/modules and their QA; include Gate D before closing deployment-requiring work.
01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md:131: Phase 5 — Deployment: authorized operator deploys only within existing context-specific permissions.
01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md:132:   QA independently verifies the deployed revision at Gate D; production confirmation/recovery as applicable.
01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md:135:   Review, Gate Q, cleanup acceptance, Gate D and Director release remain separate decisions.
01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md:138: Engine and review vocabulary: `SOFTWARE_FACTORY_PLAYBOOK.md` §2, “Phase Vocabulary — One Canonical Map”. Deployment requirements: `DEPLOYMENT_PLAYBOOK.md`; Gate D: `QA_PLAYBOOK.md` §13.

```

### AC9

Mandatory prose/seat division/retroactivity present in each required playbook; F02 demonstrates a remaining package-tree omission.

```text

03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md:42: - The ID appears on: the module folder name, every document header inside it, the `ACCEPTANCE_SPEC.md`, QA references, retrospectives, changelog entries, and cross-document links.
03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md:54: ├── ACCEPTANCE_SPEC.md           ← Engineer-finalized at handoff; criteria seeded from approved contract (see §8)
03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md:57: ├── QAM/                        ← mandatory module-specific QA package, including matching entry routes
03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md:65: Every module folder carries one manager body and matching `CLAUDE.md` / `AGENTS.md` entry routing. Engineering routes to the implementation assignment; QA routes into `QAM/`, whose two entries assign QA Executor and point to `QAM_ENTRY.md`. Redirects may share one instruction body. Required manager contents:
03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md:83: Current recon → Architect authors the module just in time, including ACCEPTANCE_SPEC and prepared QAM.
03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md:107: 2. **Contracts freeze at handoff.** Requirements and acceptance criteria remain immutable except through an attributable approved amendment. Declared lanes inside the module remain writable by their assigned owners for engineering handoff, recon, plans, evidence, findings and rulings. QA records live in the module’s `QAM/` under `agent_docs/`. A test-plan edit cannot amend acceptance criteria.
03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md:122: ## 8. ACCEPTANCE_SPEC.md (mandatory handoff artifact — Factory-level rule, restated)
03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md:124: **The contract handed from Engineering to QA. It is NOT the QA test plan.** Engineering states what it claims complete; QA independently decides how to attack and verify. Exact filename locked: `ACCEPTANCE_SPEC.md`.
03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md:143: Every newly authored module includes a complete, module-specific `QAM/` prepared by the Architect from `03_BUILD_METHODOLOGY/_templates/QAM/`. QA Lead owns the reusable playbook and standing requirements. Engineer fills factual engineering records and handoff; QA Executor performs independent Q1 recon and test planning; QA Lead approves the plan; Director releases execution; QA Executor performs Q2 and authorized retest; QA Lead adjudicates and certifies. `QAM_PLAYBOOK.md` owns this packaging and sequence. Existing modules already in flight retain their recorded sequence until an attributable amendment.
03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md:147: Required cleanup removes only authorized disposable execution debris, temporary credentials/authentication state, and owned QA processes or browser contexts. Retain durable evidence, required failed attempts and justified helpers. QA Lead governs retention and cleanup acceptance; certification, Architect closeout and Director release remain separate responsibilities. Record command, working directory, exit code and unfiltered safe output, with sensitive data excluded at collection. Prove product, tests, configuration and contract identity unchanged by cleanup. Module QA records live under `agent_docs/` in their module `QAM/`; verify production exclusion under `DEPLOYMENT_PLAYBOOK.md`.
03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md:177: - [ ] `ACCEPTANCE_SPEC.md` finalized and handed to QA
03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md:178: - [ ] Coordinator commits landed per concern; QA-environment / Coordinator setup prerequisites required by `ACCEPTANCE_SPEC.md` executed and verified (genuinely deploy-dependent steps identified separately under Gate D)
03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md:194: | 1.0-DRAFT | 2026-08-10 | Initial draft from the six-module ADK Harness pilot campaign + two doctrine upgrades (ACCEPTANCE_SPEC; app-suffixed IDs). |

```

### AC10

Director creates and merges the QA branch; Engineer repair and Executor tests use that branch; no transfer-back/abandon rule. O-1 governs this run, not a rewrite of product doctrine.

```text

03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md:29: | **Engineer** | Plans, builds within release, self-verifies, fills factual acceptance/handoff records; may inspect Git read-only; all Git mutations remain Director-only and BIM cloud-zero remains in force |
03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md:84: Director approves scope and the Engineer plan → Engineer builds and runs baseline/regression checks.
03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md:86: Engineer completes factual handoff → Director commits/pushes the numbered product candidate.
03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md:87: Director creates qa/<module-branch> at that exact engineering candidate commit.
03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md:88: QA Executor Q1: preflight, independent recon and test plan → QA Lead plan approval → Director release.
03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md:90: If needed: QA Lead dispositions → Architect/Director authorize repair → Engineer repairs on the same QA branch.
03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md:91: Director commits repair candidate → QA Executor re-pins and independently retests with regression checks.
03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md:93: Architect closeout instructions → bounded Engineer closeout → Director final commits, merge and push.
03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md:116: - **Git/cloud authority:** read-only Git inspection is allowed; the Director performs all Git mutations. The BIM Engineer does not deploy and supplies exact file lists and suggested commit messages.
03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md:143: Every newly authored module includes a complete, module-specific `QAM/` prepared by the Architect from `03_BUILD_METHODOLOGY/_templates/QAM/`. QA Lead owns the reusable playbook and standing requirements. Engineer fills factual engineering records and handoff; QA Executor performs independent Q1 recon and test planning; QA Lead approves the plan; Director releases execution; QA Executor performs Q2 and authorized retest; QA Lead adjudicates and certifies. `QAM_PLAYBOOK.md` owns this packaging and sequence. Existing modules already in flight retain their recorded sequence until an attributable amendment.
03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md:145: The Director commits and pushes the completed engineering candidate on the numbered product branch, then creates `qa/<module-branch>` at that exact commit. Engineer performs approved repairs and QA Executor independently tests on that same QA branch, with separate writable lanes and one active writer during repair or measurement. The QA branch continues to final integration; do not transfer work back or abandon it as the normal workflow. After the QA Lead’s verdict and required cleanup, the Architect issues closeout instructions, Engineer performs bounded closeout, and the Director performs final commits, merge and push. Preserve product, execution, evidence and closeout identities separately.
03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md:147: Required cleanup removes only authorized disposable execution debris, temporary credentials/authentication state, and owned QA processes or browser contexts. Retain durable evidence, required failed attempts and justified helpers. QA Lead governs retention and cleanup acceptance; certification, Architect closeout and Director release remain separate responsibilities. Record command, working directory, exit code and unfiltered safe output, with sensitive data excluded at collection. Prove product, tests, configuration and contract identity unchanged by cleanup. Module QA records live under `agent_docs/` in their module `QAM/`; verify production exclusion under `DEPLOYMENT_PLAYBOOK.md`.

```

### AC11

Contract freeze differs from writable evidence lanes; test-plan changes do not amend acceptance.

```text

03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md:28: | **Architect** | Authors the module from recon evidence, QAs the Engineer's plan, issues binding pre-execution verdicts (GO/AMEND/BLOCK on module readiness), **advises on architectural classification and routing of QA findings — advisory, not adjudicative** |
03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md:53: ├── DATA_CONTRACT_AMENDMENT.md   ← only when wire contracts change
03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md:58: └── (declared writable output lanes: engineering handoff, recon, plans, evidence, findings, rulings)
03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md:85: Requirements and acceptance criteria freeze; declared records/evidence lanes remain writable (RUL-04).
03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md:107: 2. **Contracts freeze at handoff.** Requirements and acceptance criteria remain immutable except through an attributable approved amendment. Declared lanes inside the module remain writable by their assigned owners for engineering handoff, recon, plans, evidence, findings and rulings. QA records live in the module’s `QAM/` under `agent_docs/`. A test-plan edit cannot amend acceptance criteria.
03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md:108: 3. **DRAFT until stamped.** Docs coexisting with a not-yet-run recon carry DRAFT — CLAIM STATUS until the post-recon verdict stamps them FINAL. After the stamp, requirements and acceptance criteria are frozen; changes require an attributable approved amendment. Declared engineering handoff and QA evidence lanes remain writable by their assigned owners.
03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md:117: - **Do not silently deviate:** a change outside the authorized writable surface, including diagnostic, test-runner or build configuration changes, requires explicit authorization before execution. Report the proposed change and its evidence; later ratification is not prior authorization.
03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md:143: Every newly authored module includes a complete, module-specific `QAM/` prepared by the Architect from `03_BUILD_METHODOLOGY/_templates/QAM/`. QA Lead owns the reusable playbook and standing requirements. Engineer fills factual engineering records and handoff; QA Executor performs independent Q1 recon and test planning; QA Lead approves the plan; Director releases execution; QA Executor performs Q2 and authorized retest; QA Lead adjudicates and certifies. `QAM_PLAYBOOK.md` owns this packaging and sequence. Existing modules already in flight retain their recorded sequence until an attributable amendment.
03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md:145: The Director commits and pushes the completed engineering candidate on the numbered product branch, then creates `qa/<module-branch>` at that exact commit. Engineer performs approved repairs and QA Executor independently tests on that same QA branch, with separate writable lanes and one active writer during repair or measurement. The QA branch continues to final integration; do not transfer work back or abandon it as the normal workflow. After the QA Lead’s verdict and required cleanup, the Architect issues closeout instructions, Engineer performs bounded closeout, and the Director performs final commits, merge and push. Preserve product, execution, evidence and closeout identities separately.
03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md:151: - QA independently tests the declared engineering candidate after handoff. Requirements and acceptance criteria remain frozen; QA recon, plans, evidence, findings and rulings remain writable in their declared lanes. QA cannot amend acceptance by changing a test plan.
03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md:157: - Route-handler/API **external contracts freeze** across module boundaries; only internals are ported (field proof: a middleware was replaced under an unchanged seam with zero frontend diff — the entire point of designing the seam one module earlier).
03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md:158: - Contract changes ship as **numbered amendments** (A1, A2 …) that supersede specific sections and inherit the rest, keeping history honest.
03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md:165: - **Mid-mandate contract mutation** — changing frozen requirements or acceptance criteria without an attributable approved amendment; declared owner-specific output lanes remain writable
03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md:195: | 1.0-DRAFT-R2 | 2026-08-10 | QA review AMEND pass applied (10 findings + polish): QA verdict ownership restored (Operator final authority, Architect advisory); Factory QA verdict vocabulary; spec ownership tightened (seeded pre-implementation, Engineer finalizes without redefining); shared identity/handoff doctrine promoted above BIM to SOFTWARE_FACTORY_PLAYBOOK addendum; APP_REGISTRY demoted to proposed; AC* declared a NEW decision with X*/gate-ID legacy mapping; per-module failure policy replaces universal degrade; lifecycle sequencing fixed (QA before merge); QA waiver restricted to non-runtime changes. |
03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md:196: | 1.0 ACTIVE | 2026-08-10 | Finalization pass (F1 registry refs removed, F2 Gate-D/CLOSE sequencing, F3 setup-prerequisites wording, F5 tree label). Promoted from: ADK Harness field campaign → independent QA engagements → R1 QA review → R2 amendment pass → final consistency pass. |

```

### AC12

Cleanup retains durable evidence and failed attempts; three production-exclusion surfaces are required. Q9.1–3 byte-unchanged; Q9.4 new.

```text

03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md:47: Module packs, QAM folders, QA evidence and session records live under the project's `agent_docs/` tree (RUL-03). **Their exclusion from every built and deployed artifact must be explicitly enforced and verified; the directory name alone is not proof of production exclusion** (Director ruling RUL-03, 2026-10-14).
03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md:51: 1. **Compile and test scope** — `tsconfig` `exclude` and the test runner's scope exclude `agent_docs/**` (`RECON_QUESTIONNAIRE.md` Q9.1–Q9.2).
03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md:52: 2. **Build and deploy inputs** — the platform's ignore rules exclude `agent_docs/**` from the build context and the deployed bundle: `.dockerignore` for container builds, `.gcloudignore` for Cloud Build, `.vercelignore` or the platform's equivalent for Vercel-style deploys (`RECON_QUESTIONNAIRE.md` Q9.4).
03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md:53: 3. **The artifact itself** — the built image, bundle or deployed revision is inspected for any `agent_docs` path; the inspection command, working directory, exit code and output are recorded as EVIDENCE.
03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md:55: Where the verification is performed: at module packaging (Architect declares the exclusion mechanism in the module manager), at QA readiness (QA Executor preflight), and at Gate D (Step D1 evidence names the inspected artifact). A pack that cannot show the three surfaces excluded is not deploy-ready.

```

### AC13

Responsibilities and test execution are seat-based. Tool/persona mentions that are descriptions are retained under the no-mass-rename scope, not grants. RAW/supplement_personas.txt retains all hits.

```text

03_BUILD_METHODOLOGY/QA_PLAYBOOK.md:209: - reviews and approves the QA Executor’s independent plan,
03_BUILD_METHODOLOGY/QA_PLAYBOOK.md:214: ## QA Executor
03_BUILD_METHODOLOGY/QA_PLAYBOOK.md:216: The QA Executor independently performs Q1 recon and test planning, executes the approved plan after Director release, records evidence, packages checkpoints, and performs authorized retest and cleanup. The Executor does not repair product code, grant release authority or certify its own result.
03_BUILD_METHODOLOGY/QA_PLAYBOOK.md:456: ## Stage 5 — Operator Manual QA
03_BUILD_METHODOLOGY/QA_PLAYBOOK.md:458: For newly authored modules, the QA Lead’s approved QAM plan allocates checks to the QA Executor or to declared human-only verification according to evidence needs, capability and authorized side effects. Agent-capable matrices do not default to the Director. The one-test-at-a-time protocol below applies when the plan calls for Operator execution. It does not replace independent Q1 planning, plan approval or Director release.
03_BUILD_METHODOLOGY/QA_PLAYBOOK.md:1641: Use one-test-at-a-time execution by default.

```

### AC14

FFM §22/Appendix B, BIM grammar and all three routing templates send QA to QAM as Executor, identify seat and reserve Git mutations to Director. Routing bodies match exactly; opposite-file marker comments are intentionally different.

```text

03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:63: The FFM preparation stream retains Designer, Extractor, Architect and Engineer responsibilities. The complete delivery workflow also includes independent QA Executor and QA Lead responsibilities and the Director’s approval and release authority. Each role’s outputs feed the next role’s inputs; the preparation diagram below is not a complete release lifecycle.
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:254: Every newly authored module includes a complete, module-specific `QAM/` prepared by the Architect from `03_BUILD_METHODOLOGY/_templates/QAM/`. QA Lead owns the reusable playbook and standing requirements. Engineer fills factual engineering records and handoff; QA Executor performs independent Q1 recon and test planning; QA Lead approves the plan; Director releases execution; QA Executor performs Q2 and authorized retest; QA Lead adjudicates and certifies. `QAM_PLAYBOOK.md` owns this packaging and sequence. Existing modules already in flight retain their recorded sequence until an attributable amendment.
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:267: │   ├── CLAUDE.md         # QA Executor entry → QAM_ENTRY.md
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:268: │   ├── AGENTS.md         # same QA Executor routing
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:535: The archived FFM is read-only reference material. Future architects can grep it for patterns; future engineers can read its retrospective.
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:549:    (Engineer answers RECON_QUESTIONNAIRE read-only via stark-recon; the Architect
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1287: - Produces NO code in this sub-phase — read-only
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1819: - [ ] Parent entry files route Engineering to implementation and QA to `QAM/`; both QAM entry files assign QA Executor.
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:2073: │   ├── CLAUDE.md         # QA Executor entry → QAM_ENTRY.md
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:2074: │   ├── AGENTS.md         # same QA Executor routing
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:2144: For newly authored modules, use the prepared module entry routes. Engineering launch does not approve QA execution. QA launch enters `QAM/` as QA Executor at the durable recorded state; Q1 produces the independent plan, Q2 requires QA Lead approval and Director release. Resume validates candidate, branch, approval and writable lanes before acting.
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:2151: Identify your assigned seat and released assignment before acting.
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:2154: Engineering routes to implementation; QA routes into the prepared QAM as QA Executor.
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:2156: Read-only filesystem/Git inspection and declared reporting writes are allowed.
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:2157: Diagnostic changes need explicit authorization. Git mutations remain with the Director.

```

### AC15

Corrected scope/facts/Director rule and later-ratification clause exist, but F03 is a conflicting active diagram.

```text

01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md:33: Resolve authority by the question being answered: disk and recon establish what exists; approved artifacts establish what is authorized; the named domain owner defines the reusable pattern. A conflict between these is not permission to substitute one for another. Stop the affected work, record both sources and their revisions, and obtain the Director’s attributable ruling. Preserve stage-specific authority within its stated scope.

```

### AC16

31-row withdrawal review below. F04 identifies three rows with remaining unsafe/dependent positive recipes.

```text

04_REFERENCE_MANUALS/AUTH_MANUAL.md:394: **Executable example withdrawn.** The previous example is not an approved implementation. The outgoing archived document preserves it as history. Replacement code requires the project’s approved contract, verified dependency interfaces and behavioral evidence. This withdrawal contains the misleading recipe; it does not certify the underlying finding resolved.
04_REFERENCE_MANUALS/AUTH_MANUAL.md:488: **Executable example withdrawn.** The previous example is not an approved implementation. The outgoing archived document preserves it as history. Replacement code requires the project’s approved contract, verified dependency interfaces and behavioral evidence. This withdrawal contains the misleading recipe; it does not certify the underlying finding resolved.
04_REFERENCE_MANUALS/AUTH_MANUAL.md:559: **Executable example withdrawn.** The previous example is not an approved implementation. The outgoing archived document preserves it as history. Replacement code requires the project’s approved contract, verified dependency interfaces and behavioral evidence. This withdrawal contains the misleading recipe; it does not certify the underlying finding resolved.
04_REFERENCE_MANUALS/AUTH_MANUAL.md:834: **Executable example withdrawn.** The previous example is not an approved implementation. The outgoing archived document preserves it as history. Replacement code requires the project’s approved contract, verified dependency interfaces and behavioral evidence. This withdrawal contains the misleading recipe; it does not certify the underlying finding resolved.
04_REFERENCE_MANUALS/AUTH_MANUAL.md:920: **Executable example withdrawn.** The previous example is not an approved implementation. The outgoing archived document preserves it as history. Replacement code requires the project’s approved contract, verified dependency interfaces and behavioral evidence. This withdrawal contains the misleading recipe; it does not certify the underlying finding resolved.
04_REFERENCE_MANUALS/AUTH_MANUAL.md:928: **Executable example withdrawn.** The previous example is not an approved implementation. The outgoing archived document preserves it as history. Replacement code requires the project’s approved contract, verified dependency interfaces and behavioral evidence. This withdrawal contains the misleading recipe; it does not certify the underlying finding resolved.
04_REFERENCE_MANUALS/AUTH_MANUAL.md:1307: **Executable example withdrawn.** The previous example is not an approved implementation. The outgoing archived document preserves it as history. Replacement code requires the project’s approved contract, verified dependency interfaces and behavioral evidence. This withdrawal contains the misleading recipe; it does not certify the underlying finding resolved.
04_REFERENCE_MANUALS/AUTH_MANUAL.md:1311: Use the session client for identity and RLS-bound data. Acquire an isolated admin client only after independently authorizing the elevated operation. An API route is not itself a reason to bypass RLS. Do not substitute a service-role client as a general fix for denied access.
04_REFERENCE_MANUALS/AUTH_MANUAL.md:1317: **Executable example withdrawn.** The previous example is not an approved implementation. The outgoing archived document preserves it as history. Replacement code requires the project’s approved contract, verified dependency interfaces and behavioral evidence. This withdrawal contains the misleading recipe; it does not certify the underlying finding resolved.
04_REFERENCE_MANUALS/AUTH_MANUAL.md:1327: **Executable example withdrawn.** The previous example is not an approved implementation. The outgoing archived document preserves it as history. Replacement code requires the project’s approved contract, verified dependency interfaces and behavioral evidence. This withdrawal contains the misleading recipe; it does not certify the underlying finding resolved.

```

### AC17

Preserved domain constraints and six distinctions checked against candidate and BASE. RAW/ac17_preservation.json gives exact preserved spans; the roles block includes intentional containment wording, so its whole-span false result is not a deletion of the role-table invariant.

```text

04_REFERENCE_MANUALS/DATABASE_MANUAL.md:31: ### Schema-First Development
04_REFERENCE_MANUALS/DATABASE_MANUAL.md:41: > **When Schema-First Applies:** schema-first is the law for **backend phases and conversions** (the data shape is known or extracted). For **discovery builds the factory runs frontend-first**: UI against a mock DATA_CONTRACT first, schema authored at the backend transition — see `FRONTEND_FIRST_PLAYBOOK.md` §2 (when frontend-first is allowed) and §8 (the transition point). Both orders are legitimate; the pipeline you're in decides.
04_REFERENCE_MANUALS/DATABASE_MANUAL.md:45: │                        SCHEMA-FIRST WORKFLOW                                 │
04_REFERENCE_MANUALS/DATABASE_MANUAL.md:60: ### Why Schema-First?
04_REFERENCE_MANUALS/DATABASE_MANUAL.md:179: **Synchronization example withdrawn.** The role table is the only authorization authority. Never authorize from user_metadata or a profile mirror. Superadmin creation is console-only; no app-side superadmin creation route is provided. Retire the metadata-authorized add-user, delete-user and get-users recipes. Future privileged list/delete operations remain possible only with trusted current-role lookup, operation-local authorization before elevated capability, an approved target-role allowlist and privileged-target protection. Profile mirrors contain profile data, not authorization columns. Registration metadata is not authorization. Use the session client for identity and RLS-bound data. Acquire an isolated admin client only after independently authorizing the elevated operation. An API route is not itself a reason to bypass RLS. Do not substitute a service-role client as a general fix for denied access. Use an atomic database operation for invariants inside one database. Across external boundaries, use a stable operation identity, check every forward and compensation result, and persist completed, failed or partially-completed outcomes. Partial failure creates durable reconciliation work with a recovery owner; do not report success after an unchecked compensation or deletion.
04_REFERENCE_MANUALS/DATABASE_MANUAL.md:362: ALTER TABLE user_profiles ENABLE ROW LEVEL SECURITY;
04_REFERENCE_MANUALS/DATABASE_MANUAL.md:1150: - **`FRONTEND_FIRST_PLAYBOOK.md`** — §2/§8: when schema-first defers to mock-first (see the note in §1).
04_REFERENCE_MANUALS/DATABASE_MANUAL.md:1159: | 1.0 | (original, date unknown) | Initial manual: schema-first philosophy, design patterns, data types, relationships, RLS, indexing, JSONB, type generation, query patterns, migrations, integrity, performance. Unversioned until the 2026-07 audit. |
04_REFERENCE_MANUALS/DATABASE_MANUAL.md:1160: | 1.1 | 2026-07-08 | **Wave 4 — role-doctrine surgery (F-041, security-classed).** §2: new "Roles Table Pattern" — `user_roles` as the single authorization home (labeled PATTERN SQL; kit `setup.sql` = ground truth), `handle_new_user()` creation-time transport explained, ⛔ forbidden box (no role storage OR authz reads from `user_metadata` — recon Q3.4; no role columns on profile mirrors); mirror-table pattern stripped of its `role` column + sync example rewritten to the transport model. §5: the `raw_user_meta_data` RLS policy variant REMOVED (it was shown as a peer option — it is the forbidden pattern); `user_roles` policy stands alone + ⛔ marker (ruling: reconcile BOTH examples). Doc now speaks ONE role doctrine, aligned with AUTH_MANUAL v1.3 (F-042 outcome). "When Schema-First Applies" note + FRONTEND_FIRST pointers added (F-040). GHL/QR fossil examples neutralized (naming table, mapping-table default, comments — recon Q8.5 class). Standard header (F-018); Cross-References section (F-035); this history table (D-018). |

```

### AC18

F05: explicit default not present across all four required manuals. No runtime persistence test is claimed.

```text

04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:194:       partialize: (state) => ({
04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:499: ### `partialize` - What to Persist
04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:501: **Never persist everything.** Use `partialize` to select only UX-critical state:
04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:518:       partialize: (state) => ({
04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:519:         // Raw contact information is not persisted by default.
04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:783: Do not persist raw contact details by default. Any approved personal-data persistence declares permitted fields, retention duration and user or guest scope. Sign-out and account transition reset and invalidate every affected store even when remote logout fails; a new account must not hydrate the previous account’s data. Payment and authorization state remain outside persistence. Storage readiness is separate from business-data reset.
04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:1026: - **Persist only UX-critical state** with `partialize`

```

### AC19

RULED/OPEN separation and O1–O6 owners in deployment playbook pass; its OPEN text grants nothing. F06 concerns a contradictory live platform instruction elsewhere.

```text

03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md:4: > **Version:** 1.0 · **Date:** 2026-10-18 · **Status:** DRAFT FOR EXECUTABLE-MAP REVIEW — NOT INSTALLED (sections marked OPEN are not doctrine until ruled)
03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md:7: > **Provenance:** Created by the Director's placement ruling of 2026-10-14 (RUL-06) as the owning document that the Factory lacked (certified finding FC-011). Ruled content: the module Git flow (RUL-02) and the deployment-exclusion rule (RUL-03). Source material for the sections still marked OPEN: the DevOps operating model of 2026-08-24 (harvest source SRC-W07, status REVIEW; preserved in this run's intake snapshot); its claims are not adopted here.
03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md:17: - **RULED** — Director-ruled doctrine, in force.
03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md:18: - **OPEN** — a named gap. An OPEN section records the question, its owner and what exists in the sources; it grants no authority and must not be cited as a rule. Open items are closed only by a recorded Director ruling landed through DocSet Sync.
03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md:20: ## 2. Seats and Authority — RULED
03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md:22: - **Director** holds release authority and performs project-module Git mutations under RUL-02. QA seats do not mutate product or Git. Existing BIM cloud-zero restrictions remain in force in their declared context. Existing context-specific permissions, including any recorded FFM staging permission, remain intact; missing DevOps assignments and platform procedures remain OPEN under DEC-18; this section grants no new cloud permission.
03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md:25: - **DevOps Architect seat occupant** — OPEN (see §8, O-2).
03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md:31: | Project module engineering (FFM, BIM, FIX, FEAT, RRM) | Build, test, self-verify; hand the Director file lists and suggested commit messages | Engineer (read-only Git inspection allowed; Git mutations Director-only; existing context-specific cloud permissions retained) | RULED (`BIM_PLAYBOOK.md` §7) |
03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md:32: | Project module engineering | Commit per concern to the module branch; push | Director | RULED (`BIM_PLAYBOOK.md` §6) |
03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md:33: | Project module QA | Create `qa/<module-branch>` **at the completed engineering candidate commit** after the engineering handoff; commit on it; merge it into `main`; push `main` | Director | RULED (RUL-02, 2026-10-14) |
03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md:34: | Project module QA | Authorized rework on `qa/<module-branch>` only when ruled; never on a transfer back to the engineering branch | Engineer | RULED (RUL-02) |
03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md:35: | Project module QA | Independent testing on `qa/<module-branch>`; no Git mutation | QA Executor | RULED (RUL-02; `QAM_PLAYBOOK.md` §3) |
03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md:36: | Project module QA | Certify the governed candidate; approve cleanup and retention | QA Lead | RULED (RUL-01, RUL-03) |
03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md:37: | Project module closeout | Closeout instruction; bounded closeout; commit, merge, push | Architect → Engineer → Director | RULED (RUL-02, RUL-03) |
03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md:38: | Doctrine Hub synchronization (`app-factory-docs-v1`) | Run branch, commits and the one authorized push inside the Hub only | Director-only Git mutations for this sync (RUL-15); read-only Git inspection is allowed. Historical Hub exceptions do not override this assignment | RULED (Operator ruling 2026-08-05, reconfirmed 2026-09-14; cited, not restated) |
03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md:39: | Cloud contexts beyond an existing explicit restriction | Deploy, promote, roll back, change infrastructure | Per an attributable context-specific authorization; no general grant here | OPEN under DEC-18 (§7–§8) |
03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md:40: | FFM runs | Retain the recorded FFM staging permission; verify its bounds before any action | — | OPEN (§8, O-1) |
03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md:41: | Any context | Cloud columns of this matrix (who prepares the package, who verifies readiness, who executes which phase) | — | OPEN (§8, O-1) |
03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md:45: ## 4. Deployment Exclusion of `agent_docs/**` — RULED
03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md:57: Revised [deployment workflow and stick diagram](_workflows/FFM_DEPLOYMENT.md) supersede the original August deployment picture; platform-specific procedures and new permissions remain outside this run.
03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md:63: RUL-10 (2026-10-16) approves the common requirements below, without granting new deployment authority: Record the identity chain repository → commit → build or image → deployed revision → environment → route/domain as applicable. Preserve the tested-product equivalence check through documentation-only successors (proved from the complete diff, not from a commit message). Do not generalize "redeploy runs the last phase only" without checking changed configuration, secrets, permissions, migrations and deployment prerequisites. A traffic rollback plus Git revert does not restore data or external effects; every deployment names a rollback or recovery plan suited to the changed surfaces, its operator and its evidence.
03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md:69: ## 7. Platform Profiles — OPEN
03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md:73: ## 8. Open Items Register — OPEN (not doctrine)
03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md:75: | ID | Open item | Owner | Source of the gap |
03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md:84: An OPEN item is closed only by a Director ruling recorded and landed through DocSet Sync; until then no module may cite this section as authority for a deployment action.
03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md:90: | 1.0 | 2026-10-18 | New doc entering Hub: owning document for deployment and Git / cloud authority (RUL-06; FC-011). Ruled content: seats and authority (§2), the context × action × seat matrix's ruled rows (§3; RUL-02; Hub D5 cited), deployment exclusion of `agent_docs/**` with three verified surfaces (§4; RUL-03). Gate D pointer (§5). Distribution and pinning (§6, RUL-14). Platform profiles and the DevOps remainder recorded as OPEN (§7–§8; DEC-18). [FC-011; FC-012; FC-088; IN-2026-10-15-08 … IN-2026-10-15-10 (WF-08, WF-09, WF-10); RUL-02; RUL-03; RUL-06]; current correction pass: MC-01…14; RUL-02, RUL-03, RUL-06, RUL-10 |

```

### AC20

Historical containers pass (12 markdown-it entries plus the independently checked FFM paragraph). F07 fails universal-landing-path clause. D-3 punctuation is observation only.

```text

03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:42: A **Frontend-First Module (FFM)** is a portable, self-contained folder dropped at `agent_docs/CURRENT_APP/<project>_<phase>_ffm/` inside a starter kit clone. It is the single source of truth that tells an AI coding tool (Claude Code, Codex CLI, Gemini CLI, etc.) **what to build, how to build it, and what not to touch.**
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:169: **Produces:** The complete FFM folder, ready to drop at `agent_docs/CURRENT_APP/`.
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:173: **Handoff target:** The starter kit's `agent_docs/CURRENT_APP/` directory.
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:461: - **Scannable** — operator glancing at `agent_docs/CURRENT_APP/` knows immediately what's there
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:477: agent_docs/CURRENT_APP/
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:529: ├── current_app/                          ← active FFM lives here
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:537: Some teams prefer to keep all FFMs in `current_app/` and use git tags / branches to mark phase completion. Either approach works; the discipline is **don't delete FFMs**.
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1639: The FFM lives at `agent_docs/CURRENT_APP/<project>_<phase>_ffm/`. The starter kit's root `CLAUDE.md` needs to know it's there.
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1650: The current project's Factory module lives at `agent_docs/CURRENT_APP/<ffm_folder_name>/`. Read `CLAUDE.md` in that folder for project-specific direction, doctrine, and the phase-by-phase playbook. All work for the current project follows that module.
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1663: **`agent_docs/CURRENT_APP/<ffm_folder_name>/`**
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1795: ❌ "Read the CLAUDE.md at `agent_docs/CURRENT_APP/<FFM_FOLDER>/CLAUDE.md`"
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1796: ✅ "Read the CLAUDE.md at `agent_docs/CURRENT_APP/cyber_pharma_v1_phase1_ffm/CLAUDE.md`"
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1997: This playbook describes two historical FFM examples below. Availability is unverified: obtain the source repository, immutable revision and path before use; do not assume either example is present locally.
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:2001: **Location:** `agent_docs/CURRENT_APP/app-factory-frontend-first-module/` (in the Cyberize starter kit clone)
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:2026: **Location:** `agent_docs/CURRENT_APP/cyber_pharma_v1_phase1_ffm/` (in both main app and superadmin app starter kit clones)

```

### AC34

Every excluded component has an owner and resolving trigger; deferred kit/commerce/subscription designs stay visible and open.

```text

01_CONSTITUTION/STARTER_KIT_HANDBOOK.md:73: **Session/cookie architecture:** verify the pinned server and browser clients, cookie adapters, attributes and refresh behavior together. Neither blanket `httpOnly: true` nor blanket `httpOnly: false` is approved here. Do not change attributes without a compatible verified session contract and tests.
01_CONSTITUTION/STARTER_KIT_HANDBOOK.md:164: - Historical Mark IV role-from-metadata behavior is unverified for safe public signup. Do not adopt it: privileged assignment must be inaccessible to client-controlled input and proven against pinned trigger/caller source.
01_CONSTITUTION/STARTER_KIT_HANDBOOK.md:169: **User creation requires a verified trusted role path.** Never permit client-writable metadata to grant privilege. Verify the pinned trigger and protected admin action before using creation-time transport; avoid duplicate inserts only where the verified trigger already owns those rows. Missing kit evidence blocks this recipe.
01_CONSTITUTION/STARTER_KIT_HANDBOOK.md:277: - Historical kit rail dimensions/breakpoints require verification against the pinned shell implementation; no current kit value is certified here. Verify trigger, dismissal and layout on both sides of the actual fit breakpoint.
01_CONSTITUTION/STARTER_KIT_HANDBOOK.md:278: - Historical kit rail dimensions/breakpoints require verification against the pinned shell implementation; no current kit value is certified here. Verify trigger, dismissal and layout on both sides of the actual fit breakpoint.
01_CONSTITUTION/STARTER_KIT_HANDBOOK.md:395: - Historical kit rail dimensions/breakpoints require verification against the pinned shell implementation; no current kit value is certified here. Verify trigger, dismissal and layout on both sides of the actual fit breakpoint.

```

### AC37

All four source-qualified workflow documents and SVG text-node sequences read. Steps 7/18/8/24 match the plan. Actor vocabulary creates no new permission. Creation orders Architect contract before Design, execution carries checkpoint 1/QA branch, BIM carries Engine 1 continuation/checkpoint 2/approved repair only, deployment distinguishes Gate D and existing permissions. Exact quotations:

```text

03_BUILD_METHODOLOGY/_workflows/BIM_WORKFLOW.md:1: # BIM lifecycle and Engine 2 system review
03_BUILD_METHODOLOGY/_workflows/BIM_WORKFLOW.md:2: 
03_BUILD_METHODOLOGY/_workflows/BIM_WORKFLOW.md:3: > **Version:** 1.0 · **Date:** 2026-10-18 · **Status:** Proposed — pending verified publication
03_BUILD_METHODOLOGY/_workflows/BIM_WORKFLOW.md:4: > **Governed by:** `BIM_PLAYBOOK.md`, `SOFTWARE_FACTORY_PLAYBOOK.md` §2, `RRM_PLAYBOOK.md` §2, `QAM_PLAYBOOK.md`, `DEPLOYMENT_PLAYBOOK.md`.
03_BUILD_METHODOLOGY/_workflows/BIM_WORKFLOW.md:5: 
03_BUILD_METHODOLOGY/_workflows/BIM_WORKFLOW.md:6: This revised workflow supersedes the August diagram `SRC-W04_BIM_WORKFLOW.png` for current instructions when this proposed sync is approved, landed and verified. The [unaltered original](../../_AUDIT/SYNC_2026-10-15_doctrine-part2/INTAKE_SNAPSHOT/factory-intake/SOURCES/Workflow/SRC-W04_BIM_WORKFLOW.png) remains historical evidence; it grants no current role, Git or cloud permission. This derivative follows RUL-01…15 and Tony’s explicit workflow/diagram correction assignment of 2026-10-16.
03_BUILD_METHODOLOGY/_workflows/BIM_WORKFLOW.md:7: 
03_BUILD_METHODOLOGY/_workflows/BIM_WORKFLOW.md:8: ![Revised stick-actor workflow](../_assets/workflows/BIM_WORKFLOW.svg)
03_BUILD_METHODOLOGY/_workflows/BIM_WORKFLOW.md:9: 
03_BUILD_METHODOLOGY/_workflows/BIM_WORKFLOW.md:10: ## Sequence
03_BUILD_METHODOLOGY/_workflows/BIM_WORKFLOW.md:11: 
03_BUILD_METHODOLOGY/_workflows/BIM_WORKFLOW.md:12: 1. **Engineer:** Fresh recon after preceding module closeout.
03_BUILD_METHODOLOGY/_workflows/BIM_WORKFLOW.md:13: 2. **Architect:** Author BIM just in time; prepare contract and QAM.
03_BUILD_METHODOLOGY/_workflows/BIM_WORKFLOW.md:14: 3. **Director:** Approve scope and release Engineering.
03_BUILD_METHODOLOGY/_workflows/BIM_WORKFLOW.md:15: 4. **Engineer:** Implement, verify and complete factual handoff.
03_BUILD_METHODOLOGY/_workflows/BIM_WORKFLOW.md:16: 5. **Director:** Commit/push candidate; QA branch at that exact commit.
03_BUILD_METHODOLOGY/_workflows/BIM_WORKFLOW.md:17: 6. **QA Executor:** Q1 recon and independent plan.
03_BUILD_METHODOLOGY/_workflows/BIM_WORKFLOW.md:18: 7. **QA Lead:** Approve plan.
03_BUILD_METHODOLOGY/_workflows/BIM_WORKFLOW.md:19: 8. **Director:** Release Q2.
03_BUILD_METHODOLOGY/_workflows/BIM_WORKFLOW.md:20: 9. **QA Executor:** Q2 tests and findings.
03_BUILD_METHODOLOGY/_workflows/BIM_WORKFLOW.md:21: 10. **Engineer:** Conditional authorized repairs on continuing QA branch.
03_BUILD_METHODOLOGY/_workflows/BIM_WORKFLOW.md:22: 11. **Director:** Commit repaired candidate on the continuing QA branch.
03_BUILD_METHODOLOGY/_workflows/BIM_WORKFLOW.md:23: 12. **QA Executor:** Independent retest of repairs and required regression.
03_BUILD_METHODOLOGY/_workflows/BIM_WORKFLOW.md:24: 13. **QA Lead:** Product certification; approve cleanup retention.
03_BUILD_METHODOLOGY/_workflows/BIM_WORKFLOW.md:25: 14. **QA Executor:** Perform authorized required cleanup; retain evidence.
03_BUILD_METHODOLOGY/_workflows/BIM_WORKFLOW.md:26: 15. **QA Lead:** Accept cleanup separately from product verdict.
03_BUILD_METHODOLOGY/_workflows/BIM_WORKFLOW.md:27: 16. **Architect:** Closeout instructions.
03_BUILD_METHODOLOGY/_workflows/BIM_WORKFLOW.md:28: 17. **Engineer:** Bounded closeout.
03_BUILD_METHODOLOGY/_workflows/BIM_WORKFLOW.md:29: 18. **Director:** Final commits, merge and push.
03_BUILD_METHODOLOGY/_workflows/BIM_WORKFLOW.md:30: 19. **Authorized operator:** If deployment in scope: deploy within existing permissions.
03_BUILD_METHODOLOGY/_workflows/BIM_WORKFLOW.md:31: 20. **QA Executor:** If deployed: independently verify the exact revision at Gate D.
03_BUILD_METHODOLOGY/_workflows/BIM_WORKFLOW.md:32: 21. **QA Lead:** If deployed: Gate D verdict; otherwise documented N/A.
03_BUILD_METHODOLOGY/_workflows/BIM_WORKFLOW.md:33: 22. **Architect:** Complete all Engine 1 phases/modules and their QA.
03_BUILD_METHODOLOGY/_workflows/BIM_WORKFLOW.md:34: 23. **Reviewers:** Review checkpoint 2: Engine 2 independent system review.
03_BUILD_METHODOLOGY/_workflows/BIM_WORKFLOW.md:35: 24. **Director:** Disposition findings; RRM only for approved repairs.
03_BUILD_METHODOLOGY/_workflows/BIM_WORKFLOW.md:36: 
03_BUILD_METHODOLOGY/_workflows/BIM_WORKFLOW.md:37: ## Review and release checkpoints
03_BUILD_METHODOLOGY/_workflows/BIM_WORKFLOW.md:38: 
03_BUILD_METHODOLOGY/_workflows/BIM_WORKFLOW.md:39: - Review checkpoint 1: after FFM build and its independent QA finish.
03_BUILD_METHODOLOGY/_workflows/BIM_WORKFLOW.md:40: - Review checkpoint 2: Engine 2 independent system review after all Engine 1 phases/modules and their QA are closed.
03_BUILD_METHODOLOGY/_workflows/BIM_WORKFLOW.md:41: - At either checkpoint, disposition findings; RRM only for approved findings requiring repairs. A clean review requires no RRM.
03_BUILD_METHODOLOGY/_workflows/BIM_WORKFLOW.md:42: - Review, Gate Q, required cleanup and certification, Gate D and Director release remain separate responsibilities.
03_BUILD_METHODOLOGY/_workflows/BIM_WORKFLOW.md:43: 
03_BUILD_METHODOLOGY/_workflows/BIM_WORKFLOW.md:44: ## Entry, handoff and evidence
03_BUILD_METHODOLOGY/_workflows/BIM_WORKFLOW.md:45: 
03_BUILD_METHODOLOGY/_workflows/BIM_WORKFLOW.md:46: Boot/resume through the module’s declared entry file: Engineering routes to its released implementation assignment; QA routes to `QAM/` as QA Executor. Read-only Git inspection and declared reporting writes are permitted; Tony performs all Git mutations. Requirements/acceptance freeze while declared handoff and QA evidence lanes remain writable. Preserve actual candidate, test-plan, repair/retest, cleanup and closeout identities; never prefill a verdict or planned commit SHA. Deployment additionally requires verified exclusion from build inputs and the actual artifact; a folder name is insufficient. Existing modules in flight keep their recorded sequence unless explicitly amended.
03_BUILD_METHODOLOGY/_workflows/BIM_WORKFLOW.md:47: 
03_BUILD_METHODOLOGY/_workflows/BIM_WORKFLOW.md:48: ## Version History
03_BUILD_METHODOLOGY/_workflows/BIM_WORKFLOW.md:49: 
03_BUILD_METHODOLOGY/_workflows/BIM_WORKFLOW.md:50: | Version | Date | Change | Authority |
03_BUILD_METHODOLOGY/_workflows/BIM_WORKFLOW.md:51: |---|---|---|---|
03_BUILD_METHODOLOGY/_workflows/BIM_WORKFLOW.md:52: | 1.0 | 2026-10-18 | Revised workflow and stick diagram; original retained; review checkpoints and seat boundaries reconciled | MC-06; W01–W23; RUL-01–RUL-15; Tony 2026-10-16 correction assignment |

```

```text

03_BUILD_METHODOLOGY/_workflows/FFM_CREATION.md:1: # FFM creation and Architect assembly
03_BUILD_METHODOLOGY/_workflows/FFM_CREATION.md:2: 
03_BUILD_METHODOLOGY/_workflows/FFM_CREATION.md:3: > **Version:** 1.0 · **Date:** 2026-10-18 · **Status:** Proposed — pending verified publication
03_BUILD_METHODOLOGY/_workflows/FFM_CREATION.md:4: > **Governed by:** `FFM_PLAYBOOK.md`, `SOFTWARE_FACTORY_PLAYBOOK.md` §2, `RRM_PLAYBOOK.md` §2, `QAM_PLAYBOOK.md`, `DEPLOYMENT_PLAYBOOK.md`.
03_BUILD_METHODOLOGY/_workflows/FFM_CREATION.md:5: 
03_BUILD_METHODOLOGY/_workflows/FFM_CREATION.md:6: This revised workflow supersedes the August diagram `SRC-W01_FFM_CREATION.png` for current instructions when this proposed sync is approved, landed and verified. The [unaltered original](../../_AUDIT/SYNC_2026-10-15_doctrine-part2/INTAKE_SNAPSHOT/factory-intake/SOURCES/Workflow/SRC-W01_FFM_CREATION.png) remains historical evidence; it grants no current role, Git or cloud permission. This derivative follows RUL-01…15 and Tony’s explicit workflow/diagram correction assignment of 2026-10-16.
03_BUILD_METHODOLOGY/_workflows/FFM_CREATION.md:7: 
03_BUILD_METHODOLOGY/_workflows/FFM_CREATION.md:8: ![Revised stick-actor workflow](../_assets/workflows/FFM_CREATION.svg)
03_BUILD_METHODOLOGY/_workflows/FFM_CREATION.md:9: 
03_BUILD_METHODOLOGY/_workflows/FFM_CREATION.md:10: ## Sequence
03_BUILD_METHODOLOGY/_workflows/FFM_CREATION.md:11: 
03_BUILD_METHODOLOGY/_workflows/FFM_CREATION.md:12: 1. **Engineer:** Current recon; declared reporting writes.
03_BUILD_METHODOLOGY/_workflows/FFM_CREATION.md:13: 2. **Architect:** Author APP_BRIEF from current recon.
03_BUILD_METHODOLOGY/_workflows/FFM_CREATION.md:14: 3. **Director:** Approve scope and brief.
03_BUILD_METHODOLOGY/_workflows/FFM_CREATION.md:15: 4. **Architect:** DATA_CONTRACT before Design.
03_BUILD_METHODOLOGY/_workflows/FFM_CREATION.md:16: 5. **Designer:** UI_SPEC, tokens and visual artifacts.
03_BUILD_METHODOLOGY/_workflows/FFM_CREATION.md:17: 6. **Architect:** Reconcile assembly; prepare module QAM.
03_BUILD_METHODOLOGY/_workflows/FFM_CREATION.md:18: 7. **Director:** Approve package and release Engineering.
03_BUILD_METHODOLOGY/_workflows/FFM_CREATION.md:19: 
03_BUILD_METHODOLOGY/_workflows/FFM_CREATION.md:20: ## Review and release checkpoints
03_BUILD_METHODOLOGY/_workflows/FFM_CREATION.md:21: 
03_BUILD_METHODOLOGY/_workflows/FFM_CREATION.md:22: - Review checkpoint 1: after FFM build and its independent QA finish.
03_BUILD_METHODOLOGY/_workflows/FFM_CREATION.md:23: - Review checkpoint 2: Engine 2 independent system review after all Engine 1 phases/modules and their QA are closed.
03_BUILD_METHODOLOGY/_workflows/FFM_CREATION.md:24: - At either checkpoint, disposition findings; RRM only for approved findings requiring repairs. A clean review requires no RRM.
03_BUILD_METHODOLOGY/_workflows/FFM_CREATION.md:25: - Review, Gate Q, required cleanup and certification, Gate D and Director release remain separate responsibilities.
03_BUILD_METHODOLOGY/_workflows/FFM_CREATION.md:26: 
03_BUILD_METHODOLOGY/_workflows/FFM_CREATION.md:27: ## Entry, handoff and evidence
03_BUILD_METHODOLOGY/_workflows/FFM_CREATION.md:28: 
03_BUILD_METHODOLOGY/_workflows/FFM_CREATION.md:29: Boot/resume through the module’s declared entry file: Engineering routes to its released implementation assignment; QA routes to `QAM/` as QA Executor. Read-only Git inspection and declared reporting writes are permitted; Tony performs all Git mutations. Requirements/acceptance freeze while declared handoff and QA evidence lanes remain writable. Preserve actual candidate, test-plan, repair/retest, cleanup and closeout identities; never prefill a verdict or planned commit SHA. Deployment additionally requires verified exclusion from build inputs and the actual artifact; a folder name is insufficient. Existing modules in flight keep their recorded sequence unless explicitly amended.
03_BUILD_METHODOLOGY/_workflows/FFM_CREATION.md:30: 
03_BUILD_METHODOLOGY/_workflows/FFM_CREATION.md:31: ## Version History
03_BUILD_METHODOLOGY/_workflows/FFM_CREATION.md:32: 
03_BUILD_METHODOLOGY/_workflows/FFM_CREATION.md:33: | Version | Date | Change | Authority |
03_BUILD_METHODOLOGY/_workflows/FFM_CREATION.md:34: |---|---|---|---|
03_BUILD_METHODOLOGY/_workflows/FFM_CREATION.md:35: | 1.0 | 2026-10-18 | Revised workflow and stick diagram; original retained; review checkpoints and seat boundaries reconciled | MC-06; W01–W23; RUL-01–RUL-15; Tony 2026-10-16 correction assignment |

```

```text

03_BUILD_METHODOLOGY/_workflows/FFM_DEPLOYMENT.md:1: # Deployment, identity and independent Gate D
03_BUILD_METHODOLOGY/_workflows/FFM_DEPLOYMENT.md:2: 
03_BUILD_METHODOLOGY/_workflows/FFM_DEPLOYMENT.md:3: > **Version:** 1.0 · **Date:** 2026-10-18 · **Status:** Proposed — pending verified publication
03_BUILD_METHODOLOGY/_workflows/FFM_DEPLOYMENT.md:4: > **Governed by:** `DEPLOYMENT_PLAYBOOK.md`, `SOFTWARE_FACTORY_PLAYBOOK.md` §2, `RRM_PLAYBOOK.md` §2, `QAM_PLAYBOOK.md`, `DEPLOYMENT_PLAYBOOK.md`.
03_BUILD_METHODOLOGY/_workflows/FFM_DEPLOYMENT.md:5: 
03_BUILD_METHODOLOGY/_workflows/FFM_DEPLOYMENT.md:6: This revised workflow supersedes the August diagram `SRC-W03_FFM_DEPLOYMENT.png` for current instructions when this proposed sync is approved, landed and verified. The [unaltered original](../../_AUDIT/SYNC_2026-10-15_doctrine-part2/INTAKE_SNAPSHOT/factory-intake/SOURCES/Workflow/SRC-W03_FFM_DEPLOYMENT.png) remains historical evidence; it grants no current role, Git or cloud permission. This derivative follows RUL-01…15 and Tony’s explicit workflow/diagram correction assignment of 2026-10-16.
03_BUILD_METHODOLOGY/_workflows/FFM_DEPLOYMENT.md:7: 
03_BUILD_METHODOLOGY/_workflows/FFM_DEPLOYMENT.md:8: ![Revised stick-actor workflow](../_assets/workflows/FFM_DEPLOYMENT.svg)
03_BUILD_METHODOLOGY/_workflows/FFM_DEPLOYMENT.md:9: 
03_BUILD_METHODOLOGY/_workflows/FFM_DEPLOYMENT.md:10: ## Sequence
03_BUILD_METHODOLOGY/_workflows/FFM_DEPLOYMENT.md:11: 
03_BUILD_METHODOLOGY/_workflows/FFM_DEPLOYMENT.md:12: 1. **Architect:** Declare target, permissions, exclusion and recovery.
03_BUILD_METHODOLOGY/_workflows/FFM_DEPLOYMENT.md:13: 2. **QA Lead:** Required product QA verdict remains distinct.
03_BUILD_METHODOLOGY/_workflows/FFM_DEPLOYMENT.md:14: 3. **Director:** Release the verified candidate for deployment.
03_BUILD_METHODOLOGY/_workflows/FFM_DEPLOYMENT.md:15: 4. **Authorized operator:** Deploy within existing context-specific permissions.
03_BUILD_METHODOLOGY/_workflows/FFM_DEPLOYMENT.md:16: 5. **QA Executor:** Verify deployed identity, exclusions and behavior at Gate D.
03_BUILD_METHODOLOGY/_workflows/FFM_DEPLOYMENT.md:17: 6. **QA Lead:** Issue deployed-environment verdict.
03_BUILD_METHODOLOGY/_workflows/FFM_DEPLOYMENT.md:18: 7. **Director:** Release decision or authorized recovery.
03_BUILD_METHODOLOGY/_workflows/FFM_DEPLOYMENT.md:19: 8. **Architect:** Record follow-ups; release is separate from review.
03_BUILD_METHODOLOGY/_workflows/FFM_DEPLOYMENT.md:20: 
03_BUILD_METHODOLOGY/_workflows/FFM_DEPLOYMENT.md:21: ## Review and release checkpoints
03_BUILD_METHODOLOGY/_workflows/FFM_DEPLOYMENT.md:22: 
03_BUILD_METHODOLOGY/_workflows/FFM_DEPLOYMENT.md:23: - Review checkpoint 1: after FFM build and its independent QA finish.
03_BUILD_METHODOLOGY/_workflows/FFM_DEPLOYMENT.md:24: - Review checkpoint 2: Engine 2 independent system review after all Engine 1 phases/modules and their QA are closed.
03_BUILD_METHODOLOGY/_workflows/FFM_DEPLOYMENT.md:25: - At either checkpoint, disposition findings; RRM only for approved findings requiring repairs. A clean review requires no RRM.
03_BUILD_METHODOLOGY/_workflows/FFM_DEPLOYMENT.md:26: - Review, Gate Q, required cleanup and certification, Gate D and Director release remain separate responsibilities.
03_BUILD_METHODOLOGY/_workflows/FFM_DEPLOYMENT.md:27: 
03_BUILD_METHODOLOGY/_workflows/FFM_DEPLOYMENT.md:28: ## Entry, handoff and evidence
03_BUILD_METHODOLOGY/_workflows/FFM_DEPLOYMENT.md:29: 
03_BUILD_METHODOLOGY/_workflows/FFM_DEPLOYMENT.md:30: Boot/resume through the module’s declared entry file: Engineering routes to its released implementation assignment; QA routes to `QAM/` as QA Executor. Read-only Git inspection and declared reporting writes are permitted; Tony performs all Git mutations. Requirements/acceptance freeze while declared handoff and QA evidence lanes remain writable. Preserve actual candidate, test-plan, repair/retest, cleanup and closeout identities; never prefill a verdict or planned commit SHA. Deployment additionally requires verified exclusion from build inputs and the actual artifact; a folder name is insufficient. Existing modules in flight keep their recorded sequence unless explicitly amended.
03_BUILD_METHODOLOGY/_workflows/FFM_DEPLOYMENT.md:31: 
03_BUILD_METHODOLOGY/_workflows/FFM_DEPLOYMENT.md:32: ## Version History
03_BUILD_METHODOLOGY/_workflows/FFM_DEPLOYMENT.md:33: 
03_BUILD_METHODOLOGY/_workflows/FFM_DEPLOYMENT.md:34: | Version | Date | Change | Authority |
03_BUILD_METHODOLOGY/_workflows/FFM_DEPLOYMENT.md:35: |---|---|---|---|
03_BUILD_METHODOLOGY/_workflows/FFM_DEPLOYMENT.md:36: | 1.0 | 2026-10-18 | Revised workflow and stick diagram; original retained; review checkpoints and seat boundaries reconciled | MC-06; W01–W23; RUL-01–RUL-15; Tony 2026-10-16 correction assignment |

```

```text

03_BUILD_METHODOLOGY/_workflows/FFM_EXECUTION.md:1: # FFM engineering, independent QA and post-FFM review
03_BUILD_METHODOLOGY/_workflows/FFM_EXECUTION.md:2: 
03_BUILD_METHODOLOGY/_workflows/FFM_EXECUTION.md:3: > **Version:** 1.0 · **Date:** 2026-10-18 · **Status:** Proposed — pending verified publication
03_BUILD_METHODOLOGY/_workflows/FFM_EXECUTION.md:4: > **Governed by:** `FFM_PLAYBOOK.md`, `SOFTWARE_FACTORY_PLAYBOOK.md` §2, `RRM_PLAYBOOK.md` §2, `QAM_PLAYBOOK.md`, `DEPLOYMENT_PLAYBOOK.md`.
03_BUILD_METHODOLOGY/_workflows/FFM_EXECUTION.md:5: 
03_BUILD_METHODOLOGY/_workflows/FFM_EXECUTION.md:6: This revised workflow supersedes the August diagram `SRC-W02_FFM_EXECUTION.png` for current instructions when this proposed sync is approved, landed and verified. The [unaltered original](../../_AUDIT/SYNC_2026-10-15_doctrine-part2/INTAKE_SNAPSHOT/factory-intake/SOURCES/Workflow/SRC-W02_FFM_EXECUTION.png) remains historical evidence; it grants no current role, Git or cloud permission. This derivative follows RUL-01…15 and Tony’s explicit workflow/diagram correction assignment of 2026-10-16.
03_BUILD_METHODOLOGY/_workflows/FFM_EXECUTION.md:7: 
03_BUILD_METHODOLOGY/_workflows/FFM_EXECUTION.md:8: ![Revised stick-actor workflow](../_assets/workflows/FFM_EXECUTION.svg)
03_BUILD_METHODOLOGY/_workflows/FFM_EXECUTION.md:9: 
03_BUILD_METHODOLOGY/_workflows/FFM_EXECUTION.md:10: ## Sequence
03_BUILD_METHODOLOGY/_workflows/FFM_EXECUTION.md:11: 
03_BUILD_METHODOLOGY/_workflows/FFM_EXECUTION.md:12: 1. **Engineer:** Build and self-check; factual QAM handoff.
03_BUILD_METHODOLOGY/_workflows/FFM_EXECUTION.md:13: 2. **Director:** Commit/push numbered engineering candidate.
03_BUILD_METHODOLOGY/_workflows/FFM_EXECUTION.md:14: 3. **Director:** QA branch at exact candidate commit.
03_BUILD_METHODOLOGY/_workflows/FFM_EXECUTION.md:15: 4. **QA Executor:** Q1 recon and independent test plan.
03_BUILD_METHODOLOGY/_workflows/FFM_EXECUTION.md:16: 5. **QA Lead:** Approve the specific QA plan.
03_BUILD_METHODOLOGY/_workflows/FFM_EXECUTION.md:17: 6. **Director:** Release Q2 execution.
03_BUILD_METHODOLOGY/_workflows/FFM_EXECUTION.md:18: 7. **QA Executor:** Q2 tests and evidence.
03_BUILD_METHODOLOGY/_workflows/FFM_EXECUTION.md:19: 8. **Engineer:** Conditional authorized repair on same QA branch.
03_BUILD_METHODOLOGY/_workflows/FFM_EXECUTION.md:20: 9. **Director:** Commit repaired candidate on the continuing QA branch.
03_BUILD_METHODOLOGY/_workflows/FFM_EXECUTION.md:21: 10. **QA Executor:** Independent retest of repair and regression.
03_BUILD_METHODOLOGY/_workflows/FFM_EXECUTION.md:22: 11. **QA Lead:** Product certification; approve cleanup retention.
03_BUILD_METHODOLOGY/_workflows/FFM_EXECUTION.md:23: 12. **QA Executor:** Authorized cleanup; retain durable evidence.
03_BUILD_METHODOLOGY/_workflows/FFM_EXECUTION.md:24: 13. **QA Lead:** Accept cleanup; preserve product verdict identity.
03_BUILD_METHODOLOGY/_workflows/FFM_EXECUTION.md:25: 14. **Architect:** Closeout instruction.
03_BUILD_METHODOLOGY/_workflows/FFM_EXECUTION.md:26: 15. **Engineer:** Bounded closeout.
03_BUILD_METHODOLOGY/_workflows/FFM_EXECUTION.md:27: 16. **Director:** Final commits, merge and push.
03_BUILD_METHODOLOGY/_workflows/FFM_EXECUTION.md:28: 17. **Reviewers:** Review checkpoint 1 after FFM build and independent QA.
03_BUILD_METHODOLOGY/_workflows/FFM_EXECUTION.md:29: 18. **Director:** Disposition review findings; RRM only for approved repairs.
03_BUILD_METHODOLOGY/_workflows/FFM_EXECUTION.md:30: 
03_BUILD_METHODOLOGY/_workflows/FFM_EXECUTION.md:31: ## Review and release checkpoints
03_BUILD_METHODOLOGY/_workflows/FFM_EXECUTION.md:32: 
03_BUILD_METHODOLOGY/_workflows/FFM_EXECUTION.md:33: - Review checkpoint 1: after FFM build and its independent QA finish.
03_BUILD_METHODOLOGY/_workflows/FFM_EXECUTION.md:34: - Review checkpoint 2: Engine 2 independent system review after all Engine 1 phases/modules and their QA are closed.
03_BUILD_METHODOLOGY/_workflows/FFM_EXECUTION.md:35: - At either checkpoint, disposition findings; RRM only for approved findings requiring repairs. A clean review requires no RRM.
03_BUILD_METHODOLOGY/_workflows/FFM_EXECUTION.md:36: - Review, Gate Q, required cleanup and certification, Gate D and Director release remain separate responsibilities.
03_BUILD_METHODOLOGY/_workflows/FFM_EXECUTION.md:37: 
03_BUILD_METHODOLOGY/_workflows/FFM_EXECUTION.md:38: ## Entry, handoff and evidence
03_BUILD_METHODOLOGY/_workflows/FFM_EXECUTION.md:39: 
03_BUILD_METHODOLOGY/_workflows/FFM_EXECUTION.md:40: Boot/resume through the module’s declared entry file: Engineering routes to its released implementation assignment; QA routes to `QAM/` as QA Executor. Read-only Git inspection and declared reporting writes are permitted; Tony performs all Git mutations. Requirements/acceptance freeze while declared handoff and QA evidence lanes remain writable. Preserve actual candidate, test-plan, repair/retest, cleanup and closeout identities; never prefill a verdict or planned commit SHA. Deployment additionally requires verified exclusion from build inputs and the actual artifact; a folder name is insufficient. Existing modules in flight keep their recorded sequence unless explicitly amended.
03_BUILD_METHODOLOGY/_workflows/FFM_EXECUTION.md:41: 
03_BUILD_METHODOLOGY/_workflows/FFM_EXECUTION.md:42: ## Version History
03_BUILD_METHODOLOGY/_workflows/FFM_EXECUTION.md:43: 
03_BUILD_METHODOLOGY/_workflows/FFM_EXECUTION.md:44: | Version | Date | Change | Authority |
03_BUILD_METHODOLOGY/_workflows/FFM_EXECUTION.md:45: |---|---|---|---|
03_BUILD_METHODOLOGY/_workflows/FFM_EXECUTION.md:46: | 1.0 | 2026-10-18 | Revised workflow and stick diagram; original retained; review checkpoints and seat boundaries reconciled | MC-06; W01–W23; RUL-01–RUL-15; Tony 2026-10-16 correction assignment |

```

## Withdrawal row judgments (31)

Each row was checked against its mapped edits and remaining identifier/code hits. PASS here means containment for this row only, not underlying replacement closure. Full mapped quotations: RAW/withdrawal_judgment_packet.txt; complete changed context: RAW/read_withdrawals.txt; remaining code: RAW/ac16_code_hits.txt and RAW/ac16_remaining_query_hits.txt.

| ID | Judgment | Candidate quotation and evidence |

|---|---|---|

| FC-001 | PASS — replacement remains open | 01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md:625: For kit-based builds, consume the existing kit authentication and authorization primitives and verify them through AUTH-WALK. Do not rebuild login pages, an auth store, metadata role flags or a client route guard. Page wrappers follow STARTER_KIT_HANDBOOK §5 and §7: resolve authorized server data before rendering the interactive client child. Generic non-kit examples do not apply when the kit supplies the capability. |

| FC-022 | FAIL — F04 | 03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:881: **Executable example withdrawn.** The previous example is not an approved implementation. The outgoing archived document preserves it as history. Replacement code requires the project’s approved contract, verified dependency interfaces and behavioral evidence. This withdrawal contains the misleading recipe; it does not certify the underlying finding resolved. |

| FC-030 | PASS — replacement remains open | 03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:1260: Fixture discovery returns one normalized record with role identities, scenario eligibility and a single count field named count. Validate role existence and coupon prerequisites before declaring readiness. A missing required role produces BLOCKED with the missing prerequisite; optional absence is recorded explicitly. Producers and consumers read count, not competing count aliases. |

| FC-033 | PASS — replacement remains open | 04_REFERENCE_MANUALS/AUTH_MANUAL.md:1309: The role table is the only authorization authority. Never authorize from user_metadata or a profile mirror. Superadmin creation is console-only; no app-side superadmin creation route is provided. Retire the metadata-authorized add-user, delete-user and get-users recipes. Future privileged list/delete operations remain possible only with trusted current-role lookup, operation-local authorization before elevated capability, an approved target-role allowlist and privileged-target protection. Profile mirrors contain profile data, not authorization columns. Registration metadata is not authorization. |

| FC-034 | PASS — replacement remains open | 04_REFERENCE_MANUALS/AUTH_MANUAL.md:396: At the trusted public-signup boundary, allow only approved profile fields and force the member role independently of submitted metadata. The provider-side creation path must also ignore or reject public role keys, so direct provider signup cannot bypass the endpoint. Privileged role assignment uses a separately authorized protected channel. Trigger hardening and a negative direct-provider test are required before promotion: role=admin submitted publicly must not produce an admin. |

| FC-035 | PASS — replacement remains open | 04_REFERENCE_MANUALS/AUTH_MANUAL.md:561: Server guards control page access; server-resolved { user, role } props establish first-render identity. Retire client HOC route protection and post-mount identity fetching as authoritative patterns. Zustand handles interaction and session-event reactions, with no persisted authorization authority. Display helpers are display-only and use explicit role sets; they never authorize an operation. |

| FC-038 | FAIL — F04 | 04_REFERENCE_MANUALS/AUTH_MANUAL.md:1309: The role table is the only authorization authority. Never authorize from user_metadata or a profile mirror. Superadmin creation is console-only; no app-side superadmin creation route is provided. Retire the metadata-authorized add-user, delete-user and get-users recipes. Future privileged list/delete operations remain possible only with trusted current-role lookup, operation-local authorization before elevated capability, an approved target-role allowlist and privileged-target protection. Profile mirrors contain profile data, not authorization columns. Registration metadata is not authorization. |

| FC-039 | PASS — replacement remains open | 04_REFERENCE_MANUALS/AUTH_MANUAL.md:1309: The role table is the only authorization authority. Never authorize from user_metadata or a profile mirror. Superadmin creation is console-only; no app-side superadmin creation route is provided. Retire the metadata-authorized add-user, delete-user and get-users recipes. Future privileged list/delete operations remain possible only with trusted current-role lookup, operation-local authorization before elevated capability, an approved target-role allowlist and privileged-target protection. Profile mirrors contain profile data, not authorization columns. Registration metadata is not authorization. |

| FC-041 | PASS — replacement remains open | 04_REFERENCE_MANUALS/APP_ARCHITECTURE_MANUAL.md:1013: The role table is the only authorization authority. Never authorize from user_metadata or a profile mirror. Superadmin creation is console-only; no app-side superadmin creation route is provided. Retire the metadata-authorized add-user, delete-user and get-users recipes. Future privileged list/delete operations remain possible only with trusted current-role lookup, operation-local authorization before elevated capability, an approved target-role allowlist and privileged-target protection. Profile mirrors contain profile data, not authorization columns. Registration metadata is not authorization. |

| FC-042 | PASS — replacement remains open | 04_REFERENCE_MANUALS/APP_ARCHITECTURE_MANUAL.md:1058: Session-cookie attributes must follow the verified pinned kit’s session architecture. HTTPS and Secure transport remain required in production; do not impose an unverified HttpOnly architecture on a browser-client session model. Record the verification gap rather than guessing compatible options. |

| FC-045 | PASS — replacement remains open | 04_REFERENCE_MANUALS/DATABASE_MANUAL.md:1038: // Cursor recipe withdrawn: a timestamp alone skips rows sharing that value. |

| FC-047 | PASS — replacement remains open | 04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:783: Do not persist raw contact details by default. Any approved personal-data persistence declares permitted fields, retention duration and user or guest scope. Sign-out and account transition reset and invalidate every affected store even when remote logout fails; a new account must not hydrate the previous account’s data. Payment and authorization state remain outside persistence. Storage readiness is separate from business-data reset. |

| FC-050 | PASS — replacement remains open | 04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:185: The browser may display or poll payment status; it may not choose paid or processing state. A payment-derived transition requires verified server-side evidence bound to the stored order and payment attempt, including amount and currency. Non-webhook mutations authenticate and authorize the operation and target, including an explicitly approved guest capability where supported, then validate the state transition. |

| FC-051 | PASS — replacement remains open | 04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:185: The browser may display or poll payment status; it may not choose paid or processing state. A payment-derived transition requires verified server-side evidence bound to the stored order and payment attempt, including amount and currency. Non-webhook mutations authenticate and authorize the operation and target, including an explicitly approved guest capability where supported, then validate the state transition. |

| FC-052 | PASS — replacement remains open | 04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:364: Converge each order or subscription aggregate using authoritative provider retrieval or explicit freshness and legal-transition rules. Reject stale transitions; check zero-row updates and repair missing mappings. A late event for an old subscription may not overwrite its replacement. Define reconciliation of the local mirror independently of inbound deduplication. |

| FC-053 | PASS — replacement remains open | 04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:185: The browser may display or poll payment status; it may not choose paid or processing state. A payment-derived transition requires verified server-side evidence bound to the stored order and payment attempt, including amount and currency. Non-webhook mutations authenticate and authorize the operation and target, including an explicitly approved guest capability where supported, then validate the state transition. |

| FC-054 | PASS — replacement remains open | 04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:364: Converge each order or subscription aggregate using authoritative provider retrieval or explicit freshness and legal-transition rules. Reject stale transitions; check zero-row updates and repair missing mappings. A late event for an old subscription may not overwrite its replacement. Define reconciliation of the local mirror independently of inbound deduplication. |

| FC-055 | PASS — replacement remains open | 04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:177: Subscription bootstrap, customer identity and resubscription must agree with the project’s approved schema. Universal subscription-schema design is deferred; no runnable replacement is supplied here. Preserve owner-only reads and server-only subscription writes. Keep this finding open until the project contract and recovery behavior are verified. |

| FC-056 | PASS — replacement remains open | 04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:1029: Use the provider’s stable event ID, never a random fallback. Atomically claim each event with in-progress, completed and retryable states; inspect persistence results. Make effects idempotent or transactional. A bounded lease/recovery process reclaims abandoned work and reconciles partial external success without duplicating completed effects. |

| FC-057 | PASS — replacement remains open | 04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:170: **Executable example withdrawn.** The previous example is not an approved implementation. The outgoing archived document preserves it as history. Replacement code requires the project’s approved contract, verified dependency interfaces and behavioral evidence. This withdrawal contains the misleading recipe; it does not certify the underlying finding resolved. |

| FC-058 | PASS — replacement remains open | 04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:999: Capture the raw request body once. Select exactly one provider-specific signature scheme with its documented header and encoding, verify before parsing, and reject missing or invalid headers. Do not sign reconstructed JSON or chain alternative schemes as cumulative requirements. Test signed whitespace-bearing bodies and malformed or absent signatures. |

| FC-059 | PASS — replacement remains open | 04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:364: Converge each order or subscription aggregate using authoritative provider retrieval or explicit freshness and legal-transition rules. Reject stale transitions; check zero-row updates and repair missing mappings. A late event for an old subscription may not overwrite its replacement. Define reconciliation of the local mirror independently of inbound deduplication. |

| FC-060 | PASS — replacement remains open | 04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:185: The browser may display or poll payment status; it may not choose paid or processing state. A payment-derived transition requires verified server-side evidence bound to the stored order and payment attempt, including amount and currency. Non-webhook mutations authenticate and authorize the operation and target, including an explicitly approved guest capability where supported, then validate the state transition. |

| FC-062 | PASS — replacement remains open | 04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:364: Converge each order or subscription aggregate using authoritative provider retrieval or explicit freshness and legal-transition rules. Reject stale transitions; check zero-row updates and repair missing mappings. A late event for an old subscription may not overwrite its replacement. Define reconciliation of the local mirror independently of inbound deduplication. |

| FC-064 | PASS — replacement remains open | 04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:172: Services return an explicit typed outcome: success, not-found, unavailable, invalid or forbidden. Routes map it to the approved HTTP/UI behavior with generic client messages and no upstream error text. Do not cache failures as successful public data. Degrade or fail closed according to the module’s approved failure policy; an unavailable entitlement read is not confirmed absence. |

| FC-066 | FAIL — F04 | 04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:172: Services return an explicit typed outcome: success, not-found, unavailable, invalid or forbidden. Routes map it to the approved HTTP/UI behavior with generic client messages and no upstream error text. Do not cache failures as successful public data. Degrade or fail closed according to the module’s approved failure policy; an unavailable entitlement read is not confirmed absence. |

| FC-067 | PASS — replacement remains open | 04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:346: A fixed-product coupon uses validated eligible line items and quantities in the authoritative server pricing operation. Do not advertise fixed_product through a flat-cart subtotal branch. A client calculation is a display estimate only. Verify equal-subtotal carts with different eligible quantities; preserve valid fixed-cart and percentage behavior. |

| FC-068 | PASS — replacement remains open | 04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:187: Accept product/variation identifiers, quantities, shipping selection and coupon code, never caller prices, shipping costs or discount amounts. Validate quantities and product eligibility; load authoritative catalog prices; validate the shipping selection and coupon eligibility; apply the declared tax policy; calculate currency-safe totals on the server. Bind the payment to the authorized order and verify payment identity, amount, currency and order association before marking paid. Client totals are display-only. Return generic failures and redact logs. Universal quote-storage design is deferred; the required server pricing and payment binding still apply. |

| FC-071 | PASS — replacement remains open | 05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:472: The former copyable layout is withdrawn because it hid navigation on small screens or bypassed the installed shell. Use the verified responsive shell/rail/drawer contract for the pinned kit; do not invent a breakpoint or duplicate the shell. Verify reachable navigation, focus management, keyboard/escape behavior and no page overflow at every supported width. |

| FC-072 | PASS — replacement remains open | 05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:472: The former copyable layout is withdrawn because it hid navigation on small screens or bypassed the installed shell. Use the verified responsive shell/rail/drawer contract for the pinned kit; do not invent a breakpoint or duplicate the shell. Verify reachable navigation, focus management, keyboard/escape behavior and no page overflow at every supported width. |

| FC-076 | PASS — replacement remains open | 05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1375: Consume the kit Button, including its verified variants, sizes and asChild composition. Do not replace it with this shortened implementation. An educational internal excerpt must be source-matched and labeled as an excerpt, not installation code. Preserve Link composition through the kit API. |

## Domain preservation excerpts

```json

[
  {
    "family": "roles",
    "path": "04_REFERENCE_MANUALS/DATABASE_MANUAL.md",
    "start": 140,
    "end": 156,
    "quote": "Authorization roles live in a dedicated **`user_roles`** table \u2014 never in `user_metadata`, never as a column on a profile mirror.\n\n```sql\n-- PATTERN SQL \u2014 the kit's supabase/setup.sql is the ground truth.\n-- Verify on disk before building (recon Q5.2/Q5.3); do not treat this as a kit copy.\n\n-- Roles: one row per user, the single source of truth for authorization\nCREATE TABLE user_roles (\n  user_id UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,\n  role TEXT NOT NULL DEFAULT 'member',\n  created_at TIMESTAMPTZ DEFAULT NOW()\n);\n```\n\nRoles must resolve from an authoritative server-side store. Creation and mutation require verified per-call authorization and a role input that untrusted signup cannot control. The historical Mark IV transport is not a verified safe recipe for the current kit; obtain pinned trigger and caller evidence before implementation.\n\n> \u26d4 **FORBIDDEN:** never store \u2014 or READ \u2014 roles for authorization from `user_metadata` (the recon Q3.4 smell), and never mirror a `role` column onto a profile table. Two homes for a role guarantees privilege drift. This aligns with AUTH_MANUAL (\"Where Roles Live\").",
    "byte_equal_span_in_base": false
  },
  {
    "family": "RLS ownership and explicit public access",
    "path": "04_REFERENCE_MANUALS/DATABASE_MANUAL.md",
    "start": 362,
    "end": 415,
    "quote": "ALTER TABLE user_profiles ENABLE ROW LEVEL SECURITY;\n```\n\n### Common RLS Policies\n\n#### Users See Only Their Own Data\n\n```sql\nCREATE POLICY \"Users see own records\"\nON orders FOR SELECT\nUSING (auth.uid() = user_id);\n\nCREATE POLICY \"Users insert own records\"\nON orders FOR INSERT\nWITH CHECK (auth.uid() = user_id);\n\nCREATE POLICY \"Users update own records\"\nON orders FOR UPDATE\nUSING (auth.uid() = user_id);\n\nCREATE POLICY \"Users delete own records\"\nON orders FOR DELETE\nUSING (auth.uid() = user_id);\n```\n\n#### Role-Based Access\n\n```sql\n-- Admins can see all records \u2014 roles resolve from the user_roles table (THE pattern)\nCREATE POLICY \"Admins see all\"\nON orders FOR SELECT\nUSING (\n  EXISTS (\n    SELECT 1 FROM user_roles\n    WHERE user_id = auth.uid()\n    AND role = 'admin'\n  )\n);\n```\n\n> \u26d4 **Do NOT write policies that read roles from `raw_user_meta_data`** (e.g. `raw_user_meta_data->>'is_admin'`) \u2014 that is an authorization read from user metadata, the recon Q3.4 smell (F-041). A prior edition of this manual showed that variant as a peer option; it is not one. Roles resolve from `user_roles` \u2014 everywhere, including inside RLS.\n\n#### Public Read, Authenticated Write\n\n```sql\n-- Anyone can read\nCREATE POLICY \"Public read\"\nON products FOR SELECT\nUSING (true);\n\n-- Only authenticated users can insert\nCREATE POLICY \"Authenticated insert\"\nON products FOR INSERT\nWITH CHECK (auth.uid() IS NOT NULL);",
    "byte_equal_span_in_base": true
  },
  {
    "family": "schema first",
    "path": "04_REFERENCE_MANUALS/DATABASE_MANUAL.md",
    "start": 35,
    "end": 41,
    "quote": "1. Design the tables\n2. Define relationships\n3. Set up indexes\n4. Generate TypeScript types\n5. THEN build service layer and UI\n\n> **When Schema-First Applies:** schema-first is the law for **backend phases and conversions** (the data shape is known or extracted). For **discovery builds the factory runs frontend-first**: UI against a mock DATA_CONTRACT first, schema authored at the backend transition \u2014 see `FRONTEND_FIRST_PLAYBOOK.md` \u00a72 (when frontend-first is allowed) and \u00a78 (the transition point). Both orders are legitimate; the pipeline you're in decides.",
    "byte_equal_span_in_base": true
  },
  {
    "family": "Navbar invariant",
    "path": "04_REFERENCE_MANUALS/AUTH_MANUAL.md",
    "start": 636,
    "end": 644,
    "quote": "\n1. Route guards return what they resolve (`{ user, role }`) \u2014 never compute-and-discard.\n2. Client stores (Zustand) may REACT to session events (`onAuthStateChange` sign-out)\n   and own interaction state \u2014 they are never the SOURCE of identity for rendering.\n   (See STATE_MANAGEMENT_MANUAL \u00a71 \u2014 Division of Labor.)\n3. Persisted client role state goes stale by design (written at login, survives in\n   localStorage). Any consumer treating it as truth inherits the race. (KIP-2.)\n4. Invariant-test the guarantee: an authed shell component must render its full\n   role-appropriate link set on FIRST render, synchronously (see Navbar.invariant).",
    "byte_equal_span_in_base": true
  },
  {
    "family": "state labor",
    "path": "04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md",
    "start": 86,
    "end": 112,
    "quote": "interface CounterStore {\n  count: number;\n  increment: () => void;\n  decrement: () => void;\n}\n\nexport const useCounterStore = create<CounterStore>((set) => ({\n  count: 0,\n  increment: () => set((state) => ({ count: state.count + 1 })),\n  decrement: () => set((state) => ({ count: state.count - 1 })),\n}));\n```\n\n### Division of Labor: Server Props vs. Client Stores (HARD RULE)\n\n**The server tells the UI who you are; the store helps the UI react to what you do.**\n\n| Concern | Source | Why |\n|---|---|---|\n| Identity & role for RENDERING (nav links, role-gated UI, portal chrome) | Server-resolved by the route guard, passed as props | No client fetch window \u2192 no race, no empty state, no dev/deploy divergence. Re-verified server-side on every navigation. |\n| Session EVENT reactions (sign-out in another tab), interaction state, UI state, in-memory domain state | Client store (Zustand) | Lives and changes in the browser during use \u2014 that is what a client store is for. |\n\nPersisted auth state (e.g. a `role` written only at login into localStorage) is a\nSNAPSHOT, not truth: it goes stale across browsers/devices/cleared storage. Rendering\nfrom it produces \"random\" partial-UI bugs that dev latency hides (see AUTH_MANUAL \u2014\nThe Navbar Law; origin: 2026-08-04 staging nav bug).\n",
    "byte_equal_span_in_base": true
  },
  {
    "family": "selective persistence",
    "path": "04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md",
    "start": 501,
    "end": 501,
    "quote": "**Never persist everything.** Use `partialize` to select only UX-critical state:",
    "byte_equal_span_in_base": true
  },
  {
    "family": "AUTH-WALK/live DB",
    "path": "01_CONSTITUTION/STARTER_KIT_HANDBOOK.md",
    "start": 508,
    "end": 508,
    "quote": "> A passing triad is necessary, not sufficient. Cookie/session/RBAC changes also need the operator AUTH-WALK; DB changes need live verification against the Supabase instance.",
    "byte_equal_span_in_base": true
  },
  {
    "family": "money versus permission",
    "path": "04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md",
    "start": 38,
    "end": 56,
    "quote": "\n**Stripe owns the truth about money.** Whether a subscription is active, what was charged, when the next renewal is \u2014 Stripe is always the authoritative source.\n\n**Supabase owns the cache.** Your app reads subscription state from Supabase for speed and convenience. This is a local mirror, not a source of truth.\n\n**Webhooks keep them in sync.** Stripe sends events to your webhook endpoint whenever subscription state changes. Your webhook handler writes those changes to Supabase. One-way street: Stripe speaks, Supabase listens.\n\n### The Two Systems That Must Stay Separate\n\n**RBAC (Role-Based Access Control)** answers: \"Who are you structurally?\" \u2014 superadmin, admin, member. This is about identity and permission within the app.\n\n**Subscriptions** answer: \"What have you paid for?\" \u2014 free, starter, pro, enterprise. This is about commercial state.\n\nThese are orthogonal. They cross at right angles. Never implement subscription tiers as roles. A superadmin with no subscription still has full admin power. A member with an Enterprise subscription gets premium content but can't touch admin routes.\n\n**Gate helpers compose, they never replace each other:**\n- `requireUser()` \u2014 checks login only\n- `requireRole(role)` \u2014 checks structural permission\n- `requireSubscriptionTier(tier)` \u2014 checks commercial state",
    "byte_equal_span_in_base": true
  },
  {
    "family": "raw-body signature",
    "path": "04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md",
    "start": 374,
    "end": 390,
    "quote": "**Always verify webhook signatures.** This prevents attackers from sending fake events.\n\n```typescript\n// The signature verification happens in constructEvent()\n// It uses your STRIPE_WEBHOOK_SECRET to verify the request came from Stripe\n\ntry {\n  event = stripe.webhooks.constructEvent(\n    body,           // Raw request body (must be string, not parsed JSON)\n    signature,      // stripe-signature header\n    webhookSecret   // Your webhook secret from Stripe Dashboard\n  );\n} catch (err) {\n  // Invalid signature - reject the request\n  return NextResponse.json({ error: 'Invalid signature' }, { status: 400 });\n}\n```",
    "byte_equal_span_in_base": true
  },
  {
    "family": "private data uncached",
    "path": "04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md",
    "start": 352,
    "end": 355,
    "quote": "// User-specific data (cart, orders)\nheaders: {\n  'Cache-Control': 'private, no-cache, no-store, must-revalidate',\n}",
    "byte_equal_span_in_base": true
  },
  {
    "family": "server secrets",
    "path": "04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md",
    "start": 396,
    "end": 400,
    "quote": "// Server-only credentials (never import in client components)\nexport const getServerCredentials = () => {\n  if (typeof window !== 'undefined') {\n    throw new Error('Server credentials accessed on client!');\n  }",
    "byte_equal_span_in_base": true
  },
  {
    "family": "wire/UI types",
    "path": "04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md",
    "start": 570,
    "end": 574,
    "quote": "### Wire-Format Conventions (Factory Standard)\n\n- **Wire shapes are `snake_case`** (matches FastAPI/Pydantic and most REST payloads \u2014 e.g. `regular_price`, `stock_status`).\n- **UI-internal types are `camelCase`** (e.g. `regularPrice`, `inStock`).\n- **The service layer owns the translation** \u2014 the normalize functions below are where the case boundary lives. UI code never sees wire casing; wire payloads never see UI casing.",
    "byte_equal_span_in_base": true
  }
]

```

## Historical container evidence

```json

[
  {
    "path": "01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md",
    "line": 62,
    "quote": "| `HANDOFF_PACKAGE_PLAYBOOK.md` | Historical external example (availability unverified): `agent_docs/CURRENT_APP/app-factory-frontend-first-module/_project/`. Obtain the source repository, immutable revision and path before use; do not assume this path exists locally. |",
    "containers": [
      {
        "type": "table_open",
        "map": [
          59,
          67
        ],
        "content": ""
      },
      {
        "type": "tr_open",
        "map": [
          61,
          62
        ],
        "content": ""
      },
      {
        "type": "inline",
        "map": [
          61,
          62
        ],
        "content": "`HANDOFF_PACKAGE_PLAYBOOK.md`"
      },
      {
        "type": "inline",
        "map": [
          61,
          62
        ],
        "content": "Historical external example (availability unverified): `agent_docs/CURRENT_APP/app-factory-frontend-first-module/_project/`. Obtain the source repository, immutable revision and path before use; do not assume this path exists locally."
      }
    ]
  },
  {
    "path": "01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md",
    "line": 118,
    "quote": "- Historical external example (availability unverified): **`CURRENT_APP/app-factory-frontend-first-module/_project/`** \u2014 the inaugural historical worked example Obtain the source repository, immutable revision and path before use; do not assume this path exists locally.",
    "containers": [
      {
        "type": "list_item_open",
        "map": [
          117,
          119
        ],
        "content": ""
      },
      {
        "type": "paragraph_open",
        "map": [
          117,
          118
        ],
        "content": ""
      },
      {
        "type": "inline",
        "map": [
          117,
          118
        ],
        "content": "Historical external example (availability unverified): **`CURRENT_APP/app-factory-frontend-first-module/_project/`** \u2014 the inaugural historical worked example Obtain the source repository, immutable revision and path before use; do not assume this path exists locally."
      }
    ]
  },
  {
    "path": "02_PIPELINE_AGENTS/HANDOFF_PACKAGE_PLAYBOOK.md",
    "line": 7,
    "quote": "> Historical external example (availability unverified): Paired with the Cyberize Agentic Automation handoff as the historical worked example. Obtain the source repository, immutable revision and path before use; do not assume this path exists locally.",
    "containers": [
      {
        "type": "blockquote_open",
        "map": [
          5,
          9
        ],
        "content": ""
      },
      {
        "type": "paragraph_open",
        "map": [
          5,
          9
        ],
        "content": ""
      },
      {
        "type": "inline",
        "map": [
          5,
          9
        ],
        "content": "**The instruction set for authoring project handoff packages.**\nHistorical external example (availability unverified): Paired with the Cyberize Agentic Automation handoff as the historical worked example. Obtain the source repository, immutable revision and path before use; do not assume this path exists locally.\n**Born from:** Cyberize Agentic Automation Run 001 (May 2026) \u2014 first successful Factory frontend conversion\nHistorical external example (availability unverified): **Worked example:** `agent_docs/CURRENT_APP/app-factory-frontend-first-module/_project/` Obtain the source repository, immutable revision and path before use; do not assume this path exists locally."
      }
    ]
  },
  {
    "path": "02_PIPELINE_AGENTS/HANDOFF_PACKAGE_PLAYBOOK.md",
    "line": 9,
    "quote": "> Historical external example (availability unverified): **Worked example:** `agent_docs/CURRENT_APP/app-factory-frontend-first-module/_project/` Obtain the source repository, immutable revision and path before use; do not assume this path exists locally.",
    "containers": [
      {
        "type": "blockquote_open",
        "map": [
          5,
          9
        ],
        "content": ""
      },
      {
        "type": "paragraph_open",
        "map": [
          5,
          9
        ],
        "content": ""
      },
      {
        "type": "inline",
        "map": [
          5,
          9
        ],
        "content": "**The instruction set for authoring project handoff packages.**\nHistorical external example (availability unverified): Paired with the Cyberize Agentic Automation handoff as the historical worked example. Obtain the source repository, immutable revision and path before use; do not assume this path exists locally.\n**Born from:** Cyberize Agentic Automation Run 001 (May 2026) \u2014 first successful Factory frontend conversion\nHistorical external example (availability unverified): **Worked example:** `agent_docs/CURRENT_APP/app-factory-frontend-first-module/_project/` Obtain the source repository, immutable revision and path before use; do not assume this path exists locally."
      }
    ]
  },
  {
    "path": "02_PIPELINE_AGENTS/HANDOFF_PACKAGE_PLAYBOOK.md",
    "line": 131,
    "quote": "Historical external example (availability unverified): **Canonical example:** `_project/DATA_CONTRACT.md` in the Cyberize module. Obtain the source repository, immutable revision and path before use; do not assume this path exists locally.",
    "containers": [
      {
        "type": "paragraph_open",
        "map": [
          130,
          131
        ],
        "content": ""
      },
      {
        "type": "inline",
        "map": [
          130,
          131
        ],
        "content": "Historical external example (availability unverified): **Canonical example:** `_project/DATA_CONTRACT.md` in the Cyberize module. Obtain the source repository, immutable revision and path before use; do not assume this path exists locally."
      }
    ]
  },
  {
    "path": "02_PIPELINE_AGENTS/HANDOFF_PACKAGE_PLAYBOOK.md",
    "line": 169,
    "quote": "Historical external example (availability unverified): **Canonical example:** `_project/UI_SPEC.md` in the Cyberize module. Obtain the source repository, immutable revision and path before use; do not assume this path exists locally.",
    "containers": [
      {
        "type": "paragraph_open",
        "map": [
          168,
          169
        ],
        "content": ""
      },
      {
        "type": "inline",
        "map": [
          168,
          169
        ],
        "content": "Historical external example (availability unverified): **Canonical example:** `_project/UI_SPEC.md` in the Cyberize module. Obtain the source repository, immutable revision and path before use; do not assume this path exists locally."
      }
    ]
  },
  {
    "path": "02_PIPELINE_AGENTS/HANDOFF_PACKAGE_PLAYBOOK.md",
    "line": 346,
    "quote": "Historical external example (availability unverified): The historical worked example is `agent_docs/CURRENT_APP/app-factory-frontend-first-module/_project/`. Read all four files there to see what \"good\" looks like: Obtain the source repository, immutable revision and path before use; do not assume this path exists locally.",
    "containers": [
      {
        "type": "paragraph_open",
        "map": [
          345,
          346
        ],
        "content": ""
      },
      {
        "type": "inline",
        "map": [
          345,
          346
        ],
        "content": "Historical external example (availability unverified): The historical worked example is `agent_docs/CURRENT_APP/app-factory-frontend-first-module/_project/`. Read all four files there to see what \"good\" looks like: Obtain the source repository, immutable revision and path before use; do not assume this path exists locally."
      }
    ]
  },
  {
    "path": "02_PIPELINE_AGENTS/HANDOFF_PACKAGE_PLAYBOOK.md",
    "line": 381,
    "quote": "- Historical external example (availability unverified): **Worked example:** `agent_docs/CURRENT_APP/app-factory-frontend-first-module/_project/` Obtain the source repository, immutable revision and path before use; do not assume this path exists locally.",
    "containers": [
      {
        "type": "list_item_open",
        "map": [
          380,
          381
        ],
        "content": ""
      },
      {
        "type": "paragraph_open",
        "map": [
          380,
          381
        ],
        "content": ""
      },
      {
        "type": "inline",
        "map": [
          380,
          381
        ],
        "content": "Historical external example (availability unverified): **Worked example:** `agent_docs/CURRENT_APP/app-factory-frontend-first-module/_project/` Obtain the source repository, immutable revision and path before use; do not assume this path exists locally."
      }
    ]
  },
  {
    "path": "03_BUILD_METHODOLOGY/FRONTEND_FIRST_PLAYBOOK.md",
    "line": 373,
    "quote": "Historical external example (availability unverified): The historical worked example of this pattern is at: Obtain the source repository, immutable revision and path before use; do not assume this path exists locally.",
    "containers": [
      {
        "type": "paragraph_open",
        "map": [
          372,
          373
        ],
        "content": ""
      },
      {
        "type": "inline",
        "map": [
          372,
          373
        ],
        "content": "Historical external example (availability unverified): The historical worked example of this pattern is at: Obtain the source repository, immutable revision and path before use; do not assume this path exists locally."
      }
    ]
  },
  {
    "path": "04_REFERENCE_MANUALS/APP_ARCHITECTURE_MANUAL.md",
    "line": 1206,
    "quote": "Historical external example (availability unverified): The historical worked example of this pattern is at: Obtain the source repository, immutable revision and path before use; do not assume this path exists locally.",
    "containers": [
      {
        "type": "paragraph_open",
        "map": [
          1205,
          1206
        ],
        "content": ""
      },
      {
        "type": "inline",
        "map": [
          1205,
          1206
        ],
        "content": "Historical external example (availability unverified): The historical worked example of this pattern is at: Obtain the source repository, immutable revision and path before use; do not assume this path exists locally."
      }
    ]
  },
  {
    "path": "05_DESIGN_SYSTEM/THEMING_MANUAL.md",
    "line": 268,
    "quote": "- Historical external example (availability unverified): **Cyberize Run 001 `_project/CLAUDE.md`** \u2014 the historical worked example of a Locked Palette table Obtain the source repository, immutable revision and path before use; do not assume this path exists locally.",
    "containers": [
      {
        "type": "list_item_open",
        "map": [
          267,
          269
        ],
        "content": ""
      },
      {
        "type": "paragraph_open",
        "map": [
          267,
          268
        ],
        "content": ""
      },
      {
        "type": "inline",
        "map": [
          267,
          268
        ],
        "content": "Historical external example (availability unverified): **Cyberize Run 001 `_project/CLAUDE.md`** \u2014 the historical worked example of a Locked Palette table Obtain the source repository, immutable revision and path before use; do not assume this path exists locally."
      }
    ]
  },
  {
    "path": "05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md",
    "line": 128,
    "quote": "- Historical external example (availability unverified): **Cyberize Run 001 `_project/CLAUDE.md`** \u2014 the historical worked example of a Locked Palette table Obtain the source repository, immutable revision and path before use; do not assume this path exists locally.",
    "containers": [
      {
        "type": "list_item_open",
        "map": [
          127,
          129
        ],
        "content": ""
      },
      {
        "type": "paragraph_open",
        "map": [
          127,
          128
        ],
        "content": ""
      },
      {
        "type": "inline",
        "map": [
          127,
          128
        ],
        "content": "Historical external example (availability unverified): **Cyberize Run 001 `_project/CLAUDE.md`** \u2014 the historical worked example of a Locked Palette table Obtain the source repository, immutable revision and path before use; do not assume this path exists locally."
      }
    ]
  }
]

```

FFM:1997 is a paragraph; the exact line and markdown-it types are recorded in RAW/reconciled_checks.json (historical site 13). D-3 punctuation remains an OBSERVATION, not a failure.

## External exclusions

```text

_AUDIT/SYNC_2026-10-15_doctrine-part2/EXTERNAL_FOLLOWUPS.md:1: # Remaining components — Jarvis coordinates follow-ups
_AUDIT/SYNC_2026-10-15_doctrine-part2/EXTERNAL_FOLLOWUPS.md:2: 
_AUDIT/SYNC_2026-10-15_doctrine-part2/EXTERNAL_FOLLOWUPS.md:3: RUL-08 assigns coordination to Jarvis; it does not authorize Cody to perform external jobs or assert missing facts. Tony retains authority and Git mutations. Owners below describe responsibilities, not invented appointed implementers.
_AUDIT/SYNC_2026-10-15_doctrine-part2/EXTERNAL_FOLLOWUPS.md:4: 
_AUDIT/SYNC_2026-10-15_doctrine-part2/EXTERNAL_FOLLOWUPS.md:5: | Component / finding | Owner | Resolving trigger | Current scope consequence |
_AUDIT/SYNC_2026-10-15_doctrine-part2/EXTERNAL_FOLLOWUPS.md:6: |---|---|---|---|
_AUDIT/SYNC_2026-10-15_doctrine-part2/EXTERNAL_FOLLOWUPS.md:7: | Pinned kit guard exports/call/return contracts — FC-041, kit parts FC-001/028/033–035 | Jarvis coordinates kit custodian; Cody verifies supplied evidence | Named repo + immutable revision + source/caller evidence | Incorrect examples withdrawn/qualified; no verified replacement or closure claimed |
_AUDIT/SYNC_2026-10-15_doctrine-part2/EXTERNAL_FOLLOWUPS.md:8: | Session/cookie architecture — FC-042 | Jarvis / kit custodian | Pinned server and browser session/cookie implementation plus tests | Blanket HttpOnly assumptions removed; kit architecture remains unverified |
_AUDIT/SYNC_2026-10-15_doctrine-part2/EXTERNAL_FOLLOWUPS.md:9: | Rail breakpoint and responsive shell — FC-072 / kit portion FC-071 | Jarvis / kit custodian | Pinned shell/rail source and both-side breakpoint evidence | No universal breakpoint invented; misleading layouts withdrawn |
_AUDIT/SYNC_2026-10-15_doctrine-part2/EXTERNAL_FOLLOWUPS.md:10: | External worked examples, skills and locators — FC-009, locator part FC-003 / DEC-19 | Jarvis / source custodians | Actual repository, path, immutable revision and availability | Missing external source is not fabricated; reviewer guidance remains canonical RRM scope |
_AUDIT/SYNC_2026-10-15_doctrine-part2/EXTERNAL_FOLLOWUPS.md:11: | Root authority classification / pre-approval writes / recovery / CHANGELOG / FILE_TREE alignment — FC-008/010/090/091/094; DEC-08 | Jarvis coordinates a separately authorized root-instruction owner; Tony rules | Explicit root job and authority ruling, then verified aligned instructions | No root edits in this sync; scoped RUL-09 artifact rule does not approve arbitrary root changes |
_AUDIT/SYNC_2026-10-15_doctrine-part2/EXTERNAL_FOLLOWUPS.md:12: | Skill precedence/seat/closeout/CI/merge-over-red language — FC-005/006/092/095/096 | Jarvis coordinates separately authorized skill maintainer; Tony authorizes | Skills authoring job, approved changes and verification at current main | No older review-branch skill copied into main; FC-085/086/097 remain NO correction guards |
_AUDIT/SYNC_2026-10-15_doctrine-part2/EXTERNAL_FOLLOWUPS.md:13: | CI trigger expansion / lint tooling / branch protection — FC-095/096 | Tony owns settings; Jarvis coordinates any tooling maintainer | Explicit separate authorization and actual settings/check evidence | No CI or lint rewrite; canonical nine lint repairs remain selected |
_AUDIT/SYNC_2026-10-15_doctrine-part2/EXTERNAL_FOLLOWUPS.md:14: | Platform-specific promotion, rollback/recovery operations, DevOps occupant and FFM staging permissions — FC-011/012/088 / DEC-18 remainder | Jarvis coordinates platform owner; Tony grants context authority | Platform evidence plus named authorization/procedure | Common requirements selected; missing platform procedures remain open, no new cloud grant |
_AUDIT/SYNC_2026-10-15_doctrine-part2/EXTERNAL_FOLLOWUPS.md:15: | Universal quote storage and universal subscription schema — DEC-05 / K-SUBSCRIPTION-MODEL; FC-051/053/054/055/060/067/068 dependencies | Jarvis designs only under future scope; Tony releases | Explicit future design scope and verified project contracts | DEFERRED by RUL-11; supported safety corrections/withdrawals proceed without declaring these finding families resolved |
_AUDIT/SYNC_2026-10-15_doctrine-part2/EXTERNAL_FOLLOWUPS.md:16: | QAM automation tooling, ABM/APBM methodology and TRM definition | Jarvis coordinates future scoped owners; QA Lead owns QA requirements | Separate scope and approval | Excluded; not prerequisites for accepted document-template installation |
_AUDIT/SYNC_2026-10-15_doctrine-part2/EXTERNAL_FOLLOWUPS.md:17: | Missing historical sources / disputed harvest ZIP identity — GAP-01…06 | Jarvis coordinates original custodians | Attributable originals and identity reconciliation | Preserve sources and qualify history; current rulings govern without fabricating historical proof |
_AUDIT/SYNC_2026-10-15_doctrine-part2/EXTERNAL_FOLLOWUPS.md:18: 
_AUDIT/SYNC_2026-10-15_doctrine-part2/EXTERNAL_FOLLOWUPS.md:19: Every retained finding keeps its certified identity/severity/disposition. Containment, partial canonical completion and separately tracked external work are different claims.

```

## Findings

### F01 — AC5, AC6 — Retained contradictory DATA_CONTRACT ownership sentence

Both preceding branches assign the Architect, but the live router still says “different author”. The eight amended spans are installed exactly; the surrounding contradiction prohibition nevertheless fails.

```text

02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:174: > **CONVERSION:** the Architect **PRE-AUTHORS** `DATA_CONTRACT.md` from Brain Drain evidence — the Engineer consumes and honors it.
02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:175: > **GREENFIELD:** the Architect authors `DATA_CONTRACT.md` from the approved APP_BRIEF before Design. The Designer authors UI_SPEC; the Architect reconciles the assembled package. The Engineer consumes the approved contracts. The canonical DATA_CONTRACT template remains in §12.
02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:176: > Same artifact name — different author, different moment. Router: APP_FACTORY_BLUEPRINT, "Which Pipeline Am I In?".

```

### F02 — AC9 — Operations handoff anatomy omits mandatory QA artifacts

The mandatory QAM paragraph is present, but the immediately following handoff package tree lists the contracts/code/deployment guide without QAM/ or ACCEPTANCE_SPEC. AC9 explicitly covers folder trees and package anatomy, not only inserted prose.

```text

02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:1383: Every newly authored module includes a complete, module-specific `QAM/` prepared by the Architect from `03_BUILD_METHODOLOGY/_templates/QAM/`. QA Lead owns the reusable playbook and standing requirements. Engineer fills factual engineering records and handoff; QA Executor performs independent Q1 recon and test planning; QA Lead approves the plan; Director releases execution; QA Executor performs Q2 and authorized retest; QA Lead adjudicates and certifies. `QAM_PLAYBOOK.md` owns this packaging and sequence. Existing modules already in flight retain their recorded sequence until an attributable amendment.
02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:1384: 
02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:1385: When code is complete and tested, Engineer hands off to Operations/Deployment.
02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:1386: 
02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:1387: ### Handoff Package Contents
02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:1388: 
02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:1389: ```
02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:1390: 📦 ENGINEER → OPERATIONS HANDOFF
02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:1391: │
02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:1392: ├── APP_BRIEF.md (from Architect)
02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:1393: ├── UI_SPEC.md (from Designer)
02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:1394: ├── DATA_CONTRACT.md
02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:1395: ├── Working Code (tested)
02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:1396: ├── README.md (setup instructions)
02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:1397: └── Deployment Guide
02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:1398: ```

```

### F03 — AC15 — Active filesystem-wins rule survives in kit-track diagram

The diagram retains the explicitly forbidden “filesystem wins” authority rule. The corrected recon paragraph elsewhere does not remove this categorical instruction.

```text

02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:250: PHASE 0 — RECON (§2)
02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:251:    Answer RECON_QUESTIONNAIRE read-only → Recon Report → Architect authors
02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:252:         │
02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:253:         ▼
02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:254: KIT READ — STARTER_KIT_HANDBOOK
02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:255:    Read the handbook, treat it as ASPIRATIONAL — verify every load-bearing
02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:256:    claim against disk (RECON_QUESTIONNAIRE §0). Where handbook and
02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:257:    filesystem disagree, the filesystem wins.

```

### F04 — AC16 — Withdrawal coverage leaves dependent executable recipes

FC-022: seedSubscription still upserts through the .env.local admin client without an allowlisted target/test-identity guard. FC-038: Service Role Bypass still calls API routes an appropriate reason for RLS bypass. FC-066: fetchProducts returns Product[] while its page caller destructures {items,error}; the ISR variant has no separately named contract. These remain positive executable examples despite withdrawal/invariant paragraphs. No application code or external service was executed.

```text

03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:879: ### E2E user lifecycle (Supabase apps)
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:880: 
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:881: **Executable example withdrawn.** The previous example is not an approved implementation. The outgoing archived document preserves it as history. Replacement code requires the project’s approved contract, verified dependency interfaces and behavioral evidence. This withdrawal contains the misleading recipe; it does not certify the underlying finding resolved.
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:882: 
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:883: Before privileged test setup or cleanup, verify the target project reference against the Director-approved test-project allowlist and verify the authorized test identity. Fail closed on mismatch, missing identity or unknown target. Record every run-created identity; cleanup may act only on that set. Production verification is a separately authorized, bounded, non-destructive procedure.
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:884: 
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:885: ---
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:886: 
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:887: ### Direct DB seeding to bypass Stripe in E2E
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:888: 
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:889: E2E tests need users with specific subscription tiers. Automating Stripe Checkout in a browser is brittle (Stripe changes their DOM). Solution: insert subscription rows directly into Supabase via the admin client, as if the webhook had already fired.
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:890: 
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:891: ```typescript
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:892: export async function seedSubscription(userId: string, tier: TestTier) {
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:893:   const { error } = await supabaseAdmin.from("subscriptions").upsert(
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:894:     {
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:895:       user_id: userId,
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:896:       tier,
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:897:       status: "active",
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:898:       stripe_customer_id: `cus_test_${userId.slice(0, 8)}`,
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:899:       stripe_subscription_id: `sub_test_${userId.slice(0, 8)}`,
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:900:       current_period_start: new Date().toISOString(),
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:901:       current_period_end: new Date(
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:902:         Date.now() + 30 * 24 * 60 * 60 * 1000,
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:903:       ).toISOString(),
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:904:       cancel_at_period_end: false,
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:905:     },
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:906:     { onConflict: "user_id" },
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:907:   );
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:908:   if (error) throw new Error(`Failed to seed subscription: ${error.message}`);
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:909: }
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:910: ```
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:911: 
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:912: Synthetic Stripe IDs (`cus_test_*`, `sub_test_*`) work because the gating logic only reads `tier` and `status` from the row — it never calls the Stripe API to verify the subscription ID.
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:913: 
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:914: **Trade-off:** E2E doesn't cover the actual Stripe round-trip. That's what integration tests (mocked) validate at the route level, and what manual smoke tests validate end-to-end. Each layer covers what it's good at.
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:915: 
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:916: ### Supabase admin client in E2E helpers
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:917: 
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:918: ```typescript
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:919: import { createClient } from "@supabase/supabase-js";
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:920: import * as dotenv from "dotenv";
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:921: 
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:922: // Playwright runs outside Next.js — must load .env.local manually
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:923: dotenv.config({ path: ".env.local" });
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:924: 
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:925: export const supabaseAdmin = createClient(
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:926:   process.env.NEXT_PUBLIC_SUPABASE_URL!,
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:927:   process.env.SUPABASE_SECRET_KEY!,
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:928:   { auth: { autoRefreshToken: false, persistSession: false } },
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:929: );
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:930: ```

04_REFERENCE_MANUALS/DATABASE_MANUAL.md:418: ### Service Role Bypass
04_REFERENCE_MANUALS/DATABASE_MANUAL.md:419: 
04_REFERENCE_MANUALS/DATABASE_MANUAL.md:420: When using the service role key (server-side), RLS is bypassed. This is appropriate for:
04_REFERENCE_MANUALS/DATABASE_MANUAL.md:421: - API routes
04_REFERENCE_MANUALS/DATABASE_MANUAL.md:422: - Background jobs
04_REFERENCE_MANUALS/DATABASE_MANUAL.md:423: - Admin operations
04_REFERENCE_MANUALS/DATABASE_MANUAL.md:424: 
04_REFERENCE_MANUALS/DATABASE_MANUAL.md:425: ```typescript
04_REFERENCE_MANUALS/DATABASE_MANUAL.md:426: // Server-side: Service role bypasses RLS
04_REFERENCE_MANUALS/DATABASE_MANUAL.md:427: import { createClient } from '@supabase/supabase-js';
04_REFERENCE_MANUALS/DATABASE_MANUAL.md:428: 
04_REFERENCE_MANUALS/DATABASE_MANUAL.md:429: const supabase = createClient(
04_REFERENCE_MANUALS/DATABASE_MANUAL.md:430:   process.env.SUPABASE_URL!,
04_REFERENCE_MANUALS/DATABASE_MANUAL.md:431:   process.env.SUPABASE_SERVICE_ROLE_KEY! // Bypasses RLS
04_REFERENCE_MANUALS/DATABASE_MANUAL.md:432: );

04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:613: export const fetchProducts = async (): Promise<Product[]> => {
04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:614:   const response = await fetch(API_ENDPOINTS.PRODUCTS);
04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:615:   const wooProducts: WooCommerceProduct[] = await response.json();
04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:616:   
04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:617:   // Transform each product to internal format
04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:618:   return wooProducts.map(normalizeProduct);
04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:619: };

04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:787: 
04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:788: import { fetchProducts } from '@/services/productServices';
04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:789: import { ProductList } from '@/components/shop/ProductList';
04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:790: import { EmptyState } from '@/components/common/EmptyState';
04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:791: 
04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:792: export default async function ShopPage() {
04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:793:   const { items: products, error } = await fetchProducts();
04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:794: 
04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:795:   // Graceful degradation: show empty state instead of crashing
04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:796:   if (error || products.length === 0) {
04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:797:     return (

04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:853: 
04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:854: ```typescript
04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:855: // Static generation with revalidation
04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:856: export const fetchProducts = async () => {
04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:857:   const response = await fetch(API_ENDPOINT, {
04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:858:     next: { 
04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:859:       revalidate: 3600, // Revalidate every hour
04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:860:     },
04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:861:   });
04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:862:   return response.json();

```

### F05 — AC18 — Browser-contact default is not stated across all four required manuals

STATE states the default. AUTH and TESTING do not state the required default against persistent raw contact information in browser storage; ECOMMERCE refers to an approved retention policy but does not state that default. Generic log-redaction or authorization-state restrictions are not the specified contact-storage rule. Full persist/contact matches are retained in RAW/personal_data_matches.txt.

```text

04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:501: **Never persist everything.** Use `partialize` to select only UX-critical state:
04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:502: 
04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:503: ```typescript
04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:504: export const useCheckoutStore = create<CheckoutState>()(
04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:505:   persist(
04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:506:     (set) => ({
04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:507:       // Persisted
04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:508:       billingAddress: null,
04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:509:       shippingAddress: null,
04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:510:       
04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:511:       // NOT persisted (transient)
04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:512:       isProcessing: false,
04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:513:       validationErrors: {},
04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:514:       paymentIntent: null,
04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:515:     }),
04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:516:     {
04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:517:       name: 'checkout-storage',
04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:518:       partialize: (state) => ({
04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:519:         // Raw contact information is not persisted by default.
04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:520:         // An approved exception must name fields, purpose, retention and owner.

04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:783: Do not persist raw contact details by default. Any approved personal-data persistence declares permitted fields, retention duration and user or guest scope. Sign-out and account transition reset and invalidate every affected store even when remote logout fails; a new account must not hydrate the previous account’s data. Payment and authorization state remain outside persistence. Storage readiness is separate from business-data reset.

04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:199: Accept product/variation identifiers, quantities, shipping selection and coupon code, never caller prices, shipping costs or discount amounts. Validate quantities and product eligibility; load authoritative catalog prices; validate the shipping selection and coupon eligibility; apply the declared tax policy; calculate currency-safe totals on the server. Bind the payment to the authorized order and verify payment identity, amount, currency and order association before marking paid. Client totals are display-only. Return generic failures and redact logs. Universal quote-storage design is deferred; the required server pricing and payment binding still apply.
04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:200: 
04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:201: Persist one authorized checkout-attempt identity across retries and claim it atomically against concurrent requests. Scope provider idempotency keys to that attempt and operation, reuse or retrieve existing external objects after an unknown outcome, and reconcile before creating a replacement. Use the project-approved customer-identity contract without assuming paid activation; universal subscription schema design is deferred. Handle every documented subscription state, not only active.
04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:202: 
04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:203: Use one validated checkout contract across form, state, route and service. The request carries billing.email, validated line identifiers/quantities, shippingMethod and couponCode; it carries no authoritative monetary values. The response identifies the authorized order/payment attempt or a typed generic failure. The server pricing operation from the same contract supplies totals. Revisions to items, shipping or coupon invalidate the old payment binding before a new attempt is released.
04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:204: 
04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:205: The checkout interaction contract includes shippingCost and couponDiscount as display estimates, couponCode, setCoupon(code) and clearCoupon(), alongside the existing checkout fields. The server revalidates shipping and coupons. STATE_MANAGEMENT_MANUAL owns the shared store shape; ECOMMERCE_AND_PAYMENTS_MANUAL refers to it. Personal fields follow the approved account-transition and retention policy.
04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:206: 
04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:207: ---

03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:418: For tests touching persistent client state (Zustand, Redux with localStorage, IndexedDB), assert against **both** the source of truth AND the UI:
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:419: 
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:420: ```ts
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:421: await expect(page.getByText(/Coupon Applied:/)).toBeVisible(); // user-facing claim
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:422: 
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:423: const stored = await page.evaluate(() =>
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:424:   localStorage.getItem("checkout-storage"),
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:425: );
03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:426: expect(JSON.parse(stored!).state.couponCode).toBe(expectedCode); // approved non-sensitive project fixture only

```

### F06 — AC19 — Unqualified live platform deployment recipe remains

The deployment owner correctly says platform procedure is OPEN/not adopted, while the subscription manual retains a prescriptive GCP deployment checklist with create-secret/deploy commands and no historical/unadopted qualifier. This is an authority consistency finding, not a vendor-command correctness finding.

```text

04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:484: ## 13. Deployment Checklist
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:485: 
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:486: ### GCP Cloud Run Deployment
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:487: 
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:488: **Step 1 — Create Secrets in GCP Secret Manager:**
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:489: ```bash
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:490: gcloud secrets create projectname-stripe-secret-key --data-file=-
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:491: gcloud secrets create projectname-stripe-webhook-secret --data-file=-
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:492: gcloud secrets create projectname-stripe-price-starter --data-file=-
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:493: gcloud secrets create projectname-stripe-price-pro --data-file=-
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:494: gcloud secrets create projectname-stripe-price-enterprise --data-file=-
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:495: gcloud secrets create projectname-supabase-service-role-key --data-file=-
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:496: ```
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:497: 
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:498: **Step 2 — Deploy Cloud Run with Secret Mappings:**
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:499: ```bash
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:500: gcloud run deploy projectname \
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:501:   --set-secrets=STRIPE_SECRET_KEY=projectname-stripe-secret-key:latest \
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:502:   --set-secrets=STRIPE_WEBHOOK_SECRET=projectname-stripe-webhook-secret:latest \
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:503:   --set-secrets=STRIPE_PRICE_STARTER=projectname-stripe-price-starter:latest \
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:504:   --set-secrets=STRIPE_PRICE_PRO=projectname-stripe-price-pro:latest \
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:505:   --set-secrets=STRIPE_PRICE_ENTERPRISE=projectname-stripe-price-enterprise:latest \
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:506:   --set-secrets=SUPABASE_SERVICE_ROLE_KEY=projectname-supabase-service-role-key:latest \
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:507:   --set-env-vars=NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=pk_test_... \
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:508:   --set-env-vars=NEXT_PUBLIC_SUPABASE_URL=https://xxx.supabase.co \
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:509:   --set-env-vars=NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJ...
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:510: ```
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:511: 
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:512: Note: `NEXT_PUBLIC_*` vars can be plain env vars (they're browser-safe). Secret vars use `--set-secrets`.
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:513: 
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:514: **Step 3 — Register Webhook Endpoint in Stripe Dashboard:**
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:515: 
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:516: After deployment, your Cloud Run service has a URL like `https://projectname-abc123.run.app`.
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:517: 
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:518: Go to Stripe Dashboard → Developers → Webhooks → Add endpoint:
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:519: - **URL:** `https://projectname-abc123.run.app/api/webhooks/stripe`
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:520: - **Events:** Select `checkout.session.completed`, `customer.subscription.updated`, `customer.subscription.deleted`
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:521: 
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:522: Copy the new webhook signing secret and update the GCP secret.
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:523: 
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:524: **Step 4 — Verify:**
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:525: ```
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:526: □ Visit the Cloud Run URL — app loads
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:527: □ Register a user — auth works
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:528: □ Subscribe — Stripe Checkout works
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:529: □ Webhook fires — subscription appears in Supabase
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:530: □ Content gating works
04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:531: ```

03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md:69: ## 7. Platform Profiles — OPEN
03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md:70: 
03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md:71: No platform procedure is Factory doctrine yet. The August DevOps operating model (SRC-W07) proposes a Cloud Run profile (`init-app.sh`, `cloudbuild.yaml`, `Dockerfile`, `deploy.sh`, a checklist) and two platform postures; `APP_FACTORY_SKILLS_PLAYBOOK.md` §14 names the deployment skill family. These are source claims and existing tools, not adopted rules: version-sensitive commands must be verified at implementation time, and profile-specific filenames are not imposed on Vercel or Python deployments. Adoption of any profile is the Director's decision (DEC-18 remainder).
03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md:72: 
03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md:73: ## 8. Open Items Register — OPEN (not doctrine)
03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md:74: 
03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md:75: | ID | Open item | Owner | Source of the gap |
03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md:76: |---|---|---|---|
03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md:77: | O-1 | DevOps authority: the cloud columns of the §3 matrix; "may the Engineer deploy to staging in FFM runs?"; Cloud Run as one platform profile | Director (Architect advises) | DEC-18 remainder; the reported DevOps Architect ruling of 2026-08-23 was not supplied (CL-13) |
03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md:78: | O-2 | DevOps Architect seat occupant | Director | SRC-W07 F-2 (deliberately unassigned) |
03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md:79: | O-3 | Staging → production promotion doctrine | Director | SRC-W07 F-1 |
03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md:80: | O-4 | Monitoring / incident detection after deploy | Director | SRC-W07 F-3 |
03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md:81: | O-5 | Non-Next.js deployment packages (Python / ADK services) | Director | SRC-W07 F-4 |
03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md:82: | O-6 | Gate D mapping on client platforms beyond Vercel | QA Lead / Director | SRC-W07 F-5 |
03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md:83: 
03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md:84: An OPEN item is closed only by a Director ruling recorded and landed through DocSet Sync; until then no module may cite this section as authority for a deployment action.

```

### F07 — AC20 — Universal CURRENT_APP landing instructions survive

Live FFM definition and handoff/bridging instructions prescribe agent_docs/CURRENT_APP despite the no-universal-landing-path requirement. Appendix B was repaired and passes its bounded AC14 checks. All 13 historical-pointer container checks separately pass.

```text

03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:38: ---
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:39: 
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:40: ## 1. What an FFM Is, In One Page
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:41: 
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:42: A **Frontend-First Module (FFM)** is a portable, self-contained folder dropped at `agent_docs/CURRENT_APP/<project>_<phase>_ffm/` inside a starter kit clone. It is the single source of truth that tells an AI coding tool (Claude Code, Codex CLI, Gemini CLI, etc.) **what to build, how to build it, and what not to touch.**
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:43: 
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:44: An FFM bundles:

03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:165: ### Role 3 — Architect
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:166: 
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:167: **Who:** You, Claude (in a chat session, NOT in the terminal as a coding agent).
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:168: **With:** Operator (you).
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:169: **Produces:** The complete FFM folder, ready to drop at `agent_docs/CURRENT_APP/`.
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:170: 
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:171: **Outputs:** Every file in the FFM folder structure (see [Section 3](#3-ffm-anatomy--the-folder-structure)).
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:172: 
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:173: **Handoff target:** The starter kit's `agent_docs/CURRENT_APP/` directory.
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:174: 

03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1637: ## 16. Bridging The FFM Into The Starter Kit
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1638: 
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1639: The FFM lives at `agent_docs/CURRENT_APP/<project>_<phase>_ffm/`. The starter kit's root `CLAUDE.md` needs to know it's there.
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1640: 
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1641: ### Two Bridging Patterns
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1642: 
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1643: **Pattern A — Edit Starter Kit Root `CLAUDE.md` (older convention)**
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1644: 
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1645: The operator adds a pointer paragraph to the starter kit's root `CLAUDE.md`:
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1646: 
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1647: ```markdown
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1648: ## Active Project Module
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1649: 
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1650: The current project's Factory module lives at `agent_docs/CURRENT_APP/<ffm_folder_name>/`. Read `CLAUDE.md` in that folder for project-specific direction, doctrine, and the phase-by-phase playbook. All work for the current project follows that module.
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1651: ```
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1652: 
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1653: Claudy reads root CLAUDE.md first on session start, sees the pointer, follows it to the FFM.
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1654: 
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1655: **Pattern B — `PROJECT_POINTER.md` (newer, cleaner convention)**
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1656: 
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1657: Create a separate file at the starter kit root called `PROJECT_POINTER.md`:
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1658: 
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1659: ```markdown
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1660: # PROJECT_POINTER.md — Active Project Module
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1661: 
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1662: The current project's Factory module lives at:
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1663: **`agent_docs/CURRENT_APP/<ffm_folder_name>/`**
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1664: 
03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1665: On session start, read `CLAUDE.md` in that folder. That file is the project's navigation contract. It tells you which project we're building, what's in scope, what's forbidden, what phase we're in, and where to find the project handoff docs (APP_BRIEF, DATA_CONTRACT, UI_SPEC).

```
