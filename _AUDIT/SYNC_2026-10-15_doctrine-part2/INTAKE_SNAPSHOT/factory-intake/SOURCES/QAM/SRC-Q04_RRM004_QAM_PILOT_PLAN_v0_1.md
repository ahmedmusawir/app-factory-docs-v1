# CYBER PHARMA RRM-004 QAM PILOT PLAN

## Five Pairs of Eyes · One-Shot Engineering · One-Shot Independent QA

**Version:** 0.1  
**Date:** 2026-09-29  
**Owner:** JARVIS / QA Lead  
**Director:** Tony Stark  
**Architect:** Fable  
**Engineer:** Claudy  
**QA Executor:** Cody  
**Status:** Controlled experimental plan for Architect authoring  
**Production boundary:** RRM-004 only  
**Doctrine boundary:** This plan does not amend the QA Playbook, RRM doctrine, BIM doctrine, or the Cyber Pharma Plan of Record.

---

## 1. Director's Intent

Cyber Pharma has produced a meaningful operating breakthrough:

- RRM-003 demonstrated a continuous one-shot Engineering run after careful preparation.
- RRM-002 demonstrated that Cody can execute a large independent QA body, including adaptive Playwright browser work, with the Director limited mainly to credential entry.
- RRM-003 QA is now testing whether those two gains can exist back-to-back on the same module.

The Director wants to preserve the Factory's five independent pairs of eyes while removing preventable stops, repeated prompt construction, document hunting, and large manual regression matrices.

The desired operating model is:

> Architect prepares the bounded authority package → Engineer completes the module and factual QA handoff in one continuous run → QA Lead authors the independent attack plan → QA Executor completes verification in one continuous run → QA Lead adjudicates and certifies → Architect and Engineer close out → Director commits, merges, and pushes.

Accuracy remains more important than speed. One-shot means fewer avoidable interruptions, not fewer checks, fewer people, or weaker evidence.

---

## 2. Pilot Boundary

RRM-004 is the first formal QAM pilot.

This is a controlled exception inside a client-production project. It is being used because RRM-004 is expected to be bounded, mechanically verifiable, and suitable for independent evidence collection. The QAM concept remains experimental and is intended primarily for Stark Industries internal applications such as Stark AI Workbench, Web Factory, Web Recon Scraper, and future ABM/APBM programs.

The pilot does **not** authorize:

- changing RRM-003 while its QA is in flight;
- weakening Cyber Pharma's current production QA process;
- promoting QAM into QA doctrine;
- automatically using QAM on future Cyber Pharma BIMs or RRMs;
- eliminating Architect, QA Lead, or Director review;
- allowing Engineering to write the independent QA attack plan;
- allowing Cody to repair product code, certify his own work, commit, merge, or deploy;
- unattended production mutation, billing, emailing, destructive database work, or secret handling.

After RRM-004 closes, Cyber Pharma returns to its established production process unless the Director explicitly approves another controlled trial.

All QAM experiment lessons go to the JARVIS Master 10X Lab. They do not enter canonical Factory or QA doctrine merely because the pilot succeeded.

---

## 3. Why RRM-004 Is the Right Pilot

The Architect should confirm the current campaign map and findings ledger before freezing scope. Based on the current campaign shape, RRM-004 is the dependency-hardening module: framework and image-stack upgrades, advisory closure, configuration confirmation, full regression, and visual/runtime verification.

This is a strong QAM specimen because it is:

- **bounded:** the intended product behavior should not change;
- **high blast radius:** framework and dependency changes can affect the whole application;
- **mechanically testable:** installed versions, advisories, builds, routes, headers, tests, and diffs can be independently proven;
- **visually checkable:** key pages and images can be walked in a browser without inventing new product behavior;
- **low in business ambiguity:** the module should not require new OwedBook math, data contracts, or client rulings.

The Architect must derive the exact package versions, advisory closure conditions, configuration changes, and allowed files from current disk and current authoritative sources. This pilot plan does not freeze dependency versions from earlier conversations.

---

## 4. The Five-Pairs-of-Eyes Model

### Pair 1 — Architect / Fable

Owns the destination and the legal boundaries of the work:

- frozen scope and acceptance criteria;
- protected and allowed files;
- rulings and errata;
- dependency/security success conditions;
- Engineering stage order;
- declared stop conditions;
- repair-scope rulings when QA finds a defect;
- final closeout instruction.

The Architect does not perform Engineering or issue Gate Q.

### Pair 2 — Engineer / Claudy

Owns implementation and self-verification:

