# CHUNK 07 — SKILLS / DOCUMENTATION GOVERNANCE REVIEW

## 1. STATUS

COMPLETE — bounded Chunk 07 examination finished 2026-09-13 13:06 UTC; approximately 14 minutes elapsed. Started 2026-09-13 12:52 UTC. Branch verified as `factory-docs-review-astra-w-chunks`; initial working tree clean. Baseline revision: `8fcadd474156501e788edcbff620c888dd19d7e9`. Contract reread completely; only Execution Plan Chunk 07 extracted.

Final verification: all 19 substantive primary files (1,998 lines) completely examined; supporting reads and limits listed in the coverage manifest. Eleven unique defects: **0 BLOCKER / 3 HIGH / 6 MEDIUM / 2 LOW**; three unique suggestions. All five scores are integers from 1–5. Git status/diff checks confirm only this authorized report changed and the branch remained unchanged; whitespace validation passed. Existing doctrine lint failures are recorded separately. Remote release state, deployed-copy state and other unverified matters remain explicitly UNKNOWN in §10. No prohibited review artifact was consulted.

## 2. SCOPE

Primary scope: `_SKILLS/`, `agent_docs/`, and current root governance files `CLAUDE.md`, `MANIFEST.md`, `README.md`, `RECOVERY.md`, `CHANGELOG.md`. Eight skill-package files, six response artifacts, and five current root files identified. Response artifacts were classified as historical execution evidence and were not promoted to doctrine. Root dated session logs are historical and excluded unless an explicit current dependency makes a bounded read necessary. Prior review artifacts, dispositions, synthesis, doctrine repair and future campaign design are excluded.

## 3. DOMAIN MODEL

The current Hub stores live canonical documents under five tier directories; canonical names are stable, versions live in headers, and outgoing versions belong in `_ARCHIVE/`. MANIFEST is the name/path/version routing index and a header-derived forward/reverse dependency graph. CHANGELOG records promotions and bumps. `_ARCHIVE/README.md` supplies the governing three-step snapshot/update/index procedure.

The `factory-docs-update` package operationalizes Hub changes. Its CLAUDE.md owns conduct and activation; SKILL.md owns six phases; the README addresses the Operator; references, a route tree and templates load at named phases. Operator approves scope, ripple map, route and pre-push diffs, then owns merge. Engineer conducts mechanics; Architect may provide or confirm ripple analysis. Application, kit, infrastructure and skill edits are excluded and parked separately. PACK, NEW DOC and SUPERSEDING DOC are explicitly distinguished at intake.

The intended cycle is project evidence → FLAGGED lesson/promotion pack → approved ripple map → archive/edit/header + MANIFEST/CHANGELOG → reviewed PR → Operator merge → close-out and ENCODED(PR) record. Independent observations, inferences, claims, gaps and questions have distinct labels. Root response/session/recovery protocols preserve artifacts; skill D15a separately requires inspecting actual interrupted work before adopting or abandoning it.

A release-tag model is named by MANIFEST, but its delivery details point to a still-DRAFT design under `_OTHERS/`. The skill ends at Hub merge/cleanup. The Skills Playbook, consulted only for the package's explicit governing dependency, requires version histories, a fresh-context activation test and zip distribution. Installed copies, release compatibility and ongoing update responsibility are not fully joined to the Hub update cycle in the examined sources.

## 4. FIVE-DIMENSION SCORECARD

Chunk 07 only; no Factory-wide score is inferred.

| Dimension | Score | Justification |
|---|---:|---|
| Correctness | 3 | Core archive, stable-name, evidence and promotion rules are sound; Git/gate ordering and specific inventory/archive claims fail literal checks (D01, D02, D04, D05). |
| Consistency | 2 | Root and skill conduct conflict over pre-approval writes and recovery; the skill's local mechanics contradict its own gates, and the CHANGELOG has competing instructions (D01, D02, D07–D10). |
| Completeness | 3 | A six-phase update cycle, human gates, explicit split handling and fresh-context skill testing exist. Propagation to skills and tagged downstream consumption remain incomplete (D03, D06). |
| Executability | 2 | A knowledgeable operator can run the process, but literal execution requires resolving several ordering, permission and recovery contradictions (D01, D02, D07–D09). |
| Maintainability | 3 | Canonical paths, declared dependency maps, archive rules and narrow lints offer a usable foundation; manual graph upkeep and untracked operational dependents still permit drift (D03–D06). |

## 5. WHAT IS STRONG

