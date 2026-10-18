# Factory Part 2 — New Doctrine Intake

Version: 0.1 · Prepared: 2026-10-13, Asia/Dhaka · Author: JARVIS, intake Architect

**Status: DRAFT FOR INTAKE RECONCILIATION. Not approved sync cargo, an UPDATE MAP, a QA certificate or implementation authorization.**

## 1. Purpose and reading order

This package converts Tony's workflow, RRM and QAM uploads into three readable proposals while preserving the original sources. It supplements the existing `factory-corrections/` package. It neither replaces that package nor closes any FC finding.

Read in this order:

1. This index: authority, boundaries, dependencies and open decisions.
2. [01_FACTORY_WORKFLOWS_INTAKE.md](01_FACTORY_WORKFLOWS_INTAKE.md): creation, engineering, QA, deployment and review workflow.
3. [02_RRM_INTAKE.md](02_RRM_INTAKE.md): review findings → approved repairs → independent verification → closeout.
4. [03_QAM_INTAKE.md](03_QAM_INTAKE.md): prepared QA subpackages, roles, checkpoints, evidence and recovery.
5. [SOURCE_REGISTER.md](SOURCE_REGISTER.md): source IDs, filenames, dates/status and exact packaged paths. Original uploads are under `SOURCES/`; selected archive documents are also exposed under `EXTRACTED/` for convenient reading.

Stable proposal IDs are `WF-01…WF-12`, `RRM-01…RRM-10`, and `QAM-01…QAM-14`. They identify requested outcomes, not certified defects. Preserve these IDs when the sync skill assigns its own intake IDs; maintain a crosswalk. `ND-01…ND-07` are unresolved adoption questions; `GAP-01…GAP-05` identify evidence or locator gaps. Do not renumber FC or DEC records.

## 2. What is authoritative, proposed or historical

| Label | Meaning in this package |
|---|---|
| CURRENT SESSION DIRECTION | Tony's explicit instructions for this intake and its scope |
| REPORTED DIRECTOR RULING | An identified supplied source records Tony's ruling; retain its scope and attribution |
| FIELD RESULT | A supplied report/journal describes an observed outcome; not a new independent execution here |
| PROPOSED ADOPTION | Architect's recommended reusable outcome; approval still required |
| HISTORICAL / SUPERSEDED IN PILOT | Preserve as provenance; do not import its older rule as current merely because the file exists |
| OPEN / MISSING | Not established by the supplied evidence; do not fill with invented facts |

The intake briefs are outcome-level proposals, not exact replacement text. Claudy should classify them by content under the actual installed skill. If authorized to build an UPDATE MAP later, he must verify current Hub placements and draft exact proposed wording for approval. Historical source commands are evidence, not instructions to execute in this repository.

A newer document is not automatically higher authority. Explicit amendments with scope and provenance can supersede earlier instructions. A later proposal alone cannot overwrite a live approved contract. A successful experiment does not silently create Factory-wide policy.

## 3. Connection to the existing corrections

Repository: `~/Documents/app-factory-docs-v1` on Tony's VM. The latest supplied engineer report records branch work at HEAD `626da8d`, with no Git mutation during the scoped-approval task. This is historical evidence; discover current branch, full HEAD, worktree and main before any real sync. Do not use this short SHA as a current baseline.

The certified convergence checkpoint is `c6210c32480558b343a27726a26822e8d959d0f7`: 97 FC records, 17 families, 94 requiring correction and 3 already remediated. Those numbers describe convergence, not completed doctrine repair. The correction package's R1 content passed Architect revision review; the later R2 bookkeeping records five scoped approvals. This package does not contain a replacement copy of the correction briefs or the decision record.

Required repository references:

- `factory-corrections/FACTORY_DOCTRINE_CORRECTION_INDEX_001.md`
- `factory-corrections/DECISION_RECORD_001.md`
- The seven correction briefs linked from that index.
- The current sync family instructions and supporting taxonomy/templates, read from the actual authorized repository context.

`SRC-C01` is Claudy's supplied approval-record report, not the full decision record. Verify the latter on the VM. The five approvals remain narrowly scoped:

