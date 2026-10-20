CODY — ENGINEER: BOUNDED QA-P4 REPAIR (AMENDED-v2), ONE PASS

Seat: Cody, Engineer. Issued by Fable (QA Lead) from the Phase 4 verdict
RUN/QA_PHASE4/QA_LEAD_VERDICT.md (verdict FAIL: AC5, AC6, AC9, AC15, AC16, AC18).
Director: Tony. Architect: Jarvis confirms wording before Gate 2 on this amendment.

RUN        = _AUDIT/SYNC_2026-10-15_doctrine-part2
Review repo (write records here): /home/moose/Documents/app-factory-docs-v1
Execution worktree (read-only until Tony records Gate 2 on AMENDED-v2):
           /home/moose/Documents/app-factory-docs-sync-execution
Candidate  QA_START_SHA 20f71ee932ed21c0878cb3a0f39c6fbe90d0a793
CONTENT    ef35d26d82f1904da6ed33663ad647e4ee16fe98 · BASE 9c179392f79b70da099121fc357d3107ad3bb86e
Landing date stays 2026-10-18. Spec R1 2a3867ca… is unchanged and not yours to edit.

Read first: RUN/QA_PHASE4/QA_LEAD_VERDICT.md §2/§4, RUN/QA_PHASE4/REPAIR_QA_P4/REPAIR_FINDINGS.json,
RUN/QA_PHASE4/EXECUTOR_EVIDENCE/MANUAL_READS.md §Findings (exact excerpts), RUN/AMENDED_V1/README.md
(record conventions you follow again), RUN/BOUND_EXECUTION_INDEX.json.

All six failures are content carried from BASE through the approved proposal; your Phase 3 installation
was exact. This is a content amendment (AMENDED-v2) that re-enters Gate 2, not a re-implementation.

1. REQUIRED CORRECTIONS (six documents, content-only; line numbers are at 20f71ee)

F01 · 02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:176 — replace the blockquote line
   "> Same artifact name — different author, different moment. Router: …"
   with wording that states the Architect authors DATA_CONTRACT in both runs and that only the evidence
   base and the moment differ (conversion: Brain Drain evidence, pre-authored; greenfield: approved
   APP_BRIEF, before Design). Keep the router pointer to APP_FACTORY_BLUEPRINT "Which Pipeline Am I In?".

F02 · 02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:1385 and 1389–1398 (§17)
   a. Replace "When code is complete and tested, Engineer hands off to Operations/Deployment." with a
      sentence that routes the completed, self-verified candidate and the factual QAM handoff to
      independent QA on the Director-created QA branch, and states that Operations/Deployment receives the
      package only after QA Lead certification and Director release (cite QAM_PLAYBOOK §3 and
      DEPLOYMENT_PLAYBOOK §3).
   b. In the "📦 ENGINEER → OPERATIONS HANDOFF" tree add, in the module's artifact order, entries for
      ACCEPTANCE_SPEC.md (from Architect) and QAM/ (module QA pack: ENGINEERING_HANDOFF, approved plan,
      results, certificate) so the ship-time anatomy no longer omits them. Keep the other six entries.
   c. Leave "What Operations Needs" and the Verbal Brief template as they are.

F03 · 02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:255–257 (kit-track diagram fence) — replace
   "Where handbook and filesystem disagree, the filesystem wins." with the approved RUL-12 wording already
   installed at the former sites 103/125/1582 (disk establishes implementation facts; record handbook
   drift; route any requirements conflict to the Director). Keep the diagram's line structure.
   Result: zero "filesystem wins" / "disk wins" hits in live scope outside Version History.

