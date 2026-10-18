# Exact workflow and draft-integration edits

ENGINEER-PROPOSED — review text only; no canonical or surviving draft has been changed. All old spans are unique and line-verified. Conditional rows remain open. Shared paragraphs land only once per stated location.

## W01 — `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md:251`
Authority: RUL-01/02/03/04; FC-013/025/026; WF-05/07; QAM-01…14. Conditional: none. Replace lines 251–251 with the exact text below.

````markdown
6. **Gate Q is mandatory for all code-bearing modules.** Only documentation-only / non-runtime changes may receive a recorded Operator QA waiver.

Every newly authored module includes a complete, module-specific `QAM/` prepared by the Architect from `03_BUILD_METHODOLOGY/_templates/QAM/`. QA Lead owns the reusable playbook and standing requirements. Engineer fills factual engineering records and handoff; QA Executor performs independent Q1 recon and test planning; QA Lead approves the plan; Director releases execution; QA Executor performs Q2 and authorized retest; QA Lead adjudicates and certifies. `QAM_PLAYBOOK.md` owns this packaging and sequence. Existing modules already in flight retain their recorded sequence until an attributable amendment.

The Director commits and pushes the completed engineering candidate on the numbered product branch, then creates `qa/<module-branch>` at that exact commit. Engineer performs approved repairs and QA Executor independently tests on that same QA branch, with separate writable lanes and one active writer during repair or measurement. The QA branch continues to final integration; do not transfer work back or abandon it as the normal workflow. After the QA Lead’s verdict and required cleanup, the Architect issues closeout instructions, Engineer performs bounded closeout, and the Director performs final commits, merge and push. Preserve product, execution, evidence and closeout identities separately.
````

## W02 — `03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md:30`
Authority: RUL-01; QAM-02; WF-07. Conditional: none. Replace lines 30–30 with the exact text below.

````markdown
| **QA Lead (independent seat)** | Owns standing QA requirements, approves the independent plan, adjudicates findings and certifies the governed candidate per `QA_PLAYBOOK.md` and `QAM_PLAYBOOK.md` |
| **QA Executor (independent seat)** | Performs Q1 recon and plan drafting, then approved Q2 execution and authorized retest; records evidence and never repairs product or self-certifies |
````

## W03 — `03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md:103`
Authority: RUL-04; FC-026. Conditional: none. Replace lines 103–103 with the exact text below.

````markdown
2. **Contracts freeze at handoff.** Requirements and acceptance criteria remain immutable except through an attributable approved amendment. Declared lanes inside the module remain writable by their assigned owners for engineering handoff, recon, plans, evidence, findings and rulings. QA records live in the module’s `QAM/` under `agent_docs/`. A test-plan edit cannot amend acceptance criteria.
````

## W04 — `03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md:153`
Authority: RUL-04; FC-026. Conditional: none. Replace lines 153–153 with the exact text below.

````markdown
- **Mid-mandate contract mutation** — changing frozen requirements or acceptance criteria without an attributable approved amendment; declared owner-specific output lanes remain writable
````

## W05 — `03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md:135`
Authority: RUL-01…04; FC-013/026; WF-07. Conditional: none. Replace lines 135–135 with the exact text below.

````markdown
## 9. QA Engagement (the Red Team seat)

Every newly authored module includes a complete, module-specific `QAM/` prepared by the Architect from `03_BUILD_METHODOLOGY/_templates/QAM/`. QA Lead owns the reusable playbook and standing requirements. Engineer fills factual engineering records and handoff; QA Executor performs independent Q1 recon and test planning; QA Lead approves the plan; Director releases execution; QA Executor performs Q2 and authorized retest; QA Lead adjudicates and certifies. `QAM_PLAYBOOK.md` owns this packaging and sequence. Existing modules already in flight retain their recorded sequence until an attributable amendment.

The Director commits and pushes the completed engineering candidate on the numbered product branch, then creates `qa/<module-branch>` at that exact commit. Engineer performs approved repairs and QA Executor independently tests on that same QA branch, with separate writable lanes and one active writer during repair or measurement. The QA branch continues to final integration; do not transfer work back or abandon it as the normal workflow. After the QA Lead’s verdict and required cleanup, the Architect issues closeout instructions, Engineer performs bounded closeout, and the Director performs final commits, merge and push. Preserve product, execution, evidence and closeout identities separately.

