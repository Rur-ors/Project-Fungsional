# 5 Aplikasi Sederhana dengan Python Fungsional

Project ini dibuat untuk belajar konsep pemrograman fungsional dengan pendekatan yang sederhana dan mudah dipahami. Saya menyusunnya berdasarkan pola tugas pada materi **Pemrograman Fungsional** dan mengadaptasi beberapa ide dari referensi **Fplib-main**. Tujuannya adalah agar logika program lebih jelas, lebih rapi, dan tetap mudah diuji tanpa memerlukan framework tambahan.

Program ini berjalan di **terminal/console** dan tidak menggunakan GUI, jadi cocok untuk latihan, tugas kuliah, maupun demo singkat di depan kelas.

---

## 1. Struktur folder

```text
5_Aplikasi_Pemrograman_Fungsional/
│
├── main.py                    # Menu utama untuk menjalankan 5 aplikasi
├── fplib.py                   # Library bersama berisi 8 fungsi
│
├── app_kasir_kantin.py        # Aplikasi 1
├── app_presensi_kelas.py     # Aplikasi 2
├── app_perpustakaan_mini.py  # Aplikasi 3
├── app_keuangan_pribadi.py   # Aplikasi 4
├── app_nilai_mahasiswa.py    # Aplikasi 5
│
├── test_fplib.py             # Tes untuk fungsi library
├── test_aplikasi.py          # Tes logika aplikasi dan mode demo
├── requirements.txt          # Tidak ada library tambahan
└── README.md                 # Panduan project
```

---

## 2. Cara menjalankan project di VS Code

Ikuti langkah berikut:

1. Pastikan **Python 3.9 atau versi lebih baru** sudah terinstal di komputer kamu.
2. Buka VS Code, lalu pilih **File > Open Folder** dan arahkan ke folder `5_Aplikasi_Pemrograman_Fungsional`.
3. Buka terminal baru dengan **Terminal > New Terminal**.
4. Jalankan perintah berikut:

```bash
python main.py
```

Kalau di Windows tidak bisa menggunakan `python`, coba:

```bash
py main.py
```

Setelah itu, kamu akan melihat menu pilihan:

- **1** Kasir Kantin
- **2** Presensi Kelas
- **3** Perpustakaan Mini
- **4** Keuangan Pribadi
- **5** Nilai Mahasiswa
- **6** Jalankan semua aplikasi dengan data contoh tanpa input manual
- **0** Keluar

Untuk menjalankan semua aplikasi sekaligus dalam mode demo:

```bash
python main.py --semua
```

---

## 3. Menjalankan satu aplikasi saja

Kamu tidak harus selalu lewat `main.py`. Setiap aplikasi juga bisa dijalankan secara terpisah:

```bash
python app_kasir_kantin.py
python app_presensi_kelas.py
python app_perpustakaan_mini.py
python app_keuangan_pribadi.py
python app_nilai_mahasiswa.py
```

Jika kamu pakai Windows, ganti `python` menjadi `py`.

---

## 4. Apa isi program ini?

Project ini berisi lima aplikasi kecil yang masing-masing punya fokus berbeda, namun semuanya memakai pendekatan yang serupa:

- **Kasir Kantin**: menghitung total belanja, menampilkan menu termurah, dan membuat struk sederhana.
- **Presensi Kelas**: menghitung kehadiran siswa dan menampilkan rangking kehadiran.
- **Perpustakaan Mini**: mengelola data buku, menghitung denda, dan menampilkan buku paling populer.
- **Keuangan Pribadi**: membedakan pemasukan dan pengeluaran serta menghitung saldo akhir.
- **Nilai Mahasiswa**: menghitung nilai akhir, rata-rata kelas, dan peringkat mahasiswa.

Data demo tersedia supaya aplikasi tetap bisa berjalan tanpa harus memasukkan input satu per satu.

---

## 5. Delapan fungsi utama di `fplib.py`

Library bersama ini berisi delapan fungsi yang dipakai untuk mengolah data secara fungsional.

