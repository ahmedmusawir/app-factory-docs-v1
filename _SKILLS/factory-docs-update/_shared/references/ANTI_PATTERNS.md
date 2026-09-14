# ANTI_PATTERNS.md — Named Failures From Live Doctrine Operation

> Shared reference; load during Phase 1 (Claudy) and Stage 1 (Sol, Cody). Each entry is a real incident from the Wave 0–6 campaign (2026-07), the two v0.3 field runs (2026-08), or the Stage-A review (2026-09) — not a hypothetical. The family exists largely so these never recur.

## AP-1 — Bulk work over the MCP
**Incident:** 27-doc rename via per-file MCP calls; a minutes-job consumed a full working day before the Operator killed it.
**Rule:** D3 — the Hub clone with local git is the execution environment; the MCP is a rare, Operator-chosen exception (`sync-engineer/references/TOOL_ROUTING.md`).

## AP-2 — Grinding on instead of raising a hand
**Incident:** During AP-1, the agent kept executing long past reason; the Operator had to barge in.
**Rule:** D4 mid-flight checkpoint — on the exception route the agent announces the overrun and re-opens the route itself.

## AP-3 — Floating files
**Incidents (three strikes):** uncommitted housekeeping files forced a stash dance; `RECON_WAVE0.md` vanished during branch churn after a `reset --hard`; session files drifted uncommitted across a session boundary.
**Rule:** D11 close-out sweep with the explicit durable-versus-debris list. Every run ends with a status sweep; durable artifacts ride the PR in `_AUDIT/SYNC_<run>/`.

## AP-4 — Pushing to main / fighting the wall
**Incident:** 13 files committed to local main; push rejected (GH013). Correct exit was branch → PR → merge → reset local main.
**Rule:** D6. Main is PR-only. On main you PULL, never push. The rejection is the system working.

## AP-5 — Silencing the lints
**Incident (near-miss):** exempt-patterns were proposed for versioned-ref lint hits; ruling was to de-version the refs instead — exempting blinds the drift-killer.
**Rule:** D9. Caused-by-you → fix before commit. Pre-existing → baseline, report only. Exempt-patterns for real findings: never.

## AP-6 — Guessed archive versions
**Risk pattern:** stamping `_ARCHIVE/` copies with a remembered or assumed version number.
**Rule:** D7 step 1 — the suffix is read from the live doc's header at execution time, and step 5 proves the archive byte-equal to the base-SHA file (AC-A).

## AP-7 — Trusting a failed MCP call to have failed
**Incident class:** GitHub 50x errors where the write partially landed server-side; a blind retry then double-writes or conflicts.
**Rule:** D8 verify-after-write — re-read and compare blob SHAs before believing any outcome.

## AP-8 — Authoring without grounding
**Incident:** this skill's first draft was written before reading the Skills Playbook — single file, no CLAUDE.md, no frontmatter, no folder. Rejected on sight.
**Rule:** the doc governing a task is read BEFORE the task. For this family's own evolution: re-read the Skills Playbook before any structural change.

## AP-9 — Version suffixes leaking into live names or refs
**Incident class (F-011/F-032):** versioned filenames in cross-refs guaranteed drift; two docs even cited a version that never existed.
**Rule:** live docs = canonical names; versions live in headers, MANIFEST, and `_ARCHIVE/` only. The VERSIONED-REFS lint enforces it — see AP-5 for conduct when it barks. This is also why cargo conventions translate on landing (D15).

## AP-10 — Pasted commands with invisible characters
**Incident:** a C1 control char (`\302\226`) rode in on a pasted command and broke it bafflingly. Later, an em-dash inside `git commit -m` broke the shell wrapper (exit 127).
**Rule:** type commands by hand; plain hyphens in commit messages (D22); if a command fails inexplicably, hex-inspect it before debugging anything else.

## AP-11 — Cargo that never got asked about
**Incident (near-miss, 2026-08-05):** a promotion pack sat in the conversation while the skill's intake only hunted lessons files — the pack would have been missed without the Architect naming it in the launch prompt.
**Rule:** the `_INBOX/` cargo bay (standing since 2026-08-10) — every unit in it is presumptive cargo, classified aloud per D16 before Gate 1. The repo root is a legacy fallback only. The Operator's runbook says `_INBOX/`; the scan makes forgetting impossible from either side.

## AP-12 — Derived fields that drift while every row is "updated correctly"
**Incident (observed 2026-09-13):** MANIFEST stated "29 live docs" in three places while 31 existed on disk and 31 rows sat in its own tables; two runs had each updated "the doc's row" faithfully and nobody recomputed the count. The appendix still said "27 bodies."
**Rule:** D7 — infra documents' derived fields (count, ← map, appendix scope, CHANGELOG completeness) are checked against disk every run; fields the run changes are recomputed and proven by AC-I. "Update the row" is not "update the index."

## AP-18 — Absorbing baseline drift into an unrelated run
**Risk pattern (named in the TEST A hardening pass, 2026-09-14):** a stale-at-BASE index value (the same MANIFEST count) is "fixed while in there" by a run whose approved intake only edits wording in one doc — the repair enters the diff without ever being approved, and a TINY run is inflated or escalated by drift it did not cause.
**Rule:** D7 — pre-existing drift is detected, recorded as `DRIFT-…` in map §G, and parked; its repair is in scope only when the intake authorizes it or the run itself changes the underlying value.

## AP-13 — Self-certification on a campaign-scale sync
**Risk pattern:** the seat that wrote twenty diffs is the seat that proves nothing was missed. `QA_PLAYBOOK` §34 names it; the v0.3 Gate 4 was exactly this for every run size.
**Rule:** D20 — LARGE runs have an independent QA lane; TINY runs run under a recorded docs-only waiver and only when every fast-path condition holds. The route is evidence-driven (D3), not a convenience.

## AP-14 — QA writing doctrine through acceptance criteria
**Risk pattern:** a QA seat that "derives" a spec adds a requirement nobody approved, and the run is then graded against unapproved doctrine.
**Rule:** D20 derivation-only — every AC names its source (Correction / Intake ID, map row, or a standing family in `STANDING_INVARIANTS.md`); Tony approves the spec; it freezes.

## AP-15 — Adjudicating the correction instead of propagating it
**Risk pattern:** intent-level intake tempts the Engineer to decide a correction is wrong, unnecessary, or "already covered" and to land NO-CHANGE on his own authority.
**Rule:** D17 — NO-CHANGE is a proposal with path:line evidence that Tony approves; contradiction is CONFLICT → BLOCKED → Tony; Jarvis is consulted by Tony, not by the Engineer.

## AP-16 — Propagation by memory
**Incident class (the 43-finding audit):** the same rule stated three different ways across docs that were each edited "alone"; header-declared dependencies never listed the checklist that restated the rule.
**Rule:** D19 — search the corpus for the rule's terms, disposition every hit in the map, and have Cody re-run the searches at the candidate SHA on LARGE.

## AP-17 — The handoff that names its own commit
**Risk pattern:** a handoff "containing the final SHA" cannot exist, because committing it moves the SHA; a contract built on it is unexecutable and invites a push before approval "to get the real SHA."
**Rule:** D18 — CONTENT_SHA is recorded after the last content commit exists and before the handoff is committed; Cody records QA_START_SHA from the remote independently (`SHA_AND_PUSH_CONTRACT.md`).
