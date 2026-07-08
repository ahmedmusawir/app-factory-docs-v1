# ✅ WAVE 1 — DOC 2 COMPLETE: SOFTWARE_FACTORY_PLAYBOOK → v1.2

**File:** `1_CONSTITUTION-SOFTWARE_FACTORY_PLAYBOOK_v1_1.md` (filename unchanged per Wave 1 rules)

## CHANGES MADE

| # | Change | Finding |
|---|--------|---------|
| 1 | Standard header block (Version 1.2 · 2026-07-07 · Active · Tier 1 — Constitution · Pairs-with); old version block folded in, "Born from" lineage preserved | F-018 |
| 2 | §4 Phase 2 rewritten: Stitch/Figma workflow diagram + Design Spec Document process DELETED; replaced with defer — "Design execution is owned by DESIGNER_PLAYBOOK (token file primary, Canonical Page Method)" + 4-step summary + Designer-deliverable checklist. Heading text unchanged (ToC anchor intact); phase numbering intact | F-009, F-002 |
| 3 | "Phase Vocabulary — One Canonical Map" added to §2: Blueprint lifecycle (incl. Phase 0 Recon) = canonical project-phase map; these 9 phases = execution breakdown; FFM Sub-Phases nest inside build phases. Mapping table 9→Blueprint. No renumbering | F-010 |
| 4 | Phase 8 (§10) gains Reference: TESTING_PLAYBOOK — first inbound bridge to the testing island | F-035 |
| 5 | §1.5 pairing table: 5 versioned refs stripped (`*_v1.1.md` → `*.md`) | F-011 |
| 6 | Mojibake sweep: `â–º`→►, `â–¼`→▼, `â—„`→◄, `âœ…`→✅ PLUS **16 invisible U+0090 C1 control chars removed** (one after every `┐` box corner — residue of the incomplete v1.1 encoding fix; removed via byte-safe write, UTF-8 no BOM preserved) | F-012 |
| 7 | §13 Phase-2 checklist aligned to Designer deliverables (token file / HTML+PNG / UI_SPEC + manifest) | F-009 |
| 8 | Footer suite label de-versioned ("App Factory doctrine") | approved Assumption 2 |
| 9 | Version History v1.2 row logged with finding IDs; v1.1 row annotated "(incompletely — see 1.2)" | D-018 |

## VERIFICATION GATES

| Gate | Result |
|---|---|
| `grep -ri stitch` (live doctrine) | **0** — 1 hit remains, inside the v1.2 Version History row (exempt) |
| `grep -n "_v[0-9]"` | **0** |
| `grep "â"` | **0** |
| C1 control chars U+0080–U+009F | **0** (was 16) |
| Standard header + new Version History entry | ✓ |

## THINGS I DIDN'T TOUCH

- §1 philosophy, §1.5 doctrine-pairing content (refs only), §3 and §5–§9 phase content, §12 feature spec template, §14 manual reference guide.
- Phase numbering and ToC anchors — all intact.
- All other repo files.

## CONCERNS

- **U+0090 lesson (Wave 6 lint spec):** the audit's `grep "â"` gate is blind to bare C1 control chars. The Doctrine Hub mojibake lint must add a U+0080–U+009F scan. Blueprint + Handoff already scanned this session: clean.
- REVIEW_002 item 5 ("consider extracting §1.5 to constitution level") intentionally not done — not in the Wave 1 work order.
- F-004 (knowledge-base diagram lists 7 of 27 manuals) — MANIFEST work, Wave 6.

## Suggested commit

wave1(sfp): v1.2 — Phase 2 defers to Designer, phase map, F-009/F-010/F-012
