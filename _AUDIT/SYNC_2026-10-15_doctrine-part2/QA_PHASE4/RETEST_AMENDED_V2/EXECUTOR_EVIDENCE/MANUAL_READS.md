# Independent manual reads — candidate 8dff354937bc7baf739370a9886497d9d5359186

Seat: Codex QA Executor; fresh conversation. Quotes below are from the pinned git archive. Searches are locators, not semantic proof. Full candidate documents are in RAW/candidate/.

## R1 ownership
Architect authors DATA_CONTRACT in conversion and greenfield; Designer authors UI_SPEC; Architect reconciles. Conversion uses Brain Drain pre-authorship; greenfield uses approved APP_BRIEF before Design. Router remains. E373–E380 each occurs once, old spans absent. FILE_TREE remains optional. Historical HANDOFF 1.1 statement is retained only in its Version History. BIM Engineer-finalized wording is limited by §8 to factual synchronization of pre-approved criteria, not authorship of success conditions. Broad map-query hits include negative examples, artifact mentions, historical versions and unrelated OUTSIDE/LOCKED vocabulary; full dispositions are recorded.

### 02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:133

```text
133: Before the Engineer can build, it needs these inputs. **Which package you receive depends on the pipeline** — route first via APP_FACTORY_BLUEPRINT, "Which Pipeline Am I In?".
134: 
135: ### Greenfield Inputs (Kit Track: Architect → Designer → Engineer)
136: 
137: The approved interface type determines required design inputs. A visual interface requires its approved UI_SPEC, token/style decisions and HTML/PNG references. A nonvisual backend or CLI explicitly records those inputs as NOT APPLICABLE and supplies its approved data/API/command contract, invocation examples and receiving checklist. Missing required input is not NOT APPLICABLE.
138: 
139: The Designer's handoff package (DESIGNER_PLAYBOOK §10):
140: 
141: | Input | Source | Why Required |
142: |-------|--------|--------------|
143: | **APP_BRIEF.md** (approved) | Architect | Scope, constraints, tech stack |
144: | **Token file** (`globals.css`/`globals.scss` + Tailwind map) | Designer | **THE PRIMARY DESIGN DELIVERABLE** — the executable contract the build inherits |
145: | **Style tile** (HTML + PNG) | Designer | The locked visual system reference |
146: | **Screen artifacts** (HTML + PNG, the locked set) | Designer | HTML to build from; PNG as the QC target |
147: | **UI_SPEC.md** (approved) | Designer; Architect reconciles assembly | Screens, flows, gating logic, states |
148: | **Component manifest** | Designer | Primitives per screen + KIPs to build first |
149: 
150: What the Engineer actually needs from that package (Designer §10 doctrine):
151: 
152: - **HTML to build from** (structure + token usage, verbatim)
153: - **PNG to verify against** (the QC target)
154: - **Tokens to inherit** (the contract — no reinterpretation)
155: - **Locked screen intent** (what each control does) and **gating logic** with dependency order
156: 
157: > ⛔ **Screenshots are NOT the greenfield visual input** — that was the F-026 handshake mismatch. The token file + HTML/PNG set is the package. Screenshots are the CONVERSION pipeline's visual ground truth.
158: 
159: ### Conversion Inputs (Brain Drain → 4-File Package → Engineer)
160: 
161: Per HANDOFF_PACKAGE_PLAYBOOK (the conversion pipeline's package doctrine):
162: 
163: | Input | Source | Why Required |
164: |-------|--------|--------------|
165: | **APP_BRIEF.md** | Operator/Architect | Scope, hard gates, success criteria |
166: | **DATA_CONTRACT.md** (PRE-AUTHORED) | Architect, from Brain Drain evidence | Types, service contracts, mock requirements |
167: | **UI_SPEC.md** | Designer, from approved contracts and conversion evidence; Architect reconciles | Screen-by-screen behavior and primitive mapping |
168: | **`_project/CLAUDE.md`** | Architect | Project spine: doctrine, forbidden zones, stack |
169: | **`_design/` screenshots** | Source app | The canonical visual reference (conversion only) |
170: | **`_extraction/` Brain Drain docs** | Extractor | The evidence base every package claim traces to |
171: 
172: ### DATA_CONTRACT Ownership (know which run you're in)
173: 
174: > **CONVERSION:** the Architect **PRE-AUTHORS** `DATA_CONTRACT.md` from Brain Drain evidence — the Engineer consumes and honors it.
175: > **GREENFIELD:** the Architect authors `DATA_CONTRACT.md` from the approved APP_BRIEF before Design. The Designer authors UI_SPEC; the Architect reconciles the assembled package. The Engineer consumes the approved contracts. The canonical DATA_CONTRACT template remains in §12.
176: > The Architect authors `DATA_CONTRACT.md` in both runs; only the evidence base and moment differ: conversion uses Brain Drain evidence and is pre-authored; greenfield uses the approved APP_BRIEF before Design. Router: APP_FACTORY_BLUEPRINT, "Which Pipeline Am I In?".
177: 
178: ### Pre-Flight Checklist
179: 
180: Before starting, Engineer confirms:
181: 
182: - [ ] Recon Report is current for this repo (Phase 0 — §2)
183: - [ ] Pipeline identified (conversion vs greenfield)
184: - [ ] APP_BRIEF is APPROVED
185: - [ ] UI_SPEC is APPROVED
186: - [ ] Greenfield: token file + style tile + screen HTML/PNG + component manifest received
187: - [ ] Conversion: 4-file package approved; `_extraction/` + `_design/` present
188: - [ ] Gating logic is documented
189: - [ ] Human checkpoints are identified
190: - [ ] Approved stack reconciled with current Recon evidence; any conflict has an attributable Director ruling
```


### 02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:734

```text
734: ## 12. DATA_CONTRACT Template
735: 
736: > **Ownership:** the Architect authors DATA_CONTRACT before Design, using the canonical template below. Conversion includes the approved extraction evidence. The Designer authors UI_SPEC; the Architect reconciles the assembled package. Engineering consumes the approved revisions; it does not create missing contracts during implementation.
737: 
738: The Architect prepares this contract before Design. Engineering implements the approved contract and records factual changes only through its authorized amendment and handoff lanes.
```


### 01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md:51

```text
51: 3. **If greenfield: what is the design ground truth?** Wireframes / Designer output → goes in `_design/`. Brand tokens only → the style tile must land before screens. Nothing yet → Designer work blocks; surface to operator.
52: 
53: Hybrids (a greenfield build that inherits data shapes from a related repo's extracts) are treated structurally as GREENFIELD, with `_extraction/` repurposed for the related-repo evidence.
54: 
55: **Artifact ownership:** the Architect owns DATA_CONTRACT before Design. The Designer owns UI_SPEC. The Architect reconciles the assembled package and Engineering consumes its approved revision. Conversion evidence informs those contracts; greenfield does not transfer authorship to Engineering. FILE_TREE is optional; implementation structure and boundaries must remain explicit in the approved package.
56: 
```


### 02_PIPELINE_AGENTS/ARCHITECT_PLAYBOOK.md:80

```text
80: 
81: ### 🔍 Recon Mode — Mandatory Before Authoring (Non-Negotiable)
82: 
83: > **This is the Architect's Plan Mode.** Plan Mode keeps the Engineer from coding blind. Recon Mode keeps the Architect from authoring blind. It is not optional, and it comes before every other input below.
84: 
85: **Before preparing or reconciling any project artifact, the Architect requires a current Recon Report for the actual repository state. The Architect owns APP_BRIEF, DATA_CONTRACT and assembly; the Designer owns UI_SPEC.**
86: 
87: Why this is law, not preference: docs drift. Starter-kit handbooks, prior APP_BRIEFs, and session logs make claims about disk that go stale. An Architect who authors against a stale doc produces a *correct artifact built on wrong data* — and the cost surfaces later as conflict after conflict at the Engineer's build gate. (This is the lesson of the Cyber Pharma v1 Phase 1 run: six confirmed handbook bugs, stale env names, a year-old cross-project fossil — all of which a recon catches on day one.)
88: 
```


