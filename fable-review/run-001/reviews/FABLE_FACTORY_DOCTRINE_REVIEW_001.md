# FABLE FACTORY DOCTRINE REVIEW — RUN 001

**Reviewer:** Claude Fable 5.1 (independent examiner seat)
**Baseline:** `app-factory-docs-v1` @ `0a787cb826118b4a010765d60e41a449df3ce746`, branch `factory-docs-review-fable-001`
**Started:** 2026-09-13 04:57 UTC
**Completed:** 2026-09-13 05:24 UTC
**Status:** COMPLETE — all fifteen sections present. Defects: 31 (2 BLOCKER, 5 HIGH, 15 MEDIUM, 9 LOW). Suggestions: 14.
**Independence:** no Astra material and no prior model review of this corpus was opened (see Coverage Manifest, §13).

---

## 1. EXECUTIVE ASSESSMENT

The Factory is a coherent, field-hardened operating system with real controls: recon before authoring, kit consumption over wrapping, an independent QA seat with a shared evidence discipline, module doctrine with frozen folders and acceptance contracts, and a design tier that is genuinely token-driven. The Hub's own governance mechanics (canonical names, header blocks, a dependency map, archive-on-bump, lints, and a conductor skill with logged runs) are better than most engineering organizations have. For someone who already knows the history, the operating model is executable.

**Overall health: 3 of 5 — functional, with meaningful gaps.** Major corrective work is warranted, but it is targeted work on a sound spine, not a rewrite.

**The most serious weaknesses, in order:**

1. **Two BLOCKER-class content defects.** Forbidden authorization patterns survive in four live docs, including the auth authority itself: an app-side superadmin-creation route, role reads from `user_metadata`, a role column on a mirror table, and client-side route gating. The payments manual's PaymentIntent sample says "recalculate on the server, never trust the client" and then computes the charge from client-supplied unit prices and discount.
2. **The drift-killing lint suite fails at the baseline.** Nine known stragglers have been red since at least 2026-08-10, and the standing practice is to merge over red CI. The watchdog exists but is not gating.
3. **The constitution predates the module era.** The Blueprint has no QA seat, no routing for BIM/FIX/FEAT modules, and a lifecycle that ends at "Ship it." Three APP_BRIEF templates and three UI_SPEC templates coexist while one document claims to be the single source. Seat and lifecycle vocabularies drift: "Architect" names both the human and an AI agent.
4. **Distribution is undefined.** No release tag has ever been cut, the Hub-to-project sync design is a DRAFT in `_OTHERS`, and four different project-side landing paths for Hub docs appear across live docs.
5. **Load-bearing artifacts live outside the Hub with no locator:** the recon, extraction, and frontend-first skills; every canonical worked example; the `FILE_TREE.md` the constitution requires.

**Strongest characteristics:** the recon-first, filesystem-wins doctrine is propagated consistently across seven docs; the QA, Bug-Fix, and BIM trio is the best-written doctrine in the corpus; the design-system tier is tight and cross-consistent; the testing playbook is unusually honest field doctrine; and the four-step update dance is proven by its own run logs.

**Is the Factory operationally coherent?** Yes at the module-doctrine level. No at the constitution level, where the founding documents have not caught up with what the Factory actually does.

**Is major corrective work warranted?** Yes. The ten actions in §2 resolve most of it, and none requires restructuring the repository.

## 2. TOP 10 — IF ONLY TEN THINGS GET FIXED

| # | Action | Resolves |
|---|---|---|
| 1 | Purge every forbidden authorization pattern from live samples: delete or mark LEGACY the `is_qr_*` superadmin routes, HOC, mirror-table role column, and metadata-driven summary in AUTH_MANUAL; rewrite SOFTWARE_FACTORY_PLAYBOOK Phase 7 to consume the kit; fix APP_ARCHITECTURE §2/§4/§10 and STATE_MANAGEMENT §1/§8. Rule on the `httpOnly` cookie flag against disk. | FBL-D001, FBL-D030 |
| 2 | Fix the ECOMMERCE PaymentIntent sample so the server prices line items from the catalog and validates the coupon itself, and returns a generic error, not Stripe's message. | FBL-D019 |
| 3 | Clear the nine lint stragglers (STARTER_KIT_HANDBOOK redo, two DATABASE prose refs, one UI_UX filename ref) and then end the merge-over-red practice, so CI is a real gate. | FBL-D002, FBL-D003 |
| 4 | Ratify one APP_BRIEF template and one UI_SPEC template (or one per pipeline, explicitly), and settle greenfield UI_SPEC authorship. Fix the Blueprint and ARCHITECT_PLAYBOOK to match the majority position. | FBL-D004, FBL-D005 |
| 5 | Bring the constitution to the module era: add the QA seat and Coordinator vocabulary, route BIM/FIX/FEAT in the pipeline router, and put Gate Q and Gate D into the lifecycle. | FBL-D020 |
| 6 | Publish one seat glossary and one lifecycle map covering Blueprint phases, SFP phases, FFM sub-phases, build stages, and roadmap phases; state which seat "Architect," "Engineer," and "Operator" name in each context. | FBL-D007, FBL-D008, FBL-D014 |
| 7 | Cut the first doctrine tag, promote the sync loop from DOCTRINE_HUB_DESIGN into live doctrine, and standardize one project-side landing path for Hub docs. | FBL-D010 |
| 8 | Make the design-tier examples obey Rule Zero and Rule Zero-B: fix the `hidden md:block` sidebar layouts in UI_UX and APP_ARCHITECTURE, state one rail breakpoint rule, and mark numbered-color kit conventions as migration debt. | FBL-D021, FBL-D023 |
| 9 | Author a deployment and DevOps doctrine (environments, promotion, revision recording, rollback) and a git/cloud authority matrix by context (FFM run, module run, Hub doctrine run). | FBL-D016, FBL-D017 |
| 10 | Locate the off-Hub artifacts: an examples index with repo, path, and tag; skill homes; the Engineer completion package; and a decision on `FILE_TREE.md`. | FBL-D006, FBL-D011, FBL-D015 |

## 3. RECONSTRUCTED FACTORY OPERATING MODEL

This is the model the corpus actually defines at the baseline, reconstructed from source. Items the corpus leaves materially unclear are marked **AMBIGUOUS** (multiple readings supported) or **UNKNOWN** (no reading supported).

**Purpose.** A "disciplined factory" in which humans define architecture and acceptance criteria, AI agents execute within guardrails, and manuals carry institutional knowledge (SOFTWARE_FACTORY_PLAYBOOK §1). Products are Next.js/Supabase apps built on the Stark starter kit (the "Kit Track") or Python CLI pipelines (the "Pipeline Track") (ENGINEER_PLAYBOOK Parts II–III).

**Lifecycle.** The canonical project lifecycle is APP_FACTORY_BLUEPRINT Phases 0–5: Recon → Ignition (APP_BRIEF) → Design → Engineering (specs) → Fabrication (code) → Deployment. SOFTWARE_FACTORY_PLAYBOOK's nine build phases nest inside it (§2 mapping table). FFM sub-phases 0–6 nest inside build phases. FRONTEND_BUILD_PHASE_PLAYBOOK adds six execution stages plus a Stage 0 Discovery. Project roadmaps add their own "Phase N" numbering (FFM §6). Module-era work (BIM, FIX, FEAT) follows a separate stage-gate chain (BIM §6) that the Blueprint does not reference. **AMBIGUOUS:** how module runs relate to Blueprint phases after Phase 4.

**Project routing.** Two pipelines: CONVERSION (source app exists; Brain Drain → 4-file handoff package → Engineer; no Designer) and GREENFIELD (Architect → Designer → Engineer; token file is the primary design deliverable) (Blueprint router; FFM §4 is the detailed source). Hybrids are treated as greenfield. Module types (BIM, FIX, FEAT) are routed by "center of gravity" (BIM §1, FEAT §1) but not by the constitution's router.

**Human authority.** One human, named variously Tony Stark, Commander/Final Approver, Operator, Coordinator, "the human," and "stakeholders." Holds: approval of APP_BRIEF, canonical-screen lock, screen set, specs, and packages; scope and route decisions; all git and cloud actions in module runs; the merge in Hub doctrine runs; final adjudication of QA findings and release authority (SFP §2.5, BIM §2, QA §4). Never written to by AI: `main` (skill D6, RECOVERY standing rules).

**AI authority.** The Architect issues binding pre-execution verdicts on module readiness (GO/AMEND/BLOCK) and advises on QA findings (BIM §2). The QA Lead owns the verdict (PASS / PASS WITH FOLLOW-UP FINDINGS / PASS WITH KNOWN RISK / FAIL / BLOCKED). The Engineer builds after Plan-Mode approval and never self-certifies. Doctrine may be overridden by the Operator only with explicit acknowledgment (SKILLS_PLAYBOOK §10; skill CLAUDE.md §6).

**Architect seat.** An AI in a chat session ("Jarvis"; FFM Role 3; skill CLAUDE.md §1). Runs recon-gated ignition, produces APP_BRIEF, authors the whole FFM folder, pre-authors DATA_CONTRACT in conversion runs, drafts UI_SPEC in greenfield runs (majority position), authors module packages from recon evidence, plan-QAs the Engineer. **AMBIGUOUS:** SOFTWARE_FACTORY_PLAYBOOK §1 and the Karpathy Protocol call the human "the architect."

**Designer seat.** An AI agent (DESIGNER_PLAYBOOK). Greenfield only. Produces the token file (primary), style tile, per-screen HTML+PNG via the Canonical Page Method, revises UI_SPEC, and ships a component manifest. Gates: token lock, canonical-screen lock, screen-set approval (human).

**Engineer seat.** Claude Code ("Claudy") in the target repo. Phase 0 recon executor; FFM executor; module builder under Plan Mode; authors DATA_CONTRACT in greenfield runs; git-zero and cloud-zero in module runs; runs all git in Hub doctrine runs; deploys to staging in FFM runs. **AMBIGUOUS:** the Blueprint describes an Engineer who "prompts Claudy," implying a separate spec-authoring agent.

**QA seat.** An independent "QA Lead" seat (QA_PLAYBOOK §4; BIM §2). Receives the Engineer's claim package and ACCEPTANCE_SPEC, authors its own attack, issues Gate Q and Gate D verdicts, classifies findings, protects scope. Present only in module-era doctrine. **UNKNOWN:** who or what holds the seat (human, a separate AI session, or the same agent under separation rules); the Blueprint has no QA seat.

**DevOps / deployment seat.** Named "DevOps / Deployment Operator" (QA §4, BUG_FIX §3), "Operations / SRE" (ENGINEER §1/§17), or simply "(You)" (Blueprint Phase 5). Duties listed (deploy approved revision, record identity, maintain rollback). **UNKNOWN:** who holds it and how deployment is performed; the only procedural deployment content is STRIPE_SUBSCRIPTIONS §13.

**BIM flow.** Fresh recon → Architect authors module FINAL → Coordinator approves scope → Engineer Plan Mode (one message; folder freezes) → Architect plan-QA → build → green board baseline/final → ACCEPTANCE_SPEC finalized → Coordinator commits per concern → setup steps → Gate Q → adjudication → merge/deploy → Gate D → CLOSE → RETROSPECTIVE and lessons (BIM §6). Failure policy is declared per module; fail-closed where security or integrity demands (BIM §7).

**FFM flow.** Architect authors a portable module folder (`_project/` four files, `_design/`, `_extraction/`, skill, playbook, verification) after recon; Operator fills evidence folders and boots Claudy with a fixed activation contract; Claudy runs sub-phases 0–6 with operator gates, Gate M for any UI shell, retrospective at close (FFM §2–§13, §22).

**FEAT and FIX flows.** FEAT inherits BIM mechanics by reference and adds launch conditions, v1-now/v2-seeded, scope discipline, mode parity, accessibility gates (FEAT §3–§5). FIX follows a 13-stage lifecycle: intake → triage → reproduce → recon → mechanism → plan → implement → regression protection → full suite → Gate Q → deploy → Gate D → promotion → closure (BUG_FIX §4), executed as a module folder (§16).

**Testing flow.** Four layers (unit, integration, E2E, manual smoke), `retries: 0`, environment-drift-first diagnostics, defensive error assertions, companion artifacts (TESTING_PLAYBOOK). Kit Track proof is `npm run build` + `jest` + `tsc --noEmit`; Pipeline Track proof is `pytest` in a clean venv (ENGINEER §4).

**Support / bug-fix flow.** As FIX above; defects found by QA route through Operator adjudication and reach the Engineer only as approved module content.

**Evidence model.** Five labels shared across recon, extraction, QA, bug-fix, skills, and the Hub skill: EVIDENCE / INFERENCE / CLAIM / GAP / QUESTION. Engineer reports are claim packages; QA certifies evidence, not effort.

**Handoffs.** Architect→Designer (APP_BRIEF + visual anchor + verbal brief); Designer→Engineer (token file, tile, screens, UI_SPEC, manifest); conversion Architect→Engineer (four-file package + `_design/` + `_extraction/`); Engineer→QA (ACCEPTANCE_SPEC + claim package); Engineer→Operations (ENGINEER §17); lessons→Hub via `_INBOX/` cargo and the `factory-docs-update` skill.

**Approval gates.** APP_BRIEF approval; token lock; canonical-screen lock; screen-set lock; spec approval; four-file package approval; Plan-Mode approval before any write; per-sub-phase and per-stage operator approval; module scope approval; plan approval; Gate 4 push approval in Hub runs.

**Acceptance gates.** Hard gates G1..n per FFM phase; Gate M (mobile shell); numbered module gates (X*, V*, N*, P-G*); AC1..n acceptance requirements; Gate Q (pre-deployment QA); Gate D (deployed-revision verification); production confirmation.

**Deployment / promotion gates.** Gate Q before deploy; Gate D after; "a deploy-requiring module is never CLOSED before its Gate D" (BIM §6). Staging deploy at FFM Stage 6. **UNKNOWN:** promotion procedure between environments.

**Rollback / recovery expectations.** Rollback readiness is a Gate D step (QA §13 D9) and a handoff need (ENGINEER §17); kill switches and the un-retired predecessor are designed in for BIMs (BIM §10). Session recovery via `RECOVERY.md` and session files (root CLAUDE.md; ENGINEER §16). Hub-run recovery via the skill's D15a. **UNKNOWN:** an actual rollback procedure for any deployment target.

**Source-of-truth rules.** Disk wins over docs (everywhere). QA order: accepted spec > running system > contracts > recon > env config > engineer report > prior docs > recollection (QA §5). FFM module: DATA_CONTRACT wins on data, UI_SPEC on UI, `_project/CLAUDE.md` on scope, root CLAUDE.md on structure (FFM C.1). Design: doctrine doc beats DESIGNER_PLAYBOOK (§13); Rule Zero and Rule Zero-B beat other doctrine (UI_UX). Agent conduct: ENGINEER §15 beats any paraphrase. **AMBIGUOUS:** no Factory-wide precedence among tiers or among these local "X wins" claims.

**Branch / promotion ownership.** Hub: agent branches `docs/<topic>-<date>`, one commit per doc, Operator merges by rebase-and-merge, main is PR-only. Projects: module branches lowercase-kebab of the module ID; Coordinator commits per concern and merges. FFM: **AMBIGUOUS** (Engineer deploys to staging; commit ownership unstated).

