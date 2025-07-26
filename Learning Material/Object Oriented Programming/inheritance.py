# Copyright © 2022 Indonesia AI. All Rights Reserved.
# contact@aiforindonesia.org

# ------------------------------
# INHERITANCE
# ------------------------------

# Parent class
class Animal:
    def __init__(self):
        self.tipe = "Mamalia"
        self.kecepatan = "Lambat"

    def grow(self):
        print("Mamalia ini bertumbuh...")


# Child class
class Cat(Animal):

    def __init__(self, nama, tipe):
        super().__init__()

        self.nama = nama
        self.tipe = tipe

    def run(self):
        print(f"Kucing {self.tipe} ini berlari...")


kinako = Cat(nama="Kinako", tipe="Anggora")
minto = Cat(nama="Minto", tipe="Persia")

print(kinako.kecepatan)
print(kinako.tipe)

print(minto.kecepatan)
print(minto.tipe)

kinako.run()
minto.run()

kinako.grow()
minto.grow()

print(kinako.tipe)