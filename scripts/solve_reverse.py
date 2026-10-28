"""
GDGoC CTF - Reverse Engineering Challenge Solver
Binary: challenge (ELF 64-bit)

Binary ini menyembunyikan dua array byte di dalam main():
1. local_97 -> dipakai untuk MEMVALIDASI password (dibandingkan dengan input user)
                rumus: (input[i] ^ 0x39) == local_97[i]
2. local_b8 -> dipakai untuk MENGHASILKAN flag (hanya jalan kalau password benar)
                rumus: flag[i] = local_b8[i] ^ 0x5a

Script ini membalikkan kedua operasi XOR tersebut secara otomatis untuk
mendapatkan password dan flag, tanpa perlu menjalankan binary-nya.

Usage:
    python3 solve_reverse.py
"""

# Array ini diambil langsung dari hasil dekompilasi Ghidra (pseudo-code main()),
# persis sama angka-angka yang muncul di local_97[0] sampai local_97[0xd]
local_97 = [
    0x5e, 0x5d, 0x5e, 0x56, 0x5a, 0x66, 0x0b, 0x09,
    0x0b, 0x0d, 0x66, 0x5a, 0x4d, 0x5f,
]  # 14 bytes -> password check array

# Array ini juga diambil langsung dari Ghidra, dari local_b8[0] sampai local_b8[0x16]
local_b8 = [
    0x1d, 0x1e, 0x1d, 0x35, 0x19, 0x21, 0x28, 0x69,
    0x2c, 0x69, 0x28, 0x29, 0x69, 0x05, 0x69, 0x34,
    0x3d, 0x6b, 0x34, 0x69, 0x69, 0x28, 0x27,
]  # 23 bytes -> flag generator array

# Dua key ini diambil dari operator "^" yang muncul di pseudo-code
PASSWORD_XOR_KEY = 0x39  # dipakai buat validasi password
FLAG_XOR_KEY = 0x5a      # dipakai buat generate flag

def xor_decode(byte_array: list, key: int) -> str:
    """XOR every byte in the array with `key` and return as text."""
    # Tiap byte di array di-XOR sama key, hasilnya di-convert ke karakter
    # pakai chr(), lalu semua karakter digabung jadi satu string
    return "".join(chr(b ^ key) for b in byte_array)

def main():
    # Panggil xor_decode() buat dapetin password (dari local_97 + key 0x39)
    password = xor_decode(local_97, PASSWORD_XOR_KEY)

    # Panggil xor_decode() lagi buat dapetin flag (dari local_b8 + key 0x5a)
    flag = xor_decode(local_b8, FLAG_XOR_KEY)

    # Print hasil akhirnya
    print("Recovered password:", password)
    print("recovered flag :" , flag)

if __name__ == "__main__":
    main()