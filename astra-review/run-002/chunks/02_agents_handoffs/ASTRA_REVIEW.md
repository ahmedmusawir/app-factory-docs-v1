# CHUNK 02 — AGENTS / HANDOFFS REVIEW

## 1. STATUS

COMPLETE

Branch: `factory-docs-review-astra-w-chunks`. Only authorized write target: this report. The complete Chunk Review Contract and only the Chunk 02 definition in the Execution Plan were read for this examination.

All six primary files were examined and this report was written incrementally. Findings: 0 BLOCKER, 3 HIGH, 3 MEDIUM, 0 LOW; 4 suggestions. Verification against the starting metadata for 143 repository files found only this report changed; tracked working-tree and staged diffs were empty. No other file or Factory doctrine was modified. No commit, push, branch change, Chunk 03 work or synthesis was performed.

## 2. SCOPE

Objective: determine whether Factory seats have clear, compatible, executable authority and handoff boundaries, including human approval, agent ownership, inputs/outputs, escalation, QA independence, and DevOps responsibilities.

Primary scope: all six current Markdown doctrine files in `02_PIPELINE_AGENTS/`: ARCHITECT_PLAYBOOK, ARCHITECT_QUESTIONNAIRE, DESIGNER_PLAYBOOK, ENGINEER_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, and RECON_QUESTIONNAIRE (all `.md`).

Supporting reads are limited to necessary constitutional-authority checks in `01_CONSTITUTION/`. Excluded: Run 001 artifacts, all other chunk review artifacts, Fable/Sol reviews, dispositions, synthesis material, broad neighboring-domain review, doctrine corrections, and implementation. Prior conversation review conclusions are not evidence for this chunk.

## 3. DOMAIN MODEL

The intended chain separates human decisions from agent authorship and execution. The Operator owns product decisions and approves the brief/package. The Architect obtains fresh recon, classifies the app, records scope/constraints and planning uncertainty, and submits the brief for human approval. Its approval table explicitly requires reapproval after amendment. The Designer translates approved scope into tokens, canonical HTML/PNG, screen behavior, and a component manifest. The Engineer receives the pipeline-specific package, checks readiness, and builds within scope; it must stop on conflicts and may not silently take product or design decisions (Architect §§1–2, 7–8; Designer §§1–2, 4, 8, 10; Engineer §§1–3, 15).

Recon precedes authoring: the Architect requests/tunes the instrument, the Operator dispatches the Engineer, and the Engineer returns the report the Architect consumes. The Architect marks recon stale after phase closure, kit upgrades, or branch merges. Written inspection-only limits and commands/output instructions are not completely compatible (C02-D02).

Two routing axes appear. **Conversion vs greenfield** changes package provenance and authorship: conversion uses extraction evidence and source screenshots; the Architect pre-authors DATA_CONTRACT and UI_SPEC. Greenfield uses Designer artifacts and an Engineer-authored DATA_CONTRACT based on approved APP_BRIEF and UI_SPEC. **Kit vs Pipeline Track** changes execution: Next.js/TypeScript/Supabase kit consumption versus Python/CLI/file-based backend or local tooling. The documents explicitly distinguish the axes, but do not fully adapt intake requirements for nonvisual builds (Engineer §§3, 5, 13; Handoff preamble and §5.2).

The constitutional checks establish that engineering specs must receive human approval before fabrication, and that code-bearing modules require ACCEPTANCE_SPEC, independent QA verdict ownership, mandatory Gate Q, and Operator adjudication/release authority. Those requirements remain binding even where the Engineer's own handoff procedure omits them (Blueprint lines 143–154; Software Factory Playbook lines 244–251).

Operations/SRE is named as the production operator, separate from Engineering. Engineering supplies tested code, setup/configuration documentation and a deployment guide; Operations needs health checks, logging, and rollback instructions. No separate DevOps role procedure appears in these six files. The constitutional Operator remains release authority; the identity and acceptance procedure of the Operations recipient are not specified here (Engineer lines 90–97, §17).

## 4. FIVE-DIMENSION SCORECARD

