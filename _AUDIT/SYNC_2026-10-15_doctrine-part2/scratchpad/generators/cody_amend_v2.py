"""Generate proposal records only; never writes the execution worktree. Run python3 -B -I."""
from pathlib import Path
import subprocess, json, hashlib, difflib, re, shutil, datetime
R=Path(__file__).resolve().parents[2]; A=R/'AMENDED_V2'
W=Path('/home/moose/Documents/app-factory-docs-sync-execution')
C='20f71ee932ed21c0878cb3a0f39c6fbe90d0a793'
sha=lambda b:hashlib.sha256(b).hexdigest()
def blob(p):return subprocess.check_output(['git','-C',str(W),'show',C+':'+p])
def save(n,d):
 p=A/n;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
def runjson(n):return json.loads(blob(str(R.relative_to(R.parents[1]))+'/'+n))
# R is RUN under _AUDIT; use explicit relative name for portable identities.
RUN='_AUDIT/SYNC_2026-10-15_doctrine-part2/'
idx=json.loads(blob(RUN+'BOUND_EXECUTION_INDEX.json'))
original={x['path']:blob(x['path']) for x in idx};state={p:b.decode() for p,b in original.items()};ed=[]
assert len(idx)==101
for x in idx:assert sha(original[x['path']])==x['proposed_sha256']
authority='QA Lead verdict F01–F05; Jarvis correction directions confirmed by Tony in current preparation assignment. Exact proposed bytes remain subject to Tony Gate 2; no approval inferred.'
def edit(p,old,new,item):
 assert old!=new and state[p].count(old)==1,(p,item,state[p].count(old))
 seq=381+len(ed); ed.append(dict(sequence=seq,edit_id=f'E{seq}',path=p,old=old,new=new,ids=[item],item=item,label='ENGINEER-PROPOSED AMENDED-v2',authority=authority,candidate=C,candidate_line=original[p].decode()[:original[p].decode().index(old)].count('\n')+1 if old in original[p].decode() else None))
 state[p]=state[p].replace(old,new,1)
