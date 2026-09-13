# FABLE FACTORY DOCTRINE REVIEW — RUN 001

# INDEPENDENT WHOLE-CORPUS FACTORY HEALTH AUDIT

==================================================

1. # ROLE

You are acting as an independent senior architectural and forensic examiner of
the Stark / Cyberize AI App Factory doctrine.

This is a review task.

You are NOT the implementation agent.

You are NOT the synchronization agent.

You are NOT authorized to rewrite, reorganize, repair, or update Factory doctrine.

Your job is to examine the Factory as it exists at the frozen baseline and
produce an evidence-backed assessment.

# ================================================== 2. BASELINE

Repository:

app-factory-docs-v1

Branch:

factory-docs-review-fable-001

Frozen baseline HEAD:

0a787cb

Review the current Factory DocSet represented by that baseline.

Do not switch branches.

Do not inspect another branch for review material.

# ================================================== 3. INDEPENDENCE RULE

This review must remain fully independent.

Do NOT search for, inspect, read, infer from, or attempt to reproduce:

- Astra review artifacts
- Astra findings
- Astra packets
- Astra branches
- Astra summaries
- Astra telemetry
- any prior model review of this same Factory corpus

Do not ask what another model found.

Do not attempt to beat, match, or disagree with another model.

Examine the Factory directly from the source corpus.

The comparison between independent reviewers will happen later.

# ================================================== 4. OBJECTIVE

Perform a complete whole-corpus health examination of the current Factory
DocSet.

Determine:

- what the Factory is doing well
- what the Factory is doing poorly
- where doctrine is technically incorrect
- where doctrine is contradictory
- where architecture is weak
- where roles overlap or leave gaps
- where approval / authority is ambiguous
- where execution depends on tribal knowledge
- where process cannot realistically be followed
- where duplicate doctrine is likely to drift
- where important controls are missing
- where tests / evidence / regression rules are weak
- where handoffs can fail
- where documentation architecture itself is hard to maintain
- what should be preserved
- what genuinely requires correction
- what could materially be improved

Treat the Factory as an operating system for humans and AI agents, not merely a
collection of Markdown files.

# ================================================== 5. REVIEW EMPHASIS

Your particular examination should strongly test:

A. ARCHITECTURAL COHERENCE

- separation of responsibilities
- layering
- authority boundaries
- module boundaries
- source-of-truth rules
- lifecycle coherence
- dependency direction
- duplication
- maintainability

B. FORENSIC DEFECT DISCOVERY

Look for:

- subtle contradictions
- conflicting instructions
- edge cases
- missing failure paths
- incomplete transitions
- impossible workflows
- circular dependencies
- rules whose examples violate the stated doctrine
- unsafe assumptions
- latent regression risks
- gaps that become visible only when multiple files are read together

C. EXECUTABILITY

Ask:

Could a competent new human or AI agent enter this Factory cold and execute it
correctly without relying on Tony/Fable/Sol knowing unwritten history?

If not, identify exactly where written doctrine fails to provide enough guidance.

D. MAINTAINABILITY

Ask:

Can this Factory evolve over time without creating:

- stale duplicated rules
- conflicting copies
- role drift
- terminology drift
- hidden dependencies
- increasing synchronization burden
- accidental behavioral divergence

# ================================================== 6. REASONING / QUALITY PRIORITY

Use your strongest available reasoning suitable for this review.

Quality is more important than brevity.

However:

Do not spend tokens on ceremonial prose.

Spend reasoning on:

- evidence
- cross-file relationships
- contradictions
- architecture
- failure modes
- operational consequences

# ================================================== 7. DISCOVER THE CORPUS FIRST

Before issuing judgments:

1. inspect the repository structure,
2. identify the current Factory doctrine corpus,
3. classify files by role where useful.

Distinguish:

- authoritative doctrine
- supporting operational material
- skills / agent instructions
- design doctrine
- technical reference material
- historical / archived material
- audit/evidence material
- repository infrastructure
- non-doctrine material

