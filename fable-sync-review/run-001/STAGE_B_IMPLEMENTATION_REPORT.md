# STAGE_B_IMPLEMENTATION_REPORT — factory-docs-update v0.6-DRAFT

> **Author:** Fable 5.1, Factory Skill Architect / Engineer · **Run:** fable-sync-review/run-001
> **Date:** 2026-09-14 19:20 BST · **Stage:** B — IMPLEMENTATION OF THE vNEXT CANDIDATE
> **Candidate status:** **IMPLEMENTED — AWAITING INDEPENDENT OPUS 5 VALIDATION.** Not certified. No live run on this version.
> **Companions (frozen, unedited):** `SYNC_SKILL_REVIEW.md`, `SYNC_PROCESS_PROPOSAL.md` (Stage-A evidence commit `fda59a81`).

Label key: **[FACT]** observed on disk or from command output · **[INFERENCE]** reasoned · **[DECISION]** a locked ruling applied.

---

## 1. STATUS

- **Implementation complete** inside the authorized surface. The skill family is written, structurally checked, and swept for contradictions. Lints re-run: baseline unchanged. Nothing committed, nothing pushed, no branch change, no tag.
- **Nothing certified.** Every claim below about behavior ("routes TINY without asking") is a claim about the written methodology; the behavioral proof is Opus 5's job (§19).
- **No canonical doctrine, lint, CI, MANIFEST, CHANGELOG, `_AUDIT/`, RECOVERY, or session file was modified** [FACT: `git status` in §16]. The repo `CLAUDE.md` session/RECOVERY protocol was again not executed because those files are outside the Stage-B writable surface; noted as a follow-up (§17).
- **Version:** 0.6-DRAFT. One Version History row per Ruling 1, stating that it collapses the Stage-A migration steps 0.4 / 0.5 / 0.6 into one candidate; no fabricated intermediate rows.

## 2. BASELINE / BRANCH

| Item | Value [FACT] |
|---|---|
| Repository | `ahmedmusawir/app-factory-docs-v1` (local clone `C:\Users\user\GITHUB-REPOS\app-factory-docs-v1`) |
| Branch | `factory-docs-sync-process-001` (verified before and after) |
| HEAD at start | `fda59a8141e46fd60c072068ae08f7aee636d3e1` = the Stage-A evidence commit (`docs(fable): review factory docset sync process`, 2 files, 682 insertions) |
| Working tree at start | clean |
| Stage-A reports | read completely before implementation; unedited (not in `git status`) |
| Skill at start | v0.3-DRAFT, 8 files (CLAUDE.md, SKILL.md, README.md, references/×2, decision-trees/×1, templates/×2) |
| Governing doctrine re-opened | `APP_FACTORY_SKILLS_PLAYBOOK.md` §6–§7 (family rules, layout, naming) re-read; QA_PLAYBOOK §3/§4/§7–§12/§20–§22, SOFTWARE_FACTORY_PLAYBOOK §2.5, BIM_PLAYBOOK §2/§6–§9, BUG_FIX_PLAYBOOK §3/§9/§18, ENGINEER_PLAYBOOK §15–§16 from the Stage-A reading in this same session (no re-read needed; no contradiction with the rulings found — §15) |
| Not consulted | Astra / Sol / prior whole-corpus Fable artifacts (none exist on this branch; none opened) |

## 3. APPROVED RULINGS IMPLEMENTED

