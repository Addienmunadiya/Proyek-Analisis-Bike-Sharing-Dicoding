# Bike Sharing Analysis Project
Proyek ini bertujuan untuk menganalisis tren peminjaman sepeda berdasarkan data dari tahun 2011 hingga 2012. Kami akan mengeksplorasi pola peminjaman sepeda, termasuk perbandingan antara tahun 2011 dan 2012, serta faktor-faktor lingkungan seperti musim, cuaca, dan waktu yang mempengaruhi lonjakan peminjaman sepeda.
## Hasil
Berdasarkan hasil analisis tren peminjaman sepeda menggunakan **Bike Sharing Dataset** antara tahun 2011 dan 2012, dapat disimpulkan beberapa hal penting:

1. **Tren Peminjaman Sepeda (2011-2012)**:
   - **Tahun 2011**: Peminjaman sepeda mengalami kenaikan signifikan pada kuartal pertama dan lonjakan pesat pada kuartal kedua. Namun, kuartal ketiga menunjukkan penurunan yang meskipun tidak drastis, terus berlanjut hingga kuartal keempat, dengan penurunan yang lebih tajam.
   - **Tahun 2012**: Pada akhir kuartal pertama, terdapat kenaikan sangat signifikan yang berlanjut hingga kuartal ketiga. Penurunan kembali terjadi pada kuartal keempat. Meskipun ada fluktuasi, secara keseluruhan peminjaman sepeda menunjukkan tren yang lebih positif pada tahun 2012.

2. **Musim dan Cuaca**:
   - **Musim**: Peminjaman sepeda tertinggi terjadi pada musim gugur (fall) dan musim panas (summer).
   - **Cuaca**: Puncak peminjaman sepeda terjadi saat cuaca cerah (clear) dan berawan, terutama saat cuaca cerah.

3. **Waktu Peminjaman**:
   - **Puncak Peminjaman**: Puncak peminjaman sepeda terjadi pada pukul 5 sore dan 6 sore, dengan masing-masing melebihi 300.000 peminjam. Peningkatan ini kemungkinan terkait dengan aktivitas harian seperti pulang kerja atau kegiatan luar ruangan.
   
4. **Clustering Berdasarkan Jam dan Hari**:
   - **Senin hingga Jumat**: Pemimpin sepeda meningkat signifikan pada pukul 8 pagi, 5 sore, dan 6 sore.
   - **Sabtu dan Minggu**: Peminjaman sepeda cenderung meningkat pada siang hari antara pukul 12 siang hingga 3 sore.

Secara keseluruhan, analisis ini menunjukkan pola peminjaman sepeda yang dapat dipengaruhi oleh berbagai faktor seperti waktu, cuaca, dan hari dalam seminggu. Visualisasi clustering melalui heatmap juga membantu untuk memberikan gambaran yang lebih jelas tentang tren dan perilaku peminjam sepeda.
## Persyaratan Sistem
Pastikan telah menginstal:
- Python 3.12 atau versi lebih baru
- pip (Manajer Paket Python)
## Cara Menjalankan
### Open Dashboard on URL 
1.Open the link https://addienmunadiya-bikesharingdataset.streamlit.app/
### Open Dashboard on Local 
1. Clone Repository
```bash
https://github.com/Addienmunadiya/Proyek-Analisis-Bike-Sharing-Dicoding
```
2. Setup Environment
```bash
conda create --name main-ds python
conda activate main-ds
```
3. Install the required Python packages
```bash
cd Dashboard
```
```bash
pip install -r requirements.txt
```
4. Run Streamlit in Local
```bash
streamlit run streamlitdashboardlocal.py
```
5.Run Streamlit with the link 
```bash
https://dashboardonline-addienmunadiya.streamlit.app/
```
