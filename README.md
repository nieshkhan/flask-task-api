# Task API — Personal REST API dengan Flask

REST API sederhana untuk mencatat dan mengelola daftar tugas (to-do list), dibangun dengan Python dan Flask. Data disimpan secara permanen di file JSON, dilengkapi validasi input dan error handling, serta automated testing dengan pytest.

## Fitur

- Tambah task baru (`POST /tasks`)
- Lihat semua task (`GET /tasks`)
- Tandai task sebagai selesai (`PUT /tasks/<index>`)
- Hapus task (`DELETE /tasks/<index>`)
- Data tersimpan permanen ke `tasks.json` — tidak hilang saat server restart
- Validasi input (menolak data kosong atau tipe data salah)
- Error handling untuk index yang tidak valid
- Automated testing dengan pytest untuk semua endpoint

## Cara Install & Jalankan

```bash
# Install dependency
python -m pip install flask pytest

# Jalankan server
python app.py
```

Server berjalan di `http://127.0.0.1:5000`

## Endpoint API

| Method | Endpoint | Deskripsi | Body |
|---|---|---|---|
| GET | `/` | Cek server berjalan | - |
| GET | `/tasks` | Ambil semua task | - |
| POST | `/tasks` | Tambah task baru | `{"text": "nama task"}` |
| PUT | `/tasks/<index>` | Tandai task selesai | - |
| DELETE | `/tasks/<index>` | Hapus task | - |

### Contoh Request

**Tambah task:**
```bash
curl -X POST http://127.0.0.1:5000/tasks -H "Content-Type: application/json" -d "{\"text\": \"belajar flask\"}"
```

**Response:**
```json
{"text": "belajar flask", "done": false}
```

### Error Handling

| Status Code | Kondisi |
|---|---|
| 400 | Field `text` kosong, hilang, atau bukan string |
| 404 | Index task tidak ditemukan |

## Testing

Project ini menggunakan pytest untuk automated testing di semua endpoint.

```bash
python -m pytest
```

## What I Learned

**Python:**
Saya belajar konsep `global` lewat variable `tasks` — `global` dibutuhkan ketika sebuah fungsi (seperti `load_tasks()`) perlu **mengganti seluruh isi** variable yang ada di luar fungsi, bukan cuma membuat variable baru yang sifatnya lokal. Ini beda dengan `tasks.append(...)` di `add_task()` yang tidak butuh `global`, karena itu cuma mengubah isi list yang sudah ada, bukan mengganti variable-nya. Saya juga belajar bahwa `return` menghentikan eksekusi fungsi seketika (kode setelahnya tidak akan pernah jalan), cara menangani error dengan `try/except` (`FileNotFoundError`, `JSONDecodeError`), membuat guard clause untuk mengecek kondisi tidak valid di awal fungsi sebelum masuk ke logic utama (termasuk `isinstance()` untuk validasi tipe data), bahwa index list dimulai dari 0 sehingga `len(list) - 1` dipakai untuk mengakses index terakhir, dan bahwa import bisa saling menimpa kalau ada nama sama dari modul berbeda (`json` bawaan Python vs `json` dari Flask).

**Flask & REST API:**
Saya belajar bahwa Flask otomatis mengubah dict Python jadi JSON response, penggunaan HTTP status code yang tepat (200 untuk sukses, 400 untuk request salah, 404 untuk tidak ditemukan), perbedaan HTTP method (GET untuk membaca task, POST untuk menambah, PUT untuk menandai selesai, DELETE untuk menghapus), serta pola in-memory + persistent storage — data diakses cepat lewat variable, lalu disinkronkan ke file secara permanen.

**Testing:**
Saya belajar automated testing dengan pytest sebagai pengganti testing manual berulang di Postman, menggunakan `test_client()` untuk simulasi request tanpa perlu server benar-benar jalan, konsep test isolation (kenapa hardcode index berbahaya kalau data dibagi antar test lewat variable global), serta cara membaca error/traceback Python untuk debugging (`KeyError`, `IndexError`, `SyntaxError`, `AttributeError`).

**Git:**
Saya belajar penggunaan `.gitignore` untuk mengabaikan file yang bukan bagian dari kode (data runtime, cache), dan membuat commit terpisah per fitur alih-alih satu commit besar.

## Tech Stack

- Python 3.12
- Flask
- pytest