# FINAL_HARDENING_REPORT — factory-docs-update v0.7-DRAFT → v0.8-DRAFT

> **Pass:** final bounded hardening after TEST A (TINY), TEST B (LARGE + independent Cody QA + repair/retest + Gate Q), TEST C1 (graceful resume) and TEST C2 (hard-crash resume) all passed on v0.7 · **Date:** 2026-09-26 · **Not a redesign.**
> **Candidate status:** **IMPLEMENTED — VALIDATED / FINAL HARDENING CANDIDATE.** Not v1.0. Nothing committed, nothing pushed.

Labels: **[FACT]** seen on disk or in command output · **[INFERENCE]** reasoned.

## 1. Starting SHA

| Item | Value [FACT] |
|---|---|
| Repository / branch | `app-factory-docs-v1` · `factory-docs-sync-process-001` (verified before and after) |
| HEAD | `dd6d496a3b269a6bf83ce4e85101d8e0e6e785b9` (required starting HEAD; unchanged at end — nothing staged, nothing committed) |
| Working tree at start | clean (`git status --porcelain` empty) |
| Lint baseline at start | ENCODING PASS · RETIRED-TERMS PASS · VERSIONED-REFS FAIL 8 · HEADER-PRESENCE FAIL 1 (33 live docs) — identical to the TEST A baseline |
| Rig | Windows, `core.autocrlf=true`; `git hash-object <file>` == `git rev-parse HEAD:<file>` confirmed on a skill file before any edit |

## 2. Version

v0.7-DRAFT → **v0.8-DRAFT**. Status everywhere: **IMPLEMENTED — VALIDATED / FINAL HARDENING CANDIDATE**. Header updated in `CLAUDE.md` and `README.md`; Version History rows added to `CLAUDE.md`, `sync-engineer/SKILL.md`, `sync-qa/SKILL.md`; the acceptance-spec template now cites STANDING_INVARIANTS "skill v0.8". Not promoted to v1.0.

## 3. Lessons absorbed

