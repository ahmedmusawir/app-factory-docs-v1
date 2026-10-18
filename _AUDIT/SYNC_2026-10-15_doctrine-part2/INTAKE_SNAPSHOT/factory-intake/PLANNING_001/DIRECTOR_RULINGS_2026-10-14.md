# Director Rulings — 2026-10-14 (attributable ruling record for Planning 001)

> **RULING RECORD — recorded by the Engineer seat from the Director's instruction. It records decisions; it is not sync cargo, not an UPDATE MAP, not intake approval of either package, and not authorization for canonical edits, an `_INBOX/` drop, skill changes or Git actions.**

| Field | Value |
|---|---|
| Decision date | 2026-10-14 |
| Approver | Tony (Director) |
| Relayed in | Instruction "CLAUDY — RECONCILE DIRECTOR RULINGS AND FINAL QAM PLAYBOOK" (2026-10-14), which replaces Jarvis's previous unexecuted reconciliation prompt and incorporates the cleanup clarification |
| Recorded by | Claudy (documentation Engineer seat), 2026-10-14 14:50 +0600. Ruling text below is preserved from the instruction; paraphrase is marked |
| Source material approved by this ruling | `factory-intake/QAM_PLAYBOOK_v1_0.md` — "QAM PLAYBOOK v1.0", QA Lead / JARVIS, 2026-10-14; 252 lines, 30,650 bytes; SHA-256 `97e111e2a495f9a3fe65f50213e6f2ba68c8e5e963f3d23493b1ee99ad35c897` (Claudy-computed on receipt; the file is outside `FILE_INDEX.json` and is never edited) |
| Planning companions | `COMBINED_DECISIONS_001.md` (R1), `COMBINED_DEPENDENCY_MAP_001.md` (R1), `INTAKE_CLARIFICATIONS_001.md` (R1) |
| Correction package | `factory-corrections/FACTORY_DOCTRINE_CORRECTION_INDEX_001.md` R3 (decision-status annotations only) + `DECISION_RECORD_001.md` (2026-10-12, unchanged) |
| Revision | **R1.2 (2026-10-14 19:15 +0600):** RUL-02 effect cell reworded "completed engineering candidate commit" (Jarvis); verbatim ruling text unchanged. **R1.1 (2026-10-14 18:50 +0600):** two Engineer-written "Effect" cells corrected after Jarvis's review (RUL-01 QAM-04 row; RUL-05 WF-11 row) and the closing templates bullet updated. **The verbatim ruling text is unchanged.** R1 (14:50): initial record. |

**ID conventions.** `RUL-nn` are local to this record. `A.1 … C.1` are the navigation labels of `COMBINED_DECISIONS_001.md`; they are not decision IDs and must not appear in sync artifacts, which cite the DEC / ND / WF / RRM / QAM IDs listed per ruling. "RESOLVED" means the ruling answers the question; "NARROWED" means part of the question is answered and the remainder stays OPEN.

---

## RUL-01 — Mandatory QAM (navigation label A.1)

**Ruling (verbatim).** "QAM_PLAYBOOK_v1_0.md is Director-approved source material for inclusion in the Factory DocSet. Every newly authored module MUST include a complete, module-specific QAM/ from initial Architect packaging. No optional adoption or opt-in."

Ownership (verbatim): "QA Lead authors and maintains the reusable QAM playbook. Architect uses it to instantiate the module's QAM structure, instructions, contract references and readiness requirements. Engineer completes factual manifest and engineering handoff. QA Executor independently performs recon and drafts the test plan. QA Lead reviews and approves that specific plan. QA Executor executes after approval and candidate release. QA Lead adjudicates findings and certifies."

Two planned QA shots (verbatim): "Q1 = independent recon + test planning + indexed review package. Q2 = approved continuous execution + indexed results package. Repair/retest is conditional. Genuine blockers remain reportable. Do not prefill independent QA results or certification. Do not treat two shots as permission to skip approval or required work."