**Regression expectations.** Every confirmed defect earns regression protection at the cheapest layer; baseline-first full-suite runs; assertions never weakened to restore green; flaky tests are defects; pre-existing failures proven and separated (BUG_FIX §10–§11, QA §19, BIM §7, FEAT §4).

## 4. OVERALL FIVE-DIMENSION SCORECARD

| Dimension | Score | Justification (evidence in §7 and §9) |
|---|---|---|
| Correctness | 3 | The core methodology is sound and field-derived. But the auth authority, the constitution's Phase 7, the architecture manual, and the state manual still show authorization patterns the Factory itself classifies as security smells (D001, D030), and the payments manual's central sample trusts client prices while claiming not to (D019). |
| Consistency | 2 | Three APP_BRIEF templates and three UI_SPEC templates coexist under a single-source claim (D004); seat names and lifecycle names drift across tiers (D007, D008); model docs ship examples that violate their own Rule Zero and Rule Zero-B (D021, D023); git/cloud authority differs by context without a reconciling rule (D016). |
| Completeness | 3 | Gates, evidence, and regression rules are strong. Missing: a QA seat and module routing in the constitution (D020), any deployment or rollback doctrine (D017), the Engineer completion package QA expects (D015), the `FILE_TREE.md` the constitution requires (D006), a global precedence rule (D031). |
| Executability | 3 | Module-era playbooks are executable cold. The Hub has no entry point or reading order; recon, extraction, and frontend-first skills and every worked example live off-Hub with no locator (D011); no release tag exists (D010); "Plan Mode" is defined only in a lint-exempt config file and the skills playbook (D018). |
| Maintainability | 3 | Canonical naming, header blocks, dependency map, archive-on-bump, and the update skill are strong. But the lints are red and treated as advisory (D002), the MANIFEST count is wrong after two runs (D009), duplicated templates and a second Karpathy copy can drift independently, and a 40,000-line corpus is synchronized by hand. |

**Overall: 3 — Functional, but meaningful gaps exist.**

## 5. DOMAIN SCORECARDS

| Domain | Score | Basis |
|---|---|---|
| Factory governance / constitution | 2 | Blueprint lacks QA seat, module routing, and post-fabrication lifecycle; SFP Phase 7 stale; project residue in the constitution (D020, D001). SFP §2.5 is the one modern anchor. |
| Lifecycle / routing | 2 | Five overlapping phase vocabularies with one partial map (D008); module types unrouted (D020). |
| Agent roles / ownership | 2 | "Architect" collision, Operator/Coordinator/Commander drift, Engineer identity ambiguity (D007, D014). |
| Handoffs | 3 | Well-specified Designer→Engineer and Engineer→QA contracts; but the QA claim package has no producer (D015) and the Hub→project handoff is undefined (D010). |
| Application architecture | 3 | Good App Router doctrine; examples contradict Kit Exception, Navbar Law, and Gate M (D001, D021). |
| Database | 4 | DATABASE_MANUAL v1.1 is clean and speaks one role doctrine; two lint-flagged versioned refs (D002). |
| Authentication | 2 | AUTH_MANUAL v1.4's corrected sections are right; §12–§14 and the Summary are not (D001); cookie flag contradicts the kit handbook (D030). |
| Authorization | 2 | Same root as authentication; the forbidden pattern appears in four docs. |
| Security | 3 | Strong QA security checks, defensive error assertions, secret handling; undermined by the samples above and the leaked-error API template (D022). |
| APIs / services | 3 | Service-layer law and Kit Exception are clear; error template leaks upstream messages; duplicate §10 (D022, D029). |
| Commerce / payments | 3 | STRIPE_SUBSCRIPTIONS is excellent (money-truth model, RBAC ⊥ tiers); ECOMMERCE's core sample is wrong on price trust (D019). |
| State management | 3 | Three-layer model and Division of Labor are right; §1 table and §8 auth store contradict them (D001). |
| Frontend engineering | 4 | FRONTEND_FIRST and FRONTEND_BUILD_PHASE are tight, de-duplicated, and pointer-disciplined. |
| Design system | 4 | GDSH, THEME_LIBRARY, TOKEN_FILE, THEMING form a consistent contract; UI_UX examples and rail breakpoint drift hold it back (D021, D023, D024). |
| BIM | 4 | Complete stage-gate chain, freeze rule, failure-policy rule, seams and kill switches. |
| FFM | 4 | The most complete authoring manual in the corpus; lifecycle-vocabulary and worked-example location issues are external to it. |
| FEAT / change mechanics | 4 | Correct inheritance from the Factory level; concise deltas. |
| Testing | 4 | Field-derived principles that generalize; minor env-name drift (D027). |
| QA | 4 | Separation law, claim package, verdict model, Gate Q/D, scope protection; artifact locations unspecified (D015). |
| Bug fixing / support | 4 | Mechanism rule, regression protection, environment parity, FIX anatomy. |
| DevOps / deployment | 2 | Gates exist without a process or owner; only STRIPE §13 has a recipe (D017). |
| Skills / agent instructions | 4 | SKILLS_PLAYBOOK is a strong constitution for skills; the Hub skill is well-built; supporting files drift (D028). |
| Evidence / certification | 4 | Shared five-label discipline; ENCODED records and run logs give provenance. |
| Documentation governance | 3 | Mechanics strong; lints red, count wrong, tags absent (D002, D009, D010). |
| Repository operating rules | 3 | PR-only main, rebase-and-merge, four-step dance are clear; merge-over-red is the weak point (D002). |

## 6. WHAT THE FACTORY IS DOING WELL

1. **Recon before authoring, filesystem wins.** Documented in APP_FACTORY_BLUEPRINT Phase 0, ARCHITECT_PLAYBOOK §2, ENGINEER_PLAYBOOK §2, FFM_PLAYBOOK §7 step 0, HANDOFF_PACKAGE_PLAYBOOK §4, RECON_QUESTIONNAIRE §0, and QA_PLAYBOOK §5. Value: it converts the single most common failure class (authoring against stale docs) into a day-one check with an executable instrument and a report format. Preserve: the mutual pointers, the read-only rule, and the "handbook is aspirational" framing.

2. **The Kit Exception propagated to the root.** API_AND_SERVICES §1, AUTH_MANUAL §0, FRONTEND_FIRST §0, FRONTEND_BUILD_PHASE §1.6, STARTER_KIT_HANDBOOK §13, ENGINEER §14. Value: one field lesson became an antibody at every place the wrong rule used to live. Preserve: the "Should I Author This?" verdict table as the audit's anchor.

3. **An independent QA seat with an evidence discipline.** QA_PLAYBOOK §3–§13, BIM §9, BUG_FIX §3. Value: the Engineer never grades his own paper; verdict vocabulary is fixed; Gate Q and Gate D separate "fit to deploy" from "works where deployed"; scope protection keeps velocity without hiding defects. Preserve: the one-test-at-a-time manual protocol and the final-environment-reset rule.

4. **Module doctrine done with correct inheritance.** SFP §2.5 holds Factory-wide identity and handoff rules; BIM, FIX, and FEAT inherit from the Factory level, never from each other (BIM §3, FEAT §2, BUG_FIX §17). Value: a new module type can be added without re-deriving governance. Preserve: the freeze rule, per-module failure policy, and the app-suffixed ID format.

5. **The design tier is a real contract.** GDSH §2 canonical token set, THEME_LIBRARY as the menu, TOKEN_FILE as reference values with the live file ruled to be `globals.css` (F-025), THEMING's TW3/TW4 fork. Value: "change one file, re-theme everything" is true when the rules are followed. Preserve: the identities-not-statuses role tokens and per-mode contrast tuning.

6. **Testing doctrine that tells the truth.** TESTING_PLAYBOOK Principles 1.3, 1.4, 1.10 and §3.1–§3.8. Value: "tests that pass for the wrong reason are worse than tests that fail," `retries: 0`, shadow-implementation detection, and defensive error assertions are field-earned rules that generalize across backends. Preserve verbatim.

7. **Hub governance mechanics.** Canonical live names, standard header block, MANIFEST dependency map as the "bump tool," `_ARCHIVE` snapshots stamped from headers, CHANGELOG ledger, four lints, and the `factory-docs-update` skill with six phases and four stop gates. Value: PR #10's run logs (`agent_docs/RESPONSES`) show the process working end to end with evidence labels. Preserve: D3 routing gate, D7 dance, D9 lint conduct, D16 cargo triage.

8. **Foundational doctrine at the top, re-injected per stage.** UI_UX Rule Zero placement, FRONTEND_BUILD_PHASE §1.5 doctrine refresh and Gate M as a built-in gate. Value: it addresses doctrine decay in long sessions structurally rather than by exhortation. Preserve.

9. **Lessons-promotion loops.** FFM §19, QA §31, BUG_FIX §14, FRONTEND_BUILD_PHASE §12 (Kit Improvement Proposals), RECON's Lessons Backlog. Value: structural vs project-specific classification is stated everywhere it matters. Preserve.

10. **Portable, vendor-neutral module folders.** FFM §3 anatomy with `CLAUDE.md`/`AGENTS.md`/`GEMINI.md` entry points and a copy-pasteable activation contract. Value: any coding agent can be booted deterministically. Preserve the "no placeholders in the boot prompt" rule.

## 7. RANKED DEFECT FINDINGS

IDs are stable and were assigned in discovery order; ranking is by severity then operational consequence. Every defect cites its evidence; where evidence is limited it says so.

### BLOCKER

**FBL-D001 — Forbidden authorization patterns survive in four live docs, including the auth authority**
- Classification: DEFECT · Severity: BLOCKER
- Files: `04_REFERENCE_MANUALS/AUTH_MANUAL.md`; `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md`; `04_REFERENCE_MANUALS/APP_ARCHITECTURE_MANUAL.md`; `04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md`
- Locations and evidence:
  - AUTH_MANUAL §12 "SuperAdmin User Management": three route samples (`/api/superadmin/add-user`, `delete-user`, `get-users`) authorize on `requester.user_metadata?.is_qr_superadmin !== 1` and create users with `is_qr_superadmin: 1` from the app. AUTH §13 mirror table carries `role TEXT DEFAULT 'member'`. AUTH §14 `withRoleCheck` HOC gates layouts client-side on `roles['is_qr_admin']`. AUTH Summary: "4. Roles stored in user_metadata … metadata-driven." AUTH registration flow shows `is_qr_*` default metadata. Only "Client-Side Auth" and Pattern 4 carry the v1.3 legacy advisory; §12–§14 and the Summary do not.
  - The same manual's own rules: Key Principle 5 and "Where Roles Live": "authorization is NEVER read from [user_metadata]"; STARTER_KIT_HANDBOOK §2: "no app-side superadmin-creation surface — it is a privilege-escalation attack surface"; DATABASE_MANUAL §2: "never mirror a `role` column onto a profile table"; RECON Q3.4 and TESTING §3.8 make "no `user_metadata` authz reads" a grep gate.
  - SOFTWARE_FACTORY_PLAYBOOK §9 (Phase 7): "Role flags defined in user_metadata"; `withRoleCheck(AdminLayout, { allowedRoles: ['is_admin','is_member'] })`; checklist "Login page(s) created," "Auth store configured" — all things STARTER_KIT_HANDBOOK §13 marks DO NOT BUILD.
  - APP_ARCHITECTURE_MANUAL §2 lists `src/services/authServices.ts` in the standard layout (AUTH §0: "THIS FILE SHOULD NOT EXIST"); §4 gates `(admin)/layout.tsx` as a `'use client'` component on `useAuthStore(selectIsAdmin)` (contradicts AUTH "Navbar Law" and kit `protectPage`); §10 middleware reads `user.user_metadata?.role` for admin routes.
  - STATE_MANAGEMENT_MANUAL §1 table: "User auth state | Zustand | Needed globally for route protection"; §8 "Auth Store Pattern" persists `user.role` to localStorage and exports `selectIsAdmin` — the exact stale-snapshot pattern §1's own Division of Labor and AUTH Navbar Law Rule 3 forbid. The v1.1 history row claims the audit "verified the doctrine clean."
- Why this is a defect: the docs MANIFEST calls the "Kit auth authority" and the constitution both teach patterns other live docs classify as security smells and forbidden surfaces. Doctrine contradicts doctrine on a security control.
- Operational consequence: a builder following SFP Phase 7 or copying AUTH §12–§14 ships an app-side privilege-escalation surface and metadata-based authorization, and the Factory's own grep gate then fails the build, or worse, does not run because SFP told the builder it was correct.
- Recommended resolution: delete or move §12–§14 to `_ARCHIVE` history; rewrite the AUTH Summary; add the legacy advisory to every remaining `is_qr_*` sample; rewrite SFP Phase 7 as "consume the kit; verify with AUTH-WALK"; remove `authServices.ts` from APP_ARCHITECTURE §2 and replace §4/§10 with `protectPage`-based samples; fix STATE §1 table and §8 to a non-persisted, non-authoritative store. Add a lint or grep that fails on `user_metadata` authz reads in live doctrine.

**FBL-D019 — The payments manual's central sample trusts client prices while claiming server recalculation**
- Classification: DEFECT · Severity: BLOCKER
- Files: `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md` §3 "Creating PaymentIntent (Server)"; cross-file `03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md` §1.8, §4.3
- Evidence: the route comments "CRITICAL: Recalculate total on server - never trust client," then calls `calculateOrderTotal({ items: body.items, shippingCost: body.shipping.cost, couponDiscount: body.coupon?.discount })` where `body.items[].price`, `body.shipping.cost`, and `body.coupon.discount` all come from the request. The §11 checklist requires "Server-side recalculation of totals (never trust client)" and "Coupon validation on server." The same handler returns `{ error: error.message }` for `StripeError` (status 400) — TESTING §4.3 requires the generic message and asserts that "declined" and card fragments never reach the client.
- Why this is a defect: the sample violates its own stated rule and its own security checklist; a second live doc forbids the error behavior it shows.
- Operational consequence: a build copying the sample lets a client set `price: 1` or `discount: 99900` and charges that amount; Stripe error text can leak card details.
- Recommended resolution: server fetches unit prices from the catalog by `productId`, validates the coupon via `couponServices`, computes shipping from the method id, and ignores client totals; return a generic error and log the Stripe error server-side; add the TESTING §4.3 test to §10.

### HIGH

