# BIM PLAYBOOK
## Backend Integration Modules — Authoring, Execution, and Closure

> **Version:** 1.1 · **Date:** 2026-10-16 · **Status:** Active
> **Tier:** 3 — Build Methodology
> **Governed by:** `SOFTWARE_FACTORY_PLAYBOOK.md` › Module Identity & QA Handoff · **Pairs with:** `FFM_PLAYBOOK.md`, `BUG_FIX_PLAYBOOK.md`, `FEAT_PLAYBOOK.md`, `QA_PLAYBOOK.md`, `TESTING_PLAYBOOK.md`, `ENGINEER_PLAYBOOK.md`, `ARCHITECT_PLAYBOOK.md`, `RECON_QUESTIONNAIRE.md`
> **Owner:** Stark Industries App Factory
> **Provenance:** Distilled from the ADK Harness pilot campaign (2026-07): BIM-000 → BIM-005, six modules executed end-to-end with independent QA. Every rule below was paid for in the field; citations reference that campaign as LEGACY IDs (see §3).

---

## 1. What a BIM Is

A **Backend Integration Module** is a self-contained unit of work that connects, replaces, or extends the *backend reality* behind an existing frontend seam — without breaking the promises that seam already makes.

The FFM's success metric is: *"when the operator swaps the service layer to a real backend, no component changes."*
The BIM's success metric is: **that swap, executed, with the promise kept.**

BIMs cover: mock→live service swaps, middleware replacement, native protocol ports, config-driven architecture (manifests), database-backed features (index tables, RLS), storage integrations, and cross-service wiring. A BIM may include UI surfaces when the integration demands them (the module brief declares it) — module *type* follows the nature of the work, not whether pixels are involved.

**BIM vs FFM vs FIX vs FEAT:** FFM builds frontend against mocks before a backend exists. BIM makes backends real behind existing seams. FIX repairs confirmed defects (see `BUG_FIX_PLAYBOOK.md`). FEAT adds user-facing capability to a working system (see `FEAT_PLAYBOOK.md`). When in doubt: if the center of gravity is a seam or a contract, it's a BIM.

## 2. Roles (the chain of custody)

| Role | Duty in a BIM |
|---|---|
| **Coordinator (Operator)** | Approves scope, **holds final adjudication and release authority over QA findings**, rules flagged conflicts, launches the Engineer, executes ALL git and ALL cloud actions, runs manual gates, merges, owns the release decision |
| **Architect** | Authors the module from recon evidence, QAs the Engineer's plan, issues binding pre-execution verdicts (GO/AMEND/BLOCK on module readiness), **advises on architectural classification and routing of QA findings — advisory, not adjudicative** |
| **Engineer** | Plans, builds within release, self-verifies, fills factual acceptance/handoff records; may inspect Git read-only; all Git mutations remain Director-only and BIM cloud-zero remains in force |
| **QA Lead (independent seat)** | Owns standing QA requirements, approves the independent plan, adjudicates findings and certifies the governed candidate per `QA_PLAYBOOK.md` and `QAM_PLAYBOOK.md` |
| **QA Executor (independent seat)** | Performs Q1 recon and plan drafting, then approved Q2 execution and authorized retest; records evidence and never repairs product or self-certifies |

One person may hold multiple seats; the *responsibilities* never merge. The Engineer never grades his own paper.

## 3. Module Identity (Factory-level doctrine — see `SOFTWARE_FACTORY_PLAYBOOK.md` › Module Identity & QA Handoff)

Module identity and the QA-handoff contract are **Factory-wide rules that live above this playbook** (delivered as the Factory Module Doctrine addendum; BIM, FIX, and FEAT all inherit from there — never from each other). Restated here for convenience:

**Canonical ID format: `<TYPE>-<NNN>-<APP-SLUG>`** — e.g., `BIM-006-ADK-HARNESS`, `FIX-004-CYBER-PHARMA`.

