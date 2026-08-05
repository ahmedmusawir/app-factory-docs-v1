# route-selection.md — Phase 3 Routing Decision Tree

> This tree produces the RECOMMENDATION only. The DECISION is the Operator's — always
> present both routes with estimates and wait (CLAUDE.md D3, SKILL.md Stop Gate 3).
> **Standing operator ruling (2026-08-05): LOCAL GIT IS PRIMARY.** The tree below mostly
> exists to detect the rare, genuine exception — not to give the MCP equal billing.

```
START: approved ripple map in hand
│
├─ Q1. Any rename, move, folder restructure, or new docs entering the Hub?
│      YES → RECOMMEND LOCAL GIT, no exception discussion. → PRESENT.
│      NO  → Q2
│
├─ Q2. Is this session at a Hub clone (or is one obtainable in ~a minute)?
│      YES → RECOMMEND LOCAL GIT (the standing primary; flat cost,
│             native verification, zero API risk). → PRESENT.
│      NO  → Q3
│
├─ Q3. Is the job 1–2 docs, content-only, genuinely trivial?
│      YES → the MCP is VIABLE from here — present it honestly as the
│             exception, with call-count estimate. Still note what a
│             clone session would cost (usually: one git clone).
│      NO  → RECOMMEND LOCAL GIT + obtaining a clone session; state
│             plainly that the MCP route for this shape risks the
│             day-long-failure pattern. → PRESENT.
│
└─ PRESENT: both routes + honest estimates + the recommendation + "Your call, boss."
   ⛔ WAIT for the Operator's explicit choice. Log it. Proceed on HIS route.
```

## Estimate lines to fill in when presenting

- Route A (local): `1 branch, [N] commits, ~[2+N] min` (+ note if a clone must be obtained).
- Route B (MCP): `~[calls] API calls ≈ [minutes] min` where calls ≈ files×3 + renames×2 + 2.

## Tie-breakers and edge cases

- **Operator picks against the recommendation:** that is the system working. Log it,
  execute his route, apply the D4 checkpoint as usual.
- **Job grows mid-flight** (ripple map amendment adds docs): re-run this tree from Q1
  and re-present. A route chosen for 2 docs does not silently cover 6.
- **MCP unavailable/unauthenticated:** irrelevant on the primary route — note it as a
  GAP and proceed locally. It only blocks the exception path.
- **Uncertain job shape** (can't size the edits yet): the sizing gap goes in the
  presentation as a QUESTION; do not present made-up estimates.
