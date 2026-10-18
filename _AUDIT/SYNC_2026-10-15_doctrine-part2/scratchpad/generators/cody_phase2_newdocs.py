from pathlib import Path
import json,hashlib,subprocess
r=Path('_AUDIT/SYNC_2026-10-15_doctrine-part2');dest=r/'PROPOSED_CONTENT';ed=json.loads((r/'PROPOSED_EXACT_EDITS.json').read_text());index=[]
for name in ['QAM_PLAYBOOK.md','RRM_PLAYBOOK.md','DEPLOYMENT_PLAYBOOK.md']:
 p=r/'DRAFTS'/name;s=p.read_text()
 for e in ed:
  if e['path']==str(p):assert s.count(e['old'])==1;s=s.replace(e['old'],e['new'])
 # Scoped rulings now answer those old draft-policy placeholders. Exact content still awaits map review.
 s=s.replace('PROPOSED — reviewer-guidance placement and adoption remain open under RRM-09 / DEC-19. If approved, independent review that feeds an RRM follows these rules; the pilot source is preserved unchanged.','Reviewer guidance belongs here under RUL-14 (2026-10-16). The following proposed wording expresses that guidance for map review; pilot source records remain unchanged.')
 s=s.replace('PROPOSED — ND-07 remains open. This section is not an adopted default or an approved optional policy until the Director rules.','Under RUL-15 (2026-10-16), execute continuously within a released assignment, including routine checks, reporting and packaging. Stop for concrete blockers, authority changes or required independent verdicts. This is not permission to cross a release boundary.')
 s=s.replace('**Status:** Active','**Status:** DRAFT FOR EXECUTABLE-MAP REVIEW — NOT INSTALLED')
 s=s.replace('preserved as received in this run\'s intake snapshot','preserved as received in INTAKE_SNAPSHOT/factory-intake/')
 s=s.replace('the Factory documents this playbook pairs with were reconciled in the same DocSet Sync run','the paired Factory documents must be reconciled and verified in this sync before a completion claim')
 s=s.replace('the Factory documents this playbook pairs with were reconciled with this rule when it landed','the paired Factory documents must be reconciled with this rule before landing')
 s=s.replace('Template set installed beside it.','Template set installation is proposed; verify the installed translations separately before recording completion.')
 s=s.replace('landed verbatim with integration substitutions','proposed with integration substitutions')
 s=s.replace('Older lifecycle diagrams, folder trees, role tables, prompts and handoff templates in the Factory DocSet were reconciled with this rule by the DocSet Sync run that landed this playbook (see Version History).','Older lifecycle diagrams, folder trees, role tables, prompts and handoff templates must be reconciled with this rule and verified before the sync reports completion.')
 if name=='DEPLOYMENT_PLAYBOOK.md':
  import re
  s=re.sub(r'CONDITIONAL — lands only if the Director rules the C\.2 remainder.*?: \*(.*?)\*',r'RUL-10 (2026-10-16) approves the common requirements below, without granting new deployment authority: \1',s)
  s=re.sub(r'CONDITIONAL —.*?DEC-17.*?: \*(.*?)\*',r'RUL-14 (2026-10-16) approves snapshot identity and intentional pins: \1',s)
  start=s.index('CONDITIONAL[DEC-17]');end=s.index('\n\n',start)
  s=s[:start]+'RUL-14 (2026-10-16): identify governing snapshots by canonical document name, header version and Hub commit. Preserve an intentional approved project pin until an attributable update. Declare the actual project location; no universal landing path or release tag is required. Route genuine conflicts to the Director with both identities recorded.'+s[end:]
  s=s.replace('FFM staging permission, DevOps assignment and the complete cloud-action matrix remain OPEN under DEC-18','Existing context-specific permissions, including any recorded FFM staging permission, remain intact; missing DevOps assignments and platform procedures remain OPEN under DEC-18')
  s=s.replace('Per `_SKILLS/factory-docs-update/CLAUDE.md` D5 — a bounded, Hub-only exception that does not extend to any project repository','Director-only Git mutations for this sync (RUL-15); read-only Git inspection is allowed. Historical Hub exceptions do not override this assignment')
  s=s.replace('May the Engineer deploy to staging?','Retain the recorded FFM staging permission; verify its bounds before any action')
  s=s.replace('Distribution and pinning (§6, DEC-17 as ruled at Gate 2)','Distribution and pinning (§6, RUL-14)')
  s=s.replace('Engineer (git-zero / cloud-zero)','Engineer (read-only Git inspection allowed; Git mutations Director-only; existing context-specific cloud permissions retained)')
 s=s.replace('Engineer git-zero / cloud-zero','Engineer read-only Git inspection, Director-only Git mutations, and existing context-specific cloud restrictions')
 if name=='RRM_PLAYBOOK.md':
  s=s.replace('The Engineer runs zero Git and zero cloud commands (`BIM_PLAYBOOK.md` §7); the Director performs every mutating Git and cloud operation.','The Engineer may inspect Git read-only; the Director performs every Git mutation. Existing context-specific cloud restrictions remain in force; this document grants no new cloud permission.')
  s=s.replace('## 12. The Prepared, Uninterrupted Engineering Run (optional shape)','## 12. Continuous Execution Within a Released Assignment')
  start=s.index('A prepared run —');end=s.index('\n\n',start)
  s=s[:start]+'Prepare measurable scope, prerequisites, writable lanes and enumerated stops before release. Once released, include routine checks, reporting and packaging in continuous execution. Preserve required independent verdicts and authority boundaries. Report the full lifecycle effort, interruptions, repairs and missing-package follow-ups; never omit a valid stop to claim uninterrupted success.'+s[end:]
  s=s.replace('§12 optional prepared-run shape','§12 continuous execution within released scope (RUL-15)')
 d=dest/'03_BUILD_METHODOLOGY'/name;d.parent.mkdir(parents=True,exist_ok=True);d.write_text(s)
 index.append({'path':str(d.relative_to(dest)),'source':str(p),'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'proposed_sha256':hashlib.sha256(s.encode()).hexdigest(),'label':'ENGINEER-PROPOSED new document; draft status, no installation claim'})
# Accepted sources never change. Translation proposals drop premature completed-installation claim.
plan=json.loads((r/'TEMPLATE_INSTALL_PLAN.json').read_text())
for e in plan:
 s=Path(e['source']).read_text()
 for t in e['translations']:
  assert s.count(t['old'])==t['occurrences']
  t['new']=t['new'].replace('TEMPLATE_INSTALL_PLAN.json','PHASE_2_TEMPLATE_TRANSLATIONS.json')
  t['new']=t['new'].replace('INSTALLED BY THE APPROVED DOCSET SYNC','INSTALLATION REQUIRES THE APPROVED DOCSET SYNC')
  s=s.replace(t['old'],t['new'])
 if e['source'].endswith('/QAM/README.md'):
  old='This installed set differs only by the approved status/provenance translations enumerated in `PHASE_2_TEMPLATE_TRANSLATIONS.json`;'
  new='This proposed set differs only by the status/provenance translations enumerated in this run’s `PHASE_2_TEMPLATE_TRANSLATIONS.json`; installation and translation approval remain pending;'
  assert old in s
  s=s.replace(old,new)
  e['translations'].append({'old':old,'new':new,'occurrences':1,'label':'ENGINEER-PROPOSED status correction after prior translations'})
 d=dest/e['destination'];d.parent.mkdir(parents=True,exist_ok=True);d.write_text(s)
 e['proposed_destination_sha256']=hashlib.sha256(s.encode()).hexdigest()
 e['status']='PROPOSED TRANSLATION; not installed; source acceptance unchanged'
(r/'PHASE_2_TEMPLATE_TRANSLATIONS.json').write_text(json.dumps(plan,indent=2)+'\n')
(r/'NEW_DOCUMENT_PROPOSALS.json').write_text(json.dumps(index,indent=2)+'\n')
archive=dest/'_ARCHIVE/QA_PLAYBOOK_v1_0.md';archive.parent.mkdir(parents=True,exist_ok=True)
b=subprocess.check_output(['git','show','9ad3f3f:03_BUILD_METHODOLOGY/QA_PLAYBOOK.md']);archive.write_bytes(b)
assert subprocess.check_output(['git','hash-object','--stdin'],input=b).decode().strip()=='bb41260f6b6f94372a682f04b313a451f2b3c4b1'
(r/'ARCHIVE_RESTORATION_PROPOSAL.json').write_text(json.dumps({'ruling':'RUL-14','source':'9ad3f3f:03_BUILD_METHODOLOGY/QA_PLAYBOOK.md','git_blob':'bb41260f6b6f94372a682f04b313a451f2b3c4b1','destination':'_ARCHIVE/QA_PLAYBOOK_v1_0.md','sha256':hashlib.sha256(b).hexdigest(),'status':'exact proposed bytes; history only; canonical archive not written'},indent=2)+'\n')
print('Proposed new playbooks 3; accepted-template translations 25; exact historical archive 1; canonical destinations untouched.')
