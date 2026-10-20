QA EXECUTOR — PHASE 4: INDEPENDENT VERIFICATION OF THE INSTALLED DOC SYNC (ONE PASS)

You are a FRESH Claude Code session launched by Tony (Director). Your seat is
QA EXECUTOR for run SYNC_2026-10-15_doctrine-part2, reporting to Fable (QA Lead).
You are not Cody (Engineer), not Jarvis (Architect), not Fable. You have never
seen this candidate before. Identify your seat and session start time in your
report. You produce evidence and per-AC results; you do NOT issue the verdict.

WORKING REPO (write evidence here only):
/home/moose/Documents/app-factory-docs-v1
RUN = _AUDIT/SYNC_2026-10-15_doctrine-part2

CANDIDATE (read-only; never modify, never run anything that writes there):
worktree  /home/moose/Documents/app-factory-docs-sync-execution
branch    docs/sync-doctrine-part2-2026-10-15
expected tip        20f71ee932ed21c0878cb3a0f39c6fbe90d0a793
CONTENT_SHA         ef35d26d82f1904da6ed33663ad647e4ee16fe98
BASE_SHA            9c179392f79b70da099121fc357d3107ad3bb86e
landing date        2026-10-18

READ FIRST, IN THIS ORDER (all under the working repo):
1. RUN/QA_PHASE4/QA_EXECUTOR_PROMPT.md               (this file)
2. RUN/QA_PHASE4/OVERRIDES_AND_ALIGNMENT.md           (O-1…O-8: how Tony's rulings change grading)
3. RUN/QA_PHASE4/AC_EXECUTION_CHECKLIST.md            (your full assignment, AC1…AC38 + 10X-COPY)
4. RUN/QA_RETEST_AF01/DOCSET_SYNC_ACCEPTANCE_SPEC_AMENDED_V1_R1.md
   SHA-256 2a3867cacef11c6bb0419a4c71229479efe703cee9fbcc1e4f71c0ac8e63f0fc — verify before use
5. RUN/QA_PHASE4/QA_READINESS_RECORD.md               (Fable's precondition evidence; context only)
6. /home/moose/Documents/app-factory-docs-sync-execution/_AUDIT/SYNC_2026-10-15_doctrine-part2/SYNC_HANDOFF.md
   (Engineer's handoff; context, not evidence)

DO, IN ONE PASS:
A. Pin QA_START_SHA: git ls-remote --heads origin refs/heads/docs/sync-doctrine-part2-2026-10-15
   (run in the candidate worktree). Record it with git rev-parse HEAD, git status --porcelain and
   git ls-remote origin refs/heads/main. If QA_START_SHA != expected tip, != worktree HEAD,
   porcelain non-empty, or main != BASE_SHA: write RUN/QA_PHASE4/EXECUTOR_EVIDENCE/BLOCKED.md and stop.
B. Verify ancestry: CONTENT_SHA is an ancestor of QA_START_SHA; BASE_SHA is an ancestor of CONTENT_SHA.
C. Export pristine trees with git archive (BASE, CONTENT_SHA, QA_START_SHA) into your scratchpad and
   grade the export, not the worktree files.
D. Execute every item in AC_EXECUTION_CHECKLIST.md: all 38 acceptance criteria, including the
   installed-file hash checks (AC2, AC22, AC23, AC24, AC30, AC38) and the mandatory manual
   semantic/Markdown reads (spec §5.1–§5.5: AC5–AC20, AC34, AC37) with path:line quotations,
   plus the 10x exact-copy check. Re-run every check yourself; the Engineer's PHASE3_EXECUTION
   records are the object under test, not your evidence.
E. Apply the overrides exactly: AC32 is graded on structure and hygiene (agents may run scoped
   Git and push the working branch; Tony creates the PR and merges) — do not fail on author
   identity or on a push having happened; the two 10x Lab playbooks are authorized standalone
   additions checked for exact copying only; the landing date is 2026-10-18 and the bound
   indexes (RUN/BOUND_EXECUTION_INDEX.json, RUN/BOUND_STATUS_TRANSITIONS.json) are the date
   authority; all 12 conditional closeout transitions are deliberately PENDING — grade the
   pre-closeout candidate and report "correctly pending" for AC33/AC38 closeout clauses.
F. Write ONE consolidated evidence package to
   /home/moose/Documents/app-factory-docs-v1/_AUDIT/SYNC_2026-10-15_doctrine-part2/QA_PHASE4/EXECUTOR_EVIDENCE/
   with exactly the layout in checklist §8 (EXECUTOR_REPORT.md, AC_RESULTS.json, QA_START.json,
   INPUT_IDENTITIES.json, COMMANDS.json, RAW/, MANUAL_READS.md, scripts/, SHA256SUMS.txt).
   Every cited command carries cmd, cwd, exit code and unfiltered output.
G. Bookkeeping in the working repo: session file entry (agent_docs/SESSIONS/), one RESPONSES
   file mirroring EXECUTOR_REPORT.md, RECOVERY.md header line. No other writes.

RULES:
- Git is READ-ONLY for you: ls-remote, rev-parse, merge-base, show, archive, diff, log,
  ls-tree, cat-file, hash-object (never -w). No fetch, checkout, switch, stash, worktree add,
  clean, reset, add, commit, push. If something seems to need a Git write, record it as BLOCKED
  and continue with everything else.
- No implementation edits, no changes to the candidate worktree, no changes to main, no merge,
  no PR. Do not touch frozen records (UPDATE_MAP.md, the spec, AMENDED_V1/, QA_RETEST_AF01/).
- Per-AC result vocabulary: PASS / FAIL (exact path:line or hash) / BLOCKED / OBSERVATION.
  Out-of-scope items (spec §1 exclusions XB-01…05, GAP-01…06, D-3 punctuation, kit facts) are
  OBSERVATION, never FAIL. Do not write PASS WITH…, "accepted", "certified" or any verdict.
- Do not restart intake or specification design. Do not re-grade the proposal; grade the
  installed candidate at QA_START_SHA.
- Run Python as python3 -B -I from your scripts directory; keep scripts out of the exports.
- Finish the whole assignment without asking routine "go" questions. Ask only if a precondition
  is genuinely unmet (then BLOCKED).

RETURN ON SCREEN WHEN DONE:
- QA_START_SHA actually read, and whether it equals the expected tip
- path of EXECUTOR_EVIDENCE/ and the SHA-256 of its SHA256SUMS.txt
- counts: PASS / FAIL / BLOCKED / OBSERVATION over AC1…AC38 + 10X-COPY
- the full list of FAIL and BLOCKED items with their evidence pointers
- then stop. Fable (QA Lead) adjudicates and owns the verdict.
