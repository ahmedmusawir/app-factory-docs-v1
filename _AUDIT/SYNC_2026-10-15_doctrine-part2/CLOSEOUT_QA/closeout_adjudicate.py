#!/usr/bin/env python3
"""Fable QA Lead — independent bounded closeout verification of 4c54292 vs dc3b288.
Read-only: reads fresh git-archive exports and the handoff package; runs the lint suite on the
candidate export; writes evidence JSON to the output path. No Git mutation."""
import hashlib, json, os, re, subprocess, sys, datetime
CAND_SHA="4c542922d57ca3b2acf4391082a37383744ea192"; PARENT_SHA="dc3b288246ea931962e889e9a88718c0daaf9c37"
PRODUCT_SHA="26b050fe70de66e74ec8d65bcf9287d4369a91f7"; MAIN_SHA="9c179392f79b70da099121fc357d3107ad3bb86e"
EXP, PKG, EXEC_WT, OUT = sys.argv[1:5]
RUN="_AUDIT/SYNC_2026-10-15_doctrine-part2"
C=os.path.join(EXP,"cand"); P=os.path.join(EXP,"parent")
def sha(p): h=hashlib.sha256(); h.update(open(p,"rb").read()); return h.hexdigest()
def rd(p): return open(p,"rb").read()
def git(*a): return subprocess.run(["git",*a],cwd=EXEC_WT,capture_output=True,text=True).stdout.strip()
EV={"candidate":CAND_SHA,"parent":PARENT_SHA,"generated":datetime.datetime.now(datetime.timezone.utc).isoformat(),"checks":[]}
def check(cid,title,ok,detail): EV["checks"].append({"id":cid,"title":title,"result":"PASS" if ok else "FAIL","detail":detail}); print(("PASS " if ok else "FAIL ")+cid+" "+title)

CANON=["03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md","03_BUILD_METHODOLOGY/QAM_PLAYBOOK.md","03_BUILD_METHODOLOGY/RRM_PLAYBOOK.md","03_BUILD_METHODOLOGY/_templates/QAM/README.md","03_BUILD_METHODOLOGY/_workflows/BIM_WORKFLOW.md","03_BUILD_METHODOLOGY/_workflows/FFM_CREATION.md","03_BUILD_METHODOLOGY/_workflows/FFM_DEPLOYMENT.md","03_BUILD_METHODOLOGY/_workflows/FFM_EXECUTION.md","MANIFEST.md"]
REPORTS=[RUN+"/RUN_SUMMARY.md",RUN+"/TEMPLATE_INSTALL_VERIFICATION.md"]

# ---- G: git state (read-only)
head=git("rev-parse","HEAD"); branch=git("rev-parse","--abbrev-ref","HEAD"); status=git("status","--porcelain")
parents=git("rev-list","--parents","-n1",CAND_SHA).split()
remote=git("ls-remote","origin","refs/heads/docs/sync-doctrine-part2-2026-10-15","refs/heads/main")
rem={l.split("\t")[1]:l.split("\t")[0] for l in remote.splitlines()}
anc=subprocess.run(["git","merge-base","--is-ancestor",PRODUCT_SHA,PARENT_SHA],cwd=EXEC_WT).returncode==0
meta=git("cat-file","-p",CAND_SHA); ctime=int(re.search(r"committer .* (\d+) [+-]\d{4}",meta).group(1))
commit_utc=datetime.datetime.fromtimestamp(ctime,datetime.timezone.utc).isoformat()
check("G1","Local HEAD and remote branch both equal candidate; one non-merge parent dc3b288",
      head==CAND_SHA and rem.get("refs/heads/docs/sync-doctrine-part2-2026-10-15")==CAND_SHA and parents==[CAND_SHA,PARENT_SHA],
      {"head":head,"branch":branch,"remote_branch":rem.get("refs/heads/docs/sync-doctrine-part2-2026-10-15"),"parents":parents[1:]})
check("G2","Execution tree clean (before QA records are added); main unchanged locally and on remote",
      status=="" and rem.get("refs/heads/main")==MAIN_SHA and git("rev-parse","main")==MAIN_SHA,
      {"status_porcelain_lines":len(status.splitlines()),"remote_main":rem.get("refs/heads/main"),"local_main":git("rev-parse","main")})