| # | Lesson | Resolution encoded | Where |
|---|---|---|---|
| 1 | CONTENT_SHA / frozen-map contradiction | The UPDATE MAP is frozen when the Gate 2 line is written; the only post-freeze write is an approved `AMENDED-v<n>`. CONTENT_SHA's authoritative home is `SYNC_HANDOFF.md` §0 (LARGE) / `RUN_SUMMARY.md` (TINY), later mirrored into QA evidence. Map §O ends at the Gate 2 line with a "recorded elsewhere, by design" pointer list (Gate 3 → spec §7; CONTENT_SHA, Gate 4, push, later overrides → handoff / run summary; QA_START_SHA → matrix). Override protocol (§6) writes to §O only before the freeze. | CLAUDE.md D10, D18, §6 · SHA_AND_PUSH_CONTRACT CONTENT_SHA row + both sequences · UPDATE_MAP §0 status, §O · SYNC_HANDOFF header + §0 · ACCEPTANCE_SPEC §0 · engineer P2 Gate 2 line, P4.5, anti-pattern 16 · AP-19 |
| 2 | QA intake portability | `_AUDIT/SYNC_<run>/INTAKE_SNAPSHOT/`: every in-scope cargo unit copied byte-for-byte on Gate 1 approval (run-state write), never edited afterwards (stamps go to RUN_SUMMARY), committed no later than the handoff commit so it rides the Gate 4 push; oversized units → `INTAKE_SNAPSHOT/REFERENCE.md` (repo + commit + path). Cody's intake input is the snapshot only; missing snapshot at QA_START_SHA → BLOCKED, and Cody does not ask the Engineer for files. | CLAUDE.md D10, D11 · engineer P1.7, P2.1, P5.2, P6.1, P9.3, P9.5, example, anti-pattern 19 · sync-qa independence rule, S0, S2.2, S3 AC-H · STANDING_INVARIANTS preconditions, AC-H · ACCEPTANCE_SPEC §0, §1, AC11 · SYNC_HANDOFF §0 row · UPDATE_MAP §0 row, §N · QA_MATRIX header · GATE_Q_REPORT environment · README QA step · AP-20 |
| 3 | Gate-4 metadata commit | Explicit sequence, identical in every file: CONTENT_SHA → `chore(sync): handoff for CONTENT_SHA <short>` (carries the snapshot if not yet committed) → ⛔ Gate 4 → approval time written in handoff §8 / RUN_SUMMARY → `chore(sync): gate 4 approval record [<run-id>]` (metadata-only, deliberate, after CONTENT_SHA) → the one push → Cody records QA_START_SHA. Cody's post-CONTENT diff allowance names the handoff, snapshot and Gate-4 record commits explicitly, so the commit is neither accidental nor a contradiction. | SHA_AND_PUSH_CONTRACT LARGE + TINY sequences + explanatory paragraph · CLAUDE.md D18 · engineer P5.2–P5 after-approval steps, example · SYNC_HANDOFF §8 · UPDATE_MAP §N commit plan · STANDING_INVARIANTS AC-S, AC-H · ACCEPTANCE_SPEC §1, AC2, AC11 · sync-qa S2.2 · QA_MATRIX header · README Gate 4 |
| 4 | CRLF-safe archive fidelity | Git-object method everywhere: pre-commit `git hash-object <archive>` and staged `git rev-parse :<archive>` (Engineer), committed `git rev-parse <cand>:<archive>` (QA), each equal to `git rev-parse <BASE_SHA>:<source>`. The literal `git show … \| diff -` is retired as evidence with the TEST C2 reason stated. | CLAUDE.md D7(5) · engineer P4.2.5, example, anti-pattern 17 · TOOL_ROUTING · STANDING_INVARIANTS AC-A · ACCEPTANCE_SPEC AC9 · SYNC_HANDOFF §3 · UPDATE_MAP §M · sync-qa S3 AC-A · GATE_Q_REPORT evidence row · AP-6 pointer, AP-21 |
| 5 | Interrupted-run dirty state | UPDATE_MAP §N now records the **expected run-state set** (map, snapshot, draft run summary, session / recovery state, response logs). Engineer P4.1: compute the dirty set → compare to §N → unexplained path = STOP / BLOCKED; exact subset = lawful resume → `chore(sync): run-state checkpoint [<run-id>]` when the commit plan requires it → clean tree is required before the first per-doc canonical write, not before Phase 4 entry. D22's "unexplained" is defined by §N. | engineer P4.1, P0 resume, example, anti-pattern 18 · CLAUDE.md D15a (2a), D22 · UPDATE_MAP §N · SHA_AND_PUSH_CONTRACT sequence · README resume gotcha · AP-22 |
| 6 | Recovery authority hierarchy | D15a opens with the hierarchy: RECOVERY.md / session files ADVISORY; authoritative = git branch/HEAD/history → working-tree diff → `_AUDIT/SYNC_*` artifacts → approved UPDATE MAP → intake / `INTAKE_SNAPSHOT/` → canonical disk; on contradiction git + disk + approved durable artifacts win and the discrepancy is reported. A fresh agent must reconstruct the seven items (active run, BASE_SHA, approved route, gate status, current phase, expected dirty state, next legal action) without conversational memory or a graceful shutdown. | CLAUDE.md D15a · engineer P0 RESUME, P9.7 · sync-qa independence rule · README resume gotcha · AP-22 |
| 7 | UPDATE_MAP manual row-count ambiguity | Enumerated rows are the authority. §B "Hit count `<n>`/`<n>`" placeholders removed ("the rows are the count"); §N tally redefined as derived from §C / §D / §H rows at the moment of writing; §P A1/A2 defined as counts of §A / §C rows "counted now"; §M archive count = §C "Archive expected: YES" rows; handoff CHANGELOG-row and archive claims counted from the handoff's own §1 rows. A stated total that disagrees with its rows is a defect in the total. | UPDATE_MAP §B, §M, §N, §P · SYNC_HANDOFF §3 · engineer P2.6 · AP-23 |
| 8 | Skill Validation Protocol follow-up | Recorded in §7 below only. No canonical doctrine touched. | this report |

Also updated: ANTI_PATTERNS header now names the v0.7 validation campaign as an incident source; five new entries AP-19 … AP-23 (each a real TEST B / C incident).

## 4. Files changed

All under `_SKILLS/factory-docs-update/` [FACT: `git status --porcelain`; `git diff --stat` = 13 files, +124 / −76 before the two residual fixes]:

