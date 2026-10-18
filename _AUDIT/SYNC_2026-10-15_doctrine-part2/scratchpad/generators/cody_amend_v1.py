"""AMENDED-v1 generator — ownership amendment on top of the Gate 2-frozen map.
Pass 1 (2026-10-17 13:5x): D-1/D-2 (E373/E374). Pass 2 (2026-10-17 14:xx, Jarvis resolves OBS-1 into this same draft):
OBS-1 rows + one ownership propagation sweep resolving direct contradictions of the approved rule (E375–E380).

Run from the repository root. Reads the frozen run records read-only and writes ONLY under
<run>/AMENDED_V1/. It never touches PROPOSED_CONTENT/, SELECTED_EXACT_EDITS.json,
EXECUTION_PROPOSAL_INDEX.json, UPDATE_MAP.md, Fable's files, canonical documents or Git.
Deterministic: no timestamps in its outputs (verification evidence carries the time).
"""
from pathlib import Path
import json, hashlib, difflib, re

R = Path('_AUDIT/SYNC_2026-10-15_doctrine-part2'); O = R / 'PROPOSED_CONTENT'; A = R / 'AMENDED_V1'
BASE = R / 'BASELINE_CONTENT'
sha = lambda b: hashlib.sha256(b if isinstance(b, bytes) else b.encode()).hexdigest()
B = '01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md'; E = '02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md'

# --- exact Architect-recommended spans (Tony's 2026-10-17 brief) ---------------------------------
D1_OLD = "## 📋 ENGINEER AGENT: WHAT IT PRODUCES\n\nThe Engineer's full output list:\n"
D1_NEW = ("## 📋 ENGINEERING PACKAGE: APPROVED CONTRACT ARTIFACTS\n\n"
          "The Architect assembles the approved contract artifacts below for the Engineer to implement. "
          "DATA_CONTRACT is authored before Design; FILE_TREE is optional when implementation structure "
          "and boundaries are otherwise explicit.\n")
D2_OLD = "> **Author:** Engineer Agent"
D2_NEW = "> **Author:** Architect"
AUTH = ('Architect-recommended replacement text conveyed in Tony\'s 2026-10-17 brief "CODY — PREPARE ONE BOUNDED MAP '
        'AMENDMENT"; resolves FABLE_CORRECTION_CONFIRMATION_2026-10-17.md §5 D-1/D-2 (AC6(c)/(d)); applies existing '
        'approved policy RUL-09 (DIRECTOR_RULINGS_2026-10-16.md); no new policy.')
AUTH2 = ('Jarvis (Architect) resolution of OBS-1 conveyed in Tony\'s 2026-10-17 brief "CODY — COMPLETE THE OWNERSHIP CORRECTION IN '
         'ONE PASS": fold OBS-1 into draft AMENDED-v1 with the exact replacement rows; "The Architect owns the approved contract; '
         'Engineering implements it." Applies existing approved policy RUL-09; no new policy; no AMENDED-v2.')
AUTH3 = ('Same brief: "complete ONE ownership propagation sweep across the selected live documents … Resolve direct contradictions '
         'of that approved rule in this same draft amendment." Engineer-worded under the Architect\'s rule (Architect owns the approved '
         'contract; Engineering implements it); wording for Architect/Fable confirmation.')
