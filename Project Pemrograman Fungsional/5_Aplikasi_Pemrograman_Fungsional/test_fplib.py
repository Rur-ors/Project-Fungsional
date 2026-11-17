"""Pengujian otomatis untuk delapan fungsi fplib.

Jalankan semua pengujian: python -m unittest discover -v
"""

import unittest

from fplib import (
    ambil, jumlah, rata_rata, tambah,
    urutkan, kelompokkan, peringkat, format_rupiah,
)


DATA = [
    {"nama": "Budi", "nilai": 80, "kelas": "A"},
    {"nama": "Sari", "nilai": 90, "kelas": "B"},
    {"nama": "Andi", "nilai": 70, "kelas": "A"},
]


class TestFplib(unittest.TestCase):
    def test_ambil(self):
        self.assertEqual(ambil("nama", DATA), ["Budi", "Sari", "Andi"])

    def test_jumlah(self):
        self.assertEqual(jumlah([1, 2, 3]), 6)
        self.assertEqual(jumlah([]), 0)

    def test_rata_rata(self):
        self.assertEqual(rata_rata([80, 90, 70]), 80)
        self.assertEqual(rata_rata([]), 0)
        self.assertEqual(rata_rata(angka for angka in (2, 4, 6)), 4)

    def test_tambah_tidak_mengubah_asal(self):
        asal = [1, 2]
        hasil = tambah(asal, 3)
        self.assertEqual(hasil, [1, 2, 3])
        self.assertEqual(asal, [1, 2])

    def test_urutkan_tidak_mengubah_asal(self):
        self.assertEqual(ambil("nama", urutkan("nilai", DATA)), ["Andi", "Budi", "Sari"])
        self.assertEqual(
            ambil("nama", urutkan("nilai", DATA, menurun=True)),
            ["Sari", "Budi", "Andi"],
        )
        self.assertEqual(ambil("nama", DATA), ["Budi", "Sari", "Andi"])

    def test_kelompokkan(self):
        grup = kelompokkan("kelas", DATA)
        self.assertEqual(ambil("nama", grup["A"]), ["Budi", "Andi"])
        self.assertEqual(ambil("nama", grup["B"]), ["Sari"])

    def test_peringkat(self):
        hasil = peringkat("nilai", DATA)
        self.assertEqual(ambil("nama", hasil), ["Sari", "Budi", "Andi"])
        self.assertEqual(ambil("peringkat", hasil), [1, 2, 3])
        self.assertNotIn("peringkat", DATA[0])

    def test_format_rupiah(self):
        self.assertEqual(format_rupiah(15000), "Rp 15.000")
        self.assertEqual(format_rupiah(0), "Rp 0")


if __name__ == "__main__":
    unittest.main()
