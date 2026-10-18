from pathlib import Path
import json,re,difflib,hashlib
R=Path('_AUDIT/SYNC_2026-10-15_doctrine-part2');P=json.loads((R/'scratchpad/proposals.json').read_text())['wording'];files={str(p):p.read_text() for p in Path('.').glob('0*_*/*.md')};original=files.copy();ed=[]
P['55']='Subscription bootstrap, customer identity and resubscription must agree with the project’s approved schema. Universal subscription-schema design is deferred; no runnable replacement is supplied here. Preserve owner-only reads and server-only subscription writes. Keep this finding open until the project contract and recovery behavior are verified.'

P['53']=P['53'].replace('Persist customer identity independently of paid activation.','Use the project-approved customer-identity contract without assuming paid activation; universal subscription schema design is deferred.')
P['51']=P['51'].replace('A persisted versioned quote is a proposed design, not a certified requirement.','Universal quote-storage design is deferred; the required server pricing and payment binding still apply.')

def change(path,old,new,ids):
 assert old in files[path],(path,ids,old[:90]);assert files[path].count(old)==1,(path,ids,'ambiguous')
 ed.append(dict(ids=ids,path=path,old=old,new=new,label='ENGINEER-PROPOSED exact replacement',sequence=len(ed)+1));files[path]=files[path].replace(old,new,1)
def paragraph(path,needle,new,ids):
 matches=[x for x in files[path].split('\n\n') if needle in x];assert len(matches)==1,(path,needle,len(matches));change(path,matches[0],new,ids)
def section(path,heading,new,ids):
 text=files[path];start=text.index(heading+'\n');level=len(heading)-len(heading.lstrip('#'));lines=text[start:].splitlines(keepends=True);end=start+len(lines[0]);fence=False
 for line in lines[1:]:
  if line.startswith('```'):fence=not fence
  if not fence and re.match(r'^#{1,'+str(level)+r'} ',line):break
  end+=len(line)
 old=text[start:end];change(path,old,heading+'\n\n'+new.strip()+'\n\n---\n\n',ids)
def withdraw(path,heading,ns):
 section(path,heading,'**Executable example withdrawn.** The previous example is not an approved implementation. The outgoing archived document preserves it as history. Replacement code requires the project’s approved contract, verified dependency interfaces and behavioral evidence. This withdrawal contains the misleading recipe; it does not certify the underlying finding resolved.\n\n'+'\n\n'.join(P[str(n)] for n in ns),[f'FC-{n:03}' for n in ns]+['RUL-11'])
# Replay individually anchored existing proposals; draft-only changes are handled separately.
for e in json.loads((R/'PROPOSED_EXACT_EDITS.json').read_text()):
 if e['path'] in files:change(e['path'],e['old'],e['new'],[e['id']])
for e in json.loads((R/'EXACT_CORRECTION_EDITS.json').read_text()):
 if files[e['path']].count(e['old'])==1:change(e['path'],e['old'],e['new'],[e['id']])
 else:
  # The repeated canonical-name repairs have identical intent at each distinct occurrence.
  count=files[e['path']].count(e['old'])
  if count:
   old=files[e['path']];change(e['path'],old,old.replace(e['old'],e['new']),[e['id'],'all identical reference occurrences'])
S='01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md';E='02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md';F='03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md';B='01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md';H='02_PIPELINE_AGENTS/HANDOFF_PACKAGE_PLAYBOOK.md';D='02_PIPELINE_AGENTS/DESIGNER_PLAYBOOK.md';A='02_PIPELINE_AGENTS/ARCHITECT_PLAYBOOK.md';Q='03_BUILD_METHODOLOGY/QA_PLAYBOOK.md';T='03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md';K='01_CONSTITUTION/STARTER_KIT_HANDBOOK.md'
change(E,'- **Read-only.** No file changes, no git operations — pure inspection.','- **Inspection and reporting.** Read-only filesystem and Git inspection are permitted, along with declared recon, response, session and recovery writes. Git mutations remain with the Director. Diagnostic changes require explicit authorization; no product or contract changes are implied.',['FC-014','RUL-12'])
paragraph(E,'> Where any doc and the filesystem disagree', '> Disk and the running system establish what exists. The approved project brief governs scope; governing documents control their subjects. Evidence of drift does not amend requirements or grant implementation authority. Route genuine conflicts to the Director for an attributable ruling.',['FC-005','FC-014','RUL-12'])
change('02_PIPELINE_AGENTS/RECON_QUESTIONNAIRE.md','    no file changes, no git operations. Report findings verbatim."','    read-only filesystem and Git inspection plus declared reporting writes.\n    No Git mutations. Diagnostic changes require explicit authorization.\n    Report findings verbatim."',['FC-014','RUL-12'])
change(E,'> **GREENFIELD:** the **ENGINEER AUTHORS** `DATA_CONTRACT.md` from the approved APP_BRIEF + UI_SPEC (template: §12).','> **GREENFIELD:** the Architect authors `DATA_CONTRACT.md` from the approved APP_BRIEF before Design. The Designer authors UI_SPEC; the Architect reconciles the assembled package. The Engineer consumes the approved contracts. The canonical DATA_CONTRACT template remains in §12.',['FC-015','FC-017','FC-027','RUL-09'])
paragraph(E,'> **Ownership (per-pipeline):**','> **Ownership:** the Architect authors DATA_CONTRACT before Design, using the canonical template below. Conversion includes the approved extraction evidence. The Designer authors UI_SPEC; the Architect reconciles the assembled package. Engineering consumes the approved revisions; it does not create missing contracts during implementation.',['FC-027','RUL-09'])
change(E,'| **UI_SPEC.md** (approved) | Architect drafts, Designer revises | Screens, flows, gating logic, states |','| **UI_SPEC.md** (approved) | Designer; Architect reconciles assembly | Screens, flows, gating logic, states |',['FC-017'])
paragraph(H,'**Ownership is per-pipeline:**','**Ownership:** the Architect authors DATA_CONTRACT before Design. Conversion uses extraction evidence; greenfield uses the approved brief and verified interfaces. Engineering consumes the approved contract. Use the single canonical DATA_CONTRACT template in ENGINEER_PLAYBOOK §12; this section describes authoring requirements, not a competing template.',['FC-019','FC-027','RUL-09'])
paragraph(H,'Authorship shifts with the pipeline:','The Designer owns UI_SPEC. For conversion, extraction evidence and source screenshots inform the specification; for greenfield, the Designer’s token file and screen HTML/PNG establish the visual contract. The Architect reconciles the assembled package before Director approval.',['FC-017','RUL-09'])
paragraph(F,'> **DATA_CONTRACT ownership is per-pipeline','> **DATA_CONTRACT ownership:** the Architect authors the complete contract before Design for both pipelines, using conversion extraction evidence where applicable. The Designer authors UI_SPEC; the Architect reconciles both with the approved brief before Engineering begins. A shell is not a completed contract.',['FC-027','RUL-09'])
change(F,'**DATA_CONTRACT** is authored: From operator decisions, related repos\' extracts, or the starter kit\'s existing schema (Engineer is the author of record in greenfield runs — see §7\'s ownership note).','**DATA_CONTRACT** is authored by the Architect before Design, from the approved brief and verified interface/schema evidence.',['FC-027'])
change(F,"**UI_SPEC** is authored: From the Designer's screen HTML/PNG + token file (drafted by the Architect, revised by the Designer).","**UI_SPEC** is authored by the Designer from the approved brief, DATA_CONTRACT, screen HTML/PNG and token file; the Architect reconciles the assembled package.",['FC-017'])
change(F,'| DATA_CONTRACT source | Brain Drain TOOL-SYSTEM doc | Operator decisions, related extracts (Engineer authors) |','| DATA_CONTRACT source | Architect uses approved extraction evidence before Design | Architect uses approved brief and verified interfaces before Design |',['FC-027'])
change(F,'| UI_SPEC source | Brain Drain PROMPTS-AND-PERSONA + screenshots | Designer screen HTML/PNG (Architect drafts, Designer revises) |','| UI_SPEC source | Designer uses extraction evidence and screenshots; Architect reconciles | Designer authors from approved contracts and screen HTML/PNG; Architect reconciles |',['FC-017'])
paragraph(B,'**DATA_CONTRACT ownership differs per pipeline.**','**Artifact ownership:** the Architect owns DATA_CONTRACT before Design. The Designer owns UI_SPEC. The Architect reconciles the assembled package and Engineering consumes its approved revision. Conversion evidence informs those contracts; greenfield does not transfer authorship to Engineering. FILE_TREE is optional; implementation structure and boundaries must remain explicit in the approved package.',['FC-008','FC-017','FC-027','RUL-09'])
change(B,'| `FILE_TREE.md` | Exact folder/file structure for codebase | Engineer |','| `FILE_TREE.md` (optional) | Supplementary structure view; approved package still states implementation structure and boundaries | Architect assembly |',['FC-008'])
change(B,'3. **After the screen set locks:** Engineer produces `DATA_CONTRACT.md` + `FILE_TREE.md`.','3. **Before Design:** Architect prepares DATA_CONTRACT. After the Designer authors UI_SPEC and the screen set is approved, the Architect reconciles the full package. FILE_TREE is optional; structure and boundaries remain explicit.',['FC-008','FC-027'])
section(Q,'# 5. Source-of-Truth Order',P['5']+'\n\nApproved project briefs govern scope; governing documents control their respective subjects. Acceptance criteria are amended only by attributable approval. QA treats an implementation mismatch as evidence of a finding, not as a change to the acceptance contract.',['FC-005','RUL-12'])
# Replace the old human-Architect model itself, not an added competing paragraph.
section(S,'## 1. Philosophy: Human Architect, AI Builder',P['5']+'\n\n### Shared terminology\n\n'+P['6']+'\n\n'+P['7']+'\n\nSchema-first, approved specifications, incremental verification and recorded changes remain required.',['FC-005','FC-006','FC-007','RUL-12','RUL-14'])
# Containment targets selected by actual defective section; independent valid neighboring sections stay intact.
auth='04_REFERENCE_MANUALS/AUTH_MANUAL.md';api='04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md';com='04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md';stripe='04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md'
for heading,ns in [('## Client-Side Auth (Zustand Store)',[35]),('## 12. SuperAdmin User Management',[33,38]),('## 13. User Mirror Table Pattern',[33,39]),('## 14. HOC Route Protection Pattern',[35]),('### Pattern 4: Role-Based UI (Client)',[35]),('### Pattern 5: Conditional Navbar Links',[35])]:withdraw(auth,heading,ns)
for heading,ns in [('## 3. PaymentIntent Flow',[50,51,53,60]),('## 4. Checkout Implementation',[51,53,60,68]),('## 5. Order Management',[50,51,53,60]),('### Discount Calculation',[67]),('### Webhook Endpoint Setup',[52,54,59,62])]:withdraw(com,heading,ns)
for heading,ns in [('## 3. Supabase Schema Recipe',[55]),('## 5. The Checkout Flow',[53,55]),('## 6. The Webhook Handler',[52,54,55,59]),('## 7. The Tier Upgrade Pattern',[53,65])]:withdraw(stripe,heading,ns)
for heading,ns in [('### Webhook Endpoint Structure',[58,59]),('### Webhook Security',[58]),('### Async Follow-Up Pattern (Fire-and-Forget)',[59]),('### Idempotency for Webhooks',[56]),('### Manual Sync with Progress Tracking',[57]),('### Client-Side Sync Monitoring',[57])]:withdraw(api,heading,ns)
# Approved universal designs are expressly NOT substituted for withdrawn examples.
for path in [com,stripe]:
 s=files[path]
 for old in ['one persisted, versioned quote','one authorized persisted quote']:
  if old in s:change(path,s,s.replace(old,'a project-approved authoritative pricing contract'),['RUL-11']);s=files[path]
