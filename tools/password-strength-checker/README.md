# Password Strength Checker

Estimates a password's **entropy** (length × character variety) and explains how to improve it. Runs fully offline; stores nothing.

## Run it
```bash
python3 password_checker.py   # input is hidden while typing
```
⚠️ Test with **made-up** passwords to learn the concept — never paste real passwords into random tools. For real accounts: use a password manager (generates long random passwords), a 4–5 word passphrase for the manager itself, and turn on MFA everywhere.

## What I learned
- Entropy ≈ `length × log2(pool size)`: doubling length beats adding one symbol.
- `correct-horse-battery-staple`-style passphrases: long, memorable, strong.
- A strength meter can't save a **reused** password — uniqueness + MFA matter most.

## Limitations
Simple pool-size math; doesn't check breach databases or dictionary patterns beyond a tiny built-in list. Educational sample, not an auditor.