`CLAUDE.md` · `README.md` · `_shared/references/ANTI_PATTERNS.md` · `_shared/references/SHA_AND_PUSH_CONTRACT.md` · `_shared/references/STANDING_INVARIANTS.md` · `_shared/templates/DOCSET_SYNC_ACCEPTANCE_SPEC.md` · `_shared/templates/SYNC_HANDOFF.md` · `_shared/templates/UPDATE_MAP.md` · `sync-engineer/SKILL.md` · `sync-engineer/references/TOOL_ROUTING.md` · `sync-qa/SKILL.md` · `sync-qa/templates/QA_MATRIX.md` · `sync-qa/templates/GATE_Q_REPORT.md`

Created: this report. Untouched family files: `_shared/references/INTAKE_TAXONOMY.md`, `sync-engineer/decision-trees/route-selection.md`, `sync-engineer/templates/LESSONS_LEARNED.md` (no lesson lands in them). No file added to or removed from the skill; no new folder in the skill (INTAKE_SNAPSHOT is a run-folder artifact, not a skill file).

Outside the authorized surface, uncommitted, per the Hub's own session protocol (repo `CLAUDE.md`): `session_2026-09-26.md` (new) and `agent_docs/RESPONSES/response_2026-09-26_*.md` (plan + this report's mirror). They are disposable process logs; `RECOVERY.md` was not touched.

## 5. Preserved behavior

