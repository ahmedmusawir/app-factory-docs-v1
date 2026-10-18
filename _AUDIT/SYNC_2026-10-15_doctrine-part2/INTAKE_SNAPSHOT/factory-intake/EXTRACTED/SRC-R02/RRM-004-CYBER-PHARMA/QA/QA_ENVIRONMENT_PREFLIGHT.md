# QA Environment Preflight — RRM-004-CYBER-PHARMA (QAM pilot)

**Version:** v0.1 Architect draft, 2026-09-30 · **Ratified by the QA Lead:** <date, position> · **Frozen at:** DC-4.

Machine-checkable, read-only, no secrets printed. The QA Executor runs every row **first**, before any install, build or browser action, and writes the table with results and `date -Is` to `QA/evidence/QA_PREFLIGHT.txt`. Any FAIL is stop Q1. A gate, not a checklist: the expensive body does not start on a failed row. `<qa-port>` is a free port the Executor chooses (record it); `<platform>` per the Engineering preflight PF-14 method, on the Executor's own machine.

| # | Check | Command (read-only) | Pass condition |
|---|---|---|---|
| QF-01 | Branch and HEAD | `git rev-parse --abbrev-ref HEAD && git rev-parse HEAD && git status --porcelain` | `qa/phase-3-rrm004`; HEAD recorded; porcelain empty |
| QF-02 | Candidate pinned and ancestral | `git merge-base --is-ancestor <candidate from QAM_MANIFEST.md> HEAD && echo ok` | `ok` |
| QF-03 | Docs-only successor | `git diff --stat <candidate>..HEAD -- src/ package.json package-lock.json next.config.js supabase/ scripts/` | empty |
| QF-04 | Manifest complete | every field of `QAM_MANIFEST.md` non-placeholder (`grep -c "<" QA/QAM_MANIFEST.md` over the template's field cells) | 0 unfilled fields; the plan's provenance header names the QA Lead and a date after the candidate commit |
| QF-05 | Node / npm | `node -v && npm -v` | Node ≥ 20.9.0 |
| QF-06 | Registry reachable | `npm view next@<target-next> version && npm view sharp@<target-sharp> version` | both print (targets from `../RULINGS_ADDENDUM.md` A-01/A-02) |
| QF-07 | Build-time font fetch reachable | `curl -s -o /dev/null -w '%{http_code}\n' 'https://fonts.googleapis.com/css2?family=Saira:wght@400&display=swap'` | `200` |
| QF-08 | Browser engine present | `npx playwright --version` and `node -e "require('playwright').chromium.executablePath()"` (or the equivalent for the engine the plan names) | version prints; executable path exists (`test -x`) |
| QF-09 | Display / headed capability for DC-5 | `echo ${DISPLAY:-none}` (or the platform equivalent); a headed launch smoke test that opens and closes `about:blank` | a visible browser can be shown to the Director for credential entry, or the plan's declared alternative (headed remote, VNC) is confirmed working |
| QF-10 | Target environment declared and reachable (DD-3) | read the DD-3 row in `../RULINGS_ADDENDUM.md`; `grep -cE '^(NEXT_PUBLIC_SUPABASE_URL\|NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY)=' .env.local` (names only); `curl -s -o /dev/null -w '%{http_code}\n' "$(node -e "require('dotenv').config({path:'.env.local',quiet:true});process.stdout.write(process.env.NEXT_PUBLIC_SUPABASE_URL+'/auth/v1/health')")"` | DD-3 names the target; 2 key names present; health endpoint returns `200`/`401`/`404` (reachable — any non-network-error status); **the URL value is not written to evidence** — record only the status |
| QF-11 | Test identities declared | the DD-3 row (or `QAM_MANIFEST.md` §Environment) names one ADMIN and one MEMBER account **by role only** and states who verified they exist and when | both roles named with a verification date ≤ 7 days old; if not, stop Q1 and ask the Director to confirm the accounts before the run (this is the RRM-002/RRM-003 lesson) |
| QF-12 | Known-instrument probe | in a throwaway jsdom or a headless page on `about:blank`: a native `<button>` receives `keydown Enter` and `keydown Space` and the click count is 1 for each | both fire — establishes the browser's native Enter/Space behavior before any product finding is attributed (RRM-003 QA-F02 lesson) |
| QF-13 | Ports and lanes | `node -e "require('net').createServer().listen(<qa-port>,'127.0.0.1').on('listening',function(){this.close();console.log('free')}).on('error',()=>console.log('busy'))"` · `touch QA/evidence/.w && rm QA/evidence/.w && echo ok` · `df -h . \| tail -1` | `free` · `ok` · ≥ 4 GB |
| QF-14 | Privacy scanner runs | the scanner the plan names (RRM-003's `sanitize_trace.py` allowlist approach, or the Executor's own) executes against an empty `QA/evidence/` and exits 0 | exit 0 with "0 files, 0 hits" |

The Executor's own install (`rm -rf node_modules && npm ci`) and builds come **after** this table passes. The Director is asked for nothing during the preflight; QF-11's stop is the one exception and it happens before any expensive step.
