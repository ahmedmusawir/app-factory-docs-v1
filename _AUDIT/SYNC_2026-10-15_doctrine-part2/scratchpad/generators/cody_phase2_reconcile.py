from pathlib import Path
import json,csv,re,collections,hashlib,datetime,shutil
R=Path('_AUDIT/SYNC_2026-10-15_doctrine-part2');src=json.loads((R/'scratchpad/fc_sources.json').read_text());ed=json.loads((R/'SELECTED_EXACT_EDITS.json').read_text());workflow={x['id']:x for x in json.loads((R/'PROPOSED_EXACT_EDITS.json').read_text())};covered=collections.defaultdict(list)
for e in ed:
 ids=' '.join(e['ids'])
 for id in e['ids']:
  if id in workflow:ids+=' '+workflow[id]['authority']
 for id in set(re.findall(r'FC-\d{3}',ids)):covered[id].append(e['sequence'])
# Correct source-specific false assumptions and retain explicit unresolved components.
external={5:'skill precedence consumer',6:'skill seat terminology',8:'root FILE_TREE alignment',9:'external kit/example locators',10:'root authority classification',41:'verified kit guard signature/return contract',42:'verified kit session/cookie architecture',72:'verified kit rail breakpoint',90:'root pre-approval writes',91:'root evidence-first recovery',92:'skill closeout write boundary',94:'root CHANGELOG convention',95:'skill CI wording / CI trigger option',96:'skill merge-over-red wording / branch-protection enforcement'}
contain={1,22,30,33,34,35,38,39,41,42,45,47,50,51,52,53,54,55,56,57,58,59,60,62,64,66,67,68,71,72,76}
ledger=['# Selected scope and component ledger — Phase 2\n','Scope approved by Tony 2026-10-16, RUL-08…15. Exact map/spec and Phase 3 remain unapproved. Source disposition fields preserved; selected edit is not closure. Intake physically copied and indexed in INTAKE_SNAPSHOT_INDEX.json.\n','| Finding | Certified correction | Selected component | Exact proposal evidence | Remaining component / owner / trigger |','|---|---|---|---|---|']
for e in sorted(src,key=lambda x:x['id']):
 n=int(e['id'][3:]);status='NO correction — regression guard only' if n in {85,86,97} else 'OUTSIDE canonical scope' if n in {90,91,92,94,95} else 'SELECTED supported correction'
 if n in contain:status+='; withdrawal/containment does not close replacement'
 if n==55:status+='; universal schema DEFERRED by RUL-11'
 if n in {51,60,67}:status+='; universal quote storage DEFERRED by RUL-11'
 evidence=', '.join('E'+str(x) for x in covered[e['id']]) or ('archive restoration plan' if n==89 else 'derived MANIFEST/CHANGELOG proposal' if n in {87,93,96} else 'NO canonical change' if n in {85,86,90,91,92,94,95,97} else 'DEPLOYMENT_PLAYBOOK exact new proposal §§2–8' if n in {11,12} else 'RUL-12 exact scope/authority proposals (FC-005/014); root classification stays outside' if n==10 else 'PENDING exact coverage reconciliation')
 left=[]
 if n in external:left.append(external[n]+' — Jarvis coordinates named maintainer/evidence supplier; trigger: separately authorized job or supplied immutable kit revision')
 if n in contain:left.append('verified replacement / coherent dependent examples — Cody with Jarvis; trigger: required project/kit contract, separately released replacement and independent checks')
 if n in {11,12,88}:left.append('ungranted platform permissions / missing platform procedures — Jarvis coordinates; trigger: context-specific attributable authorization and procedure evidence')
 if n in {85,86,97}:left.append('retain NO correction and inspect pinned-main regression guards; no re-open')
 if not left:left.append('Engineer proposes selected correction; Fable independently derives acceptance after approved map; implementation and verdict pending')
 ledger.append(f"| {e['id']} | {'NO' if n in {85,86,97} else 'YES'} | {status} | {evidence} | {'; '.join(left)} |")
(R/'SELECTED_SCOPE_LEDGER.md').write_text('\n'.join(ledger)+'\n')
# Individual source-hit statuses never inferred from presence alone.
rows=list(csv.DictReader((R/'PLANNING_HISTORY/PRE_PHASE2_PROPAGATION.tsv').open(),delimiter='\t'));out=[]
for i,x in enumerate(rows,1):
 text=(R/'PROPOSED_CONTENT'/x['path']).read_text();y=dict(x);y['hit_id']=f'H{i:04}';y['baseline_disposition']=y['disposition']
 if x['quote'] not in text:
  y['disposition']='CHANGE';y['review_state']='EXACT PROPOSAL CHANGES SOURCE OCCURRENCE; semantic closure still checked by FC';y['reason']='Compare EXECUTION_PROPOSAL.patch and SELECTED_EXACT_EDITS; removed/modified occurrence is not finding closure.'
 elif x['disposition']=='HISTORY':
  y['disposition']='HISTORY';y['review_state']='RETAINED HISTORY; section boundary recheck required';y['reason']='Historical evidence is preserved; verify history boundaries, not a waiver for active instructions.'
 else:
  y['disposition']='PENDING';y['review_state']='FINAL SEMANTIC REVIEW REQUIRED';y['reason']='Presence in proposed content does not establish consistency; final disposition must be justified against approved rulings and source invariant.'
 out.append(y)