A_PATH = '02_PIPELINE_AGENTS/ARCHITECT_PLAYBOOK.md'
LBL = 'ENGINEER-PROPOSED AMENDED-v1 ownership amendment'
amend = [
    dict(path=B, old=D1_OLD, new=D1_NEW, ids=['D-1', 'MC-07', 'RUL-09', 'FC-008', 'FC-017', 'FC-027'], label=LBL, amendment='AMENDED-v1', item='D-1', authority=AUTH),
    dict(path=E, old=D2_OLD, new=D2_NEW, ids=['D-2', 'MC-07', 'RUL-09', 'FC-027'], label=LBL, amendment='AMENDED-v1', item='D-2', authority=AUTH),
    # pass 2 — OBS-1 (Jarvis's exact rows)
    dict(path=A_PATH, old='| Define data schemas | Engineer Agent |', new='| Implement approved data schemas as migrations and models | Engineer Agent |',
         ids=['OBS-1', 'MC-07', 'RUL-09', 'FC-017', 'FC-027'], label=LBL, amendment='AMENDED-v1', item='OBS-1a', authority=AUTH2),
    dict(path=A_PATH, old='| Define API contracts | Engineer Agent |', new='| Implement approved API contracts | Engineer Agent |',
         ids=['OBS-1', 'MC-07', 'RUL-09', 'FC-017', 'FC-027'], label=LBL, amendment='AMENDED-v1', item='OBS-1b', authority=AUTH2),
    # pass 2 — propagation sweep: direct contradictions of the approved rule in the selected live documents
    dict(path=B, old='| `DB_SCHEMA.md` | Database tables, relationships, indexes | Engineer |', new='| `DB_SCHEMA.md` | Database tables, relationships, indexes | Architect |',
         ids=['P-1', 'OBS-1', 'MC-07', 'RUL-09', 'FC-008', 'FC-017', 'FC-027'], label=LBL, amendment='AMENDED-v1', item='P-1', authority=AUTH3,
         evidence='Blueprint "Phase 3: ENGINEERING (Architect Contract Assembly)" owner table; E373 states the Architect assembles the approved contract artifacts below (DATA_CONTRACT, DB_SCHEMA, API_SPEC, FILE_TREE); an Engineer owner cell for a contract artifact contradicts the rule.'),
    dict(path=B, old='| `API_SPEC.md` | Endpoints, methods, auth, error codes | Engineer |', new='| `API_SPEC.md` | Endpoints, methods, auth, error codes | Architect |',
         ids=['P-2', 'OBS-1', 'MC-07', 'RUL-09', 'FC-008', 'FC-017', 'FC-027'], label=LBL, amendment='AMENDED-v1', item='P-2', authority=AUTH3,
         evidence='Same owner table as P-1; API contract ownership.'),
    dict(path=E, old='| **Data Contracts** | Define schemas, APIs, file formats |', new='| **Data Contracts** | Implement the approved schemas, APIs and file formats; contract changes return to the Architect |',
         ids=['P-3', 'OBS-1', 'MC-07', 'RUL-09', 'FC-027'], label=LBL, amendment='AMENDED-v1', item='P-3', authority=AUTH3,
         evidence='ENGINEER_PLAYBOOK §"Core Responsibilities" role table assigns "Define schemas, APIs" to the Engineer; contradicts E373/E374/OBS-1 and the playbook\'s own §"DATA_CONTRACT Ownership" and §12 note. Return-to-Architect clause mirrors Blueprint FAQ row ("contract changes return to the Architect and Director").'),
    dict(path=E, old='- Database schema design (Supabase/Firebase)\n', new='- Implement approved database schemas as migrations and models (Supabase/Firebase)\n',
         ids=['P-4', 'OBS-1', 'MC-07', 'RUL-09', 'FC-027'], label=LBL, amendment='AMENDED-v1', item='P-4', authority=AUTH3,
         evidence='ENGINEER_PLAYBOOK §13 "Full-Stack Web App → Engineer Focus" bullet assigns schema *design* to the Engineer; reworded with Jarvis\'s OBS-1 phrase. The sibling bullets ("API route implementation", Backend Bundle "API contract implementation") already state implementation and are retained.'),
]

# --- frozen inputs (read-only) ---------------------------------------------------------------------
frozen_edits = json.loads((R / 'SELECTED_EXACT_EDITS.json').read_text())
frozen_index = json.loads((R / 'EXECUTION_PROPOSAL_INDEX.json').read_text())
frozen_dates = json.loads((R / 'LANDING_DATE_PLAN.json').read_text())
frozen_trace = json.loads((R / 'WORKFLOW_RULING_TRACEABILITY.json').read_text())
frozen_counts = json.loads((R / 'PROPOSAL_COUNTS.json').read_text())
frozen_content_index = json.loads((R / 'SELECTED_CONTENT_INDEX.json').read_text())
assert len(frozen_edits) == 372 and len(frozen_index) == 101

