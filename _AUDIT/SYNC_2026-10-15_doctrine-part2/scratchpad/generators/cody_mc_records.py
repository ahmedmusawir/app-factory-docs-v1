from pathlib import Path
import json,re,hashlib,difflib,shutil,datetime
R=Path('_AUDIT/SYNC_2026-10-15_doctrine-part2');O=R/'PROPOSED_CONTENT';H=R/'PLANNING_HISTORY/PRE_MC_CORRECTION_2026-10-16';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
# MC-08: bounded future closeout, with exact MANIFEST updates and existing pending evidence.
trans=json.loads((H/'POST_VERIFICATION_STATUS_TRANSITIONS.json').read_text())['transitions']
for e in trans:e['trigger']='PENDING: Gate 2/3 approval; actual installed/new-document verification; independent product verdict and cleanup acceptance; Architect closeout instruction. Tony applies only in the named closeout commit. See commit_plan and required_evidence.'
manifest=(O/'MANIFEST.md').read_text()
for name in ['QAM_PLAYBOOK','RRM_PLAYBOOK','DEPLOYMENT_PLAYBOOK']:
 line=next(l for l in manifest.splitlines() if l.startswith('| '+name+' |'));assert 'DRAFT FOR EXECUTABLE-MAP REVIEW — NOT INSTALLED' in line
 trans.append(dict(path='MANIFEST.md',old=line,new=line.replace('DRAFT FOR EXECUTABLE-MAP REVIEW — NOT INSTALLED','Active'),occurrences=1,trigger='Same closeout commit as the matching playbook header transition; rows must equal actual headers.'))
for p in sorted((O/'03_BUILD_METHODOLOGY/_workflows').glob('*.md')):
 old='**Status:** Proposed — pending verified publication';assert old in p.read_text()
 trans.append(dict(path=str(p.relative_to(O)),old=old,new='**Status:** Active reference',occurrences=1,trigger='Same named closeout commit, after actual workflow/diagram publication and independent consistency checks.'))
commit={'purpose':'Tony closeout: activate verified new doctrine/workflow references and record installed-template provenance after accepted product QA and cleanup; no product/policy changes','suggested_subject':'docs(sync): activate verified doctrine and workflow references [SYNC_2026-10-15_doctrine-part2]','actual_sha':None,'actual_sha_status':'PENDING — commit does not exist; record observed SHA only after Tony creates it, in a subsequent receipt, never self-referentially','conditions':['Gate 2 exact map including these 12 transitions approved; Fable finalized spec approved at Gate 3','Actual pre-transition installed-file comparison for all 25 templates passes, including source/translation/destination hashes and raw command/cwd/exit/output','Independent QA Lead accepts product verdict for the exact pre-transition candidate; cleanup retention and cleanup acceptance recorded separately','Architect issues bounded closeout instruction naming exactly the nine transition paths; Tony performs Git mutations'],'bounded_retest':{'owner':'Independent QA Executor; QA Lead accepts resulting evidence and final verdict','checks':['AC25: actual MANIFEST/header equality, count/reverse map/appendix unchanged','AC27: per-document history rows unchanged by status-only closeout','AC31: unchanged full lint suite green','AC32: exact nine-path canonical diff, Tony commit identity, no unapproved edits','AC33: all 12 exact spans; required evidence predates actual commit; actual SHA recorded after creation','Repeat 25-template source/approved-translation/installed comparison allowing only the one declared README provenance transition','Verify four workflow documents still link their SVGs/originals and both review checkpoints, RRM routing, QA/cleanup/release distinctions remain unchanged'],'failure_behavior':'Stop release; QA Lead routes bounded repair or a Gate 2/3 amendment. Do not transfer the pre-transition verdict to changed bytes automatically.'}}
required=[{'path':str(R/'TEMPLATE_INSTALL_VERIFICATION.md'),'status':'PENDING — not created; future actual evidence required','minimum':'25 source hashes, approved translated hashes and installed hashes before/after declared README transition; exact file set, standing amendments/SR preservation; command, cwd, exit, unfiltered safe output'}, {'path':str(R/'RUN_SUMMARY.md'),'status':'PENDING — not created; future actual evidence required','minimum':'Actual implementation/QA/cleanup identities and reports, verified landing date, Architect closeout authority, pre/post-transition hashes, intended commit purpose and actual closeout SHA only after creation, independent bounded-retest results'}, {'path':str(R/'CLOSEOUT_VERIFICATION.md'),'status':'PENDING — not created; future independent bounded verification required','minimum':'Exact closeout diff; 12 spans/9 paths; AC25/27/31/32/33 and template/workflow checks; QA Lead final acceptance or routed findings'}]
plan={'label':'ENGINEER-PROPOSED conditional closeout plan for Gate 2 review; no completed evidence or approval claimed','commit_plan':commit,'required_evidence':required,'date_binding':'Old/new spans carry planned 2026-10-16 where applicable; bind only landing-date fields through LANDING_DATE_PLAN.json before implementation; recompute both pre/post hashes from actual bytes. Do not change historical approval dates.','transitions':trans}
assert len(trans)==12;state={}
for e in trans:
 p=e['path'];s=state.get(p,(O/p).read_text());assert s.count(e['old'])==e['occurrences'],p;state[p]=s.replace(e['old'],e['new'])