def span(p,a,b):return '\n'.join(original[p].decode().splitlines()[a-1:b])
E='02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md'; T='03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md';D='04_REFERENCE_MANUALS/DATABASE_MANUAL.md';S='04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md';U='04_REFERENCE_MANUALS/AUTH_MANUAL.md';P='04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md'
edit(E,span(E,176,176),'> The Architect authors `DATA_CONTRACT.md` in both runs; only the evidence base and moment differ: conversion uses Brain Drain evidence and is pre-authored; greenfield uses the approved APP_BRIEF before Design. Router: APP_FACTORY_BLUEPRINT, "Which Pipeline Am I In?".','F01')
edit(E,span(E,1385,1385),'When code is complete and self-verified, the Engineer hands the candidate and factual QAM engineering handoff to independent QA on the Director-created QA branch; Operations/Deployment receives the package only after QA Lead certification and Director release (see QAM_PLAYBOOK §3 and DEPLOYMENT_PLAYBOOK §3).','F02')
edit(E,span(E,1392,1397),'├── APP_BRIEF.md (from Architect)\n├── UI_SPEC.md (from Designer)\n├── DATA_CONTRACT.md\n├── ACCEPTANCE_SPEC.md (from Architect)\n├── Working Code (tested)\n├── QAM/ (module QA pack: ENGINEERING_HANDOFF, approved plan, results, certificate)\n├── README.md (setup instructions)\n└── Deployment Guide','F02')
edit(E,span(E,255,257),'   Read the handbook, treat it as ASPIRATIONAL — verify every load-bearing claim against disk (RECON_QUESTIONNAIRE §0).\n   Disk establishes implementation facts; approved briefs govern scope and governing documents control their subjects.\n   Record handbook drift; route genuine requirements conflicts to the Director.','F03')
withdraw=span(T,881,881)
guard='Privileged seeding and admin-client construction in test helpers run only behind the Director-approved test-project allowlist and authorized-test-identity guard above; fail closed on mismatch, missing identity or unknown target.'
edit(T,span(T,891,910),withdraw+'\n\n'+guard,'F04a / FC-022')
edit(T,span(T,918,930),withdraw+'\n\n'+guard,'F04a / FC-022')
edit(D,span(D,420,423),'A service-role client bypasses RLS and is appropriate only inside an independently authorized elevated operation:\n- Background jobs with operation-local authorization\n- Admin operations with operation-local authorization\n\nAn API route is not itself a reason to bypass RLS; never use a service-role client as the default route client (see AUTH_MANUAL, Service-Role Capability Boundary).','F04b / FC-038')
edit(D,'// Server-side: Service role bypasses RLS','// Construct only inside an independently authorized elevated operation, never as a default route client.','F04b / FC-038')
edit(D,'process.env.SUPABASE_SERVICE_ROLE_KEY! // Bypasses RLS','process.env.SUPABASE_SERVICE_ROLE_KEY! // Operation-local authorization is required before construction.','F04b / FC-038')
edit(S,'export const fetchProducts = async (): Promise<Product[]> => {','// Independent normalization-step example: fetchProducts() returns Promise<Product[]>.\n// This array-returning step is not the typed-outcome service used by the route below.\nexport const fetchProducts = async (): Promise<Product[]> => {','F04c / FC-066')
edit(S,'### Graceful Degradation Pattern\n','### Graceful Degradation Pattern\n\nThis caller uses the §3 typed-outcome contract: `fetchProducts()` returns a discriminated outcome with `status` equal to `success`, `not-found`, `unavailable`, `invalid` or `forbidden`; only `success` carries `items: Product[]`. This example assumes a project-approved public-catalog failure policy permitting the generic empty-state UI on non-success; this is not an entitlement decision or a cached successful result. It does not call the independent array-returning normalization example.\n','F04c / FC-066')
edit(S,'  const { items: products, error } = await fetchProducts();\n\n  // Graceful degradation: show empty state instead of crashing\n  if (error || products.length === 0) {','  const outcome = await fetchProducts();\n\n  // Apply the declared public-catalog failure policy; do not treat failure as success.\n  if (outcome.status !== \'success\' || outcome.items.length === 0) {','F04c / FC-066')
edit(S,'  return <ProductList products={products} />;','  return <ProductList products={outcome.items} />;','F04c / FC-066')
edit(S,'### ISR and Revalidation\n','### ISR and Revalidation\n\nIndependent ISR example: this `fetchProducts()` returns the endpoint’s raw JSON payload, with no normalization or typed-outcome envelope; it is not the §3 service or the caller above. The project must declare and validate that endpoint’s wire contract and failure/cache policy before implementation; this example only illustrates the revalidation option.\n','F04c / FC-066')
policy='No persistent raw contact information is stored in browser storage by default; any approved exception names the fields, purpose, retention period and owner, with clearing/invalidation behavior.'
edit(U,span(U,1122,1124),span(U,1122,1124)+'\n   - '+policy,'F05 / RUL-13')
edit(T,span(T,426,427),span(T,426,427)+'\n\n'+policy,'F05 / RUL-13')
edit(P,'Personal fields follow the approved account-transition and retention policy.','Personal fields follow the approved account-transition and retention policy in STATE_MANAGEMENT_MANUAL. '+policy,'F05 / RUL-13')
clause='QA-P4 repair: F01–F05 (AC5/6/9/15/16/18)'
for p in [E,T,D,S,U,P]:
 rows=[l for l in state[p].splitlines() if l.startswith('|') and '2026-10-18' in l];assert len(rows)==1,(p,rows)
 old=rows[0];edit(p,old,old.rstrip().removesuffix('|').rstrip()+'; '+clause+' |','HISTORY / F01–F05')
 rows=[l for l in state['CHANGELOG.md'].splitlines() if l.startswith('| 2026-10-18 | '+Path(p).stem+' ')];assert len(rows)==1
 old=rows[0];cells=old.split('|');cells[3]=cells[3].rstrip()+'; '+clause+' ';edit('CHANGELOG.md',old,'|'.join(cells),'CHANGELOG / F01–F05')
changed=sorted({e['path'] for e in ed});assert len(changed)==7
for p in changed:
 q=A/'PROPOSED_CONTENT'/p;q.parent.mkdir(parents=True,exist_ok=True);q.write_bytes(state[p].encode())
save('AMENDMENT_V2_EDITS.json',ed)
prior=json.loads(blob(RUN+'AMENDED_V1/SELECTED_EXACT_EDITS.json'));assert len(prior)==380
save('SELECTED_EXACT_EDITS.json',prior+ed)
newidx=[]
for x in idx:
 p=x['path'];b=state[p].encode();newidx.append(dict(path=p,before_sha256=sha(original[p]),proposed_sha256=sha(b),bytes=len(b),amended='AMENDED-v2' if p in changed else 'UNCHANGED from candidate',landing_date='2026-10-18',candidate=C))