# --- amended proposed bytes: apply each span exactly once to the frozen proposed file --------------
amended = {}
for e in amend:
    s = amended.get(e['path'], (O / e['path']).read_text())
    assert s.count(e['old']) == 1, (e['item'], 'old span must occur exactly once in frozen proposed file')
    assert s.count(e['new']) == 0, (e['item'], 'new text must not pre-exist')
    amended[e['path']] = s.replace(e['old'], e['new'])
# the same spans must also be unique in BASE (they are retained baseline text) and in the content-stage replay
for e in amend:
    assert (BASE / e['path']).read_text().count(e['old']) == 1, (e['item'], 'BASE')

# --- 1. ordered edits: frozen 372 + amendment, sequence continues ----------------------------------
edits = [dict(x) for x in frozen_edits]
for e in amend:
    edits.append(dict(sequence=len(edits) + 1, path=e['path'], old=e['old'], new=e['new'], ids=e['ids'], label=e['label'],
                      amendment=e['amendment'], item=e['item'], authority=e['authority'], **({'evidence': e['evidence']} if 'evidence' in e else {})))
# replay all edits over BASE for the two affected docs → content stage; residual vs amended proposed must equal
# the frozen residual (header bump + history row), proving the amendment is purely the two spans.
def replay(edit_list, path):
    s = (BASE / path).read_text()
    for x in edit_list:
        if x['path'] != path: continue
        assert s.count(x['old']) == 1, (path, x['sequence']); s = s.replace(x['old'], x['new'])
    return s
def residual(stage, final):
    return [l for l in difflib.unified_diff(stage.splitlines(True), final.splitlines(True), n=0) if l[:1] in '+-' and not l.startswith(('+++', '---'))]
for path in amended:
    assert residual(replay(frozen_edits, path), (O / path).read_text()) == residual(replay(edits, path), amended[path]), path

A.mkdir(exist_ok=True)
(A / 'AMENDMENT_V1_EDITS.json').write_text(json.dumps([x for x in edits if x['sequence'] > 372], indent=2, ensure_ascii=False) + '\n')
(A / 'SELECTED_EXACT_EDITS.json').write_text(json.dumps(edits, indent=2) + '\n')
for path, s in amended.items():
    d = A / 'PROPOSED_CONTENT' / path; d.parent.mkdir(parents=True, exist_ok=True); d.write_text(s)

# --- 2. content-stage index/diff (31 docs; only the two hashes move) --------------------------------
content_index = []; cdiff = []
for x in frozen_content_index:
    y = dict(x)
    if x['path'] in amended:
        stage = replay(edits, x['path']); y['proposed_sha256'] = sha(stage); y['amended'] = 'AMENDED-v1'
    content_index.append(y)
for x in content_index:
    base = (BASE / x['path']).read_text(); stage = replay(edits, x['path']); assert sha(stage) == x['proposed_sha256'], x['path']
    cdiff.extend(difflib.unified_diff(base.splitlines(True), stage.splitlines(True), fromfile='BASE/' + x['path'], tofile='PROPOSED/' + x['path']))
(A / 'SELECTED_CONTENT_INDEX.json').write_text(json.dumps(content_index, indent=2) + '\n'); (A / 'SELECTED_CONTENT_DIFF.patch').write_text(''.join(cdiff))

# --- 3. execution index + full patch over the overlay tree (frozen tree with two files replaced) ----
def overlay(rel):
    return amended[rel].encode() if rel in amended else (O / rel).read_bytes()
index = []; diff = []; identities = []
for x in frozen_index:
    b = overlay(x['path']); y = dict(x, proposed_sha256=sha(b), bytes=len(b))
    if x['path'] in amended:
        y['amended'] = 'AMENDED-v1'; identities.append(dict(path=x['path'], before_sha256=x['before_sha256'], gate2_proposed_sha256=x['proposed_sha256'], gate2_bytes=x['bytes'], amended_proposed_sha256=y['proposed_sha256'], amended_bytes=len(b)))
    else:
        assert y['proposed_sha256'] == x['proposed_sha256'] and y['bytes'] == x['bytes'], x['path']
    index.append(y)
    old = (BASE / x['path']).read_bytes() if (BASE / x['path']).exists() else b''
    assert (sha(old) if old else None) == x['before_sha256'], x['path']
    diff.extend(difflib.unified_diff(old.decode().splitlines(True), b.decode().splitlines(True), fromfile=x['path'] if old else '/dev/null', tofile=x['path']))