Required cleanup removes only authorized disposable execution debris, temporary credentials/authentication state, and owned QA processes or browser contexts. Retain durable evidence, required failed attempts and justified helpers. QA Lead governs retention and cleanup acceptance; certification, Architect closeout and Director release remain separate responsibilities. Record command, working directory, exit code and unfiltered safe output, with sensitive data excluded at collection. Prove product, tests, configuration and contract identity unchanged by cleanup. Module QA records live under `agent_docs/` in their module `QAM/`; verify production exclusion under `DEPLOYMENT_PLAYBOOK.md`.
````

## W06 — `03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md:55`
Authority: RUL-01/04; QAM-03/04. Conditional: none. Replace lines 55–55 with the exact text below.

````markdown
├── AGENTS.md                   ← same parent routing as CLAUDE.md
├── QAM/                        ← mandatory module-specific QA package, including matching entry routes
└── (declared writable output lanes: engineering handoff, recon, plans, evidence, findings, rulings)
````

## W07 — `03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md:62`
Authority: RUL-01 via source §6; QAM-04. Conditional: none. Replace lines 62–62 with the exact text below.

````markdown
Every module folder carries one manager body and matching `CLAUDE.md` / `AGENTS.md` entry routing. Engineering routes to the implementation assignment; QA routes into `QAM/`, whose two entries assign QA Executor and point to `QAM_ENTRY.md`. Redirects may share one instruction body. Required manager contents:
````

## W08 — `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:61`
Authority: RUL-01/06; WF-01. Conditional: none. Replace lines 61–61 with the exact text below.

````markdown
## 2. The Factory Roles and Delivery Pattern
````

## W09 — `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:63`
Authority: RUL-01/06; WF-01/07. Conditional: none. Replace lines 63–63 with the exact text below.

````markdown
The FFM preparation stream retains Designer, Extractor, Architect and Engineer responsibilities. The complete delivery workflow also includes independent QA Executor and QA Lead responsibilities and the Director’s approval and release authority. Each role’s outputs feed the next role’s inputs; the preparation diagram below is not a complete release lifecycle.
````

## W10 — `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:261`
Authority: RUL-01/03/06; WF-04/05; QAM-03. Conditional: none. Replace lines 261–261 with the exact text below.

````markdown
## 3. FFM Anatomy — The Folder Structure

Every newly authored module includes a complete, module-specific `QAM/` prepared by the Architect from `03_BUILD_METHODOLOGY/_templates/QAM/`. QA Lead owns the reusable playbook and standing requirements. Engineer fills factual engineering records and handoff; QA Executor performs independent Q1 recon and test planning; QA Lead approves the plan; Director releases execution; QA Executor performs Q2 and authorized retest; QA Lead adjudicates and certifies. `QAM_PLAYBOOK.md` owns this packaging and sequence. Existing modules already in flight retain their recorded sequence until an attributable amendment.

The FFM lives under the project’s `agent_docs/` module convention. Its `QAM/` records and support material are excluded from production inputs and artifacts, with verification under `DEPLOYMENT_PLAYBOOK.md`.
````

## W11 — `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:565`
Authority: RUL-01/04/06; WF-04/05; FC-025/026; artifact ownership remains DEC-10/11/12 conditional. Conditional: none. Replace lines 565–566 with the exact text below.

````markdown
14. Return actual Designer and extraction outputs to the Architect for completeness and contract reconciliation.
15. Architect assembles the final approved package, includes ACCEPTANCE_SPEC.md and module-specific QAM/, verifies dependencies and declares writable output lanes.
16. Director approves the assembled revision and releases the Engineer on the numbered product branch. Engineering handoff, Q1, plan approval, release, Q2, conditional repair/retest, cleanup and closeout follow QAM_PLAYBOOK.
````

## W12 — `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1828`
Authority: RUL-01/03/04/06; FC-025/026; QAM-03/04. Conditional: none. Replace lines 1828–1828 with the exact text below.

````markdown
## 18. The Authoring Checklist

