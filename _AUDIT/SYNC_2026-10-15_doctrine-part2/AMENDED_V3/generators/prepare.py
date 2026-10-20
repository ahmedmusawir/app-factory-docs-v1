"""Prepare exact AMENDED-v3 artifacts; no candidate or Git writes. python3 -B -I."""
from pathlib import Path
import json,hashlib,subprocess,difflib,zipfile,shutil
A=Path(__file__).resolve().parents[1];R=A.parent;W=Path('/home/moose/Documents/app-factory-docs-sync-execution');C='8dff354937bc7baf739370a9886497d9d5359186';RUN='_AUDIT/SYNC_2026-10-15_doctrine-part2/'
sha=lambda b:hashlib.sha256(b).hexdigest()
def blob(p):return subprocess.check_output(['git','-C',str(W),'show',C+':'+p])
def save(n,d):
 p=A/n;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
idx=json.loads(blob(RUN+'AMENDED_V2/BOUND_EXECUTION_INDEX.json'));assert len(idx)==101
original={x['path']:blob(x['path']) for x in idx};state={p:b.decode() for p,b in original.items()};ed=[]
for x in idx:assert sha(original[x['path']])==x['proposed_sha256']
arch='04_REFERENCE_MANUALS/APP_ARCHITECTURE_MANUAL.md';st='04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md'
def edit(p,old,new,item):
 assert state[p].count(old)==1,(item,p);seq=410+len(ed)
 ed.append(dict(sequence=seq,edit_id=f'E{seq}',item=item,ids=['RV2-F01','FC-066',item],path=p,old=old,new=new,candidate_line=original[p].decode()[:original[p].decode().index(old)].count('\n')+1,authority='Fable JARVIS_REPAIR_RECOMMENDATION §§1–2; Jarvis exact wording confirmed by current Tony preparation assignment; Gate 2 pending'))
 state[p]=state[p].replace(old,new,1)
a='By default, all components in the App Router are Server Components:'
edit(arch,a,a+"\n\nIndependent rendering illustration: the `fetchProducts()` used in this section returns `Promise<Product[]>` and is not the API manual §3 typed-outcome service; a project implementing the §3 contract narrows `status === 'success'` and passes `items` to the list.",'V3-1')
edit(arch,'// Async component that fetches data','// Async component that fetches data\n// Same independent Promise<Product[]> illustration as the Server Component example above.','V3-2')
edit(st,'// src/services/productServices.ts',"// src/services/productServices.ts — independent store/service-separation illustration\n// this local fetchProducts() returns the route's raw JSON array; it is not the API manual §3 typed-outcome service",'V3-3')
a='Server Components cannot use hooks, but they can pass initial data to Client Components:'
edit(st,a,a+" This illustration's `fetchProducts()` returns `Promise<Product[]>` (hence `initialProducts: Product[]`) and is not the API manual §3 typed-outcome service; under that contract, narrow `status === 'success'` and pass `outcome.items`.",'V3-4')
clause='; QA-P4 repair: RV2-F01 (AC16/FC-066 labels)'
for p in [arch,st]:
 rows=[l for l in state[p].splitlines() if l.startswith('|') and '2026-10-18' in l];assert len(rows)==1;old=rows[0]
 edit(p,old,old.rstrip().removesuffix('|').rstrip()+clause+' |','HISTORY')
 rows=[l for l in state['CHANGELOG.md'].splitlines() if l.startswith('| 2026-10-18 | '+Path(p).stem+' ')];assert len(rows)==1;old=rows[0];cells=old.split('|');cells[3]=cells[3].rstrip()+clause+' '
 edit('CHANGELOG.md',old,'|'.join(cells),'CHANGELOG')
changed=sorted({e['path'] for e in ed});assert len(changed)==3
for p in changed:
 q=A/'PROPOSED_CONTENT'/p;q.parent.mkdir(parents=True,exist_ok=True);q.write_bytes(state[p].encode())
