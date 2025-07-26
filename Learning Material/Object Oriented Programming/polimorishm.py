def melaju(objek):
    objek.forward()


class Cat:
    def __init__(self):
        self.nama = "Kopi"
        self.tipe = "Persia"
    def forward(self):
        print("kucing ini berlari.....")


class Bird:
    def __init__(self):
        self.nama = "utut"
        self.tipe = "Perkutut"
    def forward(self):
        print("Burung ini Terbang.....")

kopi = Cat(); utut = Bird()

melaju(kopi)
melaju(utut)
