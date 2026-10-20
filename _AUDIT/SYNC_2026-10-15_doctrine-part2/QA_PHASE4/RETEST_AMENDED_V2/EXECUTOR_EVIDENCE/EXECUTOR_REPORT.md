# Independent QA Executor report — AMENDED-v2 bounded retest

Seat: Codex, independent QA Executor reporting to Fable. Session started 2026-10-19T13:02:17Z. This fresh conversation did not author or apply the repair. No engineering verifier was executed or accepted as the independent test suite.

Exact QA_START_SHA: `8dff354937bc7baf739370a9886497d9d5359186`
Parent: `20f71ee932ed21c0878cb3a0f39c6fbe90d0a793`
Branch: `docs/sync-doctrine-part2-2026-10-15`
BASE and remote main: `9c179392f79b70da099121fc357d3107ad3bb86e`
Scope: R1–R12 only, under frozen R1 specification, O-1…O-8, original Fable adjudication and additive Director approval. FU-1/FU-2 excluded. Landing date remains 2026-10-18.

## Results

**11 PASS / 1 FAIL / 0 BLOCKED.** All twelve checks completed. Withdrawal subtable: 30 PASS / 1 FAIL across 31 rows. These are Executor results, not a successor QA Lead verdict, certification or release.

| Check | Mapped ACs | Result | Rationale |
|---|---|---|---|
| R1 | AC5, AC6 | PASS | Architect/Designer ownership consistent across live containers; eight E373–E380 spans occur once, old spans absent. 450 mapped-query hits classified; stale-assertion sweep zero. |
| R2 | AC9 | PASS | QA-first handoff explicitly precedes Operations; eight tree entries include ACCEPTANCE_SPEC and QAM. Operations Needs/Verbal Brief unchanged. |
| R3 | AC15 | PASS | No active filesystem-wins/disk-wins phrases; three-line diagram states facts vs requirements and Director conflict routing. |
| R4 | AC16 | FAIL | FC-022/038 repaired; 30 of 31 withdrawal rows pass containment. FC-066 still has unlabeled array callers in architecture/state, inconsistent with named typed-outcome service. |
| R5 | AC18 | PASS | Four manuals express no raw-contact persistence default; exception requirements and invalidation coherent; no positive default contact write found. |
| R6 | AC2 | PASS | 101 unique rows; parent blobs match before, candidate blobs and installed files match proposed bytes/lengths; seven changes, 94 unchanged. All 23 patch hunks and 29 exact edits account for delta; original 380 preserved. |
| R7 | AC25, AC26, AC27 | PASS | Headers/date/status and MANIFEST unchanged. 39 current-run CHANGELOG rows, six amended; one amended existing history row per document. |
| R8 | AC29, AC31 | PASS | Unchanged lint suite passes with zero hits and 36 headers. Seven canonical paths have clean diff --check; full-commit warnings confined to immutable evidence formatting and approved full-file copies. |
| R9 | AC22, AC23, AC24, AC37 | PASS | Protected names/modes/blobs unchanged; 31 outgoing archives match BASE and historical QA blob matches source; 25 QAM templates unchanged; frozen approvals/map/spec/source evidence preserved; both 10x files match original sources. |
| R10 | AC33 | PASS | All 12 transitions on nine unchanged paths correctly pending; old/new counts verified, no activation or closeout commit. |
| R11 | AC32 | PASS | Exact attributable Gate 2 approval, subject, parent and single non-merge child; ancestry and local/remote pins match, tree clean, main unchanged. Receipts support fast-forward push; history alone cannot prove absence of every historical remote action. |
| R12 | AC1 | PASS | 68 changed paths independently enumerated: seven allowed canonical modifications plus 61 additive amendment/approval/verification records, including generator source. STAGED_SCOPE agrees; no frozen overwrite or unexplained addition. |

## Finding RV2-F01 — HIGH — R4 / AC16 / FC-066

The same named `fetchProducts` service still has unlabeled incompatible consumers outside the repaired API manual. API_AND_SERVICES_MANUAL.md:172–174 requires one typed result envelope or an explicitly labeled alternative; :787 declares the discriminated outcome for `@/services/productServices`. APP_ARCHITECTURE_MANUAL.md:505–516 imports that operation and forwards the whole result to `ProductList`; :611–614 repeats the assumption. STATE_MANAGEMENT_MANUAL.md:869–886 forwards the whole result as `initialProducts`, whose declared type is `Product[]`, without checking success or extracting `items`. Its :808–826 “GOOD” service/store example returns raw JSON without declaring the wire shape or labeling an alternative contract.

This is an in-scope unresolved contract contradiction: a typed outcome is not a `Product[]`. Rendering-strategy and service/store-separation headings do not establish an alternative return contract. The API normalization and ISR examples now meet the explicit labeling requirement, but their labels do not govern these other containers. Full line-numbered quotes and consumer traces are in MANUAL_READS.md; all fetchProducts hits, including distinct fetchProductsByIds, are dispositioned in PROPAGATION.tsv. No repairs made.

## Independent evidence and boundaries

The engineering handoff ZIP matches its pinned SHA-256; safe member paths and all 32 SHA256SUMS payload rows verified, with four required originals cross-checked. Semantic inspection used fresh read-only parent/candidate git archives. BASE was separately exported for archive comparisons. 101 committed/installed identities were independently measured; all 857 other pre-existing files are unchanged. The exact approved patch was inspected against old/new hunk coordinates, never applied to produce the tested candidate. Original 380 edits remain exact and new suffix is E381–E409.

36 live tier/root documents plus four workflow Markdown files and four SVGs were searched including fences and history. 155 ten-term hits have individual dispositions; 450 ownership query hits and 354 withdrawal query hits are retained. Complete pinned live documents accompany the quotations. Manual judgments are independent annotations, not copied engineering grades.

All 12 transitions remain pending. Original verdict/approvals and candidate files were not modified. No Git mutation, build, dependency installation, cloud/service test, repair, cleanup acceptance, closeout activation, merge or release occurred.

## Observations and limitations

- OBS-1: Initial sandbox DNS denied the remote read. An approved read-only network retry succeeded; start and end remote/local checks agree. This is not a blocker.
- OBS-2: Full-commit whitespace diagnostics are evidence-formatting warnings: CRLF TSVs, patch context, preserved source quotations and approved complete-file copies. Canonical seven-path diff has zero warnings. No evidence was normalized. The first independent diagnostic parser mistook a quoted path for an error record; that failed attempt and corrected run are retained.
- OBS-3: The historical verdict ZIP is no longer present at its Downloads path. Its committed sealed INPUTS copy matches the recorded historical SHA-256 `b486cccbf29fb677c84173594bfd00c12905b81f2382ae62f9c30572b28f7e5a`; all other source copies compare directly. Missing redundant Downloads location does not invalidate the pinned copy.
- Different diff engines align blank lines differently: the initial raw added/deleted-line sequence comparison is false, while every approved hunk matches parent/candidate coordinates and whole-file exact-edit accounting passes. This is not an installation mismatch.
- Attributable approval/application chronology is records evidence, not a requirement for a prior approval-only commit. Receipts and ancestry support a fast-forward push; Git history cannot prove the absence of every historical remote operation.
- This checks documentation containment and contracts; it does not certify runtime implementations, external APIs, production replacements, rendering fidelity or accessibility. No actual credential/personal data was identified; instructional placeholders were retained.

Next owner: Fable verifies evidence integrity, adjudicates RV2-F01 and issues any additive successor verdict for this exact candidate. Do not infer closeout, merge or release authority from these results.
