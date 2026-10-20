# QA EXECUTOR — AMENDED-v2 complete bounded retest R1–R12

You are a fresh independent QA EXECUTOR session launched by Tony, reporting to Fable (QA Lead). This is one complete bounded retest, not engineering or a new full Phase 4 run. Record your seat, session start UTC time and independence statement. If this conversation previously authored/applied this repair, do not test it: record BLOCKED and request a genuinely fresh session. Do not claim to be Fable or issue the successor verdict.

## Locations and pinned identities

Review repo (evidence writes): `/home/moose/Documents/app-factory-docs-v1`

RUN (relative to either repo): `_AUDIT/SYNC_2026-10-15_doctrine-part2`

Execution worktree (strictly read-only): `/home/moose/Documents/app-factory-docs-sync-execution`

- Branch: `docs/sync-doctrine-part2-2026-10-15`
- Expected QA_START_SHA: `8dff354937bc7baf739370a9886497d9d5359186`
- Exact parent / prior candidate: `20f71ee932ed21c0878cb3a0f39c6fbe90d0a793`
- Original CONTENT_SHA: `ef35d26d82f1904da6ed33663ad647e4ee16fe98`
- BASE / expected main: `9c179392f79b70da099121fc357d3107ad3bb86e`
- Landing date remains `2026-10-18`.
- Successor index: `RUN/AMENDED_V2/BOUND_EXECUTION_INDEX.json`
- Index SHA-256: `b4fe406963b13b650f11d7d688026c88ff37fb1698d6191cdec420247c156bc9`
- Patch: `RUN/AMENDED_V2/EXECUTION_PROPOSAL.patch`
- Patch SHA-256: `86fbfe6f3787c55332bb5d0c741d7ed3296c1f872e3ce26bc4af01b29a0282fd`
- Frozen spec: `RUN/QA_RETEST_AF01/DOCSET_SYNC_ACCEPTANCE_SPEC_AMENDED_V1_R1.md`
- Spec SHA-256: `2a3867cacef11c6bb0419a4c71229479efe703cee9fbcc1e4f71c0ac8e63f0fc`
- Engineering handoff: `/home/moose/Downloads/FACTORY_AMENDED_V2_EXECUTION_HANDOFF_2026-10-19_150618.zip`
- Handoff SHA-256: `a2b4c4cf57b2c93e25686d4c45c28c7302da1ed97c55f3bd219c57bef9f8a422`

Evidence destination (NEW; do not overwrite the previous Executor evidence):
`/home/moose/Documents/app-factory-docs-v1/_AUDIT/SYNC_2026-10-15_doctrine-part2/QA_PHASE4/RETEST_AMENDED_V2/EXECUTOR_EVIDENCE/`

## Read first

1. This prompt. Verify the handoff ZIP hash, member safety and SHA256SUMS inventory; retain the results.
2. In that ZIP: `AMENDED_V2_EXECUTION/FABLE_HANDOFF.md`, `QA_PHASE4/REPAIR_QA_P4/DIRECTOR_DECISIONS_V2.md`, `AMENDED_V2_EXECUTION/COMMIT_RECEIPT.json`, `PUSH_RECEIPT.json`. Cross-check against the review-repo originals. The post-commit receipts intentionally are outside the commit they identify.
3. In the review repo: `RUN/QA_PHASE4/QA_LEAD_VERDICT.md`, `REPAIR_QA_P4/ENGINEER_REPAIR_PROMPT.md`, `REPAIR_QA_P4/REPAIR_FINDINGS.json`, `OVERRIDES_AND_ALIGNMENT.md`, and relevant portions of `AC_EXECUTION_CHECKLIST.md`.
4. Verify/read the frozen spec in the candidate; read `AMENDED_V2/AMENDMENT_V2.md`, the 29 new exact edits, successor index and approved patch, plus the additive Director approval. Original AMENDED_V1 edits, UPDATE_MAP §B, SEARCH_QUERIES, and previous independent MANUAL_READS/withdrawal table are evidence-location aids.

Source precedence: frozen spec plus settled Director rulings and prior Fable adjudication; current attributable AMENDED-v2 approval/scope correction; this bounded assignment. Engineering PASS labels and propagated dispositions are hypotheses to test, not QA evidence. Do not run the engineering apply/verify helper or use its assertions as your independent test suite.

## Alignment for this retest

Preserve O-1…O-8 and all original approvals/verdict bytes. Their old candidate references describe the earlier run. For this assignment, the required tip is **8dff354**, parent **20f71ee**, and the index is **AMENDED_V2/BOUND_EXECUTION_INDEX.json**, not the historical root index. These are explicit successor identities, not spec edits.

