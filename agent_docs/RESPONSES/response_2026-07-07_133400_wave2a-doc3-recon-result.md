# ✅ WAVE 2A — DOC 3 COMPLETE: RECON_QUESTIONNAIRE → v0.5

**File:** `2_AGENTS-RECON_QUESTIONNAIRE.md`

## CHANGES MADE

| # | Change | Finding |
|---|--------|---------|
| 1 | Standard header (v0.5 · 2026-07-07 · Active, living-document note kept · Tier 2). "Where this sits" line: recon = **Blueprint lifecycle Phase 0** + **FFM Stage 0**; ARCHITECT_PLAYBOOK §2 = the law; `stark-recon` skill automates it; **this doc = the skill's source content** | F-018, F-024 |
| 2 | §7 + §10 restored as **tombstone stubs** with the stable-ID rule stated: numbers are IDs, not positions; retired numbers never reused; new sections append. Battle-cited Q-numbers (Q3.4, Q8.x, Q9.1) stay valid — no renumbering (approved Flag 3) | F-023 |
| 3 | §13 Open-Ended Sweep questions relabeled Q10.1–Q10.4 → **Q13.1–Q13.4** | F-023 |
| 4 | Recon Report Format: "Section 10 — Surprises" → "Section 13 — Surprises" | F-023 |
| 5 | **Q3.4 nuance box** (F-042 resolution, cites RECON_WAVE0 Q1): kit is TABLE-BASED (`user_roles` = truth, `get-user-role.ts` canonical). Live smell = (a) authz READ from `user_metadata` or (b) client-writable role write path. Metadata = creation-time transport ONLY, via protected channel (admin API / `app_metadata`). Grep unchanged | F-042 |
| 6 | Version History: v0.5 row appended in the table's ascending order; "Owner: … AI App Factory" → "App Factory" | D-018, F-008 |

## VERIFICATION GATES

| Gate | Result |
|---|---|
| stitch | **0 anywhere** |
| `_v[0-9]` | **0** |
| `â` / C1 control chars | **0** / **0** |
| Section sequence | 0–13 contiguous, §7/§10 marked retired ✓ |
| Q-number stability | Q3.4 / Q8.x / Q9.1 untouched ✓; live Q10.x = 0 (history rows only) |
| Standard header + v0.5 row | ✓ |

## THINGS I DIDN'T TOUCH

- Every content section (0–6, 8, 9, 11, 12), the conflict table, the Lessons Backlog, all bash — **scars preserved, zero editorializing** (REVIEW_006 rule 3).
- The v0.1–v0.4 history rows verbatim.

## CONCERNS

- The stark-recon skill (repo-side, `_SKILLS/stark-recon/`) should be re-synced against this v0.5 — especially the Q13.x relabel and the Q3.4 nuance. That's outside this doctrine repo (F-021 scope decision); flagging for the skill's own maintenance track.
- Recon Report Format has no entries for §0, §11, §12 — pre-existing shape, arguably intentional (those are operator/authoring checks, not report sections). Left as-is.

## Suggested commit

wave2a(recon): v0.5 — renumber, cross-links, Q3.4 nuance, F-023/F-024