close=R/'CLOSEOUT_PROPOSED_CONTENT';index=[];diff=[]
for p,s in sorted(state.items()):
 d=close/p;d.parent.mkdir(parents=True,exist_ok=True);d.write_text(s);before=(O/p).read_bytes();index.append(dict(path=p,before_sha256=hashlib.sha256(before).hexdigest(),proposed_sha256=hashlib.sha256(s.encode()).hexdigest()));diff.extend(difflib.unified_diff(before.decode().splitlines(True),s.splitlines(True),fromfile=p,tofile=p))
assert len(index)==9
(R/'POST_VERIFICATION_STATUS_TRANSITIONS.json').write_text(json.dumps(plan,indent=2)+'\n');(R/'POST_VERIFICATION_PROPOSAL_INDEX.json').write_text(json.dumps(index,indent=2)+'\n');(R/'POST_VERIFICATION_PROPOSAL.patch').write_text(''.join(diff))
# Future evidence forms are clearly templates, not the nonexistent evidence files above.
et=R/'EVIDENCE_TEMPLATES';et.mkdir(exist_ok=True)
(et/'TEMPLATE_INSTALL_VERIFICATION.template.md').write_text('''# TEMPLATE — actual installation verification is pending

This form is preparation only. Create the actual run/TEMPLATE_INSTALL_VERIFICATION.md after authorized canonical installation, and fill observed values. No verification result is prefilled.

| Field | Observed value |
|---|---|
| Actual candidate / tree identity | PENDING |
| Approved map/spec identities | PENDING |
| Actual landing date | PENDING |
| Exact 25-file set / source membership | PENDING |
| Per-file accepted source / approved translation / installed SHA-256 | PENDING |
| Source amendments AM-1/2/3 and SR-1…11 preservation | PENDING |
| Commands, cwd, exit codes and unfiltered safe output | PENDING |
| Pre-transition README hash | PENDING |
| Post-transition README hash (only after authorized closeout) | PENDING |
| Independent verification / limitations | PENDING |
''')
(et/'RUN_SUMMARY.template.md').write_text('''# TEMPLATE — actual run summary is pending

Record actual events and observed identities only. No canonical implementation or QA verdict exists in this preparation.

Implementation CONTENT_SHA: PENDING. Independent QA candidate/verdict evidence: PENDING. Actual landing date: PENDING. Installed template verification: PENDING. Cleanup retention/acceptance: PENDING. Architect bounded closeout instruction: PENDING.

Intended Tony closeout purpose: activate verified new doctrine/workflow references and installed-template provenance under POST_VERIFICATION_STATUS_TRANSITIONS.json. Actual closeout SHA: PENDING until Tony creates it; record afterward in a subsequent receipt. Independent bounded verification: PENDING. Final QA Lead verdict/acceptance: PENDING. Publication/merge/local-main synchronization: PENDING.

Copy the approved selected disposition sets without changing certified FC fields; record partial/external/deferred components separately. Never claim the entire 97-finding campaign resolved.
''')
# MC-11: exact date-binding spans, never blanket replacement of historical ruling dates.
dates=[]
for p in sorted(O.rglob('*.md')):
 rel=p.relative_to(O)
 if 'lints' in rel.parts or '_ARCHIVE' in rel.parts:continue
 for line in p.read_text().splitlines():
  header=line.startswith('> **Version:**') and '· **Date:** 2026-10-16' in line
  currentrow=line.startswith('| ') and '2026-10-16' in line and ('Factory DocSet sync:' in line or 'current correction pass:' in line or str(rel)=='CHANGELOG.md' or str(rel)=='MANIFEST.md' or '/_workflows/' in str(rel))
  # Restrict MANIFEST to live-doc cells; do not alter references/historical prose.
  if header or currentrow:
   new=line.replace('· **Date:** 2026-10-16','· **Date:** <<ACTUAL_LANDING_DATE>>') if header else line.replace('| 2026-10-16 |','| <<ACTUAL_LANDING_DATE>> |')
   if new!=line:dates.append(dict(path=str(rel),old=line,new=new,occurrences=p.read_text().count(line),type='header' if header else 'current row'))