1. **Stable canonical names with visible historical snapshots.** MANIFEST lines 6–10 and `_ARCHIVE/README.md` lines 8–19 separate the live name from its version and preserve outgoing content. The forward index actually resolves all 31 live tier files, with version/date values matching the inspected headers. Preserve this separation and the honest nonstandard-header footnote; fix stale totals and snapshot omissions rather than abandoning the model.
2. **There is a real approval-controlled synchronization process.** SKILL §§Phases 1–6 specifies intake, ripple analysis, an Operator-owned route decision, per-doc execution, PR handoff and close-out. The Operator approves scope/map/route/diffs and alone merges; the Architect's analytical role is explicit but optional, and Engineer mechanics are named. Preserve this end-to-end allocation while correcting the local push/discovery order.
3. **Cargo provenance is treated as a decision, not silently trusted.** Skill CLAUDE D12/D13/D15/D16 (lines 106–116) distinguishes EVIDENCE/INFERENCE/CLAIM/GAP/QUESTION, verifies real sections and outgoing versions, and classifies PACK versus NEW DOC versus SUPERSEDING DOC before approval. The lesson template lines 15–22 separates PROJECT-LOCAL from DOCTRINE-CANDIDATE and records FLAGGED → ENCODED(PR) or DECLINED. Preserve explicit provenance and human-approved promotion; journals are not self-executing doctrine.
4. **Interrupted work has a concrete specialist recovery protocol.** Skill D15a line 114 requires real branch/commit/cargo/archive inspection, DONE/NOT DONE evidence, and explicit adopt-or-abandon handling. RIPPLE_MAP records source entries, exact placements, untouched-but-checked documents, splits and approval. Preserve this observed-state versus approved-intent distinction; bring the generic root recovery path into agreement.
5. **Skill anatomy supports progressive disclosure.** The package has distinct manager, methodology and Operator entry points, phase-loaded references, one route tree and two compact templates. The 174-line SKILL.md is comfortably bounded. The governing Skills Playbook §§8/12/15 explicitly requires meaningful version history and a fresh-context activation test, including failure/retest behavior. Preserve these mechanisms and the declared DRAFT status instead of treating it as an unqualified production certification.
6. **Lint failures are visible and scope-limited.** The actual four scripts return failures with file/line identifiers and document exclusions/history handling. Skill D9 forbids masking genuine failures and distinguishes introduced findings from pre-existing ones; README lines 88–89 gives the Operator the same distinction. Preserve this honest handling. Neither a clean diff nor these four syntactic checks proves semantic consistency.

## 6. PRIORITY FINDINGS

1. **C07-D01 — HIGH:** Mutating discovery precedes both approval and interrupted-run safeguards.
2. **C07-D02 — HIGH:** The printed Phase 4 sequence pushes before its push-approval gate.
3. **C07-D03 — HIGH:** Required ripple discovery misses active skill consumers and other non-header dependents.
4. **C07-D06 — MEDIUM:** Mandatory downstream release pinning lacks a complete current producer/consumer procedure.
5. **C07-D05 — MEDIUM:** A required outgoing-version archive is missing despite recorded sequential bumps.

## 7. RANKED DEFECTS

Ranked by severity and operational impact; IDs remain stable. **11 defects: 0 BLOCKER / 3 HIGH / 6 MEDIUM / 2 LOW.**

### C07-D01 — Activation performs a Git mutation before its own approval and resume safeguards

- **Classification:** DEFECT
- **Severity:** HIGH
- **Affected files:** `_SKILLS/factory-docs-update/CLAUDE.md`; `_SKILLS/factory-docs-update/SKILL.md`; `_SKILLS/factory-docs-update/README.md`.
- **Precise evidence:** Skill CLAUDE activation lines 27–39 orders discovery and, at line 33, says “If inside a clone, `git pull` main current before anything else,” before inspecting cargo/resume evidence. Line 39 permits only read-only discovery before approval; D2 line 86 forbids writes until approval. SKILL lines 30–36 completes that activation before switching to D15a for a resume. README lines 31–33 promises the automatic pull. Skill CLAUDE lines 43–47 explicitly permits activation inside a project clone, not just the Hub.
- **Why a defect:** Pulling can modify the checkout and integrate commits. Neither branch/dirty-tree/target-repository verification nor a fast-forward-only condition precedes the instructed mutation. D15a's actual-state inventory arrives too late to protect the state the activation may already change.
- **Operational consequence:** A fresh or resumed session can integrate unrelated work into the current project/branch, change its evidence baseline or encounter avoidable conflicts before scope approval.
- **Recommended resolution:** Require read-only repository, branch and working-tree identification plus resume triage first. Place any synchronization on a verified target behind its applicable authorization and preservation checks.
- **Confidence / limits:** High by instruction order; no pull, checkout or mutation was attempted during this review. A clean Hub clone on main may work, but that is not the full declared applicability.

### C07-D02 — Phase 4 pushes before the gate that approves pushing

- **Classification:** DEFECT
- **Severity:** HIGH
- **Affected files:** `_SKILLS/factory-docs-update/SKILL.md`; `_SKILLS/factory-docs-update/README.md`; `_SKILLS/factory-docs-update/references/TOOL_ROUTING.md`.
- **Precise evidence:** SKILL Phase 4 local mechanics line 100 includes `git push -u origin <branch>`; Stop Gate 4 line 107 then says “Awaiting your APPROVED to push and hand off.” Its output line 109 is a pushed branch. README lines 66–67 clearly places push after approval. TOOL_ROUTING lines 63–66 likewise lists push without a gate pointer. The MCP route at SKILL line 101 writes remote commits throughout Phase 4, so its publication boundary is materially different.
- **Why a defect:** The linear primary-route instructions cross the exact boundary the subsequent human gate reserves. Neither route-specific wording nor an explicit defer-push instruction reconciles the ordering.
- **Operational consequence:** Unapproved changes can be published to the review branch before the Operator sees the promised pre-push verification, or two competent agents stop at different points.
- **Recommended resolution:** Put local push after Gate 4 approval and define what Gate 4 authorizes on the already-remote MCP route. Keep Operator merge ownership intact.
- **Confidence / limits:** High, direct producer/runbook disagreement. This is unapproved branch publication, not evidence of direct-to-main writes or an actual release without approval; therefore HIGH, not BLOCKER.

### C07-D03 — Ripple discovery omits known classes of active dependents

