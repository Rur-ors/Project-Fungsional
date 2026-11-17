"""Library bersama untuk lima aplikasi Pemrograman Fungsional.

Fungsi-fungsi di sini tidak mengubah list atau dictionary asli.
"""

from functools import reduce


def ambil(kunci, daftar):
    """Ambil nilai suatu kunci dari setiap dictionary di dalam daftar."""
    return [item[kunci] for item in daftar]


def jumlah(angka):
    """Jumlahkan angka menggunakan reduce; daftar kosong menghasilkan 0."""
    return reduce(lambda total, nilai: total + nilai, angka, 0)


def rata_rata(angka):
    """Hitung rata-rata; hasilnya 0 jika tidak ada angka."""
    angka = list(angka)
    return jumlah(angka) / len(angka) if angka else 0


def tambah(daftar, item):
    """Tambahkan item dengan membuat list baru (list lama tetap)."""
    return [*daftar, item]


def urutkan(kunci, daftar, menurun=False):
    """Buat daftar baru, diurutkan menurut nilai pada kunci tertentu."""
    return sorted(daftar, key=lambda item: item[kunci], reverse=menurun)


def kelompokkan(kunci, daftar):
    """Kelompokkan list of dict menjadi dictionary berisi beberapa list."""
    def masukkan(hasil, item):
        nilai_kunci = item[kunci]
        kelompok_baru = [*hasil.get(nilai_kunci, []), item]
        return {**hasil, nilai_kunci: kelompok_baru}

    return reduce(masukkan, daftar, {})


def peringkat(kunci, daftar):
    """Urutkan nilai tertinggi dahulu, beri peringkat mulai dari angka 1."""
    data_urut = urutkan(kunci, daftar, menurun=True)
    return [
        {**item, "peringkat": nomor}
        for nomor, item in enumerate(data_urut, start=1)
    ]


def format_rupiah(angka):
    """Ubah angka menjadi teks Rupiah, contoh 15000 -> Rp 15.000."""
    return "Rp {:,}".format(int(angka)).replace(",", ".")
