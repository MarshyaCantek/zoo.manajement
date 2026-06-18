from hewan_kebun_binatang import HewanKebunBinatang

# Menyimpan seluruh objek hewan
daftar_hewan = []


# =====================================
# Mencari hewan berdasarkan nama
# =====================================
def cari_hewan(nama):

    for hewan in daftar_hewan:

        if hewan.get_nama().lower() == nama.lower():
            return hewan

    return None


# =====================================
# Menampilkan seluruh data hewan
# =====================================
def tampilkan_semua():

    if not daftar_hewan:

        print("\nBelum ada data hewan.")
        return

    print("\n" + "=" * 145)

    print(
        f"{'No':<4}"
        f"{'Nama':<15}"
        f"{'Jenis Hewan':<15}"
        f"{'Kelamin':<10}"
        f"{'Umur':<8}"
        f"{'Kandang':<20}"
        f"{'Makanan':<15}"
        f"{'Jam Di BeriMakan':<12}"
        f"{'Kondisi Hewan':<20}"
        f"{'Jam Cek Kesehatan':<12}"
    )

    print("=" * 145)

    for no, hewan in enumerate(daftar_hewan, start=1):

        print(
            f"{no:<4}"
            f"{hewan.get_nama():<15}"
            f"{hewan.get_jenis():<15}"
            f"{hewan.get_kelamin():<10}"
            f"{hewan.get_umur():<8}"
            f"{hewan.kandang.get_nama_kandang():<20}"
            f"{hewan.jenis_makanan:<15}"
            f"{hewan.jam_makan:<12}"
            f"{hewan.perawatan.get_kondisi():<20}"
            f"{hewan.perawatan.get_jam_pemeriksaan():<12}"
        )

    print("=" * 145)


# =====================================
# PROGRAM UTAMA
# =====================================
while True:

    print("""
=========================================
 SISTEM MANAJEMEN HEWAN KEBUN BINATANG
=========================================

1. Tambah Hewan
2. Pindah Kandang
3. Beri Makan
4. Catat Kesehatan
5. Cek Data Hewan
6. Hapus Hewan
7. Keluar
""")

    pilihan = input("Pilih menu (1-7): ")

    # =====================================
    # CREATE
    # =====================================
    if pilihan == "1":

        print("\n=== TAMBAH HEWAN ===")

        nama = input("Nama Hewan  : ")
        jenis = input("Jenis Hewan : ")
        kelamin = input("Jenis Kelamin Hewan (Betina / Jantan) : ")
        umur = input("Umur Hewan  : ")

        hewan = HewanKebunBinatang(
    nama,
    jenis,
    kelamin,
    umur
)

        print("\nData hewan berhasil ditambahkan.")

    # =====================================
    # UPDATE KANDANG
    # =====================================
        daftar_hewan.append(hewan)

        print("\nData hewan berhasil ditambahkan.")

    # =====================================
    # UPDATE KANDANG
    # =====================================
    elif pilihan == "2":

        print("\n=== PINDAH KANDANG ===")

        nama = input("Masukkan nama hewan : ")

        hewan = cari_hewan(nama)

        if hewan:

            print("""
Pilihan Kandang:

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

                hewan.pindah_kandang(
                    kandang[pilih]
                )

                print(
                    "\nKandang berhasil diperbarui."
                )

            else:

                print(
                    "\nPilihan kandang tidak valid."
                )

        else:

            print(
                "\nHewan tidak ditemukan."
            )

    # =====================================
    # UPDATE MAKAN
    # =====================================
    elif pilihan == "3":

        print("\n=== PEMBERIAN MAKAN ===")

        nama = input("Masukkan nama hewan : ")

        hewan = cari_hewan(nama)

        if hewan:

            makanan = input(
                "Jenis makanan : "
            )

            jam = input(
                "Jam makan (contoh: 08:00) : "
            )

            hewan.beri_makan(
                makanan,
                jam
            )

            print(
                "\nData makan berhasil disimpan."
            )

        else:

            print(
                "\nHewan tidak ditemukan."
            )

    # =====================================
    # UPDATE KESEHATAN
    # =====================================
    elif pilihan == "4":

        print("\n=== CATAT KESEHATAN ===")

        nama = input("Masukkan nama hewan : ")

        hewan = cari_hewan(nama)

        if hewan:

            kondisi = input(
                "Kondisi kesehatan : "
            )

            jam = input(
                "Jam pemeriksaan (contoh: 08:00) : "
            )

            hewan.catat_kesehatan(
                kondisi,
                jam
            )

            print(
                "\nData kesehatan berhasil disimpan."
            )

        else:

            print(
                "\nHewan tidak ditemukan."
            )

    # =====================================
    # READ
    # =====================================
    elif pilihan == "5":

        print("""
=========================
 CEK INFO HEWAN
=========================

1. Cek Info Hewan Satuan
2. Cek Info Seluruh Hewan
""")

        sub_menu = input(
            "Pilih menu (1/2): "
        )

        # Detail 1 hewan
        if sub_menu == "1":

            nama = input(
                "Masukkan nama hewan : "
            )

            hewan = cari_hewan(nama)

            if hewan:

                hewan.tampilkan_info()

            else:

                print(
                    "\nHewan tidak ditemukan."
                )

        # Seluruh hewan
        elif sub_menu == "2":

            tampilkan_semua()

        else:

            print(
                "\nPilihan tidak valid."
            )

    # =====================================
    # DELETE
    # =====================================
    elif pilihan == "6":

        print("\n=== HAPUS DATA HEWAN ===")

        nama = input(
            "Masukkan nama hewan : "
        )

        hewan = cari_hewan(nama)

        if hewan:

            daftar_hewan.remove(
                hewan
            )

            print(
                "\nData berhasil dihapus."
            )

        else:

            print(
                "\nHewan tidak ditemukan."
            )

    # =====================================
    # KELUAR
    # =====================================
    elif pilihan == "7":

        print(
            "\nTerima kasih telah menggunakan sistem."
        )

        break

    else:

        print(
            "\nMenu tidak valid."
        )