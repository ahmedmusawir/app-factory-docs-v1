# ✅ WAVE 2A — DOC 2 COMPLETE: ARCHITECT_PLAYBOOK → v2.2

**File:** `2_AGENTS-ARCHITECT_PLAYBOOK_v2_1.md` (filename unchanged; F-016 filename/version mismatch resolves at Wave 6 rename)

## CHANGES MADE

| # | Change | Finding |
|---|--------|---------|
| 1 | Standard header (v2.2 · 2026-07-07 · Active · Tier 2 · Pairs-with); "AI App Factory" → "App Factory" (blockquote, footer, Example A hero statement) | F-018, F-008 |
| 2 | §1 pipeline diagram redrawn to the Designer v2.0 model — token file (primary) + HTML/PNG artifacts + UI_SPEC + Manifest; pattern copied verbatim from DESIGNER_PLAYBOOK §1 | F-002 |
| 3 | §2 de-Stitched: inputs table ("Stitch output" → "style tile") + No-Vibe-Design step 2 ("Google Stitch" → "Designer style tile, token-driven HTML") | F-002 |
| 4 | §2 gains "Instrument + law" callout: stark-recon executes RECON_QUESTIONNAIRE (single source); recon = Blueprint Phase 0 + FFM Stage 0 | F-024 |
| 5 | **§3 shrunk to relocation pointer** (heading kept for ToC anchors): what the single source provides (Phases 1–4 summary) + "Why This Split" citing F-017, the FRONTEND_FIRST §14 pattern, and the Doctrine Pairing Principle (SFP §1.5). The embedded 15-Q instrument (incl. its Stitch checkbox) is gone | F-017, F-002 |
| 6 | **§5 shrunk to relocation pointer**: canonical APP_BRIEF template lives in ARCHITECT_QUESTIONNAIRE (with Planning State + Phase-4 sections); the embedded ~190-line template (incl. its Stitch Appendix A) is gone. §6 type-specific emphasis + §7 approval flow stay — additive, not duplicated | F-017, F-002 |
| 7 | §8 handoff package de-Stitched ("screenshot/style tile/sketch") | F-002 |
| 8 | Footer version block → Version History table (2.2 / 2.1 / 2.0 rows; v2.1 prose preserved verbatim as its row) | F-016, F-018, D-018 |

Technique note: §3/§5 replaced via byte-safe splice (UTF-8, no BOM) — the old embedded template used markdown hard-break trailing spaces that defeat exact-match editing.

## VERIFICATION GATES

| Gate | Result |
|---|---|
| stitch (live doctrine) | **0** (1 hit = v2.2 history row, exempt) |
| `_v[0-9]` | **0** |
| `â` / C1 control chars / BOM | **0** / **0** / none |
| §3/§5 are pointers, not duplicated content | ✓ (~5KB duplicate removed; 28.9KB → 23.8KB) |
| ToC anchors | intact (headings unchanged) |
| Standard header + Version History | ✓ |

## THINGS I DIDN'T TOUCH

- §4 App Type Router, §6 Type-Specific Considerations, §7 Approval Criteria, §9 Anti-Patterns, §10 worked examples (content), Summary/checklist — all as-is.
- Recon Mode §2 doctrine text — only the pointer callout added.

## CONCERNS

- Example A pins "Next.js 14" — stale-pin class (F-038 family), but that finding is scoped to the manuals in Wave 4; left as-is, flagging here.
- §10 examples still show the pre-recon workflow implicitly (no Recon Report line in their flows) — cosmetic; the checklist Step 0 covers the doctrine.

## Suggested commit

wave2a(architect-playbook): v2.2 — §3/§5 to pointers, diagram fix, recon pointer, F-002/F-016/F-017/F-024