with (R/'PROPAGATION.tsv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=list(out[0]),delimiter='\t');w.writeheader();w.writerows(out)
count=collections.Counter(x['disposition'] for x in out)
# Replace current map sections; preserve previous complete map in PLANNING_HISTORY.
p=R/'UPDATE_MAP.md';m=p.read_text()
def sec(name,new):
 global m
 rg=re.compile(r'^## '+re.escape(name)+r'\.[^\n]*\n[\s\S]*?(?=^## [A-P]\.|\Z)',re.M)
 m,n=rg.subn(lambda x:new.strip()+'\n\n',m,count=1);assert n==1,name
intro='''# UPDATE MAP — doctrine-part2 — Phase 2 reconciliation

**Scope approved 2026-10-16; exact executable map NOT approved; Phase 3 NOT released.** Tony’s attributable RUL-08…15 are in DIRECTOR_RULINGS_2026-10-16.md. They resolve the selected policy questions only. The prior review draft is preserved in PLANNING_HISTORY/PRE_PHASE2_UPDATE_MAP.md; its historical OPEN labels and unselected alternatives are not current rulings.

Current exact proposal: EXECUTION_PROPOSAL.patch + EXECUTION_PROPOSAL_INDEX.json + PROPOSED_CONTENT/. Ordered content edits: SELECTED_EXACT_EDITS.json. These remain Engineer proposals, never independent acceptance or completed canonical implementation. Dates in review copies are planned 2026-10-16; at execution record the actual landing date consistently without fabricating an earlier completion. New playbooks stay DRAFT in this review tree; any Active transition must follow actual authorized landing/verification and be recorded.

**Engineering completeness remains OPEN:** final per-hit semantic dispositions and uncovered exact FC components in SELECTED_SCOPE_LEDGER.md. Do not freeze this map while PROPAGATION.tsv contains PENDING or boundary rechecks.

'''
m=intro+m[m.index('## 0. Run header'):]
m=m.replace('| Intake snapshot | Proposed `INTAKE_SNAPSHOT/` after approved scope and actual drop. Missing now; may not be represented as completed intake |','| Intake snapshot | Actual 189-file immutable snapshot from approved drop; INTAKE_RECEIPT.md and INTAKE_SNAPSHOT_INDEX.json. Not yet committed; Tony owns preservation. |')
sec('A','## A. Approved scope and actual intake\n\n'+(R/'SELECTED_SCOPE_LEDGER.md').read_text()+'\nOriginal 36 harvest and supporting-source classifications remain in PHASE1_LEDGER.md as historical planning; interpret them through RUL-01…15 and AD-01. Source templates and accepted behavior are not re-reviewed. Raw cargo can include historical alternatives without adopting them. Actual snapshot: INTAKE_RECEIPT.md; 189 hashes in INTAKE_SNAPSHOT_INDEX.json.')
# Keep verbatim source blocks; clearly mark old per-FC draft annotations as historical, not selected execution.
a=m.index('## B.');end=m.index('\n',a);m=m[:end]+ '\n\nThe source blocks below remain verbatim. Their earlier mapping-proposal/disposition annotations are retained as drafting history; SELECTED_SCOPE_LEDGER and RUL-08…15 govern current component selection, and §C exact proposals govern proposed text. No historical BLOCKED/OPEN label reopens an approved policy.\n'+m[end:]
sec('C','''## C. Exact proposed execution content

Use EXECUTION_PROPOSAL.patch and EXECUTION_PROPOSAL_INDEX.json for complete file-level proposed bytes; 334 ordered content replacements are in SELECTED_EXACT_EDITS.json. PROPOSED_CONTENT contains review copies only. DOCUMENT_VERSION_AND_ARCHIVE_PLAN.json enumerates 31 outgoing originals and proposed version bumps. No change is authorized by file existence here.

Scope represented: 31 revised tier documents, three new playbooks, 25 template translations, 30 exact outgoing archives, one restored historical archive and MANIFEST/CHANGELOG (93 changed paths). FRONTEND_FIRST_PLAYBOOK now has a bounded external-example provenance clarification; its outgoing version is preserved. The original generic paragraphs and broad placement lists are no longer execution instructions; they remain in the preserved previous map.

Uncovered exact components are explicitly marked PENDING in SELECTED_SCOPE_LEDGER. Withdrawals retain the certified finding/open dependency until verification supports closure. Metadata/index generation is a proposed mechanical reconciliation, not a claim that all findings are implemented.''')
sec('D','''## D. New playbooks and accepted templates

NEW_DOCUMENT_PROPOSALS.json identifies the three proposed new playbooks; PROPOSED_CONTENT/03_BUILD_METHODOLOGY contains exact review copies. DRAFTS holds untouched original drafts and substitutions record. RUL-08…15, not the substitutions JSON, provide approval authority.

PHASE_2_TEMPLATE_TRANSLATIONS.json replaces the earlier installation proposal for current review: 25 accepted source files, exact sequential translations and proposed hashes. Accepted source bytes are unchanged in the immutable snapshot. Source acceptance and placement remain settled (AD-01); translation approval and actual installation verification remain pending. Archive restoration is exact in ARCHIVE_RESTORATION_PROPOSAL.json and history only. No source package is retroactively labeled installed.''')
sec('F',f'''## F. Propagation status

PROPAGATION.tsv retains all {len(out)} baseline hit identities/quotes. Current counters: {dict(count)}. Changes are traceable to the proposed diff; retained occurrences are not automatically called CONSISTENT. Final semantic review and history-boundary verification are Engineer work still required before Gate 2. Baseline SEARCH_QUERIES.json defines scope/terms; SKILL_AWARENESS remains read-only main evidence. No false zero-pending claim.''')
sec('G','''## G. Index and archive proposals

PROPOSED_CONTENT/MANIFEST.md is derived from 34 proposed tier headers, with reverse dependencies and body-only references. Templates are governed via QAM_PLAYBOOK, not extra tier rows. PROPOSED_CONTENT/CHANGELOG.md carries per-document histories/IDs and historical restoration. Thirty-one outgoing archives preserve baseline bytes; QA v1.0 restores blob bb41260f6b6f94372a682f04b313a451f2b3c4b1.

The unchanged lint suite passed on the isolated proposal tree (36 linted documents); PROPOSED_LINT_CHECK.txt contains command, cwd, exit and raw output. This does not certify semantic correctness or change the actual canonical baseline’s nine findings. No lint/CI/skill files are proposed for implementation.''')
sec('K','## K. Current decisions, deferrals and engineering gates\n\n'+(R/'DIRECTOR_RULINGS_2026-10-16.md').read_text()+'\nPolicy votes are not reopened. External kit facts, root classification/implementation, skill/CI work, missing platform evidence, and expressly deferred universal quote/subscription designs retain their component status in SELECTED_SCOPE_LEDGER and EXTERNAL_FOLLOWUPS.md. K-MAP-FREEZE and K-DRAFT-INTEGRATION remain engineering/review gates, not resolved by policy approval.')
sec('N','''## N. Execution setup and commit plan

Phase 1 COMPLETE; Phase 2 CURRENT. Tony performs ALL Git mutations. Approved run-only override: one implementation commit for agreed document changes, with per-document histories, originals and verification retained. Necessary preservation, QA repair and closeout commits remain possible. No skill rewrite, release tag, universal commit-policy change or QA waiver.

Preserve the review branch; do not merge its older skill copy into main. Inspect refs and scoped changes first. OPERATOR_NEXT_STEPS.md supplies preservation and isolated-worktree commands for Tony. No execution worktree exists yet; current branch/HEAD remain factory-docs-review-astra-w-chunks / 626da8d70f4db22987dc7fcc86765492072360cd. Proposed BASE remains 9c179392f79b70da099121fc357d3107ad3bb86e (local main/origin-main; no fetch by Cody).

Lawful preparation writes: this run’s proposals, immutable intake snapshot, indexes, review evidence and handoff; approved _INBOX copies; session/recovery/response records. Original intake, corrections, drafts, accepted templates and historical ZIP remain untouched. No canonical or Git writes by Cody.''')
sec('O','''## O. Gates

- Phase 1 scope approval: Tony, 2026-10-16, explicit eight rulings; RUL-08…15 recorded.
- Actual intake/snapshot: copied and byte-verified under Phase 2 authorization; not yet committed.
- Gate 2 executable map: NOT APPROVED; remaining engineering completeness checks cannot be waived by scope approval.
- Independent acceptance specification: Fable derives; NOT authored or approved by Cody. No independent verdict is claimed.
- Phase 3 implementation: NOT RELEASED.

Execution is continuous only within released scope. Stop for concrete blockers, authority changes or required independent verdicts. After eventual map freeze, substantive changes require the governing amendment process; implementation/content identities belong in the handoff, not a retroactively altered frozen map.''')
p.write_text(m)
print('Current map reconciled; scope ledger',len(src),'FCs; propagation:',dict(count))
