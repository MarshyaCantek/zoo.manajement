from hewan_kebun_binatang import HewanKebunBinatang
from datetime import datetime, timedelta

# LIST PENYIMPANAN DATA HEWAN
daftar_hewan = []

# MENCARI HEWAN BERDASARKAN NAMA
def cari_hewan(nama):
    for hewan in daftar_hewan:
        if hewan.get_nama().lower() == nama.lower():
            return hewan
    return None

# MENAMPILKAN SELURUH DATA HEWAN
def tampilkan_semua():

    if not daftar_hewan:
        print("\nBelum ada data hewan.")
        return

    print("\n" + "=" * 140)
    print("DATA SELURUH HEWAN KEBUN BINATANG TRIPGI".center(140))
    print("=" * 140)

    print(
        f"{'No':<4}"
        f"{'Nama Hewan':<18}"
        f"{'Jenis Hewan':<18}"
        f"{'Jenis Kelamin':<18}"
        f"{'Umur':<15}"
        f"{'Kandang':<20}"
        f"{'Makanan':<15}"
        f"{'Jam Makan':<12}"
        f"{'Kondisi':<15}"
        f"{'Jadwal Cek Kesehatan':<25}"
    )

    print("-" * 140)

    for no, hewan in enumerate(daftar_hewan, start=1):

        print(
            f"{no:<4}"
            f"{hewan.get_nama():<18}"
            f"{hewan.get_jenis():<18}"
            f"{hewan.get_jenis_kelamin():<18}"
            f"{hewan.get_umur():<15}"
            f"{hewan.kandang.get_nama_kandang():<20}"
            f"{hewan.jenis_makanan:<15}"
            f"{hewan.jam_makan:<12}"
            f"{hewan.perawatan.get_kondisi():<15}"
            f"{hewan.perawatan.get_jam_pemeriksaan():<25}"
        )

    print("=" * 140)

    print("""
KETERANGAN:
- Nama Hewan            : Nama individu hewan
- Jenis Hewan           : Spesies hewan
- Jenis Kelamin         : Jantan / Betina
- Umur                  : Umur hewan (contoh: 10 Hari, 2 Bulan, 5 Tahun)
- Kandang               : Lokasi kandang saat ini
- Makanan               : Jenis makanan terakhir yang diberikan
- Jam Makan             : Waktu pemberian makan terakhir
- Kondisi               : Status kesehatan hewan
- Jadwal Cek Kesehatan  : Jadwal pemeriksaan kesehatan hewan
""")

