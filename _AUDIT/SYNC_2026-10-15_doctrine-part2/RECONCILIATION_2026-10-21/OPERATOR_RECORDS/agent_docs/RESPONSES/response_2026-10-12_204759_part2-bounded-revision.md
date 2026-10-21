🟢 PART 2 — BOUNDED ARCHITECT-REVIEW REVISION (R1) COMPLETE (STOP for Architect/Director review)

I made the seven revisions the Architect asked for, plus the containment-vs-correction distinction, and nothing else. All 97 certified records, the 17 families and the 94/3 split are unchanged and validated. The package is still DRAFT — CORRECTION INTAKE / NOT APPROVED FOR SYNC. The Architect accepted the structure for continued drafting; that is not Director approval.

**Starting state:** branch `factory-docs-review-astra-w-chunks`, HEAD `626da8d70f4db22987dc7fcc86765492072360cd` (the committed R0 draft); main = origin/main = `9c17939`. HEAD is unchanged at finish and nothing is staged.

**Exact changes** (10 FC entries + the index; `git diff --stat`: 8 files, +192 / −72)

| # | Where | Change |
| --- | --- | --- |
| 1 | `02_…` FC-014 | Recon boundary now has three write classes. **(A)** The report plus normal session/RESPONSES/RECOVERY bookkeeping is permitted. **(B)** Diagnostic-generated artifacts are allowed only inside an explicit boundary: authorizer, location (target or disposable copy), expected artifacts, post-run handling, tracked-source check; otherwise record the limitation. **(C)** Application-source changes are prohibited. Verification checks each class, and checks that nothing still literally forbids class A. DEC-14 now also asks where diagnostics run and whether read-only Git is allowed for the class-C check. |
| 2 | `06_…` FC-071 | The class string is no longer the defect. A desktop sidebar (even `hidden md:block`) is valid when the same example has an accessible mobile trigger or alternative. Verification checks that every destination is reachable at mobile widths and that the trigger is present, operable and accessible. A grep only locates candidates (CONSISTENT / NEGATIVE EXAMPLE / CHANGE). |
| 3 | `06_…` FC-080 | Outcome and verification now match. Every offered variant must get reliably generated CSS through a documented supported mechanism. Literal mapping is the recommended simple implementation; a documented safelist is acceptable. Interpolation is allowed only where the mechanism provably covers every value. |
| 4 | `07_…` FC-096 + index DEC-16 | **Recommended:** clear the 9 known findings and require `lints/run_all.py` exit 0. **Unapproved alternative:** a baseline-aware gate that passes only with zero unapproved new findings, needing a separate `XB-LINT/CI` job. The wrong "fails only on findings absent from a baseline" condition is removed. No lint or CI change is made or proposed in the `SYNC` part. Route: `SYNC` + `XB-SKILL` + `XB-LINT/CI` (only if the alternative is approved). |
| 5 | `03_…` FC-020; `05_…` FC-052, FC-059; index DEC-03, §7.2 CF-09 | Two-phase acknowledgment model. **Failure before durable acceptance** gets a retryable non-success. **Worker failure after durable acceptance** gets durable retry/recovery (bounded retries, failed-job visibility, reconciliation, owner); the acknowledgment stays lawful. Tests and verification now cover both phases. |
| 6a | `04_…` FC-033 | Separates **retiring the unsafe existing §12 routes (required)** from **no blanket ban** on future privileged list/delete operations that use role-table authorization, operation-local checks, the correct elevated client, approved target roles and target protection. Superadmin creation stays console-only. Adds a containment ≠ correction note listing the surfaces that keep FC-033 open. |
| 6b | `05_…` FC-051 + index DEC-05, §7.2 CF-08 | **Required (certified):** server-authoritative pricing and payment/order binding (no client prices/shipping/discount; amount, currency and order verified before paid; generic errors). **Architectural recommendation (awaiting DEC-05; not a finding requirement):** a single persisted, versioned quote. Verification tests the required behavior regardless of design. Adds a containment note. |
| 7 | Index §3, §6, §9 DEC-01/DEC-07, §12, §13, header; `01_…` FC-006 note | Waves are **optional sequencing**, not separate runs. **Recommended:** one coordinated intake with a single dependency map, split only where dependencies or scope justify it. DEC-01 states the Architect acceptance is for continued drafting, not Director approval. The harvest stays separate and is resolved **before intake approval**. **Persona ≠ seat:** Jarvis/Sol as intake Architect and Sol as sync QA Lead are contextual assignments, and the separate-session QA rule is kept. A revision log row is added. |
| all | Index §5 | New containment vs correction table for the 6 BLOCKERs. A contained FC stays open until its full outcome lands and its verification passes. These are package tracking terms, not certified statuses. |