- **Classification:** DEFECT
- **Severity:** HIGH
- **Affected files:** `MANIFEST.md`; `_SKILLS/factory-docs-update/SKILL.md`; `_SKILLS/factory-docs-update/templates/RIPPLE_MAP.md`; `_SKILLS/factory-docs-update/CLAUDE.md`.
- **Precise evidence:** MANIFEST lines 74–76 defines the blast radius as inverted header declarations among the tier docs. Its body-only appendix at 112–114 explicitly identifies a separate, incomplete set of undeclared dependencies. SKILL Phase 2 lines 54–62 uses the ← map to produce the definitive touch list, but does not require a body-reference or skill-consumer search. The map lists `APP_FACTORY_SKILLS_PLAYBOOK ← FFM_PLAYBOOK` only (line 107), while the active skill CLAUDE line 154 expressly makes this entire skill a child of that playbook. SKILL line 32 parks skill work only when a pack entry targets it; the ripple template lines 18–35 asks about docs, new docs and renames, with no explicit skill/distribution/template/asset dependency sweep.
- **Why a defect:** There is a real ripple model, but following its required discovery literally can miss a demonstrated active consumer outside the graph. Declaring skill writes out of scope is appropriate; failing to require their detection and separate disposition when source doctrine changes leaves the propagation obligation incomplete.
- **Operational consequence:** A correctly approved Hub change can finish while a deployed operational skill or body-only consumer continues enforcing the old rule. Minimal approved scope then protects an incomplete touch list from correction rather than ensuring all consequences are accounted for.
- **Recommended resolution:** Make the header graph an initial candidate set; require bounded checks of actual references and active operational consumers, including explicit checked/parked/not-applicable dispositions. Keep out-of-scope edits separate, with named follow-up ownership. No new campaign is designed here.
- **Confidence / limits:** High for the missing source-to-skill edge and required-process omission. No claim that the graph is intended to encode semantic implication automatically or that every body mention deserves a canonical dependency.

### C07-D06 — The mandatory release-pin model has no complete current delivery procedure

- **Classification:** DEFECT
- **Severity:** MEDIUM
- **Affected files:** `MANIFEST.md`; `_SKILLS/factory-docs-update/SKILL.md`; `_SKILLS/factory-docs-update/README.md`.
- **Precise evidence:** MANIFEST line 10 directs projects to pin `doctrine-YYYY.MM[-patch]` tags and cites DOCTRINE_HUB_DESIGN §2.6. The referenced source is `_OTHERS/DOCTRINE_HUB_DESIGN_v0_1.md`, explicitly DRAFT/awaiting approval at line 5. Its lines 39–49 describe importing a tagged set and recording `agent_docs/DOCTRINE_VERSION`, but do not assign tag creation/release acceptance or an update decision for existing pins; line 54 parks automation while referencing a `DOCTRINE_SYNC_MANIFEST` manual process that filename discovery did not find. The active update skill's completion at lines 126–166 ends with merge, clean tree and ENCODED entries; it contains no release/pin handoff. README line 104 forbids hand-copying between projects because everything should flow through this process.
- **Why a defect:** Consumers are explicitly required to use a particular release identity, but the active producer process does not say who produces that identity, when merged doctrine becomes releasable, or how that release reaches the consumers. Individual header bumps and a Hub merge are not the same operation as selecting a coherent downstream baseline.
- **Operational consequence:** An agent cannot complete the specified Hub→project consumption path without inventing release ownership or relying on an operator's private convention; zipped skill copies also lack a stated compatible DocSet baseline.
- **Recommended resolution:** Establish a small authoritative release/consumption procedure with the responsible owner, exact revision/tag, recorded downstream identity, update/intentional-pin decision and recovery direction. Promote or clearly supersede the draft reference; automation and staged rollout can remain optional.
- **Confidence / limits:** High that the bounded active workflow lacks these required steps; MEDIUM impact because projects can still use a manually chosen commit. No local `doctrine-*` tags were found. Remote tag verification failed with DNS resolution, so remote release existence is **UNKNOWN**, not asserted absent.

### C07-D05 — The mandated outgoing QA v1.0 snapshot is absent

- **Classification:** DEFECT
- **Severity:** MEDIUM
- **Affected files:** `CHANGELOG.md`; `_SKILLS/factory-docs-update/SKILL.md`; `_SKILLS/factory-docs-update/CLAUDE.md`; expected `_ARCHIVE/QA_PLAYBOOK_v1_0.md`.
- **Precise evidence:** CHANGELOG lines 31–32 records QA_PLAYBOOK v1.0 followed by v1.1. SKILL lines 92–97 and skill D7 line 96 require an archive before each doc bump; governing `_ARCHIVE/README.md` lines 11–15 agrees. The live QA header is v1.1. Path checks find `_ARCHIVE/QA_PLAYBOOK_v0_1.md` but no `_ARCHIVE/QA_PLAYBOOK_v1_0.md`.
- **Why a defect:** The required visible snapshot for a recorded intermediate outgoing version is missing; no same-run-bump exception is stated. The issue is compliance with the promised archive contract, not whether Git might retain equivalent history.
- **Operational consequence:** A reader using the archive as instructed cannot inspect or recover that outgoing version through the promised path; the archive/update completion process has not verified a mandatory artifact.
- **Recommended resolution:** Reconcile the missing snapshot against authoritative history through a separately approved correction, and make archive existence/content checks part of completion for every recorded bump, including multiple bumps in one run.
- **Confidence / limits:** High for the path gap. No old QA snapshot or Git commit body was read, and no claim of irreversible content loss is made.

### C07-D07 — Required pre-approval evidence writes conflict with absolute no-write rules