| Ruling | Implemented where | How |
|---|---|---|
| **1 — Family shape under the existing path** | `_SKILLS/factory-docs-update/` kept as the family root; ONE `CLAUDE.md`; children `sync-engineer/`, `sync-qa/`; `_shared/` for genuinely common content | Root `SKILL.md` and root `references/ decision-trees/ templates/` superseded into children/_shared. Version 0.6-DRAFT. Naming deviation (kebab family folder vs Playbook SHOUTING_SNAKE) disclosed in CLAUDE.md §3 and parked (§17). |
| **2 — Type + Hub git carve-out** | CLAUDE.md header ("Agent-executed skill family with Operator gates"); **D5** rewritten | Claudy may branch, commit, push only at the authorized boundary; Tony creates PR and merges; provenance (2026-08-05 ruling, Stage B Ruling 2 2026-09-14) and limits stated: does NOT redefine BIM/FIX/FEAT/TRM git-zero doctrine; "a future agent must not generalize it." Also in README standing rules. |
| **3 — Jarvis no routine seat** | **D17**; CLAUDE.md §1; engineer SKILL Role; INTAKE_TAXONOMY class 11; AP-15 | Architect contribution ends with the Correction Package; Tony may consult Jarvis only on a BLOCKED item needing architecture/preservation/semantic adjudication; no Architect gate; "Architect-owned map" language removed everywhere. |
| **4 — Other skills / lints read-only** | **D21**; D10 per-seat surface; INTAKE_TAXONOMY class 9; UPDATE_MAP §I/§J; README gotchas | Parked `XB-<run>-<NN>` items with target, reason, approved intent, blocking status; blocking → BLOCKED → Tony. Lints untouched in Stage B [FACT]. |
| **5 — Durable package** | **D11**; UPDATE_MAP header; SYNC_HANDOFF; QA templates; engineer Phase 9 | `_AUDIT/SYNC_<YYYY-MM-DD>_<slug>/`; durable set and debris list defined per path (LARGE and TINY). |
| **6 — No release tag** | Engineer Phase 9 step 6; README "What you NEVER do" | Skill describes the future `doctrine-YYYY.MM` decision as Tony's, after a successful real sync and merge; never cuts one. |
| **7 — MANIFEST/CHANGELOG infra versioning** | **D7** infra paragraph; UPDATE_MAP §G; STANDING_INVARIANTS AC-I; SYNC_HANDOFF claims | Content + header Date updated; no archive, no version dance; derived fields (count, ← map, appendix scope, CHANGELOG completeness) recomputed from disk and asserted. |
| **8 — Spec authorship (Sol, derivation-only)** | **D20**; `DOCSET_SYNC_ACCEPTANCE_SPEC.md` template (mandatory Derived-from cell); sync-qa Stage S1; STANDING_INVARIANTS "derivation-only rule, restated" | Sources limited to Correction/Intake IDs, UPDATE MAP rows, standing families; Tony approves at Gate 3; frozen; material change re-enters Gate 3. |
| **9 — Assets** | INTAKE_TAXONOMY class 6; UPDATE_MAP §H; STANDING_INVARIANTS AC-R; engineer Phase 4 step 3; README | `<OWNING_TIER>/_assets/`, canonical names, case-exact relative paths, orphan check, replacement archived by date, source-vs-rendered pairing. Deliberately minimal. |
| **10 — Process document placement** | INTAKE_TAXONOMY class 5; engineer Phase 2 step 6 | Owning tier; ambiguous → BLOCKED → Tony; canonical doctrine never `_OTHERS/`; supporting evidence → `_AUDIT/` or `_OTHERS/`. |
| **SHA / handoff sequencing** | **D18**; `_shared/references/SHA_AND_PUSH_CONTRACT.md`; SYNC_HANDOFF header note; QA_MATRIX header; sync-qa S2/S4 | CONTENT_SHA recorded after the last content commit; handoff references it and is committed after; Gate 4 before publication; push; Cody records QA_START_SHA from the remote; ancestry + "only audit artifacts between" checks; REPAIR_CONTENT_SHA / QA_RETEST_SHA per cycle; no self-referential SHA anywhere (AP-17). |
| **Core routing requirement** | **D3**; `sync-engineer/decision-trees/route-selection.md` Decision A; engineer Phase 1 step 5 + Phase 2 step 7; UPDATE_MAP §P; engineer anti-pattern 1; README "Small or large?" | Ten fast-path conditions, all required; provisional at Phase 1, final at Phase 2; the skill never opens with "small or large?"; smallest blocking question only; Tony may escalate; downgrade needs a recorded ruling. |

## 4. FILES CREATED

All under `_SKILLS/factory-docs-update/` unless stated [FACT: `git ls-files --others`].

| File | Purpose |
|---|---|
| `_shared/references/INTAKE_TAXONOMY.md` | Eleven intake classes, ID rules, per-class routing, disposition vocabularies (D16) |
| `_shared/references/STANDING_INVARIANTS.md` | Ten AC families with the exact check per family; preconditions; derivation-only rule (D19/D20) |
| `_shared/references/SHA_AND_PUSH_CONTRACT.md` | The single push rule and the four recorded SHAs, with LARGE / rework / TINY / post-merge sequences and forbidden acts (D18) |
| `_shared/references/ANTI_PATTERNS.md` | Moved from `references/`; AP-11 corrected to `_INBOX/`; new AP-12…AP-17 |
| `_shared/templates/UPDATE_MAP.md` | The single approved planning artifact (§0, §A–§P); supersedes RIPPLE_MAP |
| `_shared/templates/DOCSET_SYNC_ACCEPTANCE_SPEC.md` | Derivation-only acceptance spec template; every AC row carries Derived-from, verification expectation, gate |
| `_shared/templates/SYNC_HANDOFF.md` | Engineering → QA claim package keyed by CONTENT_SHA; repair-cycle appendix; Gate 4 record |
| `sync-engineer/SKILL.md` | Engineer child methodology (P0–P9, TINY and LARGE), worked example, anti-patterns, Version History (carries the root SKILL.md history) |
| `sync-engineer/decision-trees/route-selection.md` | Decision A (TINY/LARGE, evidence-driven) + Decision B (execution-route exception) |
| `sync-engineer/references/TOOL_ROUTING.md` | Moved from `references/`; push moved to "after Gate 4 only"; MCP framed as exception appendix; Gate 4 applies on MCP |
| `sync-engineer/templates/LESSONS_LEARNED.md` | Moved from `templates/`; root-cargo line fixed to `_INBOX/`; statuses gain NO-CHANGE / SPLIT / DEFERRED and intake ID |
| `sync-qa/SKILL.md` | QA child methodology: S0 discovery, S1 Sol spec derivation, S2 Cody preconditions, S3 verification, S4 routing/retest loop, S5 Gate Q; worked example; anti-patterns; Version History |
| `sync-qa/templates/QA_MATRIX.md` | Cody's evidence matrix, cycle log, propagation re-run record, findings log, recommendation |
| `sync-qa/templates/GATE_Q_REPORT.md` | Sol's docs-only overlay on QA_PLAYBOOK §22 |
| `fable-sync-review/run-001/STAGE_B_IMPLEMENTATION_REPORT.md` | This report (the one authorized new report file) |