**FBL-D002 — The doctrine lint suite fails at the baseline and the process merges over red CI**
- Classification: DEFECT · Severity: HIGH
- Files: `lints/*`, `.github/workflows/doctrine-lint.yml`, `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md`, `04_REFERENCE_MANUALS/DATABASE_MANUAL.md`, `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md`, `_SKILLS/factory-docs-update/README.md`, `agent_docs/RESPONSES/response_2026-08-10_200500_gate4-precheck.md`
- Evidence: `py -3 lints/run_all.py` at 0a787cb exits 1: VERSIONED-REFS 8 hits (STARTER_KIT_HANDBOOK lines 258, 261, 688, 690, 692; DATABASE_MANUAL lines 8, 156; UI_UX_BUILDING_MANUAL line 2092) and HEADER-PRESENCE 1 miss (STARTER_KIT_HANDBOOK). The Gate 4 precheck of 2026-08-10 calls these "the identical pre-existing stragglers … Expect the CI ❌ … does not block merge." The skill README states: "red CI from known pre-existing findings does not block your merge." lints/README.md calls VERSIONED-REFS "THE drift-killer."
- Why this is a defect: a control whose red state is expected and merged over cannot distinguish a new drift from the known set without a human diffing lint output by hand. The watchdog is advisory in practice.
- Operational consequence: any new versioned reference or missing header lands under cover of the known red; the campaign's stated purpose for the lints (F-011/F-032 drift) is unmet.
- Recommended resolution: clear the nine stragglers (part of the STARTER_KIT_HANDBOOK redo; two prose refs in DATABASE §0/§2; one filename ref in UI_UX Lesson 9), then make CI required on PRs. Until then, add a baseline file so the lint fails only on new hits.

**FBL-D020 — The constitution predates the QA seat and the module era**
- Classification: DEFECT · Severity: HIGH
- Files: `01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md`; cross-file `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md` §2.5, `03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md`, `QA_PLAYBOOK.md`, `BUG_FIX_PLAYBOOK.md`, `FEAT_PLAYBOOK.md`; `agent_docs/RESPONSES/response_2026-08-10_203000_run-summary.md`
- Evidence: the Blueprint's council is three agents plus "YOU (TONY STARK)"; its router knows only CONVERSION and GREENFIELD; Phase 5 is "Test locally · Deploy · Ship it 🚀"; no QA seat, no Gate Q, no Gate D, no Coordinator, no module types. Meanwhile BIM §2 defines four seats, QA §2 inserts Gate Q and Gate D before release, SFP §2.5 declares Factory-wide module identity and QA handoff. The 08-10 run summary parked "APP_FACTORY_BLUEPRINT pipeline router doesn't know BIM/FIX/FEAT module types" as a CONCERN; it was never landed.
- Why this is a defect: the document that MANIFEST says "owns the pipeline router" cannot route half the Factory's current work, and the constitution omits the seat that owns verdicts.
- Operational consequence: a cold agent reading top-down learns a lifecycle that ends at deployment without QA; the authority chain in SFP §2.5 has no constitutional home.
- Recommended resolution: add a third router branch (module work: BIM/FIX/FEAT by center of gravity), add the QA seat and Coordinator to the council diagram, and extend the lifecycle with Gate Q → deploy → Gate D → close.

**FBL-D004 — Three APP_BRIEF templates and three UI_SPEC templates coexist under a single-source claim**
- Classification: DEFECT · Severity: HIGH
- Files: `02_PIPELINE_AGENTS/ARCHITECT_QUESTIONNAIRE.md`; `02_PIPELINE_AGENTS/HANDOFF_PACKAGE_PLAYBOOK.md` §5.1, §5.3, §5.5; `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md` §9.1, §9.3, Appendix C.2; `02_PIPELINE_AGENTS/DESIGNER_PLAYBOOK.md` §8
- Evidence: ARCHITECT_QUESTIONNAIRE header: "This doc is the SINGLE SOURCE for … the APP_BRIEF template … do not fork this instrument" (12 sections: Mission, Hero Action, User & Auth Scope, Complexity Class, Domain Concepts, Scope Locks, Success, Planning State, Integrations, Constraints, Risks, Handoff). HANDOFF §5.1 lists 14 required sections in a different order with different names (App Type, One-Sentence Purpose, Who Uses This, … Known Discrepancies, Phase Transitions, Changelog). FFM §9.1 and C.2 list 13 sections (Mission Of This Phase, Hero Outcome, In Scope, Out of Scope, Hard Gates, Success Criteria Table, Known Risks, Common Stumbles, Estimated Effort, Handoff To Next Phase, Constraints, Phase Transitions, Changelog). UI_SPEC: DESIGNER §8 (5 sections) vs HANDOFF §5.3 (9 sections) vs FFM §9.3 (12 sections). HANDOFF §5.5: greenfield runs "still use this playbook's package definition."
- Why this is a defect: a greenfield Architect is bound by at least two incompatible APP_BRIEF definitions and a Designer by two UI_SPEC definitions; the "single source" claim is false.
- Operational consequence: different runs produce structurally different briefs and specs; downstream checks (FFM §9 cross-file consistency, verification gates citing "APP_BRIEF § 5") cannot be written against one shape.
- Recommended resolution: decide one template per artifact, or one per pipeline stated explicitly, and turn the other two locations into pointers with a "sections that differ per pipeline" table.

**FBL-D010 — Hub-to-project distribution is undefined in live doctrine and has never been exercised**
- Classification: DEFECT · Severity: HIGH
- Files: `MANIFEST.md`; `_OTHERS/DOCTRINE_HUB_DESIGN_v0_1.md`; `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md` §4/§15; `02_PIPELINE_AGENTS/HANDOFF_PACKAGE_PLAYBOOK.md` §13; `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md` §16, §22; `05_DESIGN_SYSTEM/THEME_LIBRARY.md` cross-refs; `05_DESIGN_SYSTEM/COMPONENT_REGISTRY.md` §11
- Evidence: MANIFEST: "Release tags: `doctrine-YYYY.MM[-patch]` (spec §2.6) — projects pin to a tag; first tag after Wave 6 completes: `doctrine-2026.07`." `git tag -l` at baseline returns nothing. The cited "spec" is `DOCTRINE_HUB_DESIGN_v0_1.md`, "DRAFT v0.1 — awaiting Tony's approval," in the lint-exempt `_OTHERS/` folder. Project-side landing paths for Hub docs differ: `agent_docs/APP_FACTORY/…` (STARTER_KIT §15, COMPONENT_REGISTRY §11), `agent_docs/STARTER_KIT_HANDBOOK.md` (HANDOFF §13), `agent_docs/starter-kit/starter-kit-handbook.md` (FFM §16, §22), `agent_docs/APP_FACTORY/design-system/…` (THEME_LIBRARY), and `agent_docs/` tagged release (HUB_DESIGN §2.4).
- Why this is a defect: the only description of how doctrine reaches a project and how a project pins a version is a draft outside the governed set, and the mechanism it describes has not been used.
- Operational consequence: no project can state which doctrine it is on; "which doc set is this project on?" cannot be answered by "one command" as the design promises; boot prompts point at paths that may not exist.
- Recommended resolution: cut the first tag; promote HUB_DESIGN §2.4–§2.6 into a live "DOCTRINE DISTRIBUTION" section (MANIFEST or a new infrastructure doc); standardize one project-side path and fix the five references.

**FBL-D021 — Model docs ship sidebar layouts that Rule Zero calls automatic failures, and the rail breakpoint disagrees across four docs**
- Classification: DEFECT · Severity: HIGH
- Files: `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md`; `05_DESIGN_SYSTEM/COMPONENT_REGISTRY.md` §7; `04_REFERENCE_MANUALS/APP_ARCHITECTURE_MANUAL.md` §4; `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md` §6; `03_BUILD_METHODOLOGY/FRONTEND_BUILD_PHASE_PLAYBOOK.md` Stage 2; `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md` §13.1
- Evidence: UI_UX Rule Zero: "A fixed sidebar with `hidden md:block` and no trigger = the rail vanishes on mobile = automatic failure"; "wide app rails (≥ ~20rem) stay a slide-over" at `md`. The same doc's "Layout Components" usage, "Sidebar Layout (Desktop Only)," and Example 3 all use `<div className="hidden md:block … w-[25rem]"><Sidebar /></div>` with no trigger; "Navbar … Responsive design (hidden on mobile, visible on md+)." APP_ARCHITECTURE §4: `<Sidebar className="w-64 hidden md:block" />`. COMPONENT_REGISTRY §7: "Tablet 768px (`md:`): sidebars become persistent," while its own AppShellPage entry says persistent at `xl`; STARTER_KIT §6 says the rail persists at `xl` (1280); UI_UX Rule Zero, FFM Gate M, and FBP Stage 2 say `lg` (1024) for wide rails.
- Why this is a defect: examples in the designated MODEL doc violate the doc's own top rule; four docs give three different breakpoints for the same rail.
- Operational consequence: a builder copying Example 3 ships the RUN_002 regression Gate M was created to catch; a reviewer cannot tell which breakpoint is the gate's threshold.
- Recommended resolution: replace the three UI_UX layouts and APP_ARCHITECTURE §4 with `AppShellPage` or a `Sheet`-triggered rail; state one rule ("fit breakpoint per component; AppShellPage rail = `xl` as shipped; Gate M threshold = the rail's declared fit breakpoint") and cite it from all four docs.

### MEDIUM

**FBL-D030 — Cookie `httpOnly` doctrine contradicts the kit handbook on a security-relevant flag**
- Classification: DEFECT · Severity: MEDIUM
- Files: `04_REFERENCE_MANUALS/AUTH_MANUAL.md` "Cookie Configuration," "Security Best Practices — DO 6"; `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md` §1
- Evidence: AUTH: "`httpOnly: true` - Not accessible via JavaScript … Set proper cookie options: `httpOnly: true`." Handbook: "`httpOnly: false` is intentional ('Supabase needs client-side session access'); do NOT 'tighten' it … a dropped flag is a live-session bug that no build will catch." AUTH also shows `src/middleware.ts` where the kit ships `src/proxy.ts` (APP_ARCHITECTURE §10 flags this; AUTH does not).
- Why this is a defect: two live docs give opposite instructions on the same flag and one warns that following the other breaks sessions.
- Operational consequence: an engineer "hardening" per AUTH breaks login; an engineer following the handbook violates AUTH's checklist.
- Recommended resolution: verify on disk which flag the kit ships and why; state the ruling once (STARTER_KIT §1) and make AUTH point to it; add the `proxy.ts` note to AUTH.

**FBL-D022 — Service error-handling doctrine conflicts with the testing and module failure-policy doctrine**
- Classification: DEFECT · Severity: MEDIUM
- Files: `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md` §3 "Error Handling Template," §6, §10 cheat sheet; `03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md` §1.8, §2.2, §4.3; `03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md` §7
- Evidence: API §3: "Services should never throw errors that crash the UI. Return safe defaults," returning `error: error.message` (raw upstream text); API §6 `fetchProfile` returns `error: error.message` from Supabase; API §4/§10 route templates return `{ error: result.error }` with status 400 to the client. Cheat sheet: "Graceful Degradation — Any data fetch — Return empty array on error." TESTING §2.2 test 4 and §4.3: route returns 500 with a generic message that "does NOT leak the upstream error text." BIM §7: "degrade is not a universal law … Security, audit, financial, tenant-isolation … may require fail-closed."
- Why this is a defect: the service template propagates upstream messages to the client, which the testing doctrine forbids and tests against; "graceful degradation for any fetch" contradicts the per-module failure-policy rule.
- Operational consequence: services built from the template fail the Factory's own integration tests; degrade-by-default can mask security or data-integrity failures.
- Recommended resolution: return typed error codes from services and map to generic client messages at the route; add "failure policy per BIM §7" to the API manual's error section.

**FBL-D005 — Architect seat responsibilities are assigned differently across docs**
- Classification: DEFECT · Severity: MEDIUM
- Files: `02_PIPELINE_AGENTS/ARCHITECT_PLAYBOOK.md` §1, §8; `01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md` router and Phase 2; `02_PIPELINE_AGENTS/HANDOFF_PACKAGE_PLAYBOOK.md` §5.5; `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md` §3; `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md` §2, §4; `05_DESIGN_SYSTEM/GLOBAL_DESIGN_SYSTEM_HANDBOOK.md` §8, §11
- Evidence: ARCHITECT §1 "Not Architect's Job: Design UI/UX, Define data schemas, Define API contracts." Blueprint router: Architect pre-authors DATA_CONTRACT in conversion. HANDOFF §5.5, ENGINEER §3, FFM §4, GDSH §8/§11: "UI_SPEC drafted by the Architect, revised by the Designer." Blueprint Phase 2 and DESIGNER §8 list UI_SPEC as a Designer deliverable with no Architect draft; ARCHITECT §8's handoff package to the Designer contains no UI_SPEC draft. FFM Role 3: Architect authors the entire FFM including skill and playbook.
- Why this is a defect: the doc that defines the seat excludes work four other docs assign to it.
- Operational consequence: an Architect following its own playbook will not produce the UI_SPEC draft the Designer, Engineer, and GDSH expect.
- Recommended resolution: ratify "Architect drafts, Designer revises" (the majority) and update ARCHITECT §1/§8 and Blueprint Phase 2; add conversion-pipeline duties to ARCHITECT_PLAYBOOK.

**FBL-D003 — STARTER_KIT_HANDBOOK was never migrated to Hub conventions and contradicts them**
- Classification: DEFECT · Severity: MEDIUM
- Files: `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md` header, §4, §14, §15; `_ARCHIVE/README.md`; `MANIFEST.md` footnote ¹
- Evidence: §14 "Filename carries the version. A rewrite bumps the filename (`_v1.0` → `_v1.1`)" vs `_ARCHIVE/README.md` "Live docs carry CANONICAL names — no version suffix." §4/§15 cite `COMPONENT_REGISTRY_v1.1.md`, `agent_docs/APP_FACTORY/AUTH_MANUAL_v1.2.md`, `UI-UX-BUILDING-MANUAL_v1_3.md` (lint hits). Header lacks the standard Version/Date/Status line (lint miss; MANIFEST footnote "F-022 redo queued"). It is the most-referenced doc in the graph (←12).
- Why this is a defect: the highest-blast-radius doc states a versioning rule the Hub forbids.
- Operational consequence: an agent bumping the handbook per §14 creates a versioned live filename, which the lint would catch only if the lint were gating (D002).
- Recommended resolution: execute the queued F-022 redo: standard header, canonical refs, delete §14's filename rule, replace project-side paths.

**FBL-D017 — Deployment, promotion, and rollback have gates and checklists but no owning doctrine**
- Classification: DEFECT · Severity: MEDIUM
- Files: `01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md` Phase 5; `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md` §11; `03_BUILD_METHODOLOGY/QA_PLAYBOOK.md` §4, §13; `03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md` §6; `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md` §17; `04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md` §13
- Evidence: Gate D requires a recorded revision, rollback readiness (D9), and "prior stable revision identified"; BIM §6 requires "merge / deploy-to-staging as the repo's deployment model requires"; ENGINEER §17 lists "Rollback procedure" as a need. No doc defines environments, promotion between them, how a revision is recorded, or a rollback procedure for Cloud Run or Vercel. The only deployment recipe is STRIPE §13 (Secret Manager + `gcloud run deploy`). Root CLAUDE.md names Cloud Run, GCS, Vercel, and DigitalOcean staging without process.
- Why this is a defect: a required gate depends on a process the corpus does not contain.
- Operational consequence: Gate D and rollback readiness are verified against tribal knowledge; the DevOps seat cannot be executed cold.
- Recommended resolution: author a DEPLOYMENT_PLAYBOOK (environments, promotion, revision identity, rollback per target) and name the seat holder; cross-link from QA §13 and BIM §6.

