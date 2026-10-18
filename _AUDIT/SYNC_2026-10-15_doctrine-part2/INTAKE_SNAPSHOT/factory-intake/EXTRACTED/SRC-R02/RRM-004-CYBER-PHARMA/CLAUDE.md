# RRM-004-CYBER-PHARMA — Dependencies — Engineer Front Door

**Status:** Director-approved scope (ledger R-009 ACCEPT, D4: isolated final module, full board rerun, targets verified at implementation, Cloudinary per real sources). **One-shot Engineering run** (RRM-003 shape) feeding the **first QAM pilot** on the QA side. Executable after DA-1 (branch from post-RRM-003 `main`), DA-2 (pack committed), DA-3 (P0 bookkeeping committed), DA-4 (clean tree), a green `ENVIRONMENT_PREFLIGHT.md`, and Director approval of the Plan Mode output with the rulings on disk.
**Seats:** Architect · Engineer · QA Lead · QA Executor · Director. Positions, not names.
**Repo:** `cyber-pharma-dev-v1-phase-3` · **Code baseline:** post-RRM-003 `main` — the `--no-ff` merge commit of `qa/phase-3-rrm003`. The Engineer records its full SHA at P1; every "diff vs baseline" in this pack means that commit.
**Engineering branch:** `phase-3-rrm004` · **QA branch (Director-cut after handoff):** `qa/phase-3-rrm004`
**Pack folder:** `agent_docs/ACTIONS/RRM-004-CYBER-PHARMA/` · **Campaign:** `agent_docs/RRM_CAMPAIGN_MAP_v1_0.md` §7

## Mission

The installed `next` and `sharp` match published critical and high advisories: two Next.js unauthenticated-RCE advisories fixed in `16.3.3` (one in the image-optimization API on AVIF input), and a `sharp` advisory for two libheif heap overflows fixed in `0.35.4` (libheif ≥ 1.23.2). This module pins both to exact, registry-verified versions, installs, proves the installed image stack is the fixed one by reading the installed package's own metadata, closes the image-optimizer's remote source list to what the app actually uses, and reruns the whole board — including the two things a dependency bump can silently undo: RRM-003's cache header and the image optimizer itself.

Three deliverables, one proof style (a version read, an audit, a diff, a served response):

1. **Versions.** `next` pinned exact on the `16.3` line; `sharp` override pinned exact on `0.35.x` ≥ `0.35.4`; `eslint-config-next` moves in lockstep with `next` (same exact version — it is a peer of the framework and will not stay behind). Targets are read from the registry at Plan Mode and written into the addendum; the pack names floors, never the number.
2. **Proof of the fixed stack.** `npm ls` at target; `npm audit` with zero critical/high touching `next`, `sharp` or `@img/*`; the executing platform's `@img/sharp-libvips-<platform>/versions.json` read for `"heif"` ≥ `1.23.2` — and the same read at baseline recorded first, so the instrument is shown to move (the baseline value is below the floor).
3. **Image source list.** `images.remotePatterns` in `next.config.js` drops the Cloudinary entry if the Plan Mode scan confirms no runtime image source uses it (authoring-time scan: none in `src/`, `public/`, `src/mocks/`; only README screenshots, which are Markdown, not `next/image`), or narrows it to exact host + path prefix if one is found. This also closes the R-009 facet where `/_next/image` sits outside the auth proxy: with no remote pattern, the optimizer can only serve files under `public/`.

