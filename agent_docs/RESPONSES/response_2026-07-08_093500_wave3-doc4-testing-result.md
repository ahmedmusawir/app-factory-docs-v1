# ✅ WAVE 3 — DOC 4 COMPLETE: TESTING_PLAYBOOK → v2.1

**File:** `3_METHOD-TESTING_PLAYBOOK.md` (the 75KB model doc — minimally touched)

## CHANGES MADE

| # | Change | Finding |
|---|--------|---------|
| 1 | Standard header (v2.1 · 2026-07-08 · Tier 3 · Pairs-with); provenance lines kept | F-018 |
| 2 | **"Where This Doc Sits"** section added after the header — outbound: STARTER_KIT_HANDBOOK (runner/config ground truth) + RECON_QUESTIONNAIRE (Q1.7 verify-the-runner); inbound executors named: SFP Phase 8, FFM verification/, FRONTEND_BUILD_PHASE §9 | F-035 |
| 3 | **§3.8 "Run-verification rituals"** added to Part 3 (+ ToC entry): L17 grep-at-close, L25 clear-derived-caches, L26 fresh-baseline — canonical doctrine home, written at PRINCIPLE level with a tie to Principle 1.3 | F-035 enrichment |
| 4 | Tail "END OF TESTING PLAYBOOK v2.0 DRAFT" → clean END line + **Version History table** (1.0 / 2.0 / 2.1 rows, ascending) | F-036, D-018 |

## GUARD 3 — SINGLE-SOURCE VERIFICATION

- §3.8 is **principle-level prose**, not a copy: distinctive-phrase check confirms zero verbatim overlap with RECON §12's executable Q12.x text ("Turbopack prints", "SP-close", "whack-a-mole" all absent here).
- Scope split honored: L17/L25/L26 (testing doctrine) absorbed here; **L28 (process-status) + L29 (seam-check) deliberately left in RECON §12** — they are recon/run-time checks, not test doctrine.
- RECON §12's pointer-back ("canonical home: TESTING §3.8") is a **queued later touch** — RECON is not in this wave's editable five.

## GATES

DRAFT live **0** (2 history-row mentions) · stitch **0** · `_v[0-9]` **0** · C1 **0** · header ✓ · §3.8 + ToC ✓ · history table ✓

## THINGS I DIDN'T TOUCH

All ten principles, Parts 2/4/5/6, the Quick Reference Card, every appendix — the audit's cleanest-content doc stays untouched beyond the four additions above.

## CONCERNS

1. **Queued:** RECON §12 pointer-back to §3.8 (next RECON touch); FFM `verification/` authoring guide could name TESTING_PLAYBOOK explicitly (FFM §13 was outside this wave's approved FFM scope).
2. Part 4.6 (regulated environments) remains a stub — pre-existing, correctly labeled as such, untouched.

## Suggested commit

wave3(testing): v2.1 — end the isolation, DRAFT resolved, rituals home, F-035/F-036
