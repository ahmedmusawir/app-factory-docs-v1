# Factory Workflows — Consolidated Intake Brief

Version: 0.1 · Date: 2026-10-13, Asia/Dhaka · Author: JARVIS, intake Architect

**Status: PROPOSED OUTCOMES FOR RECONCILIATION. No canonical edits or adoption approval.**

Read [00_MASTER_INDEX.md](00_MASTER_INDEX.md) for common authority, source status, correction interfaces and boundaries. Source IDs resolve through [SOURCE_REGISTER.md](SOURCE_REGISTER.md).

## 1. Objective

Make the Factory's operating sequence understandable from idea through creation, implementation, independent QA, release and deployed verification. A reader must know who decides, who executes, which artifact crosses each boundary and what evidence permits the next step.

The four uploaded diagrams provide visual orientation. The three operating models provide much of the detailed contract, including their own amendment ledgers and open questions. They were authored in August and must be reconciled against September RRM practice and later QAM rulings. The smaller text diagrams are additional proposals, not self-executing policy.

## 2. Proposal ledger

### WF-01 — Seats and human authority

**Source:** SRC-W05 §2/9/10; SRC-W06 §2/10; SRC-W07 §2/10; later SRC-Q03 §§4–5. **Status:** source-reported rulings plus proposed Factory consolidation. **Correction link:** FC-006, DEC-07.

Define Director/Operator/Coordinator terminology once. One human may occupy Development, QA, DevOps and release-authority chairs; the responsibilities remain distinct. Define Architect, Engineer, QA Lead, QA Executor and DevOps functions by responsibility rather than permanent model assignment. Claudy/Cody/Jarvis/Sol/Fable are contextual occupants, not permission sets.

QA Lead owns the evidence verdict; Director owns scope/access/release decisions. Engineer self-checks remain engineering claims. QA independence requires a separate session/context as applicable; naming the same persona in different seats does not waive independence.

**Preserve:** human release authority; separate QA judgment; Designer function; DevOps responsibility. **Verify:** all rosters, diagrams and module instructions use the same seat vocabulary and identify context-specific exceptions. Avoid importing the old pilot plan's isolated “human QA Lead” phrase as a change from the supplied AI-advisory QA Lead/human Director model.

### WF-02 — Recon before authoring, with an executable boundary

**Source:** SRC-W05 §3; SRC-W06 §3; SRC-Q03 §8/9. **Status:** existing principle requiring clarification. **Correction link:** FC-014/023, DEC-14.

Require current repository evidence before authoring scope. Disk establishes implementation facts, not permission to change approved requirements. An observed conflict with scope or policy goes to its owner.

Replace absolute “nothing is created” wording with explicit lanes: recon report and normal response/session/recovery bookkeeping; authorized diagnostics that may create build/cache output; and prohibited product/contract modifications. Name permitted diagnostics and cleanup rather than claiming every build is read-only. For pre-authored BIM sets, revalidate each module's assumptions against its actual execution baseline.

**Preserve:** no implementation before approval; no speculative improvement during recon. **Verify:** a fresh Engineer can collect and save the required evidence without violating the same document's no-write rule.

### WF-03 — Planning artifact ownership and timing

**Source:** SRC-W05 §4/11/12 B-1, B-2, E-1 and §13; SRC-W01. **Status:** DATA_CONTRACT ownership is reported as ruled in the source; UI_SPEC final ownership explicitly remains proposed. **Correction link:** FC-008/015/016/017/019/027, DEC-10/11/12.

Propose a complete producer/consumer/approval table for APP_BRIEF, DATA_CONTRACT, UI_SPEC and any required FILE_TREE. The August model places greenfield DATA_CONTRACT authorship with the Software Architect before Design. Designer receives approved product intent and data shapes, with typed mocks permitted behind the service seam. Do not allow unapproved design fields to become backend requirements by accident.

The source proposes Designer ownership of final UI_SPEC, reviewed by the Architect. Reconcile this with the existing “Architect drafts, Designer revises” contract and decide explicitly. Decide whether FILE_TREE remains mandatory and, if retained, who produces it and when. Distinguish project component manifest from Factory component registry. Resolve pipeline-specific variations instead of forcing incompatible flows into one template.

**Preserve:** approved data contract, design approval, clear artifact status and recipient completeness checks. **Verify:** each required artifact has a real template/producer, no circular handoff, and no unresolved authoring ownership disguised as an approved rule.

### WF-04 — Architect assembles and freezes the integrated FFM

**Source:** SRC-W05 §4.1–4.4 and amendment B-3; SRC-W01. **Status:** source-reported ruling proposed for consistent propagation. **Correction link:** CF-02/04, FC-025/026, DEC-13.