| Dimension | Score | Evidence-based justification |
|---|---|---|
| Correctness | 3 | Core human/agent separation, pipeline-specific DATA_CONTRACT ownership and recipient checks are sound. Inspection-only recon is not compatible with its prescribed operations (C02-D02), and the engineering procedure omits binding pre-build/post-build authority transitions (C02-D01, C02-D03). This is a role/handoff score, not a certification of embedded technical examples. |
| Consistency | 3 | Designer→Engineer visual artifacts agree and conversion provenance is explicit. Brief status labels, upstream UI_SPEC drafting obligations, and mandatory versus conditional track inputs disagree (C02-D04–D06); the local recon rules also conflict (C02-D02). |
| Completeness | 3 | Most producers, consumers, artifacts and escalation paths are named. Engineering lacks its constitutional QA interface and explicit greenfield spec-approval step (C02-D01, C02-D03); nonvisual intake is incomplete (C02-D06). Operations has useful requirements but would benefit from a receiving record (C02-S01). |
| Executability | 2 | A human familiar with the intended workflow can reconcile it, but literal execution encounters an inspection/build conflict, incompatible approval labels, a missing upstream draft, and mandatory visuals for nonvisual builds (C02-D02, C02-D04–D06). Repeated manual interpretation is needed at actual boundaries. |
| Maintainability | 3 | Single-source instruments, stable recon IDs, domain-owner pointers and session records help. Producer/consumer copies and shared templates have already diverged; greenfield additions and broad common checklists need coordinated maintenance (C02-D03–D06). No documentation synchronization process was examined. |

All scores are integers and apply only to Chunk 02; no Factory-wide score is inferred.

## 5. WHAT IS STRONG

1. **Named recon producer, consumer, and freshness triggers.** Architect lines 79–103 and Engineer lines 107–121 connect Engineer-produced evidence to Architect authoring, with a report path and stale-report triggers. Preserve that ownership and freshness discipline while correcting the operation boundary in C02-D02.
2. **Human ownership of product scope and brief unlocks.** Architect lines 56–65 and 291–326 reserves product decisions for the human, distinguishes draft/review/approved/amended states, and requires reapproval after changes. Designer lines 61–68 and Engineer lines 90–97 reinforce role limits. Preserve those authority distinctions; do not let a template default stand in for approval.
3. **Explicit uncertainty survives the planning handoff.** Architect Questionnaire lines 55–66, 132–159 records decisions, assumptions, and open questions, including unresolved optional deep-dive answers. Its scope gate at lines 30–32 forces explicit exclusions. Preserve uncertainty labels and persistence of unresolved decisions; avoid treating every question as already settled.
4. **Design handoff distinguishes implementation reference from verification evidence.** Designer lines 149–185 and 309–326 ships HTML, PNG, and tokens with different stated purposes; Engineer lines 133–153 requests the same artifact set. Preserve paired build/verification artifacts, all-mode tokens, and a human-approved canonical reference.
5. **Conversion provenance and contract ownership are explicit.** Handoff lines 125–159 and 271–279 ties conversion contracts to extraction evidence and greenfield claims to recorded Operator decisions; Engineer lines 155–172 distinguishes consumption from authorship. Preserve source behavior, known discrepancies, and the author/consumer split rather than assuming the same filename implies the same author.
6. **Recipient-side rejection is actionable.** Engineer lines 174–189 lists readiness checks and directs missing greenfield inputs back to Designer, conversion inputs back to the package author, with Operator escalation. Architect lines 376–385 also requires Designer confirmation. Preserve these receiving-side checks and clarify their variant applicability.
7. **Conflict handling and scope discipline have a named common home.** Engineer lines 1133–1141 and 1166–1223 establishes all-agent conduct, a stop/name/ask/wait response to contradictions, and explicit approval before deleting unrelated or newly dead code. Preserve escalation instead of silently choosing an interpretation.
8. **Operations gets more than a code archive.** Engineer lines 1377–1402 requires setup, environment information, health checks, logging and rollback guidance. Session-memory rules at lines 1280–1359 preserve handoff context across tools. Preserve these useful operational artifacts while adding the missing QA/release interface and clearer recipient acceptance.

## 6. PRIORITY FINDINGS