**FBL-D016 — Git and cloud authority differs between FFM-era and module-era doctrine without a reconciling rule**
- Classification: DEFECT · Severity: MEDIUM
- Files: `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md` §2 Role 4, §12.4; `03_BUILD_METHODOLOGY/FRONTEND_BUILD_PHASE_PLAYBOOK.md` Stage 6; `03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md` §2, §7; `03_BUILD_METHODOLOGY/BUG_FIX_PLAYBOOK.md` §3; `_SKILLS/factory-docs-update/CLAUDE.md` D5; `03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md` §5.1
- Evidence: FFM Role 4 Engineer outputs "Deployed staging URLs"; FBP Stage 6 Engineer activity "Deploy to staging (Vercel or equivalent)"; FFM `06-VERIFICATION.md` "Deploys to staging." BIM §7: "Git-zero / cloud-zero: the Engineer stages nothing, commits nothing, deploys nothing"; BUG_FIX §3 same. Hub skill D5: "Claudy owns all git; the Operator owns the merge." TESTING §5.1: "git-tag the commit" at deploy with no actor.
- Why this is a defect: the same seat has opposite git/cloud permissions depending on which playbook is open, and no doc states that this is intentional per context.
- Operational consequence: an Engineer in an FFM run may deploy; the same agent in a BIM run must not; a mixed run (FFM with a FIX inside it) has no rule.
- Recommended resolution: publish a one-table authority matrix (context × action × seat) in SFP §2.5 or the Blueprint and have each playbook cite it.

**FBL-D007 — Seat vocabulary is not normalized; "Architect" names both the human and an AI agent**
- Classification: DEFECT · Severity: MEDIUM
- Files: `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md` §1; `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md` §1, §15, §17; `02_PIPELINE_AGENTS/HANDOFF_PACKAGE_PLAYBOOK.md` §3; `01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md`; `03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md` §2; `03_BUILD_METHODOLOGY/QA_PLAYBOOK.md` §4; `03_BUILD_METHODOLOGY/APP_FACTORY_SKILLS_PLAYBOOK.md` header
- Evidence: SFP §1 diagram "HUMAN (ARCHITECT)"; ENGINEER §15 "the human is the architect"; HANDOFF §3 "the architect (operator)" — vs FFM Role 3 "You, Claude (in a chat session)," skill CLAUDE.md "the Architect ('Jarvis')," BIM §2 Architect seat distinct from "Coordinator (Operator)." Human seat: "YOU (TONY STARK) Commander / Final Approver," "Operator," "Coordinator," "Human (Tony Stark)," "stakeholders" (FF §7), "Generals" (SKILLS_PLAYBOOK). Deployment seat: "Operations / SRE" vs "DevOps / Deployment Operator" vs "(You)."
- Why this is a defect: BIM assigns binding verdict authority to "the Architect"; in SFP §1 that word means the human. Authority is ambiguous by name.
- Operational consequence: "Architect advises, Operator adjudicates" cannot be executed by a reader who learned from SFP §1 that the Architect is the Operator.
- Recommended resolution: one glossary (Operator = Tony/Coordinator; Architect = AI chat seat "Jarvis"; Engineer = Claudy; QA Lead; DevOps) placed in the Blueprint and cited by SFP §1; retire "stakeholders" and "Generals" or define them.

**FBL-D008 — Lifecycle vocabulary proliferates without one unifying map**
- Classification: DEFECT · Severity: MEDIUM
- Files: `01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md`; `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md` §2; `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md` §6, §11.3, §12, §20; `03_BUILD_METHODOLOGY/FRONTEND_BUILD_PHASE_PLAYBOOK.md` §1.5, §2; `02_PIPELINE_AGENTS/HANDOFF_PACKAGE_PLAYBOOK.md` §1, §2, §8
- Evidence: Blueprint Phases 0–5; SFP phases 1–9 (mapped to the Blueprint only); FFM Sub-Phases 0–6 with playbook files `00–07`; FFM §11.3 skill body calls the same steps "Phase 0 — Discovery … Phase 5 — Verification"; FBP Stages 1–6 plus "Stage 0 = Discovery"; HANDOFF §1 "8 supervised phases" and FFM §20 "`01-DISCOVERY.md` through `08-VERIFICATION.md`" vs FFM §12's `00–07`; FFM §6 "Phase 0 (Ignition) / Phase 1 (Foundation) / Phase 3 (Schema + RLS)" = project-roadmap phases, a fourth meaning; HANDOFF §8 "Claudy does not start Phase 0 Discovery" (build Phase 0) vs Blueprint Phase 0 (Recon). FBP §1.5 resolves only the Phase-0 collision.
- Why this is a defect: "Phase 1" has at least four referents; two docs disagree on how many FFM playbook files exist.
- Operational consequence: gate citations ("Phase 8 retrospective," "Phase 5 chat screen," "Phase 2 decision points") are ambiguous to anyone who did not live the runs.
- Recommended resolution: extend SFP §2's map to cover FFM sub-phases, build stages, and roadmap phases; rename the skill's internal "Phase N" to "Sub-Phase N"; fix HANDOFF §1/§2 and FFM §20 to the 00–07 file set.

**FBL-D014 — The Engineer seat's identity is ambiguous (spec-authoring chat agent vs Claude Code)**
- Classification: DEFECT · Severity: MEDIUM
- Files: `01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md` Phase 0, Phase 3, Phase 4; `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md` §1–§3, §12; `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md` §2 Role 4, §7
- Evidence: Blueprint Phase 3 "Engineer produces DATA_CONTRACT, DB_SCHEMA, API_SPEC, FILE_TREE"; Phase 4 "Engineer prompts Claudy … Claudy writes actual code" (two actors). Blueprint Phase 0, ARCHITECT §2, FFM Role 4, BIM §2: "Engineer (Claudy)," Claude Code in the terminal. FFM §7 greenfield: "the Engineer is the author of record — from the approved APP_BRIEF + UI_SPEC; step 4 then ships the contract shell." ENGINEER §12 template header "Author: Engineer Agent."
- Why this is a defect: whether DATA_CONTRACT is authored by a chat agent before the build or by the coding agent during the build is undetermined.
- Operational consequence: in a greenfield FFM, either the Architect ships a "contract shell" and Claudy fills it mid-run (touching `_project/` during a frozen module) or a second Engineer chat seat exists that no playbook activates.
- Recommended resolution: state that Engineer = Claudy in all contexts and define when and where the greenfield DATA_CONTRACT is completed (before freeze, as a Plan-Mode deliverable).

**FBL-D015 — QA intake requires a 15-item Engineer completion package that no Engineer-side doctrine instructs producing; QA artifact locations are unspecified**
- Classification: DEFECT · Severity: MEDIUM
- Files: `03_BUILD_METHODOLOGY/QA_PLAYBOOK.md` §6, §20; `03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md` §4, §5, §7; `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md` §17
- Evidence: QA §6 requires identifier, scope, spec, files changed, behavior claimed, tests added, commands run, results, build/typecheck, manual checks, limitations, env requirements, migrations/secrets, rollback notes, open risks. BIM §7: the Engineer hands "suggested commit messages plus exact file lists"; BIM §5 definition of done: "gates + spec + retrospective + protocol docs + STOP"; ENGINEER §17 defines a different "Handoff to Operations" package. QA §20 names `QA_PLAN.md`, `GATE_Q_REPORT.md`, `GATE_D_CHECKLIST.md`, `GATE_D_REPORT.md`; BIM §4 module package lists none of them, and the folder is frozen during the Engineer's hold.
- Why this is a defect: one seat requires an artifact another seat is never told to produce; QA outputs have no defined home.
- Operational consequence: QA intake starts with a GAP on every module or the Engineer improvises the package; QA reports land in undefined places.
- Recommended resolution: add "Engineer Completion Report" to BIM §4/§5 and ENGINEER as a required handoff artifact with QA §6's fields; define a `qa/` subfolder written after the module unfreezes.

**FBL-D011 — Load-bearing external artifacts are referenced but never located**
- Classification: DEFECT · Severity: MEDIUM
- Files: `02_PIPELINE_AGENTS/ARCHITECT_PLAYBOOK.md` §2; `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md` §1.5; `02_PIPELINE_AGENTS/HANDOFF_PACKAGE_PLAYBOOK.md` §10, §13; `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md` §14, §20; `03_BUILD_METHODOLOGY/APP_FACTORY_SKILLS_PLAYBOOK.md` §7, §14; `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md` §11; `03_BUILD_METHODOLOGY/FRONTEND_BUILD_PHASE_PLAYBOOK.md` §12; `05_DESIGN_SYSTEM/COMPONENT_REGISTRY.md` §8, §9; `03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md` §6
- Evidence: `stark-recon` at `_SKILLS/stark-recon/CLAUDE.md` (ARCHITECT §2) — not in this repo; `brain-drain`, `stark-frontend-first`, `CLOUD_DEPLOYMENT_SKILLS`, `SUPABASE_MIGRATION_SKILL` — not in this repo; SKILLS_PLAYBOOK §7 says `_SKILLS/` is "the operator's skill LIBRARY" while §14 says instances "live repo-side" (F-021), yet this Hub's `_SKILLS/` holds exactly one skill. Worked examples required by SFP §1.5 ("Every methodology playbook … is paired with a concrete worked example") are cited at `agent_docs/CURRENT_APP/app-factory-frontend-first-module/_project/` and `cyber_pharma_v1_phase1_ffm/`, which exist only in project repos. `KNOWN_ISSUES.md`, `KIT_PROPOSALS_ARCHIVE.md`, `STARTER_KIT_FEEDBACK.md`, `agent_docs/LESSONS/` are cited without a home.
- Why this is a defect: the Hub is the canonical home and cannot tell a cold agent where any of these live.
- Operational consequence: Phase 0 cannot be executed via the named skill from the Hub alone (mitigated: RECON_QUESTIONNAIRE is self-executing); the Doctrine Pairing Principle is unfulfilled inside the Hub.
- Recommended resolution: add a `_EXAMPLES/INDEX.md` (repo, path, tag per example) and a skill locator table (skill → repo → path) to MANIFEST or the Skills Playbook.

**FBL-D018 — "Plan Mode" and the root CLAUDE.md are load-bearing but sit outside the governed doc set**
- Classification: DEFECT · Severity: MEDIUM
- Files: `CLAUDE.md` (root); `03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md` §5–§7; `03_BUILD_METHODOLOGY/BUG_FIX_PLAYBOOK.md` §16; `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md` §13.1, §22; `03_BUILD_METHODOLOGY/FRONTEND_BUILD_PHASE_PLAYBOOK.md` Stage 2; `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md` §15; `03_BUILD_METHODOLOGY/APP_FACTORY_SKILLS_PLAYBOOK.md` §10
- Evidence: "Plan Mode" is invoked in BIM (§5 item 9, §6, §7), BUG_FIX §16, FFM boot prompts, the Hub skill D2, and root CLAUDE.md. It is defined for skills in SKILLS_PLAYBOOK §10 and for Claude Code in root CLAUDE.md, which is not in MANIFEST, is lint-exempt, carries its own version (3.1), and includes FastAPI/ADK/Streamlit rules unrelated to the Kit Track. FFM §13.1 and FBP Stage 2 cite "root CLAUDE.md forbidden zone" as Gate M's source of truth; the Hub's root CLAUDE.md contains no such zone. Root CLAUDE.md carries a second Karpathy Protocol (20 failure modes) while ENGINEER §15 (12) declares "if any other doc's paraphrase and this section disagree, this section wins."
- Why this is a defect: a behavior every playbook depends on has no home in the governed set, and a duplicated protocol has two competing "canonical" claims.
- Operational consequence: agents in other tools (Codex, Gemini) never read root CLAUDE.md; the FFM's Gate M pointer resolves to nothing in the Hub.
- Recommended resolution: define Plan Mode once in ENGINEER §15 (agent conduct) and have root CLAUDE.md and the skills playbook point to it; decide whether root CLAUDE.md is doctrine (enter MANIFEST and lint scope) or tool config (strip factory doctrine from it).

**FBL-D031 — There is no Factory-wide precedence rule; individual docs each declare themselves the winner**
- Classification: DEFECT · Severity: MEDIUM
- Files: `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md` Rule Zero and Rule Zero-B; `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md` §15; `02_PIPELINE_AGENTS/DESIGNER_PLAYBOOK.md` §13; `03_BUILD_METHODOLOGY/QA_PLAYBOOK.md` §5; `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md` "Disk wins over docs"; `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md` C.1; `_SKILLS/factory-docs-update/CLAUDE.md` §6
- Evidence: "Rule Zero wins" and "Rule Zero-B wins" (UI_UX); "this section wins" (ENGINEER §15); "the doctrine doc wins" (DESIGNER §13); an eight-level order for QA only; "disk wins" (handbook); a per-module order (FFM C.1); "the Playbook wins" (skill §6). No document states tier precedence (Constitution over Method over Manual) or how "disk wins" interacts with "Rule Zero-B wins" when the kit ships numbered colors (GDSH §3.4 acknowledges the kit does).
- Why this is a defect: authority among documents is resolved locally and inconsistently; the packet's "where approval/authority is ambiguous" test fails at the corpus level.
- Operational consequence: when the kit's running code (numbered colors, `httpOnly: false`) conflicts with design or auth doctrine, two live rules give opposite answers with no tiebreaker.
- Recommended resolution: one precedence clause in the Blueprint: reality on disk → accepted module contract → Constitution → Method → Manual → Design; local "X wins" statements become citations of it.

**FBL-D023 — Numbered Tailwind colors are presented as kit conventions while the design tier calls them automatic failures**
- Classification: DEFECT · Severity: MEDIUM
- Files: `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md` §9 "Theme Conventions"; `05_DESIGN_SYSTEM/COMPONENT_REGISTRY.md` AppShellPage "Theme behavior"; `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md` §10.5, `Main` usage, §10.8; `05_DESIGN_SYSTEM/GLOBAL_DESIGN_SYSTEM_HANDBOOK.md` §3.4; `05_DESIGN_SYSTEM/TOKEN_FILE.md` §4
- Evidence: Handbook §9: "Explicit Tailwind classes for theme-aware backgrounds: Dialog `bg-white dark:bg-slate-800`; Toast `bg-white dark:bg-zinc-900`; Input `bg-slate-100 dark:bg-slate-500`." Registry: "Dark mode default: `dark:bg-zinc-800`." UI_UX §10.5 "Explicit Dark Variants (When Needed): `bg-white dark:bg-gray-900` … `text-gray-600 dark:text-gray-400`"; `<Main className="bg-gray-50">`; §10.8 "Test at custom `lg` breakpoint (1150px)" vs Rule Zero's 1024. Rule Zero-B: "Tailwind color names that bypass tokens … AUTOMATIC FAILURES." GDSH §3.4 and TOKEN_FILE §4 call migrating these a "foundational task."
- Why this is a defect: the handbook and registry state the violations as conventions without the migration flag; UI_UX endorses the pattern in the same document that forbids it.
- Operational consequence: a builder matching the kit ("match, don't invent") fails Rule Zero-B; a reviewer cannot tell convention from debt.
- Recommended resolution: label Handbook §9 and the Registry entry "LEGACY — migration task per TOKEN_FILE §4"; delete UI_UX §10.5's explicit-variant example and the 1150px line.

