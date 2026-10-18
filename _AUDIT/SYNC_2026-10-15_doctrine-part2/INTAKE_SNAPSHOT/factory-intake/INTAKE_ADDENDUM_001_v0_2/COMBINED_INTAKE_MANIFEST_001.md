# Combined Intake Manifest 001 (PROPOSED) — Correction Package 001 R3 + Harvest v0.1 + Intake Addendum 001 v0.1

> **PROPOSED MANIFEST — DRAFT / NOT APPROVED.** This is the shape of the Director's intake approval (prerequisite P2 of the dependency map §9), prepared so that the approval can be given in one statement with its DEFERRED items named. It is not that approval. Nothing is placed in `_INBOX/` by this document; no DocSet Sync phase is activated; no Git action is taken or authorized.

| Field | Value |
|---|---|
| Prepared by | Claudy (documentation Engineer seat), 2026-10-14 |
| Basis | DEC-01 (approved form: one coordinated intake and dependency map; split only where justified); dependency map §6 (one campaign, QAM split withdrawn) and §9 (P1–P7); `COMBINED_DECISIONS_001.md` R2; `DIRECTOR_RULINGS_2026-10-14.md` R1.1 |
| Skill revision assumed for the run | `_SKILLS/factory-docs-update/` v0.8-DRAFT at main `9c17939` (or its successor at activation time; re-read then) |
| Preservation | All 97 FC identities, certified fields and totals (index §4) preserved; the five scoped approvals unchanged; harvest IDs unchanged; original sources unchanged |

## 1. The three cargo units

