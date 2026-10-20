exec(compile(open('/tmp/qa_checks.py').read().split('idx=json.loads')[0],'/tmp/qa_checks.py','exec'))
# Independent judgment annotations, authored after reading candidate containers.
hits=json.loads((E/'RAW/propagation_hits.json').read_text())
for x in hits:
 p=x['path'];t=x['text'];n=x['line'];term=x['term'];x['disposition']='RETAIN';x['context']='active'
 if term=='fetchProducts':
  if 'APP_ARCHITECTURE' in p or ('STATE_MANAGEMENT' in p and n in [810,826,869,873]):x['disposition']='FAIL';x['rationale']='RV2-F01: same named productServices operation lacks an explicit alternative contract; array consumer does not discriminate the declared typed outcome. See whole containers in MANUAL_READS.'
  elif 'STATE_MANAGEMENT' in p and n==801:x['context']='negated';x['rationale']='Inside explicitly BAD network-in-store example; not positive guidance.'
  elif n in [183,985,1179,241]:x['rationale']='Naming/layer responsibility example only; no result shape or executable caller.'
  elif 'ByIds' in t:x['rationale']='Distinct function with ids:number[] parameter and explicit Promise<Product[]> signature; no conflation with no-argument fetchProducts.'
  else:x['rationale']='API example explicitly identifies normalization array, discriminated typed outcome, or independent ISR raw JSON; implementation/caller agrees within its labeled container.'
 elif term=='raw contact':x['rationale']='Explicit no-default-contact-persistence rule; STATE partialize returns no contact fields and checkout template is withdrawn. Approved exceptions require declared fields/purpose/retention/owner and account invalidation.'
 elif term=='persist':
  if 'STATE_MANAGEMENT' in p:x['rationale']='State/persistence guidance inspected in its section: generic items/preferences/storage adapter or restriction/reset policy, not a raw-contact persistence recipe. Empty checkout partialize excludes addresses; see MANUAL_READS.'
  elif any(k in t.lower() for k in ['raw contact','personal-data','authorization authority','role state','role goes','role state']):x['rationale']='Restriction on persistent personal/authorization state, not permission to persist raw contact.'
  elif 'Executable error-handling example withdrawn' in t or 'trust-boundary matrix' in t:x['rationale']='Server-effect verification and safe-error containment; persistence refers to recorded backend outcome, not browser contact storage.'
  elif 'ECOMMERCE' in p or 'DATABASE' in p or 'STRIPE' in p:x['rationale']='Backend transaction/session/cart lifecycle persistence; no browser raw-contact storage instruction in the matched container.'
  elif 'AUTH_MANUAL' in p:x['rationale']='Session lifecycle or explicit authorization restriction; safe cookies/session persistence is distinct from raw contact fields.'
  else:x['rationale']='General persistence/checklist, historical failure narrative, durable evidence or persistent visual UI; no contact-data write or default-contact authorization.'
 else:x['rationale']='Inspected in full candidate container; no stale operative assertion.'
 if x['history']:x['context']='historical'