**FBL-D006 — `FILE_TREE.md` is required by the constitution and root CLAUDE.md but no workflow produces it**
- Classification: DEFECT · Severity: MEDIUM
- Files: `01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md` Phase 3, "Blind Spots"; `CLAUDE.md` (root) "Factory Pipeline Awareness," failure mode 19; `02_PIPELINE_AGENTS/HANDOFF_PACKAGE_PLAYBOOK.md` §1; `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md` §3, §9; `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md` §12
- Evidence: Blueprint: Engineer produces `FILE_TREE.md`; "FILE_TREE.md = source of truth; Engineer enforces 'don't touch what works.'" Root CLAUDE.md: reading order APP_BRIEF → DATA_CONTRACT → FILE_TREE → UI_SPEC; "Deviating from FILE_TREE.md without flagging it" is a named failure. HANDOFF and FFM define the package as four files (APP_BRIEF, DATA_CONTRACT, UI_SPEC, `_project/CLAUDE.md`); ENGINEER §12 embeds a "File Structure" section inside DATA_CONTRACT; UI_SPEC carries a "Component Inventory."
- Why this is a defect: one workflow requires an artifact another never creates.
- Operational consequence: an agent obeying root CLAUDE.md looks for a file that does not exist; the "don't touch what works" control has no artifact.
- Recommended resolution: decide: either add FILE_TREE.md to the package (FFM §9) or retire it from the Blueprint and root CLAUDE.md in favor of DATA_CONTRACT §2 / `_project/CLAUDE.md` "Project Structure."

### LOW

**FBL-D025 — FRONTEND_BUILD_PHASE cites QA_PLAYBOOK §9/§10 for Gate Q/Gate D; the superseded QA v1.1 has them at §12/§13**
- Files: `03_BUILD_METHODOLOGY/FRONTEND_BUILD_PHASE_PLAYBOOK.md` §9; `03_BUILD_METHODOLOGY/QA_PLAYBOOK.md`; `agent_docs/RESPONSES/response_2026-08-10_194109_phase2-ripple-map.md`
- Evidence: FBP §9: "Gate Q … per `QA_PLAYBOOK.md` §9," "Gate D … per `QA_PLAYBOOK.md` §10" (landed from the navbar pack against QA v0.1). Live QA v1.1: §9 is "QA Engagement Lifecycle," §10 "Scope Protection," §12 "Gate Q," §13 "Gate D." The 08-10 ripple map marked FBP "CONSISTENT — Gate Q/D retained" without checking anchors.
- Consequence: the pointer lands on the wrong section. Resolution: fix the two anchors; add "verify inbound section anchors" to the ripple map's consistency check.

**FBL-D009 — MANIFEST and CHANGELOG index hygiene is off; the live-doc count is wrong after two runs**
- Files: `MANIFEST.md`; `CHANGELOG.md`; `agent_docs/RESPONSES/response_2026-08-10_194109_phase2-ripple-map.md`
- Evidence: MANIFEST title "The 29 Live Docs"; 31 tier docs are listed and exist (lint counts 33 with MANIFEST and CHANGELOG). The 08-10 ripple map computed "27 → 29" for BIM and FEAT while noting QA and BUG_FIX (08-05) "were never added" — those two had already made the count 29, so the true count became 31. Appendix says "all 27 bodies." MANIFEST header still v1.0 / 2026-07-12 after two regenerations. The undeclared-dependencies appendix predates FBP v1.2.2's QA/BUG_FIX pointers. CHANGELOG "Ongoing entries" table has no header row.
- Consequence: the index lies about its own size; regeneration rules are not followed for the index's own header. Resolution: correct to 31, bump MANIFEST/CHANGELOG headers, add the table header.

**FBL-D024 — Cross-references cite section anchors that do not exist**
- Files: `05_DESIGN_SYSTEM/THEMING_MANUAL.md` §0, §7, §10; `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md` Rule Zero-B cross-ref; `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md` §14; `04_REFERENCE_MANUALS/APP_ARCHITECTURE_MANUAL.md`
- Evidence: THEMING cites "APP_ARCHITECTURE_MANUAL §Theming Files," "HANDOFF_PACKAGE_PLAYBOOK §Designer Handoff," "UI-UX-BUILDING-MANUAL §Typography," "STARTER_KIT_HANDBOOK §shadcn Defaults" and "§Lucide Icons" — none of those sections exist in the cited docs. UI_UX Lesson 9 claims APP_ARCHITECTURE was updated with theming cross-references; APP_ARCHITECTURE never mentions THEMING_MANUAL (one-way pairing). SFP §14 "Quick Pattern Lookup" cites UI-UX "Component Library" (no such section).
- Consequence: an agent following pointers finds nothing. Resolution: fix or drop the anchors; consider an anchor lint.

**FBL-D012 — Artifact status vocabularies disagree within a paired doc set**
- Files: `02_PIPELINE_AGENTS/ARCHITECT_PLAYBOOK.md` §7; `02_PIPELINE_AGENTS/ARCHITECT_QUESTIONNAIRE.md` template; `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md` C.2; `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md` §12; `02_PIPELINE_AGENTS/DESIGNER_PLAYBOOK.md` §8
- Evidence: DRAFT/REVIEW/APPROVED/AMENDED (playbook) vs `[DRAFT | REVIEW | LOCKED]` (questionnaire, same v2.2 wave) vs `Status: LOCKED` (FFM stub) vs `DRAFT | APPROVED` (DATA_CONTRACT) vs `Status: APPROVED` (UI_SPEC).
- Consequence: gate checks on "APPROVED" vs "LOCKED" are ambiguous. Resolution: one status set for all factory artifacts.

**FBL-D013 — Dangling internal reference in DESIGNER_PLAYBOOK**
- Files: `02_PIPELINE_AGENTS/DESIGNER_PLAYBOOK.md` §7
- Evidence: "All required elements present (per §5.6 minimum display fields, if defined)" — §5 has no 5.6. Resolution: delete or point to UI_SPEC §5.

**FBL-D026 — ECOMMERCE defers to a checkout store the STATE manual does not define**
- Files: `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md` §4, §7, §8; `04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md` §6
- Evidence: ECOM §7 "See STATE_MANAGEMENT_MANUAL for the full checkout store implementation," then its code uses `shippingCost`, `couponCode`, `couponDiscount`, `setCoupon`, `clearCoupon`; STATE §6's checkout template has none of them.
- Consequence: the pointed-to implementation cannot run the pointing doc's code. Resolution: align one store shape.

**FBL-D027 — Supabase secret env-var names differ across manuals**
- Files: `03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md` §4.1; `04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md` §4; `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md` §5; `04_REFERENCE_MANUALS/DATABASE_MANUAL.md` §5; `02_PIPELINE_AGENTS/RECON_QUESTIONNAIRE.md` S0.6
- Evidence: `SUPABASE_SECRET_KEY` (TESTING, StarkReads provenance) vs `SUPABASE_SERVICE_ROLE_KEY` (STRIPE, same provenance; API; DATABASE); `NEXT_PUBLIC_SUPABASE_ANON_KEY` everywhere vs RECON S0.6 "Real code used the Q4-2025 naming (publishable/secret)."
- Consequence: limited — RECON already says doc env names are suggestive. Resolution: one names table with a "verify on disk" note.

**FBL-D028 — The Hub skill's supporting files still describe the pre-v0.3 cargo location**
- Files: `_SKILLS/factory-docs-update/README.md` "New docs entering the Hub"; `templates/LESSONS_LEARNED.md` header; `references/ANTI_PATTERNS.md` AP-11
- Evidence: v0.3 CLAUDE.md/SKILL.md mandate `_INBOX/`; README's gotcha says "the files just need to be in the root (Step 3)" while Step 3 says `_INBOX/`; the lessons template says packs are found "in the Hub clone root"; AP-11 says "The Operator's runbook puts them in the root."
- Consequence: an operator reading the runbook gets two instructions. Resolution: sync the three files at the v0.4 bump.

**FBL-D029 — API_AND_SERVICES_MANUAL has two "## 10. Quick Reference" sections**
- Files: `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md`
- Evidence: "## 10. Quick Reference" appears before §11–§13 and again after them with overlapping content; the ToC lists ten sections. Resolution: renumber and merge.

## 8. RANKED SUGGESTIONS

Ranked by expected operational value. None of these is a defect; each is an improvement the doctrine does not currently forbid or require.

