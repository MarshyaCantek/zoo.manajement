# Import library untuk membuat Abstract Class
from abc import ABC, abstractmethod


# ==================================================
# ABSTRACT CLASS (Pilar OOP: Abstraction)
# Class Hewan menjadi parent class dan tidak bisa
# dibuat objek secara langsung
# ==================================================
class Hewan(ABC):

    # Constructor untuk menyimpan data dasar hewan
    def __init__(self, nama, jenis, kelamin, umur):

        # ENCAPSULATION
        # Data dibuat private menggunakan "__"
        self.__nama = nama
        self.__jenis = jenis
        self.__kelamin = kelamin
        self.__umur = umur

    # ==================================================
    # GETTER
    # Digunakan untuk mengambil data private
    # ==================================================
    def get_nama(self):
        return self.__nama

    def get_jenis(self):
        return self.__jenis

    def get_kelamin(self):
        return self.__kelamin

    def get_umur(self):
        return self.__umur

    # ==================================================
    # SETTER
    # Digunakan untuk mengubah data private
    # ==================================================
    def set_nama(self, nama):
        self.__nama = nama

    def set_jenis(self, jenis):
        self.__jenis = jenis

    def set_kelamin(self, kelamin):
        self.__kelamin = kelamin

    def set_umur(self, umur):
        self.__umur = umur

    # ==================================================
    # ABSTRACT METHOD
    # Wajib dioverride oleh class turunan
    # ==================================================
    @abstractmethod
    def tampilkan_info(self):
        pass