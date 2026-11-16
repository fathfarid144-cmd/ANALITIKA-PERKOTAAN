# Kesenjangan Jangkauan Sekolah Dasar Negeri di Kota Bandar Lampung
**UAS Analitika Perkotaan (PL25-41003) — Semester Ganjil 2026/2027 — Kelas RA, Kelompok 1**

Repository ini memuat analisis spasial dan statistik terkait kesenjangan jangkauan dan pemerataan fasilitas Sekolah Dasar Negeri (SDN) di 126 kelurahan (20 kecamatan) Kota Bandar Lampung.

---

## 📌 Ringkasan Masalah & Tujuan Analisis
Analisis ini menjawab 3 pertanyaan utama kebijakan perencanaan pendidikan dasar:
1. **Pertanyaan 1 (P1 - Spasial & Jaringan):** Mengukur keterjangkauan rute jalan kaki nyata menuju SDN terdekat menggunakan pemodelan graf jaringan jalan OpenStreetMap (OSM) dan membandingkannya dengan radius garis lurus (*buffer* 1 km).
2. **Pertanyaan 2 (P2 - Non-Spasial):** Menguji hubungan statistik antara kepadatan penduduk kelurahan dengan rasio ketersediaan SD per 1.000 anak usia 7–12 tahun.
3. **Pertanyaan 3 (P3 - Sintesis & Tipologi):** Mengelompokkan tipologi kelurahan menggunakan algoritma *K-Means Clustering* serta menyusun daftar prioritas intervensi kebijakan perkotaan.

---

## 📊 Ringkasan Temuan & Output Analisis

### 1. Keterjangkauan Jaringan Jalan vs Buffer 1 km (P1)
* **Jarak Tempuh Riil:** Median jarak jalan kaki kelurahan ke SDN terdekat adalah **645 meter** (rata-rata 759 m, maksimum 3.651 m).
* **Kesenjangan Akses:** Terdapat **28 kelurahan (22,2%)** yang berada di luar batas wajar jalan kaki (> 1.000 meter), mencakup sekitar **26.463 anak usia 7–12 tahun (22,6% anak kota)**.
* **Kelurahan Terjauh:**
  1. *Batu Putuk* (Kec. Teluk Betung Barat) — 3.651 m
  2. *Campang Raya* (Kec. Sukabumi) — 2.133 m
  3. *Campang Jaya* (Kec. Sukabumi) — 1.762 m
* **Evaluasi Bias Buffer:** Pengukuran garis lurus terbukti menyamarkan kesenjangan; terdapat **13 kelurahan** yang tampak terlayani jika diukur dengan radius 1 km, padahal jarak jaringan jalannya > 1.000 m akibat pola rute memutar dan kontur berbukit.

### 2. Kepadatan Penduduk vs Rasio Layanan (P2)
* **Korelasi Spearman ($\rho = -0,75$, $p < 0,001$):** Hubungan negatif kuat. Kelurahan dengan kepadatan penduduk tinggi memiliki rasio SD per 1.000 anak yang jauh lebih rendah.
* **Korelasi Kepadatan vs Jarak ($\rho = -0,62$, $p < 0,001$):** Kelurahan padat secara fisik dekat dengan sekolah, namun menghadapi beban rasio peserta didik yang tinggi (*overcrowded*).
* **Korelasi Kepadatan vs Jumlah Unit SD ($\rho = 0,11$, $p = 0,22$):** Tidak signifikan, menunjukkan bahwa alokasi gedung SD Negeri secara historis belum mengikuti konsentrasi sebaran anak usia sekolah.

### 3. Tipologi Kelurahan & Prioritas Kebijakan (P3)
Berdasarkan clustering *K-Means* ($k=4$), kelurahan dikelompokkan ke dalam 4 tipologi untuk intervensi yang terarah:
1. **Klaster A — Kritis Jangkauan (33 kelurahan):** Jarak jauh (rata-rata 1.341 m), rasio ketersediaan sekolah rendah.
2. **Klaster B — Padat & Beban Tinggi (28 kelurahan):** Dekat sekolah (rata-rata 417 m), namun kepadatan sangat tinggi (rata-rata 14.801 jiwa/km²) dan beban murid per sekolah berat.
3. **Klaster C — Terlayani Baik (36 kelurahan):** Jarak dekat dan rasio sekolah mencukupi.
4. **Klaster D — Bergantung pada Kelurahan Sekitar (29 kelurahan):** Tidak memiliki gedung SD di dalam batas administrasi, namun aksesibilitas jalan ke SD di kelurahan tetangga masih memadai.

---

## 🏛️ Rekomendasi Intervensi Perencanaan

| Jenis Intervensi | Target Wilayah | Kriteria & Bentuk Tindakan |
|---|---|---|
| **Prioritas 1: Unit Sekolah Baru (USB)** | 14 Kelurahan (Utama: *Batu Putuk, Rajabasa Jaya, Karang Maritim, Jagabaya III, Campang Jaya, Srengsem*) | Jarak jalan kaki > 1.000 m, masuk Klaster A, serta jumlah anak usia SD di atas median kota. Membutuhkan pengadaan lahan dan pembangunan gedung sekolah baru. |
| **Prioritas 2: Ruang Kelas Baru (RKB)** | 19 Kelurahan (Utama: *Tanjung Senang, Kalibalau Kencana, Sukadana Ham, Gunungterang, Rajabasa*) | Kawasan padat dengan jarak dekat namun rasio anak per SD sangat tinggi. Intervensi berupa vertikalisasi bangunan/penambahan ruang kelas untuk menghindari tingginya biaya lahan. |
| **Prioritas 3: Intervensi Non-Fisik** | 14 Kelurahan | Jarak jalan kaki > 1.000 m tetapi jumlah anak relatif sedikit. Intervensi efisien melalui penyediaan rute aman jalan kaki atau angkutan feeder sekolah gratis. |

---

## 📁 Struktur Berkas Output

```text
uas-ra-kelompok1/
├── notebook/
│   ├── uas-ra-kelompok1-notebook.ipynb   # Notebook utama (seluruh sel tereksekusi)
│   └── uas-ra-kelompok1-notebook.html    # Laporan interaktif lengkap (dapat dibuka di browser)
├── data/
│   ├── clean/                            # Data hasil pemrosesan bersih
│   │   ├── kelurahan_indikator_bdl.csv   # 126 kelurahan dengan indikator lengkap
│   │   ├── kelurahan_indikator_bdl.geojson
│   │   ├── sd_negeri_bdl_clean.geojson   # Titik lokasi 166 SDN terproyeksi
│   │   ├── ringkasan_kecamatan.csv       # Agregat per kecamatan
│   │   ├── rekomendasi_prioritas.csv     # Rekomendasi per kelurahan (USB/RKB/Angkutan)
│   │   └── gambar/                       # Peta tematik & visualisasi grafis
│   │       ├── peta1_peta2_jarak_vs_buffer.png
│   │       ├── peta3_peta4_klaster_prioritas.png
│   │       ├── grafik1_perubahan_peringkat.png
│   │       ├── grafik2_boxplot_indikator.png
│   │       ├── grafik3_scatter_kepadatan_rasio.png
│   │       ├── grafik4_jarak_per_kecamatan.png
│   │       ├── grafik5_elbow_silhouette.png
│   │       └── grafik6_profil_klaster.png
│   └── raw/                              # Data mentah & graf jalan kaki OSM
```
