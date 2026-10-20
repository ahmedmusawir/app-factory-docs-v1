from pathlib import Path
import hashlib,json,zipfile
E=Path(__file__).resolve().parents[1]
manifest=E/'SHA256SUMS.txt'
files=sorted(p for p in E.rglob('*') if p.is_file() and p!=manifest)
manifest.write_text(''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+str(p.relative_to(E))+'\n' for p in files))
dest=Path('/home/moose/Downloads/QA_PHASE4_EXECUTOR_20f71ee_2026-10-19.zip')
assert not dest.exists(),'Refusing to overwrite an earlier delivery'
with zipfile.ZipFile(dest,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for p in sorted(E.rglob('*')):
  if p.is_file():z.write(p,'EXECUTOR_EVIDENCE/'+str(p.relative_to(E)))
with zipfile.ZipFile(dest) as z:
 assert z.testzip() is None
 covered=set()
 for line in z.read('EXECUTOR_EVIDENCE/SHA256SUMS.txt').decode().splitlines():
  h,n=line.split('  ',1);assert hashlib.sha256(z.read('EXECUTOR_EVIDENCE/'+n)).hexdigest()==h;covered.add('EXECUTOR_EVIDENCE/'+n)
 assert set(z.namelist())==covered|{'EXECUTOR_EVIDENCE/SHA256SUMS.txt'}
 print(json.dumps(dict(zip=str(dest),zip_bytes=dest.stat().st_size,members=len(z.namelist()),manifest_sha256=hashlib.sha256(manifest.read_bytes()).hexdigest(),zip_sha256=hashlib.sha256(dest.read_bytes()).hexdigest(),crc='PASS',every_member_hash='PASS'),indent=2))
