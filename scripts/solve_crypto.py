"""
GDGoC CTF - Cryptography Challenge Solver
Layers: Hex -> Base64 -> XOR (single-byte key)

file name:
    python3 solve_crypto.py
"""
import base64 

# Payload asli dari soal, masih dalam bentuk hex string
ENCRYPTED_PAYLOAD = "425159464c514535495441374d6a5a7948534177635859706354412f"


def solve():
    # Layer 1: payload di-decode dari hex ke bytes pakai bytes.fromhex()
    step1 = bytes.fromhex(ENCRYPTED_PAYLOAD)
    print("[Layer 1] Hex decoded ->", step1.decode())

    # Layer 2: hasil dari layer 1 ternyata berbentuk base64, jadi di-decode lagi
    step2 = base64.b64decode(step1)
    print("[Layer 2] Base64 decoded ->", step2)

    # Layer 3: hasil layer 2 berupa bytes yang gak kebaca (non-printable),
    # jadi kemungkinan ini XOR cipher. Karena cuma 1 byte key, kemungkinannya
    # cuma 256 (0-255), jadi bisa di-brute-force semua sekaligus
    print("[Layer 3] Brute-forcing XOR key...")
    for key in range(256):
        # Coba XOR tiap byte di step2 pakai key yang lagi di-loop
        candidate = bytes([b ^ key for b in step2])
        try:
            text = candidate.decode()
        except UnicodeDecodeError:
            # kalau hasil XOR-nya gak valid jadi text, skip aja, lanjut key berikutnya
            continue

        # cek apakah hasilnya cocok sama format flag yang diminta soal
        if text.startswith("GDGoC{") and text.endswith("}"):
            print(f"\nFound key: 0x{key:02x} ({key})")
            print(f"FLAG: {text}")
            return text

    print("No matching key found.")
    return None


if __name__ == "__main__":
    solve()