with (E/'PROPAGATION.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['term','path','line','text','heading','history','fence','disposition','context','rationale'],delimiter='\t');w.writeheader();w.writerows(hits)
save('RAW/propagation_summary.json',dict(scope='36 live tier/root docs + four workflow Markdown + four SVG, including code fences and Version History',terms={t:sum(x['term']==t for x in hits) for t in ['different author','filesystem wins','disk wins','hands off to Operations','seedSubscription','supabaseAdmin','appropriate for:','fetchProducts','raw contact','persist']},hits=len(hits),undispositioned=0))
# Ownership classification anchored to real history boundary and explicit negations.
own=json.loads((E/'RAW/ownership_hits.json').read_text())
for x in own:
 lines=(C/x['path']).read_text().splitlines();pre='\n'.join(lines[:x['line']]);hist=bool(re.search(r'^#{1,6} .*Version History',pre,re.M));x['context']='historical' if hist or (x['path']=='CHANGELOG.md' and '2026-08-10' in x['text']) else 'active';x['disposition']='RETAIN';x['rationale']='Historical version entry preserves former policy, not live authorship.' if x['context']=='historical' else 'Approved artifact, consumption, assembly or evidence reference; does not transfer Architect DATA_CONTRACT / Designer UI_SPEC ownership. Acceptance handoff finalization is constrained by pre-implementation Architect criteria (BIM §8).'
 if 'older required-FILE_TREE' in x['text']:x['context']='negated';x['rationale']='Explicitly rejects old required-FILE_TREE rule; optional structure remains declared.'
save('RAW/ownership_dispositions.json',own)
patterns=['Engineer.{0,40}authors?[^\n]*DATA_CONTRACT','Architect.{0,25}drafts?[^\n]*UI_SPEC','Designer revises','FILE_TREE[^\n]*source.of.truth','Engineer[^\n]*produces[^\n]*FILE_TREE',"The Engineer.s full output list",'different author','filesystem wins','disk wins'];stale=[]
for p in json.loads((E/'RAW/live_scope.json').read_text()):
 text=(C/p).read_text()
 for pat in patterns:
  for m in re.finditer(pat,text,re.I):stale.append(dict(path=p,line=text[:m.start()].count('\n')+1,pattern=pat,text=m.group()))
save('RAW/stale_assertion_sweep.json',stale)
# Each withdrawal row freshly graded; original packet is a locator only.
reason={
'FC-001':'Kit auth is consumed, not rebuilt; SFP and kit guard text restrict generic examples. No amendment adds an auth construction path.',
'FC-022':'Both seeding/admin-client fences removed; setup and construction require approved test-project allowlist AND authorized identity, failing closed. Preserved prose describes test intent under that guard, not runnable unguarded setup.',
'FC-030':'Fixture producer and consumer use one count field; missing required role is BLOCKED. Its complete section is unchanged except shifted lines.',
'FC-033':'Role authority remains server table; metadata-authorized privileged routes withdrawn. Current-role and operation-local authorization required.',
'FC-034':'Public signup forces member and provider path rejects elevated public role keys; protected channel is separate.',
'FC-035':'Server guard/first-render identity rule preserved; client HOC and post-mount identity recipes remain withdrawn.',
'FC-038':'DATABASE bypass section now conditions BOTH construction comments and background/admin operations on independent elevated-operation authorization; AUTH rejects default API-route bypass.',
'FC-039':'Role resolver authority separate from profile mirrors; metadata never grants privilege. No revised executable surface reintroduces it.',
'FC-041':'Kit signatures and role transport explicitly require pinned evidence; replacement remains open and no guessed executable kit guard is introduced.',
'FC-042':'Cookie architecture requires verified kit; HTTPS/Secure preserved without unverified universal HttpOnly claims.',
'FC-045':'Timestamp-only cursor recipe is withdrawn, including dependent cursor semantics; stable composite ordering is required in preserved context.',
'FC-047':'Business reset and hydration readiness remain separate; signout/account transition invalidates stores even on remote failure; checkout executable template withdrawn.',
'FC-050':'Payment state is derived from verified server evidence, never caller-selected; no changed commerce code reintroduces browser paid mutation.',
'FC-051':'Non-webhook mutation independently authorizes actor/target and state transition; prior unsafe recipe remains withdrawn.',
'FC-052':'Ordering/reconciliation distinct from inbound deduplication; late old-subscription event cannot overwrite replacement.',
'FC-053':'Payment evidence bound to stored order/attempt, amount/currency; unsafe executable payment mutation remains withdrawn.',
'FC-054':'Mirror convergence and missing mapping repair remain explicit; withdrawn event recipes not reintroduced.',
'FC-055':'Subscription schema/customer/bootstrap remains deferred under approved project schema; owner reads/server writes preserved.',
'FC-056':'Stable provider event ID, atomic claim and recoverable states required; no random fallback recipe remains introduced.',
'FC-057':'Unsafe webhook executable recipe withdrawn; pre-acceptance failure and post-acceptance recovery distinguished in surrounding invariant.',
'FC-058':'Raw request body exactly once; provider-specific signature verification before parsing; incompatible schemes not combined.',
'FC-059':'Authoritative retrieval/freshness/legal transitions remain required independently of deduplication.',
'FC-060':'Caller cannot choose payment-derived state; server-side binding and operation authorization preserved.',
'FC-062':'Late/stale/missing-map convergence handled by declared reconciliation; no unsafe recipe restored.',
'FC-064':'Typed failure outcomes and approved degradation policy preserved. Repaired API caller narrows success before items; no entitlement absence inferred from failure.',
'FC-066':'FAIL RV2-F01: API examples are now labeled, but APP_ARCHITECTURE and STATE retain unlabeled same-name array callers; see exact service/consumer traces.',
'FC-067':'Fixed-product discounts require eligible line quantities and server pricing; flat subtotal recipe remains withdrawn.',
'FC-068':'Server loads prices and validates quantities/shipping/coupon/tax; client totals are display only. Quote-storage design remains deferred, not falsely closed.',
'FC-071':'Layout recipe withdrawn; pinned responsive shell verification required; no new breakpoint/shell implementation.',
'FC-072':'Shell/rail/drawer authority and viewport behavior preserved; no kit-root change or duplicate shell introduced.',
'FC-076':'Shortened Button installation recipe withdrawn; consume verified kit variants/asChild and preserve Link composition.'}
rows=json.loads((E/'RAW/withdrawal_candidate_passages.json').read_text());out=[]
for row in rows:
 out.append(dict(fc=row['fc'],status='FAIL' if row['fc']=='FC-066' else 'PASS',rationale=reason[row['fc']],finding_ids=['RV2-F01'] if row['fc']=='FC-066' else [],evidence=row['evidence'],boundary='Containment only; no production replacement completion claimed.',regression_basis='Full parent/candidate delta is the approved 29 edits. Remaining invariant and executable sections preserved; changed overlaps are FC-022/038/066 plus contact policy/history. See canonical.diff and edit_delta_accounting.'))
save('WITHDRAWAL_ROWS.json',out)
# quote actual candidate spans, not historical line numbers
manual=['# Independent manual reads — candidate '+cfg['candidate'],'','Seat: Codex QA Executor; fresh conversation. Quotes below are from the pinned git archive. Searches are locators, not semantic proof. Full candidate documents are in RAW/candidate/.','']
def q(p,a,b):
 lines=(C/p).read_text().splitlines();manual.append('\n### '+p+':'+str(a)+'\n\n```text\n'+'\n'.join(f'{i}: {lines[i-1]}' for i in range(a,min(b,len(lines))+1))+'\n```\n')
manual.append('## R1 ownership\nArchitect authors DATA_CONTRACT in conversion and greenfield; Designer authors UI_SPEC; Architect reconciles. Conversion uses Brain Drain pre-authorship; greenfield uses approved APP_BRIEF before Design. Router remains. E373–E380 each occurs once, old spans absent. FILE_TREE remains optional. Historical HANDOFF 1.1 statement is retained only in its Version History. BIM Engineer-finalized wording is limited by §8 to factual synchronization of pre-approved criteria, not authorship of success conditions. Broad map-query hits include negative examples, artifact mentions, historical versions and unrelated OUTSIDE/LOCKED vocabulary; full dispositions are recorded.')
for p,a,b in [('02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md',133,190),('02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md',734,738),('01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md',51,56),('02_PIPELINE_AGENTS/ARCHITECT_PLAYBOOK.md',80,88),('02_PIPELINE_AGENTS/DESIGNER_PLAYBOOK.md',62,72),('02_PIPELINE_AGENTS/HANDOFF_PACKAGE_PLAYBOOK.md',251,269),('03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md',375,405),('03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md',122,140)]:q(p,a,b)
manual.append('## R2 handoff\nThe lead instruction gates Operations on QA Lead certification and Director release. The eight-entry tree retains original six entries and adds Architect ACCEPTANCE_SPEC and QAM with engineering handoff, plan, results and certificate. The tree title describes the eventual receiving destination; it does not override the preceding explicit route through independent QA. What Operations Needs and Verbal Brief are byte-identical to parent.')
for p,a,b in [('02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md',1381,1444),('03_BUILD_METHODOLOGY/QAM_PLAYBOOK.md',35,49),('03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md',27,42)]:q(p,a,b)
manual.append('## R3 authority\nThree kit-diagram lines preserve diagram flow and distinguish implementation facts from governing requirements. No filesystem-wins/disk-wins hits in full live scope including fences/SVG. Existing aligned sites remain unchanged; a fact on disk cannot silently amend requirements.')
q('02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md',249,262)
manual.append('## R4 withdrawals and contract trace\nFC-022: guard applies to setup, seeding and client construction, with fail-closed identity/target checks. Both dangerous executable fences are absent. Remaining prose about synthetic Stripe rows and dotenv describes test intent/dependency under the guard; it is not evidence of production replacement closure. FC-038: route location alone never authorizes bypass; both construction comments constrain capability acquisition. The other 28 rows retain their mapped invariant and dependent executable surfaces, except the explicitly reviewed overlap with these repairs and contact policy. WITHDRAWAL_ROWS.json contains all 31 independent grades and candidate quotes.')
for p,a,b in [('03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md',881,908),('04_REFERENCE_MANUALS/DATABASE_MANUAL.md',418,436),('04_REFERENCE_MANUALS/AUTH_MANUAL.md',1308,1315)]:q(p,a,b)
manual.append('### RV2-F01 — HIGH — FC-066 remains inconsistent\nAPI §3 establishes one named service contract, allowing only explicitly labeled alternatives. Its normalization array example, typed-outcome caller and ISR raw-JSON example now have those labels. The typed caller checks status before items and uses an explicit public-catalog degradation policy. fetchProductsByIds is a distinct operation with an ids parameter and explicit array return.\n\nAPP_ARCHITECTURE §5 imports fetchProducts from @/services/productServices and passes its entire result to ProductList; the streaming example repeats it. Neither container declares an alternative contract. STATE §7 calls the same service and passes its result as initialProducts to a Props field explicitly typed Product[]. Its preceding service returns untyped response.json() without declaring the endpoint wire shape or labeling itself an alternative to API §3. A GOOD service/store separation label is not a return-contract label. Against the declared typed-outcome service, the caller supplies an outcome object where an array is required and never narrows success. Choosing the array normalization or raw JSON variant implicitly would still violate the explicit-alternative requirement. This is an unresolved in-scope contract contradiction, not a request to broaden implementation or reopen FU-1/FU-2.')
for p,a,b in [('04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md',166,174),('04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md',613,622),('04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md',785,815),('04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md',856,869),('04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md',942,955),('04_REFERENCE_MANUALS/APP_ARCHITECTURE_MANUAL.md',495,520),('04_REFERENCE_MANUALS/APP_ARCHITECTURE_MANUAL.md',589,616),('04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md',793,829),('04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md',863,903)]:q(p,a,b)
manual.append('## R5 browser contact persistence\nAll four named manuals express the default. STATE partialize returns an empty object, so billingAddress/shippingAddress initialization (and stale generic Persisted comment) does not write either field to storage. The generic items store, storage adapters, preferences and Form drafts row do not supply a raw-contact recipe; explicit contact restrictions govern. STATE §4 comment supplies purpose/owner, §6 supplies retention/scope and signout/account reset, coherent with the three added sentences. No contact field is added to a storage write. The complete ten-term sweep includes 155 hits; duplicate term matches are separate rows. Seven fetchProducts hits are flagged for R4; none are undispositioned.')
for p,a,b in [('03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md',416,431),('04_REFERENCE_MANUALS/AUTH_MANUAL.md',1118,1128),('04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md',201,207),('04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md',499,538),('04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md',779,787)]:q(p,a,b)
manual.append('## R7 metadata\nSix header lines are unchanged and match MANIFEST version/date/status cells; landing date remains 2026-10-18. Each document amends one existing history row with the same QA-repair clause. CHANGELOG retains 39 contiguous run rows, six amended, within Ongoing entries before separator/footer. No table column/order/header changes; no new history row or section. Exact counts and headers in RAW/metadata.json.')
q('CHANGELOG.md',34,81)
manual.append('## R10 pending transitions\nAll 12 exact old spans occur at their specified counts on nine unchanged paths. No new span occurs. Draft playbook headers and MANIFEST statuses agree; template README still says proposed, and each workflow is Proposed — pending verified publication. Old proposal approval-pending provenance is not revoked by a current additive approval. Product verdict/cleanup/release acceptance is not supplied by this retest.')
for x in json.loads((E/'RAW/transitions.json').read_text()):q(x['path'],x['line'],x['line'])
(E/'MANUAL_READS.md').write_text('\n'.join(manual)+'\n')
# Classify generator additions explicitly, without executing them.
scope=json.loads((E/'RAW/scope.json').read_text())
for x in scope:
 if '/scratchpad/generators/cody_amend_v2' in x['path']:x['purpose']='Additive engineering proposal generator/verification source required by repair assignment §3; inspected for identity/purpose, never executed or used as independent QA suite.'
save('RAW/scope.json',scope)
# Clarify whitespace copied complete approved files versus new canonical whitespace.
x=json.loads((E/'RAW/whitespace_classification.json').read_text())
for a in x:
 if '/PROPOSED_CONTENT/' in a['path']:a['category']='Unchanged whitespace within exact approved full-file copy; seven-path canonical diff has zero warnings.'
save('RAW/whitespace_classification.json',x)
(E/'scripts/judgments.py').write_bytes(Path(__file__).read_bytes());print('judgments written; withdrawal',len(out),'propagation',len(hits),'stale',stale)
