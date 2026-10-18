# ENGINEERING_HANDOFF — `<<MODULE_ID>>`

> NEWLY AUTHORED DRAFT — QA LEAD REVIEW REQUIRED. Template `QAM/HANDOFFS/ENGINEERING_HANDOFF.md` v0.2-draft (2026-10-14), from `QAM_PLAYBOOK_v1_0.md` §5 and §7. **Owner: Engineer**, as part of the original engineering assignment. Everything here is a **claim for independent QA** unless it is a command or a path. Companion to `../QAM_MANIFEST.md` (identity, environment and reproduction facts); do not restate the manifest, link to it.

**Engineer:** `<<seat / runtime>>` · **Recorded at:** `<<YYYY-MM-DD HH:MM TZ>>` (before the Director commits) · **Manifest:** `../QAM_MANIFEST.md` (identity §1; complete change inventory at handoff §2 — committed, staged, unstaged, untracked) · **Candidate:** `PENDING` until the Director commits the completed engineering work and creates `qa/<<MODULE_BRANCH>>` at that commit

## 1. What was built (claims, per acceptance criterion)

| AC | Claim | Where (paths) | Self-verification (command · working dir · result) | Evidence path |
|---|---|---|---|---|
| `<<AC-nnn>>` | CLAIM: `<<…>>` | `<<…>>` | `<<…>>` | `<<…>>` |

Every AC in the frozen contract has a row, including ACs the Engineer believes are not applicable (state why; the applicability ruling is the Architect's, not the Engineer's).

## 2. Commands (exact, with working directory)

```
<<command>>            # <<working dir>> — <<purpose>>
```

## 3. Evidence inventory (what each item means)

| Path | Meaning (CLAIM) | Produced by |
|---|---|---|
| `<<…>>` | `<<…>>` | `<<command / tool>>` |

## 4. Limitations and open points

| Item | Detail | Who should decide |
|---|---|---|
| `<<…>>` | `<<…>>` | `<<Architect / QA Lead / Director>>` |

## 5. Reproduction for an independent runtime

Steps a fresh QA runtime follows from a clean clone of `qa/<<MODULE_BRANCH>>` at the candidate: `<<numbered steps, each a command with its working directory>>`. Anything that depends on the Engineer's machine state is listed as a limitation above.

## 6. What this handoff does not contain

- Q1 findings, Q2 results, a plan, an approval, a certificate (not the Engineer's to write).
- Secret values, auth state, raw authenticated traces.
- Any statement that the acceptance criteria should change (route a contract question to the Architect through the ruling lane).

*NEWLY AUTHORED DRAFT — QA LEAD REVIEW REQUIRED.*