- runs Engineering preflight;
- plans the bounded implementation;
- performs the authorized dependency/configuration work;
- runs stage and full-board checks;
- performs only in-scope self-repairs;
- records actual changes and evidence;
- completes `QA_HANDOFF.md` as part of the same assignment;
- supplies the factual half of the QAM manifest.

The Engineer may provide reproduction facts. He does not decide how independent QA attacks his candidate and does not certify it.

### Pair 3 — QA Lead / JARVIS

Owns the independent QA strategy and verdict:

- treats Engineering's handoff as claims;
- confirms the acceptance contract is gradable;
- authors the risk-ranked QA plan;
- defines independent expected results and negative controls;
- rules which browser work Cody performs and which judgment remains with the Director;
- classifies findings;
- decides retest scope after authorized repair;
- issues or withholds Gate Q;
- selects the smallest durable certification package.

### Pair 4 — QA Executor / Cody

Owns independent execution and evidence:

- pins the candidate;
- runs QA environment preflight;
- builds the candidate independently;
- executes static, regression, runtime, browser, and exploratory checks;
- creates or repairs disposable QA helpers when needed;
- captures safe evidence;
- maps every acceptance criterion to a result;
- drafts `REPAIR_PROPOSAL.md` only if a real failure exists;
- returns one indexed result package.

Cody does not edit product source, authorize repair scope, issue Gate Q, or mutate Git history.

### Pair 5 — Director / Tony

Owns authority, not repetitive operation:

- approves plans and rulings;
- holds Git add/commit/push/merge authority;
- creates the Engineering and QA branches;
- authorizes environments;
- enters credentials directly into a visible browser when required;
- supplies product judgment for genuinely new or high-value UI/UX behavior;
- approves destructive or external mutations when any are in scope;
- accepts or rejects meaningful residual risk;
- releases the certified module.

The pilot succeeds when the Director remains fully informed and authoritative without becoming the person who manually executes every tab, button, theme, viewport, and regression combination.

---

## 5. Meaning of "One-Shot"

For this pilot, one-shot means:

- one prepared authority package;
- one approved Engineering plan before mutation;
- one continuous Engineering execution session after preflight passes;
- one complete Engineering handoff package;
- one independent QA plan prepared by the QA seat;
- one continuous QA execution session after QA preflight and any declared credential checkpoint;
- one indexed QA result package;
- clean stops when authority or safety runs out.

One-shot does not mean:

- one unreviewed code dump;
- skipping Plan Mode;
- skipping stage checks;
- skipping independent QA;
- hiding failures to keep the run continuous;
- guessing unresolved decisions;
- declaring success because the agent said it was successful.

Evidence remains the deciding factor.

---

## 6. RRM-004 Lifecycle

### Stage A — Finish RRM-003 Normally

RRM-003 continues under its already-approved process. Cody is not interrupted or redirected. No QAM requirement is retrofitted into that module.

Its final QA execution metrics and observations may later be used as comparison evidence for the RRM-004 pilot.

### Stage B — Architect Authors RRM-004 and the Pilot Overlay

Fable authors the normal RRM-004 pack using the current campaign map, findings ledger, current repository state, and current dependency evidence.

The pack must contain the normal production authority layer:

- module front door;
- brief;
- frozen acceptance specification;
- append-only rulings/errata lane;
- protected and allowed paths;
- Engineering preflight;
- enumerated stop conditions;
- Director checkpoints;
- Engineering execution and evidence requirements;
- QA handoff requirements;
- closeout requirements.

It also contains a clearly labeled **QAM PILOT OVERLAY**. The overlay changes packaging and execution flow only. It does not weaken any acceptance criterion.

The Architect must distinguish:

- facts Claudy supplies;
- independent QA judgments JARVIS supplies;
- checks Cody executes;
- decisions only the Director may make.

### Stage C — Engineering Plan Approval

Claudy performs a read-only Plan Mode pass before mutation.

Plan Mode must:

- verify the real baseline and current dependency graph;
- identify the exact advisory and version targets;
- inspect lockfile and platform-specific image dependencies;
- map every allowed file and protected path;
- confirm build/serve methods;
- run or validate the Engineering preflight;
- identify contradictions before the one-shot begins;
- propose no work outside the frozen module.

Fable rules genuine contract conflicts. Tony approves the plan and any required addendum rows.

This is the planned human decision point. It is not considered a failure of one-shot execution.

### Stage D — One-Shot Engineering

After the plan and preflight are approved, Claudy runs the complete authorized Engineering body in one continuous session.

He may move between internal stages automatically when each local gate passes. He may make bounded self-repairs only inside allowed files and only when the contract already determines the correct behavior.

He stops when:

