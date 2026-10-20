import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import *
import difflib, re, shutil

A, B, H = S / "parent", S / "candidate", S / "handoff"
PRIOR = ROOT / RUN / "QA_PHASE4/RETEST_AMENDED_V2/EXECUTOR_EVIDENCE"
ARCH = "04_REFERENCE_MANUALS/APP_ARCHITECTURE_MANUAL.md"
STATE = "04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md"
CANON = {ARCH, STATE, "CHANGELOG.md"}
checks = {}

def check(key, value, detail=None):
    checks[key] = {"ok": bool(value), "detail": detail}

def copy_input(source, relative):
    target = E / "RAW/inputs" / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(source.read_bytes())

# Protect all existing review-run material, including records never committed.
protected_review = {}
for p in sorted((ROOT / RUN).rglob("*")):
    if p.is_file() and not p.is_relative_to(E):
        protected_review[str(p.relative_to(ROOT))] = sha(p.read_bytes())
save("RAW/review_protected_start.json", protected_review)

pinned = {
    "AMENDED_V3/BOUND_EXECUTION_INDEX.json": "55537c6411724ab78837d0191d61375654839202acbf15b13a76d98aa8d483e6",
    "AMENDED_V3/EXECUTION_PROPOSAL.patch": "afd8f9249854d4e99c385b1e21c459fa297fa5ed5ddcac782d1509747c43faed",
    "AMENDED_V3/DIRECTOR_DECISIONS_V3.md": "1fa28bc81dedd96f017f9ffc9a69b7a86326917a61093e9aeb9390bcfbe300a4",
    "QA_RETEST_AF01/DOCSET_SYNC_ACCEPTANCE_SPEC_AMENDED_V1_R1.md": "2a3867cacef11c6bb0419a4c71229479efe703cee9fbcc1e4f71c0ac8e63f0fc",
}
identities = []
for p, expected in pinned.items():
    blob = git("show", f"{CAND}:{RUN}/{p}", binary_output=f"RAW/inputs/candidate/{p}").stdout
    sources = {"committed": sha(blob), "export": sha((B / RUN / p).read_bytes()),
               "review": sha((ROOT / RUN / p).read_bytes())}
    if (H / p).exists():
        sources["zip"] = sha((H / p).read_bytes())
    identities.append({"path": RUN + "/" + p, "expected": expected, "observed": sources,
                       "match": all(v == expected for v in sources.values())})
prior_manifest = sha((PRIOR / "SHA256SUMS.txt").read_bytes())
check("prior_manifest_identity", prior_manifest == "379dd10450157d0c394684ed7d460d65e42006c7d2a8974e9c778329ad318c38")
prior_rows = []
for line in (PRIOR / "SHA256SUMS.txt").read_text().splitlines():
    digest, name = line.split(maxsplit=1)
    name = name.lstrip("* ")
    actual = sha((PRIOR / name).read_bytes())
    prior_rows.append({"path": name, "expected": digest, "actual": actual, "match": digest == actual})
save("RAW/prior_inventory.json", prior_rows)
check("prior_inventory", all(x["match"] for x in prior_rows), len(prior_rows))
check("input_pins", all(x["match"] for x in identities))
authority = [
    "QA_PHASE4/RETEST_AMENDED_V3/QA_EXECUTOR_PROMPT.md",
    "QA_PHASE4/RETEST_AMENDED_V2/QA_LEAD_VERDICT_V2.md",
    "QA_PHASE4/RETEST_AMENDED_V2/JARVIS_REPAIR_RECOMMENDATION.md",
    "QA_PHASE4/QA_LEAD_VERDICT.md", "QA_PHASE4/OVERRIDES_AND_ALIGNMENT.md",
    "QA_RETEST_AF01/DIRECTOR_DECISIONS.md",
    "EXECUTION_SETUP/GIT_AUTHORIZATION_2026-10-18.md",
    "PHASE3_EXECUTION/DIRECTOR_RELEASE.md",
    "QA_PHASE4/REPAIR_QA_P4/DIRECTOR_DECISIONS_V2.md",
]
authority_rows = []
for p in authority:
    source = ROOT / RUN / p
    if not source.exists():
        source = B / RUN / p
    copy_input(source, "authority/" + p)
    authority_rows.append({"path": RUN + "/" + p, "sha256": sha(source.read_bytes()),
                           "read_from": str(source),
                           "present_at_parent": (A / RUN / p).exists(),
                           "present_at_candidate": (B / RUN / p).exists()})
