# Jarvis / Tony / Fable — AMENDED-v3 bounded handoff

Authority: Fable’s preserved QA_LEAD_VERDICT_V2 and JARVIS_REPAIR_RECOMMENDATION, plus Tony’s current message confirming Jarvis V3-1–V3-4 wording and explicitly requiring the V3-2 comment. Exact-patch approval has not been granted. Previous approvals/repairs and verdicts are not reopened or rewritten.

## Proposed identities

- `EXECUTION_PROPOSAL_INDEX.json`: `55537c6411724ab78837d0191d61375654839202acbf15b13a76d98aa8d483e6`
- `BOUND_EXECUTION_INDEX.json`: `55537c6411724ab78837d0191d61375654839202acbf15b13a76d98aa8d483e6`
- `EXECUTION_PROPOSAL.patch`: `afd8f9249854d4e99c385b1e21c459fa297fa5ed5ddcac782d1509747c43faed`
- `AMENDMENT_V3_EDITS.json`: `2a1ef7192f75505f44d6da4b31836e68af31e23de3bc3afb0afd8f5b330ae4fd`
- `SELECTED_EXACT_EDITS.json`: `087adaad2d85b39b363991520c568855d38ca7a76a6c0b275707bd30fd7839eb`

The two indices are identical, date-bound successors (landing date 2026-10-18), using candidate8dff354 before hashes. The patch is a complete three-file delta at that candidate with -p0 paths. New edits E410–E417 are appended to the original409 provenance records. Replay only the new suffix against8dff354; the complete historical list requires its original staging and date-binding history.

## Approval stop

Fable JARVIS_REPAIR_RECOMMENDATION §5(c): “STOP for Tony's Gate 2 record on AMENDED-v3 (additive DIRECTOR_DECISIONS_V3.md).” This package is ready for that decision. The future record should name the exact index and patch above and the three paths; store it additively under RUN/AMENDED_V3, consistent with §4 R12′. No approval record is fabricated here. No candidate edit, commit or push has occurred.

## Bounded retest handoff (after approved landing only)

- R4′: evaluate all fetchProducts / services/productServices matches over live scope by actual code/label/consumer context. PROPAGATION.tsv links every observed occurrence to full MANUAL_READS containers. The rejected prior “generic project-local” rationale is not used. Explicit labels now govern all four affected containers. Distinct fetchProductsByIds(ids) has an explicit Product[] contract; the service-path-only fetchProductBySlug hit is a different single-product/not-found operation, not an unlabelled fetchProducts array consumer.
- R6′: all101 proposed hashes,98 unchanged vs8dff354.
- R7′: headers/version/date and MANIFEST unchanged,39 run CHANGELOG rows with exactly two amended,one existing history row amended per changed manual.
- R8′: unchanged lint suite PASS with zero hits; unchanged lints/.github.
- R10′: twelve pre-transition spans on nine unchanged paths.
- R11′: future one non-merge commit `repair QA-P4 RV2-F01 (AMENDED-v3 <index sha>)` after Tony’s recorded exact-patch approval, authorized working branch only, clean tree/no main write. **Pending:** preparation cannot satisfy actual landing/commit checks.
- R12′: three canonical paths only plus additive RUN/AMENDED_V3/** and future RUN/AMENDED_V3_EXECUTION/**. No broad review restart.

## Carry-forward precision

All98 unchanged index paths and all other candidate-export files are byte-identical. All six previously repaired manuals are untouched; six AMENDED-v2 CHANGELOG repair clauses remain exact. The frozen spec/maps/approvals and original evidence remain unchanged.

STATE is necessarily changed by V3-3/V3-4 and participates in prior R5. We do **not** claim whole-document byte identity for STATE or ARCH. CODE_PRESERVATION verifies all non-comment fenced content and all imports; exact-edit replay bounds all other changes. STATE’s persistence section and RUL-13 default/example lines remain exact. Carry forward the unaffected checks on byte-identical documents and preserved passages; Fable adjudicates that bounded carry-forward evidence. No new R5 implementation or broad retest is proposed. This distinction prevents an impossible “every previously graded document unchanged” claim for the two expressly amended manuals.

The thirty unaffected withdrawal rows (FC-022/038 and the other28) are preserved through exact unchanged prior repair documents plus unchanged non-label content of ARCH/STATE. R4′ is confined to FC-066; no underlying production replacement is certified.

## Reproduce preparation

From the review repo:

```bash
python3 -B -I _AUDIT/SYNC_2026-10-15_doctrine-part2/AMENDED_V3/generators/prepare.py
python3 -B -I _AUDIT/SYNC_2026-10-15_doctrine-part2/AMENDED_V3/generators/verify.py
```

Requires local pinned Git objects/execution worktree and original Downloads handback. Generation writes proposal records only. Verification applies the patch only to a disposable archive export, never to the execution worktree. Reseal after regeneration; verification timestamps/scratch paths change. Preserve approved sealed records once Gate2 is recorded.

Verify the ZIP inventory from its extracted root with `sha256sum -c SHA256SUMS.txt`. Original handback and source copies are in INPUTS; identities pin their bytes. The internal delivery receipt pins payload identities, while the external delivery receipt records the enclosing ZIP hash to avoid self-reference.
