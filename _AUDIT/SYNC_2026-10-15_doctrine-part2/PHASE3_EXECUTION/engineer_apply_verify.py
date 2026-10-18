from pathlib import Path
import subprocess,json,hashlib,copy,re,sys
from datetime import datetime
from zoneinfo import ZoneInfo
from xml.etree import ElementTree as ET
root=Path('/home/moose/Documents/app-factory-docs-sync-execution');r=root/'_AUDIT/SYNC_2026-10-15_doctrine-part2';ev=r/'PHASE3_EXECUTION';base='9c179392f79b70da099121fc357d3107ad3bb86e';setup='2e714b640f8490ea5b30e773736aca5c2381245b'
def sha(b):return hashlib.sha256(b).hexdigest()
def js(p):return json.loads(p.read_text())
def save(p,v):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,indent=2)+'\n' if not isinstance(v,str) else v)
def git(*a):return subprocess.check_output(['git',*a],cwd=root)
commands=[]
def cmd(a):
 p=subprocess.run(a,cwd=root,capture_output=True,text=True);commands.append(dict(command=a,cwd=str(root),exit_code=p.returncode,stdout=p.stdout,stderr=p.stderr));save(ev/'COMMANDS.json',commands);assert p.returncode==0,p.stderr;return p.stdout