for name in ["SHA256SUMS.txt", "R_RESULTS.json", "WITHDRAWAL_ROWS.json"]:
    copy_input(PRIOR / name, "prior/" + name)
save("INPUT_IDENTITIES.json", {
    "candidate": CAND, "parent": PARENT, "base": BASE,
    "handoff_zip_sha256": sha(Path("/home/moose/Downloads/FACTORY_AMENDED_V3_EXECUTION_HANDOFF_2026-10-20_104051.zip").read_bytes()),
    "pinned_records": identities, "prior_manifest_sha256": prior_manifest, "authority_chain": authority_rows,
    "precedence": "Frozen spec + Director rulings + preserved Fable verdicts; attributable AMENDED-v3 Gate 2; bounded assignment. Engineering results are hypotheses only."
})

cross = []
for p in ["AMENDED_V3_EXECUTION/FABLE_HANDOFF.md", "AMENDED_V3/DIRECTOR_DECISIONS_V3.md",
          "AMENDED_V3_EXECUTION/COMMIT_RECEIPT.json", "AMENDED_V3_EXECUTION/PUSH_RECEIPT.json",
          "AMENDED_V3_EXECUTION/STATE_CARRY_FORWARD.json", "AMENDED_V3_EXECUTION/CODE_PRESERVATION.json"]:
    z = (H / p).read_bytes()
    committed = B / RUN / p
    review = ROOT / RUN / p
    cross.append({"path": p, "zip_sha256": sha(z), "review_equal": review.read_bytes() == z,
                  "committed": committed.exists(),
                  "committed_equal": committed.read_bytes() == z if committed.exists() else None,
                  "basis": "Compare committed bytes where present; handoff and commit/push receipts are post-commit records."})
    copy_input(H / p, "handoff/" + p)
save("RAW/handoff_crosscheck.json", cross)
check("handoff_crosscheck", all(x["review_equal"] and x["committed_equal"] is not False for x in cross))

def tree(ref, label):
    raw = git("ls-tree", "-r", "-z", ref, binary_output=f"RAW/{label}_tree.raw").stdout
    entries = {}
    for row in raw.split(b"\0"):
        if not row:
            continue
        meta, path = row.split(b"\t", 1)
        mode, kind, oid = meta.decode().split()
        entries[path.decode()] = {"mode": mode, "kind": kind, "blob": oid}
    save(f"RAW/{label}_tree.json", entries)
    return entries

ta, tb = tree(PARENT, "parent"), tree(CAND, "candidate")
delta = []
for path in sorted(ta.keys() | tb.keys()):
    if ta.get(path) != tb.get(path):
        kind = "added" if path not in ta else "deleted" if path not in tb else "modified"
        lane = ("canonical" if path in CANON else "additive_record"
                if path.startswith((RUN + "/AMENDED_V3/", RUN + "/AMENDED_V3_EXECUTION/"))
                else "OUTSIDE")
        delta.append({"path": path, "change": kind, "lane": lane, "parent": ta.get(path), "candidate": tb.get(path)})
save("RAW/scope.json", delta)
check("scope_56", len(delta) == 56)
check("scope_canonical", {x["path"] for x in delta if x["lane"] == "canonical"} == CANON
      and all(x["change"] == "modified" for x in delta if x["lane"] == "canonical"))
