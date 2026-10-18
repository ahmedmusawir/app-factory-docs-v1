# RRM-004-CYBER-PHARMA — Dependencies — Brief

**Version:** 1.0 · 2026-09-30 · **Architect** authored · **Director approval:** campaign map §7 (2026-09-20, D4) · **Pilots:** one-shot Engineering (RRM-003 shape) + first QAM run on the QA side (QA Lead's pilot plan v0.1; Architect's QAM opinion 2026-09-29)
**Code baseline:** post-RRM-003 `main` (RRM-003 merge commit; SHA recorded at P1) · **Branch:** `phase-3-rrm004` · **Ledger rows:** R-009 (accept; F9 · A-003)

## Why this module exists

Recon R6 verified that the installed `next` and `sharp` match published advisories. At authoring (2026-09-30, read from the lockfile and the registry, not from earlier conversation):

| Package | Installed (lockfile) | Advisory | Fixed in | Registry latest stable |
|---|---|---|---|---|
| `next` | 16.2.12 | GHSA-p293-qw3h-jr36 (critical, unauthenticated RCE, Windows-hosted) · GHSA-2xp9-vwfh-vxw4 (critical, unauthenticated RCE in the Image Optimization API on AVIF input) — both `>=16.0.0 <16.3.3` | 16.3.3 | 16.3.7 |
| `sharp` (override) | 0.35.3 | GHSA-rgj7-g3m4-5g8c (high) — libheif heap overflows GHSA-g89c-p67h-r497 / GHSA-2jg2-4ch7-h545 — `<0.35.4` | 0.35.4 (bundles libvips 1.3.3 → libheif 1.23.2) | 0.35.5 (libvips 1.3.4 → libheif 1.23.5) |
| `@img/sharp-libvips-*` | 1.3.2 (libheif 1.23.1) | via `sharp` | 1.3.3 | 1.3.4 |

`npm audit` on the baseline lockfile: 1 critical · 4 high · 1 moderate · 1 low (7). Of those, `next` (critical) and `sharp` (high) are this module's targets. The other three highs (`brace-expansion`, `browserslist`, `js-yaml`), the moderate (`baseline-browser-mapping`) and the low (`postcss-selector-parser`) are transitive, sit in the eslint / browserslist / istanbul / postcss build chains, and all have in-range fixes — a `--package-lock-only` dry run at authoring showed `npm audit fix` (no `--force`) resolving all of them with 18 further lockfile entries moved and `package.json` untouched. Whether to take that sweep is **DD-1**, the Director's call, because the map §7 wording said "not fixed here" before anyone knew the fixes were in-range.

A dry run of the pins at authoring (scratch copy, `16.3.7` / `0.35.5`): 41 lockfile entries moved, all in the `next`, `@next/*`, `eslint-config-next`, `sharp`, `@img/*`, `@emnapi/runtime`, `@swc/helpers` families; `npm ci` clean; tsc 0; eslint 0 errors / 35 warnings; jest 34 suites / 164 tests; placeholder build 17 routes; standalone served `/` with `no-store`, a chunk with `public, max-age=31536000, immutable`, and `/_next/image` returned a 1080×626 `image/webp` through the new sharp. Zero critical after the pins; the three transitive highs remain until DD-1. **This is authoring evidence that the module is feasible, not the Engineer's proof** — the Engineer measures everything again on the real tree with the targets the Director rules.

## Inputs and reconciliation

| Input | Specimen | Status |
|---|---|---|
| Fable F9 · Astra A-003 | reviews | VERIFIED on disk (recon R6); Astra's Dockerfile does not exist (deploy waived) |
| Cloudinary `images.remotePatterns` | `next.config.js:5-11` | authoring-time scan: no `res.cloudinary.com` reference in `src/`, `public/`, `src/mocks/`, `docs/`; only `README.md` screenshot links (Markdown). All `next/image` sources are local: `/brand/logo-color.svg`, `/brand/logo-lockup.svg`, `/landing/owedbook-mockup.png`. Plan Mode repeats the scan; **DD-2** rules remove vs narrow |
| `/_next/image` outside the proxy matcher (R-009 facet) | `src/proxy.ts:10` | by design (public images need no session); with no remote pattern the optimizer can only serve `public/` — closed by DD-2, no `proxy.ts` change |
| RRM-003 cache header | `next.config.js` `headers()` | must survive the bump byte-identical and re-measured (AC-303) |
| RRM-003 QA-F02 (E-18) | `src/components/common/MultiSelect.tsx` | origin check only: Plan Mode reports whether Enter on the closed trigger was prevented at RRM-003's baseline or introduced there; flag-only, no change |

## Approved work and boundaries

**Accepted:**
- **S1 Pin + install + proof (AC-101–107, AC-401–403):** `package.json` — `dependencies.next` and `devDependencies.eslint-config-next` set to the same exact `16.3.x` target; `overrides.sharp` set to the exact `0.35.x` target (≥ 0.35.4). Targets = the highest stable patch on each line as read from the registry at P1 (`npm view next versions`, no canary, no rc), recorded in the addendum at P1b. `npm install` (plain). If DD-1 = sweep: `npm audit fix` (no `--force`) immediately after, then prove `package.json` is unchanged by it. Proof: `npm ls next sharp eslint-config-next`; `npm audit --json`; `@img/sharp-libvips-<platform>/versions.json` `heif` read; lockfile move inventory against `<baseline>` classified by family.
- **S2 Config (AC-201–203):** `next.config.js` `images` block per DD-2 — remove `remotePatterns` (and the now-empty `images` object) or narrow to `{ protocol: "https", hostname: "res.cloudinary.com", pathname: "/dyb0qa58h/**" }` if a runtime consumer is found. `headers()` byte-identical.
- **S3 Board + served proofs (AC-204–205, AC-301–304, AC-405):** blank-env build, placeholder-env build (route count), tsc, eslint, jest (existing suites unmodified); standalone serve with the A-02 static copy; header pair + negative controls; `/_next/image` PNG through sharp; direct GETs of the three local image files.
- **Handoff (same session):** `QA_HANDOFF.md`; `QA/QAM_MANIFEST.md` (facts only); `QA/GOVERNING/` copy + `PROVENANCE.md`; ledger R-009 resolution row; `evidence/changed_files.txt`, `evidence/repair.diff`; `EXECUTION_LOG.md` §Metrics.