**Resolves.**
| ID | Status | Effect |
|---|---|---|
| ND-01 (QAM scope) | **RESOLVED** | Mandatory for every newly authored module of every type, including future types; not optional, not opt-in. Replaces the planning recommendation "optional per module contract". |
| QAM-01, QAM-14 (adoption boundary, promotion) | RESOLVED | Adoption status is mandatory; the "two internal profiles" promotion threshold is moot for adoption. Unimplemented tooling stays unapproved (RUL-07). |
| QAM-02 (five seats) | RESOLVED for the seats | Director · Architect · Engineer · QA Lead · QA Executor are the seats the ruling uses. Seat names are terminology, not permission grants (see "Boundaries"). |
| QAM-03 (package readiness and ownership) | RESOLVED | Architect instantiates from the playbook; Engineer completes manifest and handoff; no prefilled QA results. |
| QAM-05 (checkpoint sequence) | RESOLVED | Two planned shots Q1 and Q2; Q1b is approval bookkeeping (playbook §9); repair/retest (Q4) conditional; cleanup/certification/closeout per RUL-03. |
| QAM-04 (dual entry files) | RESOLVED | Playbook §6 requires `QAM/CLAUDE.md` and `QAM/AGENTS.md`, identical routing, both assigning the QA Executor seat. ~~The parent-module and FFM entry convention (COMBINED_DECISIONS D.4) is **not** ruled here.~~ **R1.1 correction (Jarvis):** playbook §6 also requires that "at the parent module, both entry conventions must route Engineering to the implementation assignment and QA to QAM"; because the playbook is approved source material, D.4 is resolved for both the `QAM/` files and the parent-module routing. The FFM_PLAYBOOK §8.3 wording is an UPDATE MAP drafting item, not an open decision. |
| QAM-06 … QAM-12 (preflight, credentials, instruments, findings, evidence, packages, metrics) | RESOLVED as source material | The playbook sections 8–15 and 17 are approved source text; integration wording is proposed in the UPDATE MAP (D17). |
| DEC-07 (seat glossary) | **NARROWED** | The ruling uses "Director" for the human seat and establishes "QA Executor" as a seat. Still OPEN: the glossary host, whether Operator/Coordinator remain synonyms, and whether any rename is made (COMBINED_DECISIONS D.1). |
| WF-05 ("QAM manifest where applicable") | RESOLVED | "Where applicable" becomes "always, for newly authored modules". |
| RRM-05 (QAM interface) | RESOLVED | Every RRM includes QAM (RUL-05). |

**Does not decide.** Retroactive application to modules already in flight (the ruling says "newly authored"; existing live modules keep their own sequence until amended, QAM-05). Any tooling build (RUL-07). Where the template set lives (RUL-06 / DEC-19).

## RUL-02 — Continuing QA branch; no disposable branches (navigation label A.2)

**Ruling (verbatim).** "The module has a numbered engineering branch, such as bim-000. After Engineering, Tony commits/pushes the work and creates the matching qa/bim-000 branch at that same starting commit. Engineer performs authorized rework on that QA branch. QA Executor independently tests on that same branch. Preserve role boundaries and avoid conflicting simultaneous writes. QA Lead certifies the governed candidate. Architect issues the closeout instruction. Engineer performs bounded closeout. Tony commits, merges the QA branch into main and pushes main. Do not transfer repairs back to the engineering branch or abandon the QA branch as the normal workflow. Preserve product, execution, evidence and closeout identities. This describes project-module policy. It does not silently amend DocSet Sync's separate Hub Git rules or authorize Git actions now."

