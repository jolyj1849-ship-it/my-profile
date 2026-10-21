# My Cybersecurity Learning Roadmap

A realistic, beginner-friendly path I'm following. I tick items off and link write-ups as I go — steady progress beats speed.

## Phase 1 — Foundations (Months 1–2)
- [ ] How computers & the internet work: CPU/RAM/storage basics, TCP/IP, DNS, HTTP/HTTPS
- [ ] Linux essentials: filesystem, permissions, users, processes, `grep`/`find`/`chmod`, reading `/var/log`
- [ ] Windows essentials: users/groups, Event Viewer, basic PowerShell
- [ ] Networking tools (lab only): `ping`, `curl`, Wireshark basics, `nmap` against my own VMs
- [ ] TryHackMe: Pre-Security path

## Phase 2 — Security Fundamentals (Months 2–4)
- [ ] CIA triad, threat vs vulnerability vs risk, common attack types (to recognize & defend)
- [ ] OWASP Top 10 (one per week) via PortSwigger Web Security Academy + local DVWA/Juice Shop
- [ ] Cryptography basics: hashing vs encryption, TLS, password storage (bcrypt/argon2)
- [ ] Blue-team basics: log analysis, file integrity monitoring, patching & hardening checklists
- [ ] Python scripting: files, regex, `hashlib`, `socket` basics → the tools in this repo

## Phase 3 — Hands-On Labs (Months 4–6)
- [ ] TryHackMe Jr Penetration Tester path / Hack The Box Starting Point (all in-scope lab machines)
- [ ] One write-up per lab: *Goal → Steps → Root cause → Detection → Fix*
- [ ] Build & harden an Ubuntu server VM; attack it from Kali VM; then fix and re-test
- [ ] Intro to detection: Sigma-style thinking, Windows event IDs (4625, 4688...), Linux `auth.log`

## Phase 4 — Decide a Direction (Month 6+)
- [ ] Blue team / SOC: LetsDefend, Blue Team Labs Online, Security+ study
- [ ] OR Pentesting: eJPT study, more HTB/THM, report-writing practice
- [ ] Portfolio: keep GitHub updated, write blog posts, join a local/online community & CTF team

## Free Resources I'm Using
- TryHackMe · Hack The Box Academy · PortSwigger Web Security Academy · PicoCTF
- Professor Messer (Security+) · NetworkChuck / John Hammond (YouTube, defensive framing)
- OWASP Cheat Sheet Series · MITRE ATT&CK (to understand attacker behavior for defense)

*Progress over perfection: small, consistent lab sessions + honest write-ups of what confused me and what finally clicked.*
