# RRM Module Kit — Architect Instructions

**v0.1 · reusable templates, not an executable Cyber Pharma module**

Replace every <...> field with project-grounded values. Remove inapplicable guidance with an explicit reason. Do not ship a packet containing unresolved blocking placeholders. Choose module identity and destination from the actual project conventions; do not infer the next number from this kit.

## Packet files

| File | Author / timing |
|---|---|
| CLAUDE.md | Architect before engineering |
| RRM_BRIEF.md | Architect; Director approves scope |
| FINDINGS_DISPOSITION_LEDGER.md | Architect proposes; Director rules; evidence lanes append |
| ACCEPTANCE_SPEC.md | Architect-approved requirements before build; Claudy hands over the artifact with completion evidence separately |
| CLAUDY_PROMPTS.md | Architect; staged engineering and bounded QA repairs |
| EXECUTION_LOG.md | Claudy during engineering/repair |
| QA_HANDOFF.md | Claudy assembles; SOL/Cody independently verify |
| QA_TEST_PLAN.md | SOL after QA entry; Cody records execution in report |
| QA_CERTIFICATION.md | SOL after adjudication |
| CLOSEOUT_CHECKLIST.md | QA cleanup followed by Architect-directed Claudy closeout and Director Git |

Place QA-generated plans/reports/evidence under the project's <module>/QA/ lane. Copy the relevant approved QA guidance into the repo's governing-doc lane with version/provenance. Original reports may live alongside the packet or be referenced from a durable repo-local evidence location. Avoid secrets, PHI and unnecessary raw workspaces.

**Contract freeze:** front door, brief, approved acceptance requirements and engineering prompts freeze at engineering handoff. Record approved changes/interpretations in an append-only errata/decision record; do not rewrite history. Completion evidence, QA reports and later decisions append with author/time/specimen.
