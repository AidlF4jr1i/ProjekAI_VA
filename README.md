# 🤖 ProjekAI_VA - Asisten Virtual Berbasis Teks

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)  
Asisten Virtual Sederhana berbasis teks (CLI) menggunakan Python murni tanpa library eksternal.

---

## 📌 Deskripsi

**ProjekAI_VA** adalah aplikasi Command-Line Interface (CLI) berbasis Python yang berfungsi sebagai **asisten virtual sederhana**.  
Aplikasi ini memungkinkan pengguna:

- Menambahkan & melihat jadwal
- Mengirim email ke beberapa kontak
- Mengganti nama sapaan asisten
- Mendengar lelucon random 😄

⚙️ Proyek ini **tidak memerlukan library eksternal** dan cocok sebagai studi kasus Python dasar yang praktis.

---

## 📁 Struktur Folder

```
ProjekAI_VA/
│
├── main.py             # Entry point aplikasi
├── Assistant.py        # Modul utama berisi logika & fungsionalitas
├── receiver_list.txt   # Daftar email penerima (manual)
├── schedule.txt        # Data agenda jadwal (manual/otomatis)
└── README.md           # Dokumentasi proyek
```

---

## 🧠 Arsitektur Sistem

- **Monolitik** berbasis CLI (Command-Line Interface)
- Tidak memerlukan pemisahan frontend/backend
- Penyimpanan data menggunakan file `.txt` sebagai basis data sederhana

### 📌 Peran Tiap Komponen

| File              | Fungsi                                                                 |
|-------------------|------------------------------------------------------------------------|
| `main.py`         | Entry point: menjalankan dan mengontrol jalannya aplikasi              |
| `Assistant.py`    | Inti asisten: menyimpan semua fungsi seperti jadwal, email, jokes dll. |
| `receiver_list.txt`| Daftar penerima email, 1 email per baris                              |
| `schedule.txt`    | Menyimpan jadwal kegiatan/agenda                                       |

---

## 🚀 Cara Menjalankan Proyek

### 1. Persiapan
- Pastikan Python 3.x sudah terinstal  
- Tidak ada dependencies eksternal

### 2. Buat file `receiver_list.txt`
Isi file ini dengan alamat email tujuan, 1 per baris:

```
emailpenerima1@example.com
emailpenerima2@example.com
```

### 3. Jalankan Aplikasi

Buka terminal dan arahkan ke folder proyek, lalu jalankan:

```bash
python main.py
```

---

## 🧭 Menu Utama Aplikasi

Saat aplikasi dijalankan, Anda akan melihat menu seperti berikut:

| No | Fitur                  | Keterangan                                                                 |
|----|------------------------|----------------------------------------------------------------------------|
| 1  | Ubah Nama              | Ganti nama sapaan asisten                                                  |
| 2  | Buat Jadwal            | Tambah jadwal baru ke `schedule.txt`                                       |
| 3  | Lihat Jadwal           | Tampilkan seluruh isi jadwal                                               |
| 4  | Lempar Jokes           | Asisten akan memberi lelucon random 😄                                     |
| 5  | Kirim Email            | Mengirim email ke semua alamat di `receiver_list.txt`                      |
| 0  | Keluar                 | Menutup program                                                            |

---

## 📬 Fitur Kirim Email

Aplikasi akan meminta Anda:

- Memasukkan **alamat email pengirim**
- Memasukkan **App Password Gmail** (bukan password biasa)

> 🔐 **Catatan Penting:**
> Jika menggunakan Gmail:
> - Aktifkan `2-Step Verification`
> - Buat **App Password** di menu "Keamanan Akun Google"
> - Jangan gunakan password utama! Google biasanya akan memblokir login dari aplikasi pihak ketiga jika tidak menggunakan App Password

---

## 🔒 Keamanan Password di Terminal

- Saat memasukkan password, **tidak akan muncul karakter apa pun di terminal** demi keamanan
- Cukup ketik dan tekan Enter

💡 Disarankan untuk menjalankan aplikasi langsung dari terminal/command prompt standar:
- ✅ Windows: Command Prompt / PowerShell
- ✅ macOS/Linux: Terminal
- ❌ Hindari console output dari IDE seperti VS Code atau PyCharm untuk fitur input password

---

## ✅ Ringkasan Fitur

- CLI sederhana tanpa library tambahan
- Penyimpanan data lokal berbasis `.txt`
- Fitur email otomatis ke banyak penerima
- Support joke generator ringan

---

## 🛠️ Untuk Pengembangan Lanjut (Opsional)

Fitur yang dapat dikembangkan di masa depan:

- Integrasi dengan kalender online (Google Calendar)
- Interface berbasis GUI (Tkinter, PyQT)
- Natural Language Processing (NLP) untuk input perintah bebas

---

## 📄 Lisensi

Proyek ini bersifat bebas dan open-source. Gunakan, ubah, dan kembangkan sesuai kebutuhan!

---


