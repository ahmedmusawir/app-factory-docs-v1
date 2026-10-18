# RRM-004-CYBER-PHARMA — Dependencies — Acceptance Specification

**Version:** 1.0 · 2026-09-30 · **Architect** authored · **Director approval:** campaign map §7 (D4) · **Contract freezes at:** engineering handoff (end of P2). Post-freeze rulings append to `RULINGS_ADDENDUM.md` and the erratum lane below; frozen text is never rewritten.
**Scope:** exact pins for `next` (with `eslint-config-next` in lockstep) and the `sharp` override; proof of the installed image stack; image remote-source list per real sources; full board and served proofs; the QAM pilot on the QA side. **Code baseline:** post-RRM-003 `main` merge commit (`<baseline>`; SHA recorded at P1). **Targets:** `<target-next>` and `<target-sharp>` are the exact versions recorded in `RULINGS_ADDENDUM.md` at P1b; the floors are `16.3.3` and `0.35.4`.

Requirements are agreed before implementation. The Engineer delivers this file unchanged with execution evidence. QA verdicts belong to the QA Lead. Grep, diff and version criteria are literal; allowed exceptions are listed in `EXECUTION_LOG.md` with path and reason.

**Two verdicts leave this module.** AC-100 … AC-600 are the **product** criteria: Gate Q is issued on them alone. AC-700 are the **QAM pilot-process** criteria: they grade how the QA ran, are recorded in `QA/QAM_PILOT_RESULTS.md`, and never block or rescue Gate Q. A clean product with a messy pilot is a PASS with lessons; a perfect pilot on a failing product is a FAIL.

## AC-100 — Versions and advisories (R-009; F9, A-003)

| AC | Required observable behavior | Controls | Boundary | Evidence |
|---|---|---|---|---|
| AC-101 | `package.json` `dependencies.next` is the exact string `<target-next>` (no `^`, no `~`); `<target-next>` ≥ `16.3.3`, is a stable release on the `16.3` line (not `canary`, not `rc`), and `npm view next@<target-next> version` prints it. | Negative: `npm view next versions --json` shows no higher stable `16.3.x` than `<target-next>` at P1 (recorded; a newer patch published between P1 and P2 is not a failure — record it). | repo + registry | `evidence/S1_versions.txt` |
| AC-102 | `package.json` `overrides.sharp` is the exact string `<target-sharp>`, ≥ `0.35.4`, stable on `0.35.x`; `devDependencies.eslint-config-next` equals `<target-next>` exactly. | — | repo + registry | `evidence/S1_versions.txt` |
| AC-103 | **Instrument.** For the executing `<platform>` (PF-14), `node -p "require('@img/sharp-libvips-<platform>/versions.json').heif"` prints a version ≥ `1.23.2` after the install, and the same command's **baseline** output (PF-16, before the install) is recorded beside it and is lower. The method is stated in `EXECUTION_LOG.md` as: *installed package metadata (`versions.json` shipped inside the `@img/sharp-libvips-*` package), cross-checked against the advisory's fixed-version statement (sharp 0.35.4 → libvips 1.3.3 → libheif 1.23.2)*. | Negative (attack the instrument): the baseline read must show a value below the floor (`1.23.1` expected on libvips 1.3.2). If baseline and after read the same, the instrument did not move and AC-103 fails regardless of the number. | node_modules | `evidence/S1_versions.txt` BASELINE / AFTER |
| AC-104 | `npm audit --json` after the install: zero advisories of severity `critical` or `high` whose `nodes` include `node_modules/next`, `node_modules/sharp`, or any `node_modules/@img/*` path; the three target advisory IDs (GHSA-p293-qw3h-jr36, GHSA-2xp9-vwfh-vxw4, GHSA-rgj7-g3m4-5g8c) absent from the output. | Positive control: `evidence/S1_audit_before.json` (baseline lockfile, `--package-lock-only`) lists all three. | registry | `evidence/S1_audit_before.json`, `evidence/S1_audit_after.json` |
| AC-105 | Remaining advisories per DD-1. **DD-1 = pins only:** every remaining advisory listed in `EXECUTION_LOG.md` by GHSA ID, package, severity, dependency path and `fixAvailable`, marked "not fixed in this module". **DD-1 = sweep:** `npm audit` reports `found 0 vulnerabilities` (`metadata.vulnerabilities.total` = 0) and `package.json` is byte-identical before and after `npm audit fix` (three-line diff vs baseline either way). | — | registry | `evidence/S1_audit_after.json`, log |
| AC-106 | Every lockfile entry whose `version` differs from `<baseline>`'s `package-lock.json` is listed (`name: old → new`) and classified into an allowed family (`RRM_BRIEF.md`). Count recorded. Zero entries outside the allowed families, or each such entry ruled in the addendum before P2. | — | repo | `evidence/S1_lockfile_moves.txt` |
| AC-107 | `npm ls next sharp eslint-config-next` exits 0 and shows `next@<target-next>`, `eslint-config-next@<target-next>`, and `sharp@<target-sharp> overridden` under `next`; `ls node_modules/@img/` contains `sharp-<platform>` and `sharp-libvips-<platform>` at the versions `sharp@<target-sharp>` declares in its `optionalDependencies`. | Negative: no `npm ls` `invalid` / `missing` / `extraneous` line for these packages. | node_modules | `evidence/S1_versions.txt` |

