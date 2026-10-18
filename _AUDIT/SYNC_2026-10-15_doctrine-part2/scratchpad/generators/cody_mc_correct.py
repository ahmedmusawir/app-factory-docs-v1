from pathlib import Path
import json,re,hashlib,difflib,subprocess,shutil,datetime,html,textwrap,zipfile
from markdown_it import MarkdownIt
R=Path('_AUDIT/SYNC_2026-10-15_doctrine-part2');O=R/'PROPOSED_CONTENT';H=R/'PLANNING_HISTORY/PRE_MC_CORRECTION_2026-10-16';md=MarkdownIt('commonmark').enable('table');date='2026-10-16'
base={str(p.relative_to(R/'BASELINE_CONTENT')):p.read_text() for p in sorted((R/'BASELINE_CONTENT').glob('0*_*/*.md'))};files=base.copy();ed=json.loads((H/'SELECTED_EXACT_EDITS.json').read_text())
for e in ed:
 assert files[e['path']].count(e['old'])==1,e['sequence'];files[e['path']]=files[e['path']].replace(e['old'],e['new'])
newdocs={str(Path('03_BUILD_METHODOLOGY')/(n+'.md')):(H/'NEW_PLAYBOOKS'/(n+'.md')).read_text() for n in ['QAM_PLAYBOOK','RRM_PLAYBOOK','DEPLOYMENT_PLAYBOOK']}
def change(path,old,new,ids):
 assert old!=new and files[path].count(old)==1,(path,ids,old[:90]);files[path]=files[path].replace(old,new)
 ed.append(dict(sequence=len(ed)+1,path=path,old=old,new=new,ids=ids,label='ENGINEER-PROPOSED MC correction'))
def ndchange(path,old,new):
 assert newdocs[path].count(old)==1,(path,old[:80]);newdocs[path]=newdocs[path].replace(old,new)
def section(path,heading,new,ids):
 s=files[path];tokens=md.parse(s);target=next(t for i,t in enumerate(tokens) if t.type=='heading_open' and tokens[i+1].content==heading)
 lvl=int(target.tag[1:]);lines=s.splitlines(True);start=target.map[0];end=len(lines)
 for t in tokens:
  if t.type=='heading_open' and t.map[0]>start and int(t.tag[1:])<=lvl:end=t.map[0];break
 old=''.join(lines[start:end]);change(path,old,'#'*lvl+' '+heading+'\n\n'+new.strip()+'\n\n',ids)
B='01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md';S='01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md';F='03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md';BI='03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md';E='02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md';RE='02_PIPELINE_AGENTS/RECON_QUESTIONNAIRE.md';RR='03_BUILD_METHODOLOGY/RRM_PLAYBOOK.md'
# MC-01: replace the exact malformed lines, keeping table/quote/list containers intact.
label='Historical external example (availability unverified): '
prefix='**Historical external example pointer — availability unverified:** '
for path in files:
 for line in list(files[path].splitlines()):
  if not line.startswith(prefix):continue
  rest=line[len(prefix):]
  if path==F and 'Two real FFMs' in rest:
   new='This playbook describes two historical FFM examples below. Availability is unverified: obtain the source repository, immutable revision and path before use; do not assume either example is present locally.'
  elif rest.startswith('|'):
   last=rest.rfind('|');row=rest[:last+1];tail=rest[last+1:].strip();cells=row.split('|');assert len(cells)==4
   cells[2]=' '+label+cells[2].strip()+'. '+tail+' ';new='|'.join(cells)
  elif rest.startswith('> '):new='> '+label+rest[2:]
  elif rest.startswith('- '):new='- '+label+rest[2:]
  else:new=label+rest
  change(path,line,new,['MC-01','FC-009'])
