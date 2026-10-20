#!/usr/bin/env python3
"""Fable read-only re-measurement for the AMENDED-v3 retest adjudication (candidate 26b050f)."""
import json,subprocess,hashlib,re,sys,os,datetime,tarfile,io
W="/home/moose/Documents/app-factory-docs-sync-execution"; RUN="_AUDIT/SYNC_2026-10-15_doctrine-part2"
BASE="9c179392f79b70da099121fc357d3107ad3bb86e"; CONTENT="ef35d26d82f1904da6ed33663ad647e4ee16fe98"
P3="20f71ee932ed21c0878cb3a0f39c6fbe90d0a793"; P="8dff354937bc7baf739370a9886497d9d5359186"; C="26b050fe70de66e74ec8d65bcf9287d4369a91f7"
out_path,export_dir=sys.argv[1],sys.argv[2]
def git(*a,ok=True):
    r=subprocess.run(["git","-C",W,*a],capture_output=True,text=True); 
    if ok and r.returncode: raise SystemExit(f"git {a} failed: {r.stderr}")
    return r
def blob(rev,p): return git("show",f"{rev}:{p}").stdout
def blobb(rev,p): return subprocess.run(["git","-C",W,"show",f"{rev}:{p}"],capture_output=True,check=True).stdout
R={"generated":datetime.datetime.now().astimezone().isoformat(),"candidate":C,"parent":P}
# 1 pins
R["remote"]=git("ls-remote","origin","docs/sync-doctrine-part2-2026-10-15","main").stdout.strip().split("\n")
R["head"]=git("rev-parse","HEAD").stdout.strip(); R["status_porcelain_lines"]=len([l for l in git("status","--porcelain").stdout.split("\n") if l])
R["ancestry"]={f"{a[:7]}->{b[:7]}":git("merge-base","--is-ancestor",a,b,ok=False).returncode==0 for a,b in [(BASE,CONTENT),(CONTENT,P3),(P3,P),(P,C)]}
meta=git("log","-1","--format=%H%n%P%n%s%n%aI%n%cI",C).stdout.split("\n"); R["commit"]={"sha":meta[0],"parents":meta[1].split(),"subject":meta[2],"author_date":meta[3],"commit_date":meta[4]}
gate=blob(C,f"{RUN}/AMENDED_V3/DIRECTOR_DECISIONS_V3.md"); m=re.search(r"Recorded at: (\S+)",gate); R["gate2_recorded_at"]=m.group(1) if m else None
# 2 index
idx=json.loads(blob(C,f"{RUN}/AMENDED_V3/BOUND_EXECUTION_INDEX.json"))
entries=idx if isinstance(idx,list) else (idx.get("paths") or idx.get("entries") or idx.get("files"))
R["index_keys"]=list(idx.keys())[:10] if isinstance(idx,dict) else "list"
def pick(e):
    path=e.get("path") or e.get("file"); h=None
    for k in ("successor_sha256","proposed_sha256","sha256","installed_sha256","candidate_sha256","after_sha256"):
        if k in e: h=e[k]; break
    return path,h
mism=[];unch=0;chg=[]
for e in entries:
    path,h=pick(e); cb=blobb(C,path); cs=hashlib.sha256(cb).hexdigest()
    if h and cs!=h: mism.append(path)
    pb=subprocess.run(["git","-C",W,"show",f"{P}:{path}"],capture_output=True).stdout
    if pb==cb: unch+=1
    else: chg.append(path)
    # installed file
    with open(os.path.join(W,path),"rb") as f:
        if hashlib.sha256(f.read()).hexdigest()!=cs: mism.append("INSTALLED:"+path)
R["index"]={"count":len(entries),"hash_key_sample":[k for k in entries[0].keys()],"mismatches":mism,"unchanged_vs_parent":unch,"changed":chg}
R["changed_paths_parent_to_cand"]=git("diff","--name-only",P,C).stdout.strip().split("\n")
R["changed_outside_records"]=[p for p in R["changed_paths_parent_to_cand"] if not p.startswith(f"{RUN}/AMENDED_V3")]
# 3 export + sweep
os.makedirs(export_dir,exist_ok=True)
tb=subprocess.run(["git","-C",W,"archive",C],capture_output=True,check=True).stdout
tarfile.open(fileobj=io.BytesIO(tb)).extractall(export_dir,filter="data")
live=[]
for root,_,files in os.walk(export_dir):
    for f in files:
        rel=os.path.relpath(os.path.join(root,f),export_dir)
        if rel.startswith(("_AUDIT","agent_docs",".git","10x Lab","_SKILLS","lints",".github")): continue
        if rel.endswith((".md",".svg")): live.append(rel)
