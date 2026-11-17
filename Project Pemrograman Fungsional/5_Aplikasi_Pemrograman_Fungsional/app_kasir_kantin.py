"""Aplikasi 1: Kasir Kantin.

Fungsi fplib: ambil, jumlah, tambah, urutkan, format_rupiah.
"""

from fplib import ambil, jumlah, tambah, urutkan, format_rupiah


# Data menu contoh. Tiap menu memiliki nama dan harga.
MENU = [
    {"nama": "Pempek", "harga": 14000},
    {"nama": "Mie Ayam", "harga": 12000},
    {"nama": "Nasi Ayam Geprek", "harga": 13000},
    {"nama": "Bakso", "harga": 11000},
    {"nama": "Soto Mie", "harga": 12000},
    {"nama": "Roti Bakar", "harga": 7000},
    {"nama": "Gorengan", "harga": 1000},
    {"nama": "Es Teh", "harga": 4000},
    {"nama": "Es Jeruk", "harga": 5000},
    {"nama": "Air Mineral", "harga": 3000},
]

PESANAN_DEMO = [MENU[0], MENU[8], MENU[9]]


def cari_menu(nama):
    """Cari menu berdasarkan nama, tanpa membedakan huruf kapital."""
    hasil = [item for item in MENU if item["nama"].lower() == nama.lower()]
    return hasil[0] if hasil else None


def cari_menu_berdasarkan_nomor(nomor):
    """Cari menu berdasarkan nomor urut pada daftar menu."""
    if not isinstance(nomor, int):
        return None
    if 1 <= nomor <= len(MENU):
        return MENU[nomor - 1]
    return None


def total_belanja(keranjang):
    """Logika perhitungan, dipisahkan dari input dan print."""
    return jumlah(ambil("harga", keranjang))


def tampilkan_menu():
    print("\n=== 1. KASIR KANTIN ===")
    print("Menu kantin:")
    for nomor, item in enumerate(MENU, start=1):
        print(f"{nomor}. {item['nama']}: {format_rupiah(item['harga'])}")


def baca_pesanan():
    """Baca nama menu atau nomor menu berulang kali; Enter kosong mengakhiri pesanan."""
    keranjang = []
    print("\nKetik nama menu atau pilih nomor menu. Enter kosong = selesai.")
    try:
        while True:
            pilihan = input("Nama menu / nomor menu: ").strip()
            if pilihan == "":
                break

            menu = None
            if pilihan.isdigit():
                menu = cari_menu_berdasarkan_nomor(int(pilihan))
            else:
                menu = cari_menu(pilihan)

            if menu is None:
                print("Menu tidak ditemukan. Silakan coba lagi.")
                continue

            keranjang = tambah(keranjang, menu)
            print(f"Ditambahkan: {menu['nama']}")
    except EOFError:
        print("Input tidak tersedia; memakai pesanan demo.")
        return PESANAN_DEMO

    if not keranjang:
        print("Tidak ada pesanan; memakai pesanan demo.")
        return PESANAN_DEMO
    return keranjang


def main(mode_demo=False):
    """Dipanggil melalui main.py atau saat file ini dijalankan sendiri."""
    tampilkan_menu()
    keranjang = PESANAN_DEMO if mode_demo else baca_pesanan()

    print("\n--- STRUK PEMBELIAN ---")
    for nama in ambil("nama", keranjang):
        print("-", nama)
    print("Jumlah barang:", len(keranjang))
    print("Total bayar :", format_rupiah(total_belanja(keranjang)))


if __name__ == "__main__":
    main()
