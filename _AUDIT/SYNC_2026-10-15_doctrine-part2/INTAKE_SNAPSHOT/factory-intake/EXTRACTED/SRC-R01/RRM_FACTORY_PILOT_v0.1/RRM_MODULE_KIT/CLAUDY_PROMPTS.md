# <MODULE_ID> — Architect's Engineering Prompts

## P1 — Plan Mode

Read the front door and approved contract. Inspect the current baseline read-only. Reconcile accepted findings against actual code; identify hidden dependencies, conflicting requirements, unclear acceptance wording and evidence/tooling gaps. Return a bounded file/stage plan, checks and risks. No product changes. Await Director approval of this plan.

## P2 — Approved implementation stage <N>

Implement only <approved objectives and ledger/AC IDs> on <active branch> within <allowed surfaces>. Preserve <invariants>. Run <engineering checks> with <authorized environment>. Stop and report any scope/contract contradiction. Append exact changes, commands, outcomes and limitations to EXECUTION_LOG.md. Deliver evidence and a GIT REMINDER; do not perform mutating Git without Tony's authorization. Do not issue QA certification.

## P3 — Engineering completion handoff

Assemble QA_HANDOFF.md with the approved acceptance specification, execution log, source dispositions, candidate identity, diff, checks, fixtures, known limitations and repo-local governing QA instructions. Treat completion statements as claims for independent verification. Hand control back to the Director for QA branch transition.

## P4 — QA-directed repair <round>

On <qa/module>, implement only the approved ruling package <reference>. Findings/ACs: <...>. Allowed files: <...>. Explicitly forbidden changes: <...>. Run <engineering regression>. Append evidence; do not change frozen AC wording. Director commits; Cody independently re-pins and retests. No self-certification or unapproved additional repairs.

## P5 — Final closeout

RESERVED FOR THE PROJECT ARCHITECT AFTER SOL CERTIFICATION AND QA CLEANUP. The Architect supplies exact record/document changes, certified implementation identity, durable evidence commits, prohibited product changes and Director Git instructions. This placeholder is not permission to close out early.
