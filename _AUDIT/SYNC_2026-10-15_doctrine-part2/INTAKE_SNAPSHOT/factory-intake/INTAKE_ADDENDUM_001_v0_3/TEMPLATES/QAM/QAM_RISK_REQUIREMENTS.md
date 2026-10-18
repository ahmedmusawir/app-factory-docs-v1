# QAM_RISK_REQUIREMENTS — `<<MODULE_ID>>`

> DRAFT v0.3 — QA LEAD ACCEPTED WITH EXACT AMENDMENTS (Fable, 2026-10-14); AMENDMENTS APPLIED AND ENGINEER-VERIFIED; ARCHITECT AMENDMENT VERIFICATION PENDING. Template `QAM/QAM_RISK_REQUIREMENTS.md` v0.3-draft (2026-10-14), from `QAM_PLAYBOOK_v1_0.md` §5, §7 ("QA Lead standing requirements are reusable"), §12 and §16. **Owners: §1 QA Lead (standing, reusable across modules; the QA Lead need not review every engineering packet before work begins); §2 Architect (module-specific risks, clearly attributed); §3 QA Executor (its own reading of both, recorded in Q1; an Executor-owned section inside this file, per `QAM_ENTRY.md` §3).** Nothing here is a test plan; the plan is drafted independently by the Executor from this file, the contract, the source, recon and the Engineer's claims.

## 1. QA Lead standing requirements (reusable; version QAM-SR v1.0; adopted by: QA Lead (Fable), 2026-10-14)

> **STANDING REQUIREMENTS ADOPTION RECORD.**
>
> | Field | Value |
> |---|---|
> | Standing requirements version | **QAM-SR v1.0** |
> | Adopted by | QA Lead (Fable) |
> | Date | 2026-10-14 |
> | Scope | SR-1 through SR-11 adopted, with amendment AM-3 (SR-3 wording) applied |
> | Reuse | Reusable across modules without per-module re-review |
> | Decision source | QA Lead decision ACCEPT WITH EXACT AMENDMENTS for template set v0.2-draft, 2026-10-14 (preserved verbatim in the intake addendum's `QA_LEAD_DECISION_2026-10-14.md`); recorded here by the Engineer seat as instructed, not as its own decision |
>
> The rows below are the adopted QAM-SR v1.0 text. Changes to them require a new QA Lead adoption record with a new version; a module never edits this section (`QAM_ENTRY.md` §3). The Architect's module-specific input (§2) and the Executor's reading (§3) remain separate sections.

| # | Standing requirement | Playbook basis | Applies to |
|---|---|---|---|
| SR-1 | Every AC gets a test or a separately authorized applicability ruling; expected results are independently derived, never copied from engineering claims | §8 | all modules |
| SR-2 | Negative controls and negative paths are planned, not only happy paths | §8, §10 | all |
| SR-3 | Evidence: every PASS/FAIL cites an evidence path with the command, working directory, exit code and unfiltered output; existence checks precede greps/diffs so vacuous passes are impossible | §10 | all |
| SR-4 | Browser coverage is stated as role × route/workflow × data/filter state × viewport × theme, with reductions explained; rendered behavior, effective theme, keyboard/focus, errors, loading/stale/rejection states and access denials are checked; screenshots supplement assertions | §12 | modules with UI |
| SR-5 | Credentials: declared ignored file only; no `NEXT_PUBLIC_*` reuse for QA passwords; file proved ignored AND untracked; schema validated without emitting values; values never in build/server env, commands, logs, exceptions, screenshots, traces, JSON or ZIPs; a service-role key never substitutes for proving a user's login | §12 | modules with auth |
| SR-6 | Privacy scanners validated with synthetic leak fixtures and clean controls; raw authenticated traces treated as sensitive; only approved sanitized evidence retained | §12 | all with browser/API traces |
| SR-7 | Side effects: backend, commerce and agent tests may mutate state or trigger cost; permitted effects and test targets are declared before execution | §12 | BIM / FEAT / FIX touching backends |
| SR-8 | Instruments: a helper that cannot fail is not an instrument; attack at least one deliberately; never weaken assertions, add hidden retries, skip tests or change product code to obtain green | §10 | all |
| SR-9 | Result labels are observations (PASS / FAIL / BLOCKED / NOT RUN / ADJUDICATE); an unresolved discrepancy never becomes PASS by relabeling | §11 | all |
| SR-10 | Human checks are declared beforehand, grouped near the end where independent, and counted; never fake an unattended run | §10 | all |
| SR-11 | Regression scope: required regression suite named by the plan; carried-forward evidence shows its applicability and original SHA/attempt | §8, §11 | all |

## 2. Architect module-specific risk input (attributed; input to the plan, not the plan)

**Architect:** `<<seat>>` · **Date:** `<<…>>`

| # | Risk / what could silently go wrong | Where to look | Why it matters for this module | Suggested evidence shape |
|---|---|---|---|---|
| MR-1 | `<<…>>` | `<<paths / routes / tables>>` | `<<…>>` | `<<…>>` |

### Module-type inputs (playbook §16 — supply the row for this module's type; delete the others)

| Type | Architect must supply; the plan must address |
|---|---|
| RRM | finding/disposition-to-AC mapping; exact rework boundary; removed behavior and preserved paths |
| FFM | canonical design/data contracts; frontend states; responsive/keyboard/access behavior; real auth/integrations where present |
| BIM | actual service/schema/API contracts; environment parity; auth/RLS/tenant negatives; data fixtures; allowed writes; rollback; regression |
| FIX / FEAT | original failure/feature contract; changed behavior; nearest regressions |
| TRM | not yet defined in the Factory DocSet; when defined, it instantiates QAM like every other type with its explicit definition and contracts (no profile is assumed from the acronym) |
| other tracks (ABM / APBM) | instantiate QAM under their own track's rules; their methodology is not Factory DocSet doctrine |

### Browser coverage inputs (if UI)

| Dimension | Values for this module |
|---|---|
| Roles | `<<by role name>>` |
| Routes / workflows | `<<…>>` |
| Data / filter states | `<<…>>` |
| Viewports | `<<from the actual contract; not a default>>` |
| Themes | `<<…>>` |
| Reductions proposed and why | `<<…>>` |

### Permitted effects and targets

| Effect | Permitted? | Target | Authority |
|---|---|---|---|
| Reads | `<<…>>` | `<<…>>` | `<<…>>` |
| Login / logout (creates session/audit activity) | `<<…>>` | `<<…>>` | `<<…>>` |
| Writes / mutations | `<<…>>` | `<<…>>` | `<<…>>` |
| Cost-bearing calls | `<<…>>` | `<<…>>` | `<<…>>` |

## 3. Executor's reading (Q1) — contradictions and open risk questions (QA Executor-owned section)

NOT RECORDED (filled by the QA Executor in Q1 without altering §1 or §2; contradictions between §1/§2, the contract and the Engineer's claims go to `QAM_RECON_REPORT.md` §4 and, if grading depends on them, to `STOP-CONTRACT`).

*DRAFT v0.3 — QA LEAD ACCEPTED WITH EXACT AMENDMENTS (Fable, 2026-10-14); AMENDMENTS APPLIED AND ENGINEER-VERIFIED; ARCHITECT AMENDMENT VERIFICATION PENDING.*
