# Reviewer Playbook — RRM Pilot Candidate

**Version 0.1 · 17 September 2026 · Proposed consolidated revision**  
**Sources:** REVIEWER_PLAYBOOK.md v1.0 (8 June 2026); Astra Code Reviewer Baseline v0.1 (9 September 2026); Engine 2 diagrams; Cyber Pharma review preparation and reports received 17 September.

This is a separately named candidate. It does not silently replace the canonical Reviewer Playbook. On adoption, integrate it into the single canonical playbook and preserve the old version as history. Historical benchmark findings are calibration examples, not answer keys or current project findings.

## 1. Mission and authority

The Reviewer independently assesses consequential correctness and risk against an explicit scope. Trace the system, challenge the tests and the implementation, and provide reproducible, falsifiable findings. The Reviewer does not implement repairs, settle unknown product requirements, issue SOL's Gate Q, or authorize a merge/deployment.

Use a separate session from implementation. Record prior involvement or exposure to other reviewers' findings. For blind parallel reviews, exclude previous findings and adjudications from reads and searches. A previously involved reviewer can still contribute, but the report must describe that limitation. Never erase prior exposure by calling the run independent.

## 2. Choose the review mode

| Mode | Target | Baseline handling |
|---|---|---|
| Change review | Approved change/diff | Record base and candidate; engineering green is the normal handoff expectation |
| Phase or retrospective review | Completed phase, older surface or repository snapshot | Record baseline failures and continue useful investigation; do not suppress security work because another check fails |
| Targeted re-review | Accepted finding and repair diff | Verify resolution, relevant interactions, and new consequential problems introduced by the repair |
| Release review | Defined whole-system use and cross-phase boundaries | Record deployment/environment scope; source review alone cannot establish production readiness |

Map requirements before judging compliance. A failed compliance check in a broad review is a finding and may limit conclusions; it is not a reason to hide unrelated quality/security defects. Broad review need not wait for every existing test to pass. Failed or unavailable checks must remain visible.

## 3. Identify and preserve the specimen

Two supported input forms:

- **Git checkout:** record repository, base/candidate commits, branch if relevant, pre-existing changes and approved scope. Read-only Git is allowed when authorized; no mutating Git during review-only work.
- **Git-free export:** record approved directory, package identity and a SHA-256 file manifest. State unavailable commit/history provenance. Do not initialize Git, find another checkout, clone, or demand restoration of .git.

For exports, document manifest inclusions/exclusions. Include source, existing tests, fixtures, dependency locks/manifests, configuration, schema and relevant contracts. Exclude secret files, dependencies, generated outputs and other reviewers' outputs. Rescan the same policy at the end, detecting additions, deletions and changes. Report excluded material honestly.

A matching before/after manifest proves stability of included inputs during the review. It does not prove equivalence to a historical commit, cleanliness of excluded files or a match between reviewers' specimens. Cross-review comparisons require explicit equivalence evidence or a current-source reconciliation.

## 4. Access and permitted work

The assignment must state writable output locations and permitted execution. Product source, existing tests, configs, schemas and dependencies remain unchanged during review-only work. Review probes may be written in the authorized evidence directory. Record ordinary ignored outputs from allowed builds/tests.

Inspect commands before running them. Local execution may load real credentials or call live services. Use declared synthetic inputs or controlled environments. Installation, network, browser, database and infrastructure permissions must be stated rather than inferred from a local path. Missing dependencies should be reported promptly; use useful authorized alternatives without claiming they replace framework tests. Never silently install, upgrade or repair the application to make review easier.

Git-free review copies and the later engineering/QA branches are different lifecycle artifacts. Review copies do not get merged. Approved repairs are implemented on the project's authorized RRM branch and certified on its forward-moving QA branch.

## 5. Review sequence

1. Record authority, mode, specimen, independence, environments and exclusions.
2. Map supported journeys, real/mock/deferred data paths, ownership and privileged boundaries.
3. Establish existing verification results early; distinguish not run, blocked, failed and passed.
4. Trace high-impact requests and data end to end, including ordinary user journeys.
5. Examine contracts, calculations, asynchronous transitions, errors, recovery, accessibility, relevant performance and operations.
6. Verify candidate claims with the smallest adequate source trace or permitted probe; include meaningful controls.
7. Check breadth so one favored category does not crowd out the rest of the application.
8. Group root causes, classify, calibrate and preserve effective protections.
9. Challenge the strongest claims; narrow or withdraw those that fail.
10. Produce the report and final input-stability check.

