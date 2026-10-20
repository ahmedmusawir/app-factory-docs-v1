from pathlib import Path
import datetime, hashlib, json, os, subprocess

E = Path(__file__).resolve().parents[1]
C = json.loads((E / "RAW/context.json").read_text())
ROOT, WT, S = (Path(C[k]) for k in ("root", "execution", "scratch"))
RUN = C["run"]
CAND, PARENT, BASE = (C[k] for k in ("candidate", "parent", "base"))
BRANCH = "docs/sync-doctrine-part2-2026-10-15"

def sha(b):
    return hashlib.sha256(b).hexdigest()

def save(path, obj):
    p = E / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n")

def command(args, cwd=WT, binary_output=None):
    started = datetime.datetime.now(datetime.timezone.utc).isoformat()
    p = subprocess.run(args, cwd=cwd, capture_output=True,
                       env={**os.environ, "GIT_OPTIONAL_LOCKS": "0", "PYTHONDONTWRITEBYTECODE": "1"})
    record = {"command": args, "cwd": str(cwd), "start_utc": started,
              "exit": p.returncode, "stderr": p.stderr.decode(errors="replace")}
    if binary_output:
        target = E / binary_output
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(p.stdout)
        record.update(stdout_file=binary_output, stdout_sha256=sha(p.stdout),
                      stdout_bytes=len(p.stdout))
    elif args[:2] == ["git", "archive"]:
        record.update(stdout_sha256=sha(p.stdout), stdout_bytes=len(p.stdout),
                      stdout_format="tar")
    else:
        record["stdout"] = p.stdout.decode(errors="replace")
    path = E / "COMMANDS.json"
    logs = json.loads(path.read_text()) if path.exists() else []
    logs.append(record)
    save("COMMANDS.json", logs)
    return p

def git(*args, binary_output=None):
    return command(["git", *args], binary_output=binary_output)

def capture_pins(stage):
    commands = {}
    for key, args in [
        ("remote", ["ls-remote", "--heads", "origin", "refs/heads/" + BRANCH, "refs/heads/main"]),
        ("head_parent", ["rev-parse", "HEAD", "HEAD^"]),
        ("branch", ["branch", "--show-current"]),
        ("status", ["status", "--porcelain"]),
        ("local_main", ["rev-parse", "main"]),
        ("commit", ["show", "-s", "--format=%H%n%P%n%an%n%ae%n%aI%n%cI%n%s", CAND]),
    ]:
        p = git(*args)
        commands[key] = {"exit": p.returncode, "stdout": p.stdout.decode(), "stderr": p.stderr.decode()}
    remote = dict(line.split()[::-1] for line in commands["remote"]["stdout"].splitlines())
    valid = (all(v["exit"] == 0 for v in commands.values())
             and remote.get("refs/heads/" + BRANCH) == CAND
             and remote.get("refs/heads/main") == BASE
             and commands["head_parent"]["stdout"].splitlines() == [CAND, PARENT]
             and commands["branch"]["stdout"].strip() == BRANCH
             and not commands["status"]["stdout"]
             and commands["local_main"]["stdout"].strip() == BASE)
    canonical = ["04_REFERENCE_MANUALS/APP_ARCHITECTURE_MANUAL.md",
                 "04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md", "CHANGELOG.md"]
    record = {"utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
              "QA_START_SHA": remote.get("refs/heads/" + BRANCH), "pins_match": valid,
              "commands": commands, "canonical_hashes": {p: sha((WT / p).read_bytes()) for p in canonical}}
    save(stage + ".json", record)
    return record