- **Classification:** DEFECT
- **Severity:** MEDIUM
- **Affected files:** root `CLAUDE.md`; `_SKILLS/factory-docs-update/CLAUDE.md`.
- **Precise evidence:** Root CLAUDE lines 51–55 requires writing a PENDING_APPROVAL plan before presenting it, and lines 209–237 requires every substantive artifact to be saved before screen output, with both response and session writes. Root lines 171–175 says every modifying tool call must stop if the plan is unapproved; lines 82–87 forbids all writes in Plan Mode. Skill D2 line 86 likewise forbids all file writes before the presented plan is approved, despite its scope allowing session artifacts later (D10, line 102). Root session start lines 443–452 also requires immediate session-file creation before the user task.
- **Why a defect:** The same artifact must be persisted before approval, but the modifying call needed to persist it is forbidden until approval. There is no scoped exception for planning/response evidence. The issue is the instruction contract, regardless of whether a particular harness permits a plan file.
- **Operational consequence:** Agents either omit required crash-recovery evidence, write contrary to an absolute rule, or stall asking for an extra undocumented approval merely to present the requested plan.
- **Recommended resolution:** Define a narrow pre-approval evidence surface and its permitted operations; distinguish it from implementation writes. Align root and skill-local protocol instead of relying on an agent to invent the exception.
- **Confidence / limits:** High for the written contradiction. No assertion was made about current Claude Code's physical tool removal; the root's harness-enforcement claim is unverified here. The user-authorized review report overrides these lower-priority logging surfaces in this examination.

### C07-D08 — Root recovery resumes historical intent without validating its current identity

- **Classification:** DEFECT
- **Severity:** MEDIUM
- **Affected files:** root `CLAUDE.md`; `RECOVERY.md`.
- **Precise evidence:** Root CLAUDE lines 254–276 defines a three-field recovery record and tells a new session to read recovery/session files “then resume.” Lines 443–452 puts them before the user task, even saying before reading the first user message. Its session template records a branch at line 467 but no base/current revision or approval-to-revision binding. Current RECOVERY lines 3–8 is an August 10 close-out record with a named housekeeping task and “Standing rules,” while this examination starts on the independently verified September review branch. Skill D15a line 114, by contrast, explicitly inventories real branches, commits and partial work before adoption.
- **Why a defect:** The generic root recovery path lacks the state/authority reconciliation already present in the specialist skill. A dated next-step memo is not proof that its branch, pending approval or instructions remain current.
- **Operational consequence:** A fresh agent may resume an obsolete task or rely on historical approval instead of discovering the live branch and present user authorization. The stated plan gate limits damage but does not resolve which plan/state is eligible to resume.
- **Recommended resolution:** Treat root recovery as a pointer to historical execution state; require current request, branch/revision, dirty-tree and approval reconciliation before resuming. Reuse the existing evidence-first D15a principle with explicit task identity.
- **Confidence / limits:** High for the protocol gap; no assertion that the old housekeeping PR is still open or that an actual agent resumed it incorrectly. Root dated session logs were not opened, and this review did not update RECOVERY.

### C07-D09 — Close-out requires inbox writes excluded by the skill's write boundary

- **Classification:** DEFECT
- **Severity:** MEDIUM
- **Affected files:** `_SKILLS/factory-docs-update/CLAUDE.md`; `_SKILLS/factory-docs-update/SKILL.md`.
- **Precise evidence:** Skill D10, CLAUDE line 102, permits approved doctrine, new docs, MANIFEST, CHANGELOG, archive additions and session artifacts; “Everything else in the Hub” is read-only. SKILL lines 130–135 requires `_INBOX/` to end EMPTY and pack/lessons entries to be marked ENCODED after merge. The input pack/cargo is not an approved live doctrine target, archive addition or response/session artifact simply because the run consumes it.
- **Why a defect:** The close-out operation entails moving/removing or updating inputs on a surface the always-on boundary does not authorize. Gate-approved doctrine edits and post-merge disposition of cargo are distinct writable scopes, with no explicit exception joining them.
- **Operational consequence:** A literal reader cannot satisfy both “nothing floats / inbox empty” and the read-only boundary without an undocumented scope interpretation or a new override.
- **Recommended resolution:** Name the permitted cargo disposition/update surfaces and approval conditions in D10 and close-out, including preservation destinations and separately permissioned project lessons. Keep arbitrary repository cleanup forbidden.
- **Confidence / limits:** High for textual mismatch; MEDIUM because the intended operation is understandable and explicitly described. This is not a claim that emptying an approved cargo bay always requires a new user permission request.

### C07-D04 — MANIFEST's declared inventory and reverse-map provenance disagree with its own data

- **Classification:** DEFECT
- **Severity:** MEDIUM
- **Affected file:** `MANIFEST.md`.
- **Precise evidence:** Lines 6, 12 and 76 claim 29 live docs. Fresh enumeration finds **31 tier files and 31 forward rows**: 3 constitution + 6 agents + 9 methodology + 7 reference + 6 design. No live tier file is missing from the forward index. Line 76 says the reverse map is computed by inverting those lists, but line 83 includes `FFM_PLAYBOOK` as a header-declared reference to `APP_FACTORY_BLUEPRINT`; FFM's forward row at line 40 and actual header line 4 do not declare that edge. MANIFEST itself puts the same edge among body-only undeclared references at line 125. The appendix line 114 still describes a scan of 27 bodies.
- **Why a defect:** The index's completeness total is wrong and one dependency is simultaneously declared and undeclared. Those are current internal contradictions, established without relying on any earlier campaign's report.
- **Operational consequence:** Reviewers cannot treat counts or dependency provenance as mechanically reliable, and future maps inherit incorrect classification or stale coverage assumptions.
- **Recommended resolution:** Recompute totals and inverse edges from a single declared source; date/scope the body-only appendix separately. Validate the two directions and allow explicit documented exceptions such as BIM's `Governed by` header.
- **Confidence / limits:** High. The BIM→SOFTWARE_FACTORY edge was separately checked and is valid under MANIFEST's explicit `Governed by` exception; it is not counted as a defect. Core forward paths and version/date fields are otherwise in good agreement with current headers, including the disclosed nonstandard Starter Kit header.

