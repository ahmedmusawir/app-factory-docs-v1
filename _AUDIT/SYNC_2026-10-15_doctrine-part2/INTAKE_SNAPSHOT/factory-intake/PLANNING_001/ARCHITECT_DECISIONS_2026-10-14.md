# Architect Decisions — 2026-10-14 (attributable record for Planning 001)

> **ARCHITECT DECISION RECORD — recorded by the Engineer seat from the Architect's review as relayed by the Director. These are Architect decisions taken under the Director's delegation (RUL-06 / navigation label C.1: "Tony delegated placement to Jarvis"). They are not new verbatim Director rulings, not sync cargo, not an UPDATE MAP, not intake approval, and not authorization for canonical edits, an `_INBOX/` drop, skill changes or Git actions.**

| Field | Value |
|---|---|
| Decision date | 2026-10-14 |
| Decider | Jarvis (Architect), under the Director's delegation of document and template placement (RUL-06) |
| Relayed in | Tony's instruction "CLAUDY — CORRECT THE QAM DRAFT AND PREPARE QA LEAD REVIEW" (2026-10-14), after Jarvis reviewed `CONSOLIDATED_INTAKE_001_2026-10-14_184845.zip` |
| Recorded by | Claudy (documentation Engineer seat), 2026-10-14 19:10 +0600. Decision text is preserved from the instruction; paraphrase is marked |
| Companions | `DIRECTOR_RULINGS_2026-10-14.md` (R1.1), `COMBINED_DECISIONS_001.md` (R3), `COMBINED_DEPENDENCY_MAP_001.md` (R3), `INTAKE_CLARIFICATIONS_001.md` (R3), `../INTAKE_ADDENDUM_001_v0_2/` |

**ID conventions.** `AD-nn` are local to this record (Architect decisions), distinct from `RUL-nn` (Director rulings) and `DEC-nn` (correction-package decisions).

---

## AD-00 — Architect assessment of CONSOLIDATED_INTAKE_001 (context, not a decision)

Verbatim: "The consolidated intake structure is accepted. The QAM templates remain drafts pending QA Lead review. Canonical DocSet synchronization has not been authorized by this review."

Provenance note (verbatim): "Jarvis verified this consolidated ZIP and its 28 indexed addendum files. The locally available harvest ZIP has a different outer hash/member count from Claudy's recorded copy; E-8 remains unconfirmed. Do not claim Jarvis confirmed that historical ZIP or replace either copy to force a match."

Recorded effects: dependency map P1 (addendum accepted as the index of the post-harvest material; v0.2 refresh to be re-verified by Jarvis); clarifications CL-28 (verification receipt) and CL-29 (two harvest ZIP copies differ; E-8 stays unconfirmed; neither copy replaced).

## AD-01 — Home of the QAM template set (DEC-19 remainder; COMBINED_DECISIONS N-2(b))

**Decision (verbatim).** "Under Tony's C.1 delegation, Jarvis selects: `03_BUILD_METHODOLOGY/_templates/QAM/`. Use the proposed versioning arrangement: Stable filenames. Template-set version and governing QAM_PLAYBOOK version recorded in the set. Superseded sets archived under `_ARCHIVE/QAM_TEMPLATES_v<version>/`. Changes tracked through the owning QAM_PLAYBOOK MANIFEST row and CHANGELOG. Explicit template verification in the sync acceptance scope because existing lints do not recurse into this folder."

**Instruction attached (verbatim).** "Record this as an Architect decision under Director delegation, not a new verbatim Director ruling. Carry the placement and cargo-path translation into the future UPDATE MAP. Do not install the templates into canonical doctrine yet."

**Basis.** `../INTAKE_ADDENDUM_001_v0_2/TEMPLATE_PLACEMENT_RECOMMENDATION.md` option A (Ruling 9 tier-subfolder precedent; `_ARCHIVE/README.md` versions-in-headers rule; non-recursive lint scope; D15 cargo-path translation).

**Resolves.**
| ID | Status | Effect |
|---|---|---|
| N-2(b) (template home) | **DECIDED (Architect, delegated)** | Home fixed as above. N-2(a), QA Lead acceptance of the draft's QA behavior, remains open and is the only remaining gate for QAM-03 besides the sync run itself. |
| DEC-19 (where templates live) | NARROWED further | The `TEMPLATES/QAM/` home is decided; kits, worked examples, issue logs and the locator remain OPEN. |
| E-11 (Hub-law home) | RESOLVED for this set | The decision pre-answers the Gate 1 class question for the template unit (taxonomy has no class for a template set; the decision supplies the landing path). A taxonomy note remains an optional later `XB-SKILL` job. |
| QAM-03 completion | still incomplete | Until QA Lead acceptance (N-2(a)) and the sync run lands the set at the decided home. |

**Carried into the future UPDATE MAP (planning map §4a / §9).** (paraphrase)
- Landing path `03_BUILD_METHODOLOGY/_templates/QAM/` for the accepted set; no MANIFEST row of its own; the QAM_PLAYBOOK row's Purpose/"Pairs with" and the CHANGELOG line carry the change.
- Cargo-path translation flagged under D15: the playbook's literal `TEMPLATES/QAM/` (§5) is cited in the Hub text as `03_BUILD_METHODOLOGY/_templates/QAM/`.
- Versioning: set version and governing QAM_PLAYBOOK version recorded in the set's `README.md`; stable filenames; superseded sets copied to `_ARCHIVE/QAM_TEMPLATES_v<version>/`.
- Acceptance scope: the sync run's acceptance specification includes explicit template verification (all files present; identical dual-entry routing; state/permission consistency; no prefilled results, approvals, SHAs or credentials), because the lints do not recurse into the folder.

**Does not decide.** Whether the draft's QA behavior is acceptable (QA Lead). When the sync run happens (Director, P2). Anything about kits, worked examples or the locator (DEC-19 remainder).

---

## What this record does not do

- It does not install anything in `03_BUILD_METHODOLOGY/`; the template set stays in intake staging (`../INTAKE_ADDENDUM_001_v0_2/TEMPLATES/QAM/`).
- It does not approve the templates, the addendum or either package as DocSet Sync cargo.
- It does not edit canonical doctrine, MANIFEST, CHANGELOG, skills, lints or CI, and does not authorize an `_INBOX/` drop, a sync run or any Git action. The Director-executed Git convention (map §9 P6) is established and is not reopened here.

*ARCHITECT DECISION RECORD — companion to Planning 001 R3. For Director (Tony) and QA Lead information.*