# MC-02/13: close the report-template fence before the actual history table.
old='- <every handbook claim that proved FALSE against the filesystem>\n\n---\n\n## Version History'
new='- <every handbook claim that proved FALSE against the filesystem>\n```\n\n---\n\n## Version History'
change(RE,old,new,['MC-02','MC-13'])
old='| 0.5 | 2026-07-07 |'
start=files[RE].index(old);end=files[RE].index('\n```',start)
change(RE,files[RE][start:end+4],files[RE][start:end],['MC-02','MC-13'])
# MC-04: restore the documented lifecycle axes, including deployment/Gate D.
flow='''```text
Phase 0 — Recon: Engineer inspects facts and records the current target state.
Phase 1 — Ignition: Architect authors APP_BRIEF and DATA_CONTRACT before Design; Director approves scope.
Phase 2 — Design: Designer authors UI_SPEC and the visual package; Architect reconciles assembly.
Phase 3 — Engineering (spec): Architect completes the module, ACCEPTANCE_SPEC and prepared QAM; FILE_TREE optional.
Phase 4 — Fabrication (build): Director releases Engineering; Engineer builds and completes factual handoff.
  Director commits/pushes the completed numbered product candidate; QA branch starts at that exact commit.
  QA Executor Q1 recon and plan → QA Lead approval → Director release → QA Executor Q2.
  Conditional authorized Engineer repair and independent retest remain on the continuing QA branch.
  QA Lead product verdict → required cleanup and QA Lead cleanup acceptance → Architect closeout.
  Engineer bounded closeout → Director final commits, merge and push; retain candidate and evidence identities.
  Review checkpoint 1: after FFM build and its independent QA finish; disposition findings; RRM only for approved repairs.
  Complete remaining Engine 1 phases/modules and their QA; include Gate D before closing deployment-requiring work.
Phase 5 — Deployment: authorized operator deploys only within existing context-specific permissions.
  QA independently verifies the deployed revision at Gate D; production confirmation/recovery as applicable.
  Review checkpoint 2: Engine 2 after all Engine 1 phases/modules and their QA are closed.
  Disposition findings; RRM only for approved repairs; a clean review requires no RRM.
  Review, Gate Q, cleanup acceptance, Gate D and Director release remain separate decisions.
```

Engine and review vocabulary: `SOFTWARE_FACTORY_PLAYBOOK.md` §2, “Phase Vocabulary — One Canonical Map”. Deployment requirements: `DEPLOYMENT_PLAYBOOK.md`; Gate D: `QA_PLAYBOOK.md` §13.'''
# Both diagram blocks are replaced; neither is allowed to omit deployment.
for title in ['THE BIG PICTURE','🔄 THE FULL WORKFLOW','THE FULL WORKFLOW']:
 if re.search(r'^## '+re.escape(title)+r'$',files[B],re.M):section(B,title,flow,['MC-04','MC-06','RUL-05','RUL-09','RUL-10'])