### 02_PIPELINE_AGENTS/DESIGNER_PLAYBOOK.md:62

```text
62: 
63: ### What the Designer Does NOT Do
64: 
65: | Not Designer's Job | Belongs To |
66: |--------------------|------------|
67: | Define app scope | Architect Agent |
68: | Write the production app | Engineer Agent / Claudy |
69: | Define DATA_CONTRACT before Design | Architect |
70: | Make product decisions | Human (Tony Stark) |
71: | Invent components the kit can compose | Flag a KIP instead |
72: 
```


### 02_PIPELINE_AGENTS/HANDOFF_PACKAGE_PLAYBOOK.md:251

```text
251: - **Token file** (`globals.css`/`.scss`, all modes) — the PRIMARY design deliverable
252: - **Style tile** — HTML + PNG
253: - **Per-screen HTML + PNG** — Playwright-rendered, light + dark
254: - **Component manifest** (`COMPONENT_MANIFEST.md`)
255: 
256: The Designer owns UI_SPEC. For conversion, extraction evidence and source screenshots inform the specification; for greenfield, the Designer’s token file and screen HTML/PNG establish the visual contract. The Architect reconciles the assembled package before Director approval.
257: 
258: ---
259: 
260: ## 6. Authoring Order
261: 
262: Author the files in this order:
263: 
264: 1. **APP_BRIEF.md FIRST** — scope must be locked before contracts or screens can be specified
265: 2. **DATA_CONTRACT.md SECOND** — data shapes inform what the UI needs to display
266: 3. **UI_SPEC.md THIRD** — screens are built from the data contract
267: 4. **_project/CLAUDE.md LAST** — the spine is informed by the other three
268: 
269: If you author UI_SPEC before DATA_CONTRACT, you'll invent data shapes that don't match the source. If you author CLAUDE.md before the others, you won't know the conventions to encode.
```


### 03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:375

```text
375: **Examples:** The original FFM v1.0 (Cyberize Agentic Automation, May 2026) converted a Streamlit prototype.
376: 
377: **`_design/` contains:** Screenshots of the source app (the canonical visual reference).
378: **`_extraction/` contains:** The 11 Brain Drain extracts from the source repo.
379: **DATA_CONTRACT** is authored: From the Brain Drain `04-TOOL-SYSTEM.md` (API surface).
380: **UI_SPEC** is authored: From the Brain Drain `06-PROMPTS-AND-PERSONA.md` (screen inventory) plus the screenshots.
381: **The "Known Discrepancies" section** is critical: drift between the source app and the desired Next.js version is preserved as documentation, not "fixed" silently.
382: 
383: ### Variant B — Greenfield FFM
384: 
385: **When to use:** No source app exists. The build is greenfield — starting from a starter kit with no prior implementation to mirror.
386: 
387: **Examples:** Cyber Pharma v1 Phase 1 FFM (June 2026) — foundation skeleton with no source app.
388: 
389: **`_design/` contains:** the Designer v2.0 package — token file (PRIMARY), style tile HTML+PNG, per-screen HTML+PNG (Canonical Page Method), component manifest, logos (the visual ground truth replaces source app screenshots).
390: **`_extraction/` contains:** Either (a) data-shape evidence from upstream/related repos that inform what the new build should look like, or (b) a `README.md` documenting "N/A — greenfield, no source to extract."
391: **DATA_CONTRACT** is authored by the Architect before Design, from the approved brief and verified interface/schema evidence.
392: **UI_SPEC** is authored by the Designer from the approved brief, DATA_CONTRACT, screen HTML/PNG and token file; the Architect reconciles the assembled package.
393: **The "Known Discrepancies" section** may not apply or may be very thin.
394: 
395: ### What Differs Between Variants
396: 
397: | Aspect | Conversion FFM | Greenfield FFM |
398: |---|---|---|
399: | Source app exists | Yes | No |
400: | `_design/` contents | Source app screenshots | Designer v2.0 package: token file (PRIMARY) + style tile HTML+PNG + screen HTML+PNG + component manifest |
401: | `_extraction/` contents | 11 Brain Drain docs | Data-shape evidence from related repos OR N/A |
402: | DATA_CONTRACT source | Architect uses approved extraction evidence before Design | Architect uses approved brief and verified interfaces before Design |
403: | UI_SPEC source | Designer uses extraction evidence and screenshots; Architect reconciles | Designer authors from approved contracts and screen HTML/PNG; Architect reconciles |
404: | Known Discrepancies relevance | High | Low / N/A |
405: | Authoring time | Faster (evidence pre-extracted) | Slower (operator decisions take time) |
```


### 03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md:122

```text
122: ## 8. ACCEPTANCE_SPEC.md (mandatory handoff artifact — Factory-level rule, restated)
123: 
124: **The contract handed from Engineering to QA. It is NOT the QA test plan.** Engineering states what it claims complete; QA independently decides how to attack and verify. Exact filename locked: `ACCEPTANCE_SPEC.md`.
125: 
126: **Ownership (precise):** the acceptance criteria are **seeded from the approved module contract — Architect/Operator-defined — before implementation.** The Engineer *maintains and finalizes* the spec at handoff, keeping it synchronized with approved scope, but **may not silently add, remove, weaken, or redefine an acceptance requirement** — any scope change requires approval. The Engineer packages the contract for QA; he does not grade his own paper, and he does not write his own exam either.
127: 
128: Minimum contents:
129: 
130: - Canonical module ID + owning application (slug)
131: - Module objective; in-scope behavior; explicit out-of-scope / forbidden behavior
132: - **Numbered acceptance requirements `AC1, AC2, …`** — testable and observable ("works correctly" and "handles sessions" are banned phrasings). *(Doctrine note: `AC*` is a NEW Factory decision effective with this playbook — the pilot campaign's field record used gate IDs (`X1–X7`, `V*`, `N*`, `P-G*`), which remain the convention for module-internal engineering gates and stay untouched as legacy. Acceptance requirements and gates are related but distinct: a mapping table gates↔ACs in the spec is encouraged. `QA_PLAYBOOK.md` examples to be synchronized at promotion. Never bare `A*` — reserved for recon assumption checklists.)*
133: - Expected observable behavior per requirement; error/failure behavior where relevant
134: - **Environment/setup prerequisites** — migrations, env changes, credentials, permissions, and every manual Coordinator step, called out FIRST (field lesson: a merge whose setup steps live only in a spec nobody opened produces three "broken" features that are actually three locked doors)
135: - Regression expectations — existing behavior that must remain intact
136: - Manual-only acceptance points where automation cannot prove the claim
137: - Known limitations; known follow-up work that does NOT belong to this contract
138: 
139: Timing: the acceptance contract is established at planning, kept synchronized with approved scope during implementation, **finalized at handoff** — never reverse-engineered afterward to justify what got built.
140: 
```

## R2 handoff
The lead instruction gates Operations on QA Lead certification and Director release. The eight-entry tree retains original six entries and adds Architect ACCEPTANCE_SPEC and QAM with engineering handoff, plan, results and certificate. The tree title describes the eventual receiving destination; it does not override the preceding explicit route through independent QA. What Operations Needs and Verbal Brief are byte-identical to parent.

### 02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:1381

