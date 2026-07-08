# ✅ WAVE 4 — DOC 1 COMPLETE: AUTH_MANUAL → v1.3 (the F-042 correction)

**File:** `4_MANUAL-AUTH_MANUAL_v1_2.md` (security-classed edit; approved before/afters honored verbatim)

## CHANGES MADE

| # | Change | Finding |
|---|--------|---------|
| 1 | Standard header (v1.3 · 2026-07-08 · Tier 4) + role-doctrine banner line; v1.2 changelog moved to the new history table | F-018 |
| 2 | **Key Principle #5** → "Table-driven roles" (approved AFTER, verbatim): `user_roles` = single source of truth; metadata = creation-time transport via protected channel; authz NEVER read from it | F-042 |
| 3 | **"User Metadata Schema" → "Where Roles Live"** (approved AFTER): table home + locked admin path; transport-not-storage nuance; ⛔ forbidden (authz reads from metadata = recon Q3.4 smell; role writes outside protected channel); hardening-ticket reference — **the vector is NOT documented** | F-042 |
| 4 | **§8 RBAC:** metadata-reading `getUserRole` implementation REPLACED with the AppRole type + canonical-path description + 📁 read-the-kit-on-disk pointer (recon Q3.2/Q5.3) + ⛔ line. No fabricated kit code (D-015 boundary, ruling 3) | F-042 |
| 5 | **§5 store:** legacy-shape advisory box (`is_qr_*` = QR-era metadata flags; verify store on disk, recon Q3.6; display-hints-only rule); Pattern 4 gets a pointer note | F-042 |
| 6 | **Troubleshooting** realigned: "check role in metadata" → check `user_roles` row/trigger; Issue 5 causes/fixes rewritten to the table model | F-042 |
| 7 | Registration-flow step 5 corrected (trigger applies role INTO `user_roles` from the transport) | F-042 |
| 8 | Cross-refs canonical (handbook/registry/frontend-first, lines 106–108) | F-032, F-011 |
| 9 | Version History table 1.0 → 1.3 (D-018) | F-018 |

## GATES

Live "Metadata-driven" / "not separate tables": **0** (one history-row quote) · `user_roles` doctrine present ×12 · advisories ×3 · 3-class encoding **0** · `_v` live refs **0** · header ✓ · §0 antibody + `src/proxy.ts` currency untouched ✓

## THINGS I DIDN'T TOUCH

§0 anti-authService (the F-039 antibody), client setup, API routes reference, session middleware, security best practices, components — all as-is. Legacy `is_qr_*` snippet BODIES retained under advisories (see boundary note).

## CONCERNS

1. **QUEUED KIT-VERIFICATION TOUCH (tracked; pairs with the kit signup-vector ticket):** resync AUTH §5/§10 code samples + the `is_qr_*` naming (64 in-snippet instances) against the kit on disk — store shape (Q3.6), `get-user-role.ts` (Q3.2), `setup.sql` trigger + `user_roles` DDL (Q5.2/Q5.3). Honest marking was chosen over fabrication per ruling 3.
2. The signup flow's anon-path metadata payload remains documented as kit behavior (factual); its hardening is the kit ticket's job, referenced without detail.

## Suggested commit

wave4(auth): v1.3 — F-042 table-role doctrine, transport nuance, D-015 pointers, F-032
