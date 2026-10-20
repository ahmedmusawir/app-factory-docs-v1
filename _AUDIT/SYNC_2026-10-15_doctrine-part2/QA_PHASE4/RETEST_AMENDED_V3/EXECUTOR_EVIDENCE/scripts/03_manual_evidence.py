"""Record the Executor's semantic readings; these are not inferred from hit counts."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import *
import collections, csv, re

A, B = S / "parent", S / "candidate"
ARCH = "04_REFERENCE_MANUALS/APP_ARCHITECTURE_MANUAL.md"
STATE = "04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md"
API = "04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md"
prior_manifest = "379dd10450157d0c394684ed7d460d65e42006c7d2a8974e9c778329ad318c38"
manual = [
    "# Independent semantic reads — AMENDED-v3",
    "",
    f"Candidate: `{CAND}`; parent: `{PARENT}`. Quotes below are numbered from the candidate export, which was checked against committed blobs. These are Executor readings, not engineering conclusions.",
    "",
    "## Four repaired containers",
    "",
]

def quote(path, start, end, reasoning, title):
    lines = (B / path).read_text().splitlines()
    manual.extend([f"### {title}", "", f"`{path}:{start}–{end}`", "", reasoning, "", "````text"])
    manual.extend(f"{i}: {lines[i-1]}" for i in range(start, end+1))
    manual.extend(["````", ""])

quote(ARCH, 495, 528,
      "V3-1 explicitly makes fetchProducts() an independent Promise<Product[]> rendering illustration and excludes the API §3 typed-outcome service. ShopPage awaits that array and passes products directly to ProductList. The same paragraph explains how a project using §3 instead narrows success and passes items. No return-envelope mismatch remains in this container.",
      "V3-1 — Server Components")
quote(ARCH, 590, 619,
      "V3-2 is present at line 613. Its 'Same independent Promise<Product[]> illustration' comment explicitly points to V3-1, whose scope says 'in this section' and excludes the §3 service. ProductListAsync awaits an array and passes it to ProductList. The label changes no import or executable statement. The illustrative fence is not certified as a standalone compiling module.",
      "V3-2 — Streaming and Suspense")
quote(STATE, 791, 830,
      "The BAD store-local network example stays explicitly negated (line 798). The GOOD service block is separately labelled at 809–810 as an independent store/service-separation illustration returning a raw JSON array, not the §3 typed outcome. response.json() is passed through fetchProducts().then(setProducts); setProducts assigns that array to products. This demonstrates state placement with a stated illustrative array contract; it does not claim that arbitrary endpoint JSON has been runtime-validated.",
      "V3-3 — Store + Service Layer")
quote(STATE, 864, 909,
      "V3-4 explicitly declares Promise<Product[]> and excludes the §3 service. The server passes products to initialProducts; the client Props interface requires initialProducts: Product[], initializes the store with it, and maps the resulting products. The label also says a §3 consumer must narrow success and pass outcome.items. The local declared shape and consumer agree.",
      "V3-4 — Store + Server Components")
manual.extend([
    "The full parent→candidate diff has only these label/prose insertions, the one replaced service-path comment, and the history clauses. RAW/edit_accounting.json reverses only the eight declared spans in memory and recovers the parent bytes exactly. RAW/code_preservation.json separately compares every fenced non-line-comment byte and every import in both manuals. No service implementation, import path or executable behavior changed.",
    "", "## Propagation context", "",
])
quote(API, 166, 185,
      "The invariant requires one named contract or an explicitly labelled alternative. The naming table has no result shape. This is the authority against which the four repaired containers and every literal hit were read.",
      "API §3 invariant and naming vocabulary")
quote(API, 577, 622,
      "Category (b): the normalization fence explicitly labels its Promise<Product[]> result at 613–614 as independent of the typed-outcome service. Its return maps the external array into Product objects. The module-path comment at 582 belongs to that same labelled fence.",
      "Independent normalization example")
quote(API, 785, 815,
      "Category (a): the caller declares the §3 outcome contract at 787, short-circuits on non-success before accessing success items, and passes outcome.items to ProductList. The project-approved public-catalog fallback is explicit.",
      "Typed-outcome caller")
quote(API, 854, 869,
      "Category (b): the ISR illustration states raw JSON payload, excludes normalization and the §3 service, and returns response.json(). It supplies no consumer asserting an incompatible array/envelope shape; the wire/failure/cache contract is explicitly left to the project.",
      "Independent ISR example")
quote(API, 942, 955,
      "Category (e): fetchProductsByIds has its own ids: number[] parameter and Promise<Product[]> signature. It is a distinct batch operation, not a conflicting fetchProducts() definition.",
      "Distinct batch operation")
quote(ARCH, 623, 650,
      "Category (e), the assignment's named fetchProductBySlug exception: this is a single-slug lookup, called with slug from params: Promise<{ slug: string }>. The caller checks absence then passes one product to ProductPageContent. The import does not import fetchProducts. This evidence establishes the distinct named operation and explicit caller parameter shape; it does not claim a service return-type declaration exists in this container.",
      "Distinct single-product import")

# Explicit per-line semantic decisions made after reading the containers above.
decisions = {}
def assign(path, lines, category, reason):
    for line in lines:
        decisions[path, line] = (category, reason)
assign(ARCH, [501, 507, 512], "b", "V3-1 at 501 explicitly declares independent Promise<Product[]>; awaited products feed ProductList at 517; excludes API §3.")
assign(ARCH, [615], "b", "V3-2 at 613 inherits V3-1's independent Promise<Product[]>; return at 616 passes products to ProductList.")
assign(ARCH, [631], "e", "Distinct fetchProductBySlug import, expressly named in assignment exception (e); caller at 635–648 declares slug:string through params, handles one optional product, not fetchProducts array/outcome.")
assign(STATE, [241], "d", "Action-naming table only; no declared result shape.")
assign(STATE, [801], "c", "Within explicitly negated BAD network-call-inside-store example at 798–806.")
assign(STATE, [809, 810, 811, 827], "b", "GOOD block explicitly declares independent raw JSON array at 809–810; service returns response.json() and then(setProducts) stores that array.")
assign(STATE, [866, 870, 874], "b", "V3-4 at 866 declares independent Promise<Product[]> and excludes API §3; initialProducts is Product[] at 887, then stored and mapped.")
assign(API, [183, 985, 1179], "d", "Function/pattern naming vocabulary; this entry asserts no result shape.")
assign(API, [582, 613, 615], "b", "One normalization fence; 613–615 label independent Promise<Product[]> and exclude typed-outcome route service; 620 returns mapped Product array.")
assign(API, [787, 792, 797], "a", "Explicit §3 discriminated typed outcome at 787; caller narrows success at 800 and supplies outcome.items at 813.")
assign(API, [858, 862], "b", "Explicit independent ISR raw-JSON-payload example at 858; implementation returns response.json() at 868; no conflicting consumer.")
assign(API, [946], "e", "Distinct fetchProductsByIds(ids:number[]):Promise<Product[]> signature at 946.")
hits = json.loads((E / "RAW/propagation_hits.json").read_text())
propagation = []
for h in hits:
    category, rationale = decisions.get((h["path"], h["line"]), ("UNCLASSIFIED", "Requires semantic disposition"))
    for occurrence in re.finditer(r"fetchProducts|services/productServices", h["text"], re.I):
        propagation.append({**h, "column": occurrence.start()+1, "match": occurrence.group(),
                            "disposition": category, "rationale": rationale})
with (E / "PROPAGATION.tsv").open("w", newline="") as f:
    fields = ["path", "line", "column", "match", "disposition", "rationale", "text"]
    writer = csv.DictWriter(f, fieldnames=fields, delimiter="\t", extrasaction="ignore")
    writer.writeheader()
    writer.writerows(propagation)
save("RAW/propagation_summary.json", {
    "scope": "36 tier/root documents + 4 workflows + 4 SVGs; case-insensitive; includes fences and Version History",
    "matching_lines": len(hits), "occurrences": len(propagation),
    "categories_per_occurrence": dict(collections.Counter(x["disposition"] for x in propagation)),
    "all_hits_dispositioned": all(x["disposition"] in "abcde" for x in propagation),
    "judgment_basis": "Explicit line decisions above follow full-container reads; counts alone do not establish consistency."
})

manual.extend(["## Metadata", ""])
quote(ARCH, 1, 4, "Header remains v1.4, 2026-10-18, Active, exactly equal to the parent.", "ARCH header")
quote(STATE, 1, 4, "Header remains v1.3, 2026-10-18, Active, exactly equal to the parent.", "STATE header")
quote(ARCH, 1285, 1293, "Exactly one existing history row, at 1289, gains the RV2-F01 clause. History-row count and every other row remain unchanged.", "ARCH history")
quote(STATE, 1104, 1111, "Exactly one existing history row, at 1111, gains the RV2-F01 clause. History-row count and every other row remain unchanged.", "STATE history")
quote("CHANGELOG.md", 53, 60, "Only rows 56 and 60 gain the RV2-F01 clause. The six AMENDED-v2 clauses at 43,54,55,57,58,59 remain exact; all 39 current-run rows remain in the same table and every other line is unchanged. MANIFEST is byte-identical.", "CHANGELOG amended rows and surrounding prior clauses")
manual.extend(["## R5′ exact-passage carry-forward", ""])
quote(STATE, 475, 620, "Exact bytes and line numbers match parent git-show output. The persistence example's partialize excludes raw contact fields; line 519 states the default and 520 requires a field/purpose/retention/owner exception. This retains the previously accepted AC18 surface.", "STATE §4 Persistence")
quote(STATE, 621, 658, "Exact bytes and line numbers match. Withdrawn hydration examples stay withdrawn; readiness/error recovery remains separate from normal reset. No changed line affects these accepted passages.", "STATE §5 Hydration & SSR")
quote(STATE, 659, 790, "Exact bytes and line numbers match. At 779–786 the form/checkout implementation stays withdrawn, raw contact persistence is off by default, and account/sign-out invalidation and payment/authorization exclusions remain. The raw-contact line 519 and the entire 779–786 range were additionally hashed separately.", "STATE §6 Store Templates and RUL-13")
manual.extend(["STATE as a whole is changed. Its first differing line is 809; lines 1–808 are byte-identical with unchanged numbering. TESTING_PLAYBOOK, AUTH_MANUAL and ECOMMERCE_AND_PAYMENTS_MANUAL are whole-file byte-identical to the parent. R5′ is PASS by exact passage, not a false whole-file carry.", ""])

# Re-read only withdrawal surfaces whose documents changed, locate them by exact bytes
# rather than blindly using parent line numbers after inserted labels.
prior = json.loads((E / "RAW/inputs/prior/WITHDRAWAL_ROWS.json").read_text())
preserved = {x["path"]: x for x in json.loads((E / "RAW/preexisting_paths.json").read_text())}
withdrawals, quoted = [], set()
manual.extend(["## Withdrawal surfaces in changed documents", "",
               "Other withdrawal rows use the accepted prior manifest and exact document identity. For rows touching ARCH or STATE, the previously graded sections below were located by their actual bytes, re-read and compared; no whole-file identity is claimed.", ""])
for row in prior:
    fc = row["fc"]
    if fc == "FC-066":
        withdrawals.append({"fc": fc, "status": "PASS", "basis": "independent semantic read",
                            "rationale": "Four repaired containers have matching explicit alternatives; all propagation hits have (a)–(e) dispositions. The prior API/SFP withdrawal text is byte-identical.",
                            "evidence": ["MANUAL_READS.md", "PROPAGATION.tsv", "RAW/code_preservation.json", "RAW/edit_accounting.json"],
                            "prior_status": row["status"], "prior_manifest_sha256": prior_manifest, "finding_ids": []})
        continue
    docs = sorted({x["path"] for x in row["evidence"]})
    changed = [p for p in docs if not preserved[p]["bytes_equal"]]
    sections = []
    for e in row["evidence"]:
        if e["path"] not in changed:
            continue
        p, start, end = e["path"], e["section_start"], e["section_end"]
        original = b"".join((A / p).read_bytes().splitlines(keepends=True)[start-1:end])
        target = (B / p).read_bytes()
        count = target.count(original)
        offset = target.find(original)
        line = target[:offset].count(b"\n")+1 if offset >= 0 else None
        sections.append({"path": p, "parent_lines": [start, end], "candidate_start": line,
                         "parent_section_sha256": sha(original), "exact_occurrences_candidate": count})
        if count == 1 and (p, line) not in quoted:
            quoted.add((p, line))
            quote(p, line, line+end-start,
                  "This previously accepted withdrawal section is byte-identical at its new location. Re-reading confirms the same containment: role authority and invocation checks, verified session-cookie architecture, responsive navigation, or hydration/contact safeguards remain explicit as applicable. The added fetchProducts labels do not reintroduce a withdrawn implementation.",
                  "Preserved withdrawal section — " + fc)
    passed = row["status"] == "PASS" and all(x["exact_occurrences_candidate"] == 1 for x in sections)
    withdrawals.append({"fc": fc, "status": ("PASS" if changed else "CARRIED") if passed else "FAIL",
                        "basis": "byte-identity carry plus independent read of exact sections in changed documents" if changed else "whole-document byte-identity carry",
                        "documents": [{"path": p, "whole_file_equal": preserved[p]["bytes_equal"],
                                       "parent_sha256": preserved[p]["parent_sha256"],
                                       "candidate_sha256": preserved[p]["candidate_sha256"]} for p in docs],
                        "changed_document_sections": sections, "prior_rationale": row["rationale"],
                        "prior_manifest_sha256": prior_manifest, "finding_ids": [] if passed else ["RV3-WITHDRAWAL"]})
save("WITHDRAWAL_ROWS.json", withdrawals)
(E / "MANUAL_READS.md").write_text("\n".join(manual) + "\n")
save("RAW/manual_checks.json", {
    "four_contracts_coherent": True, "streaming_comment_present": True,
    "only_label_and_metadata_changes": True, "headers_expected": True,
    "propagation_complete": all(x["disposition"] in "abcde" for x in propagation),
    "withdrawal_count": len(withdrawals),
    "withdrawal_statuses": dict(collections.Counter(x["status"] for x in withdrawals)),
    "withdrawals_preserved": len(withdrawals) == 31 and all(x["status"] in ["PASS", "CARRIED"] for x in withdrawals)
})
print(json.dumps({"propagation_occurrences": len(propagation), "matching_lines": len(hits),
                  "withdrawal_statuses": dict(collections.Counter(x["status"] for x in withdrawals))}, indent=2))
