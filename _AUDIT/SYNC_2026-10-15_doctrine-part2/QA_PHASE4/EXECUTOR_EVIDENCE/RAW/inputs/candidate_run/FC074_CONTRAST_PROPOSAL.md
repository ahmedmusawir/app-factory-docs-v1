# FC-074 proposed token values and computed contrast

ENGINEER-PROPOSED; no CSS or canonical document changed. Calculation uses the HSL triplets as authoritative, sRGB linearization and relative-luminance ratio (lighter + .05)/(darker + .05). All listed normal-text uses require at least 4.5:1. This checks numerical pairings, not browser rendering or every possible token combination. Charts, borders and focus indicators need their separate non-text/visual checks.

Replace these declarations inside TOKEN_FILE’s :root (Mist) or .dark (Slate) block; synchronize corresponding THEME_LIBRARY rows and remove stale hexadecimal comments for changed declarations. Preserve hue and semantic meaning.

| Mode | Token | Old HSL | Proposed HSL |
|---|---|---|---|
| Mist | `--primary` | `12 93% 64%` | `12 93% 39%` |
| Mist | `--muted-foreground` | `218 12% 42%` | `218 12% 39%` |
| Mist | `--accent` | `12 93% 64%` | `12 93% 39%` |
| Mist | `--destructive` | `2 67% 51%` | `2 67% 45%` |
| Mist | `--success` | `131 54% 40%` | `131 54% 29%` |
| Mist | `--warning` | `41 93% 47%` | `41 93% 27%` |
| Mist | `--info` | `214 74% 53%` | `214 74% 43%` |
| Mist | `--role-admin` | `189 65% 32%` | `189 65% 30%` |
| Mist | `--role-member` | `131 40% 33%` | `131 40% 32%` |
| Slate | `--primary` | `12 93% 64%` | `12 93% 66%` |
| Slate | `--primary-foreground` | `0 0% 100%` | `222 20% 13%` |
| Slate | `--accent` | `12 93% 64%` | `12 93% 66%` |
| Slate | `--accent-foreground` | `0 0% 100%` | `222 20% 13%` |
| Slate | `--info` | `214 74% 53%` | `214 74% 66%` |
| Slate | `--info-foreground` | `0 0% 100%` | `222 20% 13%` |

THEME_LIBRARY wording replacement — ENGINEER-PROPOSED: “Semantic hue and meaning hold across modes; lightness and the paired foreground may differ to meet the documented contrast requirements. TOKEN_FILE contains the reference values. Verify the exact text/fill uses against the retained contrast matrix before claiming accessibility.”

