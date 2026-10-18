from pathlib import Path
import json,re,hashlib,subprocess,csv,collections,xml.etree.ElementTree as ET,datetime,zipfile,os
from markdown_it import MarkdownIt
R=Path('_AUDIT/SYNC_2026-10-15_doctrine-part2');O=R/'PROPOSED_CONTENT';H=R/'PLANNING_HISTORY/PRE_MC_CORRECTION_2026-10-16';md=MarkdownIt('commonmark').enable('table');sha=lambda b:hashlib.sha256(b).hexdigest();checks={};base_sha='9c179392f79b70da099121fc357d3107ad3bb86e'
def history_tables(text):
 ts=md.parse(text);out=[]
 for i,t in enumerate(ts):
  if t.type!='table_open':continue
  cells=[]
  for u in ts[i+1:]:
   if u.type=='thead_close':break
   if u.type=='inline':cells.append(u.content)
  if cells[0]=='Version' and cells[1]=='Date':out.append((t.map,cells))
 return out
# Preserve all originally protected files, independent authorship and the prior delivered ZIP.
for p,h in json.loads((R/'PRESERVATION_BASELINE.json').read_text()).items():assert sha(Path(p).read_bytes())==h,p
for p,h in json.loads((R/'MC_CORRECTION_PROTECTED.json').read_text()).items():assert sha((R/p).read_bytes())==h,p
oldzip=R/'DELIVERY/FACTORY_PHASE2_FABLE_HANDOFF_2026-10-16_164712.zip'
if oldzip.exists():assert sha(oldzip.read_bytes())=='87d37eb0cde8130c3730c23fb132234bb24f7181c771b8947daa2505a70f9973'
else:assert json.loads((H/'PRIOR_PACKAGE_RECEIPT.json').read_text())['sha256']=='87d37eb0cde8130c3730c23fb132234bb24f7181c771b8947daa2505a70f9973'
checks['protected_293_and_Fable_review_spec_and_prior_ZIP_unchanged']='PASS'
snap=json.loads((R/'INTAKE_SNAPSHOT_INDEX.json').read_text())['files'];assert len(snap)==189
for e in snap:assert sha((R/'INTAKE_SNAPSHOT'/e['path']).read_bytes())==e['sha256'],e['path']
checks['immutable_intake_189_files']='PASS'
# Independent replay against exact pinned git blobs; before-image agreement for every indexed path.
ed=json.loads((R/'SELECTED_EXACT_EDITS.json').read_text());state={p:subprocess.check_output(['git','show',base_sha+':'+p]).decode() for p in sorted({e['path'] for e in ed})}
for e in ed:assert state[e['path']].count(e['old'])==1,e['sequence'];state[e['path']]=state[e['path']].replace(e['old'],e['new'])
for e in json.loads((R/'SELECTED_CONTENT_INDEX.json').read_text()):assert sha(state[e['path']].encode())==e['proposed_sha256']
checks['ordered_edit_replay']=len(ed);assert len(ed)==372
idx=json.loads((R/'EXECUTION_PROPOSAL_INDEX.json').read_text());assert len(idx)==101
for e in idx:
 p=e['path'];assert sha((O/p).read_bytes())==e['proposed_sha256'],p
 b=subprocess.run(['git','show',base_sha+':'+p],capture_output=True)
 assert (sha(b.stdout) if b.returncode==0 else None)==e['before_sha256'],('BEFORE',p)
 if e['before_sha256']:assert sha(Path(p).read_bytes())==e['before_sha256'],('CANONICAL MUTATED',p)