- [ ] Approved pre-implementation `ACCEPTANCE_SPEC.md` is present.
- [ ] Module-specific `QAM/` is prepared from the accepted template set; no independent QA result, approval or certification is prefilled.
- [ ] Parent entry files route Engineering to implementation and QA to `QAM/`; both QAM entry files assign QA Executor.
- [ ] Frozen contract and owner-specific writable output lanes are declared.
- [ ] Actual Designer/extraction outputs returned to Architect assembly and are approved before launch.
- [ ] Compile/test exclusion and build/deploy/artifact exclusion of `agent_docs/**` are declared and verifiable.
````

## W13 — `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:2141`
Authority: RUL-01/02; QAM-04/05. Conditional: none. Replace lines 2141–2141 with the exact text below.

````markdown
## 22. Appendix B — Boot Prompts

For newly authored modules, use the prepared module entry routes. Engineering launch does not approve QA execution. QA launch enters `QAM/` as QA Executor at the durable recorded state; Q1 produces the independent plan, Q2 requires QA Lead approval and Director release. Resume validates candidate, branch, approval and writable lanes before acting.
````

## W14 — `03_BUILD_METHODOLOGY/QA_PLAYBOOK.md:205`
Authority: RUL-01; QAM-02/05/09. Conditional: none. Replace lines 205–214 with the exact text below.

````markdown
The QA Lead:

- owns the reusable QA playbook and standing risk requirements,
- treats the engineering handoff as claims to verify,
- reviews and approves the QA Executor’s independent plan,
- adjudicates findings and issues the governed QA verdict and certification,
- governs retention and cleanup acceptance,
- protects the boundary between in-scope defects and follow-up findings.

## QA Executor

The QA Executor independently performs Q1 recon and test planning, executes the approved plan after Director release, records evidence, packages checkpoints, and performs authorized retest and cleanup. The Executor does not repair product code, grant release authority or certify its own result.
````

## W15 — `03_BUILD_METHODOLOGY/QA_PLAYBOOK.md:475`
Authority: RUL-01/03; WF-07. Conditional: none. Replace lines 475–475 with the exact text below.

````markdown
## Stage 5 — Operator Manual QA

For newly authored modules, the QA Lead’s approved QAM plan allocates checks to the QA Executor or to declared human-only verification according to evidence needs, capability and authorized side effects. Agent-capable matrices do not default to the Director. The one-test-at-a-time protocol below applies when the plan calls for Operator execution. It does not replace independent Q1 planning, plan approval or Director release.
````

## W16 — `03_BUILD_METHODOLOGY/QA_PLAYBOOK.md:927`
Authority: RUL-03; QAM-07/10. Conditional: none. Replace lines 927–927 with the exact text below.

````markdown
# 14. The Final Environment Reset Rule

Required cleanup removes only authorized disposable execution debris, temporary credentials/authentication state, and owned QA processes or browser contexts. Retain durable evidence, required failed attempts and justified helpers. QA Lead governs retention and cleanup acceptance; certification, Architect closeout and Director release remain separate responsibilities. Record command, working directory, exit code and unfiltered safe output, with sensitive data excluded at collection. Prove product, tests, configuration and contract identity unchanged by cleanup. Module QA records live under `agent_docs/` in their module `QAM/`; verify production exclusion under `DEPLOYMENT_PLAYBOOK.md`.
````

## W17 — `02_PIPELINE_AGENTS/RECON_QUESTIONNAIRE.md:351`
Authority: RUL-03; deployment draft §4; preserve Q9.1–Q9.3 stable IDs. Conditional: none. Replace lines 351–351 with the exact text below.

````markdown
## SECTION 9 — FFM Packaging & Compile Scope

**Q9.4 — Build/deployment exclusion.** Identify the applicable build/deploy input exclusion mechanisms for `agent_docs/**` (for example `.dockerignore`, `.gcloudignore`, `.vercelignore` or the platform equivalent). Verify the actual built image/bundle or deployed artifact excludes it. Record command, working directory, exit code and unfiltered safe output. Compile/test exclusion alone does not prove production exclusion. Follow `DEPLOYMENT_PLAYBOOK.md` §4; do not infer cloud authorization from this question.
````

