"""Read-only template provenance verification. Usage: python3 verify_templates.py REPO."""
from pathlib import Path
import sys, json, hashlib
root=Path(sys.argv[1]).resolve()
run=root/'_AUDIT/SYNC_2026-10-15_doctrine-part2'
sha=lambda b:hashlib.sha256(b).hexdigest()
rows=json.loads((run/'PHASE_2_TEMPLATE_TRANSLATIONS.json').read_text())
actual={str(p.relative_to(root)) for p in (root/'03_BUILD_METHODOLOGY/_templates/QAM').rglob('*') if p.is_file()}
assert actual=={r['destination'] for r in rows} and len(rows)==25
for r in rows:
 source=(run/'INTAKE_SNAPSHOT'/r['source']).read_bytes(); assert sha(source)==r['source_sha256']
 translated=source.decode()
 for t in r['translations']:
  assert translated.count(t['old'])==t['occurrences']
  translated=translated.replace(t['old'],t['new'])
 installed=(root/r['destination']).read_bytes()
 assert translated.encode()==installed and sha(installed)==r['proposed_destination_sha256']
 print(json.dumps({'source':r['source'],'destination':r['destination'],'source_sha256':sha(source),'translated_sha256':sha(translated.encode()),'installed_sha256':sha(installed),'result':'PASS'}))
print('PASS: 25 source/translation/installed hashes; exact installed file set.')