section('05_DESIGN_SYSTEM/THEMING_MANUAL.md','### 4.2 Supporting Deliverables (Visual Reference, Not Executable)','###placeholder',[]) if False else None
p='05_DESIGN_SYSTEM/THEMING_MANUAL.md';old='### 4.2 Supporting Deliverables (Visual Reference, Not Executable)';new='### 4.2 Required Visual Deliverables'
section(p,old,P['75'],['FC-075']);change(p,old,new,['FC-075'])
paragraph(K,'**Disk wins over docs.**','**Disk establishes implementation facts.** Verify every consumed export, route and breakpoint against the named kit revision. This handbook’s historical reconciliation is not proof for a different checkout. Approved briefs govern scope and governing documents control their subjects; route genuine conflicts to the Director.',['FC-005','FC-041','FC-042','FC-072','RUL-12'])

db='04_REFERENCE_MANUALS/DATABASE_MANUAL.md';state='04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md'
for path,heading,ns in [
 (auth,'### POST /api/auth/signup',[34]),(auth,'### Complete Registration Flow',[34]),(auth,'### RegisterForm Component',[34]),
 (db,'### Transaction Pattern (Pseudo-Transaction)',[39]),
 (state,'### Auth Store Pattern',[35]),(state,'### Form/Checkout Store Template',[40,47,68]),
 (state,'### Persisted Store Template',[47]),(state,'### `onRehydrateStorage` Callback',[47]),
 (T,'### E2E user lifecycle (Supabase apps)',[22]),(T,'### Discovery script architecture',[30]),
]:withdraw(path,heading,ns)
change(api,"if (secret !== process.env.REVALIDATION_SECRET) {","const expectedSecret = process.env.REVALIDATION_SECRET;\n  if (!expectedSecret || typeof secret !== 'string' || secret !== expectedSecret) {",['FC-061'])
change(db,'-- RLS policy excludes deleted records\nCREATE POLICY "Users see active records only"\nON resources FOR SELECT\nUSING (is_deleted = FALSE);','-- Restrictive filter: does not grant access. Enable RLS and supply a separate\n-- permissive ownership/tenant policy verified for the application.\nALTER TABLE resources ENABLE ROW LEVEL SECURITY;\nCREATE POLICY "Exclude deleted records"\nON resources AS RESTRICTIVE FOR SELECT TO authenticated\nUSING (is_deleted = FALSE);',['FC-037'])
change(db,"// Cursor-based (better for large datasets)\nconst { data } = await supabase\n  .from('orders')\n  .select('*')\n  .order('created_at', { ascending: false })\n  .lt('created_at', lastCreatedAt) // Cursor\n  .limit(20);",'// Cursor recipe withdrawn: a timestamp alone skips rows sharing that value.\n// Use a project-validated cursor over (created_at, id), ordered by both fields,\n// with a matching strict lexicographic boundary. Test tied timestamps and\n// pagination across every boundary before publishing an executable example.',['FC-045'])
change(T,'1. Log the full error server-side (for debugging).','1. Log only allow-listed structured diagnostics: correlation ID, operation, normalized failure class and safe provider code. Never log raw payment exceptions or personal data.',['FC-021'])
change(T,'  console.error("Stripe Error:", error);','  console.error("Payment operation failed", { failureClass: "provider_error" });',['FC-021'])
change(T,'  expect(data.message).not.toMatch(/declined/i);','  expect(data.message).not.toMatch(/declined/i);\n  // Also spy on the logger in this test and assert retained output contains\n  // neither synthetic sensitive marker (4242, abc-secret-leaked).',['FC-021'])
change(state,'        // Only persist addresses (user convenience)\n        billingAddress: state.billingAddress,\n        shippingAddress: state.shippingAddress,','        // Raw contact information is not persisted by default.\n        // An approved exception must name fields, purpose, retention and owner.',['FC-040','RUL-13'])
# Replace the contradictory statement and misleading heading, retaining token primacy.
p='05_DESIGN_SYSTEM/THEMING_MANUAL.md'
change(p,'### 4.2 Required Visual Deliverables','### 4.2 Required Visual Deliverables',['FC-075']) if False else None
# Exact phase-reference repairs against observed current text.
p='03_BUILD_METHODOLOGY/FRONTEND_BUILD_PHASE_PLAYBOOK.md'
for old,new in [('QA_PLAYBOOK §8','QA_PLAYBOOK §12'),('QA_PLAYBOOK §9','QA_PLAYBOOK §13')]:
 if old in files[p]:
  before=files[p];change(p,before,before.replace(old,new),['FC-032'])