1. **C02-D01 — HIGH:** the Engineer's ready-for-Operations contract omits the constitutionally required Engineering→QA handoff and release-authority interface.
2. **C02-D02 — HIGH:** recon is simultaneously prescribed as inspection-only, a build-executing procedure, and a file-producing handoff without a defined output exception.
3. **C02-D03 — HIGH:** the greenfield Engineer workflow does not establish the required engineering-spec approval checkpoint before implementation.
4. **C02-D04 — MEDIUM:** the canonical APP_BRIEF template emits LOCKED, while both receiving agents require APPROVED.
5. **C02-D05 — MEDIUM:** downstream greenfield instructions require an Architect-drafted UI_SPEC that the Architect's own handoff never supplies.

The full ranked list also includes C02-D06 on nonvisual Pipeline Track intake. Suggestions are separate below.

## 7. RANKED DEFECTS

### Rank 1 — C02-D01: The Engineer's completion contract skips the QA/release interface

- **Classification:** DEFECT
- **Severity:** HIGH
- **Affected primary file:** `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md`.
- **Supporting constitutional source:** `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md` §2.5, lines 244–251.
- **Evidence:** Engineer §12, lines 958–966, declares readiness for Operations after P0 implementation, unit/integration tests, documentation, tested deployment and monitoring. §17, lines 1377–1391, sends complete/tested code directly to Operations with APP_BRIEF, UI_SPEC, DATA_CONTRACT, code, README and deployment guide. The whole Engineer file contains no QA seat handoff, ACCEPTANCE_SPEC, or Gate Q instruction. The current constitutional rule requires ACCEPTANCE_SPEC at every code-bearing module handoff, approved Architect/Operator acceptance criteria before implementation, a QA-owned verdict, mandatory Gate Q, and Operator final release authority.
- **Why this is a defect:** the Engineer's explicit recipient and readiness contract is materially incomplete against its binding constitutional obligation. Following the listed handoff alone never transfers acceptance claims to independent QA and never identifies the QA/release evidence Operations must receive. Engineering tests and deployability do not supply that separate role decision.
- **Operational consequence:** code can arrive at Operations labeled ready with no acceptance contract or independent verdict attached. Operators must reconstruct an omitted handoff before deciding whether the package is releasable; Engineering can otherwise appear to certify its own readiness.
- **Recommended resolution:** incorporate the constitutional Engineering→QA interface before release readiness: named acceptance artifact and provenance, QA verdict reference, routing for findings/blockage, and Operator release decision. Preserve Operations' distinct setup/logging/rollback needs. Link the detailed QA owner rather than duplicating its mechanics, and retain the limited documentation/non-runtime waiver eligibility.
- **Confidence/limits:** high confidence in the missing role interface. This does not claim QA doctrine is absent elsewhere, that Operations has lawful authority to bypass QA, or that an actual release bypass occurred. The constitution remains controlling; the defect is the Engineer's executable handoff.

### Rank 2 — C02-D02: Recon's operation boundary contradicts its own procedure and output

- **Classification:** DEFECT
- **Severity:** HIGH
- **Affected primary files:** `02_PIPELINE_AGENTS/RECON_QUESTIONNAIRE.md`, `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md`, `02_PIPELINE_AGENTS/ARCHITECT_PLAYBOOK.md`.
- **Supporting constitutional source:** `01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md`, lines 109–118.
- **Evidence:** Recon “How To Use This,” lines 44–59, specifies “no file changes, no git operations” and pure reading/grepping. Engineer §2, lines 113–117, repeats that restriction but also requires producing `agent_docs/recon/RECON_<project>_<phase>_<date>.md`; Architect lines 88–101 waits for that written file. Recon's mandatory day-one sweep, S0.7 at lines 105–108, and Q8.6 at lines 341–344 instruct `npm run build` in the target repository. These are project-script execution instructions, not reading/grepping, and the doctrine does not constrain their side effects or distinguish them as separately authorized diagnostics. The Blueprint establishes recon as a read-only pass.
- **Why this is a defect:** a literal pure-inspection operator cannot fulfill the prescribed build step. The blanket no-file rule also lacks an explicit exception or separate writer for the report that the next seat requires. Interpreting the report as an intended narrow exception is reasonable, but it does not authorize executing arbitrary repository build scripts or settle their write boundary. These are manifestations of one missing operation/output boundary, not separate defect counts.
- **Operational consequence:** one Engineer stops or returns conversation-only results; another runs build scripts and writes artifacts under an inspection-only assignment. The Architect may receive no persisted evidence or evidence from a repository changed during recon. The user has to resolve permissions that the instrument should have made clear.
- **Recommended resolution:** define the exact permitted report write and prohibit application/source changes; distinguish pure inspection from any optional build/runtime diagnostics, with their authorization, execution location, and expected artifact effects made explicit. If diagnostics are unavailable or not permitted, require a recorded limitation rather than a fabricated result. Make the producer and consumer agree on where the report is persisted.
- **Confidence/limits:** high confidence from the command and role text. No recon command or project build was executed during this review, and no particular build side effect or harm is asserted. Later verification-ritual notes about deletion are not treated as commands to delete during recon.

