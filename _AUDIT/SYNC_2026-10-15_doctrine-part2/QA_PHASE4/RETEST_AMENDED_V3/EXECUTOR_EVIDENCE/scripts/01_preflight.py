import sys
from pathlib import Path, PurePosixPath
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import *
import stat, tarfile, zipfile, io

source = Path("/home/moose/Downloads/FACTORY_AMENDED_V3_EXECUTION_HANDOFF_2026-10-20_104051.zip")
expected = "5efa6fee26d94598fc6687e22b9cd50bec0b282bb4cf2196ba1b06283cd60485"
assert sha(source.read_bytes()) == expected
destination = S / "handoff"
destination.mkdir(exist_ok=True)
with zipfile.ZipFile(source) as z:
    names = z.namelist()
    assert len(names) == len(set(names))
    for info in z.infolist():
        p = PurePosixPath(info.filename)
        assert not p.is_absolute() and ".." not in p.parts and "\\" not in info.filename
        assert not stat.S_ISLNK(info.external_attr >> 16)
    manifests = [n for n in names if n.endswith("SHA256SUMS.txt")]
    assert len(manifests) == 1
    manifest = manifests[0]
    rows = []
    for line in z.read(manifest).decode().splitlines():
        digest, name = line.split(maxsplit=1)
        name = name.lstrip("* ")
        actual = sha(z.read(name))
        rows.append({"path": name, "expected": digest, "actual": actual, "match": actual == digest})
    assert len(rows) == 38 and all(r["match"] for r in rows)
    assert set(names) == {r["path"] for r in rows} | {manifest}
    if any(destination.iterdir()):
        assert all((destination / n).read_bytes() == z.read(n) for n in names)
    else:
        z.extractall(destination)
save("RAW/handoff_inventory.json", {"zip": str(source), "sha256": expected, "safe_paths": True,
                                  "exact_inventory": True, "rows": rows, "members": names})
print("Handoff: safe member paths and 38/38 inventory hashes verified")
if (E / "QA_START.json").exists():
    save("RAW/initial_network_attempt.json", json.loads((E / "QA_START.json").read_text()))
start = capture_pins("QA_START")
if not start["pins_match"]:
    raise SystemExit("BLOCKED initial pins; inspect QA_START.json; do not export or grade")
chain = [BASE, "ef35d26d82f1904da6ed33663ad647e4ee16fe98",
         "20f71ee932ed21c0878cb3a0f39c6fbe90d0a793", PARENT, CAND]
ancestry = []
for a, b in zip(chain, chain[1:]):
    p = git("merge-base", "--is-ancestor", a, b)
    ancestry.append({"ancestor": a, "descendant": b, "exit": p.returncode})
save("RAW/ancestry.json", ancestry)
assert all(r["exit"] == 0 for r in ancestry)
assert git("show", "-s", "--format=%P", CAND).stdout.decode().strip() == PARENT
for label, ref in [("parent", PARENT), ("candidate", CAND)]:
    target = S / label
    target.mkdir()
    p = git("archive", "--format=tar", ref)
    # Archive stdout is binary: replace its command log field with a durable digest,
    # retaining extracted-tree inventories in subsequent checks.
    logs = json.loads((E / "COMMANDS.json").read_text())
    logs[-1].pop("stdout", None)
    logs[-1].update(stdout_sha256=sha(p.stdout), stdout_bytes=len(p.stdout),
                    stdout_export=str(target), stdout_format="tar")
    save("COMMANDS.json", logs)
    assert p.returncode == 0
    with tarfile.open(fileobj=io.BytesIO(p.stdout)) as t:
        for member in t.getmembers():
            path = PurePosixPath(member.name)
            assert not path.is_absolute() and ".." not in path.parts
            assert member.isfile() or member.isdir(), "Unsupported archive member"
        t.extractall(target, filter="data")
print("Initial pins and ancestry match; fresh committed parent/candidate exports ready")
