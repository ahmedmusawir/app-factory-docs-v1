# UPDATE MAP — <run slug> — <YYYY-MM-DD>

> **The approved execution source of truth for this synchronization run** (supersedes RIPPLE_MAP since skill v0.6). Authored by Claudy (Engineer seat). Approved by Tony at Gate 2. Consumed by Sol (spec derivation), Cody (verification), and Claudy (execution, EXACTLY as approved). This file — not memory, not the branch — is what execution follows and what QA measures against. Lives at `_AUDIT/SYNC_<YYYY-MM-DD>_<slug>/UPDATE_MAP.md`.
>
> Evidence labels on every non-trivial cell: EVIDENCE (path:line / SHA / command output) · INFERENCE (from what) · CLAIM (package / Operator says) · GAP (looked where) · QUESTION (needs Tony).

## 0. Run header

| Field | Value |
|---|---|
| Run ID | `SYNC_<YYYY-MM-DD>_<slug>` |
| Run branch | `docs/sync-<slug>-<YYYY-MM-DD>` (default) — or the existing approved run branch, named as-is |
| BASE_SHA | `<sha>` — the execution base every placement in this map is verified against; evidence: `<launch line / intake names it>` or `<clean discovered HEAD on <branch>>`. Recorded before Gate 2 and approved with the map; never assumed to be main; execution branches FROM it or reuses the run branch at it / a lawful descendant (D18). Change after Gate 2 = AMENDED-v<n>. |
| Merge target | `main` (production sync) / `<branch>` — the compare-URL base in Phase 8 |
| Execution route | Local git at a Hub clone (standing ruling 2026-08-05) — or the MCP exception with Operator choice recorded here |
| **Path** | **TINY** / **LARGE** — decided by `sync-engineer/decision-trees/route-selection.md`; evidence in §P |
| QA arrangement | TINY: "Docs-only QA waiver recorded per SOFTWARE_FACTORY_PLAYBOOK §2.5 item 6 — Operator, <date/time>" · LARGE: "Independent QA lane (Sol / Cody); spec at `<run>/DOCSET_SYNC_ACCEPTANCE_SPEC.md`" |
| Status | DRAFT → APPROVED (Gate 2, <date/time>) → AMENDED-v<n> (Gate 2, <date/time>) |
| Lint baseline (pre-existing) | `<count>` findings: `<path:line [LINT-ID]>` … (from discovery; also §M) |
| Live-doc count on disk / MANIFEST rows / MANIFEST stated (at BASE_SHA) | `<n>` / `<n>` / `<n>` — any mismatch not caused by this run → §G baseline drift |

## A. Intake ledger