### Rank 3 — C02-D03: Greenfield engineering-spec approval has no execution checkpoint

- **Classification:** DEFECT
- **Severity:** HIGH
- **Affected primary file:** `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md`.
- **Supporting constitutional source:** `01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md`, lines 143–154.
- **Evidence:** Engineer lines 168–171 correctly assigns greenfield DATA_CONTRACT authorship to Engineering after receiving approved APP_BRIEF/UI_SPEC. Its “Before starting” checks at lines 174–189 verify those incoming approvals but omit submission and approval of the Engineer's resulting specs. §12, lines 730–741, calls DATA_CONTRACT an output produced “alongside working code” and gives a DRAFT/APPROVED field without a transition procedure. The concluding Engineer checklist, lines 1554–1564, lists build/test work before producing the greenfield DATA_CONTRACT and handing off. The Blueprint explicitly requires Engineer-produced DATA_CONTRACT, applicable schema/API specs and FILE_TREE, followed by human approval of all specs at Phase 3, before Phase 4 code writing.
- **Why this is a defect:** assigning an author and putting APPROVED in a template does not implement the required author→approver→builder transition. The Engineer's own sequence can be followed without submitting its newly authored contract/specs for approval before code. This is distinct from C02-D01: it concerns authorization of implementation inputs, not independent acceptance of implementation outputs.
- **Operational consequence:** a greenfield Engineer can design data/API requirements while coding and present the contract retrospectively, when the human's required specification decision was meant to precede implementation. Another Engineer following the Blueprint would stop for approval first.
- **Recommended resolution:** explicitly stage greenfield spec authorship, human review/approval, then fabrication, referencing the approved artifact revisions. Keep conversion consumption of pre-authored contracts separate. Treat subsequent approved changes as amendments, not as permission to bypass the initial gate.
- **Confidence/limits:** high confidence in the missing checkpoint and conflicting completion sequence. “Alongside” alone could mean a final deliverable bundle; the finding depends on the combined absence of the gate in the procedural sequence and checklist. No implementation authorization is inferred from these omissions; the Blueprint's approval rule still wins.

### Rank 4 — C02-D04: APP_BRIEF state vocabulary does not match receiving gates

- **Classification:** DEFECT
- **Severity:** MEDIUM
- **Affected primary files:** `02_PIPELINE_AGENTS/ARCHITECT_QUESTIONNAIRE.md`, `02_PIPELINE_AGENTS/ARCHITECT_PLAYBOOK.md`, `02_PIPELINE_AGENTS/DESIGNER_PLAYBOOK.md`, `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md`.
- **Evidence:** Architect Questionnaire lines 6–7 declares itself the single template source; its header at line 75 permits `[DRAFT | REVIEW | LOCKED]`. Architect Playbook lines 212–216 says to use that template as-is without forking, but lines 291–326 defines DRAFT→REVIEW→APPROVED and AMENDED, with human control of unlocking; its handoff at lines 330–339 requires APPROVED. Designer preflight line 95 and Engineer preflight line 180 also require APPROVED. No equivalence or migration rule maps LOCKED to APPROVED or explains AMENDED in the canonical template.
- **Why this is a defect:** the canonical producer schema cannot express the exact state required by the consumers and the producer's operating manual. These are explicit status labels at a gate, not merely alternate descriptive prose.
- **Operational consequence:** a correctly filled LOCKED brief is rejected by a literal consumer, or an operator silently treats the labels as interchangeable without confirming which human approval they represent. Revision/reapproval tracking also diverges.
- **Recommended resolution:** adopt one shared lifecycle vocabulary in the template, authoring procedure and receiving checklists, including amendment/reapproval handling. If existing LOCKED briefs remain valid, define the mapping and required approval evidence rather than silently relabeling them.
- **Confidence/limits:** high confidence; impact is normally recoverable by explicit clarification, hence MEDIUM rather than HIGH. Human approval requirements exist and must be preserved.

