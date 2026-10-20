#!/usr/bin/env python3
"""Fable (QA Lead) — Phase 4 QA readiness checks on the installed doc-sync candidate.
Read-only against Git and disk. Writes only QA_READINESS.json and QA_READINESS_RAW.txt
next to this script. Run: python3 -B -I qa_readiness.py
"""
import hashlib, json, os, subprocess, sys, zipfile, datetime

W = "/home/moose/Documents/app-factory-docs-sync-execution"
REVIEW = "/home/moose/Documents/app-factory-docs-v1"
RUN = "_AUDIT/SYNC_2026-10-15_doctrine-part2"
ZIP = "/home/moose/Downloads/FACTORY_PHASE3_ENGINEERING_HANDOFF_2026-10-18_212938.zip"
ZIP_SHA = "d12d0ff80c90090b16800bbd8b7c315dd2ebc4712d2dabf6cb67e75ad7c577ea"
BASE = "9c179392f79b70da099121fc357d3107ad3bb86e"
CONTENT = "ef35d26d82f1904da6ed33663ad647e4ee16fe98"
TIP = "20f71ee932ed21c0878cb3a0f39c6fbe90d0a793"
BRANCH = "docs/sync-doctrine-part2-2026-10-15"
SPEC = f"{RUN}/QA_RETEST_AF01/DOCSET_SYNC_ACCEPTANCE_SPEC_AMENDED_V1_R1.md"
SPEC_SHA = "2a3867cacef11c6bb0419a4c71229479efe703cee9fbcc1e4f71c0ac8e63f0fc"
PATCH_SHA = "cf6413c9340c80f5c1bf53a55385876470e9b3aad364bc8963f52a68580f2a6d"
HERE = os.path.dirname(os.path.abspath(__file__))
RAW = []
CHECKS = []

def sh(args, cwd=W):
    p = subprocess.run(args, cwd=cwd, capture_output=True)
    RAW.append({"cmd": args, "cwd": cwd, "exit": p.returncode,
                "stdout": p.stdout.decode("utf-8", "replace")[:4000],
                "stderr": p.stderr.decode("utf-8", "replace")[:2000]})
    return p

def out(args, cwd=W):
    return sh(args, cwd).stdout.decode("utf-8", "replace").strip()

def blob(rev, path):
    # deterministic content read; not logged to RAW to keep the raw record small
    return subprocess.run(["git", "show", f"{rev}:{path}"], cwd=W, capture_output=True).stdout

def sha(b): return hashlib.sha256(b).hexdigest()

def check(name, ok, detail):
    CHECKS.append({"check": name, "result": "PASS" if ok else "FAIL", "detail": detail})

# 1 handoff ZIP identity and inventory
with open(ZIP, "rb") as f: zs = sha(f.read())
check("ZIP SHA-256", zs == ZIP_SHA, zs)
z = zipfile.ZipFile(ZIP)
bad = z.testzip()
check("ZIP CRC", bad is None, f"first bad member: {bad}")
inv = z.read("SHA256SUMS.txt").decode().splitlines()
inv_ok = 0; inv_bad = []; payload_ok = 0; payload_bad = []
wrapper = {"DELIVERY_RECEIPT.json", "README_HANDOFF.md", "ENGINEERING_RESPONSE.md", "RECOVERY.md", "SHA256SUMS.txt"}
for line in inv:
    h, p = line.split("  ", 1)
    if sha(z.read(p)) == h: inv_ok += 1
    else: inv_bad.append(p)
    if p not in wrapper:
        if sha(blob(TIP, p)) == h: payload_ok += 1
        else: payload_bad.append(p)
check("ZIP inventory hashes", not inv_bad, f"{inv_ok}/{len(inv)} ok; bad={inv_bad[:5]}")
check("ZIP payload equals committed tip bytes", not payload_bad, f"{payload_ok} payload members equal git show {TIP[:7]}:<path>; bad={payload_bad[:5]}")

