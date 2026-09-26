# response_2026-09-26_173500 — FINAL HARDENING PLAN (v0.7-DRAFT → v0.8-DRAFT)

🔵 ENTERING PLAN MODE
Task: absorb the eight validated TEST A/B/C lessons into `_SKILLS/factory-docs-update/**`; write `fable-sync-review/run-001/FINAL_HARDENING_REPORT.md`. No redesign. No commit. No push.

Preflight [FACT]: branch `factory-docs-sync-process-001` · HEAD `dd6d496a3b269a6bf83ce4e85101d8e0e6e785b9` · tree clean · lint baseline = TEST A baseline (VERSIONED-REFS 8, HEADER-PRESENCE 1, 33 live docs) · `git hash-object <file>` == `git rev-parse HEAD:<file>` proven on this core.autocrlf=true rig.

📋 PLAN:
1. Lesson 1 (frozen map / CONTENT_SHA) — map §O is written through the Gate 2 approval line only; CONTENT_SHA, Gate 3, Gate 4, push time and post-Gate-2 overrides live in SYNC_HANDOFF (LARGE) / RUN_SUMMARY (TINY); §O keeps a pointer field. Touch: CLAUDE.md D10/D11/D18, SHA contract, UPDATE_MAP §O, SYNC_HANDOFF §0, engineer P4.5/P5/Gate 2 line/example, anti-pattern.
2. Lesson 2 (QA intake portability) — `_AUDIT/SYNC_<run>/INTAKE_SNAPSHOT/` copied as received at Gate 1 (run-state write), immutable, committed no later than the handoff commit on LARGE; Cody's evidentiary input is the snapshot, never local `_INBOX/`; missing snapshot at QA_START_SHA → BLOCKED. Touch: CLAUDE.md D11, engineer P1/P5/P9, sync-qa independence rule/S0/S2, spec preconditions, handoff §0, QA_MATRIX header, GATE_Q_REPORT environment, STANDING_INVARIANTS preconditions/AC-H, UPDATE_MAP §0, README.
3. Lesson 3 (Gate-4 metadata commit) — explicit sequence: CONTENT_SHA → handoff/audit commit → Gate 4 approval → `chore(sync): gate 4 approval record [<run-id>]` → push → Cody records QA_START_SHA; the post-CONTENT diff allowance names this commit. Touch: SHA contract sequences (LARGE + TINY), CLAUDE.md D18, engineer P5, handoff §8, spec AC2, sync-qa S2, README Gate 4.
4. Lesson 4 (CRLF-safe fidelity) — replace every `git show <BASE>:<path> | diff - <archive>` with `git hash-object <archive>` == `git rev-parse <BASE_SHA>:<path>` and, after staging, `git rev-parse :<archive>` == same. Touch: CLAUDE.md D7(5), engineer P4.2.5, TOOL_ROUTING, STANDING_INVARIANTS AC-A, spec AC9, handoff §3, sync-qa S3 AC-A, ANTI_PATTERNS AP-6, GATE_Q_REPORT automated evidence.
5. Lesson 5 (interrupted-run dirty state) — P4.1 replaces "confirm the tree is clean" with: compute dirty set → compare to the approved expected run-state set (map §N) → unexplained → STOP/BLOCKED; exact → run-state checkpoint commit when the commit plan requires it → clean tree required before the first per-doc sequence. Touch: engineer P4.1, UPDATE_MAP §N, CLAUDE.md D15a/D22.
6. Lesson 6 (recovery authority hierarchy) — D15a states: RECOVERY.md/session = advisory; authoritative = git branch/HEAD/history, working-tree diff, `_AUDIT/SYNC_*`, approved map, intake/snapshot, canonical disk; the seven reconstruction items. Touch: CLAUDE.md D15a, engineer P0, sync-qa S0, README gotcha, ANTI_PATTERNS.
7. Lesson 7 (row-count ambiguity) — enumerated rows are authority; §B hit-count placeholders removed; §N tally and §P counts defined as row counts; handoff/spec `<n>` fields stated as derived. Touch: UPDATE_MAP §B/§M/§N/§P, SYNC_HANDOFF §3, ANTI_PATTERNS.
8. Lesson 8 — follow-up record in the report only (Independent Skill Validation Protocol → APP_FACTORY_SKILLS_PLAYBOOK, after Operator approval). No doctrine edit.
9. Version 0.8-DRAFT, status IMPLEMENTED — VALIDATED / FINAL HARDENING CANDIDATE: CLAUDE.md header + VH row; README header; engineer + qa SKILL.md VH rows; spec template "(skill v0.8)".
10. Focused validation: greps for stale `| diff -`, `Write it in map §O`, `Hit count`, `confirm the tree is clean`; lint re-run; `git status` confined to the writable surface; no test-branch content merged.

FILES TO MODIFY: CLAUDE.md · README.md · _shared/references/{ANTI_PATTERNS, SHA_AND_PUSH_CONTRACT, STANDING_INVARIANTS}.md · _shared/templates/{UPDATE_MAP, SYNC_HANDOFF, DOCSET_SYNC_ACCEPTANCE_SPEC}.md · sync-engineer/SKILL.md · sync-engineer/references/TOOL_ROUTING.md · sync-qa/SKILL.md · sync-qa/templates/{QA_MATRIX, GATE_Q_REPORT}.md
FILES TO CREATE: fable-sync-review/run-001/FINAL_HARDENING_REPORT.md
FILES I WILL NOT TOUCH: INTAKE_TAXONOMY.md, route-selection.md, LESSONS_LEARNED.md (no lesson lands there) · canonical tiers, MANIFEST, CHANGELOG, lints, .github, RECOVERY.md, `_AUDIT/`, test branches.

ASSUMPTIONS: (1) the Director's directive is the approved plan (HP-01 precedent; autonomous session). (2) Session file + this RESPONSES log are uncommitted run-state writes per repo CLAUDE.md, outside the merge surface. (3) INTAKE_SNAPSHOT is copied on both routes at Gate 1 (one `cp -r`; D11 already required the package in the durable folder) but is REQUIRED-committed only on LARGE before the push.

RISKS: wording drift between the 12 files — mitigated by the grep sweep in step 10.

→ Proceeding under the directive-as-plan assumption.
