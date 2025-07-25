#list


list_1 = [1,2,3,4,5]
list_2 = ['apel','pisang','duren']
list_3 = ['mangga','alpukat']

print(list_1 + list_2)

try:
    print(list_1 - list_2)

except Exception:
    print("tidak bisa melakukan penguragan pada operasi list")
    print(TypeError)

list_4 = list_3.copy()

print(list_4)

list_2.sort()
print(list_2)


#DIctionary

dict_1 = {"tempat_tinggal": "rumah",
          "tempat_makan": "Meja_makan",
          "tempat_Belajar": "Ruang_Belajar"
          }

print(dict_1["tempat_Belajar"])

for key in dict_1.keys():
    print(key, dict_1[key] )



#Set

"""
Biasanya digunakan untuk operasi Himpunan seperti Irisan, Gabungan, etc

"""
set1 = {1,2,3,4,5,6,7,7,9}
set2 = {1,3,5,7,9,11}
#Gabungan

print( set1 | set2)

#Irisan
print( set1 & set2)

#Selisih
print( set1 - set2)

#Symmetric Difference (nilai yang tidak memiliki pasangan yg sama di kedua sisi)
print(set1 ^ set2)