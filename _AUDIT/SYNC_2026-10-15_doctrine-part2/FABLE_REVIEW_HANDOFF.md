# Revised Phase 2 review handoff — MC correction pass

**DRAFT FOR JARVIS REVIEW AND FABLE SPECIFICATION FINALIZATION. Gate 2 remains unapproved; Phase 3 is not released.** Prepared by Cody, Engineer, under Tony’s explicit 2026-10-16 correction assignment. QA Lead: Fable. Architect: Jarvis. All Git mutations remain Tony’s.

Supersedes the earlier review package `FACTORY_PHASE2_FABLE_HANDOFF_2026-10-16_164712.zip`, SHA-256 `87d37eb0cde8130c3730c23fb132234bb24f7181c771b8947daa2505a70f9973`. That original is retained unchanged on Tony’s machine; its review and prior proof remain history. The current material is a correction to the same run, not restarted intake or repeated template acceptance.

## Start here

1. [MC_CORRECTION_DISPOSITIONS.md](MC_CORRECTION_DISPOSITIONS.md): one record for all MC-01…14, exact changes, evidence, pending future conditions and specification re-anchoring needs.
2. [FABLE_MAP_REVIEW_2026-10-16.md](FABLE_MAP_REVIEW_2026-10-16.md) and [DOCSET_SYNC_ACCEPTANCE_SPEC.md](DOCSET_SYNC_ACCEPTANCE_SPEC.md): Fable’s full originals, byte-preserved. Her DRAFT specification refers to the earlier proposal; Cody has not edited or finalized it.
3. [UPDATE_MAP.md](UPDATE_MAP.md), [SELECTED_SCOPE_LEDGER.md](SELECTED_SCOPE_LEDGER.md), [EXTERNAL_FOLLOWUPS.md](EXTERNAL_FOLLOWUPS.md), [DIRECTOR_RULINGS_2026-10-16.md](DIRECTOR_RULINGS_2026-10-16.md), [MC_CORRECTION_AUTHORITY.md](MC_CORRECTION_AUTHORITY.md).
4. [EXECUTION_PROPOSAL_INDEX.json](EXECUTION_PROPOSAL_INDEX.json), [EXECUTION_PROPOSAL.patch](EXECUTION_PROPOSAL.patch), `PROPOSED_CONTENT/`, [SELECTED_EXACT_EDITS.json](SELECTED_EXACT_EDITS.json): 101 paths and 372 ordered content edits, all proposed. [PROPOSAL_COUNTS.json](PROPOSAL_COUNTS.json) derives the current counts.
5. [WORKFLOW_PUBLICATION_PLAN.json](WORKFLOW_PUBLICATION_PLAN.json): four revised workflow documents and four stick-actor SVGs. Each has explicit original-source provenance and supersession conditions. The eight paths explain 93 →101; four publication rows explain CHANGELOG 35 →39. Tier count remains 34.
6. [POST_VERIFICATION_STATUS_TRANSITIONS.json](POST_VERIFICATION_STATUS_TRANSITIONS.json), [POST_VERIFICATION_PROPOSAL_INDEX.json](POST_VERIFICATION_PROPOSAL_INDEX.json), [POST_VERIFICATION_PROPOSAL.patch](POST_VERIFICATION_PROPOSAL.patch): twelve conditional edits on nine paths, including the three MANIFEST rows. The intended Tony closeout commit is named by purpose; actual SHA and future evidence remain PENDING. `CLOSEOUT_PROPOSED_CONTENT/` is a simulation only.
7. [MC_VERIFICATION.json](MC_VERIFICATION.json), [MC_VERIFICATION_RAW.txt](MC_VERIFICATION_RAW.txt), [MC_DETERMINISTIC_REBUILD.json](MC_DETERMINISTIC_REBUILD.json), [MC_REBUILD_RAW.txt](MC_REBUILD_RAW.txt), [MC_PROPAGATION.tsv](MC_PROPAGATION.tsv), [MC_DIAGRAM_RENDER.json](MC_DIAGRAM_RENDER.json), [EVIDENCE_STATUS.md](EVIDENCE_STATUS.md): Engineer checks and retained evidence boundaries.
8. [OPERATOR_NEXT_STEPS.md](OPERATOR_NEXT_STEPS.md), [PHASE_PLAN.md](PHASE_PLAN.md), [LANDING_DATE_PLAN.json](LANDING_DATE_PLAN.json), [WORKFLOW_RULING_TRACEABILITY.json](WORKFLOW_RULING_TRACEABILITY.json).

## Revised workflow documents and original sources

