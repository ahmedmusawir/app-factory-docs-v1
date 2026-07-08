# 📋 WAVE 2A PLAN — Agent Tier Sync (4 docs) + F-017 MERGE MAP

> Status at write time: PENDING_APPROVAL · Session: 2026-07-07 · Mirrors CLI presentation.

## Required reading completed

1. FINDINGS_LOG — F-002, F-011, F-012, F-016, F-017, F-018, F-023, F-024, F-025 ✓ (+ F-042 resolution for the Q3.4 nuance)
2. REVIEW_005 (Questionnaire), REVIEW_004 (Architect Playbook), REVIEW_006 (Recon), REVIEW_007 (Designer) ✓
3. FRONTEND_FIRST §14 — the validated relocation template (READ ONLY) ✓
4. Full reads of all four target docs ✓

## Pre-plan encoding findings

- ARCHITECT_QUESTIONNAIRE: the 129 flagged chars are **CRLF line endings** (U+000D), not corruption. Other 3 docs are LF. → Proposal: normalize Questionnaire to LF during the merge rewrite (FLAG 1 — whole-file diff noise).
- Zero mojibake, zero true C1 corruption in all four docs.

---

## THE F-017 MERGE MAP (Doc 1 — needs explicit approval)

Standalone = ARCHITECT_QUESTIONNAIRE v2.1 (12-Q / 3-phase). Playbook = ARCHITECT_PLAYBOOK §3 (15-Q / 6-phase).

### Standalone questions — ALL KEEP (with two enrichments)

