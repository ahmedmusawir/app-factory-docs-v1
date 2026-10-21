# AMENDED-v3 bounded retest — Executor assignment prepared (Fable, QA Lead)

Prepared 2026-10-20T14:28:31+06:00. Candidate 26b050fe70de66e74ec8d65bcf9287d4369a91f7. Handoff ZIP SHA 5efa6fee…; index/patch/Gate 2 record identities match committed copies; remote tip and clean worktree at candidate; one non-merge commit; 56 paths; labels and amended rows present; STATE first differing line 809. Nothing graded.

Prompt: _AUDIT/SYNC_2026-10-15_doctrine-part2/QA_PHASE4/RETEST_AMENDED_V3/QA_EXECUTOR_PROMPT.md
Prompt SHA-256: 66bd5e14dab3f93c0858c9b2e799d00c5f47f0f36dcbfdd505613e4843eb6880

---

# QA EXECUTOR — AMENDED-v3 bounded retest (R4′, R6′, R7′, R8′, R10′, R11′, R12′ + carry-forward)

You are a fresh independent QA EXECUTOR session launched by Tony, reporting to Fable (QA Lead). This is the final bounded Phase 4 repair retest, not engineering, not a new full Phase 4 run, and not a reopening of settled approvals. Record your seat, session start UTC time and an independence statement. If this conversation authored, applied, committed or pushed AMENDED-v3, do not test it: record BLOCKED and ask for a genuinely fresh session. Do not claim to be Fable and do not issue the successor verdict.

## Locations and pinned identities

Review repo (evidence writes): `/home/moose/Documents/app-factory-docs-v1`
RUN (relative to either repo): `_AUDIT/SYNC_2026-10-15_doctrine-part2`
Execution worktree (strictly read-only): `/home/moose/Documents/app-factory-docs-sync-execution`

- Branch: `docs/sync-doctrine-part2-2026-10-15`
- Expected QA_START_SHA (candidate): `26b050fe70de66e74ec8d65bcf9287d4369a91f7`
- Exact parent (AMENDED-v2 candidate): `8dff354937bc7baf739370a9886497d9d5359186`
- Earlier chain: Phase 3 candidate `20f71ee932ed21c0878cb3a0f39c6fbe90d0a793`; CONTENT_SHA `ef35d26d82f1904da6ed33663ad647e4ee16fe98`; BASE / expected main `9c179392f79b70da099121fc357d3107ad3bb86e`
- Landing date remains `2026-10-18`.
- Successor index (use this one): `RUN/AMENDED_V3/BOUND_EXECUTION_INDEX.json`, SHA-256 `55537c6411724ab78837d0191d61375654839202acbf15b13a76d98aa8d483e6`
- Approved patch: `RUN/AMENDED_V3/EXECUTION_PROPOSAL.patch`, SHA-256 `afd8f9249854d4e99c385b1e21c459fa297fa5ed5ddcac782d1509747c43faed`
- Gate 2 record: `RUN/AMENDED_V3/DIRECTOR_DECISIONS_V3.md`, SHA-256 `1fa28bc81dedd96f017f9ffc9a69b7a86326917a61093e9aeb9390bcfbe300a4`
- Frozen spec: `RUN/QA_RETEST_AF01/DOCSET_SYNC_ACCEPTANCE_SPEC_AMENDED_V1_R1.md`, SHA-256 `2a3867cacef11c6bb0419a4c71229479efe703cee9fbcc1e4f71c0ac8e63f0fc`
- Engineering handoff: `/home/moose/Downloads/FACTORY_AMENDED_V3_EXECUTION_HANDOFF_2026-10-20_104051.zip`, SHA-256 `5efa6fee26d94598fc6687e22b9cd50bec0b282bb4cf2196ba1b06283cd60485` (38 inventory rows)
- Governing QA records: `RUN/QA_PHASE4/RETEST_AMENDED_V2/QA_LEAD_VERDICT_V2.md` (§4 path to PASS) and `JARVIS_REPAIR_RECOMMENDATION.md` (§1 corrections V3-1…V3-4, §4 criteria).
- Prior accepted evidence (carry-forward source): `RUN/QA_PHASE4/RETEST_AMENDED_V2/EXECUTOR_EVIDENCE/` (manifest SHA-256 `379dd10450157d0c394684ed7d460d65e42006c7d2a8974e9c778329ad318c38`), graded on `8dff354`.

