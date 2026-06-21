# CLASS PERAWATAN
# Untuk menyimpan kondisi kesehatan hewan

class Perawatan:

    def __init__(self):

        self.__kondisi = "Sehat"
        self.__jam_pemeriksaan = "-"

    # GETTER
    def get_kondisi(self):
        return self.__kondisi

    def get_jam_pemeriksaan(self):
        return self.__jam_pemeriksaan

    # SETTER
    def set_kondisi(self, kondisi):
        self.__kondisi = kondisi

    def set_jam_pemeriksaan(self, jam):
        self.__jam_pemeriksaan = jam

    # UPDATE DATA KESEHATAN
    def catat_kondisi(self, kondisi, jam):
        self.__kondisi = kondisi
        self.__jam_pemeriksaan = jam