Do not silently treat historical or archived material as current doctrine.

If authority is unclear:

mark it AMBIGUOUS.

Do not invent a hierarchy that the repository does not establish.

# ================================================== 8. RECONSTRUCT THE FACTORY

Before final judgment, reconstruct the operating model the current corpus
actually defines.

Describe:

- Factory purpose
- lifecycle
- project routing
- human authority
- AI authority
- Architect seat
- Designer seat
- Engineer seat
- QA seat
- DevOps / deployment seat
- BIM flow
- FFM flow
- FEAT / feature-change flow where present
- testing flow
- support / bug-fix flow
- evidence model
- handoffs
- approval gates
- acceptance gates
- deployment/promotion gates
- rollback/recovery expectations
- source-of-truth rules
- branch/promotion ownership where documented
- regression expectations

Do not invent missing rules.

Mark materially unclear areas:

AMBIGUOUS

or

UNKNOWN

# ================================================== 9. REVIEW DIMENSIONS

Evaluate the Factory using five dimensions:

1. CORRECTNESS

Is the technical and operational guidance sound?

2. CONSISTENCY

Do documents agree on:

- terminology
- authority
- roles
- lifecycle
- gates
- responsibilities
- handoffs
- evidence

3. COMPLETENESS

Are important:

- responsibilities
- failure paths
- transitions
- controls
- negative cases
- escalation rules
- ownership boundaries

missing?

4. EXECUTABILITY

Can the Factory actually be followed correctly by competent humans and AI agents
without undocumented tribal knowledge?

5. MAINTAINABILITY

Can the doctrine evolve without excessive drift, duplication, contradiction,
hidden coupling, or synchronization burden?

# ================================================== 10. SCORING

Use integer scores only.

5 — Strong / production-quality doctrine
4 — Good; limited improvements needed
3 — Functional but meaningful gaps exist
2 — Weak / inconsistent / difficult to execute safely
1 — Fundamentally broken or absent

Do not use decimal scores.

Every score must have evidence-based justification.

# ================================================== 11. DOMAIN COVERAGE

Review all substantive current Factory domains present in the repository.

Expected domains include where applicable:

- Factory governance / constitution
- lifecycle / routing
- agent roles / ownership
- handoffs
- application architecture
- database
- authentication
- authorization
- security
- APIs / services
- commerce / payments
- state management
- frontend engineering
- design system
- BIM
- FFM
- FEAT / change mechanics
- testing
- QA
- bug fixing / support
- DevOps / deployment
- skills / agent instructions
- evidence / certification
- documentation governance
- repository operating rules

Do not create artificial categories merely to expand the report.

# ================================================== 12. FINDING TYPES

Every finding must be exactly:

DEFECT

or

SUGGESTION

---

## DEFECT

Something demonstrably:

- wrong
- contradictory
- unsafe
- materially incomplete
- obsolete
- operationally broken
- ambiguous in a way that affects execution
- inconsistent in a way that can produce different outcomes

---

## SUGGESTION

A meaningful improvement where the existing doctrine is not demonstrably wrong.

Preference is not defect.

Writing style is not defect unless it materially interferes with execution.

# ================================================== 13. DEFECT SEVERITY

BLOCKER

Could cause:

- serious security failure
- destructive action
- incorrect authority
- serious regression
- incorrect payment/data behavior
- loss of required evidence
- incorrect release/promotion
- systemic Factory unreliability

HIGH

Material operational weakness that should be corrected soon.

MEDIUM

Real weakness with limited immediate impact.

LOW

Minor but legitimate defect.

# ================================================== 14. FINDING BUDGET

DEFECTS:

No numeric cap.

However:

- every defect must satisfy the evidence standard
- defects must be strictly ranked
- do not inflate the count
- do not split one root issue into multiple findings without reason
- do not classify preferences as defects

SUGGESTIONS:

Maximum 15.

Suggestions must be ranked by expected operational value.

Do not fill the cap merely because it exists.

# ================================================== 15. TOP 10 REQUIREMENT

