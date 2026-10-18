# RRM-004-CYBER-PHARMA — Engineering Prompts (one-shot + QAM handoff)

P0 lands RRM-003's bookkeeping (docs-only, before the pilot clock starts). P1 plans (read-only, one stop). P1b applies the Director's rulings (docs-only). P2 is the whole build, the served proofs and the QA handoff — including the factual half of the QAM — in one continuous session, ending in a single selective staging block. P4 is the QA-repair template. P5 is reserved. The Director confirms `git status --porcelain` is empty before P1 and before P2. The Engineer answers with full file paths, YOU / ENGINEER / QA LEAD labels, and one git command per line.

---

## P0 — RRM-003 bookkeeping (documentation-only; Director-instructed edits to a closed module's records)

ENGINEER — documentation-only step on `phase-3-rrm004`. No product changes, no builds, no installs, no Git mutations. The Director instructs these edits to RRM-003's closeout records now that its merge SHA exists; closed-module protection is lifted for exactly these fields and nothing else.

1. `agent_docs/RRM_CAMPAIGN_JOURNAL.md` — replace the three placeholder lines under `### RRM-003-CYBER-PHARMA — closed 2026-09-29 (Architect)` and `### Friction log — RRM-003 (Director-observed, filed by Architect)` with the two blocks below, verbatim. Leave the QA Lead's placeholder untouched (that seat appends its own).

ARCHITECT ENTRY:

- **Module:** RRM-003-CYBER-PHARMA — Access, Cache, Hygiene, Docs. Controlled one-shot Engineering pilot (QA Lead field note 2026-09-28).
- **Commits:** pack `a59f069` · P1b rulings `6655f95` · candidate (single P2 commit) `21ea108bb27b965ddc5edae29dc3b1d6971ae576` · QA HEAD `1a94277` · closeout `7309a2f` · merge to `main` `649c36d` (`--no-ff`, 2026-09-29). Baseline `3d2e655` (RRM-002 merge).
- **Verdict:** Gate Q PASS, 26/26 ACs, zero repair rounds (QA Lead, 2026-09-29).
- **Engineering pilot metrics:** P2 wall-clock 11m54s (preflight 1m18s · S1 3m21s · S2 0m44s · S3 3m20s · handoff 2m53s) · 67 checks · 3 self-repairs, all in new test code, zero in product code · 0 Director touches between P2 start and the staging block · 0 stop conditions · preflight 17/17 PASS at P2 · 3 new suites / 20 tests (31/144 → 34/164).
- **Rulings:** A-01…A-14 (PF-05 own-protocol files; standalone static copy; nested-Escape guard; AC-401/AC-306 overlap erratum). Ledger E-16 (OBS-1 `protectPage` → Phase 8), E-17 (QA target substitution), E-18 (QA-F02 Enter on PBM trigger → accessibility backlog).
- **QA observations for the campaign:** QA active time 74m55s across two segments; 8 Director touches (1 environment ruling + 7 browser sign-ins) because the pack named SCRATCH accounts that did not exist; the Enter-key observation cost diagnostic reruns. Both are pack-authoring failures, not agent failures: the QA target and the test identities must be verified at authoring and declared in the checkpoints, and a known-instrument probe (Enter vs Space on native buttons) belongs in the QA preflight.
- **Factory lesson — keep:** machine-checkable preflight as a gate; enumerated stop conditions; declared checkpoints with none inside the build; one selective staging block; the Engineer copying the governing QA snapshot with provenance.
- **Factory lesson — change:** the QA side gets the same treatment in RRM-004 — a QA preflight that queries the accounts and the browser engine, enumerated QA stop conditions, a declared credential checkpoint with a one-sign-in-per-role target, and the plan authored by the QA seat from an Engineer-supplied manifest (the QAM pilot).
- **Factory lesson — drop:** preflight rows that assert what the environment *should* have (PF-14's bare standalone, RRM-003 A-02) instead of measuring what it does; naming an environment in a checkpoint without verifying it exists.
- **Closeout:** merged; RRM-004 (dependencies + QAM pilot) authored from this merge.

FRICTION LOG:

- 2026-09-28 — PF-05 at P1 held the Engineer's own root-protocol files; ruled A-01 (P1 exception, P2 literal).
- 2026-09-28 — Bare `node .next/standalone/server.js` 404s `/_next/static`; the "before" capture measured Next's 404 header. Ruled A-02: copy `.next/static` and `public/` into standalone before boot; every capture records the status line.
- 2026-09-28 — Nested Escape order held in jsdom but not in production (`document`-level listener); ruled A-06 (`if (e.defaultPrevented) return;` guard).
- 2026-09-28 — Director's pack commit accidentally deleted `agent_docs/PHASE_2.1` and `PHASE_2.2`; restored with `git checkout 3d2e655 -- …` before P1.
- 2026-09-28 — AC-401's preserved-path list overlapped AC-306's banner files; erratum via A-13.
- 2026-09-28 — Staging block not run before the QA branch was cut; recovered with `git add -A` then commit on the engineering branch.
- 2026-09-29 — QA sandbox (`bwrap`) failed before external commands; reviewed escalation worked.
- 2026-09-29 — DC-4 named SCRATCH; no SCRATCH accounts existed. Director authorized main development Supabase, login-only (E-17); seven sign-ins across diagnosis and reruns.
- 2026-09-29 — `curl -X HEAD` exit 18 on the header probe; corrected to `curl -I`.
- 2026-09-29 — Enter on the focused, closed PBM trigger swallowed; Space works. Non-blocking (E-18); origin check scheduled for RRM-004 Plan Mode.
- 2026-09-29 — Architect's service unavailable at closeout; the Director handed the QA Lead's certification to the Engineer as the closeout instruction; the Architect's journal entry lands here, in RRM-004 P0.

2. `agent_docs/RRM_CAMPAIGN_MAP_v1_0.md` §0 — in the scoreboard line replace RRM-003's `closeout + merge SHA: Director` with `closeout 7309a2f; merged to main 649c36d`; append a status paragraph: `**Status at v1.0.4 (2026-09-30).** RRM-003 merge recorded: 649c36d (closeout 7309a2f). **RRM-004 pack AUTHORED (dependencies; first QAM pilot on the QA side) — NEXT.** RRM-004 is the last module; its merge closes the RRM campaign and hands the backend campaign BIM-004.`

3. `agent_docs/RRM_FINDINGS_DISPOSITION_LEDGER.md` — in rows R-006, R-010, R-013, R-014, R-017, R-018 replace `closeout / merge: Director` with `closeout 7309a2f; merge 649c36d`. No other change.

4. `agent_docs/ACTIONS/RRM-003-CYBER-PHARMA/EXECUTION_LOG.md` § Closeout — `Closeout commit` → `7309a2f`; `Merge SHA` → `649c36d`. `agent_docs/ACTIONS/RRM-003-CYBER-PHARMA/README.md` — append `; merged to main 649c36d (2026-09-29)` to the CLOSED sentence.

5. Verify every table you touched is still valid Markdown and every placeholder you replaced is gone (`grep -n "to be supplied by the Architect\|to be filed by the Architect\|closeout / merge: Director\|recorded by Director at merge" agent_docs/` → only the QA Lead's journal placeholder remains). Root `CLAUDE.md` protocol for session log and CHANGELOG. Return modified files and a selective staging/commit block, one git command per line, commit message `30sep2026 - RRM-003 bookkeeping: Architect journal entry, friction log, closeout/merge SHAs`.

---

## P1 — Plan Mode (read-only, one stop)

ENGINEER — RRM-004-CYBER-PHARMA, Plan Mode. Read-only on the working tree. Writes: the plan in agent_docs/RESPONSES/ (root CLAUDE.md protocol), evidence/PREFLIGHT_P1.txt, evidence/S1_versions.txt (BASELINE block), evidence/S1_audit_before.json, evidence/S3_serve_before.txt, your session log. A scratch copy outside the tree is permitted for the dry run and is deleted before you return.

1. Run every row of agent_docs/ACTIONS/RRM-004-CYBER-PHARMA/ENVIRONMENT_PREFLIGHT.md and write the table with results to evidence/PREFLIGHT_P1.txt. Record <baseline> (the full SHA of the RRM-003 merge on main) at the top of the plan. PF-12 uses the floors (16.3.3 / 0.35.4) at P1. PF-16 writes the BASELINE block of evidence/S1_versions.txt. PF-19 writes evidence/S3_serve_before.txt. If any row fails, report it and stop — no plan on a failed preflight.

2. Read in order: CLAUDE.md, AUTHORITY_POINTER.md, DIRECTOR_CHECKPOINTS.md, RRM_BRIEF.md, ACCEPTANCE_SPEC.md, QA/README.md, QA/QAM_PILOT_CHARTER.md, QA/QAM_MANIFEST.md (the template you will fill at handoff); then agent_docs/RECON/RRM001_RECON_2026-09-18.md R6 and R3; agent_docs/ACTIONS/RRM-003-CYBER-PHARMA/RULINGS_ADDENDUM.md A-01, A-02; ledger R-009, E-17, E-18.

3. Produce the plan with these sections:
   a. **Targets (S1).** `npm view next versions --json` → the highest stable `16.3.x` (no canary, no rc) = proposed <target-next>; `npm view sharp versions --json` → the highest stable `0.35.x` ≥ 0.35.4 = proposed <target-sharp>; `npm view next@<target-next> peerDependencies engines optionalDependencies` and `npm view sharp@<target-sharp> optionalDependencies engines` quoted; confirm `eslint-config-next@<target-next>` exists; confirm Node satisfies both `engines`. State the libvips version `sharp@<target-sharp>` declares for `@img/sharp-libvips-<platform>` and, in the scratch copy, `npm pack @img/sharp-libvips-<platform>@<that version>` and read its `versions.json` `heif` — the expected AFTER value for AC-103 — then delete the tarball.
   b. **Dry run (S1 consequences).** In a scratch copy (`cp -r` of the tree without node_modules/.next), set the three lines, run `npm install --package-lock-only --ignore-scripts --no-audit`, and produce: the lockfile move inventory (`name: old → new`, count, classified by family per RRM_BRIEF.md), `npm audit --package-lock-only --json` totals and IDs before and after, and the list of anything outside the allowed families (expected: none). Then, on the same copy, `npm audit fix --package-lock-only --ignore-scripts` and report: additional moves, audit totals after, and whether package.json changed (expected: no). This is the evidence for DD-1. Delete the scratch copy. The working tree's lockfile is untouched at P1 (PF-05 at the end proves it).
   c. **Cloudinary scan (S2).** `grep -rn "res.cloudinary.com\|cloudinary" src public src/mocks docs README.md next.config.js`; every `next/image` and `<img` source in src/ with path:line and whether it is local. Recommend remove or narrow for DD-2 with the exact `images` block text for each. State that `src/proxy.ts:10` excludes `/_next/image` from the auth matcher and why removal closes the R-009 facet without touching proxy.ts.
   d. **Served-proof design (S3).** The exact curl lines for AC-204, AC-205 and AC-303 including the negative host probe; how you will hex-dump the first 16 bytes of the image body into evidence/S3_serve_after.txt; confirmation that the A-02 static copy step precedes boot.
   e. **QA-F02 origin (E-18, read-only).** Compare `git show 3d2e65565d820ecc8b89bc5813959a4e324b3acd:src/components/common/MultiSelect.tsx` (RRM-003's baseline) with the current file: was Enter on the closed trigger prevented before RRM-003 (cmdk / native button behavior) or introduced by RRM-003's container `onKeyDown`? Report with path:line. Flag-only; no change proposed in this module.
   f. **Manifest preview.** List the QA/QAM_MANIFEST.md fields you will be able to fill at handoff and any field you cannot (expected: none). Confirm you understand the manifest carries facts and claims only — no plan, no attack order, no expected values other than your own measurements labeled as claims.
   g. **Contradictions and risks.** Disk vs contract, path:line, recommended RULINGS_ADDENDUM.md row. Include the proposed targets as rows A-01/A-02 for the Director to confirm.
   h. **Stage plan.** Files per stage, checks per stage, the order S1 → S2 → S3 → handoff, the evidence file at each stage end, and your estimate of install wall-clock.

Return the plan on screen. No product changes, no install on the working tree. Await Director approval and the rulings (P1b).

---

## P1b — Apply Director rulings (documentation-only; Architect fills the rows)

ENGINEER — documentation-only step. No product changes, no installs, no builds, no Git mutations. Append the rows below to agent_docs/ACTIONS/RRM-004-CYBER-PHARMA/RULINGS_ADDENDUM.md (same continuous table, no blank lines); add any spec erratum rows to the lane in ACCEPTANCE_SPEC.md; add any campaign errata to agent_docs/RRM_FINDINGS_DISPOSITION_LEDGER.md and agent_docs/RRM_CAMPAIGN_MAP_v1_0.md §9 using the next free E-NN / CE-N verified on disk. Mark DIRECTOR_CHECKPOINTS.md DC-1 as satisfied with the date and the four DD rulings in one line each. Verify each ID appears exactly once and every table is valid. Root CLAUDE.md protocol for session log and CHANGELOG. Return modified files and a selective staging/commit block, one git command per line.

ROWS: <Architect supplies after reading the plan — at minimum A-01 target-next, A-02 target-sharp, A-03 DD-1, A-04 DD-2, A-05 DD-3, A-06 DD-4>

---

## P2 — One-shot build and handoff (single continuous session)

ENGINEER — RRM-004-CYBER-PHARMA, one-shot build. Tree is clean; plan approved; rulings on disk (targets <target-next> / <target-sharp>, DD-1…DD-4); DC-1 satisfied. This is one continuous session: you move S1 → S2 → S3 → handoff on your own, stopping only on an enumerated stop condition from CLAUDE.md. No Director touch is expected until you return the staging block. Record `date -Is` at start.

PREFLIGHT (gate). Run ENVIRONMENT_PREFLIGHT.md PF-01…PF-21 again with the ruled targets in PF-12; write evidence/PREFLIGHT_P2.txt. Any FAIL → stop condition 1: report and wait. PF-16 and PF-19 re-capture the BASELINE instrument value and served proofs on the untouched tree — do not skip them because P1 recorded them.

S1 — PIN + INSTALL + PROOF (AC-101–107, AC-401–403). Edit exactly three lines of package.json: `"next": "<target-next>"`, `"eslint-config-next": "<target-next>"`, `"sharp": "<target-sharp>"` under overrides. Record `date -Is`; run `npm install` (plain; no flags beyond `--no-fund`); record `date -Is`. If DD-1 = sweep: `npm audit fix` (no `--force`), then `git diff <baseline> -- package.json` must still be exactly three lines. Proof: `npm ls next sharp eslint-config-next`; `ls node_modules/@img/`; `node -p "const v=require('@img/sharp-libvips-<platform>/versions.json'); v.heif+' vips='+v.vips"` → AFTER block of evidence/S1_versions.txt; `npm audit --json` → evidence/S1_audit_after.json (temp-then-move) and the AC-104/105 grading in EXECUTION_LOG.md; the lockfile move inventory vs `git show <baseline>:package-lock.json` classified by family → evidence/S1_lockfile_moves.txt. Stage exit: `npm ls` at target with `overridden` · zero critical/high touching next/sharp/@img (and total 0 if sweep) · heif ≥ 1.23.2 and baseline value lower · package.json diff = 3 lines · zero moves outside allowed families. Any package.json line beyond three, any move outside the families, or an install failure → the matching stop (5 or 6). Record S1 in the log. Only then proceed.

S2 — CONFIG (AC-201–203). Apply the DD-2 ruling to the `images` block of next.config.js exactly as written in the addendum. `git diff <baseline> -- next.config.js` → evidence/S2_config_diff.txt; confirm no hunk touches `headers()`; `grep -nE "unoptimized|dangerouslyAllowSVG|loader:" next.config.js` → 0. Record S2. Only then proceed.

S3 — BOARD + SERVED PROOFS (AC-204–205, AC-301–304, AC-405). `rm -rf .next` + blank-env build; `rm -rf .next` + placeholder-env build (`https://placeholder.invalid`, placeholder keys, NEXT_PUBLIC_SITE_URL=http://127.0.0.1:36055) with the route table quoted; `npx tsc --noEmit`; `npx eslint .`; `npx jest --ci`; `git diff --stat <baseline> -- src src/__tests__ README.md docs/TESTING.md` (all empty) → evidence/S3_board.txt. Then A-02 static copy, boot the standalone server on 127.0.0.1:36055, and capture with status lines: `/`, one `/_next/static/chunks/*.js` from the build output, `/auth`, `/owedbook` (unauthenticated), `POST /api/auth/login` empty body, the `/_next/image` PNG probe with `Accept: image/webp` (save body to a temp file; `xxd -l 16` or `od -A x -t x1z -N 16` into the txt; delete the body), the negative Cloudinary host probe, and direct GETs of `/brand/logo-color.svg`, `/brand/logo-lockup.svg`, `/landing/owedbook-mockup.png` → evidence/S3_serve_after.txt. Stop the server; prove the port free (PF-09 command). Stage exit: both builds exit 0 with 17 routes · tsc 0 · eslint 0 errors · jest all pass zero skipped, counts equal baseline · header pair and negative controls per AC-303 · image probe 200 image/webp RIFF/WEBP · direct GETs 200 · negative host 400 (remove) or recorded (narrow). If a served proof is red after two in-scope self-repairs → stop 4. Record S3.

HANDOFF (same session). Assemble agent_docs/ACTIONS/RRM-004-CYBER-PHARMA/QA_HANDOFF.md with every field filled: contract paths; RULINGS_ADDENDUM rows; ledger resolution row appended to agent_docs/RRM_FINDINGS_DISPOSITION_LEDGER.md for R-009 with candidate = "Director's P2 commit, SHA recorded at cut" and evidence paths; references (recon R6/R3, reviews F9/A-003, the three advisory IDs, RRM-003 A-01/A-02, your P1/P2 reports); evidence/changed_files.txt (`git diff --name-status <baseline>` against the working tree — state that the candidate SHA is assigned by the Director's commit) and evidence/repair.diff (`git diff <baseline> -- package.json package-lock.json next.config.js`, temp-then-move; the lockfile hunk is large — that is expected); reproduction (install from lockfile with `npm ci`, board commands, A-02 serve method, placeholder env, the exact curl lines, no live Supabase call); QA/GOVERNING/ copied from agent_docs/ACTIONS/RRM-003-CYBER-PHARMA/QA/GOVERNING/ with a new PROVENANCE.md; unrun by design: authenticated image walk (QA, AC-605), QA's own install/build/serve (AC-601–604). **Fill QA/QAM_MANIFEST.md — every field of the template; facts and your labeled claims only; nothing that tells QA what to test first, what to expect beyond your measurements, or how to attack.** Fill EXECUTION_LOG.md Completion claim and §Metrics (timestamps, install wall-clock, checks, self-repairs, Director touches = 0 expected, stop conditions hit = none expected). Root CLAUDE.md protocol: session log, CHANGELOG (one entry for the module), completion report in agent_docs/RESPONSES/.

RETURN: `date -Is` at end; the exact changed-file inventory (added / modified / deleted); `git status --short` (node_modules must not appear); and ONE selective staging block — every path explicit, one `git add` per line group, then the commit line — for the Director to run as-is:
   git add package.json package-lock.json next.config.js
   git add <pack files: EXECUTION_LOG.md QA_HANDOFF.md evidence/… QA/QAM_MANIFEST.md QA/GOVERNING/…>
   git add <ledger/map files>
   git add <protocol files>
   git status --short
   git commit -m "<date> - RRM-004 one-shot: next <target-next> / sharp <target-sharp> (R-009), images per DD-2, board + served proofs, QA handoff + QAM manifest"
Do not commit. Do not self-certify. Stop after returning.

---

## P4 — QA-directed repair (template; Architect fills per round)

ENGINEER — RRM-004 QA repair round <N> on qa/phase-3-rrm004. Implement only the approved ruling package <QA Lead reference, derived from QA/REPAIR_PROPOSAL.md after Architect scope ruling>. Findings/ACs: <…>. Allowed files: <…>. Forbidden: frozen AC text, any src/ file, tests, headers(), any dependency line not named in the ruling, unrelated cleanup. Run: `npm ci` if the lockfile changed · tsc · eslint · jest · both builds · the served proofs the QA Lead named. Append to EXECUTION_LOG.md "Repair round <N>". Return a selective staging block; Director commits; QA Executor re-pins and retests; QA Lead re-adjudicates. No self-certification.

---

## P5 — Final closeout

RESERVED FOR THE ARCHITECT after the QA Lead's Gate Q, the pilot verdict and QA Cleanup. Will specify: map §0 scoreboard line and campaign-close status; ledger final disposition for R-009; RRM_CAMPAIGN_JOURNAL.md Architect entry with both pilots' metrics (QA Lead writes theirs; neither edits the other); QA/QAM_PILOT_RESULTS.md acknowledged by the Director (DC-7); certified SHA / QA HEAD / closeout commit recorded separately; RECOVERY.md update (permitted at P5); the Director's `--no-ff` merge line; the RRM campaign closing line and the BIM-004 handoff pointer. Not permission to close out early.
