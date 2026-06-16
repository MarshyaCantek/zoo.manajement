class Perawatan:

    def __init__(self):

        self.__kondisi = "Sehat"
        self.__jam_pemeriksaan = "-"

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

    def catat_kondisi(self, kondisi, jam):

        self.__kondisi = kondisi
        self.__jam_pemeriksaan = jam