
# CowTopia Bot

Register : https://t.me/cowtopiabot/app?startapp=1655874127

## Installation

1. **Download Python 3.12+**
   - Pastikan kamu sudah memiliki Python versi 3.10 atau yang lebih baru. Kamu bisa mendownloadnya dari [python.org](https://www.python.org/downloads/).

2. **Install Module**
   - Buka command prompt atau terminal, lalu jalankan perintah:
     ```
     pip install requests colorama
     ```
   - Ini akan menginstal dua modul yang diperlukan: `requests` untuk melakukan permintaan HTTP dan `colorama` untuk memberi warna teks di konsol.

3. **Buka Bot Blum di PC (Telegram Web / Desktop)**
   - Buka Telegram Web atau Telegram Desktop di PC kamu.

4. **Ambil query_id**
   - Buka Bot Blum dan lakukan inspeksi elemen di halaman tersebut.
   - Pergi ke tab Application (biasanya di browser, ada di bagian atas inspector).
   - Pilih `session storage` dan kemudian `cowtopia-prod.tonfarmer.com`.
   - Di dalamnya, cari `__telegram_initparam` dan temukan `tgwebappdata`.
   - Ambil nilai `query_id=xxx` (ambil semua nilai ini kecuali `tgwebappnya`).

5. **Paste di tokens.txt**
   - Buat atau buka file `query.txt` dan paste nilai `query_id` yang telah kamu ambil sebelumnya.
  
## Features
- Auto Get Token
- Auto Upgrade Factory and House
- Auto Clear Mission
- Auto Buy Animal
- Auto Claim Offline Profit
- Auto Claim Daily
- Multi Account