Evidence destination (NEW; create it; stop rather than overwrite if it already holds completed evidence):
`/home/moose/Documents/app-factory-docs-v1/_AUDIT/SYNC_2026-10-15_doctrine-part2/QA_PHASE4/RETEST_AMENDED_V3/EXECUTOR_EVIDENCE/`

## Read first

1. This prompt. Verify the handoff ZIP hash, member-path safety and its SHA256SUMS inventory; extract it into its own empty directory and keep your scripts elsewhere.
2. In the ZIP: `AMENDED_V3_EXECUTION/FABLE_HANDOFF.md`, `AMENDED_V3/DIRECTOR_DECISIONS_V3.md`, `COMMIT_RECEIPT.json`, `PUSH_RECEIPT.json`, `STATE_CARRY_FORWARD.json`, `CODE_PRESERVATION.json`. Cross-check each against the committed copy at the candidate (post-commit receipts are intentionally outside the commit they identify).
3. In the review repo: `QA_LEAD_VERDICT_V2.md`, `JARVIS_REPAIR_RECOMMENDATION.md`, `RUN/QA_PHASE4/QA_LEAD_VERDICT.md` (Phase 4, preserved), `OVERRIDES_AND_ALIGNMENT.md`.
4. In the candidate: `RUN/AMENDED_V3/AMENDMENT_V3_EDITS.json` (8 edits), the successor index, the approved patch and the Gate 2 record.

Source precedence: frozen spec plus settled Director rulings and the two preserved Fable verdicts; the attributable AMENDED-v3 Gate 2 approval; this bounded assignment. Engineering PASS labels, hit counts and propagated dispositions are hypotheses to test, not QA evidence. Do not run `verify_installed.py`, `push_verify.py`, apply or push helpers, and do not use their assertions as your test suite.

## Alignment for this retest

- Preserve O-1…O-8, both Fable verdicts and all approval bytes. For this run the required tip is **26b050f**, parent **8dff354**, index **AMENDED_V3/BOUND_EXECUTION_INDEX.json**. These are explicit successor identities, not spec edits.
- R6′/R12′ scope per the Gate 2 record: three canonical paths (APP_ARCHITECTURE_MANUAL.md, STATE_MANAGEMENT_MANUAL.md, CHANGELOG.md), **98 unchanged of 101**. The repair commit reports 56 changed paths: 3 canonical + 53 additive records under `RUN/AMENDED_V3/` and `RUN/AMENDED_V3_EXECUTION/`. Enumerate and classify them yourself.
- All 12 conditional closeout transitions on nine paths remain pending (candidate `RUN/BOUND_STATUS_TRANSITIONS.json`, cross-checked with `RUN/AMENDED_V3/CLOSEOUT_TRANSITIONS.json`); correctly pending is the expected R10′ outcome. FU-1/FU-2 remain optional and excluded. Do not fail this run for their non-implementation and do not reopen settled approvals; report out-of-scope observations separately. A demonstrated regression on a protected surface is in scope.
- **STATE caveat (Tony-authorized):** STATE_MANAGEMENT_MANUAL.md changed in §7 and in its history row. Do not claim whole-file identity for it. Verify its previously accepted passages by exact bytes (R5′ carry-forward below).

## Execution and write boundaries

1. Independently run `git ls-remote --heads origin refs/heads/docs/sync-doctrine-part2-2026-10-15 refs/heads/main`, `git rev-parse HEAD HEAD^`, `git branch --show-current`, `git status --porcelain` in the execution worktree. Pin the actual remote tip as QA_START_SHA. Require expected local/remote SHA, exact parent, branch, clean worktree and expected remote main. Verify BASE → CONTENT → 20f71ee → 8dff354 → 26b050f ancestry (`merge-base --is-ancestor`) and that the candidate is one non-merge child of the parent. Record command/cwd/exit/stdout/stderr. Any mismatch is BLOCKED; never fetch, reset or retarget.
2. Export parent and candidate with read-only `git archive` into fresh empty directories under your scratch area; export BASE only where a protected-original comparison needs it. Keep scripts and outputs outside the exports. Hash installed files in the worktree and committed blobs independently for R6′. Never apply a patch to produce the tested tree.
3. Run every check below even if one fails. Record FAIL/BLOCKED with precise path:line evidence; do not repair. Distinguish semantic reads from literal searches: zero grep hits alone do not establish consistency.
4. Python with `python3 -B -I`; lints with the unchanged candidate-export scripts. No builds, installs, network service calls or deployment commands.
5. Repeat pins, main, worktree status and the three canonical file hashes at the end. A candidate that changed during measurement invalidates the run: BLOCKED, keep collected evidence.