# 2 remote tip, worktree head, ancestry (read-only)
remote = out(["git", "ls-remote", "--heads", "origin", f"refs/heads/{BRANCH}"])
remote_sha = remote.split("\t")[0] if remote else ""
remote_main = out(["git", "ls-remote", "origin", "refs/heads/main"]).split("\t")[0]
head = out(["git", "rev-parse", "HEAD"])
branch = out(["git", "rev-parse", "--abbrev-ref", "HEAD"])
porcelain = out(["git", "status", "--porcelain"])
check("Remote branch tip == expected handoff HEAD", remote_sha == TIP, remote)
check("origin/main == BASE_SHA", remote_main == BASE, remote_main)
check("Worktree HEAD == remote tip", head == TIP and branch == BRANCH, f"{branch} @ {head}")
check("Worktree clean (porcelain empty)", porcelain == "", porcelain[:300])
a1 = sh(["git", "merge-base", "--is-ancestor", CONTENT, TIP]).returncode == 0
a2 = sh(["git", "merge-base", "--is-ancestor", BASE, CONTENT]).returncode == 0
log = out(["git", "log", "--format=%H %P %an %cs %s", f"{BASE}..{TIP}"])
check("CONTENT_SHA ancestor of tip; BASE ancestor of CONTENT_SHA", a1 and a2, log)
check("Implementation commit date == landing date 2026-10-18", out(["git", "log", "-1", "--format=%cs", CONTENT]) == "2026-10-18", out(["git", "log", "-1", "--format=%ci", CONTENT]))

# 3 approved specification and gate records at the candidate
check("Spec R1 SHA at candidate", sha(blob(TIP, SPEC)) == SPEC_SHA, SPEC)
dd = blob(TIP, f"{RUN}/QA_RETEST_AF01/DIRECTOR_DECISIONS.md").decode()
check("Gate 2/3 recorded APPROVED naming corrected patch and spec R1",
      "APPROVED — Gate 2" in dd and "APPROVED — Gate 3" in dd and PATCH_SHA in dd and SPEC_SHA in dd,
      "QA_RETEST_AF01/DIRECTOR_DECISIONS.md §1/§2")
rel = blob(TIP, f"{RUN}/PHASE3_EXECUTION/DIRECTOR_RELEASE.md").decode()
check("Phase 3 release + agent Git authorization recorded", "authorizes full" in rel and "supersedes Tony-only Git" in rel, "PHASE3_EXECUTION/DIRECTOR_RELEASE.md")
sr = json.loads(blob(TIP, f"{RUN}/EXECUTION_SETUP/SETUP_RECEIPT.json"))
check("Setup receipt: preservation/base/checkpoint/content identities",
      sr["preservation_commit_sha"] == "e7b4a6f33e1ae2442f71d82f7f3a9d694f50da36" and sr["fetched_remote_baseline_sha"] == BASE
      and sr["execution_checkpoint_sha"] == "356206ab293dc3a3987269636bb853c84aaf4ad3" and sr["content_sha"] == CONTENT,
      json.dumps({k: sr[k] for k in ("preservation_commit_sha", "fetched_remote_baseline_sha", "execution_checkpoint_sha", "setup_head", "content_sha")}))
hand = blob(TIP, f"{RUN}/SYNC_HANDOFF.md").decode()
check("SYNC_HANDOFF.md §0 names CONTENT_SHA", CONTENT in hand, "SYNC_HANDOFF.md")

# 4 AC1 set accounting over BASE..tip
idx = json.loads(blob(TIP, f"{RUN}/AMENDED_V1/EXECUTION_PROPOSAL_INDEX.json"))
sync = {i["path"]: i for i in idx}
ns = out(["git", "diff", "--name-status", BASE, TIP]).splitlines()
cat = {"sync": [], "10x": [], "run": [], "bookkeeping": [], "other": []}
for l in ns:
    st, p = l.split("\t", 1)
    if p in sync: cat["sync"].append(st)
    elif p.startswith("10x Lab/"): cat["10x"].append(p)
    elif p.startswith(RUN + "/"): cat["run"].append(p)
    elif p == "RECOVERY.md" or p.startswith(("agent_docs/SESSIONS/", "agent_docs/RESPONSES/")) or (p.startswith("session_") and p.endswith(".md")): cat["bookkeeping"].append(p)
    else: cat["other"].append(p)
check("AC1 set: 101 sync (33M/68A) + 2 standalone 10x + run/** + bookkeeping, nothing else",
      len(cat["sync"]) == 101 and cat["sync"].count("M") == 33 and cat["sync"].count("A") == 68 and len(cat["10x"]) == 2 and not cat["other"],
      f"sync={len(cat['sync'])} 10x={len(cat['10x'])} run={len(cat['run'])} bookkeeping={len(cat['bookkeeping'])} other={cat['other'][:10]} total={len(ns)}")
prot = {p: out(["git", "diff", "--name-only", BASE, TIP, "--", p]) for p in ("lints", ".github", "_SKILLS", "CLAUDE.md", "AGENTS.md", "factory-corrections", "factory-intake", "_INBOX")}
check("Protected paths unchanged BASE..tip", all(v == "" for v in prot.values()), json.dumps({k: v[:100] for k, v in prot.items()}))

