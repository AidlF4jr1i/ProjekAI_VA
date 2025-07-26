# Kembangkanlah class Mobil yang sudah dibuat sebelumnya agar memiliki parent class bernama Kendaraan
# Pastikan parent class tersebut memiliki setidaknya 2 attributes dan 2 methods yang akan diturunkan ke child class
# Jangan lupa menggunakan super() pada child class

# Parent class
class Kendaraan:

    def __init__(self):
        self.manual = "Kopling"
        self.otomatis= "Matic"

    def plat(self, plat):
        print(f"mobil ini memiliki plat {plat}")

    def cek_transmisi(self, jenis):
        if jenis.lower() == 'manual':
            print(f"Transmisi: {self.manual}")
        elif jenis.lower() == 'otomatis':
            print(f"Transmisi: {self.otomatis}")
        else:
            print("Jenis transmisi tidak dikenali.")

# Child class
class Mobil(Kendaraan):
    def __init__(self, color, cc):
        super().__init__()
        self.color = color
        self.bensin = 40
        self.cc = cc

    def bergerak(self,kecepatan):
        print(f"Mobil ini bergerak dengan kecepatan {kecepatan} km/jam")


kijang = Mobil(color="Merah", cc=1000)

print(kijang.cc)
print(kijang.color)
kijang.cek_transmisi("manual")
kijang.bergerak(kecepatan=300)
kijang.plat("BG 1230 NW")
