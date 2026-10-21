#!/usr/bin/env python3
"""
Auth Log Analyzer (educational)
--------------------------------
Reads a Linux auth log (e.g. /var/log/auth.log) and reports:
  - total failed / accepted logins
  - source IPs with repeated failures (possible brute-force attempts)
  - most-targeted usernames

Usage:
    python3 log_analyzer.py <logfile> [--threshold N]   # default N=5

Try it with the included fake data:  python3 log_analyzer.py sample.log
For education and analysis of logs from systems you own/administer only.
"""
import re
import sys
from collections import Counter
from pathlib import Path

FAILED = re.compile(r"Failed password for (?:invalid user )?(\S+) from (\d+\.\d+\.\d+\.\d+)")
ACCEPTED = re.compile(r"Accepted password for (\S+) from (\d+\.\d+\.\d+\.\d+)")


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    threshold = 5
    if "--threshold" in sys.argv:
        threshold = int(sys.argv[sys.argv.index("--threshold") + 1])
    if not args:
        print(__doc__)
        return 1

    logfile = Path(args[0])
    if not logfile.exists():
        print(f"Error: file not found: {logfile}")
        return 1

    failed_by_ip, failed_by_user, accepted = Counter(), Counter(), Counter()
    for line in logfile.read_text(errors="ignore").splitlines():
        if m := FAILED.search(line):
            user, ip = m.groups()
            failed_by_ip[ip] += 1
            failed_by_user[user] += 1
        elif m := ACCEPTED.search(line):
            accepted[m.group(2)] += 1

    print(f"Log file:        {logfile}")
    print(f"Failed logins:   {sum(failed_by_ip.values())}")
    print(f"Accepted logins: {sum(accepted.values())}")

    print(f"\n🚨 IPs with >= {threshold} failed logins (possible brute force — investigate, don't assume):")
    flagged = [(ip, n) for ip, n in failed_by_ip.most_common() if n >= threshold]
    print("\n".join(f"  {ip}: {n} failures" for ip, n in flagged) or "  (none)")

    print("\n🎯 Most-targeted usernames:")
    print("\n".join(f"  {u}: {n}" for u, n in failed_by_user.most_common(10)) or "  (none)")

    print("\n💡 Defender next steps: check if a flagged IP later succeeded, review fail2ban/SSH "
          "key-only auth, disable password login for root, and alert on this pattern in your SIEM.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