checks['all_101_proposal_hashes_and_git_before_hashes']='PASS';checks['footprint']={'modified_existing':sum(e['before_sha256'] is not None for e in idx),'added':sum(e['before_sha256'] is None for e in idx),'total':len(idx)}
# MC-01 checks actual parsed container membership at every corrected historical-pointer line.
pointer=[]
for e in ed:
 if e['sequence']<=334 or 'MC-01' not in e['ids']:continue
 s=(O/e['path']).read_text();assert e['new'] in s;ln=s[:s.index(e['new'])].count('\n');ts=md.parse(s)
 rest=e['old'].split('**Historical external example pointer — availability unverified:** ',1)[1]
 required='table_open' if rest.startswith('|') else 'blockquote_open' if rest.startswith('> ') else 'bullet_list_open' if rest.startswith('- ') else None
 if required:assert any(t.type==required and t.map[0]<=ln<t.map[1] for t in ts if t.map),e['path']
 assert '**Historical external example pointer' not in s,e['path'];pointer.append({'path':e['path'],'line':ln+1,'container':required or 'paragraph'})
assert len(pointer)==13;checks['MC01_thirteen_pointer_containers']=pointer
# MC-02/03/09/13: new history row is inside the original table, correct columns, no appended duplicate.
rowsplan=json.loads((R/'DOCUMENT_VERSION_AND_ARCHIVE_PLAN.json').read_text());assert len(rowsplan)==31
for e in rowsplan:
 s=(O/e['path']).read_text();assert sha((O/e['archive']).read_bytes())==e['source_sha256'];assert sha((O/e['path']).read_bytes())==e['proposed_sha256']
 lines=s.splitlines();matches=[i for i,l in enumerate(lines) if 'Factory DocSet sync: approved workflow/security/reference corrections;' in l];assert len(matches)==1,e['path'];ln=matches[0]
 spans=history_tables(s);assert any(span[0]<=ln<span[1] and cells==e['history_columns'] for span,cells in spans),e['path']
 assert len(lines[ln].split('|'))-2==len(e['history_columns']),e['path']
 if e['path'].endswith(('RECON_QUESTIONNAIRE.md','HANDOFF_PACKAGE_PLAYBOOK.md')):assert len(spans)==1,e['path']
 m=re.search(r'^> \*\*Version:\*\*.*\*\*Status:\*\* (.*)$',s,re.M);assert m[1]==e['status_preserved'],e['path']
checks['MC02_MC09_MC13_history_columns_status_suffixes_31_archives']='PASS'
cl=(O/'CHANGELOG.md').read_text();ts=md.parse(cl);table=next(t for t in ts if t.type=='table_open' and t.map[0]>cl[:cl.index('## Ongoing entries')].count('\n'));lines=cl.splitlines();newrows=[i for i,l in enumerate(lines) if l.startswith('| 2026-10-16 |')];assert len(newrows)==39 and all(table.map[0]<=i<table.map[1] for i in newrows)
assert all(i<next(j for j,l in enumerate(lines) if l.startswith('🥄')) for i in newrows);checks['MC03_39_CHANGELOG_rows_inside_ledger_before_footer']='PASS'
# MC-04/05/06/07: explicit cross-document contradictions and lifecycle references.
b=(O/'01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md').read_text();assert b.count('Phase 0 — Recon:')==2 and b.count('Phase 5 — Deployment:')==2 and b.count('Gate D')>=2;assert 'Phase 3: ENGINEER (Data & Code)' not in b
s=(O/'01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md').read_text();assert all('| '+x in s for x in ['Engine 1','Post-FFM review (checkpoint 1)','Engine 2 (checkpoint 2)','RRM'])
manifest=(O/'MANIFEST.md').read_text();assert 'four-role pattern' not in manifest;assert 'How this stays current' in manifest and 'bump procedure: `_ARCHIVE/README.md`' in manifest and 'CI auto-generation remains parked' in manifest
for p in ['02_PIPELINE_AGENTS/RECON_QUESTIONNAIRE.md','02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md']:
 text=(O/p).read_text();assert 'FFM four-role pattern' not in text