| Decision | Approved direction | Limit preserved |
|---|---|---|
| DEC-01 | One coordinated intake and dependency map; split when justified | Does not approve all proposed outcomes or authorize sync |
| DEC-02 | Remove unsafe live legacy examples first; complete verified replacements | Containment alone does not close the finding |
| DEC-03 | Webhook success follows completed work or durable acceptance; later workers use durable recovery | Do not acknowledge failed persistence/enqueue before acceptance |
| DEC-04 | Each privileged operation verifies caller, permission and target | Do not substitute layout admission for operation authorization |
| DEC-16 | Clear nine known lint findings, require green checks, retire merge-over-red guidance | No CI trigger expansion or baseline-gate alternative approved |

DEC-05, DEC-06…DEC-15 and DEC-17…DEC-22 retain their unresolved parts. The new material supplies evidence for several decisions; it does not silently mark them approved.

| New intake area | Existing correction interface | Why the link matters |
|---|---|---|
| Seats, lifecycle and authority | CF-01; FC-005/006/007; DEC-06/07 | One vocabulary and conflict-resolution model |
| Planning artifacts and design handoff | CF-02; FC-008/015/016/017/019/027; DEC-10/11/12 | Producer, timing, template and approval must agree |
| Recon, scope and module freeze | CF-03/04; FC-013/014/023/025/026/029; DEC-13/14 | Distinguish frozen contract, diagnostics and authorized output lanes |
| QA environments and evidence | CF-05; especially FC-022/024/030 | Honest evidence, valid fixtures, authorized target and side effects |
| DevOps and Git authority | CF-14; FC-011/012/088; DEC-17/18 | Project delivery rules and Hub sync exceptions are contextual |
| Locators and distribution | CF-13/15/16; FC-009/087/088/093 | New playbooks/templates need resolvable references and accurate indexes |

These are overlap pointers verified against the R1 correction index/briefs, not exhaustive propagation results. Security, auth, data, commerce and design corrections outside these overlaps remain in the original package without reduction.

## 4. Chronology that must survive consolidation

| Period/source | What it establishes | Treatment |
|---|---|---|
| 2026-08-24 workflow operating models, SRC-W05…W07 | FFM/BIM/DevOps contracts, reported rulings, pending proposals | Substantial draft inputs; not blanket approved doctrine |
| 2026-09-17 RRM pilot, SRC-R01 | Reusable RRM playbook and templates; pilot not yet delivered | Base procedure plus original review evidence |
| 2026-09-29 QAM pilot plan, SRC-Q04 | Controlled RRM-004 experiment using older QA folder/plan sequence | Historical design stage |
| 2026-09-30 proposal and original RRM-004 pack | Skeleton/facts/plan split; original `QA/` launch package | Do not mistake blank templates for completed results |
| 2026-09-30…10-01 rulings, SRC-R03/R04/Q02 | QAM overlay, Executor plan draft, automated login, dual entries and checkpoint packaging | Trace each explicit amendment and its scope |
| 2026-10-02 master draft and campaign report | Product Gate Q PASS; QAM PARTIAL SUCCESS; reusable proposals and limitations | Strong synthesis input, still experimental |
| 2026-10-12 correction approval report, SRC-C01 | Five scoped correction directions recorded | Preserve exact limits |
| 2026-10-13 current intake | Tony requests combined workflow/RRM/QAM review and downloadable intake | Authorizes preparation; broader adoption remains to be decided |

The RRM-004 Q2 execution succeeded with zero reported in-run Director interventions. The pilot's formal PARTIAL SUCCESS result remains because Q1 required a scope correction. Do not rewrite that score or equate a ten-minute Q2 body with the complete lifecycle.

## 5. Proposed adoption decisions

Recommendations below are not additional gates to be run one by one. Consolidate them with existing DEC questions and ask Tony only for unresolved policy choices after source reconciliation.