Not redesigned, verified by reading the changed text against the preserve list: automatic TINY/LARGE routing (`route-selection.md` untouched; no new condition) · Correction Package intake (taxonomy untouched) · UPDATE_MAP as the single planning source (strengthened — it is now genuinely immutable after Gate 2) · Sol derivation-only acceptance spec · Cody independent QA (strengthened — inputs now portable) · Gate 1 / 2 / 3 / 4 / Q ownership unchanged (no new gate; the Gate-4 record commit is a mechanic inside Gate 4's existing owner) · bounded repair loop untouched · Hub-only git carve-out (D5 unchanged) · other `_SKILLS` and lints read-only (D21 unchanged) · per-tier `_assets` rule untouched · the ten standing invariant families (no family added; AC-A's check and AC-S/AC-H's evidence lists refined) · TINY fast path: no new gate, seat or artifact — the snapshot is one `cp -r` the D11 durable set already required, and CONTENT_SHA simply moves from the map to RUN_SUMMARY.

## 6. Focused validation results

| Check | Result |
|---|---|
| No post-Gate-2 frozen-map mutation required for CONTENT_SHA | PASS [FACT] — grep `map §O` / `UPDATE_MAP §O` / `UPDATE MAP §O` across the skill: remaining hits are the AP-19 incident text, §O's own "recorded elsewhere" list, the pre-freeze override rule, and the handoff header saying "never into the map". Both residual contradictions found by the sweep (CLAUDE.md §6 override recording; SYNC_HANDOFF header TINY fields) were fixed and re-grepped |
| Fresh QA can obtain immutable approved intake from the durable package | PASS — INTAKE_SNAPSHOT defined in D11, taken at engineer P1.7, committed by the handoff commit at the latest (P5.2, SHA contract), required by STANDING_INVARIANTS preconditions, spec §1, QA_MATRIX header, sync-qa S0/S2; Cody forbidden from reading local `_INBOX/`; immutability checked by AC-H (`git log --diff-filter=M`) |
| Gate-4 metadata commit is explicit | PASS — named commit `chore(sync): gate 4 approval record [<run-id>]` appears in the SHA contract (both sequences), D18, engineer P5, handoff §8, map §N, spec AC2/AC11, sync-qa S2.2, QA_MATRIX; the post-CONTENT diff allowance names it |
| Archive fidelity is EOL-safe | PASS [FACT] — no remaining `\| diff -` fidelity instruction except the AP-21 incident quote and explicit retirement notes; `git hash-object` == `git rev-parse HEAD:<path>` demonstrated on this autocrlf rig |
| Interrupted dirty-state recovery is executable | PASS — §N expected run-state set (a concrete path list) + P4.1 three-way outcome (STOP / checkpoint commit / proceed) + D15a step 2a + D22 definition of "unexplained" |
| Recovery works without RECOVERY.md / session truth | PASS — D15a hierarchy; "if absent, skip them"; seven reconstruction items; P0 and sync-qa restate it; README tells the Operator the same in plain words |
| No row-count self-contradiction remains in templates | PASS [FACT] — grep `Hit count` empty; §N/§P/§M/handoff counts are all defined as row-derived |
| TINY remains lightweight | PASS — no new gate, artifact or seat; TINY sequence in the SHA contract gains one metadata commit line (the Gate-4 record) and the snapshot rides the existing metadata commit |
| LARGE remains intact | PASS — P3, P6, S1–S5, Gate 3/4/Q, repair loop and verdict vocabulary unchanged; only evidence forms and preconditions refined |
| Lint baseline does not worsen | PASS [FACT] — after: ENCODING PASS · RETIRED-TERMS PASS · VERSIONED-REFS FAIL 8 · HEADER-PRESENCE FAIL 1 — identical to start |
| No canonical doctrine changed | PASS [FACT] — `git status` shows only `_SKILLS/factory-docs-update/**`, this report, and the two uncommitted process logs; MANIFEST, CHANGELOG, tiers, lints, `.github/`, `_AUDIT/`, `RECOVERY.md`, test branches untouched |
| No synthetic TEST B/C content leaked into the skill branch | PASS [FACT] — no `_AUDIT/SYNC_*`, no tier or archive path in the working tree; test branches `test/docset-sync-v0*` neither merged nor cherry-picked; HEAD still `dd6d496` |
| Line budgets | PASS [FACT] — engineer SKILL 204 lines, QA SKILL 141, CLAUDE.md 189 (500-line budget) |
| Single CLAUDE.md; no commit; no push | PASS [FACT] — nothing staged; `git rev-parse HEAD` unchanged |

TEST A / B / C were **not** rerun, per the directive.

## 7. Parked doctrine follow-ups

| ID | Item | Status |
|---|---|---|
| **FH-01 — Independent Skill Validation Protocol** | This campaign validated a reusable pattern: **TINY behavioral test → LARGE multi-seat test → independent QA → repair/retest → graceful recovery → hard-crash recovery.** Each stage found a defect class the previous one could not (TEST A: drift/BASE semantics; TEST B: frozen-map mutation, intake portability, hidden Gate-4 commit, row-count drift; TEST C: CRLF fidelity, dirty-state and recovery-authority gaps). **Recommendation:** promote it into `APP_FACTORY_SKILLS_PLAYBOOK` as an "Independent Skill Validation Protocol" section, gating any skill's DRAFT → 1.0 promotion, **after Operator approval and through the factory-docs-update run itself** (it is canonical doctrine). | PARKED — not implemented here by directive |
| TESTA-F03 | Version-bump magnitude rules | Still DEFERRED — no authorizing Factory rule |
| HP-01 | Repo `CLAUDE.md` Plan-Mode approval ceremony | Directive served as the approved plan (autonomous session, no interactive approval available); session file and RESPONSES logs were written this time but remain uncommitted and outside the authorized surface — disposition is the Director's |
| HP-03 | MANIFEST derived-field drift in the Hub | Unchanged; still needs its own authorized job (`DRIFT-…` pattern) |
| HP-04 | LF → CRLF warnings on edited skill files | Informational; now also documented as the reason for lesson 4 |
| HP-05 | `examples/` still absent | Populate from TEST B's run folder once the Operator rules which synthetic artifacts may be promoted as an example |
| FH-02 | `RECOVERY.md` at the Hub root is stale (last action 2026-08-10) | Out of surface; a resuming agent is now told to distrust it anyway (D15a) — refresh at the next housekeeping commit |

## 8. Readiness for merge

**READY for Director review and merge preparation** [INFERENCE]. The eight lessons are encoded consistently across the thirteen files, the sweep's two residual contradictions were fixed, the lint baseline is identical, the diff is confined to the authorized surface, and no test-branch content rides along. Suggested commit shape when the Director authorizes it: `fix(skill): final hardening of docset sync to v0.8-DRAFT` on this branch, followed by the Director's PR to `main`. v1.0 promotion should wait for one real (non-synthetic) LARGE sync under v0.8 and for the FH-01 doctrine decision.

---
*Final DocSet Sync hardening complete. v0.8-DRAFT is ready for Director review and merge preparation.*
