"""Tes sederhana untuk logika lima aplikasi dan mode demo main.py."""

import contextlib
import io
import unittest

import main
import app_kasir_kantin
import app_presensi_kelas
import app_perpustakaan_mini
import app_keuangan_pribadi
import app_nilai_mahasiswa


class TestAplikasi(unittest.TestCase):
    def test_kasir(self):
        self.assertEqual(app_kasir_kantin.total_belanja(app_kasir_kantin.PESANAN_DEMO), 22000)
        self.assertEqual(app_kasir_kantin.cari_menu("es teh")["harga"], 4000)
        self.assertEqual(app_kasir_kantin.cari_menu_berdasarkan_nomor(1)["nama"], "Pempek")
        self.assertIsNone(app_kasir_kantin.cari_menu("menu tidak ada"))
        self.assertIsNone(app_kasir_kantin.cari_menu_berdasarkan_nomor(999))

    def test_presensi(self):
        hasil = app_presensi_kelas.hitung_rekap(app_presensi_kelas.DATA_DEMO)
        total = {item["nama"]: item["hadir"] for item in hasil}
        self.assertEqual(total, {"Budi": 1, "Sari": 2, "Andi": 1})

    def test_presensi_tampilkan_data_absensi(self):
        keluaran = io.StringIO()
        with contextlib.redirect_stdout(keluaran):
            app_presensi_kelas.tampilkan_data_absensi(app_presensi_kelas.DATA_DEMO)
        hasil = keluaran.getvalue()
        self.assertIn("DATA ABSENSI", hasil)
        self.assertIn("Budi", hasil)
        self.assertIn("Tidak Hadir", hasil)

    def test_perpustakaan(self):
        self.assertEqual(app_perpustakaan_mini.hitung_denda(app_perpustakaan_mini.DATA_DEMO), 5000)

    def test_keuangan(self):
        hasil = app_keuangan_pribadi.hitung_keuangan(app_keuangan_pribadi.DATA_DEMO)
        self.assertEqual(hasil["pemasukan"], 5000000)
        self.assertEqual(hasil["pengeluaran"], 40000)
        self.assertEqual(hasil["saldo"], 4960000)
        self.assertEqual(hasil["rata_pengeluaran"], 20000)

    def test_nilai_mahasiswa_tidak_mengubah_asal(self):
        asal = app_nilai_mahasiswa.DATA_DEMO
        hasil = app_nilai_mahasiswa.hitung_nilai_akhir(asal)
        self.assertEqual(hasil[0]["akhir"], 85)
        self.assertNotIn("akhir", asal[0])

    def test_semua_aplikasi_mode_demo(self):
        keluaran = io.StringIO()
        with contextlib.redirect_stdout(keluaran):
            main.jalankan_semua_demo()
        hasil = keluaran.getvalue()
        self.assertIn("STRUK PEMBELIAN", hasil)
        self.assertIn("REKAP KEHADIRAN", hasil)
        self.assertIn("RINGKASAN PERPUSTAKAAN", hasil)
        self.assertIn("RINGKASAN KEUANGAN", hasil)
        self.assertIn("REKAP NILAI", hasil)


if __name__ == "__main__":
    unittest.main()
