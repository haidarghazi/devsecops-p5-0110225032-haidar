# Secure Notes CLI — DevSecOps Demo

Aplikasi CLI sederhana untuk mengelola catatan teks secara lokal. Proyek ini dibuat sebagai demonstrasi pipeline DevSecOps: build/test otomatis, Static Application Security Testing (SAST), dan Quality Gate.

## Teknologi
- Python 3.12
- `unittest` untuk unit test
- Bandit untuk SAST
- GitHub Actions untuk CI

## Struktur proyek
```text
.
devsecops-p5-[nim-anda]/
├── .github/
│   └── workflows/
│       └── devsecops.yml
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── notes.py
│   ├── validation.py
│   └── storage.py
├── tests/
│   └── test_notes.py
├── requirements.txt
└── .github/workflows/devsecops.yml
```

## Cara menjalankan
Pastikan Python 3.12 atau versi kompatibel sudah terpasang.

```bash
python -m app.main
```

Jalankan unit test:
```bash
python -m unittest discover -s tests -v
```

Jalankan pemindaian keamanan secara lokal:
```bash
python -m pip install -r requirements.txt
bandit -r app --severity-level medium --confidence-level medium
```

## Overview pipeline
Workflow `.github/workflows/devsecops.yml` dipicu saat ada `push` ke branch `main` atau `pull_request` yang menargetkan `main`. Job `build` mengatur Python, memasang dependensi, dan menjalankan unit test. Job `sast-scan` baru berjalan setelah `build` berhasil (`needs: build`), lalu menjalankan Bandit. Quality Gate ditetapkan pada tingkat severity dan confidence medium atau lebih tinggi; temuan yang memenuhi ambang tersebut membuat job SAST gagal sehingga perubahan perlu diperiksa sebelum diterima.

> Catatan: sesuaikan nama repository dengan NIM Anda. Setelah workflow dijalankan di GitHub, tambahkan screenshot repository dan tab Actions serta isi hasil aktual pada laporan.
