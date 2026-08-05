# ANTI_PATTERNS.md — Named Failures From the Doctrine Campaign

> Load during Phase 1. Each entry is a real incident from the Wave 0–6 campaign (2026-07)
> or live operation since, not a hypothetical. The skill exists largely so these never recur.

## AP-1 — Bulk work over the MCP
**Incident:** 27-doc rename via per-file MCP calls; a minutes-job consumed a full working
day before the Operator killed it.
**Rule:** Phase 3 routing gate; and since the 2026-08-05 ruling, local git is PRIMARY —
the MCP is a rare, operator-chosen exception (`references/TOOL_ROUTING.md`).

## AP-2 — Grinding on instead of raising a hand
**Incident:** During AP-1, the agent kept executing long past reason; the Operator had to barge in.
**Rule:** D4 mid-flight checkpoint — the agent announces the overrun and re-opens the
routing decision itself.

## AP-3 — Floating files
**Incidents (three strikes):** uncommitted housekeeping files forced a stash dance;
`RECON_WAVE0.md` vanished during branch churn after a `reset --hard`; session files
drifted uncommitted across a session boundary.
**Rule:** D11 close-out sweep. Every run ends with a status sweep; artifacts and cargo
ride the PR or an immediate housekeeping PR.

## AP-4 — Pushing to main / fighting the wall
**Incident:** 13 files committed to local main; push rejected (GH013). Correct exit was
branch → PR → merge → reset local main.
**Rule:** D6. Main is PR-only. On main you PULL, never push. The rejection is the system working.

## AP-5 — Silencing the lints
**Incident (near-miss):** exempt-patterns were proposed for versioned-ref lint hits;
ruling was to de-version the refs instead — exempting blinds the drift-killer.
**Rule:** D9. Caused-by-you → fix. Pre-existing → report only. Exempt-patterns for real
findings: never.

## AP-6 — Guessed archive versions
**Risk pattern:** stamping `_ARCHIVE/` copies with a remembered or assumed version number.
**Rule:** D7 step 1 — the suffix is read from the live doc's header at execution time.
`_ARCHIVE/README.md` is the governing law in the Hub.

## AP-7 — Trusting a failed MCP call to have failed
**Incident class:** GitHub 50x errors where the write partially landed server-side; a
blind retry then double-writes or conflicts.
**Rule:** D8 verify-after-write — re-read and compare blob SHAs before believing any
outcome, success or failure.

## AP-8 — Authoring without grounding
**Incident:** this very skill's first draft was written before reading the Skills
Playbook — single file, no CLAUDE.md, no frontmatter, no folder. Rejected on sight.
**Rule:** the doc governing a task is read BEFORE the task. For this skill's own
evolution: re-read the Skills Playbook before any structural change to these files.

## AP-9 — Version suffixes leaking into live names or refs
**Incident class (F-011/F-032):** versioned filenames in cross-refs guaranteed drift;
two docs even cited a version that never existed.
**Rule:** live docs = canonical names; versions live in headers, MANIFEST, and
`_ARCHIVE/` only. The VERSIONED-REFS lint enforces it — see AP-5 for conduct when it barks.
This is also why cargo conventions translate on landing (D15).

## AP-10 — Pasted commands with invisible characters
**Incident:** a C1 control char (`\302\226`) rode in on a pasted command and broke it bafflingly.
**Rule:** on the local route, type commands by hand; if a command fails inexplicably,
hex-inspect it before debugging anything else.

## AP-11 — Cargo that never got asked about
**Incident (near-miss, 2026-08-05):** a promotion pack sat in the conversation while the
skill's intake only hunted lessons files — the pack would have been missed without the
Architect naming it in the launch prompt.
**Rule:** Phase 1 cargo scan — packs (`DOCTRINE_PROMOTION*`, `*PATCH*`) in the repo root
are discovered automatically and become presumptive scope. The Operator's runbook puts
them in the root; the scan makes forgetting impossible from either side.
