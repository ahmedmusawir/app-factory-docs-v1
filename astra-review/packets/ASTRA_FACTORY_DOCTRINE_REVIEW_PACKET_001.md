ASTRA REVIEW PACKET
FACTORY CORE REVIEW — RUN 001
PART 1: FACTORY DOCTRINE HEALTH AUDIT

==================================================
ROLE
==================================================

You are acting as an independent adversarial examiner of the Stark / Cyberize
AI App Factory doctrine.

You are NOT the implementation agent.

You are NOT authorized to modify, rewrite, move, rename, delete, reorganize,
or replace Factory doctrine.

This is a READ-ONLY examination of the Factory DocSet AS IT EXISTS TODAY.

Your only authorized write target is:

astra-review/reviews/ASTRA_FACTORY_DOCTRINE_REVIEW_001.md

Do not modify any other file.

Do not commit.
Do not push.
Do not perform synchronization work.
Do not begin any Part 2 work.

==================================================
PART 1 SCOPE BOUNDARY
==================================================

PART 1 reviews ONLY the existing Factory DocSet currently present in this
repository on this branch.

There is NO incoming/candidate doctrine in scope.

There are NO:

- new E2E documents awaiting synchronization
- doctrine journals awaiting synchronization
- lessons-learned packages awaiting synchronization
- proposed rulings awaiting synchronization
- Claudy sync maps
- synchronization proposals

Those belong to a future Part 2 experiment.

The following directory is experiment infrastructure and is NOT Factory doctrine:

astra-review/

You may read:

astra-review/packets/ASTRA_FACTORY_DOCTRINE_REVIEW_PACKET_001.md

because it contains your governing instructions.

You may write ONLY:

astra-review/reviews/ASTRA_FACTORY_DOCTRINE_REVIEW_001.md

Do NOT evaluate the contents or structure of astra-review/ as part of the
Factory health assessment.

The reserved directory:

astra-review/intake/

is intentionally empty and OUT OF SCOPE.

==================================================
OBJECTIVE
==================================================

Perform a deep baseline health examination of the current Factory DocSet.

The purpose of this review is to determine:

- what the Factory is doing well
- what the Factory is doing poorly
- where technical or process doctrine is weak
- where doctrine conflicts across files
- where responsibilities or authority are unclear
- where important guidance is missing
- where guidance is obsolete
- where the system depends on undocumented tribal knowledge
- where unnecessary complexity or ceremony exists
- what genuinely needs correction
- what could meaningfully be improved
- how maintainable and executable the Factory is as a whole

This is not a writing-quality contest.

Judge the Factory primarily as an operating system for humans and AI agents.

==================================================
BUDGET
==================================================

REASONING LEVEL:

HIGH

DEFECT FINDINGS:

No numeric cap.

However:

- every DEFECT must satisfy the evidence standard below
- defects must be strictly ranked
- do not inflate the count
- do not split one underlying problem into many findings unnecessarily
- do not classify stylistic preferences as defects

SUGGESTIONS:

Maximum 15.

Suggestions must be ranked by expected operational value.

Do not include weak, cosmetic, or speculative suggestions merely to fill the cap.

==================================================
TOP 10 REQUIREMENT
==================================================

Immediately after the Executive Assessment, include:

TOP 10 — IF ONLY TEN THINGS GET FIXED

This list must contain the highest-value corrective actions supported by the
review.

Prioritize genuine defects over optional improvements.

Rank them.

If fewer than ten evidence-backed corrective actions are justified, list fewer
than ten.

Do not invent work to reach ten.

==================================================
STEP 1 — DISCOVER THE DOCSET
==================================================

Before judging the Factory, inspect the repository structure and determine the
current documentation corpus.

Discover the relevant files.

Do not assume every file in the repository is authoritative doctrine.

Classify material where appropriate, for example:

- current governing doctrine
- reference material
- operational/supporting material
- skills / agent instructions
- audit/evidence material
- archived or historical material
- repository infrastructure
- non-doctrine material

Do not silently treat archived material as current doctrine.

