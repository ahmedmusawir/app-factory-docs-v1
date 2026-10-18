# RRM-004-CYBER-PHARMA — Engineering Execution Log

Engineer · Approved scope/plan: `RRM_BRIEF.md` v1.0 + the P1 plan in `agent_docs/RESPONSES/<response file>` (Director-approved <date>) + rulings A-01…A-NN · Code baseline `<baseline>` (RRM-003 merge commit; recorded at P1) · Targets: next `<target-next>` · sharp `<target-sharp>` · Branch: `phase-3-rrm004` (P2 started at `<P1b commit>`) · Run shape: one-shot (P2 single session) · Platform: `<platform>`

## Preflight

P1: `evidence/PREFLIGHT_P1.txt` — <n>/21 PASS (exceptions listed) · P2: `evidence/PREFLIGHT_P2.txt` — <n>/21 PASS

## Stage S1 — Pin + install + proof

Start: <date -Is> · Install start / end: <date -Is> / <date -Is> · End: <date -Is>

| Item | Value | AC | Evidence |
|---|---|---|---|
| package.json lines changed | 3 (`next`, `eslint-config-next`, `overrides.sharp`) | AC-101, AC-102, AC-402 | `evidence/S1_versions.txt` |
| `npm ls next sharp eslint-config-next` | <quoted> | AC-107 | `evidence/S1_versions.txt` |
| `@img/sharp-libvips-<platform>/versions.json` heif — BASELINE / AFTER | <x> / <y> · method: installed package metadata cross-checked with the advisory's fixed-version statement | AC-103 | `evidence/S1_versions.txt` |
| `npm audit` totals before / after (critical · high · moderate · low) | <…> / <…> · target IDs absent after: <yes/no> | AC-104, AC-105 | `evidence/S1_audit_before.json`, `evidence/S1_audit_after.json` |
| Remaining advisories (DD-1 = pins only) or `found 0 vulnerabilities` (DD-1 = sweep) | <list by GHSA ID / package / severity / path / fixAvailable, or "0"> | AC-105 | log |
| Lockfile moves: count / families / outside-family entries | <n> / <families> / <none> | AC-106, AC-403 | `evidence/S1_lockfile_moves.txt` |

Allowed exceptions: <none> · Self-repairs: <…> · Deviations: <none>

## Stage S2 — Config

Start / End: <…>

| File | Change and reason | AC | Preservation |
|---|---|---|---|
| `next.config.js` | `images` block per DD-2 (<remove/narrow>) | AC-201–203 | `headers()`, `output`, `reactStrictMode` byte-identical (AC-202/405) |

## Stage S3 — Board + served proofs

Start / End: <…>

| Command/check | Exit/result | AC | Evidence |
|---|---|---|---|
| blank-env build · placeholder-env build (routes) | <0 · 0 (17)> | AC-301 | `evidence/S3_board.txt` |
| tsc · eslint (errors/warnings) · jest (suites/tests/skipped) | <0 · 0/35 · 34/164/0> | AC-302 | `evidence/S3_board.txt` |
| `git diff --stat <baseline> -- src src/__tests__ README.md docs/TESTING.md` | <empty> | AC-302, AC-304, AC-401 | `evidence/S3_board.txt` |
| `/` · chunk · `/auth` · `/owedbook` · `POST /api/auth/login` (status + Cache-Control) | <…> | AC-303 | `evidence/S3_serve_after.txt` |
| `/_next/image` PNG probe (status, content-type, first 16 bytes, Cache-Control) | <…> | AC-204 | `evidence/S3_serve_after.txt` |
| negative Cloudinary host probe | <400 / recorded> | AC-204 | `evidence/S3_serve_after.txt` |
| direct GETs: 2 SVG + 1 PNG | <200 ×3, content-types> | AC-205 | `evidence/S3_serve_after.txt` |
| server stopped, port free | <free> | AC-503 | `evidence/S3_serve_after.txt` |

## Metrics (AC-502)

| Metric | Value |
|---|---|
| P2 start / end (`date -Is`) | |
| Wall-clock P2 | |
| Install wall-clock (`npm install`, and `npm audit fix` if DD-1 = sweep) | |
| Per-stage durations preflight / S1 / S2 / S3 / handoff | |
| Checks executed (count) | |
| Self-repair attempts (count; list) | |
| Director touches between P2 start and staging block | |
| Stop conditions hit | |
| Preflight failures (P1 / P2) | |
| Lockfile entries moved (pin / sweep) | |

## Completion claim

Candidate: <the Director's single P2 commit, SHA recorded at cut> · Repair diff: `evidence/repair.diff` · Changed files: `evidence/changed_files.txt` · AC coverage claims: AC-101–107 → `evidence/S1_*` · AC-201–203 → `evidence/S2_config_diff.txt` · AC-204–205, AC-303 → `evidence/S3_serve_after.txt` (+ `S3_serve_before.txt`) · AC-301–302, AC-304 → `evidence/S3_board.txt` · AC-401–405 → `evidence/changed_files.txt`, `evidence/S3_board.txt` · AC-501 → `evidence/PREFLIGHT_P2.txt` · AC-502 → §Metrics · AC-503 → Director's commit · AC-504 → `QA/QAM_MANIFEST.md`
Limitations / not run: authenticated image walk (QA, AC-605); QA's own install/build/serve (AC-601–604); AVIF input not exercised (no AVIF source; pin + libheif read are the proof); Windows-host advisory closed by version alone
QA handoff: `QA_HANDOFF.md` · QAM manifest: `QA/QAM_MANIFEST.md`

Engineering evidence, not independent QA certification.
