# REVIEW 022: 5_DESIGN-GLOBAL_DESIGN_SYSTEM_HANDBOOK.md

> **Review Series:** Stark Industries App Factory — Full Doc Stack Audit
> **Reviewer:** Architect Jarvis
> **Date:** 2026-07-06
> **Doc Version Reviewed:** UNVERSIONED (F-018 roster) — content aligns with the June v1.1-era design doctrine
> **Tier:** 5 — Design System (TIER OPENER)
> **Verdict:** KEEP — MODEL DOC (co-champion with Starter Kit Handbook); v1.1 = --role-* contract decision + header

---

## 1. What This Doc Is

The stable design doctrine: four-layer model (tokens → components → patterns → guidelines), the canonical token contract, theming method, component vocabulary (compose > invent; KIPs), Rule Zero + canonical responsive transforms, WCAG AA bar with per-mode contrast tuning, the style-tile method, Designer deliverables, the Canonical Page workflow, anti-patterns, and a one-paragraph version. Defines the three-role token architecture: Handbook = contract (stable) · Theme Library = value-set catalog · `globals.css` = per-project live token file.

## 2. Adjudication Delivered — F-025 SETTLED

§8: "Token file (`globals.css` + Tailwind map) — the executable system. **Primary deliverable.**" The contract owner rules: `globals.css` is the live token file. THEME_LIBRARY v1.1's correction was accurate; DESIGNER_PLAYBOOK §13 is the stale outlier — its fix now cites this authority.

## 3. Strengths (one promotion)

- **§3 TW3/TW4 format fork ("confirm in `package.json`")** — the MODEL for all F-038 fixes: forks on verified kit reality instead of pinning versions.
- **D-017: "The style tile is a view of the token file, not a separate artifact to maintain. Lock the tile = lock the tokens."** No-drift-by-construction — the design-side twin of D-002. Generalizable.
- §2 canonical token set + "resist sprawl"; brand-never-status semantic rule; §6 per-mode contrast tuning (L16 institutionalized); §5 canonical responsive transforms; §12 one-paragraph version (summarization discipline for Tier 1 to copy).
- §8 deliverables table matches DESIGNER_PLAYBOOK §8 exactly — the pair is consistent. Bonus pipeline data point: "Designer revises the Architect's draft" of UI_SPEC (collaborative ownership; refines F-029/F-030 greenfield resolution).
- Canonical-name references throughout; zero mojibake; zero versioned refs.

## 4. Findings

| ID | Severity | Finding |
|----|----------|---------|
| F-043 | MEDIUM — contract/catalog mismatch (ties to F-013a) | THEME_LIBRARY v1.1 claims "the contract now includes role identity tokens (--role-*)" — but THIS doc is the contract, and §2 lists no --role-* tokens. Evidence (Gate 10 ThemeToggle ship; cleaner skill's pre-baked --role-* defaults) suggests the Handbook is the stale side. **This is F-013a with a blast radius:** Tony's parked role-colors decision now has a concrete fix location. One §2 addition closes both. |
| F-018 (roster #5) | LOW | Unversioned — no header/date/history. "Rarely changes" is not "never changed" (F-043 proves it). Standard header in v1.1. |

## 5. Required Changes for v1.1

1. **After Tony confirms F-013a:** add `--role-*` tokens to §2's canonical set (with the Theme Library's rules: identity hues, admin ≠ destructive, AA on --card) — closes F-043 + F-013a together.
2. Standard header block + version-history table.
3. Nothing else.

## 6. Cross-Doc Dependencies Noted

Contract authority for: THEME_LIBRARY (catalog), TOKEN_FILE doc (role to be defined at Review 026), DESIGNER_PLAYBOOK (F-025 fix cites §8), all Tier 5. Consistent with: DESIGNER_PLAYBOOK §8 deliverables, Canonical Page Method. Conflict: THEME_LIBRARY v1.1 --role-* claim vs §2 (F-043). Model for: F-038 fixes (§3 version fork).

---

*Part of the Factory Doc Stack Audit series. See FINDINGS_LOG.md for the running catch list.*