# Root requirements remain an external job; scoped Director ruling is explicit in canonical wording.
paragraph(B,'### **FILE_TREE.md**','### **FILE_TREE.md** (optional)\n\nThe Architect may include a structure view when useful. The approved package must still define implementation structure and boundaries. Root tool-instruction alignment is separately tracked; an older required-FILE_TREE statement does not change the Director-approved artifact model.',['FC-008','RUL-09'])
# Correct the contact-persistence recommendation table without altering unrelated safe fields.
for line in files[state].splitlines():
 if line.startswith('|') and ('address' in line.lower() or 'contact' in line.lower()):
  if 'Persist' not in line and 'partialize' not in line:
   # Preserve exact table shape; move policy to the text surrounding it in further review.
   pass


# Additional propagation corrections found during the Phase 2 semantic pass.
change(E,'9. ✅ Produce DATA_CONTRACT.md (greenfield) / honor the pre-authored one (conversion)','9. ✅ Consume the Architect-authored, approved DATA_CONTRACT; verify it precedes Design and that the Architect reconciled the assembled package.',['FC-027'])
change(B,'| `DATA_CONTRACT.md` | All data shapes, API payloads, state objects | Engineer |','| `DATA_CONTRACT.md` | All data shapes, API payloads, state objects; approved before Design | Architect |',['FC-027'])
change(B,'│   └── FILE_TREE.md (exact structure)','│   └── FILE_TREE.md (optional structure view; boundaries remain required)',['FC-008'])
change(B,'| "What does the Engineer actually produce?" | DATA_CONTRACT + DB_SCHEMA + API_SPEC + FILE_TREE |','| "What does the Engineer actually produce?" | Implementation and factual handoff against approved contracts; contract changes return to the Architect and Director |',['FC-008','FC-027'])
change(B,'| "What if Claudy breaks existing code?" | FILE_TREE.md = source of truth; Engineer enforces "don\'t touch what works" |','| "What if Claudy breaks existing code?" | Approved scope and structure boundaries govern; stop, report the regression, and repair only within authorization |',['FC-008'])
change('02_PIPELINE_AGENTS/ARCHITECT_QUESTIONNAIRE.md','> **Status:** [DRAFT | REVIEW | LOCKED]','> **Status:** [DRAFT | APPROVED | AMENDED — record approver and revision; never prefill approval]',['FC-016'])
change(D,'> **Status:** APPROVED','> **Status:** DRAFT — approval requires an attributable decision on this revision',['FC-016'])
change(F,'> **Status:** LOCKED','> **Status:** DRAFT — approval requires an attributable decision on this revision',['FC-016'])
rc='02_PIPELINE_AGENTS/RECON_QUESTIONNAIRE.md'
change(rc,'- **Read-only.** Claudy answers by reading and grepping. No file changes, no `cd && git` that could trigger hooks. Pure inspection.','- **Inspection and declared reporting.** Read-only filesystem/Git inspection and declared recon/reporting writes are allowed. Git mutations belong to the Director. Build, cache or other diagnostic changes require explicit authorization naming expected writes; otherwise report the limitation.',['FC-014','RUL-12'])
for line in list(files[rc].splitlines()):
 if line.startswith('npm run build 2>&1'):
  change(rc,line,'# DIAGNOSTIC CHANGES: run only after explicit authorization.\n# Capture command, working directory, exit code and unfiltered output.\n# Without authorization, report this check as not performed; do not run it.\nnpm run build', ['FC-014','RUL-12'])
p='03_BUILD_METHODOLOGY/FRONTEND_BUILD_PHASE_PLAYBOOK.md'
change(p,'**Gate Q — Pre-Deployment Quality Gate** passed per `QA_PLAYBOOK.md` §9','**Gate Q — Pre-Deployment Quality Gate** passed per `QA_PLAYBOOK.md` §12',['FC-032'])
if '**Gate D' in files[p]:
 for line in files[p].splitlines():
  if '**Gate D' in line and '`QA_PLAYBOOK.md` §10' in line:change(p,line,line.replace('`QA_PLAYBOOK.md` §10','`QA_PLAYBOOK.md` §13'),['FC-032'])
# Canonical Hub links do not prescribe downstream project-copy locations.
for path in [K,'05_DESIGN_SYSTEM/COMPONENT_REGISTRY.md','05_DESIGN_SYSTEM/THEME_LIBRARY.md']:
 before=files[path];after=before.replace('agent_docs/APP_FACTORY/design-system/','').replace('agent_docs/APP_FACTORY/','').replace('UI-UX-BUILDING-MANUAL.md','UI_UX_BUILDING_MANUAL.md')
 if before!=after:change(path,before,after,['FC-003','FC-081','RUL-14'])
# Client server-state synchronization: a populated store is not evidence of freshness.
change(state,'    if (products.length === 0) {\n      setProducts(initialProducts);\n    }','    setProducts(initialProducts);',['FC-048'])
change(state,'  }, [initialProducts, products.length, setProducts]);','  }, [initialProducts, setProducts]);',['FC-048'])
# Explicit authorization even where an older recipe suggested fix-then-report.
for path in [E,F,T]:
 for para in list(files[path].split('\n\n')):
  if re.search(r'fix.{0,35}(?:then|after).{0,25}(?:report|approval)|implement.{0,35}ask.{0,15}later',para,re.I) and len(para)<1000 and not para.startswith('|'):
   change(path,para,P['23'],['FC-023','RUL-12'])


u='05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md';theme='05_DESIGN_SYSTEM/THEME_LIBRARY.md';tokens='05_DESIGN_SYSTEM/TOKEN_FILE.md'
# Preserve the advertised primitive API by pointing to the existing primitive; remove the incompatible replacement.
section(u,'#### Creating Variant Recipes',P['76']+'\n\nUse the installed Shadcn Button as the component, retaining its verified Slot/asChild, ref and native-prop behavior. Do not replace it with the former simplified button implementation. Add a bounded variant only after verifying the installed API. All actionable sizes keep a 44×44px minimum target.',['FC-076','FC-079'])
for old,new in [('<Button variant="primary" size="md">','<Button variant="default" size="default">'),('<Button variant="primary" />','<Button variant="default" />')]:
 if old in files[u]:
  before=files[u];change(u,before,before.replace(old,new),['FC-076'])
section(u,'#### Dark Mode Toggle',P['78'],['FC-078'])
section(u,'#### Explicit Dark Variants (When Needed)','Use semantic tokens for both modes. If a required semantic state is missing, extend the approved token contract and verify all modes; do not create a numbered-color bypass.\n\n```tsx\n<div className="bg-background text-foreground">\n  <p className="text-muted-foreground">This text follows the active token mode.</p>\n</div>\n```',['FC-073'])
for line in files[u].splitlines():
 if line=='- [ ] No horizontal scroll':change(u,line,'- [ ] No unintended page-level horizontal overflow; intentional bounded tabs/carousels remain usable by touch, keyboard and assistive technology.',['FC-082'])
# Token values use the already computed, preserved contrast proposal; hue stays fixed.
fmt=lambda v:f'{v[0]:g} {v[1]:g}% {v[2]:g}%'
for mode,pattern in [('Mist',r':root \{(.*?)\n  \}'),('Slate',r'  \.dark \{(.*?)\n  \}')]:
 match=re.search(pattern,files[tokens],re.S);assert match;old=match.group();new=old
 for item in json.loads((R/'scratchpad/token_changes.json').read_text()):
  if item['mode']!=mode:continue
  rg=re.compile(r'('+re.escape(item['token'])+r':\s*)'+re.escape(fmt(item['old']))+r';[^\n]*')
  new,n=rg.subn(lambda m:m[1]+fmt(item['new'])+';',new);assert n==1,(mode,item['token'],n)
 change(tokens,old,new,['FC-074'])
