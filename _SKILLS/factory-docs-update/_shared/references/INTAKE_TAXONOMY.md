# INTAKE_TAXONOMY.md — The Eleven Intake Classes, IDs, and Routing (D16)

> Shared reference. Claudy applies it at Phase 1 to every cargo unit in `_INBOX/`; Cody uses it to verify that every ledger row carries a lawful class and a final disposition (AC-T). A unit that fits no class, or fits two, is BLOCKED — a QUESTION at Gate 1 — never a guess.

## Cargo units

A **cargo unit** is one file, or one folder treated as a whole, in `_INBOX/` (legacy fallback: the repo root for `DOCTRINE_PROMOTION*`, `*PATCH*`, `LESSONS*`). A correction package arrives as a folder tree and is ONE unit at the package level; each correction inside it is one ledger ROW. Recognition is by discovery (file names, headers, content shape, a Hub-counterpart match by canonical name first and content similarity second), never by asking Tony what a file is.

## IDs

| Source | ID form | Rule |
|---|---|---|
| Correction inside an approved package | The package's own Correction ID (e.g. `CP-07`, or whatever Part 1 minted) | Retained verbatim; never re-minted |
| Any other cargo unit or entry | `IN-<run>-<NN>` (e.g. `IN-2026-09-21-03`) | Minted at intake, sequential, never reused |
| Parked cross-boundary item discovered mid-run | `XB-<run>-<NN>` | Minted when parked; carries target + reason |
| Gap (a cited doc the Hub lacks) | `GAP-<run>-<NN>` | Minted at the gate where found |
| QA finding | `QA-F<nn>` | Minted by Cody; cites the AC and the intake ID |

The ID is the join key. It must appear on: the ledger row · every map row it drives · the changed doc's Version History row · the commit message `[<IDs>]` · the CHANGELOG row's last column · the handoff disposition table · QA matrix rows and findings · the Gate Q report · the final stamp on the cargo (ENCODED / NO-CHANGE / SPLIT / DEFERRED).

## The classes