**Resolves.**
| ID | Status | Effect |
|---|---|---|
| A.2 (planning question "which QA branch rule does the Hub state?") | **RESOLVED by a fresh Director decision** | The Hub states the continuing QA branch: `<module-branch>` → `qa/<module-branch>` created by the Director at the completed engineering candidate commit (the ruling's "same starting commit"; R1.2 wording per Jarvis) → rework and independent testing on that branch → certification → closeout → Director merges `qa/<module-branch>` into `main`. This is a new ruling, not an inferred supersession; the missing J-11 (CL-11) is no longer needed to decide it. |
| RRM-06 (forward certification line) | RESOLVED | Adopted in the Director's wording above. "One active writer when sessions share a worktree" survives as "avoid conflicting simultaneous writes". |
| WF-07 (branch sentence) | RESOLVED | The August BIM "abandon the QA branch by default" rule (SRC-W06 §8, REPORTED DIRECTOR RULING 2026-08-24) is **retired for module QA** by this later Director ruling. Its three guardrails survive in other form: tested-SHA and certified-revision identities are preserved; fixes stay on the QA line; harvest scripts are not needed because nothing is transferred back. |
| QAM-09 (repair on the QA line) | RESOLVED | Engineer repairs approved paths on the QA branch; Director commits; Executor re-pins and retests. |
| RRM-07 (merge identities) | RESOLVED for the branch part | Implementation, execution, evidence and closeout identities recorded separately; merge is the Director's. |
| DEC-18 (git authority matrix) | **NARROWED** | The module-QA Git flow is ruled (who creates `qa/…`, who commits, who merges). Still OPEN: cloud/deploy authority, "may the Engineer deploy to staging in FFM runs?", the DevOps seat occupant (COMBINED_DECISIONS C.2). |
| DEC-13 (home of QA artifacts) | contributes | See RUL-04. |

**Does not decide.** DocSet Sync's own Hub Git rules (family `CLAUDE.md` D5) are untouched. No Git action is authorized by this record.

## RUL-03 — Necessary QA cleanup remains required (navigation label A.3)

**Ruling (verbatim).** "Tony clarified that he had confused necessary QA cleanup with the retired disposable-branch transfer-back cleanup. Preserve QAM_PLAYBOOK_v1_0.md §14: credential and temporary authentication-state hygiene; closing owned QA processes and browser contexts; authorized removal of disposable execution debris; retention of durable evidence, required attempts and useful helpers; cleanup records, authority boundaries and governed certification/closeout requirements. Do not remove the required cleanup checkpoint or convert retention into 'keep everything.' Do not invent an extra full QA campaign. Retire only cleanup instructions tied to abandoning the QA branch or moving its work back to the engineering branch. Module QA records belong under agent_docs/ in their QAM structure. Deployment exclusion must be explicitly enforced and verified; the directory name alone is not proof of production exclusion."

**Resolves.**
| ID | Status | Effect |
|---|---|---|
| ND-04 (execution and cleanup generalization) | **RESOLVED** | Execution: the QA Executor executes the approved plan (RUL-01); human checks are declared beforehand and counted (playbook §10). Cleanup: the §14 checkpoint is mandatory for QAM packs; it is a closure operation inside the engagement, not a third QA shot. |
| RRM-07 / QAM-10 (certification vs cleanup sequence) | RESOLVED | The Hub states one sequence for QAM packs, from playbook §14: accepted product verdict (QA Lead) → required cleanup under QA Lead authority with records → durable records committed (Director) → Architect closeout instruction → bounded Engineer closeout → Director merge. Product Gate Q, cleanup acceptance and Gate D remain separate claims. Existing live modules keep their own sequence until amended. |
| QAM-07 (credential and browser lifecycle) | RESOLVED | §12 and §14 hygiene rules are approved source text. |
| SRC-W06 §8 cleanup/harvest-script steps | RETIRED | Only the steps tied to abandoning the QA branch or transferring work back are retired (consistent with RUL-02). |
| DEC-13 (home of QA artifacts) | contributes | QA records live under the project's `agent_docs/` in the module's `QAM/` structure (RUL-04). |
| NEW requirement (not in the harvest) | **ADOPTED** | "Deployment exclusion must be explicitly enforced and verified." The Hub today checks only tsconfig and test-runner exclusion of `agent_docs/**` (RECON_QUESTIONNAIRE Q9.1–Q9.2). Build/deploy exclusion (container, Vercel, Cloud Build ignore rules) and its verification are new doctrine; owning document proposed in the dependency map. |

**Does not decide.** Whether Director password rotation is part of cleanup (playbook §14: "separate… recorded as Director-reported"). Personal-data retention policy (DEC-15) is a different subject and stays OPEN.

## RUL-04 — Frozen contract, writable output lanes (navigation label A.4)

**Ruling (verbatim).** "Requirements and acceptance criteria remain frozen at handoff. Declared lanes inside the module remain writable for engineering handoffs, recon, plans, evidence, findings and approved rulings. Contract changes require an attributable approved amendment. Do not silently rewrite acceptance criteria through test-plan edits."

**Resolves.**
| ID | Status | Effect |
|---|---|---|
| DEC-13 (module freeze model; home of QA artifacts) | **RESOLVED** | Freeze model = frozen contract + declared writable lanes **inside** the module folder (engineering handoff, recon, plans, evidence, findings, approved rulings). QA artifacts live in the module's `QAM/` structure under `agent_docs/` (RUL-03). BIM_PLAYBOOK §6 "Locked Rules" ("nothing inside the folder is added… Architect outputs produced mid-module stage OUTSIDE") must be reconciled to "the frozen inputs are immutable; declared lanes are writable by their owners". |
| WF-04 (assembly and freeze lanes) | RESOLVED | Lanes as above. |
| RRM-02 (freeze the repair contract) | RESOLVED | Amendments are attributable and approved; recorded in the ruling/erratum lane (playbook §4). |
| QAM-03, QAM-10 (lanes, evidence) | RESOLVED | — |
| FC-026, FC-013 (correction package) | UNBLOCKED | Their open decision (DEC-13) is answered; wording still comes from the UPDATE MAP. |

## RUL-05 — Two review / RRM checkpoints (navigation label B.1)

**Ruling (verbatim).** "Reflect Tony's updated workflow: 1. Review after FFM completion and its QA, followed by approved RRM work. 2. Engine 2 review after all Engine 1 implementation phases and QA are closed, followed by approved RRM work. Review findings require disposition. Approved findings determine the bounded RRM work; do not manufacture repair work for a clean review. Each RRM includes QAM. Keep module QA certification distinct from broader review completion and deployed-system verification."

**Resolves.**
| ID | Status | Effect |
|---|---|---|
| ND-02 (which review workflow applies to mainstream work) | **RESOLVED** | Two review checkpoints: (1) after FFM completion and its QA; (2) "Engine 2" review after all "Engine 1" implementation phases and their QA are closed. Each is followed by approved RRM work only where dispositioned findings require it. |
| RRM-01 (RRM as the bounded repair module) | RESOLVED | Adopted: RRM is the mechanism for approved review findings; a clean review produces no RRM. |
| WF-11 (review engines) | RESOLVED in modified form | The three-engine draft (SRC-W11: per-module Engine 1, per-phase Engine 2, whole-application Engine 3) is **superseded by this ruling's two checkpoints**. ~~The "later 10X two-engine direction" that the harvest cited without a source (CL-12) is now sourced: it is this ruling.~~ **R1.1 correction (Jarvis):** this ruling governs current drafting of the review cadence; it does **not** authenticate the harvest's historical "later 10X direction", which remains an unsupplied source (CL-12 MISSING for provenance). "Both PASS" arrows still define no gate. |
| RRM-05 / QAM scope | RESOLVED | "Each RRM includes QAM" (consistent with RUL-01). |
| Gate separation | RESOLVED | Module QA certification (Gate Q) ≠ review completion ≠ deployed-system verification (Gate D). Any phase/application certificate label is still undefined (WF-11). |

**Does not decide.** The Hub definitions of the terms "Engine 1" and "Engine 2" (0 Hub hits; SRC-W11's Engine 2 is per-phase, whereas this ruling's Engine 2 runs once after all phases). Drafting proposal in COMBINED_DECISIONS N-1 for Jarvis to confirm. Reviewer guidance placement (B.2 / RRM-09) stays OPEN. Who performs the reviews (personas in SRC-W11 are not seats) is not ruled.

## RUL-06 — Architect document placement (navigation label C.1)

**Ruling (verbatim).** "Tony delegated placement to Jarvis. Use: 03_BUILD_METHODOLOGY/RRM_PLAYBOOK.md · 03_BUILD_METHODOLOGY/QAM_PLAYBOOK.md · 03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md. Fold older FFM/BIM operating models into their existing owning playbooks rather than create competing normative documents. Plan propagation across all affected existing documents: FFM, BIM, QA, Architect, Engineer, handoff instructions, role tables, module trees, startup instructions, templates, workflow references, MANIFEST and relevant deployment guidance. A new QAM playbook beside contradictory old instructions does not satisfy the requested synchronization."

**Resolves.**
| ID | Status | Effect |
|---|---|---|
| ND-05 (where new documents live) | **RESOLVED** | Three new canonical documents in `03_BUILD_METHODOLOGY/` with the names above. Operating models SRC-W05/W06 fold into FFM_PLAYBOOK / BIM_PLAYBOOK; SRC-W07 content folds into DEPLOYMENT_PLAYBOOK (content and authority still C.2). |
| WF-12 (one owning document) | RESOLVED | No competing normative documents; MANIFEST rows and "Pairs with" follow. |
| RRM-10, QAM-13 (owning playbook) | RESOLVED for the document | Kit/template placement is not decided (DEC-19). |
| WF-08, WF-09 (deployment subjects) | RESOLVED for placement only | The owning document exists by name; the DevOps seat, Cloud Run profile and authority matrix remain C.2. |
| DEC-19 (where skills, worked examples, issue logs live) | **NARROWED** | Document placement decided; template sets (`TEMPLATES/QAM/`), kits and worked examples still need a home. |
| DEC-17 (doctrine tag, landing path, release owner) | unchanged | OPEN. |
| Propagation scope | ADOPTED | The ruling's list is the minimum propagation scope for the UPDATE MAP: FFM, BIM, QA, Architect, Engineer, handoff instructions, role tables, module trees, startup instructions, templates, workflow references, MANIFEST, deployment guidance. The dependency map §4 records the per-document touch surface. |

## RUL-07 — Boundaries preserved (all groups)

Verbatim: "The original five scoped approvals remain unchanged: DEC-01, DEC-02, DEC-03, DEC-04 and DEC-16. Preserve all certified FC identities, fields and totals. Preserve original source files and historical pilot records. QAM applies across module types, including future types. ABM/APBM methodology remains in the separate 10X track; universal QAM packaging does not import that methodology into the main DocSet. Vibe Engineering remains pilot-specific. Do not invent a TRM definition. Do not approve unfinished QAM tooling merely because the playbook is approved."

Consequences recorded in planning:
- Playbook §1 and §16 name ABM, APBM and TRM. In the Hub text the universality sentence stays; the ABM/APBM rows carry no methodology (10X track), and the TRM row states that the Factory DocSet has no TRM definition (0 Hub hits) and must not supply one here. Integration wording for Jarvis to confirm (COMBINED_DECISIONS N-4, N-6).
- QAM-13's validators, exporters, state dispatchers, browser adapters and skills remain unapproved tool deliverables.
- Pilot records (RRM-004 pack, journals, PARTIAL SUCCESS verdict) are preserved; nothing is rewritten as if v1.0 existed then (playbook §4).

---

## What this record does not do

- It does not approve the harvest package v0.1 or Correction Package 001 as DocSet Sync cargo; both remain DRAFT until the Director's intake approval statement.
- It does not change any certified FC record, severity, status, family or total.
- It does not edit canonical doctrine, MANIFEST, CHANGELOG, skills, lints or CI, and does not authorize an `_INBOX/` drop, a sync run or any Git action.
- It does not certify the QAM playbook's tooling or templates. R1.1: an Engineer-drafted template set now exists in `../INTAKE_ADDENDUM_001_v0_2/TEMPLATES/QAM/`, labeled NEWLY AUTHORED DRAFT — QA LEAD REVIEW REQUIRED; this record does not approve it (INTAKE_CLARIFICATIONS CL-20, CL-26).

*RULING RECORD — for Architect (Jarvis) review. Companion to Planning 001 R1 (R1.1 correction notes applied; ruling text unchanged).*