| ID | Class (INTAKE_TAXONOMY #) | Source (file / package path) | Gist (one line) | Disposition (CHANGE / NO-CHANGE / SPLIT / BLOCKED / DEFERRED) | Gate state |
|---|---|---|---|---|---|
| | | | | | |

## B. Per-ID sections (one per Correction ID or Intake ID with disposition CHANGE, NO-CHANGE, or BLOCKED)

### <ID> — <title>

- **Approved intent** (verbatim from package / entry): … [CLAIM: source path]
- **Must-become-true invariants** (verbatim): 1. … 2. …
- **Preservation constraints** (verbatim; also mirrored in §L): 1. …
- **Likely affected files** (from the brief) + **MANIFEST ← rows** for each: …
- **Propagation search** (D19):
  - Terms: `"<old wording>"`, `<retired term>`, `<role/gate/module/artifact name>`, `<cited filename>`, `<cited section title>` …
  - Scope: `01_CONSTITUTION 02_PIPELINE_AGENTS 03_BUILD_METHODOLOGY 04_REFERENCE_MANUALS 05_DESIGN_SYSTEM MANIFEST.md CHANGELOG.md` (+ `_SKILLS/`, `_OTHERS/` read-only for awareness)
  - Command shape: `grep -rn -i -E "<term>" <scope>`
  - Hit count: `<n>` (active) / `<n>` (history)

  | # | Path:line | Hit (quoted) | Disposition (CHANGE / CONSISTENT / HISTORY / OUT-OF-SCOPE) | Drives §C row / §F row / §J item | Label |
  |---|---|---|---|---|---|
  | | | | | | |

- **Touch-list rows implementing this ID:** §C #…
- **NO-CHANGE proposal** (if any): the intent is already true at `<path:line>`: "<quoted>" — valid only on Gate 2 approval.
- **CONFLICT / open questions** (→ §K): …

## C. Touch list (execute lightest ← first, heaviest last)

| # | Canonical doc (path) | ← count (MANIFEST) | Placement — VERIFIED against live structure (section heading / line anchor at BASE_SHA) | Proposed wording / exact edit intent (full text for new or replaced sentences; "delete L a–b" for removals; a precise intent line only for mechanical edits such as a rename). Mark each span **INTAKE-VERBATIM** or **ENGINEER-PROPOSED** — every heading, wrapper, transition, label, explanation, or normalization Claudy adds is written out and marked ENGINEER-PROPOSED for Tony to approve or strike (D15) | Contributing IDs | Version: live → new | Archive expected | Structural (rename / move / new)? | Minimal-form note (D14) |
|---|---|---|---|---|---|---|---|---|---|
| 1 | | | | | | | YES / NO (new) | NO | |

## D. New canonical files

| File (path) | Owning tier + why | Header (single-line) | MANIFEST row + Pairs-with | CHANGELOG row | IDs |
|---|---|---|---|---|---|
| | | | | | |

## E. Stale / superseded material

| Path | Action (archive-and-replace / mark historical / delete — deletion needs explicit Gate 2 approval) | Evidence it is stale | IDs |
|---|---|---|---|
| | | | |

## F. Dependents checked, unchanged

| Doc / location (path:line) | Kind (example / checklist / template / quick reference / role instruction / summary) | Why checked (which ID / term) | Verdict: CONSISTENT (quote) — or moved to §C # |
|---|---|---|---|
| | | | |

## G. Infra and index effects

| Item | Expected change | Check at Gate 4 / AC-I |
|---|---|---|
| MANIFEST rows | rows for §C/§D docs updated FROM headers; Date in MANIFEST header bumped; NOT archived (Ruling 7) | header vs row equality |
| MANIFEST live-doc count | `<unchanged — no canonical doc added/removed>` or recomputed from disk: `<n>` (this run adds/removes `<docs>`) | if changed: count = disk = rows; if unchanged: byte-equal to BASE |
| MANIFEST ← dependency map | recomputed for every doc whose Pairs-with this run changed; appendix scope note updated only if its scope changed | spot-check changed docs |
| CHANGELOG | one row per bumped / new doc in the exact ledger format, IDs in last column; header Date bumped; NOT archived | row count = bumped docs |
| README / index files | `<none>` or list | present |

**Pre-existing / baseline drift (D7)** — derived, index, or infra values already stale at BASE_SHA that the approved intake does NOT authorize repairing. Detected and recorded here; parked for a follow-up job; NOT on the touch list; left exactly as at BASE. If this run changes the underlying value anyway (e.g. adds a doc), the derived field moves to the table above and this row says it is cleared by that recompute. Drift alone never fails a TINY condition.

| ID (`DRIFT-…`) | Location (path:line at BASE_SHA) | Stale value vs disk truth (EVIDENCE) | Caused by this run? | Disposition (PARKED → follow-up / CLEARED by §G recompute / REPAIR authorized by `<intake ID>`) |
|---|---|---|---|---|
| | | | NO | PARKED |

## H. Paths, links, assets

| Reference (as written) | In doc | Resolves at BASE_SHA? | Resolves after? | Asset: canonical path `<tier>/_assets/…`, source vs rendered, replacement archived as `<name>_<date>.<ext>`? | IDs |
|---|---|---|---|---|---|
| | | | | | |

## I. Skill references (read-only awareness)

| Skill file (path) | What it cites that this run changes | Disposition (CONSISTENT / parked as §J item — never edited in this run, D21) |
|---|---|---|
| | | |

## J. Parked cross-boundary / cross-repo items

| ID (`XB-…`) | Target (repo / path) | Reason | Approved intent (verbatim) | Blocking this run? (YES → §K) |
|---|---|---|---|---|
| | | | | |

## K. Unresolved Operator decisions

Type **CONFLICT** = doctrine / authority conflict (incompatible governing requirements, or an approved request that cannot coexist with governing doctrine) → BLOCKED → Tony; counts against route condition A7. Type **CLARIFICATION** = a non-doctrinal mechanical detail that evidence could not settle (record what was checked) → the smallest question; not BLOCKED; does not affect the route (D17).

| ID | Type (CONFLICT / CLARIFICATION) | Question (exact; smallest necessary) | Evidence (incl. what was checked on disk first) | What it blocks / affects | Ruling (filled by Tony) |
|---|---|---|---|---|---|
| | | | | | |

## L. Preservation constraints (all IDs, consolidated)

| Constraint (verbatim) | Source ID | Where it lives (path:line at BASE_SHA) | How QA will check (AC-P) |
|---|---|---|---|
| | | | |

## M. Expected validation

- Lints: 4 lints; expected result on the candidate: zero new findings; baseline: `<count>` — `<path:line [LINT-ID]>` …
- Propagation searches to re-run at the candidate (verbatim from §B): …
- Canonical term list / retired-term list for AC-N (from the package or Tony): …
- Derived-field assertions: MANIFEST fields this run changes (§G) — count `<n>` / unchanged, rows `<n>`, ← map recomputed for `<docs>`; §G drift values byte-unchanged from BASE: `<DRIFT IDs / none>`
- Archive fidelity: `<n>` archives expected; each byte-equal to `git show <BASE_SHA>:<path>`
- References/assets to resolve (from §H): …

## N. Write-load tally and commit plan

- Docs edited `<n>` + archives `<n>` + new docs `<n>` + MANIFEST + CHANGELOG (+ assets `<n>`) = ~`<k>` writes
- Commits, in order: `docs(<DOC>): v<X.Y> - <summary> [<IDs>]` × `<n>`; then `chore(sync): handoff for CONTENT_SHA <short> [<run-id>]`
- Hygiene: plain hyphens; no Co-Authored-By; one version bump per doc per run (D22)

## O. Approval and amendments

- [ ] Gate 1 — scope + classification APPROVED by Operator at `<date/time>`
- [ ] Gate 2 — this map APPROVED by Operator at `<date/time>` (route `<TINY/LARGE>` confirmed; NO-CHANGE rows approved: `<IDs>`; TINY waiver line: "<verbatim>"; LARGE → TINY downgrade ruling, if any: "<verbatim>")
- [ ] Gate 3 — spec APPROVED at `<date/time>` (LARGE) / N/A (TINY, waiver)
- Amendments: `AMENDED-v1 — <date/time> — <what changed, why, which finding or discovery> — re-approved at Gate 2 [and Gate 3]` …
- Overrides logged (D-number, what, confirmation): …
- CONTENT_SHA (filled after the last content commit exists): `<sha>` · Gate 4 APPROVED at `<date/time>` · pushed at `<date/time>`

## P. Route evidence (TINY / LARGE decision record)

| Fast-path condition (route-selection.md) | Evidence | Holds? |
|---|---|---|
| ≤ 3 intake IDs | | |
| ≤ 3 canonical touch-list docs (after §B search) | | |
| no new canonical document | | |
| no Factory-wide terminology rename / change | | |
| no cross-correction dependency | | |
| no high-risk governing-rule change (security / authority / payment / tenant / PHI / git-merge governance / QA verdict authority) | | |
| no unresolved conflict (no unruled §K CONFLICT row; CLARIFICATION rows and §G baseline drift do not count) | | |
| no cross-boundary change required for success (§J blocking = none) | | |
| propagation search bounded and complete before Gate 2 | | |
| docs-only QA waiver eligible (changes confined to live-scope markdown + indexes; Tony has not disallowed) | | |
| **Route** | TINY only if ALL hold; else LARGE | **`<TINY/LARGE>`** — Operator escalation / downgrade ruling: `<none / verbatim>` |