change(B,'### Phase 3: ENGINEER (Data & Code)','### Phase 3: ENGINEERING (Architect Contract Assembly)',['MC-07','RUL-09'])
change(B,'- **Consumer:** the Architect reads the Recon Report BEFORE authoring the brief. Where any doc and reality disagree, **reality wins**.','- **Consumer:** the Architect reads the Recon Report before authoring the brief. Disk establishes implementation facts; approved briefs govern scope and governing documents control their subjects. Route genuine conflicts to the Director.',['MC-04','RUL-12'])
change(RE,'**Stage 0 of the FFM four-role pattern**','**Stage 0 of FFM module preparation**',['MC-04','FC-007'])
# MC-05: glossary table contains both axes and explicit checkpoint rows.
anchor='| Phase 9 — Deployment | Phase 5 — Deployment |'
rows='''| Engine 1 | Module engineering and independent module QA, including required certification/cleanup/closeout; complete every scoped phase/module and its QA before Engine 2. |
| Post-FFM review (checkpoint 1) | Independent review after FFM build and its independent QA finish; findings require disposition. |
| Engine 2 (checkpoint 2) | Independent system review after all Engine 1 phases/modules and their QA are closed. |
| RRM | Repair work only for approved review findings requiring repair; a clean review requires no RRM. Review does not replace Gate Q, Gate D or Director release. |'''
change(S,anchor,anchor+'\n'+rows,['MC-05','MC-06','W23','RUL-05','RUL-14'])
# MC-07: replace the contradictory ownership sentence and both whole-folder freeze formulations.
change(E,'This is the output the Engineer produces alongside working code.','The Architect prepares this contract before Design. Engineering implements the approved contract and records factual changes only through its authorized amendment and handoff lanes.',['MC-07','RUL-09'])
life='''```text
Current recon → Architect authors the module just in time, including ACCEPTANCE_SPEC and prepared QAM.
Director approves scope and the Engineer plan → Engineer builds and runs baseline/regression checks.
Requirements and acceptance criteria freeze; declared records/evidence lanes remain writable (RUL-04).
Engineer completes factual handoff → Director commits/pushes the numbered product candidate.
Director creates qa/<module-branch> at that exact engineering candidate commit.
QA Executor Q1: preflight, independent recon and test plan → QA Lead plan approval → Director release.
QA Executor Q2 executes independently on that QA branch.
If needed: QA Lead dispositions → Architect/Director authorize repair → Engineer repairs on the same QA branch.
Director commits repair candidate → QA Executor re-pins and independently retests with regression checks.
QA Lead certifies the product verdict → authorized required cleanup → QA Lead cleanup acceptance.
Architect closeout instructions → bounded Engineer closeout → Director final commits, merge and push.
Authorized deployment, if in scope → independent deployed-revision Gate D → production confirmation as applicable.
No deployment in scope → record Gate D N/A with reason; no deployment merely to satisfy a template.
Module close/retrospective: deployment-requiring work closes only after its required Gate D.
Engine 1 continues through all scoped phases/modules and their QA; author later BIMs just in time.
Review checkpoint 2: Engine 2 independent system review only after all Engine 1 phases/modules and QA are closed.
Findings require disposition; create RRM only for approved findings requiring repairs; clean review requires no RRM.
```

The distinct post-FFM checkpoint is review after FFM build and its independent QA finish. Both review checkpoints follow `RRM_PLAYBOOK.md` §2 and the vocabulary in `SOFTWARE_FACTORY_PLAYBOOK.md` §2. Review completion, module QA, cleanup acceptance, Gate D and release remain distinct.'''
# Replace only the lifecycle block; retain the locked rules that follow.
s=files[BI];start=s.index('```',s.index('## 6. Lifecycle'));end=s.index('```',start+3)+3
change(BI,s[start:end],life,['MC-06','MC-07','W07','W23','RUL-02','RUL-03','RUL-04','RUL-05'])
change(BI,'- QA reviews closed or gate-green modules only — the freeze doctrine applies to attackers too.','- QA independently tests the declared engineering candidate after handoff. Requirements and acceptance criteria remain frozen; QA recon, plans, evidence, findings and rulings remain writable in their declared lanes. QA cannot amend acceptance by changing a test plan.',['MC-07','RUL-04'])
change(BI,'After the stamp: frozen; changes require a versioned re-open with Coordinator sign-off, executed only at a gate.','After the stamp, requirements and acceptance criteria are frozen; changes require an attributable approved amendment. Declared engineering handoff and QA evidence lanes remain writable by their assigned owners.',['MC-07','RUL-04'])
# MC-06: actual FFM flow and checklist, not merely an adjacent paragraph.
old='→ Architect closeout; bounded Engineering closeout; Director final Git actions'
new=old+'\n→ Review checkpoint 1: after FFM build and its independent QA finish.\n→ Disposition findings; RRM only for approved findings requiring repairs; a clean review requires no RRM.\n→ Continue Engine 1 phases/modules and QA; Engine 2 review only after all are closed.\n→ Review, module QA, cleanup acceptance, Gate D and Director release retain separate responsibilities.'
change(F,old,new,['MC-06','W23','RUL-05'])
anchor='## 3. FFM Anatomy — The Folder Structure'
change(F,anchor,'Review checkpoints and repair routing: `RRM_PLAYBOOK.md` §2; Engine vocabulary: `SOFTWARE_FACTORY_PLAYBOOK.md` §2. The FFM completion checklist must retain the post-FFM review and any approved RRM follow-up before downstream progression.\n\n'+anchor,['MC-06','RUL-05'])
# Canonical workflow publication companions and their exact sources.
workflows={
'FFM_CREATION':dict(title='FFM creation and Architect assembly',source='SRC-W01_FFM_CREATION.png',owner='FFM_PLAYBOOK.md',steps=[('Engineer','Current recon; declared reporting writes'),('Architect','Author APP_BRIEF from current recon'),('Director','Approve scope and brief'),('Architect','DATA_CONTRACT before Design'),('Designer','UI_SPEC, tokens and visual artifacts'),('Architect','Reconcile assembly; prepare module QAM'),('Director','Approve package and release Engineering')]),
'FFM_EXECUTION':dict(title='FFM engineering, independent QA and post-FFM review',source='SRC-W02_FFM_EXECUTION.png',owner='FFM_PLAYBOOK.md',steps=[('Engineer','Build and self-check; factual QAM handoff'),('Director','Commit/push numbered engineering candidate'),('Director','QA branch at exact candidate commit'),('QA Executor','Q1 recon and independent test plan'),('QA Lead','Approve the specific QA plan'),('Director','Release Q2 execution'),('QA Executor','Q2 tests and evidence'),('Engineer','Conditional authorized repair on same QA branch'),('Director','Commit repaired candidate on the continuing QA branch'),('QA Executor','Independent retest of repair and regression'),('QA Lead','Product certification; approve cleanup retention'),('QA Executor','Authorized cleanup; retain durable evidence'),('QA Lead','Accept cleanup; preserve product verdict identity'),('Architect','Closeout instruction'),('Engineer','Bounded closeout'),('Director','Final commits, merge and push'),('Reviewers','Review checkpoint 1 after FFM build and independent QA'),('Director','Disposition review findings; RRM only for approved repairs')]),
'FFM_DEPLOYMENT':dict(title='Deployment, identity and independent Gate D',source='SRC-W03_FFM_DEPLOYMENT.png',owner='DEPLOYMENT_PLAYBOOK.md',steps=[('Architect','Declare target, permissions, exclusion and recovery'),('QA Lead','Required product QA verdict remains distinct'),('Director','Release the verified candidate for deployment'),('Authorized operator','Deploy within existing context-specific permissions'),('QA Executor','Verify deployed identity, exclusions and behavior at Gate D'),('QA Lead','Issue deployed-environment verdict'),('Director','Release decision or authorized recovery'),('Architect','Record follow-ups; release is separate from review')]),
'BIM_WORKFLOW':dict(title='BIM lifecycle and Engine 2 system review',source='SRC-W04_BIM_WORKFLOW.png',owner='BIM_PLAYBOOK.md',steps=[('Engineer','Fresh recon after preceding module closeout'),('Architect','Author BIM just in time; prepare contract and QAM'),('Director','Approve scope and release Engineering'),('Engineer','Implement, verify and complete factual handoff'),('Director','Commit/push candidate; QA branch at that exact commit'),('QA Executor','Q1 recon and independent plan'),('QA Lead','Approve plan'),('Director','Release Q2'),('QA Executor','Q2 tests and findings'),('Engineer','Conditional authorized repairs on continuing QA branch'),('Director','Commit repaired candidate on the continuing QA branch'),('QA Executor','Independent retest of repairs and required regression'),('QA Lead','Product certification; approve cleanup retention'),('QA Executor','Perform authorized required cleanup; retain evidence'),('QA Lead','Accept cleanup separately from product verdict'),('Architect','Closeout instructions'),('Engineer','Bounded closeout'),('Director','Final commits, merge and push'),('Authorized operator','If deployment in scope: deploy within existing permissions'),('QA Executor','If deployed: independently verify the exact revision at Gate D'),('QA Lead','If deployed: Gate D verdict; otherwise documented N/A'),('Architect','Complete all Engine 1 phases/modules and their QA'),('Reviewers','Review checkpoint 2: Engine 2 independent system review'),('Director','Disposition findings; RRM only for approved repairs')])}
# One data source produces both textual flows and the stick-actor SVGs.
assets={};workflow_docs={}
for name,w in workflows.items():
 rel=Path('03_BUILD_METHODOLOGY/_workflows')/(name+'.md');svg=Path('03_BUILD_METHODOLOGY/_assets/workflows')/(name+'.svg')
 source='../../'+str(R/'INTAKE_SNAPSHOT/factory-intake/SOURCES/Workflow'/w['source'])
 # Relative links resolved from the nested workflow directory (two parents -> repo root).
 title=w['title'];sem=['Review checkpoint 1: after FFM build and its independent QA finish.','Review checkpoint 2: Engine 2 independent system review after all Engine 1 phases/modules and their QA are closed.','At either checkpoint, disposition findings; RRM only for approved findings requiring repairs. A clean review requires no RRM.','Review, Gate Q, required cleanup and certification, Gate D and Director release remain separate responsibilities.']
 body=f'''# {title}

> **Version:** 1.0 · **Date:** {date} · **Status:** Proposed — pending verified publication
> **Governed by:** `{w['owner']}`, `SOFTWARE_FACTORY_PLAYBOOK.md` §2, `RRM_PLAYBOOK.md` §2, `QAM_PLAYBOOK.md`, `DEPLOYMENT_PLAYBOOK.md`.

This revised workflow supersedes the August diagram `{w['source']}` for current instructions when this proposed sync is approved, landed and verified. The [unaltered original]({source}) remains historical evidence; it grants no current role, Git or cloud permission. This derivative follows RUL-01…15 and Tony’s explicit workflow/diagram correction assignment of 2026-10-16.

![Revised stick-actor workflow](../_assets/workflows/{name}.svg)

## Sequence

'''+''.join(f'{i}. **{seat}:** {action}.\n' for i,(seat,action) in enumerate(w['steps'],1))+'''\n## Review and release checkpoints

'''+''.join('- '+s+'\n' for s in sem)+'''
## Entry, handoff and evidence

Boot/resume through the module’s declared entry file: Engineering routes to its released implementation assignment; QA routes to `QAM/` as QA Executor. Read-only Git inspection and declared reporting writes are permitted; Tony performs all Git mutations. Requirements/acceptance freeze while declared handoff and QA evidence lanes remain writable. Preserve actual candidate, test-plan, repair/retest, cleanup and closeout identities; never prefill a verdict or planned commit SHA. Deployment additionally requires verified exclusion from build inputs and the actual artifact; a folder name is insufficient. Existing modules in flight keep their recorded sequence unless explicitly amended.

## Version History

| Version | Date | Change | Authority |
|---|---|---|---|
| 1.0 | '''+date+''' | Revised workflow and stick diagram; original retained; review checkpoints and seat boundaries reconciled | MC-06; W01–W23; RUL-01–RUL-15; Tony 2026-10-16 correction assignment |
'''
 workflow_docs[str(rel)]=body
 seats=list(dict.fromkeys(s for s,a in w['steps']));width=1800;lane=width/len(seats);height=270+len(w['steps'])*110+180
 parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',f'<title id="title">{html.escape(title)}</title>','<desc id="desc">Revised stick-actor sequence; original August diagram preserved as history. Required reviews, QA verdicts and release remain distinct.</desc>','<defs><marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#334155"/></marker></defs>','<rect width="100%" height="100%" fill="#ffffff"/>',f'<text x="32" y="42" font-size="28" font-family="sans-serif" fill="#0f172a">{html.escape(title)}</text>','<text x="32" y="77" font-size="18" font-family="sans-serif" fill="#334155">v1.0 · revised workflow reference · RUL-01–15</text>']
 for j,seat in enumerate(seats):
  x=lane*(j+.5);parts += [f'<g stroke="#334155" stroke-width="3" fill="none"><circle cx="{x}" cy="116" r="13"/><path d="M{x} 129v39m-22-28h44m-22 28l-20 27m20-27l20 27"/></g>',f'<text x="{x}" y="221" text-anchor="middle" font-family="sans-serif" font-size="20" fill="#0f172a">{html.escape(seat)}</text>',f'<path d="M{x} 237V{height-180}" stroke="#cbd5e1" stroke-dasharray="7 7"/>']
 for i,(seat,action) in enumerate(w['steps']):
  y=270+i*110;x=lane*(seats.index(seat)+.5);boxw=min(380,lane-12);boxx=max(10,min(width-boxw-10,x-boxw/2));wrapped=textwrap.wrap(f'{i+1}. {action}',width=int(boxw/10))
  if i:
   prev=lane*(seats.index(w['steps'][i-1][0])+.5);parts.append(f'<path d="M{prev} {y-30}V{y-14}H{x}V{y}" stroke="#334155" fill="none" marker-end="url(#arrow)"/>')
  parts.append(f'<rect x="{boxx}" y="{y}" width="{boxw}" height="76" rx="8" fill="#eff6ff" stroke="#2563eb"/>')
  for k,line in enumerate(wrapped[:4]):parts.append(f'<text x="{boxx+10}" y="{y+20+k*16}" font-family="sans-serif" font-size="15" fill="#0f172a">{html.escape(line)}</text>')
 for j,line in enumerate(sem):parts.append(f'<text x="32" y="{height-140+j*29}" font-family="sans-serif" font-size="17" fill="#0f172a">{html.escape(line)}</text>')
 parts.append('</svg>');assets[str(svg)]='\n'.join(parts)+'\n'
