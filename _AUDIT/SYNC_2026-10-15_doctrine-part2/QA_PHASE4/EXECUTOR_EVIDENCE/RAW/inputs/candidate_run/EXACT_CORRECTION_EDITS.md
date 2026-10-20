# Exact correction-edit proposals

DRAFT; no canonical write. The source spans below are checked against BASE-equivalent working-tree bytes. These supplement, not supersede, the per-ID outcomes/preservation and open decisions in UPDATE_MAP.

## FC-031 — 03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:1076
Replace lines 1076–1082 with ENGINEER-PROPOSED text:
````
function pickMeta(
  record: { meta_data: Array<{ key: string; value: unknown }> },
  key: string,
): { present: false } | { present: true; value: unknown } {
  const entry = record.meta_data.find((m) => m.key === key);
  return entry === undefined
    ? { present: false }
    : { present: true, value: entry.value };
}
````

## FC-049 — 04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:398
Replace lines 398–400 with ENGINEER-PROPOSED text:
````
      return {
        items: state.items.map((item, index) =>
          index === existingIndex ? { ...item, quantity: item.quantity + 1 } : item
        ),
      };
````

## FC-046 — 04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:727
Replace lines 727–740 with ENGINEER-PROPOSED text:
````
// Both subscriptions run on every render; only the returned value is gated.
export const useHydratedStore = <T,>(
  store: UseBoundStore<StoreApi<T & { hasHydrated: boolean }>>,
  selector: (state: T) => unknown
) => {
  const hasHydrated = store((state) => state.hasHydrated);
  const selected = store(selector as (state: T & { hasHydrated: boolean }) => unknown);
  return hasHydrated ? selected : null;
};
````

## FC-046-heading — 04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:724
Replace lines 724–724 with ENGINEER-PROPOSED text:
````
### Alternative: Hydration-Gated Selection
````

## FC-044 — 04_REFERENCE_MANUALS/AUTH_MANUAL.md:536
Replace lines 536–541 with ENGINEER-PROPOSED text:
````
  const { error } = await supabase.auth.signOut();
  if (error) {
    return NextResponse.json(
      { message: "Remote sign-out could not be confirmed. Retry sign-out." },
      { status: 503 }
    );
  }
  return NextResponse.json(
    { message: "Logged out successfully" },
    { status: 200 }
  );
````

## FC-043 — 04_REFERENCE_MANUALS/AUTH_MANUAL.md:628
Replace lines 628–628 with ENGINEER-PROPOSED text:
````
      const origin = new URL(request.url).origin;
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
      return NextResponse.redirect(fallback);
````

## FC-065-confirmed — 04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:621
Replace lines 621–621 with ENGINEER-PROPOSED text:
````
"Your subscription change is confirmed." with a Continue button. Show only after the server-authorized payment attempt resolves to its expected target tier and qualifying subscription status; an existing non-free tier is insufficient.
````

## FC-065-timeout — 04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md:624
Replace lines 624–624 with ENGINEER-PROPOSED text:
````
"Your subscription change is still pending or could not be confirmed." with Refresh and the approved support/recovery path. Show after 5 failed polls (10 seconds); timeout does not establish payment receipt.
````

## FC-080 — 05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1219
Replace lines 1219–1238 with ENGINEER-PROPOSED text:
````
const mobileCols = { 1: 'grid-cols-1', 2: 'grid-cols-2', 3: 'grid-cols-3', 4: 'grid-cols-4' } as const;
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
};
````

## FC-084 — 02_PIPELINE_AGENTS/DESIGNER_PLAYBOOK.md:232
Replace lines 232–232 with ENGINEER-PROPOSED text:
````
- [ ] All required elements and minimum display fields in the approved UI_SPEC are present; record NOT APPLICABLE only where that contract says so.
````

## FC-003/096 — 01_CONSTITUTION/STARTER_KIT_HANDBOOK.md:258
Replace lines 258–258 with ENGINEER-PROPOSED text:
````
1. Check `COMPONENT_REGISTRY.md` (sibling file) — does a primitive exist?
````

## FC-003/096 — 01_CONSTITUTION/STARTER_KIT_HANDBOOK.md:692
Replace lines 692–692 with ENGINEER-PROPOSED text:
````
- **`agent_docs/STARTER_KIT/COMPONENT_REGISTRY.md`** — scannable component lookup (sibling file)
````

## FC-003/096 — 01_CONSTITUTION/STARTER_KIT_HANDBOOK.md:261
Replace lines 261–261 with ENGINEER-PROPOSED text:
````
4. Check `agent_docs/APP_FACTORY/UI_UX_BUILDING_MANUAL.md`
````

## FC-003/096 — 01_CONSTITUTION/STARTER_KIT_HANDBOOK.md:690
Replace lines 690–690 with ENGINEER-PROPOSED text:
````
- **`agent_docs/APP_FACTORY/UI_UX_BUILDING_MANUAL.md`** — full UI patterns, Rule Zero (mobile-first)
````

## FC-003/096 — 01_CONSTITUTION/STARTER_KIT_HANDBOOK.md:688
Replace lines 688–688 with ENGINEER-PROPOSED text:
````
- **`agent_docs/APP_FACTORY/AUTH_MANUAL.md`** — full auth implementation details (deep dive)
````

## FC-003/096 — 04_REFERENCE_MANUALS/DATABASE_MANUAL.md:8
Replace lines 8–8 with ENGINEER-PROPOSED text:
````
> **Role doctrine (v1.1):** roles live in the `user_roles` table — one doctrine, aligned with AUTH_MANUAL (F-041/F-042).
````

## FC-003/096 — 04_REFERENCE_MANUALS/DATABASE_MANUAL.md:156
Replace lines 156–156 with ENGINEER-PROPOSED text:
````
> ⛔ **FORBIDDEN:** never store — or READ — roles for authorization from `user_metadata` (the recon Q3.4 smell), and never mirror a `role` column onto a profile table. Two homes for a role guarantees privilege drift. This aligns with AUTH_MANUAL ("Where Roles Live").
````

## FC-003/096 — 05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:2092
Replace lines 2092–2092 with ENGINEER-PROPOSED text:
````
**Fix applied to this manual:** Added Rule Zero-B as the companion posture to Rule Zero. Authored `THEMING_MANUAL.md` as the standalone deep dive. Updated `APP_ARCHITECTURE_MANUAL` and `HANDOFF_PACKAGE_PLAYBOOK` with cross-references. Bumped this manual to v1.2.
````

## FC-003/096 — 05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:2121
Replace lines 2121–2121 with ENGINEER-PROPOSED text:
````
| 1.2 | 2026-06-02 | Added Rule Zero-B (theming as the second foundational posture). Added TOC entries for Rule Zero and Rule Zero-B. Authored companion `THEMING_MANUAL.md`. Added Lesson 9 appendix. Born from Cyber Pharma Run 002. |
````