pat=re.compile(r"fetchProducts|services/productServices")
hits=[]
API="04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md"
def cls(rel,n,t):
    if "fetchProductsByIds" in t or "fetchProductBySlug" in t: return "e-distinct-op"
    if rel==API and (183<=n<=183 or n in (985,1179)): return "d-vocab"
    if rel==API and (172<=n<=174 or n==582 or 613<=n<=622 or 785<=n<=815 or 856<=n<=869): return "a-API§3-labelled"
    if rel.endswith("APP_ARCHITECTURE_MANUAL.md") and (499<=n<=522 or 590<=n<=620): return "b-labelled-independent"
    if rel.endswith("STATE_MANAGEMENT_MANUAL.md"):
        if n==241: return "d-vocab"
        if 797<=n<=806: return "c-negated-BAD"
        if 808<=n<=830 or 863<=n<=910: return "b-labelled-independent"
    return "UNCLASSIFIED"
for rel in sorted(live):
    with open(os.path.join(export_dir,rel),encoding="utf-8",errors="replace") as f:
        for i,l in enumerate(f,1):
            if pat.search(l): hits.append({"path":rel,"line":i,"class":cls(rel,i,l),"text":l.rstrip()[:140]})
R["sweep"]={"live_files":len(live),"hits":len(hits),"unclassified":[h for h in hits if h["class"]=="UNCLASSIFIED"],"by_class":{}}
for h in hits: R["sweep"]["by_class"][h["class"]]=R["sweep"]["by_class"].get(h["class"],0)+1
R["sweep"]["rows"]=hits
# 4 label containers + diffs
arch_p,arch_c=blob(P,"04_REFERENCE_MANUALS/APP_ARCHITECTURE_MANUAL.md").split("\n"),blob(C,"04_REFERENCE_MANUALS/APP_ARCHITECTURE_MANUAL.md").split("\n")
st_p,st_c=blob(P,"04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md").split("\n"),blob(C,"04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md").split("\n")
import difflib
def added_removed(a,b):
    d=[l for l in difflib.unified_diff(a,b,lineterm="",n=0) if l[:1] in "+-" and l[:3] not in ("+++","---")]
    return d
R["arch_diff"]=added_removed(arch_p,arch_c); R["state_diff"]=added_removed(st_p,st_c)
R["state_first_diff_line"]=next((i+1 for i,(x,y) in enumerate(zip(st_p,st_c)) if x!=y),None)
R["state_passages_identical"]={"1-808":st_p[:808]==st_c[:808],"§4 475-620":st_p[474:620]==st_c[474:620],"§5 621-658":st_p[620:658]==st_c[620:658],"§6 659-790":st_p[658:790]==st_c[658:790],"line519":st_p[518]==st_c[518] and "Raw contact information is not persisted" in st_c[518],"RUL13 779-786":st_p[778:786]==st_c[778:786]}
R["headers"]={"ARCH":arch_c[2],"STATE":st_c[2]}
cl_p,cl_c=blob(P,"CHANGELOG.md").split("\n"),blob(C,"CHANGELOG.md").split("\n")
R["changelog_diff"]=added_removed(cl_p,cl_c); R["changelog_run_rows"]=sum(1 for l in cl_c if l.startswith("| 2026-10-18 |"))
R["manifest_identical"]=blobb(P,"MANIFEST.md")==blobb(C,"MANIFEST.md")
for name,p in (("TESTING","03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md"),("AUTH","04_REFERENCE_MANUALS/AUTH_MANUAL.md"),("ECOMMERCE","04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md"),("API","04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md"),("ENGINEER","02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md"),("DATABASE","04_REFERENCE_MANUALS/DATABASE_MANUAL.md")):
    R.setdefault("identical_to_parent",{})[name]=blobb(P,p)==blobb(C,p)
# 5 transitions
tr=json.loads(blob(C,f"{RUN}/BOUND_STATUS_TRANSITIONS.json")); tl=tr if isinstance(tr,list) else (tr.get("transitions") or tr.get("items"))
pend=[];bad=[]
for t in tl:
    path=t.get("path"); old=t.get("old") or t.get("from") or t.get("old_text"); new=t.get("new") or t.get("to") or t.get("new_text")
    txt=blob(C,path)
    ok=(old in txt) and (new not in txt if new else True)
    (pend if ok else bad).append({"path":path,"old":str(old)[:60],"new":str(new)[:60]})
R["transitions"]={"total":len(tl),"pending":len(pend),"not_pending":bad,"keys":list(tl[0].keys())}
# 6 lints
lr=subprocess.run(["python3","-B","-I","lints/run_all.py"],cwd=export_dir,capture_output=True,text=True)
R["lint"]={"exit":lr.returncode,"tail":lr.stdout[-600:],"stderr":lr.stderr[-300:]}
R["lints_github_identical"]=git("diff","--quiet",P,C,"--","lints",".github",ok=False).returncode==0
json.dump(R,open(out_path,"w"),indent=1,ensure_ascii=False)
print("done")
