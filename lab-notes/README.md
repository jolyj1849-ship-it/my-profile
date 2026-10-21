# Home Lab Notes

My practice environment. Everything runs on **my own computer** in virtual machines on a **host-only / isolated network**, so lab traffic never touches the internet or anyone else's systems.

## Setup (VirtualBox — free)
1. Install VirtualBox + Extension Pack.
2. Create a **Host-only Adapter** network (e.g. `192.168.56.0/24`) — VMs can talk to each other and my host, not the internet.
3. VMs:
   - **Kali Linux** — testing tools (lab use only)
   - **Ubuntu Server 22.04+** — target/defense practice, log source
   - **Metasploitable 2 / DVWA (Docker)** — intentionally vulnerable practice targets
   - **Windows 10** — hardening & Event Log practice
4. Snapshot every VM before experiments ("clean state") so I can roll back safely.
5. Keep the host machine patched; never bridge a vulnerable VM to my home Wi-Fi network.

## Rules I Follow In The Lab
- Scan/probe **only** lab VM IP addresses (I keep a list taped next to my monitor).
- Vulnerable apps (DVWA etc.) run locally with Docker bound to `127.0.0.1` or the host-only network — never exposed online.
- No real passwords/password reuse in the lab; lab credentials are unique throwaways.
- Every session ends with notes: what I tried, what the logs showed, how to defend.

## Write-Up Template (I copy this per lab)
```markdown
# Lab: <name> — <date>
## Goal
## Environment (VMs / versions)
## What I Did (steps)
## What I Observed (logs, output)
## Root Cause
## Detection: how a defender would spot this
## Mitigation / Fix
## What I Learned / Still Confused About
```

*New write-ups will be added here as separate files, e.g. `2026-11-dvwa-sqli-low.md`.*
