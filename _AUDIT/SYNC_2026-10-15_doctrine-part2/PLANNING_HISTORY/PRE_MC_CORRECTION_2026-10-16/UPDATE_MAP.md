# UPDATE MAP — doctrine-part2 — Phase 2 reconciliation

**Scope approved 2026-10-16; exact executable map NOT approved; Phase 3 NOT released.** Tony’s attributable RUL-08…15 are in DIRECTOR_RULINGS_2026-10-16.md. They resolve the selected policy questions only. The prior review draft is preserved in PLANNING_HISTORY/PRE_PHASE2_UPDATE_MAP.md; its historical OPEN labels and unselected alternatives are not current rulings.

Current exact proposal: EXECUTION_PROPOSAL.patch + EXECUTION_PROPOSAL_INDEX.json + PROPOSED_CONTENT/. Ordered content edits: SELECTED_EXACT_EDITS.json. These remain Engineer proposals, never independent acceptance or completed canonical implementation. Dates in review copies are planned 2026-10-16; at execution record the actual landing date consistently without fabricating an earlier completion. New playbooks stay DRAFT in this review tree; any Active transition must follow actual authorized landing/verification and be recorded.

**Engineer preparation ready for map/spec review:** exact proposals, scope ledger, baseline-hit dispositions and integrity checks are recorded. Gate 2 is NOT approved; independent acceptance remains unwritten; operator preservation/setup is pending. See PHASE_2_SEMANTIC_REVIEW.md and PHASE_2_VERIFICATION.json.

## 0. Run header

| Field | Value and evidence |
|---|---|
| Active run | `_AUDIT/SYNC_2026-10-15_doctrine-part2/`; existing run reused |
| Current branch / HEAD | `factory-docs-review-astra-w-chunks` / `626da8d70f4db22987dc7fcc86765492072360cd` — EVIDENCE, read-only Git |
| Proposed execution branch | `docs/sync-doctrine-part2-2026-10-15`, created by Tony only after preservation and approval; not created |
| Proposed BASE_SHA | `9c179392f79b70da099121fc357d3107ad3bb86e`; local main and origin/main refs; canonical scope has empty working-tree diff against it. Remote not fetched in this takeover. Every placement is checked against these identical canonical bytes. |
| Merge target | main; Tony owns final Git actions |
| Execution route | Local Hub clone; explicit current instruction overrides the skill’s D5 agent-Git carve-out: ALL Git mutations are Tony-only |
| Route | LARGE; §P evidence. No docs-only QA waiver proposed |
| Seat arrangement | Director Tony; Architect Jarvis; QA Lead Fable; Engineer Cody. Independent QA Executor must be assigned in a fresh session; this Engineer cannot certify this work |
| Status | DRAFT; §O has no invented approval |
| Intake snapshot | Actual 189-file immutable snapshot from approved drop; INTAKE_RECEIPT.md and INTAKE_SNAPSHOT_INDEX.json. Not yet committed; Tony owns preservation. |
| Lint baseline | 9 findings, command/cwd/exit/unfiltered output in `LINT_BASELINE.txt`; eight VERSIONED-REFS and one HEADER-PRESENCE. DEC-16 authorizes the document fixes; expected candidate zero, not nine carried forward |
| Live-doc count | 31 tier documents + MANIFEST/CHANGELOG = lint’s 33 files; MANIFEST has 31 rows but states 29; appendix states 27 bodies. Three proposed new playbooks → 34 tier docs, excluding 25 template files |
| Governing skill | main at BASE_SHA, family CLAUDE.md + sync-engineer/SKILL.md v0.8-DRAFT. `DRAFT_AND_SKILL_HASHES.json` pins identities; working-tree skill is older |
| Recovery | Initial exact 33-path status in `RECOVERY_STATUS.txt`; handoff’s “28” was a miscount of its own 31 listed paths. Later additions: AGENTS.md and the 20:00 reporting response. No exact 28-path snapshot is available; no fictitious three-path delta is invented |

Relevant failure patterns: AP-16 propagation by memory; AP-22 trusting stale recovery prose; AP-23 maintaining totals independently of rows. The source archives, drafts and accepted template bytes remain preserved.

## A. Approved scope and actual intake

# Selected scope and component ledger — Phase 2

Scope approved by Tony 2026-10-16, RUL-08…15. Exact map/spec and Phase 3 remain unapproved. Source disposition fields preserved; selected edit is not closure. Intake physically copied and indexed in INTAKE_SNAPSHOT_INDEX.json.

| Finding | Certified correction | Selected component | Exact proposal evidence | Remaining component / owner / trigger |
|---|---|---|---|---|
| FC-001 | YES | SELECTED supported correction; withdrawal/containment does not close replacement | E136, E188, E216, E217, E218, E219, E220, E221, E222, E224, E258, E259, E260 | verified replacement / coherent dependent examples — Cody with Jarvis; trigger: required project/kit contract, separately released replacement and independent checks |
| FC-002 | YES | SELECTED supported correction | E151, E152 | Engineer proposes selected correction; Fable independently derives acceptance after approved map; implementation and verdict pending |
| FC-003 | YES | SELECTED supported correction | E34, E35, E36, E37, E38, E39, E40, E41, E42, E116, E117, E118, E314, E315 | Engineer proposes selected correction; Fable independently derives acceptance after approved map; implementation and verdict pending |
| FC-004 | YES | SELECTED supported correction | E137, E138, E139, E140, E141, E326, E330 | Engineer proposes selected correction; Fable independently derives acceptance after approved map; implementation and verdict pending |
| FC-005 | YES | SELECTED supported correction | E44, E59, E60, E84, E193, E248, E249, E255, E319, E320, E321, E322, E323, E324, E325 | skill precedence consumer — Jarvis coordinates named maintainer/evidence supplier; trigger: separately authorized job or supplied immutable kit revision |
| FC-006 | YES | SELECTED supported correction | E60, E239, E240, E241, E242 | skill seat terminology — Jarvis coordinates named maintainer/evidence supplier; trigger: separately authorized job or supplied immutable kit revision |
| FC-007 | YES | SELECTED supported correction | E60 | Engineer proposes selected correction; Fable independently derives acceptance after approved map; implementation and verdict pending |
| FC-008 | YES | SELECTED supported correction | E56, E57, E58, E102, E105, E106, E107, E137, E138, E139, E140, E141, E254 | root FILE_TREE alignment — Jarvis coordinates named maintainer/evidence supplier; trigger: separately authorized job or supplied immutable kit revision |
| FC-009 | YES | SELECTED supported correction | E225, E226, E227, E228, E229, E230, E231, E232, E233, E234, E235, E236, E237, E238, E314, E315 | external kit/example locators — Jarvis coordinates named maintainer/evidence supplier; trigger: separately authorized job or supplied immutable kit revision |
| FC-010 | YES | SELECTED supported correction | RUL-12 exact scope/authority proposals (FC-005/014); root classification stays outside | root authority classification — Jarvis coordinates named maintainer/evidence supplier; trigger: separately authorized job or supplied immutable kit revision |
| FC-011 | YES | SELECTED supported correction | DEPLOYMENT_PLAYBOOK exact new proposal §§2–8 | ungranted platform permissions / missing platform procedures — Jarvis coordinates; trigger: context-specific attributable authorization and procedure evidence |
| FC-012 | YES | SELECTED supported correction | E244, E245 | ungranted platform permissions / missing platform procedures — Jarvis coordinates; trigger: context-specific attributable authorization and procedure evidence |
| FC-013 | YES | SELECTED supported correction | E1, E5 | Engineer proposes selected correction; Fable independently derives acceptance after approved map; implementation and verdict pending |
| FC-014 | YES | SELECTED supported correction | E43, E44, E45, E111, E112, E113, E144, E243, E244, E245, E246, E247, E248, E249, E318, E319, E320, E321, E322, E323, E324, E325 | Engineer proposes selected correction; Fable independently derives acceptance after approved map; implementation and verdict pending |
| FC-015 | YES | SELECTED supported correction | E46 | Engineer proposes selected correction; Fable independently derives acceptance after approved map; implementation and verdict pending |
| FC-016 | YES | SELECTED supported correction | E108, E109, E110 | Engineer proposes selected correction; Fable independently derives acceptance after approved map; implementation and verdict pending |
| FC-017 | YES | SELECTED supported correction | E46, E48, E50, E53, E55, E56, E137, E138, E139, E140, E141, E173, E251, E252, E253, E326, E328, E329, E333 | Engineer proposes selected correction; Fable independently derives acceptance after approved map; implementation and verdict pending |
| FC-018 | YES | SELECTED supported correction | E147, E148, E149 | Engineer proposes selected correction; Fable independently derives acceptance after approved map; implementation and verdict pending |
| FC-019 | YES | SELECTED supported correction | E49, E143 | Engineer proposes selected correction; Fable independently derives acceptance after approved map; implementation and verdict pending |
| FC-020 | YES | SELECTED supported correction | E153, E154 | Engineer proposes selected correction; Fable independently derives acceptance after approved map; implementation and verdict pending |
| FC-021 | YES | SELECTED supported correction | E98, E99, E100, E250, E256, E279, E280, E281, E282, E283, E284, E285, E286, E287, E288, E289, E290, E291, E292, E293, E294 | Engineer proposes selected correction; Fable independently derives acceptance after approved map; implementation and verdict pending |
| FC-022 | YES | SELECTED supported correction; withdrawal/containment does not close replacement | E93 | verified replacement / coherent dependent examples — Cody with Jarvis; trigger: required project/kit contract, separately released replacement and independent checks |
| FC-023 | YES | SELECTED supported correction | E155 | Engineer proposes selected correction; Fable independently derives acceptance after approved map; implementation and verdict pending |
| FC-024 | YES | SELECTED supported correction | E150, E156, E157, E256 | Engineer proposes selected correction; Fable independently derives acceptance after approved map; implementation and verdict pending |
| FC-025 | YES | SELECTED supported correction | E11, E12, E143, E144, E145, E257, E310, E311, E312 | Engineer proposes selected correction; Fable independently derives acceptance after approved map; implementation and verdict pending |
| FC-026 | YES | SELECTED supported correction | E3, E4, E310, E311 | Engineer proposes selected correction; Fable independently derives acceptance after approved map; implementation and verdict pending |
| FC-027 | YES | SELECTED supported correction | E46, E47, E49, E51, E52, E54, E56, E58, E103, E104, E106, E137, E138, E139, E140, E141, E173, E326, E329 | Engineer proposes selected correction; Fable independently derives acceptance after approved map; implementation and verdict pending |
| FC-028 | YES | SELECTED supported correction | E158, E188 | Engineer proposes selected correction; Fable independently derives acceptance after approved map; implementation and verdict pending |
| FC-029 | YES | SELECTED supported correction | E142 | Engineer proposes selected correction; Fable independently derives acceptance after approved map; implementation and verdict pending |
| FC-030 | YES | SELECTED supported correction; withdrawal/containment does not close replacement | E94 | verified replacement / coherent dependent examples — Cody with Jarvis; trigger: required project/kit contract, separately released replacement and independent checks |
| FC-031 | YES | SELECTED supported correction | E24 | Engineer proposes selected correction; Fable independently derives acceptance after approved map; implementation and verdict pending |
| FC-032 | YES | SELECTED supported correction | E114, E115 | Engineer proposes selected correction; Fable independently derives acceptance after approved map; implementation and verdict pending |
| FC-033 | YES | SELECTED supported correction; withdrawal/containment does not close replacement | E62, E63, E136, E189, E195, E216, E217, E218, E219, E220, E221, E222, E223, E224 | verified replacement / coherent dependent examples — Cody with Jarvis; trigger: required project/kit contract, separately released replacement and independent checks |
| FC-034 | YES | SELECTED supported correction; withdrawal/containment does not close replacement | E85, E86, E87, E216, E217, E218, E219, E220, E221, E222, E224, E259, E260 | verified replacement / coherent dependent examples — Cody with Jarvis; trigger: required project/kit contract, separately released replacement and independent checks |
| FC-035 | YES | SELECTED supported correction; withdrawal/containment does not close replacement | E61, E64, E65, E66, E89, E190, E191, E196 | verified replacement / coherent dependent examples — Cody with Jarvis; trigger: required project/kit contract, separately released replacement and independent checks |
| FC-036 | YES | SELECTED supported correction | E136, E159, E160, E189, E218, E219, E220, E221, E222, E258 | Engineer proposes selected correction; Fable independently derives acceptance after approved map; implementation and verdict pending |
| FC-037 | YES | SELECTED supported correction | E96 | Engineer proposes selected correction; Fable independently derives acceptance after approved map; implementation and verdict pending |
| FC-038 | YES | SELECTED supported correction; withdrawal/containment does not close replacement | E62, E223, E260 | verified replacement / coherent dependent examples — Cody with Jarvis; trigger: required project/kit contract, separately released replacement and independent checks |
| FC-039 | YES | SELECTED supported correction; withdrawal/containment does not close replacement | E63, E88, E223 | verified replacement / coherent dependent examples — Cody with Jarvis; trigger: required project/kit contract, separately released replacement and independent checks |
| FC-040 | YES | SELECTED supported correction | E90, E101, E334 | Engineer proposes selected correction; Fable independently derives acceptance after approved map; implementation and verdict pending |
| FC-041 | YES | SELECTED supported correction; withdrawal/containment does not close replacement | E84, E189, E197, E198, E199, E200, E201, E202, E203, E204, E205, E206, E207, E208, E209, E224, E263, E264, E265, E266 | verified kit guard signature/return contract — Jarvis coordinates named maintainer/evidence supplier; trigger: separately authorized job or supplied immutable kit revision; verified replacement / coherent dependent examples — Cody with Jarvis; trigger: required project/kit contract, separately released replacement and independent checks |
| FC-042 | YES | SELECTED supported correction; withdrawal/containment does not close replacement | E84, E192, E210, E211, E261, E262, E267, E268, E269, E270 | verified kit session/cookie architecture — Jarvis coordinates named maintainer/evidence supplier; trigger: separately authorized job or supplied immutable kit revision; verified replacement / coherent dependent examples — Cody with Jarvis; trigger: required project/kit contract, separately released replacement and independent checks |
| FC-043 | YES | SELECTED supported correction | E29 | Engineer proposes selected correction; Fable independently derives acceptance after approved map; implementation and verdict pending |
| FC-044 | YES | SELECTED supported correction | E28 | Engineer proposes selected correction; Fable independently derives acceptance after approved map; implementation and verdict pending |
| FC-045 | YES | SELECTED supported correction; withdrawal/containment does not close replacement | E97 | verified replacement / coherent dependent examples — Cody with Jarvis; trigger: required project/kit contract, separately released replacement and independent checks |
| FC-046 | YES | SELECTED supported correction | E26, E27 | Engineer proposes selected correction; Fable independently derives acceptance after approved map; implementation and verdict pending |
| FC-047 | YES | SELECTED supported correction; withdrawal/containment does not close replacement | E90, E91, E92, E212, E213, E273, E274, E275, E276, E277, E278, E317 | verified replacement / coherent dependent examples — Cody with Jarvis; trigger: required project/kit contract, separately released replacement and independent checks |
| FC-048 | YES | SELECTED supported correction | E119, E120 | Engineer proposes selected correction; Fable independently derives acceptance after approved map; implementation and verdict pending |
| FC-049 | YES | SELECTED supported correction | E25 | Engineer proposes selected correction; Fable independently derives acceptance after approved map; implementation and verdict pending |
| FC-050 | YES | SELECTED supported correction; withdrawal/containment does not close replacement | E67, E69, E317 | verified replacement / coherent dependent examples — Cody with Jarvis; trigger: required project/kit contract, separately released replacement and independent checks |
| FC-051 | YES | SELECTED supported correction; withdrawal/containment does not close replacement; universal quote storage DEFERRED by RUL-11 | E67, E68, E69 | verified replacement / coherent dependent examples — Cody with Jarvis; trigger: required project/kit contract, separately released replacement and independent checks |
| FC-052 | YES | SELECTED supported correction; withdrawal/containment does not close replacement | E71, E74 | verified replacement / coherent dependent examples — Cody with Jarvis; trigger: required project/kit contract, separately released replacement and independent checks |
| FC-053 | YES | SELECTED supported correction; withdrawal/containment does not close replacement | E67, E68, E69, E73, E75 | verified replacement / coherent dependent examples — Cody with Jarvis; trigger: required project/kit contract, separately released replacement and independent checks |
| FC-054 | YES | SELECTED supported correction; withdrawal/containment does not close replacement | E71, E74 | verified replacement / coherent dependent examples — Cody with Jarvis; trigger: required project/kit contract, separately released replacement and independent checks |
| FC-055 | YES | SELECTED supported correction; withdrawal/containment does not close replacement; universal schema DEFERRED by RUL-11 | E72, E73, E74, E272, E273, E274, E275, E276, E277, E278 | verified replacement / coherent dependent examples — Cody with Jarvis; trigger: required project/kit contract, separately released replacement and independent checks |
| FC-056 | YES | SELECTED supported correction; withdrawal/containment does not close replacement | E79 | verified replacement / coherent dependent examples — Cody with Jarvis; trigger: required project/kit contract, separately released replacement and independent checks |
| FC-057 | YES | SELECTED supported correction; withdrawal/containment does not close replacement | E80, E81 | verified replacement / coherent dependent examples — Cody with Jarvis; trigger: required project/kit contract, separately released replacement and independent checks |
| FC-058 | YES | SELECTED supported correction; withdrawal/containment does not close replacement | E76, E77 | verified replacement / coherent dependent examples — Cody with Jarvis; trigger: required project/kit contract, separately released replacement and independent checks |
| FC-059 | YES | SELECTED supported correction; withdrawal/containment does not close replacement | E71, E74, E76, E78, E271 | verified replacement / coherent dependent examples — Cody with Jarvis; trigger: required project/kit contract, separately released replacement and independent checks |
| FC-060 | YES | SELECTED supported correction; withdrawal/containment does not close replacement; universal quote storage DEFERRED by RUL-11 | E67, E68, E69 | verified replacement / coherent dependent examples — Cody with Jarvis; trigger: required project/kit contract, separately released replacement and independent checks |
| FC-061 | YES | SELECTED supported correction | E95 | Engineer proposes selected correction; Fable independently derives acceptance after approved map; implementation and verdict pending |
| FC-062 | YES | SELECTED supported correction; withdrawal/containment does not close replacement | E71 | verified replacement / coherent dependent examples — Cody with Jarvis; trigger: required project/kit contract, separately released replacement and independent checks |
| FC-063 | YES | SELECTED supported correction | E170, E171, E172, E279, E280, E281, E282, E283, E284, E285, E286, E287, E288, E289, E290, E291, E292, E293, E294 | Engineer proposes selected correction; Fable independently derives acceptance after approved map; implementation and verdict pending |
| FC-064 | YES | SELECTED supported correction; withdrawal/containment does not close replacement | E183, E184, E185 | verified replacement / coherent dependent examples — Cody with Jarvis; trigger: required project/kit contract, separately released replacement and independent checks |
| FC-065 | YES | SELECTED supported correction | E30, E31, E75 | Engineer proposes selected correction; Fable independently derives acceptance after approved map; implementation and verdict pending |
| FC-066 | YES | SELECTED supported correction; withdrawal/containment does not close replacement | E183, E184, E185, E279, E280, E281, E282, E283, E284, E285, E286, E287, E288, E289, E290, E291, E292, E293, E294 | verified replacement / coherent dependent examples — Cody with Jarvis; trigger: required project/kit contract, separately released replacement and independent checks |
| FC-067 | YES | SELECTED supported correction; withdrawal/containment does not close replacement; universal quote storage DEFERRED by RUL-11 | E70, E273, E274, E275, E276, E277, E278 | verified replacement / coherent dependent examples — Cody with Jarvis; trigger: required project/kit contract, separately released replacement and independent checks |
| FC-068 | YES | SELECTED supported correction; withdrawal/containment does not close replacement | E68, E90, E273, E274, E275, E276, E277, E278 | verified replacement / coherent dependent examples — Cody with Jarvis; trigger: required project/kit contract, separately released replacement and independent checks |
| FC-069 | YES | SELECTED supported correction | E186 | Engineer proposes selected correction; Fable independently derives acceptance after approved map; implementation and verdict pending |
| FC-070 | YES | SELECTED supported correction | E161 | Engineer proposes selected correction; Fable independently derives acceptance after approved map; implementation and verdict pending |
| FC-071 | YES | SELECTED supported correction; withdrawal/containment does not close replacement | E176, E177, E178, E179, E190, E191, E295, E296, E297, E298, E299, E300 | verified replacement / coherent dependent examples — Cody with Jarvis; trigger: required project/kit contract, separately released replacement and independent checks |
| FC-072 | YES | SELECTED supported correction; withdrawal/containment does not close replacement | E84, E176, E177, E178, E179, E295, E296, E297, E298, E299, E300, E301, E302, E303, E304, E305 | verified kit rail breakpoint — Jarvis coordinates named maintainer/evidence supplier; trigger: separately authorized job or supplied immutable kit revision; verified replacement / coherent dependent examples — Cody with Jarvis; trigger: required project/kit contract, separately released replacement and independent checks |
| FC-073 | YES | SELECTED supported correction | E125, E180, E181, E182, E306, E307, E308, E309 | Engineer proposes selected correction; Fable independently derives acceptance after approved map; implementation and verdict pending |
| FC-074 | YES | SELECTED supported correction | E127, E128, E129, E130, E131, E132, E133, E134, E135 | Engineer proposes selected correction; Fable independently derives acceptance after approved map; implementation and verdict pending |
| FC-075 | YES | SELECTED supported correction | E82, E83 | Engineer proposes selected correction; Fable independently derives acceptance after approved map; implementation and verdict pending |
| FC-076 | YES | SELECTED supported correction; withdrawal/containment does not close replacement | E121, E122, E123 | verified replacement / coherent dependent examples — Cody with Jarvis; trigger: required project/kit contract, separately released replacement and independent checks |
| FC-077 | YES | SELECTED supported correction | E174, E175 | Engineer proposes selected correction; Fable independently derives acceptance after approved map; implementation and verdict pending |
| FC-078 | YES | SELECTED supported correction | E124 | Engineer proposes selected correction; Fable independently derives acceptance after approved map; implementation and verdict pending |
| FC-079 | YES | SELECTED supported correction | E121, E214, E215 | Engineer proposes selected correction; Fable independently derives acceptance after approved map; implementation and verdict pending |
| FC-080 | YES | SELECTED supported correction | E32 | Engineer proposes selected correction; Fable independently derives acceptance after approved map; implementation and verdict pending |
| FC-081 | YES | SELECTED supported correction | E116, E117, E118, E144 | Engineer proposes selected correction; Fable independently derives acceptance after approved map; implementation and verdict pending |
| FC-082 | YES | SELECTED supported correction | E126, E162, E163 | Engineer proposes selected correction; Fable independently derives acceptance after approved map; implementation and verdict pending |
| FC-083 | YES | SELECTED supported correction | E164, E165, E166, E167, E168, E187 | Engineer proposes selected correction; Fable independently derives acceptance after approved map; implementation and verdict pending |
| FC-084 | YES | SELECTED supported correction | E33 | Engineer proposes selected correction; Fable independently derives acceptance after approved map; implementation and verdict pending |
| FC-085 | NO | NO correction — regression guard only | NO canonical change | retain NO correction and inspect pinned-main regression guards; no re-open |
| FC-086 | NO | NO correction — regression guard only | NO canonical change | retain NO correction and inspect pinned-main regression guards; no re-open |
| FC-087 | YES | SELECTED supported correction | E194 | Engineer proposes selected correction; Fable independently derives acceptance after approved map; implementation and verdict pending |
| FC-088 | YES | SELECTED supported correction | E169 | ungranted platform permissions / missing platform procedures — Jarvis coordinates; trigger: context-specific attributable authorization and procedure evidence |
| FC-089 | YES | SELECTED supported correction | archive restoration plan | Engineer proposes selected correction; Fable independently derives acceptance after approved map; implementation and verdict pending |
| FC-090 | YES | OUTSIDE canonical scope | NO canonical change | root pre-approval writes — Jarvis coordinates named maintainer/evidence supplier; trigger: separately authorized job or supplied immutable kit revision |
| FC-091 | YES | OUTSIDE canonical scope | NO canonical change | root evidence-first recovery — Jarvis coordinates named maintainer/evidence supplier; trigger: separately authorized job or supplied immutable kit revision |
| FC-092 | YES | OUTSIDE canonical scope | NO canonical change | skill closeout write boundary — Jarvis coordinates named maintainer/evidence supplier; trigger: separately authorized job or supplied immutable kit revision |
| FC-093 | YES | SELECTED supported correction | derived MANIFEST/CHANGELOG proposal | Engineer proposes selected correction; Fable independently derives acceptance after approved map; implementation and verdict pending |
| FC-094 | YES | OUTSIDE canonical scope | NO canonical change | root CHANGELOG convention — Jarvis coordinates named maintainer/evidence supplier; trigger: separately authorized job or supplied immutable kit revision |
| FC-095 | YES | OUTSIDE canonical scope | NO canonical change | skill CI wording / CI trigger option — Jarvis coordinates named maintainer/evidence supplier; trigger: separately authorized job or supplied immutable kit revision |
| FC-096 | YES | SELECTED supported correction | derived MANIFEST/CHANGELOG proposal | skill merge-over-red wording / branch-protection enforcement — Jarvis coordinates named maintainer/evidence supplier; trigger: separately authorized job or supplied immutable kit revision |
| FC-097 | NO | NO correction — regression guard only | NO canonical change | retain NO correction and inspect pinned-main regression guards; no re-open |

Original 36 harvest and supporting-source classifications remain in PHASE1_LEDGER.md as historical planning; interpret them through RUL-01…15 and AD-01. Source templates and accepted behavior are not re-reviewed. Raw cargo can include historical alternatives without adopting them. Actual snapshot: INTAKE_RECEIPT.md; 189 hashes in INTAKE_SNAPSHOT_INDEX.json.

## B. Per-ID intent, preservation, dependencies and search

The source blocks below remain verbatim. Their earlier mapping-proposal/disposition annotations are retained as drafting history; SELECTED_SCOPE_LEDGER and RUL-08…15 govern current component selection, and §C exact proposals govern proposed text. No historical BLOCKED/OPEN label reopens an approved policy.





For each FC, the complete source block below preserves the certified field, evidence, proposed outcome, preservation and verification intent verbatim. **No distinct approved invariant field is invented:** the package supplies proposed outcomes and verification intent, not approved execution wording. Gate 1/2 must approve the applicable scope/wording. Domain-wide preservation in briefs 04/05 also applies (§L). Search rows are in `PROPAGATION.tsv`; query definitions and command/scope are in `SEARCH_QUERIES.json`. Exact workflow changes are incorporated in §C; broader correction wording and verified anchors remain visible below. Independent QA derives from the finally approved map, never from an Engineer’s claim of closure.

### FC-001 — Constitutional kit-build instructions (SFP §9 Phase 7, §8 page pattern) conflict with kit-consumption doctrine

**Proposed disposition:** BLOCKED. **Authority:** certified correction YES; package outcome remains proposed. CONDITIONAL: DEC-06. 

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/01_governance_corrections.md:37`):

- **Certified record:** CF-01 · Severity HIGH · Review CONFIRMED · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C01-D01 (primary) · Fable FBL-D001 (related; primary in FC-033)
- **Evidence:** Astra C01 §7 Rank 1; Sol C01 §3 and §5.A; Fable §7 FBL-D001, §9 row 4, §11 decision 1.
- **Defect surfaces (`0a787cb`):**
  - `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md` §9 Phase 7 (auth, login pages, `user_metadata` role flags, `withRoleCheck`) and §8 page-component pattern.
  - `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md` §§1–2, §5, §7 and the quick reference (DO NOT BUILD).
  - Supporting (QA-4 resolved set): `04_REFERENCE_MANUALS/AUTH_MANUAL.md`, `04_REFERENCE_MANUALS/APP_ARCHITECTURE_MANUAL.md`, `04_REFERENCE_MANUALS/DATABASE_MANUAL.md`, `04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md`, `MANIFEST.md`, `_ARCHIVE/**`.
- **Defect:**
  - The master playbook tells kit-based builders to:
    - add auth
    - create login pages
    - put role flags in `user_metadata`
    - gate layouts with a client HOC
    - fetch client-side in `page.tsx`
  - The Handbook marks these as already wired or DO NOT BUILD. It requires `protectPage`, thin page wrappers and Server Component data.
  - No applicability boundary separates generic from kit-based guidance, so both read as current instructions.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - For kit-based builds, the constitution names which document controls kit implementation patterns.
  - SFP §9 Phase 7 and §8 no longer prescribe building what the kit already provides.
  - Any generic or non-kit pattern kept in the constitution carries explicit applicability. Sol: "this generic example does not apply when Starter Kit v3 provides the capability".
  - Fable recommends Phase 7 become "consume the kit; verify with AUTH-WALK".
- **Preserve:**
  - The Handbook's recon-based reuse constraints.
  - Recon as a validity gate.
  - SFP §2.5's separation of acceptance authorship, QA verdict and Operator release.
  - Sol C01: do not blindly delete generic patterns. Do not merge C01 and C04 IDs: FC-001 is corrected alongside FC-033/FC-035 but stays its own record.
- **Likely affected docs / consumers:**
  - SFP §8, §9 and the Phase 7 checklist.
  - STARTER_KIT_HANDBOOK, as consumer and authority.
  - AUTH_MANUAL and STATE_MANAGEMENT_MANUAL, through FC-033/FC-035.
  - Engineer and Architect seats.
  - DocSet Sync propagation terms (D19): `withRoleCheck`, `user_metadata`, `is_admin`, `/login`, "Login page(s) created", "Auth store configured".
- **Verification intent:**
  1. SFP §9 Phase 7 has no kit-scope instruction to build login UI, an auth store, a role checker or metadata role flags. Any non-kit variant is explicitly scoped.
  2. The SFP §8 page pattern agrees with Handbook §5/§7, or is labeled non-kit.
  3. A live-corpus search for the propagation terms leaves no undispositioned hit.
  4. The constitution and AUTH/STATE no longer give different auth authorities (cross-check FC-033, FC-035).
- **Open decision:** DEC-02 (retire vs rewrite the legacy auth samples) and DEC-06 (kit-pattern authority / precedence, FC-005). Recommend ruling DEC-06 before or with this item.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** For kit-based builds, consume the existing kit authentication and authorization primitives and verify them through AUTH-WALK. Do not rebuild login pages, an auth store, metadata role flags or a client route guard. Page wrappers follow STARTER_KIT_HANDBOOK §5 and §7: resolve authorized server data before rendering the interactive client child. Generic non-kit examples do not apply when the kit supplies the capability.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md:632` — ## 8. Phase 6: UI Implementation; MANIFEST ← 8: APP_FACTORY_BLUEPRINT, FFM_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.
- `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md:717` — ## 9. Phase 7: Authentication & RBAC; MANIFEST ← 8: APP_FACTORY_BLUEPRINT, FFM_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.

**Touch proposal:** C-001. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-001` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-002 — Constitutional feature/release checklists omit required approval, acceptance and Gate Q checkpoints

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/01_governance_corrections.md:79`):

- **Certified record:** CF-01 · Severity MEDIUM · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C01-D02 · Fable none
- **Evidence:** Astra C01 §7 Rank 2; Sol C01 §3 (provisional MEDIUM, closed MEDIUM 2026-09-27) and §5.B.
- **Defect surfaces (`0a787cb`):**
  - `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md`: §13 Feature Development Checklist, "Pre-Release QA" checklist, §11 deployment steps (governing rules at §1 and §2.5).
  - `01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md`: "The Full Workflow".
- **Defect:** the reusable checklists can all be ticked without recording any of these:
  - brief, spec or full-screen-set approval
  - the `ACCEPTANCE_SPEC` handoff
  - a Gate Q verdict
  - an Operator release decision
  - an eligible recorded waiver

  The governing rules require all of them. The execution aid is incomplete; the constitution does not permit release without QA (Sol).
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - At their actual transition points, the §13 checklists and the §11 deployment steps carry, by link to the governing definitions, the five controls above. The waiver route appears only where it is eligible.
  - A completed checklist therefore implies those records exist.
  - No second QA procedure is created.
- **Preserve:**
  - SFP §2.5 as the single definition of these controls.
  - The Blueprint's approval checkpoints.
  - The narrow documentation-only/non-runtime waiver.
- **Likely affected docs / consumers:** SFP §11, §13; Blueprint (reference only); link targets in `03_BUILD_METHODOLOGY/QA_PLAYBOOK.md` (Gate Q §12, Gate D §13); Engineer, Operator and QA seat.
- **Verification intent:**
  - Each SFP §13 checklist contains, or links to, all five controls at the right transition.
  - §11 references the §2.5 release control.
  - Every new anchor resolves to a live heading.
  - No duplicated QA mechanics are introduced.
- **Open decision:** none required. Sol's conditional re-elevation to HIGH is not triggered by the certified record; any change is Tony's (DEC-22). Sequence with FC-013 and FC-025.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Before implementation, record approval of the brief, specifications and applicable full screen set. Before independent QA, provide the approved ACCEPTANCE_SPEC and engineering claim package. Before release, record the QA Lead’s Gate Q verdict and the Director’s release decision under §2.5. Record a documentation-only waiver only where §2.5 explicitly permits it; it is not a runtime QA waiver. Deployment verification follows QA_PLAYBOOK Gate D.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md:816` — ## 11. Phase 9: Deployment; MANIFEST ← 8: APP_FACTORY_BLUEPRINT, FFM_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.
- `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md:907` — ## 13. Checklists; MANIFEST ← 8: APP_FACTORY_BLUEPRINT, FFM_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.

**Touch proposal:** C-002. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-002` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-003 — STARTER_KIT_HANDBOOK references and conventions do not resolve against, or conform to, Hub conventions

**Proposed disposition:** BLOCKED. **Authority:** certified correction YES; package outcome remains proposed. CONDITIONAL: DEC-17 / DEC-19 remainder. 

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/01_governance_corrections.md:287`):

- **Certified record:** CF-13 · Severity MEDIUM · Review PARTIAL · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C01-D03 · Fable FBL-D003 (primary)
- **Evidence:** Astra C01 §7 Rank 3; Sol C01 §3; Fable §7 FBL-D003, §9 row 24; lint output in the QA report (QA-5, FC-096 block).
- **Defect surfaces (`0a787cb`):**
  - `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md`: header, §4, §11, §14, §15
  - `_ARCHIVE/README.md`
  - `MANIFEST.md`: Handbook row and footnote
- **Defect:**
  - The Factory's canonical kit entry point cites versioned or embedded-repository paths that do not exist in the Hub: `COMPONENT_REGISTRY_v1.1.md`, `agent_docs/APP_FACTORY/...UI-UX-BUILDING-MANUAL_v1_3.md`, `AUTH_MANUAL_v1.2.md`.
  - §11 places `KNOWN_ISSUES.md` at "repo root".
  - §14's rule that the filename carries the version contradicts `_ARCHIVE/README.md`.
  - The standard header line is missing (a lint miss).
  - Its blast radius is ←12.
- **Current-main status:** OPEN — SOURCE UNCHANGED. Lint rerun 2026-10-11: still 5 VERSIONED-REFS hits (lines 258, 261, 688, 690, 692) and 1 HEADER-PRESENCE miss.
- **Proposed outcome (PROPOSED — not approved):** the queued "F-022 redo", recorded in the MANIFEST footnote and Fable:
  - Consumer-facing doctrine references resolve through canonical names and paths.
  - References that intentionally target the kit repository or a project are labeled, with repository and revision context.
  - §14 is aligned with Hub law: canonical names, with versions only in headers, MANIFEST and `_ARCHIVE/`.
  - The standard single-line header is present.
- **Preserve:**
  - The Handbook as the canonical kit entry point and its disk-wins recon framing.
  - Doctrine references kept distinct from app-source paths (Astra).
  - The MANIFEST footnote's honest disclosure, updated rather than deleted.
- **Likely affected docs / consumers:**
  - STARTER_KIT_HANDBOOK is the highest-← doc, so DocSet Sync D14 minimal-diff discipline applies.
  - MANIFEST row/footnote; `_ARCHIVE/` (archive on bump).
  - Lints: 6 of the 9 baseline findings clear (FC-096).
  - Linked to FC-081/FC-088 (landing paths) and FC-009 (`KNOWN_ISSUES.md` locator).
- **Verification intent:**
  - `lints/run_all.py` at the candidate SHA shows no STARTER_KIT VERSIONED-REFS or HEADER-PRESENCE findings and no new hits.
  - Every doctrine path in §4/§15 resolves or is labeled external with repo and revision.
  - §14 no longer instructs filename version bumps.
- **Open decision:** DEC-17 (landing-path standard, shared with FC-081/FC-088); DEC-19 (`KNOWN_ISSUES.md` home, FC-009); scheduling the F-022 redo (Fable §11 decision 14).
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Hub doctrine references use canonical filenames. Versions belong in headers, MANIFEST and archives. A downstream-project or kit-repository path is explicitly labeled with its repository, path and pinned revision; it is not a Hub-relative link. Do not claim an external locator exists until its repository and revision are supplied.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md:666` — ## 14. Handbook Maintenance; MANIFEST ← 12: ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, FRONTEND_BUILD_PHASE_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, TESTING_PLAYBOOK, API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, DATABASE_MANUAL, STATE_MANAGEMENT_MANUAL, COMPONENT_REGISTRY, UI_UX_BUILDING_MANUAL.
- `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md:684` — ## 15. Cross-References; MANIFEST ← 12: ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, FRONTEND_BUILD_PHASE_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, TESTING_PLAYBOOK, API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, DATABASE_MANUAL, STATE_MANAGEMENT_MANUAL, COMPONENT_REGISTRY, UI_UX_BUILDING_MANUAL.

**Touch proposal:** C-003. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-003` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-004 — The constitution (Blueprint) predates the QA seat and the module era

**Proposed disposition:** BLOCKED. **Authority:** certified correction YES; package outcome remains proposed. CONDITIONAL: DEC-07 remainder. 

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/01_governance_corrections.md:112`):

- **Certified record:** CF-01 · Severity HIGH · Review UNIQUE (Fable) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra none · Fable FBL-D020
- **Evidence:** Fable §7 FBL-D020; §2 row 5.
- **Defect surfaces (`0a787cb`):**
  - `01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md`: council, router, Phase 5.
  - Cross: `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md` §2.5, `03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md` §2, `03_BUILD_METHODOLOGY/QA_PLAYBOOK.md` §2, `03_BUILD_METHODOLOGY/BUG_FIX_PLAYBOOK.md`, `03_BUILD_METHODOLOGY/FEAT_PLAYBOOK.md`, `MANIFEST.md`.
  - Process evidence: `agent_docs/RESPONSES/response_2026-08-10_203000_run-summary.md` (at `0a787cb`; it records the parked concern).
- **Defect:** MANIFEST says the Blueprint owns the pipeline router, yet:
  - it has no QA seat and no Coordinator;
  - it routes only CONVERSION and GREENFIELD (no BIM/FIX/FEAT);
  - its lifecycle ends at "Ship it", with no Gate Q or Gate D.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - The Blueprint includes the QA seat and the Coordinator, named per the FC-006 glossary.
  - Its router has a module-work branch (BIM/FIX/FEAT), delegated to those playbooks.
  - Its lifecycle passes Gate Q → deploy → Gate D → close, by reference to QA_PLAYBOOK.
  - The SFP §2.5 authority chain gets a constitutional home.
- **Preserve:**
  - The recon gate.
  - Conversion/greenfield routing and the DATA_CONTRACT authorship split.
  - Hybrid routing.
  - Module inheritance from the Factory level, never from each other (Fable §6 item 4).
  - The Blueprint lifecycle as canonical, with the SFP §2 mapping.
- **Likely affected docs / consumers:** Blueprint; SFP §2 (FC-007) and §2.5; MANIFEST row; every cold agent reading top-down.
- **Verification intent:**
  - The Blueprint council shows the QA seat and Coordinator, consistent with the glossary.
  - The router names a module-work branch that cites BIM/FIX/FEAT.
  - The lifecycle contains Gate Q and Gate D, with anchors that resolve to QA_PLAYBOOK.
  - The SFP §2 mapping stays consistent.
  - No QA mechanics are duplicated.
- **Open decision:** DEC-07 (seat glossary) should be ruled first. Fable §11 decision 13 (who holds the QA seat) is related backlog (FBL-S010).
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** The Director approves scope and release. The Architect assembles the approved module contract; the Engineer implements and hands off claims; the QA Executor independently plans and measures; the QA Lead approves the QA plan and certifies. Route module work to BIM_PLAYBOOK, BUG_FIX_PLAYBOOK or FEAT_PLAYBOOK as applicable, and approved review repairs to RRM_PLAYBOOK. Every newly authored module includes QAM. Gate Q, release authorization, deployment, Gate D and closeout remain distinct.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md:10` — ## THE BIG PICTURE; MANIFEST ← 7: SOFTWARE_FACTORY_PLAYBOOK, ARCHITECT_PLAYBOOK, ARCHITECT_QUESTIONNAIRE, ENGINEER_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, RECON_QUESTIONNAIRE, FFM_PLAYBOOK.
- `01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md:42` — ## 🔀 WHICH PIPELINE AM I IN?; MANIFEST ← 7: SOFTWARE_FACTORY_PLAYBOOK, ARCHITECT_PLAYBOOK, ARCHITECT_QUESTIONNAIRE, ENGINEER_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, RECON_QUESTIONNAIRE, FFM_PLAYBOOK.
- `01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md:122` — ## 🔄 THE FULL WORKFLOW; MANIFEST ← 7: SOFTWARE_FACTORY_PLAYBOOK, ARCHITECT_PLAYBOOK, ARCHITECT_QUESTIONNAIRE, ENGINEER_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, RECON_QUESTIONNAIRE, FFM_PLAYBOOK.

**Touch proposal:** C-004. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-004` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-005 — No Factory-wide precedence rule; individual docs each declare themselves the winner

**Proposed disposition:** BLOCKED. **Authority:** certified correction YES; package outcome remains proposed. CONDITIONAL: DEC-06. Cross-boundary component: XB-02.

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/01_governance_corrections.md:146`):

- **Certified record:** CF-01 · Severity MEDIUM · Review CONFLICT · Current-main OPEN — DEFECT REMAINS · Correction required YES
- **Reviewer source IDs:** Astra C01-S01 (SUGGESTION; Astra: not a defect) · Fable FBL-D031
- **Sol adjudication (certified):** ACCEPT DEFECT (2026-09-27): "Preserve stage-specific authority rules, but the missing reconciliation rule is a governance defect."
- **Evidence:** Fable §7 FBL-D031; Astra C01 §8 Rank 1 (C01-S01); Sol C01 §4 and §5.C; register §7.1.
- **Defect surfaces:**
  - At `0a787cb`:
    - `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md` (Rule Zero, Rule Zero-B)
    - `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md` §15
    - `02_PIPELINE_AGENTS/DESIGNER_PLAYBOOK.md` §13
    - `03_BUILD_METHODOLOGY/QA_PLAYBOOK.md` §5
    - `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md` ("Disk wins")
    - `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md` Appendix C.1
  - At `9c17939`: `_SKILLS/factory-docs-update/CLAUDE.md` §6 (line 178).
- **Defect:** local "X wins" clauses exist with no Factory-wide reconciliation rule. Kit reality (numbered colors, `httpOnly: false`) conflicts with doctrine, and nothing breaks the tie.
- **Current-main status:** OPEN — DEFECT REMAINS. v0.8 skill §6 still holds a local winner clause; the other surfaces are unchanged.
- **Proposed outcome (PROPOSED — not approved):** one constitutional reconciliation rule exists, and local "X wins" clauses become scoped statements that cite it. Two candidate models:
  - **(a) Question-scoped** (Astra C01-S01; Sol: "conceptually strong"). It separates four questions and their authorities:
    - what exists now: disk / recon
    - what is approved to exist: approved artifacts
    - which reusable pattern governs: the named domain doctrine owner
    - how conflicts resolve: Operator adjudication via stop-and-escalate
  - **(b) Linear tier order** (Fable): disk → accepted module contract → Constitution → Method → Manual → Design.
  - **Recommendation:** (a), because it keeps the stage-specific rules Sol's adjudication requires.
- **Preserve:**
  - Stage-specific authority rules.
  - Stop-and-escalate over silent reconciliation.
  - Disk-wins for facts.
  - "Observed code is not approval to weaken a requirement" (C01-S01).
- **Likely affected docs / consumers:**
  - The host (Blueprint or SFP).
  - Citing clauses in UI_UX, ENGINEER §15, DESIGNER §13, QA §5, STARTER_KIT, FFM C.1.
  - Skill §6 wording (`XB-SKILL`).
  - Unblocks FC-001, FC-029, FC-042, FC-073.
- **Verification intent:**
  - One anchor holds the rule.
  - Every listed local clause cites it or is scoped so that it cannot conflict.
  - The evidence cases resolve to one answer: kit numbered colors vs Rule Zero-B, and `httpOnly: false` vs AUTH.
  - A live-corpus search for "wins" is fully dispositioned.
- **Open decision:** DEC-06, the model and host document. Jarvis proposes; Tony ratifies.
- **Proposed route:** `SYNC` + `XB-SKILL`.

**Mapping proposal — ENGINEER-PROPOSED:** Resolve authority by the question being answered: disk and recon establish what exists; approved artifacts establish what is authorized; the named domain owner defines the reusable pattern. A conflict between these is not permission to substitute one for another. Stop the affected work, record both sources and their revisions, and obtain the Director’s attributable ruling. Preserve stage-specific authority within its stated scope.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md:31` — ## 1. Philosophy: Human Architect, AI Builder; MANIFEST ← 8: APP_FACTORY_BLUEPRINT, FFM_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.
- `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md:96` — ## 1.5 Doctrine Pairing Principle — Playbooks Paired With Worked Examples; MANIFEST ← 8: APP_FACTORY_BLUEPRINT, FFM_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.
- `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:1139` — ## 15. Agentic Coding Constitution (Karpathy Protocol); MANIFEST ← 7: APP_FACTORY_BLUEPRINT, DESIGNER_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, FFM_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `02_PIPELINE_AGENTS/DESIGNER_PLAYBOOK.md:374` — ## 13. Cross-References (Doctrine Docs); MANIFEST ← 10: APP_FACTORY_BLUEPRINT, SOFTWARE_FACTORY_PLAYBOOK, ARCHITECT_PLAYBOOK, ENGINEER_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, APP_FACTORY_SKILLS_PLAYBOOK, FFM_PLAYBOOK, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEME_LIBRARY, TOKEN_FILE.
- `03_BUILD_METHODOLOGY/QA_PLAYBOOK.md:231` — # 5. Source-of-Truth Order; MANIFEST ← 3: BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.
- `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md:17` — ## 🚨 The First Rule; MANIFEST ← 12: ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, FRONTEND_BUILD_PHASE_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, TESTING_PLAYBOOK, API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, DATABASE_MANUAL, STATE_MANAGEMENT_MANUAL, COMPONENT_REGISTRY, UI_UX_BUILDING_MANUAL.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:2236` — ## 23. Appendix C — Template Files (Stubs To Copy); MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.

**Touch proposal:** C-005. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-005` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-006 — Seat vocabulary not normalized; "Architect" names both the human and an AI agent

**Proposed disposition:** BLOCKED. **Authority:** certified correction YES; package outcome remains proposed. CONDITIONAL: DEC-07 remainder. Cross-boundary component: XB-02.

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/01_governance_corrections.md:188`):

- **Certified record:** CF-01 · Severity MEDIUM · Review UNIQUE (Fable) · Current-main OPEN — DEFECT REMAINS · Correction required YES
- **Reviewer source IDs:** Astra none · Fable FBL-D007
- **Evidence:** Fable §7 FBL-D007, §9 row 12; QA-5 FC-006 row.
- **Defect surfaces:**
  - At `0a787cb`:
    - `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md` §1 ("HUMAN (ARCHITECT)")
    - `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md` §1, §15, §17
    - `02_PIPELINE_AGENTS/HANDOFF_PACKAGE_PLAYBOOK.md` §3
    - `01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md`
    - `03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md` §2
    - `03_BUILD_METHODOLOGY/QA_PLAYBOOK.md` §4
    - `03_BUILD_METHODOLOGY/APP_FACTORY_SKILLS_PLAYBOOK.md` header
    - `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md` Role 3
  - At `9c17939`: `_SKILLS/factory-docs-update/CLAUDE.md` §1 (line 14).
- **Defect:** "Architect" means the human in SFP §1, ENGINEER §15 and HANDOFF §3, but the AI chat seat in FFM, BIM §2 and the skill. BIM gives "the Architect" binding advisory authority, so the name ambiguity becomes an authority ambiguity. Human and deployment seat names also vary.
- **Current-main status:** OPEN — DEFECT REMAINS. The v0.8 skill names "Jarvis (Architect)" and "Tony (Operator)", which normalizes one side only.
- **Proposed outcome (PROPOSED — not approved):**
  - One seat glossary at a constitutional anchor defines the human approver, Architect, Engineer, QA Lead / QA executor, Coordinator and deployment seat.
  - Every doc uses those names or cites the glossary.
  - "Architect" never denotes the human where authority depends on the name.
  - "Stakeholders" and "Generals" are defined or retired.
- **Preserve:**
  - Authority allocations: human final approval, the Architect advisory role, Operator adjudication.
  - BIM's four-seat model.
- **Likely affected docs / consumers:** the surfaces above; skill wording (`XB-SKILL`); FC-004, FC-011, FC-027.
- **Verification intent:**
  - The glossary exists.
  - A live-corpus search for the human-sense phrasings is fully dispositioned: "HUMAN (ARCHITECT)", "the human is the architect", "the architect (operator)".
  - Each seat name used in a gate or authority sentence matches the glossary.
- **Open decision:** DEC-07. Decision input: a **persona** (Jarvis, Sol, Claudy, Cody, Tony) and a **seat** (Architect, Engineer, QA Lead, QA executor, Director/Operator) are different things.
  - **Architect clarification (2026-10-12):** Jarvis/Sol acting as intake Architect for this package and Sol acting as QA Lead inside a DocSet Sync run are *contextual seat assignments, not inherently a conflict*.
  - DocSet Sync's separate-session QA requirement is preserved in every context (§2 seat resolution; D20).
  - The glossary should state that seats are assigned per context. It should also settle Director vs Operator vs Coordinator for the human seat.
- **Proposed route:** `SYNC` + `XB-SKILL`.

**Mapping proposal — ENGINEER-PROPOSED:** A seat defines responsibility; a persona or model name does not grant permission. Director is the human scope, access and release authority; Operator and Coordinator are contextual names for that human responsibility. Architect owns assembly and scope interpretation; Engineer owns implementation and factual handoff; QA Lead owns QA doctrine, plan approval, adjudication and certification; QA Executor independently plans and tests. Designer and deployment responsibilities remain distinct. “Architect” does not name the human approver in an authority rule.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md:31` — ## 1. Philosophy: Human Architect, AI Builder; MANIFEST ← 8: APP_FACTORY_BLUEPRINT, FFM_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.
- `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md:96` — ## 1.5 Doctrine Pairing Principle — Playbooks Paired With Worked Examples; MANIFEST ← 8: APP_FACTORY_BLUEPRINT, FFM_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.
- `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md:171` — ## 2. The Build Phases; MANIFEST ← 8: APP_FACTORY_BLUEPRINT, FFM_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.
- `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md:232` — ## 2.5 Module Identity & QA Handoff  *(Factory-wide — governs BIM, FIX, FEAT, and all future module types)*; MANIFEST ← 8: APP_FACTORY_BLUEPRINT, FFM_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.
- `01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md:10` — ## THE BIG PICTURE; MANIFEST ← 7: SOFTWARE_FACTORY_PLAYBOOK, ARCHITECT_PLAYBOOK, ARCHITECT_QUESTIONNAIRE, ENGINEER_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, RECON_QUESTIONNAIRE, FFM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:61` — ## 2. The Four-Role Factory Pattern; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md:23` — ## 2. Roles (the chain of custody); MANIFEST ← 1: FEAT_PLAYBOOK.
- `03_BUILD_METHODOLOGY/QA_PLAYBOOK.md:171` — # 4. Authority; MANIFEST ← 3: BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.

**Touch proposal:** C-006. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-006` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-007 — Lifecycle / execution-stage vocabularies lack a unifying map or crosswalk

**Proposed disposition:** BLOCKED. **Authority:** certified correction YES; package outcome remains proposed. CONDITIONAL: DEC-07 host / K-ENGINE. 

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/01_governance_corrections.md:224`):

- **Certified record:** CF-01 · Severity MEDIUM · Review PARTIAL · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C03-D10 · Fable FBL-D008 (primary)
- **Evidence:**
  - Astra C03 §7 C03-D10.
  - Sol C03 §6: "A compact crosswalk is the right correction. Do not rewrite either methodology unnecessarily."
  - Fable §7 FBL-D008, §9 row 22.
- **Defect surfaces (`0a787cb`):**
  - `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md` §§6, 11.3, 12, 12.4–12.6, 13, 20
  - `03_BUILD_METHODOLOGY/FRONTEND_BUILD_PHASE_PLAYBOOK.md` §§1.5, 2–9
  - `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md` §2
  - `01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md`
  - `02_PIPELINE_AGENTS/HANDOFF_PACKAGE_PLAYBOOK.md` §§1, 2, 8
  - `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md` §5
- **Defect:**
  - No operational crosswalk relates FFM sub-phases to FBP stages.
  - FFM numbers its Components sub-phase both 4 and 5.
  - HANDOFF and FFM §20 say "8 phases" / `01–08`, while FFM §12 uses `00–07`.
  - "Phase 1" has at least four referents.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - One compact crosswalk, extending the SFP §2 map, covers Blueprint phases, SFP phases, FFM sub-phases, FBP stages and roadmap phases.
  - It uses namespaced IDs and gives each one's parent, entry/exit artifacts and approval owner.
  - It states where demo deployment and Gate Q/D sit.
  - The Components index is consistent.
  - FFM §12/§20/§21 and HANDOFF §1/§2 agree on the playbook file set.
- **Preserve:**
  - The canonical Blueprint lifecycle and the SFP §2 nesting. Sol C01 §6.A: numbering differences are not contradictions.
  - Each methodology's own level of detail.
- **Likely affected docs / consumers:** the surfaces above; recovery instructions and gate citations that name phases.
- **Verification intent:**
  - The crosswalk exists at one anchor.
  - FFM Components has a single index.
  - File-set counts and names agree across FFM and HANDOFF.
  - Sample phase citations resolve to exactly one referent: "Phase 5 chat screen", "Phase 8 retrospective".
- **Open decision:** the host anchor. SFP §2 is recommended; Jarvis decides.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Keep lifecycle axes separate: Blueprint phases describe the Factory pipeline; SFP implementation phases describe build disciplines; FFM sub-phases and Frontend Build Phase stages describe execution within a module; roadmap phases describe product scope. Record each stage’s parent, entry artifacts, exit evidence and approver in the module contract. Demo deployment is not Gate Q or Gate D. Engine 1 is module engineering and module QA. Engine 2 is independent system review after all Engine 1 phases and their QA are closed. The separate post-FFM review occurs after FFM and its QA. Only dispositioned findings requiring repair produce RRM work.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md:171` — ## 2. The Build Phases; MANIFEST ← 8: APP_FACTORY_BLUEPRINT, FFM_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.
- `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md:232` — ## 2.5 Module Identity & QA Handoff  *(Factory-wide — governs BIM, FIX, FEAT, and all future module types)*; MANIFEST ← 8: APP_FACTORY_BLUEPRINT, FFM_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1246` — ## 12. File-By-File Authoring Guide — `playbook/`; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1250` — ### 12.1 — Overall Structure; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1266` — ### 12.2 — `00-OVERVIEW.md`; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1283` — ### 12.3 — `01-DISCOVERY.md` Through `06-VERIFICATION.md` (And `07-RETROSPECTIVE.md`); MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1296` — ### 12.4 — Per-Sub-Phase Authoring Notes; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1338` — ### 12.5 — `RETROSPECTIVES/` Folder; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1356` — ### 12.6 — Playbook Reuse Discipline; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1999` — ## 20. Worked Examples; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:2065` — ## 21. Appendix A — Skeleton Folder Tree; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `02_PIPELINE_AGENTS/HANDOFF_PACKAGE_PLAYBOOK.md:23` — ## 1. What This Playbook Is; MANIFEST ← 4: APP_FACTORY_BLUEPRINT, SOFTWARE_FACTORY_PLAYBOOK, ENGINEER_PLAYBOOK, FFM_PLAYBOOK.
- `02_PIPELINE_AGENTS/HANDOFF_PACKAGE_PLAYBOOK.md:36` — ## 2. Why This Playbook Exists; MANIFEST ← 4: APP_FACTORY_BLUEPRINT, SOFTWARE_FACTORY_PLAYBOOK, ENGINEER_PLAYBOOK, FFM_PLAYBOOK.
- `05_DESIGN_SYSTEM/COMPONENT_REGISTRY.md:16` — ## How To Use This Registry; MANIFEST ← 5: DESIGNER_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, GLOBAL_DESIGN_SYSTEM_HANDBOOK, UI_UX_BUILDING_MANUAL.

**Touch proposal:** C-007. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-007` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-008 — `FILE_TREE.md` is required by the Blueprint and root CLAUDE.md but no workflow produces it

**Proposed disposition:** BLOCKED. **Authority:** certified correction YES; package outcome remains proposed. CONDITIONAL: DEC-12 / DEC-08 root split. Cross-boundary component: XB-01.

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/01_governance_corrections.md:264`):

- **Certified record:** CF-02 · Severity MEDIUM · Review UNIQUE (Fable) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra none · Fable FBL-D006
- **Evidence:** Fable §7 FBL-D006, §9 row 17, §11 decision 11.
- **Defect surfaces (`0a787cb`):**
  - `01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md` Phase 3, "Blind Spots"
  - `CLAUDE.md` (root): "Factory Pipeline Awareness", failure mode 19
  - `02_PIPELINE_AGENTS/HANDOFF_PACKAGE_PLAYBOOK.md` §1
  - `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md` §3, §9
  - `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md` §12
- **Defect:** the Blueprint and root CLAUDE.md treat `FILE_TREE.md` as a source-of-truth deliverable. The HANDOFF/FFM package defines four files without it, and ENGINEER §12 embeds the file structure in DATA_CONTRACT.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):** consistently one of these, Factory-wide:
  - **(a)** `FILE_TREE.md` is a defined artifact with a producer, timing, approval step (FC-015) and place in the package; or
  - **(b)** it is retired from the Blueprint and root CLAUDE.md in favor of the existing DATA_CONTRACT "File Structure" or `_project/CLAUDE.md` structure section.
- **Preserve:** the "don't touch what works" control, which needs a named artifact either way; the four-file package where it applies.
- **Likely affected docs / consumers:** Blueprint, HANDOFF, FFM, ENGINEER §12; root `CLAUDE.md` (`XB-ROOT`, gated by DEC-08).
- **Verification intent:** every `FILE_TREE` mention across live docs and root CLAUDE.md is consistent with the ruling. If (a), the package definition lists it with its producer and approval step.
- **Open decision:** DEC-12, require or retire (Tony).
- **Proposed route:** `SYNC` + `XB-ROOT`.

**Mapping proposal — ENGINEER-PROPOSED:** FILE_TREE is an optional Architect assembly aid, not a mandatory independent handoff artifact. The approved DATA_CONTRACT file-structure section defines the required implementation structure. Any additional structure artifact must identify its author, approved revision and relationship to DATA_CONTRACT; conflicting structures stop assembly.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md:65` — ## 📚 FACTORY DOCUMENT STRUCTURE; MANIFEST ← 7: SOFTWARE_FACTORY_PLAYBOOK, ARCHITECT_PLAYBOOK, ARCHITECT_QUESTIONNAIRE, ENGINEER_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, RECON_QUESTIONNAIRE, FFM_PLAYBOOK.
- `01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md:122` — ## 🔄 THE FULL WORKFLOW; MANIFEST ← 7: SOFTWARE_FACTORY_PLAYBOOK, ARCHITECT_PLAYBOOK, ARCHITECT_QUESTIONNAIRE, ENGINEER_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, RECON_QUESTIONNAIRE, FFM_PLAYBOOK.
- `01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md:167` — ## 📋 ENGINEER AGENT: WHAT IT PRODUCES; MANIFEST ← 7: SOFTWARE_FACTORY_PLAYBOOK, ARCHITECT_PLAYBOOK, ARCHITECT_QUESTIONNAIRE, ENGINEER_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, RECON_QUESTIONNAIRE, FFM_PLAYBOOK.

**Touch proposal:** C-008. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-008` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-009 — Load-bearing external artifacts (skills, worked examples, issue logs) are referenced but never located

**Proposed disposition:** BLOCKED. **Authority:** certified correction YES; package outcome remains proposed. CONDITIONAL: DEC-19 remainder / RRM-09. Cross-boundary component: XB-04.

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/01_governance_corrections.md:323`):

- **Certified record:** CF-13 · Severity MEDIUM · Review UNIQUE (Fable) · Current-main OPEN — DEFECT REMAINS · Correction required YES
- **Reviewer source IDs:** Astra none · Fable FBL-D011
- **Evidence:** Fable §7 FBL-D011, §11 decision 9; QA-5 FC-009 row.
- **Defect surfaces (`0a787cb`):**
  - `02_PIPELINE_AGENTS/ARCHITECT_PLAYBOOK.md` §2
  - `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md` §1.5
  - `02_PIPELINE_AGENTS/HANDOFF_PACKAGE_PLAYBOOK.md` §10, §13
  - `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md` §14, §20
  - `03_BUILD_METHODOLOGY/APP_FACTORY_SKILLS_PLAYBOOK.md` §7, §14
  - `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md` §11
  - `03_BUILD_METHODOLOGY/FRONTEND_BUILD_PHASE_PLAYBOOK.md` §12
  - `05_DESIGN_SYSTEM/COMPONENT_REGISTRY.md` §8, §9
  - `03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md` §6
  - The `_SKILLS/` tree at `9c17939` holds only `factory-docs-update/`.
- **Defect:** live doctrine cites these with no locator, and none exists in the Hub:
  - skills: `stark-recon`, `brain-drain`, `stark-frontend-first`, `CLOUD_DEPLOYMENT_SKILLS`, `SUPABASE_MIGRATION_SKILL`
  - the SFP §1.5 worked examples
  - issue logs and lessons: `KNOWN_ISSUES.md`, `KIT_PROPOSALS_ARCHIVE.md`, `STARTER_KIT_FEEDBACK.md`, `agent_docs/LESSONS/`
- **Current-main status:** OPEN — DEFECT REMAINS. Per QA-5 this is a Hub-locator claim, not a claim that the artifacts are absent everywhere.
- **Proposed outcome (PROPOSED — not approved):**
  - Each load-bearing external artifact cited by live doctrine has one Hub locator entry (repository, path, revision or tag), or its citation is relabeled as project-local or removed.
  - The Skills Playbook's library-vs-repo-side statement agrees with where skills actually live.
- **Preserve:**
  - The SFP §1.5 Doctrine Pairing Principle.
  - RECON_QUESTIONNAIRE as a self-executing mitigation for the missing recon skill.
  - The Skills Playbook distinction between library and instances.
- **Likely affected docs / consumers:**
  - The citing docs above.
  - The locator host (MANIFEST or SKILLS_PLAYBOOK).
  - The artifacts themselves live in other repositories (`XB-EXT`; their contents are unknown to this package — GAP).
- **Verification intent:** every named artifact appears in the locator with repo, path and revision, or each citation is dispositioned. A cold reader can resolve each one from the Hub alone.
- **Open decision:** DEC-19, where skills and examples live (Fable §11 decision 9) and the locator host.
- **Proposed route:** `SYNC` + `XB-EXT`.

**Mapping proposal — ENGINEER-PROPOSED:** External skills, worked examples and issue logs require a locator naming the repository, path and immutable revision. A project-local artifact is labeled project-local. An unavailable example is a documented gap, not a prerequisite the Engineer must invent. RRM reviewer guidance belongs in RRM_PLAYBOOK; new example or kit homes require an attributable placement decision.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md:96` — ## 1.5 Doctrine Pairing Principle — Playbooks Paired With Worked Examples; MANIFEST ← 8: APP_FACTORY_BLUEPRINT, FFM_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.
- `03_BUILD_METHODOLOGY/APP_FACTORY_SKILLS_PLAYBOOK.md:331` — ## 7. Folder Layout Standards; MANIFEST ← 1: FFM_PLAYBOOK.
- `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md:616` — ## 11. Known Issues — Resolved; MANIFEST ← 12: ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, FRONTEND_BUILD_PHASE_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, TESTING_PLAYBOOK, API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, DATABASE_MANUAL, STATE_MANAGEMENT_MANUAL, COMPONENT_REGISTRY, UI_UX_BUILDING_MANUAL.
- `02_PIPELINE_AGENTS/HANDOFF_PACKAGE_PLAYBOOK.md:340` — ## 10. The Worked Example; MANIFEST ← 4: APP_FACTORY_BLUEPRINT, SOFTWARE_FACTORY_PLAYBOOK, ENGINEER_PLAYBOOK, FFM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1999` — ## 20. Worked Examples; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.

**Touch proposal:** C-009. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-009` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-010 — "Plan Mode" and root CLAUDE.md are load-bearing but sit outside the governed doc set

**Proposed disposition:** BLOCKED. **Authority:** certified correction YES; package outcome remains proposed. CONDITIONAL: DEC-08. Cross-boundary component: XB-01.

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/01_governance_corrections.md:429`):

- **Certified record:** CF-17 · Severity MEDIUM · Review UNIQUE (Fable) · Current-main OPEN — DEFECT REMAINS · Correction required YES
- **Reviewer source IDs:** Astra none · Fable FBL-D018
- **Evidence:** Fable §7 FBL-D018, §9 row 21, §11 decision 5; QA-5 FC-010 row.
- **Defect surfaces:**
  - At `0a787cb`:
    - `CLAUDE.md` (root)
    - `03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md` §§5–7
    - `03_BUILD_METHODOLOGY/BUG_FIX_PLAYBOOK.md` §16
    - `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md` §13.1, §22
    - `03_BUILD_METHODOLOGY/FRONTEND_BUILD_PHASE_PLAYBOOK.md` Stage 2
    - `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md` §15
    - `03_BUILD_METHODOLOGY/APP_FACTORY_SKILLS_PLAYBOOK.md` §10
    - `MANIFEST.md`
  - At `9c17939`: `_SKILLS/factory-docs-update/CLAUDE.md` D2 (line 96).
- **Defect:**
  - Plan Mode is invoked across BIM, BUG_FIX, FFM, FBP and the skill, but is defined only in SKILLS_PLAYBOOK (for skills) and in root CLAUDE.md.
  - Root CLAUDE.md is outside MANIFEST, lint-exempt and self-versioned.
  - It duplicates the Karpathy protocol that ENGINEER §15 claims as canonical.
  - The FFM/FBP "root CLAUDE.md forbidden zone" pointer resolves to nothing.
- **Current-main status:** OPEN — DEFECT REMAINS. Skill v0.8 D2 defines Plan Mode for skill runs only; root CLAUDE.md and MANIFEST are unchanged.
- **Proposed outcome (PROPOSED — not approved):**
  - Plan Mode has one governed definition (Fable: ENGINEER §15 agent conduct) that playbooks, skills and root CLAUDE.md cite.
  - Root CLAUDE.md's status is decided: either governed doctrine (in MANIFEST and lint scope, with its Karpathy copy reconciled with ENGINEER §15), or tool configuration (no Factory doctrine beyond pointers to the Hub).
  - The Gate M "forbidden zone" pointer resolves to a governed location.
- **Preserve:**
  - Plan Mode's intent: think before code, approve before implementation writes.
  - The pre-approval bookkeeping surface (FC-090; DocSet Sync D2 RUN-STATE writes).
  - Session and recovery crash resilience.
  - ENGINEER §15 conduct.
- **Likely affected docs / consumers:**
  - Root `CLAUDE.md` (`XB-ROOT`); ENGINEER §15, SKILLS_PLAYBOOK §10, BIM, BUG_FIX, FFM, FBP, MANIFEST.
  - Skill D2 (`XB-SKILL`).
  - Gates FC-008, FC-090, FC-091, FC-094.
  - Every agent bootstrap that loads root CLAUDE.md, including this seat.
- **Verification intent:**
  - One definition anchor.
  - Every "Plan Mode" use in live docs cites it.
  - The Gate M pointer resolves.
  - Root CLAUDE.md is either in MANIFEST and lint scope, or carries only pointers.
  - ENGINEER §15 and root CLAUDE.md no longer both claim to be canonical.
- **Open decision:** DEC-08, root CLAUDE.md status (Tony). It gates the rest of CF-17 and FC-090, FC-091, FC-094 and FC-008.
- **Proposed route:** `XB-ROOT` + `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Plan Mode requires a recorded plan and attributable approval before implementation. Recon evidence, response logs, session records and recovery state are authorized recordkeeping lanes; they do not authorize application or contract changes. The approved plan identifies writable paths and the revision it governs. Root tool configuration points to governed doctrine and grants no additional Factory authority.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:1139` — ## 15. Agentic Coding Constitution (Karpathy Protocol); MANIFEST ← 7: APP_FACTORY_BLUEPRINT, DESIGNER_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, FFM_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FRONTEND_BUILD_PHASE_PLAYBOOK.md:104` — ## 2. Frontend Build Phase — Overview; MANIFEST ← 4: ENGINEER_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, TESTING_PLAYBOOK, UI_UX_BUILDING_MANUAL.

**Touch proposal:** C-010. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-010` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-011 — Deployment, promotion and rollback have gates and checklists but no owning doctrine

**Proposed disposition:** BLOCKED. **Authority:** certified correction YES; package outcome remains proposed. CONDITIONAL: DEC-18 remainder. 

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/01_governance_corrections.md:360`):

- **Certified record:** CF-14 · Severity MEDIUM · Review UNIQUE (Fable) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra none · Fable FBL-D017
- **Evidence:** Fable §7 FBL-D017, §11 decision 12; Astra C02-S01 (suggestion, operational custody).
- **Defect surfaces (`0a787cb`):**
  - `01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md` Phase 5
  - `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md` §11
  - `03_BUILD_METHODOLOGY/QA_PLAYBOOK.md` §4, §13
  - `03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md` §6
  - `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md` §17
  - `04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md` §13
  - `CLAUDE.md` (root; it names the targets)
- **Defect:** Gate D requires a recorded revision and rollback readiness, but no doc defines environments, promotion, revision recording or rollback for the named targets.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - A governed deployment doctrine with a named owning seat defines, for each deployment target the Factory uses:
    - environments
    - promotion
    - revision identity
    - rollback
  - Gate D's checks can then be verified against doctrine, and QA §13 and BIM §6 cite it.
- **Preserve:**
  - Gate D's deployed-identity and rollback-readiness requirements.
  - Operator release authority.
  - BIM fallback switches and migration-recovery decisions (Astra C03 §5).
- **Likely affected docs / consumers:**
  - A new canonical document or section. DocSet Sync would classify it as NEW CANONICAL DOCUMENT, so the route is LARGE.
  - QA §13, BIM §6, ENGINEER §17, SFP §11, Blueprint Phase 5; MANIFEST, CHANGELOG.
- **Verification intent:**
  - Each Gate D item maps to a doctrine step.
  - Each named target has revision-identity and rollback steps, or is explicitly out of scope.
  - The owning seat matches the FC-006 glossary.
- **Open decision:** DEC-18, the deployment doctrine owner / DevOps seat, and new doc vs section. Platform procedures are not derivable from the Hub (GAP); they need a subject-matter author.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** DEPLOYMENT_PLAYBOOK owns deployment requirements. Gate D verifies the actual environment and deployed revision, separately from build success and Gate Q. Each deployment contract must identify the authorized operator, environment, source commit, build/image, deployed revision, route, promotion prerequisites and rollback or recovery evidence. An unspecified platform procedure or authority is a blocking gap, not an implied permission.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md:816` — ## 11. Phase 9: Deployment; MANIFEST ← 8: APP_FACTORY_BLUEPRINT, FFM_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.
- `03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md:77` — ## 6. Lifecycle (the stage-gate chain); MANIFEST ← 1: FEAT_PLAYBOOK.
- `03_BUILD_METHODOLOGY/QA_PLAYBOOK.md:774` — # 13. Gate D — Deployed-Environment Verification; MANIFEST ← 3: BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.
- `01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md:122` — ## 🔄 THE FULL WORKFLOW; MANIFEST ← 7: SOFTWARE_FACTORY_PLAYBOOK, ARCHITECT_PLAYBOOK, ARCHITECT_QUESTIONNAIRE, ENGINEER_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, RECON_QUESTIONNAIRE, FFM_PLAYBOOK.

**Touch proposal:** C-011. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-011` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-012 — Git/cloud authority differs between FFM-era and module-era doctrine without a reconciling rule

**Proposed disposition:** BLOCKED. **Authority:** certified correction YES; package outcome remains proposed. CONDITIONAL: DEC-18 remainder. 

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/01_governance_corrections.md:395`):

- **Certified record:** CF-14 · Severity MEDIUM · Review UNIQUE (Fable) · Current-main PARTIALLY REMEDIATED · Correction required YES
- **Reviewer source IDs:** Astra none · Fable FBL-D016
- **Evidence:** Fable §7 FBL-D016, §9 row 16, §11 decision 7; QA-5 FC-012 row.
- **Defect surfaces:**
  - At `0a787cb`:
    - `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md` §2 Role 4, §12.4
    - `03_BUILD_METHODOLOGY/FRONTEND_BUILD_PHASE_PLAYBOOK.md` Stage 6
    - `03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md` §2, §7
    - `03_BUILD_METHODOLOGY/BUG_FIX_PLAYBOOK.md` §3
    - `03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md` §5.1
  - At `9c17939`: `_SKILLS/factory-docs-update/CLAUDE.md` D5 (line 102).
- **Defect:** in FFM and FBP the Engineer deploys to staging, while BIM §7 and BUG_FIX §3 make the Engineer git-zero / cloud-zero. TESTING §5.1 tags at deploy with no named actor. No rule says the difference is intentional per context.
- **Current-main status:** PARTIALLY REMEDIATED.
  - Skill v0.8 D5 is now a bounded Hub-only carve-out that explicitly preserves module git-zero / cloud-zero.
  - Residual at main: FFM:222/1325 and FBP:397 (Engineer deploys to staging) vs BIM:110 and BUG_FIX:72; TESTING:1422 has no tag actor.
- **Proposed outcome (PROPOSED — not approved):**
  - One authority matrix, by context (FFM run, module run, Hub doctrine run) × action (commit, push, deploy, tag) × seat, is published in doctrine.
  - FFM, FBP and TESTING align with it or appear in it as named, scoped exceptions.
- **Preserve:**
  - The DocSet Sync D5 carve-out and its explicit non-generalization.
  - Module git-zero / cloud-zero.
  - Operator merge ownership.
  - main is PR-only.
- **Likely affected docs / consumers:** the matrix host (SFP §2.5 or the Blueprint); FFM, FBP, BIM, BUG_FIX, TESTING. The skill only needs to cite it.
- **Verification intent:**
  - The matrix exists.
  - FFM:222/1325, FBP:397 and TESTING:1422 (main line references per QA-5) agree with it or are listed exceptions.
  - No context grants one seat opposite permissions.
- **Open decision:** DEC-18. In particular: may the Engineer deploy to staging in FFM runs? (Tony)
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Project-module Git belongs to the Director: commit and push the completed engineering candidate, create qa/<module-branch> at that exact commit, commit approved repairs there, and perform final merge and push after certification and closeout. Engineer and QA Executor have distinct writable lanes on that branch. Cloud and staging actions require explicit context-specific authority. A Hub skill exception is confined to its named Hub context and is superseded by an explicit task restriction.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:61` — ## 2. The Four-Role Factory Pattern; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FRONTEND_BUILD_PHASE_PLAYBOOK.md:383` — ## 8. Stage 6 — Demo Deployment Prep (V1); MANIFEST ← 4: ENGINEER_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, TESTING_PLAYBOOK, UI_UX_BUILDING_MANUAL.
- `03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:1415` — ## 5.1 `CHANGELOG.md`; MANIFEST ← 11: SOFTWARE_FACTORY_PLAYBOOK, ENGINEER_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, API_AND_SERVICES_MANUAL, DATABASE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.
- `03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md:108` — ## 7. Standing Engineer Doctrine (bake into every manager); MANIFEST ← 1: FEAT_PLAYBOOK.

**Touch proposal:** C-012. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-012` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-013 — Engineer-side completion/handoff doctrine does not carry the QA intake interface

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/02_agents_handoffs_corrections.md:29`):

- **Certified record:** CF-02 · Severity HIGH · Review PARTIAL · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C02-D01 · Fable FBL-D015 (primary)
- **Severity divergence (recorded):** Astra HIGH vs Fable MEDIUM. The certified HIGH stands.
- **Evidence:** Astra C02 §7 Rank 1; Sol C02 §3 and §6.A; Fable §7 FBL-D015, §9 row 18.
- **Defect surfaces (`0a787cb`):**
  - `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md` §12 (readiness for Operations), §17 (Handoff to Operations)
  - `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md` §2.5
  - `03_BUILD_METHODOLOGY/QA_PLAYBOOK.md` §6 (15-item Engineer completion package), §20 (QA artifacts)
  - `03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md` §4, §5, §7
- **Defect:**
  - The Engineer's ready-for-Operations contract has no QA handoff, `ACCEPTANCE_SPEC`, Gate Q or Operator release interface.
  - QA §6 requires a 15-item completion package that no Engineer-side doctrine tells anyone to produce.
  - QA §20 artifacts (`QA_PLAN.md`, `GATE_Q_REPORT.md`, `GATE_D_CHECKLIST.md`, `GATE_D_REPORT.md`) have no defined home while the module folder is frozen.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - The Engineer's completion contract routes through independent QA before Operations, and Engineer-side doctrine (ENGINEER §17, BIM §4/§5/§7) names:
    - the acceptance artifact and its provenance
    - one Engineer completion artifact containing every QA §6 field
    - the QA verdict reference
    - routing for findings and blockage
    - the Operator release decision
  - QA §20 artifacts have a defined location that does not contradict the module freeze (joint with FC-026).
- **Preserve:**
  - Operations' setup, environment, logging and rollback package (Astra C02 §5 item 8).
  - The constitutional documentation-only waiver eligibility.
  - QA_PLAYBOOK as the single owner of QA mechanics: link, don't duplicate.
  - The Sol C02 distinction from FC-015.
- **Likely affected docs / consumers:** ENGINEER §12/§17, BIM §4/§5/§7, QA §6/§20, SFP §2.5 (reference); QA seat intake; Operations; FC-002 and FC-025 (sequence together).
- **Verification intent:**
  - ENGINEER §17's recipient sequence is Engineering → QA (Gate Q) → Operator release → Operations.
  - A field-by-field match shows the named Engineer completion artifact covers every QA §6 item.
  - QA §20 artifacts have a stated home consistent with FC-026's freeze model.
  - No QA procedure text is duplicated in ENGINEER.
- **Open decision:** DEC-13, the QA artifact home and module freeze model. Fable proposes a `qa/` subfolder written after unfreeze; joint with FC-026.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Engineering completion includes the factual QAM manifest and engineering handoff in the original assignment. Identify the approved acceptance contract and provenance, candidate reference, complete changed-file inventory, environment, reproduction commands, engineering checks, limitations and known findings. Before commit, the candidate SHA is explicitly pending; the Director commits and QA resolves the full candidate identity. Route to independent Q1, plan approval, Director release and Q2 before Operations. QA verdict and release decision are separate records.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:1377` — ## 17. Handoff Protocol to Operations; MANIFEST ← 7: APP_FACTORY_BLUEPRINT, DESIGNER_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, FFM_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md:46` — ## 4. The Module Package (one folder, self-contained); MANIFEST ← 1: FEAT_PLAYBOOK.
- `03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md:60` — ## 5. The Manager File (CLAUDE.md) — one module, one manager; MANIFEST ← 1: FEAT_PLAYBOOK.
- `03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md:108` — ## 7. Standing Engineer Doctrine (bake into every manager); MANIFEST ← 1: FEAT_PLAYBOOK.
- `03_BUILD_METHODOLOGY/QA_PLAYBOOK.md:260` — # 6. The Engineer Handoff Is a Claim Package; MANIFEST ← 3: BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.

**Touch proposal:** C-013. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-013` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-014 — Recon's operation boundary contradicts its own procedure and required output

**Proposed disposition:** BLOCKED. **Authority:** certified correction YES; package outcome remains proposed. CONDITIONAL: DEC-14. 

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/02_agents_handoffs_corrections.md:212`):

- **Certified record:** CF-03 · Severity MEDIUM · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C02-D02 · Fable none
- **Evidence:** Astra C02 §7 Rank 2; Sol C02 §3 (provisional MEDIUM, closed MEDIUM 2026-09-27) and §6.C (cross-check against `stark-recon`).
- **Defect surfaces (`0a787cb`):**
  - `02_PIPELINE_AGENTS/RECON_QUESTIONNAIRE.md`: "How To Use This", S0.7, Q8.6
  - `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md` §2
  - `02_PIPELINE_AGENTS/ARCHITECT_PLAYBOOK.md` (recon consumption)
  - `01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md` (recon as a read-only pass)
- **Defect:** recon is specified as "no file changes, no git operations", pure reading and grepping. The same doctrine instructs `npm run build` and requires a written recon report file, with no defined exception.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):** recon doctrine states one boundary, identically in all three recon documents, that separates three classes of write:
  - **(A) Report and bookkeeping writes: permitted.**
    - The recon report, at one path shared by producer and consumer.
    - The normal authorized session bookkeeping under the governing session protocol: `agent_docs/RESPONSES/`, the session file, `RECOVERY.md`.
    - These record evidence and state; they do not change the system under inspection.
  - **(B) Diagnostic-generated artifacts: permitted only inside an explicit diagnostic boundary.** If a diagnostic such as the S0.7 / Q8.6 `npm run build` is allowed, the doctrine names:
    - who authorizes it;
    - where it runs (the target checkout or a disposable copy);
    - which generated artifacts are expected (e.g. framework build output and caches);
    - how those artifacts are recorded or removed afterwards;
    - how the run confirms that no tracked application source changed.

    If a diagnostic is not authorized or not available, the recon report records the limitation instead of fabricating a result.
  - **(C) Application-source changes: prohibited.** No edits to application source, configuration, dependency manifests or lockfiles, and no state-changing operations on the target repository.
- **Preserve:**
  - Recon as a read-only validity gate and "invalid without recon" (Astra C01 §5 item 1). "Read-only" applies to class C; it must not be read as forbidding class A.
  - The named producer/consumer and freshness triggers (Astra C02 §5 item 1).
  - The normal authorized bookkeeping protocol.
- **Likely affected docs / consumers:** RECON_QUESTIONNAIRE, ENGINEER §2, ARCHITECT, Blueprint. The off-Hub `stark-recon` skill (`XB-EXT`; not inspected, FC-009) is awareness only.
- **Verification intent:**
  - The three recon documents state the same three-class boundary.
  - **Class A:** the report path is identical for producer and consumer, and no recon sentence, read literally, forbids the report or the normal bookkeeping writes (the original contradiction is gone).
  - **Class B:** S0.7 and Q8.6 are each removed, carry the full diagnostic boundary (authorizer, location, expected artifacts, post-run handling, tracked-source check), or are replaced by a recorded-limitation instruction.
  - **Class C:** the prohibition is stated, and the post-diagnostic check named under class B confirms that no tracked application source changed.
- **Open decision:** DEC-14 (Tony/Jarvis):
  - Are build diagnostics allowed during recon, and if so where do they run (target checkout or disposable copy) and which artifacts are acceptable?
  - Is read-only Git inspection permitted for the class-C check?

  Sol's elevation trigger (recon mutating target state) is not established by the certified record.
- **Proposed route:** `SYNC` (+ `XB-EXT` awareness).

**Mapping proposal — ENGINEER-PROPOSED:** Recon may write its report and authorized response, session and recovery records. Diagnostics that generate build or cache output require an explicit authorization naming the target checkout, command, expected writes and cleanup. Record the resulting diff and prove tracked application sources unchanged. Without authorization, report the diagnostic limitation. Recon may not modify product source, configuration, dependencies, lockfiles or the approved contract.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:107` — ## 2. Phase 0: The Recon-Executor Role; MANIFEST ← 7: APP_FACTORY_BLUEPRINT, DESIGNER_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, FFM_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:522` — #### 2. Packaging Is Not Optional; MANIFEST ← 7: APP_FACTORY_BLUEPRINT, DESIGNER_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, FFM_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:1166` — #### 2. Confusion Management (CRITICAL); MANIFEST ← 7: APP_FACTORY_BLUEPRINT, DESIGNER_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, FFM_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `02_PIPELINE_AGENTS/RECON_QUESTIONNAIRE.md:36` — ## How To Use This; MANIFEST ← 13: APP_FACTORY_BLUEPRINT, ARCHITECT_PLAYBOOK, ARCHITECT_QUESTIONNAIRE, ENGINEER_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, APP_FACTORY_SKILLS_PLAYBOOK, FFM_PLAYBOOK, TESTING_PLAYBOOK, APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `02_PIPELINE_AGENTS/RECON_QUESTIONNAIRE.md:63` — ## SECTION 0 — The Day-1 Ground-Truth Sweep (Run 001 Meta-Lesson); MANIFEST ← 13: APP_FACTORY_BLUEPRINT, ARCHITECT_PLAYBOOK, ARCHITECT_QUESTIONNAIRE, ENGINEER_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, APP_FACTORY_SKILLS_PLAYBOOK, FFM_PLAYBOOK, TESTING_PLAYBOOK, APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `02_PIPELINE_AGENTS/RECON_QUESTIONNAIRE.md:315` — ## SECTION 8 — Demo / Tutorial Scaffolding (The Cascade Trap); MANIFEST ← 13: APP_FACTORY_BLUEPRINT, ARCHITECT_PLAYBOOK, ARCHITECT_QUESTIONNAIRE, ENGINEER_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, APP_FACTORY_SKILLS_PLAYBOOK, FFM_PLAYBOOK, TESTING_PLAYBOOK, APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `02_PIPELINE_AGENTS/RECON_QUESTIONNAIRE.md:471` — ## Recon Report Format (What Claudy Returns); MANIFEST ← 13: APP_FACTORY_BLUEPRINT, ARCHITECT_PLAYBOOK, ARCHITECT_QUESTIONNAIRE, ENGINEER_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, APP_FACTORY_SKILLS_PLAYBOOK, FFM_PLAYBOOK, TESTING_PLAYBOOK, APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.

**Touch proposal:** C-014. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-014` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-015 — Greenfield engineering-spec approval has no execution checkpoint before implementation

**Proposed disposition:** BLOCKED. **Authority:** certified correction YES; package outcome remains proposed. CONDITIONAL: DEC-11. 

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/02_agents_handoffs_corrections.md:66`):

- **Certified record:** CF-02 · Severity HIGH · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C02-D03 · Fable none
- **Evidence:** Astra C02 §7 Rank 3; Sol C02 §3 ("a true pre-implementation authority boundary") and §6.B.
- **Defect surfaces (`0a787cb`):**
  - `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md`:
    - §3 (greenfield author of record)
    - "Before starting" checks
    - §12 (DATA_CONTRACT produced "alongside working code"; DRAFT/APPROVED field with no transition)
    - the closing checklist
  - `01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md`: "The Full Workflow", Phase 3 → Phase 4.
- **Defect:** the Blueprint requires human approval of the Engineer-produced DATA_CONTRACT, the applicable schema/API specs and FILE_TREE before Phase 4 code. The Engineer's own sequence, §12 and closing checklist can all be followed without submitting those specs for approval.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - The greenfield Engineer sequence runs in this order:
    1. author DATA_CONTRACT, plus applicable schema/API specs and FILE_TREE if retained (FC-008)
    2. submit for review
    3. human approval, recorded against the artifact revision
    4. fabrication
  - §12 and the closing checklist follow that order.
  - Later changes are amendments that need re-approval.
  - The conversion consumption path is unchanged.
- **Preserve:**
  - The per-pipeline authorship split: conversion is Architect-authored, greenfield is Engineer-authored (Astra C01 §5 item 2; C02 §5 item 5).
  - The Blueprint approval rule.
  - The distinction from FC-013.
- **Likely affected docs / consumers:** ENGINEER §3/§12 and closing checklist; Blueprint Phase 3/4; FFM §12.4/§14/§18 through FC-027; Engineer and Operator.
- **Verification intent:**
  - In ENGINEER, the spec-approval step comes before any code-writing step, in both the procedure and the closing checklist.
  - The DATA_CONTRACT DRAFT → APPROVED transition names an approver.
  - The outcome is consistent with FC-027's FFM sequence.
- **Open decision:** DEC-11, greenfield DATA_CONTRACT timing and Engineer seat identity (Fable §11 decision 6); joint with FC-027.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** For greenfield work, the Architect prepares DATA_CONTRACT before Design and submits its revision for Director approval. Engineering consumes the approved contract and applicable schema/API specifications before fabrication. A required change is an attributable amendment that returns for approval before implementation. Conversion continues to consume its approved extracted contract.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:129` — ## 3. Inputs Required; MANIFEST ← 7: APP_FACTORY_BLUEPRINT, DESIGNER_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, FFM_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:540` — #### 3. Editable Installs Are Mandatory; MANIFEST ← 7: APP_FACTORY_BLUEPRINT, DESIGNER_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, FFM_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:1178` — #### 3. Push Back When Warranted; MANIFEST ← 7: APP_FACTORY_BLUEPRINT, DESIGNER_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, FFM_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:390` — ## 8. The Build Sequence; MANIFEST ← 7: APP_FACTORY_BLUEPRINT, DESIGNER_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, FFM_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:730` — ## 12. DATA_CONTRACT Template; MANIFEST ← 7: APP_FACTORY_BLUEPRINT, DESIGNER_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, FFM_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `02_PIPELINE_AGENTS/ARCHITECT_PLAYBOOK.md:330` — ## 8. Handoff Protocol to Designer; MANIFEST ← 6: APP_FACTORY_BLUEPRINT, ARCHITECT_QUESTIONNAIRE, DESIGNER_PLAYBOOK, RECON_QUESTIONNAIRE, FFM_PLAYBOOK, BIM_PLAYBOOK.

**Touch proposal:** C-015. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-015` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-016 — Artifact status vocabularies disagree between producer templates and receiving gates (LOCKED vs APPROVED)

**Proposed disposition:** BLOCKED. **Authority:** certified correction YES; package outcome remains proposed. CONDITIONAL: DEC-10. 

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/02_agents_handoffs_corrections.md:100`):

- **Certified record:** CF-02 · Severity MEDIUM · Review CONFIRMED · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C02-D04 · Fable FBL-D012 (primary)
- **Severity divergence (recorded):** Astra MEDIUM vs Fable LOW. The certified MEDIUM stands.
- **Evidence:** Astra C02 §7 Rank 4; Sol C02 §4; Fable §7 FBL-D012, §9 row 23.
- **Defect surfaces (`0a787cb`):**
  - `02_PIPELINE_AGENTS/ARCHITECT_QUESTIONNAIRE.md`: template header `[DRAFT | REVIEW | LOCKED]`
  - `02_PIPELINE_AGENTS/ARCHITECT_PLAYBOOK.md`: lifecycle DRAFT→REVIEW→APPROVED / AMENDED; handoff requires APPROVED
  - `02_PIPELINE_AGENTS/DESIGNER_PLAYBOOK.md`: preflight; §8 UI_SPEC `Status: APPROVED`
  - `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md`: preflight; §12 `DRAFT | APPROVED`
  - `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md`: Appendix C.2 `Status: LOCKED`
- **Defect:** the canonical APP_BRIEF template cannot express APPROVED, the state both consumers and the producer's own manual require. No mapping connects LOCKED to APPROVED, and the vocabulary also varies across other artifacts.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - One artifact status vocabulary, including amendment and re-approval, is used by templates, authoring procedures and receiving gates for Factory planning artifacts.
  - If legacy LOCKED artifacts stay valid, an explicit mapping and the required approval evidence are stated. No silent relabeling.
- **Preserve:**
  - Human control of approval and unlock.
  - Re-approval after change (Astra C02 §5 item 2).
  - Revision/re-approval semantics (Sol).
- **Likely affected docs / consumers:** ARCHITECT_QUESTIONNAIRE, ARCHITECT_PLAYBOOK, DESIGNER, ENGINEER, FFM C.2; Designer and Engineer preflight gates; FC-019.
- **Verification intent:**
  - Every status enumeration in templates and gates draws from one set.
  - Every receiving gate's required state can be expressed by its producing template.
  - A corpus search for `LOCKED` as an artifact state is fully dispositioned.
- **Open decision:** DEC-10, the vocabulary. Recommend APPROVED / AMENDED, the producer playbook's and both consumers' existing set. Jarvis proposes; Tony ratifies.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Planning artifacts use DRAFT, APPROVED and AMENDED. APPROVED names the approver, time and exact artifact revision. AMENDED identifies the changed requirements and requires renewed approval before use. A legacy LOCKED label is accepted only with the equivalent approval evidence; relabeling alone does not create approval.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `02_PIPELINE_AGENTS/ARCHITECT_QUESTIONNAIRE.md:70` — ## 📄 APP_BRIEF.md TEMPLATE; MANIFEST ← 1: ARCHITECT_PLAYBOOK.
- `02_PIPELINE_AGENTS/ARCHITECT_PLAYBOOK.md:291` — ## 7. Approval Criteria; MANIFEST ← 6: APP_FACTORY_BLUEPRINT, ARCHITECT_QUESTIONNAIRE, DESIGNER_PLAYBOOK, RECON_QUESTIONNAIRE, FFM_PLAYBOOK, BIM_PLAYBOOK.
- `02_PIPELINE_AGENTS/DESIGNER_PLAYBOOK.md:241` — ## 8. Deliverables + UI_SPEC Template; MANIFEST ← 10: APP_FACTORY_BLUEPRINT, SOFTWARE_FACTORY_PLAYBOOK, ARCHITECT_PLAYBOOK, ENGINEER_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, APP_FACTORY_SKILLS_PLAYBOOK, FFM_PLAYBOOK, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEME_LIBRARY, TOKEN_FILE.
- `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:129` — ## 3. Inputs Required; MANIFEST ← 7: APP_FACTORY_BLUEPRINT, DESIGNER_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, FFM_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:540` — #### 3. Editable Installs Are Mandatory; MANIFEST ← 7: APP_FACTORY_BLUEPRINT, DESIGNER_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, FFM_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:1178` — #### 3. Push Back When Warranted; MANIFEST ← 7: APP_FACTORY_BLUEPRINT, DESIGNER_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, FFM_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `02_PIPELINE_AGENTS/HANDOFF_PACKAGE_PLAYBOOK.md:285` — ## 8. Approval Gates; MANIFEST ← 4: APP_FACTORY_BLUEPRINT, SOFTWARE_FACTORY_PLAYBOOK, ENGINEER_PLAYBOOK, FFM_PLAYBOOK.

**Touch proposal:** C-016. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-016` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-017 — Architect-seat responsibility (including the greenfield UI_SPEC draft) is assigned differently across docs

**Proposed disposition:** BLOCKED. **Authority:** certified correction YES; package outcome remains proposed. CONDITIONAL: DEC-10. 

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/02_agents_handoffs_corrections.md:128`):

- **Certified record:** CF-02 · Severity MEDIUM · Review PARTIAL · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C02-D05 · Fable FBL-D005 (primary)
- **Evidence:** Astra C02 §7 Rank 5; Sol C02 §4 (model A or B; "Do not preserve a phantom artifact stage"); Fable §7 FBL-D005, §9 row 11, §11 decision 4.
- **Defect surfaces (`0a787cb`):**
  - `02_PIPELINE_AGENTS/HANDOFF_PACKAGE_PLAYBOOK.md` §5.5
  - `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md` §3
  - `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md` §2 (Role 3), §4
  - `05_DESIGN_SYSTEM/GLOBAL_DESIGN_SYSTEM_HANDBOOK.md` §8, §11
  - `02_PIPELINE_AGENTS/ARCHITECT_PLAYBOOK.md` §1 ("Not Architect's Job"), §8 handoff and recipient checklist
  - `02_PIPELINE_AGENTS/DESIGNER_PLAYBOOK.md`: required inputs, §8, §10
  - `01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md`: router, Phase 2
- **Defect:**
  - Four downstream docs say the greenfield UI_SPEC is "drafted by the Architect, revised by the Designer". The Architect's handoff and the Designer's inputs never create or transfer such a draft, and the Blueprint makes UI_SPEC a Designer output.
  - More broadly, ARCHITECT §1 excludes UI/UX, schemas and API contracts, while other docs assign the Architect conversion DATA_CONTRACT pre-authoring and full FFM authorship.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - Exactly one greenfield UI_SPEC model is active, and every listed doc reflects it:
    - **(A)** the Architect produces a defined initial UI_SPEC draft and hands it off explicitly; or
    - **(B)** the Designer authors UI_SPEC from approved Architect scope.
  - ARCHITECT §1's exclusions are consistent with the Architect duties other docs assign.
- **Preserve:**
  - The conversion authorship route.
  - Designer final authorship and human approval.
  - Human ownership of product scope.
- **Likely affected docs / consumers:** the surfaces above; Designer and Engineer intake; FC-019, FC-006.
- **Verification intent:**
  - All UI_SPEC provenance statements ("drafted by the Architect", "revised by the Designer") match the chosen model.
  - Under (A), the Architect handoff package contains the draft and the Designer inputs request it; under (B), neither does.
  - ARCHITECT §1 has no exclusion contradicted elsewhere.
- **Open decision:** DEC-10, model A or B (Tony). Fable notes the majority (HANDOFF, ENGINEER, FFM, GDSH) is A; the Blueprint and DESIGNER read as B.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** For greenfield work, the Designer authors UI_SPEC from the approved APP_BRIEF and DATA_CONTRACT. The Architect verifies completeness and consistency during final assembly, and the Director approves the design revision before engineering. The Architect does not silently supply a competing UI_SPEC. Conversion retains its explicitly declared extraction and design inputs.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `02_PIPELINE_AGENTS/ARCHITECT_PLAYBOOK.md:26` — ## 1. Role Definition; MANIFEST ← 6: APP_FACTORY_BLUEPRINT, ARCHITECT_QUESTIONNAIRE, DESIGNER_PLAYBOOK, RECON_QUESTIONNAIRE, FFM_PLAYBOOK, BIM_PLAYBOOK.
- `02_PIPELINE_AGENTS/ARCHITECT_PLAYBOOK.md:330` — ## 8. Handoff Protocol to Designer; MANIFEST ← 6: APP_FACTORY_BLUEPRINT, ARCHITECT_QUESTIONNAIRE, DESIGNER_PLAYBOOK, RECON_QUESTIONNAIRE, FFM_PLAYBOOK, BIM_PLAYBOOK.
- `02_PIPELINE_AGENTS/DESIGNER_PLAYBOOK.md:77` — ## 2. Inputs Required; MANIFEST ← 10: APP_FACTORY_BLUEPRINT, SOFTWARE_FACTORY_PLAYBOOK, ARCHITECT_PLAYBOOK, ENGINEER_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, APP_FACTORY_SKILLS_PLAYBOOK, FFM_PLAYBOOK, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEME_LIBRARY, TOKEN_FILE.
- `02_PIPELINE_AGENTS/DESIGNER_PLAYBOOK.md:241` — ## 8. Deliverables + UI_SPEC Template; MANIFEST ← 10: APP_FACTORY_BLUEPRINT, SOFTWARE_FACTORY_PLAYBOOK, ARCHITECT_PLAYBOOK, ENGINEER_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, APP_FACTORY_SKILLS_PLAYBOOK, FFM_PLAYBOOK, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEME_LIBRARY, TOKEN_FILE.
- `01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md:122` — ## 🔄 THE FULL WORKFLOW; MANIFEST ← 7: SOFTWARE_FACTORY_PLAYBOOK, ARCHITECT_PLAYBOOK, ARCHITECT_QUESTIONNAIRE, ENGINEER_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, RECON_QUESTIONNAIRE, FFM_PLAYBOOK.
- `02_PIPELINE_AGENTS/HANDOFF_PACKAGE_PLAYBOOK.md:81` — ## 5. The Four Canonical Files — Authoring Rules; MANIFEST ← 4: APP_FACTORY_BLUEPRINT, SOFTWARE_FACTORY_PLAYBOOK, ENGINEER_PLAYBOOK, FFM_PLAYBOOK.
- `02_PIPELINE_AGENTS/HANDOFF_PACKAGE_PLAYBOOK.md:83` — ### 5.1 APP_BRIEF.md; MANIFEST ← 4: APP_FACTORY_BLUEPRINT, SOFTWARE_FACTORY_PLAYBOOK, ENGINEER_PLAYBOOK, FFM_PLAYBOOK.
- `02_PIPELINE_AGENTS/HANDOFF_PACKAGE_PLAYBOOK.md:125` — ### 5.2 DATA_CONTRACT.md; MANIFEST ← 4: APP_FACTORY_BLUEPRINT, SOFTWARE_FACTORY_PLAYBOOK, ENGINEER_PLAYBOOK, FFM_PLAYBOOK.
- `02_PIPELINE_AGENTS/HANDOFF_PACKAGE_PLAYBOOK.md:163` — ### 5.3 UI_SPEC.md; MANIFEST ← 4: APP_FACTORY_BLUEPRINT, SOFTWARE_FACTORY_PLAYBOOK, ENGINEER_PLAYBOOK, FFM_PLAYBOOK.
- `02_PIPELINE_AGENTS/HANDOFF_PACKAGE_PLAYBOOK.md:211` — ### 5.4 _project/CLAUDE.md (Project Spine); MANIFEST ← 4: APP_FACTORY_BLUEPRINT, SOFTWARE_FACTORY_PLAYBOOK, ENGINEER_PLAYBOOK, FFM_PLAYBOOK.
- `02_PIPELINE_AGENTS/HANDOFF_PACKAGE_PLAYBOOK.md:245` — ### 5.5 Greenfield Variant; MANIFEST ← 4: APP_FACTORY_BLUEPRINT, SOFTWARE_FACTORY_PLAYBOOK, ENGINEER_PLAYBOOK, FFM_PLAYBOOK.
- `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:129` — ## 3. Inputs Required; MANIFEST ← 7: APP_FACTORY_BLUEPRINT, DESIGNER_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, FFM_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:540` — #### 3. Editable Installs Are Mandatory; MANIFEST ← 7: APP_FACTORY_BLUEPRINT, DESIGNER_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, FFM_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:1178` — #### 3. Push Back When Warranted; MANIFEST ← 7: APP_FACTORY_BLUEPRINT, DESIGNER_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, FFM_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:365` — ## 4. The Two FFM Variants — Conversion vs Greenfield; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:541` — ## 7. Authoring Sequence; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `05_DESIGN_SYSTEM/GLOBAL_DESIGN_SYSTEM_HANDBOOK.md:97` — ## 8. The Designer's deliverables (per project); MANIFEST ← 6: DESIGNER_PLAYBOOK, COMPONENT_REGISTRY, THEME_LIBRARY, THEMING_MANUAL, TOKEN_FILE, UI_UX_BUILDING_MANUAL.

**Touch proposal:** C-017. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-017` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-018 — Mandatory visual intake has no valid path for a supported nonvisual build

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/02_agents_handoffs_corrections.md:161`):

- **Certified record:** CF-02 · Severity MEDIUM · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C02-D06 · Fable none
- **Evidence:** Astra C02 §7 Rank 6; Sol C02 §4 and §6.D; Sol C06 cross-domain item "nonvisual app routing".
- **Defect surfaces (`0a787cb`):**
  - `02_PIPELINE_AGENTS/ARCHITECT_PLAYBOOK.md`: router/type table (Backend Bundle, CLI), inputs and approval checks, DataSync example
  - `02_PIPELINE_AGENTS/ARCHITECT_QUESTIONNAIRE.md`: Q4 (STOP without a visual anchor)
  - `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md`: Part I applicability, Pipeline Track routing, preflight
- **Defect:** the router supports headless and CLI builds, but the Architect inputs, Questionnaire Q4 and Engineer preflight unconditionally require a visual anchor, UI_SPEC and the token/screen package, and STOP without them. There is no not-applicable branch.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - Intake gates follow the approved interface type: visual artifacts are REQUIRED when a visual interface is approved, and explicitly recorded as NOT APPLICABLE when none is.
  - Backend and CLI builds have their own required contract and receiving checklist.
- **Preserve:**
  - The full design package wherever screens exist (Sol: do not weaken visual requirements).
  - UX work for CLIs that need it.
- **Likely affected docs / consumers:** ARCHITECT, ARCHITECT_QUESTIONNAIRE Q4, ENGINEER preflight; FC-075 (theming artifacts); the general REQUIRED / OPTIONAL / NOT APPLICABLE mechanism Sol C02 §6.D flags.
- **Verification intent:**
  - The ARCHITECT DataSync example passes Architect and Engineer gates with recorded N/A visual artifacts and no invented visuals.
  - A UI build still STOPs without a visual anchor.
- **Open decision:** a general applicability mechanism vs a local branch (Jarvis; related backlog C01-S03).
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** The approved interface type determines required design inputs. A visual interface requires its approved UI_SPEC, token/style decisions and HTML/PNG references. A nonvisual backend or CLI explicitly records those inputs as NOT APPLICABLE and supplies its approved data/API/command contract, invocation examples and receiving checklist. Missing required input is not NOT APPLICABLE.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:129` — ## 3. Inputs Required; MANIFEST ← 7: APP_FACTORY_BLUEPRINT, DESIGNER_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, FFM_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:540` — #### 3. Editable Installs Are Mandatory; MANIFEST ← 7: APP_FACTORY_BLUEPRINT, DESIGNER_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, FFM_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:1178` — #### 3. Push Back When Warranted; MANIFEST ← 7: APP_FACTORY_BLUEPRINT, DESIGNER_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, FFM_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `02_PIPELINE_AGENTS/DESIGNER_PLAYBOOK.md:77` — ## 2. Inputs Required; MANIFEST ← 10: APP_FACTORY_BLUEPRINT, SOFTWARE_FACTORY_PLAYBOOK, ARCHITECT_PLAYBOOK, ENGINEER_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, APP_FACTORY_SKILLS_PLAYBOOK, FFM_PLAYBOOK, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEME_LIBRARY, TOKEN_FILE.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:365` — ## 4. The Two FFM Variants — Conversion vs Greenfield; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `02_PIPELINE_AGENTS/HANDOFF_PACKAGE_PLAYBOOK.md:63` — ## 4. Prerequisites Before Authoring; MANIFEST ← 4: APP_FACTORY_BLUEPRINT, SOFTWARE_FACTORY_PLAYBOOK, ENGINEER_PLAYBOOK, FFM_PLAYBOOK.
- `02_PIPELINE_AGENTS/ARCHITECT_PLAYBOOK.md:330` — ## 8. Handoff Protocol to Designer; MANIFEST ← 6: APP_FACTORY_BLUEPRINT, ARCHITECT_QUESTIONNAIRE, DESIGNER_PLAYBOOK, RECON_QUESTIONNAIRE, FFM_PLAYBOOK, BIM_PLAYBOOK.

**Touch proposal:** C-018. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-018` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-019 — Multiple incompatible APP_BRIEF and UI_SPEC templates coexist under a single-source claim

**Proposed disposition:** BLOCKED. **Authority:** certified correction YES; package outcome remains proposed. CONDITIONAL: DEC-10. 

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/02_agents_handoffs_corrections.md:184`):

- **Certified record:** CF-02 · Severity HIGH · Review UNIQUE (Fable) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra none as a defect (C02-S04 suggestion concerns fields inside the canonical template, not template multiplicity) · Fable FBL-D004
- **Evidence:** Fable §7 FBL-D004, §9 row 10, §11 decision 3; Astra C02 §8 (C02-S04).
- **Defect surfaces (`0a787cb`):**
  - `02_PIPELINE_AGENTS/ARCHITECT_QUESTIONNAIRE.md`: "SINGLE SOURCE" claim; 12-section APP_BRIEF
  - `02_PIPELINE_AGENTS/HANDOFF_PACKAGE_PLAYBOOK.md`: §5.1 (14 sections), §5.3 (UI_SPEC, 9), §5.5
  - `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md`: §9.1 / C.2 (13 sections), §9.3 (UI_SPEC, 12)
  - `02_PIPELINE_AGENTS/DESIGNER_PLAYBOOK.md`: §8 (UI_SPEC, 5)
- **Defect:** three APP_BRIEF shapes and three UI_SPEC shapes coexist while one document claims to be the single source.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - Exactly one APP_BRIEF template and one UI_SPEC template exist, or one per pipeline, explicitly declared with a "sections that differ per pipeline" table (Fable).
  - The other locations become pointers, which makes the single-source claim true.
- **Preserve:**
  - The Questionnaire as the authoring instrument.
  - Mandatory planning inputs in the canonical brief (C02-S04).
  - Real conversion/greenfield differences.
  - Uncertainty labels (Astra C02 §5 item 3).
- **Likely affected docs / consumers:** the surfaces above; checks citing "APP_BRIEF § N" (FFM §9 cross-file consistency); FC-016, FC-017.
- **Verification intent:**
  - Each artifact template is defined at one location, and all others link to it.
  - Section-number citations to APP_BRIEF and UI_SPEC across live docs resolve against the canonical template(s).
- **Open decision:** DEC-10, one template vs one per pipeline (Tony; Jarvis proposes).
- **Proposed route:** `SYNC` (multi-doc; LARGE route expected).

**Mapping proposal — ENGINEER-PROPOSED:** The canonical APP_BRIEF template is ARCHITECT_QUESTIONNAIRE, “APP_BRIEF.md TEMPLATE”; the canonical UI_SPEC template is DESIGNER_PLAYBOOK §8. Other template locations link to those owners. Each template declares pipeline-specific sections and nonvisual applicability; producer and receiver use the same approved revision.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `02_PIPELINE_AGENTS/ARCHITECT_QUESTIONNAIRE.md:70` — ## 📄 APP_BRIEF.md TEMPLATE; MANIFEST ← 1: ARCHITECT_PLAYBOOK.
- `02_PIPELINE_AGENTS/ARCHITECT_PLAYBOOK.md:212` — ## 5. APP_BRIEF Template; MANIFEST ← 6: APP_FACTORY_BLUEPRINT, ARCHITECT_QUESTIONNAIRE, DESIGNER_PLAYBOOK, RECON_QUESTIONNAIRE, FFM_PLAYBOOK, BIM_PLAYBOOK.
- `02_PIPELINE_AGENTS/DESIGNER_PLAYBOOK.md:241` — ## 8. Deliverables + UI_SPEC Template; MANIFEST ← 10: APP_FACTORY_BLUEPRINT, SOFTWARE_FACTORY_PLAYBOOK, ARCHITECT_PLAYBOOK, ENGINEER_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, APP_FACTORY_SKILLS_PLAYBOOK, FFM_PLAYBOOK, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEME_LIBRARY, TOKEN_FILE.
- `02_PIPELINE_AGENTS/HANDOFF_PACKAGE_PLAYBOOK.md:81` — ## 5. The Four Canonical Files — Authoring Rules; MANIFEST ← 4: APP_FACTORY_BLUEPRINT, SOFTWARE_FACTORY_PLAYBOOK, ENGINEER_PLAYBOOK, FFM_PLAYBOOK.
- `02_PIPELINE_AGENTS/HANDOFF_PACKAGE_PLAYBOOK.md:83` — ### 5.1 APP_BRIEF.md; MANIFEST ← 4: APP_FACTORY_BLUEPRINT, SOFTWARE_FACTORY_PLAYBOOK, ENGINEER_PLAYBOOK, FFM_PLAYBOOK.
- `02_PIPELINE_AGENTS/HANDOFF_PACKAGE_PLAYBOOK.md:125` — ### 5.2 DATA_CONTRACT.md; MANIFEST ← 4: APP_FACTORY_BLUEPRINT, SOFTWARE_FACTORY_PLAYBOOK, ENGINEER_PLAYBOOK, FFM_PLAYBOOK.
- `02_PIPELINE_AGENTS/HANDOFF_PACKAGE_PLAYBOOK.md:163` — ### 5.3 UI_SPEC.md; MANIFEST ← 4: APP_FACTORY_BLUEPRINT, SOFTWARE_FACTORY_PLAYBOOK, ENGINEER_PLAYBOOK, FFM_PLAYBOOK.
- `02_PIPELINE_AGENTS/HANDOFF_PACKAGE_PLAYBOOK.md:211` — ### 5.4 _project/CLAUDE.md (Project Spine); MANIFEST ← 4: APP_FACTORY_BLUEPRINT, SOFTWARE_FACTORY_PLAYBOOK, ENGINEER_PLAYBOOK, FFM_PLAYBOOK.
- `02_PIPELINE_AGENTS/HANDOFF_PACKAGE_PLAYBOOK.md:245` — ### 5.5 Greenfield Variant; MANIFEST ← 4: APP_FACTORY_BLUEPRINT, SOFTWARE_FACTORY_PLAYBOOK, ENGINEER_PLAYBOOK, FFM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:2236` — ## 23. Appendix C — Template Files (Stubs To Copy); MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.

**Touch proposal:** C-019. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-019` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-020 — TESTING webhook recipe acknowledges success unconditionally, without durable processing or recovery

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/03_build_method_corrections.md:30`):

- **Certified record:** CF-05 · Severity BLOCKER · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C03-D05 · Fable none
- **Evidence:** Astra C03 §7 C03-D05; Sol C03 §3 ("Accept as BLOCKER"; keep separate from the Chunk 05 finding until synthesis because the doctrine owners differ) and §9.A.
- **Defect surfaces (`0a787cb`):**
  - `03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md`: Part 6 G5, §2.2
  - `03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md` §7
  - `03_BUILD_METHODOLOGY/QA_PLAYBOOK.md` §§13, 18
- **Defect:** G5 tells the webhook handler to always return 200 to prevent retries. Processing tests check call shape, not persistence outcome. Nothing requires durable capture, processing success or reconciliation before acknowledging, so a valid event whose business write fails is acknowledged and can be lost.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - TESTING no longer prescribes unconditional success acknowledgment.
  - Acknowledgment follows the approved event-processing contract (DEC-03), which separates two failure phases:
    - **Before durable acceptance.** The handler acknowledges success only after the required state transition has completed, or the event/work has been durably captured or enqueued. If that fails, the response is a retryable non-success, so the provider redelivers.
    - **After durable acceptance.** Once the event is durably accepted, the acknowledgment is lawful. A later worker or processor failure does not retroactively invalidate it. That failure is handled by durable retry/recovery: bounded retries, failed-job visibility, reconciliation and a named recovery owner. Idempotency covers both phases.
  - Webhook tests assert response status and persisted outcome for both phases, plus duplicate delivery and recovery, not only call shape.
- **Preserve:**
  - Signature-failure rejection.
  - "Tests that pass for the wrong reason are worse than tests that fail."
  - BIM §7 per-module failure policy.
  - The testing-tier preservation note above.
- **Likely affected docs / consumers:**
  - TESTING G5 and §2.2.
  - **FC-052** (same mechanism in the ECOM/STRIPE manuals, CF-09, brief 05). Both corrections must converge on one contract.
  - FC-059, FC-062 (CF-09).
  - QA §13/§18 as consumers of the evidence.
- **Verification intent:**
  - A live-corpus search for unconditional-acknowledgment phrasing ("always return 200", "Always return 200") is fully dispositioned, together with FC-052's STRIPE §6 instance.
  - The G5 recipe includes both failure phases:
    - **Failure before durable acceptance** (the capture, enqueue or required write fails) expects a retryable non-success response, and nothing is acknowledged.
    - **Failure after durable acceptance** (the worker fails on an already-accepted event) expects the success acknowledgment to stand, and the test asserts the durable retry/recovery evidence (retry or failed-job state, recovery path) rather than a changed response.
  - A duplicate-delivery case shows idempotent handling.
  - TESTING and the CF-09 manuals state the same acknowledgment contract.
- **Open decision:** DEC-03, the Factory webhook acknowledgment contract, shared with FC-052, FC-059 and FC-062. Jarvis designs; Tony approves. Recommend Sol's synthesis candidate (C05 §7.B): "success must mean the required state transition was completed or durably accepted for recovery."
- **Proposed route:** `SYNC`. **Wave 1 BLOCKER.**

**Mapping proposal — ENGINEER-PROPOSED:** A webhook acknowledges success only after checked completion of the required state transition or checked durable capture/enqueue. Failure before that boundary returns a retryable non-success. Failure after durable acceptance is recovered through bounded durable retries, visible failed work, reconciliation and a named recovery owner; it does not retroactively invalidate the acknowledgment. Test status and persisted outcome for pre-acceptance failure, post-acceptance failure, duplicates and recovery.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:823` — ## 3.8 Run-verification rituals (promoted from Run 001); MANIFEST ← 11: SOFTWARE_FACTORY_PLAYBOOK, ENGINEER_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, API_AND_SERVICES_MANUAL, DATABASE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.

**Touch proposal:** C-020. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-020` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-021 — Payment-error recipe moves sensitive error content into server logs

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/03_build_method_corrections.md:66`):

- **Certified record:** CF-05 · Severity HIGH · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C03-D06 · Fable none
- **Evidence:** Astra C03 §7 C03-D06; Sol C03 §4 ("define an approved structured error record rather than simply suppressing diagnostics").
- **Defect surfaces (`0a787cb`):**
  - `03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md` §4.3
  - `03_BUILD_METHODOLOGY/QA_PLAYBOOK.md` §13 (D7), §29
- **Defect:** TESTING §4.3 acknowledges that payment errors can carry card details, emails and request IDs, then mandates `console.error("Stripe Error:", error)` with no redaction. Its test checks only the response body, while QA forbids PII or secrets in logs.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - TESTING §4.3 prescribes a structured, redacted error record with approved fields instead of logging the raw provider error.
  - Its defensive test asserts both the client response and the log content, using synthetic sensitive markers.
- **Preserve:**
  - The generic-client-message rule and the test that card fragments never reach the client.
  - Enough sanitized context for diagnosis.
- **Likely affected docs / consumers:** TESTING §4.3; ECOM §3 error path (FC-051, response side) and API §3/§6 (FC-064), which belong to the same leakage family; QA §29 evidence redaction.
- **Verification intent:**
  - No live recipe logs a raw provider error object; every `console.error(..., error)`-style hit in recipes is dispositioned.
  - The §4.3 test includes a log assertion.
- **Open decision:** the approved field list (Jarvis). No Director decision is needed.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Return a generic client error. Log only an allow-listed structured record: correlation ID, operation, normalized failure class and safe provider code. Exclude raw exceptions, request bodies, credentials, payment details and personal data. A negative test plants synthetic sensitive markers and asserts that neither client output nor retained logs contain them.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:1089` — ## 4.3 Stripe — wrapper-mock vs constructor-mock decision tree; MANIFEST ← 11: SOFTWARE_FACTORY_PLAYBOOK, ENGINEER_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, API_AND_SERVICES_MANUAL, DATABASE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.
- `03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:1105` — ### 4.3a — Wrapper-mock pattern (StarkReads / v1.0); MANIFEST ← 11: SOFTWARE_FACTORY_PLAYBOOK, ENGINEER_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, API_AND_SERVICES_MANUAL, DATABASE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.
- `03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:1152` — ### 4.3b — Constructor-mock pattern (Dockbloxx); MANIFEST ← 11: SOFTWARE_FACTORY_PLAYBOOK, ENGINEER_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, API_AND_SERVICES_MANUAL, DATABASE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.

**Touch proposal:** C-021. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-021` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-022 — Mutating E2E helpers lack an enforced test-environment boundary

**Proposed disposition:** BLOCKED. **Authority:** certified correction YES; package outcome remains proposed. CONDITIONAL: DEC-14 diagnostic authority. 

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/03_build_method_corrections.md:88`):

- **Certified record:** CF-05 · Severity HIGH · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C03-D08 · Fable none
- **Evidence:** Astra C03 §7 C03-D08; Sol C03 §4 ("fail closed unless the target environment is positively identified as authorized for mutation").
- **Defect surfaces (`0a787cb`):**
  - `03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md` §4.1, §4.4 (and §4.5 fixture regeneration)
  - `03_BUILD_METHODOLOGY/QA_PLAYBOOK.md` §§12, 29–30
- **Defect:** the E2E recipe registers users, seeds subscriptions through an admin client and deletes records against whatever Supabase URL and privileged key are loaded. Nothing checks that the target is an approved test project before mutating.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - Privileged E2E setup and cleanup positively verify the approved test project and test identity before any mutation, and fail closed otherwise.
  - Production confirmation is a separate, bounded, non-destructive procedure.
  - Cleanup is limited to identities the run created and recorded.
- **Preserve:**
  - Synthetic identities and cleanup ordering.
  - Read-only fixture discovery across environments.
  - QA's final-environment-reset rule.
- **Likely affected docs / consumers:** TESTING §4.1/§4.4/§4.5; QA §§12, 29–30; FC-069 (environment-variable naming, CF-07), on which the check may depend.
- **Verification intent:**
  - The recipe contains a pre-mutation target-identity assertion that refuses an unapproved project.
  - The documentation separates mutating E2E from production confirmation.
- **Open decision:** how a test project is positively identified, e.g. an allow-listed project reference vs a marker (Jarvis).
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Before privileged test setup or cleanup, verify the target project reference against the Director-approved test-project allowlist and verify the authorized test identity. Fail closed on mismatch, missing identity or unknown target. Record every run-created identity; cleanup may act only on that set. Production verification is a separately authorized, bounded, non-destructive procedure.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:847` — ## 4.1 Supabase-backed apps (StarkReads example); MANIFEST ← 11: SOFTWARE_FACTORY_PLAYBOOK, ENGINEER_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, API_AND_SERVICES_MANUAL, DATABASE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.

**Touch proposal:** C-022. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-022` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-023 — Local exceptions permit implementation before scope approval

**Proposed disposition:** BLOCKED. **Authority:** certified correction YES; package outcome remains proposed. CONDITIONAL: DEC-14. 

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/03_build_method_corrections.md:170`):

- **Certified record:** CF-03 · Severity HIGH · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C03-D04 · Fable none
- **Evidence:** Astra C03 §7 C03-D04; Sol C03 §4 ("STOP affected work → present evidence → request minimal amendment → receive approval → continue"; emergency procedures must be "explicit and bounded") and §9.B.
- **Defect surfaces (`0a787cb`):**
  - `03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md` §7
  - `03_BUILD_METHODOLOGY/FEAT_PLAYBOOK.md` §2 (imports BIM)
  - `03_BUILD_METHODOLOGY/BUG_FIX_PLAYBOOK.md` §3
  - `03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md` §3.3
  - Contrary rules: `03_BUILD_METHODOLOGY/APP_FACTORY_SKILLS_PLAYBOOK.md` §13 (Anti-Pattern 8), `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md` §2.5, `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md` §15
- **Defect:**
  - BIM §7 lets the Engineer step outside the enumerated writable surface when they judge it genuinely required, with ratification afterwards. FEAT imports this and FIX repeats it.
  - TESTING §3.3 says to fix HIGH security findings inline.
  - Both conflict with the prior-approval rules.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - No doctrine permits implementation outside the approved writable surface with after-the-fact ratification.
  - A newly necessary change follows: STOP the affected work → evidence → minimal amendment → approval → continue.
  - A newly found HIGH security issue is escalated promptly, not fixed inline without approval.
  - Any emergency path is explicit and bounded.
- **Preserve:**
  - Urgency of security escalation.
  - Explicitly approved conditional surfaces.
  - BUG_FIX scope protection.
- **Likely affected docs / consumers:** BIM §7, FEAT §2, BUG_FIX §3, TESTING §3.3; Engineer and Coordinator seats; FC-012.
- **Verification intent:**
  - A live-corpus search for ratification-after-action language and "fix inline" guidance is fully dispositioned, with none authorizing pre-approval action.
  - The BIM §7 writable-surface clause contains no open-ended exception.
- **Open decision:** DEC-14, whether to define a bounded emergency procedure now or defer it (Tony).
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** A newly necessary change outside the approved writable surface stops the affected work. Record evidence, propose the smallest scope amendment, obtain approval, then continue. Escalate a newly discovered high-severity security issue promptly; do not implement it under after-the-fact approval. No emergency implementation exception is created here.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:1139` — ## 15. Agentic Coding Constitution (Karpathy Protocol); MANIFEST ← 7: APP_FACTORY_BLUEPRINT, DESIGNER_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, FFM_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:650` — ## 3.4 Audit-then-add when joining an existing project; MANIFEST ← 11: SOFTWARE_FACTORY_PLAYBOOK, ENGINEER_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, API_AND_SERVICES_MANUAL, DATABASE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:616` — ## 8. File-By-File Authoring Guide — Root Files; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:620` — ### 8.1 — Root `CLAUDE.md`; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:659` — ### 8.2 — Root `README.md`; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:693` — ### 8.3 — `AGENTS.md`; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:713` — ### 8.4 — `GEMINI.md`; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.

**Touch proposal:** C-023. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-023` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-024 — E2E workaround recipe can remove a shipped failure from the system under test

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/03_build_method_corrections.md:112`):

- **Certified record:** CF-05 · Severity HIGH · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C03-D09 · Fable none
- **Evidence:** Astra C03 §7 C03-D09; Sol C03 §4 ("Any dependency-disabled run must be labeled as diagnostic/isolated evidence").
- **Defect surfaces (`0a787cb`):**
  - `03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md` §§3.5–3.6, Part 6 G11
  - `03_BUILD_METHODOLOGY/QA_PLAYBOOK.md` §§11–12, 19, 34
- **Defect:** TESTING recommends aborting or neutralizing a production-present script during E2E and presents that as a fix. It requires neither a reduced-coverage label nor verification with the script enabled, so the suite can go green while users still hit the failure.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - Dependency-disabled runs are labeled diagnostic or isolated evidence.
  - The full-environment flow stays FAILED or BLOCKED until it is fixed or covered by an approved compensating verification.
  - The coverage limitation is carried into the Gate Q evidence.
- **Preserve:** isolation as a diagnostic tool; the §3.6 documented skip path with a verified manual replacement, which is not the defect.
- **Likely affected docs / consumers:** TESTING §3.5, §3.6, G11; QA Gate Q (§12); FC-063.
- **Verification intent:**
  - G11 no longer presents neutralization as an unlabeled fix.
  - The recipe requires a coverage-limitation note in the Gate Q evidence.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** A run with a dependency disabled is diagnostic or isolated evidence. The full-environment flow remains FAILED or BLOCKED until repaired or covered by an explicitly approved compensating verification. Carry the omitted dependency, affected claims and coverage limitation into Gate Q evidence.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:705` — ## 3.6 Skip-and-document as a Factory pattern; MANIFEST ← 11: SOFTWARE_FACTORY_PLAYBOOK, ENGINEER_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, API_AND_SERVICES_MANUAL, DATABASE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.

**Touch proposal:** C-024. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-024` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-025 — FFM (and combined-artifact allowances) omit the mandatory `ACCEPTANCE_SPEC.md` lifecycle and QA handoff

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/03_build_method_corrections.md:223`):

- **Certified record:** CF-04 · Severity HIGH · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C03-D03 · Fable none
- **Evidence:** Astra C03 §7 C03-D03; Sol C03 §4 (a generic "equivalent artifact" allowance cannot override the Factory-wide filename and lifecycle rule; reinforces C01-D02/C02-D01 but should not be merged).
- **Defect surfaces (`0a787cb`):**
  - `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md` §§2–3, 12–13, 18, Appendix A
  - `03_BUILD_METHODOLOGY/QA_PLAYBOOK.md` §§6, 20
  - `03_BUILD_METHODOLOGY/BUG_FIX_PLAYBOOK.md` §18
  - `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md` §2.5
  - `03_BUILD_METHODOLOGY/FRONTEND_BUILD_PHASE_PLAYBOOK.md` §9 (correct)
- **Defect:**
  - FFM's folder trees, file guides, handoff diagram and authoring checklist have no `ACCEPTANCE_SPEC.md` creation or finalization step and no QA intake.
  - QA §§6/20 accept "equivalent" artifacts and BUG_FIX §18 allows combined documents, both against SFP §2.5's exact-filename mandate.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - FFM's anatomy, authoring sequence, boot/verification instructions and completion checklist include, by reference to the shared contract:
    - `ACCEPTANCE_SPEC.md` creation from a pre-implementation approved basis
    - its maintenance and finalization
    - the QA handoff
  - QA's "equivalent artifact" and BUG_FIX's combined-document allowances are limited to contexts the Factory rule actually exempts.
- **Preserve:**
  - SFP §2.5's exact-filename rule and mandatory Gate Q.
  - FBP §9's correct Gate Q/D requirement.
  - Proportional ceremony for small fixes within the rule (backlog C03-S02).
- **Likely affected docs / consumers:** FFM, QA §6/§20, BUG_FIX §18; FC-002, FC-013, FC-026 (sequence together).
- **Verification intent:**
  - The FFM Appendix A checklist contains the ACCEPTANCE_SPEC steps.
  - QA §6/§20 no longer admit a non-exempt substitute.
  - BUG_FIX §18 keeps the filename even when combining content.
- **Open decision:** whether a BUG_FIX small fix may carry all its acceptance content inside one `ACCEPTANCE_SPEC.md` (Jarvis).
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Every newly authored module includes ACCEPTANCE_SPEC.md based on the approved pre-implementation contract. The Architect prepares acceptance requirements; Engineering records factual completion without changing success criteria; independent QA evaluates them. Finalize the factual handoff before the engineering stop. A small FIX may combine supporting records, but it still supplies ACCEPTANCE_SPEC.md; runtime modules do not inherit a documentation-only waiver.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:261` — ## 3. FFM Anatomy — The Folder Structure; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:541` — ## 7. Authoring Sequence; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:616` — ## 8. File-By-File Authoring Guide — Root Files; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:620` — ### 8.1 — Root `CLAUDE.md`; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:659` — ### 8.2 — Root `README.md`; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:693` — ### 8.3 — `AGENTS.md`; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:713` — ### 8.4 — `GEMINI.md`; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1367` — ## 13. File-By-File Authoring Guide — `verification/`; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1371` — ### 13.1 — `verification/PHASE_GATES.md`; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1400` — ### 13.2 — `verification/BUILD_CHECKLIST.md`; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1414` — ### 13.3 — Authoring Discipline; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1828` — ## 18. The Authoring Checklist; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:2065` — ## 21. Appendix A — Skeleton Folder Tree; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:2141` — ## 22. Appendix B — Boot Prompts; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/BUG_FIX_PLAYBOOK.md:573` — ## 18. Required FIX Artifacts; MANIFEST ← 3: QA_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.
- `03_BUILD_METHODOLOGY/QA_PLAYBOOK.md:260` — # 6. The Engineer Handoff Is a Claim Package; MANIFEST ← 3: BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.

**Touch proposal:** C-025. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-025` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-026 — Whole-folder module freeze conflicts with required in-folder working artifacts

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/03_build_method_corrections.md:255`):

- **Certified record:** CF-04 · Severity MEDIUM · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C03-D01 · Fable none
- **Evidence:** Astra C03 §7 C03-D01; Sol C03 §5 (provisional MEDIUM, closed MEDIUM 2026-09-27; distinguish "IMMUTABLE APPROVED INPUTS from AUTHORIZED WORKING / EVIDENCE OUTPUTS").
- **Defect surfaces (`0a787cb`):**
  - `03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md` §§4, 6–8
  - `03_BUILD_METHODOLOGY/BUG_FIX_PLAYBOOK.md` §§16, 18
  - `03_BUILD_METHODOLOGY/FEAT_PLAYBOOK.md` §2
  - `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md` §2.5
- **Defect:** BIM freezes the whole module folder from Plan Mode to STOP ("nothing inside may be added or edited"), yet requires the Engineer to maintain and finalize `ACCEPTANCE_SPEC.md`, which lives inside that folder. FIX repeats this; FEAT imports it.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):** the freeze rule distinguishes immutable approved inputs from authorized working and evidence outputs. It states:
  - which files stay writable during the hold, and by whom;
  - where updates are staged and who admits them;
  - when the spec is finalized relative to STOP.
  Requirement changes still need approval.
- **Preserve:**
  - The freeze's purpose: no scope drift during execution (Fable §6 item 4).
  - Approval for requirement changes.
- **Likely affected docs / consumers:** BIM, BUG_FIX, FEAT (inherits); QA §20 artifact home (FC-013).
- **Verification intent:**
  - Following BIM literally, an Engineer can maintain and finalize the spec without violating any freeze sentence.
  - FIX and FEAT inherit the same rule.
- **Open decision:** DEC-13, the freeze model (Jarvis), joint with FC-013.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Freeze requirements and acceptance criteria at handoff. Declare owner-specific writable lanes inside the module for engineering handoff, recon, plans, evidence, findings and attributable rulings. QA records belong in the module’s QAM under agent_docs/. Contract changes require an approved amendment; neither a test-plan edit nor a new evidence file silently amends the contract.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md:46` — ## 4. The Module Package (one folder, self-contained); MANIFEST ← 1: FEAT_PLAYBOOK.
- `03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md:77` — ## 6. Lifecycle (the stage-gate chain); MANIFEST ← 1: FEAT_PLAYBOOK.
- `03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md:150` — ## 11. Anti-Patterns (block these); MANIFEST ← 1: FEAT_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:541` — ## 7. Authoring Sequence; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/QA_PLAYBOOK.md:1185` — # 20. QA Deliverables; MANIFEST ← 3: BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.

**Touch proposal:** C-026. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-026` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-027 — Greenfield DATA_CONTRACT authorship and timing are not executable as written

**Proposed disposition:** BLOCKED. **Authority:** certified correction YES; package outcome remains proposed. CONDITIONAL: DEC-11. 

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/03_build_method_corrections.md:311`):

- **Certified record:** CF-02 · Severity HIGH · Review PARTIAL · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C03-D07 · Fable FBL-D014 (primary)
- **Severity divergence (recorded):** Astra HIGH vs Fable MEDIUM. The certified HIGH stands.
- **Evidence:** Astra C03 §7 C03-D07; Sol C03 §4 (reinforces C02-D03) and §9.C; Fable §7 FBL-D014, §11 decision 6.
- **Defect surfaces (`0a787cb`):**
  - `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md` §§7, 9.2, 12.4, 14, 18
  - `03_BUILD_METHODOLOGY/FRONTEND_FIRST_PLAYBOOK.md` §3
  - `01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md` Phase 3/4
  - `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md` §§1–3, §12 ("Author: Engineer Agent")
- **Defect:** doctrine assigns the greenfield DATA_CONTRACT to the Engineer, yet the execution sequence either:
  - has the Engineer consume an unfinished "contract shell" (§12.4 goes straight to types); or
  - hands authorship back to another seat (§14).
  §18 checks for a fully populated contract, and the Blueprint names two Engineer actors.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - FFM's authoring and execution sequences have explicit conversion and greenfield branches.
  - Greenfield: Engineer authorship and approval of DATA_CONTRACT come before type and service implementation (before the freeze, if Fable's model is chosen).
  - §14 no longer reassigns authorship to the Architect, and §18 accepts a shell only at the specified earlier handoff.
  - The Engineer seat's identity is stated the same way everywhere.
- **Preserve:**
  - Conversion's complete pre-authored contract path.
  - ENGINEER §3's per-pipeline author of record.
  - FRONTEND_FIRST §3's contract-before-mock-UI rule.
- **Likely affected docs / consumers:** FFM, FRONTEND_FIRST §3, Blueprint, ENGINEER §12; FC-015 (pre-implementation approval), FC-006 (seat identity).
- **Verification intent:**
  - The FFM §12.4 greenfield branch has an authoring + approval step before Types.
  - §14 and §18 agree with it.
  - Blueprint Phase 3/4 name the same Engineer seat.
  - FRONTEND_FIRST §3 can be satisfied in sequence.
- **Open decision:** DEC-11 (Fable §11 decision 6). Is the Engineer Claudy in every context, and when is the greenfield DATA_CONTRACT completed? (Tony)
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Conversion consumes its approved extracted DATA_CONTRACT. Greenfield uses the Architect-prepared DATA_CONTRACT approved before Design and implementation. The Engineer verifies prerequisites and consumes that revision; a contract shell is not permission to implement types or services. Reopen a missing or conflicting contract through the amendment lane, not by silently changing authorship during execution.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:365` — ## 4. The Two FFM Variants — Conversion vs Greenfield; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:541` — ## 7. Authoring Sequence; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1422` — ## 14. The Extractor Question — When To Run Brain Drain; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1828` — ## 18. The Authoring Checklist; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:129` — ## 3. Inputs Required; MANIFEST ← 7: APP_FACTORY_BLUEPRINT, DESIGNER_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, FFM_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:540` — #### 3. Editable Installs Are Mandatory; MANIFEST ← 7: APP_FACTORY_BLUEPRINT, DESIGNER_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, FFM_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:1178` — #### 3. Push Back When Warranted; MANIFEST ← 7: APP_FACTORY_BLUEPRINT, DESIGNER_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, FFM_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `02_PIPELINE_AGENTS/ARCHITECT_PLAYBOOK.md:330` — ## 8. Handoff Protocol to Designer; MANIFEST ← 6: APP_FACTORY_BLUEPRINT, ARCHITECT_QUESTIONNAIRE, DESIGNER_PLAYBOOK, RECON_QUESTIONNAIRE, FFM_PLAYBOOK, BIM_PLAYBOOK.

**Touch proposal:** C-027. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-027` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-028 — FFM prescribes the auth-service wrapper that kit-consumption doctrine forbids

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/03_build_method_corrections.md:281`):

- **Certified record:** CF-04 · Severity HIGH · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C03-D02 · Fable none as primary
- **Evidence:**
  - Astra C03 §7 C03-D02.
  - Sol C03 §4: "preserve legitimate domain-specific enrichment while forbidding wrappers whose only purpose is to re-expose already complete kit behavior".
  - Register see-also: FBL-D001's APP_ARCHITECTURE §2 sub-claim, which FC-033 covers.
- **Defect surfaces (`0a787cb`):**
  - `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md` §9.2, §12.4
  - `03_BUILD_METHODOLOGY/FRONTEND_FIRST_PLAYBOOK.md` §0
  - `03_BUILD_METHODOLOGY/FRONTEND_BUILD_PHASE_PLAYBOOK.md` §1.6
  - `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md` §5
- **Defect:** FFM's auth-service contract and its service sub-phase tell the builder to wrap the kit's `getUser()` / `signInWithPassword()` in `/src/services/`. FRONTEND_FIRST §0 and FBP §1.6 prohibit redundant `authService.ts` wrappers.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - FFM's sample auth contract and service sub-phase default to direct kit-auth consumption.
  - A wrapper that only re-exposes complete kit behavior is not prescribed.
  - Genuinely missing domain auth behavior needs recon-backed justification.
- **Preserve:**
  - The Kit Exception and the "Should I Author This?" verdict table (Fable §6 item 2).
  - The service layer for project-specific domain logic (ENGINEER §5).
- **Likely affected docs / consumers:** FFM §9.2/§12.4; consistency with FRONTEND_FIRST §0, FBP §1.6, `04_REFERENCE_MANUALS/AUTH_MANUAL.md` §0, `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md` §1; FC-033 (APP_ARCHITECTURE §2 `authServices.ts`).
- **Verification intent:**
  - The FFM sample contract wraps no kit `getUser` or `signIn` primitive.
  - A live-corpus search for `authService` returns only prohibitions or justified domain enrichment.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Consume complete kit auth primitives directly. Do not create an auth service whose only purpose is to re-expose kit behavior. A genuinely missing domain capability requires recon evidence, a bounded approved contract and its own verification; it does not authorize replacing the kit’s auth authority.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:739` — ## 9. File-By-File Authoring Guide — `_project/`; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:743` — ### 9.1 — `_project/APP_BRIEF.md`; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:793` — ### 9.2 — `_project/DATA_CONTRACT.md`; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:854` — ### 9.3 — `_project/UI_SPEC.md`; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:900` — ### 9.4 — `_project/CLAUDE.md`; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1246` — ## 12. File-By-File Authoring Guide — `playbook/`; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1250` — ### 12.1 — Overall Structure; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1266` — ### 12.2 — `00-OVERVIEW.md`; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1283` — ### 12.3 — `01-DISCOVERY.md` Through `06-VERIFICATION.md` (And `07-RETROSPECTIVE.md`); MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1296` — ### 12.4 — Per-Sub-Phase Authoring Notes; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1338` — ### 12.5 — `RETROSPECTIVES/` Folder; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1356` — ### 12.6 — Playbook Reuse Discipline; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.

**Touch proposal:** C-028. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-028` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-029 — FFM gives two different documents final scope authority

**Proposed disposition:** BLOCKED. **Authority:** certified correction YES; package outcome remains proposed. CONDITIONAL: DEC-14 / DEC-06. 

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/03_build_method_corrections.md:201`):

- **Certified record:** CF-03 · Severity MEDIUM · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C03-D13 · Fable none as primary
- **Evidence:** Astra C03 §7 C03-D13; Sol C03 §6 ("One artifact should hold scope authority; derivative summaries should defer to it and STOP on disagreement").
- **Defect surfaces (`0a787cb`):** `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md` §9.1, §9.4 (Cross-File Consistency), Appendix C.1.
- **Defect:** §9.1 makes APP_BRIEF the single source of truth for scope, while the copyable root-manager stub says `_project/CLAUDE.md` wins on scope.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - One artifact holds scope authority. APP_BRIEF is recommended, per FFM §9.1.
  - The C.1 stub and every manager defer to it.
  - A disagreement stops the affected work.
- **Preserve:** the invariant that duplicated forbidden zones must match; the STOP rule.
- **Likely affected docs / consumers:**
  - FFM §9.1 and C.1.
  - `_project/CLAUDE.md` stubs already generated in downstream modules carry the old text (`XB-EXT` awareness only).
  - FC-005.
- **Verification intent:** the C.1 stub text defers to the chosen authority, and no "wins on scope" statement for another artifact remains.
- **Open decision:** DEC-14, the scope-authority artifact (Tony; APP_BRIEF recommended).
- **Proposed route:** `SYNC` (+ `XB-EXT` awareness).

**Mapping proposal — ENGINEER-PROPOSED:** APP_BRIEF is the module scope authority. Managers and startup stubs route to its approved revision; DATA_CONTRACT and UI_SPEC define their respective contracts within that scope. A disagreement stops the affected work for an attributable ruling. A manager’s summary never silently expands or overrides APP_BRIEF.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:739` — ## 9. File-By-File Authoring Guide — `_project/`; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:743` — ### 9.1 — `_project/APP_BRIEF.md`; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:793` — ### 9.2 — `_project/DATA_CONTRACT.md`; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:854` — ### 9.3 — `_project/UI_SPEC.md`; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:900` — ### 9.4 — `_project/CLAUDE.md`; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:2236` — ## 23. Appendix C — Template Files (Stubs To Copy); MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.

**Touch proposal:** C-029. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-029` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-030 — Fixture discovery can publish unusable roles, and its consumer reads a different count field

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/03_build_method_corrections.md:133`):

- **Certified record:** CF-05 · Severity MEDIUM · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C03-D12 · Fable none
- **Evidence:** Astra C03 §7 C03-D12; Sol C03 §6.
- **Defect surfaces (`0a787cb`):** `03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md` §§2.3, 4.4–4.5 (coupon rules at §§2.1, 3.7).
- **Defect:**
  - Discovery labels roles without checking that they exist or meet their prerequisites, so it can write "successful" JSON with empty roles.
  - The pagination consumer reads `.product_count`, but discovery preserved `.count`.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - Discovery validates a normalized fixture schema and scenario eligibility (role existence, coupon prerequisites) before reporting success, and uses one count property.
  - A missing required role yields an explicit setup BLOCKED result; optional absence is recorded deliberately.
- **Preserve:** the fixture-discovery concept and environment-following read-only discovery.
- **Likely affected docs / consumers:** TESTING §§2.3, 4.4–4.5; consumers of the fixture JSON.
- **Verification intent:**
  - The documented empty-dataset case yields BLOCKED, not success.
  - Producer and consumer use the same count field.
  - Coupon eligibility checks reference the §2.1/§3.7 rules.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Fixture discovery returns one normalized record with role identities, scenario eligibility and a single count field named count. Validate role existence and coupon prerequisites before declaring readiness. A missing required role produces BLOCKED with the missing prerequisite; optional absence is recorded explicitly. Producers and consumers read count, not competing count aliases.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:1256` — ## 4.4 Test data sourcing — discovered vs declared; MANIFEST ← 11: SOFTWARE_FACTORY_PLAYBOOK, ENGINEER_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, API_AND_SERVICES_MANUAL, DATABASE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.

**Touch proposal:** C-030. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-030` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-031 — Metadata helper cannot distinguish an absent key from a present null

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/03_build_method_corrections.md:154`):

- **Certified record:** CF-05 · Severity MEDIUM · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C03-D11 · Fable none
- **Evidence:** Astra C03 §7 C03-D11; Sol C03 §6.
- **Defect surfaces (`0a787cb`):** `03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md` §4.2, "Key-absent vs empty-value distinction".
- **Defect:** §4.2 requires distinguishing a missing key from a present empty value, but the sample `entry ? entry.value : null` returns `null` in both cases.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):** the helper returns an explicit presence/value result, or a distinct absence sentinel, under a documented contract, with examples for absent, null, zero and empty string.
- **Preserve:** the absent-vs-empty requirement itself.
- **Likely affected docs / consumers:** TESTING §4.2 and tests built from it.
- **Verification intent:** evaluating the documented helper on {absent, null, 0, ""} yields four distinguishable results that match the documented contract.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Metadata lookup returns { present: false } for an absent key and { present: true, value } for a present key. Null, zero and the empty string remain present values. Test all four cases; never use null for both absence and a stored null.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:955` — ## 4.2 REST-backed apps (Dockbloxx / WooCommerce example); MANIFEST ← 11: SOFTWARE_FACTORY_PLAYBOOK, ENGINEER_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, API_AND_SERVICES_MANUAL, DATABASE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.

**Touch proposal:** C-031. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-031` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-032 — FRONTEND_BUILD_PHASE checklist points Gate Q / Gate D to the wrong QA_PLAYBOOK sections

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/03_build_method_corrections.md:346`):

- **Certified record:** CF-13 · Severity LOW · Review CONFIRMED · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C03-D14 · Fable FBL-D025 (primary)
- **Evidence:** Astra C03 §7 C03-D14; Sol C03 §7; Fable §7 FBL-D025, §9 row 20.
- **Defect surfaces (`0a787cb`):**
  - `03_BUILD_METHODOLOGY/FRONTEND_BUILD_PHASE_PLAYBOOK.md` §9
  - `03_BUILD_METHODOLOGY/QA_PLAYBOOK.md` §§9–10 (actual: §12 Gate Q, §13 Gate D)
  - Process evidence: `agent_docs/RESPONSES/response_2026-08-10_194109_phase2-ripple-map.md` (at `0a787cb`; deleted from the working tree by Director ruling and present in history).
- **Defect:** FBP §9 cites QA §9 for Gate Q and §10 for Gate D. In the live QA doc those are Engagement Lifecycle and Scope Protection.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - FBP §9 points to the live QA gate sections, preferably by stable heading name.
  - Inbound anchor checks become part of sync consistency checking. The process side is covered by DocSet Sync D19 and FC-087.
- **Preserve:** the Gate Q/D requirement in FBP §9.
- **Likely affected docs / consumers:** FBP §9; any other inbound QA anchor citations.
- **Verification intent:**
  - Both references resolve to the "Gate Q" and "Gate D" headings at the candidate SHA.
  - A propagation search for `QA_PLAYBOOK.md` §9/§10 citations is fully dispositioned.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Gate Q refers to QA_PLAYBOOK §12, “Gate Q”; Gate D refers to QA_PLAYBOOK §13, “Gate D”. These are distinct checks; frontend build success and demo deployment satisfy neither gate by themselves.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `03_BUILD_METHODOLOGY/FRONTEND_BUILD_PHASE_PLAYBOOK.md:417` — ## 9. UI Phase Completion Checklist; MANIFEST ← 4: ENGINEER_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, TESTING_PLAYBOOK, UI_UX_BUILDING_MANUAL.

**Touch proposal:** C-032. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-032` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-033 — AUTH_MANUAL privileged recipes authorize from `user_metadata`, recreate competing role stores and supply an app-side superadmin-creation surface

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/04_auth_data_security_corrections.md:37`):

- **Certified record:** CF-06 · Severity BLOCKER · Review CONFIRMED · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C04-D01 · Fable FBL-D001 (primary; also related to FC-001 and FC-035)
- **Evidence:**
  - Astra C04 §7 C04-D01.
  - Sol C04 §3: "Valid BLOCKER… preserve the single-authority model rather than patch individual snippets independently."
  - Fable §7 FBL-D001, §9 rows 1–3 and 5, §11 decision 1.
- **Defect surfaces (`0a787cb`):**
  - `04_REFERENCE_MANUALS/AUTH_MANUAL.md`: Key Principle 5, "Where Roles Live", §12 SuperAdmin routes, §13 mirror table with a `role` column, Summary, registration flow (`is_qr_*` defaults)
  - `04_REFERENCE_MANUALS/DATABASE_MANUAL.md` §2 (Roles Table, User Mirror)
  - `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md` §§1–2
  - `04_REFERENCE_MANUALS/APP_ARCHITECTURE_MANUAL.md`: §2 (`authServices.ts` in the standard layout), §10 (middleware reads `user.user_metadata?.role`)
  - Grep gates that should catch this: `02_PIPELINE_AGENTS/RECON_QUESTIONNAIRE.md` Q3.4, `03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md` §3.8
- **Defect:**
  - The kit auth authority's own privileged recipes:
    - check `requester.user_metadata.is_qr_superadmin`;
    - create superadmins from the app;
    - add a `role` column to a mirror table.
  - Its Summary says roles live in metadata.
  - APP_ARCHITECTURE adds a forbidden wrapper and metadata-based middleware.
  - All of this contradicts "Where Roles Live", DATABASE §2 and STARTER_KIT §§1–2. The legacy advisory does not cover these recipes.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):** every live recipe uses one role authority, the role table, so that:
  - no privileged check reads `user_metadata`;
  - no app-side superadmin-creation surface exists (creation stays console-only);
  - no profile mirror carries an authorization column;
  - the AUTH Summary states the same model;
  - APP_ARCHITECTURE §2 does not list an auth wrapper, and §10 does not authorize from metadata.

  **Two separate things are proposed:**
  - **(1) Retire the unsafe existing routes. This is required.** The current AUTH §12 `add-user` / `delete-user` / `get-users` recipes authorize from `user_metadata` and include app-side superadmin creation. They are removed, quarantined as labeled LEGACY history, or rewritten (DEC-02).
  - **(2) No blanket prohibition on future authorized operations.** Privileged list or delete operations (other than superadmin creation) stay permissible doctrine when they:
    - authorize the current requester through the trusted role authority (the role table);
    - perform operation-local authorization (DEC-04 / FC-036);
    - use the correct elevated client only after that check (FC-038);
    - allow only approved target roles;
    - protect privileged targets.

  Superadmin creation stays console-only in every case.
- **Preserve:**
  - The domain preservation list above.
  - Console-only superadmin creation.
  - Trusted (role-table) authorization.
  - Legitimate, properly authorized administrative list/delete capability.
  - Sol C01 §5.A: keep FC-001 (governance) and this record separate.
  - The existing `_ARCHIVE/` discipline if quarantine-to-archive is chosen.
- **Likely affected docs / consumers:** AUTH_MANUAL, DATABASE_MANUAL §2, STARTER_KIT_HANDBOOK §§1–2, APP_ARCHITECTURE §2/§10, MANIFEST row; FC-001, FC-034, FC-035, FC-036, FC-038, FC-039, FC-041; RECON Q3.4 and TESTING §3.8 as verification consumers.
- **Verification intent:**
  - A live-corpus grep for metadata authorization (`is_qr_superadmin`, `user_metadata?.role`, `user_metadata.is_`) leaves zero undispositioned hits; any survivor is a labeled display hint or transport case.
  - The existing metadata-authorized §12 routes no longer appear as live patterns (removed, LEGACY-quarantined or rewritten).
  - No app-side superadmin-creation route is presented as a pattern.
  - Any privileged list or delete pattern that remains (or is added) shows:
    - role-table authorization of the requester;
    - operation-local checks before the elevated client is used;
    - an approved-target-role allow-list;
    - protection of privileged targets.
  - No recipe adds `role` to a profile mirror.
  - APP_ARCHITECTURE §2 has no `authServices.ts`.
  - The RECON Q3.4 grep gate passes when run against the doctrine itself.
- **Open decision:** DEC-02, retire/archive vs rewrite (Fable §11 decision 1). Rewriting needs disk verification of the kit (`protectPage` return shape, `useAuthStore`, cookie flag), and that kit repository is outside this package (GAP).
  - **Recommendation: containment first, then correction.** Remove or quarantine the unsafe routes with a pointer to the governing rule early; rewrite or replace against the verified kit afterwards.
  - **Containment ≠ correction.** Quarantining §12 contains the risk but does **not** close FC-033 while any other listed surface still contradicts the single role authority: the Summary, the §13 mirror `role` column, APP_ARCHITECTURE §2/§10 and the registration-flow metadata. FC-033 is corrected only when every outcome bullet has landed and its verification intent passes.
- **Proposed route:** `SYNC`. **Wave 1 BLOCKER.**

**Mapping proposal — ENGINEER-PROPOSED:** The role table is the only authorization authority. Never authorize from user_metadata or a profile mirror. Superadmin creation is console-only; no app-side superadmin creation route is provided. Retire the metadata-authorized add-user, delete-user and get-users recipes. Future privileged list/delete operations remain possible only with trusted current-role lookup, operation-local authorization before elevated capability, an approved target-role allowlist and privileged-target protection. Profile mirrors contain profile data, not authorization columns. Registration metadata is not authorization.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `04_REFERENCE_MANUALS/AUTH_MANUAL.md:130` — ## Overview & Architecture; MANIFEST ← 4: APP_ARCHITECTURE_MANUAL, DATABASE_MANUAL, STATE_MANAGEMENT_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/AUTH_MANUAL.md:344` — ## Authentication Flow; MANIFEST ← 4: APP_ARCHITECTURE_MANUAL, DATABASE_MANUAL, STATE_MANAGEMENT_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/AUTH_MANUAL.md:1761` — ## 12. SuperAdmin User Management; MANIFEST ← 4: APP_ARCHITECTURE_MANUAL, DATABASE_MANUAL, STATE_MANAGEMENT_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/AUTH_MANUAL.md:1932` — ## 13. User Mirror Table Pattern; MANIFEST ← 4: APP_ARCHITECTURE_MANUAL, DATABASE_MANUAL, STATE_MANAGEMENT_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/AUTH_MANUAL.md:2203` — ## Summary; MANIFEST ← 4: APP_ARCHITECTURE_MANUAL, DATABASE_MANUAL, STATE_MANAGEMENT_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/APP_ARCHITECTURE_MANUAL.md:96` — ## 2. Project Structure; MANIFEST ← 3: ECOMMERCE_AND_PAYMENTS_MANUAL, STATE_MANAGEMENT_MANUAL, THEMING_MANUAL.
- `04_REFERENCE_MANUALS/APP_ARCHITECTURE_MANUAL.md:1141` — ## 10. Security Architecture; MANIFEST ← 3: ECOMMERCE_AND_PAYMENTS_MANUAL, STATE_MANAGEMENT_MANUAL, THEMING_MANUAL.
- `04_REFERENCE_MANUALS/DATABASE_MANUAL.md:83` — ## 2. Schema Design Patterns; MANIFEST ← 2: API_AND_SERVICES_MANUAL, AUTH_MANUAL.

**Touch proposal:** C-033. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-033` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-034 — Public signup forwards caller-controlled role metadata into the role-creation trigger path

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/04_auth_data_security_corrections.md:101`):

- **Certified record:** CF-06 · Severity BLOCKER · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C04-D03 · Fable none as primary
- **Evidence:** Astra C04 §7 C04-D03; Sol C04 §3 ("The doctrine defect is valid and severe enough to remain BLOCKER"; installed trigger state UNKNOWN).
- **Defect surfaces (`0a787cb`):**
  - `04_REFERENCE_MANUALS/AUTH_MANUAL.md`: signup API, registration flow, "Where Roles Live"
  - `04_REFERENCE_MANUALS/DATABASE_MANUAL.md` §2 (role trigger reads `raw_user_meta_data.role`)
  - Supporting: `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md` §§1–2 (public signup creates a member)
- **Defect:** the public signup endpoint forwards the request's `user_metadata` unchanged to `auth.signUp`. The described trigger reads `raw_user_meta_data.role` on every auth-user insert, and no trusted boundary forces a member role for public signup.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - Public signup assigns the member role at a trusted boundary, independent of submitted metadata, with an allow-list of accepted profile fields.
  - Privileged creation and role assignment are separately authorized.
  - Both the app endpoint and the direct provider-signup path are covered.
  - Trigger hardening is a stated mandatory prerequisite before promotion, not "a ticket".
- **Preserve:** creation-time role transport only through a protected admin channel; table-based roles; console-only superadmin.
- **Likely affected docs / consumers:** AUTH signup and registration flow; DATABASE §2 trigger description; STARTER_KIT §§1–2; negative cases in TESTING/QA (FC-063 pattern).
- **Verification intent:**
  - No recipe forwards caller `user_metadata` wholesale into `signUp`.
  - The trigger description ignores or denies role keys arriving from the public path.
  - The doctrine states a negative case: public signup carrying `role=admin` results in a member.
- **Open decision:** trigger-side vs endpoint-side enforcement (both recommended; Jarvis).
- **Proposed route:** `SYNC`. **Wave 1 BLOCKER.**

**Mapping proposal — ENGINEER-PROPOSED:** At the trusted public-signup boundary, allow only approved profile fields and force the member role independently of submitted metadata. The provider-side creation path must also ignore or reject public role keys, so direct provider signup cannot bypass the endpoint. Privileged role assignment uses a separately authorized protected channel. Trigger hardening and a negative direct-provider test are required before promotion: role=admin submitted publicly must not produce an admin.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `04_REFERENCE_MANUALS/AUTH_MANUAL.md:344` — ## Authentication Flow; MANIFEST ← 4: APP_ARCHITECTURE_MANUAL, DATABASE_MANUAL, STATE_MANAGEMENT_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/AUTH_MANUAL.md:452` — ## API Routes Reference; MANIFEST ← 4: APP_ARCHITECTURE_MANUAL, DATABASE_MANUAL, STATE_MANAGEMENT_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/DATABASE_MANUAL.md:83` — ## 2. Schema Design Patterns; MANIFEST ← 2: API_AND_SERVICES_MANUAL, AUTH_MANUAL.

**Touch proposal:** C-034. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-034` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-035 — Active client-side recipes claim route and identity authority (HOC, post-mount Navbar, persisted auth store)

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/04_auth_data_security_corrections.md:125`):

- **Certified record:** CF-06 · Severity HIGH · Review CONFIRMED · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C04-D08 · Fable FBL-D001 (related; primary in FC-033)
- **Severity divergence (recorded):** Astra HIGH vs Fable BLOCKER (whole multi-surface finding). The certified HIGH stands.
- **Evidence:** Astra C04 §7 C04-D08; Sol C04 §4; Fable §7 FBL-D001, §9 row 6.
- **Defect surfaces (`0a787cb`):**
  - `04_REFERENCE_MANUALS/AUTH_MANUAL.md`: Navbar Law, Common Patterns 2 and 5, §14 HOC Route Protection
  - `04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md`: §1 (Division of Labor; table row "Zustand … route protection"), §8 Auth Store
  - `04_REFERENCE_MANUALS/APP_ARCHITECTURE_MANUAL.md` §4 (`'use client'` AdminLayout)
- **Defect:**
  - The `withRoleCheck` HOC gates layouts client-side on persisted role flags and admits `member` to an admin layout.
  - The later Navbar fetches identity after mount.
  - STATE persists `user.role` and exports `selectIsAdmin`, which implicitly includes superadmin.
  - `isAuthorized` stays true on redirect.
  - All of this contradicts Navbar Law and STATE's own Division of Labor.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - Client-only route-protection recipes are withdrawn; route and identity authority comes from the verified server guard and server identity props.
  - Stores are limited to session-event reactions and interaction state: non-persisted for authority and never authoritative.
  - Every role set is explicit; any display helper is labeled display-only.
- **Preserve:**
  - Navbar Law, STATE Division of Labor and the first-render invariant test.
  - Operation-local authorization, kept independent (FC-036).
- **Likely affected docs / consumers:** AUTH, STATE §1/§8, APP_ARCHITECTURE §4; FC-041 (guard contract), FC-040 (store persistence), FC-001.
- **Verification intent:**
  - No recipe gates a layout client-side on a persisted role.
  - The STATE §1 table no longer assigns route protection to Zustand.
  - `selectIsAdmin` is absent or labeled display-only.
  - APP_ARCHITECTURE §4 uses the server guard.
- **Open decision:** DEC-02 (paired with FC-033).
- **Proposed route:** `SYNC`. Wave 1, paired with FC-033.

**Mapping proposal — ENGINEER-PROPOSED:** Server guards control page access; server-resolved { user, role } props establish first-render identity. Retire client HOC route protection and post-mount identity fetching as authoritative patterns. Zustand handles interaction and session-event reactions, with no persisted authorization authority. Display helpers are display-only and use explicit role sets; they never authorize an operation.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `04_REFERENCE_MANUALS/AUTH_MANUAL.md:654` — ## Client-Side Auth (Zustand Store); MANIFEST ← 4: APP_ARCHITECTURE_MANUAL, DATABASE_MANUAL, STATE_MANAGEMENT_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/AUTH_MANUAL.md:1214` — ## Common Patterns & Recipes; MANIFEST ← 4: APP_ARCHITECTURE_MANUAL, DATABASE_MANUAL, STATE_MANAGEMENT_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/AUTH_MANUAL.md:2070` — ## 14. HOC Route Protection Pattern; MANIFEST ← 4: APP_ARCHITECTURE_MANUAL, DATABASE_MANUAL, STATE_MANAGEMENT_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:25` — ## 1. Philosophy & Strategy; MANIFEST ← 3: APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, ECOMMERCE_AND_PAYMENTS_MANUAL.
- `04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:1241` — ## 8. Common Stores Reference; MANIFEST ← 3: APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, ECOMMERCE_AND_PAYMENTS_MANUAL.
- `04_REFERENCE_MANUALS/APP_ARCHITECTURE_MANUAL.md:408` — ## 4. Layout System; MANIFEST ← 3: ECOMMERCE_AND_PAYMENTS_MANUAL, STATE_MANAGEMENT_MANUAL, THEMING_MANUAL.

**Touch proposal:** C-035. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-035` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-036 — Layout admission is presented as the authorization boundary for privileged server actions

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/04_auth_data_security_corrections.md:157`):

- **Certified record:** CF-06 · Severity BLOCKER · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C04-D02 · Fable none
- **Evidence:** Astra C04 §7 C04-D02; Sol C04 §3 (severity left to disposition); certified closure to BLOCKER on 2026-09-27; Sol C05 §7.A (the repeated "operation-local authorization" seam).
- **Defect surfaces (`0a787cb`):**
  - `04_REFERENCE_MANUALS/AUTH_MANUAL.md`: "User creation — server actions", "Security Best Practices"
  - `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md` §1 (repeats layout-then-admin-client)
- **Defect:** the server-action recipe treats the route-group layout gate as the authorization for `addMember` / `addUser`, which then use a service-role client with no caller or role check of their own.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - Before acquiring or using elevated capability, every privileged server action:
    - authenticates;
    - resolves the current role;
    - checks the allowed operation and target;
    - validates input.
  - Layout guards remain page-access controls only.
  - Negative direct-invocation tests are required.
- **Preserve:** layout guards for page access; isolation of the service-role client.
- **Likely affected docs / consumers:** AUTH server actions and best practices; STARTER_KIT §1; FC-038, FC-057 (API sync GET), FC-050.
- **Verification intent:**
  - The `addMember`/`addUser` recipes contain operation-local checks that run before the admin client.
  - STARTER_KIT §1 no longer presents layout-then-admin-client as sufficient.
  - A direct-invocation negative case is documented.
- **Open decision:** DEC-04. Adopt "every privileged operation authorizes its own invocation" as a Factory-wide invariant (Sol C05 §7.A candidate; Jarvis/Tony).
- **Proposed route:** `SYNC`. **Wave 1 BLOCKER.**

**Mapping proposal — ENGINEER-PROPOSED:** Every privileged operation authorizes its own invocation before acquiring or using elevated capability: authenticate the requester, resolve the current trusted role, authorize the operation and target, and validate input. Layout admission controls page access only. Direct unauthenticated, wrong-role and wrong-target invocations must produce no privileged side effect.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `04_REFERENCE_MANUALS/AUTH_MANUAL.md:787` — ## Server-Side Protection (RBAC); MANIFEST ← 4: APP_ARCHITECTURE_MANUAL, DATABASE_MANUAL, STATE_MANAGEMENT_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/AUTH_MANUAL.md:1512` — ## Security Best Practices; MANIFEST ← 4: APP_ARCHITECTURE_MANUAL, DATABASE_MANUAL, STATE_MANAGEMENT_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md:49` — ## 1. Auth — Already Wired; MANIFEST ← 12: ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, FRONTEND_BUILD_PHASE_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, TESTING_PLAYBOOK, API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, DATABASE_MANUAL, STATE_MANAGEMENT_MANUAL, COMPONENT_REGISTRY, UI_UX_BUILDING_MANUAL.

**Touch proposal:** C-036. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-036` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-037 — Soft-delete RLS policy is an access grant, not a safely composing exclusion

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/04_auth_data_security_corrections.md:286`):

- **Certified record:** CF-07 · Severity HIGH · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C04-D06 · Fable none
- **Evidence:** Astra C04 §7 C04-D06; Sol C04 §3 (HIGH by default; BLOCKER where used to protect private or restricted data). Certified closure: HIGH, 2026-09-27.
- **Defect surfaces (`0a787cb`):** `04_REFERENCE_MANUALS/DATABASE_MANUAL.md` §2 Soft Delete Pattern; §5 own-record and admin policies.
- **Defect:** the soft-delete recipe adds a permissive `USING (is_deleted = FALSE)` SELECT policy without enabling RLS. Composed with owner policies, permissive grants combine with OR, which can widen visibility.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - The recipe enables RLS explicitly and states whether the resource is public or private.
  - The active-record predicate sits inside each intended visibility condition, or in a correctly scoped restrictive policy.
  - Composed behavior is shown for anonymous, other-owner, deleted-own and privileged cases.
- **Preserve:** default-deny ownership, explicit public-access decisions and role-table lookup.
- **Likely affected docs / consumers:** DATABASE §2/§5.
- **Verification intent:**
  - The recipe contains RLS enablement.
  - No standalone permissive active-record SELECT policy is presented as an exclusion.
  - The case table shows the intended result for all four cases.
- **Open decision:** none. Sol's conditional BLOCKER for private data is noted; any re-elevation is Tony's (DEC-22).
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Enable RLS explicitly. Declare whether the resource is public or private. For a private resource, combine ownership or the explicitly authorized role predicate with is_deleted = false inside each visibility policy; do not add a permissive active-row policy that grants access independently. Verify anonymous, other-owner, deleted-own and authorized privileged cases against the composed policy set.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `04_REFERENCE_MANUALS/DATABASE_MANUAL.md:83` — ## 2. Schema Design Patterns; MANIFEST ← 2: API_AND_SERVICES_MANUAL, AUTH_MANUAL.
- `04_REFERENCE_MANUALS/DATABASE_MANUAL.md:390` — ## 5. Row Level Security (RLS); MANIFEST ← 2: API_AND_SERVICES_MANUAL, AUTH_MANUAL.

**Touch proposal:** C-037. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-037` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-038 — Client-capability guidance both underpowers admin calls and overgeneralizes RLS bypass

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/04_auth_data_security_corrections.md:183`):

- **Certified record:** CF-06 · Severity HIGH · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C04-D05 · Fable none
- **Evidence:** Astra C04 §7 C04-D05; Sol C04 §4 ("one consistent capability-selection rule").
- **Defect surfaces (`0a787cb`):**
  - `04_REFERENCE_MANUALS/AUTH_MANUAL.md` §§12–13 (`auth.admin.*` called with the session client)
  - `04_REFERENCE_MANUALS/DATABASE_MANUAL.md` §5 Service Role Bypass ("API routes")
  - Supporting: `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md` §§1–3, `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md` §6
- **Defect:** the session-vs-admin capability boundary is reversed on both sides. Admin operations use the anon-key session client, while DATABASE lists "API routes" in general as a reason to bypass RLS.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):** one capability-selection rule:
  - the session client for caller identity and RLS-bound data;
  - an isolated admin client only after independent authorization of elevated work.
  "API routes" is not a general bypass reason, and service-role substitution is prohibited as a general fix.
- **Preserve:** the handbook's client distinction; the API §6 session-client profile pattern.
- **Likely affected docs / consumers:** AUTH, DATABASE §5, STARTER_KIT, API §6; FC-033, FC-036.
- **Verification intent:**
  - The DATABASE §5 bypass list no longer contains generic "API routes".
  - Every `auth.admin.*` call in recipes uses the admin client after an operation-local check.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Use the session client for identity and RLS-bound data. Acquire an isolated admin client only after independently authorizing the elevated operation. An API route is not itself a reason to bypass RLS. Do not substitute a service-role client as a general fix for denied access.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `04_REFERENCE_MANUALS/DATABASE_MANUAL.md:390` — ## 5. Row Level Security (RLS); MANIFEST ← 2: API_AND_SERVICES_MANUAL, AUTH_MANUAL.
- `04_REFERENCE_MANUALS/AUTH_MANUAL.md:1761` — ## 12. SuperAdmin User Management; MANIFEST ← 4: APP_ARCHITECTURE_MANUAL, DATABASE_MANUAL, STATE_MANAGEMENT_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/AUTH_MANUAL.md:1932` — ## 13. User Mirror Table Pattern; MANIFEST ← 4: APP_ARCHITECTURE_MANUAL, DATABASE_MANUAL, STATE_MANAGEMENT_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.

**Touch proposal:** C-038. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-038` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-039 — Multi-step persistence recipes leave compensation failures unrecoverable

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/04_auth_data_security_corrections.md:306`):

- **Certified record:** CF-07 · Severity HIGH · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C04-D10 · Fable none
- **Evidence:** Astra C04 §7 C04-D10; Sol C04 §4 (distinguish complete success, recoverable failure, partial completion, failed compensation and reconciliation ownership).
- **Defect surfaces (`0a787cb`):**
  - `04_REFERENCE_MANUALS/DATABASE_MANUAL.md` §11 Pseudo-Transaction
  - `04_REFERENCE_MANUALS/AUTH_MANUAL.md` §§12–13 (synchronized create/delete)
- **Defect:** the pseudo-transaction and the synchronized create/delete paths ignore compensation or deletion results, or continue after partial failure. There is no reconciliation state and no recovery owner.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - Invariants inside one database use an atomic operation.
  - Cross-boundary work defines idempotency, checked compensation results, a durable recovery owner and reconciliation.
  - Outcomes distinguish completed, failed and partially completed.
- **Preserve:** the honest "pseudo-transaction" label; explicit relational modeling.
- **Likely affected docs / consumers:** DATABASE §11; AUTH §§12–13 (scope shrinks if DEC-02 retires those recipes under FC-033); FC-020, FC-052 (the same recovery theme).
- **Verification intent:**
  - Recipes inspect compensation results.
  - A partial-completion state is named and its recovery owner stated.
- **Open decision:** none beyond DEC-02's effect on scope.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Use an atomic database operation for invariants inside one database. Across external boundaries, use a stable operation identity, check every forward and compensation result, and persist completed, failed or partially-completed outcomes. Partial failure creates durable reconciliation work with a recovery owner; do not report success after an unchecked compensation or deletion.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `04_REFERENCE_MANUALS/DATABASE_MANUAL.md:974` — ## 11. Data Integrity; MANIFEST ← 2: API_AND_SERVICES_MANUAL, AUTH_MANUAL.
- `04_REFERENCE_MANUALS/AUTH_MANUAL.md:1932` — ## 13. User Mirror Table Pattern; MANIFEST ← 4: APP_ARCHITECTURE_MANUAL, DATABASE_MANUAL, STATE_MANAGEMENT_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.

**Touch proposal:** C-039. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-039` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-040 — Persisted personal data has no enforceable account-transition lifecycle

**Proposed disposition:** BLOCKED. **Authority:** certified correction YES; package outcome remains proposed. CONDITIONAL: DEC-15. 

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/04_auth_data_security_corrections.md:327`):

- **Certified record:** CF-07 · Severity HIGH · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C04-D11 · Fable none as primary
- **Evidence:** Astra C04 §7 C04-D11; Sol C04 §4.
- **Defect surfaces (`0a787cb`):**
  - `04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md`: §4 Persistence, §6 Form/Checkout Store, §8 Auth Store, §9 checklist
  - `04_REFERENCE_MANUALS/AUTH_MANUAL.md`: Security Best Practices (sensitive browser storage), logout flow
- **Defect:** STATE persists email, names, addresses and phone in origin-wide `checkout-storage`. Logout clears only the auth-store flags, and the reset guidance is optional ("when appropriate"), so account B can hydrate account A's personal data.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - Doctrine decides which personal fields may persist, for how long and under which user or guest scope.
  - Sign-out and account transition trigger a coordinated reset and invalidation, including failure cases.
  - AUTH's storage rule and STATE's recipe agree.
  - Raw contact data is not retained by default without justification.
- **Preserve:** selective persistence; transient payment state kept out of persistence.
- **Likely affected docs / consumers:** STATE, AUTH; FC-044 (logout result), FC-047 (reset readiness), FC-068 (checkout store shape).
- **Verification intent:**
  - Documented walkthrough: user A signs out, user B signs in on the same browser, and the recipe yields none of A's data.
  - The reset is bound to logout, not left as an option.
- **Open decision:** DEC-15, the persisted personal-data retention policy (Tony).
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Do not persist raw contact details by default. Any approved personal-data persistence declares permitted fields, retention duration and user or guest scope. Sign-out and account transition reset and invalidate every affected store even when remote logout fails; a new account must not hydrate the previous account’s data. Payment and authorization state remain outside persistence. Storage readiness is separate from business-data reset.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:473` — ## 4. Persistence; MANIFEST ← 3: APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, ECOMMERCE_AND_PAYMENTS_MANUAL.
- `04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:745` — ## 6. Store Templates; MANIFEST ← 3: APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, ECOMMERCE_AND_PAYMENTS_MANUAL.
- `04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:1241` — ## 8. Common Stores Reference; MANIFEST ← 3: APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, ECOMMERCE_AND_PAYMENTS_MANUAL.
- `04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:1472` — ## 9. Best Practices Checklist; MANIFEST ← 3: APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, ECOMMERCE_AND_PAYMENTS_MANUAL.
- `04_REFERENCE_MANUALS/AUTH_MANUAL.md:1512` — ## Security Best Practices; MANIFEST ← 4: APP_ARCHITECTURE_MANUAL, DATABASE_MANUAL, STATE_MANAGEMENT_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.

**Touch proposal:** C-040. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-040` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-041 — The canonical `protectPage` recipe's call and return contract is incompatible with its documented callers

**Proposed disposition:** BLOCKED. **Authority:** certified correction YES; package outcome remains proposed. CONDITIONAL: DEC-09 kit evidence. Cross-boundary component: XB-04.

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/04_auth_data_security_corrections.md:205`):

- **Certified record:** CF-06 · Severity HIGH · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C04-D07 · Fable none
- **Evidence:** Astra C04 §7 C04-D07; Sol C04 §4.
- **Defect surfaces (`0a787cb`):**
  - `04_REFERENCE_MANUALS/AUTH_MANUAL.md`: `protectPage`, Navbar Law
  - `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md` §2 (`getUserRole` signature, `AppRole` module)
- **Defect:** `protectPage` calls `getUserRole(user)` without `await` and returns `user`. The handbook specifies an async, no-argument `getUserRole()`, Navbar Law destructures `{ user, role }`, and the `AppRole` import source differs.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - One async guard signature and return shape, verified against the shipped kit exports, is used by the recipe, Navbar Law and the handbook.
  - The `AppRole` import source is correct.
  - The guard denies by default and uses only the server-resolved role.
- **Preserve:** deny-by-default; never accept a client-provided role.
- **Likely affected docs / consumers:** AUTH, STARTER_KIT §2; FC-035.
- **Verification intent:**
  - Every `protectPage` and `getUserRole` occurrence in live docs shares one signature.
  - Navbar Law's destructuring matches the return shape.
  - The kit verification evidence is cited with its repository and revision.
- **Open decision:** DEC-09, kit disk verification. The kit repository is outside this package (`XB-EXT`; GAP).
- **Proposed route:** `SYNC` (+ `XB-EXT` verification).

**Mapping proposal — ENGINEER-PROPOSED:** The kit guard’s async signature, role lookup, AppRole import and { user, role } return contract must be verified together against the pinned kit revision before a replacement recipe is published. Deny by default and never accept a caller-supplied role. Until that evidence is supplied, do not present mismatched signatures as executable kit guidance.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `04_REFERENCE_MANUALS/AUTH_MANUAL.md:787` — ## Server-Side Protection (RBAC); MANIFEST ← 4: APP_ARCHITECTURE_MANUAL, DATABASE_MANUAL, STATE_MANAGEMENT_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/AUTH_MANUAL.md:880` — ## Server-Resolved Identity for UI (The Navbar Law); MANIFEST ← 4: APP_ARCHITECTURE_MANUAL, DATABASE_MANUAL, STATE_MANAGEMENT_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md:124` — ## 2. RBAC & RLS — Already Wired; MANIFEST ← 12: ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, FRONTEND_BUILD_PHASE_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, TESTING_PLAYBOOK, API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, DATABASE_MANUAL, STATE_MANAGEMENT_MANUAL, COMPONENT_REGISTRY, UI_UX_BUILDING_MANUAL.

**Touch proposal:** C-041. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-041` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-042 — Cookie `httpOnly` guidance contradicts the kit session model

**Proposed disposition:** BLOCKED. **Authority:** certified correction YES; package outcome remains proposed. CONDITIONAL: DEC-09 kit evidence / DEC-06. Cross-boundary component: XB-04.

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/04_auth_data_security_corrections.md:227`):

- **Certified record:** CF-06 · Severity HIGH · Review CONFIRMED · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C04-D04 · Fable FBL-D030 (primary)
- **Severity divergence (recorded):** Astra HIGH vs Fable MEDIUM. The certified HIGH stands.
- **Evidence:** Astra C04 §7 C04-D04; Sol C04 §4 ("should not be solved by selecting the more 'secure sounding' option in isolation"); Fable §7 FBL-D030, §9 row 7, §11 decision 2.
- **Defect surfaces (`0a787cb`):**
  - `04_REFERENCE_MANUALS/AUTH_MANUAL.md`: Cookie Configuration, Security Best Practices DO 6, `src/middleware.ts` example
  - `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md` §1 (`httpOnly: false` deliberate)
  - `04_REFERENCE_MANUALS/APP_ARCHITECTURE_MANUAL.md` §10 (flags `proxy.ts`)
- **Defect:**
  - AUTH requires `httpOnly: true`; the Handbook says `httpOnly: false` is deliberate for client-side session access and must not be tightened.
  - AUTH also shows `src/middleware.ts` where the kit ships `src/proxy.ts`.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - The cookie/session architecture is documented once, in STARTER_KIT §1 per Fable, together with its tradeoff, and AUTH points to it.
  - The flag value follows the verified session design.
  - Login, refresh and logout verification is required.
  - AUTH notes `proxy.ts`.
- **Preserve:** the handbook's live-session-bug warning; AUTH-WALK.
- **Likely affected docs / consumers:** AUTH, STARTER_KIT §1, APP_ARCHITECTURE §10; FC-005 (precedence).
- **Verification intent:**
  - No live doc instructs a cookie flag contrary to the documented session architecture.
  - AUTH references that ruling.
  - Middleware/proxy naming is consistent.
- **Open decision:** DEC-09, the `httpOnly` ruling after kit disk verification (Tony; the kit repository is external).
- **Proposed route:** `SYNC` (+ `XB-EXT` verification).

**Mapping proposal — ENGINEER-PROPOSED:** Cookie flags and the session entrypoint follow the verified kit session architecture. STARTER_KIT_HANDBOOK §1 owns that architecture and its tradeoff; AUTH_MANUAL links to it rather than prescribing an incompatible flag. Verify login, refresh and logout before changing cookie behavior. Do not tighten httpOnly in isolation or substitute middleware.ts for the shipped proxy.ts without pinned kit evidence.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `04_REFERENCE_MANUALS/AUTH_MANUAL.md:159` — ## Supabase Client Setup; MANIFEST ← 4: APP_ARCHITECTURE_MANUAL, DATABASE_MANUAL, STATE_MANAGEMENT_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/AUTH_MANUAL.md:992` — ## Session Management & Middleware; MANIFEST ← 4: APP_ARCHITECTURE_MANUAL, DATABASE_MANUAL, STATE_MANAGEMENT_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/AUTH_MANUAL.md:1512` — ## Security Best Practices; MANIFEST ← 4: APP_ARCHITECTURE_MANUAL, DATABASE_MANUAL, STATE_MANAGEMENT_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md:49` — ## 1. Auth — Already Wired; MANIFEST ← 12: ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, FRONTEND_BUILD_PHASE_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, TESTING_PLAYBOOK, API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, DATABASE_MANUAL, STATE_MANAGEMENT_MANUAL, COMPONENT_REGISTRY, UI_UX_BUILDING_MANUAL.
- `04_REFERENCE_MANUALS/APP_ARCHITECTURE_MANUAL.md:1141` — ## 10. Security Architecture; MANIFEST ← 3: ECOMMERCE_AND_PAYMENTS_MANUAL, STATE_MANAGEMENT_MANUAL, THEMING_MANUAL.

**Touch proposal:** C-042. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-042` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-043 — Email confirmation route accepts an unbounded external redirect destination

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/04_auth_data_security_corrections.md:254`):

- **Certified record:** CF-06 · Severity HIGH · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C04-D09 · Fable none
- **Evidence:** Astra C04 §7 C04-D09; Sol C04 §4 (redirect/phishing risk only; no claim of credential disclosure).
- **Defect surfaces (`0a787cb`):** `04_REFERENCE_MANUALS/AUTH_MANUAL.md`, GET `/api/auth/confirm`.
- **Defect:** the route redirects to `new URL(next, request.url)` with `next` taken from the query, with no same-origin or allowed-path check. Absolute and network-path URLs therefore leave the application.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - The confirmation redirect is restricted to approved local destinations; the resolved origin and path are normalized and verified, with a safe fallback.
  - The contract covers absolute, network-path, malformed and valid local cases.
- **Preserve:** the confirmation flow itself.
- **Likely affected docs / consumers:** AUTH confirm route; any recipe reusing a `next` parameter.
- **Verification intent:** the documented cases show `https://outside.example` and `//outside.example/path` rejected, a valid local path accepted, and a stated fallback.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Resolve next against the request origin inside a guarded parse. Accept only an approved local pathname whose resolved origin equals the application origin; reject external absolute URLs, network-path URLs and malformed values. Use the fixed approved local fallback otherwise. Verify valid local, external, network-path and malformed cases.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `04_REFERENCE_MANUALS/AUTH_MANUAL.md:452` — ## API Routes Reference; MANIFEST ← 4: APP_ARCHITECTURE_MANUAL, DATABASE_MANUAL, STATE_MANAGEMENT_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.

**Touch proposal:** C-043. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-043` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-044 — Logout reports success without checking the sign-out result

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/04_auth_data_security_corrections.md:270`):

- **Certified record:** CF-06 · Severity MEDIUM · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C04-D16 · Fable none
- **Evidence:** Astra C04 §7 C04-D16; Sol C04 §5.
- **Defect surfaces (`0a787cb`):** `04_REFERENCE_MANUALS/AUTH_MANUAL.md`, POST `/api/auth/logout` and Security Best Practices.
- **Defect:** the endpoint discards the `signOut()` result and always returns 200 "Logged out successfully", contrary to the manual's own "don't ignore auth errors" rule.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):** the logout recipe inspects and classifies the sign-out result, defines local cleanup and revocation expectations, returns an accurate outcome and provides retry or recovery.
- **Preserve:** the happy-path logout bounce verification.
- **Likely affected docs / consumers:** AUTH logout; FC-040 (store cleanup on logout).
- **Verification intent:** the recipe branches on the returned error, does not return success on failure, and the doctrine includes a failed-sign-out check.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Inspect the signOut result before reporting remote logout success. Clear local personal and authority state regardless of that result, report remote revocation as failed or unknown when appropriate, and offer the bounded retry or recovery path. Do not tell the user that revocation succeeded merely because local state was cleared.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `04_REFERENCE_MANUALS/AUTH_MANUAL.md:452` — ## API Routes Reference; MANIFEST ← 4: APP_ARCHITECTURE_MANUAL, DATABASE_MANUAL, STATE_MANAGEMENT_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.

**Touch proposal:** C-044. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-044` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-045 — Timestamp-only cursor pagination silently skips tied records

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/04_auth_data_security_corrections.md:349`):

- **Certified record:** CF-07 · Severity MEDIUM · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C04-D17 · Fable none
- **Evidence:** Astra C04 §7 C04-D17; Sol C04 §5.
- **Defect surfaces (`0a787cb`):** `04_REFERENCE_MANUALS/DATABASE_MANUAL.md` §12 Pagination Patterns.
- **Defect:** the cursor orders and filters on the non-unique `created_at` alone (`.lt`, limit 20), so rows tied at a page boundary are skipped.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):** the cursor uses a stable unique tie-breaker in both the order and the cursor predicate, and keeps the same filter and authorization scope across pages.
- **Preserve:** the pagination pattern's purpose.
- **Likely affected docs / consumers:** DATABASE §12; list and batch consumers.
- **Verification intent:** the documented case of 21 rows sharing one timestamp traverses every row exactly once.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Order cursor pagination by created_at and a unique id, both descending. The next-page predicate is created_at < cursor.created_at OR (created_at = cursor.created_at AND id < cursor.id). Encode both values in the cursor, keep the same filters and authorization scope, and test ties across the page boundary.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `04_REFERENCE_MANUALS/DATABASE_MANUAL.md:1090` — ## 12. Performance Optimization; MANIFEST ← 2: API_AND_SERVICES_MANUAL, AUTH_MANUAL.

**Touch proposal:** C-045. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-045` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-046 — Alternative hydration hook changes the hook invocation count

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/04_auth_data_security_corrections.md:363`):

- **Certified record:** CF-07 · Severity MEDIUM · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C04-D13 · Fable none
- **Evidence:** Astra C04 §7 C04-D13; Sol C04 §5.
- **Defect surfaces (`0a787cb`):** `04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md` §5, "Alternative: Suspense-Style Loading".
- **Defect:** `useHydratedStore` returns early while unhydrated, then calls the store hook a second time. Its comment claims it throws a promise, but the code returns null.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):** both subscriptions are unconditional and only the returned data is gated, or a real supported suspension strategy is documented. The explanation matches the behavior.
- **Preserve:** the hydration-gating intent.
- **Likely affected docs / consumers:** STATE §5; FC-047.
- **Verification intent:** the recipe's hook call sequence is identical before and after hydration, and the comments match the code.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Subscribe to both hydration state and selected store data on every render, in the same hook order. Gate only the returned data on hydration readiness. This is readiness gating, not Suspense: it does not claim to throw a promise.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:620` — ## 5. Hydration & SSR; MANIFEST ← 3: APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, ECOMMERCE_AND_PAYMENTS_MANUAL.

**Touch proposal:** C-046. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-046` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-047 — Persistence readiness can become permanently false after a reset or storage failure

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/04_auth_data_security_corrections.md:377`):

- **Certified record:** CF-07 · Severity MEDIUM · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C04-D12 · Fable none
- **Evidence:** Astra C04 §7 C04-D12; Sol C04 §5.
- **Defect surfaces (`0a787cb`):** `04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md` §5; §6 Persisted Store and Form/Checkout Store.
- **Defect:** `reset: () => set(initialState)` resets `hasHydrated` to false, and only rehydration sets it true again. The error callback never reaches a terminal state, so gated UI can hang.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):** storage readiness is separated from business data, a normal reset preserves readiness, and failed hydration has an explicit terminal error and recovery path.
- **Preserve:** the readiness gate itself.
- **Likely affected docs / consumers:** STATE §5/§6; FC-040 (reset on logout).
- **Verification intent:** the documented checks cover reset-after-hydration and unavailable or invalid storage, and neither leaves the gate unresolved.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Keep hydration readiness outside the resettable business state. A normal reset preserves readiness. Hydration finishes in ready or error; an error exposes bounded recovery and never leaves an indefinite loading state. Verify reset after hydration, invalid stored data and unavailable storage.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:620` — ## 5. Hydration & SSR; MANIFEST ← 3: APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, ECOMMERCE_AND_PAYMENTS_MANUAL.
- `04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:745` — ## 6. Store Templates; MANIFEST ← 3: APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, ECOMMERCE_AND_PAYMENTS_MANUAL.

**Touch proposal:** C-047. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-047` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-048 — A nonempty client store permanently overrides new server data

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/04_auth_data_security_corrections.md:391`):

- **Certified record:** CF-07 · Severity MEDIUM · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C04-D15 · Fable none
- **Evidence:** Astra C04 §7 C04-D15; Sol C04 §5.
- **Defect surfaces (`0a787cb`):** `04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md` §1 (server-state ownership table), §7 Store + Server Components, §9 freshness checklist.
- **Defect:** `ProductList` initializes the store only when it is empty and renders from the store, so later server props, including an empty result, are ignored.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):** authoritative server props render directly where possible. Where a client working copy is needed, its scope, version, refresh and reconciliation with local edits are defined, including the transition to an empty dataset.
- **Preserve:** the manual's rule that product lists are server state.
- **Likely affected docs / consumers:** STATE §1/§7/§9.
- **Verification intent:** the documented refresh case shows removed records disappearing and an empty result rendering as empty.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Render authoritative server props directly for server-owned collections. If a client working copy is required, define its scope, version and reconciliation policy for incoming server revisions and local edits. A refreshed empty server result clears the displayed server collection; a nonempty client store does not override it permanently.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:1084` — ## 7. Integration Patterns; MANIFEST ← 3: APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, ECOMMERCE_AND_PAYMENTS_MANUAL.
- `04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:1472` — ## 9. Best Practices Checklist; MANIFEST ← 3: APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, ECOMMERCE_AND_PAYMENTS_MANUAL.

**Touch proposal:** C-048. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-048` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-049 — Composite-item update mutates the previous state snapshot

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/04_auth_data_security_corrections.md:405`):

- **Certified record:** CF-07 · Severity MEDIUM · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C04-D14 · Fable none
- **Evidence:** Astra C04 §7 C04-D14; Sol C04 §5.
- **Defect surfaces (`0a787cb`):** `04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md` §3 Composite Key Pattern; Immutable Update Pattern.
- **Defect:** the example shallow-copies the array and then mutates `newItems[i].quantity` in place, contradicting the manual's own immutable-update rule.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):** the example copies the changed item as well as the container, using the manual's existing map-and-spread pattern, or is an explicit Immer-backed variant.
- **Preserve:** composite identity; the immutable-update rule.
- **Likely affected docs / consumers:** STATE §3.
- **Verification intent:** the recipe leaves the prior state's item object unchanged.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Update the changed item and its container immutably: items.map(item => matchesCompositeKey(item, incoming) ? { ...item, quantity: item.quantity + incoming.quantity } : item). The composite-key predicate remains unchanged. Verify the previous item object and previous array remain unchanged.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:245` — ## 3. Core Patterns; MANIFEST ← 3: APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, ECOMMERCE_AND_PAYMENTS_MANUAL.

**Touch proposal:** C-049. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-049` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-050 — Public order-status mutation accepts the caller's assertion that payment succeeded

**Proposed disposition:** BLOCKED. **Authority:** certified correction YES; package outcome remains proposed. CONDITIONAL: DEC-05 guest capability (required authorization still applies). 

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/05_api_commerce_corrections.md:43`):

- **Certified record:** CF-08 · Severity BLOCKER · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C05-D03 · Fable none
- **Evidence:** Astra C05 §7 C05-D03; Sol C05 §3 ("Reusable Factory payment doctrine must never teach that a browser-selected payment state can directly cause authoritative paid-order state").
- **Defect surfaces (`0a787cb`):** `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md`, §3 "Handling Payment Results", §5 "Order Status Updates" and its service implementation, §11 "Order Security".
- **Defect:** the browser posts `orderId`, `status: 'processing'` and any `paymentIntentId`. The route sets `set_paid = true` and forwards the change through server WooCommerce credentials with:
  - no authentication
  - no ownership check
  - no Stripe retrieval
  - no amount/currency comparison
  - no transition check
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - Payment-derived order status changes come only from verified server-side payment evidence bound to the stored order and payment attempt. The browser never chooses payment truth.
  - Every non-webhook order mutation authenticates and authorizes, including an explicit guest-order capability where guest checkout is supported, and validates legal transitions.
- **Preserve:** server-side WooCommerce credentials. Sol: holding server credentials is not authorization to use them on a caller's behalf.
- **Likely affected docs / consumers:** ECOM §3/§5/§11; FC-051 (quote binding), FC-054 (transitions), FC-063 (forged-status negative case), FC-036 (operation-local authorization).
- **Verification intent:**
  - No live recipe sets a paid or processing state from a client-supplied status or `paymentIntentId`.
  - The client success path only displays or polls.
  - The negative matrix (FC-063) includes a forged status call that produces no state change.
- **Open decision:** DEC-05, the guest-order capability model (Jarvis). DEC-04, the operation-local authorization invariant.
- **Proposed route:** `SYNC`. **Wave 1 BLOCKER.**

**Mapping proposal — ENGINEER-PROPOSED:** The browser may display or poll payment status; it may not choose paid or processing state. A payment-derived transition requires verified server-side evidence bound to the stored order and payment attempt, including amount and currency. Non-webhook mutations authenticate and authorize the operation and target, including an explicitly approved guest capability where supported, then validate the state transition.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:181` — ## 3. PaymentIntent Flow; MANIFEST ← 3: API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:661` — ## 5. Order Management; MANIFEST ← 3: API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:1722` — ## 11. Security Checklist; MANIFEST ← 3: API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.

**Touch proposal:** C-050. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-050` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-051 — PaymentIntent amount is computed from client-supplied prices, shipping and discount despite "never trust client"

**Proposed disposition:** BLOCKED. **Authority:** certified correction YES; package outcome remains proposed. CONDITIONAL: DEC-05 design only (certified behavior remains required). 

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/05_api_commerce_corrections.md:67`):

- **Certified record:** CF-08 · Severity BLOCKER · Review CONFIRMED · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C05-D04 · Fable FBL-D019 (primary)
- **Evidence:** Astra C05 §7 C05-D04; Sol C05 §3 ("Server-side arithmetic does NOT transform untrusted values into authoritative values"); Fable §7 FBL-D019, §9 rows 8–9, §2 row 2.
- **Defect surfaces (`0a787cb`):**
  - `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md`: §1 principles, §3 PaymentIntent creation, §5 order creation, §6 totals helper, §9 success handler, §11 checklist
  - `03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md`: §1.8, §4.3 (generic error message)
- **Defect:**
  - Under the comment "Recalculate total on server – never trust client", the route feeds `body.items[].price`, `body.shipping.cost` and `body.coupon.discount` into `calculateOrderTotal`.
  - The order ID is caller-set in metadata, and the WooCommerce total is ignored.
  - The success webhook marks the metadata-selected order paid without an amount/currency binding.
  - The handler returns Stripe `error.message` to the client, contrary to TESTING §4.3.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - **Required: what the certified finding needs (server-authoritative pricing and payment/order binding).**
    - The server derives the charge amount from authoritative sources:
      - catalog prices for validated products, variations and quantities;
      - a server-validated shipping selection;
      - server-validated coupon eligibility;
      - the applicable tax policy.
    - It never uses client-supplied prices, shipping cost or discount amounts.
    - The payment is bound to an authorized order. The order is not selected by caller-set metadata alone, and amount, currency and order association are verified before any paid transition.
    - Client totals are display-only.
    - Errors return a generic client message, with a redacted server-side log (FC-021).
  - **Architectural recommendation: awaiting approval (DEC-05). Not a certified-finding requirement.**
    - Implement the requirement through one persisted, versioned server quote on the authorized order.
    - The PaymentIntent is created or reused from that quote, and its ID is bound to it.
    - Other designs that satisfy every "Required" bullet stay open for Jarvis/Tony.
- **Preserve:** the §1 "never trust client" principle and the §11 checklist, which are already correct; correct Stripe usage.
- **Likely affected docs / consumers:** ECOM; TESTING §4.3; FC-060 (checkout contract), FC-067 (coupon), FC-021 (log redaction), FC-063 (tampered-totals negative case).
- **Verification intent (tests the required behavior; independent of the quote design):**
  - The PaymentIntent recipe reads no price, shipping cost or discount amount from the request body; only identifiers and selections.
  - The server-side pricing computation it relies on is defined in the manual, not an undocumented import.
  - The success path verifies amount, currency and order association before marking an order paid, and does not trust caller metadata to select the order.
  - The error path returns a generic message.
  - The negative matrix includes tampered totals (FC-063).
  - Additional checks if the recommendation is approved: the quote is persisted and versioned, and the PaymentIntent ID is bound to it.
- **Open decision:** DEC-05 (Jarvis → Tony): the server pricing sources, the tax policy, and whether to adopt the persisted/versioned quote recommendation. **Containment note:** marking the current sample unsafe contains the risk but does not close FC-051. Closure needs the "Required" behavior landed and verified.
- **Proposed route:** `SYNC`. **Wave 1 BLOCKER.**

**Mapping proposal — ENGINEER-PROPOSED:** Accept product/variation identifiers, quantities, shipping selection and coupon code, never caller prices, shipping costs or discount amounts. Validate quantities and product eligibility; load authoritative catalog prices; validate the shipping selection and coupon eligibility; apply the declared tax policy; calculate currency-safe totals on the server. Bind the payment to the authorized order and verify payment identity, amount, currency and order association before marking paid. Client totals are display-only. Return generic failures and redact logs. A persisted versioned quote is a proposed design, not a certified requirement.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:181` — ## 3. PaymentIntent Flow; MANIFEST ← 3: API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:661` — ## 5. Order Management; MANIFEST ← 3: API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:877` — ## 6. Cart Logic; MANIFEST ← 3: API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:1511` — ## 9. Webhook Handling; MANIFEST ← 3: API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:1722` — ## 11. Security Checklist; MANIFEST ← 3: API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.

**Touch proposal:** C-051. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-051` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-052 — Commerce and subscription webhook acknowledgment conceals failed business persistence

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/05_api_commerce_corrections.md:149`):

- **Certified record:** CF-09 · Severity HIGH · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C05-D05 · Fable none
- **Evidence:** Astra C05 §7 C05-D05; Sol C05 §4 (HIGH minimum; a BLOCKER candidate depending on architecture). Certified closure: HIGH, 2026-09-27.
- **Defect surfaces (`0a787cb`):**
  - `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md` §9
  - `04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md` §6, §14
- **Defect:**
  - The ECOM §9 handlers catch WooCommerce update errors and still return `{ received: true }`.
  - The STRIPE §6 UPSERT result is never inspected, and the guidance says "Always return 200".
  - Reconciliation is only a roadmap item.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - Supported events are acknowledged only after checked durable completion or checked durable enqueue (durable acceptance).
  - **Failure before durable acceptance** (the required write or the enqueue fails or is unconfirmed) returns a retryable failure, not `{ received: true }`.
  - **Failure after durable acceptance** (a worker fails on an already-accepted event) does not retroactively invalidate the lawful acknowledgment. It is handled by durable retry/recovery: bounded retries, failed-job visibility, alerting, a replay/reconciliation procedure and a recovery owner.
  - Unknown event types are distinguished from failed known events.
  - Missing order or user mappings become actionable records instead of silent returns.
- **Preserve:** signature rejection; ignoring unsupported events.
- **Likely affected docs / consumers:** ECOM §9, STRIPE §6/§14; **FC-020** (the same mechanism in TESTING G5, brief 03), FC-059, FC-062, FC-054.
- **Verification intent:**
  - No unconditional "Always return 200" remains.
  - The handlers inspect write and enqueue results before acknowledging.
  - A documented pre-acceptance failure yields a retryable non-success response.
  - A documented post-acceptance worker failure leaves the acknowledgment standing and produces a durable retry or failed-job record with a recovery path.
  - Reconciliation is a defined procedure, not a roadmap note.
  - TESTING G5 and these manuals state the same two-phase contract.
- **Open decision:** DEC-03, the Factory acknowledgment contract (shared with FC-020). Sol's conditional BLOCKER is noted under DEC-22.
- **Proposed route:** `SYNC`. Wave 1 companion to BLOCKER FC-020.

**Mapping proposal — ENGINEER-PROPOSED:** For supported events, check business persistence or durable enqueue before acknowledging. Pre-acceptance failure returns a retryable failure. After durable acceptance, worker failures enter bounded durable retries and visible failed-work reconciliation with an alert and recovery owner. Unsupported events are explicitly distinguished from failed supported events. Missing order/user mappings create actionable recovery records, not silent success.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:1511` — ## 9. Webhook Handling; MANIFEST ← 3: API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:391` — ## 6. The Webhook Handler; MANIFEST ← 1: ECOMMERCE_AND_PAYMENTS_MANUAL.
- `04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:840` — ## 14. Phase 3 Roadmap; MANIFEST ← 1: ECOMMERCE_AND_PAYMENTS_MANUAL.

**Touch proposal:** C-052. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-052` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-053 — Checkout creation lacks the retry and concurrency identity its invariants require

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/05_api_commerce_corrections.md:179`):

- **Certified record:** CF-09 · Severity HIGH · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C05-D06 · Fable none
- **Evidence:** Astra C05 §7 C05-D06; Sol C05 §4.
- **Defect surfaces (`0a787cb`):**
  - `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md` §§1, 3–5, 11
  - `04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md` §§5, 7
- **Defect:**
  - Every initialization creates a new order and a new PaymentIntent, with no idempotency key.
  - The subscription flow creates Customers and Sessions without a stable identity and diverts only when the status is exactly `active`.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - A stable, authorized checkout attempt persists across retries, and concurrent attempts are coordinated atomically.
  - External objects are reused or retrieved rather than recreated.
  - The idempotency-key scope and unknown-outcome recovery are specified.
  - Customer identity is persisted independently of activation.
  - Every existing subscription state is handled, not only `active`.
- **Preserve:** the one-order/customer/subscription intentions the manuals already state.
- **Likely affected docs / consumers:** ECOM, STRIPE; FC-055, FC-056.
- **Verification intent:**
  - The recipes show idempotency-key usage and an attempt lookup.
  - The existing-subscription guard covers `past_due` and other nonterminal states.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Persist one authorized checkout-attempt identity across retries and claim it atomically against concurrent requests. Scope provider idempotency keys to that attempt and operation, reuse or retrieve existing external objects after an unknown outcome, and reconcile before creating a replacement. Persist customer identity independently of paid activation. Handle every documented subscription state, not only active.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:181` — ## 3. PaymentIntent Flow; MANIFEST ← 3: API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:412` — ## 4. Checkout Implementation; MANIFEST ← 3: API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:661` — ## 5. Order Management; MANIFEST ← 3: API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:1722` — ## 11. Security Checklist; MANIFEST ← 3: API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:319` — ## 5. The Checkout Flow; MANIFEST ← 1: ECOMMERCE_AND_PAYMENTS_MANUAL.
- `04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:507` — ## 7. The Tier Upgrade Pattern; MANIFEST ← 1: ECOMMERCE_AND_PAYMENTS_MANUAL.

**Touch proposal:** C-053. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-053` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-054 — Event handlers can regress newer commerce or subscription state

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/05_api_commerce_corrections.md:204`):

- **Certified record:** CF-09 · Severity HIGH · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C05-D07 · Fable none
- **Evidence:** Astra C05 §7 C05-D07; Sol C05 §4.
- **Defect surfaces (`0a787cb`):**
  - `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md` §9
  - `04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md` §6, §14
- **Defect:** handlers apply each event's snapshot directly, with no transition, freshness or ordering rule. Out-of-order delivery can end a paid order at `failed` or restore a cancelled subscription.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - State converges per aggregate, through authoritative retrieval or explicit freshness and transition rules.
  - Stale transitions are rejected.
  - Zero-row writes are checked and missing mappings recovered.
  - Mirror repair is specified.
- **Preserve:** the separation from signature verification and duplicate-delivery handling.
- **Likely affected docs / consumers:** ECOM §9, STRIPE §6/§14; FC-052, FC-056.
- **Verification intent:** the documented scenarios converge correctly: success-then-failure delivered in reverse order ends paid, and a late update after deletion does not restore access.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Converge each order or subscription aggregate using authoritative provider retrieval or explicit freshness and legal-transition rules. Reject stale transitions; check zero-row updates and repair missing mappings. A late event for an old subscription may not overwrite its replacement. Define reconciliation of the local mirror independently of inbound deduplication.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:1511` — ## 9. Webhook Handling; MANIFEST ← 3: API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:391` — ## 6. The Webhook Handler; MANIFEST ← 1: ECOMMERCE_AND_PAYMENTS_MANUAL.

**Touch proposal:** C-054. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-054` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-055 — Subscription bootstrap and resubscribe writes conflict with the prescribed schema

**Proposed disposition:** BLOCKED. **Authority:** certified correction YES; package outcome remains proposed. CONDITIONAL: K-SUBSCRIPTION-MODEL. 

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/05_api_commerce_corrections.md:224`):

- **Certified record:** CF-09 · Severity HIGH · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C05-D10 · Fable none
- **Evidence:** Astra C05 §7 C05-D10; Sol C05 §4.
- **Defect surfaces (`0a787cb`):** `04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md` §3 (schema), §5, §6.
- **Defect:**
  - `tier` is required with no default, `status` defaults to `active`, and `user_id` is unique.
  - Checkout must save the customer ID before payment, but no unpaid bootstrap state is defined.
  - The webhook UPSERT conflicts only on `stripe_subscription_id`, so the first-subscribe and resubscribe paths collide.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - The customer-link storage model and an explicit unpaid bootstrap state are decided, with narrowly authorized checkout writes.
  - Webhook persistence reconciles the user and the current subscription atomically and is protected against late events for replaced subscriptions.
  - Four lifecycle examples satisfy every constraint: first subscribe, abandoned checkout, cancellation, resubscribe.
- **Preserve:** the restricted write boundary and the money-authority separation.
- **Likely affected docs / consumers:** STRIPE §3/§5/§6; FC-053.
- **Verification intent:** the schema plus the documented write paths satisfy NOT NULL, the defaults and the unique constraints in all four lifecycle examples.
- **Open decision:** the customer-link storage model (Jarvis).
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Store provider customer identity independently of paid entitlement. Represent an unpaid checkout bootstrap explicitly and permit only narrowly authorized server writes. Reconcile user/current-subscription identity atomically; reject stale updates for replaced subscriptions. Before publishing a recipe, verify first subscribe, abandoned checkout, cancellation and resubscribe against every schema constraint.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:173` — ## 3. Supabase Schema Recipe; MANIFEST ← 1: ECOMMERCE_AND_PAYMENTS_MANUAL.
- `04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:319` — ## 5. The Checkout Flow; MANIFEST ← 1: ECOMMERCE_AND_PAYMENTS_MANUAL.
- `04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:391` — ## 6. The Webhook Handler; MANIFEST ← 1: ECOMMERCE_AND_PAYMENTS_MANUAL.

**Touch proposal:** C-055. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-055` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-056 — Webhook deduplication neither excludes concurrent execution nor identifies events reliably

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/05_api_commerce_corrections.md:244`):

- **Certified record:** CF-09 · Severity HIGH · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C05-D01 · Fable none
- **Evidence:** Astra C05 §7 C05-D01; Sol C05 §4.
- **Defect surfaces (`0a787cb`):** `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md` §11, "Idempotency for Webhooks".
- **Defect:** the handler reads `processed_webhooks`, does the work, then inserts a marker without checking the result, keyed on `webhookId || order._id`. This is non-atomic, and the key identifies an aggregate rather than an event.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - A stable provider event identity is used.
  - Claims are atomic, with in-progress, completed and retryable states, and persistence results are checked.
  - Effects are idempotent or coordinated transactionally.
  - Recovery for abandoned claims and partial external success is defined.
- **Preserve:** the intent of idempotent webhook handling.
- **Likely affected docs / consumers:** API §11; FC-053, FC-054.
- **Verification intent:** the recipe's claim is atomic and checked, two concurrent deliveries cannot both execute, and a later event for the same order is not suppressed.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Use the provider’s stable event ID, never a random fallback. Atomically claim each event with in-progress, completed and retryable states; inspect persistence results. Make effects idempotent or transactional. A bounded lease/recovery process reclaims abandoned work and reconciles partial external success without duplicating completed effects.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:1564` — ## 11. Webhook Integration Patterns; MANIFEST ← 5: APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, DATABASE_MANUAL, ECOMMERCE_AND_PAYMENTS_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.

**Touch proposal:** C-056. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-056` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-057 — Manual sync exposes a privileged mutation as an unprotected GET

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/05_api_commerce_corrections.md:318`):

- **Certified record:** CF-10 · Severity HIGH · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C05-D08 · Fable none
- **Evidence:** Astra C05 §7 C05-D08; Sol C05 §4 and §7.A.
- **Defect surfaces (`0a787cb`):**
  - `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md` §13
  - `04_REFERENCE_MANUALS/AUTH_MANUAL.md`: Security Best Practices
- **Defect:** `/api/sync` exports `GET()` with no identity or role check and upserts database records, contrary to AUTH's every-request validation rule.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - A non-safe-method mutation endpoint, authenticated and role-authorized, with explicit tenant scope.
  - CSRF protection where applicable, plus concurrency and rate controls for bulk jobs.
  - Job acceptance and progress access follow the same authorization boundary.
- **Preserve:** the manual-sync capability itself.
- **Likely affected docs / consumers:** API §13; FC-036 (DEC-04 invariant).
- **Verification intent:** the recipe uses a non-GET method with operation-local authorization, and an unauthenticated invocation is rejected in the documented checks.
- **Open decision:** DEC-04.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Manual synchronization is an authenticated, role-authorized POST operation with explicit tenant scope. Apply the context’s CSRF protection, rate and concurrency controls. Job acceptance, progress reads and retries enforce the same authorization boundary. GET is read-only and cannot initiate synchronization.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:1831` — ## 13. Data Synchronization Patterns; MANIFEST ← 5: APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, DATABASE_MANUAL, ECOMMERCE_AND_PAYMENTS_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.

**Touch proposal:** C-057. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-057` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-058 — Generic webhook verification signs reconstructed JSON and chains supposedly alternative schemes

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/05_api_commerce_corrections.md:337`):

- **Certified record:** CF-10 · Severity HIGH · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C05-D09 · Fable none
- **Evidence:** Astra C05 §7 C05-D09; Sol C05 §4.
- **Defect surfaces (`0a787cb`):**
  - `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md` §11 (validator)
  - `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md` §9 (correct raw-body Stripe pattern)
  - `04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md` §6 (correct raw-body Stripe pattern)
- **Defect:** the API §11 validator hashes `JSON.stringify(payload)` after parsing rather than the raw body. It also runs "Option 1" (shared-secret header) and "Option 2" (HMAC) in sequence, though they are meant as alternatives.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - Each provider's signature, header and encoding contract is explicit.
  - The raw body is captured once and authenticated before parsing.
  - One documented scheme is selected, using the provider's verifier or a specified HMAC comparison.
  - Verification cases include whitespace-bearing signed payloads and absent or invalid headers.
- **Preserve:** the Stripe raw-body recipes.
- **Likely affected docs / consumers:** API §11.
- **Verification intent:** no recipe signs re-serialized JSON, the options are presented as alternatives, and the documented verification cases exist.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Capture the raw request body once. Select exactly one provider-specific signature scheme with its documented header and encoding, verify before parsing, and reject missing or invalid headers. Do not sign reconstructed JSON or chain alternative schemes as cumulative requirements. Test signed whitespace-bearing bodies and malformed or absent signatures.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:1564` — ## 11. Webhook Integration Patterns; MANIFEST ← 5: APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, DATABASE_MANUAL, ECOMMERCE_AND_PAYMENTS_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.

**Touch proposal:** C-058. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-058` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-059 — Required webhook follow-up has no durable acceptance or recovery boundary

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/05_api_commerce_corrections.md:262`):

- **Certified record:** CF-09 · Severity HIGH · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C05-D02 · Fable none
- **Certified severity note:** "HIGH (Sol: HIGH when the follow-up is required business work)".
- **Evidence:** Astra C05 §7 C05-D02; Sol C05 §4.
- **Defect surfaces (`0a787cb`):** `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md` §11, endpoint and "Async Follow-Up Pattern (Fire-and-Forget)"; final cheat sheet.
- **Defect:** the fire-and-forget `triggerAsyncFollowUp` is not awaited. The handler returns success, failures are only logged, and there is no durable job or retry.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - Optional telemetry is distinguished from required work.
  - Required follow-up is durably enqueued before acknowledgment, or completed in a retry-safe handler.
    - **If the enqueue fails or is unconfirmed (before durable acceptance),** the webhook returns a retryable failure instead of acknowledging.
    - **If the follow-up worker fails after the work was durably enqueued,** the webhook acknowledgment stays lawful and is not retroactively invalidated. The failure goes to durable retry/recovery.
  - Retry limits, failed-job visibility and recovery ownership are specified, and HTTP failure responses from the follow-up target are checked.
- **Preserve:** fire-and-forget for genuinely optional telemetry.
- **Likely affected docs / consumers:** API §11 and its cheat sheet; FC-020, FC-052 (DEC-03).
- **Verification intent:**
  - No required follow-up is shown fire-and-forget.
  - A failed enqueue produces a non-success webhook response.
  - A failed follow-up after durable enqueue produces a durable, visible retry or failed-job record with a recovery owner, while the original acknowledgment stands.
- **Open decision:** DEC-03.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Distinguish optional telemetry from required follow-up. Complete required work retry-safely or durably enqueue it before acknowledgment. Failed or unconfirmed enqueue returns retryable failure. A later worker failure uses bounded durable retry, visible failed-work state and a named recovery owner. Inspect non-success HTTP responses from follow-up targets; a resolved fetch is not proof of success.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:1564` — ## 11. Webhook Integration Patterns; MANIFEST ← 5: APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, DATABASE_MANUAL, ECOMMERCE_AND_PAYMENTS_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.

**Touch proposal:** C-059. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-059` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-060 — The displayed checkout caller cannot satisfy its order endpoint contract

**Proposed disposition:** BLOCKED. **Authority:** certified correction YES; package outcome remains proposed. CONDITIONAL: DEC-05. 

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/05_api_commerce_corrections.md:107`):

- **Certified record:** CF-08 · Severity HIGH · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C05-D11 · Fable none as primary
- **Evidence:** Astra C05 §7 C05-D11; Sol C05 §4.
- **Defect surfaces (`0a787cb`):** `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md`, §4 initialization and billing schema, §5 `PlaceOrderRequest` and route, §3 pricing import, §6 helper.
- **Defect:**
  - `initializePayment` omits the required `shippingMethod`, which the route dereferences.
  - Email is sent as `customerEmail`, but the route reads `billing.email`.
  - Coupon state reaches neither order creation nor intent creation.
  - `calculateOrderTotal` does not match the exported `calculateCartTotals`.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - One validated request/response contract and one server quote interface (FC-051).
  - Caller, form/state mapping, route and helper are aligned.
  - Email, shipping selection, coupon code, failure responses and permitted checkout revisions are defined.
  - The documented happy path is verified with those exact contracts.
- **Preserve:** the scope declaration (one-time vs recurring territory).
- **Likely affected docs / consumers:** ECOM §§3–6; FC-068 (checkout store shape), FC-051.
- **Verification intent:** a contract-level consistency check across the linked snippets:
  - `shippingMethod` is present;
  - the email location agrees;
  - the coupon is delivered;
  - the helper name and signature match.
- **Open decision:** none beyond DEC-05.
- **Proposed route:** `SYNC`. Wave 1, paired with FC-051.

**Mapping proposal — ENGINEER-PROPOSED:** Use one validated checkout contract across form, state, route and service. The request carries billing.email, validated line identifiers/quantities, shippingMethod and couponCode; it carries no authoritative monetary values. The response identifies the authorized order/payment attempt or a typed generic failure. The server pricing operation from the same contract supplies totals. Revisions to items, shipping or coupon invalidate the old payment binding before a new attempt is released.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:181` — ## 3. PaymentIntent Flow; MANIFEST ← 3: API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:412` — ## 4. Checkout Implementation; MANIFEST ← 3: API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:661` — ## 5. Order Management; MANIFEST ← 3: API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:877` — ## 6. Cart Logic; MANIFEST ← 3: API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.

**Touch proposal:** C-060. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-060` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-061 — Revalidation secret comparison fails open when the environment variable is absent

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/05_api_commerce_corrections.md:358`):

- **Certified record:** CF-10 · Severity MEDIUM · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C05-D13 · Fable none
- **Evidence:** Astra C05 §7 C05-D13; Sol C05 §4 (MEDIUM by default; HIGH when invalidation scope or cost is material). Certified closure: MEDIUM, 2026-09-27.
- **Defect surfaces (`0a787cb`):** `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md` §9, "ISR and Revalidation".
- **Defect:** the route rejects only when `secret !== process.env.REVALIDATION_SECRET`, so when both are undefined the check passes.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - A non-empty configured secret is validated at startup.
  - Missing or invalid supplied credentials are rejected before comparison.
  - Invalidation targets are bounded, and the unset-secret case is verified.
- **Preserve:** the revalidation capability.
- **Likely affected docs / consumers:** API §9; other secret-comparison recipes (propagation search).
- **Verification intent:** the documented checks include the unset-secret case, and it is rejected.
- **Open decision:** none. Sol's conditional HIGH is noted under DEC-22.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Validate a nonempty revalidation secret at startup. Reject missing or invalid supplied credentials before comparing; an absent environment value never authenticates an absent request value. Authorize and bound invalidation targets. Verify the unset-secret case causes no invalidation.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:1328` — ## 9. Performance Patterns; MANIFEST ← 5: APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, DATABASE_MANUAL, ECOMMERCE_AND_PAYMENTS_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.

**Touch proposal:** C-061. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-061` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-062 — Refund and dispute events are advertised but acknowledged without their required work

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/05_api_commerce_corrections.md:285`):

- **Certified record:** CF-09 · Severity MEDIUM · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C05-D18 · Fable none
- **Evidence:** Astra C05 §7 C05-D18; Sol C05 §5 (placeholders must be unmistakably non-production).
- **Defect surfaces (`0a787cb`):** `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md` §9 (event table, `handleRefund`, dispute fall-through, production checklist).
- **Defect:** the event table requires order updates and notifications for refunds and disputes. `handleRefund` only logs, disputes fall through to an unhandled-event log, and both are acknowledged as successful.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - The minimum refund (partial vs full) and dispute state changes are defined, or these handlers are explicitly marked INCOMPLETE / not for production until implemented.
  - Notification and failure owners are named.
  - Acknowledgment comes only after the required local work is safely accepted.
- **Preserve:** the event table as the requirements statement.
- **Likely affected docs / consumers:** ECOM §9; FC-052, FC-020 (DEC-03).
- **Verification intent:** each advertised event either has its documented local effect or carries an unmistakable INCOMPLETE label, and the production checklist references the decision.
- **Open decision:** DEC-03.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Refund and dispute handling is INCOMPLETE and not a production recipe until the module contract defines partial/full refund effects, dispute transitions, notification and recovery owners. Do not acknowledge a supported event until its required local work is completed or durably accepted under the webhook contract.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:1511` — ## 9. Webhook Handling; MANIFEST ← 3: API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.

**Touch proposal:** C-062. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-062` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-063 — Local validation recipes do not require API trust-boundary or event-failure negative cases

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/05_api_commerce_corrections.md:426`):

- **Certified record:** CF-05 · Severity MEDIUM · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C05-D16 · Fable none
- **Evidence:** Astra C05 §7 C05-D16; Sol C05 §5 (conditional, pending a testing-domain cross-check). Certified closure: MEDIUM, 2026-09-27.
- **Defect surfaces (`0a787cb`):**
  - `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md` §§10–11
  - `04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md` §12 and deployment verification
  - `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md` (testing cross-reference)
  - `03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md`
- **Defect:** the local test recipes cover happy paths, declines and 3DS. They do not require these negative cases:
  - forged status calls
  - cross-user IDs
  - tampered totals
  - concurrency
  - invalid signatures
  - failed persistence
  - reordering
  - resubscription
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - A minimum API-level negative matrix covers those eight classes. Each case states the expected status, the absence of unauthorized effects, the persisted final state and the retry/recovery evidence.
  - The matrix has a named producer and reviewer.
  - Recommended placement: the Factory test owner (TESTING), referenced by ECOM, STRIPE and API rather than duplicated.
- **Preserve:** the existing negative checks:
  - STRIPE §§11–12: redirect rejection, tier combinations, unknown Price mapping, single-subscription upgrades
  - ECOM §10: declines and 3DS
- **Likely affected docs / consumers:** TESTING, ECOM, STRIPE, API. The expected behaviors come from the CF-08, CF-09 and CF-10 outcomes.
- **Verification intent:** all eight case classes appear with expected outcomes, and the ECOM, STRIPE and API recipes link to the matrix.
- **Open decision:** where the matrix lives, TESTING vs each manual (Jarvis).
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** The Architect includes the API trust-boundary matrix in the acceptance contract; the Engineer supplies engineering results, the QA Executor derives independent checks, and the QA Lead approves and grades them. Cover unauthenticated/wrong-role/wrong-owner calls, forged payment status, tampered totals, duplicate and concurrent requests, invalid signatures, pre-acceptance persistence failure, post-acceptance worker failure, and stale/out-of-order events. Each case records status, absence of unauthorized effects, persisted final state and retry/recovery evidence. TESTING_PLAYBOOK owns the matrix; commerce, subscription and API manuals refer to it.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:823` — ## 3.8 Run-verification rituals (promoted from Run 001); MANIFEST ← 11: SOFTWARE_FACTORY_PLAYBOOK, ENGINEER_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, API_AND_SERVICES_MANUAL, DATABASE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.
- `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:1647` — ## 10. Testing Payments; MANIFEST ← 3: API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:732` — ## 12. Testing Strategy; MANIFEST ← 1: ECOMMERCE_AND_PAYMENTS_MANUAL.
- `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:1564` — ## 11. Webhook Integration Patterns; MANIFEST ← 5: APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, DATABASE_MANUAL, ECOMMERCE_AND_PAYMENTS_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.

**Touch proposal:** C-063. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-063` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-064 — Service error-handling doctrine collapses or propagates dependency failures inconsistently with testing and module failure-policy doctrine

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/05_api_commerce_corrections.md:375`):

- **Certified record:** CF-10 · Severity MEDIUM · Review PARTIAL · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C05-D14 · Fable FBL-D022 (primary)
- **Evidence:** Astra C05 §7 C05-D14; Sol C05 §5; Fable §7 FBL-D022, §9 row 9.
- **Defect surfaces (`0a787cb`):**
  - `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md` §3 (Error Handling Template), §4, §6, §8, §10 (cheat sheet)
  - `04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md` §3, §8
  - `03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md` §1.8, §2.2, §4.3
  - `03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md` §7
- **Defect:**
  - Failure, absence and empty data are collapsed into one result.
  - Public caches can hold an empty catalog after an outage.
  - Every error is mapped to 400.
  - A failed subscription read is treated as a free user.
  - The template propagates raw upstream `error.message` to clients.
  - Degrade-by-default contradicts BIM §7's per-module failure policy.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - An explicit result contract (success, not-found, unavailable, invalid, forbidden) maps to HTTP and UI behavior.
  - Services return typed errors, and routes map them to generic client messages without raw upstream text.
  - Failed results are never served from successful public caches.
  - Degrade vs fail-closed follows BIM §7's per-module failure policy rather than a universal "return empty array".
  - A failed entitlement read is never represented as confirmed absence.
- **Preserve:** safe UI rendering; the `{ data, error, success }` envelope; machine-readable error and correlation information.
- **Likely affected docs / consumers:** API §3/§4/§6/§8/§10, STRIPE §3/§8; TESTING §2.2 test 4 (must be satisfiable); FC-021, FC-051.
- **Verification intent:**
  - The cheat-sheet "Graceful Degradation — return empty array on error" is removed or scoped by failure policy.
  - No route template forwards `error.message`.
  - TESTING §2.2 test 4 passes against the template.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Services return an explicit typed outcome: success, not-found, unavailable, invalid or forbidden. Routes map it to the approved HTTP/UI behavior with generic client messages and no upstream error text. Do not cache failures as successful public data. Degrade or fail closed according to the module’s approved failure policy; an unavailable entitlement read is not confirmed absence.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:166` — ## 3. Service Layer Implementation; MANIFEST ← 5: APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, DATABASE_MANUAL, ECOMMERCE_AND_PAYMENTS_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:1164` — ## 8. Error Handling Strategy; MANIFEST ← 5: APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, DATABASE_MANUAL, ECOMMERCE_AND_PAYMENTS_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:1328` — ## 9. Performance Patterns; MANIFEST ← 5: APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, DATABASE_MANUAL, ECOMMERCE_AND_PAYMENTS_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:550` — ## 8. The Service Layer Swap Pattern; MANIFEST ← 1: ECOMMERCE_AND_PAYMENTS_MANUAL.
- `03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:151` — ## Principle 1.8 — Defensive error message assertions for security-sensitive endpoints; MANIFEST ← 11: SOFTWARE_FACTORY_PLAYBOOK, ENGINEER_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, API_AND_SERVICES_MANUAL, DATABASE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.

**Touch proposal:** C-064. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-064` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-065 — Success polling can confirm an old tier and claims receipt of unverified payment

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/05_api_commerce_corrections.md:302`):

- **Certified record:** CF-09 · Severity MEDIUM · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C05-D15 · Fable none
- **Evidence:** Astra C05 §7 C05-D15; Sol C05 §5.
- **Defect surfaces (`0a787cb`):** `04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md` §1, §7, §9.
- **Defect:** the success page confirms whenever the tier is no longer `free`, which an upgrading user already satisfies. After the polls time out it says "Your payment was received!".
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):** polling targets the server-authorized expected transition (target tier plus qualifying status). Timeouts show an honest pending/unknown state with a recovery or support path.
- **Preserve:** the rule that redirects are cosmetic and never confirm payment on their own.
- **Likely affected docs / consumers:** STRIPE §7/§9.
- **Verification intent:** an upgrade from Starter to Pro does not confirm before the Pro transition, and the timeout copy makes no payment claim.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Poll the server-authorized payment attempt and expected target tier with its qualifying subscription status. A pre-existing paid tier is not evidence of this upgrade. A timeout shows pending or unknown and its recovery/support path; it never claims payment receipt. Redirects remain cosmetic.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:507` — ## 7. The Tier Upgrade Pattern; MANIFEST ← 1: ECOMMERCE_AND_PAYMENTS_MANUAL.
- `04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:605` — ## 9. Success Page Polling Pattern; MANIFEST ← 1: ECOMMERCE_AND_PAYMENTS_MANUAL.

**Touch proposal:** C-065. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-065` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-066 — API examples assign incompatible signatures and representations to the same service contracts

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/05_api_commerce_corrections.md:407`):

- **Certified record:** CF-10 · Severity MEDIUM · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C05-D12 · Fable none
- **Evidence:** Astra C05 §7 C05-D12; Sol C05 §5.
- **Defect surfaces (`0a787cb`):** `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md` §3, §4, §7, §8.
- **Defect:** `fetchProducts` has three incompatible signatures and return shapes, and `Product` is both a wire-shaped and a normalized type in the same module.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - Wire and internal types are distinct.
  - One service signature and result envelope is used, with explicit ownership of normalization.
  - Consumers are aligned, or incompatible examples are labeled as independent alternatives with their own contracts.
- **Preserve:** the rule that UI code never sees wire casing.
- **Likely affected docs / consumers:** API; FC-070, best done in the same sync.
- **Verification intent:** every `fetchProducts` and `Product` occurrence matches one declared contract or a labeled alternative.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Declare wire and internal types separately and normalize once at the service boundary. A named operation uses one parameter signature and typed result envelope in its service, route and client examples. Any independent alternative is explicitly labeled with its own contract; callers do not silently mix array, paginated and wrapped results.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:166` — ## 3. Service Layer Implementation; MANIFEST ← 5: APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, DATABASE_MANUAL, ECOMMERCE_AND_PAYMENTS_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:383` — ## 4. API Route Patterns; MANIFEST ← 5: APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, DATABASE_MANUAL, ECOMMERCE_AND_PAYMENTS_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:998` — ## 7. Data Transformation; MANIFEST ← 5: APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, DATABASE_MANUAL, ECOMMERCE_AND_PAYMENTS_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:1164` — ## 8. Error Handling Strategy; MANIFEST ← 5: APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, DATABASE_MANUAL, ECOMMERCE_AND_PAYMENTS_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.

**Touch proposal:** C-066. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-066` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-067 — The per-product coupon calculator has no line-item information and applies one flat discount

**Proposed disposition:** BLOCKED. **Authority:** certified correction YES; package outcome remains proposed. CONDITIONAL: DEC-05 pricing interface. 

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/05_api_commerce_corrections.md:133`):

- **Certified record:** CF-08 · Severity MEDIUM · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C05-D17 · Fable none
- **Evidence:** Astra C05 §7 C05-D17; Sol C05 §5.
- **Defect surfaces (`0a787cb`):** `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md` §8.
- **Defect:** the `fixed_product` branch of `calculateCouponDiscount(coupon, subtotal)` returns the same flat amount as `fixed_cart`. It receives no product, eligibility or quantity input.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):** the discount comes from the authoritative quote with eligible line items, or a display estimate uses a validated line/quantity model. `fixed_product` is not advertised through the flat-cart branch.
- **Preserve:** coupon types that are correct.
- **Likely affected docs / consumers:** ECOM §8; FC-051 (quote).
- **Verification intent:** two carts with the same subtotal but different eligible quantities yield different documented discounts, or the `fixed_product` claim is withdrawn.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** A fixed-product coupon uses validated eligible line items and quantities in the authoritative server pricing operation. Do not advertise fixed_product through a flat-cart subtotal branch. A client calculation is a display estimate only. Verify equal-subtotal carts with different eligible quantities; preserve valid fixed-cart and percentage behavior.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:1285` — ## 8. Coupon System; MANIFEST ← 3: API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.

**Touch proposal:** C-067. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-067` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-068 — ECOMMERCE defers to a checkout store the STATE manual does not define

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/05_api_commerce_corrections.md:459`):

- **Certified record:** CF-07 · Severity LOW · Review UNIQUE (Fable) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra none · Fable FBL-D026
- **Evidence:** Fable §7 FBL-D026.
- **Defect surfaces (`0a787cb`):**
  - `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md` §4, §7, §8
  - `04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md` §6
- **Defect:** ECOM §7 points to STATE for "the full checkout store", then uses `shippingCost`, `couponCode`, `couponDiscount`, `setCoupon` and `clearCoupon`. None of these exist in STATE §6's template.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):** ECOM and STATE share one checkout store shape, and the cross-reference resolves to it.
- **Preserve:** whatever shape is chosen must also satisfy FC-040's personal-data lifecycle.
- **Likely affected docs / consumers:** ECOM §4/§7/§8, STATE §6; FC-060, FC-040.
- **Verification intent:** every store member ECOM uses exists in the STATE template, or ECOM defines it.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** The checkout interaction contract includes shippingCost and couponDiscount as display estimates, couponCode, setCoupon(code) and clearCoupon(), alongside the existing checkout fields. The server revalidates shipping and coupons. STATE_MANAGEMENT_MANUAL owns the shared store shape; ECOMMERCE_AND_PAYMENTS_MANUAL refers to it. Personal fields follow the approved account-transition and retention policy.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:412` — ## 4. Checkout Implementation; MANIFEST ← 3: API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:1224` — ## 7. Checkout Store; MANIFEST ← 3: API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:1285` — ## 8. Coupon System; MANIFEST ← 3: API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:745` — ## 6. Store Templates; MANIFEST ← 3: APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, ECOMMERCE_AND_PAYMENTS_MANUAL.

**Touch proposal:** C-068. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-068` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-069 — Supabase secret environment-variable names differ across manuals

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/05_api_commerce_corrections.md:475`):

- **Certified record:** CF-07 · Severity LOW · Review UNIQUE (Fable) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra none · Fable FBL-D027
- **Evidence:** Fable §7 FBL-D027.
- **Defect surfaces (`0a787cb`):**
  - `03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md` §4.1
  - `04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md` §4
  - `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md` §5
  - `04_REFERENCE_MANUALS/DATABASE_MANUAL.md` §5
  - `02_PIPELINE_AGENTS/RECON_QUESTIONNAIRE.md` S0.6
- **Defect:** TESTING uses `SUPABASE_SECRET_KEY` while STRIPE, API and DATABASE use `SUPABASE_SERVICE_ROLE_KEY`, and RECON notes the newer publishable/secret naming. Fable rates the impact limited because RECON calls doc env names suggestive.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):** one environment-variable names table, including the newer publishable/secret naming, carries a "verify on disk" note, and the manuals reference it.
- **Preserve:** RECON's "doc env names are suggestive; disk wins".
- **Likely affected docs / consumers:** the surfaces above; FC-022 (the E2E target check may depend on these names).
- **Verification intent:** every Supabase key name in live recipes matches the table or cites it.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Verify credential names and capabilities on disk. SUPABASE_SERVICE_ROLE_KEY and SUPABASE_SECRET_KEY are server-only elevated-credential conventions, not interchangeable proof of project configuration; public anon/publishable keys are a separate capability class. RECON_QUESTIONNAIRE S0.6 owns the environment-name/capability table. Record the actual variable, provider key type and server-only exposure without printing values; manuals refer to that table.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `02_PIPELINE_AGENTS/RECON_QUESTIONNAIRE.md:63` — ## SECTION 0 — The Day-1 Ground-Truth Sweep (Run 001 Meta-Lesson); MANIFEST ← 13: APP_FACTORY_BLUEPRINT, ARCHITECT_PLAYBOOK, ARCHITECT_QUESTIONNAIRE, ENGINEER_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, APP_FACTORY_SKILLS_PLAYBOOK, FFM_PLAYBOOK, TESTING_PLAYBOOK, APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:847` — ## 4.1 Supabase-backed apps (StarkReads example); MANIFEST ← 11: SOFTWARE_FACTORY_PLAYBOOK, ENGINEER_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, API_AND_SERVICES_MANUAL, DATABASE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.
- `04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:271` — ## 4. Environment Variables; MANIFEST ← 1: ECOMMERCE_AND_PAYMENTS_MANUAL.
- `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:543` — ## 5. External API Integration; MANIFEST ← 5: APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, DATABASE_MANUAL, ECOMMERCE_AND_PAYMENTS_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/DATABASE_MANUAL.md:390` — ## 5. Row Level Security (RLS); MANIFEST ← 2: API_AND_SERVICES_MANUAL, AUTH_MANUAL.

**Touch proposal:** C-069. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-069` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-070 — API_AND_SERVICES_MANUAL has two "§10 Quick Reference" sections

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/05_api_commerce_corrections.md:496`):

- **Certified record:** CF-13 · Severity LOW · Review CONFLICT · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C05-S03 (SUGGESTION) · Fable FBL-D029
- **Sol adjudication (certified):** ACCEPT DEFECT (2026-09-27): "Duplicate §10 Quick Reference sections and an inconsistent ToC are objective documentation defects, albeit low impact."
- **Evidence:** Fable §7 FBL-D029; Astra C05 §8 (C05-S03, which cites the duplicates at baseline lines 1442 and 1993); register §7.1.
- **Defect surfaces (`0a787cb`):** `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md`, the ToC and both "## 10. Quick Reference" headings.
- **Defect:** "## 10. Quick Reference" appears twice, with overlapping content, before and after §§11–13, and the ToC lists only ten sections.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):** one Quick Reference section, consistent section numbering and a ToC listing every section. The overlapping content is merged, with recipe assumptions declared beside the recipes (C05-S03).
- **Preserve:** the content of both quick references, merged rather than dropped.
- **Likely affected docs / consumers:** API manual; FC-066 (same sync); inbound "§10"/"§11–13" citations (propagation search).
- **Verification intent:** exactly one `## 10.` heading exists, the ToC matches the headings, and inbound section citations resolve.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Maintain one Quick Reference after the numbered API sections. Merge both existing quick-reference bodies without dropping unique content. Keep sections 1–13 stable, number the merged Quick Reference 14, and update the table of contents and incoming references to the actual heading. Declare each recipe’s service contract beside it.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:11` — ## Table of Contents; MANIFEST ← 5: APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, DATABASE_MANUAL, ECOMMERCE_AND_PAYMENTS_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:1442` — ## 10. Quick Reference; MANIFEST ← 5: APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, DATABASE_MANUAL, ECOMMERCE_AND_PAYMENTS_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.
- `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:1993` — ## 10. Quick Reference; MANIFEST ← 5: APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, DATABASE_MANUAL, ECOMMERCE_AND_PAYMENTS_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK.

**Touch proposal:** C-070. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-070` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-071 — Copyable portal and sidebar layouts hide navigation on mobile, contrary to Rule Zero, and bypass the kit shell

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/06_design_frontend_corrections.md:37`):

- **Certified record:** CF-11 · Severity HIGH · Review CONFIRMED · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C06-D02 · Fable FBL-D021 (primary; also related to FC-072)
- **Evidence:** Astra C06 §7 C06-D02; Sol C06 (ACCEPT HIGH); Fable §7 FBL-D021, §9 row 13, §2 row 8.
- **Defect surfaces (`0a787cb`):**
  - `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md`: Rule Zero; Sidebar usage; "Sidebar Layout (Desktop Only)"; Example 3 Members Portal; Navbar "hidden on mobile"
  - `05_DESIGN_SYSTEM/COMPONENT_REGISTRY.md`: AppShellPage; raw app-shell anti-pattern
  - `04_REFERENCE_MANUALS/APP_ARCHITECTURE_MANUAL.md` §4 (`<Sidebar className="w-64 hidden md:block" />`)
  - Gate M consumers: `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md`, `03_BUILD_METHODOLOGY/FRONTEND_BUILD_PHASE_PLAYBOOK.md`, `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md`
- **Defect:** Rule Zero makes a `hidden md:block` sidebar with no trigger an automatic failure. The same manual's Sidebar usage, Desktop-Only Sidebar Layout and complete Members Portal layout use exactly that pattern, with no mobile trigger, and bypass the Registry's AppShellPage.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - Every positive layout example in UI_UX and APP_ARCHITECTURE §4 keeps every navigation destination reachable at mobile widths, through an accessible mobile alternative. Any one of these qualifies:
    - the kit AppShellPage;
    - a complete, approved Sheet/drawer-triggered equivalent;
    - a desktop sidebar (which may use `hidden md:block`) paired, in the same example, with an accessible mobile trigger or alternative navigation.
  - Otherwise the example is explicitly retired.
  - **The class string is not the defect;** a hidden sidebar *without* a mobile alternative is.
- **Preserve:**
  - Rule Zero's mobile requirements and Gate M.
  - Registry drawer behavior: close-on-navigate, Esc, outside-tap.
  - Kit shell reuse.
  - Legitimate desktop-sidebar patterns that ship with a mobile alternative.
- **Likely affected docs / consumers:** UI_UX, APP_ARCHITECTURE §4, REGISTRY; FC-072; builders copying Example 3.
- **Verification intent:**
  - For each positive layout example, a reviewer confirms:
    - every navigation destination the desktop sidebar offers is reachable at mobile widths;
    - the mobile trigger or alternative is present in the example itself, operable and accessible (labeled control, keyboard operable, dismissible per the Registry drawer behavior).
  - Example 3, the Sidebar Layout, the Sidebar usage and APP_ARCHITECTURE §4 each pass that check, or are retired.
  - A live-corpus grep for `hidden md:block` is used only to *locate* candidates. Each hit is dispositioned:
    - **CONSISTENT:** the reachable mobile alternative is present;
    - **NEGATIVE EXAMPLE:** labeled as such;
    - **CHANGE.**
  - A surviving occurrence is acceptable when paired with a verified mobile alternative.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Every positive layout example keeps every navigation destination reachable at mobile widths. Consume AppShellPage or provide a complete accessible mobile trigger/drawer or equivalent navigation alongside the desktop sidebar. hidden md:block is acceptable only when that same example supplies the mobile alternative. Retire an incomplete layout as a copyable positive example.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:477` — ## Layout Components; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:839` — ## Complete Page Examples; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `04_REFERENCE_MANUALS/APP_ARCHITECTURE_MANUAL.md:408` — ## 4. Layout System; MANIFEST ← 3: ECOMMERCE_AND_PAYMENTS_MANUAL, STATE_MANAGEMENT_MANUAL, THEMING_MANUAL.

**Touch proposal:** C-071. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-071` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-072 — Rail breakpoint rules disagree across the design tier and kit docs

**Proposed disposition:** BLOCKED. **Authority:** certified correction YES; package outcome remains proposed. CONDITIONAL: DEC-09 kit evidence. Cross-boundary component: XB-04.

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/06_design_frontend_corrections.md:74`):

- **Certified record:** CF-11 · Severity MEDIUM · Review CONFIRMED · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C06-D04 · Fable FBL-D021 (related; primary in FC-071), FBL-D023 (related; primary in FC-073)
- **Severity divergence (recorded):** Astra MEDIUM vs Fable HIGH (Fable's whole combined finding). The certified MEDIUM stands.
- **Evidence:** Astra C06 §7 C06-D04; Sol C06; Fable §7 FBL-D021, §9 row 14.
- **Defect surfaces (`0a787cb`):**
  - `05_DESIGN_SYSTEM/GLOBAL_DESIGN_SYSTEM_HANDBOOK.md` (sidebar → drawer below `lg`)
  - `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md` (Rule Zero 1024; quick reference "custom `lg` 1150px"; breakpoint table)
  - `05_DESIGN_SYSTEM/COMPONENT_REGISTRY.md` (AppShellPage `xl`/1280; quick table 768; §7)
  - `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md` §6 (`xl`/1280; per-component fit)
  - `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md` (Gate M, §13.1)
  - `03_BUILD_METHODOLOGY/FRONTEND_BUILD_PHASE_PLAYBOOK.md` (Stage 2)
  - `05_DESIGN_SYSTEM/TOKEN_FILE.md`
  - `04_REFERENCE_MANUALS/APP_ARCHITECTURE_MANUAL.md`
- **Defect:** one wide app rail is given three persistence/drawer breakpoints: `lg`/1024, `xl`/1280 and 768. The UI quick reference also calls `lg` a custom 1150px breakpoint.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - One rail rule defers to the verified per-component fit contract. Fable: the AppShellPage rail is `xl` as shipped, and the Gate M threshold is the rail's declared fit breakpoint.
  - Generic tables and quick references are synchronized, and the 1150px line is corrected.
  - Verification exercises both sides of the actual transition.
- **Preserve:** the Handbook's per-component fit override; mobile drawer behavior; Gate M.
- **Likely affected docs / consumers:** the surfaces above; Gate M checks in FFM and FBP.
- **Verification intent:**
  - Every rail-breakpoint statement in live docs agrees or cites the rule.
  - Gate M cites it.
  - The documented test widths include the rail transition.
- **Open decision:** DEC-09, confirming the shipped kit value. `xl`/1280 is corroborated by the Handbook; kit source was not inspected (`XB-EXT`; GAP).
- **Proposed route:** `SYNC` (+ `XB-EXT` verification).

**Mapping proposal — ENGINEER-PROPOSED:** The rail transition follows the component’s verified fit contract, not an unrelated generic device label. Verify both sides of the actual transition. The Handbook reports xl/1280 for AppShellPage; publish that as the universal kit value only after pinned kit verification. The 1150px assertion is not a substitute for that check.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:661` — ## Responsive Design Patterns; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/COMPONENT_REGISTRY.md:589` — ## 7. Mobile Behavior Reference; MANIFEST ← 5: DESIGNER_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, GLOBAL_DESIGN_SYSTEM_HANDBOOK, UI_UX_BUILDING_MANUAL.
- `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md:429` — ## 6. Responsive & Mobile-Nav; MANIFEST ← 12: ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, FRONTEND_BUILD_PHASE_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, TESTING_PLAYBOOK, API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, DATABASE_MANUAL, STATE_MANAGEMENT_MANUAL, COMPONENT_REGISTRY, UI_UX_BUILDING_MANUAL.
- `05_DESIGN_SYSTEM/GLOBAL_DESIGN_SYSTEM_HANDBOOK.md:64` — ## 5. Layout & responsive (Rule Zero); MANIFEST ← 6: DESIGNER_PLAYBOOK, COMPONENT_REGISTRY, THEME_LIBRARY, THEMING_MANUAL, TOKEN_FILE, UI_UX_BUILDING_MANUAL.

**Touch proposal:** C-072. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-072` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-073 — Positive examples present numbered Tailwind colors as convention while Rule Zero-B calls them automatic failures

**Proposed disposition:** BLOCKED. **Authority:** certified correction YES; package outcome remains proposed. CONDITIONAL: DEC-06. 

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/06_design_frontend_corrections.md:103`):

- **Certified record:** CF-11 · Severity MEDIUM · Review CONFIRMED · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C06-D06 · Fable FBL-D023 (primary)
- **Evidence:** Astra C06 §7 C06-D06; Sol C06; Fable §7 FBL-D023, §9 row 15.
- **Defect surfaces (`0a787cb`):**
  - `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md` (`Main` usage `bg-gray-50`; §10.5 "explicit dark variants"; §10.8)
  - `05_DESIGN_SYSTEM/COMPONENT_REGISTRY.md` (AppShellPage theme behavior `dark:bg-zinc-800`)
  - `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md` §9 "Theme Conventions"
  - `05_DESIGN_SYSTEM/GLOBAL_DESIGN_SYSTEM_HANDBOOK.md` §3.4
  - `05_DESIGN_SYSTEM/TOKEN_FILE.md` §4
- **Defect:** UI_UX and the Registry positively endorse palette literals that Rule Zero-B fails and that GDSH/TOKEN_FILE treat as migration debt. The Handbook states its explicit classes as conventions, with no migration flag.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - Positive examples use semantic token utilities.
  - Unmigrated kit palette literals are labeled as a surfaced migration dependency, never the target convention. Fable's wording: "LEGACY — migration task per TOKEN_FILE §4".
- **Preserve:**
  - Rule Zero-B.
  - The kit baseline: Astra is explicit that this finding does not authorize changing the kit.
  - "Match, don't invent", as scoped by the FC-005 precedence ruling.
- **Likely affected docs / consumers:** the surfaces above; FC-005, FC-077.
- **Verification intent:**
  - Positive examples contain no numbered palette classes.
  - Handbook §9 and the Registry entry carry the migration label.
- **Open decision:** DEC-06, the precedence ruling (disk-wins vs Rule Zero-B). This is the Sol C06 cross-domain item "kit authority vs token migration".
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Use semantic token utilities in positive examples. A palette literal inherited from a kit is labeled “LEGACY — migration task per TOKEN_FILE §4”; it is evidence of current state, not the target convention. Resolve a conflict through the approved question-scoped authority rule rather than silently selecting disk or Rule Zero-B.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:212` — ## Common Components; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1339` — #### 10. Developer Experience Tools; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1481` — ## 10. Advanced Design Patterns; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1487` — ### 10.1 CVA (Class Variance Authority); MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1600` — ### 10.2 Design Tokens; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1750` — ### 10.3 Component Catalogue Pattern; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1847` — ### 10.4 Class Ordering Convention; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1899` — ### 10.5 Dark Mode Best Practices; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1948` — ### 10.6 Touch Device Considerations; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:2007` — ### 10.7 The `cn()` Utility; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:2042` — ### 10.8 Quick Reference: Do's and Don'ts; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/COMPONENT_REGISTRY.md:85` — ## 1. Common Layout Primitives (`src/components/common/`); MANIFEST ← 5: DESIGNER_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, GLOBAL_DESIGN_SYSTEM_HANDBOOK, UI_UX_BUILDING_MANUAL.
- `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md:525` — ## 9. Build & Framework Notes; MANIFEST ← 12: ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, FRONTEND_BUILD_PHASE_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, TESTING_PLAYBOOK, API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, DATABASE_MANUAL, STATE_MANAGEMENT_MANUAL, COMPONENT_REGISTRY, UI_UX_BUILDING_MANUAL.

**Touch proposal:** C-073. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-073` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-074 — The drop-in token palette fails its own AA contrast claim

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/06_design_frontend_corrections.md:210`):

- **Certified record:** CF-12 · Severity HIGH · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C06-D03 · Fable none
- **Evidence:** Astra C06 §7 C06-D03 (computed contrast table); Sol C06 (ACCEPT HIGH; "not a subjective palette disagreement").
- **Defect surfaces (`0a787cb`):**
  - `05_DESIGN_SYSTEM/TOKEN_FILE.md` (HSL values; "Verified in the style tile")
  - `05_DESIGN_SYSTEM/GLOBAL_DESIGN_SYSTEM_HANDBOOK.md` (AA requirement)
  - `05_DESIGN_SYSTEM/THEME_LIBRARY.md` (status values; brand-only list)
- **Defect:** pairs computed from the HSL values fall below the 4.5:1 ordinary-text threshold, yet TOKEN_FILE says "Verified in the style tile":
  - success on card (Mist): 3.48
  - warning: 2.21
  - info: 4.16 (Mist) and 2.95 (Slate)
  - primary-foreground on primary: 2.82
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - The failing text/fill pairs are retuned per mode, keeping their semantic meaning.
  - A computed contrast matrix covering the documented uses is kept, and any "verified" claim cites it.
  - THEME_LIBRARY values are synchronized.
  - Accessible foreground pairing is allowed for brand colors.
- **Preserve:**
  - The destructive and role colors that pass. Astra: do not replace the whole palette.
  - Per-mode tuning; identities-not-statuses role tokens.
- **Likely affected docs / consumers:** TOKEN_FILE, THEME_LIBRARY, GDSH; FC-077.
- **Verification intent:** recompute every documented text/fill pair with Astra's stated method (HSL → sRGB, linearize at 0.04045, weights 0.2126/0.7152/0.0722). Each must reach ≥ 4.5:1 for ordinary text or carry a documented large-text exception.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Do not claim AA verification without a computed contrast matrix for each documented text/fill use in light and dark modes. Retune failing semantic pairs and synchronize THEME_LIBRARY. Brand fills may use a separate accessible foreground. Record the exact token values, ratio, intended use and threshold; large-text or non-text thresholds do not justify a normal-text claim.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `05_DESIGN_SYSTEM/TOKEN_FILE.md:14` — ## 1. Entry stylesheet (`globals.css` _or_ `globals.scss`); MANIFEST ← 3: GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEME_LIBRARY, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/THEME_LIBRARY.md:25` — ## 2. The "Metro Warm" family (Cyber Pharma v1); MANIFEST ← 4: DESIGNER_PLAYBOOK, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL, TOKEN_FILE.
- `05_DESIGN_SYSTEM/THEME_LIBRARY.md:72` — ## 3. Adding a new theme (the repeatable process); MANIFEST ← 4: DESIGNER_PLAYBOOK, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL, TOKEN_FILE.

**Touch proposal:** C-074. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-074` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-075 — Theming handoff instructions demote required executable visual artifacts (HTML/PNG)

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/06_design_frontend_corrections.md:129`):

- **Certified record:** CF-11 · Severity HIGH · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C06-D01 · Fable none
- **Evidence:** Astra C06 §7 C06-D01; Sol C06 (ACCEPT HIGH; "a real producer/consumer contract break").
- **Defect surfaces (`0a787cb`):**
  - `05_DESIGN_SYSTEM/THEMING_MANUAL.md` §§4.2–4.3, Phase 1 sequence
  - `05_DESIGN_SYSTEM/GLOBAL_DESIGN_SYSTEM_HANDBOOK.md` (deliverable contract; human locks)
  - Consumer check: `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md`, `02_PIPELINE_AGENTS/DESIGNER_PLAYBOOK.md`
- **Defect:** THEMING labels supporting deliverables "Visual Reference, Not Executable" and goes straight from the token snippet to fabrication. The GDSH and the Engineer consumer require locked, token-driven HTML/PNG plus human canonical-screen and style-tile locks.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - THEMING §4 defers to the GDSH full deliverable contract: HTML as build reference, PNG as fidelity target.
  - Its phase sequence includes or links the canonical-screen and style-tile human locks before fabrication.
- **Preserve:** the Sol C06 preservation list; the FC-018 not-applicable path for nonvisual builds.
- **Likely affected docs / consumers:** THEMING, GDSH; Designer and Engineer handshake.
- **Verification intent:**
  - THEMING no longer calls HTML/PNG non-executable or "NOT the contract".
  - Phase 1 includes both locks before fabrication.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Designer handoff follows GLOBAL_DESIGN_SYSTEM_HANDBOOK §8: executable HTML is the build reference and PNG is the fidelity target for visual interfaces. Lock the canonical screen and style tile with the human approver before fabrication. Theme notes do not replace either deliverable.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `05_DESIGN_SYSTEM/THEMING_MANUAL.md:126` — ## 4. The Designer's Deliverable; MANIFEST ← 5: DESIGNER_PLAYBOOK, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEME_LIBRARY, TOKEN_FILE, UI_UX_BUILDING_MANUAL.
- `05_DESIGN_SYSTEM/THEMING_MANUAL.md:130` — ### 4.1 Primary Deliverable — The Tokens File; MANIFEST ← 5: DESIGNER_PLAYBOOK, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEME_LIBRARY, TOKEN_FILE, UI_UX_BUILDING_MANUAL.
- `05_DESIGN_SYSTEM/THEMING_MANUAL.md:158` — ### 4.2 Supporting Deliverables (Visual Reference, Not Executable); MANIFEST ← 5: DESIGNER_PLAYBOOK, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEME_LIBRARY, TOKEN_FILE, UI_UX_BUILDING_MANUAL.
- `05_DESIGN_SYSTEM/THEMING_MANUAL.md:168` — ### 4.3 Why This Format; MANIFEST ← 5: DESIGNER_PLAYBOOK, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEME_LIBRARY, TOKEN_FILE, UI_UX_BUILDING_MANUAL.
- `05_DESIGN_SYSTEM/THEMING_MANUAL.md:247` — ## 9. The Phase 0 / Phase 1 Discipline; MANIFEST ← 5: DESIGNER_PLAYBOOK, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEME_LIBRARY, TOKEN_FILE, UI_UX_BUILDING_MANUAL.

**Touch proposal:** C-075. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-075` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-076 — The replacement Button recipe breaks its advertised variant and `asChild` composition API

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/06_design_frontend_corrections.md:237`):

- **Certified record:** CF-12 · Severity MEDIUM · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C06-D08 · Fable none
- **Evidence:** Astra C06 §7 C06-D08; Sol C06.
- **Defect surfaces (`0a787cb`):** `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md` §10.1 (replacement `button.tsx`) and the public-home `<Button asChild><Link>` example.
- **Defect:** the replacement defines variants and sizes that do not include the documented `variant="primary"` / `size="md"`. It declares `asChild` but always renders `<button>`.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):** the manual tells builders to consume the kit Button. If its internals are taught, it uses a source-matched excerpt that keeps the actual variant names and child composition, clearly separate from any replacement instruction.
- **Preserve:** kit reuse; the documented link-composition pattern.
- **Likely affected docs / consumers:** UI_UX §10.1; FC-079 (same recipe).
- **Verification intent:** every Button usage in the docs type-checks against the documented API, and `asChild` composition yields a single link element.
- **Open decision:** none.
- **Proposed route:** `SYNC`, paired with FC-079.

**Mapping proposal — ENGINEER-PROPOSED:** Consume the kit Button, including its verified variants, sizes and asChild composition. Do not replace it with this shortened implementation. An educational internal excerpt must be source-matched and labeled as an excerpt, not installation code. Preserve Link composition through the kit API.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1339` — #### 10. Developer Experience Tools; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1481` — ## 10. Advanced Design Patterns; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1487` — ### 10.1 CVA (Class Variance Authority); MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1600` — ### 10.2 Design Tokens; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1750` — ### 10.3 Component Catalogue Pattern; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1847` — ### 10.4 Class Ordering Convention; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1899` — ### 10.5 Dark Mode Best Practices; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1948` — ### 10.6 Touch Device Considerations; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:2007` — ### 10.7 The `cn()` Utility; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:2042` — ### 10.8 Quick Reference: Do's and Don'ts; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.

**Touch proposal:** C-076. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-076` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-077 — Token inventory and setup quick paths have not inherited the canonical token contract

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/06_design_frontend_corrections.md:150`):

- **Certified record:** CF-11 · Severity MEDIUM · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C06-D05 · Fable none
- **Evidence:** Astra C06 §7 C06-D05; Sol C06.
- **Defect surfaces (`0a787cb`):**
  - `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md` (token minimum; Rule Zero-B setup path)
  - `05_DESIGN_SYSTEM/THEMING_MANUAL.md` (Phase 1 checklist)
  - `05_DESIGN_SYSTEM/GLOBAL_DESIGN_SYSTEM_HANDBOOK.md` (canonical token set; TW3/TW4 fork)
- **Defect:**
  - The UI token minimum omits the info, chart, role and radius tokens the Handbook requires.
  - The Theming Phase 1 checklist and UI Rule Zero-B hard-code `globals.css` and `tailwind.config.ts`, whatever the kit's stylesheet or Tailwind major version.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - One canonical token inventory is referenced everywhere.
  - Setup and checklists branch on the confirmed kit stylesheet and Tailwind major version.
  - Abbreviated examples are marked as excerpts.
- **Preserve:** the GDSH token contract and its TW3/TW4 fork; TOKEN_FILE as a reference template, not the live authority.
- **Likely affected docs / consumers:** UI_UX, THEMING, GDSH; FC-073, FC-074.
- **Verification intent:**
  - Every token list in live docs is the canonical set or a labeled excerpt.
  - The setup checklist has TW3/TW4 and stylesheet branches.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** GLOBAL_DESIGN_SYSTEM_HANDBOOK §2 owns the canonical token inventory; TOKEN_FILE supplies reference values. Verify the project entry stylesheet and Tailwind major version before applying setup. Abbreviated snippets are excerpts and do not replace the full token contract, including role tokens.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `05_DESIGN_SYSTEM/GLOBAL_DESIGN_SYSTEM_HANDBOOK.md:138` — ## 11. New-project checklist (so future labs are fast); MANIFEST ← 6: DESIGNER_PLAYBOOK, COMPONENT_REGISTRY, THEME_LIBRARY, THEMING_MANUAL, TOKEN_FILE, UI_UX_BUILDING_MANUAL.
- `05_DESIGN_SYSTEM/THEMING_MANUAL.md:58` — ## 3. The Token Architecture; MANIFEST ← 5: DESIGNER_PLAYBOOK, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEME_LIBRARY, TOKEN_FILE, UI_UX_BUILDING_MANUAL.
- `05_DESIGN_SYSTEM/THEMING_MANUAL.md:60` — ### 3.1 Semantic Token Categories; MANIFEST ← 5: DESIGNER_PLAYBOOK, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEME_LIBRARY, TOKEN_FILE, UI_UX_BUILDING_MANUAL.
- `05_DESIGN_SYSTEM/THEMING_MANUAL.md:96` — ### 3.2 The Files — Where Tokens Live; MANIFEST ← 5: DESIGNER_PLAYBOOK, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEME_LIBRARY, TOKEN_FILE, UI_UX_BUILDING_MANUAL.
- `05_DESIGN_SYSTEM/THEMING_MANUAL.md:114` — ### 3.3 The Light / Dark / Brand Triad; MANIFEST ← 5: DESIGNER_PLAYBOOK, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEME_LIBRARY, TOKEN_FILE, UI_UX_BUILDING_MANUAL.
- `05_DESIGN_SYSTEM/THEMING_MANUAL.md:181` — ## 5. The Quick-Swap Workflow (The Pressure-Point Win); MANIFEST ← 5: DESIGNER_PLAYBOOK, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEME_LIBRARY, TOKEN_FILE, UI_UX_BUILDING_MANUAL.
- `05_DESIGN_SYSTEM/COMPONENT_REGISTRY.md:745` — ## 10. Quick Reference — "Which Primitive Should I Use?"; MANIFEST ← 5: DESIGNER_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, GLOBAL_DESIGN_SYSTEM_HANDBOOK, UI_UX_BUILDING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1339` — #### 10. Developer Experience Tools; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1481` — ## 10. Advanced Design Patterns; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1487` — ### 10.1 CVA (Class Variance Authority); MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1600` — ### 10.2 Design Tokens; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1750` — ### 10.3 Component Catalogue Pattern; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1847` — ### 10.4 Class Ordering Convention; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1899` — ### 10.5 Dark Mode Best Practices; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1948` — ### 10.6 Touch Device Considerations; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:2007` — ### 10.7 The `cn()` Utility; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:2042` — ### 10.8 Quick Reference: Do's and Don'ts; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.

**Touch proposal:** C-077. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-077` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-078 — The dark-mode example creates a second theme controller beside the kit's provider

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/06_design_frontend_corrections.md:174`):

- **Certified record:** CF-11 · Severity MEDIUM · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C06-D07 · Fable none
- **Evidence:** Astra C06 §7 C06-D07; Sol C06.
- **Defect surfaces (`0a787cb`):**
  - `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md` §10.5 (`src/lib/theme.ts`)
  - `05_DESIGN_SYSTEM/COMPONENT_REGISTRY.md` (ThemeToggle "don't author")
  - Supporting: `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md` (DO NOT BUILD)
- **Defect:** UI §10.5 proposes a controller that toggles the HTML class and writes `localStorage.theme` independently of the kit's next-themes ThemeToggle. It also mishandles a stored `system` value.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):** the manual teaches the existing provider/ThemeToggle API. The standalone DOM/storage controller is retired or isolated as a labeled non-kit demonstration.
- **Preserve:** kit reuse; the light/dark/system three-state model.
- **Likely affected docs / consumers:** UI_UX §10.5; REGISTRY.
- **Verification intent:** no positive example creates a second theme controller in a kit build.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Consume the existing theme provider and ThemeToggle for light, dark and system modes. Do not create a second controller that edits the HTML class or localStorage.theme independently of the provider. A standalone demonstration, if retained, must be explicitly non-kit and cannot be copied into a kit project.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1339` — #### 10. Developer Experience Tools; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1481` — ## 10. Advanced Design Patterns; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1487` — ### 10.1 CVA (Class Variance Authority); MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1600` — ### 10.2 Design Tokens; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1750` — ### 10.3 Component Catalogue Pattern; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1847` — ### 10.4 Class Ordering Convention; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1899` — ### 10.5 Dark Mode Best Practices; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1948` — ### 10.6 Touch Device Considerations; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:2007` — ### 10.7 The `cn()` Utility; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:2042` — ### 10.8 Quick Reference: Do's and Don'ts; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.

**Touch proposal:** C-078. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-078` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-079 — The Button recipe violates the mandatory 44px target floor

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/06_design_frontend_corrections.md:251`):

- **Certified record:** CF-12 · Severity MEDIUM · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C06-D09 · Fable none
- **Evidence:** Astra C06 §7 C06-D09; Sol C06.
- **Defect surfaces (`0a787cb`):**
  - `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md` (Rule Zero; §10.6; Button sizes)
  - Supporting: `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md` (`coarse:` mechanism)
- **Defect:** the copyable Button sizes are 40px, 36px and 40×40px, while Rule Zero and §10.6 require targets of at least 44px.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):** the recipe meets the 44px floor or keeps the kit's coarse-pointer target-floor mechanism. Any scoped exception is stated consistently, and actual hit areas are verified.
- **Preserve:** the 44px Factory floor; the kit's `coarse:` mechanism.
- **Likely affected docs / consumers:** UI_UX; FC-076.
- **Verification intent:** every documented interactive size meets 44px, or carries the coarse-pointer mechanism and a stated, verified exception.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Interactive targets meet the Factory’s 44px floor. Retain the kit’s coarse-pointer target-floor mechanism and verify the rendered hit area, including icon and compact variants. A 36px or 40px visual box alone is not evidence of a 44px target.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1339` — #### 10. Developer Experience Tools; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1481` — ## 10. Advanced Design Patterns; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1487` — ### 10.1 CVA (Class Variance Authority); MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1600` — ### 10.2 Design Tokens; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1750` — ### 10.3 Component Catalogue Pattern; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1847` — ### 10.4 Class Ordering Convention; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1899` — ### 10.5 Dark Mode Best Practices; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1948` — ### 10.6 Touch Device Considerations; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:2007` — ### 10.7 The `cn()` Utility; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:2042` — ### 10.8 Quick Reference: Do's and Don'ts; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.

**Touch proposal:** C-079. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-079` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-080 — The proposed Grid builds utility class names Tailwind cannot reliably discover

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/06_design_frontend_corrections.md:267`):

- **Certified record:** CF-12 · Severity MEDIUM · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C06-D10 · Fable none
- **Evidence:** Astra C06 §7 C06-D10; Sol C06.
- **Defect surfaces (`0a787cb`):** `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md` (Proposed Grid; the existing literal-class helper).
- **Defect:** the proposed Grid interpolates `grid-cols-${n}` and `gap-${gap}` from numeric props, with no static mapping or safelist.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - Every variant the Grid offers has reliably generated CSS, produced through a documented mechanism the project's Tailwind version supports.
  - **Recommended simple implementation:** a bounded prop-to-literal mapping (the existing helper's approach). Each offered value maps to a complete literal class string that Tailwind's scanner can see.
  - Another supported mechanism, such as an explicit safelist, is acceptable only if it is documented beside the recipe and covers every offered variant.
  - Unbounded interpolation with no such mechanism is not acceptable.
- **Preserve:** the existing literal-class helper.
- **Likely affected docs / consumers:** UI_UX.
- **Verification intent:**
  - For every variant the recipe offers, the class it applies is generated through the documented mechanism. Check by literal presence in scanned source, or by the documented safelist/configuration, and confirm in the generated CSS for the documented variants.
  - No offered variant depends on a class appearing incidentally elsewhere in the codebase.
  - Interpolated class names are acceptable only where the documented mechanism provably covers every value they can produce.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Grid variants map each supported prop to a complete literal utility class string. Use a bounded lookup and reject unsupported values; do not construct unbounded Tailwind utility names by interpolation. Any alternative scanner/safelist mechanism must document the actual supported project version and cover every offered variant.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1339` — #### 10. Developer Experience Tools; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1481` — ## 10. Advanced Design Patterns; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1487` — ### 10.1 CVA (Class Variance Authority); MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1600` — ### 10.2 Design Tokens; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1750` — ### 10.3 Component Catalogue Pattern; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1847` — ### 10.4 Class Ordering Convention; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1899` — ### 10.5 Dark Mode Best Practices; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1948` — ### 10.6 Touch Device Considerations; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:2007` — ### 10.7 The `cn()` Utility; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:2042` — ### 10.8 Quick Reference: Do's and Don'ts; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.

**Touch proposal:** C-080. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-080` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-081 — Design-tier cross-reference paths (`agent_docs/APP_FACTORY/...`) do not resolve in the DocSet

**Proposed disposition:** BLOCKED. **Authority:** certified correction YES; package outcome remains proposed. CONDITIONAL: DEC-17 project-path part. 

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/06_design_frontend_corrections.md:290`):

- **Certified record:** CF-13 · Severity LOW · Review PARTIAL · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C06-D11 · Fable FBL-D010 (related; primary in FC-088)
- **Severity divergence (recorded):** Astra LOW vs Fable HIGH (whole finding; related only). The certified LOW stands.
- **Evidence:** Astra C06 §7 C06-D11; Sol C06; Fable §7 FBL-D010; register §7.3 item 1 (interpretive difference).
- **Defect surfaces (`0a787cb`):**
  - Primary: `05_DESIGN_SYSTEM/THEME_LIBRARY.md` (cross-references), `05_DESIGN_SYSTEM/COMPONENT_REGISTRY.md` §11
  - QA-4 resolved set: `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md`, `02_PIPELINE_AGENTS/HANDOFF_PACKAGE_PLAYBOOK.md`, `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md`, `05_DESIGN_SYSTEM/GLOBAL_DESIGN_SYSTEM_HANDBOOK.md`, `MANIFEST.md`, `_OTHERS/DOCTRINE_HUB_DESIGN_v0_1.md`
- **Defect:** THEME_LIBRARY and REGISTRY cite `agent_docs/APP_FACTORY/...` paths for the Handbook, STARTER_KIT and the UI manual, and none resolves in the Hub. Astra frames these as broken DocSet links; Fable frames the same locations as inconsistent project-side landing paths.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - Doctrine cross-references resolve DocSet-relative.
  - Paths that intentionally target a downstream project are labeled as such and follow the landing-path standard FC-088 sets.
- **Preserve:** canonical basenames, which already make recovery possible.
- **Likely affected docs / consumers:** THEME_LIBRARY, REGISTRY; FC-088, FC-003.
- **Verification intent:** every `agent_docs/APP_FACTORY/...` citation in these docs resolves at the candidate SHA or carries a project-path label consistent with FC-088.
- **Open decision:** DEC-17, whether these are project-side landing paths (joint with FC-088).
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Within the Hub, reference doctrine through canonical DocSet-relative paths. Label an intentional downstream-project snapshot separately with repository, landing path and pinned revision. The project landing-path standard remains conditional on the release/pinning decision; do not make agent_docs/APP_FACTORY a universal rule by inference.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `05_DESIGN_SYSTEM/THEME_LIBRARY.md:115` — ## Cross-References; MANIFEST ← 4: DESIGNER_PLAYBOOK, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL, TOKEN_FILE.
- `05_DESIGN_SYSTEM/COMPONENT_REGISTRY.md:775` — ## 11. Cross-References; MANIFEST ← 5: DESIGNER_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, GLOBAL_DESIGN_SYSTEM_HANDBOOK, UI_UX_BUILDING_MANUAL.
- `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md:254` — ## 4. Components — Inventory; MANIFEST ← 12: ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, FRONTEND_BUILD_PHASE_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, TESTING_PLAYBOOK, API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, DATABASE_MANUAL, STATE_MANAGEMENT_MANUAL, COMPONENT_REGISTRY, UI_UX_BUILDING_MANUAL.
- `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md:684` — ## 15. Cross-References; MANIFEST ← 12: ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, FRONTEND_BUILD_PHASE_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, TESTING_PLAYBOOK, API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, DATABASE_MANUAL, STATE_MANAGEMENT_MANUAL, COMPONENT_REGISTRY, UI_UX_BUILDING_MANUAL.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1650` — ## 16. Bridging The FFM Into The Starter Kit; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.

**Touch proposal:** C-081. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-081` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-082 — Blanket horizontal-scroll prohibitions conflict with prescribed tab and carousel patterns

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/06_design_frontend_corrections.md:191`):

- **Certified record:** CF-11 · Severity LOW · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C06-D12 · Fable none
- **Evidence:** Astra C06 §7 C06-D12; Sol C06.
- **Defect surfaces (`0a787cb`):**
  - `05_DESIGN_SYSTEM/GLOBAL_DESIGN_SYSTEM_HANDBOOK.md` (tabs as a horizontal scroll strip)
  - `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md` (Rule Zero; §10.6 carousel)
  - `05_DESIGN_SYSTEM/COMPONENT_REGISTRY.md` (checklist)
- **Defect:** the Handbook prescribes a horizontal tab strip and UI §10.6 supplies a carousel, while UI Rule Zero and the Registry checklist forbid horizontal scroll at any width.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):** the prohibited condition is defined as unintended viewport or content overflow. Contained scrolling is permitted, with reachable controls and keyboard behavior specified.
- **Preserve:** the no-overflow intent; the mobile transforms (tab strip, carousel).
- **Likely affected docs / consumers:** GDSH, UI_UX, REGISTRY.
- **Verification intent:** the rule text distinguishes overflow from contained scroll, and the tab and carousel patterns pass the literal checklist.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Prohibit unintended horizontal overflow of the viewport or content. A contained tab strip or carousel may scroll horizontally when all controls remain reachable and keyboard operation is defined. Test the containment and navigation at the supported widths; do not ban the very mobile transforms the design contract prescribes.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:11` — ## ⚡ RULE ZERO — MOBILE-FIRST IS THE FOUNDATIONAL POSTURE; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1339` — #### 10. Developer Experience Tools; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1481` — ## 10. Advanced Design Patterns; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1487` — ### 10.1 CVA (Class Variance Authority); MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1600` — ### 10.2 Design Tokens; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1750` — ### 10.3 Component Catalogue Pattern; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1847` — ### 10.4 Class Ordering Convention; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1899` — ### 10.5 Dark Mode Best Practices; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1948` — ### 10.6 Touch Device Considerations; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:2007` — ### 10.7 The `cn()` Utility; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:2042` — ### 10.8 Quick Reference: Do's and Don'ts; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/COMPONENT_REGISTRY.md:589` — ## 7. Mobile Behavior Reference; MANIFEST ← 5: DESIGNER_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, GLOBAL_DESIGN_SYSTEM_HANDBOOK, UI_UX_BUILDING_MANUAL.
- `05_DESIGN_SYSTEM/GLOBAL_DESIGN_SYSTEM_HANDBOOK.md:64` — ## 5. Layout & responsive (Rule Zero); MANIFEST ← 6: DESIGNER_PLAYBOOK, COMPONENT_REGISTRY, THEME_LIBRARY, THEMING_MANUAL, TOKEN_FILE, UI_UX_BUILDING_MANUAL.

**Touch proposal:** C-082. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-082` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-083 — Cross-references cite section anchors that do not exist

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/06_design_frontend_corrections.md:309`):

- **Certified record:** CF-13 · Severity LOW · Review UNIQUE (Fable) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra none · Fable FBL-D024
- **Evidence:** Fable §7 FBL-D024.
- **Defect surfaces (`0a787cb`):**
  - `05_DESIGN_SYSTEM/THEMING_MANUAL.md` §0, §7, §10
  - `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md` (Lesson 9; Rule Zero-B cross-reference)
  - `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md` §14 (Quick Pattern Lookup)
  - `04_REFERENCE_MANUALS/APP_ARCHITECTURE_MANUAL.md`
  - Targets: `02_PIPELINE_AGENTS/HANDOFF_PACKAGE_PLAYBOOK.md`, `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md`
- **Defect:**
  - THEMING cites five anchors that don't exist: "§Theming Files", "§Designer Handoff", "§Typography", "§shadcn Defaults" and "§Lucide Icons".
  - UI_UX Lesson 9 claims APP_ARCHITECTURE was cross-linked, but it never mentions THEMING.
  - SFP §14 cites a non-existent UI-UX "Component Library" section.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):** every cited section anchor exists, or the citation is retargeted or removed. The THEMING ↔ APP_ARCHITECTURE pairing is made true, or the Lesson 9 claim is corrected.
- **Preserve:** the cross-reference intent.
- **Likely affected docs / consumers:** the surfaces above. Backlog FBL-S003 (an anchor lint) is optional.
- **Verification intent:** a manual or scripted anchor check over these documents finds every cited "§Name" present in its target.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Cross-references identify the actual canonical file and live heading. Use GLOBAL_DESIGN_SYSTEM_HANDBOOK §8 for Designer deliverables, TOKEN_FILE §3 for font wiring, and COMPONENT_REGISTRY §5 for Shadcn primitives. Add the missing APP_ARCHITECTURE reference to THEMING_MANUAL for token architecture. Replace nonexistent section labels only with the verified equivalent, not a guessed anchor.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `05_DESIGN_SYSTEM/THEMING_MANUAL.md:12` — ## 0. Reader's Guide; MANIFEST ← 5: DESIGNER_PLAYBOOK, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEME_LIBRARY, TOKEN_FILE, UI_UX_BUILDING_MANUAL.
- `05_DESIGN_SYSTEM/THEMING_MANUAL.md:218` — ## 7. What This Manual Does NOT Cover; MANIFEST ← 5: DESIGNER_PLAYBOOK, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEME_LIBRARY, TOKEN_FILE, UI_UX_BUILDING_MANUAL.
- `05_DESIGN_SYSTEM/THEMING_MANUAL.md:266` — ## 10. Cross-References; MANIFEST ← 5: DESIGNER_PLAYBOOK, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEME_LIBRARY, TOKEN_FILE, UI_UX_BUILDING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:84` — ## 🎨 RULE ZERO-B — THEMING IS THE SECOND FOUNDATIONAL POSTURE; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:2070` — ## Appendix — Run 001 Lessons That Updated This Manual; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md:1006` — ## 14. Manual Reference Guide; MANIFEST ← 8: APP_FACTORY_BLUEPRINT, FFM_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.
- `04_REFERENCE_MANUALS/APP_ARCHITECTURE_MANUAL.md:783` — ## 7. Component Architecture; MANIFEST ← 3: ECOMMERCE_AND_PAYMENTS_MANUAL, STATE_MANAGEMENT_MANUAL, THEMING_MANUAL.

**Touch proposal:** C-083. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-083` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-084 — Dangling internal reference in DESIGNER_PLAYBOOK (§5.6)

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/06_design_frontend_corrections.md:331`):

- **Certified record:** CF-13 · Severity LOW · Review UNIQUE (Fable) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra none · Fable FBL-D013
- **Evidence:** Fable §7 FBL-D013.
- **Defect surfaces (`0a787cb`):** `02_PIPELINE_AGENTS/DESIGNER_PLAYBOOK.md` §7.
- **Defect:** DESIGNER §7 cites "§5.6 minimum display fields", but §5 has no 5.6.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):** the reference resolves (Fable suggests UI_SPEC §5) or is removed.
- **Preserve:** the "all required elements present" check.
- **Likely affected docs / consumers:** DESIGNER §7.
- **Verification intent:** the citation resolves at the candidate SHA, or it is gone.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** - [ ] All required elements and minimum display fields in the approved UI_SPEC are present; record NOT APPLICABLE only where that contract says so.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `02_PIPELINE_AGENTS/DESIGNER_PLAYBOOK.md:217` — ## 7. Screen-by-Screen Discipline; MANIFEST ← 10: APP_FACTORY_BLUEPRINT, SOFTWARE_FACTORY_PLAYBOOK, ARCHITECT_PLAYBOOK, ENGINEER_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, APP_FACTORY_SKILLS_PLAYBOOK, FFM_PLAYBOOK, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEME_LIBRARY, TOKEN_FILE.

**Touch proposal:** C-084. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-084` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-085 — Skill activation performs `git pull` before its own approval and resume safeguards

**Proposed disposition:** NO-CHANGE. **Authority:** certified correction NO; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/07_skills_doc_governance_corrections.md:32`):

- **Certified record:** CF-15 · Severity HIGH · Review UNIQUE (Astra) · Current-main REMEDIATED — CURRENT MAIN · Correction required NO
- **Reviewer source IDs:** Astra C07-D01 · Fable none
- **Evidence:** Astra C07 §7 C07-D01; Sol C07 (ACCEPT HIGH; class tag "unsafe activation ordering"); QA-5 FC-085 row.
- **Defect surfaces:**
  - At `0a787cb` (defect): `_SKILLS/factory-docs-update/CLAUDE.md` (activation, line 33), `_SKILLS/factory-docs-update/SKILL.md`, `_SKILLS/factory-docs-update/README.md`.
  - At `9c17939` (remediation):
    - `_SKILLS/factory-docs-update/CLAUDE.md` §2 (lines 28–43, "Do not pull")
    - `_SKILLS/factory-docs-update/README.md` (line 23)
    - `_SKILLS/factory-docs-update/sync-engineer/SKILL.md` (Phase 0; post-merge pull at line 144)
    - `_SKILLS/factory-docs-update/sync-engineer/references/TOOL_ROUTING.md` (line 21)
- **Defect (baseline):** activation said to `git pull` main "before anything else", ahead of cargo/resume inspection, branch and dirty-tree checks, and approval.
- **Current-main status:** REMEDIATED — CURRENT MAIN. Every frozen activation surface is corrected.
- **Proposed outcome:** **NO NEW CORRECTION.** The certified value is "Correction required NO".
- **Preserve (regression guard):**
  - No pull during discovery.
  - Seat resolution and advisory-state reading before discovery.
  - The D15a resume switch inside discovery.
  - The only pull is the post-merge Phase 9 sync.
- **Likely affected docs / consumers:** none. Awareness only for any future docs-update family revision (`XB-SKILL`).
- **Verification intent (regression guard only):** whenever the family is next revised, confirm the activation order and the "Do not pull" rule still hold. This package proposes no change.
- **Open decision:** none.
- **Proposed route:** none (no correction).

**Mapping proposal — ENGINEER-PROPOSED:** NO CORRECTION — preserve the certified remediated disposition and verify main’s activation uses fetch/discovery rather than pre-approval pull.

**Regression evidence:** main skill family (not the older review-branch copy): FC-085 family §2 says “Do not pull”; FC-086 sync-engineer Phase 4 says NO PUSH and Phase 5 gates publication; FC-097 README Step 3 and AP-11 identify `_INBOX/`. Certified severity remains unchanged; no correction proposed.

**Search:** query `FC-085` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-086 — Phase 4 pushes before the gate that approves pushing

**Proposed disposition:** NO-CHANGE. **Authority:** certified correction NO; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/07_skills_doc_governance_corrections.md:56`):

- **Certified record:** CF-15 · Severity HIGH · Review UNIQUE (Astra) · Current-main REMEDIATED — CURRENT MAIN · Correction required NO
- **Reviewer source IDs:** Astra C07-D02 · Fable none
- **Evidence:** Astra C07 §7 C07-D02; Sol C07 (ACCEPT HIGH; class tag "push sequencing"); QA-5 FC-086 row.
- **Defect surfaces:**
  - At `0a787cb` (defect): `_SKILLS/factory-docs-update/SKILL.md` (Phase 4 line 100 push; Gate 4 line 107), `_SKILLS/factory-docs-update/README.md`, `_SKILLS/factory-docs-update/references/TOOL_ROUTING.md`.
  - At `9c17939` (remediation):
    - `_SKILLS/factory-docs-update/sync-engineer/SKILL.md` (Phase 4 lines 84–101, no push; Gate 4 line 113; line 115 orders approval record → commit → push)
    - `_SKILLS/factory-docs-update/README.md` (line 40)
    - `_SKILLS/factory-docs-update/sync-engineer/references/TOOL_ROUTING.md` (lines 27, 38)
    - `_SKILLS/factory-docs-update/_shared/references/SHA_AND_PUSH_CONTRACT.md` (lines 7, 35)
- **Defect (baseline):** the Phase 4 local mechanics pushed the branch before Gate 4, which said "Awaiting your APPROVED to push".
- **Current-main status:** REMEDIATED — CURRENT MAIN.
- **Proposed outcome:** **NO NEW CORRECTION.** The certified value is "Correction required NO".
- **Preserve (regression guard):** push only after Gate 4; the D18 publication sequence (CONTENT_SHA → handoff commit → Gate 4 → approval-record commit → single push).
- **Likely affected docs / consumers:** none. Awareness only (`XB-SKILL`).
- **Verification intent (regression guard only):** whenever the family is next revised, confirm Phase 4 contains no push and Gate 4 still precedes the only push.
- **Open decision:** none.
- **Proposed route:** none (no correction).

**Mapping proposal — ENGINEER-PROPOSED:** NO CORRECTION — preserve the certified remediated disposition and verify publication remains after Gate 4 approval.

**Regression evidence:** main skill family (not the older review-branch copy): FC-085 family §2 says “Do not pull”; FC-086 sync-engineer Phase 4 says NO PUSH and Phase 5 gates publication; FC-097 README Step 3 and AP-11 identify `_INBOX/`. Certified severity remains unchanged; no correction proposed.

**Search:** query `FC-086` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-087 — Ripple discovery omits known classes of active dependents (skills, body-only references)

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/07_skills_doc_governance_corrections.md:76`):

- **Certified record:** CF-15 · Severity HIGH · Review UNIQUE (Astra) · Current-main PARTIALLY REMEDIATED · Correction required YES
- **Reviewer source IDs:** Astra C07-D03 · Fable none as primary
- **Evidence:** Astra C07 §7 C07-D03; Sol C07 (ACCEPT HIGH; class tag "propagation/ripple completeness"); QA-5 FC-087 row.
- **Defect surfaces:**
  - Residual at `9c17939`: `MANIFEST.md`. Line 76 says "read its ← row — that's the blast radius"; line 107 lists `APP_FACTORY_SKILLS_PLAYBOOK ← FFM_PLAYBOOK` only.
  - Remediated side at `9c17939`: `_SKILLS/factory-docs-update/CLAUDE.md` D19 (line 132), `_SKILLS/factory-docs-update/_shared/templates/UPDATE_MAP.md` (§I, line 97).
  - Baseline: `_SKILLS/factory-docs-update/SKILL.md` Phase 2, `_SKILLS/factory-docs-update/templates/RIPPLE_MAP.md`.
- **Defect:** at baseline, ripple discovery produced a "definitive touch list" from MANIFEST's header-inverted ← map, with no body-reference or skill-consumer check. The map omits the active skill's declared parent, APP_FACTORY_SKILLS_PLAYBOOK.
- **Current-main status:** PARTIALLY REMEDIATED. v0.8 D19 requires a corpus-wide search with every hit dispositioned and `_SKILLS/` read for awareness. MANIFEST still presents the ← row as the blast radius.
- **Proposed outcome (PROPOSED — not approved):**
  - MANIFEST describes its ← map as the starting candidate set, not the complete blast radius, consistent with DocSet Sync D19.
  - The skill-consumer relation (APP_FACTORY_SKILLS_PLAYBOOK as parent of the docs-update family) is visible to propagation checks, recorded in MANIFEST or explicitly scoped out of the ← map with a pointer to D19.
- **Preserve:**
  - D19 corpus-wide search and disposition; D21 parking.
  - MANIFEST as the bump tool.
  - The header-declared vs body-only provenance distinction.
- **Likely affected docs / consumers:** `MANIFEST.md`, an infrastructure doc whose content and date DocSet Sync D7 updates without archiving; FC-093 (same file, recomputed in the same sync).
- **Verification intent:**
  - MANIFEST no longer calls the ← row the (complete) blast radius.
  - The skill-consumer relation is recorded or explicitly scoped.
  - The edit is consistent with the FC-093 recomputation.
- **Open decision:** none beyond sequencing with FC-093.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** The MANIFEST reverse-dependency table is the header-declared starting candidate set, not the complete propagation surface. Search body references, examples, checklists, templates and read-only skill consumers under DocSet Sync D19. APP_FACTORY_SKILLS_PLAYBOOK governs its skill children; that relationship is outside this table’s header-edge count and remains part of propagation analysis.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `03_BUILD_METHODOLOGY/APP_FACTORY_SKILLS_PLAYBOOK.md:910` — ## 15. Authoring A New Skill — Step By Step; MANIFEST ← 1: FFM_PLAYBOOK.

**Touch proposal:** C-087. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-087` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-088 — Hub→project distribution and release pinning are undefined in live doctrine

**Proposed disposition:** BLOCKED. **Authority:** certified correction YES; package outcome remains proposed. CONDITIONAL: DEC-17 / DEC-18 remainder. 

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/07_skills_doc_governance_corrections.md:198`):

- **Certified record:** CF-14 · Severity MEDIUM · Review CONFIRMED · Current-main PARTIALLY REMEDIATED · Correction required YES
- **Reviewer source IDs:** Astra C07-D06 · Fable FBL-D010 (primary; also related to FC-081)
- **Severity divergence (recorded):** Astra MEDIUM vs Fable HIGH. The certified MEDIUM stands.
- **Evidence:** Astra C07 §7 C07-D06; Sol C07; Fable §7 FBL-D010, §9 row 19, §11 decision 8; QA-5 FC-088 row.
- **Defect surfaces:**
  - At `9c17939` (= `0a787cb`):
    - `MANIFEST.md` (line 10: projects pin `doctrine-YYYY.MM[-patch]`, citing draft spec §2.6)
    - `_OTHERS/DOCTRINE_HUB_DESIGN_v0_1.md` (DRAFT)
    - the five divergent landing-path surfaces: `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md` §15, `05_DESIGN_SYSTEM/COMPONENT_REGISTRY.md` §11, `02_PIPELINE_AGENTS/HANDOFF_PACKAGE_PLAYBOOK.md` §13, `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md` §16/§22, `05_DESIGN_SYSTEM/THEME_LIBRARY.md`
  - Remediated side at `9c17939`: `_SKILLS/factory-docs-update/sync-engineer/SKILL.md` (line 149, Phase 9 step 6), `_SKILLS/factory-docs-update/README.md` (line 67): the tag decision is Tony's, after a real sync and merge.
- **Defect:** MANIFEST tells projects to pin doctrine tags and cites a DRAFT in `_OTHERS/`. No live procedure assigns tag creation, release acceptance or consumer update; no doctrine tag exists locally; and five docs give divergent project-side landing paths.
- **Current-main status:** PARTIALLY REMEDIATED. The tag-decision owner is now named; MANIFEST, the draft spec and the five landing paths are unchanged; `git tag -l` is empty locally (remote not inferred).
- **Proposed outcome (PROPOSED — not approved):**
  - Live doctrine holds a small authoritative release/consumption procedure that states:
    - the responsible owner;
    - the release identity (tag or commit);
    - when merged doctrine becomes releasable;
    - how a project records its pinned identity;
    - the update vs intentional-pin decision;
    - the recovery direction.
  - MANIFEST line 10 points to that procedure or is withdrawn.
  - One project-side landing path is standardized, and the five references are aligned to it.
  - The draft HUB_DESIGN §2.4–2.6 is promoted or explicitly superseded.
  - Automation is optional (Astra).
- **Preserve:**
  - DocSet Sync's rule that the tag decision is Tony's, taken only after a real merged sync.
  - No tag cut from inside a run.
- **Likely affected docs / consumers:**
  - `MANIFEST.md`; the five landing-path docs; a possible NEW CANONICAL DOCUMENT or MANIFEST section; `_OTHERS/` (supersession note).
  - FC-081, FC-003.
  - Cutting the tag is Tony's git action, outside this package.
- **Verification intent:**
  - MANIFEST's pin statement cites a live, non-DRAFT procedure that names its owner.
  - All five landing-path references agree.
- **Open decision:** DEC-17: cut a first doctrine tag now? (Fable §11 decision 8); the landing-path standard; the release owner (Tony).
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** The Director releases a merged, verified doctrine revision. A consuming project records canonical document names, header versions, Hub commit SHA, source paths and its approved landing path. It explicitly chooses update or intentional pin; recovery restores the recorded revision before applying later approved changes. A tag is optional pending the Director’s decision. Do not claim deployment authorization from doctrine distribution.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md:96` — ## 1.5 Doctrine Pairing Principle — Playbooks Paired With Worked Examples; MANIFEST ← 8: APP_FACTORY_BLUEPRINT, FFM_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FRONTEND_BUILD_PHASE_PLAYBOOK.md:41` — ## 1.5 Pre-Phase Doctrine Refresh (MANDATORY Before Every Stage); MANIFEST ← 4: ENGINEER_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, TESTING_PLAYBOOK, UI_UX_BUILDING_MANUAL.

**Touch proposal:** C-088. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-088` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-089 — The mandated outgoing QA_PLAYBOOK v1.0 archive snapshot is absent

**Proposed disposition:** BLOCKED. **Authority:** certified correction YES; package outcome remains proposed. CONDITIONAL: DEC-20. 

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/07_skills_doc_governance_corrections.md:238`):

- **Certified record:** CF-16 · Severity MEDIUM · Review UNIQUE (Astra) · Current-main OPEN — DEFECT REMAINS · Correction required YES
- **Reviewer source IDs:** Astra C07-D05 · Fable none
- **Evidence:** Astra C07 §7 C07-D05; Sol C07; QA-5 FC-089 row.
- **Defect surfaces (`0a787cb` = `9c17939`):**
  - `CHANGELOG.md` (lines 31–32: QA v1.0 then v1.1)
  - `_ARCHIVE/README.md`
  - `_ARCHIVE/QA_PLAYBOOK_v0_1.md` (present)
  - `03_BUILD_METHODOLOGY/QA_PLAYBOOK.md` (live v1.1)
  - Expected-but-absent: `_ARCHIVE/QA_PLAYBOOK_v1_0.md`
  - Contrast at `9c17939`: `_SKILLS/factory-docs-update/CLAUDE.md` D7 (line 106) strengthens archive fidelity for future runs only.
- **Defect:** CHANGELOG records QA v1.0 and then v1.1, and the archive rules require a snapshot before each bump, but there is no v1.0 snapshot.
- **Current-main status:** OPEN — DEFECT REMAINS.
- **Proposed outcome (PROPOSED — not approved):**
  - The missing outgoing snapshot is reconciled against authoritative Git history through this approved correction, by one of:
    - restoring `_ARCHIVE/QA_PLAYBOOK_v1_0.md` byte-equal to the historical v1.0 blob; or
    - recording a documented exception in `_ARCHIVE/README.md` and CHANGELOG.
  - Completion checks verify an archive exists for every recorded bump, including several bumps in one run.
- **Preserve:** archive-on-bump discipline; additions-only archive.
- **Likely affected docs / consumers:** `_ARCHIVE/`, `_ARCHIVE/README.md`, `CHANGELOG.md`; FBL-S014 (optional backlog note on archive coverage bounds).
- **Verification intent:**
  - If restored: `git hash-object _ARCHIVE/QA_PLAYBOOK_v1_0.md` equals the QA_PLAYBOOK.md blob at the commit that carried v1.0 (the DocSet Sync D7 Git-object method).
  - If excepted: the exception entry exists.
- **Open decision:** DEC-20, restore vs documented exception (Tony). Identifying the v1.0 commit needs a history inspection that this package did not perform (GAP).
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Restore the missing QA_PLAYBOOK v1.0 archive only from its identified authoritative Git blob, byte-for-byte. If that identity cannot be established, record an explicit approved exception with the missing bump and evidence. The new outgoing v1.1 snapshot remains a separate required archive; it cannot substitute for v1.0.

**Search:** query `FC-089` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-090 — Required pre-approval evidence writes conflict with absolute no-write rules

**Proposed disposition:** SPLIT. **Authority:** certified correction YES; package outcome remains proposed.  Cross-boundary component: XB-01.

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/07_skills_doc_governance_corrections.md:101`):

- **Certified record:** CF-15 · Severity MEDIUM · Review UNIQUE (Astra) · Current-main PARTIALLY REMEDIATED · Correction required YES
- **Reviewer source IDs:** Astra C07-D07 · Fable none as primary
- **Evidence:** Astra C07 §7 C07-D07; Sol C07 (class tag "bounded pre-approval run-state writes"); QA-5 FC-090 row.
- **Defect surfaces:**
  - Residual at `9c17939` (= `0a787cb`, unchanged): `CLAUDE.md` (root):
    - the Plan Mode "MUST NOT … Write files" list (line 84)
    - "Before EVERY tool call that modifies a file … STOP" (lines 171–175)
    - the mandatory write-before-display session and RESPONSES protocol
  - Remediated side at `9c17939`: `_SKILLS/factory-docs-update/CLAUDE.md` D2 (line 96), D10 (line 112).
- **Defect:** root CLAUDE.md requires PENDING_APPROVAL plans, session files and response artifacts to be written before display or approval, while the same file and the baseline skill D2 forbid all writes before approval, with no scoped exception.
- **Current-main status:** PARTIALLY REMEDIATED. v0.8 D2 separates RUN-STATE / PLANNING writes from CANONICAL writes for skill runs; root CLAUDE.md is unchanged.
- **Proposed outcome (PROPOSED — not approved):**
  - Root CLAUDE.md defines a narrow pre-approval run-state/evidence write surface: session file, `agent_docs/RESPONSES/`, `RECOVERY.md`.
  - That surface is distinct from implementation writes and aligned with DocSet Sync D2's RUN-STATE vs CANONICAL distinction.
- **Preserve:**
  - Write-before-display crash resilience.
  - Plan Mode for implementation work.
  - The D2/D10 skill-local resolution.
- **Likely affected docs / consumers:** root `CLAUDE.md` (`XB-ROOT`); every agent session bootstrapped from it.
- **Verification intent:** root CLAUDE.md contains no absolute write prohibition that conflicts with its own mandatory pre-approval bookkeeping, and the permitted surface is enumerated.
- **Open decision:** DEC-08, root CLAUDE.md status (FC-010, CF-17), and DEC-21, who executes `XB-ROOT` changes.
- **Proposed route:** `XB-ROOT`.

**Mapping proposal — ENGINEER-PROPOSED:** PARKED ROOT JOB — define the narrow pre-approval run-state/evidence surface separately from implementation writes, under DEC-08 and DEC-21.

**No canonical touch row:** separate authorized job required; full intent and preservation retained above. This run does not close the cross-boundary finding.

**Search:** query `FC-090` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-091 — Root recovery resumes historical intent without validating its current identity

**Proposed disposition:** SPLIT. **Authority:** certified correction YES; package outcome remains proposed.  Cross-boundary component: XB-01.

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/07_skills_doc_governance_corrections.md:125`):

- **Certified record:** CF-15 · Severity MEDIUM · Review UNIQUE (Astra) · Current-main OPEN — DEFECT REMAINS · Correction required YES
- **Reviewer source IDs:** Astra C07-D08 · Fable none as primary
- **Evidence:** Astra C07 §7 C07-D08; Sol C07 (class tag "recovery authority hierarchy"); QA-5 FC-091 row.
- **Defect surfaces:**
  - At `9c17939` (= `0a787cb`): `CLAUDE.md` (root). "Read RECOVERY.md first, then session file, then resume" (line 276); before the first user message (line 451); a session template with no revision or approval binding. Also `RECOVERY.md`.
  - Contrast (skill only): `_SKILLS/factory-docs-update/CLAUDE.md` D15a (line 124).
- **Defect:** root CLAUDE.md tells a new session to read RECOVERY and session files and then resume, before reading the user message, with no branch, revision or approval reconciliation.
- **Current-main status:** OPEN — DEFECT REMAINS. D15a's hierarchy binds skill runs only.
- **Proposed outcome (PROPOSED — not approved):**
  - Root recovery treats RECOVERY.md and the session file as advisory pointers.
  - Before resuming, the agent reconciles the current request, branch and revision, dirty tree and approval, reusing D15a's evidence-first hierarchy with explicit task identity.
  - The session template records the base/current revision and an approval-to-revision binding.
- **Preserve:** RECOVERY.md's 3-second recovery value; the session-first discipline; D15a.
- **Likely affected docs / consumers:** root `CLAUDE.md`, `RECOVERY.md` template (`XB-ROOT`).
- **Corroborating observation (this session; INFERENCE, not certified):** at bootstrap on 2026-10-11, RECOVERY.md's top entry still placed the review branch at `3308046` while git showed HEAD `c6210c3`. The discrepancy was found only because git was checked against the memo.
- **Verification intent:** the root recovery section names git and disk as authoritative over the memo, requires reconciliation before resuming, and the template includes revision fields.
- **Open decision:** DEC-08, DEC-21.
- **Proposed route:** `XB-ROOT`.

**Mapping proposal — ENGINEER-PROPOSED:** PARKED ROOT JOB — reconcile request identity, branch, revision, dirty work and approval before resuming; recovery prose remains advisory.

**No canonical touch row:** separate authorized job required; full intent and preservation retained above. This run does not close the cross-boundary finding.

**Search:** query `FC-091` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-092 — Close-out requires inbox/cargo writes excluded by the skill's write boundary

**Proposed disposition:** SPLIT. **Authority:** certified correction YES; package outcome remains proposed.  Cross-boundary component: XB-02.

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/07_skills_doc_governance_corrections.md:145`):

- **Certified record:** CF-15 · Severity MEDIUM · Review UNIQUE (Astra) · Current-main PARTIALLY REMEDIATED · Correction required YES
- **Reviewer source IDs:** Astra C07-D09 · Fable none as primary
- **Evidence:** Astra C07 §7 C07-D09; Sol C07 (class tag "cargo/write-surface handling"); QA-5 FC-092 row.
- **Defect surfaces:**
  - Residual at `9c17939`: `_SKILLS/factory-docs-update/sync-engineer/SKILL.md` (Phase 9 step 3, line 146: stamp "the cargo's home ledger — a project `LESSONS_LEARNED.md`, a package index in its own repo") vs `_SKILLS/factory-docs-update/CLAUDE.md` D10 (line 112) and D21 (line 136).
  - Baseline: `_SKILLS/factory-docs-update/CLAUDE.md` D10, `_SKILLS/factory-docs-update/SKILL.md` close-out.
- **Defect:** at baseline, close-out required `_INBOX/` writes and ENCODED stamps outside the D10 boundary. At main, `_INBOX/` disposition is authorized, but the home-ledger stamp in another repository is not, and D21 makes every other repository read-only during a sync.
- **Current-main status:** PARTIALLY REMEDIATED.
- **Proposed outcome (PROPOSED — not approved):** Phase 9 and D10/D21 agree. The cargo home-ledger stamp is removed from the sweep, named as a separately permissioned cross-repository write, or converted into a parked `XB-` follow-up.
- **Preserve:**
  - The `_INBOX/` disposition authority.
  - RUN_SUMMARY disposition stamps.
  - D21's cross-repository read-only rule.
- **Likely affected docs / consumers:** the docs-update family (`XB-SKILL`); project lessons files (`XB-EXT`).
- **Verification intent:** every write the sweep requires is inside D10's enumerated surface or is an explicitly parked `XB-` item.
- **Open decision:** DEC-21, the Skills Playbook job owner.
- **Proposed route:** `XB-SKILL`.

**Mapping proposal — ENGINEER-PROPOSED:** PARKED SKILL JOB — reconcile the permitted write boundary with inbox disposition at closeout; preserve D11 durable evidence and authorized cleanup.

**No canonical touch row:** separate authorized job required; full intent and preservation retained above. This run does not close the cross-boundary finding.

**Search:** query `FC-092` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-093 — MANIFEST's declared live-doc count and index data disagree with its own contents

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/07_skills_doc_governance_corrections.md:264`):

- **Certified record:** CF-16 · Severity MEDIUM · Review CONFIRMED · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C07-D04 · Fable FBL-D009 (primary)
- **Severity divergence (recorded):** Astra MEDIUM vs Fable LOW. The certified MEDIUM stands.
- **Evidence:** Astra C07 §7 C07-D04; Sol C07; Fable §7 FBL-D009.
- **Defect surfaces (`0a787cb`):**
  - `MANIFEST.md`:
    - "29 live docs" at lines 6, 12, 76
    - FFM→BLUEPRINT edge as header-declared (line 83) and body-only (line 125)
    - "27 bodies" at line 114
    - header still v1.0 / 2026-07-12
  - `CHANGELOG.md`: "Ongoing entries" table has no header row.
  - Cross: `01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md`, `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md`, `03_BUILD_METHODOLOGY/FRONTEND_BUILD_PHASE_PLAYBOOK.md`.
  - Process evidence: `agent_docs/RESPONSES/response_2026-08-10_194109_phase2-ripple-map.md` (at `0a787cb`).
- **Defect:**
  - MANIFEST claims 29 live docs while listing 31 tier files.
  - One edge is both declared and undeclared.
  - The appendix scope is stale.
  - The index header was never re-dated, and CHANGELOG's ongoing table lacks a header row.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - MANIFEST totals and reverse edges are recomputed from one declared source; there are 31 live tier docs at baseline, re-counted at the candidate SHA.
  - The FFM→BLUEPRINT edge is classified exactly once.
  - The body-only appendix is dated and scoped.
  - The MANIFEST header date is current.
  - CHANGELOG's ongoing table has a header row.
- **Preserve:**
  - The correct forward index and version/date agreement.
  - The honest nonstandard-header footnote.
  - BIM's valid "Governed by" exception (Astra).
- **Likely affected docs / consumers:** `MANIFEST.md`, `CHANGELOG.md`; the lints (they read canonical names from MANIFEST); FC-087 (same file).
- **Sync interaction:** DocSet Sync D7 treats a stale pre-existing count as BASELINE DRIFT that it must park unless approved intake authorizes the repair. Once approved, this correction is that authorization.
- **Verification intent:**
  - The count equals the number of tier `.md` files at the candidate SHA.
  - Every ← edge derives from a forward header row or is a marked exception.
  - No edge is both declared and undeclared.
  - CHANGELOG's ongoing table renders with a header.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Recompute live-doc totals and reverse edges from canonical tier headers. Count templates separately through their owning playbook. Date and scope the body-reference appendix, classify FFM→BLUEPRINT once, and include the missing ongoing CHANGELOG table header. Index values are derived from disk, never manually asserted.

**Search:** query `FC-093` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-094 — Root CLAUDE.md prescribes a CHANGELOG record format that competes with CHANGELOG's own

**Proposed disposition:** SPLIT. **Authority:** certified correction YES; package outcome remains proposed.  Cross-boundary component: XB-01.

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/07_skills_doc_governance_corrections.md:304`):

- **Certified record:** CF-16 · Severity LOW · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C07-D10 · Fable none as primary
- **Evidence:** Astra C07 §7 C07-D10; Sol C07.
- **Defect surfaces (`0a787cb`):**
  - `CLAUDE.md` (root): Changelog Protocol, `## YYYY-MM-DD HH:MM UTC — [CC]` headings with Updated/Reason bullets
  - `CHANGELOG.md`: gate-ledger row format, lines 6 and 22
- **Defect:** the two documents govern the same artifact with different record shapes and provenance fields.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):** root CLAUDE.md points to CHANGELOG's own ledger format and separates session/response timestamps from the repository change ledger.
- **Preserve:** the CHANGELOG gate-ledger row format with IDs, which DocSet Sync D7 step 4 depends on.
- **Likely affected docs / consumers:** root `CLAUDE.md` (`XB-ROOT`); every agent that loads it.
- **Corroborating observation (this session; INFERENCE, not certified):** this package followed the Director instruction to leave CHANGELOG unchanged, which overrides the root Changelog Protocol's instruction to log documentation changes there. A live instance of the competing-instruction problem.
- **Verification intent:** root CLAUDE.md contains no CHANGELOG format that differs from CHANGELOG's own.
- **Open decision:** DEC-08, DEC-21.
- **Proposed route:** `XB-ROOT`.

**Mapping proposal — ENGINEER-PROPOSED:** PARKED ROOT JOB — make the root changelog instruction point to the governed CHANGELOG ledger format; do not add a competing format.

**No canonical touch row:** separate authorized job required; full intent and preservation retained above. This run does not close the cross-boundary finding.

**Search:** query `FC-094` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-095 — The skill promises CI "on every push", which the workflow does not cover

**Proposed disposition:** SPLIT. **Authority:** certified correction YES; package outcome remains proposed.  Cross-boundary component: XB-02.

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/07_skills_doc_governance_corrections.md:164`):

- **Certified record:** CF-15 · Severity LOW · Review UNIQUE (Astra) · Current-main OPEN — DEFECT REMAINS · Correction required YES
- **Reviewer source IDs:** Astra C07-D11 · Fable none as primary
- **Evidence:** Astra C07 §7 C07-D11; Sol C07; QA-5 FC-095 row.
- **Defect surfaces:**
  - At `9c17939`: `_SKILLS/factory-docs-update/CLAUDE.md` D9 (line 110).
  - At `9c17939` (= `0a787cb`): `.github/workflows/doctrine-lint.yml` (lines 3–7: push to `main`, pull requests to `main`).
- **Defect:** D9 says the Hub's lints run in CI "on every push and PR", but the workflow triggers only on pushes to `main` and PRs targeting `main`.
- **Current-main status:** OPEN — DEFECT REMAINS.
- **Proposed outcome (PROPOSED — not approved):** D9 states the actual CI triggers and names the required local pre-push validation separately. Alternatively, the workflow triggers are changed in a separate CI job.
- **Preserve:** D9's run-lints-locally-before-commit discipline and baseline honesty.
- **Likely affected docs / consumers:** the docs-update family (`XB-SKILL`); if triggers change, `.github/` (`XB-LINT/CI`); FC-096.
- **Verification intent:** the skill's CI wording matches the workflow's `on:` block at the candidate revision.
- **Open decision:** DEC-16, fix the wording vs extend the triggers (Fable FBL-S003 suggests running on every branch; optional backlog).
- **Proposed route:** `XB-SKILL` (+ `XB-LINT/CI` if triggers change).

**Mapping proposal — ENGINEER-PROPOSED:** PARKED SKILL JOB — describe the actual CI triggers. The approved wording correction does not authorize expanding CI triggers.

**No canonical touch row:** separate authorized job required; full intent and preservation retained above. This run does not close the cross-boundary finding.

**Search:** query `FC-095` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-096 — The doctrine lint suite fails at baseline, and the documented process merges over red CI

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  Cross-boundary component: XB-02 / XB-03.

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/07_skills_doc_governance_corrections.md:321`):

- **Certified record:** CF-16 · Severity HIGH · Review CONFLICT · Current-main OPEN — DEFECT REMAINS · Correction required YES
- **Reviewer source IDs:** Astra none as a defect (C07 §5 Strength 6 evaluates the same practice favourably) · Fable FBL-D002
- **Sol adjudication (certified):** ACCEPT DEFECT (2026-09-27): "Honest handling of known pre-existing lint failures is worth preserving, but a drift-killing CI control that is permanently red and explicitly non-blocking cannot reliably serve as a gate."
- **Evidence:** Fable §7 FBL-D002, §11 decision 10; Astra C07 §5 item 6; register §7.1; QA-5 FC-096 row and lint output.
- **Defect surfaces:**
  - At `0a787cb` = `9c17939`:
    - `lints/run_all.py`, `lints/versioned_refs_lint.py`, `lints/header_lint.py`
    - `.github/workflows/doctrine-lint.yml`
    - the flagged docs: `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md` (lines 1, 258, 261, 688, 690, 692), `04_REFERENCE_MANUALS/DATABASE_MANUAL.md` (lines 8, 156), `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md` (line 2092)
  - At `9c17939`: `_SKILLS/factory-docs-update/README.md` (line 60, "merge anyway"), `_SKILLS/factory-docs-update/sync-engineer/SKILL.md` (line 136).
  - Process evidence: `agent_docs/RESPONSES/response_2026-08-10_200500_gate4-precheck.md` (at `0a787cb`).
- **Defect:** `lints/run_all.py` exits 1 at baseline, with 8 VERSIONED-REFS hits and 1 HEADER-PRESENCE miss. The documented process merges over that red, so the "drift-killer" cannot tell new drift from the known set.
- **Current-main status:** OPEN — DEFECT REMAINS. The lint rerun on 2026-10-11 (this session, read-only) reproduced exit 1 with the same 8 + 1 findings, identical to the certified record.
- **Proposed outcome (PROPOSED — not approved):**
  - **Recommended:** clear all nine known findings, then require `lints/run_all.py` to exit 0. The findings are:
    - six STARTER_KIT findings via FC-003;
    - two prose references in DATABASE;
    - one filename reference in UI_UX.

    With zero known findings, any red result means new drift, and CI works as a real gate. This path needs no change to the lint scripts or CI workflow. Making a green result a merge requirement is a branch-protection / governance setting owned by Tony.
  - **Alternative (UNAPPROVED option, kept only for Tony's choice): a baseline-aware gate.** Acceptable only if all of these hold:
    1. A reviewed, approved baseline lists exactly the known findings.
    2. The gate passes, meaning zero findings outside that approved baseline, i.e. zero unapproved new findings.
    3. Any finding outside the baseline fails the gate.
    4. Changes to the baseline need approval.

    Implementing this needs a separately approved `XB-LINT/CI` job. **This package does not modify lint scripts or CI.**
  - Under either path:
    - honest reporting is kept, with no exemption patterns added to hide findings (DocSet Sync D9, AP-5);
    - the skill text stops instructing merge-over-red.
- **Preserve:**
  - D9's "never exempted" baseline discipline.
  - Honest lint reporting (Sol C07).
  - The introduced-vs-pre-existing distinction.
- **Likely affected docs / consumers:**
  - The three flagged docs (`SYNC`).
  - The skill README/SKILL merge-over-red text (`XB-SKILL`).
  - `lints/` and `.github/` **only if** the baseline-aware alternative is approved (`XB-LINT/CI`).
  - Branch-protection settings (Tony; governance outside the package).
- **Verification intent:**
  - **Recommended path:** `PYTHONDONTWRITEBYTECODE=1 python3 -B lints/run_all.py` exits 0 at the candidate SHA. The nine known findings are gone and there are zero new findings.
  - **Alternative path (only if approved instead):** the baseline-aware gate passes at the candidate SHA with zero unapproved new findings. The `XB-LINT/CI` job shows that a finding outside the approved baseline fails the gate.
  - **Both paths:**
    - no exemption pattern is added;
    - the skill README/SKILL text no longer instructs merging over red;
    - the lint scripts and CI workflow are unchanged by the `SYNC` part of this correction.
- **Open decision:** DEC-16 (Fable §11 decision 10; Tony). The choice is between the recommended clear-and-require-exit-0 path and the unapproved baseline-aware alternative. **Sequencing recommendation:** clear the DATABASE and UI_UX findings early, since they are small, and the STARTER_KIT findings via FC-003. Lint red then becomes meaningful for the rest of the campaign.
- **Proposed route:** `SYNC` (doc findings) + `XB-SKILL` (merge-over-red wording) + `XB-LINT/CI` (only if the baseline-aware alternative is approved).

**Mapping proposal — ENGINEER-PROPOSED:** Clear the nine identified documentation lint defects through their mapped canonical corrections, then require lints/run_all.py to exit 0. Do not add exemptions or silently normalize merge-over-red. Changes to skill merge wording, CI policy or branch protection require their separate owners and authorization.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `04_REFERENCE_MANUALS/DATABASE_MANUAL.md:83` — ## 2. Schema Design Patterns; MANIFEST ← 2: API_AND_SERVICES_MANUAL, AUTH_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:2070` — ## Appendix — Run 001 Lessons That Updated This Manual; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md:666` — ## 14. Handbook Maintenance; MANIFEST ← 12: ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, FRONTEND_BUILD_PHASE_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, TESTING_PLAYBOOK, API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, DATABASE_MANUAL, STATE_MANAGEMENT_MANUAL, COMPONENT_REGISTRY, UI_UX_BUILDING_MANUAL.
- `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md:684` — ## 15. Cross-References; MANIFEST ← 12: ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, FRONTEND_BUILD_PHASE_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, TESTING_PLAYBOOK, API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, DATABASE_MANUAL, STATE_MANAGEMENT_MANUAL, COMPONENT_REGISTRY, UI_UX_BUILDING_MANUAL.

**Touch proposal:** C-096. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-096` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-097 — Hub skill supporting files still describe the pre-v0.3 cargo location

**Proposed disposition:** NO-CHANGE. **Authority:** certified correction NO; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/07_skills_doc_governance_corrections.md:180`):

- **Certified record:** CF-15 · Severity LOW · Review UNIQUE (Fable) · Current-main REMEDIATED — CURRENT MAIN · Correction required NO
- **Reviewer source IDs:** Astra none · Fable FBL-D028
- **Evidence:** Fable §7 FBL-D028; QA-5 FC-097 row.
- **Defect surfaces:**
  - At `0a787cb` (defect): `_SKILLS/factory-docs-update/README.md`, `_SKILLS/factory-docs-update/templates/LESSONS_LEARNED.md`, `_SKILLS/factory-docs-update/references/ANTI_PATTERNS.md` (AP-11).
  - At `9c17939` (remediation): `_SKILLS/factory-docs-update/README.md` (line 27), `_SKILLS/factory-docs-update/sync-engineer/templates/LESSONS_LEARNED.md` (line 5), `_SKILLS/factory-docs-update/_shared/references/ANTI_PATTERNS.md` (line 47).
- **Defect (baseline):** the supporting files said cargo goes in the Hub root, while the v0.3 CLAUDE.md and SKILL.md mandated `_INBOX/`.
- **Current-main status:** REMEDIATED — CURRENT MAIN.
- **Proposed outcome:** **NO NEW CORRECTION.** The certified value is "Correction required NO".
- **Preserve (regression guard):** `_INBOX/` as the standing cargo bay, with the repo root as legacy fallback only.
- **Likely affected docs / consumers:** none. Awareness only (`XB-SKILL`).
- **Verification intent (regression guard only):** at the next family revision, confirm all three files still name `_INBOX/`.
- **Open decision:** none.
- **Proposed route:** none (no correction).

**Mapping proposal — ENGINEER-PROPOSED:** NO CORRECTION — preserve the certified remediated disposition and verify main’s family supporting files identify _INBOX as the standing cargo bay.

**Regression evidence:** main skill family (not the older review-branch copy): FC-085 family §2 says “Do not pull”; FC-086 sync-engineer Phase 4 says NO PUSH and Phase 5 gates publication; FC-097 README Step 3 and AP-11 identify `_INBOX/`. Certified severity remains unchanged; no correction proposed.

**Search:** query `FC-097` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### Harvest items — IN-2026-10-15-01…36

The historical harvest is quoted intact; RUL-01…07 supersede only the stated questions. Current adoption and crosswalk follow each item. No historical record is rescored.

#### IN-2026-10-15-01 — WF-01: Seats and human authority

INTAKE-VERBATIM from `factory-intake/01_FACTORY_WORKFLOWS_INTAKE.md:17`:


**Source:** SRC-W05 §2/9/10; SRC-W06 §2/10; SRC-W07 §2/10; later SRC-Q03 §§4–5. **Status:** source-reported rulings plus proposed Factory consolidation. **Correction link:** FC-006, DEC-07.

Define Director/Operator/Coordinator terminology once. One human may occupy Development, QA, DevOps and release-authority chairs; the responsibilities remain distinct. Define Architect, Engineer, QA Lead, QA Executor and DevOps functions by responsibility rather than permanent model assignment. Claudy/Cody/Jarvis/Sol/Fable are contextual occupants, not permission sets.

QA Lead owns the evidence verdict; Director owns scope/access/release decisions. Engineer self-checks remain engineering claims. QA independence requires a separate session/context as applicable; naming the same persona in different seats does not waive independence.

**Preserve:** human release authority; separate QA judgment; Designer function; DevOps responsibility. **Verify:** all rosters, diagrams and module instructions use the same seat vocabulary and identify context-specific exceptions. Avoid importing the old pilot plan's isolated “human QA Lead” phrase as a change from the supplied AI-advisory QA Lead/human Director model.



Mapping: §C shared workflow edits and corresponding FC rows. Ruling interface: RUL-01 mandatory QAM, RUL-02 continuing candidate-based QA branch, RUL-03 required cleanup/production exclusion, RUL-04 frozen contract/writable lanes, RUL-05 two reviews with conditional RRM, RUL-06 owning documents, RUL-07 preservation/tooling boundaries. Unruled content remains conditional under §K. Search: query `WORKFLOW` plus linked FC queries. Verification: source Preserve/Verify requirements, §M and template checks. Source claims of supersession do not authenticate missing historical rulings.

#### IN-2026-10-15-02 — WF-02: Recon before authoring, with an executable boundary

INTAKE-VERBATIM from `factory-intake/01_FACTORY_WORKFLOWS_INTAKE.md:27`:


**Source:** SRC-W05 §3; SRC-W06 §3; SRC-Q03 §8/9. **Status:** existing principle requiring clarification. **Correction link:** FC-014/023, DEC-14.

Require current repository evidence before authoring scope. Disk establishes implementation facts, not permission to change approved requirements. An observed conflict with scope or policy goes to its owner.

Replace absolute “nothing is created” wording with explicit lanes: recon report and normal response/session/recovery bookkeeping; authorized diagnostics that may create build/cache output; and prohibited product/contract modifications. Name permitted diagnostics and cleanup rather than claiming every build is read-only. For pre-authored BIM sets, revalidate each module's assumptions against its actual execution baseline.

**Preserve:** no implementation before approval; no speculative improvement during recon. **Verify:** a fresh Engineer can collect and save the required evidence without violating the same document's no-write rule.



Mapping: §C shared workflow edits and corresponding FC rows. Ruling interface: RUL-01 mandatory QAM, RUL-02 continuing candidate-based QA branch, RUL-03 required cleanup/production exclusion, RUL-04 frozen contract/writable lanes, RUL-05 two reviews with conditional RRM, RUL-06 owning documents, RUL-07 preservation/tooling boundaries. Unruled content remains conditional under §K. Search: query `WORKFLOW` plus linked FC queries. Verification: source Preserve/Verify requirements, §M and template checks. Source claims of supersession do not authenticate missing historical rulings.

#### IN-2026-10-15-03 — WF-03: Planning artifact ownership and timing

INTAKE-VERBATIM from `factory-intake/01_FACTORY_WORKFLOWS_INTAKE.md:37`:


**Source:** SRC-W05 §4/11/12 B-1, B-2, E-1 and §13; SRC-W01. **Status:** DATA_CONTRACT ownership is reported as ruled in the source; UI_SPEC final ownership explicitly remains proposed. **Correction link:** FC-008/015/016/017/019/027, DEC-10/11/12.

Propose a complete producer/consumer/approval table for APP_BRIEF, DATA_CONTRACT, UI_SPEC and any required FILE_TREE. The August model places greenfield DATA_CONTRACT authorship with the Software Architect before Design. Designer receives approved product intent and data shapes, with typed mocks permitted behind the service seam. Do not allow unapproved design fields to become backend requirements by accident.

The source proposes Designer ownership of final UI_SPEC, reviewed by the Architect. Reconcile this with the existing “Architect drafts, Designer revises” contract and decide explicitly. Decide whether FILE_TREE remains mandatory and, if retained, who produces it and when. Distinguish project component manifest from Factory component registry. Resolve pipeline-specific variations instead of forcing incompatible flows into one template.

**Preserve:** approved data contract, design approval, clear artifact status and recipient completeness checks. **Verify:** each required artifact has a real template/producer, no circular handoff, and no unresolved authoring ownership disguised as an approved rule.



Mapping: §C shared workflow edits and corresponding FC rows. Ruling interface: RUL-01 mandatory QAM, RUL-02 continuing candidate-based QA branch, RUL-03 required cleanup/production exclusion, RUL-04 frozen contract/writable lanes, RUL-05 two reviews with conditional RRM, RUL-06 owning documents, RUL-07 preservation/tooling boundaries. Unruled content remains conditional under §K. Search: query `WORKFLOW` plus linked FC queries. Verification: source Preserve/Verify requirements, §M and template checks. Source claims of supersession do not authenticate missing historical rulings.

#### IN-2026-10-15-04 — WF-04: Architect assembles and freezes the integrated FFM

INTAKE-VERBATIM from `factory-intake/01_FACTORY_WORKFLOWS_INTAKE.md:47`:


**Source:** SRC-W05 §4.1–4.4 and amendment B-3; SRC-W01. **Status:** source-reported ruling proposed for consistent propagation. **Correction link:** CF-02/04, FC-025/026, DEC-13.

Return Designer and extraction outputs to the Architect for final assembly, completeness verification and contract freeze before Engineer handoff. The simplified diagram's two streams joining a folder do not eliminate this responsibility.

Retain approved tokens, style tile, screen artifacts, UI_SPEC and component inventory. HTML/PNG obligations apply according to the actual interface/design contract, not indiscriminately to non-visual modules. Preserve the kit infrastructure exception: use complete kit auth primitives directly rather than inventing a redundant project auth service.

Freeze the approved contract; allow declared engineering handoff, QA evidence, rulings and retrospective lanes. A whole-folder immutable rule cannot coexist with required in-folder outputs.

**Verify:** the package contains explicit entry/read order, complete dependencies, approved acceptance requirements and an allowed-output map. Diagram and prose must both show Architect assembly.



Mapping: §C shared workflow edits and corresponding FC rows. Ruling interface: RUL-01 mandatory QAM, RUL-02 continuing candidate-based QA branch, RUL-03 required cleanup/production exclusion, RUL-04 frozen contract/writable lanes, RUL-05 two reviews with conditional RRM, RUL-06 owning documents, RUL-07 preservation/tooling boundaries. Unruled content remains conditional under §K. Search: query `WORKFLOW` plus linked FC queries. Verification: source Preserve/Verify requirements, §M and template checks. Source claims of supersession do not authenticate missing historical rulings.

#### IN-2026-10-15-05 — WF-05: Engineering completion includes handoff

INTAKE-VERBATIM from `factory-intake/01_FACTORY_WORKFLOWS_INTAKE.md:59`:


**Source:** SRC-W05 §§5–6; SRC-W06 §§5–6; SRC-Q03 §§5/8. **Status:** proposed consolidation. **Correction link:** FC-025/026 and CF-02.

Retain Plan Mode, approved scope, bounded implementation, internal checks and self-verification. Acceptance requirements come from the pre-build approved contract. Engineer maintains factual completion claims and may propose errata, but cannot redefine success to fit the implementation.

The original engineering assignment includes the complete QA handoff: candidate reference to be resolved after commit, changed files, environment, reproduction, engineering results, known limitations and factual QAM manifest where applicable. No routine extra mission is needed solely to write that handoff.

**Preserve:** internal Development gates distinct from independent Gate Q; Director Git authority under applicable project rules. **Verify:** QA can reconstruct how to run the candidate and identify which statements are claims rather than independent results.



Mapping: §C shared workflow edits and corresponding FC rows. Ruling interface: RUL-01 mandatory QAM, RUL-02 continuing candidate-based QA branch, RUL-03 required cleanup/production exclusion, RUL-04 frozen contract/writable lanes, RUL-05 two reviews with conditional RRM, RUL-06 owning documents, RUL-07 preservation/tooling boundaries. Unruled content remains conditional under §K. Search: query `WORKFLOW` plus linked FC queries. Verification: source Preserve/Verify requirements, §M and template checks. Source claims of supersession do not authenticate missing historical rulings.

#### IN-2026-10-15-06 — WF-06: BIM campaigns and lifecycle terminology

INTAKE-VERBATIM from `factory-intake/01_FACTORY_WORKFLOWS_INTAKE.md:69`:


**Source:** SRC-W06 §§1/4/5/9; SRC-W04. **Status:** proposed consolidation with glossary reconciliation. **Correction link:** FC-007 and CF-02.

Retain sequenced, bounded BIM work; allow author-all-upfront or plan-names/author-just-in-time when the Director chooses. Execution baseline recon and retrospective learning remain meaningful in both patterns. A pre-authored future module is revalidated when released for execution.

The uploaded model expands BIM as “Backend Integration Module”; other campaign usage includes “Backend Implementation Module.” Reconcile the current Hub glossary and Director usage rather than globally replacing the acronym's expansion from one source. Likewise, distinguish product phases, module internal stages, Factory CREATE/MATURE/OPERATE loops and the proposed review engines. They are different axes, not interchangeable numbering.

**Verify:** one lifecycle crosswalk explains module vs phase vs gate; workflow diagrams do not imply mandatory FFM for every backend-only project.



Mapping: §C shared workflow edits and corresponding FC rows. Ruling interface: RUL-01 mandatory QAM, RUL-02 continuing candidate-based QA branch, RUL-03 required cleanup/production exclusion, RUL-04 frozen contract/writable lanes, RUL-05 two reviews with conditional RRM, RUL-06 owning documents, RUL-07 preservation/tooling boundaries. Unruled content remains conditional under §K. Search: query `WORKFLOW` plus linked FC queries. Verification: source Preserve/Verify requirements, §M and template checks. Source claims of supersession do not authenticate missing historical rulings.

#### IN-2026-10-15-07 — WF-07: QA execution by evidence needs

INTAKE-VERBATIM from `factory-intake/01_FACTORY_WORKFLOWS_INTAKE.md:79`:


**Source:** SRC-W05 §7; SRC-W06 §§7–9; SRC-Q03 §§4/8/17. **Status:** older FFM human-execution rule conflicts with later QAM practice; adoption scope open under ND-01/04.

The August FFM model uses human browser execution and reserves Codex for technical checks. Later RRM reports demonstrate agent browser matrices. Propose that the QA Lead allocates checks according to tool capability, evidence needs and authorized environment. Human product/visual judgment stays where it adds value; repetitive matrices need not default to Tony.

Retain independent plan approval and verdict. Define the active certification branch and cleanup sequence explicitly. The old BIM “abandon QA branch by default” rule is superseded in the supplied RRM/QAM lineage by a forward-moving QA line carrying approved repairs and durable certification records.

**Verify:** QA never edits product code under its execution role, never self-certifies, and never treats automation capability as permission for broader side effects. Do not retroactively reorder an already approved live module.



Mapping: §C shared workflow edits and corresponding FC rows. Ruling interface: RUL-01 mandatory QAM, RUL-02 continuing candidate-based QA branch, RUL-03 required cleanup/production exclusion, RUL-04 frozen contract/writable lanes, RUL-05 two reviews with conditional RRM, RUL-06 owning documents, RUL-07 preservation/tooling boundaries. Unruled content remains conditional under §K. Search: query `WORKFLOW` plus linked FC queries. Verification: source Preserve/Verify requirements, §M and template checks. Source claims of supersession do not authenticate missing historical rulings.

#### IN-2026-10-15-08 — WF-08: DevOps as a shared function

INTAKE-VERBATIM from `factory-intake/01_FACTORY_WORKFLOWS_INTAKE.md:89`:


**Source:** SRC-W07; SRC-W05 §8; SRC-W03. **Status:** proposed owning doctrine, several reported prior rulings. **Correction link:** FC-011, DEC-18.

Use a DevOps contract covering deployment readiness, package authoring, authorized execution, release identity, rollback planning and Gate D evidence. Identify Director, Architect and Engineer responsibilities. Separate QA verdict from release authorization and deployment execution.

The supplied model's Cloud Run package uses `init-app.sh`, `cloudbuild.yaml`, `Dockerfile`, `deploy.sh` and a checklist. Correct the diagram's older filenames if this profile is adopted. These are profile-specific names; do not impose them on Vercel or Python deployments. Classify secrets by build/runtime use and public/server-only exposure, and identify human, build-service and runtime actors.

**Preserve:** no implied cloud authority, exact deployed revision, Gate D separate from build/health checks. **Verify:** platform profiles point to real mechanisms and required approval; version-sensitive technical commands are verified at implementation time, not copied from August as current advice.



Mapping: §C shared workflow edits and corresponding FC rows. Ruling interface: RUL-01 mandatory QAM, RUL-02 continuing candidate-based QA branch, RUL-03 required cleanup/production exclusion, RUL-04 frozen contract/writable lanes, RUL-05 two reviews with conditional RRM, RUL-06 owning documents, RUL-07 preservation/tooling boundaries. Unruled content remains conditional under §K. Search: query `WORKFLOW` plus linked FC queries. Verification: source Preserve/Verify requirements, §M and template checks. Source claims of supersession do not authenticate missing historical rulings.

#### IN-2026-10-15-09 — WF-09: Deployment identity, rollback and redeployment limits

INTAKE-VERBATIM from `factory-intake/01_FACTORY_WORKFLOWS_INTAKE.md:99`:


**Source:** SRC-W07 §§3/6–9/13; SRC-W05 §§8–9. **Status:** proposed correction to overbroad source wording. **Correction link:** CF-14, DEC-17/18.

Record repo → commit → build/image → deployed revision → environment → route/domain identity as applicable. Preserve the tested-product equivalence check through documentation-only successors. Gate D verifies the actual target revision.

Do not generalize “redeploy runs Phase 3 only” without checking changed configuration, secrets, permissions, migrations and deployment prerequisites. Do not promise traffic rollback plus Git revert restores all data or external effects. Require a rollback or recovery plan suited to the changed surfaces, with operator responsibility and evidence.

The source explicitly leaves staging-to-production promotion and monitoring/incident detection incomplete. Record those gaps and scope decisions; do not claim this intake supplies a complete operations manual.



Mapping: §C shared workflow edits and corresponding FC rows. Ruling interface: RUL-01 mandatory QAM, RUL-02 continuing candidate-based QA branch, RUL-03 required cleanup/production exclusion, RUL-04 frozen contract/writable lanes, RUL-05 two reviews with conditional RRM, RUL-06 owning documents, RUL-07 preservation/tooling boundaries. Unruled content remains conditional under §K. Search: query `WORKFLOW` plus linked FC queries. Verification: source Preserve/Verify requirements, §M and template checks. Source claims of supersession do not authenticate missing historical rulings.

#### IN-2026-10-15-10 — WF-10: Context-specific Git and sync authority

INTAKE-VERBATIM from `factory-intake/01_FACTORY_WORKFLOWS_INTAKE.md:109`:


**Source:** SRC-W05 §5.2; SRC-W06 §6; SRC-W07 §2; SRC-W10; existing correction index. **Status:** reconciliation required. **Correction link:** FC-012, DEC-18/21.

Use a context × action × seat matrix. Project engineering's Director-controlled Git/cloud rules do not erase the sync skill's bounded Hub-specific Git exception; the exception does not grant arbitrary project Git/cloud permission. Explicit current task instructions remain controlling: the present folder-preparation task authorizes no Git mutations or full sync.

Project `--no-ff` examples are not universal Hub merge policy. The doc-sync flow must follow the installed skill and Director gates. Include post-merge local main refresh and branch-baseline verification in the appropriate workflow so GitHub merge is not mistaken for local synchronization. Preserve uncommitted work before switching or pulling.



Mapping: §C shared workflow edits and corresponding FC rows. Ruling interface: RUL-01 mandatory QAM, RUL-02 continuing candidate-based QA branch, RUL-03 required cleanup/production exclusion, RUL-04 frozen contract/writable lanes, RUL-05 two reviews with conditional RRM, RUL-06 owning documents, RUL-07 preservation/tooling boundaries. Unruled content remains conditional under §K. Search: query `WORKFLOW` plus linked FC queries. Verification: source Preserve/Verify requirements, §M and template checks. Source claims of supersession do not authenticate missing historical rulings.

#### IN-2026-10-15-11 — WF-11: Review engines, targeted repair and certification

INTAKE-VERBATIM from `factory-intake/01_FACTORY_WORKFLOWS_INTAKE.md:117`:


**Source:** SRC-W08/W09/W11; SRC-R01/RRM_PLAYBOOK.md; current campaign boundary. **Status:** scope decision ND-02; supporting concepts proposed.

The three-engine text proposes per-module build/QA, per-phase review/improvement and final whole-application review. Other later 10X direction described review after all implementation phases. Do not conflate these or automatically add every review stage to mainstream projects. Present the alternatives with their intended scope to Tony.

Where review is approved, preserve the useful sequence: identify/freeze specimen, obtain independent review evidence, adjudicate material findings, approve bounded repairs, verify those repairs and required regression. Original reviewer re-review is conditional on the approved verification plan, not an unqualified rule that every issue requires the same old session.

A review “both PASS” arrow is insufficient to define Gate Q, Gate D or release authority. RRM handles accepted rework; QA certifies the approved contract; Director releases. Define any phase/application certificate separately before using that label.



Mapping: §C shared workflow edits and corresponding FC rows. Ruling interface: RUL-01 mandatory QAM, RUL-02 continuing candidate-based QA branch, RUL-03 required cleanup/production exclusion, RUL-04 frozen contract/writable lanes, RUL-05 two reviews with conditional RRM, RUL-06 owning documents, RUL-07 preservation/tooling boundaries. Unruled content remains conditional under §K. Search: query `WORKFLOW` plus linked FC queries. Verification: source Preserve/Verify requirements, §M and template checks. Source claims of supersession do not authenticate missing historical rulings.

#### IN-2026-10-15-12 — WF-12: One owning document and synchronized visuals

INTAKE-VERBATIM from `factory-intake/01_FACTORY_WORKFLOWS_INTAKE.md:127`:


**Source:** all workflow sources and their amendment ledgers. **Status:** placement proposal ND-05. **Correction link:** CF-13/16, FC-009/087/093.

Determine whether FFM/BIM operating models become separate adopted docs or feed their existing playbooks. A DevOps owning document is a candidate to fill FC-011. Avoid creating two normative explanations with overlapping but conflicting authority. Link specialized RRM and QAM procedure from the general workflow rather than copying their entire contents.

Keep the original diagrams as historical sources. If revised diagrams are in scope, make their source editable and label simplified views clearly; the approved textual contract governs omitted detail. Correct missing recon, Architect assembly, module-close QA, Gate Q/release/Gate D transitions, current seat labels and deployment filenames where relevant. Verify links, headers, indexes and assets under actual Hub conventions.



Mapping: §C shared workflow edits and corresponding FC rows. Ruling interface: RUL-01 mandatory QAM, RUL-02 continuing candidate-based QA branch, RUL-03 required cleanup/production exclusion, RUL-04 frozen contract/writable lanes, RUL-05 two reviews with conditional RRM, RUL-06 owning documents, RUL-07 preservation/tooling boundaries. Unruled content remains conditional under §K. Search: query `WORKFLOW` plus linked FC queries. Verification: source Preserve/Verify requirements, §M and template checks. Source claims of supersession do not authenticate missing historical rulings.

#### IN-2026-10-15-13 — RRM-01: Route accepted findings into a bounded module

INTAKE-VERBATIM from `factory-intake/02_RRM_INTAKE.md:32`:


**Sources:** SRC-R01/RRM_PLAYBOOK.md §§1–4; reviewer candidate; SRC-W08/09. **Status:** pilot procedure proposed for adoption.

Require current-source reconciliation before turning a historical report into a work order. Preserve reviewer IDs, specimen identity, evidence level, uncertainty and limitations. Both reviewers agreeing is not proof; a finding from only one reviewer is not automatically weak. Separate severity, origin and approved scope. An inherited issue may be severe and still require an explicit disposition.

Use ACCEPT REPAIR, NEEDS DECISION/EVIDENCE, DEFER/FUTURE GATE, REJECT/NOT APPLICABLE/ALREADY RESOLVED and DUPLICATE with evidence and reasons. A deferral identifies owner and trigger. Accepted risk requires the Director's recorded decision. Scope comes from accepted objectives, not raw finding counts.

**Preserve:** raw reports unchanged; review timing follows the approved project workflow, not a new universal engine rule. **Verify:** every material finding has a retained identity and disposition; no raw review item silently becomes an authorized edit.



Mapping: §D RRM_PLAYBOOK draft (actual §§1–14). Ruling interface: RUL-01 mandatory QAM, RUL-02 continuing candidate-based QA branch, RUL-03 required cleanup/production exclusion, RUL-04 frozen contract/writable lanes, RUL-05 two reviews with conditional RRM, RUL-06 owning documents, RUL-07 preservation/tooling boundaries. Unruled content remains conditional under §K. Search: query `WORKFLOW` plus linked FC queries. Verification: source Preserve/Verify requirements, §M and template checks. Source claims of supersession do not authenticate missing historical rulings.

#### IN-2026-10-15-14 — RRM-02: Freeze the repair contract before implementation

INTAKE-VERBATIM from `factory-intake/02_RRM_INTAKE.md:42`:


**Sources:** SRC-R01/RRM_PLAYBOOK.md §§4–5; module kit; SRC-R03 campaign report §6. **Correction interface:** FC-013/025/026, DEC-13.

The Architect proposes a module with brief, findings ledger, acceptance requirements, preserved behaviors, permitted surfaces, forbidden scope, environment and verification needs. Director approves. Acceptance exists before build; Engineer may challenge ambiguity through an explicit errata lane, not silently redefine it.

Freeze authority inputs and preserve amendment provenance. Engineering logs, QA artifacts and retrospective outputs remain writable in declared lanes. Mid-flight QAM changes in RRM-004 were recorded as an overlay with append-only rulings; use this as evidence for traceable amendment, not a command to repeat that costly overlay on every future pack.

**Verify:** finding → approved objective → AC → repair → independent result → final disposition can be followed end to end.



Mapping: §D RRM_PLAYBOOK draft (actual §§1–14). Ruling interface: RUL-01 mandatory QAM, RUL-02 continuing candidate-based QA branch, RUL-03 required cleanup/production exclusion, RUL-04 frozen contract/writable lanes, RUL-05 two reviews with conditional RRM, RUL-06 owning documents, RUL-07 preservation/tooling boundaries. Unruled content remains conditional under §K. Search: query `WORKFLOW` plus linked FC queries. Verification: source Preserve/Verify requirements, §M and template checks. Source claims of supersession do not authenticate missing historical rulings.

#### IN-2026-10-15-15 — RRM-03: Establish current baseline and complete preflight

INTAKE-VERBATIM from `factory-intake/02_RRM_INTAKE.md:52`:


**Sources:** SRC-R01 §§2/6; SRC-R03 engineering report §§3/5; SRC-R02 preflight. **Correction interface:** FC-014/022/030, DEC-14.

Inspect current code, dependencies, environment and permissions before authoring/execution. Resolve full baseline identity at the appropriate checkpoint. A placeholder such as “previous module merge” is not sufficient at certification. Keep the candidate separate from docs/evidence successors.

Preflight rows should measure prerequisites relevant to the module: route status, environment reachability, expected identities, supported library access, builds and evidence tools. Avoid unmeasured constants and stale registry claims. Do not mandate an entire scratch implementation by the Architect for every task: validate risky assumptions in proportion to the actual uncertainty.

**Verify:** failure produces a specific blocker before expensive execution; read-only inspection, diagnostics and write boundaries are described truthfully.



Mapping: §D RRM_PLAYBOOK draft (actual §§1–14). Ruling interface: RUL-01 mandatory QAM, RUL-02 continuing candidate-based QA branch, RUL-03 required cleanup/production exclusion, RUL-04 frozen contract/writable lanes, RUL-05 two reviews with conditional RRM, RUL-06 owning documents, RUL-07 preservation/tooling boundaries. Unruled content remains conditional under §K. Search: query `WORKFLOW` plus linked FC queries. Verification: source Preserve/Verify requirements, §M and template checks. Source claims of supersession do not authenticate missing historical rulings.

#### IN-2026-10-15-16 — RRM-04: Prepared engineering run and same-assignment handoff

INTAKE-VERBATIM from `factory-intake/02_RRM_INTAKE.md:62`:


**Sources:** SRC-R01 §§5–6; SRC-R03 report §§3–5; SRC-Q03 §5/8.

Retain Plan Mode and Director-approved rulings. Permit continuous execution through already authorized stages, with bounded self-repairs and enumerated material stops. A new unexpected authority/safety conflict still stops; an incomplete list cannot authorize guessing. Ordinary progress does not require repeated permission prompts.

Finish with changed-file inventory, product/configuration diff, engineering checks, limitations, environment/reproduction instructions and factual QA handoff. If QAM is adopted for that module, complete its manifest. Report unresolved values explicitly; Director commit establishes the immutable candidate.

**Preserve:** narrow scope, no weakening tests to claim green, engineering claims distinct from QA evidence. **Verify:** handoff can enter QA without another prompt asking for basic readiness documents.



Mapping: §D RRM_PLAYBOOK draft (actual §§1–14). Ruling interface: RUL-01 mandatory QAM, RUL-02 continuing candidate-based QA branch, RUL-03 required cleanup/production exclusion, RUL-04 frozen contract/writable lanes, RUL-05 two reviews with conditional RRM, RUL-06 owning documents, RUL-07 preservation/tooling boundaries. Unruled content remains conditional under §K. Search: query `WORKFLOW` plus linked FC queries. Verification: source Preserve/Verify requirements, §M and template checks. Source claims of supersession do not authenticate missing historical rulings.

#### IN-2026-10-15-17 — RRM-05: Independent QA and the QAM interface

INTAKE-VERBATIM from `factory-intake/02_RRM_INTAKE.md:72`:


**Sources:** SRC-R01 §7; SRC-Q03 §§4–8; SRC-R03 QAM authorship opinion.

RRM defines repair objectives and protected behavior. QAM, where approved, packages independent verification; it is not a second engineering module or a replacement scope contract. QA Lead owns plan approval and certification; QA Executor drafts and executes within that approval. Architect supplies risks and scope, Engineer supplies facts, neither pre-grades the independent result.

Tests must reach the boundary claimed. Function probes do not automatically prove HTTP/framework behavior; synthetic data does not establish deployed RLS. Require only the environments/checks justified by the approved contract and risk plan, and report limits honestly. Targeted original-reviewer re-review is used where explicitly required or useful, not to force reopening an unavailable session.



Mapping: §D RRM_PLAYBOOK draft (actual §§1–14). Ruling interface: RUL-01 mandatory QAM, RUL-02 continuing candidate-based QA branch, RUL-03 required cleanup/production exclusion, RUL-04 frozen contract/writable lanes, RUL-05 two reviews with conditional RRM, RUL-06 owning documents, RUL-07 preservation/tooling boundaries. Unruled content remains conditional under §K. Search: query `WORKFLOW` plus linked FC queries. Verification: source Preserve/Verify requirements, §M and template checks. Source claims of supersession do not authenticate missing historical rulings.

#### IN-2026-10-15-18 — RRM-06: Forward certification line and bounded repairs

INTAKE-VERBATIM from `factory-intake/02_RRM_INTAKE.md:80`:


**Sources:** SRC-R01 §§6–8; SRC-Q03 §12; SRC-R03 journals. **Status:** later lineage supersedes the August disposable-branch rule for these campaigns.

Normal pattern: approved main baseline → engineering branch → active QA branch → integration under project policy. After handoff, approved QA-driven repairs stay on the QA line. Engineer repairs; QA Executor measures. Use one active writer when sessions share a worktree.

QA Lead classifies product defect, contract gap, environment blocker, instrument issue or observation. Architect/Director rule actual repair scope; Engineer implements; Director commits; QA re-pins and checks the diff, affected ACs and required regression. Carry forward evidence only with explicit candidate/environment validity reasoning. Helper corrections are logged as instrument events, not disguised product repairs.

**Limit:** RRM-004 did not exercise a product repair round. The generalized QAM repair mechanism remains a proposed procedure until supported by additional evidence. Do not invent a successful Q4 from a zero-repair campaign.



Mapping: §D RRM_PLAYBOOK draft (actual §§1–14). Ruling interface: RUL-01 mandatory QAM, RUL-02 continuing candidate-based QA branch, RUL-03 required cleanup/production exclusion, RUL-04 frozen contract/writable lanes, RUL-05 two reviews with conditional RRM, RUL-06 owning documents, RUL-07 preservation/tooling boundaries. Unruled content remains conditional under §K. Search: query `WORKFLOW` plus linked FC queries. Verification: source Preserve/Verify requirements, §M and template checks. Source claims of supersession do not authenticate missing historical rulings.

#### IN-2026-10-15-19 — RRM-07: Certification, cleanup, closeout and integration

INTAKE-VERBATIM from `factory-intake/02_RRM_INTAKE.md:90`:


**Sources:** SRC-R01 §9; SRC-Q03 §§8/15; SRC-R03 final journal entry. **Correction interface:** DEC-13/18 and CF-14.

Retain the separation of product verdict, cleanup acceptance, pilot verdict, Director adoption, merge and deployment. The older RRM playbook places Gate Q before cleanup; the later approved RRM-004 QAM sequence performs credential cleanup before final certification. Future adopted packs need one explicit sequence; do not paste both instructions without reconciliation.

Keep the smallest sufficient durable evidence set, including cited helpers/failed attempts where needed to explain the verdict. Remove only authorized transient/sensitive items. Verify cleanup did not change product, tests, config or contract. The exact QA Lead certificate must be present or accessible for attributed transcription at closeout.

Record implementation, evidence, closeout and merge identities separately. Do not loop forever adding a commit's own hash to itself. Director controls project Git and release. After merge, refresh local main safely before starting a new branch. Gate D remains separate when deployment is required.



Mapping: §D RRM_PLAYBOOK draft (actual §§1–14). Ruling interface: RUL-01 mandatory QAM, RUL-02 continuing candidate-based QA branch, RUL-03 required cleanup/production exclusion, RUL-04 frozen contract/writable lanes, RUL-05 two reviews with conditional RRM, RUL-06 owning documents, RUL-07 preservation/tooling boundaries. Unruled content remains conditional under §K. Search: query `WORKFLOW` plus linked FC queries. Verification: source Preserve/Verify requirements, §M and template checks. Source claims of supersession do not authenticate missing historical rulings.

#### IN-2026-10-15-20 — RRM-08: One-shot engineering as a scoped option

INTAKE-VERBATIM from `factory-intake/02_RRM_INTAKE.md:100`:


**Sources:** SRC-R03 report §§2–3/7 and RRM-003 field note; SRC-Q03 §16. **Status:** recommendation under ND-07, not a universal standard.

Preserve the useful recipe: prepare measurable scope, validate prerequisites, retain Plan Mode, record rulings, declare human checkpoints and finish the handoff in the same assignment. The demonstrated uninterrupted run covers execution between checkpoints, not preparation, approval, QA, cleanup and merge combined.

Report total lifecycle effort, planned touches, in-run interruptions, helper corrections, product repairs and missing-package follow-ups. Do not optimize a success label by omitting a valid stop. Two clean engineering examples do not justify forcing uncertain architectural work into an unattended run.



Mapping: §D RRM_PLAYBOOK draft (actual §§1–14). Ruling interface: RUL-01 mandatory QAM, RUL-02 continuing candidate-based QA branch, RUL-03 required cleanup/production exclusion, RUL-04 frozen contract/writable lanes, RUL-05 two reviews with conditional RRM, RUL-06 owning documents, RUL-07 preservation/tooling boundaries. Unruled content remains conditional under §K. Search: query `WORKFLOW` plus linked FC queries. Verification: source Preserve/Verify requirements, §M and template checks. Source claims of supersession do not authenticate missing historical rulings.

#### IN-2026-10-15-21 — RRM-09: Reviewer playbook modernization

INTAKE-VERBATIM from `factory-intake/02_RRM_INTAKE.md:108`:


**Source:** SRC-R01/REVIEWER_PLAYBOOK_RRM_PILOT_v0.1.md and RRM_FACTORY_DOCSET_CHANGE_MAP.md. **Status:** candidate adoption; inspect current Hub counterpart before replacement.

The supplied change map asks to distinguish ordinary change review from broad/retrospective investigation; disclose baseline failures without preventing security investigation; separate inherited origin from severity; retain evidence, conditions and falsifiers; route repair through Architect/Director disposition; and avoid unsupported security claims based solely on missing application filters when RLS or another effective boundary may apply.

Do not require three repeated incidents before correcting one severe supported issue. Calibrate claim confidence and specimen equivalence. Keep original reports unchanged; append dispositions/errata. This intake does not approve every sentence in the reviewer candidate verbatim.



Mapping: §D RRM_PLAYBOOK draft (actual §§1–14). Ruling interface: RUL-01 mandatory QAM, RUL-02 continuing candidate-based QA branch, RUL-03 required cleanup/production exclusion, RUL-04 frozen contract/writable lanes, RUL-05 two reviews with conditional RRM, RUL-06 owning documents, RUL-07 preservation/tooling boundaries. Unruled content remains conditional under §K. Search: query `WORKFLOW` plus linked FC queries. Verification: source Preserve/Verify requirements, §M and template checks. Source claims of supersession do not authenticate missing historical rulings.

#### IN-2026-10-15-22 — RRM-10: Owning playbook, kit and references

INTAKE-VERBATIM from `factory-intake/02_RRM_INTAKE.md:116`:


**Source:** SRC-R01 change map and kit; SRC-R03 lessons. **Status:** proposed placement under ND-05.

Create or update one RRM_PLAYBOOK and a compatible module kit. Link general Factory workflow, Architect, Engineer, Handoff, QA and Testing guidance to that owner. Include findings ledger, approved acceptance, front door, plan/build prompts, engineering evidence/handoff, QA references and closeout/retrospective expectations. If QAM is adopted, use its common templates instead of maintaining competing QA procedure copies inside every RRM kit.

Verify actual ACTION/ACTIONS conventions and Hub paths. Separate reusable procedure from the Cyber Pharma worked example. Publish a complete example only after obtaining its actual completed records; source-reported summaries may be used now with attribution and evidence limits.



Mapping: §D RRM_PLAYBOOK draft (actual §§1–14). Ruling interface: RUL-01 mandatory QAM, RUL-02 continuing candidate-based QA branch, RUL-03 required cleanup/production exclusion, RUL-04 frozen contract/writable lanes, RUL-05 two reviews with conditional RRM, RUL-06 owning documents, RUL-07 preservation/tooling boundaries. Unruled content remains conditional under §K. Search: query `WORKFLOW` plus linked FC queries. Verification: source Preserve/Verify requirements, §M and template checks. Source claims of supersession do not authenticate missing historical rulings.

#### IN-2026-10-15-23 — QAM-01: Definition and adoption boundary

INTAKE-VERBATIM from `factory-intake/03_QAM_INTAKE.md:32`:


**Sources:** SRC-Q03 §§1–3/17–20; SRC-Q04 §2. **Status:** proposed adoption ND-01.

QAM packages QA readiness, independent planning, execution, evidence, repair routing, cleanup and review transport. It does not replace the product acceptance contract, invent release authority, or turn every module into an unattended task.

RRM-004 was a specifically approved Cyber Pharma experiment. A report of its success is not blanket authorization for future client migrations, commerce writes or deployments. Propose the reusable playbook now and make its scope/adoption status explicit. Carry experimental state/export/runtime mechanisms as proposals until implemented and evidenced.

**Verify:** the adopted document states who may use which parts, what remains experimental and which governing project contract wins at a live run.



Mapping: §D QAM_PLAYBOOK draft and accepted template installation plan. Ruling interface: RUL-01 mandatory QAM, RUL-02 continuing candidate-based QA branch, RUL-03 required cleanup/production exclusion, RUL-04 frozen contract/writable lanes, RUL-05 two reviews with conditional RRM, RUL-06 owning documents, RUL-07 preservation/tooling boundaries. Unruled content remains conditional under §K. Search: query `WORKFLOW` plus linked FC queries. Verification: source Preserve/Verify requirements, §M and template checks. Source claims of supersession do not authenticate missing historical rulings.

#### IN-2026-10-15-24 — QAM-02: Authorship and five seats

INTAKE-VERBATIM from `factory-intake/03_QAM_INTAKE.md:42`:


**Sources:** SRC-Q03 §§4–5; SRC-Q01 §0/1; SRC-R03 authorship opinion. **Correction interface:** FC-006/025, DEC-07/13.

| Seat | Owns | Must not do under that seat |
|---|---|---|
| Architect | Approved scope, pre-build acceptance, module/QAM skeleton, scope rulings, closeout instructions | Pre-issue independent QA results |
| Engineer | Product implementation, self-tests, factual handoff and manifest | Approve QA plan, grade independent results or certify |
| QA Lead | Standing risks, plan approval, finding classification, retention judgment, certification | Quietly redefine product scope or claim unrun tests |
| QA Executor | Q1 recon, plan draft, independent checks, evidence, review packages and authorized cleanup | Repair product, self-certify or mutate Git without applicable authorization |
| Director | Scope/access decisions, approvals, Git, release and meaningful human judgment | No requirement to perform repetitive agent-capable matrices |

QA may reuse useful engineering tests while deriving independent expectations, inspecting instruments and challenging failure cases. Independence does not require redundant copies of every test. Tool/provider replacement preserves role, approval state and candidate identity. The same worktree has one active writer during repair and measurement.



Mapping: §D QAM_PLAYBOOK draft and accepted template installation plan. Ruling interface: RUL-01 mandatory QAM, RUL-02 continuing candidate-based QA branch, RUL-03 required cleanup/production exclusion, RUL-04 frozen contract/writable lanes, RUL-05 two reviews with conditional RRM, RUL-06 owning documents, RUL-07 preservation/tooling boundaries. Unruled content remains conditional under §K. Search: query `WORKFLOW` plus linked FC queries. Verification: source Preserve/Verify requirements, §M and template checks. Source claims of supersession do not authenticate missing historical rulings.

#### IN-2026-10-15-25 — QAM-03: Package readiness and ownership

INTAKE-VERBATIM from `factory-intake/03_QAM_INTAKE.md:56`:


**Source:** SRC-Q03 §§5–6; SRC-R03 report §4. **Status:** proposed template contract under ND-05.

Architect ships the QAM skeleton with the original engineering pack. Engineer completes factual readiness in the build assignment. The folder becomes ready for recon, not automatically approved for execution. Link to the enclosing frozen acceptance contract instead of creating a second authoritative copy.

Proposed common files: matching CLAUDE.md/AGENTS.md, QAM_ENTRY.md, QAM_MANIFEST.md, QAM_RISK_REQUIREMENTS.md, QAM_PREFLIGHT.md, QAM_TEST_PLAN.md, QAM_PROMPTS.md, QAM_CHECKPOINTS.md; evidence matrix, execution report, cleanup report, artifact inventory and certification record; GOVERNING/, AUTOMATION/, evidence/ and HANDOFFS/ lanes. REPAIR_PROPOSAL.md appears when needed. Pilot charter/results are required for experiments, not gratuitous paperwork on every routine run. QAM_STATE.json is a proposed routing aid, not a delivered runtime or new authority.

Actual generic templates were not included with SRC-Q03 (GAP-03). If authoring them here is approved, label them newly authored and validate pointers/ownership; do not claim byte identity with missing templates.

**Verify:** no fabricated PASS, pre-issued certificate, real credentials or historical fixed candidate in a blank kit; required missing fields are explicit.



Mapping: §D QAM_PLAYBOOK draft and accepted template installation plan. Ruling interface: RUL-01 mandatory QAM, RUL-02 continuing candidate-based QA branch, RUL-03 required cleanup/production exclusion, RUL-04 frozen contract/writable lanes, RUL-05 two reviews with conditional RRM, RUL-06 owning documents, RUL-07 preservation/tooling boundaries. Unruled content remains conditional under §K. Search: query `WORKFLOW` plus linked FC queries. Verification: source Preserve/Verify requirements, §M and template checks. Source claims of supersession do not authenticate missing historical rulings.

#### IN-2026-10-15-26 — QAM-04: Folder-only startup and safe resume

INTAKE-VERBATIM from `factory-intake/03_QAM_INTAKE.md:68`:


**Sources:** SRC-R04 Observation 004; SRC-Q03 §§6–7/14. **Status:** source-reported Director requirement plus proposed implementation.

Both CLAUDE.md and AGENTS.md at each independently launched module entry provide the same role and route to a common instruction body. At the engineering root they assign engineering; under QAM they assign QA Executor. Filename or model name does not change authority.

Entry explains module, repository root, current phase, completed work, candidate, governing versions, approval pointers, permitted paths, next action and output location. A fresh session reads durable records rather than pretending to remember its predecessor. Wrong folder/branch/phase produces useful guidance without automatic switching, resetting or restarting.

Test actual discovery in supported tools. If a runtime needs bootstrap instructions, package them explicitly. A folder pointer starts the permitted recon/resume step; it does not approve all later phases, repair, certification or Git.

**Verify:** first launch, resume, completed module, wrong folder and provider substitution preserve the same role and pending approvals.



Mapping: §D QAM_PLAYBOOK draft and accepted template installation plan. Ruling interface: RUL-01 mandatory QAM, RUL-02 continuing candidate-based QA branch, RUL-03 required cleanup/production exclusion, RUL-04 frozen contract/writable lanes, RUL-05 two reviews with conditional RRM, RUL-06 owning documents, RUL-07 preservation/tooling boundaries. Unruled content remains conditional under §K. Search: query `WORKFLOW` plus linked FC queries. Verification: source Preserve/Verify requirements, §M and template checks. Source claims of supersession do not authenticate missing historical rulings.

#### IN-2026-10-15-27 — QAM-05: Explicit checkpoint sequence

INTAKE-VERBATIM from `factory-intake/03_QAM_INTAKE.md:80`:


**Sources:** SRC-Q03 §8/15; later SRC-Q02/R04 rulings. **Status:** proposed adopted sequence under ND-04.

| Stage | Work | Exit/approval |
|---|---|---|
| Engineering handoff | Facts, diff, reproduction, limitations, manifest | Director commits candidate; QA resolves full identity |
| Q1 | Readiness, independent recon, scope contradictions, draft plan | One review package; QA Lead review |
| Q1b | Record approved plan and any authorized errata | Bind approval to candidate, plan and ruling set; Director releases Q2 |
| Q2 | Continuous approved verification and evidence collection | One package; Lead adjudication |
| Repair/Q4 if needed | Ruled Engineer repair, commit, re-pin, targeted and required regression checks | Lead re-adjudication |
| Q5 | Authorized retention/credential cleanup, identity proof, final package | Lead accepts cleanup/evidence |
| Certification/closeout | Exact Lead certificate, separate pilot result, Architect instructions, Engineer bookkeeping | Director integration/release actions |

No repeated “may I continue?” between already authorized passing checks. No skipped check to preserve one-shot claims. Q5 does not rerun the product board without a concrete reason. Existing approved live modules retain their own sequence until amended through the proper lane.



Mapping: §D QAM_PLAYBOOK draft and accepted template installation plan. Ruling interface: RUL-01 mandatory QAM, RUL-02 continuing candidate-based QA branch, RUL-03 required cleanup/production exclusion, RUL-04 frozen contract/writable lanes, RUL-05 two reviews with conditional RRM, RUL-06 owning documents, RUL-07 preservation/tooling boundaries. Unruled content remains conditional under §K. Search: query `WORKFLOW` plus linked FC queries. Verification: source Preserve/Verify requirements, §M and template checks. Source claims of supersession do not authenticate missing historical rulings.

#### IN-2026-10-15-28 — QAM-06: Preflight and concrete stops

INTAKE-VERBATIM from `factory-intake/03_QAM_INTAKE.md:96`:


**Sources:** SRC-Q03 §9; SRC-R03 report §5; SRC-Q04 stages F/G. **Correction interface:** FC-014/022/030, DEC-14.

Check identity/ancestry, authority pointers, runtime/browser, required network access, authorized target, test roles, trustworthy instruments, writable evidence lanes and permitted side effects. Use bounded probes that answer actual readiness questions. Eighteen historical rows are not a universal minimum.

Q1 may need explicitly authorized builds or login probes; describe these as diagnostics with effects, not magically write-free recon. Revalidate changed/time-sensitive prerequisites at Q2/resume. A failing environment produces a classified blocker with evidence, owner and smallest next action. Do not endlessly retry unavailable credentials or services.

Stop when candidate/approval identity, scope, access, evidence integrity or permitted operations no longer hold. Ordinary instrument correction may continue within its assigned lane and budget. New material uncertainty cannot be ignored merely because a numbered list omitted it.



Mapping: §D QAM_PLAYBOOK draft and accepted template installation plan. Ruling interface: RUL-01 mandatory QAM, RUL-02 continuing candidate-based QA branch, RUL-03 required cleanup/production exclusion, RUL-04 frozen contract/writable lanes, RUL-05 two reviews with conditional RRM, RUL-06 owning documents, RUL-07 preservation/tooling boundaries. Unruled content remains conditional under §K. Search: query `WORKFLOW` plus linked FC queries. Verification: source Preserve/Verify requirements, §M and template checks. Source claims of supersession do not authenticate missing historical rulings.

#### IN-2026-10-15-29 — QAM-07: Credential and browser lifecycle

INTAKE-VERBATIM from `factory-intake/03_QAM_INTAKE.md:106`:


**Sources:** SRC-Q05 Part 1; SRC-Q03 §10; SRC-Q02 later rulings. **Status:** reusable protocol proposal from a scoped pilot, not authorization for a new environment.

Director chooses the environment and supplies authorized dedicated identities. A temporary ignored QA credential file is one adapter; the pilot's exact five keys and ADMIN/MEMBER roles are project examples. Check ignored/untracked state, required key names, target match and authorized authentication without printing values. Respect the actual tool's credential-handling and browser-auth policy; do not bypass MFA or CAPTCHA.

Login can write session/audit state. Business-data writes, emails, payments, role changes and destructive operations need explicit scope. Keep credentials, cookies, tokens, browser storage and raw authenticated traces out of export/evidence. Load required secret values only inside the authorized process.

Under the proposed QAM cleanup sequence: run the applicable value/encoding scan while the credential source is available; remove authorized credential/auth state with evidence; rescan retained output for patterns. On a stopped run, apply the approved pause policy rather than retaining sessions indefinitely. Record Director rotation attestations separately from file deletion. Do not claim a new value scan after deleting the only value source.



Mapping: §D QAM_PLAYBOOK draft and accepted template installation plan. Ruling interface: RUL-01 mandatory QAM, RUL-02 continuing candidate-based QA branch, RUL-03 required cleanup/production exclusion, RUL-04 frozen contract/writable lanes, RUL-05 two reviews with conditional RRM, RUL-06 owning documents, RUL-07 preservation/tooling boundaries. Unruled content remains conditional under §K. Search: query `WORKFLOW` plus linked FC queries. Verification: source Preserve/Verify requirements, §M and template checks. Source claims of supersession do not authenticate missing historical rulings.

#### IN-2026-10-15-30 — QAM-08: Independent instruments and literal grading

INTAKE-VERBATIM from `factory-intake/03_QAM_INTAKE.md:116`:


**Source:** SRC-Q03 §11; SRC-R01 §7; SRC-Q04 §§6/12. **Correction interface:** CF-05, FC-024.

Each AC row links requirement/ruling, expected outcome, observed outcome, candidate/environment, evidence and qualification. Unrun/blocked evidence is not PASS because engineering reported green. Use independent reference derivations and relevant positive/negative/boundary controls. Retain failed instrument attempts and the correction history.

QA helpers may change within authorized lanes to repair measurement. Changes that alter coverage or acceptance meaning need Lead review. Do not change assertions merely to accept unexpected behavior. Direct function probes, synthetic fixtures, runtime HTTP checks, browser interaction and deployed checks support different claims; name the level actually exercised.

Human visual/product judgment remains where the approved plan needs it; repetitive browser matrices can be automated. Permanent regression tests should be selected for durable value rather than converting every exploratory click into a maintained test.



Mapping: §D QAM_PLAYBOOK draft and accepted template installation plan. Ruling interface: RUL-01 mandatory QAM, RUL-02 continuing candidate-based QA branch, RUL-03 required cleanup/production exclusion, RUL-04 frozen contract/writable lanes, RUL-05 two reviews with conditional RRM, RUL-06 owning documents, RUL-07 preservation/tooling boundaries. Unruled content remains conditional under §K. Search: query `WORKFLOW` plus linked FC queries. Verification: source Preserve/Verify requirements, §M and template checks. Source claims of supersession do not authenticate missing historical rulings.

#### IN-2026-10-15-31 — QAM-09: Finding classification and repair

INTAKE-VERBATIM from `factory-intake/03_QAM_INTAKE.md:126`:


**Source:** SRC-Q03 §12; SRC-Q01 §5; SRC-R01 §8.

Classify product defect, contract gap, environment blocker, instrument problem or observation before selecting the owner. Executor proposes; Lead adjudicates; Architect/Director scope product repair; Engineer edits; Director commits; Executor re-pins and measures. A helper fix is not a product repair round.

Retest affected ACs, the actual repair diff and regression required by the approved plan. Reuse unaffected evidence with explicit identity/environment reasoning. Preserve attempts. In a shared worktree, pause QA writes while engineering repairs. RRM-004's clean product run does not prove the Q4 path; later evidence may close this gap, otherwise state it as unvalidated.



Mapping: §D QAM_PLAYBOOK draft and accepted template installation plan. Ruling interface: RUL-01 mandatory QAM, RUL-02 continuing candidate-based QA branch, RUL-03 required cleanup/production exclusion, RUL-04 frozen contract/writable lanes, RUL-05 two reviews with conditional RRM, RUL-06 owning documents, RUL-07 preservation/tooling boundaries. Unruled content remains conditional under §K. Search: query `WORKFLOW` plus linked FC queries. Verification: source Preserve/Verify requirements, §M and template checks. Source claims of supersession do not authenticate missing historical rulings.

#### IN-2026-10-15-32 — QAM-10: Durable evidence and certification

INTAKE-VERBATIM from `factory-intake/03_QAM_INTAKE.md:134`:


**Sources:** SRC-Q03 §§11/15; SRC-R04; SRC-Q02 final entry. **Correction interface:** DEC-13.

Lead selects the smallest durable package that can explain/reproduce the verdict. Preserve issued decisions, necessary helper source, meaningful failed attempts, matrix and provenance. Remove only identified temporary or sensitive items; never blanket-delete a cited evidence tree or unknown process/profile. Prove product/config/test/contract identity is unchanged by cleanup.

Certification names full tested identity, authority versions, results, accepted rulings, package references/hashes, qualifications, cleanup outcome and remaining external actions. Engineer may transcribe the exact Lead text with attribution; a summary or a promise that “the letter was supplied” is insufficient.



Mapping: §D QAM_PLAYBOOK draft and accepted template installation plan. Ruling interface: RUL-01 mandatory QAM, RUL-02 continuing candidate-based QA branch, RUL-03 required cleanup/production exclusion, RUL-04 frozen contract/writable lanes, RUL-05 two reviews with conditional RRM, RUL-06 owning documents, RUL-07 preservation/tooling boundaries. Unruled content remains conditional under §K. Search: query `WORKFLOW` plus linked FC queries. Verification: source Preserve/Verify requirements, §M and template checks. Source claims of supersession do not authenticate missing historical rulings.

#### IN-2026-10-15-33 — QAM-11: Automatic checkpoint review packages

INTAKE-VERBATIM from `factory-intake/03_QAM_INTAKE.md:142`:


**Sources:** SRC-R04 Observations 005–006; SRC-Q03 §13. **Status:** source-reported Director requirement proposed for template propagation.

Each Q1/Q2/Q4/Q5 or material stop needing review produces one indexed package in `QAM/HANDOFFS/` as part of the assignment. Include REVIEW_START_HERE with module, phase/attempt, full candidate and QA HEAD, tree state, time, authorized target label, outcomes, missing material, read order and exact decision requested. Include current authority needed by the recipient, with engineering claims and QA evidence labeled.

Use an explicit file allowlist, preserve relative/original paths, record bytes and SHA-256, exclude the index from its own hash and record final ZIP hash separately. Verify archive paths/integrity and declared scan coverage. Avoid recursive handoffs and secrets/dependency/build/Git directories. Incremental references are acceptable only if the recipient actually has the referenced immutable package; a new reviewer needs the dependency set.

Shared-repository access can use an index in place instead of an unnecessary ZIP. Transport never grants approval. Export does not rerun QA, change a verdict or authorize the next phase.



Mapping: §D QAM_PLAYBOOK draft and accepted template installation plan. Ruling interface: RUL-01 mandatory QAM, RUL-02 continuing candidate-based QA branch, RUL-03 required cleanup/production exclusion, RUL-04 frozen contract/writable lanes, RUL-05 two reviews with conditional RRM, RUL-06 owning documents, RUL-07 preservation/tooling boundaries. Unruled content remains conditional under §K. Search: query `WORKFLOW` plus linked FC queries. Verification: source Preserve/Verify requirements, §M and template checks. Source claims of supersession do not authenticate missing historical rulings.

#### IN-2026-10-15-34 — QAM-12: Honest metrics and separate verdicts

INTAKE-VERBATIM from `factory-intake/03_QAM_INTAKE.md:152`:


**Sources:** SRC-Q03 §16; SRC-Q02 final entry; SRC-R03 campaign report. **Status:** proposed measurement standard.

Record preparation, Q1, review delay, Q2 body and release elapsed, repairs/Q4, cleanup/Q5, Director attention, planned vs unplanned touches, credential entries, instrument corrections and missing-package follow-ups. Mark unknowns and estimates. Measure total effort alongside attractive inner-loop timings.

RRM-004's reported product result is Gate Q PASS, 31 criteria and zero product repairs. Its process verdict remains PARTIAL SUCCESS; Q1 required A-15 scope reconciliation, while Q2 reported zero Director interventions. New experiments may use a clearer component rubric if approved before execution; never rescore the past to improve appearances.



Mapping: §D QAM_PLAYBOOK draft and accepted template installation plan. Ruling interface: RUL-01 mandatory QAM, RUL-02 continuing candidate-based QA branch, RUL-03 required cleanup/production exclusion, RUL-04 frozen contract/writable lanes, RUL-05 two reviews with conditional RRM, RUL-06 owning documents, RUL-07 preservation/tooling boundaries. Unruled content remains conditional under §K. Search: query `WORKFLOW` plus linked FC queries. Verification: source Preserve/Verify requirements, §M and template checks. Source claims of supersession do not authenticate missing historical rulings.

#### IN-2026-10-15-35 — QAM-13: Integration with current DocSet and tooling boundaries

INTAKE-VERBATIM from `factory-intake/03_QAM_INTAKE.md:160`:


**Sources:** SRC-Q03 §§6/18–20; existing correction package. **Status:** new owning playbook/kit proposal ND-05.

Propose one QAM_PLAYBOOK linked from QA_PLAYBOOK, Handoff, Architect, Engineer and applicable module playbooks. Existing QA doctrine remains the owner of Factory-wide independence, verdicts and Gate Q/Gate D unless an approved map explicitly reallocates ownership. Carry governing bodies locally with version/source provenance so the Executor can read what it must obey.

Keep templates aligned with the adopted playbook and module contracts. A generic validator, exporter, state dispatcher, browser adapter or skill implementation is a separately scoped tool deliverable; describing it in a draft is not proof it exists. Do not expand this sync into that engineering project by implication.



Mapping: §D QAM_PLAYBOOK draft and accepted template installation plan. Ruling interface: RUL-01 mandatory QAM, RUL-02 continuing candidate-based QA branch, RUL-03 required cleanup/production exclusion, RUL-04 frozen contract/writable lanes, RUL-05 two reviews with conditional RRM, RUL-06 owning documents, RUL-07 preservation/tooling boundaries. Unruled content remains conditional under §K. Search: query `WORKFLOW` plus linked FC queries. Verification: source Preserve/Verify requirements, §M and template checks. Source claims of supersession do not authenticate missing historical rulings.

#### IN-2026-10-15-36 — QAM-14: Portability, validation and promotion

INTAKE-VERBATIM from `factory-intake/03_QAM_INTAKE.md:168`:


**Source:** SRC-Q03 §§17–20; SRC-Q04 §2. **Status:** proposed promotion policy ND-01.

Reusable core can support RRM, FFM and BIM with different environment/side-effect needs. ABM/APBM adaptations stay on the 10X track. Cyber Pharma examples remain attributed pilot evidence. No module inherits main-dev targeting, login-only permissions or specific browser/runtime behavior from an example.

Proposed template checks include wrong folder/branch, missing authority, unapproved/stale plan, altered lockfile, unavailable target, planted-secret/clean controls, helper vs product defect routing, complete checkpoint exports, missing certificate, bounded cleanup and provider-resume continuity. The master's “two different internal profiles including repair” promotion threshold is a proposal, not an existing mandatory rule or a new blocker imposed here. Bring later validation evidence if available; otherwise distinguish adopted principles from unvalidated mechanisms.



Mapping: §D QAM_PLAYBOOK draft and accepted template installation plan. Ruling interface: RUL-01 mandatory QAM, RUL-02 continuing candidate-based QA branch, RUL-03 required cleanup/production exclusion, RUL-04 frozen contract/writable lanes, RUL-05 two reviews with conditional RRM, RUL-06 owning documents, RUL-07 preservation/tooling boundaries. Unruled content remains conditional under §K. Search: query `WORKFLOW` plus linked FC queries. Verification: source Preserve/Verify requirements, §M and template checks. Source claims of supersession do not authenticate missing historical rulings.

### Supporting intake IN-37…67

These records are not extra correction findings. IN-37 is the Director-approved QAM source, unchanged SHA `97e111e2a495f9a3fe65f50213e6f2ba68c8e5e963f3d23493b1ee99ad35c897`; IN-38 is the 25-file accepted template set. IN-39…45 preserve separate Director, Architect, QA Lead, verification, planning and provenance records. IN-46…67 preserve all 22 original source identities/hashes from SOURCE_INVENTORY, including diagrams and historical pilot packages. Original source files and extracted pilot evidence are never rewritten. Their content is incorporated only through the explicit FC/harvest rows and attributable rulings. Old diagram flows are historical, not competing adopted policy. No new diagram asset is commissioned by this map.

P1 local check: `INTAKE_VERIFICATION.txt` establishes 35/35 addendum members + 24/24 referenced-in-place members and exact folder coverage. This is Cody’s Engineer verification, not an Architect confirmation. The 25 template members match the separately Architect-verified ZIP; the corrected QA decision provenance is preserved outside that historical ZIP.

## C. Exact proposed execution content

Use EXECUTION_PROPOSAL.patch and EXECUTION_PROPOSAL_INDEX.json for complete file-level proposed bytes; 334 ordered content replacements are in SELECTED_EXACT_EDITS.json. PROPOSED_CONTENT contains review copies only. DOCUMENT_VERSION_AND_ARCHIVE_PLAN.json enumerates 31 outgoing originals and proposed version bumps. No change is authorized by file existence here.

Scope represented: 31 revised tier documents, three new playbooks, 25 template translations, 31 exact outgoing archives, one restored historical archive and MANIFEST/CHANGELOG (93 changed paths). FRONTEND_FIRST_PLAYBOOK now has a bounded external-example provenance clarification; its outgoing version is preserved. The original generic paragraphs and broad placement lists are no longer execution instructions; they remain in the preserved previous map.

SELECTED_SCOPE_LEDGER maps every selected component to exact edits, new documents or derived records; external components remain explicitly tracked. Withdrawals retain the certified finding/open dependency until verification supports closure. Metadata/index generation is a proposed mechanical reconciliation, not a claim that all findings are implemented.

## D. New playbooks and accepted templates

NEW_DOCUMENT_PROPOSALS.json identifies the three proposed new playbooks; PROPOSED_CONTENT/03_BUILD_METHODOLOGY contains exact review copies. DRAFTS holds untouched original drafts and substitutions record. RUL-08…15, not the substitutions JSON, provide approval authority.

PHASE_2_TEMPLATE_TRANSLATIONS.json replaces the earlier installation proposal for current review: 25 accepted source files, exact sequential translations and proposed hashes. Accepted source bytes are unchanged in the immutable snapshot. Source acceptance and placement remain settled (AD-01); translation approval and actual installation verification remain pending. Archive restoration is exact in ARCHIVE_RESTORATION_PROPOSAL.json and history only. No source package is retroactively labeled installed. POST_VERIFICATION_STATUS_TRANSITIONS.json supplies the exact five conditional status/provenance edits on four existing proposed paths, executable only after their named actual verification triggers; it is included in Gate 2 scope. EXECUTION_PROPOSAL_INDEX describes the pre-verification proposed bytes, not a completed Active state.

## E. Stale / superseded material

| Material | Proposed treatment | Authority / preservation |
|---|---|---|
| Unsafe auth and client route-guard examples | Archive outgoing canonical documents; remove/quarantine the named unsafe recipes and link governing role/operation rules; kit-specific replacement waits for verified kit evidence | DEC-02; FC-001/033/034/035/036/038/039/041/042. Containment alone does not close all these findings |
| Whole-folder freeze instructions | Replace only frozen-folder claims with frozen-contract / declared-output rules | RUL-04; W03/W04; preserve contract approval |
| Old FFM four-role release implication / handoff omitting QAM | Update complete workflow while preserving Designer/Extractor preparation responsibilities | RUL-01/06; W08…13 |
| Historical disposable QA branch / transfer-back source | Preserve as history in the input snapshot; current prose follows continuing QA line | RUL-02/03; no deletion of evidence or source packages |
| Missing historical QA_PLAYBOOK v1.0 archive | DEC-20 restoration proposal C-M08; not yet performed | Never counterfeit v1.0 from v1.1 |
| Original diagrams and pilot records | Historical input only, unchanged | RUL-07; no revised raster assets or pilot rescore |
| Source templates v0.1/v0.2/v0.3 | Preserve all source folders and verified ZIPs; first canonical installation has no predecessor canonical set to archive | AD-01; future replacement sets use `_ARCHIVE/QAM_TEMPLATES_v<version>/` |

No deletion of existing tracked/untracked work is proposed. Runtime/product debris cleanup rules concern future module execution, not permission to clean this review checkout.

## F. Propagation status

All 2,236 baseline hits have Engineer dispositions: {"CHANGE": 808, "CONSISTENT": 1265, "HISTORY": 123, "OUT-OF-SCOPE": 40}. See PROPAGATION.tsv and PHASE_2_SEMANTIC_REVIEW.md for quotes, boundaries, retained external dependencies and limitations. This is not independent QA or full FC closure. Re-run on actual candidate bytes.

## G. Index and archive proposals

PROPOSED_CONTENT/MANIFEST.md is derived from 34 proposed tier headers, with reverse dependencies and body-only references. Templates are governed via QAM_PLAYBOOK, not extra tier rows. PROPOSED_CONTENT/CHANGELOG.md carries per-document histories/IDs and historical restoration. Thirty-one outgoing archives preserve baseline bytes; QA v1.0 restores blob bb41260f6b6f94372a682f04b313a451f2b3c4b1.

The unchanged lint suite passed on the isolated proposal tree (36 linted documents); PROPOSED_LINT_CHECK.txt contains command, cwd, exit and raw output. This does not certify semantic correctness or change the actual canonical baseline’s nine findings. No lint/CI/skill files are proposed for implementation.

## H. Paths, links and assets

- QAM source `TEMPLATES/QAM/` → Hub `03_BUILD_METHODOLOGY/_templates/QAM/` (AD-01), instantiated as module `QAM/` under project `agent_docs/`.
- Source `QAM_PLAYBOOK_v1_0.md` remains an immutable provenance identifier; live canonical citations use `QAM_PLAYBOOK.md`.
- RECON Q9.4 is an explicit new stable-ID question; Q9.3 is retained unchanged.
- New RRM §2 citation to SFP Engine 1/2 requires W23 before it resolves.
- FC-003/081/083/084 mechanical references follow actual canonical paths/headings. Do not publish a nonexistent external locator or guessed kit revision.
- Template provenance links target the actual snapshot and current translation plan; byte/link checks are recorded. The snapshot is not yet committed; Tony’s preservation receipt is required.
- Original PNG/ZIP sources stay in the snapshot; no new canonical image/asset, image generation, or replacement is proposed.

## I. Skill references — read-only awareness

Main’s DocSet Sync family is the governing workflow. The review-branch skill copy is older and cannot be used to re-open FC-085/086/097. Skills referencing FFM/BIM/QA/Engineer and deployment are consumers, not writable passengers. D5’s Git exception is overridden by Tony’s explicit instruction for this run only; no skill file is changed. The main runbook’s merge-over-red wording and CI claim belong to XB-02 (DEC-16), not this sync’s canonical file edits. `_OTHERS/DOCTRINE_HUB_DESIGN_v0_1.md` remains an unpromoted historical draft; RUL-14 settles current pinning without promoting this unrelated source.

## J. Cross-boundary work and evidence gaps

| ID | Target / associated FCs | Why separate | Blocking effect / recommendation |
|---|---|---|---|
| XB-01 | Root CLAUDE.md / AGENTS.md; FC-008/010/090/091/094 | Outside canonical sync surface; DEC-08/21 | Blocks full closure of root components; recommend a separately authorized root-instruction job; no change now |
| XB-02 | `_SKILLS/**`, including this family; FC-005/006/092/095/096 | Skill authoring job under Skills Playbook | Blocks closure of those skill components; does not prevent coherent canonical rows after explicit scope split; no silent “all 94 closed” |
| XB-03 | lints/, .github/, branch protection | DEC-16 approved green document fixes, not CI trigger expansion | Existing document fixes proceed; governance owner Tony must separately enforce required checks; no baseline-aware gate built |
| XB-04 | Pinned starter-kit repository and external skills/examples; FC-009/041/042/072 | Repository/revision evidence not supplied here | Blocks exact kit signature/session/breakpoint closure. Ask for named kit revision or retain explicit blocked rows; never invent verified exports |
| XB-05 | QAM validator/exporter/dispatcher/browser adapter; ABM/APBM methodology | RUL-07 boundary | Not required to install accepted document templates; separately scoped work only |
| GAP-01 | Doctrine Journal v0.3 / J-19 | CL-11 missing historical source | New Director rulings govern current branch/cleanup policy, but do not authenticate the journal; remove dangling normative dependence only through explicit map substitution |
| GAP-02 | Fully certified pilot example/evidence dossier | Harvest records are limited | No retroactive pilot completion or rescore; generic doctrine may proceed from current rulings |
| GAP-03 | Later historical 10X direction | CL-12 missing | RUL-05 governs present cadence; original historical claim remains unverified |
| GAP-04 | DevOps Architect ruling 2026-08-23 | CL-13 missing | DEC-18 remainder remains open; current source model is not permission |
| GAP-05 | Companion synchronization brief | CL-21 missing | This map supplies current planning; do not claim the missing brief was supplied |
| GAP-06 | Harvest outer-ZIP identity difference | E-8 / CL-29 | Local 75/75 file index is verified; Jarvis’s different ZIP is not reconciled by overwriting either copy; non-blocking for this drafting |

Source intent and preservation for each split FC remain verbatim in §B. “Parked” here means outside this run’s writable boundary, not a Director-approved deferral.

## K. Current decisions, deferrals and engineering gates

# Director rulings — 2026-10-16


Recorded by Cody (Engineer) at 2026-10-16T16:14:02+06:00 from Tony’s instruction “PHASE 1 APPROVED; BEGIN PHASE 2 OF 6”. Tony explicitly approved all eight Jarvis recommendations: **“approve all eight ... i mean your recoms ...”**. The eight supplied decisions below are recorded as Director rulings. Not approval of every alternative in the old map, an unfinished executable map, an unwritten independent specification, or canonical implementation. RUL-08…15 continue the earlier RUL-01…07 IDs.


## RUL-08 — SCOPE

Finish supported canonical Factory-document corrections, mandatory QAM and accepted templates, workflow/branch/cleanup/exclusion reconciliation, and verified reference/lint repairs. Track external kit, root-instruction, skill and CI components separately. Jarvis coordinates follow-ups; name each remaining component, owner and resolving trigger. Do not claim all 97 findings are resolved.


## RUL-09 — ARTIFACT OWNERSHIP

Architect owns DATA_CONTRACT before design; Designer owns UI_SPEC; Architect reconciles the assembled package. FILE_TREE is optional, while implementation structure and boundaries must remain clear. Maintain one canonical template per artifact.


## RUL-10 — DEPLOYMENT

Publish common release, identity, exclusion, verification and recovery requirements. Retain existing context-specific permissions. No new cloud authority is granted. Platform procedures requiring missing evidence remain open.


## RUL-11 — SECURITY AND COMMERCE

Correct supported security guidance and misleading examples now. Defer universal quote-storage and subscription-schema designs. Correct or explicitly withdraw unsafe executable examples; a new warning beside contradictory active instructions is insufficient. Preserve unresolved finding status and dependencies.


## RUL-12 — AUTHORITY AND RECON

Approved project briefs govern scope; governing documents control their respective subjects. Route genuine conflicts for attributable Director resolution. Permit read-only inspection and declared reporting writes. Diagnostic changes require explicit authorization; there is no implicit emergency implementation exception.


## RUL-13 — PERSONAL DATA

Default to no persistent raw contact information in browser storage. Exceptions must specify fields, purpose, retention period and owner, with appropriate clearing/invalidation behavior.


## RUL-14 — HOUSEKEEPING

Identify governing snapshots by canonical document name, header version and Hub commit. Preserve intentional project pins until an authorized update. Put shared terminology in the Factory playbook and reviewer guidance in RRM. Restore the verified historical QA archive as history, not active instructions. Retain certified severities and just-in-time BIM authoring for this run. Do not invent a universal project landing path or require a release tag.


## RUL-15 — EXECUTION AND COMMITS

Execute continuously within a released assignment, including routine checks, reporting and packaging. Stop for concrete blockers, authority changes or required independent verdicts. For THIS SYNC, Tony approves one implementation commit containing the agreed document changes, with per-document histories, preserved originals and verification records. This overrides the sync skill’s one-commit-per-canonical-document requirement for this run only. Necessary preservation, QA repair and closeout commits remain possible. Tony retains ALL Git mutations. Independent QA remains required.


## Decision crosswalk (partial resolution is explicit)


| New ruling | Existing IDs | Effect / remainder |

|---|---|---|

| RUL-08 | DEC-01, DEC-21, XB-01…05 | Supported canonical scope selected; Jarvis coordinates external follow-ups. Root authority classification DEC-08 and external job implementation are not resolved. DEC-09 remains an evidence dependency. |

| RUL-09 | D.2; DEC-10/11/12; WF-03/04 | Ownership, before-design timing, one template and optional FILE_TREE settled. Exact artifact wording/status translation remains map review; no unilateral root edit. |

| RUL-10 | C.2; DEC-18 remainder; FC-011/012/088 | Common deployment requirements selected. No new cloud authority; DevOps occupant, platform procedures and unverified FFM staging permissions remain ungranted/open. |

| RUL-11 | DEC-02/03/04 preserved; DEC-05; K-SUBSCRIPTION-MODEL | Security correction/withdrawal selected; universal quote storage and subscription schema expressly DEFERRED. Project pricing/tax/guest design not supplied; unsafe dependent examples must be corrected coherently or withdrawn. |

| RUL-12 | DEC-06/14; WF-02; RRM-03; QAM-06 | Subject-specific authority, approved-brief scope, inspection/reporting boundaries and no implicit emergency exception settled. Exact prose is still proposed. |

| RUL-13 | DEC-15; FC-040 | Browser raw-contact nonpersistence default and explicit exceptions settled; no invented exception fields/duration. |

| RUL-14 | DEC-07/17/19/20/22; RRM-09; K-ENGINE; K-BIM-SCHEDULE | Shared glossary host, snapshot identity/pins, reviewer host, history restore, certified severities and JIT settled. No universal landing path or required release tag; unavailable external locators remain gaps. Existing RUL-05 supplies review cadence; exact glossary wording remains reviewable. |

| RUL-15 | ND-07; map §N; skill commit rule | Continuous execution within released assignment; run-only single implementation commit approved. No universal workflow outside released scope, no agent Git mutations, no QA waiver; preservation/repair/closeout commits may still occur. |

| All | K-DRAFT-INTEGRATION / K-MAP-FREEZE | Engineering completion and map/spec approval gates remain; these are not policy votes being reopened. |


## Gates
Phase 1 COMPLETE. Phase 2 CURRENT. Scope/intake preparation expressly authorized. Actual intake is recorded separately after byte verification. Gate 2 executable map approval NOT received; independent specification NOT written or approved; Phase 3 NOT released. No historical Active/landed/reconciled claim is adopted by this record.

Policy votes are not reopened. External kit facts, root classification/implementation, skill/CI work, missing platform evidence, and expressly deferred universal quote/subscription designs retain their component status in SELECTED_SCOPE_LEDGER and EXTERNAL_FOLLOWUPS.md. K-MAP-FREEZE and K-DRAFT-INTEGRATION remain engineering/review gates, not resolved by policy approval.

## L. Preservation constraints

All per-ID Preserve bullets in §B are incorporated verbatim and remain testable obligations. Do not conflate baseline severity with later correction status, collapse distinct FC identities, or alter the certified 97/94/3 register. Raw reviews, pilot records, accepted source templates, all ZIPs and staging indexes remain unchanged.

Across auth/data: one authoritative role table; narrow independently authorized creation-time transport; server-resolved first-render identity; RLS user ownership with explicit public-access decisions; schema-first modeling; small/selectively persisted stores; behavioral AUTH-WALK/live-DB evidence beyond a green build.

Across payments/API: separate money truth, permission and entitlement; server-only subscription writers; raw-body signature verification; kit/scope boundaries; server-only secrets; private data uncached; wire/UI type separation; existing negative tests. Keep authentication versus authorization, server execution versus trusted input, authenticity versus processing, deduplication versus ordering, outbound versus inbound idempotency, and mirror versus provider truth distinct.

Preserve Designer/Extractor responsibilities, conversion/greenfield routing, module inheritance from Factory level, Plan Mode, mandatory acceptance contracts, QA independence, exact verdict vocabulary, cleanup and evidence retention, Gate D applicability, and human release authority. Required QAM packaging does not define TRM, import ABM/APBM methodology, authorize tooling or retroactively rewrite already-running modules.

### Verbatim domain-wide preservation — `factory-corrections/04_auth_data_security_corrections.md`

**Domain preservation (Astra C04 §5; Sol C04 §9; applies to every entry below):**
- one authoritative role table, kept separate from profiles, with only the narrow, independently authorized creation-time transport exception
- server-resolved identity on first render (Navbar Law, `{ user, role }` props, the invariant test)
- RLS-enforced user ownership with explicit public-access decisions
- schema-first modeling
- small stores with selective persistence
- behavioral evidence beyond a green build (AUTH-WALK, live DB verification)

Sol C04 §9: corrections must remove stale examples, summaries and helper signatures that contradict the newer rule. Patching one snippet in isolation is not a correction.

### Verbatim domain-wide preservation — `factory-corrections/05_api_commerce_corrections.md`

**Domain preservation (Astra C05 §5; applies to every entry below):**
- explicit money authority kept separate from roles (Stripe truth, Supabase mirror, permission, entitlement)
- the restricted subscription write boundary (owner reads, blocked user writes, server-only writer)
- raw-body Stripe signature verification before dispatch
- the scope and kit-reuse boundaries
- service/data-boundary principles: secrets server-only, private data uncached, wire types separate from UI types
- the negative checks that already exist

Sol C05 §8: keep these concepts separate in every correction:
- authentication vs operation authorization
- server execution vs trusted input
- authenticity vs successful processing
- deduplication vs ordering
- outbound vs inbound idempotency
- mirror vs provider truth

## M. Expected validation and evidence contract

1. Re-hash all immutable intake sources and compare the installed 25 templates to the approved translation plan. Current Engineer integrity checks are in INTAKE_VERIFICATION.txt; independent QA repeats against committed snapshot and candidate.
2. Check FC uniqueness/coverage: 97 records, 94 YES, FC-085/086/097 NO, certified severity B6/H36/M44/L11. Source fields remain unchanged; no source proposal becomes approved without the ruling.
3. Re-run SEARCH_QUERIES over candidate live scope; every CHANGE resolves to approved edits, every retained active hit has defensible disposition, and no new contradiction remains. Check examples, stubs, checklists, handoff/startup instructions, role tables and workflow diagrams, not just new playbooks.
4. Verify mandatory QAM in FFM/BIM/FIX/FEAT/RRM packaging; Architect preparation, Engineer facts, Executor Q1, Lead plan approval, Director release, Q2 and conditional repair/retest, required cleanup, Lead certification and Architect closeout remain distinct. Verify QA branch starts at the exact committed engineering candidate and repairs stay on it.
5. Verify module records under agent_docs and production exclusion by applicable inputs plus actual artifact inspection. The folder name alone and tsconfig alone do not prove exclusion.
6. Verify frozen requirements with declared writable output lanes; no test-plan amendment changes acceptance without approval.
7. Recompute MANIFEST totals, reverse edges and scoped body appendix; compare rows to actual headers and CHANGELOG entries. Derive write/archive counts from approved rows.
8. Run all four existing lints: expected exit 0 after DEC-16 document corrections. No script or CI exemption changes. Preserve raw baseline evidence, not a fictitious baseline PASS.
9. Archive proof: expected outgoing archive blob equals `git rev-parse BASE_SHA:path`; working/staged/committed comparisons use Git-object hashes. The optional historical v1.0 restore uses the separately identified historical blob. Tony performs all staging/commits.
10. Resolve all canonical path/heading references and snapshot/template links. Explicitly verify Q9.4 and SFP Engine definitions before new drafts cite them.
11. Recompute FC-074 contrast from landed HSL, exercise code examples/contract negative cases at the claimed level, and obtain pinned kit evidence before kit-specific closure. This drafting task does not claim runtime/vendor behavior was tested.
12. Fable derives the LARGE acceptance spec from the approved map and standing invariants; Tony approves at Gate 3. Independent fresh-session QA records its own candidate identity. Cody’s drafting checks are not an independent verdict.

Exact raw evidence records include command, working directory, exit code and unfiltered safe output; prevent secret capture at collection rather than trimming failures from the record.

## N. Execution setup and commit plan

Phase 1 COMPLETE; Phase 2 CURRENT. Tony performs ALL Git mutations. Approved run-only override: one implementation commit for agreed document changes, with per-document histories, originals and verification retained. Necessary preservation, QA repair and closeout commits remain possible. No skill rewrite, release tag, universal commit-policy change or QA waiver.

Preserve the review branch; do not merge its older skill copy into main. Inspect refs and scoped changes first. OPERATOR_NEXT_STEPS.md supplies preservation and isolated-worktree commands for Tony. No execution worktree exists yet; current branch/HEAD remain factory-docs-review-astra-w-chunks / 626da8d70f4db22987dc7fcc86765492072360cd. Proposed BASE remains 9c179392f79b70da099121fc357d3107ad3bb86e (local main/origin-main; no fetch by Cody).

Lawful preparation writes: this run’s proposals, immutable intake snapshot, indexes, review evidence and handoff; approved _INBOX copies; session/recovery/response records. Original intake, corrections, drafts, accepted templates and historical ZIP remain untouched. No canonical or Git writes by Cody.

## O. Gates

- Phase 1 scope approval: Tony, 2026-10-16, explicit eight rulings; RUL-08…15 recorded.
- Actual intake/snapshot: copied and byte-verified under Phase 2 authorization; not yet committed.
- Gate 2 executable map: NOT APPROVED; remaining engineering completeness checks cannot be waived by scope approval.
- Independent acceptance specification: Fable derives; NOT authored or approved by Cody. No independent verdict is claimed.
- Phase 3 implementation: NOT RELEASED.

Execution is continuous only within released scope. Stop for concrete blockers, authority changes or required independent verdicts. After eventual map freeze, substantive changes require the governing amendment process; implementation/content identities belong in the handoff, not a retroactively altered frozen map.

## P. Route evidence

| Fast-path condition | Evidence | Holds? |
|---|---|---|
| At most three intake IDs | 97 FCs plus 36 harvest items and supporting source units | NO |
| At most three touched canonical docs | §C enumerates changes across all five tiers | NO |
| No new canonical doc | Three playbooks proposed | NO |
| No Factory-wide terminology/lifecycle change | QAM, seats, branch lifecycle and Engine crosswalk | NO |
| No cross-correction dependencies | Auth, webhook, checkout, artifact ownership and workflow families overlap | NO |
| No high-risk governing rules | Authorization, money authority, QA verdict, release/Git authority | NO |
| No unresolved conflict | §K / external ledger retain evidence-dependent components | NO |
| No cross-boundary requirement for complete outcome | Kit/root/skill portions remain §J; scope split approved by RUL-08; external completion remains separate | NO for full 94-finding closure |
| Bounded complete propagation before freeze | Engineer dispositions and exact selected spans are supplied; independent review and Gate 2 approval remain required | Must be satisfied; not waived |
| Docs-only waiver | Independent review requested and campaign-scale | No waiver proposed |
| **Route** | **LARGE, independent QA after approved map/spec** | **LARGE** |

**Review request:** Jarvis reviews the complete selected wording and scope split; Tony approves the exact map at Gate 2. Fable derives the independent LARGE acceptance specification from that approved map and standing invariants; Tony approves it at Gate 3. Obtain Tony’s preservation/setup receipts and verify baseline equivalence before Phase 3 release. Policy rulings alone approve none of those later gates.
