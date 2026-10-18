from pathlib import Path
import json,hashlib,posixpath,re
R=Path('_AUDIT/SYNC_2026-10-15_doctrine-part2');src=Path('factory-intake/INTAKE_ADDENDUM_001_v0_3/TEMPLATES/QAM');dest=Path('03_BUILD_METHODOLOGY/_templates/QAM');rows=[]
old='DRAFT v0.3 — QA LEAD ACCEPTED WITH EXACT AMENDMENTS (Fable, 2026-10-14); AMENDMENTS APPLIED AND ENGINEER-VERIFIED; ARCHITECT AMENDMENT VERIFICATION PENDING.'
new='TEMPLATE SET v0.3 — QA LEAD ACCEPTED WITH EXACT AMENDMENTS (Fable, 2026-10-14); AMENDMENTS ARCHITECT-VERIFIED; INSTALLED BY THE APPROVED DOCSET SYNC.'
for p in sorted(src.rglob('*')):
 if not p.is_file():continue
 rel=p.relative_to(src);s=p.read_text();n=s;changes=[]
 def change(a,b):
  global n
  if a in n:changes.append({'old':a,'new':b,'occurrences':n.count(a),'label':'ENGINEER-PROPOSED mechanics only'});n=n.replace(a,b)
 change(old,new)
 change('Not canonical; not installed; staging only.','Installed reusable template; instantiate and resolve module-specific fields before launch.')
 if rel==Path('README.md'):
  change('# TEMPLATES/QAM/ — reusable QA Module template set (draft)','# QAM — reusable QA Module template set')
  oldline=n.splitlines()[3]
  newl='> Template set **v0.3**. Governing playbook: **QAM_PLAYBOOK v1.0**. QA behavior was accepted by Fable on 2026-10-14 with three exact amendments; Jarvis verified their application. Source set v0.3-draft is preserved byte-for-byte in this run’s intake snapshot. This installed set differs only by the approved status/provenance translations enumerated in `TEMPLATE_INSTALL_PLAN.json`; it is newly authored from the approved playbook, not the pilot’s missing original templates. Source playbook SHA-256: `97e111e2a495f9a3fe65f50213e6f2ba68c8e5e963f3d23493b1ee99ad35c897`.'
  change(oldline,newl)
  change('**Not installed yet**: this copy is intake staging until the DocSet Sync run lands it.','**Installation provenance:** see the sync run’s template-install plan and retained acceptance records; source acceptance alone is not installation verification.')
  # Add exact links to snapshot authority beside provenance; no extra file is installed.
  anchor='## 1. What this set is'
  links='Acceptance and provenance: [QA Lead decision](../../../_AUDIT/SYNC_2026-10-15_doctrine-part2/INTAKE_SNAPSHOT/factory-intake/INTAKE_ADDENDUM_001_v0_3/QA_LEAD_DECISION_2026-10-14.md), [Architect verification](../../../_AUDIT/SYNC_2026-10-15_doctrine-part2/INTAKE_SNAPSHOT/factory-intake/INTAKE_ADDENDUM_001_v0_3/ARCHITECT_VERIFICATION_2026-10-14.md), [installation translations](../../../_AUDIT/SYNC_2026-10-15_doctrine-part2/TEMPLATE_INSTALL_PLAN.json).'
  change(anchor,links+'\n\n'+anchor)
 # Provenance source filename is intentionally retained; it identifies the immutable input, not a live Hub link.
 rows.append({'source':str(p),'destination':str(dest/rel),'source_sha256':hashlib.sha256(s.encode()).hexdigest(),'proposed_destination_sha256':hashlib.sha256(n.encode()).hexdigest(),'translations':changes})
assert len(rows)==25
(R/'TEMPLATE_INSTALL_PLAN.json').write_text(json.dumps(rows,indent=2)+'\n')
md=['# QAM template installation proposal\n\nDRAFT — source acceptance is settled; installation is pending. No destination file exists yet. AD-01 fixes the destination. Only the exact status/provenance translations below are proposed; no QA behavior changes, placeholder values, approvals, results or credentials are introduced. The immutable source snapshot must accompany the run. Accepted source version remains v0.3-draft; installed set is proposed as v0.3, governed by QAM_PLAYBOOK v1.0.\n\n| Source relative path | Destination | Source SHA-256 | Expected installed SHA-256 after approved translations |\n|---|---|---|---|']
for row in rows:md.append('| '+str(Path(row['source']).relative_to(src))+' | `'+row['destination']+'` | '+row['source_sha256']+' | '+row['proposed_destination_sha256']+' |')
md+=['\n## Exact translation authority\n\n`TEMPLATE_INSTALL_PLAN.json` enumerates every old/new span and expected count per file. Recompute destination hashes after installation; never claim byte identity to the source after relabeling. Internal module-relative placeholders are not Hub links and remain unchanged. The provenance source filename identifies the preserved input.\n\n## Required installation checks (Engineer then independent QA)\n\n1. Exact 25-file destination set and source manifest membership; no missing or extra files.\n2. Each source SHA matches the accepted package; each installed SHA matches the approved transformed bytes.\n3. CLAUDE.md and AGENTS.md routing bodies remain byte-identical and assign QA Executor; parent routing still separates Engineering from QA.\n4. AM-1 exact cleanup column, AM-2 exact STOP cell, AM-3 command/cwd/exit/unfiltered output, and all eleven adopted SR rows remain unchanged.\n5. Nineteen-state vocabulary matches dispatch rows; READY FOR ENGINEERING is initial; REPAIR RULED — AWAITING COMMIT remains a waiting state distinct from RELEASED FOR Q4. Unknown state routes to discrepancy and next owner.\n6. Owner/writable-lane/permission tables agree. No populated result, approval, certificate, candidate SHA, credential or production target. Source provenance hash is not a candidate SHA.\n7. Parent-contract references, local governing source provenance and snapshot links resolve after the snapshot is committed.\n8. Enumerate template checks explicitly in the independent acceptance spec: current lints do not recurse here. No template exporter, validator, runtime dispatcher or browser adapter is delivered by this installation.\n\nThese are proposed installation verifications, not a fresh acceptance review of Fable’s already accepted QA behavior.\n']
(R/'TEMPLATE_INSTALL_PLAN.md').write_text('\n'.join(md));print('25 template destinations and exact mechanical translations saved; nothing installed.')