## AC-200 — Image configuration (R-009 Cloudinary facet; DD-2)

| AC | Required observable behavior | Controls | Boundary | Evidence |
|---|---|---|---|---|
| AC-201 | Per DD-2. **Remove:** `next.config.js` contains no `remotePatterns` and no `res.cloudinary.com`; the `images` key is absent (or present and empty only if a ruling says so). **Narrow:** exactly one entry `{ protocol: "https", hostname: "res.cloudinary.com", pathname: "/dyb0qa58h/**" }` and Plan Mode's consumer path:line recorded in the addendum. | Positive control: `grep -rn "res.cloudinary.com" src public src/mocks docs` → 0 at baseline and at candidate (README.md hits are Markdown and are listed as the allowed exception). | repo | `evidence/S2_config_diff.txt` |
| AC-202 | `git diff <baseline> -- next.config.js` touches only the `images` block; the `headers()` function, `output: "standalone"` and `reactStrictMode` are byte-identical. | — | repo | diff |
| AC-203 | `grep -nE "unoptimized|dangerouslyAllowSVG|loader:" next.config.js` → 0. | — | repo | grep |
| AC-204 | **Sharp in the loop.** Served from the standalone build (placeholder env, A-02 static copy): `curl -s -o body.bin -D - -H 'Accept: image/webp' 'http://127.0.0.1:36055/_next/image?url=%2Flanding%2Fowedbook-mockup.png&w=1080&q=75'` → status `200`, `Content-Type: image/webp`, and `body.bin` begins with the bytes `RIFF` … `WEBP` (offset 8) — a real encoded image, not an error page. The response's `Cache-Control` is recorded verbatim (authoring-time observation: `public, max-age=14400, must-revalidate`, Next's own optimizer header; no requirement on its value). | Negative: `curl -s -o /dev/null -w '%{http_code}' 'http://127.0.0.1:36055/_next/image?url=https%3A%2F%2Fres.cloudinary.com%2Fdyb0qa58h%2Fimage%2Fupload%2Fx.png&w=64&q=75'` → `400` after DD-2 = remove (the optimizer refuses the un-listed host). Under narrow, this line is recorded, not graded. | served build | `evidence/S3_serve_after.txt`, `evidence/S3_image_probe.bin` (first 16 bytes hex-dumped into the txt; the binary itself is not committed) |
| AC-205 | Direct GETs on the served build: `/brand/logo-color.svg` and `/brand/logo-lockup.svg` → `200` with `Content-Type` containing `image/svg+xml`; `/landing/owedbook-mockup.png` → `200` with `image/png`. (`next/image` renders SVG sources unoptimized, so the SVGs are fetched directly by the browser; the optimizer's `400` on an SVG `url=` is expected and recorded, not graded.) | — | served build | `evidence/S3_serve_after.txt` |

## AC-300 — Board and served regressions

| AC | Required observable behavior | Controls | Boundary | Evidence |
|---|---|---|---|---|
| AC-301 | `rm -rf .next` then `next build` with **blank** Supabase env exits 0; `rm -rf .next` then `next build` with the **placeholder** env exits 0 and prints 17 routes (recorded verbatim). Both on the final dependency set and config. | — | build | `evidence/S3_board.txt` |
| AC-302 | `npx tsc --noEmit` 0 errors · `npx eslint .` 0 errors (warning count recorded; baseline 35) · `npx jest --ci` all pass, zero skipped, zero failed (suites/tests recorded; baseline 34/164) · `git diff --stat <baseline> -- src/__tests__` empty · `git diff --stat <baseline> -- src` empty. | Negative: a jest count different from baseline with an empty `src/` diff is stop 7, not a pass. | repo + tools | `evidence/S3_board.txt` |
| AC-303 | **RRM-003's fix survives.** From the served build: `curl -sI /` → `200`, `Cache-Control` contains `no-store`; `curl -sI /_next/static/chunks/<any>.js` → `200`, `Cache-Control` contains `immutable` **or** `max-age=31536000` and not `no-store`; `/auth` (`200`), `/owedbook` unauthenticated (`307` → `/auth`) and `POST /api/auth/login` empty body all carry `no-store`. The before-capture (PF-19) sits beside it. | — | served build | `evidence/S3_serve_before.txt`, `evidence/S3_serve_after.txt` |
| AC-304 | `README.md` and `docs/TESTING.md` test counts still equal the AC-302 jest numbers with **no edit** to either file (`git diff <baseline> -- README.md docs/TESTING.md` empty). | — | repo | diff + jest |

## AC-400 — Preserved

| AC | Required observable behavior | Boundary | Evidence |
|---|---|---|---|
| AC-401 | `git diff --stat <baseline> -- src supabase scripts docs public README.md tsconfig.json jest.config.js eslint.config.mjs tailwind.config.ts postcss.config.js .gitignore` → empty. | repo | diff transcript |
| AC-402 | `git diff <baseline> -- package.json` is exactly three changed lines: `"next"`, `"eslint-config-next"`, `"sharp"` (inside `overrides`). Nothing added, nothing removed. | repo | diff |
| AC-403 | `git diff --name-only <baseline>` lists only: `package.json`, `package-lock.json`, `next.config.js`, files under `agent_docs/ACTIONS/RRM-004-CYBER-PHARMA/`, the ledger/map lines instructed at handoff, and root-protocol files. `node_modules/` never appears in `git status`. | repo | `evidence/changed_files.txt` |
| AC-404 | No product-code change. If the upgrade forced one, the module stopped (stop 2) and this AC records the stop; it is not satisfied by a change. | repo | log |
| AC-405 | `git diff <baseline> -- next.config.js` shows no hunk inside `headers()` (AC-202 restated as the preserved side). | repo | diff |

## AC-500 — Engineering board, metrics, hygiene

| AC | Required observable behavior | Evidence |
|---|---|---|
| AC-501 | `ENVIRONMENT_PREFLIGHT.md` PF-01…PF-21 recorded PASS at P2 start (`evidence/PREFLIGHT_P2.txt`); PF-16 and PF-19 captured the baseline instrument value and served proofs before any install. | evidence |
| AC-502 | `EXECUTION_LOG.md` §Metrics filled: P2 start/end; per-stage start/end; checks executed; self-repair attempts (count and what); Director touches between P2 start and the staging block (expected 0); stop conditions hit (expected none); install wall-clock. | log |
| AC-503 | `git status --porcelain` empty after the Director's single commit; candidate SHA recorded; `.env.local` not edited (Engineer states it); no local server left running; scratch copy from Plan Mode deleted. | log |
| AC-504 | `QA/QAM_MANIFEST.md` filled with every field in its template; contains **no** test plan, risk ranking, attack order, or reference value beyond the literal Engineer measurements it labels as claims. | manifest |

## AC-600 — QA product verification (QA-graded; the Executor derives every value itself)

| AC | Required observable behavior | Boundary | Evidence |
|---|---|---|---|
| AC-601 | From a clean `node_modules` (`rm -rf node_modules && npm ci`) on the pinned candidate: `npm ls next sharp eslint-config-next` at targets with `sharp … overridden`; `npm audit --json` satisfies AC-104 and AC-105 independently; `@img/sharp-libvips-<platform>/versions.json` `heif` ≥ 1.23.2 read by the Executor on its own platform (recorded with its own `<platform>`, which may differ from the Engineer's). | QA tools | `QA/evidence/deps/` |
| AC-602 | The Executor's own build (never the Engineer's `.next/`): blank-env and placeholder-env builds exit 0, 17 routes; tsc 0; eslint 0 errors; jest all pass zero skipped; counts equal AC-302. | QA build | `QA/evidence/board/` |
| AC-603 | Header pair and negative controls re-captured from the Executor's served build per AC-303. | QA served build | `QA/evidence/headers/` |
| AC-604 | `/_next/image` PNG probe and the three direct image GETs per AC-204/205 from the Executor's served build; the negative host probe returns `400` under DD-2 = remove. | QA served build | `QA/evidence/images/` |
| AC-605 | **Authenticated image walk** (DC-5; target per DD-3): as ADMIN — `/`, `/auth` (signed-out first), `/owedbook`, `/admin-portal`; as MEMBER — `/`, `/owedbook`. At desktop and 375px (theme at the QA Lead's discretion, recorded). For each route: every `<img>` element satisfies `complete && naturalWidth > 0`; zero failed image requests (`requestfailed` on image resource type, or `response.status() >= 400` on an image); zero console errors; the expected image inventory per route — derived by the Executor from source (`src/components/global/Navbar*.tsx`, `src/app/(public)/HomePageContent.tsx`), not from the manifest — matches what rendered. Login and logout each succeed once per role. | browser, real auth | `QA/evidence/browser/` (cropped screenshots, sanitized traces, no auth state) |
| AC-606 | Executor's evidence privacy scan: zero credential, token, cookie, key value or env value in `QA/evidence/**`; no `storageState`, no raw authenticated trace retained. | QA lane | `QA/evidence/privacy_audit.json` |

## AC-700 — QAM pilot-process criteria (graded separately; never gate Gate Q)

| AC | Required observable behavior | Evidence |
|---|---|---|
| AC-701 | `QA/QAM_MANIFEST.md` was authored by the Engineer at handoff, every template field filled, and contains no plan/attack/reference content (AC-504 seen from the QA side). | manifest + `QA_HANDOFF.md` |
| AC-702 | `QA/QA_TEST_PLAN.md` carries a provenance header naming the QA Lead (position) and a date after the candidate commit; its risk ranking, negative controls and reference values were derived by the QA seat; the Engineer's `QA_HANDOFF.md` is cited as claims, not as expected values. | plan header + diff of authorship |
| AC-703 | `QA/QA_ENVIRONMENT_PREFLIGHT.md` QF-01…QF-14 recorded before any build, install or browser action by the Executor (`QA/evidence/QA_PREFLIGHT.txt` with `date -Is`); any FAIL stopped the run (QA stop Q1) rather than being worked around. | evidence |
| AC-704 | Every QA stop that occurred is logged in `QA/QA_EXECUTION_REPORT.md` with its Q-number, timestamp and resolution; no unenumerated stop occurred. Target: zero. | report |
| AC-705 | Director touches during QA counted and classified (credential entry / ruling / spot-check / other) in `QA/QAM_PILOT_RESULTS.md`; credential entries target ≤ 2 (one per role); RRM-003 comparison: 8 touches, 7 sign-ins. | results |
| AC-706 | The Executor built and installed the candidate itself (AC-601/602 evidence carries the Executor's own `date -Is`, `node -v`, and platform), never reusing `node_modules/` or `.next/` from the Engineer's session. | evidence |
| AC-707 | `QA/REPAIR_PROPOSAL.md` exists **iff** at least one AC-100…600 row is FAIL. If it exists, it is a proposal: finding IDs, evidence paths, affected ACs, suggested allowed-file list, suggested retest scope — and no edit under `src/`, `package.json`, `package-lock.json` or `next.config.js` was made by any QA seat. | file presence + `git diff` on the QA branch |
| AC-708 | `QA/QAM_PILOT_RESULTS.md` metrics filled: pilot start (DC-4 `date -Is`), Executor active time, Director active time, interruptions, preflight failures, product findings by class, repair rounds, helpers promoted, evidence count; RRM-002 and RRM-003 comparison columns filled from their journal/observation records. | results |
| AC-709 | The Executor was started by the single command recorded verbatim in `QA/QAM_PILOT_RESULTS.md`; no further Director instruction reached the Executor between that command and DC-5 except a logged stop resolution. | results |
| AC-710 | The QA Lead read `QA/AC_EVIDENCE_MATRIX.md` and the evidence map before signing `QA/QA_CERTIFICATION.md`, and the certification says so in one line (a green execution report is an input, not a verdict). | certification |

## Required regression and constraints

- All existing suites green unmodified. Journeys: every route builds; header pair; image optimizer; authenticated image walk.
- Mocks: OwedBook and adminDemo stay mock. Real auth only in the QA walk.
- Unavailable boundaries that do not block acceptance: deployment (waived; no Dockerfile); Windows-host advisory GHSA-p293-qw3h-jr36 closed by the version pin alone (no Windows host to test); AVIF input not exercised (no AVIF source in the app; the pin and the libheif read are the proof).
- Version numbers are recorded, never a pass criterion without the registry check beside them.

## Acceptance gates

Every product AC needs independent evidence. Ambiguity or failure → QA Lead; scope → Architect/Director. Engineer green ≠ Gate Q. This certificate, when issued, certifies the pinned dependency set on the certified commit and the served standalone build; it certifies neither deployment nor any host's runtime.

## Erratum lane (append-only; empty at freeze)

| Date | AC | Original requirement | Ruling / rationale | Authority | Verification consequence |
|---|---|---|---|---|---|