workflow_ref='''Revised workflow references: [FFM creation](_workflows/FFM_CREATION.md), [FFM execution and post-FFM review](_workflows/FFM_EXECUTION.md), [deployment and Gate D](_workflows/FFM_DEPLOYMENT.md), and [BIM through Engine 2](_workflows/BIM_WORKFLOW.md). Each includes a revised stick diagram and links its superseded original as history. The source diagrams are not current instructions.'''
for path in [F,BI]:
 anchor='## 3.' if path==F else '## 7.';pos=files[path].index(anchor);change(path,files[path][pos:pos+len(anchor)],workflow_ref+'\n\n'+files[path][pos:pos+len(anchor)],['MC-06','RUL-05','RUL-07'])
# For high-level docs use correct relative paths, not an assumed project landing location.
ref='Revised workflow documents and stick diagrams: [FFM creation](../03_BUILD_METHODOLOGY/_workflows/FFM_CREATION.md), [FFM execution and post-FFM review](../03_BUILD_METHODOLOGY/_workflows/FFM_EXECUTION.md), [deployment](../03_BUILD_METHODOLOGY/_workflows/FFM_DEPLOYMENT.md), [BIM and Engine 2](../03_BUILD_METHODOLOGY/_workflows/BIM_WORKFLOW.md). They supersede the historical August pictures when verified and published; originals are retained.'
for path in [S,B]:
 anchor='## 1.5 ' if path==S else '## 🔀 WHICH PIPELINE AM I IN?';pos=files[path].index(anchor);change(path,files[path][pos:pos+len(anchor)],ref+'\n\n'+files[path][pos:pos+len(anchor)],['MC-06','RUL-05','RUL-07'])
