class Cat:
    """
    ini adalah Class untuk membuat sebuah Objek bernama Kucing

    """
    spesies = "Kucing"

    def __init__(self,nama,tipe):
        self.nama = nama
        self.tipe = tipe

    def run(self, speed):
        print(f"kucing {self.nama} sedang berlari dengan {speed} ")

    def play(self):
        print(f"kucing {self.nama} sedang bermain dengan kucing lain")

    def eat(self):
        print(f"kucing {self.nama} sedang Makan")

kopi = Cat(nama="Kopi", tipe="Persia")

manis = Cat(nama="Manis", tipe="Kampung")

print(kopi.nama)
print(manis.tipe)

print(f"Kopi adalah sejenis {kopi.__class__.spesies}")
print(f"{kopi.nama} sedang bermain dengan {manis.nama}, mereka berdua memiliki jenis yang berbeda, kalo kopi jenisnya {kopi.tipe}, sementara manis adalah jenis kucing {manis.tipe}")


kopi.run("cepat")
manis.play()

print(kopi.__doc__)


class Employee():
    '''
    Ini adalah Class untuk memanipulasi data employee
    Melalui kelas ini kita bisa memanipulasi data yang ada seperti baca, hapus dan tambah
    '''

    def __init__(self, lokasi_file):

        self.data_employee = open(f'{lokasi_file}', mode='r', encoding='utf-8')
        self.data_per_sesi = 10

    def baca_data(self):

        self.data_employee = self.data_employee[:self.data_per_sesi]
        return self.data_employee

    def hapus_data(self, baris, kolom):

        del self.data_employee[baris][kolom]

    def tambah_data(self, data_baru):

        nama, gaji, posisi, jabatan, domisili = data_baru
        self.data_employee.append([nama, gaji, posisi, jabatan, domisili])

# Membuat objek
it = Employee(lokasi_file='./karyawan_IT.xls')
marketing = Employee(lokasi_file='./karyawan_marketing.xls')
product = Employee(lokasi_file='./karyawan_product.xls')

# Abstract Object
class RandomForest():
    pass