| # | Class | Recognition (evidence) | Routing |
|---|---|---|---|
| 1 | **APPROVED CORRECTION PACKAGE** | A master index + bounded domain briefs; each brief carries confirmed problem, source evidence / finding IDs, approved correction intent, invariants that must become true, behavior to preserve, likely affected domains/files, constraints; the index shows APPROVED status | One ledger row per correction, keyed by its Correction ID. Map §B section per ID with intent, invariants, preservation verbatim. Propagation search mandatory (D19). A brief missing a required field → that ID is BLOCKED, not the package. Claudy never adjudicates the correction (D17). |
| 2 | **DOCTRINE JOURNAL / LESSON** | `DOCTRINE_PROMOTION*`, `*PATCH*`, `LESSONS*`, `*JOURNAL*`; entries with target doc + placement + content, or FLAGGED lesson entries | One row per entry (`IN-…`). Edit-level entries: verify placement against live structure, land content exactly, translate mechanics (D15). Intent-level entries: draft proposed wording in the map like a correction. Propagation search for any entry that changes a rule. |
| 3 | **NEW CANONICAL DOCUMENT** | No Hub counterpart by canonical name or by content similarity; intended as live doctrine | Tier placement from the doc's own subject and header claims; if the owning tier is ambiguous → BLOCKED (Ruling 10). Standard single-line header, MANIFEST row + Pairs-with, CHANGELOG row, ← map recompute. Never `_OTHERS/` for canonical doctrine. Always forces LARGE. |
| 4 | **UPDATE / SUPERSEDING CANONICAL DOCUMENT** | A Hub counterpart exists; the cargo is a full replacement (or a large partial rewrite delivered as a whole file) | Archive the live copy (stamped from its header), replace under the canonical filename, version forward FROM the live header (cargo's version claim verified, never trusted), MANIFEST, CHANGELOG. Diff the two and treat every removed rule as a propagation search term (D19). |
| 5 | **PROCESS DOCUMENT** | Describes how the Factory works (a gate procedure, a runbook, a lifecycle) and is intended as doctrine | It is a canonical document in the tier that OWNS the process (e.g. build methodology → `03_BUILD_METHODOLOGY/`). Ambiguous ownership → BLOCKED → Tony. Then class 3 or 4 mechanics. Supporting process EVIDENCE (a run record, a report) is class 7, not this class. |
| 6 | **DIAGRAM / IMAGE** | A binary or SVG file, or a doc that embeds one via `![…](…)` / `<img src>` | Canonical asset location `<OWNING_TIER>/_assets/<canonical-name>.<ext>` (Ruling 9). Map §H records: referencing doc(s), relative path, case-exact resolution, source-vs-rendered pairing (source file rides beside the render with the same stem; only the render is referenced from doctrine). Replacement of an existing asset: outgoing file copied to `_ARCHIVE/<name>_<YYYY-MM-DD>.<ext>` (date, not version — assets have no header). No orphan canonical asset may exist after the run. No MANIFEST row for assets; the referencing doc's row and CHANGELOG line carry the change. |
| 7 | **SUPPORTING / NONCANONICAL ASSET** | Reference material, run records, reports, examples, finalization reports; not intended as live doctrine | `_AUDIT/` (run and campaign records, incl. the durable run folder) or `_OTHERS/` (design notes, master lists). No header law, no MANIFEST row, no CHANGELOG row; recorded in the ledger with its landing path. |
| 8 | **ARCHIVE / HISTORICAL MATERIAL** | Explicitly marked historical, or a superseded version arriving late, or a versioned snapshot | `_ARCHIVE/` ONLY if it is a versioned snapshot of a live doc whose version suffix can be read from its own header; otherwise `_AUDIT/`. Never a live tier. Never edited. |
| 9 | **CROSS-BOUNDARY / CROSS-REPO ITEM** | Targets another repository, another `_SKILLS/*` folder, `lints/`, `.github/`, or Hub governance | Parked with `XB-…` ID: target, reason, approved intent (verbatim), blocking / non-blocking for this run. Read-only during the sync (D21). Blocking → BLOCKED → Tony. Restated at close-out and in RECOVERY.md. |
| 10 | **NO CANONICAL CHANGE REQUIRED** | Evidence shows the approved intent is already true in the live corpus (path:line), or the item is informational | A NO-CHANGE **proposal** in the map with the evidence; valid only when Tony approves the row at Gate 2 (D17). Cargo still gets its final stamp `NO-CHANGE (approved Gate 2, <date>)`. |
| 11 | **BLOCKED / NEEDS OPERATOR DECISION** | Unclassifiable unit; ambiguous counterpart match; conflicting corrections; a cited doc the Hub lacks with no doc riding in; a placement that does not exist; an invariant that cannot hold without breaking a preservation constraint; ambiguous tier ownership | A BLOCKED row with the exact question, the evidence, and what it blocks. Presented at the nearest gate. Never guessed, never silently resolved. Tony may consult Jarvis for architecture / preservation / semantic adjudication (D17) — Claudy does not. |

## Dispositions (the vocabulary on every ledger row)

`CHANGE` (drives touch-list rows) · `NO-CHANGE` (proposal → approved) · `SPLIT` (parked cross-boundary, target named) · `BLOCKED` (Tony decision pending) · `DEFERRED` (Tony ruling: not this run, reason and date) · after merge: `ENCODED (PR #n)`.

Per-hit dispositions inside a propagation search are a different vocabulary and live in map §B: `CHANGE` · `CONSISTENT` · `HISTORY` · `OUT-OF-SCOPE`.

## What the taxonomy is NOT

It is not permission to invent content. A class tells you the mechanics that apply; the WORDS that land come only from approved cargo (edit-level) or from the UPDATE MAP rows Tony approved (intent-level). It is not a substitute for the propagation search: classes 1, 2, 4, and 5 always trigger D19.