check("G3","Certified product commit 26b050f is an ancestor of parent dc3b288",anc,{"ancestor":anc,"commit_time_utc":commit_utc,"subject":meta.splitlines()[-1]})

# ---- Package identities
pkg_ids={"CLOSEOUT.patch":sha(f"{PKG}/RUN/PHASE5_CLEANUP/CLOSEOUT.patch"),"CLOSEOUT_SUCCESSOR_INDEX.json":sha(f"{PKG}/RUN/PHASE5_CLEANUP/CLOSEOUT_SUCCESSOR_INDEX.json"),
 "ARCHITECT_CLEANUP_ACCEPTANCE.md":sha(f"{PKG}/RUN/CLOSEOUT_EXECUTION/ARCHITECT_CLEANUP_ACCEPTANCE.md"),"ARCHITECT_ACTIVATION_INSTRUCTION.md":sha(f"{PKG}/RUN/CLOSEOUT_EXECUTION/ARCHITECT_ACTIVATION_INSTRUCTION.md")}
cand_ids={"CLOSEOUT.patch":sha(f"{C}/{RUN}/PHASE5_CLEANUP/CLOSEOUT.patch"),"CLOSEOUT_SUCCESSOR_INDEX.json":sha(f"{C}/{RUN}/PHASE5_CLEANUP/CLOSEOUT_SUCCESSOR_INDEX.json"),
 "ARCHITECT_CLEANUP_ACCEPTANCE.md":sha(f"{C}/{RUN}/CLOSEOUT_EXECUTION/ARCHITECT_CLEANUP_ACCEPTANCE.md"),"ARCHITECT_ACTIVATION_INSTRUCTION.md":sha(f"{C}/{RUN}/CLOSEOUT_EXECUTION/ARCHITECT_ACTIVATION_INSTRUCTION.md")}
exp_ids={"CLOSEOUT.patch":"127230024105899fb67b8172212d96a574dc0d9fefedf82a9f26f365f3d4fa3e","CLOSEOUT_SUCCESSOR_INDEX.json":"d46ed5ae0f70c7ad1ea1b55a4df9fae67c2e97a53dbf8c559593e9635f651e0c",
 "ARCHITECT_CLEANUP_ACCEPTANCE.md":"e2a772f7e37eef19ca3f9521d27ba0b85babeec4f96991357cc87973644bce68","ARCHITECT_ACTIVATION_INSTRUCTION.md":"3d19b1d439ea460dbec1795aa124207a9d2dfd3bfe79159390199008075de567"}
patch_in_parent=sha(f"{P}/{RUN}/PHASE5_CLEANUP/CLOSEOUT.patch"); idx_in_parent=sha(f"{P}/{RUN}/PHASE5_CLEANUP/CLOSEOUT_SUCCESSOR_INDEX.json")
check("A1","Approved patch/index and both Architect decision records: package == candidate commit == recorded hashes; patch/index already present in parent",
      pkg_ids==cand_ids==exp_ids and patch_in_parent==exp_ids["CLOSEOUT.patch"] and idx_in_parent==exp_ids["CLOSEOUT_SUCCESSOR_INDEX.json"],{"package":pkg_ids,"candidate":cand_ids,"parent_patch":patch_in_parent,"parent_index":idx_in_parent})
