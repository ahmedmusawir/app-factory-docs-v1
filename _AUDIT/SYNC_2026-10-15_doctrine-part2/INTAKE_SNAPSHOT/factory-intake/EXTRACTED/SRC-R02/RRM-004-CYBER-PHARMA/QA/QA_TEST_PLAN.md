# RRM-004-CYBER-PHARMA — Independent QA test plan

**Author:** QA Lead (position) · **Date:** <after the candidate commit, before DC-4> · **Candidate:** `<sha>` · **QA HEAD:** `<sha>` · **Baseline:** `<sha>`

> Placeholder left by the Architect on 2026-09-30. **This file is authored by the QA Lead after DC-3** from `QAM_MANIFEST.md`, `../QA_HANDOFF.md`, `../ACCEPTANCE_SPEC.md` and the governing playbook. Not by the Engineer, not by the Architect. The Architect's risk notes are in `README.md` and are input, not the plan. AC-702 grades that this header names the QA Lead and a date after the candidate.

Expected sections (the QA Lead's shape governs; these are the halves the charter names):

1. Entry and stop gates (Q1–Q7 by number; the QF preflight as the first act).
2. Risk ranking — what is attacked first and why.
3. Independent execution — per AC group, with the derivation rule for every reference value (registry reads, installed metadata on the Executor's platform, route table from the Executor's build, image inventory from source).
4. Negative controls — what must still be true (header pair, negative host probe, existing suites unmodified, `src/` diff empty).
5. The deliberate instrument attack (which value or helper is corrupted, and the expected non-zero failure).
6. Authenticated image walk — matrix (roles × viewports × theme at the QA Lead's discretion), the one-sign-in-per-role protocol, what is captured, what is never retained.
7. Evidence and status rules; finding classification; when `REPAIR_PROPOSAL.md` is drafted.
8. Pilot-process rows (AC-700) — what the Executor records, separately from the product grades.