| Mode | Foreground | Background | Baseline ratio | Proposed ratio |
|---|---|---|---|---|
| Mist | primary | card | 2.823 | 5.829 |
| Mist | primary | background | 2.226 | 4.596 |
| Mist | primary-foreground | primary | 2.823 | 5.829 |
| Mist | accent | card | 2.823 | 5.829 |
| Mist | accent | background | 2.226 | 4.596 |
| Mist | accent-foreground | accent | 2.823 | 5.829 |
| Mist | destructive | card | 4.792 | 5.825 |
| Mist | destructive | background | 3.778 | 4.593 |
| Mist | destructive-foreground | destructive | 4.792 | 5.825 |
| Mist | success | card | 3.483 | 5.977 |
| Mist | success | background | 2.746 | 4.712 |
| Mist | success-foreground | success | 3.483 | 5.977 |
| Mist | warning | card | 2.213 | 5.933 |
| Mist | warning | background | 1.745 | 4.677 |
| Mist | warning-foreground | warning | 2.213 | 5.933 |
| Mist | info | card | 4.165 | 5.867 |
| Mist | info | background | 3.283 | 4.625 |
| Mist | info-foreground | info | 4.165 | 5.867 |
| Mist | role-superadmin | card | 7.363 | 7.363 |
| Mist | role-superadmin | background | 5.805 | 5.805 |
| Mist | role-superadmin-foreground | role-superadmin | 7.363 | 7.363 |
| Mist | role-admin | card | 5.218 | 5.776 |
| Mist | role-admin | background | 4.114 | 4.554 |
| Mist | role-admin-foreground | role-admin | 5.218 | 5.776 |
| Mist | role-member | card | 5.538 | 5.808 |
| Mist | role-member | background | 4.366 | 4.579 |
| Mist | role-member-foreground | role-member | 5.538 | 5.808 |
| Mist | foreground | background | 11.466 | 11.466 |
| Mist | card-foreground | card | 14.543 | 14.543 |
| Mist | popover-foreground | popover | 14.543 | 14.543 |
| Mist | secondary-foreground | secondary | 12.603 | 12.603 |
| Mist | muted-foreground | muted | 4.110 | 4.595 |
| Slate | primary | card | 4.352 | 4.592 |
| Slate | primary | background | 5.697 | 6.011 |
| Slate | primary-foreground | primary | 2.823 | 6.197 |
| Slate | accent | card | 4.352 | 4.592 |
| Slate | accent | background | 5.697 | 6.011 |
| Slate | accent-foreground | accent | 2.823 | 6.197 |
| Slate | destructive | card | 4.511 | 4.511 |
| Slate | destructive | background | 5.906 | 5.906 |
| Slate | destructive-foreground | destructive | 6.088 | 6.088 |
| Slate | success | card | 7.039 | 7.039 |
| Slate | success | background | 9.215 | 9.215 |
| Slate | success-foreground | success | 9.500 | 9.500 |
| Slate | warning | card | 5.552 | 5.552 |
| Slate | warning | background | 7.269 | 7.269 |
| Slate | warning-foreground | warning | 7.494 | 7.494 |
| Slate | info | card | 2.950 | 4.547 |
| Slate | info | background | 3.862 | 5.952 |
| Slate | info-foreground | info | 4.165 | 6.136 |
| Slate | role-superadmin | card | 4.646 | 4.646 |
| Slate | role-superadmin | background | 6.082 | 6.082 |
| Slate | role-superadmin-foreground | role-superadmin | 6.270 | 6.270 |
| Slate | role-admin | card | 6.031 | 6.031 |
| Slate | role-admin | background | 7.895 | 7.895 |
| Slate | role-admin-foreground | role-admin | 8.139 | 8.139 |
| Slate | role-member | card | 6.906 | 6.906 |
| Slate | role-member | background | 9.040 | 9.040 |
| Slate | role-member-foreground | role-member | 9.320 | 9.320 |
| Slate | foreground | background | 13.514 | 13.514 |
| Slate | card-foreground | card | 10.324 | 10.324 |
| Slate | popover-foreground | popover | 10.324 | 10.324 |
| Slate | secondary-foreground | secondary | 8.623 | 8.623 |
| Slate | muted-foreground | muted | 6.299 | 6.299 |
| Bright | primary | card | 2.823 | 5.829 |
| Bright | primary | background | 2.823 | 5.829 |
| Bright | primary-foreground | primary | 2.823 | 5.829 |
| Bright | accent | card | 2.823 | 5.829 |
| Bright | accent | background | 2.823 | 5.829 |
| Bright | accent-foreground | accent | 2.823 | 5.829 |
| Bright | destructive | card | 4.792 | 5.825 |
| Bright | destructive | background | 4.792 | 5.825 |
| Bright | destructive-foreground | destructive | 4.792 | 5.825 |
| Bright | success | card | 3.483 | 5.977 |
| Bright | success | background | 3.483 | 5.977 |
| Bright | success-foreground | success | 3.483 | 5.977 |
| Bright | warning | card | 2.213 | 5.933 |
| Bright | warning | background | 2.213 | 5.933 |
| Bright | warning-foreground | warning | 2.213 | 5.933 |
| Bright | info | card | 4.165 | 5.867 |
| Bright | info | background | 4.165 | 5.867 |
| Bright | info-foreground | info | 4.165 | 5.867 |
| Bright | role-superadmin | card | 7.363 | 7.363 |
| Bright | role-superadmin | background | 7.363 | 7.363 |
| Bright | role-superadmin-foreground | role-superadmin | 7.363 | 7.363 |
| Bright | role-admin | card | 5.218 | 5.776 |
| Bright | role-admin | background | 5.218 | 5.776 |
| Bright | role-admin-foreground | role-admin | 5.218 | 5.776 |
| Bright | role-member | card | 5.538 | 5.808 |
| Bright | role-member | background | 5.538 | 5.808 |
| Bright | role-member-foreground | role-member | 5.538 | 5.808 |
| Bright | foreground | background | 14.543 | 14.543 |
| Bright | card-foreground | card | 14.543 | 14.543 |
| Bright | popover-foreground | popover | 14.543 | 14.543 |
| Bright | secondary-foreground | secondary | 13.231 | 13.231 |
| Bright | muted-foreground | muted | 4.904 | 5.483 |
| Dark-deep | primary | card | 5.383 | 5.679 |
| Dark-deep | primary | background | 6.030 | 6.362 |
| Dark-deep | primary-foreground | primary | 2.823 | 6.197 |
| Dark-deep | accent | card | 5.383 | 5.679 |
| Dark-deep | accent | background | 6.030 | 6.362 |
| Dark-deep | accent-foreground | accent | 2.823 | 6.197 |
| Dark-deep | destructive | card | 5.580 | 5.580 |
| Dark-deep | destructive | background | 6.251 | 6.251 |
| Dark-deep | destructive-foreground | destructive | 6.088 | 6.088 |
| Dark-deep | success | card | 8.706 | 8.706 |
| Dark-deep | success | background | 9.753 | 9.753 |
| Dark-deep | success-foreground | success | 9.500 | 9.500 |
| Dark-deep | warning | card | 6.868 | 6.868 |
| Dark-deep | warning | background | 7.693 | 7.693 |
| Dark-deep | warning-foreground | warning | 7.494 | 7.494 |
| Dark-deep | info | card | 3.649 | 5.624 |
| Dark-deep | info | background | 4.088 | 6.300 |
| Dark-deep | info-foreground | info | 4.165 | 6.136 |
| Dark-deep | role-superadmin | card | 5.747 | 5.747 |
| Dark-deep | role-superadmin | background | 6.437 | 6.437 |
| Dark-deep | role-superadmin-foreground | role-superadmin | 6.270 | 6.270 |
| Dark-deep | role-admin | card | 7.459 | 7.459 |
| Dark-deep | role-admin | background | 8.356 | 8.356 |
| Dark-deep | role-admin-foreground | role-admin | 8.139 | 8.139 |
| Dark-deep | role-member | card | 8.542 | 8.542 |
| Dark-deep | role-member | background | 9.568 | 9.568 |
| Dark-deep | role-member-foreground | role-member | 9.320 | 9.320 |
| Dark-deep | foreground | background | 14.304 | 14.304 |
| Dark-deep | card-foreground | card | 12.769 | 12.769 |
| Dark-deep | popover-foreground | popover | 12.769 | 12.769 |
| Dark-deep | secondary-foreground | secondary | 8.623 | 8.623 |
| Dark-deep | muted-foreground | muted | 6.299 | 6.299 |

The matrix includes the optional Bright/Dark-deep overrides as well as the default Mist/Slate pair. Candidate QA must recompute the ratios from the actual landed tokens and verify the preserved role meaning and real rendered uses.