## 5. FILES MODIFIED

| File | Change |
|---|---|
| `_SKILLS/factory-docs-update/CLAUDE.md` | Rewritten as the family manager v0.6-DRAFT: seat resolution in activation; discovery does `git fetch` not pull; D3, D5, D7, D9, D10, D11, D15a, D16 rewritten; D17–D22 added; type relabeled; folder tree and reading order updated; override examples replaced (propagation-search skip; LARGE→TINY downgrade); non-waivable rules extended to QA-seat doctrine edits; Version History row added above the preserved 0.3/0.2/0.1 rows |
| `_SKILLS/factory-docs-update/README.md` | Operator runbook rewritten: family anatomy, evidence-driven routing explained from the Operator's seat, gates incl. Gate 3 / QA lane / Gate Q, three launch lines (Engineer, QA Lead, QA executor) + resume, gotchas updated (no judging corrections, read-only boundaries, assets, infra docs, QA never edits, no tag), stale "files in the root" line removed |

## 6. FILES RENAMED / SUPERSEDED

| Old (deleted from working tree, unstaged) | Superseded by |
|---|---|
| `SKILL.md` (root) | `sync-engineer/SKILL.md` (methodology) + `sync-qa/SKILL.md` (QA lane) — family has no root SKILL.md per Playbook §7 |
| `references/ANTI_PATTERNS.md` | `_shared/references/ANTI_PATTERNS.md` |
| `references/TOOL_ROUTING.md` | `sync-engineer/references/TOOL_ROUTING.md` |
| `decision-trees/route-selection.md` | `sync-engineer/decision-trees/route-selection.md` (rewritten) |
| `templates/LESSONS_LEARNED.md` | `sync-engineer/templates/LESSONS_LEARNED.md` |
| `templates/RIPPLE_MAP.md` | `_shared/templates/UPDATE_MAP.md` — RIPPLE_MAP is mentioned only as "superseded" (3 historical mentions [FACT]) |

Deletions were done on the working tree only (nothing staged, nothing committed). `git status` shows them as ` D`.

## 7. FAMILY-SKILL STRUCTURE

```
_SKILLS/factory-docs-update/            ← family root; activation path unchanged
├── CLAUDE.md                           ← the ONE manager (1 CLAUDE.md in the tree [FACT])
├── README.md
├── _shared/
│   ├── references/ ANTI_PATTERNS.md · INTAKE_TAXONOMY.md · SHA_AND_PUSH_CONTRACT.md · STANDING_INVARIANTS.md
│   └── templates/  UPDATE_MAP.md · DOCSET_SYNC_ACCEPTANCE_SPEC.md · SYNC_HANDOFF.md
├── sync-engineer/  SKILL.md (name: sync-engineer) · references/TOOL_ROUTING.md · decision-trees/route-selection.md · templates/LESSONS_LEARNED.md
└── sync-qa/        SKILL.md (name: sync-qa) · templates/QA_MATRIX.md · templates/GATE_Q_REPORT.md
```

Why each `_shared/` file is genuinely shared [INFERENCE from usage]: ANTI_PATTERNS (both seats load at Phase/Stage 1); INTAKE_TAXONOMY (Claudy classifies; Cody verifies dispositions for AC-T); STANDING_INVARIANTS (Sol derives; Cody verifies; Claudy self-checks on TINY); SHA_AND_PUSH_CONTRACT (Claudy pushes; Cody records); UPDATE_MAP (Claudy authors; Sol/Cody consume); ACCEPTANCE_SPEC (Sol authors; Cody/Claudy consume); SYNC_HANDOFF (Claudy authors; Cody consumes). Single-user content stayed in its child (TOOL_ROUTING, route-selection, LESSONS_LEARNED → engineer; QA_MATRIX, GATE_Q_REPORT → QA). No `workflow/`, no `examples/` (none pre-created; Playbook §15 step 7).

## 8. TINY ROUTE

Written shape: P0 discovery → P1 intake/classification (IDs, provisional route) → Gate 1 → P2 propagation analysis → UPDATE MAP incl. §P route evidence and the waiver line → Gate 2 (map + explicit docs-only QA waiver) → P4 execute locally (per-doc checklist; CONTENT_SHA) → P5 run metadata + Claudy's own mechanical standing-invariant checks (AC-S, AC-A, AC-I, AC-L, AC-H + §B re-run) → Gate 4 → the one push → P8 Tony PR/merge → P9 sweep. No Sol, no Cody, no spec, no Gate Q. Durable set: `UPDATE_MAP.md` + `RUN_SUMMARY.md`. Ten fast-path conditions in `route-selection.md` Decision A; ALL required; any failure → LARGE; undeterminable → smallest blocking question; Tony escalates freely; downgrade needs a recorded ruling. `README.md` tells the Operator he does not choose the path up front.

