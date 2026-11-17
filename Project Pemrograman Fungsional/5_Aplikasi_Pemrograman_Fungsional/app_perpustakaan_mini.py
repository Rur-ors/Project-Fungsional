"""Aplikasi 3: Perpustakaan Mini.

Fungsi fplib: ambil, jumlah, kelompokkan, peringkat, tambah, format_rupiah.
"""

from fplib import ambil, jumlah, kelompokkan, peringkat, tambah, format_rupiah


DATA_DEMO = [
    {"judul": "Laskar Pelangi", "kategori": "Novel", "pinjam": 12, "hari_telat": 2},
    {"judul": "Bumi Manusia", "kategori": "Novel", "pinjam": 18, "hari_telat": 0},
    {"judul": "Python Dasar", "kategori": "Teknologi", "pinjam": 9, "hari_telat": 3},
]

DENDA_PER_HARI = 1000


def hitung_denda(daftar_buku):
    """Denda tiap buku = hari terlambat x Rp 2.000."""
    semua_denda = [buku["hari_telat"] * DENDA_PER_HARI for buku in daftar_buku]
    return jumlah(semua_denda)


def baca_buku_baru():
    print("\n=== 3. PERPUSTAKAAN MINI ===")
    print("Data buku contoh tersedia. Tambahkan satu buku (opsional).")
    try:
        judul = input("Judul buku (Enter = lewati): ").strip()
        if not judul:
            return None
        kategori = input("Kategori: ").strip()
        pinjam = int(input("Jumlah kali dipinjam: "))
        hari_telat = int(input("Jumlah hari terlambat: "))
        if not kategori or pinjam < 0 or hari_telat < 0:
            print("Kategori tidak boleh kosong; angka tidak boleh negatif. Data dilewati.")
            return None
        return {
            "judul": judul,
            "kategori": kategori,
            "pinjam": pinjam,
            "hari_telat": hari_telat,
        }
    except (EOFError, ValueError):
        print("Input tidak valid/tersedia; memakai data demo.")
        return None


def main(mode_demo=False):
    buku = DATA_DEMO  # daftar awal tidak dimodifikasi
    if mode_demo:
        print("\n=== 3. PERPUSTAKAAN MINI (DEMO) ===")
    else:
        buku_baru = baca_buku_baru()
        if buku_baru is not None:
            buku = tambah(buku, buku_baru)

    print("\n--- RINGKASAN PERPUSTAKAAN ---")
    print("Jumlah judul per kategori:")
    for kategori, daftar in kelompokkan("kategori", buku).items():
        print(f"- {kategori}: {len(daftar)} judul")

    print("\n2 buku paling sering dipinjam:")
    for item in peringkat("pinjam", buku)[:2]:
        print(f"{item['peringkat']}. {item['judul']} ({item['pinjam']} kali)")

    print("\nTotal denda:", format_rupiah(hitung_denda(buku)))
    print("Semua judul:", ", ".join(ambil("judul", buku)))


if __name__ == "__main__":
    main()
