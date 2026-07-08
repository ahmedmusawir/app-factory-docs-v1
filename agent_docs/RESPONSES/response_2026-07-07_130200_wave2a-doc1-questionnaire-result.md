# ✅ WAVE 2A — DOC 1 COMPLETE: ARCHITECT_QUESTIONNAIRE → v2.2

**File:** `2_AGENTS-ARCHITECT_QUESTIONNAIRE_v2_1.md` (filename unchanged per wave rules; full rewrite — merge + CRLF→LF normalization, both approved)

## CHANGES MADE

| # | Change | Finding |
|---|--------|---------|
| 1 | Standard header (v2.2 · 2026-07-07 · Active · Tier 2) + explicit SINGLE SOURCE declaration pointing at ARCHITECT_PLAYBOOK §3/§5 | F-018, F-017 |
| 2 | Recon-precedes-ignition note in preamble (one line, ties to Phase 0) | F-024 support |
| 3 | Q2 enriched: technical level + environment sub-bullets (absorbed playbook Q2 detail) | F-017 |
| 4 | Q4 de-Stitched → "screenshot, style tile, or Figma link" + absorbed "None → STOP" rule from playbook Q15 | F-002 |
| 5 | Q10 enriched: per-layer spec when exotic (absorbed playbook Q6 blanks) | F-017 |
| 6 | **New Phase 4 — Constraints Deep-Dive (OPTIONAL per guardrail):** Q13 App Type (feeds §4 router) · Q14 Tech Constraints & Deadline · Q15 Integrations · Q16 Security/Compliance · Q17 Risks & Unknowns. Explicit "12 questions do the work of 40; Phase 4 is never mandatory" framing + 📥 routing rule: unresolved answers land in Planning State as ❓/⚠️ | F-017 |
| 7 | 7 playbook duplicates DROPPED per approved map (what-building, problem, done-looks-like, must-haves, out-of-scope, anchor checklist) | F-017 |
| 8 | APP_BRIEF template: +Deployment Class line (§4), +Technical Level/Environment (§3), +§9 Integrations, +§10 Constraints & Deadline, +§11 Risks & Unknowns (with Planning State cross-rule); Planning State stays §8 (stable cited ID); Handoff Checklist → §12 | F-017 |
| 9 | "✅ Changes Applied — GPT Recommendation" table retired into a real Version History (as the v2.1 row); chat-residue closing line removed (logged in history) | F-018/D-018 |
| 10 | ⛔ Hard Gate, 📌 Reality Rule, Planning State — PRESERVED UNTOUCHED | crown jewels |

## VERIFICATION GATES

| Gate | Result |
|---|---|
| stitch (live doctrine) | **0** (1 hit = v2.2 history row, exempt) |
| `_v[0-9]` | **0** |
| `â` / C1 control chars | **0** / **0** |
| Line endings | LF-only (CR count: 0) |
| Hard Gate / Reality Rule / Planning State | present ✓ |
| Standard header + Version History | ✓ |

## THINGS I DIDN'T TOUCH

- Phase 1–3 question wording beyond the approved enrichments; Phase 2 entirely untouched.
- ARCHITECT_PLAYBOOK — next doc, after your commit.

## CONCERNS

- Template section count grew 9 → 12; the brief's 200–300-line expectation (HANDOFF_PACKAGE_PLAYBOOK §5.1) still holds since Phase 4 sections may be "None for v1" one-liners.

## Suggested commit

wave2a(questionnaire): v2.2 — F-017 single-source merge, de-Stitch, header