for old,new in [('coral `#f9704f` → `12 93% 64%`','coral hue — `12 93% 39%` light / `12 93% 66%` dark'),('`131 54% 40%` light','`131 54% 29%` light'),('`2 67% 51%` light','`2 67% 45%` light'),('blue `#2f7ce0` → `214 74% 53%`','blue hue — `214 74% 43%` light / `214 74% 66%` dark'),('amber `#e8a008` → `41 93% 47%`','amber hue — `41 93% 27%` light / `41 93% 47%` dark'),('What changes between modes is **only the neutral surface stack**:','Semantic hue and meaning hold across modes; lightness and paired foregrounds may differ to meet contrast requirements. TOKEN_FILE contains the reference values. Verify the documented text/fill uses before claiming accessibility:'),('only the surface stack changes (background, card, muted, border, secondary). Brand + semantic + role stay fixed.','choose the surface stack; preserve brand, semantic and role hue/meaning while adjusting lightness and paired foregrounds for verified contrast.')]:
 change(theme,old,new,['FC-074'])
# Template/source paths are explicit Hub canonical references, not project installation instructions.
section(S,'## 9. Phase 7: Authentication & RBAC',P['1']+'\n\n'+P['33']+'\n\n'+P['36']+'\n\nVerify authentication state, table-backed current role, object-level authorization, denied targets, session expiry, logout and first server render. The former metadata-role/auth-store checklist is withdrawn. Kit-dependent signatures require the pinned kit evidence; this containment does not close those replacements.',['FC-001','FC-033','FC-036','RUL-11'])


# Rewrite obsolete pipeline diagrams and boot routes rather than retain competing instructions.
for path in [B,A,D,E]:
 matches=list(re.finditer(r'^```[^\n]*\n[\s\S]*?^```',files[path],re.M))
 for m in matches:
  old=m.group()
  if 'DATA_CONTRACT' in old and ('┌' in old or 'PHASE 0: RECON' in old):
   new='''```text
Director approves scope and releases each assignment.
Engineer: ground-truth recon -> Architect: approved APP_BRIEF + DATA_CONTRACT before Design
Designer: UI_SPEC + applicable visual artifacts -> Architect: reconciled module + ACCEPTANCE_SPEC + QAM
Director release -> Engineer implementation and factual handoff -> Director commits completed candidate
QA Executor Q1 -> QA Lead plan approval -> Director Q2 release -> QA Executor execution
Conditional Engineer repair / independent retest on continuing QA branch -> QA Lead verdict
Required cleanup -> Architect closeout -> bounded Engineer closeout -> Director final Git actions
Reviews: after FFM + QA, and Engine 2 after all Engine 1 engineering and QA; RRM only for approved findings.
FILE_TREE is optional; implementation structure and boundaries remain explicit.
```'''
   change(path,old,new,['FC-004','FC-008','FC-017','FC-027','RUL-01','RUL-09'])
change(F,'Conflict resolution: `DATA_CONTRACT.md` wins on data shapes, `UI_SPEC.md` wins on UI behavior, `_project/CLAUDE.md` wins on scope, this file wins on module structure. If two sources still conflict, STOP and surface to the operator.','Conflict resolution: the approved APP_BRIEF governs scope; DATA_CONTRACT and UI_SPEC govern their subjects. Managers route to those contracts and cannot change them. Genuine conflicts stop affected work for attributable Director resolution.',['FC-029','RUL-12'])
section(F,'### C.2 — `_project/APP_BRIEF.md` Stub','Instantiate the single canonical APP_BRIEF template from ARCHITECT_QUESTIONNAIRE.md. Fill its pipeline-specific sections from attributable evidence; record the actual approval and revision. Do not fork the former duplicate stub. The approved package also contains the Architect-owned DATA_CONTRACT, Designer-owned UI_SPEC, ACCEPTANCE_SPEC and prepared QAM.',['FC-019','FC-025'])
section(F,'### B.1 — First Session (Fresh Boot)','''```text
Identify your assigned seat and released assignment before acting.
Read applicable root instructions, then the project’s declared module pointer and its actual entry file.
Read the approved APP_BRIEF, DATA_CONTRACT and applicable UI_SPEC at their declared locations.
Engineering routes to implementation; QA routes into the prepared QAM as QA Executor.
Verify acceptance contract, candidate identity, governing snapshot pins and declared writable lanes.
Read-only filesystem/Git inspection and declared reporting writes are allowed.
Diagnostic changes need explicit authorization. Git mutations remain with the Director.
Missing or contradictory prerequisites: report evidence and STOP the affected work.
Q1 prepares the independent plan; Q2 requires QA Lead approval and Director release.
Continue within the released assignment; stop at its required boundaries.
```

The module declares actual project paths and available skills; no universal project-copy path is assumed. Mirror parent routing in CLAUDE.md and AGENTS.md. Do not prefill independent QA approvals or results.''',['FC-014','FC-025','FC-081','RUL-12','RUL-15'])
section(F,'### B.2 — Resume Session (After Interruption)','''```text
Read RECOVERY.md and the declared active module entry, then verify their claims against disk.
Confirm assigned seat, branch/candidate, approved contract revision, latest approval and writable lanes.
Use QAM’s durable state for QA; do not resume from historical prose alone.
Report the last verified completed step and next authorized action.
Continue within the still-valid released assignment; stop for a changed authority, concrete blocker or required independent verdict.
```''',['FC-025','RUL-15'])
change(F,"Roll back the work that wasn't approved.","Preserve and inventory the unapproved work. Report the affected paths; the Director authorizes recovery and performs any Git mutation.",['RUL-15'])
# Subject authority may not silently redefine brief scope elsewhere in the manager prose.
for para in list(files[F].split('\n\n')):
 if 'wins on scope' in para and len(para)<1000:change(F,para,P['29'],['FC-029'])
# Nonvisual builds have explicit applicability; append at receiving checklists without retaining a universal visual demand.
for path,heading in [(E,'### Greenfield Inputs (Kit Track: Architect → Designer → Engineer)'),(D,'## 2. Inputs Required'),(H,'## 4. Prerequisites Before Authoring')]:
 change(path,heading+'\n',heading+'\n\n'+P['18']+'\n', ['FC-018'])
# Do not treat build-with-disabled-dependency as passing the full deployed flow.
paragraph(T,"When a test can't be made reliable due to an architectural issue outside the test layer",P['24']+' A skipped check records the reason, attempts, coverage gap and approved compensating verification; it is not a passing result.',['FC-024'])


change(S,'### Feature Development Checklist\n','### Feature Development Checklist\n\n- [ ] Approved brief, applicable specifications and complete applicable screen set are identified before implementation.\n- [ ] Approved ACCEPTANCE_SPEC and engineering QAM handoff are ready before independent QA.\n',['FC-002'])
change(S,'## Pre-Release QA\n','## Pre-Release QA\n\n- [ ] QA Lead Gate Q verdict and Director release decision are recorded separately.\n- [ ] Applicable deployed-environment Gate D is planned and verified; build success is not Gate D.\n',['FC-002'])
section(T,'### G5: Webhook handler always returns 200',P['20'],['FC-020','DEC-03'])
change(T,'### G5: Webhook handler always returns 200','### G5: Webhook acknowledgment follows durable acceptance',['FC-020'])
change(T,'- **HIGH-severity findings** — fix inline in the same session (small, contained source change + test that locks in the fix).','- **HIGH-severity findings** — report immediately. Implement only within the existing approved scope; otherwise obtain an attributable scope amendment first. Severity creates urgency, not an emergency authorization.',['FC-023'])
change(T,'│             (a) page.route to abort the script\'s network request','│             (a) diagnostic isolation only: abort the request, record omitted coverage',['FC-024'])