# New playbooks get exact reference corrections, recorded in a separate full-file diff.
newdoc_mc=[]
for path in newdocs:
 before=newdocs[path]
 if path==RR:
  newdocs[path]=newdocs[path].replace('(Engine 1 = module build and module QA — FFM, BIM, FIX, FEAT and their QAM certification; Engine 2 = the independent system review that runs once after all Engine 1 phases and their QA are closed. Definitions: `SOFTWARE_FACTORY_PLAYBOOK.md` §2 "Phase Vocabulary — One Canonical Map".)','(Definitions and lifecycle vocabulary: `SOFTWARE_FACTORY_PLAYBOOK.md` §2, “Phase Vocabulary — One Canonical Map”.)')
  anchor='## 3. Inputs and Entry Conditions';newdocs[path]=newdocs[path].replace(anchor,workflow_ref+'\n\n'+anchor)
 if path.endswith('DEPLOYMENT_PLAYBOOK.md'):
  anchor='## 5. Release Identity';newdocs[path]=newdocs[path].replace(anchor,'Revised [deployment workflow and stick diagram](_workflows/FFM_DEPLOYMENT.md) supersede the original August deployment picture; platform-specific procedures and new permissions remain outside this run.\n\n'+anchor)
 if newdocs[path]!=before:newdoc_mc.append({'path':path,'before':before,'after':newdocs[path],'ids':['MC-05','MC-06','RUL-05','RUL-07']})