(R/'LANDING_DATE_PLAN.json').write_text(json.dumps({'label':'ENGINEER-PROPOSED deterministic execution-date binding; no actual landing date exists yet','planned_review_date':'2026-10-16','actual_landing_date':None,'instructions':'Before authorized implementation, bind only these declared current header/row fields to actual landing date, record the value in actual execution evidence and generate BOUND_EXECUTION_INDEX.json and BOUND_STATUS_TRANSITIONS.json with recomputed pre/post hashes; retain the reviewed/frozen map and review-time indexes unchanged. Historical approval/source dates remain untouched. If a span changed, stop and reconcile approved map identities; do not blanket-replace dates.','spans':dates},indent=2)+'\n')
# MC-12: join all W and RUL consumers; FC dispositions and certified fields are preserved.
ed=json.loads((R/'SELECTED_EXACT_EDITS.json').read_text());workflow={e['id']:e for e in json.loads((R/'PROPOSED_EXACT_EDITS.json').read_text())};rows=[]
metadata=json.loads((R/'DOCUMENT_VERSION_AND_ARCHIVE_PLAN.json').read_text())
for prefix,ns in [('W',range(1,24)),('RUL-',range(1,16))]:
 for n in ns:
  id=f'{prefix}{n:02}';direct=[e for e in ed if id in e['ids']];docs=sorted({e['path'] for e in direct}|{e['path'] for e in metadata if id in e['ids']})
  if id in workflow:docs=sorted(set(docs+[workflow[id]['path']]))
  if prefix=='RUL-':
   for name in ['QAM_PLAYBOOK','RRM_PLAYBOOK','DEPLOYMENT_PLAYBOOK']:
    text=(O/'03_BUILD_METHODOLOGY'/(name+'.md')).read_text()
    if id in text:docs=sorted(set(docs+['03_BUILD_METHODOLOGY/'+name+'.md']))
  assert docs,id
  rows.append(dict(id=id,selection='SELECTED within attributed scope; unrelated alternatives and exclusions unchanged',edit_ids=['E'+str(e['sequence']) for e in direct],documents=docs,authority=workflow[id].get('authority','') if id in workflow else 'DIRECTOR_RULINGS_2026-10-16.md' if n>=8 else 'INTAKE_SNAPSHOT/factory-intake/PLANNING_001/DIRECTOR_RULINGS_2026-10-14.md'))