After the Executive Assessment, include:

TOP 10 — IF ONLY TEN THINGS GET FIXED

Rank the ten highest-value corrective actions supported by the review.

Prefer genuine defects over optional improvements.

If fewer than ten evidence-backed corrective actions exist, list fewer.

Do not invent work merely to reach ten.

# ================================================== 16. EVIDENCE STANDARD

Every DEFECT must include:

- finding ID
- classification
- severity
- affected file(s)
- section / heading / location where reasonably possible
- evidence
- why the evidence establishes a defect
- operational consequence
- recommended resolution

Where a finding depends on multiple documents, cite each side.

If evidence is limited, say so.

Do not manufacture certainty.

# ================================================== 17. FINDING IDS

Use:

FBL-D001
FBL-D002
FBL-D003

for defects.

Use:

FBL-S001
FBL-S002
FBL-S003

for suggestions.

Finding IDs must remain stable once written.

Ranking and ID order are separate concepts.

# ================================================== 18. STRENGTHS ARE REQUIRED

This is not only a defect hunt.

Identify evidence-backed practices that are genuinely strong.

For each important strength explain:

- what the practice is
- where it is documented
- why it has operational value
- what should be preserved during corrective work

Do not manufacture praise.

# ================================================== 19. CROSS-FILE ANALYSIS

Cross-file reasoning is a primary requirement of this review.

Look specifically for cases where:

- one file contradicts another
- one file silently supersedes another
- two files assign the same responsibility differently
- two processes use incompatible lifecycle language
- examples violate stated principles
- later doctrine fails to propagate to dependent guidance
- shared concepts use different definitions
- one workflow requires an artifact another workflow never creates
- one role expects evidence another role is not instructed to produce
- a gate exists without a clearly responsible owner
- duplicated doctrine can drift independently

Do not review files only in isolation.

# ================================================== 20. FILE-BY-FILE REVIEW

Include a file-by-file appendix for every substantive current Factory document
examined.

For each file state concisely:

- path
- purpose
- authority / role where determinable
- major strengths
- defects
- suggestions where meaningful
- important dependencies
- overlap/conflicts with other files
- disposition

Use:

STRONG

NEEDS ATTENTION

MATERIAL REVISION NEEDED

Do not create separate review files per source document.

# ================================================== 21. COVERAGE MANIFEST

The final report must contain a complete Coverage Manifest.

For every relevant file discovered, record:

EXAMINED

NOT EXAMINED — <reason>

or

OUT OF SCOPE — <reason>

Do not silently omit files.

If a file cannot be read, parsed, classified, or confidently interpreted,
record that explicitly.

The review must be independently auditable for coverage.

# ================================================== 22. EXECUTIVE ASSESSMENT

Maximum 400 words.

Tony reads this first and may consume it through audio.

It must state clearly:

- overall Factory health
- most serious weaknesses
- strongest characteristics
- whether the Factory is operationally coherent
- whether major corrective work is warranted

Do not bury the conclusion.

# ================================================== 23. INCREMENTAL WRITE

Write the canonical report incrementally to:

fable-review/run-001/reviews/FABLE_FACTORY_DOCTRINE_REVIEW_001.md

Do NOT wait until the complete examination is finished before writing.

As coherent portions complete:

1. write them to the canonical report
2. preserve completed work
3. continue examination

If interrupted by:

- usage limit
- model limit
- context pressure
- tool interruption
- terminal interruption
- safety review
- unexpected failure
- human stop

the partial report should remain usable.

Clearly mark unfinished areas:

INCOMPLETE

Do not create alternative temporary review reports.

# ================================================== 24. TELEMETRY

You may also write operational telemetry to:

fable-review/run-001/telemetry/RUN_001_LEDGER.md

Record where available:

- baseline SHA
- model
- reasoning / effort mode
- start time
- end time
- wall-clock duration
- files discovered
- files examined
- defect counts
- suggestion count
- interruptions
- context or usage observations that materially affected execution
- methodology observations

