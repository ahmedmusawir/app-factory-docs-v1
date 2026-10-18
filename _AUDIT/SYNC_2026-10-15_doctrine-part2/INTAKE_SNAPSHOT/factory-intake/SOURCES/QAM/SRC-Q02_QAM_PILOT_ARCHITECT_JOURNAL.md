# QAM Pilot — Architect's Journal

**Scope:** the first QA Module run, carried on RRM-004-CYBER-PHARMA (Cyber Pharma v1, repo `cyber-pharma-dev-v1-phase-3`). Architect's seat only; the QA Lead keeps his own, and neither edits the other. Entries are dated in the Director's local time. Facts first, opinion marked. Destination: the 10X Lab, as the primary record of how the QAM shape was born, what it cost, and what it taught — the basis for every future ABM and APBM.

**Seats:** Architect (Fable) · Engineer (Claudy) · QA Lead (SOL) · QA Executor (Cody) · Director (Tony). Positions, not names, in the pack files.

---

## Lineage — how we got here (recorded 2026-09-30, from the campaign record)

- **RRM-001** (closed 2026-09-22): manual QA matrix; Director copied governing QA docs into the repo with provenance. Lesson: the Executor must never need an outside-repo read.
- **RRM-002** (closed 2026-09-28): first agent-driven browser QA (16-state authenticated matrix); the only interruption was the environment (paused replica, drifted identities). QA Lead's field note proposed a one-shot run shape with a mandatory environment preflight.
- **RRM-003** (closed 2026-09-29): one-shot **Engineering** pilot — 17-row preflight as a gate, 8 enumerated stops, 6 declared checkpoints, 3 prompts. P2 ran 11m54s, 67 checks, 0 stops, 0 Director touches. QA side: 74m55s active over two segments, **8 Director touches (1 ruling + 7 browser sign-ins)** because the pack named SCRATCH accounts that did not exist. QA Lead proposed the QAM (prepared QA folder, one command); Architect's opinion (2026-09-29): adopt, but *whoever built the candidate does not write the plan that tests it*.
- Architect wrote the one-shot Engineering field note and the QAM opinion for the 10X Lab the same day.

## 2026-09-30 — RRM-004 pack authored with the QAM overlay inside `QA/` (v1.0)