## W18 — `02_PIPELINE_AGENTS/ARCHITECT_PLAYBOOK.md:330`
Authority: RUL-01/06; WF-05; QAM-03/13. Conditional: none. Replace lines 330–330 with the exact text below.

````markdown
## 8. Handoff Protocol to Designer

Every newly authored module includes a complete, module-specific `QAM/` prepared by the Architect from `03_BUILD_METHODOLOGY/_templates/QAM/`. QA Lead owns the reusable playbook and standing requirements. Engineer fills factual engineering records and handoff; QA Executor performs independent Q1 recon and test planning; QA Lead approves the plan; Director releases execution; QA Executor performs Q2 and authorized retest; QA Lead adjudicates and certifies. `QAM_PLAYBOOK.md` owns this packaging and sequence. Existing modules already in flight retain their recorded sequence until an attributable amendment.
````

## W19 — `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:1377`
Authority: RUL-01/06; WF-05; QAM-03/13. Conditional: none. Replace lines 1377–1377 with the exact text below.

````markdown
## 17. Handoff Protocol to Operations

Every newly authored module includes a complete, module-specific `QAM/` prepared by the Architect from `03_BUILD_METHODOLOGY/_templates/QAM/`. QA Lead owns the reusable playbook and standing requirements. Engineer fills factual engineering records and handoff; QA Executor performs independent Q1 recon and test planning; QA Lead approves the plan; Director releases execution; QA Executor performs Q2 and authorized retest; QA Lead adjudicates and certifies. `QAM_PLAYBOOK.md` owns this packaging and sequence. Existing modules already in flight retain their recorded sequence until an attributable amendment.
````

## W20 — `02_PIPELINE_AGENTS/HANDOFF_PACKAGE_PLAYBOOK.md:285`
Authority: RUL-01/06; WF-05; QAM-03/13. Conditional: none. Replace lines 285–285 with the exact text below.

````markdown
## 8. Approval Gates

Every newly authored module includes a complete, module-specific `QAM/` prepared by the Architect from `03_BUILD_METHODOLOGY/_templates/QAM/`. QA Lead owns the reusable playbook and standing requirements. Engineer fills factual engineering records and handoff; QA Executor performs independent Q1 recon and test planning; QA Lead approves the plan; Director releases execution; QA Executor performs Q2 and authorized retest; QA Lead adjudicates and certifies. `QAM_PLAYBOOK.md` owns this packaging and sequence. Existing modules already in flight retain their recorded sequence until an attributable amendment.
````

## W21 — `03_BUILD_METHODOLOGY/BUG_FIX_PLAYBOOK.md:573`
Authority: RUL-01/06; WF-05; QAM-03/13. Conditional: none. Replace lines 573–573 with the exact text below.

````markdown
## 18. Required FIX Artifacts

Every newly authored module includes a complete, module-specific `QAM/` prepared by the Architect from `03_BUILD_METHODOLOGY/_templates/QAM/`. QA Lead owns the reusable playbook and standing requirements. Engineer fills factual engineering records and handoff; QA Executor performs independent Q1 recon and test planning; QA Lead approves the plan; Director releases execution; QA Executor performs Q2 and authorized retest; QA Lead adjudicates and certifies. `QAM_PLAYBOOK.md` owns this packaging and sequence. Existing modules already in flight retain their recorded sequence until an attributable amendment.
````

## W22 — `03_BUILD_METHODOLOGY/FEAT_PLAYBOOK.md:43`
Authority: RUL-01/06; WF-05; QAM-03/13. Conditional: none. Replace lines 43–43 with the exact text below.

````markdown
## 5. Definition of Done — delta only

Every newly authored module includes a complete, module-specific `QAM/` prepared by the Architect from `03_BUILD_METHODOLOGY/_templates/QAM/`. QA Lead owns the reusable playbook and standing requirements. Engineer fills factual engineering records and handoff; QA Executor performs independent Q1 recon and test planning; QA Lead approves the plan; Director releases execution; QA Executor performs Q2 and authorized retest; QA Lead adjudicates and certifies. `QAM_PLAYBOOK.md` owns this packaging and sequence. Existing modules already in flight retain their recorded sequence until an attributable amendment.
````

