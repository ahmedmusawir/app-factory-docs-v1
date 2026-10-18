# Current MC generator recovery

Run only in the existing repository/run preparation context. No generator applies canonical implementation or mutates Git. Inputs are pinned BASELINE_CONTENT, PRE_MC history/original new-playbook copies and accepted source translations. Fresh dependent order: cody_mc_correct.py → cody_mc_metadata.py → cody_mc_records.py. Stop on error. cody_mc_rebuild_check.py performs two fresh rebuilds and compares the plan/index bytes. Then cody_mc_update_map.py and cody_mc_propagation.py reconcile current run records; cody_mc_verify.py verifies them read-only except its own evidence output. Final handoff/disposition/operator prose is curated, not an automatic QA verdict.

Use the environment Python with markdown_it for structural checks. Renderer uses /usr/bin/python3 with installed gi/Rsvg/cairo; it writes review previews only. Existing lints are copied unchanged and run with -B -I; no lint/CI rewrite. New/changed proposals after review require renewed semantic checks and new package hashes. Never rerun a classifier to manufacture independent acceptance.

POST_VERIFICATION_STATUS_TRANSITIONS and LANDING_DATE_PLAN describe future conditional actions only. EVIDENCE_TEMPLATES supply no completion evidence. Older cody_phase2_* generators are retained as historical recovery material and must not overwrite the MC-corrected state.