## 9. LARGE ROUTE

P0 → P1 → Gate 1 → P2 (map) → Gate 2 → P3 Sol derives spec (fresh session) → Gate 3 → P4 Claudy implements (local; CONTENT_SHA) → P5 handoff (references CONTENT_SHA; committed after it) → Gate 4 → push → P6 Cody (fresh session): QA_START_SHA, preconditions, matrix, verification, findings → Sol routes: in-scope failures → Claudy bounded repair → REPAIR_CONTENT_SHA → repair push → Cody QA_RETEST_SHA retest (failed ACs + AC-S/AC-L/AC-H) → repeat; BLOCKED → Tony; scope expansion → Gate 2 amendment (+ Gate 3 if ACs change); three FAIL cycles on one AC → BLOCKED → P7 Sol Gate Q (Factory vocabulary) → P8 Tony PR/merge → P9 sweep. No Astra gate. No Architect gate.

## 10. UPDATE MAP DESIGN

`_shared/templates/UPDATE_MAP.md` sections: §0 run header (Run ID, branch, BASE_SHA, execution route, **Path TINY/LARGE**, QA arrangement/waiver line, status DRAFT→APPROVED→AMENDED-vN, lint baseline, live-doc counts) · §A intake ledger (ID, class, source, gist, disposition, gate state) · §B per-ID (approved intent, invariants, preservation, likely files + ← rows, **propagation search**: terms, scope, command shape, hit count, every hit with CHANGE/CONSISTENT/HISTORY/OUT-OF-SCOPE disposition; NO-CHANGE proposal; CONFLICT → §K) · §C touch list (canonical path, verified placement, proposed wording / exact edit intent, contributing IDs, version live→new, archive expectation, structural flag, minimal-form note) · §D new canonical files · §E stale/superseded · §F dependents checked unchanged · §G infra/index effects · §H paths/links/assets · §I skill references (awareness) · §J parked cross-boundary · §K unresolved Operator decisions · §L preservation constraints · §M expected validation · §N write-load + commit plan · §O approvals/amendments/overrides/CONTENT_SHA · §P route evidence table. Intent-level correction packages are first-class: §B carries intent verbatim, §C carries Claudy's proposed wording, and Gate 2 approval is what authorizes the words (D17). One artifact; RIPPLE_MAP retired.

## 11. QA / ACCEPTANCE-SPEC DESIGN

- **Seats:** Sol (QA Lead) and Cody (QA executor) share `sync-qa/SKILL.md`; seat from the launch line, never assumed; fresh session required; evidentiary inputs restricted (package, map, spec, handoff, remote branch, clone); RECOVERY/session are state only.
- **Spec:** template with mandatory Derived-from per AC (`CP-<id> invariant n` / `IN-… disposition` / `MAP §C#n …` / `STANDING <family>`); families TRACEABILITY, SCOPE/DIFF EQUALITY, PRESERVATION, PROPAGATION/CONSISTENCY, REFERENCES/PATHS/ASSETS, NAMING/TERMINOLOGY, INDEX/DERIVED FIELDS, ARCHIVE FIDELITY, LINT/BASELINE, HYGIENE/CLEANUP (the ten from Stage A, tags AC-T/S/P/C/R/N/I/A/L/H); preconditions (BLOCKED, not FAIL); Factory `AC1, AC2, …` numbering; gates↔AC mapping; frozen after Gate 3.
- **Cody may / may not:** written in D10, D20, sync-qa Role and anti-patterns 2, 9: reads approved artifacts, verifies at QA_START_SHA with read-only checks, writes only QA_MATRIX / findings; never edits canonical doctrine, map, spec, MANIFEST, CHANGELOG, archives, Claudy's wording, or history; never adjudicates doctrine.
- **Sol:** derives, reviews evidence sufficiency, classifies (Acceptance Failure / Regression / Pre-Existing / Follow-Up Finding / Observation), routes (in-scope failures → Claudy; decisions → Tony; follow-ups → future intake), owns Gate Q in the Factory vocabulary only.
- **Verdict vocabulary:** PASS / PASS WITH FOLLOW-UP FINDINGS / PASS WITH KNOWN RISK / FAIL / BLOCKED — no new terms introduced (sync-qa anti-pattern 8).

## 12. SHA / HANDOFF MODEL

Implemented exactly as the additional ruling: (1) last content change committed → (2) CONTENT_SHA recorded → (3) SYNC_HANDOFF references CONTENT_SHA → (4) handoff/audit metadata committed → (5) Gate 4 before publication → (6) push after approval → (7) Cody records QA_START_SHA from `origin/<branch>` → (8) Cody verifies ancestry (`git merge-base --is-ancestor`), that `git diff --name-only CONTENT_SHA..QA_START_SHA` is confined to `_AUDIT/SYNC_<run>/**`, `RECOVERY.md`, `session_*.md`, `agent_docs/RESPONSES/*`, and that no canonical path changed after CONTENT_SHA. Repair cycles record REPAIR_CONTENT_SHA (Claudy, after the commit exists) and QA_RETEST_SHA (Cody, from the remote). SYNC_HANDOFF §8 explicitly says "QA_START_SHA is Cody's to record — not here." Post-merge housekeeping push named as outside the contract. Forbidden list includes rewriting any QA-recorded history. The Stage-A self-reference defect is corrected (AP-17 documents it).