assert len(index) == 101 and len(identities) == 3
(A / 'EXECUTION_PROPOSAL_INDEX.json').write_text(json.dumps(index, indent=2) + '\n'); (A / 'EXECUTION_PROPOSAL.patch').write_text(''.join(diff))

# --- 4. landing-date binding regenerated over the overlay tree (same rule as cody_mc_records.py) ----
dates = []
for x in frozen_index:
    rel = x['path']
    if not rel.endswith('.md') or rel.startswith('_ARCHIVE/'): continue
    text = overlay(rel).decode()
    for line in text.splitlines():
        header = line.startswith('> **Version:**') and '· **Date:** 2026-10-16' in line
        currentrow = line.startswith('| ') and '2026-10-16' in line and ('Factory DocSet sync:' in line or 'current correction pass:' in line or rel == 'CHANGELOG.md' or rel == 'MANIFEST.md' or '/_workflows/' in rel)
        if header or currentrow:
            new = line.replace('· **Date:** 2026-10-16', '· **Date:** <<ACTUAL_LANDING_DATE>>') if header else line.replace('| 2026-10-16 |', '| <<ACTUAL_LANDING_DATE>> |')
            if new != line: dates.append(dict(path=rel, old=line, new=new, occurrences=text.count(line), type='header' if header else 'current row'))
assert dates == frozen_dates['spans'], 'landing-date spans must be unchanged by a body-only amendment'
(A / 'LANDING_DATE_PLAN.json').write_text(json.dumps({**frozen_dates, 'label': frozen_dates['label'] + '; re-derived over the AMENDED-v1 overlay tree (spans unchanged)', 'spans': dates}, indent=2) + '\n')

# --- 5. traceability: RUL-09 consumers gain the amendment edits; FC rows get a supplement ------------
trace = []
for row in frozen_trace:
    y = dict(row); extra = ['E' + str(x['sequence']) for x in edits if x['sequence'] > 372 and row['id'] in x['ids']]
    if extra: y['edit_ids'] = row['edit_ids'] + extra; y['amended'] = 'AMENDED-v1: ' + ', '.join(extra)
    trace.append(y)
(A / 'WORKFLOW_RULING_TRACEABILITY.json').write_text(json.dumps(trace, indent=2) + '\n')
fc_rows = {}
for x in edits:
    if x['sequence'] > 372:
        for i in x['ids']:
            if i.startswith('FC-'): fc_rows.setdefault(i, []).append('E' + str(x['sequence']))
ledger = (R / 'SELECTED_SCOPE_LEDGER.md').read_text()
sup = ['# SELECTED_SCOPE_LEDGER supplement — AMENDED-v1', '', 'The frozen ledger (97 certified FC rows, 94 YES / 3 NO; W01…W23; RUL-01…15; AD-01) is unchanged. This supplement adds the AMENDED-v1 edit IDs to the evidence column of the affected rows. Dispositions, severities and NO guards are not altered. Partial correction is not whole-finding closure.', '', '| ID | Frozen disposition row (verbatim) | Added AMENDED-v1 edits |', '|---|---|---|']
for fc, es in sorted(fc_rows.items()):
    m = re.search(r'^\| ' + fc + r' \|[^\n]*$', ledger, re.M); assert m, fc
    cells = [c.strip() for c in m[0].strip().strip('|').split('|')]
    sup.append('| ' + fc + ' | ' + ' / '.join(cells[1:3]) + ' | ' + ', '.join(es) + ' |')
sup += ['', 'RUL-09 traceability row: see `WORKFLOW_RULING_TRACEABILITY.json` in this directory (`amended` field).', '']
(A / 'SCOPE_LEDGER_SUPPLEMENT.md').write_text('\n'.join(sup))

