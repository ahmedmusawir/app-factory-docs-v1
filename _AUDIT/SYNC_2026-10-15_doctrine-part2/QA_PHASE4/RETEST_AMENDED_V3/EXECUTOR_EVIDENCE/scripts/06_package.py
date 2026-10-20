"""Verify sealed evidence, create one ZIP, deliver without overwriting, log handback."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import *
import shutil, zipfile

manifest = E / "SHA256SUMS.txt"
expected = {}
for line in manifest.read_text().splitlines():
    digest, name = line.split(maxsplit=1)
    expected[name] = digest
files = {str(p.relative_to(E)): p for p in E.rglob("*") if p.is_file()}
assert set(files) == set(expected) | {"SHA256SUMS.txt"}
assert all(sha(files[name].read_bytes()) == digest for name, digest in expected.items())
manifest_hash = sha(manifest.read_bytes())
now = datetime.datetime.now(datetime.timezone.utc)
zip_name = "QA_AMENDED_V3_EXECUTOR_26b050f_" + now.strftime("%Y-%m-%d") + ".zip"
temporary_zip = S / zip_name
with zipfile.ZipFile(temporary_zip, "x", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
    for name, source in sorted(files.items()):
        z.write(source, "EXECUTOR_EVIDENCE/" + name)
with zipfile.ZipFile(temporary_zip) as z:
    assert z.testzip() is None
    assert set(z.namelist()) == {"EXECUTOR_EVIDENCE/" + name for name in files}
    assert all(sha(z.read("EXECUTOR_EVIDENCE/" + name)) == digest for name, digest in expected.items())
    assert sha(z.read("EXECUTOR_EVIDENCE/SHA256SUMS.txt")) == manifest_hash
destination = Path("/home/moose/Downloads") / zip_name
with destination.open("xb") as target, temporary_zip.open("rb") as source:
    shutil.copyfileobj(source, target)
zip_hash = sha(destination.read_bytes())
assert zip_hash == sha(temporary_zip.read_bytes())
counts = json.loads((E / "RAW/result_counts.json").read_text())
start = json.loads((E / "QA_START.json").read_text())
receipt = {"zip": str(destination), "zip_sha256": zip_hash, "manifest_sha256": manifest_hash,
           "manifest_rows": len(expected), "zip_members": len(files), "sealed_inventory_verified": True,
           "zip_inventory_verified": True, "delivery_bytes_verified": True,
           "QA_START_SHA": start["QA_START_SHA"], "counts": counts,
           "evidence": str(E), "utc": now.isoformat(), "next_owner": "Fable", "closeout": "12 PENDING"}
(S / "DELIVERY_RECEIPT.json").write_text(json.dumps(receipt, indent=2) + "\n")
summary = (
    f"Completed: **{counts['PASS']} PASS, {counts['CARRIED']} CARRIED, {counts['FAIL']} FAIL, {counts['BLOCKED']} BLOCKED** across all 12 entries. "
    "The repaired contract labels are consistent, protected evidence is preserved, and lints pass.\n\n"
    f"[Download evidence ZIP]({destination})\n\n"
    f"- ZIP SHA-256: `{zip_hash}`\n"
    f"- Actual QA_START_SHA: `{start['QA_START_SHA']}`\n"
    f"- Evidence-manifest SHA-256: `{manifest_hash}`\n"
    f"- [Evidence directory]({E})\n\n"
    "All 12 closeout transitions remain pending. Stopped for Fable’s verdict; no merge or release authorized.\n"
)
response = ROOT / "agent_docs/RESPONSES" / ("response_" + now.strftime("%Y-%m-%d_%H%M%S") + "_amended-v3-executor-handback.md")
response.write_text(summary)
with (ROOT / "agent_docs/SESSIONS/session_2026-10-20.md").open("a") as f:
    f.write("\n### " + now.isoformat() + " — COMPLETE (independent QA Executor; Fable verdict pending)\n\n"
            f"**Candidate:** {CAND}. **Results:** {counts}. **Evidence:** {E}.\n"
            f"**Manifest SHA256:** {manifest_hash}; {len(expected)} files verified after sealing.\n"
            f"**ZIP:** {destination}; SHA256 {zip_hash}; {len(files)} members verified against inventory; delivery bytes verified.\n"
            "**Files changed:** New RETEST_AMENDED_V3/EXECUTOR_EVIDENCE, scratch, review response/session/RECOVERY, one Downloads ZIP only. "
            "All1,461 protected review-run files unchanged. No Git mutations, repairs or transitions.\n"
            "**Next:** STOP for Fable successor verdict. All12 closeout transitions pending; no merge/release authority.\n")
recovery = ROOT / "RECOVERY.md"
old_recovery = recovery.read_text()
recovery.write_text(
    "# Recovery State\n\n"
    f"Last action: Independent QA Executor completed AMENDED-v3 bounded retest at {CAND}: "
    f"{counts['PASS']} PASS / {counts['CARRIED']} CARRIED / {counts['FAIL']} FAIL / {counts['BLOCKED']} BLOCKED. "
    f"Evidence `{E.relative_to(ROOT)}`; manifest SHA256 `{manifest_hash}`.\n"
    "Pending: Fable adjudication and successor verdict. All12 closeout transitions remain pending. No Git mutation, repair, merge or release.\n"
    f"Next step: Fable reviews `{destination}`; ZIP SHA256 `{zip_hash}`. "
    f"Response `{response.relative_to(ROOT)}`. Executor stopped.\n\n"
    "## Historical checkpoints (preserved)\n\n" + old_recovery)
print(summary)
print("Delivery receipt: " + str(S / "DELIVERY_RECEIPT.json"))
