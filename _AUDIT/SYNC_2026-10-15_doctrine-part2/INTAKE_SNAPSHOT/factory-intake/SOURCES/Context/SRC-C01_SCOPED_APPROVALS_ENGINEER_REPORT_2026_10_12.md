✅ SCOPED DIRECTOR APPROVALS RECORDED (STOP)

I recorded Tony's scoped approvals of five directions recommended by Jarvis. The package stays DRAFT — CORRECTION INTAKE / NOT APPROVED FOR SYNC.

**Approved directions (scoped; verbatim in the record)**
- **DEC-01:** one coordinated intake and dependency map, split only where justified. This does **not** approve the package as sync cargo.
- **DEC-02:** remove unsafe legacy examples from live guidance first. Findings count as resolved only after verified replacements land.
- **DEC-03:** acknowledge webhooks after completed work or durable acceptance. Later worker failures use durable retry/recovery.
- **DEC-04:** every privileged operation verifies its own caller, permission and target.
- **DEC-16:** clear the 9 lint findings, require green checks, retire "merge anyway". CI-trigger expansion and the baseline-gate alternative are **not** approved.

**Still undecided:**
- DEC-05's persisted/versioned quote design, and DEC-05's other parts (pricing sources, tax policy, guest-order capability).
- DEC-06 … DEC-15 and DEC-17 … DEC-22.
- The newer-doctrine harvest, which must be resolved before intake approval.

**Where it is recorded**
- **New:** `factory-corrections/DECISION_RECORD_001.md`. This is the approval record: each approval verbatim with its scope limit and affected FCs, plus what stays undecided and what the record does not authorize.
- **Index** (`FACTORY_DOCTRINE_CORRECTION_INDEX_001.md`):
  - status tags on DEC-01/02/03/04/16;
  - an UNDECIDED tag on DEC-05;
  - a §1 contents row for the record;
  - an R2 revision-log entry.
- **Unchanged:** all seven briefs are byte-identical to R1, and no FC content changed.

**Checks**
- Validator: 0 problems. 97/97 entries; certified fields and totals unchanged (B6/H36/M44/L11 · 81/8/5/3 · YES 94 / NO 3).
- Document checks: 0 problems across all 9 package files.
- Protected files: all 100 identical.
- HEAD `626da8d` unchanged; nothing staged.
- No sync, no canonical edits, no Git mutations.

→ **STOP.**

📋 Approval record: `factory-corrections/DECISION_RECORD_001.md`
📄 Logged: agent_docs/RESPONSES/response_2026-10-12_215553_scoped-approvals-recorded.md
