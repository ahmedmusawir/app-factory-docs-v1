from pathlib import Path
import json,hashlib,zipfile,datetime,collections
R=Path('/home/moose/Documents/app-factory-docs-v1');E=R/'_AUDIT/SYNC_2026-10-15_doctrine-part2/QA_PHASE4/RETEST_AMENDED_V2/EXECUTOR_EVIDENCE'
h=lambda b:hashlib.sha256(b).hexdigest()
results=json.loads((E/'R_RESULTS.json').read_text());assert [x['id'] for x in results]==['R'+str(i) for i in range(1,13)];assert collections.Counter(x['status'] for x in results)=={'PASS':11,'FAIL':1};assert len(json.loads((E/'WITHDRAWAL_ROWS.json').read_text()))==31
(E/'scripts/seal.py').write_bytes(Path(__file__).read_bytes())
files=sorted(p for p in E.rglob('*') if p.is_file() and p.name!='SHA256SUMS.txt');inventory=''.join(h(p.read_bytes())+'  '+p.relative_to(E).as_posix()+'\n' for p in files);(E/'SHA256SUMS.txt').write_text(inventory)
for line in inventory.splitlines():digest,n=line.split('  ',1);assert h((E/n).read_bytes())==digest
zpath=Path('/tmp/QA_AMENDED_V2_EXECUTOR_8dff354_2026-10-19.zip')
with zipfile.ZipFile(zpath,'x',zipfile.ZIP_DEFLATED) as z:
 for p in sorted(E.rglob('*')):
  if p.is_file():z.write(p,'EXECUTOR_EVIDENCE/'+p.relative_to(E).as_posix())
with zipfile.ZipFile(zpath) as z:
 assert len(z.namelist())==len(files)+1 and z.testzip() is None
 for line in inventory.splitlines():digest,n=line.split('  ',1);assert h(z.read('EXECUTOR_EVIDENCE/'+n))==digest
receipt=dict(zip=str(zpath),zip_sha256=h(zpath.read_bytes()),manifest_sha256=h((E/'SHA256SUMS.txt').read_bytes()),evidence_files=len(files),zip_members=len(files)+1,candidate='8dff354937bc7baf739370a9886497d9d5359186',counts={'PASS':11,'FAIL':1,'BLOCKED':0});Path('/tmp/qa_seal_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt,indent=2))