Allowed Git: read-only status, branch --show-current, rev-parse, ls-remote, merge-base --is-ancestor, show, archive, diff, log, ls-tree, cat-file, hash-object without -w. Nothing that writes the tree, index, history or remote. Evidence writes only to the new destination, scratch exports/scripts and normal review-repo session/RESPONSES/RECOVERY bookkeeping. Preserve earlier evidence; record disagreement additively.

## Test matrix

### R4′ — AC16, FC-066 row (the repaired finding)
- Search live scope (36 tier/root documents, 4 `_workflows/*.md`, 4 SVGs; include fences and Version History; case-insensitive) for `fetchProducts` and `services/productServices`. Disposition every hit as one of: (a) inside the labelled API §3 typed-outcome examples (API_AND_SERVICES_MANUAL.md:172–174, 582, 613–622, 785–815, 856–869); (b) inside an explicitly labelled independent illustration whose stated return shape matches its own consumer; (c) a ❌ negated example; (d) naming vocabulary with no result shape; (e) a distinct operation with its own explicit signature (`fetchProductsByIds`, `fetchProductBySlug`). Any hit outside (a)–(e) is FAIL.
- Read the four repaired containers whole, at the candidate: APP_ARCHITECTURE_MANUAL.md §5 Server Components (label sentence before the fence, ~line 501) and Streaming (`ProductListAsync` comment, ~line 613; V3-2 must be present); STATE_MANAGEMENT_MANUAL.md §7 Store + Service Layer GOOD fence (two comment lines, ~809–810) and Store + Server Components (label sentence, ~865). Confirm each label states a return contract (`Promise<Product[]>` / raw JSON array), names it as not the API §3 typed-outcome service, and that the consumer in the same container actually uses that shape (`initialProducts: Product[]`, `<ProductList products={products} />`).
- Confirm executable code and imports in those four containers are byte-identical to the parent except the added comment/prose lines (the only diff lines in both manuals are the label insertions and the history-row clause). Labels must not alter behavior; a changed import path or new service implementation is FAIL.
- FC-022, FC-038 and the other 28 withdrawal rows: re-grade on byte-identity of their documents to `8dff354` (see carry-forward); do not re-read unless a document changed.

### R6′ — AC2 exact installation
All 101 index paths: installed worktree file hash = committed blob at the candidate = `AMENDED_V3/BOUND_EXECUTION_INDEX.json` successor hash. 98 paths byte-identical to `8dff354`; the three changed paths equal `AMENDED_V3` proposed content. Every pre-existing file outside the 101 is byte-identical to `8dff354`.

### R7′ — AC25/26/27 metadata
ARCH header `Version 1.4 · Date 2026-10-18 · Status Active` and STATE header `Version 1.3 · Date 2026-10-18 · Status Active` unchanged. Exactly one amended existing history row per document (ARCH ~1289, STATE ~1111) carrying `QA-P4 repair: RV2-F01 (AC16/FC-066 labels)`; no new rows. CHANGELOG: 39 current-run rows; only rows 56 and 60 amended with the same clause; the six AMENDED-v2 clauses (rows 43, 54, 55, 57, 58, 59 per your own enumeration) and all other rows unchanged. MANIFEST byte-identical.

### R8′ — AC29/AC31 lints
Run the unchanged lint suite from the candidate export (`python3 -B -I lints/run_all.py`): PASS, zero hits. `lints/` and `.github/` byte-identical to `8dff354`.

### R10′ — AC33 transitions
All 12 transitions on nine paths remain in their pre-transition state (old text present, new text absent) at the candidate; no closeout commit exists after the candidate.