# --- 6. counts derived from actual data ------------------------------------------------------------
counts = dict(frozen_counts, ordered_edits=len(edits), paths=len(index), amended_paths=len(identities), amendment_edits=len(edits) - 372,
              existing_tier=sum(1 for x in index if x['before_sha256'] and not x['path'] in ('MANIFEST.md', 'CHANGELOG.md')),
              changelog_rows=sum(1 for l in overlay('CHANGELOG.md').decode().splitlines() if l.startswith('| 2026-10-16 |')),
              landing_date_spans=len(dates), transitions=frozen_counts['transitions'], transition_paths=frozen_counts['transition_paths'])
assert counts['existing_tier'] == 31 and counts['changelog_rows'] == 39
(A / 'PROPOSAL_COUNTS.json').write_text(json.dumps(counts, indent=2) + '\n')

# --- 7. identities of changed/unchanged records -----------------------------------------------------
rec = {}
for name in ['SELECTED_EXACT_EDITS.json', 'SELECTED_CONTENT_INDEX.json', 'SELECTED_CONTENT_DIFF.patch', 'EXECUTION_PROPOSAL_INDEX.json', 'EXECUTION_PROPOSAL.patch', 'LANDING_DATE_PLAN.json', 'WORKFLOW_RULING_TRACEABILITY.json', 'PROPOSAL_COUNTS.json']:
    rec[name] = dict(gate2_sha256=sha((R / name).read_bytes()), amended_sha256=sha((A / name).read_bytes()))
unaffected = {n: sha((R / n).read_bytes()) for n in ['POST_VERIFICATION_STATUS_TRANSITIONS.json', 'POST_VERIFICATION_PROPOSAL_INDEX.json', 'POST_VERIFICATION_PROPOSAL.patch', 'PHASE_2_TEMPLATE_TRANSLATIONS.json', 'WORKFLOW_PUBLICATION_PLAN.json', 'DOCUMENT_VERSION_AND_ARCHIVE_PLAN.json', 'NEW_DOCUMENT_PROPOSALS.json', 'ARCHIVE_RESTORATION_PROPOSAL.json', 'UPDATE_MAP.md', 'GATE2_APPROVAL_RECORD_2026-10-17.md', 'DOCSET_SYNC_ACCEPTANCE_SPEC.md', 'FABLE_CORRECTION_CONFIRMATION_2026-10-17.md', 'FABLE_MAP_REVIEW_2026-10-16.md']}
(A / 'AMENDMENT_IDENTITIES.json').write_text(json.dumps(dict(
    amendment='AMENDED-v1', status='ENGINEER-PROPOSED; re-enters Gate 2; not approved; Gate 3 pending; Phase 3 NOT RELEASED',
    base_sha='9c179392f79b70da099121fc357d3107ad3bb86e', gate2_frozen_map_sha256='cd291270bb6c8e537bcb050685c6464d326254f0d2a703c21f7f304dfe286931',
    gate2_index_sha256='84337dcd3b60d059e8c67d1586cd8dba58827c64e14ab46d6d05ab57a611da39',
    amended_documents=identities, amended_edit_sequences=[x['sequence'] for x in edits if x['sequence'] > 372],
    regenerated_records=rec, unaffected_records_sha256=unaffected,
    note='Gate 2 records remain the frozen approved identities; the AMENDED_V1 directory holds the proposed successor records. Neither is implemented.'), indent=2) + '\n')

# --- 8. D-4: STARTER_KIT metadata normalization recorded as an already-approved byte transformation -
sk = '01_CONSTITUTION/STARTER_KIT_HANDBOOK.md'; stage = replay(edits, sk); final = (O / sk).read_text()
d4 = residual(stage, final)
(A / 'D4_STARTER_KIT_METADATA_NORMALIZATION.json').write_text(json.dumps(dict(
    path=sk, status='ALREADY APPROVED AS BYTES at Gate 2 (index hash); recorded here explicitly; AMENDED-v1 adds NO content change to this document',
    source='scratchpad/generators/cody_mc_metadata.py lines 26–28 (header insertion after the H1; replacement of the "**Version:** v1.1 (Kit-Perfection campaign applied)" line by the kit-campaign reference line); history row insertion as for every revised document',
    content_stage_sha256=sha(stage), gate2_proposed_sha256=sha(final), amended_proposed_sha256=sha(final),
    exact_residual_lines=d4), indent=2, ensure_ascii=False) + '\n')

