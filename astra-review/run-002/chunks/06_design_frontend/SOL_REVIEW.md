# SOL SECONDARY REVIEW — CHUNK 06 DESIGN / FRONTEND

## STATUS

COMPLETE

## SOURCE

ASTRA_REVIEW.md for Chunk 06

## SOL VERDICT

Accept all 12 Astra defect findings.
No severity changes.

## DISPOSITIONS

- **C06-D01 — HIGH — ACCEPT HIGH**
  The theming engagement path can omit required HTML/PNG artifacts even though the governing Handbook and Engineer consumer require the locked visual package. This is a real producer/consumer contract break.

- **C06-D02 — HIGH — ACCEPT HIGH**
  Positive portal examples reproduce the exact hidden-sidebar/no-mobile-trigger pattern that Rule Zero prohibits and bypass the existing reusable shell. This can create unreachable navigation on mobile.

- **C06-D03 — HIGH — ACCEPT HIGH**
  The advertised drop-in palette claims verification while multiple ordinary-text color pairs fail the stated AA requirement. This is a repeatable shared design-system accessibility defect, not a subjective palette disagreement.

- **C06-D04 — MEDIUM — ACCEPT MEDIUM**
  Rail breakpoint rules conflict across governing documents and examples.

- **C06-D05 — MEDIUM — ACCEPT MEDIUM**
  Token inventory and setup quick paths have drifted from the canonical token contract and Tailwind/version-aware setup rules.

- **C06-D06 — MEDIUM — ACCEPT MEDIUM**
  Positive examples explicitly teach bypassing semantic colors even though governing doctrine forbids that pattern.

- **C06-D07 — MEDIUM — ACCEPT MEDIUM**
  The dark-mode example introduces a second controller beside the kit/provider ownership model.

- **C06-D08 — MEDIUM — ACCEPT MEDIUM**
  The replacement Button recipe contradicts its advertised variant/composition API and breaks documented asChild usage.

- **C06-D09 — MEDIUM — ACCEPT MEDIUM**
  The Button recipe violates the Factory's documented 44px target floor.

- **C06-D10 — MEDIUM — ACCEPT MEDIUM**
  The proposed Grid dynamically constructs Tailwind class names that are not reliably discoverable by the scanner.

- **C06-D11 — LOW — ACCEPT LOW**
  Canonical cross-reference paths do not resolve in the reviewed DocSet.

- **C06-D12 — LOW — ACCEPT LOW**
  The blanket horizontal-scroll prohibition conflicts with intentionally contained tab/carousel scrolling patterns.

## ROOT PATTERNS OBSERVED BY SOL

1. **Canonical rule vs copyable-example drift.**
   Strong governing rules exist, but later copyable examples violate them.

2. **Duplicate executable truth tables.**
   Breakpoints and token inventories are repeated across docs and drift independently.

3. **Kit-consumption doctrine is not consistently enforced.**
   Several examples rebuild or bypass capabilities the kit already owns.

4. **Verification claims are sometimes stronger than the evidence.**
   Printed recipes can appear "verified" while failing the actual governing requirement.

## SUGGESTIONS

- **C06-S01 — ACCEPT FOR LATER CONSIDERATION**
  Reproducible visual capture/comparison manifest.
  Do not make pixel-diff infrastructure mandatory for every project.

- **C06-S02 — ACCEPT FOR LATER CONSIDERATION**
  Small accessibility evidence matrix separating design responsibility from implemented-browser verification.

## CROSS-DOMAIN ITEMS — CARRY TO SYNTHESIS, DO NOT RESOLVE HERE

- thin-page / server-fetching authority
- kit authority vs token migration
- desktop-only exception authority
- nonvisual app routing
- KIP deferral/unblock path
- UI_SPEC approval-recording defaults

## PRESERVATION RULE

Do not weaken the strong design contract while correcting drift.

Preserve:
- semantic-token discipline
- human design lock points
- mobile reachability
- kit reuse
- HTML as build reference
- PNG as fidelity target
- independent QA separation

## FINAL SOL CHUNK 06 VERDICT

ALL 12 DEFECTS ACCEPTED.
NO SEVERITY CHANGES.
2 SUGGESTIONS ACCEPTED FOR LATER CONSIDERATION.
CROSS-DOMAIN CANDIDATES CARRIED TO SYNTHESIS.