| ID | Question and recommendation | Connection |
|---|---|---|
| ND-01 | What QAM scope should this sync propose? Recommend a reusable QAM playbook with explicit adoption status and project applicability. Do not auto-enable experimental mechanisms for all client work. | QAM-01/14; DEC-07/13 |
| ND-02 | Which review workflow applies to mainstream Factory work? Reconcile the three-engine draft with the separate later 10X two-engine direction before making phase/release reviews universal. | WF-11; RRM-01 |
| ND-03 | Do FFM DATA_CONTRACT timing and UI_SPEC ownership receive the source's proposed roles? Recommend pre-design approved data shapes and Architect final assembly; UI_SPEC ownership still needs explicit reconciliation. | WF-03/04; DEC-10/11/12 |
| ND-04 | How should QA execution and cleanup be generalized? Recommend capable Executor automation under QA Lead approval, plus an explicit cleanup-before-final-certificate sequence for adopted QAM packs. Preserve other live approved sequences until amended. | WF-07; QAM-05/10; DEC-13/14 |
| ND-05 | Where do new operating models, RRM/QAM playbooks and kits belong? Recommend one owning document per subject, with linked templates and diagrams. Verify Hub tiers/paths; avoid parallel competing canons. | WF-12; RRM-10; QAM-13; DEC-17/19/21 |
| ND-06 | Which DevOps authority and platform rules become general? Recommend explicit context/action/seat matrix, Cloud Run instructions scoped as one platform profile. | WF-08/09; DEC-18 |
| ND-07 | Should one-shot engineering become a default? Recommend an optional prepared run shape when scope and environment permit; record total preparation/coordination cost. Two successful examples do not establish a universal default. | RRM-08; QAM-12 |

## 6. Known gaps and what they block

| ID | Gap | Consequence / smallest resolution |
|---|---|---|
| GAP-01 | `RRM_CAMPAIGN_v1.0.zip` has directories only | Inventory as empty scaffolding; use supplied campaign report for attributed history. Obtain current campaign ledger/map only if needed for a specific unresolved claim. |
| GAP-02 | Original RRM-004 pack has unfilled execution/results forms; final QAM certification and completed results are referenced, not supplied as standalone records | Enough for proposal drafting and attributed results; insufficient to present this ZIP as the complete certified worked example. Request a sanitized final evidence/closeout export if publishing that example. |
| GAP-03 | QAM master draft references `01_EVIDENCE_DOSSIER.md` and `TEMPLATES/`, absent from these uploads | Record missing companions. Source text is enough to author proposed replacements, labeled newly authored; do not claim the originals were received or tested. |
| GAP-04 | Actual VM intake path and installed skill format pending Claudy's preparation report | Package remains portable with internal relative paths. Adapt placement after that report, without changing policy meaning. |
| GAP-05 | Some inherited sources and current external kit/skill counterparts are not in these batches | Use repository discovery for real targets; park inaccessible external changes rather than inventing sections or approvals. |

The standalone QAM Architect journal may duplicate the copy inside the RRM bundle. `SOURCE_REGISTER.md` records byte comparison. Both original uploads are retained as provenance; do not count repeated text as independent corroboration.

## 7. Boundaries and preservation requirements

- Mainstream corrections remain one coordinated campaign unless dependencies justify a split. Do not merge the historical review branch wholesale into main.
- ABM/APBM-specific proposals remain on the separate 10X track. Vibe Engineering remains Cyber Pharma pilot-specific. Mentioning those classes in a source does not expand this campaign.
- RRM and QAM reusable procedures must not inherit Cyber Pharma business rules, dependency versions, role names, environment targets, phase numbers or merge strategy as universal defaults.
- Preserve original reviews, journals and issued certificates byte-for-byte. New summaries cite them; later rulings append or live separately.
- Source labels such as “Tier 1,” “canonical,” “ratified,” or “all modules” are claims with context, not authority to overwrite Hub rules.
- Skill directories, root instruction changes, CI/lint implementation and other repositories follow existing cross-boundary jobs. Intake analysis may identify these dependencies without editing them.
- A playbook's proposed automation is not a delivered validator/exporter/runtime. Do not build a new tooling project merely to complete documentation intake.
- The current Claudy task only prepares the drop folder and reports requirements. Receipt of this package does not activate the full sync or authorize Git mutations.

## 8. Next authorized-stage proposal

After Claudy reports intake requirements, place the package using those conventions. Preserve originals and classify each proposal. Reconcile the existing correction package and decision record, verify current canonical targets, and return one combined decision list and dependency map when Tony authorizes that analysis. Formal intake approval, exact-wording UPDATE MAP approval, the independent sync acceptance specification, implementation, QA and publication follow the current skill's gates.

Acceptance of these intake documents should mean that every proposal has a source, status, target intent, preservation requirement and decision route. It must not mean that all proposed rules have already been adopted.