R6/R12 use Tony’s approved correction: seven canonical paths (six documents plus CHANGELOG), **94 unchanged of 101**. Audit records are additional run paths, not additions to the canonical 101. The repair commit reports 68 total changed paths: seven canonical plus 61 additive run records; independently enumerate and classify them.

All 12 conditional closeout transitions on nine paths remain pending. Correctly pending is the expected R10/AC33 outcome. Gate 2 is approved for these exact repair bytes; old sealed proposal PENDING labels remain historical and are superseded only by the additive Director approval. FU-1/FU-2 remain optional follow-ups excluded from this repair. Do not fail this bounded run for their deliberate non-implementation or reopen settled approvals. Report out-of-scope observations separately. A demonstrated regression in a protected surface is still in scope.

## Execution and write boundaries

1. Independently run `git ls-remote --heads origin refs/heads/docs/sync-doctrine-part2-2026-10-15 refs/heads/main`, `git rev-parse HEAD HEAD^`, `git branch --show-current`, and `git status --porcelain` in the execution worktree. Pin actual remote tip as QA_START_SHA. Require expected local/remote SHA, exact parent/branch, clean worktree and expected remote main. Verify BASE → CONTENT → parent → candidate ancestry and one non-merge child commit from parent. Record command/cwd/exit/stdout/stderr. A mismatch is BLOCKED; never fetch/reset or silently retarget.
2. Use read-only `git archive` to export parent and candidate into fresh `/tmp` directories. Use BASE/original archive identities where required to validate protected originals. Keep scripts and outputs outside those exports. Perform semantic checks on pinned exports; independently hash real installed files and committed blobs for R6. Do not apply any patch, even as the means of producing the tested candidate.
3. Run all R1–R12 below. A content failure does not end the remaining independent checks. Record FAIL/BLOCKED with precise evidence, do not repair it. Distinguish semantic checks from literal searches; zero grep hits alone cannot establish policy consistency.
4. Run Python scripts with `python3 -B -I`; for lints use the unchanged candidate-export scripts with bytecode disabled. No application builds, dependencies, network service calls, or deployment commands copied from examples.
5. Repeat local/remote pins, main, worktree status and relevant file hashes at end. Changed candidate during measurement invalidates the run: BLOCKED, preserve collected evidence.

Allowed Git: read-only status, branch --show-current, rev-parse, ls-remote, merge-base --is-ancestor, show, archive, diff, log, ls-tree, cat-file, hash-object without -w. No fetch/checkout/switch/stash/worktree add/clean/reset/add/commit/push/merge/PR. No candidate writes. Evidence writes only to the new destination, temporary exports/scripts, and normal review-repo session/RESPONSES/RECOVERY bookkeeping. Preserve earlier evidence even if it appears wrong; record disagreement additively. If destination already contains completed evidence, stop rather than overwrite it.

## Complete test matrix (independent automation AND manual review)

### R1 — AC5/AC6 ownership

Run the map §B ownership searches for FC-008/015/016/017/019/025/026/027, using SEARCH_QUERIES and original checklist. Scan all 36 live tier/root documents plus workflow prose/SVG text; include code fences. Classify each hit by actual context (active, historical, negated). Check stale assertions including “Engineer authors DATA_CONTRACT”, “Architect drafts UI_SPEC”, “Designer revises”, FILE_TREE source-of-truth variants, Engineer produces FILE_TREE, “The Engineer's full output list”, and “different author”.

Independently verify all eight E373–E380 AMENDED-v1 new spans occur exactly once and old spans are absent in their intended containers. Manually read ENGINEER ownership lines and surrounding conversion/greenfield sections: Architect authors both; Brain Drain/pre-authored conversion vs approved APP_BRIEF/before Design greenfield; router preserved. Read adjacent Blueprint/Architect/Designer/FFM/handoff ownership statements to detect contradiction. Quote path:line evidence and justify retained hits.

### R2 — AC9 handoff

Manually read ENGINEER §17 and QAM_PLAYBOOK §3 / DEPLOYMENT_PLAYBOOK §3. Verify self-verified candidate + factual engineering handoff → independent QA on Director-created QA branch → QA Lead certification and Director release → Operations. Inspect the rendered/structural tree: eight entries, original six preserved, ACCEPTANCE_SPEC from Architect and QAM pack including ENGINEERING_HANDOFF, approved plan, results, certificate. Compare What Operations Needs and Verbal Brief byte-exactly with parent. A nearby corrective paragraph cannot excuse a contradictory operative instruction.

