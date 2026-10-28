"""Data penjadwalan: jadwal Semester 5 prodi, KELAS B saja (disederhanakan).

Sumber: file Jadwal_Semester_5.pdf. Hanya mata kuliah berlabel (B) yang dipakai.
Aturan penyederhanaan:
- Tiap mata kuliah 3 SKS = 1 sesi per minggu berdurasi 150 menit (1 blok slot).
- Jam kuliah di jadwal asli tidak seragam, jadi dirapikan menjadi 4 blok 150 menit
  per hari (blok-blok ini muncul di jadwal asli).
- Beberapa mata kuliah diajar tim 2 dosen: kedua dosen harus bebas pada slot tersebut.

PERHATIAN (isi/koreksi sendiri): jumlah mahasiswa kelas B dan kapasitas tiap ruang
TIDAK ada di file jadwal, jadi nilai di bawah hanyalah PLACEHOLDER.
"""

HARI = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat"]
SLOT = ["07:00-09:30", "09:30-12:00", "12:00-14:30", "14:30-17:00"]

JUMLAH_MHS_KELAS_B = 30   # TODO: ganti dengan jumlah mahasiswa kelas B yang sebenarnya

# (nama ruang, kapasitas)  -- kapasitas = TODO, placeholder
RUANG = [
    ("FT5", 40),
    ("FT6", 40),
    ("FT7", 40),
    ("FT8", 40),
    ("F5", 40),
    ("GKT(A)-LT5", 40),
    ("AUDIT", 40),
]

# Kendala lunak: hari yang dihindari dosen (nama dosen -> set indeks hari, 0 = Senin).
# Kosong karena tidak ada di file; isi bila kelompok punya datanya.
PREFERENSI_DOSEN_HINDARI_HARI = {
    # "Deddy Ronaldo": {4},
}

# (kode, nama, [dosen], kelas, jumlah sesi, jumlah mahasiswa)
MATA_KULIAH = [
    ("MP",   "Metodologi Penelitian", ["Devi Karolita", "Jadiaman Parhusip"], "TI-5B", 1, JUMLAH_MHS_KELAS_B),
    ("ADPL", "Analisis dan Desain Perangkat Lunak", ["Deddy Ronaldo", "Licantik"], "TI-5B", 1, JUMLAH_MHS_KELAS_B),
    ("PCD",  "Pengolahan Citra Digital", ["Nahumi Nugrahaningsih", "Tomas Leonardo"], "TI-5B", 1, JUMLAH_MHS_KELAS_B),
    ("JST",  "Jaringan Syaraf Tiruan Kurikulum", ["Nahumi Nugrahaningsih", "Rony Teguh"], "TI-5B", 1, JUMLAH_MHS_KELAS_B),
    ("DM",   "Data Mining", ["Efrans Christian", "Nova Noor Kamala Sari"], "TI-5B", 1, JUMLAH_MHS_KELAS_B),
]


def bangun_sesi():
    """Mengembang mata kuliah menjadi daftar sesi (1 sesi = 1 gen)."""
    sesi = []
    for kode, nama, dosen, kelas, n_sesi, mhs in MATA_KULIAH:
        for k in range(n_sesi):
            sesi.append({
                "kode": kode, "nama": nama, "dosen": list(dosen),
                "kelas": kelas, "sesi_ke": k + 1, "mhs": mhs,
            })
    return sesi