# PROGRAM UTAMA
while True:
    print("""
=================================================
 SISTEM MANAJEMEN HEWAN KEBUN BINATANG TRIPGI
=================================================

1. Tambah Hewan
2. Pindah Kandang
3. Beri Makan
4. Cek Kesehatan
5. Cek Data Hewan
6. Hapus Hewan
7. Keluar
""")

    pilihan = input("Pilih menu (1-7): ")

    # MENU 1 - CREATE
    if pilihan == "1":
        print("\n=== TAMBAH HEWAN ===")

        while True:
            nama = input("Nama Hewan : ").strip()
            if nama:
                break
            print("Nama tidak boleh kosong.")

        while True:
            jenis = input("Jenis Hewan : ").strip()
            if jenis:
                break
            print("Jenis tidak boleh kosong.")

        while True:
            jenis_kelamin = input("Jenis Kelamin (Jantan/Betina): ").capitalize()
            if jenis_kelamin in ["Jantan","Betina"]:
                break
            print("Masukkan Jantan atau Betina.")

        while True:
            umur = input("Umur Hewan (Hari, Bulan, Tahun) : ").strip()
            if umur:
                break
            print("Umur tidak boleh kosong.")

        hewan = HewanKebunBinatang(nama, jenis, jenis_kelamin, umur)

        daftar_hewan.append(hewan)
        print("\nData hewan berhasil ditambahkan.")

    # MENU 2 - PINDAH KANDANG
    elif pilihan == "2":
        nama = input("Nama Hewan : ")
        hewan = cari_hewan(nama)

        if hewan:
            print("""
1. Kandang Anak-anak
2. Kandang Umum
3. Kandang Kawin
""")

            pilih = input("Pilih kandang : ")

            kandang = {
                "1": "Kandang Anak-anak",
                "2": "Kandang Umum",
                "3": "Kandang Kawin",
            }

            if pilih in kandang:

                hewan.pindah_kandang(kandang[pilih])

                if kandang[pilih] != "Kandang Isolasi":
                    hewan.kandang_sebelumnya = (kandang[pilih])
                print(
                    "\nKandang berhasil diperbarui.")

        else:
            print("\nHewan tidak ditemukan.")

    # MENU 3 - BERI MAKAN
    elif pilihan == "3":
        print("\n=== PEMBERIAN MAKAN ===")

        while True:
            jenis_cari = input("Masukkan jenis hewan : ").strip()

            hewan_ditemukan = []
            for h in daftar_hewan:

                if (h.get_jenis().lower()==jenis_cari.lower()):
                    hewan_ditemukan.append(h)

            if hewan_ditemukan:
                break
            print("Jenis hewan tidak ditemukan.")

        makanan = input("Jenis makanan : ")

        while True:
            jam_awal = input("Waktu mulai makan (format HH.MM): ")

            try:
                datetime.strptime(jam_awal,"%H.%M")
                break

            except ValueError:
                print("Format jam harus HH.MM")

        while True:
            try:
                interval = int(input("Interval pemberian makan (jam): "))

                if interval > 0:
                    break
            except:
                pass
            print("Masukkan angka yang valid.")

        waktu_awal = datetime.strptime(jam_awal,"%H.%M")

        jadwal_otomatis = []
        waktu_sekarang = waktu_awal

        for i in range(9):
            waktu_sekarang = (waktu_sekarang + timedelta(hours=interval))

            jadwal_otomatis.append(waktu_sekarang.strftime("%H.%M"))

        for h in hewan_ditemukan:
            h.beri_makan(makanan, jam_awal, jadwal_otomatis[0])

        print("\n")
        print("=" * 55)
        print("JADWAL PEMBERIAN MAKAN OTOMATIS")
        print("=" * 55)
        print("\nJenis Hewan :", jenis_cari)
        print("Makanan     :", makanan)
        print("Waktu Awal  :", jam_awal)
        print("\nJadwal Pemberian Makan Selanjutnya:")

        for no, jam in enumerate(jadwal_otomatis, start=1):
            print(f"{no}. Pukul {jam}")
        print("=" * 55)

    # MENU 4 - CEK KESEHATAN
    elif pilihan == "4":
        nama = input("Nama Hewan : ")
        hewan = cari_hewan(nama)

        if not hewan:
            print("Hewan tidak ditemukan.")
            continue

        status = input("Apakah hewan sakit? (YA/TIDAK): ").upper()

        # HEWAN SAKIT
        if status == "YA":
            jam = input("Jam pemeriksaan (contoh 14.00): ")

            if (hewan.kandang.get_nama_kandang()!="Kandang Isolasi"):
                hewan.kandang_sebelumnya = (hewan.kandang.get_nama_kandang())

            hewan.pindah_kandang("Kandang Isolasi")

            hewan.catat_kesehatan("Sakit", jam)
            print("\nHewan dipindahkan ke Kandang Isolasi.")

        # HEWAN SEHAT
        elif status == "TIDAK":

            hewan.pindah_kandang(hewan.kandang_sebelumnya)

            hewan.catat_kesehatan("Sehat", "1 Bulan Sekali")

            print("\nHewan dinyatakan sehat.")
            print("Dikembalikan ke:", hewan.kandang_sebelumnya)

    # MENU 5 - READ
    elif pilihan == "5":

        print("""
1. Cek Data Satuan
2. Cek Semua Data
""")

        sub = input("Pilih : ")

        if sub == "1":
            nama = input("Nama Hewan : ")
            hewan = cari_hewan(nama)

            if hewan:
                hewan.tampilkan_info()

            else:
                print("Hewan tidak ditemukan.")

        elif sub == "2":
            tampilkan_semua()

    # MENU 6 - DELETE
    elif pilihan == "6":
        nama = input("Nama Hewan : ")
        hewan = cari_hewan(nama)

        if hewan:
            daftar_hewan.remove(hewan)
            print("\nData berhasil dihapus.")

        else:
            print("\nHewan tidak ditemukan.")

    # MENU 7 - EXIT
    elif pilihan == "7":
        print("\nTerima kasih telah menggunakan sistem.")
        break

    else:
        print("\nMenu tidak valid.")