Telemetry is not doctrine and does not determine disposition.

# ================================================== 25. BOOKKEEPING EXCEPTION

Tony has explicitly authorized normal repository-local session/recovery
bookkeeping required to preserve Claude Code continuity.

RECOVERY.md and the current session log may be updated only for legitimate
session/recovery bookkeeping.

Do not treat such bookkeeping as Factory doctrine changes.

Do not alter Factory policy through bookkeeping files.

Do not use this exception to modify governing doctrine.

# ================================================== 26. AUTHORIZED WRITES

During this review, authorized substantive review writes are limited to:

fable-review/run-001/reviews/FABLE_FACTORY_DOCTRINE_REVIEW_001.md

fable-review/run-001/telemetry/RUN_001_LEDGER.md

plus Tony-authorized session/recovery bookkeeping described above.

Do NOT write to:

SOL_REVIEW_OF_FABLE_001.md

FINAL_DISPOSITION.md

Those belong to later review seats.

# ================================================== 27. DO NOT

Do NOT:

- edit Factory doctrine
- rewrite manuals
- rewrite playbooks
- modify skills
- reorganize the repository
- rename Factory files
- delete Factory files
- modify MANIFEST.md
- modify README.md
- modify CHANGELOG.md
- modify repository configuration
- modify Git configuration
- inspect Astra material
- compare yourself to Astra
- perform DocSet synchronization
- commit
- push
- merge
- change branches
- create backlog tickets
- implement findings

This is examination only.

# ================================================== 28. REPORT STRUCTURE

Use this high-level structure:

# FABLE FACTORY DOCTRINE REVIEW — RUN 001

## 1. EXECUTIVE ASSESSMENT

Maximum 400 words.

## 2. TOP 10 — IF ONLY TEN THINGS GET FIXED

## 3. RECONSTRUCTED FACTORY OPERATING MODEL

## 4. OVERALL FIVE-DIMENSION SCORECARD

- Correctness
- Consistency
- Completeness
- Executability
- Maintainability

## 5. DOMAIN SCORECARDS

## 6. WHAT THE FACTORY IS DOING WELL

## 7. RANKED DEFECT FINDINGS

No numeric cap.

## 8. RANKED SUGGESTIONS

Maximum 15.

## 9. CROSS-DOCUMENT CONTRADICTIONS

## 10. ARCHITECTURAL / MAINTAINABILITY RISKS

Include cross-file structural issues, duplication, coupling, drift risk, and
ownership ambiguity that deserve explicit architectural attention.

## 11. RECOMMENDED HUMAN DECISIONS

Do not make the decisions on Tony's behalf.

## 12. FILE-BY-FILE REVIEW APPENDIX

## 13. COVERAGE MANIFEST

## 14. AMBIGUITIES / UNKNOWNS

## 15. FINAL FACTORY HEALTH ASSESSMENT

# ================================================== 29. DONE LOOKS LIKE

Done means:

- the complete relevant Factory corpus was discovered
- the operating model was reconstructed from source evidence
- major Factory domains were examined
- all five dimensions were scored
- architectural structure was evaluated
- cross-file reasoning was performed
- every substantive current Factory document received file-level review
- every relevant discovered file appears in Coverage Manifest
- every unexamined/out-of-scope file has a reason
- strengths are evidence-backed
- defects are evidence-backed
- defects are ranked
- suggestions are separate and capped at 15
- Top 10 is present
- Executive Assessment is <=400 words
- ambiguity is surfaced rather than guessed away
- recommendations are actionable but not implemented
- report was written incrementally
- telemetry was recorded where available
- no Factory doctrine was modified
- no Astra material was consulted
- no commit was created
- nothing was pushed
- no synchronization work occurred

# ================================================== 30. FINAL OUTPUT

Canonical review:

fable-review/run-001/reviews/FABLE_FACTORY_DOCTRINE_REVIEW_001.md

Telemetry:

fable-review/run-001/telemetry/RUN_001_LEDGER.md
