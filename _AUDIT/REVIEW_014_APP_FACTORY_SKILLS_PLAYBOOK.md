# REVIEW 014: 3_METHOD-APP_FACTORY_SKILLS_PLAYBOOK.md

> **Review Series:** Stark Industries App Factory — Full Doc Stack Audit
> **Reviewer:** Architect Jarvis
> **Date:** 2026-07-06
> **Doc Version Reviewed:** v1.0 (2026-05-05) — oldest METHOD doc, single changelog entry
> **Tier:** 3 — Build Methodology (TIER CLOSER)
> **Verdict:** KEEP — needs v1.1 (de-Stitch example, launch-CWD doctrine, June exemplars, outbound refs, header)

---

## 1. What This Doc Is

The skill-authoring constitution: two-type taxonomy (Stark Skills = agent guides / operator executes; Agent Skills = agent executes), the CLAUDE.md + SKILL.md two-file contract, single-vs-family structures, Anthropic Skills v2 format, activation flow, Plan Mode + operator override, evidence discipline, evolution principle, eight named anti-patterns from real authoring history, and exemplar-based teaching (Brain Drain as the model).

## 2. Strengths

- **The activation contract as an enforceable test:** "drop in folder, point at folder, observe correct behavior with zero operator preparation" — with the failure definition: "you have not built a skill. You have built a checklist with extra steps."
- **One-question type test** — operator pastes commands (Stark) vs agent executes (Agent). Taxonomy as a single fork; blurred skills must split.
- Doctrine with a voice ("Tony Stark refuses to be a Vibe Coder"; "a bad skill is a force divider").
- Walks its own talk: exemplar-based, evidence-disciplined, evolution-principled; anti-patterns sourced from real prior failures (e.g., the navigation-not-management CLAUDE.md case).
- Hygiene: zero mojibake, zero versioned cross-refs.

## 3. Findings

| ID | Severity | Finding |
|----|----------|---------|
| F-002 (instance) | MEDIUM | §2 + §16 feature "Stitch Prompting Discipline" as a fully-specified Agent Skill example (5 refs: chunking rules, activation triggers). Pre-retirement doc, never updated. v1.1 swaps for the living successor: a token-driven-HTML Designer skill per the Canonical Page Method. |
| F-037 | MEDIUM — pre-ecosystem staleness | v1.0 (May 5) predates the factory's actual skills: the repo's June `_SKILLS/` ecosystem (stark-recon, starter-kit-cleaner, repo-security) is absent; the launch-CWD lesson (skills resolve from Claude Code's launch directory — Q6.5, a skills-domain lesson) is missing (zero CWD mentions); recon: zero refs. Location ambiguity: this doc homes skills at `_SKILLS/`; RECON_QUESTIONNAIRE checks `.claude/skills/` — two conventions, no bridge. Outbound factory cross-refs: zero (FFM points in; nothing points out). |
| F-018 (instance) | LOW | No version header at top; history lives at §17 tail. |

## 4. F-021 Input (scope recommendation)

This playbook = factory doctrine → in the audit (done, this review). Repo `_SKILLS/*/CLAUDE.md` files = skill INSTANCES governed by this playbook → separate track, audited later against this playbook's activation contract. Doctrine lives in the Hub; instances stay repo-side. Tony's confirm closes F-021.

## 5. Required Changes for v1.1

1. Replace the Stitch skill example with a token-driven-HTML Designer skill example.
2. Add launch-CWD doctrine (+ reconcile `_SKILLS/` vs `.claude/skills/` conventions with RECON_QUESTIONNAIRE).
3. Add the June skill exemplars (stark-recon as a Stark Skill case study).
4. Add outbound cross-refs (FFM_PLAYBOOK §11 pairing, RECON_QUESTIONNAIRE §6).
5. Standard top header block.

## 6. Cross-Doc Dependencies Noted

Inbound: FFM_PLAYBOOK (pairs-with). Outbound: none (gap). Should reference: RECON_QUESTIONNAIRE (Q6.1/Q6.5), FFM_PLAYBOOK skills/ authoring guide, DESIGNER_PLAYBOOK (replacement example source). Governs: repo `_SKILLS/` instances (F-021 split).

---

## TIER 3 CLOSING SUMMARY (Reviews 010–014)

Five docs, five KEEPs. The methodology layer is the factory's strongest tier content-wise — lesson-driven, gate-enforced, exemplar-paired — and its findings are mostly *bytes and pointers*, not doctrine: encoding corruption (F-012/F-034), header/version metadata lies (F-033), same-campaign stale refs (F-032), and isolation (F-035 testing island; F-037 skills time capsule). Two structural items: recon absent from the FFM it's supposed to open (F-024), and the Designer-v2.0 modernization never propagated (F-031). Gold promoted: D-013 (lesson routing), D-014 (doctrine re-injection), D-015 (honesty artifacts). Tier 3 rewrite theme: *reconnect the islands, repair the bytes, modernize Role 1.*

---

*Part of the Factory Doc Stack Audit series. See FINDINGS_LOG.md for the running catch list.*
