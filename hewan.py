from abc import ABC, abstractmethod

# ABSTRACT CLASS HEWAN
# Pilar OOP:
# 1. Abstraction
# 2. Encapsulation

class Hewan(ABC):

    def __init__(self, nama, jenis, jenis_kelamin, umur):

        # Encapsulation (atribut private)
        self.__nama = nama
        self.__jenis = jenis
        self.__jenis_kelamin = jenis_kelamin
        self.__umur = umur

    # GETTER
    def get_nama(self):
        return self.__nama

    def get_jenis(self):
        return self.__jenis

    def get_jenis_kelamin(self):
        return self.__jenis_kelamin

    def get_umur(self):
        return self.__umur

    # SETTER
    def set_nama(self, nama):
        self.__nama = nama

    def set_jenis(self, jenis):
        self.__jenis = jenis

    def set_jenis_kelamin(self, jenis_kelamin):
        self.__jenis_kelamin = jenis_kelamin

    def set_umur(self, umur):
        self.__umur = umur

    # ABSTRACT METHOD
    @abstractmethod
    def tampilkan_info(self):
        pass