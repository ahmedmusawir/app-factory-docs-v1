from pathlib import Path
import json
R=Path('_AUDIT/SYNC_2026-10-15_doctrine-part2');ed=[]
def rep(id,p,old,new):
 s=Path(p).read_text();assert s.count(old)==1,(id,s.count(old));i=s.index(old);ed.append(dict(id=id,path=p,start_line=s[:i].count('\n')+1,end_line=s[:i+len(old)].count('\n')+1,old=old,new=new,label='ENGINEER-PROPOSED'))
rep('FC-031','03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md','''function pickMeta(
  record: { meta_data: Array<{ key: string; value: unknown }> },
  key: string,
): unknown {
  const entry = record.meta_data?.find((m) => m.key === key);
  return entry ? entry.value : null; // null = absent; falsy value = present-but-empty
}''','''function pickMeta(
  record: { meta_data: Array<{ key: string; value: unknown }> },
  key: string,
): { present: false } | { present: true; value: unknown } {
  const entry = record.meta_data.find((m) => m.key === key);
  return entry === undefined
    ? { present: false }
    : { present: true, value: entry.value };
}''')
p='04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md'
rep('FC-049',p,'''      const newItems = [...state.items];
      newItems[existingIndex].quantity += 1;
      return { items: newItems };''','''      return {
        items: state.items.map((item, index) =>
          index === existingIndex ? { ...item, quantity: item.quantity + 1 } : item
        ),
      };''')
old='''// Custom hook that throws promise until hydrated
export const useHydratedStore = <T,>(
  store: UseBoundStore<StoreApi<T & { hasHydrated: boolean }>>,
  selector: (state: T) => unknown
) => {
  const hasHydrated = store((state) => state.hasHydrated);
  
  if (!hasHydrated) {
    // Return null or default during SSR
    return null;
  }
  
  return store(selector as (state: T & { hasHydrated: boolean }) => unknown);
};'''
new='''// Both subscriptions run on every render; only the returned value is gated.
export const useHydratedStore = <T,>(
  store: UseBoundStore<StoreApi<T & { hasHydrated: boolean }>>,
  selector: (state: T) => unknown
) => {
  const hasHydrated = store((state) => state.hasHydrated);
  const selected = store(selector as (state: T & { hasHydrated: boolean }) => unknown);
  return hasHydrated ? selected : null;
};'''
rep('FC-046',p,old,new);rep('FC-046-heading',p,'### Alternative: Suspense-Style Loading','### Alternative: Hydration-Gated Selection')
p='04_REFERENCE_MANUALS/AUTH_MANUAL.md'
rep('FC-044',p,'''  await supabase.auth.signOut();

  return NextResponse.json(
    { message: "Logged out successfully" },
    { status: 200 }
  );''','''  const { error } = await supabase.auth.signOut();
  if (error) {
    return NextResponse.json(
      { message: "Remote sign-out could not be confirmed. Retry sign-out." },
      { status: 503 }
    );
  }
  return NextResponse.json(
    { message: "Logged out successfully" },
    { status: 200 }
  );''')
rep('FC-043',p,'      return NextResponse.redirect(new URL(next, request.url));','''      const origin = new URL(request.url).origin;
      const fallback = new URL("/", origin);
      const allowedPaths = new Set(["/"]); // Extend only with approved local destinations.
      try {
        const destination = new URL(next, origin);
        if (destination.origin === origin && allowedPaths.has(destination.pathname)) {
          destination.search = "";
          destination.hash = "";
          return NextResponse.redirect(destination);
        }
      } catch {
        // Malformed destinations use the fixed safe fallback.
      }
      return NextResponse.redirect(fallback);''')