# chronology
pre=json.load(open(f"{C}/{RUN}/CLOSEOUT_EXECUTION/PRE_APPLICATION_DECISION_RECEIPT.json"))
apply_cmds=json.load(open(f"{C}/{RUN}/CLOSEOUT_EXECUTION/APPLY_COMMANDS.json"))
apply_t=[c["time"] for c in apply_cmds if c["command"][:2]==["git","apply"] and "--check" not in c["command"]][0]
accept_txt=rd(f"{C}/{RUN}/CLOSEOUT_EXECUTION/ARCHITECT_CLEANUP_ACCEPTANCE.md").decode(); act_txt=rd(f"{C}/{RUN}/CLOSEOUT_EXECUTION/ARCHITECT_ACTIVATION_INSTRUCTION.md").decode()
rec_t=re.search(r"at (2026-\S+?),",accept_txt).group(1); rec_t2=re.search(r"at (2026-\S+?),",act_txt).group(1)
dec_ok=(pre["decisions"]["ARCHITECT_CLEANUP_ACCEPTANCE.md"]==exp_ids["ARCHITECT_CLEANUP_ACCEPTANCE.md"] and pre["decisions"]["ARCHITECT_ACTIVATION_INSTRUCTION.md"]==exp_ids["ARCHITECT_ACTIVATION_INSTRUCTION.md"])
chron=rec_t<pre["time"]<apply_t<commit_utc and rec_t2<pre["time"]
act_paths=re.findall(r"^- `([^`]+)`$",act_txt,re.M)
check("A2","Chronology: decision records → pre-application receipt → git apply → commit; activation instruction names exactly the nine paths and both approved identities",
      dec_ok and chron and sorted(act_paths)==sorted(CANON) and exp_ids["CLOSEOUT.patch"] in act_txt and exp_ids["CLOSEOUT_SUCCESSOR_INDEX.json"] in act_txt and PARENT_SHA in act_txt,
      {"decisions_recorded":rec_t,"pre_application_receipt":pre["time"],"git_apply":apply_t,"commit_utc":commit_utc,"activation_paths":act_paths})
# product verdict predates commit
v3=f"{C}/{RUN}/QA_PHASE4/RETEST_AMENDED_V3/QA_LEAD_VERDICT_V3.md"
v3_same=os.path.exists(v3) and sha(v3)==sha(f"{P}/{RUN}/QA_PHASE4/RETEST_AMENDED_V3/QA_LEAD_VERDICT_V3.md")
check("A3","Product verdict (QA_LEAD_VERDICT_V3.md) present in parent and candidate, byte-identical; predates closeout commit by ancestry",v3_same,{"verdict_sha256":sha(v3) if os.path.exists(v3) else None})

# ---- AC32: scope
ns=[l.split("\t") for l in open(f"{EXP}/name_status.txt").read().splitlines()]
changed={p:s for s,p in ns}
canon_changed=sorted(p for p in changed if not p.startswith(RUN+"/"))
records=sorted(p for p in changed if p.startswith(RUN+"/CLOSEOUT_EXECUTION/"))
reports=sorted(p for p in changed if p in REPORTS)
other=sorted(set(changed)-set(canon_changed)-set(records)-set(reports))
append_ok=all(rd(f"{C}/{r}").startswith(rd(f"{P}/{r}")) for r in REPORTS)
check("AC32a","Diff parent→candidate: exactly nine canonical paths (M), 32 additive CLOSEOUT_EXECUTION records (A), two append-only run reports (M), nothing else, no deletions",
      canon_changed==sorted(CANON) and len(records)==32 and all(changed[r]=="A" for r in records) and reports==sorted(REPORTS) and append_ok and other==[] and all(s in ("A","M") for s,_ in ns) and len(ns)==43,
      {"total":len(ns),"canonical":canon_changed,"records_added":len(records),"reports_append_only":append_ok,"unexpected":other})
# 101 index
idx=json.load(open(f"{C}/{RUN}/PHASE5_CLEANUP/CLOSEOUT_SUCCESSOR_INDEX.json"))
rows=[]; bad=[]
for e in idx:
    cs=sha(f"{C}/{e['path']}"); ps=sha(f"{P}/{e['path']}"); ws=sha(f"{EXEC_WT}/{e['path']}")
    ok=cs==e["proposed_sha256"]==ws and ps==e["before_sha256"] and ((e["status"]=="UNCHANGED")==(cs==ps)) and os.path.getsize(f"{C}/{e['path']}")==e["bytes"]
    rows.append({"path":e["path"],"status":e["status"],"candidate_sha256":cs,"parent_sha256":ps,"ok":ok}); 
    if not ok: bad.append(e["path"])
unch=[r["path"] for r in rows if r["status"]=="UNCHANGED"]; chg=[r["path"] for r in rows if r["status"]!="UNCHANGED"]
check("AC32b","All 101 candidate blobs match the approved successor index (and the installed worktree); 92 unchanged vs parent; the 9 changed are exactly the canonical nine",
      len(idx)==101 and not bad and len(unch)==92 and sorted(chg)==sorted(CANON),{"total":len(idx),"unchanged":len(unch),"changed":sorted(chg),"mismatches":bad})
