class Kandang:

    def __init__(self, nama_kandang):
        self.__nama_kandang = nama_kandang

    # Getter
    def get_nama_kandang(self):
        return self.__nama_kandang

    # Setter
    def set_nama_kandang(self, nama_kandang):
        self.__nama_kandang = nama_kandang

    def __str__(self):
        return self.__nama_kandang