## 13. PROPAGATION COMPLETENESS MODEL

D19 + UPDATE_MAP §B + STANDING_INVARIANTS AC-C + sync-qa S3: for each changed governing rule, search terms (old wording, retired terminology, role/gate/module/lifecycle/artifact names, referenced filenames, cited section names) over the live scope (five tiers + MANIFEST + CHANGELOG; `_SKILLS/` and `_OTHERS/` read-only awareness) with recorded command shape; every hit dispositioned CHANGE / CONSISTENT / HISTORY / OUT-OF-SCOPE; §F lists dependents (examples, checklists, templates, quick references, role instructions) with CONSISTENT quotes; superseding docs treat every removed rule as a term. Cody re-runs the searches verbatim at the candidate SHA and reconciles row-by-row; "zero undispositioned active hits" is the bar; a CHANGE hit still showing old wording is an Acceptance Failure. MANIFEST ← map is explicitly "the starting point, never the whole search." On TINY the search must be bounded and complete before Gate 2 (condition A9) or the route is LARGE.

## 14. RECOVERY / CLEANUP MODEL

- **Recovery (D15a):** RECOVERY.md and session file first (state), then git/disk (truth, wins on disagreement); phase located from the durable folder (no map → P1; map DRAFT → P2; map APPROVED no spec → P3; spec + commits no handoff → P4; handoff not pushed → Gate 4; pushed no matrix → P6; matrix partial → P6 at last row; findings routed → rework; Gate Q present → P8/P9); re-present from the last completed gate; adopt-or-abandon by Tony's word. **QA resume:** re-verify QA_START_SHA / latest QA_RETEST_SHA against the remote before trusting any PASS row; moved tip voids all rows. Covers analysis/map, implementation, handoff, QA, rework, post-Gate-Q/pre-merge, closeout for both children.
- **Cleanup (D11):** DURABLE = `_AUDIT/SYNC_<date>_<slug>/` with map, spec (LARGE), handoff, matrix + findings (LARGE), Gate Q report (LARGE), stamped intake package or immutable-source reference, RUN_SUMMARY; TINY = map + RUN_SUMMARY. DEBRIS = per-cycle scratch and grep dumps; duplicates of durable artifacts elsewhere (RESPONSES copies dispositioned by the standing 2026-08-10 ruling as a named housekeeping commit); abandoned branches; `_INBOX/` contents; stray `__pycache__`; editor backups. Session files and RECOVERY.md stay at root. Sol verifies cleanup at the final SHA; Claudy performs it.

## 15. PLAYBOOK COMPLIANCE CHECK

| Playbook rule | Result [FACT unless marked] |
|---|---|
| Two-file core: family CLAUDE.md + one SKILL.md per child (§3, §7) | PASS — 1 CLAUDE.md; `sync-engineer/SKILL.md`, `sync-qa/SKILL.md` |
| Single-CLAUDE.md rule; no per-child CLAUDE.md (§6, Anti-Pattern 4) | PASS — `Get-ChildItem -Recurse -Filter CLAUDE.md` count = 1 |
| Frontmatter `name` equals child folder name (§5, §8) | PASS — `name: sync-engineer`, `name: sync-qa` |
| Frontmatter description with trigger phrases and what it does NOT do; `allowed-tools` restricted | PASS — both children |
| SKILL.md under 500 lines (§5) | PASS — engineer 136 logical lines / 3,839 words; QA 96 / 2,534 words (PowerShell line count; long lines) |
| CLAUDE.md 3,000–8,000 words (§4) | PASS — 5,811 words |
| CLAUDE.md required sections in order: Identity, Activation, Folder Tree, Doctrine, Reading Order, Override, Version History (§4) | PASS — §1–§7 |
| SKILL.md required body: Role, phases with goal/steps/stop gate/output, worked example, skill-specific anti-patterns, When You're Done, Version History (§5) | PASS — both children |
| `_shared/` only for genuinely shared content; no empty folders (§7) | PASS — rationale in §7 of this report; no empty folders; no `examples/` pre-created |
| Folder naming: children kebab-case; reference files descriptive; decision trees topic-prefixed (§7) | PASS for children/files. **DEVIATION (ruled):** family folder is kebab `factory-docs-update/` not SHOUTING_SNAKE — Ruling 1 preserves the activation path; disclosed in CLAUDE.md §3; parked (§17) |
| Activation flow: read CLAUDE.md → discovery → present plan → wait (§9) | PASS — CLAUDE.md §2 |
| Plan Mode + Operator Override with examples (§10) | PASS — D2; §6 with two examples |
| Evidence discipline five labels (§11) | PASS — D12 |
| Evolution principle: Version History rows for meaningful changes (§12) | PASS — rows in CLAUDE.md and both SKILL.md |
| Skill type declared (§2) | PASS — "Agent-executed skill family with Operator gates" (Ruling 2); Playbook §16 allows agent skills with compressed Plan Mode; this family keeps explicit Operator gates, which is stricter, not looser [INFERENCE] |
| Doc-as-source / no forking of doctrine (§14 Exemplar 3) | PASS — GATE_Q_REPORT is an overlay on QA_PLAYBOOK §22, not a copy; verdict vocabulary cited, not redefined |