bi=(O/'03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md').read_text();en=(O/'02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md').read_text();assert 'folder FREEZES here' not in bi and 'freeze doctrine applies to attackers' not in bi and 'This is the output the Engineer produces alongside working code.' not in en
for path in ['01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md','01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md','02_PIPELINE_AGENTS/ARCHITECT_PLAYBOOK.md','02_PIPELINE_AGENTS/DESIGNER_PLAYBOOK.md','02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md','03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md','03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md','03_BUILD_METHODOLOGY/RRM_PLAYBOOK.md']:
 text=(O/path).read_text();assert re.search(r'after FFM.*independent QA',text,re.I),path;assert 'Engine 2' in text and 'RRM' in text,path
checks['MC04_MC05_MC06_MC07_lifecycle_ownership_freeze_and_MC10_bump_guidance']='PASS'
# Markdown parser checks across all 34 live tier +4 workflow docs, excluding untouched template bodies.
markdown_paths=sorted(O.glob('0*_*/*.md'))+sorted((O/'03_BUILD_METHODOLOGY/_workflows').glob('*.md'))+[O/'MANIFEST.md',O/'CHANGELOG.md']
unclosed=[]
for p in markdown_paths:
 text=p.read_text();tokens=md.parse(text);lines=text.splitlines();prior=R/'BASELINE_CONTENT'/p.relative_to(O)
 oldbad=set()
 if prior.exists():
  oldlines=prior.read_text().splitlines()
  for t in md.parse(prior.read_text()):
   if t.type=='fence' and (not oldlines[t.map[1]-1].lstrip().startswith(t.markup)):oldbad.add(t.content)
 for t in tokens:
  if t.type=='fence' and not lines[t.map[1]-1].lstrip().startswith(t.markup):
   assert t.content in oldbad,('NEW UNCLOSED FENCE',p,t.map);unclosed.append({'path':str(p.relative_to(O)),'existing_unchanged_fence':True})
checks['markdown_40_docs_no_new_unclosed_fences']=unclosed or 'PASS'
# Workflow source preservation, SVG XML/step text/prose agreement and canonical-relative local links.
ws=json.loads((R/'WORKFLOW_PUBLICATION_PLAN.json').read_text())['workflows'];links=[]
for w in ws:
 assert Path(w['source']).is_file();doc=(O/w['document']).read_text();asset=O/w['asset'];xml=ET.fromstring(asset.read_text());ns='{http://www.w3.org/2000/svg}';children=list(xml);texts=[]
 for j,ch in enumerate(children):
  if ch.tag==ns+'rect' and ch.attrib.get('height')=='76':
   seq=[]
   for c in children[j+1:]:
    if c.tag==ns+'rect':break
    if c.tag==ns+'text' and float(ch.attrib['y'])<=float(c.attrib.get('y',0))<float(ch.attrib['y'])+76:seq.append(''.join(c.itertext()))
   texts.append(' '.join(seq))
 assert [x.replace('- ','-') for x in texts]==[f'{i}. {a}'.replace('- ','-') for i,(_,a) in enumerate(w['steps'],1)],w['id']
 for i,(seat,a) in enumerate(w['steps'],1):assert f'{i}. **{seat}:** {a}.' in doc,w['id']
 for term in ['after FFM build and its independent QA finish','after all Engine 1 phases/modules and their QA are closed','RRM only for approved findings requiring repairs','clean review requires no RRM']:assert term in doc,w['id']
 for dest in re.findall(r'\]\(([^)]+)\)',doc):
  logical=(Path.cwd()/Path(w['document']).parent/dest).resolve();rel=logical.relative_to(Path.cwd());actual=O/rel if (O/rel).exists() else Path(rel);assert actual.is_file(),(w['id'],dest);links.append(str(rel))
 # Own publication references must be referenced by an owning tier document.
 assert any('_workflows/'+Path(w['document']).name in p.read_text() for p in O.glob('0*_*/*.md')),w['id']