save('AMENDMENT_V3_EDITS.json',ed);prior=json.loads(blob(RUN+'AMENDED_V2/SELECTED_EXACT_EDITS.json'));assert len(prior)==409;save('SELECTED_EXACT_EDITS.json',prior+ed)
newidx=[dict(path=x['path'],before_sha256=sha(original[x['path']]),proposed_sha256=sha(state[x['path']].encode()),bytes=len(state[x['path']].encode()),landing_date='2026-10-18',candidate=C,amended='AMENDED-v3' if x['path'] in changed else 'UNCHANGED') for x in idx]
save('EXECUTION_PROPOSAL_INDEX.json',newidx);save('BOUND_EXECUTION_INDEX.json',newidx)
diff=[]
for p in changed:
 for line in difflib.unified_diff(original[p].decode().splitlines(True),state[p].splitlines(True),fromfile=p,tofile=p):diff.append(line if line.endswith('\n') else line+'\n\\ No newline at end of file\n')
(A/'EXECUTION_PROPOSAL.patch').write_text(''.join(diff))
I=A/'INPUTS';I.mkdir(exist_ok=True);zpath=Path('/home/moose/Downloads/FACTORY_QA_AMENDED_V2_VERDICT_HANDBACK_2026-10-19_193051.zip');assert sha(zpath.read_bytes())=='7d8b58b747b952de0c1f573fc9c37219b9bf739c2ab274edc2fbb0460c6ae925';shutil.copyfile(zpath,I/zpath.name)
with zipfile.ZipFile(zpath) as z:
 for n in ['QA_LEAD_VERDICT_V2.md','JARVIS_REPAIR_RECOMMENDATION.md']:(I/n).write_bytes(z.read('RETEST_AMENDED_V2/'+n))
for n in ['AMENDED_V2/BOUND_EXECUTION_INDEX.json','AMENDED_V2/SELECTED_EXACT_EDITS.json','QA_PHASE4/REPAIR_QA_P4/DIRECTOR_DECISIONS_V2.md','QA_RETEST_AF01/DOCSET_SYNC_ACCEPTANCE_SPEC_AMENDED_V1_R1.md','BOUND_STATUS_TRANSITIONS.json']:
 p=I/'candidate_run'/n;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(blob(RUN+n))
text='# AMENDED-v3 — exact label-only proposal\n\nENGINEER-PROPOSED. Jarvis wording confirmed by Tony; exact-patch Gate 2 PENDING. Candidate `'+C+'`. Four required containers, with explicit V3-2 streaming comment included. No optional V3-1 fence comment needed: its sentence directly precedes the fence.\n\nThree canonical paths: ARCH, STATE, CHANGELOG; 98 unchanged of101. Eight new edits E410–E417. Existing headers/dates/imports/executable code preserved. Frozen records and all prior repairs untouched; twelve transitions pending. SELECTED_EXACT_EDITS retains409 historical records; replay only E410+ against this candidate, not the whole provenance list against BASE.\n\n'
for e in ed:text+=f"## {e['edit_id']} / {e['item']} — {e['path']}:{e['candidate_line']}\n\nOld:\n````text\n{e['old']}\n````\n\nNew:\n````text\n{e['new']}\n````\n\n"
(A/'AMENDMENT_V3.md').write_text(text)
save('AMENDMENT_IDENTITIES.json',{'candidate':C,'status':'PROPOSED — exact-patch Gate 2 PENDING','changed_paths':changed,'unchanged_paths':98,'new_edits':len(ed),'total_edits':len(prior)+len(ed),'inputs':{str(p.relative_to(I)):sha(p.read_bytes()) for p in I.rglob('*') if p.is_file()},'artifacts':{n:sha((A/n).read_bytes()) for n in ['EXECUTION_PROPOSAL_INDEX.json','BOUND_EXECUTION_INDEX.json','EXECUTION_PROPOSAL.patch','AMENDMENT_V3_EDITS.json','SELECTED_EXACT_EDITS.json']}})
print('Prepared E410–E417;3 files;101 index rows;98 unchanged.')
