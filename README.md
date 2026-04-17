

## Deskripsi Sistem
Aplikasi ini merupakan sistem pakar yang digunakan untuk membantu mendiagnosa penyakit THT (Telinga, Hidung, Tenggorokan) berdasarkan gejala yang dipilih oleh pengguna. Sistem bekerja dengan membandingkan gejala yang dipilih dengan data penyakit yang tersedia, kemudian menghitung tingkat kecocokan dalam bentuk persentase untuk menentukan kemungkinan penyakit.

## Cara Menggunakan Aplikasi
1. Pilih gejala yang sesuai dengan kondisi yang dirasakan (centang checkbox).
2. Klik tombol PROSES DIAGNOSA.
3. Lihat hasil diagnosa yang ditampilkan:

   * Penyakit utama
   * Persentase kecocokan
   * Ranking penyakit lainnya
4. Jika ingin mengulang, klik tombol RESET.

## Alur Kerja Sistem
1. Sistem menampilkan daftar gejala.
2. Pengguna memilih gejala yang dirasakan.
3. Pengguna menekan tombol PROSES DIAGNOSA.
4. Sistem melakukan validasi:
   * Jika tidak ada gejala → tampil peringatan
   * Jika ada → lanjut ke proses perhitungan
5. Sistem menghitung kecocokan:
   * Menghitung jumlah gejala yang cocok
   * Menghitung persentase kecocokan tiap penyakit
6. Sistem mengurutkan hasil berdasarkan nilai tertinggi.
7. Sistem menampilkan:
   * Penyakit dengan nilai tertinggi
   * Daftar ranking penyakit lain

## Alur Program (Secara Teknis)
### 1. Inisialisasi Data
Program memuat dua data utama:
* Data gejala (kode dan nama gejala)
* Data penyakit (nama penyakit dan daftar gejalanya)
Data ini digunakan sebagai dasar dalam proses diagnosa.

### 2. Pembuatan Tampilan
Program membuat tampilan aplikasi yang terdiri dari:
* Judul aplikasi
* Instruksi penggunaan
* Daftar gejala dalam bentuk checkbox
* Scroll agar semua gejala dapat ditampilkan
* Tombol PROSES DIAGNOSA dan RESET

### 3. Inisialisasi Variabel Input
Setiap checkbox dihubungkan dengan variabel boolean (True/False) yang disimpan dalam dictionary `vars` untuk mencatat gejala yang dipilih.

### 4. Pengambilan Input Pengguna
Saat tombol PROSES DIAGNOSA ditekan:
* Program membaca semua checkbox
* Mengambil gejala yang dipilih ke dalam list `input_gejala`

### 5. Validasi Input
* Jika `input_gejala` kosong → tampil pesan peringatan
* Jika tidak kosong → lanjut ke proses perhitungan

### 6. Proses Perhitungan Kecocokan
Untuk setiap penyakit:
* Menghitung jumlah gejala yang cocok (`cocok`)
* Menghitung persentase:
  cocok / total gejala penyakit × 100%
* Menyimpan hasil ke dictionary `hasil`

### 7. Pengurutan Hasil
* Data pada `hasil` diurutkan dari nilai tertinggi ke terendah
* Disimpan dalam variabel `ranking`

### 8. Penentuan Hasil Utama
* Mengambil data dengan nilai tertinggi sebagai hasil utama
* Disimpan dalam variabel `terbaik` dan `nilai`

### 9. Menampilkan Output
* Jika nilai tertinggi = 0 → tampilkan “tidak ada penyakit yang cocok”
* Jika ada hasil → tampilkan:
  * Penyakit utama dan persentase
  * Daftar ranking penyakit lain

### 10. Reset Sistem
* Jika tombol RESET ditekan
* Semua checkbox dikembalikan ke kondisi awal

## Kesimpulan
Aplikasi ini dapat membantu pengguna dalam melakukan diagnosa awal penyakit THT secara sederhana dan cepat berdasarkan gejala yang dipilih. Hasil ditampilkan dalam bentuk persentase sehingga memudahkan pengguna dalam memahami tingkat kemungkinan penyakit.
