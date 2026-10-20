import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import *
import collections

mechanical = json.loads((E / "RAW/automated_checks.json").read_text())
manual = json.loads((E / "RAW/manual_checks.json").read_text())
stable = json.loads((E / "RAW/stability.json").read_text())
prop = json.loads((E / "RAW/propagation_summary.json").read_text())
inputs = json.loads((E / "INPUT_IDENTITIES.json").read_text())
prior_manifest = inputs["prior_manifest_sha256"]
candidate_stable = all(stable[k] for k in [
    "start_pins_match", "end_pins_match", "same_remote_tip", "same_canonical_hashes", "review_protected_unchanged"])
input_valid = all(mechanical[k]["ok"] for k in [
    "input_pins", "prior_manifest_identity", "prior_inventory", "handoff_crosscheck"])

definitions = [
    ("R4′", ["AC16"], "PASS",
     ["eight_edits_present", "only_eight_edits", "code_imports_unchanged", "live_scope_counts"],
     ["MANUAL_READS.md", "PROPAGATION.tsv", "WITHDRAWAL_ROWS.json", "RAW/edit_accounting.json", "RAW/code_preservation.json"],
     "All four return-contract labels match their consumers, including V3-2. All 29 occurrences on 26 lines across 44 live-scope files are dispositioned. No executable/import changes. FC-066 independently read; other withdrawal rows preserved by file identity or exact-section re-read."),
    ("R6′", ["AC2"], "PASS", ["installation_101", "unchanged_98", "three_proposals", "outside_101_preserved"],
     ["RAW/index_hashes.json", "RAW/preexisting_paths.json", "RAW/candidate_blobs/"],
     "101 installed-file hashes equal independently read candidate blobs and the successor index; 98 are parent-identical. Three changed canonical files equal proposed content. Every pre-existing file outside the 101 remains byte-identical."),
    ("R7′", ["AC25", "AC26", "AC27"], "PASS", ["manual_metadata", "changelog_metadata", "manifest_unchanged"],
     ["RAW/metadata.json", "RAW/canonical.diff", "MANUAL_READS.md"],
     "ARCH v1.4 and STATE v1.3 headers retain 2026-10-18 / Active. One amended existing history row each (1289,1111), no new rows. CHANGELOG retains 39 run rows; only 56/60 changed; six v2 clauses unchanged. MANIFEST exact."),
    ("R8′", ["AC29", "AC31"], "PASS", ["lint_exit", "protected_surfaces"],
     ["RAW/lints.txt", "RAW/protected_trees.json", "COMMANDS.json"],
     "Unchanged candidate-export lint suite exits 0: zero encoding/retired-term/versioned-reference hits across 36 docs and all headers pass. lints/ and .github/ remain exact."),
    ("R10′", ["AC33"], "PASS", ["transitions_pending", "no_later_local_commit"],
     ["RAW/transitions.json", "QA_START.json", "QA_END.json"],
     "All 12 spans on nine paths retain old wording exactly once; new wording is absent. V3 transition plan agrees. Local and remote branch tips remain the candidate, with no later closeout commit on the tested branch."),
    ("R11′", ["AC32"], "PASS", ["authorization"],
     ["RAW/authorization.json", "RAW/ancestry.json", "RAW/handoff_crosscheck.json", "QA_START.json", "QA_END.json", "COMMANDS.json"],
     "One non-merge child of the exact parent, full-index-hash subject, attributable author, committed Tony approval predating the commit. Ancestry, authorized branch, local/remote candidate, clean worktree and BASE main match; receipts agree. O-1 structure-only assessment."),
    ("R12′", ["AC1"], "PASS", ["scope_56", "scope_canonical", "scope_additions", "scope_no_other",
                             "protected_surfaces", "frozen_records", "root_files"],
     ["RAW/scope.json", "RAW/parent_tree.json", "RAW/candidate_tree.json", "RAW/preexisting_paths.json", "RAW/stability.json"],
     "56 paths independently enumerated: three canonical modifications plus 53 new records under AMENDED_V3/ and AMENDED_V3_EXECUTION/. No frozen overwrite. Protected archives/templates/workflows/SVGs/10x/skills/root files unchanged; all 1,461 existing review-run files also preserved."),
    ("R1", ["AC5", "AC6"], "CARRIED", ["carry_R1"],
     ["RAW/carry_forward.json", "RAW/prior_inventory.json"],
     "Accepted parent PASS carried: BLUEPRINT, ARCHITECT, DESIGNER, ENGINEER, HANDOFF_PACKAGE, FFM and BIM are whole-file byte-identical. No ownership re-execution."),
    ("R2", ["AC9"], "CARRIED", ["carry_R2"],
     ["RAW/carry_forward.json", "RAW/prior_inventory.json"],
     "Accepted parent PASS carried: ENGINEER, QAM and DEPLOYMENT are whole-file byte-identical. No handoff re-execution."),
    ("R3", ["AC15"], "CARRIED", ["carry_R3"],
     ["RAW/carry_forward.json", "RAW/prior_inventory.json"],
     "Accepted parent PASS carried: ENGINEER is whole-file byte-identical. No filesystem-authority re-execution."),
    ("R5′", ["AC18"], "PASS", ["state_passages", "carry_R5_prime_other"],
     ["RAW/state_passages.json", "RAW/parent_state.md", "RAW/candidate_state.md", "RAW/carry_forward.json", "MANUAL_READS.md"],
     "PASS carried by exact STATE passages: §§4/5/6, raw-contact comment and RUL-13 default range all identical; lines 1–808 identical and first difference at 809. STATE whole-file identity is false. TESTING, AUTH and ECOMMERCE files remain exact."),
    ("R9", ["AC22", "AC23", "AC24", "AC37"], "CARRIED", ["carry_R9", "protected_surfaces", "frozen_records"],
     ["RAW/carry_forward.json", "RAW/protected_trees.json", "RAW/prior_inventory.json", "RAW/stability.json"],
     "Accepted parent PASS carried for the 31 outgoing archives plus historical QA restoration, 25 templates, four workflows and four SVGs, two 10x files and frozen records. Protected full tree sets match; no archive-original or workflow semantic re-execution.")
]
results, findings = [], []
for rid, acs, preferred, keys, evidence, rationale in definitions:
    failed = [key for key in keys if not mechanical[key]["ok"]]
    if rid == "R4′":
        failed += [key for key in ["four_contracts_coherent", "streaming_comment_present",
                   "only_label_and_metadata_changes", "propagation_complete", "withdrawals_preserved"] if not manual[key]]
    status = "BLOCKED" if not (candidate_stable and input_valid) else "FAIL" if failed else preferred
    ids = []
    if status in ["FAIL", "BLOCKED"]:
        fid = "RV3-" + rid.replace("′", "") + "-01"
        ids.append(fid)
        findings.append({"id": fid, "severity": "HIGH", "check": rid, "status": status,
                         "basis": failed or ["Candidate stability or authority-input integrity failed"],
                         "evidence": evidence})
    results.append({"id": rid, "mapped_acs": acs, "status": status, "rationale": rationale,
                    "evidence": evidence, "mechanical_check_keys": keys, "finding_ids": ids,
                    "prior_manifest_sha256": prior_manifest if rid in ["R1", "R2", "R3", "R5′", "R9", "R4′"] else None})