p='04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md'
rep('FC-065-confirmed',p,'"Welcome to Pro!" with a Continue button. Shown when the subscription tier is no longer "free."','"Your subscription change is confirmed." with a Continue button. Show only after the server-authorized payment attempt resolves to its expected target tier and qualifying subscription status; an existing non-free tier is insufficient.')
rep('FC-065-timeout',p,'"Your payment was received! Your subscription will activate momentarily." with a Refresh button. Shown after 5 failed polls (10 seconds).','"Your subscription change is still pending or could not be confirmed." with Refresh and the approved support/recovery path. Show after 5 failed polls (10 seconds); timeout does not establish payment receipt.')
p='05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md';s=Path(p).read_text();start=s.index('interface GridProps {');end=s.index('\n```',start);old=s[start:end]
new='''const mobileCols = { 1: 'grid-cols-1', 2: 'grid-cols-2', 3: 'grid-cols-3', 4: 'grid-cols-4' } as const;
const tabletCols = { 1: 'md:grid-cols-1', 2: 'md:grid-cols-2', 3: 'md:grid-cols-3', 4: 'md:grid-cols-4' } as const;
const desktopCols = { 1: 'lg:grid-cols-1', 2: 'lg:grid-cols-2', 3: 'lg:grid-cols-3', 4: 'lg:grid-cols-4' } as const;
const gaps = { 0: 'gap-0', 2: 'gap-2', 4: 'gap-4', 6: 'gap-6', 8: 'gap-8' } as const;

interface GridProps {
  children: ReactNode;
  cols?: {
    mobile?: keyof typeof mobileCols;
    tablet?: keyof typeof tabletCols;
    desktop?: keyof typeof desktopCols;
  };
  gap?: keyof typeof gaps;
  className?: string;
}

const Grid = ({ children, cols = {}, gap = 4, className = '' }: GridProps) => {
  const { mobile = 1, tablet = 2, desktop = 3 } = cols;
  if (!(mobile in mobileCols) || !(tablet in tabletCols) || !(desktop in desktopCols) || !(gap in gaps)) {
    throw new Error('Unsupported Grid variant');
  }
  return (
    <div className={`grid ${mobileCols[mobile]} ${tabletCols[tablet]} ${desktopCols[desktop]} ${gaps[gap]} ${className}`}>
      {children}
    </div>
  );
};'''
rep('FC-080',p,old,new)
rep('FC-084','02_PIPELINE_AGENTS/DESIGNER_PLAYBOOK.md','- [ ] All required elements present (per §5.6 minimum display fields, if defined)','- [ ] All required elements and minimum display fields in the approved UI_SPEC are present; record NOT APPLICABLE only where that contract says so.')
# Mechanical exact replacements are enumerated per occurrence, not hand-counted.
for p,old,new in [('01_CONSTITUTION/STARTER_KIT_HANDBOOK.md','COMPONENT_REGISTRY_v1.1.md','COMPONENT_REGISTRY.md'),('01_CONSTITUTION/STARTER_KIT_HANDBOOK.md','UI-UX-BUILDING-MANUAL_v1_3.md','UI_UX_BUILDING_MANUAL.md'),('01_CONSTITUTION/STARTER_KIT_HANDBOOK.md','AUTH_MANUAL_v1.2.md','AUTH_MANUAL.md'),('04_REFERENCE_MANUALS/DATABASE_MANUAL.md','AUTH_MANUAL v1.3','AUTH_MANUAL'),('05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md','THEMING_MANUAL_v1.0.md','THEMING_MANUAL.md')]:
 s=Path(p).read_text()
 for i,line in enumerate(s.splitlines(),1):
  if old in line and not (p.endswith('DATABASE_MANUAL.md') and i>1200):ed.append(dict(id='FC-003/096',path=p,start_line=i,end_line=i,old=line,new=line.replace(old,new),label='ENGINEER-PROPOSED mechanical'))
(R/'EXACT_CORRECTION_EDITS.json').write_text(json.dumps(ed,indent=2)+'\n')
md=['# Exact correction-edit proposals\n\nDRAFT; no canonical write. The source spans below are checked against BASE-equivalent working-tree bytes. These supplement, not supersede, the per-ID outcomes/preservation and open decisions in UPDATE_MAP.\n']
for e in ed:md.extend([f"## {e['id']} — {e['path']}:{e['start_line']}",f"Replace lines {e['start_line']}–{e['end_line']} with ENGINEER-PROPOSED text:",'````\n'+e['new']+'\n````\n'])
(R/'EXACT_CORRECTION_EDITS.md').write_text('\n'.join(md));print(len(ed),'exact correction spans saved')