### Rank 5 — C02-D05: Greenfield UI_SPEC drafting is assigned downstream but absent upstream

- **Classification:** DEFECT
- **Severity:** MEDIUM
- **Affected primary files:** `02_PIPELINE_AGENTS/ARCHITECT_PLAYBOOK.md`, `02_PIPELINE_AGENTS/DESIGNER_PLAYBOOK.md`, `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md`, `02_PIPELINE_AGENTS/HANDOFF_PACKAGE_PLAYBOOK.md`.
- **Supporting constitutional source:** `01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md`, lines 130–144.
- **Evidence:** Handoff §5.5, line 254, says greenfield UI_SPEC is drafted by the Architect and revised by the Designer; Engineer §3, line 143, repeats that provenance. Architect's explicit handoff at lines 334–341 contains only approved APP_BRIEF, visual anchor and verbal brief, and its recipient checklist at lines 376–385 never transfers a UI_SPEC draft. Designer required inputs at lines 81–99 likewise do not request one; §§8 and 10 instead provides its own UI_SPEC template and treats the approved result as a Designer deliverable (lines 243–288, 311–318). The Blueprint explicitly makes UI_SPEC a Designer output at line 140; it does not establish the extra Architect-draft stage.
- **Why this is a defect:** two current downstream documents promise an upstream artifact/provenance that neither the producer's handoff nor the intermediary's receiving protocol implements. Architect scope authoring and Designer final authorship can coexist with an Architect draft, but that draft needs an explicit creation/transfer step if it is required.
- **Operational consequence:** one team has the Designer create UI_SPEC from the brief; another waits for or demands an Architect draft. Responsibility for initial screen behavior and missing spec content depends on which document is followed, adding avoidable rework and disputed ownership.
- **Recommended resolution:** decide whether an Architect draft is required or optional in greenfield. If required, add its scope, timing and receiving responsibility to the actual handoff; if not, remove the mandatory draft provenance and retain Designer authorship from approved scope. Preserve the distinct conversion authorship route.
- **Confidence/limits:** high confidence in the producer/consumer mismatch, not a claim that both agents are forbidden to collaborate. A final Designer-approved spec can still be produced; the missing draft is a bounded handoff defect.

### Rank 6 — C02-D06: Mandatory visual intake has no valid path for a supported nonvisual build

- **Classification:** DEFECT
- **Severity:** MEDIUM
- **Affected primary files:** `02_PIPELINE_AGENTS/ARCHITECT_PLAYBOOK.md`, `02_PIPELINE_AGENTS/ARCHITECT_QUESTIONNAIRE.md`, `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md`.
- **Evidence:** Architect's router/type table explicitly supports Backend Bundle with minimal/no UI or CLI (lines 153–200); its DataSync example at lines 504–539 has a scheduled service and excludes admin/manual-trigger UI. Nevertheless, its inputs and approval checks require a visual anchor and forbid proceeding without one (lines 112, 124–130, 303). The canonical Questionnaire's mandatory Q4 at line 29 likewise says STOP without a visual anchor. Engineer Part I declares its common doctrine applicable to every track (lines 51–53), routes Backend Bundle to the Pipeline Track at line 989, but its preflight at lines 174–189 unconditionally requires approved UI_SPEC and, for greenfield, token/style-tile/screen HTML/PNG/component-manifest inputs; absence means STOP. No nonvisual/not-applicable branch is supplied.
- **Why this is a defect:** the domain explicitly accepts applications without screens, yet the mandatory authoring and receiving gates require screen-design inputs before those applications can advance. CLI documentation or a service's API documentation can be legitimate deliverables; they are not a rendered screen/token package for a backend with no visual interface.
- **Operational consequence:** a valid nonvisual Pipeline Track engagement either stalls, invents irrelevant visuals, or relies on an undocumented waiver. Architect and Engineer may disagree on which inputs can be marked not applicable.
- **Recommended resolution:** make intake conditional on an actual interface/track decision. Define the required backend/CLI contract and receiving checklist, and an explicit not-applicable treatment for visual artifacts when no visual interface is approved. Preserve the complete design package where screens exist.
- **Confidence/limits:** high confidence in the applicability gap. This does not remove UX work for a CLI that actually needs it and does not assert that every backend is headless. The example supplies a supported case in which mandatory visual artifacts lack a purpose.

