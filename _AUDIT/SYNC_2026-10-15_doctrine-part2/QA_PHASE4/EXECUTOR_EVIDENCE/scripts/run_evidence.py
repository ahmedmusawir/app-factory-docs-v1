from pathlib import Path
import subprocess,json,shutil
E=Path(__file__).resolve().parents[1]
backup=E/'RAW/first_run';backup.mkdir(exist_ok=True)
for n in ['automated_checks.json','supplement_checks.json','final_checks.json','reconciled_checks.json']:
 shutil.copy2(E/'RAW'/n,backup/n)
for n in ['checks.py','read_packet.py','supplement.py','final_checks.py','reconcile.py']:
 args=['python3','-B','-I',n];p=subprocess.run(args,cwd=E/'scripts',capture_output=True,text=True)
 records=json.loads((E/'COMMANDS.json').read_text());records.append(dict(cmd=args,cwd=str(E/'scripts'),exit=p.returncode,stdout=p.stdout,stderr=p.stderr));(E/'COMMANDS.json').write_text(json.dumps(records,indent=2)+'\n');print(n,p.returncode)
 assert p.returncode==0
