# ==================================================
# CLASS PERAWATAN
# Menyimpan data kesehatan hewan
# ==================================================
class Perawatan:

    def __init__(self):

        # Kondisi awal hewan
        self.__kondisi = "Sehat"

        # Jadwal pemeriksaan default
        self.__jam_pemeriksaan = "1 Bulan Sekali"

    # Getter
    def get_kondisi(self):
        return self.__kondisi

    def get_jam_pemeriksaan(self):
        return self.__jam_pemeriksaan

    # Setter
    def set_kondisi(self, kondisi):
        self.__kondisi = kondisi

    def set_jam_pemeriksaan(self, jam):
        self.__jam_pemeriksaan = jam

    # Menyimpan hasil pemeriksaan kesehatan
    def catat_kondisi(self, kondisi, jam):

        self.__kondisi = kondisi
        self.__jam_pemeriksaan = jam