# Phase 3 — Route Decision (Gate 3, Operator-owned)

> **Run:** factory-module-doctrine · **Date:** 2026-08-10 · **Status:** PENDING — awaiting Operator's route choice

**Decision-tree exit:** Q1 = YES (two new docs entering the Hub: BIM_PLAYBOOK, FEAT_PLAYBOOK) → RECOMMEND LOCAL GIT, no exception discussion (route-selection.md; TOOL_ROUTING rule 3).

**The job:** 4 docs edited (QA twice), 2 new docs, 0 renames, ~12 total file writes (3 archive copies + MANIFEST + CHANGELOG included), 6 doc commits.

**Route A — Local git (PRIMARY):** one branch `docs/factory-module-doctrine-2026-08-10` off current main, 6 commits, one push. Estimate: ~15–20 minutes (the BUG_FIX seamless merge and QA supersession are the careful parts; mechanics are minutes).

**Route B — GitHub MCP (exception):** ~35 API calls ((11 file-touches × 3) + 2 overhead) with SHA fetch-and-verify on every existing-path write ≈ 35–70 minutes. The new-doc set alone disqualifies it per the standing ruling.

**Recommendation:** Local git, per your standing ruling (2026-08-05). No exception conditions hold — we are AT the clone, the job is bulk-shaped.

**Your call, boss.**
