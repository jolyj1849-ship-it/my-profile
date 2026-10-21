# File Integrity Checker

Hashes every file in a folder (SHA-256), saves a **baseline**, and later reports what was **modified / added / removed**. Defenders use this idea (File Integrity Monitoring) to spot tampering on servers.

## Run it (no installs — Python 3 standard library)
```bash
# 1) Create a baseline of a folder you own
python3 integrity_checker.py baseline /path/to/folder

# 2) Later, check for changes
python3 integrity_checker.py check /path/to/folder
```
Exit codes: `0` = no changes, `2` = changes found (handy for scripting/cron).

## What I learned
- Hashing detects *change*, not *intent* — a changed file may be a legit update; a human still investigates.
- Protect the baseline itself (store a copy off the machine), or an attacker could just re-baseline.
- Real-world equivalents: AIDE, Tripwire, Wazuh/OSSEC FIM.

## Limitations
Single-machine, no scheduling/alerting, follows all files under the folder. Educational sample — use a maintained FIM tool in production.