change(T,'│             (b) addInitScript to neutralize history.replaceState etc.','│             (b) diagnostic isolation only: neutralize effects, no full-flow PASS',['FC-024'])
# Remove the auth-wrapper interface itself; preserve neighboring domain-contract content.
m=re.search(r'export interface AuthService \{[\s\S]*?\n\}',files[F]);assert m
change(F,m.group(),'// Kit auth is consumed directly after recon; do not author an AuthService wrapper.\n// Declare only genuinely missing, approved project-domain services.', ['FC-028'])
line=next(x for x in files[K].splitlines() if x.startswith('**User creation is via server actions'))
change(K,line,'**User creation requires operation-local authorization.** A role-gated layout is not the security boundary for a server action: verify the invocation’s authenticated caller, current table-backed role, allowed target and privileged-target protection before obtaining elevated capability. Verify kit action signatures at the pinned revision. Superadmin creation remains console-only.',['FC-036','DEC-04'])
change(auth,'| User creation (admin/superadmin) | `addMember` / `addUser` server actions | role-gated layout + service-role admin client |','| User creation (admin/superadmin) | Verify named actions against pinned kit | Each invocation checks caller, current role, allowed target and privileged-target protection before elevated capability |',['FC-036'])
# Stable distinct quick-reference anchors, preserving both reference bodies.
old='## 10. Quick Reference';matches=[m.start() for m in re.finditer(re.escape(old),files[api])];assert len(matches)==2
before=files[api];i=matches[-1];change(api,before,before[:i]+before[i:].replace(old,'## 14. Integration Quick Reference',1),['FC-070'])
change('05_DESIGN_SYSTEM/COMPONENT_REGISTRY.md','- [ ] Does horizontal scroll occur at any width? (If yes, fix the layout)','- [ ] No unintended page-level horizontal overflow; bounded intentional tabs/carousels remain accessible and usable.',['FC-082'])
change(u,'- **No horizontal scroll** at any width below desktop','- **No unintended page-level horizontal overflow** below desktop; bounded intentional tabs/carousels are permitted with accessible controls.',['FC-082'])
for path,old,new in [
 ('05_DESIGN_SYSTEM/THEMING_MANUAL.md','**APP_ARCHITECTURE_MANUAL** §Theming Files','**APP_ARCHITECTURE_MANUAL** §7 Component Architecture'),
 ('05_DESIGN_SYSTEM/THEMING_MANUAL.md','**HANDOFF_PACKAGE_PLAYBOOK** §Designer Handoff','**GLOBAL_DESIGN_SYSTEM_HANDBOOK** §8 The Designer’s deliverables'),
 ('05_DESIGN_SYSTEM/THEMING_MANUAL.md','**STARTER_KIT_HANDBOOK** §shadcn Defaults','**COMPONENT_REGISTRY** §5 Shadcn Primitives'),
 (u,'**`APP_ARCHITECTURE_MANUAL.md`** §Theming Files','**`TOKEN_FILE.md`** §1 Entry stylesheet'),
 (u,'**`HANDOFF_PACKAGE_PLAYBOOK.md`** §Designer Handoff','**`GLOBAL_DESIGN_SYSTEM_HANDBOOK.md`** §8 The Designer’s deliverables'),
]:
 change(path,old,new,['FC-083'])
# Pin refresh follows the approved project snapshot, not an implied latest-main update.
p='03_BUILD_METHODOLOGY/FRONTEND_BUILD_PHASE_PLAYBOOK.md'
change(p,'At the START of each stage below (before any work), re-read:','At the START of each stage below (before any work), re-read the approved project snapshots, identified by canonical document name, header version and Hub commit. Preserve intentional pins until an authorized update; resolve the project’s declared paths rather than assuming a universal landing path. Re-read:',['FC-088','RUL-14'])
# Missing API trust-boundary cases are required verification, not a purported completed campaign.
for path,heading in [(T,'## 3.8 Run-verification rituals (promoted from Run 001)'),(com,'## 10. Testing Payments'),(stripe,'## 12. Testing Strategy')]:
 change(path,heading+'\n',heading+'\n\n'+P['63']+'\n', ['FC-063'])


g='05_DESIGN_SYSTEM/GLOBAL_DESIGN_SYSTEM_HANDBOOK.md'
change(g,'3. Asks the Architect for the **UI_SPEC draft** (or drafts the screen list with them).','3. Receives the Architect’s approved **DATA_CONTRACT before Design**, then authors UI_SPEC; the Architect reconciles the assembled package.',['FC-017','FC-027'])
change(g,'4. Produces, in order: **token file → canonical screen → style tile → remaining screen artifacts → UI_SPEC revision → component manifest.**','4. Produces **token file → canonical screen → style tile → remaining screen artifacts → UI_SPEC → component manifest**, using the full canonical token contract; validates all modes and role/semantic distinctions.',['FC-077'])
section(u,'#### CSS Variables in globals.scss','Use the complete mode declarations in TOKEN_FILE.md §1 and the canonical token contract in GLOBAL_DESIGN_SYSTEM_HANDBOOK.md §2. The former partial CSS block is withdrawn as a drop-in setup recipe: it omitted required semantic and role tokens. Preserve every required category, foreground pairing, radius and mode override when instantiating the stylesheet.',['FC-077'])
for path,heading in [(u,'### Sidebar Component (Members)'),(u,'### AdminSidebar Component'),(u,'#### Sidebar Layout (Desktop Only)'),(u,'### Example 3: Members Portal with Layout')]:
 section(path,heading,P['71']+'\n\nThe former copyable layout is withdrawn because it hid navigation on small screens or bypassed the installed shell. Use the verified responsive shell/rail/drawer contract for the pinned kit; do not invent a breakpoint or duplicate the shell. Verify reachable navigation, focus management, keyboard/escape behavior and no page overflow at every supported width.',['FC-071','FC-072'])
# Positive numbered-color examples conflict with the semantic-token contract. Negative examples stay negative.
for path in [u,'05_DESIGN_SYSTEM/COMPONENT_REGISTRY.md']:
 for match in list(re.finditer(r'^```[^\n]*\n[\s\S]*?^```',files[path],re.M)):
  block=match.group()
  if not re.search(r'(?:bg|text|border)-(?:blue|gray|slate|red|green|yellow|purple)-\d{2,3}',block):continue
  if '❌' in block or '// WRONG' in block:continue
  def color(m):
   prefix,family,shade=m.groups();token={'blue':'primary','red':'destructive','green':'success','yellow':'warning','purple':'accent'}.get(family)
   if token:return prefix+'-'+token
   return prefix+'-'+('border' if prefix=='border' else 'foreground' if prefix=='text' and int(shade)>=800 else 'muted-foreground' if prefix=='text' else 'muted')
  new=re.sub(r'(bg|text|border)-(blue|gray|slate|red|green|yellow|purple)-(\d{2,3})',color,block)
  if new!=block:change(path,block,new,['FC-073'])
# Service failure/shape examples require one approved contract; withdraw incompatible complete examples.
for heading in ['### Creating a Service File','### Error Handling Template','### GET Route Template']:
 withdraw(api,heading,[64,66])
if '**The Golden Rule:** Services should never throw errors that crash the UI. Return safe defaults.' in files[api]:
 change(api,'**The Golden Rule:** Services should never throw errors that crash the UI. Return safe defaults.','**Failure policy:** distinguish successful empty data, not-found, validation/authorization failure and dependency failure under the approved service contract. A fallback is permitted only by the module’s declared failure policy and remains distinguishable from success; UI safety does not justify concealing outages.',['FC-064'])
# One documented credential-name contract per project; aliases are not assumed equivalent automatically.
change(rc,'## SECTION 0 — The Day-1 Ground-Truth Sweep (Run 001 Meta-Lesson)\n','## SECTION 0 — The Day-1 Ground-Truth Sweep (Run 001 Meta-Lesson)\n\nRecord the actual server-only Supabase credential variable name used by this project and its approved alias mapping. Reference examples using SUPABASE_SERVICE_ROLE_KEY or SUPABASE_SECRET_KEY are alternative project profiles, not two automatically configured credentials. Confirm each consumer against the same contract; never expose either credential in client bundles or logs.\n',['FC-069'])
# Complete the missed exact anchor spelling.
change('05_DESIGN_SYSTEM/THEMING_MANUAL.md','§5 Shadcn Primitives','§5 Shadcn UI Primitives',['FC-083'])


