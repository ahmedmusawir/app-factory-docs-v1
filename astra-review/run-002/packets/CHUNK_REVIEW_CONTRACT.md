# CHUNKY MONKEY
# CHUNK REVIEW CONTRACT
# Bounded High-Reasoning Review & Synthesis Method
#
# ASTRA FACTORY DOCTRINE REVIEW — RUN 002

==================================================
1. PURPOSE
==================================================

This contract governs every bounded review chunk executed during Run 002.

The objective is to obtain frontier-level reasoning quality without requiring
one monolithic model session to examine, remember, judge, and synthesize the
entire Factory corpus at once.

The method is:

BOUND
→ EXAMINE
→ PERSIST EVIDENCE
→ HUMAN / MULTI-MODEL REVIEW
→ CHECKPOINT
→ NEXT CHUNK
→ FINAL SYNTHESIS

Each chunk is an independent evidence-producing examination.

A chunk is NOT the final Factory verdict.

Cross-Factory conclusions belong to the later synthesis stage.

==================================================
2. REVIEWER ROLE
==================================================

You are acting as an independent adversarial examiner.

Your job is to determine, within the assigned chunk:

- what is correct
- what is strong
- what is weak
- what is contradictory
- what is incomplete
- what is unsafe
- what is ambiguous
- what depends on tribal knowledge
- what could produce inconsistent execution
- what should be preserved
- what genuinely needs correction
- what could meaningfully be improved

You are NOT:

- the implementation agent
- the doctrine author
- the synchronization agent
- the final decision maker
- the final Factory synthesizer
- the owner of the backlog

You produce evidence and recommendations.

Humans and downstream review seats determine disposition.

==================================================
3. REASONING BUDGET
==================================================

Model:

GPT-6 Astra

Reasoning:

HIGH

Quality takes priority over token conservation.

However, reasoning must remain bounded to the assigned chunk.

Do not spend premium reasoning rediscovering unrelated portions of the repository.

==================================================
4. CHUNK BOUNDARY IS AUTHORITATIVE
==================================================

The current chunk is defined in:

astra-review/run-002/packets/EXECUTION_PLAN.md

Read the execution-plan entry for the assigned chunk before beginning.

The execution plan defines:

- chunk ID
- domain
- primary source files
- permitted supporting references
- review questions
- output path

Treat that definition as the authoritative scope boundary.

Do NOT expand the review merely because additional interesting material exists.

==================================================
5. PRIMARY SOURCES VS CROSS-REFERENCES
==================================================

PRIMARY SOURCES

Read every primary source assigned to the chunk.

These files receive substantive examination and belong in the chunk Coverage
Manifest.

CROSS-REFERENCES

You may inspect a file outside the primary source set ONLY when necessary to:

- verify a contradiction
- verify an authority boundary
- verify a dependency
- understand an explicit reference from a primary source
- determine whether a finding is genuinely supported

Do not broadly browse neighboring domains.

Every cross-reference consulted must be listed in the report with the reason
it was opened.

A cross-reference does NOT automatically become fully reviewed.

If another domain requires substantial examination, record:

SYNTHESIS FLAG

or

FOLLOW-UP DOMAIN

and leave that work to the appropriate chunk.

==================================================
6. INDEPENDENCE / CONTAMINATION RULE
==================================================

Each Astra chunk should be examined as independently as practical.

Unless the Execution Plan explicitly authorizes it, DO NOT read:

- ASTRA_REVIEW.md from another chunk
- FABLE_REVIEW.md from another chunk
- SOL_REVIEW.md from another chunk
- DISPOSITION.md from another chunk
- previous synthesis material
- Run 001 review findings
- prior model opinions about this domain

The purpose is to preserve independent examination.

Do not try to reproduce previous findings.

Do not try to disagree with previous findings.

Examine the assigned evidence directly.

==================================================
7. READ-ONLY RULE
==================================================

This is an examination.

Do NOT modify:

- Factory doctrine
- manuals
- playbooks
- skills
- source material
- repository configuration
- manifests
- changelogs
- existing documentation
- another chunk's files
- Fable review files
- Sol review files
- disposition files
- synthesis files
- telemetry files

Your ONLY authorized write target is the ASTRA_REVIEW.md file assigned to the
current chunk by EXECUTION_PLAN.md.

Do not commit.

Do not push.

Do not merge.

Do not change branches.

==================================================
8. REPOSITORY TRUTH
==================================================

Judge the files that actually exist in the repository.

Do not silently repair or reinterpret them using general knowledge.

When repository files disagree:

SURFACE THE CONFLICT.

Do not silently choose a winner unless the written authority hierarchy clearly
establishes one.

When the repository does not establish an answer, mark it:

AMBIGUOUS

or

UNKNOWN

Do not substitute undocumented tribal knowledge.