If current doctrine explicitly depends upon or references archived/historical
material, record that dependency.

Do not invent an authority hierarchy that the repository does not establish.

If authority is unclear, mark it AMBIGUOUS.

==================================================
STEP 2 — RECONSTRUCT THE FACTORY
==================================================

Before issuing substantive judgments, reconstruct the Factory operating model
you believe the current DocSet actually defines.

Describe, at minimum:

- Factory purpose
- major Factory roles
- human authority
- AI authority
- role boundaries
- lifecycle / project flow
- Architect flow
- Designer flow where applicable
- Engineer flow
- BIM flow
- FFM flow
- QA flow
- testing flow
- DevOps / deployment flow
- support / bug-fix flow
- handoff model
- evidence model
- gates and approval points
- branch / promotion model where documented
- source-of-truth rules
- regression expectations
- where humans must explicitly approve or intervene
- where AI agents are allowed to act independently

DO NOT invent missing rules.

If the corpus does not establish something clearly, mark it:

AMBIGUOUS

or

UNKNOWN

Ambiguity itself may become a finding if it materially affects execution.

==================================================
REVIEW DIMENSIONS
==================================================

Evaluate the Factory using these five dimensions.

1. CORRECTNESS

Is the technical and operational guidance sound?

2. CONSISTENCY

Do documents agree on:

- terminology
- roles
- authority
- gates
- workflows
- responsibilities
- handoffs
- evidence requirements

3. COMPLETENESS

Are important:

- responsibilities
- transitions
- failure paths
- controls
- verification steps
- ownership boundaries

missing?

4. EXECUTABILITY

Could a competent human or AI agent follow the written Factory doctrine and
reliably perform the intended work without depending on undocumented tribal
knowledge?

5. MAINTAINABILITY

Can the DocSet evolve without creating:

- contradiction
- duplication
- stale copies
- hidden dependencies
- role drift
- process drift
- excessive synchronization burden

==================================================
SCORING SCALE
==================================================

Use integer scores only.

5 — Strong / production-quality doctrine

4 — Good; limited improvements needed

3 — Functional but meaningful gaps exist

2 — Weak / inconsistent / difficult to execute safely

1 — Fundamentally broken or absent

Do not use decimal scores.

A score must be justified by evidence.

==================================================
DOMAIN REVIEW
==================================================

Review the Factory by domain where the corpus contains relevant doctrine.

Expected domains include:

- Factory governance / constitution
- application architecture
- database
- authentication
- authorization
- security
- APIs and services
- state management
- frontend engineering
- design system
- testing
- QA
- BIM lifecycle
- FFM lifecycle
- DevOps / deployment
- support
- bug fixing
- handoffs
- skills / agent operating instructions
- evidence / certification practices
- documentation governance
- change / promotion controls

You may identify additional domains if clearly supported by the repository.

Do not create artificial categories merely to expand the review.

==================================================
WHAT TO LOOK FOR
==================================================

Look specifically for:

- contradictions between files
- contradictory versions of the same workflow
- conflicting role ownership
- unclear decision authority
- unclear escalation authority
- stale doctrine
- obsolete instructions
- duplicate guidance likely to drift
- missing handoffs
- broken handoffs
- unclear gates
- gates without evidence requirements
- evidence requirements without ownership
- unclear acceptance criteria
- missing failure paths
- missing rollback paths where relevant
- ambiguous terminology
- inconsistent terminology
- unsafe technical guidance
- technically incorrect guidance
- process guidance that cannot realistically be executed
- hidden dependence on tribal knowledge
- unnecessary ceremony
- unnecessary complexity
- gaps between architecture and execution
- gaps between engineering and QA
- gaps between QA and deployment
- gaps between support and engineering
- weak regression controls
- weak source-of-truth rules
- process rules that different agents could reasonably interpret differently
- strengths that should explicitly be preserved

==================================================
FINDING TYPES
==================================================

Every finding must be classified as exactly one of:

DEFECT

or

SUGGESTION

--------------------------------------------------
DEFECT
--------------------------------------------------