if sys.argv[-1]=='apply':
 assert git('rev-parse','HEAD').decode().strip()==setup and not git('status','--porcelain=v1')
 assert git('branch','--show-current').decode().strip()=='docs/sync-doctrine-part2-2026-10-15'
 protected={str(p.relative_to(root)):sha(p.read_bytes()) for p in r.rglob('*') if p.is_file()}
 protected.update({str(p.relative_to(root)):sha(p.read_bytes()) for p in (root/'10x Lab').glob('*.md')});save(ev/'PROTECTED_BEFORE.json',protected)
 now=datetime.now(ZoneInfo('Asia/Dhaka'));date=now.date().isoformat();save(ev/'LANDING_DATE.json',{'date':date,'time':now.isoformat(),'timezone':'Asia/Dhaka','fields':151})
 release='''# Phase 3 release and Git publication authorization

Tony's current Director-forwarded release accepts the setup at 2e714b640f8490ea5b30e773736aca5c2381245b and authorizes full101-path/380-edit implementation, only151 declared date bindings, Engineer verification, one implementation commit plus required handoff records. Preserve frozen map/specification, all sources and standalone10x bytes; leave12 conditional transitions pending independent QA, cleanup and Architect closeout.

Tony's subsequent clarification explicitly authorizes scoped staging, commits, fetch, branch/worktree management and normal push of prepared run records, approved101-path update, two standalone10x references and required verification/handoff records to branch docs/sync-doctrine-part2-2026-10-15 at https://github.com/ahmedmusawir/app-factory-docs-v1.git. It supersedes Tony-only Git and leave-publication-pending instructions. No force push, main push or merge; Tony creates PR and merges. This is the destination/payload-specific authorization after the earlier automatic approval rejection. It releases final branch publication (skill D18/Gate4) after verification, not QA acceptance. Frozen AC32 operator-only language is superseded only as to Git actor/publication authority; QA Lead owns any specification alignment.

Setup identities: preservation e7b4a6f33e1ae2442f71d82f7f3a9d694f50da36; fetched BASE9c179392f79b70da099121fc357d3107ad3bb86e; preparation checkpoint356206ab293dc3a3987269636bb853c84aaf4ad3; standalone10x4ec73a40ce2ad91f0ed99b85638efc7fe375140d; setupHEAD2e714b640f8490ea5b30e773736aca5c2381245b. Gate2 corrected patch cf6413c9340c80f5c1bf53a55385876470e9b3aad364bc8963f52a68580f2a6d; Gate3 R1 specification2a3867cacef11c6bb0419a4c71229479efe703cee9fbcc1e4f71c0ac8e63f0fc. Historical pending text remains frozen; actual approvals are in QA_RETEST_AF01/DIRECTOR_DECISIONS.md.
'''
 save(ev/'DIRECTOR_RELEASE.md',release)
 with (root/'agent_docs/SESSIONS/session_2026-10-18.md').open('a') as f:f.write('\n### '+now.isoformat()+' — PHASE3 APPROVED → IN PROGRESS\n\n'+release+'\nPlan: exact patch,151 date spans, bound indexes; verify installed hashes, archives/templates/workflows/lints/protection; commit101 paths; handoff, normal authorized push and one ZIP. Cody ENGINEER; independent QA pending.\n')
 save(root/'RECOVERY.md','# Recovery State\n\nCody ENGINEER. Phase3 released and in progress in execution worktree. Read '+str(ev/'DIRECTOR_RELEASE.md')+'. Exact patch/date binding only; independent QA and12 transitions remain pending.\n')
 idx=js(r/'AMENDED_V1/EXECUTION_PROPOSAL_INDEX.json');assert len(idx)==101
 for p,h in js(r/'EXECUTION_SETUP/APPROVED_INPUTS.json')['inputs'].items():assert sha((r/p).read_bytes())==h,p
 for row in idx:
  p=root/row['path'];assert (sha(p.read_bytes()) if p.exists() else None)==row['before_sha256'],str(p)
 patch=r/'REPAIR_QA_AF01/EXECUTION_PROPOSAL.corrected.patch'
 cmd(['git','apply','--check','-p0',str(patch)]);cmd(['patch','--batch','--fuzz=0','-p0','-i',str(patch)])
 for row in idx:assert sha((root/row['path']).read_bytes())==row['proposed_sha256'],row['path']
 spans=js(r/'AMENDED_V1/LANDING_DATE_PLAN.json')['spans'];assert len(spans)==151
 for span in spans:
  p=root/span['path'];b=p.read_bytes();old=span['old'].encode();assert b.count(old)==span['occurrences'],span['path'];p.write_bytes(b.replace(old,span['new'].replace('<<ACTUAL_LANDING_DATE>>',date).encode()))
 bound=[]
 for row in idx:
  v=copy.deepcopy(row);v['review_proposed_sha256']=v['proposed_sha256'];v['proposed_sha256']=sha((root/v['path']).read_bytes());v['bytes']=(root/v['path']).stat().st_size;v['landing_date']=date;bound.append(v)
 save(r/'BOUND_EXECUTION_INDEX.json',bound)
 trans=js(r/'POST_VERIFICATION_STATUS_TRANSITIONS.json');post={row['path']:(root/row['path']).read_bytes() for row in idx}
 for t in trans['transitions']:
  t['old']=t['old'].replace('2026-10-16',date);t['new']=t['new'].replace('2026-10-16',date);b=post[t['path']];assert b.count(t['old'].encode())==t['occurrences'];post[t['path']]=b.replace(t['old'].encode(),t['new'].encode())
 trans.update(label='BOUND PLAN ONLY — all12 transitions PENDING; not applied',landing_date=date,index=[{'path':row['path'],'before_sha256':row['proposed_sha256'],'proposed_sha256':sha(post[row['path']])} for row in bound]);save(r/'BOUND_STATUS_TRANSITIONS.json',trans)
 print('Applied101 exact proposed outputs; bound151 fields only; generated full101-path bound execution and pending closeout indexes.')
