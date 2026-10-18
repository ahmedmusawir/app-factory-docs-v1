from pathlib import Path
import re,colorsys,json
R=Path('_AUDIT/SYNC_2026-10-15_doctrine-part2');s=Path('05_DESIGN_SYSTEM/TOKEN_FILE.md').read_text();modes={}
for name,pattern in [('Mist',r':root \{(.*?)\n  \}'),('Slate',r'  \.dark \{(.*?)\n  \}')]:
 b=re.search(pattern,s,re.S).group(1);modes[name]={k:tuple(map(float,v.split())) for k,v in re.findall(r'--([\w-]+):\s*([\d.]+\s+[\d.]+%?\s+[\d.]+%?)',b.replace('%',''))}
def lum(v):
 h,ss,l=v;rgb=colorsys.hls_to_rgb(h/360,l/100,ss/100);return sum(c*w for c,w in zip([x/12.92 if x<=.04045 else ((x+.055)/1.055)**2.4 for x in rgb],[.2126,.7152,.0722]))
def cr(a,b):x,y=sorted([lum(a),lum(b)]);return (y+.05)/(x+.05)
sem=['primary','accent','destructive','success','warning','info','role-superadmin','role-admin','role-member']
changes=[];new={k:dict(v) for k,v in modes.items()}
for mode,t in new.items():
 for name in sem:
  fg=name+'-foreground';v=t[name]
  # Preserve hue and saturation; minimally adjust lightness and use accessible foreground per mode.
  foreground=(0.,0.,100.) if mode=='Mist' else (222.,20.,13.)
  candidates=sorted(range(1,100),key=lambda l:abs(l-v[2]))
  for l in candidates:
   val=(v[0],v[1],float(l))
   if min(cr(val,t['card']),cr(val,t['background']),cr(val,foreground))>=4.5:
    t[name]=val;t[fg]=foreground;break
 for key in ['muted-foreground']:
  v=t[key]
  if min(cr(v,t['muted']),cr(v,t['background']),cr(v,t['card']))<4.5:
   for l in sorted(range(1,100),key=lambda l:abs(l-v[2])):
    val=(v[0],v[1],float(l))
    if min(cr(val,t['muted']),cr(val,t['background']),cr(val,t['card']))>=4.5:t[key]=val;break
 for key,val in t.items():
  if val!=modes[mode][key]:changes.append({'mode':mode,'token':'--'+key,'old':modes[mode][key],'new':val})
for alias,parent,overrides in [('Bright','Mist',{'background':(0.,0.,100.),'secondary':(220.,19.,96.),'muted':(220.,16.,94.)}),('Dark-deep','Slate',{'background':(224.,18.,12.),'card':(225.,16.,16.),'popover':(225.,16.,16.)})]:
 modes[alias]={**modes[parent],**overrides};new[alias]={**new[parent],**overrides}
rows=[]
for mode,t in new.items():
 for name in sem:
  for fg,bg in [(name,'card'),(name,'background'),(name+'-foreground',name)]:rows.append((mode,fg,bg,cr(modes[mode][fg],modes[mode][bg]),cr(t[fg],t[bg])))
 for fg,bg in [('foreground','background'),('card-foreground','card'),('popover-foreground','popover'),('secondary-foreground','secondary'),('muted-foreground','muted')]:rows.append((mode,fg,bg,cr(modes[mode][fg],modes[mode][bg]),cr(t[fg],t[bg])))
assert all(row[-1]>=4.5 for row in rows)
md=['# FC-074 proposed token values and computed contrast\n\nENGINEER-PROPOSED; no CSS or canonical document changed. Calculation uses the HSL triplets as authoritative, sRGB linearization and relative-luminance ratio (lighter + .05)/(darker + .05). All listed normal-text uses require at least 4.5:1. This checks numerical pairings, not browser rendering or every possible token combination. Charts, borders and focus indicators need their separate non-text/visual checks.\n\nReplace these declarations inside TOKEN_FILE’s :root (Mist) or .dark (Slate) block; synchronize corresponding THEME_LIBRARY rows and remove stale hexadecimal comments for changed declarations. Preserve hue and semantic meaning.\n\n| Mode | Token | Old HSL | Proposed HSL |\n|---|---|---|---|']
fmt=lambda v:f'{v[0]:g} {v[1]:g}% {v[2]:g}%'
for c in changes:md.append(f"| {c['mode']} | `{c['token']}` | `{fmt(c['old'])}` | `{fmt(c['new'])}` |")
md+=['\nTHEME_LIBRARY wording replacement — ENGINEER-PROPOSED: “Semantic hue and meaning hold across modes; lightness and the paired foreground may differ to meet the documented contrast requirements. TOKEN_FILE contains the reference values. Verify the exact text/fill uses against the retained contrast matrix before claiming accessibility.”\n\n| Mode | Foreground | Background | Baseline ratio | Proposed ratio |\n|---|---|---|---|---|']
for mode,fg,bg,old,newratio in rows:md.append(f'| {mode} | {fg} | {bg} | {old:.3f} | {newratio:.3f} |')
md+=['\nThe matrix includes the optional Bright/Dark-deep overrides as well as the default Mist/Slate pair. Candidate QA must recompute the ratios from the actual landed tokens and verify the preserved role meaning and real rendered uses.\n']
(R/'FC074_CONTRAST_PROPOSAL.md').write_text('\n'.join(md));(R/'scratchpad/token_changes.json').write_text(json.dumps(changes,indent=2)+'\n');print(len(changes),'declaration changes;',len(rows),'computed default-mode pairings all >=4.5')