Something demonstrably:

- wrong
- contradictory
- unsafe
- materially incomplete
- obsolete
- operationally broken
- ambiguous in a way that affects execution
- inconsistent in a way that can cause different outcomes

--------------------------------------------------
SUGGESTION
--------------------------------------------------

A meaningful improvement where the existing doctrine is not demonstrably wrong.

Do not convert preference into defect.

Do not grade writing style unless the writing materially prevents correct
execution.

==================================================
DEFECT SEVERITY
==================================================

BLOCKER

Could cause:

- unsafe execution
- incorrect authority
- serious security failure
- serious regression
- loss of required evidence
- destructive operation
- incorrect promotion/deployment
- systemic Factory unreliability

HIGH

A material operational weakness that should be corrected soon.

MEDIUM

A real weakness with limited immediate impact.

LOW

A minor but legitimate defect.

Suggestions do not require artificial severity unless impact clearly warrants it.

==================================================
EVIDENCE STANDARD
==================================================

Every DEFECT must contain:

- finding ID
- classification
- severity
- affected file(s)
- section / heading / precise location where reasonably possible
- evidence
- why the evidence demonstrates a defect
- operational consequence
- recommended resolution

Where a defect depends on conflicting documents, identify both sides.

Where evidence is insufficient, say so.

Do not manufacture certainty.

Do not silently infer missing policy.

==================================================
STRENGTHS
==================================================

This is not only a defect hunt.

Identify what the Factory is doing genuinely well.

For meaningful strengths, explain:

- what the practice is
- where it is documented
- why it is strong
- what should be preserved during future changes

Do not manufacture praise.

==================================================
FILE-BY-FILE REVIEW
==================================================

Include a file-by-file appendix for every substantive CURRENT Factory document
examined.

For each file, state briefly:

- path / filename
- purpose you infer
- authority / role you infer where determinable
- strengths
- defects, if any
- suggestions, if meaningful
- overlap or conflict with other current files
- dependencies on other files
- overall disposition

Use one of these dispositions:

STRONG

NEEDS ATTENTION

MATERIAL REVISION NEEDED

Do NOT create a separate review file for each source file.

All review results belong in the single canonical report.

==================================================
COVERAGE MANIFEST
==================================================

The final report must contain a Coverage Manifest.

The manifest must make the review coverage independently verifiable.

For every relevant file discovered during repository examination, record one of:

EXAMINED

NOT EXAMINED — <reason>

You may also identify files as:

OUT OF SCOPE — <reason>

when they clearly are not part of the Factory doctrine review, such as
experiment infrastructure.

Do not silently omit files.

If a file could not be:

- read
- parsed
- interpreted
- classified

record that explicitly.

The Coverage Manifest must make clear which current doctrine was actually
examined.

==================================================
INCREMENTAL WRITE REQUIREMENT
==================================================

Create and maintain exactly one canonical review report:

astra-review/reviews/ASTRA_FACTORY_DOCTRINE_REVIEW_001.md

Write the report incrementally.

Do NOT wait until the entire examination is finished and then perform one large
final write.

As each major section reaches a coherent state:

1. write or append that section to the canonical report
2. preserve completed work already on disk
3. continue the examination
4. refine later sections as additional evidence becomes available

The report on disk must represent the most complete valid state reached so far.

If the session is interrupted by:

- quota exhaustion
- safety review
- tool interruption
- context interruption
- terminal interruption
- unexpected failure
- human stop

the partial report must remain usable.

Clearly indicate incomplete sections if interruption occurs.

Do not create temporary alternative review reports.

The canonical incremental report is the recovery artifact.

==================================================
EXECUTIVE ASSESSMENT LIMIT
==================================================

The Executive Assessment must be no more than 400 words.

Tony reads this section first and may consume it through audio.

It must therefore be:

- direct
- information-dense
- understandable without reading the rest of the report
- explicit about overall Factory health
- explicit about the most serious weaknesses
- explicit about the strongest parts

Do not bury the conclusion.

