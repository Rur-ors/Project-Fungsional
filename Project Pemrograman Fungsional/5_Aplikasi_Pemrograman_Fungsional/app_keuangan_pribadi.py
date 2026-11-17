"""Aplikasi 4: Keuangan Pribadi.

Fungsi fplib: ambil, jumlah, kelompokkan, rata_rata, tambah,
             urutkan, format_rupiah.
"""

from fplib import ambil, jumlah, kelompokkan, rata_rata, tambah, urutkan, format_rupiah


DATA_DEMO = [
    {"ket": "Gaji", "tipe": "masuk", "kategori": "Pekerjaan", "jumlah": 5000000},
    {"ket": "Makan", "tipe": "keluar", "kategori": "Kebutuhan", "jumlah": 25000},
    {"ket": "Transportasi", "tipe": "keluar", "kategori": "Transportasi", "jumlah": 15000},
]


def hitung_keuangan(transaksi):
    """Kembalikan hasil olah transaksi tanpa mengubah data awal."""
    pemasukan = [item for item in transaksi if item["tipe"] == "masuk"]
    pengeluaran = [item for item in transaksi if item["tipe"] == "keluar"]

    total_masuk = jumlah(ambil("jumlah", pemasukan))
    total_keluar = jumlah(ambil("jumlah", pengeluaran))
    grup_pengeluaran = kelompokkan("kategori", pengeluaran)
    total_per_kategori = {
        nama: jumlah(ambil("jumlah", daftar))
        for nama, daftar in grup_pengeluaran.items()
    }
    rata_keluar = rata_rata(ambil("jumlah", pengeluaran))
    terbesar = urutkan("jumlah", transaksi, menurun=True)[0] if transaksi else None

    return {
        "pemasukan": total_masuk,
        "pengeluaran": total_keluar,
        "saldo": total_masuk - total_keluar,
        "per_kategori": total_per_kategori,
        "rata_pengeluaran": rata_keluar,
        "terbesar": terbesar,
    }


def baca_transaksi_baru():
    print("\n=== 4. KEUANGAN PRIBADI ===")
    print("Data transaksi contoh tersedia. Tambahkan satu transaksi (opsional).")
    try:
        keterangan = input("Keterangan (Enter = lewati): ").strip()
        if not keterangan:
            return None
        tipe = input("Tipe (masuk/keluar): ").strip().lower()
        if tipe not in ("masuk", "keluar"):
            print("Tipe harus masuk atau keluar. Data dilewati.")
            return None
        kategori = input("Kategori: ").strip()
        nilai = int(input("Jumlah uang (angka): "))
        if not kategori or nilai < 0:
            print("Kategori tidak boleh kosong dan jumlah tidak boleh negatif.")
            return None
        return {"ket": keterangan, "tipe": tipe, "kategori": kategori, "jumlah": nilai}
    except (EOFError, ValueError):
        print("Input tidak valid/tersedia; memakai data demo.")
        return None


def main(mode_demo=False):
    transaksi = DATA_DEMO
    if mode_demo:
        print("\n=== 4. KEUANGAN PRIBADI (DEMO) ===")
    else:
        transaksi_baru = baca_transaksi_baru()
        if transaksi_baru is not None:
            transaksi = tambah(transaksi, transaksi_baru)

    hasil = hitung_keuangan(transaksi)
    print("\n--- RINGKASAN KEUANGAN ---")
    print("Total pemasukan :", format_rupiah(hasil["pemasukan"]))
    print("Total pengeluaran:", format_rupiah(hasil["pengeluaran"]))
    print("Sisa saldo      :", format_rupiah(hasil["saldo"]))
    print("Pengeluaran per kategori:")
    for nama, nilai in hasil["per_kategori"].items():
        print(f"- {nama}: {format_rupiah(nilai)}")
    print("Rata-rata pengeluaran:", format_rupiah(hasil["rata_pengeluaran"]))
    if hasil["terbesar"] is not None:
        terbesar = hasil["terbesar"]
        print(f"Transaksi terbesar: {terbesar['ket']} ({format_rupiah(terbesar['jumlah'])})")


if __name__ == "__main__":
    main()