### R3 — AC15 RUL-12

Independently scan live scope including diagram/code fences for filesystem-wins/disk-wins phrases; require zero active hits outside actual Version History. Read ENGINEER kit-track diagram in context: disk establishes implementation facts, handbook drift is recorded, requirements conflicts route to Director, approved briefs/governing documents retain authority. Check diagram line structure and existing aligned RUL-12 sites.

### R4 — AC16 withdrawal/contract rows

Build a 31-row withdrawal judgment table using the original Executor table/mapped queries as a locator, but re-evaluate the new candidate yourself. For FC-022 inspect both withdrawn TESTING fences and surrounding prose: no executable seedSubscription or unguarded supabaseAdmin construction in live scope; privileged setup/client construction requires test-project allowlist and authorized identity and fails closed. Do not interpret containment as completed production replacement.

For FC-038 read DATABASE Service Role Bypass and AUTH capability boundary: API route alone never justifies bypass; elevated operation is independently authorized, including background/admin operations; both construction comments agree; no positive default-route instruction survives.

For FC-066 enumerate every fetchProducts hit across live scope (including distinct fetchProductsByIds), read whole service/caller/example containers and labels, and trace result shapes. Validate normalization array alternative, discriminated typed-outcome caller, and independent ISR raw-JSON contract. Inspect architecture/state-manual occurrences too: independently assess whether local context actually justifies retention. Do not accept the Engineer’s “separate example” rationale without examining the consumer and referenced service. Flag any in-scope unresolved contract contradiction with evidence; do not broaden implementation scope or rewrite examples.

For the remaining 28 rows, verify mapped invariant/withdrawal passages and dependent executable surfaces remain unchanged/contained; excerpt survival alone is insufficient if adjacent behavior changed. Record row-level PASS/FAIL/BLOCKED and exact supporting quotations.

### R5 — AC18 RUL-13

Read AUTH Security Best Practices, TESTING dual-verification section, ECOMMERCE checkout policy, and STATE persistence examples/default. Confirm all four express no persistent raw browser contact data by default; approved exception requirements and clearing/account invalidation are coherent with the approved rule. Inspect fences, partialize fields and storage writes for a contradictory contact-persistence recipe. STATE is unchanged; three added policy sentences introduce no persistence example. Re-run the ten-term propagation sweep listed below and disposition every hit yourself.

### R6 — AC2 exact installation

Verify successor index hash; exactly 101 unique paths. For every row independently compute parent blob hash = before_sha256 and candidate blob + installed file hashes = proposed_sha256; check length. Require exactly seven changed and 94 unchanged. Verify seven installed files equal approved PROPOSED_CONTENT; compare actual canonical diff with approved patch/exact edits without using a patched export as your candidate. Preserve original 380 edit records and new E381–E409 ordering; do not mistakenly replay all 409 directly against BASE without original metadata/date-binding stages.

### R7 — AC25/26/27 metadata

Compare six header version/date/status lines with parent and MANIFEST cells; landing date 2026-10-18 unchanged. MANIFEST byte-identical. Count 39 current-run CHANGELOG rows (not all historical rows), six amended existing rows, no added run rows. Each changed document has one amended existing run-history row, no new row or header bump. Inspect Markdown table columns/order and history placement; only the approved QA-repair clauses are added.

### R8 — AC29/AC31 lints

Verify lints/ and .github/ bytes against parent, then independently execute `python3 -B -I lints/run_all.py` in candidate export with PYTHONDONTWRITEBYTECODE=1. Retain full command/output, require suite PASS, zero encoding/retired-term/versioned-reference hits and header-presence PASS. Inspect seven-path canonical whitespace/Markdown validity. Preserve exact evidence formatting; classify separately any full-commit whitespace warnings from immutable patch context, source quotes or TSV CRLF (verify the explanation, do not normalize evidence).

### R9 — AC22/23/24/37 preservation

Independently enumerate parent/candidate trees, compare names/modes/blob hashes for archives (31 outgoing plus QA v1.0 and other existing archive contents), 25 QAM templates, workflows/SVG/assets, both standalone 10x files, _SKILLS, lints/.github and root instructions. No removal/addition/change in protected sets. Check 10x against existing authorization/source hashes if available; no doctrine integration. Verify frozen UPDATE_MAP, INTAKE_SNAPSHOT, AMENDED_V1, QA_RETEST_AF01/spec, prior approvals and source evidence byte-identical. New copied INPUTS are evidence copies, not permission to mutate originals.

