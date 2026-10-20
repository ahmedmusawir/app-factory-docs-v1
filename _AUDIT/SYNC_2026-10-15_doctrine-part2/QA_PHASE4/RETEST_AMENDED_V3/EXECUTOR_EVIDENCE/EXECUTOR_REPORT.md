# Independent QA Executor report — AMENDED-v3 bounded retest

**Results over 12 entries:** 8 PASS / 4 CARRIED / 0 FAIL / 0 BLOCKED.

**Actual QA_START_SHA:** `26b050fe70de66e74ec8d65bcf9287d4369a91f7`. Parent `8dff354937bc7baf739370a9886497d9d5359186`; authorized branch `docs/sync-doctrine-part2-2026-10-15`. BASE/main `9c179392f79b70da099121fc357d3107ad3bb86e`.
**Seat:** Independent QA Executor, reporting to Fable (QA Lead). **Session start UTC:** 2026-10-20T09:53:28.071581+00:00. **Remote pin captured:** 2026-10-20T09:55:24.409559+00:00.
**Independence:** This conversation did not author, apply, commit or push AMENDED-v3, and did not act as Fable. The assignment was launched by Tony in this fresh conversation. Engineering scripts/results were not used as the test suite; no apply/push/verify_installed helpers were run.

## Scope and authority

The frozen R1 specification, O-1…O-8, Director rulings, both preserved Fable verdicts, attributable AMENDED-v3 Gate 2 and the bounded assignment govern this run. Seven bounded checks were re-executed; R1/R2/R3/R9 were carried by exact identity and R5′ checked by exact passage. No broad Phase 4 restart, approval reopening, repair, closeout, merge or release occurred.
Input hashes and authority paths: INPUT_IDENTITIES.json. Prior accepted evidence manifest: `379dd10450157d0c394684ed7d460d65e42006c7d2a8974e9c778329ad318c38`; all 118 inventoried files verified. Handoff ZIP `5efa6fee26d94598fc6687e22b9cd50bec0b282bb4cf2196ba1b06283cd60485`: safe paths, exact 38-row inventory, extracted into its own scratch directory.

## Per-check results

| Check | ACs | Result | Evidence and rationale |
|---|---|---|---|
| R4′ | AC16 | PASS | All four return-contract labels match their consumers, including V3-2. All 29 occurrences on 26 lines across 44 live-scope files are dispositioned. No executable/import changes. FC-066 independently read; other withdrawal rows preserved by file identity or exact-section re-read. See `MANUAL_READS.md`. |
| R6′ | AC2 | PASS | 101 installed-file hashes equal independently read candidate blobs and the successor index; 98 are parent-identical. Three changed canonical files equal proposed content. Every pre-existing file outside the 101 remains byte-identical. See `RAW/index_hashes.json`. |
| R7′ | AC25, AC26, AC27 | PASS | ARCH v1.4 and STATE v1.3 headers retain 2026-10-18 / Active. One amended existing history row each (1289,1111), no new rows. CHANGELOG retains 39 run rows; only 56/60 changed; six v2 clauses unchanged. MANIFEST exact. See `RAW/metadata.json`. |
| R8′ | AC29, AC31 | PASS | Unchanged candidate-export lint suite exits 0: zero encoding/retired-term/versioned-reference hits across 36 docs and all headers pass. lints/ and .github/ remain exact. See `RAW/lints.txt`. |
| R10′ | AC33 | PASS | All 12 spans on nine paths retain old wording exactly once; new wording is absent. V3 transition plan agrees. Local and remote branch tips remain the candidate, with no later closeout commit on the tested branch. See `RAW/transitions.json`. |
| R11′ | AC32 | PASS | One non-merge child of the exact parent, full-index-hash subject, attributable author, committed Tony approval predating the commit. Ancestry, authorized branch, local/remote candidate, clean worktree and BASE main match; receipts agree. O-1 structure-only assessment. See `RAW/authorization.json`. |
| R12′ | AC1 | PASS | 56 paths independently enumerated: three canonical modifications plus 53 new records under AMENDED_V3/ and AMENDED_V3_EXECUTION/. No frozen overwrite. Protected archives/templates/workflows/SVGs/10x/skills/root files unchanged; all 1,461 existing review-run files also preserved. See `RAW/scope.json`. |
| R1 | AC5, AC6 | CARRIED | Accepted parent PASS carried: BLUEPRINT, ARCHITECT, DESIGNER, ENGINEER, HANDOFF_PACKAGE, FFM and BIM are whole-file byte-identical. No ownership re-execution. See `RAW/carry_forward.json`. |
| R2 | AC9 | CARRIED | Accepted parent PASS carried: ENGINEER, QAM and DEPLOYMENT are whole-file byte-identical. No handoff re-execution. See `RAW/carry_forward.json`. |
| R3 | AC15 | CARRIED | Accepted parent PASS carried: ENGINEER is whole-file byte-identical. No filesystem-authority re-execution. See `RAW/carry_forward.json`. |
| R5′ | AC18 | PASS | PASS carried by exact STATE passages: §§4/5/6, raw-contact comment and RUL-13 default range all identical; lines 1–808 identical and first difference at 809. STATE whole-file identity is false. TESTING, AUTH and ECOMMERCE files remain exact. See `RAW/state_passages.json`. |
| R9 | AC22, AC23, AC24, AC37 | CARRIED | Accepted parent PASS carried for the 31 outgoing archives plus historical QA restoration, 25 templates, four workflows and four SVGs, two 10x files and frozen records. Protected full tree sets match; no archive-original or workflow semantic re-execution. See `RAW/carry_forward.json`. |