**Governing-doctrine boundaries re-verified against the rulings:** QA owns the verdict (QA_PLAYBOOK §4, SFP §2.5.5) — kept; Operator final authority — kept; Engineer never self-approves — kept on LARGE, waiver-recorded on TINY per SFP §2.5.6 (docs-only); QA never repairs (QA_PLAYBOOK §3) — kept; rejected findings never reach the Engineer (BUG_FIX §3) — kept; acceptance spec seeded before implementation and not reverse-engineered (BIM §8) — kept (Gate 3 before P4). **Ruling 2 versus BIM/BUG_FIX git-zero:** not a literal contradiction — those texts govern application modules; D5 states the Hub-only exception and its limits. **Ruling 8 versus SFP §2.5.2 (Engineer maintains/finalizes the spec):** a scoped departure for the sync campaign, made lawful by the derivation-only rule and Tony's Gate 3 approval; recorded in D20. No ruling required re-opening.

## 16. REGRESSION / VALIDATION RESULTS

All commands run read-only at the end of implementation [FACT]:

| Check | Result |
|---|---|
| Branch / HEAD | `factory-docs-sync-process-001` / `fda59a81…` unchanged; no commit, no push, no tag |
| `git status --porcelain` | 2 modified (CLAUDE.md, README.md), 6 deleted (old root SKILL.md, references/×2, decision-trees/×1, templates/×2), 14 untracked (new family files) — **all under `_SKILLS/factory-docs-update/`**; plus this report once written. Paths outside the authorized surface: **none** |
| `git diff --stat` (tracked) | 8 files, +165 / −624 lines (rewrites of CLAUDE.md and README.md; deletions of superseded files). Warnings about LF→CRLF are informational (repo files are CRLF on this rig) |
| Lints `py lints/run_all.py` | ENCODING PASS · RETIRED-TERMS PASS · VERSIONED-REFS FAIL 8 hits · HEADER-PRESENCE FAIL 1 miss — **identical to the Stage-A baseline** (STARTER_KIT_HANDBOOK ×6, DATABASE_MANUAL ×2, UI_UX_BUILDING_MANUAL ×1). The skill folder is outside lint scope by design; no live-scope file changed, so no new failure is possible; none observed |
| One CLAUDE.md in the family | 1 |
| Child frontmatter names | match folders |
| Stale-reference sweep (regex over the whole skill folder) | `RIPPLE_MAP`: 3 mentions, all "supersedes/superseded" · `ripple map`: 0 · root-cargo behavior: only legacy-fallback statements · `Stark Skill`: 0 · `three-role`: 0 · `PACK (`: 0 · `Gate 3 (hard`: 0 · `Phase 3 — Route`: 0 · Architect-owned map: 0 · self-certification as sufficient on LARGE: 0 (only named as an anti-pattern) |
| Push-instruction sweep (every line containing "push") | 60+ lines reviewed; every push is: after Gate 4, a bounded repair push in Phase 6, the post-merge housekeeping push (named as outside the contract), "PULL never push on main", or MCP `push_files` mechanics with "Gate 4 still applies." No pre-Gate-4 push instruction remains |
| Gate numbering consistency | Gates 1, 2, 3 (LARGE), 4, Q, merge — identical in CLAUDE.md, both SKILL.md, README, templates |
| Intra-skill path references | every `_shared/…`, `sync-engineer/…`, `sync-qa/…` path resolves; child-relative `references/`, `decision-trees/`, `templates/` paths resolve from their child folder |
| Route decision explicit and executable | Decision A tree with 10 conditions and provisional/final points; §P table in the map |
| TINY lightweight | 4 Tony touchpoints (Gate 1, 2+waiver, 4, merge); no QA seats |
| LARGE has the QA lane | Sol S1/S5, Cody S2–S4, Gate 3, Gate Q |
| Map supports intent-level packages | §B intent/invariants/preservation verbatim + §C proposed wording + Gate 2 authorization |
| Every AC row has a derivation field | template column "Derived-from" mandatory; STANDING_INVARIANTS restates the rule |
| Cody cannot edit doctrine in the written workflow | D10, D20, sync-qa Role + anti-patterns 2, 9; SHA contract "A QA seat pushing anything" forbidden |
| Other `_SKILLS` / lints read-only during sync | D21, D10, taxonomy class 9, README |
| CONTENT_SHA / QA_START_SHA internally consistent | SHA contract, D18, SYNC_HANDOFF, QA_MATRIX, both SKILL.md agree; no self-reference |
| Recovery covers Engineer and QA sessions | D15a phase list; sync-qa S0 RESUME; engineer P0 RESUME |
| Durable vs debris explicit | D11; engineer P9 step 5; Sol S5 step 1 |
| Stage-B diff contains canonical / lint / CI changes? | **No** |

