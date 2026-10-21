#!/usr/bin/env python3
"""
File Integrity Checker (educational)
-------------------------------------
Computes SHA-256 hashes for files in a directory, saves a baseline,
and later compares against it to detect added / modified / deleted files.

This is a core blue-team idea (real tools: AIDE, Tripwire, OSSEC FIM).

Usage:
    python3 integrity_checker.py baseline  <directory> [baseline.json]
    python3 integrity_checker.py check     <directory> [baseline.json]

For education and use on your own files only.
"""
import hashlib
import json
import sys
from pathlib import Path


def hash_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def scan(directory: Path) -> dict[str, str]:
    results = {}
    for p in sorted(directory.rglob("*")):
        if p.is_file():
            try:
                results[str(p.relative_to(directory))] = hash_file(p)
            except (PermissionError, OSError) as e:
                print(f"  ! skipped {p}: {e}", file=sys.stderr)
    return results


def main() -> int:
    if len(sys.argv) < 3 or sys.argv[1] not in ("baseline", "check"):
        print(__doc__)
        return 1
    mode, directory = sys.argv[1], Path(sys.argv[2])
    baseline_file = Path(sys.argv[3]) if len(sys.argv) > 3 else Path("baseline.json")
    if not directory.is_dir():
        print(f"Error: {directory} is not a directory")
        return 1

    current = scan(directory)

    if mode == "baseline":
        baseline_file.write_text(json.dumps(current, indent=2))
        print(f"✅ Baseline saved: {len(current)} file(s) -> {baseline_file}")
        return 0

    # check mode
    if not baseline_file.exists():
        print(f"Error: baseline not found: {baseline_file} (run 'baseline' first)")
        return 1
    baseline = json.loads(baseline_file.read_text())

    added = sorted(set(current) - set(baseline))
    removed = sorted(set(baseline) - set(current))
    modified = sorted(k for k in current.keys() & baseline.keys() if current[k] != baseline[k])

    for label, items in (("MODIFIED", modified), ("ADDED", added), ("REMOVED", removed)):
        for name in items:
            print(f"{label}: {name}")

    if not (added or removed or modified):
        print("✅ No changes detected. All files match the baseline.")
        return 0
    print(f"\n⚠️  {len(modified)} modified, {len(added)} added, {len(removed)} removed.")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