**Preserved behavior / invariants:** every route renders as at baseline · every image that rendered at baseline renders (QA walk) · header pair identical to RRM-003's after-capture · `headers()` byte-identical · all existing tests green unmodified · README/TESTING counts still true (no edit expected; if jest numbers change with zero test-file changes, that is stop 7) · `.env.local` untouched.

**Allowed files:** `package.json` (exactly three lines) · `package-lock.json` (moves in the allowed families only) · `next.config.js` (`images` block only) · this pack's `EXECUTION_LOG.md`, `QA_HANDOFF.md`, `RULINGS_ADDENDUM.md` (rows under instruction), `evidence/**`, `QA/QAM_MANIFEST.md`, `QA/GOVERNING/**` (copy) · root-protocol files per root `CLAUDE.md` · `agent_docs/RRM_FINDINGS_DISPOSITION_LEDGER.md` resolution rows and `agent_docs/RRM_CAMPAIGN_MAP_v1_0.md` §0/§9 when instructed.

**Allowed lockfile move families:** `next`, `@next/env`, `@next/eslint-plugin-next`, `@next/swc-*`, `eslint-config-next`, `sharp`, `@img/*`, `@emnapi/runtime`, `@swc/helpers`. **If DD-1 = sweep, additionally:** `brace-expansion` (all nested copies), `js-yaml` (all copies), `baseline-browser-mapping`, `browserslist`, `caniuse-lite`, `electron-to-chromium`, `node-releases`, `update-browserslist-db`, `postcss-selector-parser`. Any other move → stop condition 6, unless Plan Mode's dry run predicted it and the Director ruled it at P1b.

**Forbidden:** any file under `src/` · any test · `headers()` · `images.unoptimized`, `dangerouslyAllowSVG`, `images.loader` · `react` / `react-dom` / any other dependency line · `--force`, `--legacy-peer-deps`, `npm update` · `supabase/**`, `scripts/**`, `docs/**`, `public/**`, `README.md` · any database, dashboard or Git mutation · `RECOVERY.md` before P5.

**Permitted tooling / environment:** the npm registry (install, `npm view`, `npm audit`); local `node_modules`; tsc/eslint/jest; `next build` + standalone `server.js` with placeholder env; `curl` to `127.0.0.1` only (plus the PF-13 fonts probe); a scratch copy outside the tree for the Plan Mode dry run; no browser (the image walk is QA's).

## Stages (inside the single P2 session)

| Stage | Objective | Exit (all must hold before the next stage starts) | Evidence written |
|---|---|---|---|
| **S1 Pin + install + proof** | AC-101–107, AC-401–403 | `npm ls` at target with `sharp … overridden` · audit zero critical/high touching next/sharp/@img (and zero total if DD-1 = sweep) · `versions.json` heif ≥ 1.23.2 · `package.json` diff = 3 lines · moves classified, none outside allowed families | `evidence/S1_versions.txt` (BASELINE and AFTER blocks), `evidence/S1_audit_before.json`, `evidence/S1_audit_after.json`, `evidence/S1_lockfile_moves.txt` |
| **S2 Config** | AC-201–203 | `git diff <baseline> -- next.config.js` confined to `images`; `headers()` hunk absent | `evidence/S2_config_diff.txt` |
| **S3 Board + served proofs** | AC-204–205, AC-301–304, AC-405 | blank build exit 0 · placeholder build exit 0, 17 routes · tsc 0 · eslint 0 errors · jest all pass, zero skipped, `git diff --stat <baseline> -- src/__tests__` empty · served: header pair + 3 negative controls · `/_next/image` PNG 200 `image/webp` · three direct image GETs 200 · server stopped, port free | `evidence/S3_board.txt`, `evidence/S3_serve_before.txt` (from PF-19), `evidence/S3_serve_after.txt` |
| **Handoff** (same session) | `QA_HANDOFF.md`, `QA/QAM_MANIFEST.md`, ledger row, `changed_files.txt`, `repair.diff`, `QA/GOVERNING/` copy + `PROVENANCE.md`, `EXECUTION_LOG.md` §Metrics | one selective staging block, one git command per line | — |

Order is S1 → S2 → S3 because S3's board must run on the final dependency set and the final config.

## Handoff and exit

Engineer delivers candidate (the Director's single commit), repair diff, execution log with metrics, unchanged acceptance spec, evidence, and the factual half of the QAM. Director cuts `qa/phase-3-rrm004`. QA Lead authors the plan and ratifies the QA operating law; Director commits the QA planning docs and starts the QA Executor with one command; the Executor runs its own preflight, builds the candidate itself from the lockfile, reproduces every proof independently, runs the authenticated image walk (Director enters credentials, DC-5), grades the product ACs, and — separately — records the pilot-process ACs and metrics. QA Lead issues Gate Q on the product ACs and a pilot verdict on the process ACs. Bounded cleanup, Architect closeout, Engineer closeout, Director `--no-ff` merge + push, journal entries (Architect's and QA Lead's, each their own). RRM campaign closes with this merge. Deployment / Gate D: outside this module.