## W23 — `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md:171`
Authority: RUL-05; WF-11; K-ENGINE proposed terminology. Conditional: none. Replace lines 171–171 with the exact text below.

````markdown
## 2. The Build Phases

Engine 1 denotes module engineering and module QA across the implementation phases. Review occurs after FFM completion and its QA, and again at Engine 2 after all Engine 1 phase/module engineering and QA are closed. Findings require disposition; only approved findings needing repair produce bounded RRM work, and each RRM includes QAM. A clean review produces no RRM. Module QA certification, broader review completion and deployed-system Gate D remain distinct.
````

## D-QAM-1 — `_AUDIT/SYNC_2026-10-15_doctrine-part2/DRAFTS/QAM_PLAYBOOK.md:257`
Authority: D17; DEC-06 pending. Conditional: DEC-06. Replace lines 257–257 with the exact text below.

````markdown
A later contradiction is recorded and routed for an attributable authority ruling before affected doctrine is changed; DocSet Sync propagates the approved resolution.
````

## D-RRM-1 — `_AUDIT/SYNC_2026-10-15_doctrine-part2/DRAFTS/RRM_PLAYBOOK.md:117`
Authority: RRM-09 placement open. Conditional: RRM-09 / DEC-19. Replace lines 117–117 with the exact text below.

````markdown
PROPOSED — reviewer-guidance placement and adoption remain open under RRM-09 / DEC-19. If approved, independent review that feeds an RRM follows these rules; the pilot source is preserved unchanged.
````

## D-RRM-2 — `_AUDIT/SYNC_2026-10-15_doctrine-part2/DRAFTS/RRM_PLAYBOOK.md:126`
Authority: ND-07. Conditional: ND-07. Replace lines 126–126 with the exact text below.

````markdown
## 12. The Prepared, Uninterrupted Engineering Run (optional shape)

PROPOSED — ND-07 remains open. This section is not an adopted default or an approved optional policy until the Director rules.
````

## D-DEPLOY-1 — `_AUDIT/SYNC_2026-10-15_doctrine-part2/DRAFTS/DEPLOYMENT_PLAYBOOK.md:22`
Authority: DEC-18 remainder is open. Conditional: DEC-18. Replace lines 22–22 with the exact text below.

````markdown
- **Director** holds release authority and performs project-module Git mutations under RUL-02. QA seats do not mutate product or Git. Existing BIM cloud-zero restrictions remain in force in their declared context. FFM staging permission, DevOps assignment and the complete cloud-action matrix remain OPEN under DEC-18; this section grants no new cloud permission.
````

## D-DEPLOY-2 — `_AUDIT/SYNC_2026-10-15_doctrine-part2/DRAFTS/DEPLOYMENT_PLAYBOOK.md:39`
Authority: DEC-18. Conditional: DEC-18. Replace lines 39–39 with the exact text below.

````markdown
| Cloud contexts beyond an existing explicit restriction | Deploy, promote, roll back, change infrastructure | Per an attributable context-specific authorization; no general grant here | OPEN under DEC-18 (§7–§8) |
````

## D-DEPLOY-3 — `_AUDIT/SYNC_2026-10-15_doctrine-part2/DRAFTS/DEPLOYMENT_PLAYBOOK.md:65`
Authority: DEC-17 and DEC-06. Conditional: DEC-17 / DEC-06. Replace lines 65–65 with the exact text below.

````markdown
A project intentionally pinned to an approved revision continues under that pin until an attributable update decision. A disagreement is recorded with both identities and routed to its authority owner; newer main is not automatic authorization to alter a project contract.
````

## D-QAM-2 — `_AUDIT/SYNC_2026-10-15_doctrine-part2/DRAFTS/QAM_PLAYBOOK.md:51`
Authority: GAP-01; CL-11; preserve source attribution without authenticating missing source. Conditional: K-DRAFT-INTEGRATION. Replace lines 51–51 with the exact text below.

````markdown
the intake attributes earlier pilot guidance to Doctrine Journal v0.3, which was not supplied for this sync. That historical attribution is unverified; current requirements derive from the recorded Director rulings and approved Hub integration, not the unavailable journal.
````