EV["index_101"]=rows
# protected content spot-hashes (QA, spec, archives, 10x, lints, .github, workflows svg, intake)
def tree_hash(root,rel):
    out={}
    for dp,_,fs in os.walk(os.path.join(root,rel)):
        for f in fs:
            p=os.path.join(dp,f); out[os.path.relpath(p,root)]=sha(p)
    return out
prot={}
for rel in [RUN+"/QA_PHASE4",RUN+"/QA_RETEST_AF01",RUN+"/CERTIFIED_REVIEW",RUN+"/AMENDED_V3",RUN+"/PHASE5_CLEANUP","_ARCHIVE","10x Lab","lints",".github","03_BUILD_METHODOLOGY/_assets",RUN+"/INTAKE_SNAPSHOT/factory-intake/SOURCES/Workflow"]:
    a=tree_hash(C,rel); b=tree_hash(P,rel); prot[rel]={"files":len(a),"identical":a==b}
spec=sha(f"{C}/{RUN}/QA_RETEST_AF01/DOCSET_SYNC_ACCEPTANCE_SPEC_AMENDED_V1_R1.md")
check("AC32c","Protected trees identical parent↔candidate: all QA evidence, frozen spec R1, certified review, AMENDED_V3, PHASE5_CLEANUP, _ARCHIVE, 10x Lab, lints, .github, SVG assets, intake workflow originals",
      all(v["identical"] for v in prot.values()) and spec.startswith("2a3867ca"),{"trees":prot,"spec_r1_sha256":spec})

# ---- AC33: replay 12 spans
bt=json.load(open(f"{C}/{RUN}/BOUND_STATUS_TRANSITIONS.json")); trs=bt["transitions"]
by={}
for t in trs: by.setdefault(t["path"],[]).append(t)
replay=[]; rep_ok=True
for pth in CANON:
    txt=rd(f"{P}/{pth}").decode("utf-8")
    for t in by.get(pth,[]):
        n=txt.count(t["old"]); txt=txt.replace(t["old"],t["new"]); 
        cand_txt=rd(f"{C}/{pth}").decode("utf-8")
        r={"path":pth,"old":t["old"],"new":t["new"],"expected_occurrences":t["occurrences"],"parent_occurrences":n,"candidate_has_old":cand_txt.count(t["old"]),"candidate_has_new":cand_txt.count(t["new"])}
        replay.append(r)
        if n!=t["occurrences"] or r["candidate_has_old"]!=0 or r["candidate_has_new"]<t["occurrences"]: rep_ok=False
    if txt.encode("utf-8")!=rd(f"{C}/{pth}"): rep_ok=False; replay.append({"path":pth,"replay_equals_candidate":False})
check("AC33","Replay of all 12 exact old→new spans (BOUND_STATUS_TRANSITIONS.json) on parent bytes reproduces candidate bytes for all nine paths; old absent / new present in candidate",
      rep_ok and len(trs)==12 and sorted(by)==sorted(CANON) and sum(len(v) for v in by.values())==12,{"transitions":len(trs),"paths":len(by),"per_path":{k:len(v) for k,v in by.items()}})
EV["replay"]=replay
# patch matches diff
pdiff=subprocess.run(["git","diff",PARENT_SHA,CAND_SHA,"--",*CANON],cwd=EXEC_WT,capture_output=True,text=True).stdout
patch=rd(f"{C}/{RUN}/PHASE5_CLEANUP/CLOSEOUT.patch").decode()
def hunks(d): return [l for l in d.splitlines() if l.startswith(("+","-")) and not l.startswith(("+++","---"))]
check("AC33b","Actual canonical diff (+/- lines) equals the approved CLOSEOUT.patch (+/- lines)",hunks(pdiff)==hunks(patch),{"diff_lines":len(hunks(pdiff)),"patch_lines":len(hunks(patch))})
EV["canonical_diff"]=pdiff

# ---- AC25: headers vs MANIFEST
def status_of(pth):
    for l in rd(f"{C}/{pth}").decode().splitlines()[:8]:
        m=re.search(r"\*\*Status:\*\*\s*(.+?)(?:\s*\(|$)",l)
        if m: return m.group(1).strip()