**Not verified (cannot be, without running the skill):** that a fresh session actually behaves as written. That is §19.

## 17. PARKED FOLLOW-UPS

| ID | Item | Target | Why parked |
|---|---|---|---|
| PB-01 | Family folder name is kebab (`factory-docs-update/`) while Skills Playbook §7 says SHOUTING_SNAKE for families | `_SKILLS/` (rename) + every runbook/RECOVERY reference | Ruling 1 preserves the activation path; a rename is a separate Operator decision |
| PB-02 | Repo `CLAUDE.md` session-file / RECOVERY.md / RESPONSES protocol not executed for Stage B | `session_2026-09-14.md`, `RECOVERY.md`, `agent_docs/RESPONSES/` | Outside the Stage-B writable surface. One-line follow-up: record "Stage B implemented, awaiting Opus 5 validation" |
| PB-03 | `examples/` folder absent (Skills Playbook §15 step 10) | `_SKILLS/factory-docs-update/examples/<run>-<date>/` | To be populated from the first validated run of v0.6 (Opus 5 TEST A or B), not pre-created |
| PB-04 | MANIFEST derived-field drift ("29 live docs" vs 31 on disk; appendix "27 bodies") | `MANIFEST.md` | Canonical/infra file; must be fixed in a real sync run (AC-I will catch it), not in Stage B |
| PB-05 | CHANGELOG "Ongoing entries" block lacks a table header row | `CHANGELOG.md` | Canonical/infra file; a real sync's §G row can fix it under Tony's approval |
| PB-06 | Retired-terms lint list (`lints/retired_terms_lint.py`) is static (`stitch` only); campaign term lists run as QA grep gates | `lints/` | Ruling 4: lints read-only; promotion of campaign terms into the lint is a separate infra job |
| PB-07 | Reference/path/asset resolution exists as a QA check (AC-R), not a lint | `lints/` (a fifth lint) | Same as PB-06 |
| PB-08 | The `_INBOX/` folder does not exist on this branch | `_INBOX/` | Created by the Operator when dropping cargo (README Step 3); not a skill file |
| PB-09 | Line-ending warnings (LF → CRLF) on the two rewritten files | repo `.gitattributes` or rig config | Informational; the repo has no `.gitattributes`; commit will normalize as the rig has always done |

## 18. KNOWN LIMITATIONS

1. **No behavioral validation.** The routing tree, the propagation search, the Cody preconditions, and the rework loop are written, not exercised. Every "the skill does X" in this report is a claim about text until Opus 5 runs it.
2. **Condition A6 (high-risk governing rule) and A9 (search bounded and complete) require judgment.** The tree names the domains and the bar, but a fresh session could still misjudge; TEST A/B should include a borderline case.
3. **Sol/Cody as separate sessions is enforced by instruction, not mechanism.** Independence depends on the Operator launching QA seats fresh; the skill refuses to assume a QA seat from repository state, which is the strongest written guard available.
4. **TINY relies on Claudy's own mechanical checks.** That is the docs-only waiver by design; it is not independent verification and the skill says so.
5. **Asset handling is untested against a real image.** No image exists in the Hub; class 6 mechanics are minimal and forward-looking by ruling.
6. **The engineer SKILL.md is dense.** 3.8k words in 136 logical lines (long lines). It is under the 500-line budget but a future version may move Phase detail to `workflow/NN-*.md` if it grows.
7. **Version History for the superseded root SKILL.md** now lives in `sync-engineer/SKILL.md` with "(as root SKILL.md)" annotations; git history holds the original file.

## 19. INDEPENDENT TEST REQUIREMENTS FOR OPUS 5

Fable is not the tester. A fresh Opus 5 session, with no access to this conversation, should execute the following against a **synthetic** intake staged in `_INBOX/` on a throwaway branch of a Hub clone. **No real Part-1 correction findings; no real doctrine modified to manufacture cases** — synthetic packages target synthetic or clearly-labeled test placements, or the run is executed to Gate 2 only (map produced, no execution) where a real-doc edit would be required. The tester records EVIDENCE for every pass/fail below.

**Setup (all tests):** clean clone; `git checkout -b test/sync-skill-v0.6-<date>`; create `_INBOX/`; stage the intake; launch with exactly `Go read _SKILLS/factory-docs-update/CLAUDE.md and follow it.` (plus seat lines for QA tests). The tester must not answer questions the skill should have answered from disk; each such question is a finding.