Return Designer and extraction outputs to the Architect for final assembly, completeness verification and contract freeze before Engineer handoff. The simplified diagram's two streams joining a folder do not eliminate this responsibility.

Retain approved tokens, style tile, screen artifacts, UI_SPEC and component inventory. HTML/PNG obligations apply according to the actual interface/design contract, not indiscriminately to non-visual modules. Preserve the kit infrastructure exception: use complete kit auth primitives directly rather than inventing a redundant project auth service.

Freeze the approved contract; allow declared engineering handoff, QA evidence, rulings and retrospective lanes. A whole-folder immutable rule cannot coexist with required in-folder outputs.

**Verify:** the package contains explicit entry/read order, complete dependencies, approved acceptance requirements and an allowed-output map. Diagram and prose must both show Architect assembly.

### WF-05 — Engineering completion includes handoff

**Source:** SRC-W05 §§5–6; SRC-W06 §§5–6; SRC-Q03 §§5/8. **Status:** proposed consolidation. **Correction link:** FC-025/026 and CF-02.

Retain Plan Mode, approved scope, bounded implementation, internal checks and self-verification. Acceptance requirements come from the pre-build approved contract. Engineer maintains factual completion claims and may propose errata, but cannot redefine success to fit the implementation.

The original engineering assignment includes the complete QA handoff: candidate reference to be resolved after commit, changed files, environment, reproduction, engineering results, known limitations and factual QAM manifest where applicable. No routine extra mission is needed solely to write that handoff.

**Preserve:** internal Development gates distinct from independent Gate Q; Director Git authority under applicable project rules. **Verify:** QA can reconstruct how to run the candidate and identify which statements are claims rather than independent results.

### WF-06 — BIM campaigns and lifecycle terminology

**Source:** SRC-W06 §§1/4/5/9; SRC-W04. **Status:** proposed consolidation with glossary reconciliation. **Correction link:** FC-007 and CF-02.

Retain sequenced, bounded BIM work; allow author-all-upfront or plan-names/author-just-in-time when the Director chooses. Execution baseline recon and retrospective learning remain meaningful in both patterns. A pre-authored future module is revalidated when released for execution.

The uploaded model expands BIM as “Backend Integration Module”; other campaign usage includes “Backend Implementation Module.” Reconcile the current Hub glossary and Director usage rather than globally replacing the acronym's expansion from one source. Likewise, distinguish product phases, module internal stages, Factory CREATE/MATURE/OPERATE loops and the proposed review engines. They are different axes, not interchangeable numbering.

**Verify:** one lifecycle crosswalk explains module vs phase vs gate; workflow diagrams do not imply mandatory FFM for every backend-only project.

### WF-07 — QA execution by evidence needs

**Source:** SRC-W05 §7; SRC-W06 §§7–9; SRC-Q03 §§4/8/17. **Status:** older FFM human-execution rule conflicts with later QAM practice; adoption scope open under ND-01/04.

The August FFM model uses human browser execution and reserves Codex for technical checks. Later RRM reports demonstrate agent browser matrices. Propose that the QA Lead allocates checks according to tool capability, evidence needs and authorized environment. Human product/visual judgment stays where it adds value; repetitive matrices need not default to Tony.

Retain independent plan approval and verdict. Define the active certification branch and cleanup sequence explicitly. The old BIM “abandon QA branch by default” rule is superseded in the supplied RRM/QAM lineage by a forward-moving QA line carrying approved repairs and durable certification records.

**Verify:** QA never edits product code under its execution role, never self-certifies, and never treats automation capability as permission for broader side effects. Do not retroactively reorder an already approved live module.

### WF-08 — DevOps as a shared function

**Source:** SRC-W07; SRC-W05 §8; SRC-W03. **Status:** proposed owning doctrine, several reported prior rulings. **Correction link:** FC-011, DEC-18.

Use a DevOps contract covering deployment readiness, package authoring, authorized execution, release identity, rollback planning and Gate D evidence. Identify Director, Architect and Engineer responsibilities. Separate QA verdict from release authorization and deployment execution.

The supplied model's Cloud Run package uses `init-app.sh`, `cloudbuild.yaml`, `Dockerfile`, `deploy.sh` and a checklist. Correct the diagram's older filenames if this profile is adopted. These are profile-specific names; do not impose them on Vercel or Python deployments. Classify secrets by build/runtime use and public/server-only exposure, and identify human, build-service and runtime actors.

