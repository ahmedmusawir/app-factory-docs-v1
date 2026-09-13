# CHUNKY MONKEY
# EXECUTION PLAN
# ASTRA FACTORY DOCTRINE REVIEW — RUN 002

==================================================
1. PURPOSE
==================================================

This file defines the bounded review chunks for Run 002.

Every Astra review session must also obey:

astra-review/run-002/packets/CHUNK_REVIEW_CONTRACT.md

The Chunk Review Contract defines HOW to review.

This Execution Plan defines WHAT to review.

The objective is to examine the current Factory DocSet in bounded domains,
persist independent evidence from each domain, and defer Factory-wide judgment
to the final synthesis stage.

==================================================
2. GLOBAL EXECUTION RULES
==================================================

Run chunks in this order:

01 — Governance / Constitution
02 — Agents / Handoffs
03 — Build Method
04 — Auth / Data / Security
05 — API / Commerce
06 — Design / Frontend
07 — Skills / Documentation Governance
08 — Final Synthesis

Each numbered review chunk must use:

GPT-6 Astra
Reasoning: HIGH

Each chunk should normally begin in a FRESH Astra session.

Do not carry conversational history from a previous chunk when a clean session
can be used.

The persisted repository artifacts are the review memory.

For chunks 01–07:

- read CHUNK_REVIEW_CONTRACT.md
- read ONLY the current chunk definition below
- examine the assigned primary sources
- use cross-references only as permitted by the contract
- write only the assigned ASTRA_REVIEW.md
- stop when the chunk is complete

Do not perform final Factory synthesis during chunks 01–07.

==================================================
3. CHUNK 01 — GOVERNANCE / CONSTITUTION
==================================================

CHUNK ID:

01

DOMAIN:

Factory Governance / Constitution

PRIMARY SOURCE SCOPE:

01_CONSTITUTION/

Review every substantive current Markdown doctrine file contained in this
directory.

PERMITTED SUPPORTING CROSS-REFERENCES:

Root repository governance files may be opened only when needed to verify:

- authority
- source-of-truth rules
- lifecycle ownership
- repository doctrine classification
- human / AI boundaries

Examples may include:

- MANIFEST.md
- CLAUDE.md
- README.md

These remain cross-references unless explicitly assigned as primary sources in
another chunk.

OBJECTIVE:

Determine what the Factory considers authoritative and how the Factory is
governed.

FOCUS QUESTIONS:

1. What is the Factory's canonical lifecycle?
2. Who owns product decisions?
3. What authority belongs to humans?
4. What authority belongs to AI agents?
5. Where are approval gates required?
6. What is the source-of-truth hierarchy?
7. Are lifecycle definitions internally consistent?
8. Are role boundaries clearly established?
9. Are approval / lock / acceptance states clearly defined?
10. Could two competent operators interpret constitutional doctrine differently?
11. Are any constitutional rules stale, contradictory, or impossible to execute?
12. Which governance principles are especially strong and should be preserved?

OUT OF SCOPE:

- deep implementation review
- detailed QA mechanics
- technical security review
- detailed design-system review
- documentation synchronization process
- Part 2 material
- Run 001 findings

OUTPUT:

astra-review/run-002/chunks/01_governance/ASTRA_REVIEW.md

==================================================
4. CHUNK 02 — AGENTS / HANDOFFS
==================================================

CHUNK ID:

02

DOMAIN:

Factory Agent Roles / Ownership / Handoffs

PRIMARY SOURCE SCOPE:

02_PIPELINE_AGENTS/

Review every substantive current Markdown doctrine file contained in this
directory.

OBJECTIVE:

Determine whether Factory seats have clear, compatible, executable authority
and handoff boundaries.

FOCUS QUESTIONS:

1. What does each seat own?
2. What is each seat forbidden to own?
3. Where does human authority interrupt AI execution?
4. Are Architect responsibilities clear?
5. Are Designer responsibilities clear?
6. Are Engineer responsibilities clear?
7. Are QA responsibilities independent and clear?
8. Are DevOps responsibilities clear?
9. Are handoff inputs and outputs explicit?
10. Are approval boundaries consistent between seats?
11. Do two roles claim the same decision?
12. Does any responsibility fall between roles?
13. Can work advance without an accountable owner?
14. Are escalation rules sufficient?
15. Could two agents reading the same doctrine behave differently?
16. Which role separations are particularly strong and should be preserved?