check("scope_additions", len([x for x in delta if x["lane"] == "additive_record"]) == 53
      and all(x["change"] == "added" for x in delta if x["lane"] == "additive_record"))
check("scope_no_other", all(x["lane"] != "OUTSIDE" for x in delta))
git("diff", "--no-ext-diff", "--no-renames", PARENT, CAND, "--", *sorted(CANON),
    binary_output="RAW/canonical.diff")
git("diff", "--no-ext-diff", "--name-status", "--no-renames", PARENT, CAND,
    binary_output="RAW/changed_paths.txt")

index = json.loads((B / RUN / "AMENDED_V3/BOUND_EXECUTION_INDEX.json").read_text())
hashes = []
for row in index:
    p = row["path"]
    blob = git("show", f"{CAND}:{p}", binary_output="RAW/candidate_blobs/" + p).stdout
    installed, parent, exported = (WT / p).read_bytes(), (A / p).read_bytes(), (B / p).read_bytes()
    proposed = B / RUN / "AMENDED_V3/PROPOSED_CONTENT" / p
    hashes.append({"path": p, "index_sha256": row["proposed_sha256"], "installed_sha256": sha(installed),
                   "blob_sha256": sha(blob), "export_sha256": sha(exported), "parent_sha256": sha(parent),
                   "equal_index": sha(installed) == sha(blob) == sha(exported) == row["proposed_sha256"],
                   "unchanged_parent": parent == blob, "byte_count_ok": len(blob) == row["bytes"],
                   "proposal_equal": proposed.read_bytes() == blob if proposed.exists() else None})
save("RAW/index_hashes.json", hashes)
check("installation_101", len(index) == len({x["path"] for x in index}) == 101
      and all(x["equal_index"] and x["byte_count_ok"] for x in hashes))
check("unchanged_98", sum(x["unchanged_parent"] for x in hashes) == 98)
check("three_proposals", {x["path"] for x in hashes if not x["unchanged_parent"]} == CANON
      and all(x["proposal_equal"] for x in hashes if x["path"] in CANON))
indexed = {x["path"] for x in index}
preserved = []
for p in sorted(ta):
    a, b = (A / p).read_bytes(), (B / p).read_bytes() if p in tb else b""
    preserved.append({"path": p, "parent_sha256": sha(a), "candidate_sha256": sha(b),
                      "bytes_equal": a == b, "tree_equal": ta[p] == tb.get(p), "indexed": p in indexed})
save("RAW/preexisting_paths.json", preserved)
check("outside_101_preserved", all(x["bytes_equal"] and x["tree_equal"] for x in preserved if not x["indexed"]))
protected = {}
for prefix in ["_ARCHIVE/", "03_BUILD_METHODOLOGY/_templates/QAM/", "03_BUILD_METHODOLOGY/_workflows/",
               "03_BUILD_METHODOLOGY/_assets/workflows/", "10x Lab/", "_SKILLS/", "lints/", ".github/", RUN + "/"]:
    pa = {p: v for p, v in ta.items() if p.startswith(prefix)}
    pb = {p: v for p, v in tb.items() if p.startswith(prefix)}
    old_equal = all(pb.get(p) == v for p, v in pa.items())
    protected[prefix] = {"parent_count": len(pa), "candidate_count": len(pb),
                         "existing_equal": old_equal, "exact_tree_equal": pa == pb}
save("RAW/protected_trees.json", protected)
check("protected_surfaces", all(x["exact_tree_equal"] for p, x in protected.items() if p != RUN + "/"))
check("frozen_records", protected[RUN + "/"]["existing_equal"])
check("root_files", all(ta[p] == tb.get(p) for p in ta if "/" not in p and p != "CHANGELOG.md"))