arch='04_REFERENCE_MANUALS/APP_ARCHITECTURE_MANUAL.md'
change(arch,'├── authServices.ts               # Auth operations','├── <domain>Services.ts           # Approved domain logic; consume kit auth directly',['FC-001','FC-028'])
for heading in ['### Route Protection']:
 withdraw(arch,heading,[33,36,41])
# Replace only the conflicting example fences, not the whole layout/security chapter.
for match in list(re.finditer(r'^```[^\n]*\n[\s\S]*?^```',files[arch],re.M)):
 block=match.group()
 if 'useAuthStore(selectIsAdmin)' in block or 'w-64 hidden md:block' in block:
  change(arch,block,'**Example withdrawn:** consume the verified responsive kit shell and server-resolved identity props. Client-store role hints are not page authority; navigation must remain reachable on mobile. '+P['71'],['FC-035','FC-071'])
for para in list(files[arch].split('\n\n')):
 if 'httpOnly: true' in para:
  change(arch,para,'Session-cookie attributes must follow the verified pinned kit’s session architecture. HTTPS and Secure transport remain required in production; do not impose an unverified HttpOnly architecture on a browser-client session model. Record the verification gap rather than guessing compatible options.',['FC-042'])
change(D,'**Conflict rule:** if this playbook and a doctrine doc disagree on tokens or method, the doctrine doc wins — surface the conflict and update this playbook.','**Conflict rule:** governing documents control their subjects and the approved brief controls scope. Record the conflicting revisions and obtain an attributable Director resolution; do not silently update either side.',['FC-005','RUL-12'])
# Do not make an external skill job a passenger of this canonical playbook update.
sk='03_BUILD_METHODOLOGY/APP_FACTORY_SKILLS_PLAYBOOK.md'
change(sk,'## 15. Authoring A New Skill — Step By Step\n','## 15. Authoring A New Skill — Step By Step\n\nBefore changing referenced doctrine, use MANIFEST header dependencies as a starting set, then inspect body-only references, templates, checklists, examples and consuming skills. Record every affected consumer and route changes outside the authorized boundary to a separately approved job. A header graph is not a complete impact analysis.\n',['FC-087'])


# Residual semantic checks: remove the obsolete summary and other active consumers.
change(auth,'4. Roles stored in user_metadata','4. Authorization roles resolved from the authoritative user_roles table; never from user_metadata.',['FC-033'])
for block in list(re.finditer(r'^```[^\n]*\n[\s\S]*?^```',files[auth],re.M)):
 old=block.group()
 if 'is_qr_superadmin:' in old and 'user_metadata:' in old:
  change(auth,old,'**Legacy response example withdrawn:** client metadata flags are not authorization or first-render identity. Use the verified server-resolved user/role contract for the pinned kit.',['FC-035'])
for path in [auth,K]:
 for block in list(re.finditer(r'^```[^\n]*\n[\s\S]*?^```',files[path],re.M)):
  old=block.group()
  if 'protectPage(' in old and not ('❌' in old or 'WRONG' in old):
   change(path,old,'**Kit-signature example withdrawn pending verification:** '+P['41'],['FC-041'])
for old,new in [('`httpOnly: true` - Not accessible via JavaScript','HttpOnly attributes — verify against the approved kit session architecture; no blanket value is prescribed here'),('   - `httpOnly: true`','   - HttpOnly only where compatible with the verified session architecture')]:
 change(auth,old,new,['FC-042'])
for heading in ['### Hydration Flags','### Cart Store Pattern']:
 withdraw(state,heading,[47])
for old,new in [("'h-8 text-sm'","'min-h-11 min-w-11 text-sm'"),("'h-10 text-base'","'min-h-11 min-w-11 text-base'")]:
 if old in files[u]:
  before=files[u];change(u,before,before.replace(old,new),['FC-079'])

# Residual propagation review: exact source occurrences, preserving unrelated history.
hits=json.loads((R/'scratchpad/phase2_retained_hits.json').read_text())
def hit(i,new,ids=None):
 e=hits[i];old=e['quote'];path=e['path']
 if old not in files[path]:return
 if files[path].count(old)==1:change(path,old,new,ids or e['queries'])
 else:
  before=files[path];change(path,before,before.replace(old,new),ids or e['queries'])
hit(0,'**User creation requires a verified trusted role path.** Never permit client-writable metadata to grant privilege. Verify the pinned trigger and protected admin action before using creation-time transport; avoid duplicate inserts only where the verified trigger already owns those rows. Missing kit evidence blocks this recipe.',['FC-001','FC-033','FC-034'])
hit(4,'> **Q3.4:** inspect both authorization reads and creation-time writes. User-writable metadata must never grant privilege, including through a trigger. A protected caller alone does not make a shared metadata field trustworthy: prove that public signup cannot supply the privileged value. Record the pinned role table, resolver, trigger and caller evidence; otherwise flag the path as unsafe.',['FC-001','FC-033','FC-034'])
for i in [9,13,16,362,363]:hit(i,'Roles must resolve from an authoritative server-side store. Creation and mutation require verified per-call authorization and a role input that untrusted signup cannot control. The historical Mark IV transport is not a verified safe recipe for the current kit; obtain pinned trigger and caller evidence before implementation.',['FC-001','FC-033','FC-034','FC-036'])
# Withdraw the duplicated unsafe compensation/metadata recipe, not just its companion example.
s=files[db];start=s.index('**Synchronization Logic:**');end=s.index('### External System Mapping Table',start)
change(db,s[start:end],'**Synchronization example withdrawn.** '+P['33']+' '+P['38']+' '+P['39']+'\n\n',['FC-033','FC-038','FC-039','RUL-11'])
paragraph(auth,'**Authorization:** the route-group layout gates access','**Authorization:** the server action itself must authenticate and authorize each invocation before any privileged client call. A route-group layout is not an action authorization boundary. Resolve roles from the authoritative server store and allow only explicitly permitted target roles. Do not use a user-writable metadata trigger to assign privilege. The historical action/trigger recipe is withdrawn pending pinned kit verification.',['FC-001','FC-033','FC-034','FC-041'])
# Unavailable worked examples are identified as historical external pointers, not promised local files.
hit(68,'> Pair each methodology with an available, verified worked example. Historical external pointers below are not proof that an example is present in this Hub or in a project. Record repository, immutable revision and path before requiring it.',['FC-009'])
for i in [72,77,78,81,83,108,115,117,119,120,268,391,1129]:
 e=hits[i];hit(i,'**Historical external example pointer — availability unverified:** '+e['quote'].replace('canonical worked example','historical worked example').replace('canonical example','historical example')+' Obtain the source repository, immutable revision and path before use; do not assume this path exists locally.',['FC-009'])
