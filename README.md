# Sistem Manajemen Hewan Kebun Binatang

## Deskripsi Program

Program ini merupakan aplikasi berbasis Python yang digunakan untuk membantu pengelolaan data hewan pada kebun binatang. Sistem ini dibuat menggunakan konsep Object Oriented Programming (OOP) dan mengimplementasikan empat pilar utama OOP yaitu Encapsulation, Abstraction, Inheritance, dan Polymorphism.

Program memungkinkan pengguna untuk menambahkan data hewan, memindahkan kandang, mencatat jadwal pemberian makan, mencatat kondisi kesehatan, melihat informasi hewan, serta menghapus data hewan.

---

## Studi Kasus

Kebun binatang membutuhkan sistem yang dapat membantu petugas dalam mengelola informasi hewan secara terstruktur, mulai dari identitas hewan, lokasi kandang, jadwal makan, hingga kondisi kesehatan hewan.

Untuk menyelesaikan permasalahan tersebut dibuatlah Sistem Manajemen Hewan Kebun Binatang berbasis Object Oriented Programming.

---

## Fitur Program

### Create (Tambah Data)

* Menambahkan hewan baru.
* Input nama hewan.
* Input jenis hewan.
* Input jenis kelamin.
* Input umur hewan.

### Read (Lihat Data)

* Menampilkan informasi satu hewan berdasarkan nama.
* Menampilkan seluruh data hewan dalam bentuk tabel.

### Update (Perbarui Data)

* Memindahkan kandang hewan.
* Mencatat jadwal pemberian makan.
* Mencatat kondisi kesehatan dan jadwal pemeriksaan.

### Delete (Hapus Data)

* Menghapus data hewan berdasarkan nama.

---

## Struktur Folder

```text
zoo_management/
│
├── main.py
├── hewan.py
├── hewan_kebun_binatang.py
├── kandang.py
└── perawatan.py
```

---

## Penjelasan File

### 1. hewan.py

Berisi class abstrak Hewan yang menjadi parent class.

Fungsi:

* Menyimpan data dasar hewan.
* Mengimplementasikan Encapsulation.
* Mengimplementasikan Abstraction.

Atribut:

* nama
* jenis
* kelamin
* umur

Method:

* Getter
* Setter
* tampilkan_info() sebagai abstract method

---

### 2. kandang.py

Berisi class Kandang.

Fungsi:

* Menyimpan informasi kandang hewan.
* Memiliki getter dan setter untuk nama kandang.

---

### 3. perawatan.py

Berisi class Perawatan.

Fungsi:

* Menyimpan kondisi kesehatan hewan.
* Menyimpan jadwal pemeriksaan kesehatan.

---

### 4. hewan_kebun_binatang.py

Berisi class HewanKebunBinatang yang mewarisi class Hewan.

Fungsi:

* Mengimplementasikan Inheritance.
* Mengimplementasikan Polymorphism.
* Menambahkan fitur kandang, pemberian makan, dan kesehatan.

---

### 5. main.py

Berisi program utama.

Fungsi:

* Menampilkan menu.
* Mengelola seluruh proses CRUD.
* Membuat objek hewan.
* Menjalankan sistem.

---

# Implementasi 4 Pilar OOP

## 1. Encapsulation

Encapsulation diterapkan dengan menggunakan atribut private.

Contoh:

```python
self.__nama
self.__jenis
self.__kelamin
self.__umur
```

Atribut tersebut hanya dapat diakses melalui getter dan setter.

Getter:

```python
get_nama()
get_jenis()
get_kelamin()
get_umur()
```

Setter:

```python
set_nama()
set_jenis()
set_kelamin()
set_umur()
```

File:

* hewan.py
* kandang.py
* perawatan.py

---

## 2. Abstraction

Abstraction diterapkan menggunakan Abstract Class dan Abstract Method.

Contoh:

```python
from abc import ABC, abstractmethod

class Hewan(ABC):

    @abstractmethod
    def tampilkan_info(self):
        pass
```

Class Hewan tidak dapat dibuat objek secara langsung dan harus diturunkan ke class lain.

File:

* hewan.py

---

## 3. Inheritance

Inheritance diterapkan dengan pewarisan class.

Contoh:

```python
class HewanKebunBinatang(Hewan):
```

Class HewanKebunBinatang mewarisi seluruh atribut dan method dari class Hewan.

File:

* hewan_kebun_binatang.py

---

## 4. Polymorphism

Polymorphism diterapkan dengan melakukan override terhadap method abstrak tampilkan_info().

Contoh:

```python
def tampilkan_info(self):
    print("Informasi Hewan")
```

Method ini merupakan implementasi ulang dari method abstrak pada class Hewan.

File:

* hewan_kebun_binatang.py

---

# Implementasi CRUD

## Create

Menambahkan data hewan baru.

Menu:

```text
1. Tambah Hewan
```

---

## Read

Menampilkan informasi hewan.

Menu:

```text
5. Cek Info Hewan
```

Submenu:

```text
1. Cek Info Hewan Satuan
2. Cek Info Seluruh Hewan
```

---

## Update

Memperbarui data hewan.

Menu:

```text
2. Pindah Kandang
3. Beri Makan
4. Catat Kesehatan
```

---

## Delete

Menghapus data hewan.

Menu:

```text
6. Hapus Hewan
```

---

# Alur Program

1. Pengguna menjalankan program.
2. Sistem menampilkan menu utama.
3. Pengguna memilih menu yang diinginkan.
4. Sistem memproses data sesuai pilihan.
5. Data disimpan ke dalam objek hewan.
6. Informasi dapat ditampilkan kembali melalui menu cek data.
7. Program berakhir saat pengguna memilih menu keluar.

---

# Kesimpulan

Program Sistem Manajemen Hewan Kebun Binatang berhasil dibuat dengan menerapkan konsep Object Oriented Programming (OOP) yang terdiri dari Encapsulation, Abstraction, Inheritance, dan Polymorphism. Program juga telah mengimplementasikan operasi CRUD (Create, Read, Update, Delete) sehingga mampu mengelola data hewan secara efektif dan terstruktur. Dengan pemisahan modul ke beberapa file, program menjadi lebih rapi, mudah dikembangkan, dan sesuai dengan prinsip pemrograman berorientasi objek.