save("R_RESULTS.json", results)
save("RAW/findings.json", findings)
counts = {status: sum(x["status"] == status for x in results) for status in ["PASS", "CARRIED", "FAIL", "BLOCKED"]}
save("RAW/result_counts.json", counts)

# Personal commit metadata is inspected for attribution and then redacted in delivery.
start = json.loads((E / "QA_START.json").read_text())
commit_lines = start["commands"]["commit"]["stdout"].splitlines()
author_name, author_email = commit_lines[2:4]
redactions = []
for p in sorted(E.rglob("*.json")):
    if p.name == "author_identity.json":
        continue
    old = p.read_text()
    new = old.replace(author_email, "[REDACTED AUTHOR EMAIL]").replace(author_name, "[REDACTED AUTHOR NAME]")
    if old != new:
        p.write_text(new)
        redactions.append({"path": str(p.relative_to(E)), "fields": ["Git author name/email"],
                           "reason": "Assignment requires personal-data redaction; author-presence and identity digests retained."})
save("RAW/author_identity.json", {"author_present": bool(author_name), "email_present": bool(author_email),
     "author_name_sha256": sha(author_name.encode()), "author_email_sha256": sha(author_email.encode()),
     "attribution": "Consistent Git author metadata was inspected at the pinned commit; attributable under O-1.",
     "redacted_files": redactions})
