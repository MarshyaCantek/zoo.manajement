from abc import ABC, abstractmethod

class Hewan(ABC):

    def __init__(self, nama, jenis, kelamin, umur):

        self.__nama = nama
        self.__jenis = jenis
        self.__kelamin = kelamin
        self.__umur = umur

    # Getter
    def get_nama(self):
        return self.__nama

    def get_jenis(self):
        return self.__jenis

    def get_kelamin(self):
        return self.__kelamin

    def get_umur(self):
        return self.__umur

    # Setter
    def set_nama(self, nama):
        self.__nama = nama

    def set_jenis(self, jenis):
        self.__jenis = jenis

    def set_kelamin(self, kelamin):
        self.__kelamin = kelamin

    def set_umur(self, umur):
        self.__umur = umur

    @abstractmethod
    def tampilkan_info(self):
        pass