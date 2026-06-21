# Import class yang dibutuhkan
from hewan import Hewan
from kandang import Kandang
from perawatan import Perawatan


# ==================================================
# INHERITANCE
# Class ini mewarisi class Hewan
# ==================================================
class HewanKebunBinatang(Hewan):

    def __init__(self, nama, jenis, kelamin, umur):

        # Memanggil constructor parent
        super().__init__(
            nama,
            jenis,
            kelamin,
            umur
        )

        # Membuat objek kandang
        self.kandang = Kandang("Kandang Umum")

        # Membuat objek perawatan
        self.perawatan = Perawatan()

        # Data makan
        self.jenis_makanan = "-"
        self.jam_makan = "-"
        self.jadwal_makan_berikutnya = "-"

    # ==================================================
    # Menyimpan data pemberian makan
    # ==================================================
    def beri_makan(
        self,
        makanan,
        jam,
        jadwal_berikutnya
    ):

        self.jenis_makanan = makanan
        self.jam_makan = jam
        self.jadwal_makan_berikutnya = jadwal_berikutnya

    # ==================================================
    # Memindahkan kandang hewan
    # ==================================================
    def pindah_kandang(
        self,
        kandang_baru
    ):

        self.kandang.set_nama_kandang(
            kandang_baru
        )

    # ==================================================
    # Menyimpan data kesehatan
    # ==================================================
    def catat_kesehatan(
        self,
        kondisi,
        jam
    ):

        self.perawatan.catat_kondisi(
            kondisi,
            jam
        )

    # ==================================================
    # POLYMORPHISM
    # Override abstract method dari class Hewan
    # ==================================================
    def tampilkan_info(self):

        print("\n===== DETAIL HEWAN =====")

        print("Nama                :", self.get_nama())
        print("Jenis Hewan         :", self.get_jenis())
        print("Kelamin             :", self.get_kelamin())
        print("Umur                :", self.get_umur())

        print("Kandang             :", self.kandang.get_nama_kandang())

        print("Jenis Makanan       :", self.jenis_makanan)
        print("Jam Diberi Makan    :", self.jam_makan)
        print("Jadwal Berikutnya   :", self.jadwal_makan_berikutnya)

        print("Kondisi Hewan       :", self.perawatan.get_kondisi())
        print("Jadwal Pemeriksaan  :", self.perawatan.get_jam_pemeriksaan())