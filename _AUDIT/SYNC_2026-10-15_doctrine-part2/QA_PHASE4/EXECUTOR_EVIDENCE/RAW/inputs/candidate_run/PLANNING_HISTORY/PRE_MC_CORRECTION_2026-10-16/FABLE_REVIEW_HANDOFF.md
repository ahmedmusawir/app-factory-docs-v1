# Fable review handoff — Phase 2 preparation

**DRAFT FOR EXECUTABLE-MAP REVIEW AND SUBSEQUENT INDEPENDENT SPEC DERIVATION. NOT AN EXECUTION RELEASE, MAP FREEZE, ACCEPTANCE SPECIFICATION OR QA VERDICT.**

Director: Tony. Architect: Jarvis. Engineer: Cody. QA Lead: Fable. Run: `SYNC_2026-10-15_doctrine-part2`. Baseline: `9c179392f79b70da099121fc357d3107ad3bb86e`. Review branch remains `factory-docs-review-astra-w-chunks` at `626da8d70f4db22987dc7fcc86765492072360cd`; remote not refreshed by Cody.

Tony approved eight bounded recommendations on 2026-10-16: “approve all eight ... i mean your recoms ...”. The supplied full rulings are recorded as RUL-08…15. This approves the selected policy, not every old alternative, these Engineer wording proposals, an unwritten independent specification, or implementation.

## Read in this order

1. `DIRECTOR_RULINGS_2026-10-16.md`: attributable rulings and partial decision-ID crosswalk. Earlier RUL-01…07 and AD-01 are in `INTAKE_SNAPSHOT/factory-intake/PLANNING_001/`. QA source acceptance and Architect verification are distinct records under `INTAKE_SNAPSHOT/factory-intake/INTAKE_ADDENDUM_001_v0_3/`.
2. `UPDATE_MAP.md`, `SELECTED_SCOPE_LEDGER.md`, `EXTERNAL_FOLLOWUPS.md`: current selected scope, preserved 97 findings and component-level exclusions. Map §B preserves source intent/invariants verbatim; its old proposed mapping annotations are explicitly historical. Current sections A/C/D/F/K/N/O govern the proposal.
3. `EXECUTION_PROPOSAL.patch`, `EXECUTION_PROPOSAL_INDEX.json`, `PROPOSED_CONTENT/`: exact full-file proposal. `SELECTED_EXACT_EDITS.json` records 334 ordered content edits with old/new text and IDs. `DOCUMENT_VERSION_AND_ARCHIVE_PLAN.json` covers original bytes and version/history mechanics. `POST_VERIFICATION_STATUS_TRANSITIONS.json` contains five exact conditional status/provenance edits on four paths; apply only after their named actual verification triggers. Planned dates must be reconciled with actual execution dates before approval/application.
4. `PHASE_2_TEMPLATE_TRANSLATIONS.json`, `NEW_DOCUMENT_PROPOSALS.json`, `ARCHIVE_RESTORATION_PROPOSAL.json`: source-to-proposal mechanics. The accepted 25-file v0.3 source set is unchanged. Source acceptance is settled; translated installation remains to be approved and verified. `DRAFTS/` contains Opy’s original three playbook drafts and QAM substitution ledger, unchanged and not independent authority.
5. `SEARCH_QUERIES.json`, `PROPAGATION.tsv`, `PHASE_2_SEMANTIC_REVIEW.md`: every baseline hit, exact quote, disposition and limitations. Seven original mapping parts are under `scratchpad/map_parts/`; their older proposal labels are history, not current policy decisions.
6. `PHASE_2_VERIFICATION.json`, `PHASE_2_VERIFY_RAW.txt`, `PROPOSED_LINT_CHECK.txt`, `PHASE_2_CONTRAST_CHECK.json`: Engineer checks only. `BASELINE_CONTENT/` contains exact pinned-main canonical bytes. `CERTIFIED_REVIEW/` contains the original certified disposition and prior convergence QA record, not QA of this proposed sync.
7. `GOVERNING_SKILL_MAIN/_SKILLS/factory-docs-update/CLAUDE.md`, `sync-engineer/SKILL.md`, `sync-qa/SKILL.md`, and `_shared/references/STANDING_INVARIANTS.md`: governing main skill, exported read-only at the pinned baseline. Use the current seats named above. Tony’s run-specific instructions override historical seat names, agent-Git permission, and the per-document commit rule. No skill rewrite is proposed.

