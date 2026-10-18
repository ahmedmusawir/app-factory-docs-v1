# Review Rework Modules — Consolidated Intake Brief

Version: 0.1 · Date: 2026-10-13, Asia/Dhaka · Author: JARVIS, intake Architect

**Status: PROPOSED ADOPTION / RECONCILIATION. An RRM pilot playbook exists; canonical promotion is not yet approved.**

Common rules: [00_MASTER_INDEX.md](00_MASTER_INDEX.md). Sources: [SOURCE_REGISTER.md](SOURCE_REGISTER.md). QA packaging interface: [03_QAM_INTAKE.md](03_QAM_INTAKE.md).

## 1. What RRM contributes

RRM means Review Rework Module in the supplied pilot playbook. It converts adjudicated review findings into bounded engineering work and independent verification. It can apply to completed frontend, backend or cross-cutting work. It does not consume the next BIM's identity or renumber the product plan.

The original September pilot contains an RRM playbook, reviewer guidance, module templates and a proposed doc-set change map. October campaign reports add field lessons. Use the first as the procedure's starting point and the latter as attributed evidence for refinements. The original review archives are historical inputs; this documentation task does not commission a fresh review of Cyber Pharma code.

## 2. Evidence and its limits

| Supplied source | What it provides | What it does not provide |
|---|---|---|
| SRC-R01: factory pilot ZIP | Actual RRM_PLAYBOOK.md, reviewer candidate, kit, change map and original review ZIPs | Completed RRM certification at its 17 September publication |
| SRC-R02: RRM-004 v1.0 pack | Concrete dependency-module contract and original QAM pilot layout | Filled execution/results forms or the later QAM overlay/certificate |
| SRC-R03: Architect bundle | Campaign metrics, RRM-003 field note, QAM authorship opinion/proposal and journal | All original machine evidence or final merge attestation |
| SRC-R04: QA observation journal | QA-side lessons and explicit later packaging requirements; Q1 observations | Final RRM-004 product certificate in this supplied journal version |
| SRC-R05: campaign ZIP | Empty directory scaffold | Campaign map, ledger, rulings or module contents |
| SRC-Q03: QAM master draft | QA-authored synthesis reporting Gate Q PASS and cleanup acceptance | The referenced separate evidence dossier/templates |

The Architect's 2 October report records RRM-001…004 Gate Q passes with zero repair rounds. RRM-003 engineering is reported as 11m54s, 67 checks, no stops and no in-run Director touches. RRM-004 engineering is reported as 11m15s, 80 checks, no stops or in-run touches; Q2 QA body 10m08s, release elapsed 17m21s excluding Q1. These are source-reported measurements, not new measurements here. Work profiles differ; no universal speed multiplier follows.

RRM-004 product candidate is reported as `2fbc72f1f514049255f2b94054bd11cc77cbd158`. The journal reports product Gate Q PASS and QAM pilot PARTIAL SUCCESS. Its final entry still lists merge/rotation/adoption records as open. Do not infer current incompletion or completion from that old entry: later records would settle the present state. A fully certified worked-example export remains GAP-02.

## 3. Proposal ledger

### RRM-01 — Route accepted findings into a bounded module

**Sources:** SRC-R01/RRM_PLAYBOOK.md §§1–4; reviewer candidate; SRC-W08/09. **Status:** pilot procedure proposed for adoption.

Require current-source reconciliation before turning a historical report into a work order. Preserve reviewer IDs, specimen identity, evidence level, uncertainty and limitations. Both reviewers agreeing is not proof; a finding from only one reviewer is not automatically weak. Separate severity, origin and approved scope. An inherited issue may be severe and still require an explicit disposition.

Use ACCEPT REPAIR, NEEDS DECISION/EVIDENCE, DEFER/FUTURE GATE, REJECT/NOT APPLICABLE/ALREADY RESOLVED and DUPLICATE with evidence and reasons. A deferral identifies owner and trigger. Accepted risk requires the Director's recorded decision. Scope comes from accepted objectives, not raw finding counts.

**Preserve:** raw reports unchanged; review timing follows the approved project workflow, not a new universal engine rule. **Verify:** every material finding has a retained identity and disposition; no raw review item silently becomes an authorized edit.

### RRM-02 — Freeze the repair contract before implementation