### R10 — AC33 transitions

Use candidate `RUN/BOUND_STATUS_TRANSITIONS.json` and original transition plan to enumerate all 12 transitions/nine paths; verify every expected pre-transition span and count, and byte-identical transition paths relative to parent. Read headers, MANIFEST statuses, template README provenance and four workflow statuses in context. No closeout commit, activated status, or claimed cleanup/release acceptance. Record each transition as correctly pending; do not apply any.

### R11 — AC32 authorization, commit and push

Verify additive Director Gate 2 record names exact approved index/patch, source approval and seven-path scope; original decisions preserved. Check commit parent, single non-merge repair commit, subject `repair QA-P4 F01–F05 (AMENDED-v2 <full index sha>)`, tree and push receipts, actual remote match and clean working tree. Grade authorized agent Git on structure/hygiene per O-1, not author identity. Verify main unchanged and ancestry consistent with fast-forward push; explain that receipts/ancestry support no-force-push claims but Git history alone cannot prove the absence of every historical remote action. Approval/application chronology is attributable records evidence, not a separate prior approval commit requirement.

### R12 — AC1 total scope

Derive full parent→candidate name/status list independently. Canonical change allowlist:
- 02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md
- 03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md
- 04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md
- 04_REFERENCE_MANUALS/AUTH_MANUAL.md
- 04_REFERENCE_MANUALS/DATABASE_MANUAL.md
- 04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md
- CHANGELOG.md

Classify all remaining changed paths individually as additive amendment/approval/verification records. Compare claimed 68 paths / 61 additions to actual tree and STAGED_SCOPE, but do not use the Engineer’s list as the sole allowlist: check purpose, no frozen-record overwrite and copied sealed bytes. No canonical change outside seven; no new root instruction, main/skill/inbox/deployment change. Surface unexplained additions as findings.

## Evidence requirements and handback

Every R gets PASS / FAIL / BLOCKED, with OBSERVATION entries separate. No PASS WITH..., acceptance, certification or QA Lead verdict. Include all 12 even if some fail. Keep result totals consistent; include mapped ACs without regrading all 38 ACs. Previous adjudication stays intact.

Required files in new EXECUTOR_EVIDENCE:
- EXECUTOR_REPORT.md: identity/independence, scope, all R results, findings with severity and path:line evidence, limitations and next owner.
- R_RESULTS.json: exactly R1–R12 with mapped ACs, status, evidence pointers, rationale and finding IDs.
- QA_START.json / QA_END.json: actual pins, timestamps, status and main checks.
- INPUT_IDENTITIES.json: source paths/hashes and authority chain, including exact ZIP/index/patch/spec/approval.
- COMMANDS.json: command, cwd, exit, full safe stdout/stderr; record failures as well as successes.
- MANUAL_READS.md: actual candidate line-numbered quotes, whole-container reasoning and retained-hit decisions for R1–R5/R7/R10.
- WITHDRAWAL_ROWS.json or .md: all 31 rows, independent judgments; do not copy old grades.
- PROPAGATION.tsv: case-insensitive searches for “different author”, “filesystem wins”, “disk wins”, “hands off to Operations”, “seedSubscription”, “supabaseAdmin”, “appropriate for:”, “fetchProducts”, “raw contact”, “persist”; explicit scope incl fences/history; every hit dispositioned with rationale. Unreviewed hit blocks the relevant R.
- RAW/ and scripts/: independent scripts and raw search/hash/tree/lint/structural evidence sufficient to reproduce results.
- SHA256SUMS.txt: all evidence files except itself; verify inventory after sealing. Preserve evidence if blocked.

Record only safe evidence; if actual secrets/personal information are encountered, redact them and record safe location/count plus the limitation. Do not treat instructional placeholders as secrets.

Write a matching response artifact and append session/recovery bookkeeping in the review repo. Return one consolidated handback, no per-finding questions or partial packages. State actual QA_START_SHA, evidence path, evidence-manifest SHA-256, counts over R1–R12, and all FAIL/BLOCKED findings. Stop for Fable to adjudicate. Do not modify the prior verdict or issue a successor verdict yourself.

After return, the QA Lead will verify evidence integrity/independence, reconcile each R and confirmed F01–F05, preserve original adjudication, and issue an additive successor Phase 4 verdict for this exact candidate. Even a favorable retest does not apply the 12 closeout transitions or authorize merge/release.