### C07-D10 — Root CHANGELOG instructions prescribe a competing record format

- **Classification:** DEFECT
- **Severity:** LOW
- **Affected files:** root `CLAUDE.md`; `CHANGELOG.md`.
- **Precise evidence:** Root CLAUDE lines 712–726 requires a timestamped `## YYYY-MM-DD HH:MM UTC — [CC] Claude Code` heading with Updated/Reason bullets for every documentation/playbook edit. CHANGELOG lines 6 and 22 instead defines a gate-ledger row with date, doc version, one-line change and finding/lesson IDs; its ongoing entries at 24–34 follow that row convention. The skill calls for updating CHANGELOG but does not resolve these competing root instructions.
- **Why a defect:** Both instructions govern the same artifact and updates but require different shapes and provenance fields. Following the agent bootstrap does not produce the artifact's stated row format.
- **Operational consequence:** Mixed records, inconsistent version/origin traceability and unnecessary clarification for routine one-file updates.
- **Recommended resolution:** Make root CLAUDE point to the canonical CHANGELOG format, distinguishing session/response timestamps from the repository change ledger.
- **Confidence / limits:** High for format disagreement; LOW because both forms remain human-readable and this alone does not lose the code/doc change.

### C07-D11 — The skill promises CI on pushes that the workflow does not cover

- **Classification:** DEFECT
- **Severity:** LOW
- **Affected file:** `_SKILLS/factory-docs-update/CLAUDE.md`; supporting `.github/workflows/doctrine-lint.yml`.
- **Precise evidence:** Skill D9 line 100 states that Hub CI lints run “on every push.” The workflow lines 3–7 runs on pushes to `main` and pull requests targeting `main`. A push to the skill's `docs/<topic>-<date>` branch before PR creation satisfies neither trigger.
- **Why a defect:** The described automatic verification event does not match the configured event filter.
- **Operational consequence:** The agent/Operator can expect a lint result from an initial topic-branch push that never starts a workflow. PR validation remains available, limiting impact.
- **Recommended resolution:** State the actual CI triggers and name any required local pre-push validation separately; do not imply branch publication itself guarantees a check.
- **Confidence / limits:** High for the tracked workflow; remote branch protection and externally installed workflows were not verified. No CI run was triggered.

## 8. RANKED SUGGESTIONS

**3 suggestions**, ranked by expected value. None requires a large release/synchronization architecture.

### C07-S01 — Give a fresh reader one small repository landing map

- **Classification:** SUGGESTION
- **Evidence:** Root README is two lines; MANIFEST routes tier doctrine well but does not index the current skill, root operational instructions, lint entry point or evidence locations. The skill README itself is a useful cold-start runbook.
- **Recommended direction:** Add a short root entry map pointing to MANIFEST, update skill/runbook, lints and archive rules, with explicit labels for current doctrine, operational skill, execution record and historical evidence. Link the existing sources instead of copying their rules.
- **Value / limits:** Improves discoverability without claiming the current repository is un-navigable or that one local skill needs a complex registry.

### C07-S02 — Extend mechanical checks in proportion to the assurance needed

- **Classification:** SUGGESTION
- **Evidence:** The four existing lints check encoding signatures, one retired term, versioned reference syntax and header presence. They do not validate target/anchor existence, manifest equality, archive completeness, allowed status transitions, skill-local references or semantic agreement. Their scope omits `_SKILLS/` and root agent instructions; this is visible in `lints/lint_common.py` lines 21–47.
- **Recommended direction:** Consider small read-only checks for index/header/count agreement, approved archive requirements and resolvable local paths, plus the already-required skill activation test. Name each check's limits and record fresh before/after findings so known reds do not become a blanket waiver. Keep semantic review explicit.
- **Value / limits:** A bounded improvement to intentionally narrow checks. The existing lints are not defective merely because they cannot prove every governance property; specific current contradictions are counted separately.

### C07-S03 — Make skill release and retirement evidence easy to locate

- **Classification:** SUGGESTION
- **Evidence:** Skill CLAUDE line 154 and Skills Playbook §§12/15 require version history and fresh-context testing, but the primary package has no concise record binding a distributable version to an activation result, compatible doctrine revision and replacement/retirement decision. Its optional `examples/` location is absent; current run records live outside the package.
- **Recommended direction:** Use a small package-level record linking the tested revision, governing baseline, activation evidence and successor/deprecation status when applicable. Preserve point-in-time run records rather than rewriting them as current authority.
- **Value / limits:** Improves reuse and deprecation without asserting that this DRAFT package must already be retired or that its documented live-run claims constitute an independent fresh-context test.

## 9. CROSS-DOMAIN DEPENDENCIES

These records are not additional counted defects or suggestions.