observations = [
    {"id": "OBS-V3-01", "kind": "OBSERVATION", "scope": "execution environment",
     "text": "Initial sandbox ls-remote exited 128 because GitHub DNS was unavailable. The authorized network-enabled read-only retry succeeded before any grading; final remote check also succeeded. Failure output is retained."},
    {"id": "OBS-V3-02", "kind": "OBSERVATION", "scope": "harness correction",
     "text": "The first measurement invocation assumed DIRECTOR_RELEASE.md existed in the review repo and stopped. It exists in the candidate export; input selection was corrected and the complete measurement script rerun. No candidate defect or candidate write occurred."},
    {"id": "OBS-V3-03", "kind": "OBSERVATION", "scope": "carry-forward boundaries",
     "text": "STATE and ARCH are changed documents. R5 uses exact STATE passages. Seven other withdrawal rows touching these documents were re-read at preserved sections and marked PASS, rather than claiming whole-file carry; the other 23 withdrawal rows are CARRIED and FC-066 is independently PASS."},
    {"id": "OBS-V3-04", "kind": "OBSERVATION", "scope": "excluded follow-ups",
     "text": "FU-1/FU-2 remain optional, excluded and unchanged. No failure or new disposition is assigned to them."}
]
save("RAW/observations.json", observations)
save("RAW/harness_invocations.json", [
    {"command": ["python3", "-B", "-I", str(E / "scripts/01_preflight.py")], "cwd": str(ROOT),
     "exit": 1, "stdout": "Handoff: safe member paths and 38/38 inventory hashes verified\n",
     "stderr": "BLOCKED initial pins; inspect QA_START.json; do not export or grade\n",
     "resolution": "Same read-only remote check retried with network access; pins matched before export/testing."},
    {"command": ["python3", "-B", "-I", str(E / "scripts/02_measure.py")], "cwd": str(ROOT),
     "exit": 1, "stdout": "",
     "stderr": "FileNotFoundError: review-repo _AUDIT/SYNC_2026-10-15_doctrine-part2/PHASE3_EXECUTION/DIRECTOR_RELEASE.md (copy_input/source.read_bytes)",
     "resolution": "Read committed candidate copy; complete 02_measure.py rerun exited 0."}
])
# Main command ledger includes failures from verification subprocesses and wrapper invocations.
logs = json.loads((E / "COMMANDS.json").read_text())
logs.extend(json.loads((E / "RAW/harness_invocations.json").read_text()))
save("COMMANDS.json", logs)

report = [
    "# Independent QA Executor report — AMENDED-v3 bounded retest",
    "",
    f"**Results over 12 entries:** {counts['PASS']} PASS / {counts['CARRIED']} CARRIED / {counts['FAIL']} FAIL / {counts['BLOCKED']} BLOCKED.",
    "",
    f"**Actual QA_START_SHA:** `{start['QA_START_SHA']}`. Parent `{PARENT}`; authorized branch `{BRANCH}`. BASE/main `{BASE}`.",
    f"**Seat:** Independent QA Executor, reporting to Fable (QA Lead). **Session start UTC:** {C['start_utc']}. **Remote pin captured:** {start['utc']}.",
    "**Independence:** This conversation did not author, apply, commit or push AMENDED-v3, and did not act as Fable. The assignment was launched by Tony in this fresh conversation. Engineering scripts/results were not used as the test suite; no apply/push/verify_installed helpers were run.",
    "",
    "## Scope and authority",
    "",
    "The frozen R1 specification, O-1…O-8, Director rulings, both preserved Fable verdicts, attributable AMENDED-v3 Gate 2 and the bounded assignment govern this run. Seven bounded checks were re-executed; R1/R2/R3/R9 were carried by exact identity and R5′ checked by exact passage. No broad Phase 4 restart, approval reopening, repair, closeout, merge or release occurred.",
    f"Input hashes and authority paths: INPUT_IDENTITIES.json. Prior accepted evidence manifest: `{prior_manifest}`; all 118 inventoried files verified. Handoff ZIP `{inputs['handoff_zip_sha256']}`: safe paths, exact 38-row inventory, extracted into its own scratch directory.",
    "",
    "## Per-check results",
    "",
    "| Check | ACs | Result | Evidence and rationale |",
    "|---|---|---|---|",
]
for r in results:
    report.append(f"| {r['id']} | {', '.join(r['mapped_acs'])} | {r['status']} | {r['rationale']} See `{r['evidence'][0]}`. |")