**Preserve:** no implied cloud authority, exact deployed revision, Gate D separate from build/health checks. **Verify:** platform profiles point to real mechanisms and required approval; version-sensitive technical commands are verified at implementation time, not copied from August as current advice.

### WF-09 — Deployment identity, rollback and redeployment limits

**Source:** SRC-W07 §§3/6–9/13; SRC-W05 §§8–9. **Status:** proposed correction to overbroad source wording. **Correction link:** CF-14, DEC-17/18.

Record repo → commit → build/image → deployed revision → environment → route/domain identity as applicable. Preserve the tested-product equivalence check through documentation-only successors. Gate D verifies the actual target revision.

Do not generalize “redeploy runs Phase 3 only” without checking changed configuration, secrets, permissions, migrations and deployment prerequisites. Do not promise traffic rollback plus Git revert restores all data or external effects. Require a rollback or recovery plan suited to the changed surfaces, with operator responsibility and evidence.

The source explicitly leaves staging-to-production promotion and monitoring/incident detection incomplete. Record those gaps and scope decisions; do not claim this intake supplies a complete operations manual.

### WF-10 — Context-specific Git and sync authority

**Source:** SRC-W05 §5.2; SRC-W06 §6; SRC-W07 §2; SRC-W10; existing correction index. **Status:** reconciliation required. **Correction link:** FC-012, DEC-18/21.

Use a context × action × seat matrix. Project engineering's Director-controlled Git/cloud rules do not erase the sync skill's bounded Hub-specific Git exception; the exception does not grant arbitrary project Git/cloud permission. Explicit current task instructions remain controlling: the present folder-preparation task authorizes no Git mutations or full sync.

Project `--no-ff` examples are not universal Hub merge policy. The doc-sync flow must follow the installed skill and Director gates. Include post-merge local main refresh and branch-baseline verification in the appropriate workflow so GitHub merge is not mistaken for local synchronization. Preserve uncommitted work before switching or pulling.

### WF-11 — Review engines, targeted repair and certification

**Source:** SRC-W08/W09/W11; SRC-R01/RRM_PLAYBOOK.md; current campaign boundary. **Status:** scope decision ND-02; supporting concepts proposed.

The three-engine text proposes per-module build/QA, per-phase review/improvement and final whole-application review. Other later 10X direction described review after all implementation phases. Do not conflate these or automatically add every review stage to mainstream projects. Present the alternatives with their intended scope to Tony.

Where review is approved, preserve the useful sequence: identify/freeze specimen, obtain independent review evidence, adjudicate material findings, approve bounded repairs, verify those repairs and required regression. Original reviewer re-review is conditional on the approved verification plan, not an unqualified rule that every issue requires the same old session.

A review “both PASS” arrow is insufficient to define Gate Q, Gate D or release authority. RRM handles accepted rework; QA certifies the approved contract; Director releases. Define any phase/application certificate separately before using that label.

### WF-12 — One owning document and synchronized visuals

**Source:** all workflow sources and their amendment ledgers. **Status:** placement proposal ND-05. **Correction link:** CF-13/16, FC-009/087/093.

Determine whether FFM/BIM operating models become separate adopted docs or feed their existing playbooks. A DevOps owning document is a candidate to fill FC-011. Avoid creating two normative explanations with overlapping but conflicting authority. Link specialized RRM and QAM procedure from the general workflow rather than copying their entire contents.

Keep the original diagrams as historical sources. If revised diagrams are in scope, make their source editable and label simplified views clearly; the approved textual contract governs omitted detail. Correct missing recon, Architect assembly, module-close QA, Gate Q/release/Gate D transitions, current seat labels and deployment filenames where relevant. Verify links, headers, indexes and assets under actual Hub conventions.

## 3. Likely targets and acceptance expectations

Candidate targets: SOFTWARE_FACTORY_PLAYBOOK, APP_FACTORY_BLUEPRINT, ARCHITECT_PLAYBOOK, ENGINEER_PLAYBOOK, DESIGNER_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, FFM_PLAYBOOK, BIM_PLAYBOOK if present, QA_PLAYBOOK, TESTING_PLAYBOOK, design-system references and a DevOps owning document. Exact paths/versions are for current repository discovery. Root instructions, skill implementations and external deployment tools require separately scoped work.

The eventual map should demonstrate: one seat vocabulary; one lifecycle crosswalk; complete artifact producers/consumers; explicit freeze/output boundaries; independent QA; contextual Git/cloud authority; coherent deploy/Gate D responsibility; and all diagrams/examples consistent with the adopted rules. Existing security and design protections must survive. No statement in this brief approves a new release process or fills the open promotion/monitoring gaps by implication.