# Propagate explicit checkpoint wording through retained council flows and boot/checklist consumers.
reviewline='Review checkpoint 1: after FFM build and its independent QA finish. Review checkpoint 2: Engine 2 independent system review after all Engine 1 phases/modules and their QA are closed. At either checkpoint, disposition findings; RRM only for approved findings requiring repairs; a clean review requires no RRM. Review, Gate Q, cleanup acceptance, Gate D and release remain distinct.'
old='Reviews: after FFM + QA, and Engine 2 after all Engine 1 engineering and QA; RRM only for approved findings.'
for path in ['02_PIPELINE_AGENTS/ARCHITECT_PLAYBOOK.md','02_PIPELINE_AGENTS/DESIGNER_PLAYBOOK.md',E]:
 if old in files[path]:change(path,old,reviewline,['MC-06','RUL-05','W23'])
path='02_PIPELINE_AGENTS/DESIGNER_PLAYBOOK.md'
change(path,'| Define data schemas | Engineer Agent |','| Define DATA_CONTRACT before Design | Architect |',['MC-07','RUL-09'])
change(S,"| Design | Can't model data without knowing the UI needs |",'| Design | Consume the Architect’s approved DATA_CONTRACT; proposed contract refinements require approved amendments before implementation. |',['MC-07','RUL-09'])
change(F,'Continue within the released assignment; stop at its required boundaries.','Continue within the released assignment; stop at its required boundaries.\nRetain the post-FFM review after FFM build and independent QA finish.\nEngine 2 review waits until every Engine 1 phase/module and its QA are closed.\nRoute review findings for disposition; RRM only for approved repairs; a clean review requires no RRM.',['MC-06','RUL-05'])
anchor='- [ ] PHASE_ROADMAP is locked; this FFM is for phase N'
change(F,anchor,anchor+'\n- [ ] Schedule review after FFM build and independent QA finish; disposition findings and route only approved repairs to RRM.\n- [ ] Keep Engine 2 review after all Engine 1 phases/modules and their QA close; do not substitute review for QA or release.',['MC-06','RUL-05'])
old='**Review after FFM completion and its QA**, followed by approved RRM work.'
new='**Review after FFM build and its independent QA finish**; disposition findings and authorize RRM only when approved findings require repair.'
ndchange(RR,old,new)
# Store exact proposal content before metadata; original canonical files remain unchanged.
for path,body in files.items():(O/path).parent.mkdir(parents=True,exist_ok=True);(O/path).write_text(body)
for path,body in {**newdocs,**workflow_docs,**assets}.items():(O/path).parent.mkdir(parents=True,exist_ok=True);(O/path).write_text(body)
(R/'SELECTED_EXACT_EDITS.json').write_text(json.dumps(ed,indent=2)+'\n');(R/'MC_NEW_DOCUMENT_EDITS.json').write_text(json.dumps([{**e,'after':newdocs[e['path']]} for e in newdoc_mc],indent=2)+'\n')
(R/'WORKFLOW_PUBLICATION_PLAN.json').write_text(json.dumps({'authority':'Tony explicit 2026-10-16 MC correction assignment; revised derivatives required; originals preserved','status':'ENGINEER-PROPOSED published references and stick diagrams; not installed','workflows':[{**w,'id':name,'document':f'03_BUILD_METHODOLOGY/_workflows/{name}.md','asset':f'03_BUILD_METHODOLOGY/_assets/workflows/{name}.svg','source':str(R/'INTAKE_SNAPSHOT/factory-intake/SOURCES/Workflow'/w['source'])} for name,w in workflows.items()]},indent=2)+'\n')
# Rebuild content-only stage index; final hashes are emitted after metadata.
index=[];diff=[]
for path,new in files.items():
 if new==base[path]:continue
 index.append({'path':path,'base_sha256':hashlib.sha256(base[path].encode()).hexdigest(),'proposed_sha256':hashlib.sha256(new.encode()).hexdigest(),'status':'content-stage bytes; final EXECUTION_PROPOSAL_INDEX is authoritative'})
 diff.extend(difflib.unified_diff(base[path].splitlines(True),new.splitlines(True),fromfile='BASE/'+path,tofile='PROPOSED/'+path))
(R/'SELECTED_CONTENT_INDEX.json').write_text(json.dumps(index,indent=2)+'\n');(R/'SELECTED_CONTENT_DIFF.patch').write_text(''.join(diff))
print(len(ed),'ordered content edits;',len(index),'revised existing documents; 4 workflow references + 4 SVG stick diagrams proposed.')
