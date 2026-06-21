from hewan import Hewan
from kandang import Kandang
from perawatan import Perawatan

# CLASS HEWAN KEBUN BINATANG
# Pilar OOP:
# Inheritance
# Polymorphism

class HewanKebunBinatang(Hewan):

    def __init__(self, nama, jenis, jenis_kelamin, umur):

        super().__init__(
            nama,
            jenis,
            jenis_kelamin,
            umur            
        )

        # Kandang awal
        self.kandang = Kandang(
            "Kandang Umum"
        )

        # Menyimpan kandang sebelum sakit
        self.kandang_sebelumnya = (
            "Kandang Umum"
        )

        # Objek perawatan
        self.perawatan = Perawatan()

        # Data makan
        self.jenis_makanan = "-"
        self.jam_makan = "-"
        self.jadwal_makan_berikutnya = "-"

    # UPDATE DATA MAKAN
    def beri_makan(
        self,
        makanan,
        jam,
        jadwal="-"
    ):

        self.jenis_makanan = makanan
        self.jam_makan = jam
        self.jadwal_makan_berikutnya = jadwal

    # PINDAH KANDANG
    def pindah_kandang(
        self,
        kandang_baru
    ):

        self.kandang.set_nama_kandang(
            kandang_baru
        )

    # CATAT KESEHATAN
    def catat_kesehatan(
        self,
        kondisi,
        jam
    ):

        self.perawatan.catat_kondisi(
            kondisi,
            jam
        )

    # POLYMORPHISM
    # Override method abstract
    def tampilkan_info(self):

        print("\n===== DETAIL HEWAN =====")

        print(
            "Nama                :",
            self.get_nama()
        )

        print(
            "Jenis Hewan         :",
            self.get_jenis()
        )

        print(
            "Jenis Kelamin       :",
            self.get_jenis_kelamin()
        )

        print(
            "Umur                :",
            self.get_umur()
        )

        print(
            "Kandang             :",
            self.kandang.get_nama_kandang()
        )

        print(
            "Jenis Makanan       :",
            self.jenis_makanan
        )

        print(
            "Jam Diberi Makan    :",
            self.jam_makan
        )

        print(
            "Jadwal Makan Berikut:",
            self.jadwal_makan_berikutnya
        )

        print(
            "Kondisi Hewan       :",
            self.perawatan.get_kondisi()
        )

        print(
            "Jadwal Pemeriksaan  :",
            self.perawatan.get_jam_pemeriksaan()
        )