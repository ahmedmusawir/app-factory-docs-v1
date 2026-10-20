import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import *

end = capture_pins("QA_END")
start = json.loads((E / "QA_START.json").read_text())
protected = json.loads((E / "RAW/review_protected_start.json").read_text())
changed = []
for p, digest in protected.items():
    target = ROOT / p
    actual = sha(target.read_bytes()) if target.exists() else None
    if actual != digest:
        changed.append({"path": p, "expected_sha256": digest, "actual_sha256": actual})
stability = {
    "start_pins_match": start["pins_match"],
    "end_pins_match": end["pins_match"],
    "same_remote_tip": end["QA_START_SHA"] == start["QA_START_SHA"] == CAND,
    "same_canonical_hashes": end["canonical_hashes"] == start["canonical_hashes"],
    "review_protected_files": len(protected),
    "review_protected_mismatches": changed,
    "review_protected_unchanged": not changed,
}
save("RAW/stability.json", stability)
print(json.dumps(stability, indent=2))
