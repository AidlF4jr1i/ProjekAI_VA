#Encapsulation(pembatasan modifikasi pada Class)

class Mobil:
    def __init__(self,plat):
        self.__plat = plat
        self.__tipe = "Avanza"
        self.__bensin = 40 #dalam liter

    #fungsi Getter
    def lihatMaximumbensin(self):
        print(f"Maksimum bensin adalah {self.__bensin} liter")
    #Fungsi Setter
    def aturMaximumbensin(self,bensin):
        self.__bensin = bensin

avanza = Mobil(plat="BG 1230 NW")

# print(avanza.tipe)
# print(avanza.bensin)
# print(avanza.plat)

avanza.__bensin = 30
print(avanza.__bensin)

avanza.lihatMaximumbensin()
avanza.aturMaximumbensin(50)
avanza.lihatMaximumbensin()