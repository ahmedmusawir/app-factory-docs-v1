"""Doctrine lint runner — executes all four lints; exit 1 if any fail."""
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
LINTS = ["encoding_lint.py", "retired_terms_lint.py", "versioned_refs_lint.py", "header_lint.py"]


def main():
    print("=== DOCTRINE LINTS ===")
    worst = 0
    for script in LINTS:
        print(f"\n--- {script} ---")
        rc = subprocess.call([sys.executable, str(HERE / script)])
        worst = max(worst, rc)
    print("\n=== RESULT:", "FAIL" if worst else "PASS", "===")
    return worst


if __name__ == "__main__":
    sys.exit(main())