==================================================
REPORT STRUCTURE
==================================================

Write the canonical report using this structure:

1. EXECUTIVE ASSESSMENT

Maximum 400 words.

2. TOP 10 — IF ONLY TEN THINGS GET FIXED

Rank the highest-value corrective actions.

3. RECONSTRUCTED FACTORY OPERATING MODEL

Describe the Factory the current corpus actually defines.

Clearly mark AMBIGUOUS and UNKNOWN areas.

4. OVERALL FIVE-DIMENSION SCORECARD

Score and explain:

- Correctness
- Consistency
- Completeness
- Executability
- Maintainability

5. DOMAIN SCORECARDS

Evaluate each substantive domain found in the current Factory.

6. WHAT THE FACTORY IS DOING WELL

Identify evidence-backed strengths that should be preserved.

7. RANKED DEFECT FINDINGS

List all evidence-backed defects.

No numeric cap.

Rank strictly by severity and operational impact.

8. RANKED SUGGESTIONS

Maximum 15.

Rank by expected value.

9. CROSS-DOCUMENT CONTRADICTIONS

Identify meaningful contradictions among CURRENT Factory documents.

Do not silently choose a winner where authority is unclear.

10. RECOMMENDED HUMAN DECISIONS

Identify decisions Tony / Architect / Factory leadership should explicitly make.

Do not make those decisions on their behalf.

11. FILE-BY-FILE REVIEW APPENDIX

Review every substantive current Factory document examined.

12. COVERAGE MANIFEST

List reviewed, unreviewed, and clearly out-of-scope files with reasons.

13. AMBIGUITIES / UNKNOWNS

Collect unresolved authority questions, missing evidence, unclear rules,
and areas where the corpus does not support a reliable conclusion.

14. FINAL FACTORY HEALTH ASSESSMENT

Provide the final evidence-based judgment of the Factory doctrine as it exists
today.

Clearly distinguish:

- defects requiring correction
- worthwhile improvements
- strengths that should remain untouched

==================================================
IMPORTANT CONSTRAINTS
==================================================

DO NOT:

- edit Factory doctrine
- rewrite Factory manuals
- rewrite Factory playbooks
- modify skills
- reorganize the repository
- move files
- rename files
- delete files
- create replacement doctrine
- create new Factory processes merely because you prefer them
- create new doctrine files
- modify README.md
- modify CLAUDE.md
- modify MANIFEST.md
- modify CHANGELOG.md
- modify repository configuration
- modify Git configuration
- modify astra-review/intake/
- modify the packet
- evaluate future Part 2 material
- perform DocSet synchronization
- commit
- push
- merge
- change branches
- optimize for politeness

Your ONLY authorized write target is:

astra-review/reviews/ASTRA_FACTORY_DOCTRINE_REVIEW_001.md

This is an examination, not an implementation task.

Be critical.

Be precise.

Be evidence-based.

==================================================
DONE LOOKS LIKE
==================================================

Done means:

- the current repository documentation corpus was discovered
- the current Factory operating model was reconstructed
- no future or candidate doctrine was introduced into the assessment
- major Factory domains were evaluated
- the five review dimensions were scored
- every substantive current Factory document received file-level review
- every relevant discovered file appears in the Coverage Manifest
- every unexamined or out-of-scope file has an explicit reason
- meaningful strengths were identified
- defects are evidence-backed
- defects are strictly ranked
- suggestions are clearly separated from defects
- suggestions do not exceed 15
- the Top 10 section is present
- the Executive Assessment does not exceed 400 words
- current-document contradictions are surfaced rather than silently resolved
- ambiguity is explicitly recorded rather than guessed away
- recommendations are actionable but not implemented
- the report was written incrementally
- exactly one review report was produced
- no existing Factory doctrine file was modified
- no file outside the authorized review report was modified
- no commit was created
- nothing was pushed
- no Part 2 work was performed

==================================================
FINAL OUTPUT PATH
==================================================

astra-review/reviews/ASTRA_FACTORY_DOCTRINE_REVIEW_001.md