report.extend([
    "",
    "## Findings",
    "",
    "No FAIL or BLOCKED findings." if not findings else "\n".join(f"- {x['id']} ({x['severity']}): {x['basis']}" for x in findings),
    "",
    "The repaired finding was read at APP_ARCHITECTURE_MANUAL.md:501–520 and 592–619, and STATE_MANAGEMENT_MANUAL.md:793–830 and 864–909. Labels at ARCH:501/613 and STATE:809–810/866 agree with array consumers at ARCH:517/616 and STATE:827/877/887. See complete line-numbered containers in MANUAL_READS.md. PROPAGATION.tsv records all 29 literal occurrences, including the three imports that each match both search terms; this is 26 matching lines, not 29 distinct lines.",
    "",
    "WITHDRAWAL_ROWS.json contains all 31 rows: 8 PASS (FC-066 plus seven rows with re-read preserved sections in changed documents) and 23 CARRIED. FC-022 and FC-038 carry on exact document identity. No whole-file identity is claimed for ARCH or STATE.",
    "",
    "## Observations, separate from findings",
    "",
])
report.extend(f"- **{o['id']} — {o['scope']}:** {o['text']}" for o in observations)
report.extend([
    "",
    "## Preservation and stability",
    "",
    "QA_START.json and QA_END.json agree: local and actual remote branch tips are the pinned candidate, exact parent and branch match, the worktree is clean, local/remote main equal BASE, and all three canonical file hashes are stable. The candidate is one non-merge child of 8dff354; every adjacent link BASE→CONTENT→20f71ee→8dff354→26b050f is ancestral. Gate 2 at 2026-10-20T10:38:21.679686+06:00 precedes commit time 10:39:41+06:00. Post-commit handoff/commit/push receipts are correctly absent from their own commit; pre-commit carry/code records and approval match their committed copies.",
    "",
    "All 1,461 pre-existing files under the review RUN were fingerprinted and remain unchanged, including accepted evidence, both verdicts and approvals. The candidate's complete parent tree was compared with the successor tree and bytes. No Git write command was run. Candidate exports were created by git archive, not patch application. No BASE export was needed because protected-original checks were carried from accepted parent evidence on exact identity.",
    "",
    "## Limits and next owner",
    "",
    "These are documentation-level bounded results, not runtime/API/browser certification. No builds, installs, live service tests or deployment commands were run. Git history, current refs and receipts support structural grading; they cannot prove the absence of every past remote operation. Commit author personal details are redacted in delivered telemetry; presence and identity digests are retained. Instructional synthetic addresses and credential placeholders are retained.",
    "",
    "**All 12 closeout transitions on nine paths remain pending.** No transition was applied and no later closeout commit exists on the measured branch. Fable owns adjudication and the successor verdict. Stop for Fable; this report grants no merge or release authority.",
    "",
    "Evidence inventory is SHA256SUMS.txt (all evidence files except itself), verified after sealing. The final response gives its hash and the consolidated Downloads ZIP hash.",
])
report_text = "\n".join(report) + "\n"
(E / "EXECUTOR_REPORT.md").write_text(report_text)
now = datetime.datetime.now(datetime.timezone.utc)
response = ROOT / "agent_docs/RESPONSES" / ("response_" + now.strftime("%Y-%m-%d_%H%M%S") + "_amended-v3-executor-report.md")
response.write_text(report_text)
(E / "REPRODUCE.md").write_text(
    "# Reproduction\n\n"
    "Preserve this sealed evidence directory. Use a NEW empty evidence directory and NEW empty scratch directory. "
    "Copy scripts/ and RAW/context.json there, updating only evidence/scratch filesystem locations in the copied context. "
    "The review repo, execution worktree and pinned commit identities remain the named inputs. "
    "Run 01_preflight.py, 02_measure.py, 03_manual_evidence.py, 04_end.py with `python3 -B -I <script>` in that order. "
    "Network access is needed only for the two read-only ls-remote pin checks. Do not bypass a pin mismatch. "
    "Scripts 01/02/04 derive mechanical evidence; 03 records this Executor's explicit semantic decisions and must be independently read, not treated as an independent oracle. "
    "Script 05 records results, redacts author telemetry and seals the current directory; never rerun it over sealed evidence. "
    "No git apply, fetch, checkout, reset, add, commit, push, install or engineering helper is required.\n\n"
    "COMMANDS.json records verification commands/cwd/exit and safe stdout/stderr. Binary outputs use file pointers and hashes or export pointers. "
    "RAW/harness_invocations.json retains the two resolved wrapper failures; the missing-source traceback is summarized there. "
    "RAW/candidate_blobs contains independent git-show bytes for all 101 paths. Tree/hash JSON, canonical.diff, lints.txt, manual quotes and propagation decisions make the checks reviewable without running the scripts.\n"
)
save("RAW/script_hashes.json", {str(p.relative_to(E)): sha(p.read_bytes()) for p in sorted((E / "scripts").glob("*.py"))})
# The root inventory must also include copied prior manifests with the same basename.
inventory = [(str(p.relative_to(E)), sha(p.read_bytes())) for p in sorted(E.rglob("*"))
             if p.is_file() and p != E / "SHA256SUMS.txt"]
(E / "SHA256SUMS.txt").write_text("".join(f"{digest}  {name}\n" for name, digest in inventory))
assert all(sha((E / name).read_bytes()) == digest for name, digest in inventory)
print(json.dumps({"counts": counts, "evidence_files": len(inventory),
                  "manifest_sha256": sha((E / "SHA256SUMS.txt").read_bytes()),
                  "report_response": str(response)}, indent=2))