# Role and authorization wording must agree at actual consumer sites.
hit(54,'1. [Philosophy and Factory Seats](#1-philosophy-and-factory-seats)',['FC-006'])
hit(55,'## 1. Philosophy and Factory Seats',['FC-006'])
hit(57,'✅ **Collaborative** — Director, Architect, Designer, Engineer and independent QA retain distinct responsibilities.',['FC-006'])
hit(58,'> Read by skill authors in their assigned seats. Engineer agents consume skills and may author them only under an explicit skill-authoring assignment.',['FC-006'])
hit(155,'| **Engineer** | Plans, builds within release, self-verifies, fills factual acceptance/handoff records; may inspect Git read-only; all Git mutations remain Director-only and BIM cloud-zero remains in force |',['FC-014','RUL-12'])
hit(218,'- **Git/cloud authority:** read-only Git inspection is allowed; the Director performs all Git mutations. The BIM Engineer does not deploy and supplies exact file lists and suggested commit messages.',['FC-012','FC-014','RUL-12'])
hit(530,'The Engineer may inspect Git read-only; all Git mutations remain Director-only and existing FIX cloud restrictions remain in force. Engineering fills factual handoff records within the approved acceptance contract. Changes beyond the released writable surface require explicit authorization before execution.',['FC-012','FC-014','RUL-12'])
hit(161,hits[161]['quote'].replace('git-zero/cloud-zero','read-only Git inspection with Director-only mutations and the existing BIM cloud restrictions'),['FC-014','RUL-12'])
hit(546,'- **Do not silently deviate:** a change outside the authorized writable surface, including diagnostic, test-runner or build configuration changes, requires explicit authorization before execution. Report the proposed change and its evidence; later ratification is not prior authorization.',['FC-014','RUL-12'])
hit(567,'**Why:** the historical wrapper near-miss and phantom exports demonstrate the need to inspect the pinned kit. Filesystem evidence establishes implementation facts; approved briefs govern scope and governing documents control their subjects. Route genuine conflicts to the Director.',['FC-005','FC-014'])
hit(248,'- **Discipline encoded:** read-only inspection plus declared reporting writes, verbatim findings and evidence-based recon. Facts on disk do not silently amend approved requirements.',['FC-005','FC-014'])
hit(245,'- Inspect relevant environment variable names and whether required configuration is present; do not print secret values or dump `.env.local`.',['FC-021'])
hit(385,'| **UI_SPEC.md** | Designer, from approved contracts and conversion evidence; Architect reconciles | Screen-by-screen behavior and primitive mapping |',['FC-017','RUL-09'])
hit(416,'| 4 | **UI_SPEC.md** | Designer-authored hierarchy, gating, states, responsive rules and checkpoints; Architect reconciles the assembled package |',['FC-017','RUL-09'])
hit(417,'5. **Designer authors UI_SPEC and component manifest; Architect reconciles the assembled package.**',['FC-017'])
hit(421,'| "How do we version this?" | Record the project-declared artifact locations and governing canonical names, header versions and Hub commit; preserve intentional pins until an authorized update. No universal `/docs` landing path. |',['FC-008','RUL-14'])
hit(331,'- [ ] Approved stack reconciled with current Recon evidence; any conflict has an attributable Director ruling',['FC-005','RUL-12'])
hit(472,'3. **Error-message leak in a catch block:** report the finding with the certified severity and obtain an authorized repair assignment. Replace unsafe responses/logging only within that assignment; QA does not silently implement the fix.',['FC-021','FC-024','RUL-12'])
hit(535,'1. The module’s mandatory `ACCEPTANCE_SPEC.md`,',['FC-025'])
hit(198,'- Privileged account creation and role promotion require the approved project authority and verified kit path; do not treat a silent downgrade or manual console workaround as successful creation.',['FC-001','FC-036'])
hit(642,'- Historical Mark IV role-from-metadata behavior is unverified for safe public signup. Do not adopt it: privileged assignment must be inaccessible to client-controlled input and proven against pinned trigger/caller source.',['FC-001','FC-034'])
hit(679,'Verify the pinned trigger’s name field and role input contract. Public user metadata must never grant privilege; protected admin creation alone does not prove a shared trigger safe.',['FC-001','FC-034','FC-038'])
hit(730,'| Middleware | Verify the pinned kit entry and session helper | Session refresh; no universal filename or cookie contract | NO |',['FC-042'])
hit(731,'**Session/cookie architecture:** verify the pinned server and browser clients, cookie adapters, attributes and refresh behavior together. Neither blanket `httpOnly: true` nor blanket `httpOnly: false` is approved here. Do not change attributes without a compatible verified session contract and tests.',['FC-042'])
hit(689,'- Inspect the pinned page-guard export, arguments and return value; no callable signature is asserted here.',['FC-041'])
hit(690,'**Server component protection:** use the verified kit guard at the approved boundary. Confirm its export, arguments, return shape and unauthorized behavior before writing the call.',['FC-041'])
hit(717,'Do not assume the page guard returns `{ user, role }`; verify the pinned implementation and callers before destructuring its result.',['FC-041'])
# Remaining active code fences invoking an unverified guard are withdrawn completely.
for path in [K,auth,u]:
 for mat in list(re.finditer(r'```[^\n]*\n[\s\S]*?```',files[path])):
  block=mat.group()
  if re.search(r'\b(?:await\s+)?protectPage\s*\(',block):
   change(path,block,'**Guard-call example withdrawn pending pinned-kit verification.** '+P['41'],['FC-041'])
for i in [742,743,745,747]:hit(i,hits[i]['quote'].replace('`src/middleware.ts`','the verified framework-version entry').replace('(src/middleware.ts)','(verified entry for the installed framework)').replace('└── middleware.ts                   # Next.js middleware','└── <verified-session-entry>        # framework-version-specific entry'),['FC-042'])
hit(822,'| Durable asynchronous work | Required webhook follow-up | Acknowledge only after verified durable acceptance; no unawaited fire-and-forget promise |',['FC-059'])
hit(809,'**Customer identity:** use the project-approved ownership and storage contract. Do not prescribe universal storage on a subscription row; universal subscription-schema design is deferred.',['FC-055','RUL-11'])
# References to removed payment/hydration implementations cannot remain runnable dependants.
for path,heading,ns in [(com,'## 6. Cart Management',[47,50]),(com,'## 7. Pricing Calculations',[51,60]),(com,'### Coupon Input Component',[67,68])]:
 if heading+'\n' in files[path]:withdraw(path,heading,ns)
for path in [com,state,stripe]:
 for mat in list(re.finditer(r'```(?:typescript|tsx?|javascript)\n[\s\S]*?```',files[path])):
  block=mat.group()
  if any(t in block for t in ['calculateCouponDiscount(', 'useCheckoutStore(', 'hasHydrated','stripe.billingPortal.sessions.create']):
   change(path,block,'**Dependent executable example withdrawn.** Use a project-approved state/payment contract with explicit hydration errors, server-authoritative pricing, authenticated ownership and recovery. The removed example’s missing contract is still tracked; no universal quote/subscription schema is introduced.',['FC-047','FC-055','FC-067','FC-068','RUL-11'])
# No active error-swallowing or raw upstream-error recipes under the supported corrections.
for path in [S,api,'04_REFERENCE_MANUALS/APP_ARCHITECTURE_MANUAL.md',auth]:
 for mat in list(re.finditer(r'```(?:typescript|tsx?|javascript)\n[\s\S]*?```',files[path])):
  block=mat.group()
  if ('error.message' in block or 'console.error(' in block) and not ('WRONG' in block or '❌' in block):
   change(path,block,'**Executable error-handling example withdrawn.** '+P['21']+' '+P['63']+' '+P['66']+' Implement only against a verified project service contract; distinguish empty success from failure and redact internal/upstream detail from public responses and logs.',['FC-021','FC-063','FC-066','RUL-11'])
# Rail numbers are verified component facts, not global policy; replace conflicting recipes.
for i in [195,922,937,955,956,957]:
 hit(i,'- **Responsive rail:** determine the fit breakpoint from the pinned component and actual content. Below that breakpoint supply a reachable, keyboard-accessible drawer trigger; no vanished or untriggered sidebar. Verify on both sides of the breakpoint and at 375px. Do not infer a universal `md`, `lg` or `xl` rail rule.',['FC-071','FC-072'])
for i in [537,917,940,952,953]:
 hit(i,'- Historical kit rail dimensions/breakpoints require verification against the pinned shell implementation; no current kit value is certified here. Verify trigger, dismissal and layout on both sides of the actual fit breakpoint.',['FC-072'])
for i in [962,963,964,970]:hit(i,'Use the appropriate semantic surface, foreground and role tokens; confirm contrast in every supported mode. Numbered palette values describe historical kit debt, not an approved component recipe.',['FC-073'])
# Mandatory QAM is structural, in each current authoring tree and checklist.
for anchor in ['├── README.md             ← operator\'s setup guide','├── AGENTS.md                          # Codex CLI pointer']:
 if anchor in files[F]:change(F,anchor,anchor+'\n├── ACCEPTANCE_SPEC.md    # approved acceptance contract; Engineer factual handoff\n├── QAM/                  # Architect-prepared module QAM from accepted templates\n│   ├── CLAUDE.md         # QA Executor entry → QAM_ENTRY.md\n│   ├── AGENTS.md         # same QA Executor routing\n│   └── QAM_ENTRY.md      # module-specific QA instructions and required records',['RUL-01','FC-025','FC-026'])
