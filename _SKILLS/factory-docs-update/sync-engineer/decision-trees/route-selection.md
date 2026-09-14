# route-selection.md — TINY / LARGE Path Routing (evidence-driven) + Execution-Route Exception

> Two decisions live here. **Decision A** — which PATH (TINY fast path or LARGE with the independent QA lane) — is made by the skill from evidence, provisionally at the end of Phase 1 and finally at the end of Phase 2, and recorded in UPDATE MAP §P for Tony's approval at Gate 2. **Decision B** — which EXECUTION ROUTE (local git at a Hub clone, or the GitHub MCP exception) — is fixed by the standing ruling unless no clone exists, in which case the Operator chooses. Neither decision starts by asking Tony "small or large?" (family CLAUDE.md D3).

## Decision A — the path

**TINY is allowed only when ALL of the following hold, each with evidence in §P.** Any single failure → LARGE. Any condition that cannot be evaluated from disk and intake → ask Tony the smallest blocking question (one question, the specific condition), not "which path?".

```
START: ledger drafted (Phase 1) / UPDATE MAP drafted (Phase 2)
│
├─ A1. Intake IDs in scope ≤ 3?                                  (count §A rows with CHANGE/NO-CHANGE)
│      NO → LARGE
├─ A2. Canonical touch-list docs ≤ 3?                            (count §C distinct docs — final only after the §B search;
│      NO → LARGE                                                  at Phase 1 use the briefs' likely-files as provisional)
├─ A3. No NEW CANONICAL DOCUMENT (class 3 or 5-as-new)?          (§D empty)
│      NO → LARGE
├─ A4. No Factory-wide terminology rename / change?              (no role, gate, module, lifecycle, or artifact name changes;
│      NO → LARGE                                                  no retired-term introduction)
├─ A5. No cross-correction dependency?                           (no §B item's invariant depends on or collides with another's)
│      NO → LARGE
├─ A6. No high-risk governing-rule change?                       (auth / RBAC / tenant isolation / PHI / payments /
│      NO → LARGE                                                  subscriptions / QA verdict authority / merge & git
│                                                                  governance / role authority chains; judged from the
│                                                                  intent text and the target docs' subjects)
├─ A7. No unresolved conflict?                                    (§K empty, or every §K row ruled by Tony)
│      NO → LARGE (or BLOCKED until ruled)
├─ A8. No cross-boundary change required for success?            (§J has no BLOCKING item)
│      NO → BLOCKED → Tony (then LARGE if it proceeds)
├─ A9. Propagation search bounded and complete before Gate 2?    (every §B term searched over the full live scope; every hit
│      NO → LARGE                                                  dispositioned; hit volume small enough to present aloud)
├─ A10. Docs-only QA waiver eligible?                            (all changes are live-scope markdown + MANIFEST/CHANGELOG/
│      NO → LARGE                                                  _ARCHIVE; no assets, lints, CI, skills; Tony has not
│                                                                  disallowed waivers for this campaign)
│
└─ ALL YES → TINY. Write the waiver line in §0/§O for Gate 2. Otherwise → LARGE.
```

**Provisional vs final.** At Phase 1, A1, A3, A4 (from intent text), A5, A6, A8 are usually decidable; A2, A7, A9, A10 are confirmed after the Phase 2 search. Say which are provisional. If the final route differs from the provisional, announce it at Gate 2 with the condition that flipped.

**Operator overrides.** Tony may escalate TINY → LARGE at any time, for any reason; record "Operator escalation" in §P. A downgrade LARGE → TINY requires an explicit Operator ruling recorded verbatim in §O and §P together with the waiver line; the skill never proposes a downgrade for convenience and never silently applies one (CLAUDE.md §6 second example).

**What TINY changes and does not change.** TINY skips Phase 3 (spec), Phase 6 (Cody), and Phase 7 (Gate Q). It does NOT skip the ledger, the search, the map, Gate 2, the per-doc checklist, the CONTENT_SHA record, Gate 4, or the sweep. Claudy runs the mechanical standing-invariant checks himself at Gate 4 (AC-S, AC-A, AC-I, AC-L, AC-H + the §B re-run) and presents the output as evidence under the recorded waiver.

## Decision B — the execution route

```
START: approved UPDATE MAP in hand
│
├─ B1. Is this session at a Hub clone?
│      YES → Route line in §0: "Local git at Hub clone (standing ruling 2026-08-05)". No ceremony. → DONE.
│      NO  → B2
├─ B2. Is a clone obtainable in about a minute?
│      YES → Say so; recommend obtaining it; route line as B1 once at the clone. → DONE.
│      NO  → B3
└─ B3. Is the job 1–2 docs, content-only, no rename / move / new doc / asset, and genuinely trivial?
       YES → the MCP is VIABLE: present BOTH routes with honest estimates
             (local: minutes ≈ 2 + docs; MCP: calls ≈ files×3 + renames×2 + 2, minutes ≈ calls × 1–2)
             and WAIT for the Operator's explicit choice. Log it in §0. Apply D4 and D8 on the MCP.
       NO  → recommend local git + obtaining a clone; state plainly that the MCP for this shape risks the
             day-long-failure pattern (AP-1). WAIT for the Operator's word.
```

Tie-breakers: the Operator picking against the recommendation is the system working — log it and apply D4. A job that grows mid-flight re-runs Decision A from A1 (a route chosen for 2 docs does not silently cover 6) and, on the MCP, re-runs Decision B. Uncertain job shape → a QUESTION in the presentation, never invented estimates.