| Fungsi | Fungsi utama | Konsep yang dipakai |
|---|---|---|
| `ambil(kunci, daftar)` | Mengambil nilai berdasarkan field tertentu | List comprehension |
| `jumlah(angka)` | Menjumlahkan bilangan | `reduce` dan `lambda` |
| `rata_rata(angka)` | Menghitung rata-rata | Komposisi dengan `jumlah` |
| `tambah(daftar, item)` | Menambahkan item ke daftar baru | Immutability (`[*daftar, item]`) |
| `urutkan(kunci, daftar, menurun=False)` | Mengurutkan data | `sorted` dan `lambda` |
| `kelompokkan(kunci, daftar)` | Mengelompokkan data berdasarkan kriteria tertentu | `reduce`, dictionary unpacking |
| `peringkat(kunci, daftar)` | Membuat ranking dari data | `urutkan`, `enumerate` |
| `format_rupiah(angka)` | Menampilkan format uang Rupiah | Fungsi pemformatan |

Intinya, semua fungsi ini dibuat agar **tidak mengubah data input** secara langsung. Jadi, data masuk tetap aman dan mudah diuji.

---

## 6. Cara kerja `main.py`

`main.py` berperan sebagai penghubung utama untuk semua aplikasi. Ia berisi menu pilihan dan memanggil fungsi aplikasi sesuai nomor yang dipilih.

Cara kerjanya singkatnya seperti ini:

- `import app_kasir_kantin` dan empat file aplikasi lain agar fungsi `main()` bisa dipanggil.
- Dictionary `APLIKASI` berisi nomor, nama, dan fungsi yang relevan.
- `tampilkan_menu()` menampilkan daftar pilihan aplikasi.
- Saat memilih **1–5**, program memanggil aplikasi yang dipilih dan kembali ke menu utama.
- Saat memilih **6**, program langsung menjalankan semua aplikasi dalam mode demo.
- Saat memilih **0**, program berhenti.

Setiap file aplikasi diakhiri dengan:

```python
if __name__ == "__main__":
    main()
```

Artinya, file tersebut bisa dijalankan langsung, tetapi tidak otomatis berjalan saat di-import oleh `main.py`.

---

## 7. Penggunaan fungsi per aplikasi

Berikut gambaran penggunaan fungsi utama di masing-masing aplikasi:

| Fungsi | Kasir | Presensi | Perpustakaan | Keuangan | Nilai | Total |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| `ambil` | ✓ | ✓ | ✓ | ✓ | ✓ | 5 |
| `jumlah` | ✓ | ✓ | ✓ | ✓ | – | 4 |
| `rata_rata` | – | ✓ | – | ✓ | ✓ | 3 |
| `tambah` | ✓ | ✓ | ✓ | ✓ | ✓ | 5 |
| `urutkan` | ✓ | – | – | ✓ | ✓ | 3 |
| `kelompokkan` | – | ✓ | ✓ | ✓ | – | 3 |
| `peringkat` | – | ✓ | ✓ | – | ✓ | 3 |
| `format_rupiah` | ✓ | – | ✓ | ✓ | – | 3 |

Ini menunjukkan bahwa fungsi-fungsi di `fplib.py` benar-benar dipakai dalam praktik, bukan sekadar teori.

---

## 8. Cara menguji program

Project ini tidak membutuhkan instalasi library tambahan. Untuk menjalankan semua tes bawaan Python:

```bash
python -m unittest discover -v
```

Kalau ingin mencoba semua aplikasi tanpa harus mengisi input secara manual:

```bash
python main.py --semua
```

---

## 9. Catatan untuk demo atau presentasi

Saat menjelaskan project ini, konsep yang paling penting adalah urutan:

**Input → Proses (fplib.py) → Output**

Contohnya, pada aplikasi Kasir Kantin:

- input menu ditambahkan ke keranjang menggunakan `tambah`
- harga diambil dengan `ambil`
- total dihitung dengan `jumlah`
- hasil akhirnya ditampilkan dalam format rupiah dengan `format_rupiah`

Itu membuat proses program terasa jelas dan lebih mudah dipahami, terutama saat presentasi atau tugas akhir.

---

## 10. Kesimpulan

Project ini sangat cocok untuk belajar:

- pemrograman fungsional di Python,
- penggunaan list/dictionary secara lebih terstruktur,
- teknik pemecahan masalah menjadi fungsi-fungsi kecil,
- dan kemampuan membuat program sederhana yang tetap rapi serta mudah dites.

Semua file dibuat dengan Python standar tanpa database, tanpa internet, dan tanpa framework tambahan.

Selamat belajar dan semoga project ini bermanfaat.