- preflight fails;
- the contract and disk disagree without a ruling;
- an edit is required outside allowed scope;
- a dependency change requires a product or architecture decision;
- an expected security advisory cannot be closed within scope;
- tests fail and the only path to green would weaken or rewrite an existing test;
- the same failure remains after the permitted self-repair budget;
- a credential, live mutation, destructive action, deployment, Git mutation, or Director decision is required;
- evidence cannot be produced safely.

The same assignment must finish with:

- Engineering completion report;
- full changed-file inventory;
- product/configuration diff;
- dependency and advisory evidence;
- complete board results;
- environment and serve instructions;
- `QA_HANDOFF.md`;
- factual QAM manifest fields;
- one explicit staging block for the Director.

No separate post-build mission should be needed merely to ask Claudy to prepare QA.

### Stage E — Director Pins the Candidate and Opens QA

Tony reviews the staging block, commits the Engineering candidate, pushes it, and creates the QA branch.

The cleanest pilot shape is:

- Engineering changes and completed handoff documents land in the final Engineering commit.
- The QA branch is cut directly from that commit.
- Cody records the full QA-entry HEAD as the immutable candidate before writing QA artifacts.

If any documentation-only commit sits above the candidate, QA must prove the candidate-to-HEAD product/configuration diff is empty. Candidate identity is never inferred from a short SHA or conversation.

### Stage F — QA Lead Finalizes the Independent QAM Plan

At QA entry, JARVIS reads the frozen contract and Engineering handoff, then completes the independent half of the QAM.

The QA plan must not be copied from Claudy's verification list. It must define:

- the highest-risk claims to attack;
- independent version/advisory checks;
- negative controls;
- protected-behavior checks;
- regression board;
- required browser coverage;
- environment and credential checkpoints;
- evidence format;
- finding classifications;
- repair and retest rules;
- exit evidence required for Gate Q.

For RRM-004, the risk plan should normally include:

- installed package and lockfile consistency;
- current audit/advisory status for the exact affected packages;
- platform-specific `sharp`/libvips/libheif resolution where applicable;
- clean production builds under the contract's environment states;
- route-count and runtime-start confirmation;
- cache-header regression recheck after the framework upgrade;
- critical authentication and OwedBook route smoke;
- actual image rendering for every relevant `next/image` consumer;
- desktop and narrow viewport coverage;
- light and dark theme smoke where relevant;
- console, hydration, network, and runtime error review;
- TypeScript, lint, full Jest regression, and zero-skipped enforcement;
- protected-path and unexpected-diff review;
- evidence-security and cleanup requirements.

Tony may visually inspect genuinely new or high-value behavior. Cody owns repetitive regression matrices.

### Stage G — One-Shot Independent QA

Cody receives one standard entry instruction pointing to the module's `QA/` area.

He begins with a hard QA preflight that verifies:

- repository, branch, candidate, ancestry, and clean source state;
- runtime, package manager, browser engine, and required tools;
- required environment-variable names without printing values;
- authorized environment and service reachability;
- required identities and roles where authentication is needed;
- Director access to credentials before browser work starts;
- ports, disk space, and writable evidence locations;
- exact build and standalone-serve method;
- screenshot and trace safety rules;
- declared Director checkpoints;
- trustworthiness of the test instrument.

A preflight failure stops the expensive QA body and returns a precise blocker with an owner. It is not called a product defect.

After preflight passes, Cody runs the complete authorized QA body continuously. He may:

- operate the browser adaptively;
- create temporary Playwright helpers;
- repair those helpers inside `QA/AUTOMATION/`;
- use screenshots and sanitized traces;
- recommend selected stable checks for later promotion into permanent regression coverage.

He may not modify `src/`, application tests, dependency files, configuration, migrations, or contracts.

He returns one indexed result package containing the AC matrix, execution report, evidence map, artifact inventory, findings, and process metrics. He recommends; he does not certify.

### Stage H — Finding and Repair Loop, If Needed

A clean first pass is not required for the process pilot to succeed. Finding a real defect is evidence that the independent system works.

If Cody finds a failure:

1. Cody writes `REPAIR_PROPOSAL.md` with the failed AC, exact reproduction, actual/expected behavior, evidence, suspected paths clearly labeled as suggestion, and proposed retest scope.
2. JARVIS classifies the issue as implementation defect, regression, contract gap, environment/setup issue, instrument failure, inherited condition, follow-up, or observation.
3. Fable rules the allowed repair scope and any contract erratum.
4. Tony approves the repair and retains Git authority.
5. Claudy performs only the authorized repair on the QA line.
6. Tony commits the repair.
7. Cody pins the new candidate and reruns the repair diff, affected ACs, connected regression, and the mandatory full board.

