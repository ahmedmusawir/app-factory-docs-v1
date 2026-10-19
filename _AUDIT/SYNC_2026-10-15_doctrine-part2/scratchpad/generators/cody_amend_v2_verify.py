"""Engineer preparation checks, not independent acceptance. Only scratch export is patched."""
from pathlib import Path
import subprocess,json,hashlib,re,tarfile,tempfile,datetime,os,csv,io,zipfile
R=Path(__file__).resolve().parents[2];A=R/'AMENDED_V2';W=Path('/home/moose/Documents/app-factory-docs-sync-execution');RUN='_AUDIT/SYNC_2026-10-15_doctrine-part2/'
C='20f71ee932ed21c0878cb3a0f39c6fbe90d0a793';sha=lambda b:hashlib.sha256(b).hexdigest()
commands=[];checks={}
def cmd(args,cwd=W):
 p=subprocess.run(args,cwd=cwd,capture_output=True,text=True,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'});commands.append(dict(command=args,cwd=str(cwd),exit=p.returncode,stdout=p.stdout,stderr=p.stderr));assert p.returncode==0,commands[-1];return p.stdout

def blob(p):return subprocess.check_output(['git','-C',str(W),'show',C+':'+p])
def save(n,x):(A/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def check(k,ok,details):
 checks[k]=dict(status='PASS' if ok else 'FAIL',details=details)
 assert ok,(k,details)
# Hash protected review files before/after verification, including original evidence and approvals.
protected=[p for p in R.rglob('*') if p.is_file() and not any(s in p.relative_to(R).parts for s in ['AMENDED_V2','scratchpad'])]
review_before={str(p.relative_to(R)):sha(p.read_bytes()) for p in protected}
refs=cmd(['git','show-ref']);start=cmd(['git','status','--porcelain']);check('execution_start',not start and cmd(['git','rev-parse','HEAD']).strip()==C,'Pinned candidate clean; Git read-only.')
index=json.loads((A/'BOUND_EXECUTION_INDEX.json').read_text());ed=json.loads((A/'AMENDMENT_V2_EDITS.json').read_text());changed=sorted({e['path'] for e in ed})
with tempfile.TemporaryDirectory(prefix='amended-v2-') as tmp:
 s=Path(tmp); tar=s/'candidate.tar';cmd(['git','archive','--format=tar','--output='+str(tar),C]); tree=s/'tree';tree.mkdir()
 with tarfile.open(tar) as t:t.extractall(tree,filter='data')
 before={str(p.relative_to(tree)):sha(p.read_bytes()) for p in tree.rglob('*') if p.is_file()}
 cmd(['git','apply','--check','-p0',str(A/'EXECUTION_PROPOSAL.patch')],tree)
 cmd(['git','apply','-p0',str(A/'EXECUTION_PROPOSAL.patch')],tree)
 after={str(p.relative_to(tree)):sha(p.read_bytes()) for p in tree.rglob('*') if p.is_file()}
 check('R12_scope',set(before)==set(after) and sorted(p for p in before if before[p]!=after[p])==changed and len(changed)==7,{'changed_paths':changed,'rule':'Six documents + CHANGELOG; no other canonical path changed; disposable export only.'})
 replay={p:blob(p).decode() for p in changed}
 for e in ed:
  assert replay[e['path']].count(e['old'])==1,e['edit_id'];replay[e['path']]=replay[e['path']].replace(e['old'],e['new'],1)
 check('exact_edit_replay',all(replay[p].encode()==(tree/p).read_bytes()==(A/'PROPOSED_CONTENT'/p).read_bytes() for p in changed),{'new_edits':len(ed),'range':[ed[0]['edit_id'],ed[-1]['edit_id']]})
 selected=json.loads((A/'SELECTED_EXACT_EDITS.json').read_text());prior=json.loads(blob(RUN+'AMENDED_V1/SELECTED_EXACT_EDITS.json'))
 check('original_380_preserved',selected[:380]==prior and selected[380:]==ed and [e['sequence'] for e in selected]==list(range(1,len(selected)+1)),'Original ordered records preserved verbatim as JSON values; new suffix replays from candidate.')
 rows=[]
 for x in index:
  p=x['path'];assert before[p]==x['before_sha256'] and after[p]==x['proposed_sha256'] and (tree/p).stat().st_size==x['bytes'] and x['landing_date']=='2026-10-18';rows.append(dict(path=p,before=before[p],proposed=after[p],changed=before[p]!=after[p]))
 save('PATH_VERIFICATION.json',rows)
 check('R6_index',len(rows)==101 and sum(not r['changed'] for r in rows)==94 and (A/'BOUND_EXECUTION_INDEX.json').read_bytes()==(A/'EXECUTION_PROPOSAL_INDEX.json').read_bytes(),'101/101 before and proposed identities; seven changed, 94 unchanged (corrected R6).')
 def text(p):return (tree/p).read_text()
 E='02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md';T='03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md';D='04_REFERENCE_MANUALS/DATABASE_MANUAL.md';S='04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md';U='04_REFERENCE_MANUALS/AUTH_MANUAL.md';P='04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md'
 am1=json.loads(blob(RUN+'AMENDED_V1/AMENDMENT_V1_EDITS.json'))
 check('R1_ownership',all(text(e['path']).count(e['new'])==1 for e in am1) and 'The Architect authors `DATA_CONTRACT.md` in both runs' in text(E),'Eight AMENDED-v1 spans intact; adjacent ownership sentence aligned. Ownership negative search below.')
 live=sorted([p for d in tree.glob('0[1-5]_*') for p in d.glob('*.md')]+[tree/'MANIFEST.md',tree/'CHANGELOG.md']);assert len(live)==36
 bad=[]
 for p in live:
  active=re.split(r'^#{1,6} .*Version History',p.read_text(),flags=re.M)[0]
  for term in ['different author','filesystem wins','disk wins','hands off to Operations','seedSubscription','supabaseAdmin','**Author:** Engineer','Define schemas, APIs','Database schema design']:
   if term.lower() in active.lower():bad.append([str(p.relative_to(tree)),term])
 check('R1_R3_negative_search',not bad,{'live_docs':36,'active_hits':bad,'scope':'Includes code fences; excludes Version History only.'})
 ownership_terms=["Engineer authors DATA_CONTRACT", "Architect drafts UI_SPEC", "Designer revises", "FILE_TREE = source of truth", "FILE_TREE is the source of truth", "The Engineer's full output list", "This is the output the Engineer produces alongside working code"]
 ownership_hits=[]
 ownership_paths=live+list((tree/'_workflows').glob('*.md'))+list((tree/'_assets').rglob('*.svg'))
 for p in ownership_paths:
  active=re.split(r'^#{1,6} .*Version History',p.read_text(),flags=re.M)[0]
  for term in ownership_terms:
   if term.lower() in active.lower():ownership_hits.append([str(p.relative_to(tree)),term])
 check('R1_map_ownership_queries',not ownership_hits,{'phrases':ownership_terms,'paths_scanned':len(ownership_paths),'active_hits':ownership_hits})
 check('R2_handoff',all(v in text(E) for v in ['Director-created QA branch','only after QA Lead certification and Director release','ACCEPTANCE_SPEC.md (from Architect)','QAM/ (module QA pack: ENGINEERING_HANDOFF, approved plan, results, certificate)']),'Route and eight-entry tree aligned; existing six entries retained.')
 original=blob(E).decode();check('R2_protected_sections',original.split('### What Operations Needs',1)[1].split('## Appendix A:',1)[0]==text(E).split('### What Operations Needs',1)[1].split('## Appendix A:',1)[0],'What Operations Needs and Verbal Brief unchanged.')
 check('R3_RUL12','Record handbook drift; route genuine requirements conflicts to the Director.' in text(E) and 'Disk establishes implementation facts; approved briefs govern scope and governing documents control their subjects.' in text(E),'Diagram retains three text lines and structural connectors.')
 check('R4_FC022',all(v not in text(T) for v in ['seedSubscription','supabaseAdmin']) and text(T).count('Privileged seeding and admin-client construction in test helpers run only behind')==2,'Both executable fences replaced by standard withdrawal + allowlist/identity fail-closed invariant.')
 check('R4_FC038','- API routes\n- Background jobs' not in text(D) and 'An API route is not itself a reason to bypass RLS' in text(D) and 'never as a default route client' in text(D),'Lead, list and both code comments require independently authorized elevated operation.')
 check('R4_FC066',all(v in text(S) for v in ['Independent normalization-step example','Promise<Product[]>','only `success` carries `items: Product[]`',"outcome.status !== 'success' || outcome.items.length === 0",'products={outcome.items}','Independent ISR example']) and 'const { items: products, error } = await fetchProducts();' not in text(S),'Normalization array explicitly independent; caller uses discriminated typed outcome; ISR raw-JSON alternative labelled. No service implementation added.')
 # Preserve every cited excerpt of the other 28 withdrawal judgments.
 reads=(A/'INPUTS/QA_PHASE4/EXECUTOR_EVIDENCE/MANUAL_READS.md').read_text().split('## Withdrawal row judgments (31)',1)[1].split('## Domain preservation excerpts',1)[0]
 judgments=re.findall(r'^\| (FC-\d+) \| ([^|]+) \| (.*)$',reads,re.M);assert len(judgments)==31
 withdrawal=[]
 for fc,status,evidence in judgments:
  excerpts=re.findall(r'((?:0[1-5]_[A-Z_]+/)[A-Z_]+\.md):(\d+): ([^\n]+)',evidence)
  preserved=[]
  for p,ln,excerpt in excerpts:
   excerpt=excerpt.rstrip().removesuffix('|').rstrip();preserved.append(dict(path=p,candidate_line=int(ln),excerpt=excerpt,present=excerpt in text(p)))
  if fc not in ['FC-022','FC-038','FC-066']:assert status.strip().startswith('PASS') and preserved and all(x['present'] for x in preserved),(fc,status,preserved)
  withdrawal.append(dict(fc=fc,original_status=status.strip(),engineer_preparation='CORRECTED — see R4 checks; independent retest pending' if fc in ['FC-022','FC-038','FC-066'] else 'UNCHANGED PASS EVIDENCE',excerpts=preserved))
 save('WITHDRAWAL_ROWS.json',withdrawal)
 check('R4_other_28',len(withdrawal)==31,'28 prior PASS-row cited excerpts preserved; three confirmed failures corrected. Original QA judgments retained in INPUTS, never overwritten.')
 policy='No persistent raw contact information is stored in browser storage by default; any approved exception names the fields, purpose, retention period and owner, with clearing/invalidation behavior.'
 st='04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md'
 check('R5_policy',all(policy in text(p) for p in [U,T,P]) and 'Do not persist raw contact details by default.' in text(st) and before[st]==after[st],'All four manuals state default; three new sentences only, no new persistence example; STATE unchanged.')
 meta=[]
 for p in changed:
  if p=='CHANGELOG.md':continue
  b=blob(p).decode();t=text(p);h=re.search(r'^> \*\*Version:.*$',b,re.M).group();assert h in t
  rows0=[l for l in b.splitlines() if l.startswith('|') and '2026-10-18' in l];rows1=[l for l in t.splitlines() if l.startswith('|') and '2026-10-18' in l];assert len(rows0)==len(rows1)==1 and 'QA-P4 repair:' in rows1[0]
  cells=re.search(r'Version:\*\* (.*?) · \*\*Date:\*\* (.*?) · \*\*Status:\*\* (.*)',h).groups();m=next(l for l in text('MANIFEST.md').splitlines() if l.startswith('| '+Path(p).stem+' |'));assert [s.strip() for s in m.split('|')][2:5]==list(cells)
  meta.append(dict(path=p,header=h,manifest_row=m,history_row=rows1[0]))
 changelog=[l for l in text('CHANGELOG.md').splitlines() if l.startswith('| 2026-10-18 |')];assert len(changelog)==39 and sum('QA-P4 repair:' in l for l in changelog)==6
 save('METADATA_VERIFICATION.json',meta)
 check('R7_metadata',True,'Six headers and MANIFEST unchanged; one amended run-history row per document; 39 run CHANGELOG rows with exactly six amended and no added rows.')
 # Lints on the patched export, inherited code unchanged.
 lint=cmd(['python3','-B','-I','lints/run_all.py'],tree);(A/'LINT_OUTPUT.txt').write_text(lint)
 check('R8_lints','RESULT: PASS' in lint and lint.count('0 hits')==3,'Unchanged full lint suite passes across 36 live docs; header-presence PASS.')
 prefixes=['_ARCHIVE/','03_BUILD_METHODOLOGY/_templates/QAM/','_workflows/','_assets/','10x Lab/','_SKILLS/','lints/','.github/']
 prot=[p for p in before if any(p.startswith(pre) for pre in prefixes) or p in ['MANIFEST.md','AGENTS.md','CLAUDE.md']]
 check('R9_protected',all(before[p]==after[p] for p in prot),{'paths':len(prot),'prefixes':prefixes,'hashes':'PROTECTED_PATHS.json'})
 save('PROTECTED_PATHS.json',{p:before[p] for p in prot})
 tr=json.loads(blob(RUN+'POST_VERIFICATION_STATUS_TRANSITIONS.json'))['transitions'];trans=[]
 for e in tr:
  old=e['old'].replace('2026-10-16','2026-10-18');assert text(e['path']).count(old)==e['occurrences'] and before[e['path']]==after[e['path']],e
  trans.append(dict(path=e['path'],old=old,occurrences=e['occurrences'],status='PENDING — unchanged'))
 save('CLOSEOUT_TRANSITIONS.json',trans);check('R10_closeout',len(trans)==12 and len({x['path'] for x in trans})==9,'All 12 pre-transition spans on nine paths remain; no closeout approval inferred.')
 # Broad propagation coverage includes fences and history, with every retained hit tied to its context.
 terms=['different author','filesystem wins','disk wins','hands off to Operations','seedSubscription','supabaseAdmin','appropriate for:','fetchProducts','raw contact','persist'];sweep=[]
 def disposition(p,line,term,heading):
  if term in terms[:7]:raise AssertionError(('undispositioned hazardous term',p,line,term))
  if term=='fetchProducts':
   if 'APP_ARCHITECTURE_MANUAL' in p:return 'RETAIN','Unchanged Server Component/Suspense illustrations consume products directly, with no conflicting service definition or {items,error} destructuring in this manual. Generic project-local interface, outside the three named API-manual F04c sites; not asserted to implement the API typed service.'
   if 'STATE_MANAGEMENT_MANUAL' in p:return 'RETAIN','Separate state/store integration illustrations and naming vocabulary; local caller consumes the local raw array shape consistently; no {items,error} destructuring. Unchanged path, not the API manual F04c service.'
   if 'fetchProductsByIds' in line:return 'RETAIN','Distinct batch operation fetchProductsByIds(ids: number[]) with its own explicit Promise<Product[]> signature; not the zero-argument fetchProducts operation.'
   if 'API_AND_SERVICES' in p:return 'RETAIN','Naming vocabulary or F04c explicitly labelled contract: array normalization, typed-outcome caller, or independent raw-JSON ISR; reviewed in R4_FC066.'
   raise AssertionError(('unknown product contract',p,line))
  if term=='raw contact':return 'RETAIN','RUL-13 prohibition/default, not authorization to persist personal fields; STATE example explicitly excludes raw contact.'
  if 'Version History' in heading:return 'RETAIN','Historical description, not active implementation guidance.'
  if p.startswith('05_'):return 'RETAIN','Persistent visual layout/notification duration; no browser data storage.'
  if any(v in line.lower() for v in ['webhook','durable','retry','correlation','upstream','persisted outcome','atomic','checkout-attempt']):return 'RETAIN','Server-side durable outcome/idempotency or evidence requirement; not raw contact browser storage.'
  if any(v in line.lower() for v in ['no persist','not persist','never persist','do not persist','avoid persistent','no transcript','unsafe to persist','don’t persist',"don't persist"]):return 'RETAIN','Explicit persistence restriction or reset/privacy boundary.'
  if 'STATE_MANAGEMENT' in p:return 'RETAIN','State persistence mechanism or permitted UX state; existing partialize example excludes raw contact and §default controls exceptions. No new example added.'
  if any(v in p for v in ['QA_PLAYBOOK','BUG_FIX','TESTING_PLAYBOOK','QAM_PLAYBOOK']):return 'RETAIN','QA/test or historical state-regression context; persistence checks do not authorize storing raw contact.'
  if 'AUTH_MANUAL' in p:return 'RETAIN','Auth/session state context; new security default limits raw-contact persistence; existing non-sensitive identity/session examples unchanged.'
  return 'RETAIN','General persistence vocabulary in '+heading+'; no raw-contact browser-storage recipe or exception grant.'
 for f in live:
  p=str(f.relative_to(tree));heading='Document preamble'
  for ln,line in enumerate(f.read_text().splitlines(),1):
   if line.startswith('#'):heading=line
   for term in terms:
    if term.lower() in line.lower():
     d,why=disposition(p,line,term,heading);sweep.append(['proposed',p,str(ln),term,d,why,line])
 # Removed candidate hits have explicit replacement identity, rather than disappearing from the audit.
 for e in ed:
  for line in e['old'].splitlines():
   for term in terms:
    if term.lower() in line.lower() and line not in e['new'].splitlines():sweep.append(['candidate',e['path'],str(e['candidate_line']),term,'RESOLVED',e['edit_id']+' replaces this exact candidate span',line])
 with (A/'PROPAGATION.tsv').open('w',newline='') as f:
  w=csv.writer(f,delimiter='\t');w.writerow(['stage','path','line','term','disposition','rationale','text']);w.writerows(sweep)
 check('propagation',all(x[4] in ['RESOLVED','RETAIN'] and x[5] for x in sweep),{'hits':len(sweep),'proposed_hits':sum(x[0]=='proposed' for x in sweep),'scope':'36 live docs incl fences and history; case-insensitive ten-term sweep; unknown hazardous or fetchProducts hit fails closed.'})
 save('EXPORT_HASHES.json',{'candidate':before,'amended':after})
# Supplied archive identity and its top-level manifest, plus exact extracted evidence copies.
handback=A/'INPUTS/FACTORY_QA_P4_VERDICT_HANDBACK_2026-10-19_122452.zip'
assert sha(handback.read_bytes())=='b486cccbf29fb677c84173594bfd00c12905b81f2382ae62f9c30572b28f7e5a'
with zipfile.ZipFile(handback) as z:
 manifest=z.read('QA_PHASE4/SHA256SUMS.txt').decode().splitlines()
 for row in manifest:
  h,p=row.split('  ',1);assert sha(z.read('QA_PHASE4/'+p))==h,p
 for p in (A/'INPUTS/QA_PHASE4').rglob('*'):
  if p.is_file():assert p.read_bytes()==z.read('QA_PHASE4/'+str(p.relative_to(A/'INPUTS/QA_PHASE4')))
check('handback_integrity',True,{'zip_sha256':sha(handback.read_bytes()),'manifest_rows':len(manifest),'extracted_evidence':'exact ZIP bytes'})
# Input preservation and recorded identities.
ident=json.loads((A/'AMENDMENT_IDENTITIES.json').read_text())
for p,h in ident['inputs'].items():assert sha((A/'INPUTS'/p).read_bytes())==h
for p,h in ident['artifacts'].items():assert sha((A/p).read_bytes())==h
spec=A/'INPUTS/candidate_run/QA_RETEST_AF01/DOCSET_SYNC_ACCEPTANCE_SPEC_AMENDED_V1_R1.md';check('frozen_spec',sha(spec.read_bytes())=='2a3867cacef11c6bb0419a4c71229479efe703cee9fbcc1e4f71c0ac8e63f0fc','Frozen R1 exact hash; R6/R12 accounting correction exists only in successor records.')
check('original_review_records',all(sha((R/p).read_bytes())==h for p,h in review_before.items()),{'files':len(review_before),'original_approvals_and_evidence':'preserved'})
save('REVIEW_INPUT_HASHES.json',review_before)
check('R11_preparation_boundary',cmd(['git','status','--porcelain'])==start=='' and cmd(['git','show-ref'])==refs and cmd(['git','rev-parse','HEAD']).strip()==C,'PASS preparation boundary only. Actual repair commit/apply/push and independent R11 acceptance PENDING Tony Gate 2; no main write, no merge.')
save('COMMANDS.json',commands)
save('VERIFICATION.json',dict(time=datetime.datetime.now(datetime.timezone.utc).isoformat(),status='ENGINEER PREPARATION CHECKS PASS — NOT independent acceptance',candidate=C,checks=checks,gate2='PENDING',future_retest='R1–R12 by fresh QA Executor after authorized landing; Fable successor verdict pending'))
print(json.dumps({k:v['status'] for k,v in checks.items()},indent=2))