```text
1381: ## 17. Handoff Protocol to Operations
1382: 
1383: Every newly authored module includes a complete, module-specific `QAM/` prepared by the Architect from `03_BUILD_METHODOLOGY/_templates/QAM/`. QA Lead owns the reusable playbook and standing requirements. Engineer fills factual engineering records and handoff; QA Executor performs independent Q1 recon and test planning; QA Lead approves the plan; Director releases execution; QA Executor performs Q2 and authorized retest; QA Lead adjudicates and certifies. `QAM_PLAYBOOK.md` owns this packaging and sequence. Existing modules already in flight retain their recorded sequence until an attributable amendment.
1384: 
1385: When code is complete and self-verified, the Engineer hands the candidate and factual QAM engineering handoff to independent QA on the Director-created QA branch; Operations/Deployment receives the package only after QA Lead certification and Director release (see QAM_PLAYBOOK §3 and DEPLOYMENT_PLAYBOOK §3).
1386: 
1387: ### Handoff Package Contents
1388: 
1389: ```
1390: 📦 ENGINEER → OPERATIONS HANDOFF
1391: │
1392: ├── APP_BRIEF.md (from Architect)
1393: ├── UI_SPEC.md (from Designer)
1394: ├── DATA_CONTRACT.md
1395: ├── ACCEPTANCE_SPEC.md (from Architect)
1396: ├── Working Code (tested)
1397: ├── QAM/ (module QA pack: ENGINEERING_HANDOFF, approved plan, results, certificate)
1398: ├── README.md (setup instructions)
1399: └── Deployment Guide
1400: ```
1401: 
1402: ### What Operations Needs
1403: 
1404: | Need | Why |
1405: |------|-----|
1406: | Clear setup instructions | Can deploy without guessing |
1407: | Environment variable list | Knows what to configure |
1408: | Health check endpoints | Can monitor the system |
1409: | Logging configuration | Can debug issues |
1410: | Rollback procedure | Can recover from failures |
1411: 
1412: ### Verbal Brief Template
1413: 
1414: ```
1415: "Operations, here's your brief:
1416: 
1417: PROJECT: [Name]
1418: TYPE: [App Type]
1419: DEPLOYMENT TARGET: [Cloud Run / Vercel / Local]
1420: 
1421: SETUP:
1422: 1. [Step 1]
1423: 2. [Step 2]
1424: 3. [Step 3]
1425: 
1426: ENVIRONMENT VARIABLES:
1427: - [VAR_1]: [Purpose]
1428: - [VAR_2]: [Purpose]
1429: 
1430: HEALTH CHECK: [Endpoint]
1431: 
1432: MONITORING: [What to watch]
1433: 
1434: KNOWN ISSUES: [Any gotchas]
1435: 
1436: Questions?"
1437: ```
1438: 
1439: ---
1440: 
1441: ## Appendix A: Lessons from the Field (Pipeline Track — AI Video Pipeline)
1442: 
1443: ### Real Experience: AI Video Generation Pipeline
1444: 
```


### 03_BUILD_METHODOLOGY/QAM_PLAYBOOK.md:35

```text
35: ## 3. Authority and the five seats
36: 
37: | Seat | Responsibility | Boundary |
38: |---|---|---|
39: | Director | Approves scope/targets and risk decisions; controls credentials, Git, release and destructive authority | Does not have to perform every repeatable UI check |
40: | Architect | Defines frozen acceptance contract, module scope and protections; instantiates QAM from this playbook; resolves contract ambiguity; directs closeout | Does not substitute an engineering-green result for independent QA |
41: | Engineer | Implements approved scope, self-verifies, completes manifest and engineering handoff; repairs only ruled scope | Does not approve the QA plan, fill independent QA results or issue a certificate |
42: | QA Lead | Owns this playbook and standing risks; amends/approves Q1 plan; adjudicates findings; approves cleanup/retention and certifies | Does not invent missing evidence or silently repair the product |
43: | QA Executor | Performs Q1, drafts plan, executes approved Q2, records findings, executes approved retests and cleanup, exports packages | Does not self-approve, self-certify, mutate Git or make unauthorized product changes |
44: 
45: Names and models are interchangeable; authority follows the seat. The agent that engineered a candidate must not independently certify its own work. When one runtime changes seats, record the handoff and preserve an independent verification assignment and QA Lead review.
46: 
47: The Architect owns or validates acceptance criteria before implementation. The Engineer may propose clarifications during planning; approval and frozen-contract rules still apply. The Engineer's handoff reports what was built, not what the acceptance criteria ought to become after building it.
48: 
49: ## 4. How this fits existing doctrine
```


### 03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md:27

```text
27: ## 3. Context × Action × Seat Matrix
28: 
29: | Context | Action | Seat that acts | Status |
30: |---|---|---|---|
31: | Project module engineering (FFM, BIM, FIX, FEAT, RRM) | Build, test, self-verify; hand the Director file lists and suggested commit messages | Engineer (read-only Git inspection allowed; Git mutations Director-only; existing context-specific cloud permissions retained) | RULED (`BIM_PLAYBOOK.md` §7) |
32: | Project module engineering | Commit per concern to the module branch; push | Director | RULED (`BIM_PLAYBOOK.md` §6) |
33: | Project module QA | Create `qa/<module-branch>` **at the completed engineering candidate commit** after the engineering handoff; commit on it; merge it into `main`; push `main` | Director | RULED (RUL-02, 2026-10-14) |
34: | Project module QA | Authorized rework on `qa/<module-branch>` only when ruled; never on a transfer back to the engineering branch | Engineer | RULED (RUL-02) |
35: | Project module QA | Independent testing on `qa/<module-branch>`; no Git mutation | QA Executor | RULED (RUL-02; `QAM_PLAYBOOK.md` §3) |
36: | Project module QA | Certify the governed candidate; approve cleanup and retention | QA Lead | RULED (RUL-01, RUL-03) |
37: | Project module closeout | Closeout instruction; bounded closeout; commit, merge, push | Architect → Engineer → Director | RULED (RUL-02, RUL-03) |
38: | Doctrine Hub synchronization (`app-factory-docs-v1`) | Run branch, commits and the one authorized push inside the Hub only | Director-only Git mutations for this sync (RUL-15); read-only Git inspection is allowed. Historical Hub exceptions do not override this assignment | RULED (Operator ruling 2026-08-05, reconfirmed 2026-09-14; cited, not restated) |
39: | Cloud contexts beyond an existing explicit restriction | Deploy, promote, roll back, change infrastructure | Per an attributable context-specific authorization; no general grant here | OPEN under DEC-18 (§7–§8) |
40: | FFM runs | Retain the recorded FFM staging permission; verify its bounds before any action | — | OPEN (§8, O-1) |
41: | Any context | Cloud columns of this matrix (who prepares the package, who verifies readiness, who executes which phase) | — | OPEN (§8, O-1) |
42: 
```

## R3 authority
Three kit-diagram lines preserve diagram flow and distinguish implementation facts from governing requirements. No filesystem-wins/disk-wins hits in full live scope including fences/SVG. Existing aligned sites remain unchanged; a fact on disk cannot silently amend requirements.

### 02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:249