Earlier evidence may carry forward only when the repair could not have changed it and provenance is stated.

### Stage I — Gate Q, Cleanup, and Closeout

JARVIS reads the AC matrix and evidence map, adjudicates all findings, and issues or withholds Gate Q against an immutable candidate.

Gate Q is followed by bounded QA cleanup:

- preserve the smallest durable package proving the verdict;
- preserve useful process metrics and 10X observations;
- remove or exclude disposable browser state, cookies, tokens, caches, raw runtime copies, redundant screenshots, oversized traces, and temporary helper debris;
- prove product, tests, contracts, and protected paths were not changed during cleanup;
- return the working tree clean.

After Gate Q PASS and cleanup completion:

- Fable authors the closeout instruction;
- Claudy performs the documentation/repository closeout;
- Tony reviews, commits, merges, and pushes.

---

## 7. QAM Pilot Folder Shape

The canonical module contract remains at the RRM-004 pack root. Do not create drifting copies of frozen authority files inside QA.

The existing `QA/` area becomes the QAM execution area for the pilot:

```text
RRM-004-CYBER-PHARMA/
├── CLAUDE.md
├── RRM_BRIEF.md
├── ACCEPTANCE_SPEC.md
├── RULINGS_ADDENDUM.md
├── ENVIRONMENT_PREFLIGHT.md
├── DIRECTOR_CHECKPOINTS.md
├── QA_HANDOFF.md
├── EXECUTION_LOG.md
├── evidence/
└── QA/
    ├── AGENTS.md
    ├── QAM_PILOT_CHARTER.md
    ├── QAM_MANIFEST.md
    ├── QA_TEST_PLAN.md
    ├── AUTOMATION/
    ├── evidence/
    ├── AC_EVIDENCE_MATRIX.md
    ├── QA_EXECUTION_REPORT.md
    ├── REPAIR_PROPOSAL.md          # only if a failure exists
    ├── ARTIFACT_INVENTORY.json
    ├── QA_CLEANUP_REPORT.md
    ├── QA_CERTIFICATION.md         # authored by QA Lead
    └── QAM_PILOT_RESULTS.md
```

`QA/AGENTS.md` must state in plain language:

- Cody owns files only inside the authorized QA execution lanes.
- Cody may repair disposable QA helpers.
- Cody never repairs product code.
- Engineering claims are not PASS evidence.
- Cody never self-certifies.
- Git mutation remains Director-owned.
- Secrets, credentials, cookies, tokens, PHI, PII, and reusable authenticated state never enter evidence.
- Uncertainty beyond enumerated authority causes a clean stop.

---

## 8. Director Checkpoints

The RRM-004 pack must declare all expected human checkpoints before execution.

Expected checkpoints are:

1. Director approves the Architect's RRM-004 pack.
2. Director approves Claudy's read-only plan and rulings.
3. Director commits/pushes the Engineering candidate and creates the QA branch.
4. Director enters browser credentials if authenticated QA is required.
5. Director provides a brief visual judgment only for behavior where human taste or product judgment is actually material.
6. Director approves any repair scope or residual risk.
7. Director commits/merges/pushes after certification and closeout.

Routine builds, test commands, browser matrices, screenshots, evidence indexing, diff checks, and regression work are not Director checkpoints.

---

## 9. Pilot Success Criteria

The QAM pilot is successful when all of the following process claims are supported by evidence:

- the five-seat authority model remained intact;
- the Engineer did not self-certify;
- the QA plan was independently authored by the QA seat;
- Engineering ran continuously after its approved plan and preflight, except for declared stop conditions;
- QA ran continuously after its preflight and declared credential checkpoint, except for declared stop conditions;
- every acceptance criterion received traceable evidence or an explicit non-PASS status;
- no product defect was hidden to preserve one-shot status;
- the Director performed authority and judgment work rather than repetitive execution work;
- browser regression work was substantially agent-driven;
- environment/setup problems were detected before the expensive execution body;
- one indexed QA package was sufficient for QA Lead adjudication;
- repair, if needed, followed the governed repair loop;
- Gate Q remained a human QA Lead decision;
- the final branch was clean and the durable evidence package was intentionally selected;
- experimental lessons were exported to the 10X Lab without silently changing production doctrine.

The pilot does not fail merely because a real product defect produces a repair round. It fails as a process experiment if the package forces repeated preventable clarification loops, hides authority decisions, compromises independence, leaks evidence, or requires the Director to manually reconstruct and transport the QA body again.