What this module does **not** do: touch any file under `src/` (any product-code change forced by the upgrade is a stop, not a fix) · touch `headers()` in `next.config.js` (RRM-003's, byte-identical) · introduce `images.unoptimized` or `dangerouslyAllowSVG` · bump anything not named here except what `npm install` moves as a consequence of the pins (every incidental move listed and classified) or what the Director rules in DD-1 · deploy · touch a database.

## How this run works

- **P0** is a docs-only bookkeeping step that lands RRM-003's journal entries and scoreboard SHAs before this module starts. It is not part of the pilot clock.
- **P1 Plan Mode** is read-only and ends in one stop. It resolves the exact targets from the registry, inventories the lockfile consequences by a `--package-lock-only` dry run in a scratch copy (never the working tree), scans for Cloudinary consumers, reads the baseline instrument value, and surfaces contradictions. The Director rules DD-1…DD-4 and the Architect turns them into P1b rows.
- **P2 is one continuous session:** preflight (gate) → S1 pin + install + proof → S2 config → S3 board + served proofs → handoff, including `QA/QAM_MANIFEST.md` (the factual half of the QAM — never the plan). One selective staging block; the Director commits once.
- **You stop only on an enumerated stop condition** (below). If you are unsure whether something is one, it is.
- **Metrics** in `EXECUTION_LOG.md` §Metrics: timestamps per stage, checks run, self-repairs, Director touches (zero expected between P2 start and the staging block), stop conditions hit.
- **QA is the QAM pilot.** After DC-3 the QA Lead authors the plan, the Director starts the QA Executor with one command, and the Executor runs the QA body against `QA/AGENTS.md` and `QA/QA_ENVIRONMENT_PREFLIGHT.md`. You supply facts (`QA_HANDOFF.md`, `QA/QAM_MANIFEST.md`); you never supply the plan, the risk ranking or the reference values.

## Enumerated stop conditions (P2)

1. Any `ENVIRONMENT_PREFLIGHT.md` check fails.
2. Any edit is needed outside the allowed files in `RRM_BRIEF.md` — including any file under `src/`, any test, `headers()`, or a fourth line of `package.json`.
3. An existing test fails after the install and the only fix would be to modify that test, a config file, or product code.
4. The board (build / tsc / eslint errors / jest) or a served proof (header pair, `/_next/image` response) is still red after two in-scope self-repair attempts on the same failure (in scope: `rm -rf node_modules .next` + reinstall from the lockfile; `npm cache verify`; re-running the pin).
5. The exact targets recorded at P1b cannot be resolved from the registry, `npm install` exits non-zero, or the host's `@img/sharp-<platform>` / `@img/sharp-libvips-<platform>` packages are not installed after the install.
6. `npm install` (or the DD-1 sweep) moves a lockfile entry outside the allowed families in `RRM_BRIEF.md` that the pin does not explain, or alters `package.json` beyond the three pinned lines.
7. Disk and contract disagree on a point not already covered by `RULINGS_ADDENDUM.md`.
8. Anything would require a live database, dashboard, credential, or Git mutation.

On a stop: write what you have to `EXECUTION_LOG.md`, save evidence, report the stop with its number and the exact path:line (or package:version), and wait.

## Read in order

1. Root `CLAUDE.md` (its protocol wins over this pack where they collide — RRM-001 A-10)
2. `agent_docs/RRM_CAMPAIGN_MAP_v1_0.md` §2, §7, §8, §10
3. `AUTHORITY_POINTER.md` · `ENVIRONMENT_PREFLIGHT.md` · `DIRECTOR_CHECKPOINTS.md`
4. `RRM_BRIEF.md` · `ACCEPTANCE_SPEC.md` · `CLAUDY_PROMPTS.md`
5. `QA/README.md` and `QA/QAM_PILOT_CHARTER.md` (so you know what the manifest is for and what it must not contain)
6. Evidence inputs: `agent_docs/RECON/RRM001_RECON_2026-09-18.md` R6 (dependencies), R3 (header capture method); `agent_docs/ACTIONS/RRM-003-CYBER-PHARMA/RULINGS_ADDENDUM.md` A-01 (PF-05 own-protocol-files rule), A-02 (standalone static copy); `agent_docs/FABLE_CODE_REVIEW.md` F9; `agent_docs/ASTRA_CODE_REVIEW.md` A-003; ledger R-009, E-17, E-18

## Rules of the road

- Read-only Git. Mutating Git, dashboard, live database: Director.
- `npm install` is permitted in this module and only in this module of the campaign. Never `--force`, never `--legacy-peer-deps`, never `npm update`, never `npm audit fix --force`. The registry is the only network you use; no `curl` to anything but `127.0.0.1` and the one Google Fonts reachability probe in the preflight.
- Placeholder Supabase env only for any build or serve; never real keys in the shell; `.env.local` untouched; temp-then-move for any redirect into a tracked file; stop any local server you start and prove the port is free.
- Plan Mode dry runs happen in a scratch copy outside the working tree (`git worktree` is a Git mutation — use `cp -r` to a temp directory and delete it after). The working tree's `package-lock.json` changes only in S1.
- `EXECUTION_LOG.md` as you go, per stage. `QA_HANDOFF.md` and `QA/QAM_MANIFEST.md` at the end of P2. You do not certify QA. During QA you act only on an approved repair instruction on `qa/phase-3-rrm004`.
- Full file paths. YOU / ENGINEER / QA LEAD labels. Selective staging blocks, one git command per line.

## Preserved (byte-identical or test-green at handoff)

Everything under `src/` · every test file · `next.config.js` except the `images` block · `supabase/**` · `scripts/**` · `docs/**` · `public/**` · `README.md` · `tsconfig.json`, `jest.config.js`, `eslint.config.mjs`, `tailwind.config.ts`, `postcss.config.js` · `package.json` except the three pinned lines · all closed module folders.

## Protected (never touch)

`RECOVERY.md` until P5 · `agent_docs/SESSIONS/**` beyond your own session log · closed module folders under `agent_docs/ACTIONS/` · `.env.local` · `supabase/migrations/**` · `node_modules/` is never staged.