## 8. RANKED SUGGESTIONS

### Rank 1 — C02-S01: Make operational custody acceptance explicit

- **Classification:** SUGGESTION
- **Evidence:** Engineer §17, lines 1377–1428, gives the Operations role concrete setup, logging, health-check and rollback needs. Engineer line 97 excludes production operation from Engineering. Blueprint lines 159–162 assigns deployment to the human, and Software Factory Playbook line 250 reserves release authority for the Operator.
- **Improvement:** name the receiving operator/Operations delegate and record acceptance of a specific release/package, environment, rollback procedure and outstanding manual steps; state what happens if the recipient rejects the package or is unavailable. Keep custody acceptance distinct from QA verdict and release approval.
- **Value:** makes the Engineer→Operations boundary actionable in both a one-person Factory and a delegated deployment. Existing human authority means the absence of a named individual is not itself evidence that production has no owner.

### Rank 2 — C02-S02: Give recon a complete coverage and freshness record

- **Classification:** SUGGESTION
- **Evidence:** Architect lines 88–101 requires a current report and defines staleness triggers. Recon lines 471–532 provides a return template covering sections 1–6, 8–9 and 13, but no explicit slots for the section 0 sweep or sections 11–12, no repository revision identity, and no per-question unavailable/not-applicable status. Questions can be tuned per project (lines 40–42).
- **Improvement:** record target repository, branch/revision or equivalent snapshot identity, capture time, question IDs examined, observations versus deferred Operator checks, and explicit blocked/not-applicable outcomes. Cover all current instrument sections without renumbering stable question IDs.
- **Value:** lets the Architect verify currency and completeness instead of inferring them from a dated filename or a partially populated template. Existing recommendation/surprise fields can carry missing detail, so this is an improvement to the handoff rather than proof that every current report loses evidence.

### Rank 3 — C02-S03: Define a provisional visual-alignment step before brief approval

- **Classification:** SUGGESTION
- **Evidence:** Architect lines 124–130 proposes asking the Designer for a quick style tile when no anchor exists, while Designer lines 94–99 requires an already-approved brief before starting. Blueprint line 57 recognizes brand-tokens-only input with a style tile before screens; the Architect also permits independent sketches/screenshots as alternatives.
- **Improvement:** distinguish a small Operator-authorized exploratory style tile from production design, with provisional scope and no power to lock product requirements. State how its output feeds the subsequent brief approval.
- **Value:** makes the documented Designer-assisted fallback executable without asking the operator to invent an exception. This is a suggestion because independent visual anchors already provide a valid escape route; it is not a universal deadlock and is separate from the nonvisual applicability defect.

### Rank 4 — C02-S04: Preserve mandatory planning inputs in the canonical brief template

- **Classification:** SUGGESTION
- **Evidence:** Architect approval checks at lines 298–317 require a complete acceptable tech stack and P0 priorities; Questionnaire Q10 at line 49 asks for stack information, but the canonical template at lines 70–166 has no dedicated per-layer stack block or explicit P0 priority field. It provides general scope, constraints, and Planning State fields instead.
- **Improvement:** provide explicit slots for the approved per-layer stack, prioritized in-scope capabilities, and visual-anchor reference, with a clear mapping from questionnaire answers to approval checks. Retain the optional nature of the deep-dive phase.
- **Value:** reduces handoff omissions and pressure to fork the single-source template. Existing generic fields can hold these decisions, so lack of dedicated fields alone is not classified as a defect.

## 9. CROSS-DOMAIN DEPENDENCIES

