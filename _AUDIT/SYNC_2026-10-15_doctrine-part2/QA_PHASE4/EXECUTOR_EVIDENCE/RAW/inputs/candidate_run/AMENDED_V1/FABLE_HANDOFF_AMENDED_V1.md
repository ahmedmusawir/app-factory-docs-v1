# Handoff to Fable (QA Lead) — AMENDED-v1 (D-1 / D-2 / OBS-1 / ownership sweep)

From Cody (Engineer), 2026-10-17 (supersedes the 13:50 two-span handoff). Your specification stays Fable-owned; I have not edited it and claim no acceptance. Gate 3 has not been approved. Phase 3 is not released.

## 1. Amended ownership wording (eight spans, three documents)

| Edit | Item | Document : line | Old → New | Authority |
|---|---|---|---|---|
| E373 | D-1 | `APP_FACTORY_BLUEPRINT.md` : 140–142 | `## 📋 ENGINEER AGENT: WHAT IT PRODUCES` + blank + `The Engineer's full output list:` → `## 📋 ENGINEERING PACKAGE: APPROVED CONTRACT ARTIFACTS` + blank + "The Architect assembles the approved contract artifacts below for the Engineer to implement. DATA_CONTRACT is authored before Design; FILE_TREE is optional when implementation structure and boundaries are otherwise explicit." | Architect text, Tony brief 1 |
| E374 | D-2 | `ENGINEER_PLAYBOOK.md` : 746 (§12 template fence) | `> **Author:** Engineer Agent` → `> **Author:** Architect` | Architect text, Tony brief 1 |
| E375 | OBS-1a | `ARCHITECT_PLAYBOOK.md` : 63 ("What the Architect Does NOT Do") | `\| Define data schemas \| Engineer Agent \|` → `\| Implement approved data schemas as migrations and models \| Engineer Agent \|` | Jarvis rows, Tony brief 2 |
| E376 | OBS-1b | `ARCHITECT_PLAYBOOK.md` : 67 | `\| Define API contracts \| Engineer Agent \|` → `\| Implement approved API contracts \| Engineer Agent \|` | Jarvis rows, Tony brief 2 |
| E377 | P-1 | `APP_FACTORY_BLUEPRINT.md` : 87 (Phase 3 owner table) | ``\| `DB_SCHEMA.md` \| Database tables, relationships, indexes \| Engineer \|`` → owner `Architect` | sweep; Engineer-worded under the rule |
| E378 | P-2 | `APP_FACTORY_BLUEPRINT.md` : 88 | ``\| `API_SPEC.md` \| Endpoints, methods, auth, error codes \| Engineer \|`` → owner `Architect` | sweep; Engineer-worded |
| E379 | P-3 | `ENGINEER_PLAYBOOK.md` : 86 (Core Responsibilities) | `\| **Data Contracts** \| Define schemas, APIs, file formats \|` → `\| **Data Contracts** \| Implement the approved schemas, APIs and file formats; contract changes return to the Architect \|` | sweep; Engineer-worded |
| E380 | P-4 | `ENGINEER_PLAYBOOK.md` : 998 (§13 Engineer Focus) | `- Database schema design (Supabase/Firebase)` → `- Implement approved database schemas as migrations and models (Supabase/Firebase)` | sweep; Jarvis phrase |

Rule applied throughout (Jarvis): **the Architect owns the approved contract; Engineering implements it.** No new policy. E377–E380 are Engineer wording under that rule and are offered for your and Jarvis's confirmation like the rest.

Nothing else moved: versions, dates, history rows, MANIFEST, CHANGELOG, archives, templates, workflows, SVGs, closeout transitions and all 151 landing-date spans are identical. Evidence: `AMENDMENT_V1.md`, `AMENDMENT_V1_EDITS.json`, `AMENDMENT_IDENTITIES.json`, `OWNERSHIP_PROPAGATION.tsv` (39 hits, 8 resolved, 31 retained with rationale), `VERIFICATION.json`.

## 2. Requests

1. **Confirm D-1 and D-2, and grade OBS-1 / P-1…P-4** against the amended tree (`AMENDED_V1/PROPOSED_CONTENT/` for the three files; every other path unchanged from the Gate 2 tree). AC6(c)/(d) are the anchors for D-1/D-2; the remaining six spans fall under the same ownership rule (AC5/AC6 family) — your call how to cite them.
2. **Re-anchor only the affected specification references** when you issue spec AMENDED-v1:
   - edit count 372 → **380** (AC1/AC2 cells; §3 "§C exact proposal (372 edits …)");
   - `EXECUTION_PROPOSAL_INDEX.json` identity `84337dcd…` → `69244f4edc347b30b81ed6a909bae4fbb5130864319e9f8cd84b5d5c22e59ba6` once Tony approves the amendment at Gate 2 (until then the frozen identity remains the approved one);
   - `proposed_sha256` / bytes: Blueprint `de0321e3…` → `df17ac84…` (14,636 B); ARCHITECT_PLAYBOOK `ad0712bf…` → `3ec6bc37…` (26,479 B); ENGINEER `72477ec8…` → `b0f74569…` (50,972 B) — full values in `AMENDMENT_IDENTITIES.json`;
   - AC6(c)/(d) wording from "currently RETAINED" to the amended text; §6 D-4 note can cite `D4_STARTER_KIT_METADATA_NORMALIZATION.json`;
   - line references: all eight spans are line-count-neutral (three lines → three lines for E373; single-line replacements elsewhere), so Blueprint 87/88/140–142, ARCHITECT 63/67 and ENGINEER 86/746/998 keep their positions.
   - The 13:50 identities (`5ac27e0d…`, `ef3826c9…`, index `c35406fe…`) are superseded; do not anchor to them.
   Paths (101), templates (25), archives (32), CHANGELOG (39), MANIFEST (34), transitions (12/9) and date spans (151) need no change.
3. **Correct the AC37 role whitelist (already identified by Jarvis).** AC37 currently allows only Architect / Engineer / Director / Designer / QA Lead / QA Executor. The approved `WORKFLOW_PUBLICATION_PLAN.json` steps (and therefore the approved SVG lane labels) use eight seat labels: **Architect, Authorized operator, Designer, Director, Engineer, QA Executor, QA Lead, Reviewers**. Please derive the permitted labels from that plan file (data-bound rather than hand-typed), keeping the prohibition on historical personas ("Director of QA", "Codex", "Sol", "Claudy", `INITSCRIPT`, `CLOUDDEPLOYMENT`) and on ungranted authority ("QA Lead executes/runs tests"). The frozen SVGs pass that derived list today.

## 3. Observation, no change proposed

**OBS-2** — `04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:535` (DevOps Handoff Note): "Schema design and migration SQL are the developer's responsibility." Developer-vs-DevOps operational split, not a seat statement; retained. Also retained: ARCHITECT_PLAYBOOK "Type Implications for Engineer" rows naming "DB schema" / "API contracts" as implementation subjects. Dispositions: `AMENDMENT_V1.md` §7.

## 4. Status you should preserve

AMENDED-v1 is a proposal that re-enters Gate 2 (map §O freeze rule). Gate 3 remains pending Tony. No installation, QA, cleanup or closeout has occurred. Phase 3 is NOT RELEASED.