F04a · FC-022 · 03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:887–930 — withdraw both executable fences
   ("Direct DB seeding to bypass Stripe in E2E" seedSubscription upsert; "Supabase admin client in E2E
   helpers" createClient from .env.local) using the standard withdrawal sentence already used at 881, and
   state the invariant: privileged seeding and admin-client construction in test helpers run only behind
   the allowlist/identity guard of line 883 and fail closed. You may keep the prose rationale (889) and
   the Trade-off paragraph (914) as prose. Result: no code fence in live scope contains seedSubscription
   or an unguarded supabaseAdmin construction; grep "seedSubscription|supabaseAdmin" over the 36 live docs
   returns only prose or nothing.

F04b · FC-038 · 04_REFERENCE_MANUALS/DATABASE_MANUAL.md:418–432 (§5 Service Role Bypass) — rewrite the
   lead sentence and list so the service-role client is appropriate only inside an independently
   authorized elevated operation (background jobs; admin operations with operation-local authorization),
   and state that an API route is not itself a reason to bypass RLS (same rule as AUTH_MANUAL:1311).
   Update the code comments ("// Bypasses RLS") to say the client is constructed only inside such an
   operation, never as a default route client. Keep the heading.

F04c · FC-066 · 04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:613, 793, 856 — make every
   fetchProducts occurrence match one declared contract or carry an explicit alternative label:
   the declared contract is the typed outcome at 172–174. Acceptable: (i) label the normalization
   example at 613 as the array-returning normalization step and have the caller at 793 consume the typed
   outcome per 172 (or a labelled wrapper), and (ii) label the ISR variant at 856 as an independent
   example with its own return contract. Not acceptable: a caller silently destructuring a shape its
   service does not return. Do not add new service code beyond labels/signature alignment.

F05 · FC-040 / RUL-13 — add one sentence stating the default in each of:
   04_REFERENCE_MANUALS/AUTH_MANUAL.md near 1122 (Security Best Practices ❌ DON'T list: extend or add a
   bullet), 03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md inside 416–428 (after the dual-verification
   example), 04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md:205 (make the policy reference
   explicit). Wording: no persistent raw contact information in browser storage by default; any approved
   exception names fields, purpose, retention period and owner with clearing/invalidation behavior.
   STATE_MANAGEMENT_MANUAL:783 already states it; do not duplicate examples; add no example that
   persists contact data.

OPTIONAL (not required for PASS; include only if Jarvis agrees, labelled FU-1/FU-2 in the amendment):
   FU-1 STRIPE_SUBSCRIPTIONS_PLAYBOOK.md §13 (484–486): one-line qualifier — historical project procedure,
   not Factory deployment doctrine; see DEPLOYMENT_PLAYBOOK §7 (OPEN); verify commands at implementation.
   FU-2 FFM_PLAYBOOK.md:42/169/173/1639: "the project's declared module location, conventionally
   agent_docs/CURRENT_APP/<project>_<phase>_ffm/" so §1/§16 agree with the path-agnostic Appendix B.

2. WHAT YOU MUST NOT CHANGE
   - Header Version/Date lines of the six documents (versions already bumped this run; date 2026-10-18).
   - Version History tables: no new row; append a short "QA-P4 repair: F01–F05 (AC5/6/9/15/16/18)" clause
     to each document's existing 2026-10-18 run row. CHANGELOG: amend the six existing run rows the same
     way; row count stays 39. MANIFEST: unchanged (headers unchanged).
   - _ARCHIVE/** (31 outgoing + QA v1.0), 03_BUILD_METHODOLOGY/_templates/QAM/**, _workflows/**,
     _assets/**, 10x Lab/**, _SKILLS/**, lints/**, .github/**, root CLAUDE.md/AGENTS.md.
   - The 12 conditional transitions on 9 paths (DEPLOYMENT/QAM/RRM headers, template README, MANIFEST
     rows, 4 workflow status lines) stay at pre-transition wording.
   - Frozen records: UPDATE_MAP.md, AMENDED_V1/**, QA_RETEST_AF01/**, the spec, INTAKE_SNAPSHOT/**.
   - Everything else in the 101 paths: byte-identical to the candidate.

3. RECORDS TO PRODUCE (review repo, RUN/AMENDED_V2/, same conventions as AMENDED_V1/)
   AMENDMENT_V2.md (per-finding old→new spans with evidence, authority = this verdict + Jarvis
   confirmation), AMENDMENT_V2_EDITS.json (E381+), SELECTED_EXACT_EDITS.json (380 + new, ordered),
   EXECUTION_PROPOSAL_INDEX.json (101 paths; before_sha256 = candidate bytes at 20f71ee, proposed =
   amended), BOUND_EXECUTION_INDEX.json successor (landing_date 2026-10-18), EXECUTION_PROPOSAL.patch
   (-p0 against a fresh `git archive 20f71ee` export; include "\ No newline at end of file" markers; must
   pass `git apply --check`), PROPOSED_CONTENT/ (six files), AMENDMENT_IDENTITIES.json, VERIFICATION.json
   (generator + verify scripts under RUN/scratchpad/generators/, run with python3 -B -I), a propagation
   sweep TSV for the terms: "different author", "filesystem wins", "disk wins", "hands off to
   Operations", "seedSubscription", "supabaseAdmin", "appropriate for:", "fetchProducts", "raw contact",
   "persist" — every hit dispositioned RESOLVED/RETAIN with rationale, fail closed on undispositioned.
   Then one handoff to Jarvis (wording confirmation) and to Fable (retest handoff), a Downloads ZIP with
   SHA256SUMS, delivery receipt, RESPONSES file, session/RECOVERY entries.

4. ACCEPTANCE CRITERIA FOR THIS REPAIR (graded by the bounded retest)
   R1 AC5/AC6: map §B ownership searches zero active hits; ENGINEER:174–176 consistent; the eight
      AMENDED-v1 spans unchanged. R2 AC9: ENGINEER §17 sentence + tree include QA routing, QAM/,
      ACCEPTANCE_SPEC. R3 AC15: zero "filesystem wins"/"disk wins" active hits; RUL-12 wording present.
   R4 AC16: FC-022/038/066 rows PASS per the Executor's withdrawal-table method; the other 28 unchanged.
   R5 AC18: all four manuals state the RUL-13 default; no example persists raw contact data.
   R6 AC2: all 101 paths equal the AMENDED-v2 bound index; 95 unchanged paths byte-identical to 20f71ee.
   R7 AC25/26/27: headers unchanged; MANIFEST rows = headers; 39 CHANGELOG rows; one history row per doc.
   R8 AC29/AC31: lint suite PASS, 0 hits; lints/.github unchanged. R9 AC23/AC24/AC22/AC37: archives,
      templates, workflows byte-unchanged. R10 AC33: 12 transitions still pending. R11 AC32: the repair
      lands as one commit "repair QA-P4 F01–F05 (AMENDED-v2 <index sha>)" after Tony's Gate 2 record;
      no main write, no merge, clean tree. R12 AC1: no path outside the six documents and run records
      changes.

5. SEQUENCE AND STOPS
   a. Prepare AMENDED_V2 records and verification in the review repo (no execution-worktree writes).
   b. Hand to Jarvis for wording confirmation; fold confirmed wording into the same AMENDED-v2 (no v3
      unless Jarvis changes substance).
   c. Tony records Gate 2 on AMENDED-v2 (QA_PHASE4/REPAIR_QA_P4/DIRECTOR_DECISIONS_V2.md, naming the
      index and patch identities; prior identities preserved).
   d. Only then apply on the execution branch, verify, commit, push the working branch (Tony's agent-Git
      authorization of 2026-10-18 applies; no force push, no main, no merge, no PR).
   e. Hand off to Fable; a fresh QA Executor runs the bounded retest (R1–R12); Fable issues the
      successor verdict. Closeout transitions remain pending until then.
   Finish a–b without routine "go" questions; stop at c for Tony.