- Authored from `main @ 649c36d` with versions and advisories read from the lockfile and the registry, not memory. Ran the full upgrade in a scratch copy first: 41 lockfile moves, build 17 routes, jest 34/164, cache header survives, `/_next/image` serves webp through sharp 0.35.5. Found that `eslint-config-next` must move in lockstep (three-line `package.json` diff, not two) and that `npm audit fix` without `--force` clears three transitive highs — surfaced as Director decision DD-1 instead of being decided by me.
- Sandbox lesson: `next/font/google` fetches at build time; my container's network refused it and the build died. Became preflight row PF-13 / QF-07. *Opinion:* every preflight row should come from a real failure somewhere.
- QAM overlay v1.0 shipped inside `QA/`: `AGENTS.md` (Cody's law), charter, QF preflight, manifest template (Engineer fills), plan placeholder marked "QA Lead only", output templates, Q-stops, one Director command. Separate AC-700 lane grades the pilot process; never gates Gate Q.
- P0 landed RRM-003's missing Architect journal entry and friction log (lost to a service outage on closeout night). P1 plan matched the authoring dry run exactly and caught a real instrument bug: `require('.../versions.json')` throws `ERR_PACKAGE_PATH_NOT_EXPORTED`; the exported subpath `.../versions` reads the same file (A-03). P1b: targets 16.3.7 / 0.35.5, DD-1 sweep, DD-2 remove Cloudinary, DD-3 main-dev login-only, DD-4 authorship split.
- **P2 one-shot: 11m15s, 80 checks, 0 stops, 0 self-repairs, 0 Director touches.** heif 1.23.1 → 1.23.5; audit 7 → 0; 59 moves, 0 outside families; Cloudinary host probe `400` with the attributable body. Every number equal to P1 and to my authoring run. Second consecutive clean one-shot on the Engineering side.

## 2026-09-30 — The Director's brain-dump and the reconciliation

- Director, while P2 ran: "what we are doing now is not QAM" — two scenarios for who writes the QAM folder and when; Part 1 asks for a QA env file so the Director stops typing credentials. Dropped on both the Architect and the QA Lead to "work it out, make it pretty".
- Architect's proposal (same day): skeleton authored with the pack from the QA Lead's playbook (Scenario One); facts filled by the Engineer at handoff; **plan written by the QA seat** (the line neither scenario named); Cody runs Q1 recon → QA Lead thumbs up → Q2 one-shot; `.env.qa.local` with gitignore proof, key-count-never-cat, login-only, deletion with proof, privacy scan blocking certification, Director-owned rotation. Pointed out that RRM-004 v1.0 already *was* this in everything but the folder name.
- **QA Lead's rulings (2026-09-30 evening):** model accepted. R1: RRM-004 is the pilot — rename `QA/`→`QAM/`, add Q1/Q1b/Q2/Q4/cleanup entry points, enable the env file now, not at BIM-004. R2: Cody *drafts* the plan in Q1 from the frozen spec + the QA Lead's carried risk requirements + the manifest + recon; the QA Lead amends and approves before Q2 — independence kept, one fewer file for the Director to install. R3: `QAM_ENTRY.md` model-neutral start; Cody's law stays `AGENTS.md`, never `CLAUDE.md` (Cody is a persistent seat with a swappable brain). R4: five env keys; Q1 must prove ignored / exact keys / target match / both identities authenticate / nothing leaks; no dotenv as product dep; delete env + auth state at the end pass or fail; certification blocked on any leak; rotation Director-owned.
- *Correction the Architect had to make to the premise:* "authored but not started" was not the state — v1.0 was committed and P2 was mid-run. v1.1 therefore lands as an **overlay after DC-2** with a tracked `git mv`, and the frozen engineering files take their changes as addendum rows A-09…A-12 plus erratum-lane entries, never a rewrite. *Opinion:* this is the first time the frozen-contract rule and the pilot pulled in opposite directions; the rule won, and the cost was one docs-only prompt (P2b). Worth keeping as precedent.
- One technical catch from the QA Lead: a `\|` in a Markdown table cell is not a shell pipe. v1.1 writes every command with a pipe as a plain line, never a cell.

## 2026-10-01 — Overlay v1.1 delivered; DC-2 done

- Candidate committed: **`2fbc72f1f514049255f2b94054bd11cc77cbd158`** (Director, DC-2, 10:40 KL). Clean tree, pushed.
- Overlay v1.1 (17 files): `QAM_ENTRY.md`, `AGENTS.md` (phases, Q1–Q8 stops incl. new Q8 for the env file), `QAM_PROMPTS.md` (P2b · Q1 · Q1b · Q2 · Q4 · Q5), `QAM_CHECKPOINTS.md` (QC-1…QC-5 with the exact commands), `QAM_PREFLIGHT.md` (QF-01…QF-18; QF-13–17 are the credential rows; QF-10 is the Enter/Space known-instrument probe from RRM-003's QA-F02), `QAM_RISK_REQUIREMENTS.md` (§A the QA Lead's standing doctrine lifted from his RRM-002/003 plans so no second file is installed; §B Architect risk input; §C for the QA Lead to fill), plan placeholder, charter and results templates revised. Excludes Claudy's `QAM_MANIFEST.md` and `GOVERNING/` so the rename carries them untouched.
- Q5 ordering decided: value-hash privacy scan **while the env file still exists**, then delete env + auth state with proof, then pattern-mode rescan. Certification blocked unless both read 0.
- Director runway from here: OV-1 (mv, rm, unzip, commit) → OV-2 (P2b) → DC-3 (QA branch + QA Lead ratifies four files) → QC-1 (env file, Q1 command) → QC-2 (plan approved, Q2 command) → QC-4 (Q5) → certification → QC-5 rotation → DC-7 merge, RRM campaign closes.

## Open questions the pilot should answer (for the 10X Lab)

1. Does Cody's Q1 plan draft, written from the spec + carried requirements, need more than light amendment from the QA Lead? If yes, the carried requirements (§A/§C) are the lever, not the Executor.
2. Director touches inside Q2: is zero achievable with the env file, or does the headless login hit a wall (MFA, captcha, rate limit) that forces a QC-3?
3. Q1 recon wall-clock vs the hours RRM-003 lost to a missing environment — the number that justifies the planned stop.
4. Does the value-hash scan ever fire? If it never does across modules, keep it anyway; it is cheap and the one time it fires pays for all of them.
5. Does the overlay-after-freeze pattern (A-09…A-12) read cleanly to a QA Executor that never saw v1.0? If Cody trips on a stale `QA/` path in a frozen file despite A-09, the lesson is that path indirection belongs in the entry file, not the contract.

*(Entries continue as the pilot runs. Metrics land in `QAM/QAM_PILOT_RESULTS.md`; this journal records what the metrics cannot — the decisions, the corrections, and why.)*

## 2026-10-02 — Gate Q PASS; pilot PARTIAL SUCCESS; closeout written

- QA Lead certified: **Gate Q PASS**, 31 product ACs, zero repair rounds, candidate `2fbc72f`, QA HEAD `6b6cad6`, evidence `0463086`. Product identity proven unchanged from candidate to closeout (empty product diff). Handoff zips hash-matched.
- **Pilot verdict: PARTIAL SUCCESS** under the charter's own recorded-Q-stop rule — Q1 raised a contract/scope stop (A-15: narrow AC-403 exception for predecessor closeout hunks and the 12 `_OLD/` moves), resolved through Q1b. *Opinion:* that stop was authoring debt — the Architect should have pre-ruled it in the pack. It is exactly what the recon stop is for, and it fired before any expensive step.
- **Q2 one-shot succeeded:** 10m08s body (17m21s release elapsed, excluding Q1), zero Director interventions, one automated sign-in per role from `.env.qa.local`, zero Q2 stops, one helper self-correction (Q2-SR01: non-exported `sharp/package.json` path — the same export-map trap the Engineer hit at P1 with `versions.json`). Q5: value scan before deletion, env file and auth state removed with proof, post-deletion scan 0. Comparison: RRM-003 QA took 74m55s active and 8 Director touches, 7 of them human sign-ins.
- KEEP / CHANGE / DROP per the QA Lead's letter. CHANGE that lands on the Architect: resolve scope exceptions before Q1; make `CLAUDE.md` and `AGENTS.md` both reliable model-neutral entries; ship `QAM/` in the pack from day one so no mid-flight overlay is ever needed again.
- **Process lesson from P5 itself:** the Architect's first closeout prompt *referred to* the QA Lead's letter without *carrying* it. The Engineer searched, found nothing, and refused to reconstruct a certificate from the Architect's summary — correctly. Rule: a prompt that says "transcribe verbatim" must contain the text it transcribes.
- Engineer flagged: the Architect's journal entry says P2b wrote A-09…A-12; on disk P2b also wrote A-13, ratification added A-14, Q1b added A-15. He did not edit another seat's entry. Corrected here and in the post-merge touch.
- Open: Director's `--no-ff` merge (DC-7), QC-5 password rotation, DC-7 adopt/amend/drop ruling, post-merge SHA recording.