ledger=(H/'SELECTED_SCOPE_LEDGER.md').read_text()
# Enrich existing FC evidence with newly appended corrections, without rewriting disposition fields.
for id in re.findall(r'^\| (FC-\d{3}) \|',ledger,re.M):
 extra=['E'+str(e['sequence']) for e in ed if e['sequence']>334 and id in e['ids']]
 if extra:
  pattern=re.compile(r'(^\| '+id+r' \|[^\n]*?\|[^\n]*?\|)([^|]*)(\|[^\n]*$)',re.M)
  ledger=pattern.sub(lambda m:m[1]+m[2].rstrip()+', '+', '.join(extra)+' '+m[3],ledger,count=1)
ledger+='\n## Workflow and ruling coverage — MC-12\n\nAll rows below preserve bounded attribution; a cited history row is provenance, not approval of an unrelated policy alternative. This supplements the 97 certified FC rows.\n\n| ID | Selection | Exact edits / proposed records | Document consumers | Authority |\n|---|---|---|---|---|\n'
for e in rows:ledger+='| '+e['id']+' | '+e['selection']+' | '+(', '.join(e['edit_ids']) or 'Full new-document proposal / metadata history row')+' | '+', '.join(e['documents'])+' | '+e['authority']+' |\n'
ledger+='| AD-01 | SELECTED accepted template placement; installation still pending | PHASE_2_TEMPLATE_TRANSLATIONS.json; 25 exact source/translation hashes | 03_BUILD_METHODOLOGY/_templates/QAM/; QAM_PLAYBOOK | Architect decision under Director delegation; accepted source unchanged |\n'
(R/'SELECTED_SCOPE_LEDGER.md').write_text(ledger);(R/'WORKFLOW_RULING_TRACEABILITY.json').write_text(json.dumps(rows,indent=2)+'\n')
(R/'SYNC_HANDOFF_DISPOSITIONS.template.md').write_text('# TEMPLATE — identical selected disposition sets for future handoff\n\nCopy this approved set at the actual engineering handoff; it supplies no QA verdict. Fable/QA independently derives and grades the candidate.\n\n'+ledger)
# MC-14: retain obsolete plans explicitly as historical, with one current expected-hash authority.
for name in ['TEMPLATE_INSTALL_PLAN.md','TEMPLATE_INSTALL_PLAN.json']:
 if not (H/name).exists():shutil.copyfile(R/name,H/name)
p=R/'TEMPLATE_INSTALL_PLAN.md';s=(H/p.name).read_text();p.write_text('> **HISTORICAL — SUPERSEDED.** This old proposal is retained as review history. Its destination hashes are NOT current expectations. Use PHASE_2_TEMPLATE_TRANSLATIONS.json for the pre-verification proposal and POST_VERIFICATION_STATUS_TRANSITIONS.json for the bounded later README transition. Required checks are preserved in TEMPLATE_INSTALL_CHECKS.md.\n\n'+s.replace('Destination SHA-256','Historical destination SHA-256'))
p=R/'TEMPLATE_INSTALL_PLAN.json';old=json.loads((H/p.name).read_text())
for e in old:e['status']='HISTORICAL — SUPERSEDED; hashes are not current QA expectations';e['superseded_by']='PHASE_2_TEMPLATE_TRANSLATIONS.json plus declared post-verification README transition'
p.write_text(json.dumps(old,indent=2)+'\n')
s=(H/'TEMPLATE_INSTALL_PLAN.md').read_text();start=s.index('## Required installation checks');s=s[start:]
(R/'TEMPLATE_INSTALL_CHECKS.md').write_text('# Current installation checks — preserved requirements\n\nAccepted source behavior is settled. These checks verify actual installation; they are not a repeated template acceptance review. Current hash authority: PHASE_2_TEMPLATE_TRANSLATIONS.json; later exact README change: POST_VERIFICATION_STATUS_TRANSITIONS.json.\n\n'+s)
print('12 conditional closeout edits /9 paths; required evidence explicitly PENDING; date binding',len(dates),'spans; W23/RUL15/AD01 coverage; obsolete template plan marked HISTORICAL.')