| Classification | Evidence and bounded handoff | Follow-up domain |
|---|---|---|
| DEPENDENCY | Engineer lines 261–288 delegates module anatomy, supervised execution and testing to FFM/build/testing owners. C02-D01 establishes a missing role interface against the constitution; later review must examine the QA/module procedures for verdict evidence, routing, retest and release integration. Those files were not opened. | Build method / QA. |
| DEPENDENCY | Designer lines 374–384 explicitly defers token/method conflicts to named design doctrine. The locked artifacts and KIPs depend on that domain's component and design-system rules; this review verifies the handoff shape, not those technical rules. | Design/frontend. |
| DEPENDENCY | Recon Q3.4, lines 194–209, distinguishes role authorization reads/client-writable writes from protected creation-time transport. This is useful evidence framing for the auth domain; no live authorization implementation or vulnerability was tested here. | Auth/data/security. |
| CONTRADICTION CANDIDATE | Engineer Pipeline Track lines 390–442 and 1113–1118 requires implementation/manual execution before tests, while its all-agent conduct table at line 1230 says to write the test defining success first. Track scope may explain some uses, but “all agents” and the shared-reference placement do not settle every case. Detailed build-method precedence should be examined without changing this chunk's role-focused defect count. | Build method. |
| SYNTHESIS FLAG | C02-D03 places the missing approval between engineering-spec authorship and implementation; C02-D01 places a separate missing interface between implementation and independent QA/release. Later synthesis should distinguish these transitions and avoid merging or double-counting related findings from other chunks by filename alone. No other chunk review was consulted. | Eventual synthesis after domain review. |
| DEPENDENCY | Recon and Architect identify the stark-recon skill as the executable instrument (Recon lines 6–8; Architect lines 93–101). Actual skill behavior, output writes, diagnostic permissions and question coverage need a later comparison to C02-D02/C02-S02. The skill was not opened or invoked. | Skills/documentation governance. |
| SYNTHESIS FLAG | The Operations boundary includes setup, logging, monitoring and rollback but lacks a documented receiving acceptance step. C02-S01 should be compared with any deployment/module workflow before a separate DevOps seat or additional ceremony is proposed. | Operations-facing workflow / eventual synthesis. |

## 10. AMBIGUITIES / UNKNOWNS

- **QA mechanics outside this folder — UNKNOWN.** Constitutional ownership, verdict names, Gate Q and waiver eligibility are explicit. Detailed QA procedures may exist in another domain, but the Chunk 02 scope does not permit opening them. C02-D01 is limited to the missing Engineering interface and makes no claim of Factory-wide QA absence.
- **Operations recipient — partially defined.** Operations/SRE has a stated remit; the Operator holds constitutional release authority. These sources do not say which named person/agent accepts custody for a run, how acceptance is recorded, or what happens on rejection (C02-S01). A separate DevOps seat is not established by this primary set.
- **Recon exception authority — AMBIGUOUS in the written scope.** Architect line 103 permits an explicit human override for a trivial case, while Blueprint lines 111–118 calls a brief/package without current recon invalid. Human override may be intended as the controlling exception, but its acknowledgement/record and effect on validity are unspecified here. No independent AI waiver authority is inferred; no waiver was used in this examination.
- **Greenfield authoring order — resolved in principle, insufficiently labeled locally.** Handoff lines 15–19 routes greenfield through the agent playbooks while retaining the package definition; §6, lines 258–267, orders DATA_CONTRACT before UI_SPEC using a source-conversion rationale. The Blueprint and Engineer lines 168–172 explicitly make greenfield DATA_CONTRACT depend on approved UI_SPEC. The pipeline-specific constitutional rule therefore establishes the greenfield direction; this report does not count a second circular-dependency defect from reading the conversion order universally. The missing execution checkpoint is C02-D03, and the draft-producer mismatch is C02-D05.
- **Different brief structures — variant relationship needs care.** The Architect Questionnaire is the canonical brief instrument, while Handoff §5.1 supplies conversion-oriented required sections and §5.5 adds greenfield artifacts. Whether every conversion-specific section is mandatory in a greenfield brief is not fully explicit. The proven approval-state mismatch is C02-D04; different structures alone are not automatically a duplicate-template defect.
- **Router coverage beyond the demonstrated nonvisual case — limited.** The Architect tree at lines 159–180 routes browser UI without cloud database/auth to Local-First, while the Engineer assigns that class to the Pipeline Track (line 989). Hosted browser-only apps and non-kit/exotic stacks are not clearly handled by these combined axes. C02-D06 concerns the stronger, explicit supported headless case; no broad platform redesign is recommended here.
- **Design approval provenance — not fully specified.** Designer line 259 defaults the UI_SPEC template to APPROVED, while lines 152 and 177 require human canonical approval and the receiving package requires approved UI_SPEC. The template is not evidence that approval occurred. A copied default could mislead, but the explicit human gates prevent treating the default alone as authorization; this is not counted as a separate defect.
- **Platform/framework and runtime claims — NOT VERIFIED.** Cloud limits, ADC/environment parity, code examples, actual kit auth, token output, tests and live services were read as embedded doctrine but not independently validated. Their technical assessment belongs to the appropriate domain; this report does not turn unverified sample claims into role defects.
- **Examples and past findings — NOT CONSULTED.** Current files contain historical mentions and worked-example pointers. No Run 001 example, retrospective, previous review, or review-seat opinion was opened. Claims that past packages were successful are not independently endorsed.

