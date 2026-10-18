# QAM Manifest — RRM-004-CYBER-PHARMA

**Author:** Engineer, at handoff (end of P2) · **Date:** <date -Is> · **Nature:** facts and labeled claims. **This file contains no test plan, no risk ranking, no attack order and no expected value other than the Engineer's own measurements, each marked CLAIM.** The QA Lead's `QA_TEST_PLAN.md` decides what is attacked, in what order, and what "correct" means.

## 1. Identity

| Field | Value |
|---|---|
| Module | RRM-004-CYBER-PHARMA — Dependencies |
| Repo | `cyber-pharma-dev-v1-phase-3` |
| Code baseline | `<baseline>` (RRM-003 `--no-ff` merge on `main`) |
| Candidate | `<the Director's single P2 commit — SHA recorded by the Director at DC-2/DC-3>` |
| Engineering branch / QA branch | `phase-3-rrm004` / `qa/phase-3-rrm004` |
| Provenance chain | RRM-003 merge → pack commit `<sha>` → P0 `<sha>` → P1b `<sha>` → candidate |
| Targets (addendum A-01/A-02) | next `<target-next>` · eslint-config-next `<target-next>` · sharp override `<target-sharp>` |
| Director rulings applied | DD-1 `<pins only / sweep>` · DD-2 `<remove / narrow>` · DD-3 `<target>` · DD-4 `<confirmed>` |
| Engineer platform (PF-14) | `<platform>`; Node `<v>`; npm `<v>` |

## 2. Contract pointers

`../ACCEPTANCE_SPEC.md` (frozen) · `../RULINGS_ADDENDUM.md` rows A-01…A-NN · erratum lane rows: `<none / list>` · ledger row R-009 (resolution appended) · errata `<E-NN / CE-N if any>`

## 3. Product diff (facts)

| Path | Status | What changed |
|---|---|---|
| `package.json` | M | 3 lines: `next`, `eslint-config-next`, `overrides.sharp` |
| `package-lock.json` | M | `<n>` entries moved; families: `<list>`; outside-family: `<none>` (`../evidence/S1_lockfile_moves.txt`) |
| `next.config.js` | M | `images` block per DD-2; `headers()` untouched |

Diff command: `git diff <baseline>..<candidate> -- package.json package-lock.json next.config.js` (= `../evidence/repair.diff`). Everything else: `git diff --name-only <baseline>..<candidate>` lists only the above plus `agent_docs/**` and root-protocol files.

## 4. Reproduction (facts — exact commands, no interpretation)

| Step | Command |
|---|---|
| Clean install from lockfile | `rm -rf node_modules && npm ci` |
| Blank-env build | `rm -rf .next && env NEXT_PUBLIC_SUPABASE_URL= NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY= SUPABASE_SECRET_KEY= NEXT_PUBLIC_SITE_URL= npx next build` |
| Placeholder-env build | `rm -rf .next && env NEXT_PUBLIC_SUPABASE_URL=https://placeholder.invalid NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY=placeholder-publishable SUPABASE_SECRET_KEY=placeholder-secret NEXT_PUBLIC_SITE_URL=http://127.0.0.1:<port> npx next build` |
| Standalone serve (RRM-003 A-02) | `cp -r .next/static .next/standalone/.next/static && cp -r public .next/standalone/public` then `env <same placeholders> PORT=<port> HOSTNAME=127.0.0.1 node .next/standalone/server.js` |
| Header pair + negative controls | `<the exact curl lines from ../evidence/S3_serve_after.txt>` |
| Image optimizer probe | `<the exact curl line>` |
| Negative host probe | `<the exact curl line>` |
| Direct image GETs | `<three curl lines>` |
| Instrument read | `node -p "const v=require('@img/sharp-libvips-<platform>/versions.json'); v.heif+' vips='+v.vips"` |
| Board | `npx tsc --noEmit` · `npx eslint .` · `npx jest --ci` |
| Audit | `npm audit --json` |
| Version listing | `npm ls next sharp eslint-config-next` · `ls node_modules/@img/` |

Placeholder env only; no live Supabase call in any of the above. `.env.local` is not needed for engineering reproduction; it is needed only for the QA authenticated walk (target per DD-3).

## 5. Environment the QA body needs (facts)

| Item | Value |
|---|---|
| Services | npm registry (install, `npm view`, `npm audit`); `fonts.googleapis.com` at build time (`next/font/google` in `src/app/layout.tsx`); the DD-3 Supabase target for the authenticated walk only |
| Ports | one free local port for the served build (Engineer used 36055) |
| Identities and roles required | one ADMIN, one MEMBER on the DD-3 target — **verified to exist by:** `<Director / date>`; named by role only here |
| Browser | any Chromium-class engine the QA Lead's plan names; RRM-003 used Playwright 1.59.1 Chromium via a QA-only driver |
| Tools | Node ≥ 20.9.0, npm, curl, Playwright (already a devDependency: `@playwright/test`) |
| Routes with images (from source, for the Executor to re-derive) | `/` (`HomePageContent.tsx`: `/landing/owedbook-mockup.png`; `NavbarHome.tsx`: `/brand/logo-lockup.svg`) · `/auth` (`NavbarLoginReg.tsx`: `/brand/logo-lockup.svg`) · authenticated routes (`Navbar.tsx`: `/brand/logo-color.svg`) — **the Executor derives this list itself; this row is a claim** |

## 6. Engineer measurements (CLAIMS — the Executor derives its own)

| Measurement | CLAIM | Engineer evidence |
|---|---|---|
| `npm ls` | `<quoted>` | `../evidence/S1_versions.txt` |
| heif BASELINE / AFTER | `<x>` / `<y>` | `../evidence/S1_versions.txt` |
| audit totals before / after | `<…>` / `<…>` | `../evidence/S1_audit_*.json` |
| lockfile moves | `<n>`, families `<…>` | `../evidence/S1_lockfile_moves.txt` |
| builds (routes) · tsc · eslint · jest | `<0/0 (17) · 0 · 0/<w> · 34/164/0>` | `../evidence/S3_board.txt` |
| header pair + negative controls | `<statuses + Cache-Control values>` | `../evidence/S3_serve_after.txt` |
| image probe | `<200 image/webp RIFF…WEBP>` | `../evidence/S3_serve_after.txt` |
| negative host probe | `<400 / recorded>` | `../evidence/S3_serve_after.txt` |
| direct GETs | `<200 ×3>` | `../evidence/S3_serve_after.txt` |
| P2 metrics | `<wall-clock, install time, checks, self-repairs, touches 0, stops 0>` | `../EXECUTION_LOG.md` §Metrics |

## 7. Evidence schema the Executor fills

`QA/evidence/QA_PREFLIGHT.txt` · `QA/evidence/deps/` (npm ls, audit json, versions.json read, platform) · `QA/evidence/board/` (both builds, tsc, eslint, jest json + totals, versions) · `QA/evidence/headers/` · `QA/evidence/images/` (probe headers, hex dump, negative host, direct GETs) · `QA/evidence/browser/` (readiness, per-role matrices, cropped screenshots, sanitized traces, server shutdown) · `QA/evidence/privacy_audit.json` · `QA/evidence/entry_gate.json` · `QA/evidence/static/` (diffs vs baseline, changed paths).

## 8. Governing snapshot

`GOVERNING/` copied from `agent_docs/ACTIONS/RRM-003-CYBER-PHARMA/QA/GOVERNING/`; chain in `GOVERNING/PROVENANCE.md`.

## 9. Not done by engineering (facts)

Authenticated image walk · any install/build/serve on a machine other than the Engineer's · AVIF input · Windows host · deployment.