**Sources:** SRC-R01/RRM_PLAYBOOK.md §§4–5; module kit; SRC-R03 campaign report §6. **Correction interface:** FC-013/025/026, DEC-13.

The Architect proposes a module with brief, findings ledger, acceptance requirements, preserved behaviors, permitted surfaces, forbidden scope, environment and verification needs. Director approves. Acceptance exists before build; Engineer may challenge ambiguity through an explicit errata lane, not silently redefine it.

Freeze authority inputs and preserve amendment provenance. Engineering logs, QA artifacts and retrospective outputs remain writable in declared lanes. Mid-flight QAM changes in RRM-004 were recorded as an overlay with append-only rulings; use this as evidence for traceable amendment, not a command to repeat that costly overlay on every future pack.

**Verify:** finding → approved objective → AC → repair → independent result → final disposition can be followed end to end.

### RRM-03 — Establish current baseline and complete preflight

**Sources:** SRC-R01 §§2/6; SRC-R03 engineering report §§3/5; SRC-R02 preflight. **Correction interface:** FC-014/022/030, DEC-14.

Inspect current code, dependencies, environment and permissions before authoring/execution. Resolve full baseline identity at the appropriate checkpoint. A placeholder such as “previous module merge” is not sufficient at certification. Keep the candidate separate from docs/evidence successors.

Preflight rows should measure prerequisites relevant to the module: route status, environment reachability, expected identities, supported library access, builds and evidence tools. Avoid unmeasured constants and stale registry claims. Do not mandate an entire scratch implementation by the Architect for every task: validate risky assumptions in proportion to the actual uncertainty.

**Verify:** failure produces a specific blocker before expensive execution; read-only inspection, diagnostics and write boundaries are described truthfully.

### RRM-04 — Prepared engineering run and same-assignment handoff

**Sources:** SRC-R01 §§5–6; SRC-R03 report §§3–5; SRC-Q03 §5/8.

Retain Plan Mode and Director-approved rulings. Permit continuous execution through already authorized stages, with bounded self-repairs and enumerated material stops. A new unexpected authority/safety conflict still stops; an incomplete list cannot authorize guessing. Ordinary progress does not require repeated permission prompts.

Finish with changed-file inventory, product/configuration diff, engineering checks, limitations, environment/reproduction instructions and factual QA handoff. If QAM is adopted for that module, complete its manifest. Report unresolved values explicitly; Director commit establishes the immutable candidate.

**Preserve:** narrow scope, no weakening tests to claim green, engineering claims distinct from QA evidence. **Verify:** handoff can enter QA without another prompt asking for basic readiness documents.

### RRM-05 — Independent QA and the QAM interface

**Sources:** SRC-R01 §7; SRC-Q03 §§4–8; SRC-R03 QAM authorship opinion.

RRM defines repair objectives and protected behavior. QAM, where approved, packages independent verification; it is not a second engineering module or a replacement scope contract. QA Lead owns plan approval and certification; QA Executor drafts and executes within that approval. Architect supplies risks and scope, Engineer supplies facts, neither pre-grades the independent result.

Tests must reach the boundary claimed. Function probes do not automatically prove HTTP/framework behavior; synthetic data does not establish deployed RLS. Require only the environments/checks justified by the approved contract and risk plan, and report limits honestly. Targeted original-reviewer re-review is used where explicitly required or useful, not to force reopening an unavailable session.

### RRM-06 — Forward certification line and bounded repairs

**Sources:** SRC-R01 §§6–8; SRC-Q03 §12; SRC-R03 journals. **Status:** later lineage supersedes the August disposable-branch rule for these campaigns.

Normal pattern: approved main baseline → engineering branch → active QA branch → integration under project policy. After handoff, approved QA-driven repairs stay on the QA line. Engineer repairs; QA Executor measures. Use one active writer when sessions share a worktree.

QA Lead classifies product defect, contract gap, environment blocker, instrument issue or observation. Architect/Director rule actual repair scope; Engineer implements; Director commits; QA re-pins and checks the diff, affected ACs and required regression. Carry forward evidence only with explicit candidate/environment validity reasoning. Helper corrections are logged as instrument events, not disguised product repairs.