- **DEPENDENCY — skill-authoring authority.** The package explicitly defers to `03_BUILD_METHODOLOGY/APP_FACTORY_SKILLS_PLAYBOOK.md` for its own evolution. The bounded excerpts confirm two-file anatomy, progressive disclosure, versioning, installation/distribution and fresh-context activation tests. The update skill properly excludes edits to itself and names a separate procedure; D03 concerns discovering/owning that dependent work, not removing the boundary.
- **CONTRADICTION CANDIDATE — skill type and execution role.** The package calls itself a Stark Skill under a “semi-execution / Brain Drain precedent” (skill CLAUDE line 3), yet assigns all Git mechanics to Engineer. Skills Playbook lines 64–95 defines Stark as Operator-executed, Agent as agent-executed and says to split a blurred type, while allowing a narrower document-writing Brain Drain precedent at line 72. The package's exact operational roles are clear, so this classification mismatch is left for the skill-authoring owner rather than counted as an authority failure.
- **DEPENDENCY — document-change verification versus application QA.** The skill assigns diff/lint evidence to its Conductor and final review/merge to Operator. It does not claim independent application Gate Q certifies documentation changes. No broader QA domain was opened to impose that ceremony. Whether a particular doctrine change also requires independent specialist review belongs in its approval/acceptance scope.
- **CONTRADICTION CANDIDATE — root engineering instructions.** Root CLAUDE says every module follows Build → Unit Test (lines 363–381), while its Test First section says write the defining test before implementation (417–425). It also says code serves project specs (396–399), whereas skill D13 distinguishes observed reality from documentary claims. Clarify context and precedence with the build/role owners; this chunk does not decide technical TDD, service, state or framework doctrine.
- **DEPENDENCY — delivery design authority.** MANIFEST and archive rules expressly cite the Hub Design's specific versioning/release sections. Those sections were consulted as a current explicit dependency despite their DRAFT location; historical audit argumentation and findings sections were not consulted or treated as evidence. D06 identifies the incomplete active delivery contract.
- **SYNTHESIS FLAG — current mechanisms versus historical process notes.** The response files contain dated plans, pending gates, final summaries and refinement proposals. Their text is historical execution evidence, not this examiner's verified account of earlier behavior. No claim in those records was adopted as a new standing rule; no prospective refinement batch or past review conclusion was used to establish a defect.

## 10. AMBIGUITIES / UNKNOWNS

- **UNKNOWN — remote enforcement and releases:** `git ls-remote --tags origin 'doctrine-*'` failed with “Could not resolve host: github.com.” No local matching tags exist, but remote tags, branch protection, required checks and current PR states were not verified. Claims that protection enforces a rule “as physics” remain claims.
- **UNKNOWN — downstream state:** Installed skill copies, zip provenance, actual project `DOCTRINE_VERSION` files, deliberate old-baseline pins and local modifications were outside this checkout. D06 does not claim those deployments lack tags or records.
- **UNKNOWN — fresh-context skill certification:** The canonical test procedure exists. This examination did not activate the mutating skill, spawn a test agent, modify a fixture repo or certify the response records' historical claims. No `examples/` directory exists in the current package; successful prior cold-start certification is not inferred from that absence or from the records.
- **UNKNOWN — runtime harness guarantees:** Root CLAUDE's claims about physical Plan Mode tool removal were not tested. Platform-specific frontmatter/tool names and GitHub MCP behavior depend on the installed harness; this review assessed the printed operational contract without certifying current external APIs.
- **UNKNOWN — images and diagrams beyond this scope:** No raster/vector/diagram asset files were found under the five tier folders, `_SKILLS/` or `agent_docs/`. Inline trees/diagrams live in their containing Markdown. A separate asset release/replacement policy was not established, but no current asset-dependent failure is alleged.
- **UNKNOWN — global deprecation/status vocabulary:** Active, living, field-tested and DRAFT labels exist; the examined active governance does not supply one transition/compatibility table covering every document/skill state. This is not evidence of an actual invalid approval or of a need for a complex lifecycle engine.
- **Session/model limitation:** The session is identified as GPT-6 and assigned the Astra examiner role; exact backend variant and HIGH reasoning configuration are not independently attestable from available tools. The conversation inherits earlier work context, so this is not a technically empty context window. No prior chunk report was opened for this examination and no prior conclusion was used as evidence. No sub-agents or secondary reviewers were consulted.
- **Read discipline:** Some batched outputs were truncated. The missing skill-CLAUDE tail and Phase 2 response file were reread explicitly before marking coverage complete. Historical response artifacts were read because `agent_docs/` is primary scope; their conclusions were not used to validate this review's claims. Root dated session logs and prohibited review/disposition/synthesis artifacts were not read.

## 11. COVERAGE MANIFEST

### Assigned primary sources — fully examined

**19 files, 1,998 lines.** Root files are current repository inputs; response files are examined as historical execution artifacts, not canonical doctrine. All primary substantive content was read completely, including examples, templates, checklists and histories. Missing portions from truncated batches were explicitly reread.

| Primary file | Status | Full extent |
|---|---|---|
| `CLAUDE.md` | EXAMINED | 1–744 |
| `MANIFEST.md` | EXAMINED | 1–137 |
| `README.md` | EXAMINED | 1–2 |
| `RECOVERY.md` | EXAMINED | 1–8 |
| `CHANGELOG.md` | EXAMINED | 1–38 |
| `_SKILLS/factory-docs-update/CLAUDE.md` | EXAMINED | 1–162 |
| `_SKILLS/factory-docs-update/README.md` | EXAMINED | 1–126 |
| `_SKILLS/factory-docs-update/SKILL.md` | EXAMINED | 1–174 |
| `_SKILLS/factory-docs-update/decision-trees/route-selection.md` | EXAMINED | 1–46 |
| `_SKILLS/factory-docs-update/references/ANTI_PATTERNS.md` | EXAMINED | 1–70 |
| `_SKILLS/factory-docs-update/references/TOOL_ROUTING.md` | EXAMINED | 1–74 |
| `_SKILLS/factory-docs-update/templates/LESSONS_LEARNED.md` | EXAMINED | 1–43 |
| `_SKILLS/factory-docs-update/templates/RIPPLE_MAP.md` | EXAMINED | 1–46 |
| `agent_docs/RESPONSES/response_2026-08-10_192235_phase1-intake-triage.md` | EXAMINED; historical execution evidence | 1–74 |
| `agent_docs/RESPONSES/response_2026-08-10_194109_phase2-ripple-map.md` | EXAMINED; historical execution evidence | 1–85 |
| `agent_docs/RESPONSES/response_2026-08-10_194500_phase3-route-decision.md` | EXAMINED; historical execution evidence | 1–15 |
| `agent_docs/RESPONSES/response_2026-08-10_200500_gate4-precheck.md` | EXAMINED; historical execution evidence | 1–57 |
| `agent_docs/RESPONSES/response_2026-08-10_201500_phase5-pr-handoff.md` | EXAMINED; historical execution evidence | 1–38 |
| `agent_docs/RESPONSES/response_2026-08-10_203000_run-summary.md` | EXAMINED; historical execution evidence | 1–59 |