```text
249: ```
250: PHASE 0 — RECON (§2)
251:    Answer RECON_QUESTIONNAIRE read-only → Recon Report → Architect authors
252:         │
253:         ▼
254: KIT READ — STARTER_KIT_HANDBOOK
255:    Read the handbook, treat it as ASPIRATIONAL — verify every load-bearing claim against disk (RECON_QUESTIONNAIRE §0).
256:    Disk establishes implementation facts; approved briefs govern scope and governing documents control their subjects.
257:    Record handbook drift; route genuine requirements conflicts to the Director.
258:         │
259:         ▼
260: KIT AUDIT — FRONTEND_FIRST_PLAYBOOK §0
261:    Before authoring ANY code: what does the kit already provide? What is
262:    consumed directly? What actually needs building?
```

## R4 withdrawals and contract trace
FC-022: guard applies to setup, seeding and client construction, with fail-closed identity/target checks. Both dangerous executable fences are absent. Remaining prose about synthetic Stripe rows and dotenv describes test intent/dependency under the guard; it is not evidence of production replacement closure. FC-038: route location alone never authorizes bypass; both construction comments constrain capability acquisition. The other 28 rows retain their mapped invariant and dependent executable surfaces, except the explicitly reviewed overlap with these repairs and contact policy. WITHDRAWAL_ROWS.json contains all 31 independent grades and candidate quotes.

### 03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:881

```text
881: ### E2E user lifecycle (Supabase apps)
882: 
883: **Executable example withdrawn.** The previous example is not an approved implementation. The outgoing archived document preserves it as history. Replacement code requires the project’s approved contract, verified dependency interfaces and behavioral evidence. This withdrawal contains the misleading recipe; it does not certify the underlying finding resolved.
884: 
885: Before privileged test setup or cleanup, verify the target project reference against the Director-approved test-project allowlist and verify the authorized test identity. Fail closed on mismatch, missing identity or unknown target. Record every run-created identity; cleanup may act only on that set. Production verification is a separately authorized, bounded, non-destructive procedure.
886: 
887: ---
888: 
889: ### Direct DB seeding to bypass Stripe in E2E
890: 
891: E2E tests need users with specific subscription tiers. Automating Stripe Checkout in a browser is brittle (Stripe changes their DOM). Solution: insert subscription rows directly into Supabase via the admin client, as if the webhook had already fired.
892: 
893: **Executable example withdrawn.** The previous example is not an approved implementation. The outgoing archived document preserves it as history. Replacement code requires the project’s approved contract, verified dependency interfaces and behavioral evidence. This withdrawal contains the misleading recipe; it does not certify the underlying finding resolved.
894: 
895: Privileged seeding and admin-client construction in test helpers run only behind the Director-approved test-project allowlist and authorized-test-identity guard above; fail closed on mismatch, missing identity or unknown target.
896: 
897: Synthetic Stripe IDs (`cus_test_*`, `sub_test_*`) work because the gating logic only reads `tier` and `status` from the row — it never calls the Stripe API to verify the subscription ID.
898: 
899: **Trade-off:** E2E doesn't cover the actual Stripe round-trip. That's what integration tests (mocked) validate at the route level, and what manual smoke tests validate end-to-end. Each layer covers what it's good at.
900: 
901: ### Supabase admin client in E2E helpers
902: 
903: **Executable example withdrawn.** The previous example is not an approved implementation. The outgoing archived document preserves it as history. Replacement code requires the project’s approved contract, verified dependency interfaces and behavioral evidence. This withdrawal contains the misleading recipe; it does not certify the underlying finding resolved.
904: 
905: Privileged seeding and admin-client construction in test helpers run only behind the Director-approved test-project allowlist and authorized-test-identity guard above; fail closed on mismatch, missing identity or unknown target.
906: 
907: The `dotenv` import is required because Playwright runs in its own Node process, not inside Next.js. Without it, env vars from `.env.local` aren't available to the helpers.
908: 
```


### 04_REFERENCE_MANUALS/DATABASE_MANUAL.md:418

```text
418: ### Service Role Bypass
419: 
420: A service-role client bypasses RLS and is appropriate only inside an independently authorized elevated operation:
421: - Background jobs with operation-local authorization
422: - Admin operations with operation-local authorization
423: 
424: An API route is not itself a reason to bypass RLS; never use a service-role client as the default route client (see AUTH_MANUAL, Service-Role Capability Boundary).
425: 
426: ```typescript
427: // Construct only inside an independently authorized elevated operation, never as a default route client.
428: import { createClient } from '@supabase/supabase-js';
429: 
430: const supabase = createClient(
431:   process.env.SUPABASE_URL!,
432:   process.env.SUPABASE_SERVICE_ROLE_KEY! // Operation-local authorization is required before construction.
433: );
434: ```
435: 
436: ---
```


### 04_REFERENCE_MANUALS/AUTH_MANUAL.md:1308

```text
1308: **Executable example withdrawn.** The previous example is not an approved implementation. The outgoing archived document preserves it as history. Replacement code requires the project’s approved contract, verified dependency interfaces and behavioral evidence. This withdrawal contains the misleading recipe; it does not certify the underlying finding resolved.
1309: 
1310: The role table is the only authorization authority. Never authorize from user_metadata or a profile mirror. Superadmin creation is console-only; no app-side superadmin creation route is provided. Retire the metadata-authorized add-user, delete-user and get-users recipes. Future privileged list/delete operations remain possible only with trusted current-role lookup, operation-local authorization before elevated capability, an approved target-role allowlist and privileged-target protection. Profile mirrors contain profile data, not authorization columns. Registration metadata is not authorization.
1311: 
1312: Use the session client for identity and RLS-bound data. Acquire an isolated admin client only after independently authorizing the elevated operation. An API route is not itself a reason to bypass RLS. Do not substitute a service-role client as a general fix for denied access.
1313: 
1314: ---
1315: 
```

### RV2-F01 — HIGH — FC-066 remains inconsistent
API §3 establishes one named service contract, allowing only explicitly labeled alternatives. Its normalization array example, typed-outcome caller and ISR raw-JSON example now have those labels. The typed caller checks status before items and uses an explicit public-catalog degradation policy. fetchProductsByIds is a distinct operation with an ids parameter and explicit array return.

APP_ARCHITECTURE §5 imports fetchProducts from @/services/productServices and passes its entire result to ProductList; the streaming example repeats it. Neither container declares an alternative contract. STATE §7 calls the same service and passes its result as initialProducts to a Props field explicitly typed Product[]. Its preceding service returns untyped response.json() without declaring the endpoint wire shape or labeling itself an alternative to API §3. A GOOD service/store separation label is not a return-contract label. Against the declared typed-outcome service, the caller supplies an outcome object where an array is required and never narrows success. Choosing the array normalization or raw JSON variant implicitly would still violate the explicit-alternative requirement. This is an unresolved in-scope contract contradiction, not a request to broaden implementation or reopen FU-1/FU-2.

### 04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:166

```text
166: ## 3. Service Layer Implementation
167: 
168: ### Creating a Service File
169: 
170: **Executable example withdrawn.** The previous example is not an approved implementation. The outgoing archived document preserves it as history. Replacement code requires the project’s approved contract, verified dependency interfaces and behavioral evidence. This withdrawal contains the misleading recipe; it does not certify the underlying finding resolved.
171: 
172: Services return an explicit typed outcome: success, not-found, unavailable, invalid or forbidden. Routes map it to the approved HTTP/UI behavior with generic client messages and no upstream error text. Do not cache failures as successful public data. Degrade or fail closed according to the module’s approved failure policy; an unavailable entitlement read is not confirmed absence.
173: 
174: Declare wire and internal types separately and normalize once at the service boundary. A named operation uses one parameter signature and typed result envelope in its service, route and client examples. Any independent alternative is explicitly labeled with its own contract; callers do not silently mix array, paginated and wrapped results.
```


### 04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:613

```text
613: // Independent normalization-step example: fetchProducts() returns Promise<Product[]>.
614: // This array-returning step is not the typed-outcome service used by the route below.
615: export const fetchProducts = async (): Promise<Product[]> => {
616:   const response = await fetch(API_ENDPOINTS.PRODUCTS);
617:   const wooProducts: WooCommerceProduct[] = await response.json();
618:   
619:   // Transform each product to internal format
620:   return wooProducts.map(normalizeProduct);
621: };
622: ```
```