---

## 10. Metrics Required

Record separately for Engineering and QA:

- preparation time;
- wall-clock execution time;
- agent-active time;
- Director-active time;
- planned Director checkpoints;
- unplanned Director interruptions;
- number of prompts after the execution GO;
- preflight failures;
- stop conditions reached;
- clarification loops;
- in-scope self-repairs;
- product findings;
- environment/setup incidents;
- test-instrument incidents;
- repair rounds;
- builds, routes, suites, tests, warnings, and skips;
- browser states exercised;
- screenshots/traces retained versus discarded;
- temporary helpers created;
- helpers recommended for permanent regression promotion;
- evidence gaps at first handoff;
- final verdict;
- cleanup result;
- total Director touches from Engineering GO through Gate Q.

Compare the result against the documented RRM-001, RRM-002, and RRM-003 field observations. Do not compare only elapsed time; compare interruptions, evidence completeness, and Director workload.

---

## 11. What We Intentionally Do Not Automate

The pilot is not an automation contest.

These remain human- or seat-owned:

- product and business decisions;
- acceptance-contract authorship;
- scope and architecture rulings;
- QA risk prioritization;
- finding classification;
- meaningful visual or usability judgment on new functionality;
- credential entry;
- destructive authorization;
- repair-scope authorization;
- residual-risk acceptance;
- Gate Q certification;
- Git history and release approval.

Automation and agents absorb repetition. They do not erase accountability.

---

## 12. UI/UX and Playwright Policy for the Pilot

Tony remains involved in testing newly introduced user behavior and major end-to-end business paths, such as a complete e-commerce transaction, onboarding flow, payment outcome, or other consequential experience.

Cody should own repetitive regression coverage such as:

- every existing tab opens;
- buttons remain reachable and operable;
- navigation works at desktop and narrow widths;
- light and dark themes render without breakage;
- keyboard-critical paths remain usable;
- protected routes preserve expected behavior;
- images load;
- no hydration, console, or network regression appears;
- repeated role/viewport/theme combinations behave consistently.

Use three levels of browser automation:

1. Agent-driven live browser work for adaptive checking.
2. Temporary Playwright helpers for repetitive matrices and evidence capture.
3. Permanent regression tests only for stable, high-risk, repeatable behaviors worth maintaining.

Do not turn every exploratory click into permanent test code.

---

## 13. 10X Lab Export

After RRM-004 closes, create a production field note for the JARVIS Master 10X Lab containing:

- predicted versus actual Engineering flow;
- predicted versus actual QA flow;
- metrics from Section 10;
- Director interventions and their causes;
- environment, tooling, and identity failures;
- Playwright lessons;
- evidence-packaging lessons;
- repair-loop performance;
- which QAM files were useful;
- which QAM files became paperwork without value;
- what should be kept, changed, or dropped;
- implications for internal ABM/APBM/QAM design;
- explicit statement that no doctrine promotion occurred.

The 10X Lab may later turn repeated, successful observations into an internal QAM handbook and supporting tools. That is a separate activity with separate approval.

---

## 14. Architect Assignment

Fable should use this plan to author RRM-004 in the current Cyber Pharma campaign grammar.

The Architect's return should contain:

1. The reconciled, current RRM-004 product scope from the campaign map, findings ledger, current disk, and current dependency advisories.
2. The normal RRM-004 pack, complete enough for Plan Mode and one-shot Engineering.
3. The QAM pilot overlay described here, using the existing `QA/` area rather than inventing a second competing module hierarchy.
4. Frozen acceptance criteria that separately grade product success and pilot-process evidence.
5. Enumerated Engineering and QA stop conditions.
6. Declared Director checkpoints.
7. A complete Engineering handoff requirement inside the original build assignment.
8. A QA entry structure that allows JARVIS to add the independent plan and Cody to begin from one standard instruction.
9. A results template that exports lessons only to the 10X Lab.
10. A short list of genuine Director decisions, if any. Do not manufacture choices that current evidence already settles.

The Architect must not alter RRM-003, pre-certify RRM-004, write Cody's independent verdict, or promote QAM to production doctrine.

---

## 15. Bottom Line

Cyber Pharma is not being turned into an unattended automation experiment.

RRM-004 will test a disciplined operating improvement:

> Five pairs of eyes remain. Decisions remain separated. Engineering and QA each receive a complete, pre-authorized package and execute continuously until completion or a real stop condition. The Director remains the authority without becoming the repetitive operator.

If the pilot works, Cyber Pharma gains one carefully measured improvement. The larger QAM, ABM, and APBM opportunity belongs to the 10X Lab.