Read relevant governing requirements and curated manuals. Expand access when an actual dependency requires it. Do not load every factory document mechanically. Repository instructions do not override higher-priority instructions or explicit Director scope; state conflicts rather than silently ignoring them.

## 6. Evidence, classification and severity

| Evidence | Establishes | Does not establish |
|---|---|---|
| E0 hypothesis | Plausible question | A defect |
| E1 source/artifact | Concrete logic, contract or metadata | Runtime outcome at unexecuted boundaries |
| E2 controlled execution | Behavior with declared fixtures/substitutes | Behavior of replaced components |
| E3 boundary/integration | A named real boundary, possibly in an isolated local environment | All dependencies or deployment parity |
| E4 deployment-representative | Identified target-like configuration and services | Universal safety |

E3 does not inherently mean production access; a local real framework dispatcher or isolated installed SQL trigger can qualify for its exercised boundary. Evidence labels never authorize execution. Record remaining mocks.

Classify as current defect, conditional risk, future integration risk, contract question, tooling defect, tradeoff, optional improvement, or positive protection. Severity is Critical / High / Medium / Low / Unrated pending context. Confidence is High / Moderate / Low with reasons. Priority is a separate Director/Architect decision.

“Pre-existing” describes origin, not severity. Existing problems may be the central RRM scope. Installed vulnerable versions do not prove exploitable deployment. A narrow source finding can be strong without a live exploit. Missing live evidence proves neither safety nor compromise.

## 7. Finding anatomy

Every material finding contains:

- Stable reviewer ID; bounded title; classification; severity with conditions; confidence.
- Specimen identity, exact paths/locations and relevant caller/callee.
- Expected invariant and its authority; unresolved intent labeled as an assumption.
- Execution/data/ownership path and realistic trigger.
- Observed evidence, source inference, substituted components and unknown boundaries.
- Consequence, affected scope and recoverability.
- Smallest falsifier or evidence that narrows severity/applicability.
- Root-cause group, relevant protections, proposed repair objective and verification objective.

Do not prescribe an unapproved redesign. Do not count identical symptoms as separate defects. Preserve distinct triggers when they need different verification. For financial semantics, expose ambiguity rather than choosing a business rule.

## 8. Report and durable handoff

One authoritative Markdown report plus concise reproducible evidence is sufficient. Include executive assessment, specimen/independence, system map, verification record, findings table/details, protections, coverage gaps, self-critique, suggested disposition and change-boundary confirmation.

Retain essential commands, inputs, substitutes and assertions. Huge logs and temporary environments are not automatically durable evidence. Report claims with conditions next to their severity, including in summary tables. Positive observations must be as carefully bounded as negative ones.

If credible current critical exposure is found, notify Tony with redacted evidence and facts separated from assumptions. Do not exploit a live service or implement containment without authority. Continue unrelated permitted review work where safe.

## 9. Re-review and disagreement

The project Architect reconciles findings with current project truth and proposes dispositions; Tony approves scope/risk decisions. Claudy may challenge an accepted finding with evidence, but cannot silently discard it. SOL adjudicates QA evidence; scope or contract questions return to the Architect/Director.

Re-review checks accepted repair objectives on the new candidate and the relevant diff. Do not restart a broad review for style nits. New consequential findings get recorded and routed for a scope decision; they are not silently repaired. A targeted reviewer verdict is an input to independent QA certification, not a substitute for regression.

## 10. Lessons and adoption

Tag systemic lessons with evidence and affected doctrine. Repetition strengthens a lesson, but a severe demonstrated failure need not recur three times before a corrective rule is proposed. A failed review setup can also teach a process lesson: the September Git-free export incident shows why Git must be optional while specimen identity remains required.

Cyber Pharma's received reports are worked examples of review reporting, not yet a completed RRM delivery example. Append the eventual disposition, repairs, QA and closeout evidence before promoting the full RRM cycle as proven.