### 04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:785

```text
785: ### Graceful Degradation Pattern
786: 
787: This caller uses the §3 typed-outcome contract: `fetchProducts()` returns a discriminated outcome with `status` equal to `success`, `not-found`, `unavailable`, `invalid` or `forbidden`; only `success` carries `items: Product[]`. This example assumes a project-approved public-catalog failure policy permitting the generic empty-state UI on non-success; this is not an entitlement decision or a cached successful result. It does not call the independent array-returning normalization example.
788: 
789: ```typescript
790: // src/app/(public)/shop/page.tsx
791: 
792: import { fetchProducts } from '@/services/productServices';
793: import { ProductList } from '@/components/shop/ProductList';
794: import { EmptyState } from '@/components/common/EmptyState';
795: 
796: export default async function ShopPage() {
797:   const outcome = await fetchProducts();
798: 
799:   // Apply the declared public-catalog failure policy; do not treat failure as success.
800:   if (outcome.status !== 'success' || outcome.items.length === 0) {
801:     return (
802:       <EmptyState
803:         title="No products available"
804:         description="Please check back later or try refreshing the page."
805:         action={{
806:           label: 'Refresh',
807:           href: '/shop',
808:         }}
809:       />
810:     );
811:   }
812: 
813:   return <ProductList products={outcome.items} />;
814: }
815: ```
```


### 04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:856

```text
856: ### ISR and Revalidation
857: 
858: Independent ISR example: this `fetchProducts()` returns the endpoint’s raw JSON payload, with no normalization or typed-outcome envelope; it is not the §3 service or the caller above. The project must declare and validate that endpoint’s wire contract and failure/cache policy before implementation; this example only illustrates the revalidation option.
859: 
860: ```typescript
861: // Static generation with revalidation
862: export const fetchProducts = async () => {
863:   const response = await fetch(API_ENDPOINT, {
864:     next: { 
865:       revalidate: 3600, // Revalidate every hour
866:     },
867:   });
868:   return response.json();
869: };
```


### 04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:942

```text
942: ### Batch Operations
943: 
944: ```typescript
945: // Batch multiple IDs into single request
946: export const fetchProductsByIds = async (ids: number[]): Promise<Product[]> => {
947:   if (ids.length === 0) return [];
948:   
949:   // WooCommerce supports include parameter
950:   const response = await fetch(
951:     `${API_ENDPOINT}/products?include=${ids.join(',')}`
952:   );
953:   
954:   return response.json();
955: };
```


### 04_REFERENCE_MANUALS/APP_ARCHITECTURE_MANUAL.md:495

```text
495: ## 5. Rendering Strategies
496: 
497: ### Server Components (Default)
498: 
499: By default, all components in the App Router are Server Components:
500: 
501: ```typescript
502: // src/app/(public)/shop/page.tsx
503: // This is a Server Component (no 'use client' directive)
504: 
505: import { fetchProducts } from '@/services/productServices';
506: import { ProductList } from '@/components/shop/ProductList';
507: 
508: export default async function ShopPage() {
509:   // This runs on the server
510:   const products = await fetchProducts();
511:   
512:   return (
513:     <div className="container mx-auto py-8">
514:       <h1 className="text-3xl font-bold mb-6">Shop</h1>
515:       <ProductList products={products} />
516:     </div>
517:   );
518: }
519: ```
520: 
```


### 04_REFERENCE_MANUALS/APP_ARCHITECTURE_MANUAL.md:589

```text
589: 
590: ```typescript
591: // src/app/(public)/shop/page.tsx
592: 
593: import { Suspense } from 'react';
594: import { ProductList } from '@/components/shop/ProductList';
595: import { ProductListSkeleton } from '@/components/shop/ProductListSkeleton';
596: 
597: export default function ShopPage() {
598:   return (
599:     <div className="container mx-auto py-8">
600:       <h1 className="text-3xl font-bold mb-6">Shop</h1>
601:       
602:       {/* Stream in product list */}
603:       <Suspense fallback={<ProductListSkeleton />}>
604:         <ProductListAsync />
605:       </Suspense>
606:     </div>
607:   );
608: }
609: 
610: // Async component that fetches data
611: async function ProductListAsync() {
612:   const products = await fetchProducts();
613:   return <ProductList products={products} />;
614: }
615: ```
616: 
```


### 04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:793

```text
793: ### Store + Service Layer
794: 
795: **Keep network calls in services, not stores.** Stores manage state; services fetch data.
796: 
797: ```typescript
798: // ❌ BAD: Network call inside store
799: const useProductStore = create((set) => ({
800:   products: [],
801:   fetchProducts: async () => {
802:     const response = await fetch('/api/products'); // Network call in store!
803:     const data = await response.json();
804:     set({ products: data });
805:   },
806: }));
807: 
808: // ✅ GOOD: Service handles network, store handles state
809: // src/services/productServices.ts
810: export const fetchProducts = async () => {
811:   const response = await fetch('/api/products');
812:   return response.json();
813: };
814: 
815: // src/store/useProductStore.ts
816: export const useProductStore = create((set) => ({
817:   products: [],
818:   setProducts: (products) => set({ products }),
819: }));
820: 
821: // Component orchestrates both
822: const ProductPage = () => {
823:   const setProducts = useProductStore((state) => state.setProducts);
824:   
825:   useEffect(() => {
826:     fetchProducts().then(setProducts);
827:   }, []);
828: };
829: ```
```


### 04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:863

