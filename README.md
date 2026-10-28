# CTF Writeups

Write-up for the **Cybersecurity Pathway Final Project** at GDGoC USU (July 2026),
awarded **1st Best Project**. 🥇

4 challenges solved across web exploitation, cryptography, reverse engineering,
and digital forensics.

📄 **[Read the full writeup (PDF)](./GDGoC-Cybersecurity-Pathway-Final-Project.pdf)**
*(written in Bahasa Indonesia)*

## Challenges

| # | Challenge | Category | Technique | Tools |
|---|---|---|---|---|
| 1 | The Secure Vault | Web Exploitation | SQL Injection (authentication bypass) | Browser DevTools, Burp Suite |
| 2 | Layered Secrets | Cryptography | Hex → Base64 → single-byte XOR brute-force | CyberChef, Python |
| 3 | The Password Checker | Reverse Engineering | Static analysis of an ELF binary, XOR-obfuscated data | Ghidra, strings, Python |
| 4 | Hidden Pixels | Digital Forensics | LSB steganography in a PNG | exiftool, zsteg |

## What I Learned

- **Web:** Reading page source for developer hints, and how comment-based SQL
  injection (`admin' -- `) works when queries use string formatting instead of
  parameterized queries.
- **Crypto:** Encoding (Hex, Base64) is not encryption, and single-byte XOR only
  has 256 possible keys, so brute-force is trivial.
- **Reverse engineering:** Reading Ghidra's decompiled pseudo-code and recovering
  hardcoded XOR-obfuscated data without running the binary.
- **Forensics:** Decoy flags in metadata, why `steghide` doesn't work on PNG,
  and how `zsteg` checks bit-plane combinations.

## Repository Contents

- `GDGoC-Cybersecurity-Pathway-Final-Project.pdf`: full writeup with methodology,
  tools, commands, and screenshots

---
*Written by Naulia Situmeang*
