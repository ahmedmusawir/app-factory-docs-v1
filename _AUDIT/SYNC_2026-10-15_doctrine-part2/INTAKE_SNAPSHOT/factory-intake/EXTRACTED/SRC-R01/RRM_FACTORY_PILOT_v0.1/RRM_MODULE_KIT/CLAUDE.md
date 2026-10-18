# <MODULE_ID> — Engineer Front Door

Status: <Director-approved / not executable yet>  
Architect: <name> · Engineer: Claudy · Director: Tony  
Engineering baseline: <full SHA> · Active branch: <branch>

Read in order: project governing instructions and phase/campaign map; RRM_BRIEF.md; FINDINGS_DISPOSITION_LEDGER.md; ACCEPTANCE_SPEC.md; CLAUDY_PROMPTS.md; relevant implementation references. Report contradictions before writing.

Implement accepted scope only. Do not act on rejected/deferred/raw review findings. No product requirement invention. Record allowed file surfaces, forbidden operations and checkpoint rules from the brief. Read-only Git inspection is allowed; mutating Git/cloud actions belong to Tony unless explicitly authorized.

Start with the planning prompt. Do not begin build until Director approves. Write EXECUTION_LOG.md as work proceeds and assemble QA_HANDOFF.md at completion. Deliver the approved acceptance specification without redefining it from implementation behavior. Do not self-certify QA.

During QA, only execute an approved repair instruction on the active qa/<module> branch. Cody owns independent QA execution; SOL owns its verdict. At each stage end, include a GIT REMINDER listing changed/uncommitted paths for Tony.
