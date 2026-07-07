# REVIEW 005: 2_AGENTS-ARCHITECT_QUESTIONNAIRE_v2_1.md

> **Review Series:** Stark Industries App Factory — Full Doc Stack Audit
> **Reviewer:** Architect Jarvis
> **Date:** 2026-07-06
> **Doc Version Reviewed:** v2.1 (FINAL) — no date in doc (see finding 3)
> **Tier:** 2 — Pipeline Agents
> **Verdict:** KEEP — needs v2.2 (merge into single source + de-Stitch + standard header)

---

## 1. What This Doc Is

The ignition instrument: a 12-question, 3-phase interview (Quick Ignition → Data Reality → Constraints & Success) plus the APP_BRIEF.md template. The preamble is constitution-grade: "a state transition tool... the anti-hallucination boundary for the entire planning chain." Converts raw ideas into machine-usable planning state that downstream agents operate on without assumptions.

## 2. Strengths

- **Preamble framing** — clearest statement of the Architect phase's purpose in the entire stack ("NOT requirements gathering. NOT design... the anti-hallucination boundary").
- **Planning State table (template §8)** — 🔒 Decision / ⚠️ Assumption / ❓ Open Question classification. Promotable doctrine (D-009): epistemics as a table format; every factory artifact could classify claims this way.
- **⛔ Hard Gate** — out-of-scope requires 5+ items or the Architect must pause. A refusal condition built into the doc; agents execute hard gates better than guidelines.
- **📌 Reality Rule** — core objects are real/persisted unless explicitly marked UI-only. Kills a class of downstream assumption bugs.
- Hero Action (<10s), Brain Check (AI vs CRUD), 3-step Success Demo — high signal-to-question ratio; 12 questions do the work of 40.

## 3. Findings

| ID | Severity | Finding |
|----|----------|---------|
| F-017 (characterized) | HIGH — structural divergence | NOT copy drift — two different instruments. Standalone: 12-Q / 3-phase with Hard Gate + Reality Rule + Planning State. Playbook §3: 15-Q / 6-phase with NONE of those features but with unique content (tech constraints Q7, deadline Q10, integrations Q11, risks/unknowns Q12-13, security Q14). APP_BRIEF templates likewise diverged (playbook's lacks Planning State §8). Siblings that evolved separately from a common ancestor. |
| F-002 (this doc's instance) | HIGH — retired tool | Phase 1 Q4: "screenshot, Stitch output, or Figma link." Stitch retired by Blueprint v2.0. |
| F-018 (this doc's instance) | LOW — convention | No standard header block, no date, no version-history table. Provenance lives in a "Changes Applied — GPT Recommendation" table (chat residue as changelog). |

## 4. Required Changes for v2.2

1. **Become the single source (F-017 resolution):** absorb the playbook-only questions worth keeping — tech constraints, external integrations, security/compliance, risks/unknowns — either as Phase 3 additions or an optional Phase 4 "Constraints Deep-Dive." Explicitly drop or fold duplicates (playbook Q1-4 ≈ standalone Q1/Q11). Playbook §3 + §5 then shrink to summary + pointer (coordinate with ARCHITECT_PLAYBOOK v2.2 / REVIEW_004 changes).
2. De-Stitch Q4 → "screenshot, style tile, or Figma link" per Blueprint v2.0.
3. Add standard header block (name, version, date, status) + real version-history table; retire the "GPT Recommendation" table into it as the v2.1 entry.
4. Keep Hard Gate, Reality Rule, Planning State untouched — they are the doc's crown jewels.

## 5. Cross-Doc Dependencies Noted

Duplicated/diverged content in: ARCHITECT_PLAYBOOK §3 + §5 (F-017). Referenced by: Blueprint Phase 1 (implicitly), APP_BRIEF consumers (Designer, Engineer via Handoff). Conflicts with: Blueprint v2.0 (Stitch, F-002).

---

*Part of the Factory Doc Stack Audit series. See FINDINGS_LOG.md for the running catch list.*
