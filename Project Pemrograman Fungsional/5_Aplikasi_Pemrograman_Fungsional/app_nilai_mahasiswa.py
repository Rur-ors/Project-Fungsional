"""Aplikasi 5: Nilai Mahasiswa.

Fungsi fplib: ambil, rata_rata, peringkat, urutkan, tambah.
"""

from fplib import ambil, rata_rata, peringkat, urutkan, tambah


DATA_DEMO = [
    {"nama": "Wildan", "tugas": 80, "uts": 85, "uas": 90},
    {"nama": "Moly", "tugas": 75, "uts": 78, "uas": 80},
    {"nama": "Citra", "tugas": 92, "uts": 88, "uas": 95},
]


def hitung_nilai_akhir(daftar_mahasiswa):
    """Tambahkan nilai 'akhir' pada salinan tiap data mahasiswa."""
    return [
        {
            **item,
            "akhir": rata_rata([item["tugas"], item["uts"], item["uas"]]),
        }
        for item in daftar_mahasiswa
    ]


def baca_mahasiswa_baru():
    print("\n=== 5. NILAI MAHASISWA ===")
    print("Data nilai contoh tersedia. Tambahkan satu mahasiswa (opsional).")
    try:
        nama = input("Nama mahasiswa (Enter = lewati): ").strip()
        if not nama:
            return None
        tugas = float(input("Nilai tugas (0-100): "))
        uts = float(input("Nilai UTS (0-100): "))
        uas = float(input("Nilai UAS (0-100): "))
        if not all(0 <= nilai <= 100 for nilai in (tugas, uts, uas)):
            print("Semua nilai harus berada di antara 0 dan 100. Data dilewati.")
            return None
        return {"nama": nama, "tugas": tugas, "uts": uts, "uas": uas}
    except (EOFError, ValueError):
        print("Input tidak valid/tersedia; memakai data demo.")
        return None


def main(mode_demo=False):
    mahasiswa = DATA_DEMO
    if mode_demo:
        print("\n=== 5. NILAI MAHASISWA (DEMO) ===")
    else:
        mahasiswa_baru = baca_mahasiswa_baru()
        if mahasiswa_baru is not None:
            # Bukan mahasiswa.append(...), agar list asli tidak berubah.
            mahasiswa = tambah(mahasiswa, mahasiswa_baru)

    hasil = hitung_nilai_akhir(mahasiswa)
    nama_urut = ambil("nama", urutkan("nama", hasil))

    print("\n--- REKAP NILAI ---")
    print("Nama urut abjad:", ", ".join(nama_urut))
    print(f"Rata-rata nilai kelas: {rata_rata(ambil('akhir', hasil)):.2f}")
    print("Peringkat mahasiswa:")
    for item in peringkat("akhir", hasil):
        print(f"{item['peringkat']}. {item['nama']}: {item['akhir']:.2f}")


if __name__ == "__main__":
    main()