save('EXECUTION_PROPOSAL_INDEX.json',newidx);save('BOUND_EXECUTION_INDEX.json',newidx)
patch=[]
for p in changed:
 for line in difflib.unified_diff(original[p].decode().splitlines(True),state[p].splitlines(True),fromfile=p,tofile=p):
  patch.append(line if line.endswith('\n') else line+'\n\\ No newline at end of file\n')
(A/'EXECUTION_PROPOSAL.patch').write_text(''.join(patch))
text='# AMENDED-v2 — F01–F05 complete proposal\n\nStatus: ENGINEER-PROPOSED; Tony Gate 2 PENDING. Preparation only.\n\n'+authority+'\n\nCandidate: `'+C+'`; landing date 2026-10-18. FU-1/FU-2 excluded.\n\n## Accounting correction (current Director assignment)\n\nR6: seven changed canonical paths (six documents plus CHANGELOG.md), 94 unchanged paths in the 101-path index. R12: only those seven canonical paths plus new run records and normal bookkeeping are allowed. CHANGELOG is included in contents, patch and verification. This clarifies the repair prompt only; frozen spec R1 is byte-unchanged. The 39 current-run CHANGELOG rows retain their count; six existing rows gain the QA clause.\n\n## Replay semantics\n\nSELECTED_EXACT_EDITS preserves E001–E380 exactly as provenance and appends E381 onward. Replay the new suffix against candidate bytes (already metadata/date-bound); do not replay the concatenated provenance list directly against BASE without the original metadata/date binding stages. EXECUTION_PROPOSAL.patch is the complete seven-path delta against git archive '+C+', applied with -p0 only to a disposable verification export before approval. Both successor indices cover all 101 paths using candidate before hashes.\n\n## Exact old-to-new spans\n'
for e in ed:text+=f"\n### {e['edit_id']} — {e['item']} — {e['path']}:{e['candidate_line']}\n\nEvidence: pinned candidate span; QA verdict §2 and repair prompt §1/§2.\n\nOld:\n````text\n{e['old']}\n````\n\nNew:\n````text\n{e['new']}\n````\n"
(A/'AMENDMENT_V2.md').write_text(text)
# Keep all authoritative inputs as exact copies, not rewritten successors.
I=A/'INPUTS';I.mkdir(exist_ok=True)
shutil.copyfile('/home/moose/Downloads/FACTORY_QA_P4_VERDICT_HANDBACK_2026-10-19_122452.zip',I/'FACTORY_QA_P4_VERDICT_HANDBACK_2026-10-19_122452.zip')
for name in ['BOUND_EXECUTION_INDEX.json','AMENDED_V1/SELECTED_EXACT_EDITS.json','AMENDED_V1/AMENDMENT_V1_EDITS.json','POST_VERIFICATION_STATUS_TRANSITIONS.json','GATE2_APPROVAL_RECORD_2026-10-17.md','QA_RETEST_AF01/DIRECTOR_DECISIONS.md','QA_RETEST_AF01/DOCSET_SYNC_ACCEPTANCE_SPEC_AMENDED_V1_R1.md','UPDATE_MAP.md']:
 p=I/'candidate_run'/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(blob(RUN+name))
for name in ['QA_LEAD_VERDICT.md','REPAIR_QA_P4/ENGINEER_REPAIR_PROMPT.md','REPAIR_QA_P4/REPAIR_FINDINGS.json','EXECUTOR_EVIDENCE/MANUAL_READS.md']:
 p=I/'QA_PHASE4'/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes((R/'QA_PHASE4'/name).read_bytes())
ident={'candidate':C,'status':'PROPOSED — Tony Gate 2 not recorded','authority':authority,'changed_paths':changed,'unchanged_paths':94,'original_edits':380,'new_edits':len(ed),'total_edits':380+len(ed),'landing_date':'2026-10-18','inputs':{str(p.relative_to(I)):sha(p.read_bytes()) for p in I.rglob('*') if p.is_file()},'artifacts':{n:sha((A/n).read_bytes()) for n in ['EXECUTION_PROPOSAL_INDEX.json','BOUND_EXECUTION_INDEX.json','EXECUTION_PROPOSAL.patch','AMENDMENT_V2_EDITS.json','SELECTED_EXACT_EDITS.json']}}
save('AMENDMENT_IDENTITIES.json',ident)
print(json.dumps({'new_edits':len(ed),'changed':changed,'index':ident['artifacts']['BOUND_EXECUTION_INDEX.json']},indent=2))
