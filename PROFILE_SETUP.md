# Copy-Paste: Profile Bio, Repo Description & Setup Checklist

Use these texts on GitHub. They are written to look like a real learner (not a bot/scammer) and to use safe, professional wording for security work.

---

## 1) GitHub Profile Bio (max 160 characters) — pick ONE

Go to: github.com → your avatar → Settings → Public profile → Bio

**Option A (recommended):**
```
Aspiring cybersecurity practitioner | Learning defensive security & ethical pentesting in a home lab | Python • Linux • CTFs
```

**Option B (shorter):**
```
Cybersecurity learner 🛡️ Home-lab pentesting & blue-team practice | TryHackMe • HackTheBox • Python scripting
```

**Option C (very safe / beginner tone):**
```
Student of cybersecurity. Building small defensive tools in Python and documenting my home-lab learning journey.
```

**Other profile fields to fill:**
- **Name:** your real first name (Joly is fine) — accounts with a name + photo get flagged far less
- **Location:** Singapore (or your city/country)
- **Company:** leave blank or `Student / Self-learning` — do NOT invent a fake company
- **Website:** leave blank until you have a real blog/LinkedIn — do NOT put a suspicious short link (bit.ly etc.)

---

## 2) Repository "About" Description — for THIS repo

On the repo page → click the ⚙️ gear next to "About" → paste:

**Description:**
```
My cybersecurity learning portfolio: home-lab notes, CTF write-ups, and small defensive Python tools (file integrity, log analysis, password strength) built while studying ethical pentesting & blue-team fundamentals.
```

**Topics (add these tags):**
```
cybersecurity  infosec  blue-team  ethical-hacking  penetration-testing  home-lab
python  linux  ctf  security-tools  learning-in-public  owasp
```

**Website field:** leave empty for now.

> ✅ Good words to use: *defensive, blue-team, educational, home lab, authorized, responsible disclosure, learning, detection, hardening*
>
> 🚫 Words/phrases to AVOID in names & descriptions: *crack, keygen, bypass, steal, free accounts, hacking services, anonymous, malware, RAT, phishing, exploit-for-sale, crypto giveaway* — these trigger spam/abuse filters fast.

---

## 3) IMPORTANT: Make This Show On Your Profile Page

A repo only appears as your big profile README if the repo name **exactly matches your username**.

- Your username: `jolyj1849-ship-it`
- This repo: `my-profile` → it will NOT auto-show on your profile page.

**Fix (pick one):**
1. Create a NEW public repo named exactly `jolyj1849-ship-it`, tick "Add a README", then copy the contents of this repo's `README.md` into it, **OR**
2. Keep `my-profile` as your portfolio repo and **Pin it**: Profile page → "Customize your pins" → select `my-profile`. Pinned repos with good descriptions also build a lot of trust.

---

## 4) Sample Descriptions For Your NEXT Repos (copy & adapt)

| Repo idea | Suggested repo name | About description |
|---|---|---|
| Lab write-ups | `lab-writeups` | Step-by-step write-ups from my isolated home lab and CTFs (TryHackMe/HTB), each with root cause + mitigation/defense notes. For education & authorized testing only. |
| Notes | `security-notes` | My personal study notes on networking, Linux, OWASP Top 10, and Security+ concepts — summarized in my own words with sources. |
| Python tools | `python-security-tools` | Small defensive Python utilities for learning: log parsing, hashing, and system hardening checks. Standard library only. |
| Web practice | `owasp-labs` | Practice notes from PortSwigger Web Security Academy & DVWA running locally in Docker. Includes how each vulnerability is fixed. |
| Hardening | `linux-hardening-checklist` | A practical Linux server hardening checklist with the commands I use in my lab, and why each setting matters. |

**Repo naming rules:** lowercase, hyphens, describes the content (`linux-hardening-checklist` ✅, `hack-tools-free2026` ❌).

## 5) Every New Repo Should Have (2 minutes each)

1. A `README.md` with: what it is, what *you* learned, how to run it, and the disclaimer below
2. A `LICENSE` file (MIT is fine: Add file → type `LICENSE` → "Choose a license template" → MIT)
3. An About description + 4–8 topics (see above)
4. **This disclaimer paragraph** at the end of the README:

```markdown
## Disclaimer
For educational purposes and authorized testing in my own lab only.
Do not use against any system you do not own or have explicit written permission to test.
```

---

## 6) Anti-Ban Checklist For New Accounts ✅

GitHub rarely bans learners. It bans *patterns* that look like bots/scams. Avoid the patterns:

**Do this (builds trust):**
- [ ] Verify your email address
- [ ] Turn on **two-factor authentication (2FA)**: Settings → Password and authentication
- [ ] Upload a profile picture (a real photo or a simple avatar — not a stock "hacker" image)
- [ ] Fill in Name + Bio + Location (above)
- [ ] Write READMEs in your own words, commit steadily over days/weeks with clear messages like `Add failed-login detection to log analyzer`
- [ ] Star/follow/comment **slowly and genuinely** — a few per day, on things you actually read
- [ ] Respond like a human to any GitHub verification email; appeal politely with facts if ever flagged

**Never do this (instant-flag patterns):**
- [ ] ❌ Mass-follow / mass-star / fork dozens of repos in one hour
- [ ] ❌ Open spam issues/PRs, or copy-paste the same comment everywhere
- [ ] ❌ Upload malware, RATs, stealers, phishing kits, cracked software, leaked passwords/databases, or API keys/secrets
- [ ] ❌ Create many empty repos, or repos that only contain a link to an external download
- [ ] ❌ Offer "hacking services", account recovery, or anything for sale in your bio/README
- [ ] ❌ Use multiple accounts to star/follow yourself

**Security-research specific (GitHub's rules, in plain English):**
- Learning, defensive tools, and CTF/lab write-ups = **allowed and welcome**
- Sharing a proof-of-concept = usually OK **if** you frame it defensively: explain impact + detection + fix, test only in a lab, and follow responsible disclosure for real products
- Working malware / tools whose only purpose is unauthorized harm = **removed + account action**

*If in doubt, ask in your README framing: "How would a defender detect and stop this?" — that question keeps you on the right side of the line, and it's also what employers want to see.*
