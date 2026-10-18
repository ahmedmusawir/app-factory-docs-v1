# RRM Factory Doc-Set Change Map

**v0.1 · 17 September 2026 · Proposed integration; no canonical edits performed**

Use this package as a controlled sync intake. The supplied DOC_SET_SYNC_PROCESS defines: Claudy analysis/update map → Tony approval → SOL-authored sync acceptance specification approved by Tony → Claudy implementation → Cody QA and repair loop → SOL closeout → Tony PR/merge. Preserve that workflow. This map is input to analysis, not a substitute for inspecting the actual doc repository.

| Target | Proposed change | Source / acceptance check |
|---|---|---|
| REVIEWER_PLAYBOOK.md | Consolidate evidence calibration; add modes, export support, limitations and RRM handoff | Candidate file in package; one canonical reviewer playbook after adoption |
| New RRM_PLAYBOOK.md | Define review-to-contract and existing delivery lifecycle | Findings cannot silently become work orders; QA remains independent |
| New RRM_MODULE_KIT | Front door, scope, ledger, ACs, prompts, execution, QA and closeout forms | Complete trace from source finding to final evidence |
| SOFTWARE_FACTORY_PLAYBOOK.md / Blueprint | Connect Engines 1/2/3, RRM routing, headquarters/project roles | Do not renumber project phases or imply merge equals deployment |
| ARCHITECT_PLAYBOOK.md | Current-source reconciliation, dispositions, Director decisions, RRM packet and closeout | Project facts owned by project Architect; no invented math |
| ENGINEER_PLAYBOOK.md | Consume approved repairs, preserve ACs, execution log, QA-line repair scope | Engineer may challenge but not silently reject/change contracts |
| QA_PLAYBOOK.md | RRM repair verification + regression; Cody execution/SOL verdict; cleanup | No routine engineering-packet approval; certification pinned to specimen |
| HANDOFF_PACKAGE_PLAYBOOK.md | RRM kit and repo-local QA guidance, evidence references | QA can access required instructions without outside-repo reads |
| BIM/FFM/TRM/ABM guidance | Add routing/reference only where applicable | Avoid copying entire RRM procedure into every module playbook |
| STARTER_KIT_HANDBOOK.md | Confirm module/evidence lane location and non-runtime boundary | Verify ACTION/ACTIONS conventions on actual repo before changing paths |
| TESTING_PLAYBOOK.md | Evidence boundaries, relevant regression, bounded retest | Probe successes never relabeled full framework integration |
| Doctrine journal / worked examples | Import supported lessons, later add completed RRM example | Preparation evidence distinct from delivered/certified outcome |

Blueprint, Architect, Handoff, BIM, TRM, ABM and Testing documents were referenced but not all supplied in this session. Their exact sections, versions and cross-links require sync-stage inspection; this map does not claim those files were audited.

## Explicit conflicts to resolve during adoption

1. June reviewer rule “tests green before every review”: retain as normal change-review expectation; allow broad/retrospective investigation with baseline failures disclosed.
2. June “Stage 2 only after compliance passes”: for broad reviews, record compliance failures and continue material quality/security investigation.
3. June “pre-existing” severity/nonblocking category: separate origin from severity and scope; RRMs intentionally target inherited problems.
4. June four-field/no-prose report restriction: permit calibrated evidence, conditions, falsifiers and human-readable summary.
5. June direct reviewer-to-engineer repair flow: insert Architect/Director disposition and preserve SOL/Cody certification and cleanup.
6. June illustrative tenant query example: absence of an application filter alone does not establish cross-tenant disclosure if effective RLS or another boundary exists. Trace actual authority and state evidence limits.
7. June systemic change only after three occurrences: permit evidence-backed correction after one severe failure; keep recurrence as useful evidence, not an absolute threshold.
8. Earlier QA disposable-branch and keep-all-QA-output wording: use forward-moving certification line and later J-19 cleanup refinement.
9. Blanket module-folder freeze: freeze engineering contract; allow append-only evidence/errata lanes.
10. Git-only identity: export manifests are valid stability evidence with provenance limits.

## Sync validation objectives

Check roles, gate sequence, terminology, evidence scale, template links, branch rules and authority across every affected document. Confirm legacy statements are removed or explicitly scoped. Preserve historical examples with their dates/status. Do not bulk-replace project-specific phase numbering or old certified evidence.

Keep this pilot package separately versioned. Formal canonical promotion occurs only through the approved sync run. After the Cyber Pharma pilot, add actual delivery lessons before claiming the RRM lifecycle is field-proven.