## Findings

No FAIL or BLOCKED findings.

The repaired finding was read at APP_ARCHITECTURE_MANUAL.md:501–520 and 592–619, and STATE_MANAGEMENT_MANUAL.md:793–830 and 864–909. Labels at ARCH:501/613 and STATE:809–810/866 agree with array consumers at ARCH:517/616 and STATE:827/877/887. See complete line-numbered containers in MANUAL_READS.md. PROPAGATION.tsv records all 29 literal occurrences, including the three imports that each match both search terms; this is 26 matching lines, not 29 distinct lines.

WITHDRAWAL_ROWS.json contains all 31 rows: 8 PASS (FC-066 plus seven rows with re-read preserved sections in changed documents) and 23 CARRIED. FC-022 and FC-038 carry on exact document identity. No whole-file identity is claimed for ARCH or STATE.

## Observations, separate from findings

- **OBS-V3-01 — execution environment:** Initial sandbox ls-remote exited 128 because GitHub DNS was unavailable. The authorized network-enabled read-only retry succeeded before any grading; final remote check also succeeded. Failure output is retained.
- **OBS-V3-02 — harness correction:** The first measurement invocation assumed DIRECTOR_RELEASE.md existed in the review repo and stopped. It exists in the candidate export; input selection was corrected and the complete measurement script rerun. No candidate defect or candidate write occurred.
- **OBS-V3-03 — carry-forward boundaries:** STATE and ARCH are changed documents. R5 uses exact STATE passages. Seven other withdrawal rows touching these documents were re-read at preserved sections and marked PASS, rather than claiming whole-file carry; the other 23 withdrawal rows are CARRIED and FC-066 is independently PASS.
- **OBS-V3-04 — excluded follow-ups:** FU-1/FU-2 remain optional, excluded and unchanged. No failure or new disposition is assigned to them.

## Preservation and stability

QA_START.json and QA_END.json agree: local and actual remote branch tips are the pinned candidate, exact parent and branch match, the worktree is clean, local/remote main equal BASE, and all three canonical file hashes are stable. The candidate is one non-merge child of 8dff354; every adjacent link BASE→CONTENT→20f71ee→8dff354→26b050f is ancestral. Gate 2 at 2026-10-20T10:38:21.679686+06:00 precedes commit time 10:39:41+06:00. Post-commit handoff/commit/push receipts are correctly absent from their own commit; pre-commit carry/code records and approval match their committed copies.

All 1,461 pre-existing files under the review RUN were fingerprinted and remain unchanged, including accepted evidence, both verdicts and approvals. The candidate's complete parent tree was compared with the successor tree and bytes. No Git write command was run. Candidate exports were created by git archive, not patch application. No BASE export was needed because protected-original checks were carried from accepted parent evidence on exact identity.

## Limits and next owner

These are documentation-level bounded results, not runtime/API/browser certification. No builds, installs, live service tests or deployment commands were run. Git history, current refs and receipts support structural grading; they cannot prove the absence of every past remote operation. Commit author personal details are redacted in delivered telemetry; presence and identity digests are retained. Instructional synthetic addresses and credential placeholders are retained.

**All 12 closeout transitions on nine paths remain pending.** No transition was applied and no later closeout commit exists on the measured branch. Fable owns adjudication and the successor verdict. Stop for Fable; this report grants no merge or release authority.

Evidence inventory is SHA256SUMS.txt (all evidence files except itself), verified after sealing. The final response gives its hash and the consolidated Downloads ZIP hash.