| Revised document | Revised stick diagram | Preserved original |
|---|---|---|
| [FFM creation](PROPOSED_CONTENT/03_BUILD_METHODOLOGY/_workflows/FFM_CREATION.md) | [SVG](PROPOSED_CONTENT/03_BUILD_METHODOLOGY/_assets/workflows/FFM_CREATION.svg) | [SRC-W01](INTAKE_SNAPSHOT/factory-intake/SOURCES/Workflow/SRC-W01_FFM_CREATION.png) |
| [FFM execution / post-FFM review](PROPOSED_CONTENT/03_BUILD_METHODOLOGY/_workflows/FFM_EXECUTION.md) | [SVG](PROPOSED_CONTENT/03_BUILD_METHODOLOGY/_assets/workflows/FFM_EXECUTION.svg) | [SRC-W02](INTAKE_SNAPSHOT/factory-intake/SOURCES/Workflow/SRC-W02_FFM_EXECUTION.png) |
| [Deployment / Gate D](PROPOSED_CONTENT/03_BUILD_METHODOLOGY/_workflows/FFM_DEPLOYMENT.md) | [SVG](PROPOSED_CONTENT/03_BUILD_METHODOLOGY/_assets/workflows/FFM_DEPLOYMENT.svg) | [SRC-W03](INTAKE_SNAPSHOT/factory-intake/SOURCES/Workflow/SRC-W03_FFM_DEPLOYMENT.png) |
| [BIM / Engine 2](PROPOSED_CONTENT/03_BUILD_METHODOLOGY/_workflows/BIM_WORKFLOW.md) | [SVG](PROPOSED_CONTENT/03_BUILD_METHODOLOGY/_assets/workflows/BIM_WORKFLOW.svg) | [SRC-W04](INTAKE_SNAPSHOT/factory-intake/SOURCES/Workflow/SRC-W04_BIM_WORKFLOW.png) |

`MC_EVIDENCE/diagram_previews/` contains rendered review PNGs. They are review evidence, not extra implementation paths. Published-path references inside proposal documents resolve in the intended canonical repository namespace after actual landing; the links in this table resolve directly inside the extracted review package.

## Scope and verification

101 paths =31 revised existing tier documents +3 new playbooks +25 templates +32 archives (31 outgoing, one restored history) +MANIFEST/CHANGELOG +4 workflow documents +4 SVGs. All 97 FC identities, certified severities and 94 YES /3 NO correction flags remain unchanged. There are 89 selected canonical component rows, five outside rows and three NO guards; partial external work remains separately tracked.

Fable independently verified the earlier package’s counts, archives, edits, templates and lints. Those results are preserved. Current Engineer checks repeat the changed structure/hashes/workflow/count relationships; they are not her acceptance. Template source acceptance is settled, source bytes unchanged and the current 25-file translation replay is exact. Actual installed-translation verification remains a later candidate requirement. The 151 date fields are proposed mechanical bindings, not an actual landing date. No runtime, platform, kit or accessibility certification is claimed.

`TEMPLATE_INSTALL_PLAN.md/json` are visibly historical. Current template hash authority is `PHASE_2_TEMPLATE_TRANSLATIONS.json`, with the one later README provenance transition explicitly recorded. `TEMPLATE_INSTALL_CHECKS.md` retains required installation checks. No actual `TEMPLATE_INSTALL_VERIFICATION.md`, `RUN_SUMMARY.md`, `CLOSEOUT_VERIFICATION.md` or closeout SHA has been fabricated; `EVIDENCE_TEMPLATES/` contains forms only.

## Review sequence and remaining gates

Jarvis reviews the corrected map/dispositions. Fable confirms corrections and re-anchors/finalizes her DRAFT specification against the approved exact map, including changed counts, workflow assets, traceability, preserved statuses and twelve conditional closeout spans. Her old AC28 “no new assets” must reconcile with Tony’s explicit new workflow/diagram requirement; only Fable edits her specification. Tony approves Gate 2 and then the finalized independent spec at Gate 3. Tony supplies preservation/remote-baseline/worktree receipts; Cody verifies setup and the implementation release before Phase 3 begins.

The closeout proposal requires actual install verification, an accepted exact product verdict, required cleanup acceptance and Architect instructions before Tony’s named bounded commit. Independent retest covers AC25/27/31/32/33, all twelve spans/nine paths, templates and workflow references. The later QA Lead verdict must name the actual later candidate. The run-only single implementation commit exception remains; necessary preservation/QA-repair/closeout commits remain possible.

## Export provenance and recovery

`BASELINE_CONTENT/` contains exact canonical before-images from main `9c179392f79b70da099121fc357d3107ad3bb86e`. `GOVERNING_SKILL_MAIN/` contains the governing main skill instructions exported read-only, with Tony’s current seat/Git/commit instructions taking precedence. `INTAKE_SNAPSHOT/` has 189 unchanged files. `DRAFTS/`, certified review records and `PLANNING_HISTORY/` preserve prior sources/work; older counts/statuses there are historical.

Current generators are the `cody_mc_*` scripts and `MC_GENERATORS.md` under `scratchpad/generators/`; older phase generators are retained recovery history. Do not execute any proposal as canonical implementation during this review. Inventory files cover every payload file except their own self-referential entries; ZIP integrity and all payload hashes are checked before delivery.
