# Factory Doctrine Correction Package 001 — Decision Record

> **PACKAGE STATUS: DRAFT — CORRECTION INTAKE / NOT APPROVED FOR SYNC**
> This record holds **scoped directional approvals only**. The package as a whole stays DRAFT, pending the remaining decisions (index §9) and the newer-doctrine harvest (index §12). Nothing here approves the package, or any part of it, as DocSet Sync cargo, and nothing here authorizes canonical edits.

| Field | Value |
|---|---|
| Decision date | 2026-10-12 |
| Approver | Tony (Director) |
| Recommended by | Jarvis (Architect) |
| Recorded by | Claudy (documentation Engineer seat), 2026-10-12 21:54 +0600, from the Director/Architect clarification as relayed. Wording below is preserved from that clarification. |
| Package revision | R1 (working tree on `factory-docs-review-astra-w-chunks`, over HEAD `626da8d70f4db22987dc7fcc86765492072360cd`) |

---

## 1. Approved directions (scoped)

### DEC-01 — Intake form: APPROVED (scoped)
- **Approved direction (verbatim):** "One coordinated intake and dependency map. Split only where justified. This does not approve the full package as sync cargo."
- **Scope limit:** it approves the *form* of intake only. The 94 proposed outcomes are **not** approved as cargo. Intake approval still waits on the remaining decisions and on the newer-doctrine harvest, which is to be resolved before intake approval.
- **Affects:** index §6 (sequencing), §13 (intake fit); all FCs as a delivery form.

### DEC-02 — Legacy auth examples: APPROVED (scoped)
- **Approved direction (verbatim):** "Remove unsafe legacy examples from live guidance first. Complete verified replacements before declaring the findings resolved."
- **Scope limit:**
  - Removal from live guidance is a containment step. It does **not** resolve FC-033, FC-034, FC-035, FC-001 or FC-039 (the AUTH part).
  - Each finding is resolved only when its verified replacement lands and its verification intent passes (index §5, containment ≠ correction).
  - Kit verification for the replacements is still needed (DEC-09).
- **Affects:** FC-033, FC-035, FC-001, FC-039 (AUTH part), FC-034.

### DEC-03 — Webhook acknowledgment contract: APPROVED (scoped)
- **Approved direction (verbatim):** "Acknowledge webhooks after completed work or durable acceptance. Later worker failures use durable retry/recovery."
- **Scope limit:** this approves the two-phase direction as stated in R1 (FC-020, FC-052, FC-059):
  - before durable acceptance, a retryable non-success;
  - after durable acceptance, durable retry/recovery, and the acknowledgment stays lawful.
  Concrete doctrine wording is still proposed later in the DocSet Sync UPDATE MAP and approved there.
- **Affects:** FC-020, FC-052, FC-059, FC-062.

### DEC-04 — Operation-local authorization: APPROVED (scoped)
- **Approved direction (verbatim):** "Every privileged operation verifies its own caller, permission and target."
- **Scope limit:** this is a direction for the Factory-wide invariant. Where and how it is stated in doctrine is still proposed in the UPDATE MAP.
- **Affects:** FC-036, FC-057, FC-050, FC-038; consistent with FC-033 (authorized list/delete stays permissible).

### DEC-16 — Lint gate: APPROVED (scoped)
- **Approved direction (verbatim):** "Clear the nine existing lint findings, require green checks, and retire 'merge anyway' guidance. CI-trigger expansion is not approved by this decision."
- **Scope limit:**
  - The approved path is clear-and-require-green.
  - The baseline-aware gate alternative in FC-096 was **not** approved.
  - **CI-trigger expansion is not approved**, which affects FC-095's trigger option. FC-095's wording-fix path is unaffected.
  - Retiring the "merge anyway" guidance concerns the docs-update skill (`XB-SKILL`) and still needs its own separately approved job (DEC-21).
  - Making green checks a merge requirement is a governance / branch-protection setting owned by Tony.
  - No lint script or CI workflow change is approved here.
- **Affects:** FC-096, FC-003 (6 of the 9 findings), FC-095 (trigger option).

## 2. Explicitly not decided

- **DEC-05:** the persisted/versioned quote design remains **undecided**. The certified requirement in FC-051 (server-authoritative pricing and payment/order binding) is unchanged, but DEC-05's other elements are not approved by this record:
  - pricing sources
  - tax policy
  - guest-order capability
  - quote design
- **All other decisions** in index §9 (DEC-06 … DEC-15, DEC-17 … DEC-22) remain open.
- **Newer-doctrine harvest** (index §12): still separate and pending, to be resolved before intake approval.

## 3. What this record does not do

- It does not change any certified FC record, severity, status or family.
- It does not approve the package as sync cargo.
- It does not authorize canonical doctrine, skill, lint or CI edits.
- It does not start DocSet Sync or authorize an `_INBOX/` drop.
- It does not mutate Git.

*PACKAGE STATUS: DRAFT — CORRECTION INTAKE / NOT APPROVED FOR SYNC.*