# 5 bound index vs committed bytes at CONTENT_SHA
bound = json.loads(blob(TIP, f"{RUN}/BOUND_EXECUTION_INDEX.json"))
ok = 0; bad = []
for i in bound:
    b = blob(CONTENT, i["path"])
    if sha(b) == i["proposed_sha256"] and len(b) == i["bytes"] and i["review_proposed_sha256"] == sync[i["path"]]["proposed_sha256"]: ok += 1
    else: bad.append(i["path"])
check("BOUND_EXECUTION_INDEX: 101 committed hashes/bytes equal; review hashes equal amended index", ok == 101 and not bad, f"{ok}/101 bad={bad[:5]}")
same_at_tip = sum(1 for i in bound if sha(blob(TIP, i["path"])) == i["proposed_sha256"])
check("101 sync paths unchanged between CONTENT_SHA and tip", same_at_tip == 101, f"{same_at_tip}/101")

# 6 conditional transitions still pre-closeout
tr = json.loads(blob(TIP, f"{RUN}/BOUND_STATUS_TRANSITIONS.json"))
pre = []
for x in tr["transitions"]:
    body = blob(TIP, x["path"]).decode("utf-8", "replace")
    pre.append(body.count(x["old"]) == x["occurrences"] and (x["new"] not in body or x["new"] in x["old"]))
check("12 conditional transitions on 9 paths pending (old spans present, new absent)", all(pre) and len(tr["transitions"]) == 12 and len({x["path"] for x in tr["transitions"]}) == 9, f"{sum(pre)}/12; label={tr['label']}")

# 7 snapshot, 10x, archive restoration, lints
snapidx = json.loads(blob(TIP, f"{RUN}/INTAKE_SNAPSHOT_INDEX.json"))
snap = snapidx["files"]  # paths relative to snapidx["snapshot"]
sok = sum(1 for s in snap if sha(blob(TIP, f"{snapidx['snapshot']}/{s['path']}")) == s["sha256"] and len(blob(TIP, f"{snapidx['snapshot']}/{s['path']}")) == s["bytes"])
mod = out(["git", "log", "--diff-filter=M", "--format=%h", f"{BASE}..{TIP}", "--", f"{RUN}/INTAKE_SNAPSHOT"])
check("INTAKE_SNAPSHOT 189 files byte-identical to index; never modified", sok == 189 == len(snap) and mod == "", f"{sok}/{len(snap)}; modified-commits='{mod}'")
tenx = json.loads(blob(TIP, f"{RUN}/EXECUTION_SETUP/STANDALONE_10X_AUTHORIZATION.json"))["files"]
tok = []
for f in tenx:
    with open(f["source"], "rb") as fh: s_src = sha(fh.read())
    tok.append(s_src == f["source_sha256"] == sha(blob(TIP, f["destination"])))
check("Two standalone 10x files exact copies of /home/moose/Documents sources", all(tok) and len(tok) == 2, json.dumps([(f["destination"], f["destination_sha256"][:12]) for f in tenx]))
check("AC24 blob: _ARCHIVE/QA_PLAYBOOK_v1_0.md", out(["git", "rev-parse", f"{TIP}:_ARCHIVE/QA_PLAYBOOK_v1_0.md"]) == "bb41260f6b6f94372a682f04b313a451f2b3c4b1", out(["git", "rev-parse", f"{TIP}:_ARCHIVE/QA_PLAYBOOK_v1_0.md"]))
lint = sh(["python3", "-B", "-I", "lints/run_all.py"])
check("Pinned lint suite at candidate worktree exits 0 / RESULT: PASS", lint.returncode == 0 and b"=== RESULT: PASS ===" in lint.stdout, lint.stdout.decode()[:400])
check("Worktree still clean after lint", out(["git", "status", "--porcelain"]) == "", "")

now = datetime.datetime.now().astimezone().isoformat()
res = {"seat": "Fable (QA Lead)", "purpose": "Phase 4 QA readiness — not the product verdict", "time": now,
       "qa_start_sha_remote_read": remote_sha, "content_sha": CONTENT, "base_sha": BASE, "spec_sha256": SPEC_SHA,
       "checks": CHECKS, "overall": "READY" if all(c["result"] == "PASS" for c in CHECKS) else "NOT READY"}
json.dump(res, open(os.path.join(HERE, "QA_READINESS.json"), "w"), indent=2)
json.dump(RAW, open(os.path.join(HERE, "QA_READINESS_RAW.json"), "w"), indent=2)
for c in CHECKS: print(f"[{c['result']}] {c['check']} — {c['detail'][:160]}")
print("OVERALL:", res["overall"], now)
sys.exit(0 if res["overall"] == "READY" else 1)
