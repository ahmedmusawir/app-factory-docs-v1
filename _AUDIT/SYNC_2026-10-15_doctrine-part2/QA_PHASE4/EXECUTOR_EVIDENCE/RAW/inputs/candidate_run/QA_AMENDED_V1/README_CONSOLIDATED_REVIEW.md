# Consolidated amendment and specification review

**Eight ownership corrections confirmed; one execution-package acceptance failure (QA-AF01). Gate 2 amendment and Gate 3 remain PENDING. Phase 3 is NOT RELEASED.**

Read in order:
1. `QA_AMENDED_V1/AMENDMENT_CONFIRMATION.md`.
2. `QA_AMENDED_V1/QA_AF01_PATCH_FIDELITY.md`: two archive outputs are wrong when the supplied patch is applied; source content/index is correct. Engineer repair and independent retest required.
3. `AMENDED_V1/AMENDMENT_V1.md` and the eight exact edits.
4. `QA_AMENDED_V1/DOCSET_SYNC_ACCEPTANCE_SPEC_AMENDED_V1.md` and `SPEC_REVISION.diff`.
5. `QA_AMENDED_V1/REVIEW_IDENTITIES.json`, `ORDERED_GATE_DECISIONS.md`, `OPERATOR_INSTRUCTIONS.md` and complete preservation files.

Prepared by Cody in the QA Lead seat at Tony’s explicit assignment. Jarvis’s acceptance is conveyed by Tony; QA’s source-based verification is separate. The exact current 14:58 input ZIP is retained under SOURCE_PACKAGE; its SHA-256 is `711914a986cd64071f4372e0c428249ba27c6eba8ace160918c312d098b34f60`. The 13:50 package is superseded and not used.

Archive layout mirrors paths relative to the existing run: AMENDED_V1 is exact source, QA_AMENDED_V1 contains this review, and root records/PROPOSED_CONTENT/BASELINE_CONTENT are unchanged context needed to compare the complete proposal. The original spec at root is historical; the proposed matching revision is under QA_AMENDED_V1. No root canonical file is installed by extracting this review. Extract only into a fresh review directory, never over the repository.

SHA256SUMS.txt inventories every payload member except itself. Verify after extraction with `sha256sum -c SHA256SUMS.txt`. One ZIP is delivered: `FACTORY_AMENDED_V1_QA_SPEC_REVIEW_2026-10-17_160835.zip`. Its outer hash is recorded in the external delivery receipt and response, not recursively inside the ZIP. Source scripts are included as evidence; do not execute downloaded scripts from the extracted tree. The independent verification helper was authored locally and operates from the trusted repository with isolated Python.

This package is review evidence, not the full execution worktree or intake snapshot. Tony’s preservation commit and run-only transfer carry the full existing run, including the 189-file snapshot. All Git commands are Tony-only. No approval, implementation, publication, installed-template acceptance or Gate Q result is fabricated.