```text
863: ### Store + Server Components
864: 
865: Server Components cannot use hooks, but they can pass initial data to Client Components:
866: 
867: ```typescript
868: // src/app/(public)/shop/page.tsx (Server Component)
869: import { fetchProducts } from '@/services/productServices';
870: import { ProductList } from '@/components/shop/ProductList';
871: 
872: export default async function ShopPage() {
873:   const products = await fetchProducts();
874:   
875:   // Pass server data to client component
876:   return <ProductList initialProducts={products} />;
877: }
878: 
879: // src/components/shop/ProductList.tsx (Client Component)
880: 'use client';
881: 
882: import { useEffect } from 'react';
883: import { useProductStore, selectProducts } from '@/store/useProductStore';
884: 
885: interface Props {
886:   initialProducts: Product[];
887: }
888: 
889: export const ProductList = ({ initialProducts }: Props) => {
890:   const products = useProductStore(selectProducts);
891:   const setProducts = useProductStore((state) => state.setProducts);
892:   
893:   // Initialize store with server data on mount
894:   useEffect(() => {
895:     setProducts(initialProducts);
896:   }, [initialProducts, setProducts]);
897:   
898:   return (
899:     <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
900:       {products.map((product) => (
901:         <ProductCard key={product.id} product={product} />
902:       ))}
903:     </div>
```

## R5 browser contact persistence
All four named manuals express the default. STATE partialize returns an empty object, so billingAddress/shippingAddress initialization (and stale generic Persisted comment) does not write either field to storage. The generic items store, storage adapters, preferences and Form drafts row do not supply a raw-contact recipe; explicit contact restrictions govern. STATE §4 comment supplies purpose/owner, §6 supplies retention/scope and signout/account reset, coherent with the three added sentences. No contact field is added to a storage write. The complete ten-term sweep includes 155 hits; duplicate term matches are separate rows. Seven fetchProducts hits are flagged for R4; none are undispositioned.

### 03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:416

```text
416: ### localStorage + UI dual-verification
417: 
418: For tests touching persistent client state (Zustand, Redux with localStorage, IndexedDB), assert against **both** the source of truth AND the UI:
419: 
420: ```ts
421: await expect(page.getByText(/Coupon Applied:/)).toBeVisible(); // user-facing claim
422: 
423: const stored = await page.evaluate(() =>
424:   localStorage.getItem("checkout-storage"),
425: );
426: expect(JSON.parse(stored!).state.couponCode).toBe(expectedCode); // approved non-sensitive project fixture only
427: ```
428: 
429: No persistent raw contact information is stored in browser storage by default; any approved exception names the fields, purpose, retention period and owner, with clearing/invalidation behavior.
430: 
431: The UI proves the user sees the right thing. The persistent state proves the system actually did the right thing. UIs can lie (e.g., showing optimistic state that doesn't match the store).
```


### 04_REFERENCE_MANUALS/AUTH_MANUAL.md:1118

```text
1118: 1. **Don't trust client state**
1119:    - Client can be manipulated
1120:    - Always verify on server
1121: 
1122: 2. **Don't store sensitive data in localStorage**
1123:    - Accessible via JavaScript
1124:    - Use secure cookies instead
1125:    - No persistent raw contact information is stored in browser storage by default; any approved exception names the fields, purpose, retention period and owner, with clearing/invalidation behavior.
1126: 
1127: 3. **Don't expose API keys**
1128:    - Never commit to git
```


### 04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:201

```text
201: Persist one authorized checkout-attempt identity across retries and claim it atomically against concurrent requests. Scope provider idempotency keys to that attempt and operation, reuse or retrieve existing external objects after an unknown outcome, and reconcile before creating a replacement. Use the project-approved customer-identity contract without assuming paid activation; universal subscription schema design is deferred. Handle every documented subscription state, not only active.
202: 
203: Use one validated checkout contract across form, state, route and service. The request carries billing.email, validated line identifiers/quantities, shippingMethod and couponCode; it carries no authoritative monetary values. The response identifies the authorized order/payment attempt or a typed generic failure. The server pricing operation from the same contract supplies totals. Revisions to items, shipping or coupon invalidate the old payment binding before a new attempt is released.
204: 
205: The checkout interaction contract includes shippingCost and couponDiscount as display estimates, couponCode, setCoupon(code) and clearCoupon(), alongside the existing checkout fields. The server revalidates shipping and coupons. STATE_MANAGEMENT_MANUAL owns the shared store shape; ECOMMERCE_AND_PAYMENTS_MANUAL refers to it. Personal fields follow the approved account-transition and retention policy in STATE_MANAGEMENT_MANUAL. No persistent raw contact information is stored in browser storage by default; any approved exception names the fields, purpose, retention period and owner, with clearing/invalidation behavior.
206: 
207: ---
```


### 04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:499

```text
499: ### `partialize` - What to Persist
500: 
501: **Never persist everything.** Use `partialize` to select only UX-critical state:
502: 
503: ```typescript
504: export const useCheckoutStore = create<CheckoutState>()(
505:   persist(
506:     (set) => ({
507:       // Persisted
508:       billingAddress: null,
509:       shippingAddress: null,
510:       
511:       // NOT persisted (transient)
512:       isProcessing: false,
513:       validationErrors: {},
514:       paymentIntent: null,
515:     }),
516:     {
517:       name: 'checkout-storage',
518:       partialize: (state) => ({
519:         // Raw contact information is not persisted by default.
520:         // An approved exception must name fields, purpose, retention and owner.
521:         // DO NOT persist: isProcessing, validationErrors, paymentIntent
522:       }),
523:     }
524:   )
525: );
526: ```
527: 
528: #### What to Persist vs What NOT to Persist
529: 
530: | Persist ✅ | Don't Persist ❌ |
531: |-----------|-----------------|
532: | Cart items | Loading states |
533: | User preferences | Validation errors |
534: | Form drafts | API responses |
535: | Selected filters | Temporary UI state |
536: | Theme preference | Payment intents |
537: | Recently viewed | Session tokens |
538: 
```


### 04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:779

```text
779: ### Form/Checkout Store Template
780: 
781: **Executable example withdrawn.** The previous example is not an approved implementation. The outgoing archived document preserves it as history. Replacement code requires the project’s approved contract, verified dependency interfaces and behavioral evidence. This withdrawal contains the misleading recipe; it does not certify the underlying finding resolved.
782: 
783: Do not persist raw contact details by default. Any approved personal-data persistence declares permitted fields, retention duration and user or guest scope. Sign-out and account transition reset and invalidate every affected store even when remote logout fails; a new account must not hydrate the previous account’s data. Payment and authorization state remain outside persistence. Storage readiness is separate from business-data reset.
784: 
785: Keep hydration readiness outside the resettable business state. A normal reset preserves readiness. Hydration finishes in ready or error; an error exposes bounded recovery and never leaves an indefinite loading state. Verify reset after hydration, invalid stored data and unavailable storage.
786: 
787: The checkout interaction contract includes shippingCost and couponDiscount as display estimates, couponCode, setCoupon(code) and clearCoupon(), alongside the existing checkout fields. The server revalidates shipping and coupons. STATE_MANAGEMENT_MANUAL owns the shared store shape; ECOMMERCE_AND_PAYMENTS_MANUAL refers to it. Personal fields follow the approved account-transition and retention policy.
```

## R7 metadata
Six header lines are unchanged and match MANIFEST version/date/status cells; landing date remains 2026-10-18. Each document amends one existing history row with the same QA-repair clause. CHANGELOG retains 39 contiguous run rows, six amended, within Ongoing entries before separator/footer. No table column/order/header changes; no new history row or section. Exact counts and headers in RAW/metadata.json.

### CHANGELOG.md:34

```text
34: | 2026-08-10 | QA_PLAYBOOK v1.1 | AC-numbering sync (Finalization F6): AC*/gate-ID distinct-families note at §7; legacy gate-ID labels on FIX-002 field-evidence examples (§7, §15); no renumbering — historical evidence stays historically true | factory-module-doctrine |
35: | 2026-08-10 | BUG_FIX_PLAYBOOK v1.0 | Seamless merge of the field amendments kit (v0.1 archived): role additions (git-zero Engineer, QA verdict ownership, Architect-advises), cross-module repair commits, ACCEPTANCE_SPEC as required artifact, app-suffixed BUG_REPORT header, new §16 FIX Module Anatomy + §17 Module Identity + §22 Field Case Studies (FIX-001/002/003) | factory-module-doctrine |
36: | 2026-08-10 | SOFTWARE_FACTORY_PLAYBOOK v1.3 | New §2.5 "Module Identity & QA Handoff" (Factory-wide — governs BIM, FIX, FEAT, and future module types): app-suffixed IDs, ACCEPTANCE_SPEC contract, AC* numbering, QA verdict ownership + Operator final authority. Fractional section number follows the file's own §1.5 precedent (v1.2 archived) | factory-module-doctrine |
37: | 2026-10-18 | APP_FACTORY_BLUEPRINT v2.2 | Factory DocSet sync; preserved outgoing original; MC correction pass | FC-004, FC-008, FC-017, FC-027, MC-04, MC-06, MC-07, RUL-01, RUL-05, RUL-07, RUL-09, RUL-10, RUL-12, RUL-14 |
38: | 2026-10-18 | SOFTWARE_FACTORY_PLAYBOOK v1.4 | Factory DocSet sync; preserved outgoing original; MC correction pass | FC-001, FC-002, FC-005, FC-006, FC-007, FC-009, FC-021, FC-033, FC-036, FC-063, FC-066, MC-01, MC-05, MC-06, MC-07, RUL-01, RUL-05, RUL-07, RUL-08, RUL-09, RUL-11, RUL-12, RUL-14, W01, W23 |
39: | 2026-10-18 | STARTER_KIT_HANDBOOK v1.2 | Factory DocSet sync; preserved outgoing original; MC correction pass | DEC-04, FC-001, FC-003, FC-003/096, FC-005, FC-033, FC-034, FC-036, FC-038, FC-041, FC-042, FC-072, FC-073, FC-081, RUL-12, RUL-14 |
40: | 2026-10-18 | ARCHITECT_PLAYBOOK v2.3 | Factory DocSet sync; preserved outgoing original; MC correction pass | FC-004, FC-005, FC-008, FC-014, FC-017, FC-027, MC-06, RUL-01, RUL-05, RUL-09, RUL-12, W18, W23 |
41: | 2026-10-18 | ARCHITECT_QUESTIONNAIRE v2.3 | Factory DocSet sync; preserved outgoing original; MC correction pass | FC-016 |
42: | 2026-10-18 | DESIGNER_PLAYBOOK v2.2 | Factory DocSet sync; preserved outgoing original; MC correction pass | FC-004, FC-005, FC-008, FC-016, FC-017, FC-018, FC-027, FC-084, MC-06, MC-07, RUL-01, RUL-05, RUL-09, RUL-12, W23 |
43: | 2026-10-18 | ENGINEER_PLAYBOOK v1.3 | Factory DocSet sync; preserved outgoing original; MC correction pass; QA-P4 repair: F01–F05 (AC5/6/9/15/16/18) | FC-004, FC-005, FC-008, FC-014, FC-015, FC-017, FC-018, FC-027, MC-06, MC-07, RUL-01, RUL-05, RUL-09, RUL-12, W19, W23 |
44: | 2026-10-18 | HANDOFF_PACKAGE_PLAYBOOK v1.2 | Factory DocSet sync; preserved outgoing original; MC correction pass | FC-009, FC-017, FC-018, FC-019, FC-027, MC-01, RUL-09, W20 |
45: | 2026-10-18 | RECON_QUESTIONNAIRE v0.6 | Factory DocSet sync; preserved outgoing original; MC correction pass | FC-001, FC-005, FC-007, FC-014, FC-033, FC-034, FC-069, MC-02, MC-04, MC-13, RUL-03, RUL-12, W17 |
46: | 2026-10-18 | APP_FACTORY_SKILLS_PLAYBOOK v1.2 | Factory DocSet sync; preserved outgoing original; MC correction pass | FC-005, FC-006, FC-014, FC-021, FC-087 |
47: | 2026-10-18 | BIM_PLAYBOOK v1.1 | Factory DocSet sync; preserved outgoing original; MC correction pass | FC-012, FC-014, MC-06, MC-07, RUL-01, RUL-02, RUL-03, RUL-04, RUL-05, RUL-07, RUL-12, RUL-15, W02, W03, W04, W05, W06, W07, W23 |
48: | 2026-10-18 | BUG_FIX_PLAYBOOK v1.1 | Factory DocSet sync; preserved outgoing original; MC correction pass | FC-012, FC-014, RUL-12, W21 |
49: | 2026-10-18 | FEAT_PLAYBOOK v1.1 | Factory DocSet sync; preserved outgoing original; MC correction pass | FC-014, RUL-12, W22 |
50: | 2026-10-18 | FFM_PLAYBOOK v1.3 | Factory DocSet sync; preserved outgoing original; MC correction pass | FC-003, FC-004, FC-005, FC-009, FC-014, FC-016, FC-017, FC-019, FC-025, FC-026, FC-027, FC-028, FC-029, FC-071, FC-072, FC-081, MC-01, MC-06, RUL-01, RUL-02, RUL-03, RUL-05, RUL-07, RUL-09, RUL-12, RUL-14, RUL-15, W08, W09, W10, W11, W12, W13, W23 |
51: | 2026-10-18 | FRONTEND_BUILD_PHASE_PLAYBOOK v1.3.0 | Factory DocSet sync; preserved outgoing original; MC correction pass | FC-032, FC-071, FC-072, FC-088, RUL-14 |
52: | 2026-10-18 | FRONTEND_FIRST_PLAYBOOK v1.2.0 | Factory DocSet sync; preserved outgoing original; MC correction pass | FC-009, MC-01 |
53: | 2026-10-18 | QA_PLAYBOOK v1.2 | Factory DocSet sync; preserved outgoing original; MC correction pass | FC-005, FC-025, RUL-03, RUL-12, W14, W15, W16 |
54: | 2026-10-18 | TESTING_PLAYBOOK v2.2 | Factory DocSet sync; preserved outgoing original; MC correction pass; QA-P4 repair: F01–F05 (AC5/6/9/15/16/18) | DEC-03, FC-020, FC-021, FC-022, FC-023, FC-024, FC-030, FC-031, FC-040, FC-063, RUL-11, RUL-12, RUL-13 |
55: | 2026-10-18 | API_AND_SERVICES_MANUAL v1.2 | Factory DocSet sync; preserved outgoing original; MC correction pass; QA-P4 repair: F01–F05 (AC5/6/9/15/16/18) | FC-021, FC-056, FC-057, FC-058, FC-059, FC-061, FC-063, FC-064, FC-066, FC-070, RUL-11 |
56: | 2026-10-18 | APP_ARCHITECTURE_MANUAL v1.4 | Factory DocSet sync; preserved outgoing original; MC correction pass | FC-001, FC-009, FC-021, FC-028, FC-033, FC-035, FC-036, FC-041, FC-042, FC-063, FC-066, FC-071, MC-01, RUL-11 |
57: | 2026-10-18 | AUTH_MANUAL v1.5 | Factory DocSet sync; preserved outgoing original; MC correction pass; QA-P4 repair: F01–F05 (AC5/6/9/15/16/18) | FC-001, FC-021, FC-033, FC-034, FC-035, FC-036, FC-038, FC-039, FC-041, FC-042, FC-043, FC-044, FC-063, FC-066, RUL-11 |
58: | 2026-10-18 | DATABASE_MANUAL v1.2 | Factory DocSet sync; preserved outgoing original; MC correction pass; QA-P4 repair: F01–F05 (AC5/6/9/15/16/18) | FC-001, FC-003/096, FC-033, FC-034, FC-036, FC-037, FC-038, FC-039, FC-045, RUL-11 |
59: | 2026-10-18 | ECOMMERCE_AND_PAYMENTS_MANUAL v1.2 | Factory DocSet sync; preserved outgoing original; MC correction pass; QA-P4 repair: F01–F05 (AC5/6/9/15/16/18) | FC-047, FC-050, FC-051, FC-052, FC-053, FC-054, FC-055, FC-059, FC-060, FC-062, FC-063, FC-067, FC-068, RUL-11 |
60: | 2026-10-18 | STATE_MANAGEMENT_MANUAL v1.3 | Factory DocSet sync; preserved outgoing original; MC correction pass | FC-035, FC-040, FC-046, FC-046-heading, FC-047, FC-048, FC-049, FC-055, FC-067, FC-068, RUL-11, RUL-13 |
61: | 2026-10-18 | STRIPE_SUBSCRIPTIONS_PLAYBOOK v1.2 | Factory DocSet sync; preserved outgoing original; MC correction pass | FC-047, FC-052, FC-053, FC-054, FC-055, FC-059, FC-063, FC-065, FC-065-confirmed, FC-065-timeout, FC-067, FC-068, RUL-11 |
62: | 2026-10-18 | COMPONENT_REGISTRY v1.2 | Factory DocSet sync; preserved outgoing original; MC correction pass | FC-003, FC-072, FC-073, FC-081, FC-082, RUL-14 |
63: | 2026-10-18 | GLOBAL_DESIGN_SYSTEM_HANDBOOK v1.2 | Factory DocSet sync; preserved outgoing original; MC correction pass | FC-017, FC-027, FC-071, FC-072, FC-077, RUL-09 |
64: | 2026-10-18 | THEME_LIBRARY v1.3 | Factory DocSet sync; preserved outgoing original; MC correction pass | FC-003, FC-074, FC-081, RUL-14 |
65: | 2026-10-18 | THEMING_MANUAL v1.3 | Factory DocSet sync; preserved outgoing original; MC correction pass | FC-009, FC-075, FC-083, MC-01 |
66: | 2026-10-18 | TOKEN_FILE v1.3 | Factory DocSet sync; preserved outgoing original; MC correction pass | FC-074 |
67: | 2026-10-18 | UI_UX_BUILDING_MANUAL v1.5 | Factory DocSet sync; preserved outgoing original; MC correction pass | FC-003/096, FC-009, FC-041, FC-071, FC-072, FC-073, FC-076, FC-077, FC-078, FC-079, FC-080, FC-082, FC-083, MC-01 |
68: | 2026-10-18 | QAM_PLAYBOOK v1.0 | New owning playbook; accepted template installation verified separately | RUL-01, RUL-04, RUL-06; RUL-01…15; AD-01 |
69: | 2026-10-18 | RRM_PLAYBOOK v1.0 | New owning playbook | RUL-05, RUL-06, RUL-14, RUL-15; RUL-01…15; AD-01 |
70: | 2026-10-18 | DEPLOYMENT_PLAYBOOK v1.0 | New owning playbook | RUL-02, RUL-03, RUL-06, RUL-10; RUL-01…15; AD-01 |
71: | 2026-10-18 | Historical QA_PLAYBOOK v1.0 | Exact historical restoration; not active instructions | FC-089; RUL-14 |
72: | 2026-10-18 | FFM_CREATION workflow v1.0 | Revised reference and SVG stick diagram; original retained as superseded history | MC-06; W01–W23; RUL-01–RUL-15; Tony 2026-10-16 correction assignment |
73: | 2026-10-18 | FFM_EXECUTION workflow v1.0 | Revised reference and SVG stick diagram; original retained as superseded history | MC-06; W01–W23; RUL-01–RUL-15; Tony 2026-10-16 correction assignment |
74: | 2026-10-18 | FFM_DEPLOYMENT workflow v1.0 | Revised reference and SVG stick diagram; original retained as superseded history | MC-06; W01–W23; RUL-01–RUL-15; Tony 2026-10-16 correction assignment |
75: | 2026-10-18 | BIM_WORKFLOW workflow v1.0 | Revised reference and SVG stick diagram; original retained as superseded history | MC-06; W01–W23; RUL-01–RUL-15; Tony 2026-10-16 correction assignment |
76: 
77: ---
78: 
79: 🥄 *Part of Stark Industries — App Factory doctrine.*
```

## R10 pending transitions
All 12 exact old spans occur at their specified counts on nine unchanged paths. No new span occurs. Draft playbook headers and MANIFEST statuses agree; template README still says proposed, and each workflow is Proposed — pending verified publication. Old proposal approval-pending provenance is not revoked by a current additive approval. Product verdict/cleanup/release acceptance is not supplied by this retest.

### 03_BUILD_METHODOLOGY/QAM_PLAYBOOK.md:4

```text
4: > **Version:** 1.0 · **Date:** 2026-10-18 · **Status:** DRAFT FOR EXECUTABLE-MAP REVIEW — NOT INSTALLED
```


### 03_BUILD_METHODOLOGY/RRM_PLAYBOOK.md:4

```text
4: > **Version:** 1.0 · **Date:** 2026-10-18 · **Status:** DRAFT FOR EXECUTABLE-MAP REVIEW — NOT INSTALLED
```


### 03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md:4

```text
4: > **Version:** 1.0 · **Date:** 2026-10-18 · **Status:** DRAFT FOR EXECUTABLE-MAP REVIEW — NOT INSTALLED (sections marked OPEN are not doctrine until ruled)
```


### 03_BUILD_METHODOLOGY/RRM_PLAYBOOK.md:119

```text
119: Reviewer guidance belongs here under RUL-14 (2026-10-16). The following proposed wording expresses that guidance for map review; pilot source records remain unchanged.
```


### 03_BUILD_METHODOLOGY/_templates/QAM/README.md:4

```text
4: > Template set **v0.3**. Governing playbook: **QAM_PLAYBOOK v1.0**. QA behavior was accepted by Fable on 2026-10-14 with three exact amendments; Jarvis verified their application. Source set v0.3-draft is preserved byte-for-byte in this run’s intake snapshot. This proposed set differs only by the status/provenance translations enumerated in this run’s `PHASE_2_TEMPLATE_TRANSLATIONS.json`; installation and translation approval remain pending; it is newly authored from the approved playbook, not the pilot’s missing original templates. Source playbook SHA-256: `97e111e2a495f9a3fe65f50213e6f2ba68c8e5e963f3d23493b1ee99ad35c897`.
```


### MANIFEST.md:47

```text
47: | QAM_PLAYBOOK | 1.0 | 2026-10-18 | DRAFT FOR EXECUTABLE-MAP REVIEW — NOT INSTALLED | Mandatory module QAM and accepted _templates/QAM set | ARCHITECT_PLAYBOOK, BIM_PLAYBOOK, BUG_FIX_PLAYBOOK, DEPLOYMENT_PLAYBOOK, ENGINEER_PLAYBOOK, FEAT_PLAYBOOK, FFM_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, QA_PLAYBOOK, RRM_PLAYBOOK, SOFTWARE_FACTORY_PLAYBOOK, TESTING_PLAYBOOK |
```


### MANIFEST.md:49

```text
49: | RRM_PLAYBOOK | 1.0 | 2026-10-18 | DRAFT FOR EXECUTABLE-MAP REVIEW — NOT INSTALLED | Approved review repairs with QAM; post-FFM and Engine 2 checkpoints | ARCHITECT_PLAYBOOK, BIM_PLAYBOOK, BUG_FIX_PLAYBOOK, DEPLOYMENT_PLAYBOOK, ENGINEER_PLAYBOOK, FEAT_PLAYBOOK, FFM_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, QAM_PLAYBOOK, QA_PLAYBOOK, SOFTWARE_FACTORY_PLAYBOOK, TESTING_PLAYBOOK |
```


### MANIFEST.md:42

```text
42: | DEPLOYMENT_PLAYBOOK | 1.0 | 2026-10-18 | DRAFT FOR EXECUTABLE-MAP REVIEW — NOT INSTALLED (sections marked OPEN are not doctrine until ruled) | Common identity, exclusion, verification and recovery; context-specific permissions retained | APP_FACTORY_SKILLS_PLAYBOOK, BIM_PLAYBOOK, FFM_PLAYBOOK, QAM_PLAYBOOK, QA_PLAYBOOK, RECON_QUESTIONNAIRE, RRM_PLAYBOOK, SOFTWARE_FACTORY_PLAYBOOK |
```


### 03_BUILD_METHODOLOGY/_workflows/BIM_WORKFLOW.md:3

```text
3: > **Version:** 1.0 · **Date:** 2026-10-18 · **Status:** Proposed — pending verified publication
```


### 03_BUILD_METHODOLOGY/_workflows/FFM_CREATION.md:3

```text
3: > **Version:** 1.0 · **Date:** 2026-10-18 · **Status:** Proposed — pending verified publication
```


### 03_BUILD_METHODOLOGY/_workflows/FFM_DEPLOYMENT.md:3

```text
3: > **Version:** 1.0 · **Date:** 2026-10-18 · **Status:** Proposed — pending verified publication
```


### 03_BUILD_METHODOLOGY/_workflows/FFM_EXECUTION.md:3

```text
3: > **Version:** 1.0 · **Date:** 2026-10-18 · **Status:** Proposed — pending verified publication
```