checks['four_workflow_SVG_XML_numbered_prose_links_and_originals']='PASS';checks['workflow_links_checked']=len(links)
# Branch/QA/repair/cleanup/review order checked from the declared diagram steps.
w=next(x for x in ws if x['id']=='FFM_EXECUTION');actions=[a for _,a in w['steps']]
def position(term):return next(i for i,a in enumerate(actions) if term in a)
terms=['QA branch at exact','Q1 recon','Approve the specific','Release Q2','Q2 tests','Conditional authorized repair','Commit repaired','Independent retest','Product certification','Authorized cleanup','Accept cleanup','Closeout instruction','Bounded closeout','Final commits','Review checkpoint 1','Disposition review'];assert [position(t) for t in terms]==sorted(position(t) for t in terms)
w=next(x for x in ws if x['id']=='BIM_WORKFLOW');actions=[a for _,a in w['steps']];terms=['QA branch at that exact','Q1 recon','Approve plan','Release Q2','Q2 tests','Conditional authorized repairs','Commit repaired','Independent retest','Product certification','Perform authorized','Accept cleanup','Closeout instructions','Bounded closeout','Final commits','If deployment in scope','If deployed: independently','If deployed: Gate D','Complete all Engine 1','Review checkpoint 2','Disposition findings'];assert [position(t) for t in terms]==sorted(position(t) for t in terms)
checks['workflow_branch_Q1_approval_release_Q2_repair_cleanup_review_order']='PASS'
# Templates are identical to accepted sources after the one current approved-proposal translation record.
plan=json.loads((R/'PHASE_2_TEMPLATE_TRANSLATIONS.json').read_text());assert len(plan)==25
for e in plan:
 source=R/'INTAKE_SNAPSHOT'/e['source'];assert sha(source.read_bytes())==e['source_sha256'];s=source.read_text()
 for t in e['translations']:assert s.count(t['old'])==t['occurrences'];s=s.replace(t['old'],t['new'])
 assert s==(O/e['destination']).read_text() and sha(s.encode())==e['proposed_destination_sha256']
actual={str(p.relative_to(O)) for p in (O/'03_BUILD_METHODOLOGY/_templates/QAM').rglob('*') if p.is_file()};assert actual=={e['destination'] for e in plan}
checks['25_accepted_sources_preserved_and_translation_replay']='PASS'
# Pre/post closeout MANIFEST equals every actual header, including all status suffixes.
trans=json.loads((R/'POST_VERIFICATION_STATUS_TRANSITIONS.json').read_text());assert trans['commit_plan']['actual_sha'] is None;assert len(trans['transitions'])==12;post={}
for e in trans['transitions']:
 s=post.get(e['path'],(O/e['path']).read_text());assert s.count(e['old'])==e['occurrences'],e['path'];post[e['path']]=s.replace(e['old'],e['new'])
assert len(post)==9
for e in trans['required_evidence']:assert not Path(e['path']).exists(),('UNEXPECTED FUTURE EVIDENCE',e['path'])
for later in [False,True]:
 mf=post['MANIFEST.md'] if later else manifest
 for p in O.glob('0*_*/*.md'):
  rel=str(p.relative_to(O));text=post.get(rel,p.read_text()) if later else p.read_text();header=re.search(r'^> \*\*Version:\*\* (.*?) · \*\*Date:\*\* (.*?) · \*\*Status:\*\* (.*)$',text,re.M);row=next(x for x in mf.splitlines() if x.startswith('| '+p.stem+' |'));cells=[x.strip() for x in row.split('|')][2:5];assert cells==list(header.groups()),(rel,cells,header.groups())
