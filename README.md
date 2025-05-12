# Time Server and Client (Multithreaded TCP-based)

## 📋 Deskripsi
Proyek ini merupakan implementasi **Time Server** berbasis TCP socket yang berjalan pada port `45000`. Server ini mampu menangani beberapa koneksi client secara **concurrent** menggunakan konsep **multithreading**. Setiap client dapat mengirim perintah untuk mendapatkan waktu saat ini dari server atau menutup koneksi dengan perintah `QUIT`.

## 🧩 Fitur
- Server membuka port `45000` menggunakan protokol **TCP**.
- Setiap client yang terhubung akan dilayani dalam thread tersendiri.
- Perintah yang dikenali oleh server:
  - `TIME\r\n`: Mengembalikan waktu sekarang dalam format `dd mm yyyy HH:MM:SS`.
  - `QUIT\r\n`: Menutup koneksi dengan client.
  - Perintah lainnya akan menghasilkan respon error.



## 🚀 Cara Menjalankan Program

### 1. Jalankan Server

Buka terminal dan jalankan file `timeServer.py`:

```bash
python timeServer.py
```

Output akan menampilkan log setiap kali ada client yang terhubung dan permintaan yang diterima.

### 2. Jalankan Client

Buka terminal baru dan jalankan `client.py`:

```bash
python timeClient.py
```

Kemudian kamu akan diminta untuk memasukkan perintah untuk masing-masing client yang berjalan secara paralel:

```
Enter command for client 0 (TIME, QUIT, or anything else): TIME
Enter command for client 1 (TIME, QUIT, or anything else): HELLO
Enter command for client 2 (TIME, QUIT, or anything else): QUIT
```

Jika kamu memasukkan `TIME`, maka server akan mengembalikan waktu sekarang. Kamu akan ditanya apakah ingin mengirim `QUIT` untuk menutup koneksi.

## 📦 Contoh Output (Client)

```bash
[Client-0] Sending: TIME
[Client-0] Received: JAM 05 05 2025 19:35:12
Send QUIT to close the connection? (y/n): y
[Client-0] Sending: QUIT
```

## 🔒 Catatan Keamanan
Untuk keperluan produksi, pastikan port yang digunakan tidak terbuka untuk publik jika tidak diperlukan. Gunakan autentikasi dan enkripsi jika ingin mengembangkan lebih lanjut.

## 🧑‍💻 Author
- Nama: Muhammad Bimatara Indianto
- Tugas: Pembuatan Time Server TCP Multithreaded
- Mata Kuliah: Pemrograman Jaringan 