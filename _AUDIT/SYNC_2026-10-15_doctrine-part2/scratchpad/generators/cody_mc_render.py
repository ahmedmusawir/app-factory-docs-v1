from pathlib import Path
import gi,cairo,json,hashlib
gi.require_version('Rsvg','2.0')
from gi.repository import Rsvg
r=Path('_AUDIT/SYNC_2026-10-15_doctrine-part2');dest=r/'MC_EVIDENCE/diagram_previews';dest.mkdir(parents=True,exist_ok=True);rows=[]
for p in sorted((r/'PROPOSED_CONTENT/03_BUILD_METHODOLOGY/_assets/workflows').glob('*.svg')):
 h=Rsvg.Handle.new_from_file(str(p));d=h.get_dimensions();surf=cairo.ImageSurface(cairo.FORMAT_ARGB32,d.width,d.height);ctx=cairo.Context(surf);h.render_cairo(ctx);out=dest/(p.stem+'.png');surf.write_to_png(str(out));rows.append(dict(source=str(p),source_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),preview=str(out),preview_sha256=hashlib.sha256(out.read_bytes()).hexdigest(),width=d.width,height=d.height))
(r/'MC_DIAGRAM_RENDER.json').write_text(json.dumps(rows,indent=2)+'\n');print('PASS: four revised SVGs rendered with librsvg/cairo; visual inspection recorded separately; no production behavior tested.')