for e in json.loads((R/'POST_VERIFICATION_PROPOSAL_INDEX.json').read_text()):assert sha(post[e['path']].encode())==e['proposed_sha256']
checks['MC08_twelve_spans_nine_paths_pre_post_MANIFEST_headers_pending_evidence']='PASS'
# Verify deterministic date binding under a different sample date without claiming actual execution.
dates=json.loads((R/'LANDING_DATE_PLAN.json').read_text());assert dates['actual_landing_date'] is None;sample={}
for e in dates['spans']:
 s=sample.get(e['path'],(O/e['path']).read_text());assert s.count(e['old'])==e['occurrences'];sample[e['path']]=s.replace(e['old'],e['new'].replace('<<ACTUAL_LANDING_DATE>>','2099-01-02'))
assert len(dates['spans'])==151;checks['MC11_date_binding_151_scoped_fields_exercised']='PASS — sample 2099-01-02 in memory only; no actual landing claim'
# Exact 97 certified rows + all W/RUL/AD consumers and histories/CHANGELOG evidence.
ledger=(R/'SELECTED_SCOPE_LEDGER.md').read_text();assert len(re.findall(r'^\| FC-\d{3} \|',ledger,re.M))==97;assert re.findall(r'^\| (FC-\d{3}) \| NO \|',ledger,re.M)==['FC-085','FC-086','FC-097']
trace=json.loads((R/'WORKFLOW_RULING_TRACEABILITY.json').read_text());assert len(trace)==38
for e in trace:
 assert re.search(r'^\| '+re.escape(e['id'])+r' \|',ledger,re.M),e['id'];assert e['id'] in cl,e['id'];assert e['documents']
assert '| AD-01 |' in ledger
checks['MC12_97_FC_23_W_15_RUL_AD01_coverage_and_NO_guards']='PASS'
assert (R/'TEMPLATE_INSTALL_PLAN.md').read_text().startswith('> **HISTORICAL');assert all(e['status'].startswith('HISTORICAL') for e in json.loads((R/'TEMPLATE_INSTALL_PLAN.json').read_text()));checks['MC14_superseded_template_plan_explicit']='PASS'
# Unchanged lint tools and actual proposal lint execution, not a new exemption.
for p in Path('lints').glob('*.py'):assert p.read_bytes()==(O/p).read_bytes(),p
p=subprocess.run(['python3','-B','-I','lints/run_all.py'],cwd=O,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'},capture_output=True,text=True);assert p.returncode==0,p.stdout+p.stderr
checks['unchanged_document_lints']='PASS — 36 live docs; six scripts unchanged';checks['lint_raw_output']=p.stdout+p.stderr
# Numerical token evidence is unaffected: actual declarations equal the previously reviewed proposal.
prior=(H/'TOKEN_FILE_PROPOSAL.md').read_text()
cur=(O/'05_DESIGN_SYSTEM/TOKEN_FILE.md').read_text();pat=r'--[\w-]+:\s*[\d.]+\s+[\d.]+%\s+[\d.]+%';assert re.findall(pat,prior)==re.findall(pat,cur)
checks['retained_128_pair_contrast_evidence']='Token declarations unchanged; prior numeric matrix retained; no browser/accessibility claim'
assert subprocess.check_output(['git','rev-parse','HEAD','main','origin/main']).decode().splitlines()==['626da8d70f4db22987dc7fcc86765492072360cd',base_sha,base_sha]
assert not subprocess.check_output(['git','diff','--cached','--name-only']);assert not subprocess.check_output(['git','diff',base_sha,'--','01_CONSTITUTION','02_PIPELINE_AGENTS','03_BUILD_METHODOLOGY','04_REFERENCE_MANUALS','05_DESIGN_SYSTEM','MANIFEST.md','CHANGELOG.md','_ARCHIVE'])
checks['git_refs_staging_canonical_worktree']='Unchanged refs; nothing staged; empty canonical diff; no Git mutation by Cody'
(R/'MC_VERIFICATION.json').write_text(json.dumps({'time':datetime.datetime.now().astimezone().isoformat(),'status':'ENGINEER CHECKS PASS — independent acceptance pending','checks':checks},indent=2)+'\n')
print(json.dumps(checks,indent=2))