# Independently account for the exact eight declared edits; no patch application.
edits = json.loads((B / RUN / "AMENDED_V3/AMENDMENT_V3_EDITS.json").read_text())
copy_input(B / RUN / "AMENDED_V3/AMENDMENT_V3_EDITS.json", "candidate/AMENDED_V3/AMENDMENT_V3_EDITS.json")
edit_rows = []
for e in edits:
    a, b = (A / e["path"]).read_text(), (B / e["path"]).read_text()
    edit_rows.append({"id": e["edit_id"], "path": e["path"], "old_count_parent": a.count(e["old"]),
                      "new_count_candidate": b.count(e["new"]),
                      "candidate_line": b[:b.find(e["new"])].count("\n") + 1})
save("RAW/edit_locations.json", edit_rows)
check("eight_edits_present", len(edits) == 8 and all(x["old_count_parent"] == x["new_count_candidate"] == 1 for x in edit_rows))
# Reverse only declared additions in memory to prove there is no hidden executable delta.
reversed_rows = []
for path in sorted(CANON):
    b = (B / path).read_bytes()
    for e in reversed(edits):
        if e["path"] == path:
            b = b.replace(e["new"].encode(), e["old"].encode(), 1)
    reversed_rows.append({"path": path, "restores_parent_exactly": b == (A / path).read_bytes()})
save("RAW/edit_accounting.json", reversed_rows)
check("only_eight_edits", all(x["restores_parent_exactly"] for x in reversed_rows))

code_rows = []
for path in [ARCH, STATE]:
    contents = []
    for source in [A, B]:
        text = (source / path).read_text()
        fences = re.findall(r"^```[^\n]*\n(.*?)^```[ \t]*$", text, re.M | re.S)
        code = [b"".join(line for line in f.encode().splitlines(keepends=True)
                        if not line.lstrip().startswith(b"//")) for f in fences]
        imports = re.findall(r"^import\b.*$", text, re.M)
        contents.append((code, imports))
    code_rows.append({"path": path, "parent_fences": len(contents[0][0]),
                      "candidate_fences": len(contents[1][0]),
                      "non_comment_fenced_bytes_equal": contents[0][0] == contents[1][0],
                      "imports_equal": contents[0][1] == contents[1][1]})
save("RAW/code_preservation.json", code_rows)
check("code_imports_unchanged", all(x["non_comment_fenced_bytes_equal"] and x["imports_equal"] for x in code_rows))

clause = "; QA-P4 repair: RV2-F01 (AC16/FC-066 labels)"
metadata = {}
for path, version in [(ARCH, "1.4"), (STATE, "1.3")]:
    a, b = (A / path).read_text().splitlines(), (B / path).read_text().splitlines()
    headers = [line for line in b[:15] if "**Version:**" in line]
    history_a = a[a.index("## Version History"):]
    history_b = b[b.index("## Version History"):]
    rows_a, rows_b = [l for l in history_a if l.startswith("|")], [l for l in history_b if l.startswith("|")]
    changed_rows = [(x, y) for x, y in zip(rows_a, rows_b) if x != y]
    metadata[path] = {"header": headers, "header_prefix_equal": a[:15] == b[:15],
                      "history_rows_parent": len(rows_a), "history_rows_candidate": len(rows_b),
                      "changed_history_rows": changed_rows,
                      "only_clause_added": len(changed_rows) == 1 and changed_rows[0][1].replace(clause, "") == changed_rows[0][0],
                      "version_expected": version}
a, b = (A / "CHANGELOG.md").read_text().splitlines(), (B / "CHANGELOG.md").read_text().splitlines()
runrows = [{"line": i, "text": l} for i, l in enumerate(b, 1) if l.startswith("| 2026-10-18 |")]
changes = [{"line": i, "old": x, "new": y} for i, (x, y) in enumerate(zip(a, b), 1) if x != y]
previous_clauses = [{"line": i, "text": l, "unchanged": i <= len(a) and a[i-1] == l}
                    for i, l in enumerate(b, 1) if "QA-P4 repair:" in l and "RV2-F01" not in l]
metadata["changelog"] = {"run_rows": runrows, "changes": changes, "same_line_count": len(a) == len(b),
                         "previous_clauses": previous_clauses}
