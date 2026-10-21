#!/usr/bin/env python3
"""
Password Strength Checker (educational)
----------------------------------------
Estimates password entropy from length + character variety and gives
practical tips. Runs 100% LOCALLY: no network, nothing is stored or sent.

Usage:
    python3 password_checker.py            # prompts privately (input hidden)

Never type a real password you care about into ANY tool you don't fully
trust — use this with made-up examples to learn how entropy works, and
use a reputable password manager + passphrases for real accounts.
"""
import getpass
import math
import string

COMMON = {"password", "password1", "123456", "12345678", "qwerty", "letmein",
          "admin", "welcome", "iloveyou", "abc123", "111111", "dragon"}


def assess(pw: str) -> tuple[int, list[str]]:
    tips: list[str] = []
    pool = 0
    if any(c in string.ascii_lowercase for c in pw): pool += 26
    if any(c in string.ascii_uppercase for c in pw): pool += 26
    if any(c in string.digits for c in pw): pool += 10
    if any(c in string.punctuation for c in pw): pool += len(string.punctuation)
    if any(c == " " for c in pw): pool += 1

    entropy = int(len(pw) * math.log2(pool)) if pool else 0

    if len(pw) < 12:
        tips.append("Use at least 14+ characters — length matters most. Try a passphrase: 4+ random words.")
    if pool <= 26:
        tips.append("Add character variety (upper/lower/digits/symbols) — or just make it much longer.")
    if pw.lower() in COMMON:
        entropy = min(entropy, 5)
        tips.append("This is a very common password — attackers try these first. Never use it anywhere.")
    if len(set(pw)) <= 3 and pw:
        tips.append("Too much repetition (e.g. 'aaaa', '1212') — patterns are guessed quickly.")
    if not tips:
        tips.append("Good structure! Still: use a UNIQUE password per site + a password manager + MFA.")
    return entropy, tips


def label(entropy: int) -> str:
    return ("Very weak" if entropy < 28 else "Weak" if entropy < 50 else
            "Moderate" if entropy < 75 else "Strong" if entropy < 100 else "Very strong")


def main() -> int:
    print("Password Strength Checker — runs locally, stores nothing.")
    print("Tip: test with MADE-UP passwords to learn, not your real ones.\n")
    pw = getpass.getpass("Enter a sample password to assess: ")
    if not pw:
        print("No input given.")
        return 1
    entropy, tips = assess(pw)
    print(f"\nEstimated entropy: ~{entropy} bits  ({label(entropy)})")
    print("Feedback:")
    for t in tips:
        print(f"  - {t}")
    print("\nRemember: MFA + a password manager protect you more than any single clever password.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