**Excluded root historical files (not opened):** `session_2026-07-07.md`, `session_2026-07-08.md`, `session_2026-07-12.md`, `session_2026-08-05.md`, `session_2026-08-10.md`. They are dated execution history, not current primary doctrine under the Execution Plan's exclusion. RECOVERY's pointer was sufficient to assess its resume protocol without reading the old task logs. No other substantive current root file was found requiring primary inclusion.

### Bounded supporting reads

| Supporting source | Status / scope | Reason |
|---|---|---|
| `_ARCHIVE/README.md` | CROSS-REFERENCE — all 21 lines | Explicit MANIFEST/CHANGELOG/skill authority for archive, naming and per-bump obligations |
| `_OTHERS/DOCTRINE_HUB_DESIGN_v0_1.md` | CROSS-REFERENCE — lines 1–8, 14–55, 64–69 only | Explicit MANIFEST dependency for release tags, distribution, naming, ownership and parked automation; inspect authority status, not historical audit findings |
| `03_BUILD_METHODOLOGY/APP_FACTORY_SKILLS_PLAYBOOK.md` | CROSS-REFERENCE — heading discovery; lines 34–153, 416–429, 492–500, 588–636, 678–724, 1010–1045, 1047–1087 | Verify the primary skill's declared governing source: anatomy, type, activation, installation, approval, evolution, fresh-context testing and distribution |
| `.github/workflows/doctrine-lint.yml` | CROSS-REFERENCE — all 18 lines | Verify promised CI events and actual validator entry point |
| `lints/README.md` | CROSS-REFERENCE — all 36 lines | Verify advertised assurance, live scope and exclusions |
| `lints/run_all.py` | CROSS-REFERENCE — all 22 lines | Check the runner is read-only and determine the exact validation calls |
| `lints/lint_common.py` | CROSS-REFERENCE — all 80 lines | Verify scan targets avoid prohibited artifacts; inspect exemptions and runtime scope |
| `lints/header_lint.py` | CROSS-REFERENCE — all 33 lines | Determine header validation assurance and limits |
| `lints/versioned_refs_lint.py` | CROSS-REFERENCE — all 55 lines | Verify reference matching, canonical-name derivation and exclusions |
| `lints/encoding_lint.py` | CROSS-REFERENCE — all 45 lines | Verify byte-signature/fence scope and read-only execution |
| `lints/retired_terms_lint.py` | CROSS-REFERENCE — all 31 lines | Verify retired-term scope and read-only execution |

### Mechanical checks of referenced tier documents

The current lints read all tier Markdown plus MANIFEST/CHANGELOG; this was a bounded check of the governance mechanism, **not substantive review of those domains**. The following 31 tier sources also had their first ten header lines extracted mechanically to check index identity/version/date/status. No body-level technical conclusions were drawn. FFM, BIM and SOFTWARE_FACTORY headers were additionally displayed through line 12 to resolve the precise reverse-map/`Governed by` question.