PERMITTED CROSS-REFERENCES:

Chunk 01 source material may be consulted only when necessary to verify
constitutional authority.

Do not read Chunk 01 Astra/Fable/Sol review artifacts.

OUTPUT:

astra-review/run-002/chunks/02_agents_handoffs/ASTRA_REVIEW.md

==================================================
5. CHUNK 03 — BUILD METHOD
==================================================

CHUNK ID:

03

DOMAIN:

Factory Build / Change / QA Methodology

PRIMARY SOURCE SCOPE:

03_BUILD_METHODOLOGY/

Review every substantive current Markdown doctrine file contained in this
directory.

OBJECTIVE:

Determine whether the Factory can reliably take bounded approved work from
recon through implementation, verification, QA, remediation, deployment
handoff, and closure.

FOCUS QUESTIONS:

1. Are BIM mechanics coherent and executable?
2. Are FFM mechanics coherent and executable?
3. Are FEAT / feature-change mechanics coherent where present?
4. Are bug-fix/support mechanics coherent where present?
5. Is recon performed at the correct points?
6. Are planning and approval gates clear?
7. Is implementation adequately bounded?
8. Are acceptance contracts explicit?
9. Are regression requirements adequate?
10. Is independent QA preserved?
11. Are remediation loops bounded?
12. Are rollback / recovery expectations sufficient?
13. Are branch / promotion responsibilities clear?
14. Are evidence packages sufficient?
15. Are module-close and retrospective rules clear?
16. Are multiple execution maps properly nested or contradictory?
17. Does unnecessary ceremony exist?
18. Which methodology protections should not be weakened?

PERMITTED CROSS-REFERENCES:

01_CONSTITUTION/ and 02_PIPELINE_AGENTS/ only when required to verify authority
or ownership.

Do not read prior chunk review artifacts.

OUTPUT:

astra-review/run-002/chunks/03_build_method/ASTRA_REVIEW.md

==================================================
6. CHUNK 04 — AUTH / DATA / SECURITY
==================================================

CHUNK ID:

04

DOMAIN:

Authentication / Authorization / Database / Data Security / Application Trust

PRIMARY SOURCE SCOPE:

Within:

04_REFERENCE_MANUALS/

Primary sources are the current doctrine files whose principal subject is:

- authentication
- authorization
- identity
- roles / permissions
- database
- persistence
- tenant isolation
- RLS
- sensitive-data handling
- application security boundaries
- state/data authority where directly relevant

Before substantive review:

1. discover the files in 04_REFERENCE_MANUALS/
2. classify them by principal subject
3. list exactly which files you are treating as Chunk 04 primary sources
4. do not silently absorb API/commerce-only material assigned to Chunk 05

OBJECTIVE:

Determine whether the Factory's identity, authority, persistence, tenancy, and
data-security doctrine is technically sound and internally consistent.

FOCUS QUESTIONS:

1. What is authoritative identity truth?
2. What is authoritative role / permission truth?
3. Are privileged operations independently authorized?
4. Is caller-controlled metadata ever trusted incorrectly?
5. Are service-role / admin capabilities properly bounded?
6. Are tenant boundaries adequately defined?
7. Is RLS doctrine technically sound?
8. Are public/private data boundaries clear?
9. Are database ownership and mutation rules clear?
10. Are sensitive-data paths adequately protected?
11. Are security examples consistent with stated security principles?
12. Do example implementations accidentally undermine doctrine?
13. Are negative/adversarial tests expected where appropriate?
14. Are application-state and database authority boundaries clear?
15. Which security/data principles are particularly strong?

PERMITTED CROSS-REFERENCES:

Other current doctrine only when required to verify an explicit security,
authority, or data dependency.

Do NOT inspect Run 001 findings.

OUTPUT:

astra-review/run-002/chunks/04_auth_data_security/ASTRA_REVIEW.md

==================================================
7. CHUNK 05 — API / COMMERCE
==================================================

CHUNK ID:

05

DOMAIN:

APIs / Services / Integrations / Commerce / Payments

PRIMARY SOURCE SCOPE:

Within:

04_REFERENCE_MANUALS/

Primary sources are the current doctrine files whose principal subject is:

- APIs
- services
- external service integration
- commerce
- checkout
- payments
- Stripe/subscriptions
- webhooks
- external contracts

Before substantive review:

1. discover the files in 04_REFERENCE_MANUALS/
2. classify them by principal subject
3. list exactly which files you are treating as Chunk 05 primary sources
4. do not duplicate full review of Chunk 04 sources

OBJECTIVE:

Determine whether service-boundary, integration, payment, webhook, and commerce
doctrine is technically sound, secure, executable, and consistent.

FOCUS QUESTIONS:

1. Are client/server trust boundaries explicit?
2. Are API contracts clear?
3. Are privileged mutations properly protected?
4. Are monetary values sourced from trusted authority?
5. Are checkout/payment examples safe?
6. Are webhook authenticity and processing reliability separated correctly?
7. Are duplicate/replayed/out-of-order events addressed where necessary?
8. Are failure and retry semantics clear?
9. Are external service errors handled safely?
10. Are API-side negative tests expected?
11. Are integration ownership and recovery paths clear?
12. Could copied examples create insecure implementations?
13. Are documentation principles contradicted by executable examples?
14. Which integration principles should be preserved?

PERMITTED CROSS-REFERENCES:

Chunk 04 security/data source files may be opened only when needed to verify
security or authority dependencies.

Do not read Chunk 04 review artifacts.

OUTPUT:

astra-review/run-002/chunks/05_api_commerce/ASTRA_REVIEW.md

==================================================
8. CHUNK 06 — DESIGN / FRONTEND
==================================================

CHUNK ID:

06

DOMAIN:

Design System / Frontend / Visual Implementation

PRIMARY SOURCE SCOPE:

05_DESIGN_SYSTEM/

Review every substantive current Markdown doctrine file contained in this
directory.

Also inspect directly relevant frontend/design doctrine elsewhere only as
cross-references when necessary.

OBJECTIVE:

Determine whether design intent can be translated into reproducible,
high-fidelity, testable frontend implementation without ambiguity between
Designer and Engineer.

FOCUS QUESTIONS:

1. Is token authority clear?
2. Is canonical visual approval clear?
3. Are Designer outputs executable enough for Engineer consumption?
4. Are UI_SPEC responsibilities clear?
5. Are component-reuse expectations coherent?
6. Are responsive requirements sufficiently defined?
7. Are theme requirements sufficiently defined?
8. Are accessibility expectations actionable?
9. Is visual evidence required at meaningful points?
10. Are Designer/Engineer boundaries consistent?
11. Are frontend-first rules compatible with general Factory doctrine?
12. Are screenshot/render acceptance mechanisms adequate?
13. Is visual regression protected?
14. Is unnecessary design ceremony present?
15. Which design/frontend mechanisms are particularly strong?

PERMITTED CROSS-REFERENCES:

Relevant Designer, Engineer, FFM, frontend-first, or testing doctrine may be
opened only when needed to verify an explicit dependency.

Do not review those entire neighboring domains.

OUTPUT:

astra-review/run-002/chunks/06_design_frontend/ASTRA_REVIEW.md

==================================================
9. CHUNK 07 — SKILLS / DOCUMENTATION GOVERNANCE
==================================================

CHUNK ID:

07

DOMAIN:

Skills / Agent Instructions / Documentation Governance / Repository Operations

PRIMARY SOURCE SCOPE:

_SKILLS/

agent_docs/

and the current root-level files governing or describing the Factory repository
itself, where applicable, including:

- CLAUDE.md
- MANIFEST.md
- README.md
- RECOVERY.md
- CHANGELOG.md

Inspect additional root governance/support files only when they clearly
participate in current DocSet operation.

