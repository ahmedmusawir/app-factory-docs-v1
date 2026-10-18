# RRM-004-CYBER-PHARMA — Environment Preflight (Engineering)

Machine-checkable, read-only, no secrets printed. The Engineer runs every row at the start of P1 (report) and again at the start of P2 (gate). Any FAIL at P2 is stop condition 1: write the table to `evidence/PREFLIGHT_P2.txt`, report, wait. Do not begin S1 on a failed preflight. Rows carried from RRM-003 keep its rulings: PF-05 passes at P1 when the only dirty paths are this session's own root-protocol files (RRM-003 A-01) and must be literally empty at P2; the standalone server gets `.next/static` and `public/` copied in before boot (RRM-003 A-02).

`<platform>` below is the value of `node -p "process.platform+'-'+process.arch"` joined the way `@img` names it (`linux-x64`, `linuxmusl-x64`, `darwin-arm64`, …); on Linux the glibc/musl split decides `linux-` vs `linuxmusl-` (PF-14).

| # | Check | Command (read-only) | Pass condition |
|---|---|---|---|
| PF-01 | Branch | `git rev-parse --abbrev-ref HEAD` | `phase-3-rrm004` |
| PF-02 | Baseline identity | `git log --oneline --merges -3 main` | the `--no-ff` merge of `qa/phase-3-rrm003` is found; its full SHA recorded as `<baseline>` |
| PF-03 | Baseline is an ancestor | `git merge-base --is-ancestor <baseline> HEAD && echo ok` | `ok` |
| PF-04 | Nothing above baseline but docs | `git diff --stat <baseline>..HEAD -- src/ supabase/ scripts/ public/ package.json package-lock.json next.config.js` | empty |
| PF-05 | Clean tree | `git status --porcelain` | empty (P1: own root-protocol files only, A-01) |
| PF-06 | Node / npm meet both targets' engines | `node -v && npm -v` | Node ≥ 20.9.0 (`next` 16.3.x and `sharp` 0.35.x both declare `>=20.9.0`) |
| PF-07 | Dependencies installed at baseline | `npx next --version && npx jest --version && npx tsc --version && npx eslint --version` | all four print; `next` prints the baseline version (expect `16.2.12`); no install performed |
| PF-08 | Env key names present (names only) | `grep -cE '^(NEXT_PUBLIC_SUPABASE_URL\|NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY\|SUPABASE_SECRET_KEY\|NEXT_PUBLIC_SITE_URL)=' .env.local` | `4` (values never read or printed) |
| PF-09 | Port free | `node -e "require('net').createServer().listen(36055,'127.0.0.1').on('listening',function(){this.close();console.log('free')}).on('error',()=>console.log('busy'))"` | `free` |
| PF-10 | Evidence lane writable | `touch agent_docs/ACTIONS/RRM-004-CYBER-PHARMA/evidence/.w && rm agent_docs/ACTIONS/RRM-004-CYBER-PHARMA/evidence/.w && echo ok` | `ok` |
| PF-11 | Disk headroom (install churn + two builds + a scratch copy) | `df -h . \| tail -1` | ≥ 4 GB free |
| PF-12 | Registry reachable and targets resolvable | `npm view next@<target-next> version && npm view sharp@<target-sharp> version && npm view eslint-config-next@<target-next> version` (P1: use the floors `16.3.3` / `0.35.4` if targets are not yet ruled) | three version strings print; no install performed |
| PF-13 | Build-time font fetch reachable | `curl -s -o /dev/null -w '%{http_code}\n' 'https://fonts.googleapis.com/css2?family=Saira:wght@400&display=swap'` | `200` (`src/app/layout.tsx` uses `next/font/google`; a build cannot complete without it — authoring-time lesson from a sandboxed build) |
| PF-14 | Platform identity and libc | `node -p "process.platform+'-'+process.arch"` and `node -p "process.report.getReport().header.glibcVersionRuntime \|\| 'musl-or-none'"` | platform string recorded; `<platform>` derived and recorded |
| PF-15 | Baseline image stack present for this platform | `ls node_modules/@img/ \| grep -E "^sharp-(libvips-)?<platform>$"` and `npm ls sharp next` | both `@img/sharp-<platform>` and `@img/sharp-libvips-<platform>` listed; `npm ls` shows the baseline `next` and `sharp overridden` |
| PF-16 | Baseline instrument value (the before) | `node -p "const v=require('@img/sharp-libvips-<platform>/versions.json'); v.heif+' vips='+v.vips"` | prints; expected below the floor (`1.23.1` on libvips 1.3.2 — that is the defect); recorded verbatim in `evidence/S1_versions.txt` under BASELINE |
| PF-17 | Baseline board is green (pipes-alive) | `rm -rf .next && env NEXT_PUBLIC_SUPABASE_URL=https://placeholder.invalid NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY=placeholder-publishable SUPABASE_SECRET_KEY=placeholder-secret NEXT_PUBLIC_SITE_URL=http://127.0.0.1:36055 npx next build` then `npx tsc --noEmit` then `npx jest --ci` | build exit 0 (record route count; expect 17) · tsc 0 · jest all pass, zero skipped (record suites/tests; expect 34/164 after RRM-003) |
| PF-18 | Standalone server boots (with A-02 static copy) | `cp -r .next/static .next/standalone/.next/static && cp -r public .next/standalone/public` then `env <same placeholders> PORT=36055 HOSTNAME=127.0.0.1 node .next/standalone/server.js &` then `curl -s -o /dev/null -w '%{http_code}\n' http://127.0.0.1:36055/` | `200`; server left up only for PF-19, then stopped and PF-09 confirmed again |
| PF-19 | Baseline served proofs (the before) | with the server up: `curl -sI http://127.0.0.1:36055/ \| grep -iE '^HTTP\|cache-control'` · `curl -sI http://127.0.0.1:36055/_next/static/chunks/<any>.js \| grep -iE '^HTTP\|cache-control'` · `curl -s -o /dev/null -D - -H 'Accept: image/webp' 'http://127.0.0.1:36055/_next/image?url=%2Flanding%2Fowedbook-mockup.png&w=1080&q=75' \| grep -iE '^HTTP\|content-type\|cache-control'` | all three recorded verbatim with status lines to `evidence/S3_serve_before.txt`; expected: `/` 200 with `no-store`; chunk 200 with `immutable` (RRM-003's fix); image 200 `image/webp` (the baseline optimizer works — so a regression after the bump is attributable) |
| PF-20 | Governing QA snapshot source exists | `ls agent_docs/ACTIONS/RRM-003-CYBER-PHARMA/QA/GOVERNING/` | lists `QA_PLAYBOOK.md` and `PROVENANCE.md` |
| PF-21 | No Director checkpoint pending mid-run | read `DIRECTOR_CHECKPOINTS.md` | DC-1 satisfied (plan approved, DD-1…DD-4 ruled, rows on disk); no other checkpoint falls inside P2 |

Engineering needs no browser, no real credentials and no live service. The authenticated image walk is QA's; the QA Executor runs `QA/QA_ENVIRONMENT_PREFLIGHT.md` before opening a browser.