# --- 9. ownership propagation sweep over the amended live tree (role tables, headings, templates, examples,
#        boot prompts, checklists). Every hit must carry a curated disposition; an uncurated hit fails the build. ---------
import re as _re
SWEEP = _re.compile(r"ENGINEER AGENT: WHAT IT PRODUCES|Engineer's full output list|\*\*Author:\*\* Engineer|Engineer Agent|\| *Engineer *\|? *$"
                    r"|Define data schemas|Define API contracts|Define schemas|schema design|Engineer Focus|Engineer owns|Engineer produces|Engineer authors"
                    r"|owned by the Engineer|Engineering owns|Engineer (defines|designs|writes|creates) [^.]*(schema|contract|API_SPEC|DB_SCHEMA|DATA_CONTRACT)", _re.I)
# resolved rows are listed from the frozen (Gate 2) proposed tree at their pre-amendment line numbers
rows = ['path\tline\tmatch\tdisposition\ttext']
for e in amend:
    x = next(x for x in edits if x['sequence'] > 372 and x['old'] == e['old']); first = e['old'].split('\n')[0]
    n = next(n for n, l in enumerate((O / e['path']).read_text().splitlines(), 1) if l == first)
    rows.append(f"{e['path']}\t{n} (Gate 2 tree)\t{first.strip()[:60]}\tRESOLVED E{x['sequence']} ({x['item']})\t{first.strip()[:220]}")