| Unit | Folder on disk today | Files | Status today | Proposed D16 class at Phase 1 (Claudy's expectation; the skill triages aloud) |
|---|---|---|---|---|
| U1 **Correction Package 001 R3** | `factory-corrections/` | 9: index R3, briefs 01–07, `DECISION_RECORD_001.md` | DRAFT — CORRECTION INTAKE / NOT APPROVED FOR SYNC | class 1 APPROVED CORRECTION PACKAGE (after approval); FC IDs as join keys; DEFERRED rows per §3 ride as CONDITIONAL ledger rows |
| U2 **Harvest Package v0.1** | `factory-intake/` (flat): 4 briefs/index, register, 3 JSON indexes, `SOURCES/`, `EXTRACTED/` (75 indexed files + `FILE_INDEX.json`) | 76 | DRAFT FOR INTAKE RECONCILIATION | class 2 intent-level entries for the approved WF/RRM/QAM items; class 3 for the three new documents' content; class 7/8 for sources (map §3.4); class 9 parks for external targets |
| U3 **Intake Addendum 001 v0.2** (v0.1 superseded; preserved, not a drop candidate) | `factory-intake/INTAKE_ADDENDUM_001_v0_2/` + the in-place files it indexes (`../QAM_PLAYBOOK_v1_0.md`, `../PLANNING_001/*` incl. `ARCHITECT_DECISIONS_2026-10-14.md`) | index, manifest (this file), placement recommendation, correction record, QA Lead review entry, file index, `TEMPLATES/QAM/` (25, v0.2-draft) | DRAFT — INTAKE ADDENDUM / NOT APPROVED FOR SYNC (structure accepted by the Architect, AD-00) | playbook: class 3 content + class 7 original; ruling record and Architect decision record: class 7 supporting (authority for intent-level rows and for the template landing path); planning documents: class 7 supporting (no cargo entries; they inform the UPDATE MAP); `TEMPLATES/QAM/`: home decided (AD-01: `03_BUILD_METHODOLOGY/_templates/QAM/`, cargo path translated under D15); **rides only if QA Lead-accepted**; otherwise excluded from the drop and recorded as DEFERRED (affects QAM-03) |

## 2. Proposed `_INBOX/` layout (for drop time; nothing placed now)

```
_INBOX/                                    ← at a Hub clone on main; empty today (does not exist)
├── CORRECTION_PACKAGE_001/                ← U1: the 9 files, byte-identical to the approved revision
├── HARVEST_PART2_v0_1/                    ← U2: the 76 files as extracted (or the as-received ZIP beside them, Director's choice)
└── INTAKE_ADDENDUM_001_v0_2/              ← U3
    ├── 00_ADDENDUM_INDEX.md · COMBINED_INTAKE_MANIFEST_001.md · TEMPLATE_PLACEMENT_RECOMMENDATION.md
    ├── TEMPLATE_CORRECTION_RECORD_001.md · QA_LEAD_REVIEW_ENTRY.md · ADDENDUM_FILE_INDEX.json
    ├── QAM_PLAYBOOK_v1_0.md               ← copy of the unchanged source (hash 97e111e2…5c897 verified at drop)
    ├── PLANNING_001/                       ← rulings R1.1 + Architect decisions (AD-01) + decisions/map/clarifications R3 (supporting records)
    └── TEMPLATES/QAM/                      ← only if QA Lead-accepted (P4a); home decided (AD-01); else omitted
```

Rules at drop time: the skill treats every file in `_INBOX/` as presumptive cargo and a non-empty `_INBOX/` as a RESUME signal (family `CLAUDE.md` §2, D15a), so nothing enters it before P1 and P2 are done; the Director performs the drop and every Git step (global Rule Zero; map §9 P6); Claudy verifies hashes against `ADDENDUM_FILE_INDEX.json`, `FILE_INDEX.json` and the correction package hashes before Phase 1 and records the comparison.

## 3. Unresolved decisions, assessed individually

Categories: **A — required before intake acceptance** (the approval statement cannot be given coherently without it) · **B — resolvable in the formal UPDATE MAP** (Gate 2 presents proposed wording; the Director approves there) · **C — deferred outside this run** (rides as a DEFERRED/CONDITIONAL row; the completion claims it affects are named and stay open). *A deferred dependency never makes a finding "resolved"; the affected FCs and harvest items keep their open status with the deferral recorded.*

| Item | What is undecided | Category | Owner | If deferred: completion claims that stay open |
|---|---|---|---|---|
| P1 | Architect acceptance (or revision) of this addendum as the index of the post-harvest material | **A** | Jarvis | the drop itself |
| P2 | Director intake approval statement for U1 + U2 + U3 as one coordinated intake, naming the DEFERRED rows | **A** | Tony | the drop itself |
| P5 | Working-tree hygiene: commit or keep the uncommitted R1–R3 package edits, `factory-intake/` and bookkeeping on the review branch; the run starts from `main` at a Hub clone | **A** | Tony | the drop (U1 must be byte-identical to an identifiable revision) |
| P6 | Git execution convention for the run (Claudy prints every Git block; the Director runs it) | **Established** (Director-executed Git; not reopened) | Tony | — |
| N-2 (a) | QA Lead acceptance of the `TEMPLATES/QAM/` v0.2 draft's QA behavior (`QA_LEAD_REVIEW_ENTRY.md`) | **A if the set rides in this run; otherwise C** | QA Lead | QAM-03 completion; the mandatory-QAM acceptance check (an Architect cannot instantiate an unaccepted set) |
| N-2 (b) | Home of the template set | **Decided** — AD-01 (Architect under Director delegation): `03_BUILD_METHODOLOGY/_templates/QAM/`; placement and cargo-path translation carried into the UPDATE MAP | Jarvis (done) | — |
| DEC-19 remainder | Kits, worked examples, issue logs, locator | **C** | Tony (Jarvis advises) | RRM-10 kit row; FC-009, FC-003 (locator/kit parts) |
| N-1 | Engine 1 / Engine 2 definitions (SFP §2) | **B** | Jarvis confirms wording; Tony approves at Gate 2 | — |
| N-3, N-4, N-5, N-6, N-7 | Integration wording: retroactivity line; ABM/APBM rows; journal-citation substitution; TRM placeholder; deployment-exclusion row (RECON Q9.3 + DEPLOYMENT_PLAYBOOK) | **B** | Jarvis confirms; Gate 2 | — |
| D.1 (DEC-07 remainder) | Glossary host; Operator/Coordinator as synonyms; no mass rename | **B** (default: synonyms kept, no rename; glossary at SFP §2) | Tony at Gate 2 | if rejected at Gate 2: FC-004, FC-006, FC-007, FC-027 wording rows |
| D.3 (DEC-14) | Recon lanes; named diagnostics; no emergency procedure now | **B** | Tony at Gate 2 | if deferred: FC-014, FC-022, FC-023, FC-029, FC-030; WF-02, RRM-03, QAM-06 diagnostics sentence |
| B.2 (RRM-09) | Reviewer guidance as a section of RRM_PLAYBOOK | **B** | Tony at Gate 2 | if deferred: RRM-09; FC-009 reviewer-artifact part |
| D.2 (DEC-10/11/12) | DATA_CONTRACT timing (confirm B-1/B-2); UI_SPEC owner model A vs **B** (a real change to Hub text); FILE_TREE retire-as-mandatory; one template per artifact; APPROVED/AMENDED vocabulary | **A or C** — a policy change the UPDATE MAP cannot infer; rule it before acceptance or defer it | Tony (Jarvis proposes) | if deferred: FC-008, FC-015, FC-016, FC-017, FC-019, FC-027; WF-03, WF-04 ownership rows |
| C.2 (DEC-18 remainder; ND-06) | DevOps seat occupant/authority; Cloud Run as one platform profile; cloud columns of the context × action × seat matrix; "may the Engineer deploy to staging in FFM runs?" | **A or C** — policy; CL-13 source still missing | Tony (Jarvis advises) | if deferred: **FC-011, FC-012, FC-088**; WF-08, WF-09, WF-10 cloud rows. DEPLOYMENT_PLAYBOOK still lands with placement (RUL-06), the module-Git row (RUL-02) and the deployment-exclusion rule (RUL-03/N-7) |
| E (ND-07) | One-shot engineering as a default (recommended: no; optional prepared run shape) | **C** (or B if Tony rules "no default" at Gate 2) | Tony | RRM-08, QAM-12 one-shot sentence; RRM-04 "continuous execution" sentence. No FC |
| C.3 (DEC-21) | Who executes the `XB-*` jobs and in which job | **C** (parks are non-blocking by design, D21) | Tony | **XB parks stay open**: FC-005/006/096 (skill wording parts), FC-090/091/092/094/095 (root/CI), CF-17; FC-041/042/072 (kit) |
| DEC-05 | Commerce pricing authority: persisted/versioned quote design | **A or C** — gates Wave 1 (BLOCKERs); the certified requirement (server-authoritative pricing, payment/order binding) is unaffected | Tony (Jarvis designs) | if deferred: FC-050, FC-051, FC-060, FC-067 land only to the certified-requirement extent; the quote-design wording stays open |
| DEC-06 | Precedence / reconciliation model and host doc (question-scoped recommended) | **B** | Tony at Gate 2 | if deferred: FC-005, FC-001, FC-029, FC-042, FC-073 |
| DEC-08 | Root `CLAUDE.md`: governed doctrine or tool configuration | **C** (needs the Director's intent; root is `XB-ROOT`) | Tony | FC-010, FC-008 (root reference), FC-090, FC-091, FC-094 |
| DEC-09 / E-10 | Kit disk verification against a named kit repo + revision | **C** (needs kit access) | Tony | **FC-041, FC-042, FC-072** cannot complete in this run |
| DEC-15 | Personal-data retention policy | **C** (policy) | Tony | FC-040 |
| DEC-17 | Doctrine tag now?; project-side landing path; release owner | **A or C** — ties to how projects pin the three new playbooks (QAM-04/13 governing versions) | Tony | if deferred: FC-088, FC-081, FC-003; QAM_PLAYBOOK §2 "versioned local snapshot" cites a tag that does not exist yet (state it as such) |
| DEC-20 | QA_PLAYBOOK v1.0 archive: restore from history or documented exception | **B** (timely: QA_PLAYBOOK is bumped this campaign) | Tony at Gate 2 | if deferred: FC-089 |
| DEC-22 | Optional severity re-elevations (FC-002, FC-037, FC-052, FC-061) | **C** (optional; certified severities kept until ruled) | Tony | none — severities stay certified |
| CL-13 | DevOps Architect ruling of 2026-08-23 (source) | evidence gap, not a decision | Jarvis/Tony supply or rule afresh (C.2) | see C.2 |
| E-8 | Jarvis's confirmation of the outer harvest ZIP hash | evidence gap | Jarvis | none |

## 4. What acceptance would mean, and what it would not

**Would mean:** every FC and every approved WF/RRM/QAM item has a source, status, target intent, preservation requirement and decision route (harvest index §8); the Director has named which rows ride DEFERRED; DocSet Sync Phase 1 may begin at a Hub clone on `main` once the drop is made.

**Would not mean:** that any proposed rule has already landed; that the DEFERRED FCs are resolved (they stay OPEN with the deferral recorded and are reported as such at Gate Q); that the template draft is QA-approved; that any Git action is authorized to this agent; that ABM/APBM, Vibe Engineering or a TRM definition enter the DocSet.

## 5. Preservation statement for the run

| Invariant | Value | Where verified |
|---|---|---|
| FC records / primary entries | 97 / 97 unique | index §4; `validate.py` |
| Correction Families | 17 | index §7.1 |
| BLOCKER / HIGH / MEDIUM / LOW | 6 / 36 / 44 / 11 | index §4 |
| CORRECTION REQUIRED YES / NO | 94 / 3 (FC-085, FC-086, FC-097 regression guards) | index §4 |
| Scoped approvals | DEC-01, DEC-02, DEC-03, DEC-04, DEC-16 — unchanged | `DECISION_RECORD_001.md` §1 |
| Harvest IDs | WF-01…12, RRM-01…10, QAM-01…14, ND-01…07, GAP-01…05, SRC-W/R/Q/C — unchanged | harvest index; map §8 |
| Rulings | RUL-01…07 — verbatim text unchanged in R1.1 | ruling record |
| Sources | all 75 harvest files, the playbook, the archives — byte-identical | `FILE_INDEX.json`, `SOURCE_INVENTORY.json`, `ADDENDUM_FILE_INDEX.json` |

*PROPOSED MANIFEST — DRAFT / NOT APPROVED. For Architect (Jarvis) review; Director (Tony) decides. No synchronization has begun.*
