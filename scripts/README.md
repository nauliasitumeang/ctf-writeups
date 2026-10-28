# Scripts

Python scripts used to solve the CTF challenges in this repository,
written for the **Cybersecurity Pathway Final Project** at GDGoC USU (2026).
The filenames match the ones mentioned in the full writeup.

| Script | Challenge | What it does |
|---|---|---|
| [`solve_crypto.py`](./solve_crypto.py) | Layered Secrets (Cryptography) | Decodes a Hex → Base64 payload, then brute-forces all 256 single-byte XOR keys and checks each result against the known flag format |
| [`solve_reverse.py`](./solve_reverse.py) | The Password Checker (Reverse Engineering) | Reverses two XOR operations found through static analysis in Ghidra to recover the password and the hidden output, without running the binary |

## How They Work

**`solve_crypto.py`**
1. Decodes the payload from hexadecimal using `bytes.fromhex()`
2. Decodes the result from Base64
3. Tries every possible key (0-255) on the remaining bytes
4. Keeps the result that is valid text and matches the expected format

**`solve_reverse.py`**
1. Takes the byte arrays read from Ghidra's decompiled `main()`
2. Applies the XOR keys found in the pseudo-code to each byte
3. Converts the results to characters

## Usage

Requires Python 3 and no extra libraries.

```bash
python3 solve_crypto.py
python3 solve_reverse.py
```

## What I Learned

- Hex and Base64 are encodings, not encryption
- A single-byte XOR key has only 256 possibilities, so brute-force is trivial
- Data hardcoded in a binary can be recovered with static analysis alone

> ⚠️ Educational use only. These scripts solve CTF challenges built for learning.