- CROSS-REFERENCE — `01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md`: header/index comparison and documented lint scan only.
- CROSS-REFERENCE — `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md`: header/index comparison and documented lint scan only.
- CROSS-REFERENCE — `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md`: header/index comparison and documented lint scan only.
- CROSS-REFERENCE — `02_PIPELINE_AGENTS/ARCHITECT_PLAYBOOK.md`: header/index comparison and documented lint scan only.
- CROSS-REFERENCE — `02_PIPELINE_AGENTS/ARCHITECT_QUESTIONNAIRE.md`: header/index comparison and documented lint scan only.
- CROSS-REFERENCE — `02_PIPELINE_AGENTS/DESIGNER_PLAYBOOK.md`: header/index comparison and documented lint scan only.
- CROSS-REFERENCE — `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md`: header/index comparison and documented lint scan only.
- CROSS-REFERENCE — `02_PIPELINE_AGENTS/HANDOFF_PACKAGE_PLAYBOOK.md`: header/index comparison and documented lint scan only.
- CROSS-REFERENCE — `02_PIPELINE_AGENTS/RECON_QUESTIONNAIRE.md`: header/index comparison and documented lint scan only.
- CROSS-REFERENCE — `03_BUILD_METHODOLOGY/APP_FACTORY_SKILLS_PLAYBOOK.md`: header/index comparison and documented lint scan only; bounded additional skill-governance excerpts listed above.
- CROSS-REFERENCE — `03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md`: header/index comparison and documented lint scan only.
- CROSS-REFERENCE — `03_BUILD_METHODOLOGY/BUG_FIX_PLAYBOOK.md`: header/index comparison and documented lint scan only.
- CROSS-REFERENCE — `03_BUILD_METHODOLOGY/FEAT_PLAYBOOK.md`: header/index comparison and documented lint scan only.
- CROSS-REFERENCE — `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md`: header/index comparison and documented lint scan only.
- CROSS-REFERENCE — `03_BUILD_METHODOLOGY/FRONTEND_BUILD_PHASE_PLAYBOOK.md`: header/index comparison and documented lint scan only.
- CROSS-REFERENCE — `03_BUILD_METHODOLOGY/FRONTEND_FIRST_PLAYBOOK.md`: header/index comparison and documented lint scan only.
- CROSS-REFERENCE — `03_BUILD_METHODOLOGY/QA_PLAYBOOK.md`: header/index comparison and documented lint scan only.
- CROSS-REFERENCE — `03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md`: header/index comparison and documented lint scan only.
- CROSS-REFERENCE — `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md`: header/index comparison and documented lint scan only.
- CROSS-REFERENCE — `04_REFERENCE_MANUALS/APP_ARCHITECTURE_MANUAL.md`: header/index comparison and documented lint scan only.
- CROSS-REFERENCE — `04_REFERENCE_MANUALS/AUTH_MANUAL.md`: header/index comparison and documented lint scan only.
- CROSS-REFERENCE — `04_REFERENCE_MANUALS/DATABASE_MANUAL.md`: header/index comparison and documented lint scan only.
- CROSS-REFERENCE — `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md`: header/index comparison and documented lint scan only.
- CROSS-REFERENCE — `04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md`: header/index comparison and documented lint scan only.
- CROSS-REFERENCE — `04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md`: header/index comparison and documented lint scan only.
- CROSS-REFERENCE — `05_DESIGN_SYSTEM/COMPONENT_REGISTRY.md`: header/index comparison and documented lint scan only.
- CROSS-REFERENCE — `05_DESIGN_SYSTEM/GLOBAL_DESIGN_SYSTEM_HANDBOOK.md`: header/index comparison and documented lint scan only.
- CROSS-REFERENCE — `05_DESIGN_SYSTEM/THEME_LIBRARY.md`: header/index comparison and documented lint scan only.
- CROSS-REFERENCE — `05_DESIGN_SYSTEM/THEMING_MANUAL.md`: header/index comparison and documented lint scan only.
- CROSS-REFERENCE — `05_DESIGN_SYSTEM/TOKEN_FILE.md`: header/index comparison and documented lint scan only.
- CROSS-REFERENCE — `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md`: header/index comparison and documented lint scan only.

### Verification evidence

- Fresh `PYTHONDONTWRITEBYTECODE=1 /usr/bin/python3 lints/run_all.py`: ENCODING PASS; RETIRED-TERMS PASS; VERSIONED-REFS FAIL (8); HEADER-PRESENCE FAIL (1). **33 scanned files = 31 tier files + MANIFEST + CHANGELOG.** No cache files were written.
- Current versioned-reference hits: `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md` lines 258, 261, 688, 690, 692; `04_REFERENCE_MANUALS/DATABASE_MANUAL.md` lines 8, 156; `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md` line 2092. Header miss: `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md` line 1. These are independently observed existing findings, not imported counts from response records or added defects in neighboring domains.
- Forward index versus disk: 31 rows / 31 files / zero unindexed live tier files. Header version/date values agree; the Starter Kit exception is disclosed. Reverse-map validation isolates the FFM→BLUEPRINT discrepancy; BIM's governed-by edge was checked and accepted.
- Archive existence checks: `QA_PLAYBOOK_v0_1`, `BUG_FIX_PLAYBOOK_v0_1`, `SOFTWARE_FACTORY_PLAYBOOK_v1_2` exist; `QA_PLAYBOOK_v1_0` does not. Snapshot contents and old commit bodies were not read.
- Primary/source path discovery found no `DOCTRINE_SYNC_MANIFEST` or `DOCTRINE_VERSION` file in the permitted filename inventory. Downstream repositories were not searched.
- Git tag listing was read-only; remote listing failed due DNS. No checkout, fetch, pull, push, commit, merge, branch creation/deletion or history modification occurred.

### Examination controls and independence

- `astra-review/run-002/packets/CHUNK_REVIEW_CONTRACT.md`: reread completely at this examination's start.
- `astra-review/run-002/packets/EXECUTION_PLAN.md`: only Chunk 07, lines 445–493, extracted using exact entry boundaries.
- Read-only branch/status/revision and applicable AGENTS discovery established the starting environment. No applicable AGENTS file was found.
- No prior Astra chunk report, Sol/Fable review, disposition, Run 001 finding or synthesis artifact was opened. Historical references embedded in assigned source files were not treated as independent review evidence. Only the authorized Chunk 07 report was written, incrementally.

## 12. SYNTHESIS HANDOFF

- **Strongest conclusion:** The Factory has a substantive governed update system, not merely an informal collection of documents. Its current literal instructions still disagree at execution boundaries, and its dependency/distribution model does not cover every active operational consumer.
- **Most serious finding:** C07-D01 — a supposedly read-only activation can mutate a checkout before approval/resume safeguards. C07-D02 is the related but distinct publication-gate ordering failure; C07-D03 is the principal synchronization-completeness weakness.
- **Most important strength:** The explicit promotion workflow combines human approval, provenance labels, versioned outgoing snapshots and evidence-first interrupted-run adoption. Preserve those mechanisms and correct their inconsistencies.
- **Unresolved issue most likely to affect another domain:** Who owns updating/verifying installed skills and downstream doctrine pins after their canonical source changes; actual deployed-copy state remains UNKNOWN.
- **Findings deserving later Factory-wide consideration:** D03 (operational-consumer ripple coverage), D06 (merged doctrine versus released/distributed baseline), D07/D08 (root instruction and recovery authority). These are bounded handoff items, not a Factory-wide score or disposition.

No synchronization campaign was designed, no skill or doctrine was repaired, no journal was promoted, and no synthesis or final disposition was performed. Stop after the Chunk 07 completion summary.