hit(103,'- [ ] Create module-specific `QAM/` from the accepted canonical templates, both QA entry routes and all required records; prepare `ACCEPTANCE_SPEC.md`; create `_project/`, `_design/`, `_extraction/`, `skills/stark-frontend-first/`, `playbook/RETROSPECTIVES/` and `verification/`.',['RUL-01','FC-025'])
hit(545,'Small modules may fold brief and contract into the manager, but matching entry routes, acceptance spec, prepared module QAM and retrospective remain mandatory. Delivery is one module ZIP plus a file tree; Coordinator notes remain outside it.',['RUL-01'])
# Landing paths below are module conventions, not universal locations for governing docs.
hit(1180,'- Governing starter-kit handbook: use its recorded canonical name, header version and Hub commit at the project-declared location; verify the referenced kit revision.',['FC-003','FC-009','RUL-14'])
hit(1181,'- Governing component registry: use its recorded canonical name, header version and Hub commit at the project-declared location.',['FC-003','FC-009','RUL-14'])
hit(1146,'**Architect uses this to:** declare and verify compile/test exclusions, build/deploy input exclusions and inspection of the actual produced artifact. A non-compiled extension prevents compilation only; it does not prove deployment exclusion. Keep module/QAM/evidence records under `agent_docs/` and preserve required evidence.',['RUL-03'])


# Replace complete dependent cart/pricing recipes; keep headings as withdrawal records.
for heading,ns in [('## 6. Cart Logic',[47,50]),('## 7. Pricing & Totals',[51,60]),('### Coupon Input UI',[67,68])]:
 if heading+'\n' in files[com]:withdraw(com,heading,ns)
# Normalize active-only Git-zero phrases; historical version rows are preserved.
for path in [S,E,F,'03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md','03_BUILD_METHODOLOGY/FEAT_PLAYBOOK.md','03_BUILD_METHODOLOGY/BUG_FIX_PLAYBOOK.md']:
 before=files[path];lines=before.splitlines(True)
 for j,line in enumerate(lines):
  if re.match(r'^\| \d+\.',line):continue
  line=line.replace('zero git','no Git mutations').replace('git-zero/cloud-zero','Director-only Git mutations / existing context-specific cloud restrictions').replace('git-zero','Director-only Git mutations')
  lines[j]=line
 after=''.join(lines)
 if after!=before:change(path,before,after,['FC-014','RUL-12'])
# Authority propagation includes boot sequences, quotations used as active maxims, and recon prompts.
for path in [A,E,F,'02_PIPELINE_AGENTS/RECON_QUESTIONNAIRE.md']:
 s=files[path]
 for block in list(s.split('\n\n')):
  if 'filesystem wins' not in block:continue
  if re.match(r'^\| \d',block):continue
  new=re.sub(r'Where any doc and the filesystem disagree, the\s+filesystem wins(?: — every time)?\.?','Disk establishes implementation facts; approved briefs govern scope and governing documents control their subjects. Route genuine conflicts to the Director.',block,flags=re.I)
  new=re.sub(r'Where the handbook and the filesystem disagree, the filesystem wins — every time\.','Disk establishes implementation facts; report drift without changing approved scope or requirements.',new)
  new=new.replace('the filesystem wins and the drift gets recorded','record the factual drift and route any requirements conflict to the Director')
  new=new.replace('the kit handbook (and APP_BRIEF, and every doc) is ASPIRATIONAL, not contractual','handbook implementation claims require recon; the approved APP_BRIEF remains the scope contract')
  if new!=block:change(path,block,new,['FC-005','FC-014','RUL-12'])
section(F,'### The Roles','''```text
Current recon and approved brief / extraction evidence
→ Architect authors DATA_CONTRACT before Design
→ Designer authors UI_SPEC, tokens and the complete visual package
→ Architect reconciles assembly, prepares module-specific QAM and entry routing
→ Director approves package and releases Engineering
→ Engineer builds, verifies and fills factual handoff
→ Director commits/pushes the numbered engineering candidate
→ QA branch starts at that exact candidate; Q1 recon and independent plan
→ QA Lead approves; Director releases Q2 execution
→ Authorized repair/retest on the same QA branch as needed
→ QA Lead product verdict; required cleanup and acceptance
→ Architect closeout; bounded Engineering closeout; Director final Git actions
```''',['FC-004','FC-017','FC-027','RUL-01','RUL-02','RUL-03','RUL-09'])
change(F,'The Architect authors files in this order. Each step gets the previous step\'s outputs as inputs.','The Architect coordinates this authoring order; each artifact retains its assigned owner. Each step consumes the previous step’s approved outputs.',['RUL-09'])
change(F,'5. Author _project/UI_SPEC.md THIRD (screens built from data contract)','5. Designer authors _project/UI_SPEC.md THIRD from the approved DATA_CONTRACT; Architect reconciles',['FC-017','RUL-09'])
paragraph(F,'Designer and Extractor can work in parallel','Extraction and evidence gathering may run in parallel with visual research. The Architect prepares DATA_CONTRACT from the approved brief and available verified extraction evidence before Design. The Designer authors UI_SPEC and the complete visual package; the Architect reconciles the assembly and prepares QAM before Engineering release.',['FC-017','FC-027','RUL-09'])
change(F,'2. [The Four-Role Factory Pattern](#2-the-four-role-factory-pattern)','2. [The Factory Roles and Delivery Pattern](#2-the-factory-roles-and-delivery-pattern)',['FC-004'])
for old,new in [('Surface any gaps or questions during the run. Plan Mode before each document.','Surface gaps or questions during the run. Plan before release, then execute continuously within the released extraction assignment; stop for concrete blockers or authority changes.'),("- **Don't skip Plan Mode** — Claudy still plans before each doc",'- **Plan before release** — execute the approved assignment continuously, including checks and reporting; stop for concrete blockers, authority changes or required independent verdicts.')]:
 if old in files[F]:change(F,old,new,['RUL-15'])
# Canonical ownership does not turn historical visual references into a new author.
change(A,'**The Architect does NOT author an APP_BRIEF, DATA_CONTRACT, UI_SPEC, `_project/CLAUDE.md`, or any FFM file against a repo until a current `stark-recon` Recon Report exists for that repo\'s actual state.**','**Before preparing or reconciling any project artifact, the Architect requires a current Recon Report for the actual repository state. The Architect owns APP_BRIEF, DATA_CONTRACT and assembly; the Designer owns UI_SPEC.**',['FC-017','RUL-09'])
# The project-specific fixture remains an example, not a requirement to persist contact data.
change(T,'expect(JSON.parse(stored!).state.checkoutData.coupon.code).toBe(expectedCode); // ground truth','expect(JSON.parse(stored!).state.couponCode).toBe(expectedCode); // approved non-sensitive project fixture only',['FC-040','RUL-13'])

# Persist exact ordered proposals and rendered review copies, never canonical files.
out=R/'PROPOSED_CONTENT';out.mkdir(exist_ok=True);diffs=[];manifest=[]
for path,new in sorted(files.items()):
 if new==original[path]:continue
 dest=out/path;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(new)
 diffs.extend(difflib.unified_diff(original[path].splitlines(True),new.splitlines(True),fromfile='BASE/'+path,tofile='PROPOSED/'+path))
 manifest.append(dict(path=path,base_sha256=hashlib.sha256(original[path].encode()).hexdigest(),proposed_sha256=hashlib.sha256(new.encode()).hexdigest(),status='CONTENT PROPOSAL ONLY; version/index integration and full semantic review pending'))
(R/'SELECTED_EXACT_EDITS.json').write_text(json.dumps(ed,indent=2)+'\n');(R/'SELECTED_CONTENT_DIFF.patch').write_text(''.join(diffs));(R/'SELECTED_CONTENT_INDEX.json').write_text(json.dumps(manifest,indent=2)+'\n')
print('Saved',len(ed),'ordered exact proposals across',len(manifest),'documents; original canonical files unchanged.')
