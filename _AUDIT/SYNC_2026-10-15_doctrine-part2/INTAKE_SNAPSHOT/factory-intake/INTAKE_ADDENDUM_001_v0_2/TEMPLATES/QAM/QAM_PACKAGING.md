# QAM_PACKAGING — automatic review packages for `<<MODULE_ID>>`

> NEWLY AUTHORED DRAFT — QA LEAD REVIEW REQUIRED. Template `QAM/QAM_PACKAGING.md` v0.2-draft (2026-10-14), from `QAM_PLAYBOOK_v1_0.md` §13 (and §12 privacy, §8/§10 returns, §15 state). **Owner: QA Executor builds every package; the Architect sets module-specific exclusions at packaging.** These are instructions, not a tool: no exporter or validator is delivered with this set (RUL-07). The Director should never ask "which files?" or search temporary folders.

## 1. When a package is produced

Every Q1 return, Q2 return, material stop and repair/retest (Q4) return — subject to privacy. Packaging does not require rerunning passed tests.

## 2. Canonical destination and naming

`QAM/HANDOFFS/<<MODULE_ID>>_<PHASE>_REVIEW_<ATTEMPT>.zip` where `<PHASE>` ∈ `Q1`, `Q2`, `Q4`, `STOP` and `<ATTEMPT>` is a two-digit counter per phase (`01`, `02`, …). The module copy is canonical. A byte-identical convenience copy in the Director's Downloads folder is allowed when requested. Never nest previous ZIPs by default.

Return, in the response: the absolute path, member count, SHA-256 of the completed ZIP, and the exact decision requested.

## 3. Inclusion list (explicit; per phase)

| Member | Q1 | Q2 / Q4 | STOP |
|---|---|---|---|
| `REVIEW_START_HERE.md` (from `HANDOFFS/REVIEW_START_HERE.md`) | ✔ | ✔ | ✔ |
| `FILE_INDEX.json` (schema: `HANDOFFS/FILE_INDEX.template.json`) | ✔ | ✔ | ✔ |
| `QAM_STATE.md` — the **immutable pre-export snapshot** (see §6) | ✔ | ✔ | ✔ |
| `QAM_ENTRY.md` | ✔ | ✔ | ✔ |
| Frozen contract + ruling lane (copies or exact references with hashes) | ✔ | ✔ | ✔ |
| `GOVERNING/README.md` (+ necessary governing sources) | ✔ | ✔ | ✔ |
| `QAM_MANIFEST.md`, `HANDOFFS/ENGINEERING_HANDOFF.md` | ✔ | ✔ | as relevant |
| `QAM_PREFLIGHT.md` + `evidence/preflight/<attempt>/` | ✔ | rechecked rows | ✔ |
| `QAM_RECON_REPORT.md` (the actual recon response files, not only a summary) | ✔ | ✔ | as relevant |
| `QAM_TEST_PLAN.md` (draft in Q1; bound plan in Q2) | ✔ | ✔ | ✔ |
| `QAM_APPROVAL.md` | — | ✔ | as relevant |
| `QAM_EXECUTION_REPORT.md`, `AC_EVIDENCE_MATRIX.md`, `FINDINGS.md` | — | ✔ | partial, as safe |
| `evidence/**` approved sanitized evidence + `AUTOMATION/` helper sources | identity evidence | ✔ | partial, as safe |
| Exact certification / approval text when someone is instructed to transcribe it | — | ✔ when present | — |
| Repository-required response/session records (indexed by path; included where review needs them) | ✔ | ✔ | ✔ |

Missing items are listed honestly in `REVIEW_START_HERE.md` §"Not included".

## 4. Exclusions (always)

Env/credential files (`<<QA_CREDENTIAL_FILE>>` and any `.env*`), auth state (`storageState`, cookies, tokens), browser profiles, dependencies (`node_modules/`, venvs), builds (`.next/`, `dist/`, caches), Git internals, disposable mirrors, unreviewed raw sensitive logs or traces, image bodies beyond the approved sanitized set. Module-specific additions set by the Architect: `<<…>>`.

## 5. Build and verify (manual procedure; any zip tool)

1. Record the pre-export state entry in `QAM_STATE.md` (phase, identities, package name and member count; **no ZIP hash yet**).
2. Assemble the inclusion list for the phase; confirm every path exists (existence check first).
3. Write `FILE_INDEX.json` with, for every member except itself: archive path, source path, purpose, byte size, SHA-256.
4. Create the ZIP with a single top-level folder named after the ZIP stem.
5. Verify: exact index membership (no extra, no missing), hashes, safe paths (no absolute or `..`), no duplicates, archive integrity test, privacy scan of the selected export contents **and** expanded archive members with the validated scanner (safe counts/locations only).
6. Compute the ZIP's SHA-256 **outside** the ZIP (external receipt). Record it in `HANDOFFS/README.md` (receipts table), in the return message, and in a **subsequent live entry** of `QAM_STATE.md`.

Withhold an unsafe export; supply a safe partial package when possible. A stop is never a reason to hide completed evidence.

## 6. Snapshot rule (expected difference between archived and live state)

- The `QAM_STATE.md` inside the ZIP is the immutable pre-export snapshot written at step 1. It cannot and must not contain the ZIP's own hash.
- The completed ZIP hash lives only in the external receipt and in the live state entry written after export (step 6).
- **Never rebuild the ZIP merely to insert its own hash**; a rebuilt ZIP has a new hash and a new receipt.
- The difference between the archived snapshot and the later live state is expected; it is recorded with provenance (date, seat, "post-export receipt") so that a reader of the archive does not mistake it for an inconsistency.
- Privacy and evidence-preservation requirements (§4, §5 step 5, playbook §12–§14) apply unchanged to every package, including partial and stop packages.

*NEWLY AUTHORED DRAFT — QA LEAD REVIEW REQUIRED.*