| ID | Suggestion | Where | Value |
|---|---|---|---|
| FBL-S001 | Add a Hub entry point (`START_HERE.md` or a MANIFEST preamble) with a reading order by seat (Operator, Architect, Designer, Engineer, QA), the tier precedence, and a "where things live" table (skills, examples, kit, projects). The root README is two lines; a cold agent has no path in. | `README.md`, `MANIFEST.md` | Highest: removes the largest cold-start executability gap without touching doctrine content. |
| FBL-S002 | Publish one gate registry: Gate M, Gate Q, Gate D, production confirmation, FFM Gates 0–6 and G1..n, module gates (X*, V*, N*, P-G*), AC1..n — each with owner seat, verdict vocabulary, doc home, and the phase it closes. | New section in SFP §2.5 or Blueprint | Gates are the Factory's control surface; today they are discoverable only by reading eight docs. |
| FBL-S003 | Extend the lints: an anchor lint (every "§X" or "Section Y" citation resolves in the target doc), a project-path lint (`agent_docs/…` refs in live doctrine), and a baseline file so CI fails only on new hits until the stragglers are cleared; run on every branch, not only main. | `lints/`, `.github/workflows/doctrine-lint.yml` | Turns the watchdog back into a gate and catches the D024/D025 class automatically. |
| FBL-S004 | Un-park MANIFEST auto-generation (DOCTRINE_HUB_DESIGN §3): generate the doc table, count, and ← map from headers in CI; assert the count. | `lints/`, `MANIFEST.md` | Ends the hand-computed index that has drifted twice in two runs (D009). |
| FBL-S005 | Add the Recon Report to DESIGNER_PLAYBOOK §2 inputs; it already carries the Tailwind version, token location, dark-mode mechanism, and font setup the Designer is told to discover by hand. | `DESIGNER_PLAYBOOK.md` §2 | Removes a duplicate discovery step and closes the recon loop for the one seat that does not read the report. |
| FBL-S006 | Give the Recon Report format slots for Sections 11 and 12 (nav/auth-state answers and verification-ritual confirmations) so those prompts have a place to land. | `RECON_QUESTIONNAIRE.md` report format | Two sections of the instrument currently produce output with no home. |
| FBL-S007 | Prune project residue from constitution-tier and model docs: Blueprint "Immediate Next Steps" and the Pepper's Rig Streamlit tree; UI_UX "Suggestions for Improvement" and "Questions & Discussion Points" (which re-open questions Rule Zero already answers). | `APP_FACTORY_BLUEPRINT.md`, `UI_UX_BUILDING_MANUAL.md` | Shortens the two docs every new agent reads first and removes contradictory open questions from a MODEL doc. |
| FBL-S008 | Adopt BIM's "Governed by" header field across the Hub so precedence is declared per doc, and let the lint check that every "Governed by" target exists. | Header standard, `lints/header_lint.py` | Makes the tier hierarchy machine-visible; pairs with the D031 resolution. |
| FBL-S009 | Cross-link the three companion artifacts TESTING Part 5 defines (`CHANGELOG.md`, `SECURITY_FINDINGS.md`, `CLEANUP_BACKLOG.md`) from BUG_FIX §9/§14, QA §31, and BIM §12, and scaffold them in the FFM skeleton tree. | Four docs | The artifacts are required by three playbooks but defined in one; the skeleton does not create them. |
| FBL-S010 | Define the QA seat's activation contract the way FFM defines the Engineer's: who holds it, how a QA session is booted, what it reads first, and where its artifacts land. | `QA_PLAYBOOK.md` §4 or a `QA_ACTIVATION` section | The seat is the Factory's newest and most authority-bearing role and has no boot procedure. |
| FBL-S011 | Add a kit-baseline line to MANIFEST or CHANGELOG (kit v3, Next 16.2.1, React 19.2.4, Tailwind 3.4) and bump it when the kit changes, so doctrine-versus-kit drift is dated. | `MANIFEST.md` | The handbook is the only doc that dates the kit; RECON's "handbook is aspirational" lesson has no counter-signal. |
| FBL-S012 | Write the negative paths for the Blueprint's gates: REVIEW rejected, APPROVED then AMENDED, Designer blocked on a missing anchor, recon stale mid-run — with the re-entry point for each. | `APP_FACTORY_BLUEPRINT.md` | The lifecycle is written as the happy path; ARCHITECT §7's AMENDED state has no downstream consequence. |
| FBL-S013 | Codify Version History ordering (the 08-10 run's refinement item 1): newest-last for new and superseded docs; follow the existing order on edits. | `_ARCHIVE/README.md` bump procedure | Two conventions coexist today (SFP newest-first; 03-tier newest-last); the rule exists only in a run log. |
| FBL-S014 | Note in `_ARCHIVE/README.md` that snapshots begin at 2026-07-12 and earlier versions are recoverable only from git history, so the "visible-history record" claim is bounded. | `_ARCHIVE/README.md` | Prevents a reader from assuming the archive is complete for pre-Wave-6 versions. |

## 9. CROSS-DOCUMENT CONTRADICTIONS

Each row is a case where two live documents cannot both be followed. Defect IDs link to the evidence in §7.

| # | Side A | Side B | Nature | ID |
|---|---|---|---|---|
| 1 | AUTH_MANUAL Key Principle 5 / "Where Roles Live": authorization is NEVER read from `user_metadata` | AUTH_MANUAL §12 routes authorize on `requester.user_metadata?.is_qr_superadmin`; Summary "Roles stored in user_metadata" | Same document contradicts itself on a security control | D001 |
| 2 | STARTER_KIT_HANDBOOK §2: no app-side superadmin-creation surface, ever | AUTH_MANUAL §12 `/api/superadmin/add-user` creates users with `is_qr_superadmin: 1` | Forbidden surface documented as a pattern | D001 |
| 3 | DATABASE_MANUAL §2: never mirror a `role` column onto a profile table | AUTH_MANUAL §13 `app_users … role TEXT DEFAULT 'member'` | Direct contradiction | D001 |
| 4 | STARTER_KIT_HANDBOOK §13: login UI, auth store, role checker are DO NOT BUILD | SOFTWARE_FACTORY_PLAYBOOK §9 Phase 7 checklist builds all three | Constitution vs kit authority | D001 |
| 5 | AUTH_MANUAL §0: `authService.ts` "SHOULD NOT EXIST" | APP_ARCHITECTURE_MANUAL §2 lists `authServices.ts` in the standard layout | Manual vs manual | D001 |
| 6 | AUTH_MANUAL Navbar Law: UI is never gated on client-resolved identity | APP_ARCHITECTURE §4 `'use client'` AdminLayout gated on `selectIsAdmin`; STATE §1 "Zustand … route protection" | Manual vs manual; STATE §1 table vs STATE §1 Division of Labor | D001 |
| 7 | STARTER_KIT_HANDBOOK §1: `httpOnly: false` is deliberate, do not tighten | AUTH_MANUAL cookie options and DO-list: `httpOnly: true` | Opposite instructions on one flag | D030 |
| 8 | ECOMMERCE §11: server recalculates totals, never trusts client; coupon validated on server | ECOMMERCE §3 sample computes from `body.items[].price` and `body.coupon.discount` | Sample violates its own checklist | D019 |
| 9 | TESTING §4.3: payment routes return a generic message; upstream error text never leaks | ECOMMERCE §3 returns `error.message` for StripeError; API §3/§6 return raw `error.message` to routes that forward it | Testing doctrine vs manuals | D019, D022 |
| 10 | ARCHITECT_QUESTIONNAIRE: SINGLE SOURCE for the APP_BRIEF template, do not fork | HANDOFF §5.1 (14 sections) and FFM §9.1/C.2 (13 sections) define different APP_BRIEFs | Three templates, one single-source claim | D004 |
| 11 | ARCHITECT_PLAYBOOK §1: designing UI/UX and defining data schemas is not the Architect's job | HANDOFF §5.5, ENGINEER §3, FFM §4, GDSH §8: Architect drafts UI_SPEC; Blueprint router: Architect pre-authors DATA_CONTRACT | Seat definition vs four assignments | D005 |
| 12 | SOFTWARE_FACTORY_PLAYBOOK §1: the human is the Architect | BIM §2: the Architect issues binding verdicts and advises the Coordinator (the human) | Same word, two seats | D007 |
| 13 | UI_UX Rule Zero: `hidden md:block` with no trigger is an automatic failure | UI_UX "Layout Components," "Sidebar Layout," Example 3; APP_ARCHITECTURE §4 | Examples violate the doc's own rule | D021 |
| 14 | UI_UX Rule Zero and FBP/FFM Gate M: wide rails persist at `lg` | STARTER_KIT §6 and COMPONENT_REGISTRY AppShellPage: `xl`; COMPONENT_REGISTRY §7: `md` | Three breakpoints for one rail | D021 |
| 15 | UI_UX Rule Zero-B: Tailwind color names that bypass tokens are automatic failures | UI_UX §10.5 explicit `dark:bg-gray-900` variants; STARTER_KIT §9 Theme Conventions; COMPONENT_REGISTRY `dark:bg-zinc-800` | Conventions documented as violations | D023 |
| 16 | BIM §7 / BUG_FIX §3: Engineer runs zero git and zero cloud commands | FFM Role 4 / FBP Stage 6: Engineer deploys to staging; Hub skill D5: Claudy owns all git | Same seat, opposite permissions by context | D016 |
| 17 | Blueprint Phase 3/Phase 4 and root CLAUDE.md: `FILE_TREE.md` is an Engineer deliverable and source of truth | HANDOFF §1, FFM §3/§9: the package is four files, none of them FILE_TREE | Required artifact never produced | D006 |
| 18 | QA §6: Engineer hands a 15-item completion package | BIM §7: Engineer hands commit messages and file lists; ENGINEER §17: a different Operations package | Handoff expected by one seat, unspecified for the other | D015 |
| 19 | MANIFEST: projects pin to `doctrine-YYYY.MM` tags; first tag `doctrine-2026.07` | Repository has no tags | Stated mechanism vs repository state | D010 |
| 20 | FBP §9: Gate Q per QA_PLAYBOOK §9, Gate D per §10 | QA_PLAYBOOK v1.1: §9 lifecycle, §10 scope protection, §12 Gate Q, §13 Gate D | Stale anchors after supersession | D025 |
| 21 | ENGINEER §15: this section is canonical for the Karpathy Protocol; other paraphrases lose | Root CLAUDE.md carries a 20-item variant and additional protocols (Plan Mode, TDD flow) not in ENGINEER §15 | Two canonical claims | D018 |
| 22 | FFM §12/§21: playbook files `00-OVERVIEW` … `07-RETROSPECTIVE` | FFM §20 and HANDOFF §1/§2: `01-DISCOVERY` … `08-VERIFICATION`, "8 supervised phases" | File set disagrees within one doc | D008 |
| 23 | ARCHITECT_PLAYBOOK §7: APPROVED / AMENDED | ARCHITECT_QUESTIONNAIRE template: LOCKED; FFM C.2: LOCKED | Status vocabulary within one pair | D012 |
| 24 | STARTER_KIT_HANDBOOK §14: filename carries the version; a rewrite bumps the filename | `_ARCHIVE/README.md`: live docs carry canonical names, no version suffix | Versioning rule vs Hub law | D003 |

## 10. ARCHITECTURAL / MAINTAINABILITY RISKS

**R1 — Duplicated doctrine with independent drift vectors.** The corpus intentionally duplicates in some places (forbidden zones in APP_BRIEF and `_project/CLAUDE.md`; hard gates in three FFM files) and unintentionally in others: APP_BRIEF template ×3, UI_SPEC template ×3 (D004); Kit Audit in FRONTEND_FIRST §0 and FBP §1.6; Pre-Write Check in FRONTEND_FIRST §13 and FBP Stage 2 even though FRONTEND_FIRST §14 says stage doctrine was relocated; Rule Zero in UI_UX, GDSH §5, and COMPONENT_REGISTRY §7 with different breakpoint claims (D021); module identity restated "for convenience" in BIM §3 and BUG_FIX §17; Karpathy Protocol in ENGINEER §15 and root CLAUDE.md (D018). Every restatement is a place the next bump can miss. The MANIFEST appendix already lists 41 undeclared body mentions the header pairs do not capture.

**R2 — The index and the lints are the only machine checks, and both are weak today.** MANIFEST's count and ← map are hand-computed and have drifted twice (D009); the lints read canonical names from MANIFEST, so a MANIFEST error propagates into the drift-killer; the lints are red and merged over (D002). The one skill that keeps the Hub consistent depends on the ← map for its ripple analysis, so index errors become missed ripples (the 08-05 QA/BUG_FIX backfill gap was exactly this).

**R3 — Constitution lag.** New doctrine enters at the method tier (QA, BUG_FIX, BIM, FEAT: four docs in five weeks) faster than the constitution absorbs it (D020). Parked concerns ("Blueprint router doesn't know module types") live in run logs, and the 08-10 run deleted 31 prior run logs, so the parked-concern backlog has no durable home. Recommendation: a standing `CONCERNS.md` or a CHANGELOG "parked" section.

**R4 — Per-project forks of reusable doctrine by design.** FFM §3 copies `skills/`, `playbook/`, and `verification/` forward into every module and says they are "refined with every run." Nothing states how refinements return to the canonical copy or where the canonical copy is (D011). Over N runs, N variants of `stark-frontend-first` exist with no reconciliation rule; the Skills Playbook's "sync obligation" (§14) is stated only for doc-backed skills.

**R5 — Authority is local, not layered.** Precedence is asserted document-by-document (D031) and seat names are not normalized (D007). As more seats and gates are added, the number of pairwise "who wins" questions grows quadratically; a single tier-precedence clause and a glossary collapse it.

**R6 — Hidden dependencies on ungoverned files.** Root CLAUDE.md (Plan Mode, session protocol, reading order), DOCTRINE_HUB_DESIGN (the distribution spec), project-side path conventions, and off-Hub skills are all load-bearing and all outside MANIFEST and lint scope (D010, D011, D018). A change to any of them is invisible to the Hub's controls.

**R7 — Size and shape.** ~40,000 lines across 31 live docs; the FFM manual alone is 2,643 lines with embedded templates; the ENGINEER manual carries two tracks in one file. Large docs are where anchors go stale (D024, D025) and where examples drift from rules (D001, D021, D023) because rule and example are far apart. The Factory's own lesson ("doctrine that lives mid-document does not survive long sessions," UI_UX Lesson 5) applies to the corpus itself.

**R8 — Gates without named owners.** Gate M is "verified in the same sub-phase" by the Engineer, approved by the Operator, and umbrella'd by Gate Q — three docs, no single owner. The token lock and canonical-screen lock are human gates with no artifact recording the lock. The gate registry (S002) is the structural fix.

**R9 — Evidence records are the only executability proof.** `agent_docs/RESPONSES` shows the update process working, which is a strength, but the same folder was 31 files lighter after the last run by operator choice. If run logs are the only evidence that a process is followable, their retention policy is a doctrine question, not housekeeping.

## 11. RECOMMENDED HUMAN DECISIONS

These are decisions only the Operator can make. The review states the options and, where the corpus supports one, the majority position; it does not decide.

1. **Auth samples: delete or archive?** AUTH_MANUAL §12–§14 and the SFP Phase 7 samples can be deleted, moved to `_ARCHIVE` as history, or rewritten against the kit. Deletion is fastest; rewriting requires disk verification of `useAuthStore`, `protectPage`'s return shape, and the cookie flag (D001, D030).
2. **`httpOnly` ruling.** The handbook says `false` is deliberate; AUTH says `true`. Verify on disk and rule once (D030).
3. **One APP_BRIEF and one UI_SPEC template, or one per pipeline?** The corpus supports either; it does not support three (D004).
4. **Greenfield UI_SPEC authorship.** Majority position across HANDOFF, ENGINEER, FFM, and GDSH: Architect drafts, Designer revises. Ratify it and fix the Blueprint and ARCHITECT_PLAYBOOK, or rule the other way (D005).
5. **Is root CLAUDE.md doctrine?** If yes, enter it in MANIFEST and lint scope and reconcile its Karpathy copy with ENGINEER §15. If no, strip Factory doctrine from it and point to the Hub (D018).
6. **Engineer seat identity.** Rule that the Engineer is Claudy in every context, and state when the greenfield DATA_CONTRACT is completed (D014).
7. **Git/cloud authority matrix.** Ratify who may commit, push, deploy in FFM runs, module runs, and Hub doctrine runs (D016).
8. **Cut a doctrine tag now?** `doctrine-2026.09` would be the first; it makes MANIFEST's pinning promise true and dates this baseline (D010).
9. **Where do skills live?** The Hub hosts one skill; the Skills Playbook says instances live repo-side. Choose: Hub-hosted library, repo-side with a locator table, or both with a sync rule (D011).
10. **Merge-over-red: keep or end?** Either clear the nine stragglers and require green CI, or adopt a baseline file so CI is red only for new hits (D002).
11. **`FILE_TREE.md`: require it or retire it** from the Blueprint and root CLAUDE.md (D006).
12. **Deployment doctrine owner.** Who authors the deployment/rollback playbook and holds the DevOps seat (D017).
13. **QA seat holder.** Human, dedicated AI session, or the same agent under separation rules; and its activation contract (S010).
14. **STARTER_KIT_HANDBOOK redo (F-022): schedule it.** It is the widest-referenced doc and the source of six of nine lint hits (D003).
15. **APP_REGISTRY.md.** Still proposed-only; approve, defer, or drop so the "pending approval" note can be resolved (SFP §2.5, BIM §3).

## 12. FILE-BY-FILE REVIEW APPENDIX

Format per file: purpose · authority · strengths · defects · suggestions · dependencies · overlaps/conflicts · **disposition** (STRONG / NEEDS ATTENTION / MATERIAL REVISION NEEDED).

### 01_CONSTITUTION

**`01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md`** (v2.1) — The constitution: council, pipeline router, Phase 0–5 lifecycle. Authority: Tier 1, "owns the pipeline router" (MANIFEST). Strengths: the two-pipeline router with per-pipeline DATA_CONTRACT ownership is clear; Phase 0 recon is stated as law. Defects: no QA seat, no module routing, lifecycle ends at "Ship it" (D020); FILE_TREE required but never produced (D006); Engineer/Claudy split (D014); "Windsurf/Cascade" reviewer and Pepper's Rig Streamlit tree are project residue (S007); no negative paths (S012). Dependencies: everything (←7 declared). Overlaps: router duplicated from FFM §4 by design. **MATERIAL REVISION NEEDED.**

**`01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md`** (v1.3) — Process spine: nine build phases, Doctrine Pairing Principle, §2.5 Module Identity & QA Handoff. Authority: Tier 1. Strengths: §2 phase-vocabulary map; §1.5 pairing principle; §2.5 is the best-written governance text in the corpus. Defects: §9 Phase 7 teaches metadata roles and builds what the kit forbids (D001); §1 names the human "Architect" (D007); §6 service template swallows errors (D022 adjacent); §14 cites non-existent section names (D024); §1.5 example paths resolve only in project repos (D011). Dependencies: ←8. Overlaps: Phase 2 correctly defers to DESIGNER_PLAYBOOK. **MATERIAL REVISION NEEDED** (Phase 7 and §1 only; §2.5 is STRONG).

**`01_CONSTITUTION/STARTER_KIT_HANDBOOK.md`** (v1.1, pre-standard header) — What the kit provides; the "Should I Author This?" table. Authority: Tier 1 but declared "aspirational — verify on disk" by RECON and the Blueprint. Strengths: DO NOT BUILD table; two-table pattern; console-only superadmin doctrine; AUTH-WALK; verification triad. Defects: non-standard header and six versioned refs (D002, D003); §14 filename-carries-version rule contradicts Hub law (D003); §9 numbered-color conventions without a migration flag (D023); `httpOnly` ruling conflicts with AUTH (D030). Dependencies: ←12, widest in the graph. **MATERIAL REVISION NEEDED** (the queued F-022 redo).

### 02_PIPELINE_AGENTS

**`02_PIPELINE_AGENTS/ARCHITECT_PLAYBOOK.md`** (v2.2) — How to be the Architect. Strengths: Recon Mode as the Architect's Plan Mode; anti-patterns with tests; type-specific emphases. Defects: §1 "not my job" table contradicts four docs (D005); §2 skill path not in Hub (D011); §7 status vocabulary vs questionnaire (D012); no conversion-pipeline duties. Dependencies: ARCHITECT_QUESTIONNAIRE (single source it points to). **NEEDS ATTENTION.**

**`02_PIPELINE_AGENTS/ARCHITECT_QUESTIONNAIRE.md`** (v2.2) — The ignition instrument and APP_BRIEF template. Strengths: Hard Gate on out-of-scope; Planning State table; optional Phase 4 routing rule. Defects: single-source claim contradicted by HANDOFF and FFM templates (D004); "App Type" means two things (Q13 vs template §4); LOCKED vs APPROVED (D012). **NEEDS ATTENTION.**

**`02_PIPELINE_AGENTS/DESIGNER_PLAYBOOK.md`** (v2.1) — How to be the Designer. Strengths: Canonical Page Method; tokens-are-the-contract; §13 conflict rule (doctrine doc wins). Defects: §7 dangling §5.6 (D013); §8 UI_SPEC template is one of three (D004); inputs omit the Recon Report (S005). Overlaps: GDSH §8/§9 restate deliverables and workflow consistently. **STRONG** with two small fixes.

**`02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md`** (v1.2) — How to be the Engineer, two tracks, Karpathy Protocol, session protocol. Strengths: Part I recon-executor role; §3 per-pipeline inputs; §14 kit anti-pattern; §15 all-agent conduct. Defects: seat identity vs Blueprint (D014); §17 "Operations" seat unnamed elsewhere (D007, D017); §15 has a competing copy in root CLAUDE.md (D018); §12 DATA_CONTRACT template is Python-shaped while the Kit Track's contract is defined in HANDOFF §5.2 (two DATA_CONTRACT shapes; noted, not split into a separate defect). Dependencies: ←7. **NEEDS ATTENTION.**

**`02_PIPELINE_AGENTS/HANDOFF_PACKAGE_PLAYBOOK.md`** (v1.1) — Conversion-pipeline package doctrine plus greenfield variant. Strengths: evidence traceability; numbered forbidden zones; approval gates; common mistakes. Defects: §5.1/§5.3 templates duplicate the questionnaire and FFM (D004); §5.5 authorship statement contradicts Blueprint/ARCHITECT (D005); "8 supervised phases" vs FFM's 00–07 (D008); §10/§13 example and doc paths resolve only project-side (D010, D011). **NEEDS ATTENTION.**

**`02_PIPELINE_AGENTS/RECON_QUESTIONNAIRE.md`** (v0.5, "Active (living)") — The executable ground-truth instrument. Strengths: Section 0 sweep; Q3.4 nuance; stable section IDs (retired numbers never reused); report format; lessons backlog with a promotion rule. Defects: report format lacks Sections 11/12 (S006); FFM-specific vocabulary ("SP5," "Cluster 2") is tribal (D008 adjacent). Dependencies: ←13, the most-referenced doc. **STRONG.**

### 03_BUILD_METHODOLOGY

**`03_BUILD_METHODOLOGY/APP_FACTORY_SKILLS_PLAYBOOK.md`** (v1.1) — Skill-authoring constitution. Strengths: two-file contract; Plan Mode and override protocol defined; eight named anti-patterns; launch-CWD rule. Defects: "Generals" audience term (D007); §7 `_SKILLS/` library vs §14 repo-side instances vs the Hub hosting one skill (D011). **STRONG.**

**`03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md`** (v1.0) — Backend Integration Module doctrine. Strengths: four seats with chain of custody; freeze rule; DRAFT-until-stamped; per-module failure policy; seams and kill switches; Definition of Done. Defects: Engineer completion package absent (D015); git-zero conflicts with FFM (D016); Architect "binding verdicts" rely on a seat name that is ambiguous elsewhere (D007). **STRONG.**

**`03_BUILD_METHODOLOGY/BUG_FIX_PLAYBOOK.md`** (v1.0) — FIX lifecycle. Strengths: reproduce-before-repair; mechanism rule; regression protection at the cheapest layer; environment parity; FIX anatomy; field case studies. Defects: none material; DevOps seat unnamed (D017). **STRONG.**

**`03_BUILD_METHODOLOGY/FEAT_PLAYBOOK.md`** (v1.0) — Feature Module deltas. Strengths: correct Factory-level inheritance; launch conditions; v1-now/v2-seeded; no-weakened-assertions law. Defects: none. **STRONG.**

**`03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md`** (v1.2) — FFM authoring manual. Strengths: four-role pattern with handoff discipline; anatomy and reusability matrix; §7 authoring sequence with recon Step 0; Gate M; stumbles; boot prompts; skeleton tree. Defects: third APP_BRIEF/UI_SPEC template (D004); "Phase" reused for skill steps and roadmap phases; §20 file set vs §12 (D008); `current_app/` vs `CURRENT_APP/` casing (§6 vs §1); worked examples off-Hub (D011); §16 project-side handbook path (D010); Engineer deploys (D016); copy-forward of reusable parts with no return path (R4). Dependencies: ←9. **NEEDS ATTENTION** (strong content; the vocabulary and template issues are cross-file).

**`03_BUILD_METHODOLOGY/FRONTEND_BUILD_PHASE_PLAYBOOK.md`** (v1.2.2) — Six-stage frontend execution. Strengths: §1.5 doctrine refresh; §1.6 Kit Audit; Stage 2 pre-write check; Gate M with the RUN_002 lesson; Lesson 10 desktop-frame check; §12 KIPs. Defects: §9 QA anchors stale (D025); Stage 6 Engineer deploys (D016); "root CLAUDE.md forbidden zone" pointer (D018). **STRONG** with two anchor fixes.

**`03_BUILD_METHODOLOGY/FRONTEND_FIRST_PLAYBOOK.md`** (v1.1.3) — When and why frontend-first. Strengths: §0 Kit Audit; §2 exclusions (ledgers, compliance); service-layer law; §14 relocation note. Defects: §13 Pre-Write Check remains duplicated in FBP Stage 2 despite the relocation note (R1); §4 cites a project-specific `CYBERBUGS_DATA_CONTRACT.md`; "stakeholders" as a seat (D007). **STRONG.**

**`03_BUILD_METHODOLOGY/QA_PLAYBOOK.md`** (v1.1) — The QA seat. Strengths: separation law; claim package; source-of-truth order; evidence classes; finding classification; verdict model; Gate Q/Gate D checklists; final environment reset; anti-patterns; ten field lessons. Defects: §6 package has no producer and §20 artifacts have no home (D015); seat holder and activation undefined (S010); "DevOps / Deployment Operator" seat unowned (D017). **STRONG.**

**`03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md`** (v2.1) — Testing bible. Strengths: ten principles; four layers; diagnostic principles; backend appendices; companion artifacts; gotchas. Defects: env-var name drift (D027); Part 5 says SECURITY_FINDINGS lives "at project root in `agent_docs/`" (two locations in one sentence); §5.1 "git-tag the commit" has no actor (D016). **STRONG.**

### 04_REFERENCE_MANUALS

**`04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md`** (v1.1) — Service-layer law and integration patterns. Strengths: Kit Exception at §1; wire-format conventions; proxy pattern; webhook idempotency. Defects: error template leaks upstream text and "degrade for any fetch" (D022); duplicate §10 (D029); GHL/Socket.IO fossils (§12–§13). **NEEDS ATTENTION.**

**`04_REFERENCE_MANUALS/APP_ARCHITECTURE_MANUAL.md`** (v1.3) — Next.js App Router reference. Strengths: de-pinned versions; §11 co-location; §12 server/client boundary; proxy-vs-middleware note. Defects: §2 `authServices.ts`; §4 client-gated layout with `w-64 hidden md:block`; §10 metadata role check (D001, D021); no theming section despite three docs citing "§Theming Files" (D024). **MATERIAL REVISION NEEDED** (three sections).

**`04_REFERENCE_MANUALS/AUTH_MANUAL.md`** (v1.4) — Auth authority. Strengths: §0 anti-authService doctrine; Key Principle 5; "Where Roles Live"; the Navbar Law. Defects: §12–§14, Summary, registration flow (D001); cookie `httpOnly` (D030); `src/middleware.ts` vs `proxy.ts`; "Full code-sample resync vs the kit = queued" has been queued since v1.3. **MATERIAL REVISION NEEDED.**

**`04_REFERENCE_MANUALS/DATABASE_MANUAL.md`** (v1.1) — Supabase schema doctrine. Strengths: one role doctrine; RLS policy from `user_roles` with the forbidden variant removed; schema-first-vs-frontend-first note. Defects: two versioned prose refs (D002); §5 service-role sample bypasses the kit's `createAdminClient` (Kit Exception adjacent); §8 manual `User` type carries `role` (example vs §2 principle, minor). **STRONG.**

**`04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md`** (v1.1) — One-time payments. Strengths: scope declaration; Order-First pattern; webhook signature verification; security checklist. Defects: §3 client-trusted totals and leaked Stripe errors (D019); §7 store mismatch with STATE (D026). **MATERIAL REVISION NEEDED** (§3).

**`04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md`** (v1.2) — Zustand doctrine. Strengths: three-layer model; Division of Labor hard rule; selector and hydration patterns. Defects: §1 table and §8 auth store contradict §1's own hard rule (D001); §6 checkout template vs ECOM (D026). **NEEDS ATTENTION.**

**`04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md`** (v1.1) — Recurring billing. Strengths: money-truth model; RBAC ⊥ subscriptions; upgrade path; polling pattern; the only deployment recipe in the corpus (§13). Defects: env-var naming (D027). **STRONG.**

### 05_DESIGN_SYSTEM

**`05_DESIGN_SYSTEM/COMPONENT_REGISTRY.md`** (v1.1) — Primitive lookup. Strengths: decision tree; when-NOT-to-use clauses; KIP process. Defects: §7 "sidebars become persistent at md" vs AppShellPage `xl` (D021); `dark:bg-zinc-800` convention (D023); `STARTER_KIT_FEEDBACK.md` and `KIT_PROPOSALS_ARCHIVE.md` unlocated (D011); §11 project-side path (D010). **NEEDS ATTENTION.**

**`05_DESIGN_SYSTEM/GLOBAL_DESIGN_SYSTEM_HANDBOOK.md`** (v1.1) — The design contract. Strengths: canonical token set; role identity tokens; theming method; §3.4 "reconcile the kit"; deliverables and workflow. Defects: none material. **STRONG.**

**`05_DESIGN_SYSTEM/THEME_LIBRARY.md`** (v1.2) — Theme catalog. Strengths: value-set model; add-a-theme process; per-tenant rule. Defects: cross-refs use `agent_docs/APP_FACTORY/design-system/…` paths (D010). **STRONG.**

**`05_DESIGN_SYSTEM/THEMING_MANUAL.md`** (v1.2) — Token architecture. Strengths: tokens-before-pixels; entry-stylesheet portability rule; TW3/TW4 fork; Phase 0/1 discipline. Defects: five dangling section anchors in §0/§7/§10 (D024). **NEEDS ATTENTION** (anchors only).

**`05_DESIGN_SYSTEM/TOKEN_FILE.md`** (v1.2) — Reference token values. Strengths: explicit "reference, not live" role; AA-computed role tokens; usage rules; migration task. Defects: none. **STRONG.**

**`05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md`** (v1.4) — UI/UX operating standard. Strengths: Rule Zero and Rule Zero-B at the top; forbidden patterns enumerated; §10 advanced patterns. Defects: three sidebar examples violate Rule Zero (D021); §10.5 and `Main` example violate Rule Zero-B, §10.8 1150px breakpoint (D023); Rule Zero-B cross-ref to a non-existent APP_ARCHITECTURE section (D024); versioned filename ref in Lesson 9 (D002); "Suggestions for Improvement" and "Questions & Discussion Points" residue (S007). **MATERIAL REVISION NEEDED** (examples), Rule Zero text itself is STRONG.

### Repository infrastructure

**`MANIFEST.md`** (v1.0) — Doc index and dependency map. Strengths: canonical name→path mapping; ← blast-radius table; undeclared-deps appendix. Defects: count 29 vs 31; stale header; stale appendix (D009); cites a draft as its spec and a tag that does not exist (D010). **NEEDS ATTENTION.**

**`CHANGELOG.md`** (v1.0) — Gate-ledger change feed. Strengths: one line per bump with origin IDs. Defects: ongoing-entries table has no header row; header not bumped (D009). **NEEDS ATTENTION** (cosmetic).

**`_ARCHIVE/README.md`** (v1.0) — Snapshot rule and bump procedure. Strengths: clear three-step dance. Suggestions: archive start date (S014); Version History ordering (S013). **STRONG.**

**`lints/README.md`, `lints/run_all.py`, `lints/lint_common.py`, `lints/encoding_lint.py`, `lints/retired_terms_lint.py`, `lints/versioned_refs_lint.py`, `lints/header_lint.py`, `lints/.gitignore`** — The four watchdogs. Strengths: well-scoped, MANIFEST-driven false-positive guard, honest-history exemptions. Defects: failing at baseline and merged over (D002); no anchor or path lint (S003). Note: `lint_common.py` treats an unmatched fence toggle as state, so an odd number of ``` in a doc inverts fence detection for the rest of the file (observed as a risk, not a hit). **NEEDS ATTENTION** (as a control, not as code).

**`.github/workflows/doctrine-lint.yml`** — Runs lints on push/PR to main. Defect: exit 1 is not treated as blocking by process (D002); does not run on feature branches (S003). **NEEDS ATTENTION.**

**`README.md`** (root) — Two lines. Suggestion: entry point (S001). **NEEDS ATTENTION.**

**`CLAUDE.md`** (root, v3.1) — Claude Code configuration for this repo: Plan Mode protocol, response logging, disaster recovery, Karpathy behaviors, TDD flow, factory doc reading order, FastAPI/ADK rules. Authority: **AMBIGUOUS** — not in MANIFEST, lint-exempt, yet cited as "root CLAUDE.md forbidden zone" by FFM and FBP. Defects: D006 (FILE_TREE reading order), D018 (competing Karpathy copy, Plan Mode home); contains Kit-irrelevant stack rules. **NEEDS ATTENTION** pending the human decision on its status.

**`RECOVERY.md`** — Session recovery pointer. Bookkeeping; not doctrine. Examined for context only. **OUT OF DOCTRINE SCOPE.**

### `_SKILLS/factory-docs-update/` (v0.3-DRAFT)

**`CLAUDE.md`** — Skill doctrine D1–D16. Strengths: every rule cites its incident; D3 routing gate; D7 dance; D9 lint conduct; D13 no invention; D15 Hub law over cargo; D16 triage. Defects: D5 git ownership differs from module doctrine without cross-reference (D016). **STRONG.**
**`SKILL.md`** — Six phases, four stop gates, worked example. Strengths: exact presentation shapes; mid-flight checkpoint. Defects: `allowed-tools` lists `github-mcp` (not a tool name; cosmetic). **STRONG.**
**`README.md`** — Operator runbook. Defects: "files just need to be in the root" vs Step 3 `_INBOX/` (D028); codifies merge-over-red (D002). **NEEDS ATTENTION.**
**`decision-trees/route-selection.md`**, **`references/TOOL_ROUTING.md`** — Routing logic and war story. **STRONG.**
**`references/ANTI_PATTERNS.md`** — AP-1..11. Defect: AP-11 still says root (D028). **NEEDS ATTENTION** (one line).
**`templates/LESSONS_LEARNED.md`** — Defect: header says clone root (D028). **NEEDS ATTENTION** (one line).
**`templates/RIPPLE_MAP.md`** — Strengths: consistency-ripples table; write-load tally. Suggestion: add "inbound anchors verified" (D025). **STRONG.**

### `_OTHERS/`

**`_OTHERS/DOCTRINE_HUB_DESIGN_v0_1.md`** — Draft design of the Hub, sync loop, releases. Authority: **AMBIGUOUS** — DRAFT "awaiting approval" yet cited by MANIFEST as "spec §2.6" and by `_ARCHIVE/README` as the rule's source. Disposition: promote §2.3–§2.6 to live doctrine or stop citing it (D010). **NEEDS ATTENTION.**
**`_OTHERS/MASTER_DOC_LIST_v1_0_FINAL.md`** — Seed plan from 2026-07-04. Historical; superseded by MANIFEST. Note: the seed plan's `_ARCHIVE` list of six superseded copies was never realized (S014). **OUT OF LIVE SCOPE — historical.**

### `_AUDIT/` process records (examined)

**`_AUDIT/DOCTRINE_PROMOTION_2026-08-04_NAVBAR_SAGA.md`** — ENCODED pack (PR #8). Evidence value: shows the pack→Hub process; Entry 4's "§9/§10" anchors are the source of D025; landing instruction 2 "filename-carries-version" is the cargo convention D15 translates. **EVIDENCE — consistent with the process.**
**`_AUDIT/FINALIZATION_REPORT_2026-08-10_FACTORY_MODULE_DOCTRINE.md`** — ENCODED report (PR #10). Evidence value: names the Architect seat as "Jarvis (Fable 5)"; confirms APP_REGISTRY remains proposed. **EVIDENCE.**

### `agent_docs/RESPONSES/` (six run logs, 2026-08-10)

Phase 1 triage, Phase 2 ripple map, Phase 3 route, Gate 4 precheck, Phase 5 handoff, run summary. Evidence value: demonstrate the update skill end to end with evidence labels; they are also the source of three findings — the "27 → 29" count error (D009), "known stragglers … does not block merge" (D002), and the parked Blueprint-router concern (D020). Suggestion: the run summary's six refinement notes (Version History ordering, PR-number discovery, kit-reference resolution, unexplained-tree STOP, em-dash gotcha, fractional insert) belong in the skill's v0.4, not only in a log (R3). **EVIDENCE — STRONG as records.**

## 13. COVERAGE MANIFEST

Every file discovered at baseline 0a787cb (110 tracked) plus the 6 untracked files present in the working tree. Status values: **EXAMINED** (read in full and reviewed), **EXAMINED — header only** (classified by header; content out of live scope), **NOT EXAMINED — reason**, **OUT OF SCOPE — reason**. No file was omitted. Classification per packet §7 is given in brackets.

**Repository root and infrastructure**

| File | Status | Class |
|---|---|---|
| `README.md` | EXAMINED | repository infrastructure |
| `CLAUDE.md` | EXAMINED | agent instructions — authority AMBIGUOUS (see D018) |
| `MANIFEST.md` | EXAMINED | repository infrastructure (index) |
| `CHANGELOG.md` | EXAMINED | repository infrastructure (ledger) |
| `RECOVERY.md` | EXAMINED (context only; bookkeeping) | non-doctrine |
| `.github/workflows/doctrine-lint.yml` | EXAMINED | repository infrastructure |
| `lints/README.md` | EXAMINED | technical reference / infrastructure |
| `lints/run_all.py` | EXAMINED (source read; executed read-only) | infrastructure |
| `lints/lint_common.py` | EXAMINED | infrastructure |
| `lints/encoding_lint.py` | EXAMINED | infrastructure |
| `lints/header_lint.py` | EXAMINED | infrastructure |
| `lints/retired_terms_lint.py` | EXAMINED | infrastructure |
| `lints/versioned_refs_lint.py` | EXAMINED | infrastructure |
| `lints/.gitignore` | EXAMINED | infrastructure |

**01_CONSTITUTION** — `APP_FACTORY_BLUEPRINT.md`, `SOFTWARE_FACTORY_PLAYBOOK.md`, `STARTER_KIT_HANDBOOK.md`: all **EXAMINED** [authoritative doctrine, Tier 1].

**02_PIPELINE_AGENTS** — `ARCHITECT_PLAYBOOK.md`, `ARCHITECT_QUESTIONNAIRE.md`, `DESIGNER_PLAYBOOK.md`, `ENGINEER_PLAYBOOK.md`, `HANDOFF_PACKAGE_PLAYBOOK.md`, `RECON_QUESTIONNAIRE.md`: all **EXAMINED** [authoritative doctrine, Tier 2].

**03_BUILD_METHODOLOGY** — `APP_FACTORY_SKILLS_PLAYBOOK.md`, `BIM_PLAYBOOK.md`, `BUG_FIX_PLAYBOOK.md`, `FEAT_PLAYBOOK.md`, `FFM_PLAYBOOK.md`, `FRONTEND_BUILD_PHASE_PLAYBOOK.md`, `FRONTEND_FIRST_PLAYBOOK.md`, `QA_PLAYBOOK.md`, `TESTING_PLAYBOOK.md`: all **EXAMINED** [authoritative doctrine, Tier 3].

**04_REFERENCE_MANUALS** — `API_AND_SERVICES_MANUAL.md`, `APP_ARCHITECTURE_MANUAL.md`, `AUTH_MANUAL.md`, `DATABASE_MANUAL.md`, `ECOMMERCE_AND_PAYMENTS_MANUAL.md`, `STATE_MANAGEMENT_MANUAL.md`, `STRIPE_SUBSCRIPTIONS_PLAYBOOK.md`: all **EXAMINED** [technical reference doctrine, Tier 4].

**05_DESIGN_SYSTEM** — `COMPONENT_REGISTRY.md`, `GLOBAL_DESIGN_SYSTEM_HANDBOOK.md`, `THEME_LIBRARY.md`, `THEMING_MANUAL.md`, `TOKEN_FILE.md`, `UI_UX_BUILDING_MANUAL.md`: all **EXAMINED** [design doctrine, Tier 5].

**_ARCHIVE** (superseded snapshots)

| File | Status |
|---|---|
| `_ARCHIVE/README.md` | EXAMINED [repository infrastructure] |
| `_ARCHIVE/.gitkeep` | OUT OF SCOPE — empty placeholder |
| `_ARCHIVE/AUTH_MANUAL_v1_3.md` | EXAMINED — header only; superseded snapshot, not live doctrine |
| `_ARCHIVE/BUG_FIX_PLAYBOOK_v0_1.md` | EXAMINED — header only; superseded snapshot |
| `_ARCHIVE/FRONTEND_BUILD_PHASE_PLAYBOOK_v1_2_1.md` | EXAMINED — header only; superseded snapshot |
| `_ARCHIVE/QA_PLAYBOOK_v0_1.md` | EXAMINED — header only; superseded snapshot |
| `_ARCHIVE/SOFTWARE_FACTORY_PLAYBOOK_v1_2.md` | EXAMINED — header only; superseded snapshot |
| `_ARCHIVE/STATE_MANAGEMENT_MANUAL_v1_1.md` | EXAMINED — header only; superseded snapshot |

All six snapshot headers carry the version their filename claims; the archive-naming rule is honored.

**_AUDIT** (audit / evidence material)

| File | Status |
|---|---|
| `_AUDIT/DOCTRINE_PROMOTION_2026-08-04_NAVBAR_SAGA.md` | EXAMINED [evidence — ENCODED process record] |
| `_AUDIT/FINALIZATION_REPORT_2026-08-10_FACTORY_MODULE_DOCTRINE.md` | EXAMINED [evidence — ENCODED process record] |
| `_AUDIT/GRAND_AUDIT_SUMMARY.md` | NOT EXAMINED — independence rule: a prior model review of this same corpus |
| `_AUDIT/FINDINGS_LOG.md` | NOT EXAMINED — independence rule: prior-review findings |
| `_AUDIT/RECONCILIATION_REPORT.md` | NOT EXAMINED — independence rule: prior-review reconciliation |
| `_AUDIT/RECON_WAVE0.md` | NOT EXAMINED — independence rule: prior-review recon |
| `_AUDIT/REVIEW_001_AI_APP_FACTORY_BLUEPRINT_v2_0.md` through `_AUDIT/REVIEW_027_COMPONENT_REGISTRY_v1_1.md` (27 files: REVIEW_001, 002, 003, 004, 005, 006, 007, 008, 009, 010, 011, 012, 013, 014, 015, 016, 017, 018, 019, 020, 021, 022, 023, 024, 025, 026, 027) | NOT EXAMINED — independence rule: prior per-document model reviews of this corpus |

**_OTHERS** — `DOCTRINE_HUB_DESIGN_v0_1.md`: **EXAMINED** [design draft — authority AMBIGUOUS]; `MASTER_DOC_LIST_v1_0_FINAL.md`: **EXAMINED** [historical seed plan].

**_SKILLS/factory-docs-update** — `CLAUDE.md`, `README.md`, `SKILL.md`, `decision-trees/route-selection.md`, `references/ANTI_PATTERNS.md`, `references/TOOL_ROUTING.md`, `templates/LESSONS_LEARNED.md`, `templates/RIPPLE_MAP.md`: all **EXAMINED** [skills / agent instructions — not in MANIFEST; authority AMBIGUOUS relative to the governed set].

**agent_docs/RESPONSES** — `response_2026-08-10_192235_phase1-intake-triage.md`, `response_2026-08-10_194109_phase2-ripple-map.md`, `response_2026-08-10_194500_phase3-route-decision.md`, `response_2026-08-10_200500_gate4-precheck.md`, `response_2026-08-10_201500_phase5-pr-handoff.md`, `response_2026-08-10_203000_run-summary.md`: all **EXAMINED** [evidence — run logs of the update skill].

**Session logs**

| File | Status |
|---|---|
| `session_2026-07-07.md`, `session_2026-07-08.md`, `session_2026-07-12.md` | NOT EXAMINED — bookkeeping for the Grand Audit waves; likely to contain prior-review material (independence rule) |
| `session_2026-08-05.md`, `session_2026-08-10.md` | NOT EXAMINED — bookkeeping; run content is covered by the ENCODED records and RESPONSES logs above |
| `session_2026-09-13.md` (untracked) | EXAMINED — this run's bookkeeping; not doctrine |

**Untracked review workspace (`fable-review/run-001/`)**

| File | Status |
|---|---|
| `packets/FABLE_FACTORY_DOCTRINE_REVIEW_PACKET_001.md` | EXAMINED — the governing packet for this run |
| `reviews/FABLE_FACTORY_DOCTRINE_REVIEW_001.md` | OUT OF SCOPE — this report |
| `telemetry/RUN_001_LEDGER.md` | OUT OF SCOPE — this run's telemetry |
| `reviews/SOL_REVIEW_OF_FABLE_001.md` | OUT OF SCOPE — reserved for the Sol seat; not opened (0 bytes at start) |
| `reviews/FINAL_DISPOSITION.md` | OUT OF SCOPE — reserved for Tony; not opened (0 bytes at start) |

**Astra material:** none exists on this branch by filename; nothing Astra-named was opened. No file could not be read or parsed.

Totals: 110 tracked files — 72 EXAMINED (including 6 header-only archives), 36 NOT EXAMINED (all under the independence rule or as prior-session bookkeeping), 2 OUT OF SCOPE (`.gitkeep`, and none else tracked); 6 untracked — 2 EXAMINED, 4 OUT OF SCOPE.

## 14. AMBIGUITIES / UNKNOWNS

Surfaced rather than guessed. Each is stated with the readings the corpus supports.

1. **Who is "the Architect"?** AI chat seat ("Jarvis") in FFM, BIM, and the skill; the human in SFP §1, the Karpathy Protocol, and HANDOFF §3. AMBIGUOUS (D007).
2. **Is the Engineer one seat or two?** Claudy everywhere except the Blueprint's Phase 3/4, where an Engineer "prompts Claudy." AMBIGUOUS (D014).
3. **Who holds the QA seat, and how is it booted?** Not stated anywhere. UNKNOWN (S010).
4. **Who holds the DevOps seat and how are deployments, promotions, and rollbacks performed?** UNKNOWN (D017).
5. **Is root `CLAUDE.md` Factory doctrine?** Cited as a source of truth by FFM and FBP; outside MANIFEST and lints. AMBIGUOUS (D018).
6. **Is `DOCTRINE_HUB_DESIGN_v0_1.md` the distribution spec?** MANIFEST and `_ARCHIVE/README` cite it; it says DRAFT awaiting approval. AMBIGUOUS (D010).
7. **Where do Hub docs land in a project?** Four paths in live docs. AMBIGUOUS (D010).
8. **Where do skills live?** `_SKILLS/` library (Skills Playbook §7) vs repo-side instances (§14) vs one skill in the Hub. AMBIGUOUS (D011).
9. **Where are the canonical worked examples?** Project-repo paths only; no repo or tag named. UNKNOWN from the Hub alone (D011).
10. **Which APP_BRIEF and UI_SPEC template binds a greenfield FFM?** Three each. AMBIGUOUS (D004).
11. **Who drafts UI_SPEC in greenfield?** Majority: Architect drafts, Designer revises; Blueprint and ARCHITECT_PLAYBOOK disagree. AMBIGUOUS (D005).
12. **When is the greenfield DATA_CONTRACT completed, and by whom?** "Engineer is the author of record … step 4 ships the contract shell." AMBIGUOUS (D014).
13. **May the Engineer deploy or commit?** Yes in FFM/FBP, no in BIM/FIX, yes (git only) in Hub runs. AMBIGUOUS (D016).
14. **Which breakpoint is the Gate M threshold for the app rail?** `md`, `lg`, or `xl` depending on the doc. AMBIGUOUS (D021).
15. **`httpOnly` for session cookies: true or false?** Opposite instructions. AMBIGUOUS pending disk (D030).
16. **Is `FILE_TREE.md` a required artifact?** Required by two docs, produced by none. AMBIGUOUS (D006).
17. **Which is canonical for agent conduct: ENGINEER §15 or root CLAUDE.md?** Both claim it. AMBIGUOUS (D018).
18. **What does "Active (living)" status permit for RECON_QUESTIONNAIRE?** Not defined against the bump procedure. UNKNOWN (minor).
19. **What is the retention policy for run logs (`agent_docs/RESPONSES`)?** 31 were deleted by operator ruling on 2026-08-10; no rule. UNKNOWN (R9).
20. **Does the kit's `useAuthStore` expose derived flags today?** The handbook (2026-06-28) says yes; RECON (from the June run) says the flags were absent; AUTH's store sample is marked legacy. Disk-dependent; UNKNOWN from the corpus (D001 adjacent).
21. **Is the lint failure on `main` currently red in CI, or has CI never run green?** The workflow runs on main; the process merges over red; the review did not query GitHub. UNKNOWN; evidence limited to local execution (D002).

## 15. FINAL FACTORY HEALTH ASSESSMENT

**Score: 3 of 5 — Functional, but meaningful gaps exist.**

The Factory's operating model is real and mostly executable: a cold, competent agent can run a BIM, a FIX, a FEAT, a QA engagement, or a Hub doctrine update from the written playbooks alone, because those documents name their seats, gates, artifacts, evidence rules, and stop conditions. That is the achievement of the last two months, and it should be protected during corrective work.

The same agent cannot run the front half of the Factory cold. The constitution does not know the QA seat or the module types, the Blueprint and the Architect's own playbook disagree with four other docs about what the Architect produces, three different APP_BRIEF templates claim to be the brief, and no document says where the recon skill, the examples, or a project's copy of the doctrine actually live. These are not deep design failures. They are the predictable lag of founding documents behind field practice, and they are fixable with pointers and one glossary.

Two content defects are severe enough to warrant fixing before anything else: the auth authority's own later sections and the constitution's Phase 7 still teach authorization patterns the Factory greps for as smells, and the payments manual's central sample trusts client prices while saying it does not. Both are the kind of drift the Factory built lints and QA to catch, and both survived because the lints are red and merged over, and because examples sit far from the rules that govern them.

What to preserve: the recon-first law, the Kit Exception, the QA separation law and verdict model, module doctrine with correct inheritance, the design-token contract, the testing principles, and the four-step update dance with its logged runs.

What genuinely requires correction: the two BLOCKERs, the lint gate, the constitution's lag, the duplicated templates, the seat and lifecycle vocabularies, and the distribution mechanism.

What could materially be improved: a Hub entry point, a gate registry, anchor and path lints, MANIFEST generation, a deployment playbook, and a precedence clause.

With the Top 10 executed, this corpus would score 4. Nothing found here argues for restructuring the repository, retiring a tier, or rewriting a playbook wholesale.

---

**Review complete.** Written incrementally; all sections present. Telemetry: `fable-review/run-001/telemetry/RUN_001_LEDGER.md`.