man_c=rd(f"{C}/MANIFEST.md").decode().splitlines(); man_p=rd(f"{P}/MANIFEST.md").decode().splitlines()
mdiff=[(i,a,b) for i,(a,b) in enumerate(zip(man_p,man_c),1) if a!=b]
hdr={p:status_of(p) for p in CANON[:3]}
man_rows={}
for p in CANON[:3]:
    name=os.path.basename(p)[:-3]
    rows_=[l for l in man_c if l.startswith(f"| {name} |") and len(l.split("|"))>=7]  # document table only; reverse-map rows share the prefix
    man_rows[name]=rows_
def man_status(row): return row.split("|")[4].strip()
ac25=len(man_p)==len(man_c) and len(mdiff)==3 and all(hdr[p]=="Active" for p in hdr) and all(len(man_rows[os.path.basename(p)[:-3]])==1 and man_status(man_rows[os.path.basename(p)[:-3]][0]).split(" (")[0]=="Active" for p in CANON[:3]) and sorted(x[2].split("|")[1].strip() for x in mdiff)==sorted(os.path.basename(p)[:-3] for p in CANON[:3])
check("AC25","Three activated playbook headers read 'Active' and the matching MANIFEST rows say so; MANIFEST differs from parent in exactly three rows, same line count (count/reverse map/appendix untouched)",
      ac25,{"headers":hdr,"manifest_changed_rows":[{"line":i,"old":a,"new":b} for i,a,b in mdiff],"manifest_lines":len(man_c)})

# ---- AC27: versions/dates/history/CHANGELOG
meta_ok=True; meta_rows=[]
for pth in CANON:
    pc=rd(f"{C}/{pth}").decode(); pp=rd(f"{P}/{pth}").decode()
    vd_c=re.findall(r"\*\*(?:Version|Date):\*\*\s*[^·\n]+",pc); vd_p=re.findall(r"\*\*(?:Version|Date):\*\*\s*[^·\n]+",pp)
    def hist(t):
        ls=t.splitlines(); st=[i for i,l in enumerate(ls) if l.startswith("## ") and "History" in l]
        if not st: return None
        i=st[0]; j=next((k for k in range(i+1,len(ls)) if ls[k].startswith("## ")),len(ls))
        return hashlib.sha256("\n".join(ls[i:j]).encode()).hexdigest()
    hc,hp=hist(pc),hist(pp)
    ok=vd_c==vd_p and hc==hp and (("2026-10-18" in "".join(vd_c)) if vd_c else True)
    meta_rows.append({"path":pth,"version_date":vd_c[:2],"history_sha256":hc,"ok":ok}); meta_ok&=ok
cl=sha(f"{C}/CHANGELOG.md")==sha(f"{P}/CHANGELOG.md")
check("AC27","Versions, landing date 2026-10-18 and Version History sections identical parent↔candidate for all nine paths; canonical CHANGELOG.md byte-identical (no blanket row added)",meta_ok and cl,{"rows":meta_rows,"changelog_sha256":sha(f"{C}/CHANGELOG.md")})

# ---- AC31: lints on fresh export + unchanged lint/.github bytes
lint_same=tree_hash(C,"lints")==tree_hash(P,"lints") and tree_hash(C,".github")==tree_hash(P,".github")  # snapshot BEFORE running (run may write __pycache__ in scratch only)
lint=subprocess.run([sys.executable,"-B","-I","lints/run_all.py"],cwd=C,capture_output=True,text=True)
check("AC31","Unchanged four-lint suite passes on fresh candidate export (exit 0, RESULT: PASS); lints/ and .github/ byte-identical to parent",
      lint.returncode==0 and "RESULT: PASS" in lint.stdout and lint_same,{"command":"python3 -B -I lints/run_all.py","cwd":"<fresh git archive of 4c54292>","exit":lint.returncode,"stdout":lint.stdout,"stderr":lint.stderr})