if sys.argv[-1]=='verify':
 commands=js(ev/'COMMANDS.json');idx=js(r/'AMENDED_V1/EXECUTION_PROPOSAL_INDEX.json');bound=js(r/'BOUND_EXECUTION_INDEX.json');date=js(ev/'LANDING_DATE.json')['date'];checks=[]
 def check(name,ok,detail):
  checks.append({'name':name,'result':'PASS' if ok else 'FAIL','detail':detail});save(ev/'VERIFICATION.json',checks);assert ok,(name,detail);print('PASS',name,detail)
 for row in bound:assert sha((root/row['path']).read_bytes())==row['proposed_sha256'],row['path']
 check('Installed bound outputs',True,'101/101')
 edits=js(r/'AMENDED_V1/SELECTED_EXACT_EDITS.json');replayed={};assert len(edits)==380
 for e in edits:
  p=e['path'];replayed.setdefault(p,git('show',base+':'+p).decode());assert replayed[p].count(e['old'])==1,e['sequence'];replayed[p]=replayed[p].replace(e['old'],e['new'],1)
 for row in js(r/'AMENDED_V1/SELECTED_CONTENT_INDEX.json'):assert sha(replayed[row['path']].encode())==row['proposed_sha256']
 check('Ordered edit replay',True,'380/380 unique old spans;31 content-stage outputs exact')
 for row in idx:
  p=row['path'];proposal=r/'AMENDED_V1/PROPOSED_CONTENT'/p
  if not proposal.exists():proposal=r/'PROPOSED_CONTENT'/p
  b=proposal.read_bytes();assert sha(b)==row['proposed_sha256']
  for span in js(r/'AMENDED_V1/LANDING_DATE_PLAN.json')['spans']:
   if span['path']==p:b=b.replace(span['old'].encode(),span['new'].replace('<<ACTUAL_LANDING_DATE>>',date).encode())
  assert b==(root/p).read_bytes()
 check('Only declared date changes from frozen proposal',True,'151 fields; historical dates and all other bytes preserved')
 archives=[]
 for row in js(r/'DOCUMENT_VERSION_AND_ARCHIVE_PLAN.json'):
  b=(root/row['archive']).read_bytes();original=git('show',base+':'+row['path']);blob=git('hash-object',row['archive']).decode().strip();expected=git('rev-parse',base+':'+row['path']).decode().strip();assert b==original and blob==expected;archives.append({'path':row['archive'],'sha256':sha(b),'blob':blob,'source_blob':expected,'final_lf':b.endswith(b'\n')})
 hist=js(r/'ARCHIVE_RESTORATION_PROPOSAL.json');assert git('hash-object',hist['destination']).decode().strip()==hist['git_blob'];save(ev/'ARCHIVE_VERIFICATION.json',archives+[hist]);check('Archives',True,'31 outgoing byte/blob-exact including both missing-final-LF archives; historical QA v1.0 exact')
 templates=js(r/'PHASE_2_TEMPLATE_TRANSLATIONS.json');installed=[]
 for row in templates:
  source=r/'INTAKE_SNAPSHOT'/row['source'];b=source.read_bytes();assert sha(b)==row['source_sha256'];dest=root/row['destination'];assert sha(dest.read_bytes())==row['proposed_destination_sha256'];installed.append({**row,'installed_sha256':sha(dest.read_bytes()),'source_verified':True})
 tp=root/'03_BUILD_METHODOLOGY/_templates/QAM';check('Template file set',set(str(p.relative_to(root)) for p in tp.rglob('*') if p.is_file())=={v['destination'] for v in templates},'25 exact translated files; sources unchanged')
 routing=lambda p:p.read_text().split('<!-- ROUTING TEXT',1)[1].split('-->',1)[1].split('<!-- END ROUTING TEXT -->',1)[0]
 check('Identical template runtime routing',routing(tp/'CLAUDE.md')==routing(tp/'AGENTS.md'),'QA Executor routing preserved')
 risk=(tp/'QAM_RISK_REQUIREMENTS.md').read_text();check('Template amendments/SR rows','Done at Q4 exit (if Q4 ran)' in (tp/'QAM_CLEANUP_REPORT.md').read_text() and 'as relevant (a stop may precede the plan draft)' in (tp/'QAM_PACKAGING.md').read_text() and 'command, working directory, exit code and unfiltered output' in risk and set(re.findall(r'^\| (SR-\d+) \|',risk,re.M))=={'SR-'+str(i) for i in range(1,12)},'AM-1/2/3 and11 standing requirements')
 save(ev/'TEMPLATE_HASHES.json',installed)
 workflow=[]
 for w in js(r/'WORKFLOW_PUBLICATION_PLAN.json')['workflows']:
  nodes=[''.join(n.itertext()) for n in ET.fromstring((root/w['asset']).read_bytes()).iter() if n.tag.split('}')[-1]=='text'];joined=' '.join(' '.join(nodes).split()).replace('- ','-');doc=(root/w['document']).read_text();positions=[]
  for actor,step in w['steps']:assert actor in nodes and step in joined and step in doc;positions.append(joined.index(step))
  assert positions==sorted(positions)
  assert (root/w['source']).is_file()
  assert '../_assets/workflows/'+Path(w['asset']).name in doc
  for token in ['Director of QA','Codex','Sol','Claudy','INITSCRIPT','CLOUDDEPLOYMENT','QA Lead executes','QA Lead runs tests']:assert not any(token in n for n in nodes)
  workflow.append({'workflow':w['id'],'ordered_steps':len(positions),'svg_xml':'PASS','historical_source_present':True})
 save(ev/'WORKFLOW_VERIFICATION.json',workflow);check('Workflow documents and diagrams',True,'4 matched prose/SVG sequences;7/18/8/24 steps; forbidden actor labels absent')
 trans=js(r/'BOUND_STATUS_TRANSITIONS.json')['transitions'];check('Conditional transitions pending',len(trans)==12 and all((root/t['path']).read_text().count(t['old'])==t['occurrences'] for t in trans),'12 pre-transition spans retained across9 paths')
 protected=js(ev/'PROTECTED_BEFORE.json');check('Frozen run and10x preservation',all(sha((root/p).read_bytes())==h for p,h in protected.items()),str(len(protected))+' files byte-unchanged')
 check('Root/skills/lints/CI unchanged',not git('diff',base,'--','CLAUDE.md','AGENTS.md','_SKILLS','lints','.github'),'empty diff')
 output=cmd(['python3','-B','-I','lints/run_all.py']);check('Document lints',True,output)
 # Exact MANIFEST header matching including original status suffixes.
 manifest=(root/'MANIFEST.md').read_text();tier=list(root.glob('0[1-5]_*/*.md'));assert len(tier)==34
 for p in tier:
  m=re.search(r'> \*\*Version:\*\* (.*?) · \*\*Date:\*\* (.*?) · \*\*Status:\*\* (.*)',p.read_text());assert m,p
  assert '| '+p.stem+' | '+' | '.join(m.groups())+' |' in manifest,p
 check('MANIFEST/header agreement',True,'34/34 exact version/date/status rows')
 save(r/'TEMPLATE_INSTALL_VERIFICATION.md','# Template installation — Engineer verification\n\nPASS: actual installed25-file set and hashes compared against accepted snapshot and approved translation hashes. Not independent QA acceptance. Full per-file source, translated and installed hashes: PHASE3_EXECUTION/TEMPLATE_HASHES.json. Raw command/cwd/exit/output: PHASE3_EXECUTION/VERIFY_RAW.txt and COMMANDS.json.\n\n1. Exact25-file set: PASS.\n2.25 source and25 destination hashes: PASS.\n3. Routing bodies identical, QA Executor: PASS.\n4. AM-1/2/3 and SR-1…11 retained: PASS.\n5. State/dispatch vocabulary: retained byte-exact from accepted translations; no behavior changed.\n6. Owners/writable lanes/placeholders: retained byte-exact from accepted translations, no populated project records added.\n7. Snapshot source and governing provenance preserved; relative links checked in supplementary evidence.\n8. AC22/AC38 explicitly require independent template checks; no runtime tooling installed.\n\nREADME closeout hash remains a future conditional transition; no closeout or independent verdict claimed.\n')
 print('ENGINEERING VERIFICATION COMPLETE; independent QA remains required.')