RETAIN = [  # (path substring, line substring) -> rationale
    ('APP_FACTORY_BLUEPRINT.md', '| **Claude Code (Claudy)** |', 'Phase 4 tool table "Prompted By": persona-to-seat prompting for implementation; not an artifact-ownership statement.'),
    ('APP_FACTORY_BLUEPRINT.md', '| `ENGINEER_PLAYBOOK.md` | How to BE the Engineer agent | Factory |', 'Playbook row; owner is "Factory".'),
    ('SOFTWARE_FACTORY_PLAYBOOK.md', 'A seat defines responsibility', 'States the approved seat split (Engineer owns implementation and factual handoff); consistent with the rule.'),
    ('DESIGNER_PLAYBOOK.md', '| Write the production app | Engineer Agent / Claudy |', 'Implementation ownership; consistent with the rule.'),
    ('ARCHITECT_PLAYBOOK.md', '| Implement approved data schemas as migrations and models | Engineer Agent |', 'Amended row (E375): implementation assigned to the Engineer; consistent with the rule.'),
    ('ARCHITECT_PLAYBOOK.md', '| Implement approved API contracts | Engineer Agent |', 'Amended row (E376): implementation assigned to the Engineer; consistent with the rule.'),
    ('ARCHITECT_PLAYBOOK.md', '### Type Implications for Engineer', 'Heading of the implementation-focus table; subject naming, no ownership claim.'),
    ('ARCHITECT_PLAYBOOK.md', '| Type | Engineer Focus |', 'Table header; see rows.'),
    ('ARCHITECT_PLAYBOOK.md', '| **Full-Stack Web** | DB schema, API routes, auth config, state management, deployment |', 'Implementation-focus subjects (parallels ENGINEER §13 "API route implementation"); names the subject matter the Engineer implements, does not assign definition/ownership. RETAIN; Architect may tighten in a later pass.'),
    ('ARCHITECT_PLAYBOOK.md', '| **Backend Bundle** | Service architecture, job queues, API contracts, logging, monitoring |', 'As above; ENGINEER §13 Backend Bundle bullet reads "API contract implementation".'),
    ('ARCHITECT_PLAYBOOK.md', '| **Local-First Tool** | File structure, local storage, packaging, installers, cross-platform |', 'Implementation focus; no contract artifact.'),
    ('ENGINEER_PLAYBOOK.md', '**Engineer Focus:**', 'Section label in §13; rows dispositioned individually (P-4 resolved; others implementation wording).'),
    ('ENGINEER_PLAYBOOK.md', 'The definitive manual for the Engineer Agent', 'Playbook subject name.'),
    ('ENGINEER_PLAYBOOK.md', '### Who is the Engineer Agent?', 'Playbook subject heading.'),
    ('ENGINEER_PLAYBOOK.md', 'When the Engineer Agent operates in an agentic coding environment', 'Agentic-conduct section; no ownership claim.'),
    ('ENGINEER_PLAYBOOK.md', "The Engineer Agent's mission is to **build systems that remain stable**", 'Mission statement: build/implement; consistent.'),
    ('DEPLOYMENT_PLAYBOOK.md', '| Project module QA | Authorized rework', 'Authority table row for QA-branch rework (RUL-02); not contract ownership.'),
    ('DATABASE_MANUAL.md', '| **API Contract** | Schema defines the data contract |', 'Technical statement (schema-first), no role assignment.'),
    ('SOFTWARE_FACTORY_PLAYBOOK.md', '### Schema Design Process', 'SFP §5 "Phase 3: Database Schema" is an implementation-phase build discipline (SFP line 39: lifecycle axes are separate; vocabulary map row maps it to Engineering (spec) → Fabrication (build)); describes the process, assigns no seat.'),
    ('SOFTWARE_FACTORY_PLAYBOOK.md', '- [ ] Schema designed', 'SFP build-phase checklist item; no seat assignment; the approved contract supplies the design.'),
    ('SOFTWARE_FACTORY_PLAYBOOK.md', '| DB schema | DATABASE | Schema Design Patterns |', 'Manual cross-reference table; technical topic routing.'),
    ('ENGINEER_PLAYBOOK.md', '# ENGINEER AGENT PLAYBOOK', 'Document title.'),
    ('APP_FACTORY_SKILLS_PLAYBOOK.md', 'Engineer agents consume skills', 'Skill-authoring authority statement; not contract ownership.'),
    ('DATABASE_MANUAL.md', 'Schema Design Patterns', 'Technical reference section; no seat assignment.'),
    ('ECOMMERCE_AND_PAYMENTS_MANUAL.md', 'schema design is deferred', 'Technical scope statement; no seat assignment.'),
    ('STRIPE_SUBSCRIPTIONS_PLAYBOOK.md', 'schema design is deferred', 'Technical scope statement; no seat assignment.'),
    ('STRIPE_SUBSCRIPTIONS_PLAYBOOK.md', 'Universal subscription-schema design is deferred', 'Technical scope statement; no seat assignment.'),
    ('STRIPE_SUBSCRIPTIONS_PLAYBOOK.md', 'project-approved ownership and storage contract', 'Refers to the project\'s approved contract; consistent.'),
    ('STRIPE_SUBSCRIPTIONS_PLAYBOOK.md', "Schema design and migration SQL are the developer's responsibility", 'DevOps handoff note: developer-vs-DevOps operational split, not an Architect-vs-Engineer seat statement; the approved contract still governs the schema. RETAIN; noted for the Architect (OBS-2, no change proposed).'),
]
und = []
scan = [x['path'] for x in index if x['path'].endswith(('.md', '.svg')) and not x['path'].startswith('_ARCHIVE/')]
for rel in scan:
    for n, line in enumerate(overlay(rel).decode().splitlines(), 1):
        m = SWEEP.search(line)
        if not m: continue
        disp = None
        if True:
            for ps, ls, why in RETAIN:
                if ps in rel and ls in line: disp = 'RETAIN — ' + why; break
        if not disp: disp = 'UNDISPOSITIONED'; und.append((rel, n, line.strip()[:160]))
        rows.append(f'{rel}\t{n}\t{m[0]}\t{disp}\t{line.strip()[:220]}')
assert not und, und
assert sum(r.split('\t')[3].startswith('RESOLVED') for r in rows[1:]) == len(amend)
(A / 'OWNERSHIP_PROPAGATION.tsv').write_text('\n'.join(rows) + '\n')
print(len(edits), 'ordered edits;', len(index), 'paths;', len(identities), 'amended documents;', len(dates), 'date spans;', len(rows) - 1, 'sweep hits (', sum('RESOLVED' in r for r in rows[1:]), 'resolved,', sum('RETAIN' in r for r in rows[1:]), 'retained )')