# ---- Templates: 25 replay
tt=json.load(open(f"{C}/{RUN}/PHASE_2_TEMPLATE_TRANSLATIONS.json"))
trows=[]; t_ok=len(tt)==25
readme_tr=by.get("03_BUILD_METHODOLOGY/_templates/QAM/README.md",[])
for e in tt:
    src=f"{C}/{RUN}/INTAKE_SNAPSHOT/{e['source']}"; s_ok=sha(src)==e["source_sha256"]
    txt=rd(src).decode()
    occ_ok=True
    for tr in e["translations"]:
        if txt.count(tr["old"])!=tr["occurrences"]: occ_ok=False
        txt=txt.replace(tr["old"],tr["new"])
    repl=hashlib.sha256(txt.encode()).hexdigest()
    pi=sha(f"{P}/{e['destination']}"); ci=sha(f"{C}/{e['destination']}")
    if e["destination"].endswith("_templates/QAM/README.md"):
        for tr in readme_tr: txt=txt.replace(tr["old"],tr["new"])
        after=hashlib.sha256(txt.encode()).hexdigest(); allow=True
    else: after=repl; allow=False
    ok=s_ok and occ_ok and repl==e["proposed_destination_sha256"]==pi and ci==after and (allow or ci==pi)
    trows.append({"destination":e["destination"],"source_ok":s_ok,"translation_replay_sha256":repl,"parent_installed":pi,"candidate_installed":ci,"readme_allowance":allow,"ok":ok}); t_ok&=ok
check("T1","All 25 templates: pinned intake source hash matches; source+approved translation replays to parent-installed bytes; candidate bytes identical except README, which equals parent + its bound provenance span only",
      t_ok,{"count":len(tt),"rows":trows})
# README provenance span content: show the README diff
rdiff=subprocess.run(["git","diff",PARENT_SHA,CAND_SHA,"--","03_BUILD_METHODOLOGY/_templates/QAM/README.md"],cwd=EXEC_WT,capture_output=True,text=True).stdout
EV["readme_diff"]=rdiff

# ---- Workflows: status lines only; links; SVGs
wf_rows=[]; wf_ok=True
for pth in CANON[4:8]:
    lc=rd(f"{C}/{pth}").decode().splitlines(); lp=rd(f"{P}/{pth}").decode().splitlines()
    d=[(i,a,b) for i,(a,b) in enumerate(zip(lp,lc),1) if a!=b]
    only_status=len(lc)==len(lp) and all("**Status:**" in a and "**Status:**" in b for _,a,b in d)
    links=re.findall(r"\]\(([^)]+)\)","\n".join(lc)); linksp=re.findall(r"\]\(([^)]+)\)","\n".join(lp))
    svg=[l for l in links if l.endswith(".svg")]; png=[l for l in links if l.endswith(".png")]
    svg_exists=all(os.path.exists(os.path.normpath(os.path.join(C,os.path.dirname(pth),l))) for l in svg+png)
    ok=only_status and links==linksp and len(svg)>=1 and len(png)>=1 and svg_exists
    wf_rows.append({"path":pth,"changed_lines":[{"line":i,"old":a,"new":b} for i,a,b in d],"links":links,"links_resolve":svg_exists,"ok":ok}); wf_ok&=ok
svgs={}
for n in ["BIM_WORKFLOW","FFM_CREATION","FFM_DEPLOYMENT","FFM_EXECUTION"]:
    p=f"03_BUILD_METHODOLOGY/_assets/workflows/{n}.svg"; svgs[p]={"candidate":sha(f"{C}/{p}"),"same_as_parent":sha(f"{C}/{p}")==sha(f"{P}/{p}")}
check("W1","Four workflow documents differ from parent only in their Status line; bodies, links, checkpoints and routing text identical; SVG and PNG links resolve; four SVGs byte-identical to parent",
      wf_ok and all(v["same_as_parent"] for v in svgs.values()),{"workflows":wf_rows,"svgs":svgs})

# ---- Engineering claims cross-check (informational)
eng=json.load(open(f"{PKG}/RUN/CLOSEOUT_EXECUTION/FINAL_VERIFICATION.json"))  # post-commit receipt lives outside its own commit
EV["engineering_claims"]={"total_commit_paths":eng["total_commit_paths"],"result":eng["result"],"agrees_with_qa":eng["total_commit_paths"]==43}
EV["summary"]={"pass":sum(1 for c in EV["checks"] if c["result"]=="PASS"),"fail":[c["id"] for c in EV["checks"] if c["result"]=="FAIL"],"total":len(EV["checks"])}
json.dump(EV,open(OUT,"w"),indent=1,ensure_ascii=False)
print("SUMMARY",json.dumps(EV["summary"]))