metadata["manifest_unchanged"] = (A / "MANIFEST.md").read_bytes() == (B / "MANIFEST.md").read_bytes()
save("RAW/metadata.json", metadata)
check("manual_metadata", all(metadata[p]["header_prefix_equal"] and metadata[p]["only_clause_added"]
      and metadata[p]["history_rows_parent"] == metadata[p]["history_rows_candidate"] for p in [ARCH, STATE]))
check("changelog_metadata", len(runrows) == 39 and [x["line"] for x in changes] == [56, 60]
      and len(a) == len(b) and all(x["new"].replace(clause, "") == x["old"] for x in changes)
      and len(previous_clauses) == 6 and all(x["unchanged"] for x in previous_clauses))
check("manifest_unchanged", metadata["manifest_unchanged"])

lint = command(["python3", "-B", "-I", "lints/run_all.py"], cwd=B, binary_output="RAW/lints.txt")
check("lint_exit", lint.returncode == 0, lint.stderr.decode())

transitions = json.loads((B / RUN / "BOUND_STATUS_TRANSITIONS.json").read_text())
v3trans = json.loads((B / RUN / "AMENDED_V3/CLOSEOUT_TRANSITIONS.json").read_text())
tr = []
for row in transitions["transitions"]:
    p, old, new = row["path"], row["old"], row["new"]
    text = (B / p).read_text()
    tr.append({"path": p, "old": old, "new": new, "old_count": text.count(old), "new_count": text.count(new),
               "line": text[:text.find(old)].count("\n") + 1,
               "v3_plan_match": any(v["path"] == p and v["old"] == old and v["status"] == "PENDING" for v in v3trans)})
save("RAW/transitions.json", tr)
check("transitions_pending", len(tr) == 12 and len({x["path"] for x in tr}) == 9
      and all(x["old_count"] == 1 and x["new_count"] == 0 and x["v3_plan_match"] for x in tr))
after = git("log", "--format=%H %s", CAND + "..HEAD")
check("no_later_local_commit", after.returncode == 0 and not after.stdout)

gate = (B / RUN / "AMENDED_V3/DIRECTOR_DECISIONS_V3.md").read_text()
gate_time = datetime.datetime.fromisoformat(re.search(r"Recorded at: ([^\n]+)", gate)[1])
commit = git("show", "-s", "--format=%P%n%cI%n%s%n%an", CAND).stdout.decode().splitlines()
receipt = json.loads((H / "AMENDED_V3_EXECUTION/COMMIT_RECEIPT.json").read_text())
push = json.loads((H / "AMENDED_V3_EXECUTION/PUSH_RECEIPT.json").read_text())
auth = {"gate_time": gate_time.isoformat(), "commit_time": commit[1], "parent": commit[0],
        "subject": commit[2], "author_present": bool(commit[3].strip()),
        "author_identity_sha256": sha(commit[3].encode()),
        "approval_precedes_commit": gate_time < datetime.datetime.fromisoformat(commit[1]),
        "receipt_matches": receipt["commit"] == CAND and receipt["parent"] == PARENT and receipt["subject"] == commit[2],
        "push_receipt_matches": push["local_sha"] == push["remote_sha"] == CAND and push["remote_main"] == BASE,
        "push_command_nonforce": push["push_command"]["command"] == ["git", "push", "origin", "HEAD:refs/heads/" + BRANCH],
        "limitation": "Present refs, ancestry and receipts establish structure; they cannot prove absence of every historical remote operation."}
save("RAW/authorization.json", auth)
check("authorization", auth["approval_precedes_commit"] and auth["receipt_matches"] and auth["push_receipt_matches"]
      and auth["push_command_nonforce"] and auth["author_present"] and commit[0] == PARENT
      and commit[2] == "repair QA-P4 RV2-F01 (AMENDED-v3 " + pinned["AMENDED_V3/BOUND_EXECUTION_INDEX.json"] + ")")

