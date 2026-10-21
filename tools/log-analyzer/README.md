# Auth Log Analyzer

Parses Linux SSH auth logs and flags IPs with repeated failed logins — a classic first blue-team / SOC detection exercise.

## Run it
```bash
python3 log_analyzer.py sample.log            # included FAKE sample data
python3 log_analyzer.py /var/log/auth.log --threshold 10   # on your OWN machine
```
`sample.log` uses documentation IP ranges (`203.0.113.x` = TEST-NET, RFC 5737) — no real data.

## What I learned
- A burst of failures ≠ proof of compromise: check for a later *success* from the same IP.
- Defenses that stop this class of attack: SSH keys + `PasswordAuthentication no`, fail2ban, MFA, disabling direct root login.
- In real SOC work this becomes a SIEM rule (e.g. "≥10 failures / 5 min / same source").

## Limitations
Parses the common OpenSSH `sshd` text format only; no geo-IP, no live tailing. Educational sample.
