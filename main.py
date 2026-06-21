# ==================================================
# IMPORT MODULE
# ==================================================

# Mengimpor class HewanKebunBinatang dari file terpisah
from hewan_kebun_binatang import HewanKebunBinatang

# Digunakan untuk menghitung jadwal makan berikutnya
from datetime import datetime, timedelta


# ==================================================
# MENYIMPAN SELURUH DATA HEWAN
# ==================================================
daftar_hewan = []


# ==================================================
# FUNGSI MENCARI HEWAN BERDASARKAN NAMA
# Digunakan pada menu pindah kandang,
# cek kesehatan, cek data, dan hapus data
# ==================================================
def cari_hewan(nama):

    for hewan in daftar_hewan:

        if hewan.get_nama().lower() == nama.lower():
            return hewan

    return None


# ==================================================
# MENAMPILKAN SELURUH DATA HEWAN DALAM TABEL
# (READ DATA)
# ==================================================
def tampilkan_semua():

    # Jika belum ada data hewan
    if not daftar_hewan:

        print("\nBelum ada data hewan.")
        return

    print("\n" + "=" * 190)

    # Header tabel
    print(
        f"{'No':<4}"
        f"{'Nama':<15}"
        f"{'Jenis':<15}"
        f"{'Kelamin':<10}"
        f"{'Umur':<12}"
        f"{'Kandang':<20}"
        f"{'Makanan':<15}"
        f"{'Jam Makan':<12}"
        f"{'Jadwal Berikutnya':<18}"
        f"{'Kondisi':<15}"
        f"{'Jadwal Cek':<20}"
    )

    print("=" * 190)

    # Menampilkan seluruh data hewan
    for no, hewan in enumerate(daftar_hewan, start=1):

        print(
            f"{no:<4}"
            f"{hewan.get_nama():<15}"
            f"{hewan.get_jenis():<15}"
            f"{hewan.get_kelamin():<10}"
            f"{hewan.get_umur():<12}"
            f"{hewan.kandang.get_nama_kandang():<20}"
            f"{hewan.jenis_makanan:<15}"
            f"{hewan.jam_makan:<12}"
            f"{hewan.jadwal_makan_berikutnya:<18}"
            f"{hewan.perawatan.get_kondisi():<15}"
            f"{hewan.perawatan.get_jam_pemeriksaan():<20}"
        )