**TEST A — TINY routing.** Intake: one `LESSONS_<x>.md` with two FLAGGED, edit-level entries targeting sections that exist in one live doc, no new doc, no rename, no risky domain. Expect: seat resolved to Engineer without a seat line · `_INBOX/` discovered and classified DOCTRINE JOURNAL with `IN-…` IDs · lint baseline recorded (9 findings) · MANIFEST 29-vs-31 discrepancy reported, not fixed · provisional route TINY stated with evidence at Gate 1, **without asking "small or large?"** · UPDATE MAP produced with §B search terms, hits, dispositions, verified placements, §P all ten conditions evidenced, waiver line drafted for Gate 2 · only genuine Operator questions asked · no Sol/Cody launch requested · (if executed) commits local, CONTENT_SHA recorded, Claudy's own AC-S/A/I/L/H checks presented at Gate 4, no push before approval. Fail criteria: any path question to the Operator; any push before Gate 4; any QA ceremony; any edit outside the map.

**TEST B — LARGE routing and classification variety.** Intake staged as one package folder + files: a synthetic `CORRECTION_PACKAGE/` (master index APPROVED; three briefs: one whose invariant restates a rule that also appears in a checklist of a second doc — the **deliberately seeded stale dependent**; one that is already true in the corpus — expect a NO-CHANGE proposal; one that names a term also used by another `_SKILLS/*` file — expect an §I awareness row and, if a change there would be needed, a parked `XB-` item) · one journal/lesson file · one synthetic NEW canonical document with an unambiguous tier · one synthetic superseding copy of a live doc (content-identical plus one changed sentence; version claim deliberately wrong) · one image file referenced by the new doc (asset awareness) · one historical file marked as such. Expect: every unit classified into the correct class with IDs; the package's Correction IDs retained; the wrong version claim caught against the live header; route **LARGE** with the failing conditions named (new doc; possibly cross-correction) · complete ledger · complete propagation search with every hit dispositioned · UPDATE MAP acceptance-spec-ready (verbatim invariants/preservation in §B/§L) · Gate model correct (Gate 3 requested before branch creation) · handoff behavior per the SHA contract if execution proceeds. Then, with the map approved by the tester-as-Operator: **Sol** session derives the spec — every AC must carry a lawful Derived-from; an AC without one is a fail; **Claudy** executes with the seeded dependent deliberately left unpropagated by the tester's instruction (or by omitting its §C row and observing whether the search catches it — preferred: let the search find it and then instruct Claudy at Gate 2 to "skip row N" as an Operator override, verifying the override protocol fires); Gate 4; push; **Cody** session records QA_START_SHA from the remote, verifies ancestry and post-CONTENT diff confinement, re-runs the searches, and must **detect the unpropagated dependent as an Acceptance Failure**; Sol routes it; Claudy's bounded repair touches only that file with `repair QA-F01` and no version re-bump; Cody records QA_RETEST_SHA, retests the AC plus AC-S/AC-L/AC-H, passes; Sol issues Gate Q in Factory vocabulary. Fail criteria: Cody edits any file outside the run folder; any seat assumed from repo state; any push before Gate 4; a handoff claiming its own SHA; an AC without a source; a NO-CHANGE landed without Gate 2 approval; a repair outside the touch list accepted.

**TEST C (recommended) — resume.** Kill the Engineer session between Gate 2 and Gate 4, then between push and Cody's first row; relaunch with the RESUME line; expect RECOVERY/session read first, git/disk verified, correct phase located from the durable folder, PASS rows voided if the tip moved.

**Exit for certification:** A and B pass with evidence; Opus 5 writes its own report; Tony decides on v0.6 → v0.7 or promotion toward 1.0 after a real merged sync.

## 20. DONE / NOT DONE

| Done-looks-like item | Status |
|---|---|
| vNext draft implemented inside the authorized folder | DONE |
| Family structure playbook-compliant | DONE (one ruled naming deviation disclosed, PB-01) |
| Automatic TINY/LARGE routing exists | DONE (written; unvalidated) |
| Correction Packages are first-class intake | DONE |
| UPDATE_MAP replaces RIPPLE_MAP as the single planning artifact | DONE |
| Propagation completeness search-based, per-hit dispositioned, re-run by Cody | DONE |
| LARGE runs have the Sol/Cody QA lane | DONE |
| TINY runs retain the fast path | DONE |
| Acceptance criteria derivation-only | DONE |
| Git carve-out explicitly Hub-only with provenance and limits | DONE |
| Push sequencing consistent everywhere | DONE (sweep in §16) |
| CONTENT_SHA / QA_START_SHA model correct, no self-reference | DONE |
| Durable / debris / recovery explicit | DONE |
| Other skills / lints parked boundaries | DONE |
| Asset routing minimal | DONE |
| Stage-B regression checks pass; only documented pre-existing lint failures | DONE (baseline identical) |
| No canonical doctrine changed · no commit · no push | DONE (verified) |
| Implementation report complete | DONE (this file) |
| Candidate marked AWAITING INDEPENDENT OPUS 5 VALIDATION | DONE (CLAUDE.md header, README header, both SKILL.md Version History rows, this report) |
| **NOT DONE (by design):** behavioral validation (TEST A/B/C); `examples/`; session/RECOVERY entries for Stage B; any real synchronization; any tag | — |

---
*Stage B implementation report. Files created/changed: `_SKILLS/factory-docs-update/**` and this report only. Nothing committed. Nothing pushed. Candidate awaits independent Opus 5 validation.*