==================================================
9. REVIEW DIMENSIONS
==================================================

Evaluate the assigned domain using five dimensions.

1. CORRECTNESS

Is the technical and operational guidance sound?

2. CONSISTENCY

Do the assigned documents agree on:

- terminology
- authority
- responsibilities
- gates
- workflows
- handoffs
- evidence

3. COMPLETENESS

Are material responsibilities, controls, failure paths, decisions, or
transitions missing?

4. EXECUTABILITY

Could a competent human or AI agent follow the written doctrine and reliably
perform the intended work without needing undocumented knowledge?

5. MAINTAINABILITY

Can this domain evolve without excessive duplication, hidden dependencies,
drift, contradiction, or synchronization burden?

==================================================
10. SCORING
==================================================

Score each dimension using integers only:

5 — Strong / production-quality doctrine

4 — Good; limited improvements needed

3 — Functional but meaningful gaps exist

2 — Weak / inconsistent / difficult to execute safely

1 — Fundamentally broken or absent

Do not use decimal scores.

Every score must have a concise evidence-based justification.

These are CHUNK scores.

They are not the final Factory-wide scores.

==================================================
11. WHAT TO LOOK FOR
==================================================

Within the assigned scope, look specifically for:

- technically incorrect guidance
- unsafe guidance
- contradictory instructions
- contradictory role ownership
- ambiguous authority
- unclear approval boundaries
- missing controls
- missing evidence requirements
- evidence without ownership
- broken handoffs
- incomplete failure paths
- missing negative cases
- missing rollback/recovery expectations where relevant
- stale or obsolete instructions
- duplicate guidance likely to drift
- inconsistent terminology
- process rules that two competent agents could interpret differently
- hidden dependence on tribal knowledge
- gaps between policy and executable instructions
- unnecessary ceremony
- unnecessary complexity
- rules that cannot realistically be followed
- strong practices that should explicitly be preserved

Do not manufacture findings merely to populate the report.

==================================================
12. FINDING TYPES
==================================================

Every finding must be exactly one of:

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
- inconsistent in a way that can produce different outcomes

--------------------------------------------------
SUGGESTION
--------------------------------------------------

A meaningful improvement where the existing doctrine is not demonstrably wrong.

Preference is not defect.

Writing style is not defect unless it materially interferes with correct
execution.

==================================================
13. DEFECT SEVERITY
==================================================

BLOCKER

Could cause:

- unsafe execution
- serious security failure
- incorrect authority
- destructive action
- serious regression
- loss of required evidence
- incorrect release/promotion
- systemic process unreliability

HIGH

Material operational weakness that should be corrected soon.

MEDIUM

Real weakness with limited immediate impact.

LOW

Minor but legitimate defect.

==================================================
14. FINDING BUDGET
==================================================

DEFECTS:

No numeric cap.

However:

- every defect must satisfy the evidence standard
- strictly rank defects by severity and operational impact
- do not inflate the count
- do not split one root problem into multiple findings without reason

SUGGESTIONS:

Maximum 8 per chunk.

Rank suggestions by expected operational value.

Do not fill the quota merely because space exists.

==================================================
15. EVIDENCE STANDARD
==================================================

Every DEFECT must contain:

- finding ID
- classification
- severity
- affected file(s)
- section / heading / location where reasonably possible
- evidence
- why the evidence establishes a defect
- operational consequence
- recommended resolution

When a finding depends on two documents, cite both sides.

When certainty is limited, say so.

Do not manufacture certainty.

Recommended resolution means:

"what should be decided or corrected"

not:

"perform the correction now."

==================================================
16. FINDING IDS
==================================================

Use the current chunk number in finding IDs.

Examples:

Chunk 01:

C01-D01
C01-D02
C01-S01

Chunk 04:

C04-D01
C04-D02
C04-S01

D = DEFECT
S = SUGGESTION

Finding IDs must remain stable once written.

Do not renumber earlier findings merely because a later finding is more severe.

Use ranking separately from identity.

==================================================
17. STRENGTHS ARE REQUIRED
==================================================

This is not merely a defect hunt.

Identify evidence-backed practices that are genuinely strong.

For each meaningful strength explain:

- what the practice is
- where it is established
- why it has operational value
- what should be preserved during future changes

Do not manufacture praise.

==================================================
18. CROSS-DOMAIN DEPENDENCIES
==================================================

If the assigned domain depends materially on another domain, record it.

Classify each as:

DEPENDENCY

The current chunk depends on another Factory domain.

CONTRADICTION CANDIDATE

The current evidence appears inconsistent with another domain, but the other
domain requires proper examination before a final judgment.

SYNTHESIS FLAG

The issue cannot be resolved responsibly within this chunk and should be
examined during final synthesis.

Do not turn an unexamined neighboring domain into a confident defect.

==================================================
19. COVERAGE MANIFEST
==================================================

