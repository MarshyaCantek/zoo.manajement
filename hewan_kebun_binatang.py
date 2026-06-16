from hewan import Hewan
from kandang import Kandang
from perawatan import Perawatan

class HewanKebunBinatang(Hewan):

    def __init__(self, nama, jenis, kelamin, umur):

        super().__init__(
            nama,
            jenis,
            kelamin,
            umur
        )

        self.kandang = Kandang("Kandang Umum")
        self.perawatan = Perawatan()

        self.jenis_makanan = "-"
        self.jam_makan = "-"

    def beri_makan(self, makanan, jam):
        self.jenis_makanan = makanan
        self.jam_makan = jam

    def pindah_kandang(self, kandang_baru):
        self.kandang.set_nama_kandang(kandang_baru)

    def catat_kesehatan(self, kondisi, jam):
        self.perawatan.catat_kondisi(kondisi, jam)

    def tampilkan_info(self):

        print("\n===== DETAIL HEWAN =====")

        print("Nama                :", self.get_nama())
        print("Jenis Hewan         :", self.get_jenis())
        print("Kelamin             :", self.get_kelamin())
        print("Umur                :", self.get_umur())

        print("Kandang             :", self.kandang.get_nama_kandang())
        print("Jenis Makanan       :", self.jenis_makanan)
        print("Jam Diberi Makan    :", self.jam_makan)

        print("Kondisi Hewan       :", self.perawatan.get_kondisi())
        print("Jam Cek Kesehatan   :", self.perawatan.get_jam_pemeriksaan())