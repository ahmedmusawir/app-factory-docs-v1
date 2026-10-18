# RRM-004-CYBER-PHARMA — QA Handoff (Engineer → QA Lead)

**Every line below is a claim.** The QA Executor reproduces each proof from its own install and build; the QA Lead's plan decides what to attack first. The factual half of the QAM is `QA/QAM_MANIFEST.md`; this file is the narrative handoff the previous modules used, kept for continuity.

## Identity

| Field | Value |
|---|---|
| Module | RRM-004-CYBER-PHARMA — Dependencies |
| Code baseline | `<baseline>` (RRM-003 merge commit on `main`) |
| Candidate | the Director's single P2 commit (SHA recorded at cut) |
| Engineering branch / QA branch | `phase-3-rrm004` / `qa/phase-3-rrm004` |
| Targets (addendum A-01 / A-02) | next `<target-next>` · sharp `<target-sharp>` · eslint-config-next `<target-next>` |
| DD rulings | DD-1 <pins only / sweep> · DD-2 <remove / narrow> · DD-3 <QA target> · DD-4 <authorship split confirmed> |
| Provenance chain | RRM-003 merge `<baseline>` → pack commit → P0 → P1b → candidate |

## Contract

`CLAUDE.md` · `RRM_BRIEF.md` · `ACCEPTANCE_SPEC.md` (frozen) · `RULINGS_ADDENDUM.md` A-01…A-NN · erratum lane rows: <none / list> · ledger: R-009 resolution row appended; errata <E-NN…> · map §9: <CE-N if DD-1 = sweep>

## Changed files (`evidence/changed_files.txt`)

| Path | Status | Reason |
|---|---|---|
| `package.json` | M | three pinned lines |
| `package-lock.json` | M | <n> entries moved; families listed in `evidence/S1_lockfile_moves.txt` |
| `next.config.js` | M | `images` block per DD-2 |
| `agent_docs/ACTIONS/RRM-004-CYBER-PHARMA/**` | A/M | log, evidence, manifest, governing copy |
| ledger / map / protocol files | M | resolution row, errata, session log, CHANGELOG |

Product diff for QA: `git diff <baseline>..<candidate> -- package.json package-lock.json next.config.js` (= `evidence/repair.diff`).

## Reproduction (facts, not instructions on what to test)

- Install: `rm -rf node_modules && npm ci` (from the committed lockfile; no network beyond the registry).
- Builds: `rm -rf .next && env <blank Supabase env> npx next build`; `rm -rf .next && env NEXT_PUBLIC_SUPABASE_URL=https://placeholder.invalid NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY=placeholder-publishable SUPABASE_SECRET_KEY=placeholder-secret NEXT_PUBLIC_SITE_URL=http://127.0.0.1:<port> npx next build` (17 routes claimed).
- Serve: copy `.next/static` → `.next/standalone/.next/static` and `public/` → `.next/standalone/public` (RRM-003 A-02), then `PORT=<port> HOSTNAME=127.0.0.1 node .next/standalone/server.js`.
- Header pair, negative controls, `/_next/image` probe, negative host probe, direct image GETs: exact lines in `evidence/S3_serve_after.txt`.
- Instrument: `node -p "require('@img/sharp-libvips-<platform>/versions.json').heif"`; baseline value `<x>` recorded at PF-16 before install; after `<y>`.
- Board: `npx tsc --noEmit` · `npx eslint .` · `npx jest --ci` (claimed 34/164, 0 skipped; eslint 0 errors / <n> warnings).
- No live Supabase call in engineering. `.env.local` untouched.

## References

Recon R6, R3 · reviews F9, A-003 · advisories GHSA-p293-qw3h-jr36, GHSA-2xp9-vwfh-vxw4, GHSA-rgj7-g3m4-5g8c · RRM-003 A-01, A-02 · P1 plan and P2 report in `agent_docs/RESPONSES/`

## Governing snapshot

`QA/GOVERNING/` copied from `agent_docs/ACTIONS/RRM-003-CYBER-PHARMA/QA/GOVERNING/` with a fresh `PROVENANCE.md` (chain: RRM-001 Director copy → RRM-002 → RRM-003 → RRM-004).

## Unrun by design

Authenticated image walk (AC-605, DC-5) · QA's own install/build/serve (AC-601–604) · AVIF input · Windows host.