## 11. COVERAGE MANIFEST

| Primary file | Status |
|---|---|
| `02_PIPELINE_AGENTS/ARCHITECT_PLAYBOOK.md` | EXAMINED — full file, lines 1–615. |
| `02_PIPELINE_AGENTS/ARCHITECT_QUESTIONNAIRE.md` | EXAMINED — full file, lines 1–180. |
| `02_PIPELINE_AGENTS/DESIGNER_PLAYBOOK.md` | EXAMINED — full file, lines 1–396. |
| `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md` | EXAMINED — full file, lines 1–1598. |
| `02_PIPELINE_AGENTS/HANDOFF_PACKAGE_PLAYBOOK.md` | EXAMINED — full file, lines 1–385. |
| `02_PIPELINE_AGENTS/RECON_QUESTIONNAIRE.md` | EXAMINED — full file, lines 1–562. |

All primary files were read completely, including their embedded examples and history; review judgments concern current role, authority, and handoff doctrine. Commands shown in doctrine were examined as text, not executed. Technical code samples and service/version claims were not independently certified.

| Supporting source | Status and reason |
|---|---|
| `01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md` | CROSS-REFERENCE — lines 42–61 and 109–162 only, to verify constitutional authority over pipeline ownership, read-only recon, Designer/Engineer outputs, spec approval, and human deployment responsibility. |
| `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md` | CROSS-REFERENCE — lines 232–252 only, to verify the binding Engineering→QA acceptance contract, QA independence, Gate Q, and Operator release authority. |

The full `astra-review/run-002/packets/CHUNK_REVIEW_CONTRACT.md` and only the Chunk 02 definition of `astra-review/run-002/packets/EXECUTION_PLAN.md` were read as control inputs. No other chunk report, Fable/Sol review, disposition, synthesis file, Run 001 artifact, root governance reference, nonconstitutional supporting doctrine, skill implementation, or external web source was opened for this chunk. Historical mentions within current assigned doctrine were not followed. Prior conversation findings were not used as evidence.

## 12. SYNTHESIS HANDOFF

- **Strongest conclusion:** the principal seats and most artifacts are clearly described, but end-to-end handoffs are not consistently implemented as compatible producer/consumer contracts. Missing engineering approval/QA transitions and incompatible status/input requirements still require operator knowledge.
- **Most serious defect:** C02-D01 — the Engineer's own completion contract reaches Operations without the constitutionally required QA acceptance interface. C02-D02 and C02-D03 separately affect the permitted recon work and the pre-implementation approval boundary.
- **Most important strength to preserve:** human ownership of product scope and brief unlocks, combined with recipient-side stop/escalate checks and evidence-based, pipeline-specific authorship. Preserve the aligned Designer HTML/PNG/token handoff as a concrete example of compatible inputs and outputs.
- **Unresolved issue most likely to affect another domain:** the detailed QA/module workflow must connect approved acceptance requirements to independent verdicts and Operator release decisions. Its mechanics were not examined, and Engineering's implementation tests must not silently substitute for that interface.
- **Findings deserving later Factory-wide consideration:** C02-D01/C02-D03's two authority transitions, C02-D02's inspection-versus-execution distinction, and C02-D04's producer/consumer status vocabulary. Compare source evidence across chunks before deciding common causes or disposition.
- **Totals:** 6 DEFECTS — BLOCKER: 0; HIGH: 3; MEDIUM: 3; LOW: 0. SUGGESTIONS: 4. Dependencies, contradiction candidates and unknowns are not additional findings.

This section is evidence for eventual synthesis only. No Factory-wide verdict, disposition, implementation or synthesis was performed.