### R11′ — AC32 authorization, commit and push
One non-merge commit, subject `repair QA-P4 RV2-F01 (AMENDED-v3 55537c64…)` naming the full index hash, parent `8dff354`, author attributable, on the authorized working branch; the Gate 2 record is in the commit and its recorded time precedes the commit time; remote tip = local HEAD; main unchanged at BASE; clean tree. Assess receipts and ancestry; do not claim Git history proves the absence of every past remote operation (O-1 structure-only grading).

### R12′ — AC1 total scope
Changed paths parent→candidate = exactly 3 canonical + additive records under `RUN/AMENDED_V3/` and `RUN/AMENDED_V3_EXECUTION/` (56 total per the receipt; count them yourself). No frozen record overwritten (R1 spec, maps, Gate 2 records, both Fable verdicts, AMENDED_V1/V2 records, QA_PHASE4 evidence): compare their blobs to `8dff354`. Archives, templates, workflows, SVGs, `10x Lab/`, `_SKILLS/`, root files unchanged.

### Carry-forward — R1, R2, R3, R5, R9 (no re-execution)
Record CARRIED (PASS on `8dff354` evidence remains valid) only where every document the prior Executor graded for that check is byte-identical to `8dff354` at the candidate: R1 (BLUEPRINT, ARCHITECT, DESIGNER, ENGINEER, HANDOFF_PACKAGE, FFM, BIM), R2 (ENGINEER, QAM, DEPLOYMENT), R3 (ENGINEER), R9 (31 archives, 25 templates, 4 workflows + 4 SVGs, two `10x Lab/` files, frozen records). Cite the prior evidence manifest hash.
**R5′ (AC18) — STATE changed, so verify by passage, not by file:** extract from git at both `8dff354` and `26b050f` and compare bytes: STATE §4 Persistence (lines 475–620), §5 Hydration & SSR (621–658), §6 Store Templates (659–790), the raw-contact exclusion comment (519) and the RUL-13 default paragraph (779–786). Every STATE line before 809 is expected identical in content and number; confirm independently and state the first differing line. TESTING_PLAYBOOK, AUTH_MANUAL and ECOMMERCE_AND_PAYMENTS_MANUAL: byte-identical to `8dff354`. If all hold, R5′ = PASS (carried by exact passage); otherwise re-read the AC18 sites.

## Evidence requirements and handback

Every check gets PASS / FAIL / BLOCKED / CARRIED, with OBSERVATION entries separate. No "PASS WITH…", acceptance, certification or QA Lead verdict. Required files in the new EXECUTOR_EVIDENCE:
- `EXECUTOR_REPORT.md`: identity/independence, scope, every result, findings with severity and path:line evidence, limitations, next owner.
- `R_RESULTS.json`: R4′, R6′, R7′, R8′, R10′, R11′, R12′, R1, R2, R3, R5′, R9 with mapped ACs, status, evidence pointers, rationale, finding IDs.
- `QA_START.json` / `QA_END.json`; `INPUT_IDENTITIES.json` (ZIP/index/patch/spec/approval/prior-manifest hashes and authority chain); `COMMANDS.json` (command, cwd, exit, stdout/stderr, failures included).
- `MANUAL_READS.md`: line-numbered candidate quotes and whole-container reasoning for the four R4′ containers, the two history rows, the two CHANGELOG rows and the R5′ passages.
- `PROPAGATION.tsv`: every `fetchProducts` / `services/productServices` hit with disposition (a)–(e) and rationale.
- `WITHDRAWAL_ROWS.json`: all 31 rows with status and basis (independent read or byte-identity carry).
- `RAW/` and `scripts/`: independent scripts, hashes, trees, lint output, diffs sufficient to reproduce.
- `SHA256SUMS.txt`: every evidence file except itself; verify after sealing.
Redact any real secret or personal datum; instructional placeholders are not secrets.

Write the matching response artifact and session/RECOVERY bookkeeping in the review repo. Return one consolidated handback ZIP in `/home/moose/Downloads/` named `QA_AMENDED_V3_EXECUTOR_26b050f_<date>.zip`; state its SHA-256, the actual QA_START_SHA, evidence path, evidence-manifest SHA-256, counts over the 12 entries and every FAIL/BLOCKED finding. Stop for Fable. Even a fully favorable retest applies no closeout transition and authorizes no merge or release.

---
Response: agent_docs/RESPONSES/response_2026-10-20_142831_amended-v3-executor-assignment.md
