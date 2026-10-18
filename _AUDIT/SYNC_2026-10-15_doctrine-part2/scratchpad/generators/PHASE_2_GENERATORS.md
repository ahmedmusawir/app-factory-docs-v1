> HISTORICAL — superseded for current recovery by MC_GENERATORS.md and the cody_mc_* scripts. Prior counts/instructions below describe the earlier review package.

# Phase 2 generator recovery

Current proposal: 334 exact content edits, 93 paths. All scripts operate on the isolated PROPOSED_CONTENT and run records, never canonical destinations or Git mutations. Run from repository root. Sources referenced by original factory-intake paths are preserved under INTAKE_SNAPSHOT at the same relative paths; do not infer a missing original is missing cargo.

Content → newdocs → metadata is a dependent sequence: stop if any step fails. The metadata step requires fresh content/newdocs first (do not repeatedly bump an already generated tree). Verify with cody_phase2_verify.py. lints in the proposal tree are unchanged verification inputs, not implementation changes. No copied generator is an instruction to apply the patch or a substitute for Gate 2/3.

Reconcile/finalize scripts record the reviewed snapshot and are recovery evidence, not automatic semantic approval for future changed wording. A changed proposal requires a new semantic review, map amendment as applicable, hashes and handoff; do not run a classification script to manufacture a verdict. POST_VERIFICATION_STATUS_TRANSITIONS.json is a separate conditional part of the proposed map.