## Proposed implementation footprint

93 canonical/archive paths: 31 revised existing documents across all five tiers; QAM, RRM and Deployment playbooks; 25 QAM template files; 31 exact outgoing archives; restored historical QA v1.0; MANIFEST and CHANGELOG. The file index is authoritative for path count. Copied `PROPOSED_CONTENT/lints/` files are unchanged check inputs and are excluded from that implementation index.

The proposal reconciles actual old sections, diagrams, templates, boot prompts and checklists. It changes ownership to Architect DATA_CONTRACT before Design / Designer UI_SPEC / Architect assembly; makes prepared QAM mandatory; carries the exact-candidate continuing QA branch, cleanup and verified exclusion rules; preserves independent QA and Architect closeout; reconciles authority, personal-data defaults, pins and canonical references. Unsupported unsafe executable examples are explicitly withdrawn, including dependent examples, instead of retained beneath a warning. This reduces example code materially and warrants whole-diff review. It supplies no universal quote-storage or subscription schema.

## Tracked exclusions and limits

External kit interfaces/session architecture/rail behavior, root instructions, skill consumers, CI/settings/tooling and missing platform procedures remain separate. Jarvis coordinates the named custodians; `EXTERNAL_FOLLOWUPS.md` lists each component, owner responsibility and resolving trigger. Existing context-specific deployment permissions remain; no cloud authority is added. Universal quote storage and subscription schema are explicitly deferred. A withdrawal may contain a bad recipe without closing its replacement or full certified finding. FC-085/086/097 remain NO correction; all severities remain certified. No claim that all 97 findings are resolved.

Numerical contrast checks are not browser/accessibility certification. No runtime code, platform deployment, kit behavior or independent acceptance was tested in this preparation. All canonical destinations are unchanged. New draft statuses and installation-pending labels reflect that fact; conditional transitions cannot run early.

## Required review sequence and outstanding dependencies

- Jarvis reviews the selected exact wording and exclusions; Tony approves the exact UPDATE_MAP at Gate 2, including full proposal files, conditional status transitions, NO-CHANGE dispositions, baseline and LARGE route. Until then this handoff is review material only.
- After Gate 2, Fable independently derives `DOCSET_SYNC_ACCEPTANCE_SPEC.md` using the approved map, approved cargo and standing invariants. No Engineer-authored acceptance specification is supplied. Map §M records source-required verification; it is not Fable’s approval or a replacement for independent derivation. Tony approves the independent specification at Gate 3.
- Tony performs preservation, remote-baseline confirmation and execution-worktree setup using `OPERATOR_NEXT_STEPS.md`; return actual SHAs and status. Cody verifies the transferred snapshot, base and worktree before any canonical execution. Do not merge the review branch’s older skill copy.
- Phase 3 requires those completed gates and an explicit released implementation assignment. The one implementation commit exception applies only to this sync; Tony still owns all Git mutations. Necessary preservation, QA-repair and closeout commits remain possible.

## Package and source-path interpretation

The ZIP is a snapshot of this existing run, not a regenerated copy of the earlier Jarvis review ZIP. `FILE_INVENTORY_SHA256.json` and `SHA256SUMS.txt` cover every payload file; inventory files themselves are excluded from their own lists. Verify extracted bytes before review.

Original source paths such as `factory-intake/...` resolve within `INTAKE_SNAPSHOT/` at the same relative path. Canonical before-images resolve in `BASELINE_CONTENT/`; after-images in `PROPOSED_CONTENT/`. Main skill paths resolve beneath `GOVERNING_SKILL_MAIN/`. These are export roots, not proposed project landing paths. `PLANNING_HISTORY/`, old draft-verification reports and original generators preserve earlier states; they do not override the current records listed above. Do not execute copied scripts as an implementation instruction.