# ==================================================
# PROGRAM UTAMA
# Menampilkan menu secara berulang
# sampai user memilih keluar
# ==================================================
while True:

    print("""
=========================================
 SISTEM MANAJEMEN HEWAN KEBUN BINATANG
=========================================

1. Tambah Hewan
2. Pindah Kandang
3. Beri Makan
4. Cek Kesehatan
5. Cek Data Hewan
6. Hapus Hewan
7. Keluar
""")

    pilihan = input("Pilih menu : ")

    # ==================================================
    # CREATE
    # Menambahkan data hewan baru
    # ==================================================
    if pilihan == "1":

        # Validasi nama tidak boleh kosong
        while True:
            nama = input("Nama Hewan : ").strip()
            if nama:
                break

        # Validasi jenis hewan tidak boleh kosong
        while True:
            jenis = input("Jenis Hewan : ").strip()
            if jenis:
                break

        # Validasi kelamin hanya Jantan atau Betina
        while True:
            kelamin = input(
                "Kelamin (Jantan/Betina): "
            ).capitalize()

            if kelamin in [
                "Jantan",
                "Betina"
            ]:
                break

        # Validasi umur tidak boleh kosong
        while True:
            umur = input(
                "Umur Hewan : "
            ).strip()

            if umur:
                break

        # Membuat object hewan baru
        hewan = HewanKebunBinatang(
            nama,
            jenis,
            kelamin,
            umur
        )

        # Menambahkan object ke list
        daftar_hewan.append(
            hewan
        )

        print(
            "\nData berhasil ditambahkan."
        )

    # ==================================================
    # UPDATE
    # Memindahkan kandang hewan
    # ==================================================
    elif pilihan == "2":

        nama = input(
            "Nama Hewan : "
        )

        hewan = cari_hewan(
            nama
        )

        if hewan:

            print("""
1. Kandang Anak-anak
2. Kandang Umum
3. Kandang Kawin
""")

            pilih = input(
                "Pilih : "
            )

            kandang = {
                "1": "Kandang Anak-anak",
                "2": "Kandang Umum",
                "3": "Kandang Kawin"
            }

            if pilih in kandang:

                hewan.pindah_kandang(
                    kandang[pilih]
                )

                print(
                    "Kandang berhasil diperbarui."
                )

    # ==================================================
    # UPDATE
    # Memberikan makan berdasarkan jenis hewan
    # Semua hewan dengan jenis yang sama
    # akan mendapatkan jadwal makan yang sama
    # ==================================================
    elif pilihan == "3":

        jenis_cari = input(
            "Jenis Hewan : "
        )

        ditemukan = False

        # Mengecek apakah jenis hewan ada
        for h in daftar_hewan:

            if (
                h.get_jenis().lower()
                ==
                jenis_cari.lower()
            ):
                ditemukan = True
                break

        if not ditemukan:

            print(
                "Jenis hewan tidak ditemukan."
            )

            continue

        # Input data makan
        makanan = input(
            "Jenis makanan : "
        )

        jam_awal = input(
            "Start makan (contoh 08.00) : "
        )

        interval = int(
            input(
                "Berapa jam sekali makan : "
            )
        )

        # Mengubah string jam menjadi object waktu
        waktu_awal = datetime.strptime(
            jam_awal,
            "%H.%M"
        )

        # Menghitung jadwal makan berikutnya
        waktu_berikut = (
            waktu_awal +
            timedelta(
                hours=interval
            )
        )

        jadwal = waktu_berikut.strftime(
            "%H.%M"
        )

        # Memberikan makanan ke semua hewan
        # dengan jenis yang sama
        for h in daftar_hewan:

            if (
                h.get_jenis().lower()
                ==
                jenis_cari.lower()
            ):

                h.beri_makan(
                    makanan,
                    jam_awal,
                    jadwal
                )

        # Menampilkan hasil jadwal makan
        print("\n=== JADWAL MAKAN ===")

        print(
            "Jenis Hewan :",
            jenis_cari
        )

        print(
            "Makanan :",
            makanan
        )

        print(
            "Start Makan :",
            jam_awal
        )

        print(
            "Jadwal Berikutnya :",
            jadwal
        )

    # ==================================================
    # UPDATE
    # Mencatat kondisi kesehatan hewan
    # ==================================================
    elif pilihan == "4":

        nama = input(
            "Nama Hewan : "
        )

        hewan = cari_hewan(
            nama
        )

        # Jika hewan tidak ditemukan
        if not hewan:

            print(
                "Hewan tidak ditemukan."
            )

            continue

        status = input(
            "Apakah hewan sakit? (YA/TIDAK): "
        ).upper()

        # Jika hewan sakit
        if status == "YA":

            jam = input(
                "Jadwal pemeriksaan (14.00): "
            )

            # Otomatis pindah ke kandang isolasi
            hewan.pindah_kandang(
                "Kandang Isolasi"
            )

            # Simpan data kesehatan
            hewan.catat_kesehatan(
                "Sakit",
                jam
            )

            print(
                "Hewan dipindahkan ke Kandang Isolasi."
            )

        # Jika hewan sehat
        elif status == "TIDAK":

            # Otomatis kembali ke kandang umum
            hewan.pindah_kandang(
                "Kandang Umum"
            )

            # Jadwal pemeriksaan rutin
            hewan.catat_kesehatan(
                "Sehat",
                "1 Bulan Sekali"
            )

            print(
                "Hewan sehat dan kembali ke Kandang Umum."
            )

    # ==================================================
    # READ
    # Menampilkan data hewan
    # ==================================================
    elif pilihan == "5":

        print("""
1. Cek Data Satuan
2. Cek Semua Data
""")

        sub = input(
            "Pilih : "
        )

        # Menampilkan satu hewan
        if sub == "1":

            nama = input(
                "Nama Hewan : "
            )

            hewan = cari_hewan(
                nama
            )

            if hewan:

                hewan.tampilkan_info()

        # Menampilkan seluruh hewan
        elif sub == "2":

            tampilkan_semua()

    # ==================================================
    # DELETE
    # Menghapus data hewan
    # ==================================================
    elif pilihan == "6":

        nama = input(
            "Nama Hewan : "
        )

        hewan = cari_hewan(
            nama
        )

        if hewan:

            daftar_hewan.remove(
                hewan
            )

            print(
                "Data berhasil dihapus."
            )

    # ==================================================
    # KELUAR PROGRAM
    # ==================================================
    elif pilihan == "7":

        print(
            "Terima kasih."
        )

        break