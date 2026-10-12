# 07 — Skills / Documentation Governance — Correction Brief

> **DRAFT — CORRECTION INTAKE / NOT APPROVED FOR SYNC**

- **Package:** Factory Doctrine Correction Package 001. Index: `FACTORY_DOCTRINE_CORRECTION_INDEX_001.md`.
- **Prepared by:** Claudy (documentation Engineer seat), 2026-10-11. This is not a QA product and certifies nothing.
- **Primary entries:** FC-085 … FC-097 (13), the certified register §5.G. **3 are already remediated on current main** (FC-085, FC-086, FC-097): no new correction, regression guard only. **10 require correction.**
- **Authority:** every outcome is **PROPOSED** for Jarvis (Architect) review and Tony (Director) approval. Nothing here is approved policy.
- **Nature:** these are documentation and governance findings about the Hub's own controls, not about client applications. No replacement doctrine text is written.

## Pinned sources

| Ref | Revision | Path |
|---|---|---|
| Certified register / QA | `c6210c3` = `c6210c32480558b343a27726a26822e8d959d0f7` | `astra-review/run-002/synthesis/PART1_FINDINGS_DISPOSITION.md`, `astra-review/run-002/synthesis/QA/PART1_CONVERGENCE_QA.md` |
| Astra chunk 07 / Sol chunk 07 | `c6210c3` | `astra-review/run-002/chunks/07_skills_doc_governance/ASTRA_REVIEW.md`, `astra-review/run-002/chunks/07_skills_doc_governance/SOL_REVIEW.md` |
| Fable (blind) | `39a1c6114d72b22d3550d7ff65234ec0f01418f6` (`origin/factory-docs-review-fable-001`) | `fable-review/run-001/reviews/FABLE_FACTORY_DOCTRINE_REVIEW_001.md` |
| Review baseline | `0a787cb` = `0a787cb826118b4a010765d60e41a449df3ce746` | v0.3 skill surfaces (`_SKILLS/factory-docs-update/SKILL.md` etc.) and Hub infrastructure |
| Current main | `9c17939` = `9c179392f79b70da099121fc357d3107ad3bb86e` | v0.8-DRAFT skill family (`sync-engineer/`, `sync-qa/`, `_shared/`); main line numbers per certified QA-5 |
| DocSet Sync (read for intake fit) | `9c17939` | `_SKILLS/factory-docs-update/CLAUDE.md`, `_SKILLS/factory-docs-update/README.md` |

Route codes are as in the index.

**Scope boundary for this brief.** DocSet Sync v0.8 §1 declines to update "this family itself", other `_SKILLS/*`, `lints/` or `.github/`. Its synchronized DocSet is the five tier folders plus `MANIFEST.md`, `CHANGELOG.md` and `_ARCHIVE/`, which does not include root `CLAUDE.md`. Every `XB-*` item below therefore needs its own separately approved job (Skills Playbook authoring, lint/CI change, or root-instruction change). A sync run would park it as an `XB-` item (D21).

**Sol C07 preservation rule:** do not weaken stable canonical names, archive discipline, human approval, provenance labels, evidence-first recovery, progressive skill disclosure or honest lint reporting.

---

## CF-15 — Hub sync / recovery / write-boundary mechanics (FC-085, 086, 087, 090, 091, 092, 095, 097)

### FC-085 — Skill activation performs `git pull` before its own approval and resume safeguards
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

### FC-086 — Phase 4 pushes before the gate that approves pushing
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

### FC-087 — Ripple discovery omits known classes of active dependents (skills, body-only references)
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

### FC-090 — Required pre-approval evidence writes conflict with absolute no-write rules
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

### FC-091 — Root recovery resumes historical intent without validating its current identity
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

### FC-092 — Close-out requires inbox/cargo writes excluded by the skill's write boundary
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

### FC-095 — The skill promises CI "on every push", which the workflow does not cover
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

### FC-097 — Hub skill supporting files still describe the pre-v0.3 cargo location
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

## CF-14 — Deployment / Git authority / doctrine distribution (FC-088 here)

### FC-088 — Hub→project distribution and release pinning are undefined in live doctrine
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

## CF-16 — Hub index / archive / changelog / lint controls (FC-089, 093, 094, 096)

### FC-089 — The mandated outgoing QA_PLAYBOOK v1.0 archive snapshot is absent
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

### FC-093 — MANIFEST's declared live-doc count and index data disagree with its own contents
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

### FC-094 — Root CLAUDE.md prescribes a CHANGELOG record format that competes with CHANGELOG's own
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

### FC-096 — The doctrine lint suite fails at baseline, and the documented process merges over red CI
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
  - CI becomes a real gate. The nine baseline findings are cleared:
    - six STARTER_KIT findings via FC-003;
    - two prose references in DATABASE;
    - one filename reference in UI_UX.
  - Then either green CI is required for merge, or a reviewed, committed baseline file makes CI fail only on new findings (Fable's two options).
  - Honest reporting is kept: no exemption patterns are added to hide findings (DocSet Sync D9, AP-5).
- **Preserve:**
  - D9's "never exempted" baseline discipline.
  - Honest lint reporting (Sol C07).
  - The introduced-vs-pre-existing distinction.
- **Likely affected docs / consumers:**
  - The three flagged docs (`SYNC`).
  - `lints/` and `.github/` if a baseline file or trigger change is chosen (`XB-LINT/CI`).
  - The skill README/SKILL merge-over-red text (`XB-SKILL`).
  - Branch-protection settings (Tony; governance outside the package).
- **Verification intent:**
  - `python3 lints/run_all.py` exits 0 at the candidate SHA, or fails only on findings absent from a reviewed baseline file.
  - The skill text no longer instructs merging over red without that mechanism.
- **Open decision:** DEC-16, end merge-over-red vs adopt a baseline file (Fable §11 decision 10; Tony). **Sequencing recommendation:** clear the DATABASE and UI_UX findings early, since they are small, and the STARTER_KIT ones via FC-003. Lint red then becomes meaningful for later waves.
- **Proposed route:** `SYNC` (doc findings) + `XB-LINT/CI` + `XB-SKILL`.

---

*End of brief 07. Primary entries: 13 (FC-085 … FC-097); 10 require correction, 3 are regression-guard only. DRAFT — CORRECTION INTAKE / NOT APPROVED FOR SYNC.*
