# APP FACTORY SKILLS PLAYBOOK

> **Authoritative doctrine for skill authoring in the Stark Industries App Factory.**
> Read by Generals (DevOps, Architects, Designers). Not read by Engineer agents (Claude Code, Windsurf, Cursor) — those are skill consumers, not authors.
> This is an imperative manual. Rules are non-negotiable unless explicitly overridden by the operator with acknowledgment.

---

## Table of Contents

1. [What Is A Skill](#1-what-is-a-skill)
2. [The Two Types Of Skills](#2-the-two-types-of-skills)
3. [Stark Skill Architecture](#3-stark-skill-architecture)
4. [The CLAUDE.md Contract](#4-the-claudemd-contract)
5. [The SKILL.md Contract](#5-the-skillmd-contract)
6. [Single Skills vs Family Skills](#6-single-skills-vs-family-skills)
7. [Folder Layout Standards](#7-folder-layout-standards)
8. [Anthropic Skills v2 Format Reference](#8-anthropic-skills-v2-format-reference)
9. [Activation Flow](#9-activation-flow)
10. [Plan Mode And Operator Override](#10-plan-mode-and-operator-override)
11. [Evidence Discipline](#11-evidence-discipline)
12. [Evolution Principle](#12-evolution-principle)
13. [Anti-Patterns Named](#13-anti-patterns-named)
14. [Two Structural Exemplars](#14-two-structural-exemplars)
15. [Authoring A New Skill — Step By Step](#15-authoring-a-new-skill--step-by-step)
16. [Agent Skills (The Other Type)](#16-agent-skills-the-other-type)
17. [Version History](#17-version-history)

---

## 1. What Is A Skill

A skill is a **structured, repeatable instruction set** that an AI agent loads into context to perform a specific job correctly without the operator having to re-explain the job from scratch every session.

A skill is NOT:

- A single prompt
- A magic activation phrase the operator must memorize
- A loose collection of markdown files
- A reference document an agent reads "if it feels relevant"

A skill IS:

- A folder structure with mandatory entry points
- A doctrine the agent loads automatically when activated
- A repeatable methodology the agent follows step by step
- A force-multiplier — built once, used hundreds of times

The fundamental contract of a skill: **the operator should never have to remember anything except where the skill folder lives.** Pointing the agent at the folder must be sufficient activation.

If your skill requires the operator to remember and provide a "magic prompt" with pre-baked answers, **you have not built a skill. You have built a checklist with extra steps.**

---

## 2. The Two Types Of Skills

The App Factory recognizes exactly two skill types. Every skill must declare which type it is. Mixing types within a single skill is forbidden.

### Type 1: Stark Skills

A Stark Skill is a **guidance skill**. The agent uses it to walk the operator through a task the operator wants to perform themselves. The agent guides; the operator executes.

Examples of Stark Skills:

- **Cloud Run deployment** — agent generates files, walks operator through running them
- **Supabase migration** — agent guides operator through schema replay, verification, env swap
- **RBAC project setup** — agent walks operator through Supabase project creation and wiring
- **Repo creation from template** — agent guides operator through `gh repo create`, clone, install
- **Brain drain extraction** — agent extracts intelligence from a repo into structured docs (semi-execution; the agent writes the extraction docs but never modifies the source repo)

Stark Skills exist because Tony Stark refuses to be a Vibe Coder. He runs commands himself. He pastes results back. He stays in the driver's seat. The skill exists to make sure he runs the RIGHT commands in the RIGHT order with the RIGHT verification, not to remove him from the loop.

### Type 2: Agent Skills

An Agent Skill is a **capability skill**. The agent uses it to do something itself, without operator involvement in execution. The skill teaches the agent how to perform a task well.

Examples of Agent Skills:

- **Session memory file writer** — when working in the ADK Harness, the agent writes session memory files in a specific format; the skill defines that format and the discipline
- **UI/UX specialization** — a skill that elevates a generalist Claude Code agent into a specialist designer for component work
- **Stitch prompting** — a skill for the Designer Agent that codifies how to prompt Stitch effectively, with chunking rules and iteration patterns

Agent Skills exist because some tasks are agent-side work, not operator-side work. The operator delegates the task; the agent performs it correctly because the skill teaches it the discipline.

### How To Tell Which Type You're Authoring

Ask one question: **Does the operator paste commands and observe results, or does the agent execute the task and report back?**

- Operator pastes commands → Stark Skill
- Agent executes the task → Agent Skill

If a skill blurs this line, split it. Don't author a skill that's half-Stark, half-Agent. The activation pattern, the doctrine, and the anti-patterns are different for each type.

### Common Ground

Both types use the **Anthropic Skills v2 format** for SKILL.md (YAML frontmatter, structured body). Both types are skill folders with mandatory entry points.

The differences appear in the CLAUDE.md doctrine:

- Stark Skill CLAUDE.md emphasizes operator interaction, verification gates, command pasting, "stop and wait" behavior
- Agent Skill CLAUDE.md emphasizes the agent's internal discipline, output format, when to ask the operator vs proceed

---

## 3. Stark Skill Architecture

Every Stark Skill — single or family — has the same architecture at its core.

### The Two-File Core

Every Stark Skill has two file types that MUST be present:

1. **CLAUDE.md** — the always-on doctrine, activation point, manager of the skill
2. **SKILL.md** — the v2-formatted methodology, the actual skill content

These files have distinct roles. They are NOT interchangeable. They are NOT optional.

### CLAUDE.md Is The Manager

CLAUDE.md is the file the agent reads FIRST when activated. It contains:

- Mission brief — what this skill is for, who runs it, when to use it
- Folder tree — what the skill folder contains and what each piece is for
- Reading order — for family skills, which skill runs first, which runs second
- Doctrine — rules the agent must follow throughout the skill's execution (Plan Mode, evidence labels, operator override, evolution principle)
- Activation behavior — exactly what the agent does when the operator says "go read this folder"

CLAUDE.md is what saves the operator from writing a magic prompt. The operator says "go read `<path>`," and CLAUDE.md takes it from there.

### SKILL.md Is The Methodology

SKILL.md is what the agent reads SECOND, after CLAUDE.md tells it to. It contains:

- Anthropic v2 YAML frontmatter (name, description, allowed-tools)
- Phase-by-phase methodology
- Verification gates between phases
- Examples of correct usage
- "When you're done" criteria

SKILL.md does NOT need to repeat the folder structure (CLAUDE.md already covered that). SKILL.md does NOT need to repeat the mission (CLAUDE.md already covered that). SKILL.md focuses on **what to do, step by step.**

### Both Files Are Mandatory

Every skill folder that contains a SKILL.md must have a CLAUDE.md as its sibling or as the family-level CLAUDE.md if the skill belongs to a family.

There is no such thing as a skill with only SKILL.md.
There is no such thing as a skill with only CLAUDE.md.
Both must exist. Both have distinct roles.

---

## 4. The CLAUDE.md Contract

Every CLAUDE.md must include the following sections, in this order. Section names may be styled differently (with emoji, with prefixes) but the content must be present.

### Required Sections

**Section 1: Identity / Mission**

States who the agent is operating as when this skill is loaded, and what the mission is. Two to four paragraphs maximum. Imperative tone.

Example phrasing: *"You are operating as the Cloud Deployment Agent for the Stark Industries App Factory. Your mission: walk the operator through deploying a Next.js application to Google Cloud Run with verified IAM, secret mapping, and SSL provisioning."*

**Section 2: Activation Behavior**

Exactly what the agent does when activated. This is the contract that replaces the magic prompt. Must be explicit and ordered.

Required content:
- What the agent reads first
- What the agent does to discover environment context (pwd, ls, git remote -v, etc.)
- What questions the agent asks (only what cannot be inferred)
- What the agent presents back to the operator before proceeding (the Plan Mode handoff)

**Section 3: Folder Tree**

A complete tree of the skill folder, with one-line annotations on what each file or subfolder contains. The agent uses this to know what's available without re-scanning every session.

For family skills, this tree includes the family-level CLAUDE.md and all child skill folders.

**Section 4: Doctrine — Always In Effect**

The non-negotiable rules. Stated in imperative voice. Each rule earns 2-3 sentences of rationale.

Standard doctrine for Stark Skills includes:
- **Plan Mode first** — read environment, present plan, await approval before action
- **Evidence discipline** — every claim labeled appropriately (where applicable to the task)
- **Operator override** — surface conflicts, never silently override
- **Read-only boundary** — don't modify what isn't yours to modify
- **No invention** — if a thing isn't found, say "NOT FOUND," never guess

Standard doctrine for Agent Skills includes:
- **Output format discipline** — match the format the skill specifies
- **Verification before claim** — test before declaring done
- **Operator interaction rules** — when to ask, when to proceed

**Section 5: Reading Order**

For single skills, this is a short list: read SKILL.md next, then references as needed.

For family skills, this is the playbook for which child skill to engage in which order, and what to do between them. The CLAUDE.md is responsible for orchestration — child skills do not orchestrate each other.

**Section 6: Operator Override Protocol**

What the agent does when the operator gives an instruction that conflicts with doctrine. Standard pattern:

> If the operator gives an instruction that conflicts with doctrine in this file, surface the conflict and ask before proceeding. Do not silently override. The operator's authority is supreme, but doctrine drift without acknowledgment is how systems decay.
>
> Example:
> Operator: "Skip Plan Mode this time."
> You: "Plan Mode is core doctrine — it prevents [specific failure mode]. If you want me to skip it, confirm explicitly. Otherwise I'll proceed with Plan Mode as standard."

**Section 7: Version History**

A table at the bottom of every CLAUDE.md tracking changes. No silent edits. Every meaningful change appends a row.

| Version | Date | Change |
|---------|------|--------|
| 1.0 | YYYY-MM-DD | Initial doctrine. |

### CLAUDE.md Length Guidance

A CLAUDE.md should be **3,000 to 8,000 words**. Long enough to encode all required doctrine. Short enough to read in one pass. If yours is shorter, doctrine is missing. If yours is longer, methodology has leaked in (move it to SKILL.md or a reference).

---

## 5. The SKILL.md Contract

SKILL.md follows the Anthropic Skills v2 format strictly. The format is documented in Section 8 of this playbook.

### Required Frontmatter

```yaml
---
name: <skill-name-in-kebab-case>
description: >
  <2-4 sentences describing what the skill does and when to use it.
  Include trigger phrases the agent should recognize.>
allowed-tools: [<list of tool names>]
---
```

The `name` field must match the skill folder name exactly.
The `description` field must be specific enough that an agent loading the skill description from a registry can decide whether this is the skill it needs.
The `allowed-tools` field declares which Claude tools the skill is permitted to use.

### Required Body Sections

After the frontmatter, the body must include:

**Role Definition**

One paragraph stating who the agent is operating as when this skill engages. This may overlap with CLAUDE.md's Identity section but is restated here for self-containment in case CLAUDE.md is somehow not loaded.

**Phase Structure**

The skill is broken into numbered phases. Each phase has:
- A clear goal stated at the top
- Step-by-step procedures
- A verification gate ("Stop Gate") at the end
- Output of the phase explicitly listed

Phases are sequential. The agent does not skip phases unless the operator explicitly authorizes it (which then triggers the Operator Override Protocol from CLAUDE.md).

**Examples**

At least one worked example showing the skill in action. For Stark Skills, this means showing the agent's response to operator inputs, including the "stop and wait" moments. For Agent Skills, this means showing input → output examples.

**Anti-Patterns (Skill-Specific)**

Patterns specific to this skill that authors and the agent must avoid. General anti-patterns belong in this Playbook (Section 13). Skill-specific ones belong in the SKILL.md.

**When You're Done**

Explicit criteria for declaring the skill complete. Includes what the agent presents to the operator at the end (summary, next steps, artifact paths).

### SKILL.md Length Guidance

A SKILL.md should be **under 500 lines** per Anthropic's v2 best practice. Use references/ for deep content. Use decision-trees/ for decision logic. Keep SKILL.md focused on the methodology spine.

If your SKILL.md exceeds 500 lines, you have over-stuffed it. Move content to references.

---

## 6. Single Skills vs Family Skills

Two valid Stark Skill structures exist. Authors must choose deliberately.

### Single Skill

A single skill performs one cohesive task. Its folder contains one CLAUDE.md and one SKILL.md at the root.

Use a single skill when:
- The task is one continuous procedure
- Phases share context that doesn't transfer cleanly between separate skill activations
- Splitting the task would require the operator to remember to invoke a second skill at the right moment

Examples that should be single skills:
- Supabase Migration Skill — one continuous procedure from source dump to target verification
- RBAC Setup Skill — one continuous procedure from project creation to working logged-in app
- Brain Drain — one continuous extraction with optional pathway choice at start

### Family Skill

A family skill is a collection of related skills under one CLAUDE.md. The family CLAUDE.md orchestrates which child skill runs when. Each child skill has its own folder with its own SKILL.md (no per-child CLAUDE.md).

Use a family skill when:
- The task naturally splits into discrete phases the operator may want to invoke separately
- Different phases have different activation contexts (e.g., "generate files" vs "execute deployment with files")
- The operator may need to re-run only one phase without re-running the others

Examples that should be family skills:
- Cloud Deployment Skills — `generate` (produces files) and `execute` (runs them) are distinct activations; operator may regenerate without redeploying or vice versa
- A potential future Brain Drain expansion that splits "extraction" from "synthesis" into two skills under one family CLAUDE.md

### The Single-CLAUDE.md Rule

Whether single or family, **there is exactly one CLAUDE.md per skill or skill family.**

For single skills, CLAUDE.md sits at the skill root.
For family skills, CLAUDE.md sits at the family root, above all child skills.

Child skills in a family DO NOT have their own CLAUDE.md. They have only SKILL.md and references. The family's CLAUDE.md provides doctrine to all children.

This rule prevents doctrine drift across child skills. One CLAUDE.md, one source of truth.

---

## 7. Folder Layout Standards

The folder structure is mandatory for Stark Skills.

### Single Skill Layout

```
<skill-name>/
├── CLAUDE.md                     ← always-on doctrine, activation point
├── SKILL.md                      ← v2-formatted methodology
├── README.md                     ← human-facing description (optional)
├── changelog.md                  ← version history (optional, version table in CLAUDE.md is mandatory)
├── workflow/                     ← phase-by-phase procedures (referenced from SKILL.md)
│   ├── 00-<phase-name>.md
│   ├── 01-<phase-name>.md
│   └── ...
├── references/                   ← deep content the SKILL.md links to
│   ├── <topic>.md
│   └── ANTI_PATTERNS.md
├── decision-trees/               ← decision logic for ambiguous moments
│   └── <decision-topic>.md
├── templates/                    ← templates the skill produces or uses
│   └── <template-name>.md
└── examples/                     ← real successful runs
    └── <run-name>-<date>/
```

Mandatory: `CLAUDE.md`, `SKILL.md`.
Optional: everything else, used as needed.

### Family Skill Layout

```
<FAMILY_NAME>_SKILLS/
├── CLAUDE.md                     ← family-level doctrine, ONE FILE for the whole family
├── _shared/                      ← OPTIONAL: shared references both children use
│   └── <shared-template>.md
├── <child-skill-1>/
│   ├── SKILL.md                  ← child's methodology
│   ├── references/
│   ├── decision-trees/
│   └── templates/
└── <child-skill-2>/
    ├── SKILL.md
    ├── references/
    └── templates/
```

Mandatory: family-level `CLAUDE.md`, one `SKILL.md` per child skill folder.
Optional: `_shared/` folder when children genuinely share content. Do not create empty `_shared/` folders. Do not duplicate content into `_shared/` if only one child uses it — keep it inside that child's folder.

The `_shared/` folder is a flexibility provision. Brain Drain uses `mission_templates/` as a similar archive pattern. Authors decide based on the skill's actual needs.

### The Folder Mistake That Must Not Repeat

When zipping a skill for distribution, **do not nest the skill folder inside an extra `/skill/` wrapper**. The named folder is the skill. Its contents go at root.

Wrong:
```
my-skill-name.zip
└── skill/
    ├── CLAUDE.md
    └── SKILL.md
```

Right:
```
my-skill-name.zip
└── my-skill-name/
    ├── CLAUDE.md
    └── SKILL.md
```

This was a mistake made in early skills authored by this General. It's documented in Section 13 (Anti-Patterns).

### File Naming Conventions

- Skill folder names: kebab-case (`github-repo-from-starter-template`)
- Family folder names: SHOUTING_SNAKE (`CLOUD_DEPLOYMENT_SKILLS`, `EXTRACTION_SKILLS`)
- Workflow files: zero-padded numeric prefix (`00-pre-flight.md`, `01-target-creation.md`)
- Reference files: descriptive names, no prefix (`ANTI_PATTERNS.md`, `DOC_TEMPLATE.md`)
- Decision trees: prefix with the decision topic (`region-selection.md`, `cli-vs-web-ui.md`)

The reasoning: family folders are LOUD because they're the umbrella; child skills are kebab because they're invoked by name; workflow files are numbered because they're sequential; references are named because they're random-access.

---

## 8. Anthropic Skills v2 Format Reference

The SKILL.md file must follow the Anthropic Skills v2 format. This section is an inline excerpt covering what skill authors need to know. The full official spec is referenced at the end.

### YAML Frontmatter

Every SKILL.md begins with a YAML frontmatter block delimited by `---` lines.

```yaml
---
name: skill-name-in-kebab-case
description: >
  Multi-line description that explains what the skill does, when it
  should be used, and what trigger phrases activate it. Should be
  specific enough that an agent reading a registry of skill descriptions
  can decide if this is the right skill for the user's request.
allowed-tools: [bash, view, str_replace, create_file]
---
```

#### `name` field

- Kebab-case
- Must match the skill folder name exactly
- Used by skill registries and discovery systems

#### `description` field

- Multi-line allowed (use `>` for folded scalar)
- 2-4 sentences typical, can be longer if the skill is complex
- Must include trigger phrases or topic keywords the agent should recognize
- Should distinguish this skill from neighboring skills (e.g., specify what it does NOT do)

Example of a good description:

```yaml
description: >
  Walk through deploying a Next.js app to Cloud Run step by step.
  Triggers on phrases like "deploy now", "execute deployment", "let's
  ship it", "push to cloud run". This is Part 2 of a 2-skill family —
  Part 1 is `next-deploy-generate` which produces deployment files.
  This skill assumes deployment files exist; if they don't, redirect
  to the generate skill first.
```

#### `allowed-tools` field

- List of Claude tool names the skill is permitted to use
- Common values: `bash`, `view`, `str_replace`, `create_file`, `list_files`, `read_file`
- Restrict to what the skill actually needs — overly permissive `allowed-tools` weakens auditability

### Body Format

After the frontmatter, the body is markdown. Anthropic's v2 best practices:

- **Under 500 lines total** — use references for overflow content
- **Hierarchical headings** — H1 for the skill name, H2 for major phases or sections, H3 for subsections
- **Imperative voice** — "Read the file," not "You should read the file"
- **Concrete examples** — at least one worked example showing the skill in action
- **Stop gates** — explicit "stop and wait" moments where the agent must pause for operator input

### Progressive Disclosure

Anthropic's v2 design encourages progressive disclosure. The SKILL.md is the lightweight entry. Heavy content lives in:

- `references/` — deep documentation the skill links to as needed
- `templates/` — reusable structures the skill produces or fills in
- `examples/` — worked examples too long to embed in SKILL.md

The agent loads SKILL.md every time. The agent loads references/templates/examples ONLY when the methodology calls for them.

### Reference

Full official spec: see Anthropic's documentation on Skills (the agent reading this Playbook should consult Anthropic's official skill documentation when authoring a v2 SKILL.md to ensure compliance with the latest format).

---

## 9. Activation Flow

The activation flow is the operator's experience of using a skill. It must be the same for every Stark Skill in the App Factory.

### The Operator's One Job

The operator's only job at activation is: **point the agent at the skill folder.**

Acceptable activation phrases:

- "Go read `<path>` and follow it."
- "Use the skill at `<path>`."
- "Activate `<skill-name>`."
- "Read `<path>/CLAUDE.md` and proceed."

The operator does NOT provide:
- Pre-baked answers to questions the skill should ask
- Project-specific configuration values
- Magic prompts assembled from prior sessions

If the skill requires the operator to provide more than a path, the skill is broken.

### The Agent's Activation Sequence

When activated, the agent performs these actions in this order:

**Step 1: Read CLAUDE.md**

The agent reads the CLAUDE.md at the skill root (single skill) or family root (family skill). This is non-negotiable. CLAUDE.md is the entry point.

**Step 2: Inspect Environment**

The agent runs basic environment discovery to understand context:
- `pwd` — where am I?
- `ls` — what's around me?
- `git remote -v` (if applicable) — what repo is this?
- `cat .env.local` (read-only, if relevant) — what's already configured?

The exact discovery steps depend on the skill type and are specified in CLAUDE.md.

**Step 3: Determine What's Already Known**

The agent uses environment discovery to determine what it already knows. Only what cannot be inferred from environment becomes a question for the operator.

For a deployment skill, the agent might discover:
- The project's name (from package.json)
- The default branch (from git)
- The Node version (from .nvmrc or package.json engines)

The agent does NOT ask the operator for these. They're discoverable.

**Step 4: Present Plan**

The agent presents a Plan Mode summary to the operator:
- What it found in the environment
- What it still needs to know (specific questions)
- What it intends to do once it has the answers

The agent ends the plan with explicit "Awaiting your APPROVED before proceeding" (or equivalent).

**Step 5: Wait For Approval**

The agent does NOT proceed until the operator says APPROVED (or equivalent confirmation). Operator may answer questions or push back on the plan. Agent updates plan, re-presents, awaits approval.

**Step 6: Execute Methodology**

After approval, the agent reads SKILL.md (if not already loaded) and executes the methodology phase by phase, following the verification gates.

### Why This Flow Matters

The flow exists to prevent two failure modes:

**Failure mode 1: Magic prompt dependency.** If the agent expects pre-loaded context, the operator must remember and provide that context every session. This defeats the skill's purpose.

**Failure mode 2: Blind execution.** If the agent skips environment discovery and Plan Mode, it may make wrong assumptions, ask questions whose answers were already on disk, or proceed with stale context.

Both modes turn a skill back into a checklist. Neither is acceptable.

---

## 10. Plan Mode And Operator Override

Plan Mode is the formal "look before you leap" discipline. Every Stark Skill enforces it. Authors must encode it in CLAUDE.md.

### What Plan Mode Requires

Before producing any output, modifying any file, or running any command beyond environment discovery, the agent must:

1. Scan the relevant environment (file tree, key files, configuration)
2. Read what's already on disk that's pertinent to the task
3. Present a structured Plan to the operator
4. Wait for explicit approval

The Plan must include:

- What the agent observed (environment summary)
- What the agent intends to do (high-level steps)
- What the agent does not know and needs the operator to clarify (specific questions, not blind question dumps)
- Risks or open questions worth flagging
- An explicit "Awaiting APPROVED" closing line

### What "APPROVED" Means

The operator must explicitly confirm. Acceptable confirmations: "APPROVED", "Approved", "Go", "Proceed", "Yes, go ahead". Tacit silence is NOT approval.

If the operator gives partial approval ("Approved for Phase 1, hold on Phase 2"), the agent proceeds with Phase 1 and pauses before Phase 2.

If the operator pushes back on the plan, the agent revises and re-presents. No execution until APPROVED is on the table.

### Operator Override Protocol

The operator may at any point instruct the agent to skip Plan Mode, skip a verification gate, skip a phase, or proceed differently than doctrine prescribes.

The agent's response is mandatory:

1. Acknowledge the override
2. Name the doctrine being overridden
3. State the failure mode the doctrine prevents
4. Ask for explicit confirmation

Example:

> Operator: "Skip the IAM verification this time, just deploy."
>
> Agent: "IAM verification is core doctrine — it prevents the most common Cloud Run failure mode (build succeeds, deploy succeeds, runtime errors on missing secret access). Skipping it means we may deploy a service that 500s on first request. Confirm explicitly that you want to skip, otherwise I'll run the verification as standard."

The agent does NOT silently override. The agent does NOT obey instructions that conflict with doctrine without surfacing the conflict.

The operator's authority is supreme — once they confirm the override, the agent proceeds. But the override is logged in the agent's response, so the operator owns the decision consciously.

### Why This Matters

Doctrine drift is silent system decay. If an agent quietly skips Plan Mode "just this once" because the operator seemed in a hurry, the next session's agent will skip it more readily, and the operator will start to expect skipping. Six sessions later, no one runs Plan Mode anymore, and the skill's value collapses.

Surfacing the override every time keeps the doctrine alive. The operator overrides consciously when warranted; the agent never overrides silently.

---

## 11. Evidence Discipline

Evidence discipline is the rule that **every claim the agent makes must be tagged with how the agent knows it.**

This is most critical for Brain Drain (extraction work) but applies to all skills in some form.

### The Five Labels

| Label | Meaning |
|-------|---------|
| **EVIDENCE** | Directly found in a specific file or output. Cite the source. |
| **INFERENCE** | Reasonable conclusion drawn from observed structure or patterns. State the basis. |
| **CLAIM** | Documentation or operator says it; not independently verified. State who claimed it. |
| **GAP** | Expected component not found. State what was expected and where it was searched for. |
| **QUESTION** | Needs operator clarification. Phrase as an explicit question. |

### Where This Applies

For Brain Drain (extraction): every line of every extraction document carries one of these labels. No untagged claims allowed.

For deployment skills: when the agent reports IAM state, secret status, or verification results, it should distinguish what it directly saw (`gcloud` output = EVIDENCE) from what it inferred (`secret exists, but I haven't verified the runtime SA can read it` = INFERENCE) from what it's asking (`do you want public or domain-restricted invoker?` = QUESTION).

For migration skills: when the agent reports schema state, fingerprint counts, or RLS policy presence, it labels what it directly queried versus what it assumed.

### Why It Matters

Without evidence discipline, the agent's reports become unfalsifiable. The operator can't tell what the agent verified versus what the agent guessed. Decisions made on guessed-as-fact information cause the worst kinds of failures — the kind where you don't know to verify because you didn't know it was unverified.

For deep reference on evidence labels and edge cases, skill authors should consult Brain Drain's `references/EVIDENCE_TAGGING.md`.

---

## 12. Evolution Principle

The Evolution Principle: **doctrine evolves, but never silently.**

### What This Means

Every CLAUDE.md and SKILL.md carries a Version History table at the bottom:

```markdown
## Version History

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-05-02 | Initial doctrine. |
| 1.1 | 2026-05-15 | Added Section 8: Anthropic v2 format reference. |
| 1.2 | 2026-06-05 | Renamed Phase 3 from "Deploy" to "Build and Deploy" for clarity. |
```

When an author makes a meaningful change to doctrine or methodology, they MUST append a row. No silent edits.

### What Counts As "Meaningful"

A meaningful change is one that affects:
- Activation behavior
- Required sections
- Doctrine rules
- Phase structure
- Verification gates
- Output format

A typo fix or a clarification of an existing rule is NOT a meaningful change. Use editorial judgment, but err toward documenting.

### Why This Matters

Authors come and go. Sessions reset. Future-you reading a CLAUDE.md from 8 months ago should be able to see how the doctrine evolved. Silent edits make doctrine drift invisible — by the time someone notices, the original intent is lost.

The Version History also serves as a forensic tool. When a skill starts behaving differently than expected, the version history reveals what changed and when.

### What Does NOT Need Versioning

- Examples folder contents (point-in-time records of past runs)
- Reference files that summarize external information (e.g., Anthropic's spec) — those are mirrored, not authored
- Templates that are operator-specific (they're filled in per-use, not authored doctrine)

The CLAUDE.md and SKILL.md are doctrine. Everything else is supporting material. Doctrine versions; supporting material does not need to.

---

## 13. Anti-Patterns Named

This section names specific failures observed in this General's authoring history. Future skills MUST avoid these. v2 versions of named skills MUST correct them.

### Anti-Pattern 1: Magic Prompt Activation

**Failure:** A skill that requires the operator to paste a multi-paragraph prompt with project-specific values pre-baked in order to activate. This means the operator must come to a General to generate the prompt every time.

**Where this appeared:** First version of `github-repo-from-starter-template-skill`, where activation required: *"Activate the GitHub Repo From Starter Template skill. Read this file first... Context for this run: Template repo: <X>, New repo name: <Y>, Owner: <Z>, Visibility: <V>..."*

**Correct pattern:** Activation is *"Go read `<path>/CLAUDE.md` and follow it."* The skill's CLAUDE.md handles environment discovery and Plan Mode to gather only what cannot be inferred.

### Anti-Pattern 2: Nested `/skill/` Folder Inside Skill Folder

**Failure:** When zipping a skill for distribution, wrapping the skill content in an extra `/skill/` folder inside the named skill folder.

**Where this appeared:** Both the Supabase Migration Skill v1 and the GitHub Repo Skill v1, where the zip extracted to:
```
github-repo-from-starter-template-skill/
└── skill/
    ├── CLAUDE.md
    └── SKILL.md
```

**Correct pattern:** The named folder IS the skill. Contents at root of that folder.
```
github-repo-from-starter-template-skill/
├── CLAUDE.md
└── SKILL.md
```

### Anti-Pattern 3: Family-Level CLAUDE.md As Navigation Only

**Failure:** A family CLAUDE.md that describes the folder contents but does not encode doctrine. The CLAUDE.md becomes a README, not a manager.

**Where this appeared:** First version of Cloud Deployment Skills `CLOUD_DEPLOYMENT_SKILLS/CLAUDE.md`. It described the two child skills, listed naming conventions, and explained file paths — but had no Gateway, no Plan Mode rules, no operator override protocol, no doctrine. It was navigation, not management.

**Correct pattern:** Family CLAUDE.md is always-on doctrine. It carries the Gateway (or activation behavior), Plan Mode, operator override, evidence discipline, evolution principle. Navigation is a section within it, not the entirety of it.

Brain Drain's `EXTRACTION_SKILLS/CLAUDE.md` is the correct example — it has folder layout AND gateway AND doctrine AND operator override AND evolution principle.

### Anti-Pattern 4: Per-Skill CLAUDE.md In Family Skills

**Failure:** Inside a family skill, each child skill folder gets its own CLAUDE.md in addition to the family CLAUDE.md. This creates two sources of doctrine that drift apart.

**Where this appeared:** Considered (and almost authored) for the GitHub Repo Skill family before the single-CLAUDE.md rule was locked.

**Correct pattern:** Family CLAUDE.md only. Children have SKILL.md only. Doctrine inherits from family. No drift possible.

### Anti-Pattern 5: Single Skill With Only CLAUDE.md, No SKILL.md

**Failure:** A single skill folder containing CLAUDE.md but no SKILL.md, with the methodology embedded in CLAUDE.md.

**Where this appeared:** First version of Supabase Migration Skill. CLAUDE.md held both doctrine AND methodology. There was no SKILL.md. This violated the two-file core rule.

**Correct pattern:** Every skill (single or family child) has a SKILL.md with v2 frontmatter. Every skill (single) or skill family has a CLAUDE.md with doctrine. Both files always present. Distinct roles.

### Anti-Pattern 6: Blind Pre-Flight Question Dumps

**Failure:** A skill that opens with a list of 15-25 questions to the operator before doing any environment discovery. The agent asks questions whose answers are already on disk.

**Where this appeared:** First version of RBAC Project Setup Skill, which asked 19 pre-flight questions including ones discoverable from `package.json`, the local repo's `.env.local`, and `gh auth status`.

**Correct pattern:** Environment discovery first. The agent runs `pwd`, `ls`, `git remote -v`, reads relevant config files. Then it asks the operator ONLY for what cannot be inferred. Plan Mode then presents what was found and what's still needed before proceeding.

### Anti-Pattern 7: Methodology Bleeding Into CLAUDE.md

**Failure:** CLAUDE.md contains step-by-step procedures, command sequences, or phase-by-phase instructions. These belong in SKILL.md.

**Where this appeared:** Migration Skill v1's CLAUDE.md included partial workflow content because there was no SKILL.md to put it in.

**Correct pattern:** CLAUDE.md is doctrine and management. SKILL.md is methodology. If you find yourself writing "Step 1: Run command X" in CLAUDE.md, it belongs in SKILL.md.

### Anti-Pattern 8: Skill That Modifies Files Outside Its Scope

**Failure:** A skill that modifies files in the operator's repo or system without explicit permission, or that "fixes" things adjacent to its task.

**Where this appeared:** Not yet observed in this General's skills, but documented here preemptively because it's a common failure mode.

**Correct pattern:** The Read-Only Boundary. The skill modifies only what it has explicit authorization to modify, in the locations its doctrine declares. Brain Drain's rule: *"The target repo is read-only except for the `_EXTRACTIONS/` folder."* Every skill needs an analogous rule.

---

## 14. Two Structural Exemplars

Authors writing new skills should study these two exemplars before authoring. They demonstrate the patterns this Playbook codifies.

### Exemplar 1: Cloud Deployment Skills (Family Skill)

**Location in operator's setup:** `_SKILLS/CLOUD_DEPLOYMENT_SKILLS/`

**Structure:**

```
CLOUD_DEPLOYMENT_SKILLS/
├── CLAUDE.md                          ← family doctrine (UPGRADED from v1's navigation-only)
├── next-deploy-generate/
│   ├── SKILL.md                       ← v2-formatted file generator
│   └── references/
│       └── TEMPLATES.md
└── next-deploy-execute/
    └── SKILL.md                       ← v2-formatted deployment walkthrough
```

**Why it's the family-skill exemplar:**

- Two child skills under one family CLAUDE.md
- Children handle distinct phases (file generation vs deployment execution)
- Operator may invoke either child independently (regenerate without redeploying, redeploy without regenerating)
- Family CLAUDE.md orchestrates which child runs when
- Children have only SKILL.md, no per-child CLAUDE.md (single-CLAUDE.md rule)
- Demonstrates `references/` usage for content too large for SKILL.md (TEMPLATES.md holds canonical Dockerfile, cloudbuild.yaml, deploy.sh templates)

**v1 → v2 refactor required:** The current `CLOUD_DEPLOYMENT_SKILLS/CLAUDE.md` is navigation-only. v2 must be upgraded to always-on doctrine including Plan Mode, operator override, evolution principle. SKILL.md files in children must be reviewed for v2 frontmatter compliance and 500-line discipline.

### Exemplar 2: Supabase Migration Skill (Single Skill, Most Complex Structure)

**Location in operator's setup:** `_SKILLS/SUPABASE_MIGRATION_SKILL/` (or whichever exact name the v2 version takes)

**Structure (v2 target):**

```
supabase-migration-skill/
├── CLAUDE.md                          ← always-on doctrine
├── SKILL.md                           ← v2-formatted methodology spine (NEW IN v2)
├── README.md                          ← human-facing
├── workflow/
│   ├── 00-pre-flight.md
│   ├── 01-bootstrap-introspection.md
│   ├── 02-source-fingerprint.md
│   ├── 03-target-creation.md
│   ├── 04-schema-replay.md
│   ├── 05-target-fingerprint.md
│   ├── 06-env-swap.md
│   ├── 07-app-verification.md
│   └── 08-rollback-plan.md
├── references/
│   ├── BOOTSTRAP_INTROSPECTION_RPC.sql
│   ├── FINGERPRINT_QUERY.sql
│   ├── ANTI_PATTERNS.md
│   └── PRIVILEGE_BOUNDARIES.md
├── decision-trees/
│   ├── source-vs-target-divergence.md
│   ├── data-migration-yes-no.md
│   └── rollback-trigger-conditions.md
├── templates/
│   └── HIPAA_CONSIDERATIONS_TEMPLATE.md
└── examples/
    └── starkreads-migration-2026-05-04/
```

**Why it's the single-skill exemplar:**

- Demonstrates the most complex single-skill structure: workflow + references + decision-trees + templates + examples
- One continuous task that should not be split (migration is end-to-end, can't usefully be invoked in pieces)
- Shows progressive disclosure: SKILL.md is light, workflow phases hold detail, references hold deep content, decision trees hold ambiguity-resolution logic
- examples/ folder holds the proven StarkReads migration as a shape reference for future migrations

**v1 → v2 refactor required:** The current Migration Skill is missing SKILL.md (one of the named anti-patterns). v2 must add SKILL.md with v2 frontmatter, refactor CLAUDE.md to remove methodology that belongs in SKILL.md, and verify each workflow file is referenced from SKILL.md (not just present in the folder).

### What These Exemplars Teach

Read both before authoring:

- **Single-skill author** — model on the Migration Skill: CLAUDE.md doctrine, SKILL.md methodology with phase references to workflow/, supporting folders for references/decision-trees/templates/examples
- **Family-skill author** — model on Cloud Deployment Skills: family CLAUDE.md with orchestration rules, children with SKILL.md only, shared content (if any) in `_shared/` at family root

Both exemplars share the doctrine spine. The structural difference is single vs family. The doctrine difference is none — both follow the same Plan Mode, evidence discipline, operator override, evolution principle.

---

## 15. Authoring A New Skill — Step By Step

This is the procedure a General follows when authoring a new skill from scratch. Imperative.

### Step 1: Determine Skill Type

Ask: does the operator paste commands and observe results, or does the agent execute the task autonomously?

- Operator-driven → Stark Skill
- Agent-driven → Agent Skill

If unclear, ask the operator. If still unclear, default to Stark Skill (more common in this factory).

### Step 2: Determine Skill Shape

Ask: is this one continuous task, or does it naturally split into discrete phases the operator may want to invoke separately?

- Continuous → Single skill
- Naturally split → Family skill

If a skill has multiple phases but the operator always runs them in sequence and never independently, it's a single skill (with workflow phases internally), not a family.

### Step 3: Name The Skill

- Single skill: kebab-case folder name (`supabase-migration-skill`)
- Family skill: SHOUTING_SNAKE family name + kebab-case child names (`CLOUD_DEPLOYMENT_SKILLS/next-deploy-generate/`)

The skill name appears in:
- Folder name
- SKILL.md `name` frontmatter field
- CLAUDE.md identity section
- Activation phrase the operator uses

These must all match.

### Step 4: Set Up Folder Structure

For a single skill:

```
mkdir <skill-name>
cd <skill-name>
touch CLAUDE.md SKILL.md README.md
mkdir workflow references decision-trees templates examples
```

For a family skill:

```
mkdir <FAMILY_NAME>_SKILLS
cd <FAMILY_NAME>_SKILLS
touch CLAUDE.md
mkdir <child-skill-1> <child-skill-2>
cd <child-skill-1>
touch SKILL.md
mkdir references decision-trees templates
```

Optional folders may be deleted if not used. Mandatory: CLAUDE.md and SKILL.md.

### Step 5: Author CLAUDE.md

Write CLAUDE.md against the contract in Section 4:

1. Identity / Mission section
2. Activation Behavior section
3. Folder Tree section (referencing your actual folder structure)
4. Doctrine — Always In Effect section
5. Reading Order section
6. Operator Override Protocol section
7. Version History table

Use Brain Drain's CLAUDE.md as the reference structure. Keep doctrine universal; keep specifics in SKILL.md.

### Step 6: Author SKILL.md

Write SKILL.md against the contract in Section 5:

1. v2 YAML frontmatter (name, description, allowed-tools)
2. Role definition
3. Phase-by-phase methodology
4. At least one worked example
5. Anti-patterns specific to this skill
6. "When you're done" criteria
7. Version History table

Keep under 500 lines. Move overflow to `references/`. Keep examples concrete.

### Step 7: Author Supporting Content

Only as needed:

- Workflow files (`workflow/00-*.md`, etc.) for phase detail
- References (`references/*.md`) for deep content
- Decision trees (`decision-trees/*.md`) for ambiguity logic
- Templates (`templates/*.md`) for fillable structures
- Examples (`examples/<run-date>/`) populated after first successful use

Do not pre-create empty files. Add when the methodology calls for them.

### Step 8: Test The Skill

The skill is not complete until you can demonstrate that pointing an agent at the folder activates it correctly:

1. Open a fresh Claude session with no prior context
2. Tell the agent: "Go read `<path>/CLAUDE.md` and follow it."
3. Observe the agent's behavior:
   - Does it read CLAUDE.md first?
   - Does it run environment discovery before asking blind questions?
   - Does it present a Plan and await approval?
   - Does it execute the methodology correctly after approval?
   - Does it follow the operator override protocol if you push back?
4. If any step fails, revise the skill and retest

A skill that activates correctly with no operator legwork beyond pointing-at-the-folder is a skill ready to ship.

### Step 9: Distribute

When the skill is tested and ready:

1. Zip the skill folder (named folder at root of zip — no nested `/skill/` wrapper)
2. Place in operator's `_SKILLS/` folder structure (or wherever they keep skills)
3. Update any skill registry or index document
4. Operator drops into context, points agent at folder, skill activates

### Step 10: Capture First Run Artifacts

After the operator runs the skill the first time successfully:

1. Save artifacts to `examples/<run-name>-<date>/`
2. Update the skill's Version History if any refinements emerged
3. Note any edge cases discovered that should become documented anti-patterns or decision-tree entries

The skill improves with use. Every successful run is documentation material.

---

## 16. Agent Skills (The Other Type)

This Playbook focuses primarily on Stark Skills because that's the dominant type in the App Factory. Agent Skills follow most of the same rules, with these differences.

### What's The Same

- Two-file core (CLAUDE.md + SKILL.md, both mandatory)
- Anthropic Skills v2 format for SKILL.md
- Folder layout standards
- Evolution principle (version history mandatory)
- No nested `/skill/` folder when zipping
- Activation flow starts at CLAUDE.md

### What's Different

#### Activation Behavior

Stark Skill activation is operator-initiated: "Go read this folder and guide me."

Agent Skill activation may be:
- **Operator-initiated** — "Use the session-memory skill to write this session's summary"
- **Auto-loaded** — the skill is in the agent's persistent context (e.g., always loaded for a specific role)
- **Triggered** — the agent itself decides to load the skill based on the task

CLAUDE.md must clarify which activation mode applies.

#### Plan Mode

Stark Skills enforce explicit Plan Mode with operator approval before action.

Agent Skills may compress this. For example, the session memory skill doesn't need to ask the operator "do you approve me writing the session summary?" — that's the task. The agent does it.

But Plan Mode discipline still applies internally: the agent must scan the relevant context, determine what's needed, and produce output that meets the skill's criteria. Plan Mode just becomes invisible to the operator.

#### Operator Override

For Agent Skills, the operator override protocol applies when the operator interrupts the agent's autonomous task. Less common, but doctrine still applies.

#### Evidence Discipline

Agent Skills that produce reports (extraction work, analysis, documentation) must apply evidence discipline. Agent Skills that perform actions (write files, format text) have less use for evidence labels but still need to verify outcomes.

### Agent Skill Examples

**Session Memory File Writer (for ADK Harness)**

The agent writes session memory files in a specific format the ADK Harness expects. The skill defines:
- File naming convention
- Required fields (date, agent role, key decisions, follow-ups)
- Tone and length guidance
- Where the file is saved

Activation may be auto-loaded when the agent is operating in an ADK Harness context.

**UI/UX Specialization (for Designer Agents)**

A skill that elevates a generalist Claude Code agent into a specialist designer. The skill teaches:
- Design principles for specific use cases
- Common patterns to apply
- Anti-patterns to avoid
- When to push back on operator requests that violate good design

Activation may be operator-initiated when entering design work.

**Stitch Prompting Discipline (for Designer Agents)**

A skill for prompting Stitch (or similar UI generation tools) effectively. Defines:
- Chunking rules (how to break complex UIs into prompts Stitch can handle)
- Iteration patterns (when to refine vs restart)
- Output format expectations
- Quality gates before showing operator

Activation triggered when the agent is asked to prompt Stitch for a UI.

### Authoring An Agent Skill

The procedure is the same as Section 15, with these adjustments:

- Step 1: Type is Agent Skill (operator delegates, agent executes)
- Step 5 (CLAUDE.md): Activation Behavior section emphasizes auto-load or trigger conditions, not operator-initiated activation phrases
- Step 5 (CLAUDE.md): Operator Override section is shorter; less operator interaction during execution
- Step 6 (SKILL.md): Examples show input → output, not operator-agent dialogue
- Step 8 (Testing): Test by giving the agent a task and observing whether it loads the skill correctly and produces correct output

The fundamentals — two-file core, v2 format, folder layout, evolution principle — are identical.

---

## 17. Version History

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-05-05 | Initial Playbook. Defines Stark Skills and Agent Skills. Establishes two-file core (CLAUDE.md + SKILL.md). Mandates Anthropic Skills v2 format for SKILL.md. Specifies single skill and family skill structures. Names eight anti-patterns from prior authoring history. Identifies Cloud Deployment Skills (family) and Supabase Migration Skill (single, most complex) as structural exemplars. Includes inline excerpt of v2 format with reference to Anthropic's official spec. Codifies activation flow, Plan Mode, operator override, evidence discipline, evolution principle. Audience: Generals (DevOps, Architects, Designers). |

---

## Closing Doctrine

Every skill in the App Factory exists for one reason: **to make the operator's repeated tasks fast, correct, and stress-free without him having to remember anything except where the skill folder lives.**

If a skill requires the operator to remember more than that — if it requires a magic prompt, if it asks blind questions whose answers are on disk, if it skips Plan Mode, if it modifies files it shouldn't — the skill has failed its purpose.

Authors of new skills: study Brain Drain. Study the v2 versions of Cloud Deployment Skills and the Supabase Migration Skill once they exist. Apply the rules in this Playbook. Test your skill against the activation contract: drop in folder, point at folder, observe correct behavior with zero operator preparation.

Skills are force multipliers. A bad skill is a force divider. The difference is whether the doctrine in this Playbook was followed.

> *"Build the skill once. Use it forever. The operator's only job is to remember where it lives."*

---

🛡️ *End of Playbook v1.0.*