**Revised outcomes vs their verification intents (checked one by one)**

| FC | Each outcome element has a matching verification check? |
| --- | --- |
| FC-014 | Yes. A, B and C each have a check, plus "no literal ban on A". |
| FC-071 | Yes. Reachability, trigger presence/operability, and grep as locator only. |
| FC-080 | Yes. Generated CSS per offered variant via the documented mechanism, and no reliance on incidental classes. |
| FC-096 | Yes. Exit 0 (recommended), or the baseline gate (only if approved), plus no exemptions and the skill-text check. |
| FC-020 / FC-052 / FC-059 | Yes. A pre-acceptance failure case, a post-acceptance worker-failure case and a duplicate case in each. |
| FC-033 | Yes. Retired routes, no superadmin creation surface, and properly authorized list/delete shape. |
| FC-051 | Yes. Each "Required" bullet has a check; the quote checks apply only if DEC-05 adopts it. |

**Validation (my own read-only checks; not independent QA)**
- Coverage: 97/97 unique primary entries (12/7/13/17/21/14/13); 17 families.
- Certified fields and totals: 6/36/44/11 severity; 81/8/5/3 current main; 94 yes / 3 no. Every certified field matches the register at `c6210c3`. **0 problems.**
- Superseded wording: all 10 old phrases checked are gone.
- Generated tables: the CF and master tables in the index match the generated ones exactly. The FC-096 route row was regenerated.
- Document checks: 0 problems (UTF-8, line endings, tables, labels).
- Paths: 98 resolve. The same 6 deliberately cited missing paths remain.
- Untouched by this revision: the other 87 FC entries and all brief headers.
- Protected inputs: all 100 tracked files are byte-identical (certified evidence, doctrine, MANIFEST, CHANGELOG, skills, lints, CI, root CLAUDE.md).
- Lints: output identical to the baseline (exit 1, the 9 pre-existing findings).

**Not changed (outside the bounded scope; noted for the Architect)**
- FC-050, FC-060 and FC-067 still say "quote" loosely ("quote binding", "server quote interface", "authoritative quote"). They read correctly as server-authoritative pricing. Aligning their wording with FC-051's required-vs-recommended split is a small optional follow-up.
- FC-062 is already consistent with the two-phase model ("acknowledge only after the required local work is safely accepted"), so I left it.

**Remaining policy decisions (unchanged list; index §9)**
- DEC-01: Director approval and intake form.
- DEC-02: retire vs rewrite.
- DEC-03: the two-phase acknowledgment contract.
- DEC-04: operation-local authorization.
- DEC-05: server pricing sources and tax policy, and whether to adopt the quote design.
- DEC-06 … DEC-22 as listed, including DEC-14 (now also the recon diagnostic location and read-only Git question) and DEC-16 (exit 0 vs the unapproved baseline gate).

**Boundaries kept:** writes went only to the 8 `factory-corrections/` files plus bookkeeping. No certified evidence, doctrine, skill, lint or CI edits. No Git writes. No DocSet Sync activation.

**Delivery:** a new review ZIP will be built in `~/Downloads` as `PART2_ARCHITECT_REVIEW_R1_2026-10-12_204759.zip`. It holds the 8 revised files, this response and a hash manifest; the previous ZIP is kept. Its path and SHA-256 are reported in the delivery record.

📄 Logged: agent_docs/RESPONSES/response_2026-10-12_204759_part2-bounded-revision.md
