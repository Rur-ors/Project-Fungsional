"""Menu utama untuk menjalankan lima aplikasi dari satu tempat.

Jalankan: python main.py
Atau:     python main.py --semua  (langsung tampilkan kelima demo)
"""

import sys

import app_kasir_kantin
import app_presensi_kelas
import app_perpustakaan_mini
import app_keuangan_pribadi
import app_nilai_mahasiswa


# Pasangkan pilihan menu dengan fungsi main() tiap aplikasi.
APLIKASI = {
    "1": ("Kasir Kantin", app_kasir_kantin.main),
    "2": ("Presensi Kelas", app_presensi_kelas.main),
    "3": ("Perpustakaan Mini", app_perpustakaan_mini.main),
    "4": ("Keuangan Pribadi", app_keuangan_pribadi.main),
    "5": ("Nilai Mahasiswa", app_nilai_mahasiswa.main),
}


def tampilkan_menu():
    print("\n" + "=" * 46)
    print("   MENU UTAMA - 5 APLIKASI PYTHON SEDERHANA")
    print("=" * 46)
    for nomor, (nama, _) in APLIKASI.items():
        print(f"{nomor}. {nama}")
    print("6. Jalankan semua aplikasi (mode demo)")
    print("0. Keluar")
    print("=" * 46)


def jalankan_semua_demo():
    """Jalankan kelima aplikasi berurutan TANPA menunggu input."""
    for nomor, (nama, jalankan) in APLIKASI.items():
        print("\n" + "-" * 46)
        print(f"DEMO {nomor}: {nama}")
        print("-" * 46)
        jalankan(mode_demo=True)
    print("\nSelesai menjalankan 5 aplikasi dalam mode demo.")


def main():
    # Cara cepat untuk demonstrasi: python main.py --semua
    if len(sys.argv) == 2 and sys.argv[1] == "--semua":
        jalankan_semua_demo()
        return

    # Tanpa argumen, tampilkan menu sampai pengguna memilih keluar.
    while True:
        tampilkan_menu()
        try:
            pilihan = input("Pilih menu (0-6): ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nProgram dihentikan.")
            return

        if pilihan == "0":
            print("Terima kasih, sampai jumpa!")
            return
        if pilihan == "6":
            jalankan_semua_demo()
        elif pilihan in APLIKASI:
            nama, jalankan = APLIKASI[pilihan]
            print(f"\nMembuka aplikasi: {nama}")
            jalankan()
        else:
            print("Pilihan tidak tersedia. Masukkan angka 0 sampai 6.")


if __name__ == "__main__":
    main()
