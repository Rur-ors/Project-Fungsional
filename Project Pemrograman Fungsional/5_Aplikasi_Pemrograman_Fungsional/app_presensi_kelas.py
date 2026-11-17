"""Aplikasi 2: Presensi Kelas.

Fungsi fplib: ambil, jumlah, kelompokkan, peringkat, tambah, rata_rata.
"""

from fplib import ambil, jumlah, kelompokkan, peringkat, tambah, rata_rata


# Satu baris data mencatat kehadiran satu mahasiswa pada satu pertemuan.
DATA_DEMO = [
    {"nama": "Budi", "hadir": 1},
    {"nama": "Sari", "hadir": 1},
    {"nama": "Andi", "hadir": 1},
    {"nama": "Sari", "hadir": 1},
    {"nama": "Budi", "hadir": 0},
]


def hitung_rekap(catatan):
    """Kelompokkan mahasiswa lalu jumlahkan kehadiran masing-masing."""
    kelompok = kelompokkan("nama", catatan)
    return [
        {"nama": nama, "hadir": jumlah(ambil("hadir", data))}
        for nama, data in kelompok.items()
    ]


def tampilkan_data_absensi(catatan):
    """Tampilkan setiap data absensi yang sudah masuk."""
    print("\n--- DATA ABSENSI ---")
    if not catatan:
        print("Belum ada data absensi.")
        return

    for nomor, item in enumerate(catatan, start=1):
        status = "Hadir" if item["hadir"] == 1 else "Tidak Hadir"
        print(f"{nomor}. {item['nama']}: {status}")


def tampilkan_menu():
    print("\n=== 2. PRESENSI KELAS ===")
    print("1. Tambah data absensi")
    print("2. Tampilkan data absensi")
    print("3. Rekap kehadiran")
    print("0. Kembali")


def baca_presensi():
    catatan = []
    print("\nMasukkan nama dan status. Enter kosong = selesai.")
    try:
        while True:
            nama = input("Nama mahasiswa: ").strip()
            if nama == "":
                break
            status = input("Hadir? (1 = hadir, 0 = tidak): ").strip()
            if status not in ("0", "1"):
                print("Status harus 1 atau 0. Catatan dilewati.")
                continue
            catatan = tambah(catatan, {"nama": nama, "hadir": int(status)})
            print("Catatan berhasil ditambahkan.")
    except EOFError:
        print("Input tidak tersedia; memakai data demo.")
        return DATA_DEMO

    if not catatan:
        print("Tidak ada catatan; memakai data demo.")
        return DATA_DEMO
    return catatan


def main(mode_demo=False):
    if mode_demo:
        print("\n=== 2. PRESENSI KELAS (DEMO) ===")
        catatan = DATA_DEMO
        tampilkan_data_absensi(catatan)
    else:
        catatan = []
        while True:
            tampilkan_menu()
            pilihan = input("Pilih menu: ").strip()

            if pilihan == "1":
                catatan = baca_presensi()
                tampilkan_data_absensi(catatan)
            elif pilihan == "2":
                tampilkan_data_absensi(catatan)
            elif pilihan == "3":
                break
            elif pilihan == "0":
                return
            else:
                print("Pilihan tidak valid. Silakan pilih 1, 2, 3, atau 0.")

    rekap = hitung_rekap(catatan)
    print("\n--- REKAP KEHADIRAN ---")
    print(f"Rata-rata hadir per mahasiswa: {rata_rata(ambil('hadir', rekap)):.2f} kali")
    for mahasiswa in peringkat("hadir", rekap):
        print(f"{mahasiswa['peringkat']}. {mahasiswa['nama']}: {mahasiswa['hadir']} kali hadir")


if __name__ == "__main__":
    main()
