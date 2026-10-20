#!/usr/bin/env python3
"""Read-only adjudication evidence for RV2-F01 (AMENDED-v2 retest, candidate 8dff354).
Re-extracts every fetchProducts/productServices span at BASE, 20f71ee and 8dff354 from git
(no working-tree reads), records blob identities, and records prior dispositions."""
import json, subprocess, hashlib, re, sys, datetime
W = "/home/moose/Documents/app-factory-docs-sync-execution"
BASE = "9c179392f79b70da099121fc357d3107ad3bb86e"
P3   = "20f71ee932ed21c0878cb3a0f39c6fbe90d0a793"
CAND = "8dff354937bc7baf739370a9886497d9d5359186"
DOCS = ["04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md",
        "04_REFERENCE_MANUALS/APP_ARCHITECTURE_MANUAL.md",
        "04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md"]
def git(*a): return subprocess.run(["git","-C",W,*a],capture_output=True,text=True,check=True).stdout
def show(rev,p): return git("show",f"{rev}:{p}")
out={"generated":datetime.datetime.now().astimezone().isoformat(),"candidate":CAND,"parent":P3,"base":BASE,
     "remote":git("ls-remote","origin","docs/sync-doctrine-part2-2026-10-15","main").strip().split("\n"),
     "blobs":{},"hits":{}}
pat=re.compile(r"fetchProducts(?!ByIds|BySlug)|services/productServices")
for p in DOCS:
    out["blobs"][p]={r:git("rev-parse",f"{r}:{p}").strip() for r in ("base","parent","cand") for r in [r]} if False else {
        "base":git("rev-parse",f"{BASE}:{p}").strip(),"parent":git("rev-parse",f"{P3}:{p}").strip(),"cand":git("rev-parse",f"{CAND}:{p}").strip()}
    for name,rev in (("base",BASE),("parent",P3),("cand",CAND)):
        lines=show(rev,p).split("\n")
        out["hits"].setdefault(p,{})[name]=[{"line":i+1,"text":l} for i,l in enumerate(lines) if pat.search(l)]
# contradiction trace: same import path, array consumer vs typed outcome declaration
cand_api=show(CAND,DOCS[0]).split("\n")
out["declared_contract"]={"path":DOCS[0],"lines":{"172":cand_api[171],"174":cand_api[173],"582":cand_api[581],"787":cand_api[786][:160]}}
def span(p,a,b): L=show(CAND,p).split("\n"); return [{"line":i+1,"text":L[i]} for i in range(a-1,b)]
out["unlabelled_consumers"]={
 "ARCH_server_component":span(DOCS[1],497,519),
 "ARCH_streaming":span(DOCS[1],589,615),
 "STATE_store_service_good":span(DOCS[2],808,813),
 "STATE_store_server_components":span(DOCS[2],863,889)}
out["prior_dispositions"]={
 "gate2_PROPAGATION_tsv":"FC-066 rows for APP_ARCHITECTURE 533/538/640 and STATE 1094/1103/1119/1162/1166 (BASE numbering): CONSISTENT, note '§F; final review required'",
 "phase4_executor_F04":"API_AND_SERVICES_MANUAL only (613/793/856)",
 "phase4_qa_lead_F04c_repair_anchor":"API_AND_SERVICES_MANUAL.md:613, 793, 856 — 'make every fetchProducts occurrence match one declared contract or carry an explicit alternative label'",
 "amended_v2_PROPAGATION_tsv":"ARCH 505/510/612 and STATE 241/801/810/826/869/873: RETAIN — 'outside the three named API-manual F04c sites; not asserted to implement the API typed service'",
 "director_decisions_v2":"approves exact AMENDED-v2 seven-path scope; 'authorizes engineering execution, not independent QA acceptance'"}
json.dump(out,open(sys.argv[1],"w"),indent=1,ensure_ascii=False)
print("ok",{p:len(v["cand"]) for p,v in out["hits"].items()})