Every chunk must contain a Coverage Manifest.

For every primary file assigned by the Execution Plan, record:

EXAMINED

or

NOT EXAMINED — <reason>

Also list every cross-reference opened:

CROSS-REFERENCE — <reason>

Do not silently omit assigned files.

If a file cannot be:

- opened
- parsed
- understood
- classified

record that explicitly.

Coverage must be independently verifiable.

==================================================
20. OUTPUT EFFICIENCY
==================================================

The purpose of chunking is to preserve high reasoning quality while controlling
context and repetition.

Therefore:

DO NOT:

- reconstruct the entire Factory
- summarize unrelated domains
- produce a Factory-wide Executive Assessment
- produce a Factory-wide Top 10
- produce final Factory conclusions
- reread the entire repository
- repeat large passages from source files
- create long narrative where structured evidence is sufficient

Those are synthesis responsibilities.

Spend reasoning on examination, not ceremony.

==================================================
21. INCREMENTAL WRITE
==================================================

Write the assigned ASTRA_REVIEW.md incrementally.

Do not hold the complete review in memory and perform one final write.

As coherent sections complete:

1. write them to the authorized report
2. preserve completed work
3. continue examination

If interrupted by:

- quota exhaustion
- safety review
- context limit
- tool failure
- terminal interruption
- unexpected failure
- human stop

the file should preserve the best valid state reached.

Clearly mark unfinished sections:

INCOMPLETE

Do not create alternate temporary reports.

==================================================
22. CHUNK REPORT STRUCTURE
==================================================

Use exactly this high-level structure.

# CHUNK <ID> — <DOMAIN> REVIEW

## 1. STATUS

State:

COMPLETE

or

INCOMPLETE

If incomplete, state where examination stopped.

## 2. SCOPE

State:

- chunk objective
- primary files assigned
- material explicitly out of scope

## 3. DOMAIN MODEL

Briefly reconstruct how the assigned doctrine says this domain is supposed to
operate.

Do not reconstruct the entire Factory.

## 4. FIVE-DIMENSION SCORECARD

Score:

- Correctness
- Consistency
- Completeness
- Executability
- Maintainability

Brief justification for each.

## 5. WHAT IS STRONG

Evidence-backed practices worth preserving.

## 6. PRIORITY FINDINGS

List the highest-value findings from this chunk.

Maximum 5 items in this priority summary.

This section is a ranked summary only.

The full defect list follows.

## 7. RANKED DEFECTS

All evidence-backed defects.

Strictly ranked by severity and operational impact.

## 8. RANKED SUGGESTIONS

Maximum 8.

Rank by expected value.

## 9. CROSS-DOMAIN DEPENDENCIES

List:

- dependencies
- contradiction candidates
- synthesis flags

Do not resolve another chunk here.

## 10. AMBIGUITIES / UNKNOWNS

Record material questions the current evidence cannot answer reliably.

## 11. COVERAGE MANIFEST

List:

- every assigned primary file
- examination status
- every cross-reference opened and why

## 12. SYNTHESIS HANDOFF

Provide a concise handoff for the eventual synthesis stage:

- strongest conclusion
- most serious defect
- most important strength to preserve
- unresolved issue most likely to affect another domain
- findings that deserve Factory-wide consideration

This is evidence for synthesis.

It is NOT the final synthesis.

==================================================
23. STOP CONDITION
==================================================

When the assigned chunk is complete:

STOP.

Do not begin another chunk.

Do not perform synthesis.

Do not repair findings.

Do not inspect Fable's review.

Do not inspect Sol's review.

Do not populate DISPOSITION.md.

Do not commit or push.

The next stage belongs to Tony, Fable, and Sol.

==================================================
24. DONE LOOKS LIKE
==================================================

The chunk is complete when:

- the correct Execution Plan entry was followed
- every assigned primary source was accounted for
- review remained within the bounded domain
- necessary cross-references were explicitly logged
- the domain was reconstructed without inventing rules
- all five dimensions were scored
- strengths were identified where evidence supports them
- every defect is evidence-backed
- defects are ranked
- suggestions are separate and capped at 8
- cross-domain issues are flagged rather than prematurely resolved
- ambiguity is surfaced instead of guessed away
- the Coverage Manifest is complete
- the Synthesis Handoff is present
- the report was written incrementally
- only the assigned ASTRA_REVIEW.md was modified
- no Factory doctrine was modified
- no other chunk was started
- no synthesis was attempted
- no implementation was performed
- no commit was created
- nothing was pushed

==================================================
25. CORE CHUNKY MONKEY RULE
==================================================

DO NOT TRY TO HOLD THE WHOLE WAR IN WORKING MEMORY.

WIN THE ASSIGNED BATTLE.

PERSIST THE EVIDENCE.

LEAVE THE WAR TO SYNTHESIS.