- Slugs come from the application's **canonical identity in its project brief/APP_BRIEF**. *(A central `APP_REGISTRY.md` is a proposed future doctrine addition, pending separate Operator approval — until it exists, no document may cite it as a source of truth.)*
- The ID appears on: the module folder name, every document header inside it, the `ACCEPTANCE_SPEC.md`, QA references, retrospectives, changelog entries, and cross-document links.
- **Casing:** canonical ID is UPPERCASE in documents and folder names; git branches use lowercase-kebab (`bim-006-adk-harness`); commit tags use the canonical ID.
- **Why (state it, don't assume it):** module artifacts escape their folders — into QA reports, branches, search results, handoffs. A naked `FIX-002` is ambiguous the day a second app mints one. The suffix preserves provenance wherever the artifact travels.
- **Legacy:** pre-doctrine modules (e.g., the pilot campaign's `BIM-004`) keep their names as LEGACY IDs; no retroactive mass-renaming. When citing them in new documents, append the app parenthetically: "BIM-004 (ADK-HARNESS, legacy)."

## 4. The Module Package (one folder, self-contained)

```
<TYPE>-<NNN>-<APP-SLUG>/
├── CLAUDE.md                    ← THE MANAGER — always read first (see §5)
├── MODULE_BRIEF.md              ← scope lock, gates, forbidden zones (larger modules)
├── DATA_CONTRACT_AMENDMENT.md   ← only when wire contracts change
├── ACCEPTANCE_SPEC.md           ← Engineer-finalized at handoff; criteria seeded from approved contract (see §8)
├── RETROSPECTIVE.md             ← Engineer-authored at close
├── AGENTS.md                   ← same parent routing as CLAUDE.md
├── QAM/                        ← mandatory module-specific QA package, including matching entry routes
└── (declared writable output lanes: engineering handoff, recon, plans, evidence, findings, rulings)
```

Small modules may fold brief and contract into the manager, but matching entry routes, acceptance spec, prepared module QAM and retrospective remain mandatory. Delivery is one module ZIP plus a file tree; Coordinator notes remain outside it.

## 5. The Manager File (CLAUDE.md) — one module, one manager

Every module folder carries one manager body and matching `CLAUDE.md` / `AGENTS.md` entry routing. Engineering routes to the implementation assignment; QA routes into `QAM/`, whose two entries assign QA Executor and point to `QAM_ENTRY.md`. Redirects may share one instruction body. Required manager contents:

1. **Status line** — FINAL stamp date + launch condition (e.g., "only after BIM-005 merges")
2. **Mission** — one sentence
3. **Verified ground** — facts from recon/prior closures the Engineer may build on WITHOUT re-verification (each with provenance)
4. **Rulings table** — decisions already made by Architect/Coordinator, numbered, with "flag disagreement, don't silently deviate"
5. **TO VERIFY FIRST** — the facts the Engineer's plan must open with, each demanding file:line evidence (the informed-state bridge for anything recon didn't pin)
6. **Scope** — in, and OUT said loud
7. **Forbidden zones** — hard stops, path-level
8. **Numbered hard gates** — measurable, each with its verification method (unit / manual / Coordinator ceremony)
9. **Launch procedure** — Plan Mode contents demanded of the Engineer's ONE plan message
10. **Definition of done** — gates + spec + retrospective + protocol docs + STOP
11. **The Operator launch line** — the single sentence the Coordinator types
12. When a module CLOSES, its manager flips from GO to CLOSED status — a tombstone with a map (status, deliverables, where everything went) so no future session mistakes history for orders.

## 6. Lifecycle (the stage-gate chain)

```text
Current recon → Architect authors the module just in time, including ACCEPTANCE_SPEC and prepared QAM.
Director approves scope and the Engineer plan → Engineer builds and runs baseline/regression checks.
Requirements and acceptance criteria freeze; declared records/evidence lanes remain writable (RUL-04).
Engineer completes factual handoff → Director commits/pushes the numbered product candidate.
Director creates qa/<module-branch> at that exact engineering candidate commit.
QA Executor Q1: preflight, independent recon and test plan → QA Lead plan approval → Director release.
QA Executor Q2 executes independently on that QA branch.
If needed: QA Lead dispositions → Architect/Director authorize repair → Engineer repairs on the same QA branch.
Director commits repair candidate → QA Executor re-pins and independently retests with regression checks.
QA Lead certifies the product verdict → authorized required cleanup → QA Lead cleanup acceptance.
Architect closeout instructions → bounded Engineer closeout → Director final commits, merge and push.
Authorized deployment, if in scope → independent deployed-revision Gate D → production confirmation as applicable.
No deployment in scope → record Gate D N/A with reason; no deployment merely to satisfy a template.
Module close/retrospective: deployment-requiring work closes only after its required Gate D.
Engine 1 continues through all scoped phases/modules and their QA; author later BIMs just in time.
Review checkpoint 2: Engine 2 independent system review only after all Engine 1 phases/modules and QA are closed.
Findings require disposition; create RRM only for approved findings requiring repairs; clean review requires no RRM.
```

The distinct post-FFM checkpoint is review after FFM build and its independent QA finish. Both review checkpoints follow `RRM_PLAYBOOK.md` §2 and the vocabulary in `SOFTWARE_FACTORY_PLAYBOOK.md` §2. Review completion, module QA, cleanup acceptance, Gate D and release remain distinct.

### The Locked Rules (Lesson L1 — paid for in the field)

1. **Just-in-time authoring.** Implementation-grade module docs are authored only after (a) the previous module's retrospective exists and (b) a fresh recon of the current repo state is in hand. Before that, a phase holds only a **Phase Seed Brief** (mission, why, dependencies, likely scope, open questions), explicitly non-executable.
2. **Contracts freeze at handoff.** Requirements and acceptance criteria remain immutable except through an attributable approved amendment. Declared lanes inside the module remain writable by their assigned owners for engineering handoff, recon, plans, evidence, findings and rulings. QA records live in the module’s `QAM/` under `agent_docs/`. A test-plan edit cannot amend acceptance criteria.
3. **DRAFT until stamped.** Docs coexisting with a not-yet-run recon carry DRAFT — CLAIM STATUS until the post-recon verdict stamps them FINAL. After the stamp, requirements and acceptance criteria are frozen; changes require an attributable approved amendment. Declared engineering handoff and QA evidence lanes remain writable by their assigned owners.
4. **Placeholders from the first keystroke.** Real URLs, credentials, and infrastructure values NEVER enter documents — even as examples. Structural placeholders only; real values live in local env files, supplied by the Coordinator in-session.
5. **Lessons live at repo level** (`agent_docs/LESSONS/`, timestamped, one lesson per file, append-never-edit) — modules end; lessons compound.

Revised workflow references: [FFM creation](_workflows/FFM_CREATION.md), [FFM execution and post-FFM review](_workflows/FFM_EXECUTION.md), [deployment and Gate D](_workflows/FFM_DEPLOYMENT.md), and [BIM through Engine 2](_workflows/BIM_WORKFLOW.md). Each includes a revised stick diagram and links its superseded original as history. The source diagrams are not current instructions.

## 7. Standing Engineer Doctrine (bake into every manager)

- **Git/cloud authority:** read-only Git inspection is allowed; the Director performs all Git mutations. The BIM Engineer does not deploy and supplies exact file lists and suggested commit messages.
- **Do not silently deviate:** a change outside the authorized writable surface, including diagnostic, test-runner or build configuration changes, requires explicit authorization before execution. Report the proposed change and its evidence; later ratification is not prior authorization.
- **Baseline-first regression:** full suite before the first change (entering red? repair-or-report before proceeding — a red baseline is a finding, possibly a prior module's defect), full board after the last. Pre-existing failures are proven pre-existing, never silently repaired or suppressed.
- **Failure policy is declared per module contract — degrade is not a universal law.** Degrade-with-console-error-and-safe-fallback applies only where the module contract explicitly declares that losing the dependency is safe (e.g., a convenience index, a receipt). Security, audit, financial, tenant-isolation, and data-integrity-critical dependencies may require **fail-closed** behavior — the contract says which, per dependency, before the Engineer builds.
- **Stop means stop.** Momentum after a stage gate is the enemy; the next stage begins only on the Coordinator's plain words.

## 8. ACCEPTANCE_SPEC.md (mandatory handoff artifact — Factory-level rule, restated)

**The contract handed from Engineering to QA. It is NOT the QA test plan.** Engineering states what it claims complete; QA independently decides how to attack and verify. Exact filename locked: `ACCEPTANCE_SPEC.md`.

**Ownership (precise):** the acceptance criteria are **seeded from the approved module contract — Architect/Operator-defined — before implementation.** The Engineer *maintains and finalizes* the spec at handoff, keeping it synchronized with approved scope, but **may not silently add, remove, weaken, or redefine an acceptance requirement** — any scope change requires approval. The Engineer packages the contract for QA; he does not grade his own paper, and he does not write his own exam either.

Minimum contents:

- Canonical module ID + owning application (slug)
- Module objective; in-scope behavior; explicit out-of-scope / forbidden behavior
- **Numbered acceptance requirements `AC1, AC2, …`** — testable and observable ("works correctly" and "handles sessions" are banned phrasings). *(Doctrine note: `AC*` is a NEW Factory decision effective with this playbook — the pilot campaign's field record used gate IDs (`X1–X7`, `V*`, `N*`, `P-G*`), which remain the convention for module-internal engineering gates and stay untouched as legacy. Acceptance requirements and gates are related but distinct: a mapping table gates↔ACs in the spec is encouraged. `QA_PLAYBOOK.md` examples to be synchronized at promotion. Never bare `A*` — reserved for recon assumption checklists.)*
- Expected observable behavior per requirement; error/failure behavior where relevant
- **Environment/setup prerequisites** — migrations, env changes, credentials, permissions, and every manual Coordinator step, called out FIRST (field lesson: a merge whose setup steps live only in a spec nobody opened produces three "broken" features that are actually three locked doors)
- Regression expectations — existing behavior that must remain intact
- Manual-only acceptance points where automation cannot prove the claim
- Known limitations; known follow-up work that does NOT belong to this contract

Timing: the acceptance contract is established at planning, kept synchronized with approved scope during implementation, **finalized at handoff** — never reverse-engineered afterward to justify what got built.

## 9. QA Engagement (the Red Team seat)

Every newly authored module includes a complete, module-specific `QAM/` prepared by the Architect from `03_BUILD_METHODOLOGY/_templates/QAM/`. QA Lead owns the reusable playbook and standing requirements. Engineer fills factual engineering records and handoff; QA Executor performs independent Q1 recon and test planning; QA Lead approves the plan; Director releases execution; QA Executor performs Q2 and authorized retest; QA Lead adjudicates and certifies. `QAM_PLAYBOOK.md` owns this packaging and sequence. Existing modules already in flight retain their recorded sequence until an attributable amendment.

The Director commits and pushes the completed engineering candidate on the numbered product branch, then creates `qa/<module-branch>` at that exact commit. Engineer performs approved repairs and QA Executor independently tests on that same QA branch, with separate writable lanes and one active writer during repair or measurement. The QA branch continues to final integration; do not transfer work back or abandon it as the normal workflow. After the QA Lead’s verdict and required cleanup, the Architect issues closeout instructions, Engineer performs bounded closeout, and the Director performs final commits, merge and push. Preserve product, execution, evidence and closeout identities separately.

Required cleanup removes only authorized disposable execution debris, temporary credentials/authentication state, and owned QA processes or browser contexts. Retain durable evidence, required failed attempts and justified helpers. QA Lead governs retention and cleanup acceptance; certification, Architect closeout and Director release remain separate responsibilities. Record command, working directory, exit code and unfiltered safe output, with sensitive data excluded at collection. Prove product, tests, configuration and contract identity unchanged by cleanup. Module QA records live under `agent_docs/` in their module `QAM/`; verify production exclusion under `DEPLOYMENT_PLAYBOOK.md`.

- QA receives the spec and authors its own attack: `QA_PLAN.md`, manual sequences, exploratory probes, state-transition and negative-path testing. The most valuable field finding of the pilot campaign came from deliberately breaking state, not from following the happy path.
- QA findings carry a **QA-owned verdict**; the **Operator holds final adjudication and release authority** when a product/scope/risk decision is required; the **Architect advises** where architectural classification or routing is needed. An in-scope acceptance failure does not need anyone's permission to be a FAIL. Accepted work routes to Engineering only as approved module content — rejected findings never land on the Engineer's desk.
- QA independently tests the declared engineering candidate after handoff. Requirements and acceptance criteria remain frozen; QA recon, plans, evidence, findings and rulings remain writable in their declared lanes. QA cannot amend acceptance by changing a test plan.
- Evidence bar is symmetric: QA claims cite file:line, payloads, or reproducible steps; findings without evidence are returned unread.
- Verdict vocabulary — exactly the Factory QA set, no local dialects: **PASS / PASS WITH FOLLOW-UP FINDINGS / PASS WITH KNOWN RISK / FAIL / BLOCKED.** Findings are severity-classified, each explicitly marked blocking-or-not for the module under test.

## 10. Contracts & Seams

- Route-handler/API **external contracts freeze** across module boundaries; only internals are ported (field proof: a middleware was replaced under an unchanged seam with zero frontend diff — the entire point of designing the seam one module earlier).
- Contract changes ship as **numbered amendments** (A1, A2 …) that supersede specific sections and inherit the rest, keeping history honest.
- When replacing a system, **the old system is the oracle for its replacement**: equivalence gates + fixture batteries encode its observable behavior; the old system stays deployed and untouched until a Coordinator retirement ceremony AFTER all gates pass.
- Kill switches are designed in: env-flag fallbacks (mock mode), git-revert paths, and the not-yet-retired predecessor. A kill switch that has never been flipped is a prayer — test the flip as a gate.

## 11. Anti-Patterns (block these)

- **Pre-authoring against assumptions** — implementation docs written before recon (L1's origin: two defects authored into a module six days before evidence existed)
- **Mid-mandate contract mutation** — changing frozen requirements or acceptance criteria without an attributable approved amendment; declared owner-specific output lanes remain writable
- **Scope smuggling** — "while I'm here" fixes, passengers on risky modules; one variable per experiment
- **The Engineer grading his own paper** — acceptance spec drifting into a QA plan, or QA skipped because the board is green
- **Momentum through a stage gate** — starting the next stage in the same session/on the same nod
- **Real values as examples** — a URL in a doc's example row is a URL in git history forever
- **Naked module IDs in new work** — provenance is doctrine now
- **Happy-path-only QA** — if nobody deliberately stressed the product, it wasn't QA

## 12. Definition of Done (module level)

- [ ] All numbered gates green (unit + manual + ceremony as declared)
- [ ] Green board: build + typecheck + full suite, baseline and final
- [ ] `ACCEPTANCE_SPEC.md` finalized and handed to QA
- [ ] Coordinator commits landed per concern; QA-environment / Coordinator setup prerequisites required by `ACCEPTANCE_SPEC.md` executed and verified (genuinely deploy-dependent steps identified separately under Gate D)
- [ ] Independent QA engaged — Gate Q is mandatory for all code-bearing modules; only documentation-only / non-runtime changes may receive a recorded Operator QA waiver
- [ ] Gate D verified for deploy-requiring modules (or recorded N/A with reason)
- [ ] Findings adjudicated and routed
- [ ] `RETROSPECTIVE.md` written — what fought back, not just what worked; lesson candidates flagged for `LESSONS/`
- [ ] Manager flipped to CLOSED with deliverables map
- [ ] Changelog + session log per repo protocol

## 13. Worked Example (LEGACY: the ADK-HARNESS pilot arc)

BIM-000 (recon & baseline; the closed-module-with-delivered-artifact pattern) → BIM-001 (mock→live behind a route-handler seam; sentinel conflict flagged-not-resolved, ruled D1(b)) → BIM-002 (middleware ported to native protocol; wrapper as oracle; retirement ceremony) → BIM-003 (agent manifest; env-var *names* in committed config, never URLs; the four-line test) → BIM-004 (index table + RLS; "the index is not the transcript"; degrade-not-block) → BIM-005 (GCS write integration; backup-before-write law; server-side path derivation as injection fence). Full artifacts in the pilot repo's `agent_docs/`; QA acceptance reports for BIM-002 and FIX-002 (ADK-HARNESS, legacy) are the reference QA engagements.

## 14. Version History

| Version | Date | Change |
|---|---|---|
| 1.0-DRAFT | 2026-08-10 | Initial draft from the six-module ADK Harness pilot campaign + two doctrine upgrades (ACCEPTANCE_SPEC; app-suffixed IDs). |
| 1.0-DRAFT-R2 | 2026-08-10 | QA review AMEND pass applied (10 findings + polish): QA verdict ownership restored (Operator final authority, Architect advisory); Factory QA verdict vocabulary; spec ownership tightened (seeded pre-implementation, Engineer finalizes without redefining); shared identity/handoff doctrine promoted above BIM to SOFTWARE_FACTORY_PLAYBOOK addendum; APP_REGISTRY demoted to proposed; AC* declared a NEW decision with X*/gate-ID legacy mapping; per-module failure policy replaces universal degrade; lifecycle sequencing fixed (QA before merge); QA waiver restricted to non-runtime changes. |
| 1.0 ACTIVE | 2026-08-10 | Finalization pass (F1 registry refs removed, F2 Gate-D/CLOSE sequencing, F3 setup-prerequisites wording, F5 tree label). Promoted from: ADK Harness field campaign → independent QA engagements → R1 QA review → R2 amendment pass → final consistency pass. |
| 1.1 | 2026-10-16 | Factory DocSet sync: approved workflow/security/reference corrections; preserved original; explicit exclusions per doctrine-part2 map. IDs: FC-012, FC-014, MC-06, MC-07, RUL-01, RUL-02, RUL-03, RUL-04, RUL-05, RUL-07, RUL-12, RUL-15, W02, W03, W04, W05, W06, W07, W23 |