**Limit:** RRM-004 did not exercise a product repair round. The generalized QAM repair mechanism remains a proposed procedure until supported by additional evidence. Do not invent a successful Q4 from a zero-repair campaign.

### RRM-07 — Certification, cleanup, closeout and integration

**Sources:** SRC-R01 §9; SRC-Q03 §§8/15; SRC-R03 final journal entry. **Correction interface:** DEC-13/18 and CF-14.

Retain the separation of product verdict, cleanup acceptance, pilot verdict, Director adoption, merge and deployment. The older RRM playbook places Gate Q before cleanup; the later approved RRM-004 QAM sequence performs credential cleanup before final certification. Future adopted packs need one explicit sequence; do not paste both instructions without reconciliation.

Keep the smallest sufficient durable evidence set, including cited helpers/failed attempts where needed to explain the verdict. Remove only authorized transient/sensitive items. Verify cleanup did not change product, tests, config or contract. The exact QA Lead certificate must be present or accessible for attributed transcription at closeout.

Record implementation, evidence, closeout and merge identities separately. Do not loop forever adding a commit's own hash to itself. Director controls project Git and release. After merge, refresh local main safely before starting a new branch. Gate D remains separate when deployment is required.

### RRM-08 — One-shot engineering as a scoped option

**Sources:** SRC-R03 report §§2–3/7 and RRM-003 field note; SRC-Q03 §16. **Status:** recommendation under ND-07, not a universal standard.

Preserve the useful recipe: prepare measurable scope, validate prerequisites, retain Plan Mode, record rulings, declare human checkpoints and finish the handoff in the same assignment. The demonstrated uninterrupted run covers execution between checkpoints, not preparation, approval, QA, cleanup and merge combined.

Report total lifecycle effort, planned touches, in-run interruptions, helper corrections, product repairs and missing-package follow-ups. Do not optimize a success label by omitting a valid stop. Two clean engineering examples do not justify forcing uncertain architectural work into an unattended run.

### RRM-09 — Reviewer playbook modernization

**Source:** SRC-R01/REVIEWER_PLAYBOOK_RRM_PILOT_v0.1.md and RRM_FACTORY_DOCSET_CHANGE_MAP.md. **Status:** candidate adoption; inspect current Hub counterpart before replacement.

The supplied change map asks to distinguish ordinary change review from broad/retrospective investigation; disclose baseline failures without preventing security investigation; separate inherited origin from severity; retain evidence, conditions and falsifiers; route repair through Architect/Director disposition; and avoid unsupported security claims based solely on missing application filters when RLS or another effective boundary may apply.

Do not require three repeated incidents before correcting one severe supported issue. Calibrate claim confidence and specimen equivalence. Keep original reports unchanged; append dispositions/errata. This intake does not approve every sentence in the reviewer candidate verbatim.

### RRM-10 — Owning playbook, kit and references

**Source:** SRC-R01 change map and kit; SRC-R03 lessons. **Status:** proposed placement under ND-05.

Create or update one RRM_PLAYBOOK and a compatible module kit. Link general Factory workflow, Architect, Engineer, Handoff, QA and Testing guidance to that owner. Include findings ledger, approved acceptance, front door, plan/build prompts, engineering evidence/handoff, QA references and closeout/retrospective expectations. If QAM is adopted, use its common templates instead of maintaining competing QA procedure copies inside every RRM kit.

Verify actual ACTION/ACTIONS conventions and Hub paths. Separate reusable procedure from the Cyber Pharma worked example. Publish a complete example only after obtaining its actual completed records; source-reported summaries may be used now with attribution and evidence limits.

## 4. Proposed acceptance checks for the eventual update

- One canonical definition and routing rule for RRM; next BIM/phase identity remains intact.
- Review findings cannot authorize their own repair; each accepted objective has scope, AC and preservation trace.
- Contract freeze, evidence lanes and amendments agree across playbook, kit and QA guidance.
- Active QA branch, repair ownership, retest and cleanup are consistent with adopted current policy.
- Model names, dependency versions, credentials, fixed SHAs and Cyber Pharma business rules are absent from generic templates except clearly labeled examples.
- Product Gate Q, pilot result, merge, Director adoption and Gate D are separately recorded.
- Claimed successful automation is bounded to the supplied field results; missing final evidence is not fabricated.
