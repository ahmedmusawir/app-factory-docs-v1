#!/usr/bin/env python3
"""Fable (QA Lead) — independent adjudication checks for Executor findings F01–F07.
Read-only Git. Writes only ADJUDICATION_EVIDENCE.json next to this script.
Run: python3 -B -I qa_adjudicate.py
"""
import json, os, re, subprocess, datetime
W = "/home/moose/Documents/app-factory-docs-sync-execution"
RUN = "_AUDIT/SYNC_2026-10-15_doctrine-part2"
B = "9c179392f79b70da099121fc357d3107ad3bb86e"
T = "20f71ee932ed21c0878cb3a0f39c6fbe90d0a793"
HERE = os.path.dirname(os.path.abspath(__file__))

def blob(rev, path):
    return subprocess.run(["git", "show", f"{rev}:{path}"], cwd=W, capture_output=True).stdout.decode("utf-8", "replace")

def count(rev, path, needle): return blob(rev, path).count(needle)
def lines(rev, path, needle): return [i + 1 for i, l in enumerate(blob(rev, path).splitlines()) if needle in l]

ENG = "02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md"; TST = "03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md"
DB = "04_REFERENCE_MANUALS/DATABASE_MANUAL.md"; API = "04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md"
AUTH = "04_REFERENCE_MANUALS/AUTH_MANUAL.md"; ECOM = "04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md"
STATE = "04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md"; STRIPE = "04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md"
FFM = "03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md"

def span(path, needle):
    return {"path": path, "needle": needle, "base_count": count(B, path, needle), "cand_count": count(T, path, needle), "cand_lines": lines(T, path, needle)[:12]}

ev = {"seat": "Fable (QA Lead)", "time": datetime.datetime.now().astimezone().isoformat(), "candidate": T, "base": B, "findings": {}}
ev["findings"]["F01"] = {"spans": [span(ENG, "different author, different moment"), span(ENG, "the Architect authors `DATA_CONTRACT.md` from the approved APP_BRIEF before Design")],
    "note": "Line 176 retained from BASE beside the corrected 175; both pipelines now name the Architect."}
ev["findings"]["F02"] = {"spans": [span(ENG, "ENGINEER → OPERATIONS HANDOFF"), span(ENG, "Engineer hands off to Operations/Deployment"), span(ENG, "QAM/")],
    "note": "§17 tree and lead sentence unchanged from BASE; QAM sentence inserted above them; tree omits QAM/ and ACCEPTANCE_SPEC; sentence routes to Operations without QA."}
ev["findings"]["F03"] = {"spans": [span(ENG, "the filesystem wins")], "base_sites": lines(B, ENG, "filesystem wins"),
    "note": "BASE had 4 sites; the approved proposal replaced 3 (quotes at 103/125/1582) and left the kit-track diagram site."}
ev["findings"]["F04"] = {"spans": [span(TST, "seedSubscription"), span(TST, "export const supabaseAdmin = createClient"), span(DB, "This is appropriate for:\n- API routes"), span(API, "export const fetchProducts = async (): Promise<Product[]>"), span(API, "const { items: products, error } = await fetchProducts()"), span(API, "export const fetchProducts = async () => {")],
    "certified": {"FC-022": "E2E recipe seeds subscriptions through an admin client ... nothing checks approved test project (PART1_FINDINGS_DISPOSITION.md)",
                  "FC-038": "DATABASE §5 lists 'API routes' generally as a reason to bypass RLS (named defect surface; map §B FC-038)",
                  "FC-066": "verification intent: every fetchProducts occurrence matches one declared contract or a labeled alternative (map §B FC-066)"},
    "note": "All three retained recipes pre-exist at BASE; PROPAGATION.tsv marked them CONSISTENT; the certified defect mechanisms remain live beside the inserted invariants."}
ev["findings"]["F05"] = {"spans": [span(STATE, "Do not persist raw contact details by default"), span(AUTH, "contact"), span(TST, "contact"), span(ECOM, "Personal fields follow the approved account-transition and retention policy"), span(AUTH, "Don't store sensitive data in localStorage")],
    "note": "RUL-13 default stated only in STATE; AUTH has the older 'sensitive data' bullet; TESTING none; ECOMMERCE refers to a policy without stating the default."}
ev["findings"]["F06"] = {"spans": [span(STRIPE, "### GCP Cloud Run Deployment"), span("03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md", "No platform procedure is Factory doctrine yet")],
    "map": "PROPAGATION.tsv rows 1435/1628 retain STRIPE §13 lines as CONSISTENT; FC-088 map outcome routed to DEPLOYMENT_PLAYBOOK; spec §1 excludes platform procedures (DEC-18 remainder) from failure.",
    "note": "Pre-existing project-stack checklist; no doctrine claim text; authority gap is real but excluded by contract → follow-up."}
ev["findings"]["F07"] = {"spans": [span(FFM, "CURRENT_APP"), span("01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md", "CURRENT_APP"), span("02_PIPELINE_AGENTS/HANDOFF_PACKAGE_PLAYBOOK.md", "CURRENT_APP")],
    "ruling_text": "RUL-14: 'Do not invent a universal project landing path or require a release tag.'",
    "map": "Approved edits removed CURRENT_APP from FFM Appendix B boot/resume prompts and authoring step 15 (AC14 PASS); FFM §1/§3/§16/§17 keep the FFM's own in-kit module location convention (pre-existing, not invented); SFP/HANDOFF hits are labelled historical pointers.",
    "note": "Module location convention of the FFM pattern ≠ Hub doctrine landing path; not a failure under RUL-14 → follow-up wording harmonization."}
json.dump(ev, open(os.path.join(HERE, "ADJUDICATION_EVIDENCE.json"), "w"), indent=2, ensure_ascii=False)
for k, v in ev["findings"].items():
    print(k, [(s["path"].split("/")[-1], s["base_count"], s["cand_count"], s["cand_lines"][:6]) for s in v["spans"]])
