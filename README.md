# Hi, I'm Joly 👋

**Aspiring Cybersecurity Practitioner | Security + Pentesting Learner | Home Lab Builder**

I am learning cybersecurity with a focus on **defensive security, ethical penetration testing, and security tooling** — always in my own lab, on systems I own, or on platforms that give explicit permission to test (CTFs, TryHackMe, Hack The Box, and vulnerable-by-design labs like DVWA / Metasploitable).

This repository is my public learning portfolio: notes, lab write-ups, and small defensive tools I build while studying.

> 🔒 **Ethics first:** Everything here is for education and authorized testing only. I do not test systems I don't own or have written permission to test. See [Ethics & Responsible Use](docs/ethics-and-responsible-use.md).

---

## 🎯 What I'm Learning

- **Foundations:** Linux, networking (TCP/IP, DNS, HTTP), how the web works
- **Defensive / Blue Team:** Log analysis, file integrity monitoring, hardening, detection basics
- **Offensive (in labs only):** Web vulnerabilities (OWASP Top 10), reconnaissance, privilege escalation concepts
- **Scripting for Security:** Python & Bash for automation and small security tools
- **Platforms:** TryHackMe · Hack The Box · PortSwigger Web Security Academy · PicoCTF

Full plan: [My Learning Roadmap](docs/learning-roadmap.md)

## 🧪 Home Lab

I practice in an isolated virtual lab (VirtualBox / VMware, host-only network — **not** on the public internet):

| Machine | Purpose |
|---|---|
| Kali Linux | Testing tools, run only inside the lab |
| Ubuntu Server | Target / defender machine, log collection |
| Metasploitable / DVWA | Intentionally vulnerable apps for practice |
| Windows 10 VM | Hardening & event-log practice |

Setup notes: [Lab Notes](lab-notes/README.md)

## 🛠️ Sample Projects in This Repo

Small, defensive, beginner-friendly tools written in Python (standard library only):

| Project | What it does | Link |
|---|---|---|
| File Integrity Checker | Hash files (SHA-256) and detect changes — a core blue-team concept | [tools/file-integrity-checker](tools/file-integrity-checker/) |
| Auth Log Analyzer | Parse Linux auth logs and flag repeated failed logins | [tools/log-analyzer](tools/log-analyzer/) |
| Password Strength Checker | Estimate password entropy and give improvement tips (runs 100% locally) | [tools/password-strength-checker](tools/password-strength-checker/) |

Each tool includes its own README, usage examples, and limitations.

## 📚 Currently Studying

- [ ] CompTIA Security+ concepts / TryHackMe Pre-Security & Jr Penetration Tester paths
- [ ] OWASP Top 10 — one vulnerability class at a time, with mitigation notes
- [ ] Python for security automation
- [ ] Writing one lab write-up per week (what I tried, what I learned, how to defend against it)

## 📫 Contact & Responsible Disclosure

- Open an [issue](../../issues) for questions about code in this repo.
- If you find a security issue **in this repo's code**, please see [SECURITY.md](SECURITY.md) — I appreciate responsible disclosure and will credit reporters.
- I am happy to connect with other learners, CTF players, and mentors.

---

### ⚖️ Disclaimer

All content in this repository is provided **for educational purposes and authorized security testing only**. Do not use any tool or technique described here against systems you do not own or do not have explicit, written permission to test. Unauthorized access is illegal. The author is not responsible for misuse.

*Learning in public — feedback and corrections are very welcome.*