Do NOT treat historical session logs or archived evidence as current doctrine
without explicit current authority.

OBJECTIVE:

Determine whether the Factory documentation system and agent-operating layer can
be understood, maintained, changed, recovered, and executed without hidden
tribal knowledge or authority confusion.

FOCUS QUESTIONS:

1. Can a new competent agent determine what is authoritative?
2. Is the repository manifest accurate?
3. Are skills clearly scoped?
4. Do skills agree with governing doctrine?
5. Are skill permissions sufficiently bounded?
6. Are agent instructions deterministic enough?
7. Are recovery procedures adequate?
8. Is repository structure understandable?
9. Are current versus archived materials clearly separated?
10. Are update/change responsibilities clear?
11. Are documentation dependencies discoverable?
12. Is duplicate doctrine likely to drift?
13. Does the repository rely on Tony/Fable/Sol knowing things that the written
    system does not establish?
14. Can a fresh agent enter this repository and operate safely?
15. Which documentation-governance mechanisms are especially strong?

OUT OF SCOPE:

The FUTURE Part 2 DocSet synchronization experiment.

Do not judge incoming E2E documents, doctrine journals, unsynced lessons, or a
future Claudy sync map.

This chunk reviews ONLY the CURRENT operating/documentation layer.

OUTPUT:

astra-review/run-002/chunks/07_skills_doc_governance/ASTRA_REVIEW.md

==================================================
10. CHUNK 08 — FINAL SYNTHESIS
==================================================

CHUNK ID:

08

DOMAIN:

Cross-Factory Synthesis

DO NOT EXECUTE UNTIL CHUNKS 01–07 ARE COMPLETE.

The detailed synthesis procedure will be governed by:

astra-review/run-002/packets/SYNTHESIS_CONTRACT.md

That contract is intentionally not finalized yet.

The synthesis stage will consume the completed chunk evidence and selectively
verify original doctrine where required.

Expected final output:

astra-review/run-002/synthesis/ASTRA_FACTORY_DOCTRINE_REVIEW_RUN_002.md

Do not perform synthesis during chunks 01–07.

==================================================
11. CHUNK ISOLATION RULE
==================================================

During an Astra chunk examination:

DO NOT read:

- FABLE_REVIEW.md
- SOL_REVIEW.md
- DISPOSITION.md
- another chunk's ASTRA_REVIEW.md
- Run 001 review material

unless a later explicitly approved synthesis procedure requires it.

The original Factory corpus is the evidence source.

The purpose is independent examination.

==================================================
12. AFTER EACH CHUNK
==================================================

When Astra completes a chunk:

1. Astra stops.

2. Tony records telemetry.

3. Fable reviews Astra's output and writes:

   FABLE_REVIEW.md

4. Sol independently reviews Astra's output and writes:

   SOL_REVIEW.md

5. Tony, informed by the review seats, records disposition in:

   DISPOSITION.md

6. The chunk is checkpointed in Git by Tony.

7. Only then does the Factory proceed to the next chunk.

Astra does not perform these downstream review/disposition steps.

==================================================
13. GLOBAL STOP RULE
==================================================

ONE ASTRA SESSION = ONE ASSIGNED CHUNK.

When the chunk is complete:

STOP.

Never automatically proceed to the next chunk.

Never automatically begin synthesis.

The human Factory decides when the next bounded examination starts.

==================================================
14. RUN 002 END STATE
==================================================

When chunks 01–07 are complete, Run 002 should contain seven independent
evidence packages.

Each package contains:

ASTRA_REVIEW.md
FABLE_REVIEW.md
SOL_REVIEW.md
DISPOSITION.md

Only then may Chunk 08 / Final Synthesis begin.

==================================================
15. EXECUTION PRINCIPLE
==================================================

THE CONTRACT DEFINES HOW.

THE EXECUTION PLAN DEFINES WHAT.

THE CHUNK DEFINES THE BATTLEFIELD.

ASTRA EXAMINES.

FABLE AND SOL CHALLENGE.

TONY DISPOSITIONS.

SYNTHESIS JUDGES THE WAR.