# Exact R5 passages from independent git-show blobs at both commits.
sb = {}
for label, ref in [("parent", PARENT), ("candidate", CAND)]:
    sb[label] = git("show", f"{ref}:{STATE}", binary_output=f"RAW/{label}_state.md").stdout
la, lb = (sb[k].splitlines(keepends=True) for k in ["parent", "candidate"])
passages = []
for title, start, end in [("Persistence", 475, 620), ("Hydration & SSR", 621, 658),
                          ("Store Templates", 659, 790), ("Raw-contact exclusion", 519, 519),
                          ("RUL-13 default", 779, 786)]:
    a, b = b"".join(la[start-1:end]), b"".join(lb[start-1:end])
    passages.append({"title": title, "start": start, "end": end, "parent_sha256": sha(a),
                     "candidate_sha256": sha(b), "equal": a == b})
first = next((i for i, (a, b) in enumerate(zip(la, lb), 1) if a != b), None)
save("RAW/state_passages.json", {"whole_file_equal": sb["parent"] == sb["candidate"],
     "prefix_lines_1_808_equal": la[:808] == lb[:808], "first_differing_line": first, "passages": passages})
check("state_passages", first == 809 and la[:808] == lb[:808] and all(x["equal"] for x in passages))

groups = {
    "R1": ["01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md"] +
          ["02_PIPELINE_AGENTS/" + x + "_PLAYBOOK.md" for x in ["ARCHITECT", "DESIGNER", "ENGINEER", "HANDOFF_PACKAGE"]] +
          ["03_BUILD_METHODOLOGY/" + x + "_PLAYBOOK.md" for x in ["FFM", "BIM"]],
    "R2": ["02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md", "03_BUILD_METHODOLOGY/QAM_PLAYBOOK.md", "03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md"],
    "R3": ["02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md"],
    "R5_prime_other": ["03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md", "04_REFERENCE_MANUALS/AUTH_MANUAL.md",
                       "04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md"],
    "R9": [x["path"] for x in preserved if x["path"].startswith(("_ARCHIVE/", "03_BUILD_METHODOLOGY/_templates/QAM/",
               "03_BUILD_METHODOLOGY/_workflows/", "03_BUILD_METHODOLOGY/_assets/workflows/", "10x Lab/", RUN + "/"))]
}
carried = {}
by_path = {x["path"]: x for x in preserved}
for k, paths in groups.items():
    carried[k] = [by_path[p] for p in paths]
    check("carry_" + k, all(by_path[p]["bytes_equal"] and by_path[p]["tree_equal"] for p in paths))
save("RAW/carry_forward.json", carried)

live = sorted(B.glob("0[1-5]_*/*.md")) + [B / "MANIFEST.md", B / "CHANGELOG.md"]
workflows = sorted(B.glob("03_BUILD_METHODOLOGY/_workflows/*.md"))
svgs = sorted(B.glob("03_BUILD_METHODOLOGY/_assets/workflows/*.svg"))
check("live_scope_counts", [len(live), len(workflows), len(svgs)] == [36, 4, 4])
scope = [str(p.relative_to(B)) for p in live + workflows + svgs]
save("RAW/live_scope.json", scope)
hits = []
for p in scope:
    for i, line in enumerate((B / p).read_text().splitlines(), 1):
        matches = [m.group() for m in re.finditer(r"fetchProducts|services/productServices", line, re.I)]
        if matches:
            hits.append({"path": p, "line": i, "matches": matches, "text": line})
save("RAW/propagation_hits.json", hits)
command(["rg", "-n", "-i", "fetchProducts|services/productServices", *scope], cwd=B,
        binary_output="RAW/propagation_rg.txt")
save("RAW/automated_checks.json", checks)
print(json.dumps({"checks": len(checks), "failed": [k for k, v in checks.items() if not v["ok"]],
                  "hits": len(hits), "changed_paths": len(delta), "first_state_difference": first}, indent=2))
