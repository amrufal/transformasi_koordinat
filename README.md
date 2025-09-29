# Transformasi Koordinat 3D dengan Python & NumPy

## 📌 Latar Belakang
Proyek ini adalah simulasi transformasi koordinat menggunakan bahasa pemrograman **Python** dan pustaka **NumPy**.  
Sebuah titik awal pada kerangka acuan *U* direpresentasikan dalam bentuk koordinat homogen, lalu ditransformasikan ke kerangka acuan *B* menggunakan kombinasi **rotasi** (roll, pitch, yaw) dan **translasi**. Semua operasi diwujudkan dalam bentuk perkalian matriks homogen berukuran 4×4. Dengan mengubah variabel konfigurasi di bagian awal program, pengguna dapat menguji berbagai kasus transformasi tanpa mengubah logika utama.

---

## 🎯 Tujuan
- Mempelajari konsep transformasi koordinat homogen dalam memodelkan perubahan posisi dan orientasi titik di ruang 3D.  
- Memahami cara membangun matriks rotasi dan translasi dalam bentuk matriks homogen 4×4.  
- Mengimplementasikan transformasi koordinat homogen menggunakan Python dan NumPy.  
- Merancang program Python yang dapat menghitung posisi titik setelah diberikan rotasi dan translasi tertentu.  
- Menyediakan program modular yang mudah digunakan sebagai sarana pembelajaran.  

---

## ✨ Fitur Proyek
- **Konfigurasi sederhana** di awal program: ubah nilai titik, sudut rotasi, atau translasi tanpa memodifikasi logika inti.  
- **Matriks homogen 4×4** yang menyatukan rotasi dan translasi dalam satu operasi.  
- **Fungsi modular** untuk rotasi di sekitar sumbu X, Y, dan Z serta translasi.  
- **Menampilkan hasil** berupa matriks transformasi dan koordinat titik sebelum & sesudah transformasi.  

---

## 🛠️ Software yang Dibutuhkan
- **Python** ≥ 3.8 → bahasa pemrograman utama.  
- **NumPy** → pustaka Python untuk operasi vektor/matriks.  
- **Editor Teks / IDE** (VS Code, PyCharm, atau lainnya).  
- **Terminal / Command Prompt** → untuk mengeksekusi program.  

## 🚀 Tutorial Penggunaan

1. **Instalasi Python dan NumPy**  
   - Pastikan Python (versi ≥ 3.8) sudah terpasang pada komputer Anda.  
   - Instal pustaka NumPy dengan perintah:  
     ```bash
     pip install numpy
     ```

2. **Persiapan Folder Kerja**  
   - Simpan file program `transformasi.py` di dalam satu folder kerja.  
   - Pastikan semua file pendukung (jika ada) berada di folder yang sama.  

3. **Edit Bagian Konfigurasi Program**  
   - Buka file `transformasi.py` menggunakan editor teks (misalnya VS Code atau Notepad++).  
   - Ubah nilai variabel konfigurasi di bagian awal program:  
     - Sudut rotasi: `roll`, `pitch`, `yaw` (satuan derajat).  
     - Vektor translasi: `tx`, `ty`, `tz`.  
     - Titik awal yang akan ditransformasi: `px`, `py`, `pz`.  

4. **Menjalankan Program**  
   - Buka terminal atau command prompt pada folder kerja.  
   - Jalankan program dengan perintah:  
     ```bash
     python transformasi.py
     ```

5. **Melihat Hasil**  
   - Program akan menampilkan:  
     - Matriks transformasi homogen berukuran 4×4.  
     - Koordinat titik sebelum transformasi.  
     - Koordinat titik setelah transformasi.  
   - Hasil ditampilkan langsung pada terminal.  