| Std Q | Content | Disposition |
|---|---|---|
| Q1 | Hero Action (<10s sentence) | KEEP |
| Q2 | Primary User + Roles (single/multiplayer) | KEEP + ENRICH with playbook Q2's tech-level + environment sub-bullets |
| Q3 | Brain Check (AI vs CRUD) | KEEP |
| Q4 | Visual Anchor | KEEP + DE-STITCH → "screenshot, style tile, or Figma link" (F-002) |
| Q5 | Out-of-Scope Lock (min 5) + ⛔ HARD GATE | KEEP UNTOUCHED (crown jewel) |
| Q6–Q9 | Data Reality (Core Objects / Inputs / Persistence / Output) + 📌 REALITY RULE | KEEP UNTOUCHED (crown jewel) |
| Q10 | Tech Stack (Factory Standard or exotic) | KEEP + ENRICH: "if exotic, specify per layer (frontend/backend/DB/auth/hosting/AI)" (absorbs playbook Q6's blanks) |
| Q11 | Success Demo (3 steps) | KEEP |
| Q12 | Failure Modes (top 3) | KEEP |

### Playbook §3 questions — dispositions

| Pbk Q | Content | Disposition | Rationale |
|---|---|---|---|
| Q1 | What are we building (one sentence) | DROP-DUPLICATE | ≈ Std Q1 Hero Action (sharper form) |
| Q2 | Primary user (role / tech level / environment) | ABSORB-DETAIL into Std Q2 | Tech level + environment are unique and drive UX decisions |
| Q3 | What problem does this solve | DROP-DUPLICATE | Covered by APP_BRIEF §1 Mission Statement |
| Q4 | What does "done" look like | DROP-DUPLICATE | ≈ Std Q11 Success Demo (stricter 3-step form) |
| Q5 | App type (Full-Stack / Backend / Local-First) | **ABSORB → new Q13** | Feeds ARCHITECT_PLAYBOOK §4 App Type Router; no standalone equivalent |
| Q6 | Stack predetermined (per-layer blanks) | ABSORB-DETAIL into Std Q10 | Layer blanks become the "if exotic" follow-up |
| Q7 | Tech constraints (must/cannot/prefer) | **ABSORB → new Q14** | Named absorb-worthy in F-017/REVIEW_005 |
| Q8 | 3–5 must-have features | DROP-DUPLICATE | Captured by APP_BRIEF §6 In-Scope + Hero Action + Success Demo |
| Q9 | Out-of-scope list | DROP-DUPLICATE | ≈ Std Q5 (which has the Hard Gate — stronger) |
| Q10 | Hard deadline | **ABSORB → folded into new Q14** (Constraints & Deadline) | Named in F-017 characterization |
| Q11 | External integrations (APIs/services/data) | **ABSORB → new Q15** | Named absorb-worthy |
| Q12 | What could go wrong (tech/dependency/timeline) | **ABSORB → new Q17** (Risks & Unknowns) | Named absorb-worthy; complements Std Q12 failure modes |
| Q13 | What don't we know yet | **ABSORB → folded into Q17** | Unresolved items land in Planning State as ❓ Open Questions — natural fit |
| Q14 | Security/compliance requirements | **ABSORB → new Q16** | Named absorb-worthy |
| Q15 | Visual anchor checklist | DROP-DUPLICATE | ≈ Std Q4; the "None → STOP" rule gets one line added to Q4's note |

### Result: new "Phase 4 — Constraints Deep-Dive" (optional, before handoff)

- **Q13 App Type:** Full-Stack Web / Backend Bundle / Local-First Tool → feeds the ARCHITECT_PLAYBOOK §4 router
- **Q14 Tech Constraints & Deadline:** must use / cannot use / prefer / hard deadline
- **Q15 External Integrations:** APIs, services, data sources ("none" is a valid answer — record it)
- **Q16 Security / Compliance:** requirements or "none identified"
- **Q17 Risks & Unknowns:** technical / dependency / timeline risks + what we don't know yet → unresolved items MUST land in Planning State as ❓

### APP_BRIEF template merge

Standalone template stays canonical (it has Planning State §8 — the playbook's lacks it). It gains three compact sections fed by Phase 4: **Integrations** (after Domain Concepts), **Constraints** (must/cannot/prefer + deadline), **Risks & Unknowns** (unresolved → Planning State ❓). Playbook's §5 template retires (its unique persona-table detail is represented via enriched Q2 + existing template §3 User & Auth Scope).

### Housekeeping (Doc 1)

- Standard header (Tier 2 — Pipeline Agents · v2.2 · 2026-07-07); title "🏗️ ARCHITECT QUESTIONNAIRE".
- "✅ Changes Applied — GPT Recommendation" table → retired into a real Version History (as the v2.1 row); chat-residue closing line ("Ready for the manual experiment… Tony. 🎯") removed, noted in history.
- CRLF → LF normalization (FLAG 1).

---

## DOC 2 — ARCHITECT_PLAYBOOK → v2.2 (only after Doc 1)

| # | Change | Finding |
|---|---|---|
| 1 | §3 → summary + pointer to ARCHITECT_QUESTIONNAIRE (single source), using the FRONTEND_FIRST §14 relocation pattern: "Doctrine relocated" callout + what lives there + "Why This Split" citing the Doctrine Pairing Principle (SFP §1.5). Heading kept (ToC anchor) | F-017 |
| 2 | §5 → same treatment: pointer to the questionnaire's APP_BRIEF template. Playbook keeps only the type-specific EMPHASIS guidance (§6 stays — it's additive, not duplicated) | F-017 |
| 3 | §1 pipeline diagram redrawn to Designer v2.0 model (token file primary + HTML/PNG + UI_SPEC + manifest) — pattern copied from DESIGNER_PLAYBOOK §1 | F-002 |
| 4 | De-Stitch: §2 "Suggest using Google Stitch" → style tile / reference screenshot; §2 inputs table "Stitch output" → "style tile"; §8 package "(screenshot/Stitch/sketch)" → "(screenshot/style tile/sketch)". §3's Stitch checkbox dies with the shrink | F-002 |
| 5 | §2 Recon Mode gains the RECON_QUESTIONNAIRE mutual pointer ("the stark-recon skill executes RECON_QUESTIONNAIRE; recon = Phase 0 of the Blueprint lifecycle") | F-024 |
| 6 | Version = 2.2 everywhere; footer version block → proper Version History table at bottom (rows: 2.2, 2.1 from existing prose, 2.0 baseline); standard header at top | F-016, F-018 |
| 7 | "AI App Factory" → "App Factory" in blockquote/footer (FLAG 2 — F-008 consistency) | F-008 spirit |

## DOC 3 — RECON_QUESTIONNAIRE → v0.5

| # | Change | Finding |
|---|---|---|
| 1 | §13 questions Q10.1–Q10.4 → Q13.1–Q13.4; Recon Report Format "Section 10 — Surprises" → "Section 13 — Surprises" | F-023 |
| 2 | Numbering gap: **TOMBSTONE stubs** for §7 and §10 ("Retired number — see Version History; numbers are stable IDs, not positions") instead of renumbering 8–13 → 7–12. RECOMMENDED (FLAG 3): renumbering breaks battle-referenced question IDs — the audit itself cites Q8.1–8.3/Q9.1, F-042 cites Q3.4, and the repo-side stark-recon skill consumes this doc; cross-repo refs can't be updated from here | F-023 |
| 3 | F-024 mutual pointers in "How To Use This": ARCHITECT_PLAYBOOK §2 makes recon law; the stark-recon skill automates this questionnaire (this doc = the skill's source content); recon = FFM Stage 0 + Blueprint lifecycle Phase 0 | F-024 |
| 4 | Q3.4 nuance box (F-042 outcome, cites RECON_WAVE0 Q1): kit is TABLE-BASED (`user_roles` = source of truth; `get-user-role.ts` canonical). The live smell = any AUTHZ read from `user_metadata` OR any client-writable role write path. Nuance: metadata MAY carry a role ONLY as creation-time transport IF written via the protected channel. Grep unchanged | F-042 |
| 5 | Standard header (replacing the ad-hoc status blockquote; purpose lines preserved); Version History row 0.5 | F-018 |

## DOC 4 — DESIGNER_PLAYBOOK → v2.1 (micro)

| # | Change | Finding |
|---|---|---|
| 1 | §13: `TOKEN_FILE.md` line → "reference snapshot / drop-in template — NOT the live file; the live token values are `globals.css` (GDSH §8 ruling)" | F-025 |
| 2 | §13: `THEMING_MANUAL_v1.0.md` → `THEMING_MANUAL.md` | F-011 |
| 3 | Standard header; footer version block folds into it; Changelog → "Version History" + v2.1 row; "AI App Factory" → "App Factory" in blockquote/footer (FLAG 2) | F-018 |
| 4 | Nothing else — Tier 2 gold standard stays untouched | — |

## Order & process

Questionnaire FIRST → Playbook → Recon → Designer. One suggested commit per doc; stop after each for operator review. No git.

## Files I will NOT touch

ENGINEER_PLAYBOOK (Wave 2B), FFM_PLAYBOOK, FRONTEND_FIRST (read-only template), all Wave 1 docs, all manuals/design docs, _AUDIT/, _OTHERS/.

## Flagged decisions needing approval

1. **CRLF→LF normalization** of the Questionnaire (matches repo; whole-file diff).
2. **"AI App Factory" → "App Factory"** in blockquotes/footers of the four edited docs (F-008 consistency sweep).
3. **Tombstone stubs instead of renumbering** in the Recon doc (preserves Q8.x/Q9.x IDs cited by audit + repo-side skill).

## Verification gates

- stitch → 0 in live doctrine (history rows exempt); `_v[0-9]` → 0 (history exempt); mojibake + C1 (excl. CR/LF/TAB) → 0
- Playbook §3/§5 are pointers; questionnaire has Hard Gate + Reality Rule + Planning State intact
- 4/4 standard headers + new Version History rows
- Final CHANGES / DIDN'T TOUCH / CONCERNS summary
