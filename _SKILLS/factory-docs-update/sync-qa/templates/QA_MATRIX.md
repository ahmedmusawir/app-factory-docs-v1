# QA_MATRIX — <run slug> — <YYYY-MM-DD>

> Cody's evidence matrix and findings log for a LARGE synchronization run. One row per AC of the frozen `DOCSET_SYNC_ACCEPTANCE_SPEC.md`. Every Result is backed by pasted command output or a path:line read (EVIDENCE); a CLAIM from the handoff is never a Result. Lives at `_AUDIT/SYNC_<YYYY-MM-DD>_<slug>/QA_MATRIX.md`. Written only by the QA executor; never by the Engineer.

## 0. Header

| Field | Value |
|---|---|
| Run ID | `SYNC_<YYYY-MM-DD>_<slug>` |
| Branch | `docs/sync-<slug>-<YYYY-MM-DD>` |
| BASE_SHA | `<sha>` (from map §0) |
| CONTENT_SHA (from handoff) | `<sha>` |
| **QA_START_SHA** (recorded by Cody from `git rev-parse origin/<branch>`) | `<sha>` at `<date/time>` |
| Preconditions | ancestry `<PASS/BLOCKED>` · post-CONTENT diff only audit artifacts `<PASS/BLOCKED: paths>` · map APPROVED `<yes>` · spec APPROVED `<yes>` · lints execute `<yes>` |
| Spec version | APPROVED (Gate 3 `<date/time>`) [+ AMENDED-v<n>] |
| Lint baseline (from map §M) | `<count>`: `<path:line [LINT-ID]>` … |

## 1. Cycle log

| Cycle | Tip SHA (QA_START_SHA / QA_RETEST_SHA) | REPAIR_CONTENT_SHA (from handoff §7) | Started | ACs verified | Outcome |
|---|---|---|---|---|---|
| 1 | | — | | all | |
| 2 | | | | failed ACs + AC-S, AC-L, AC-H (+ AC-A) | |

## 2. Acceptance traceability matrix (cycle 1; later cycles append columns or rows as needed)

| AC | Family | Check (exact) | Method (command / diff / grep / read) | SHA | Result (PASS / FAIL / BLOCKED / N/A) | Evidence (pasted output or path:line) | Finding |
|---|---|---|---|---|---|---|---|
| AC1 | AC-T | | | | Pending | | |
| AC2 | AC-S | | | | Pending | | |
| … | | | | | | | |

## 3. Propagation re-run record (AC-C)

| ID | Term | Scope | Command (verbatim) | Hits at SHA | Reconciled against map §B? (every hit matches a disposition row) | Undispositioned / mismatched hits |
|---|---|---|---|---|---|---|
| | | | | | | |

## 4. Findings log

### QA-F<nn> — <title>
- **AC:** `AC<n>` (`<family>`) · **Intake ID:** `<CP-/IN-…>` · **Map row:** `§C#<n>`
- **Severity:** Critical / High / Medium / Low · **Classification:** Acceptance Failure / Regression / Pre-Existing / Follow-Up Finding / Observation
- **Location:** `<path:line>` at `<SHA>`
- **Expected:** `<from the AC / map row>`
- **Actual:** `<quoted>`
- **Evidence:** `<command + output, or read>`
- **Scope impact:** in-scope / outside approved scope (→ future intake)
- **Gate impact:** blocking / non-blocking
- **Retest requirement:** `<AC(s) + mandatory families>`
- **Routing (Sol fills):** → Claudy (bounded repair) / → Tony (decision) / → recorded (pre-existing / follow-up) · **Status:** OPEN / REPAIRED (cycle n) / CLOSED / ROUTED

## 5. Exploratory probe (bounded)

| Seam probed | Location | Observation | Classification |
|---|---|---|---|
| | | | |

## 6. Recommendation to Sol (per cycle)

- Cycle `<n>` at `<SHA>`: **`<PASS / PASS WITH FOLLOW-UP FINDINGS / PASS WITH KNOWN RISK / FAIL / BLOCKED>`** — open findings: `<IDs>`; follow-up findings: `<IDs>`; blocked on: `<decision>`.
