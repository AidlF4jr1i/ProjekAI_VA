"""
Berdasarkan video yang Anda berikan,
Regex atau Regular Expression adalah sebuah modul dalam Python yang,
digunakan untuk memanipulasi teks dengan cara mendefinisikan pola karakter
beberapa contoh fungsi dalam regex yang sering digunakan yakni:

1. match() --> untuk mengembalikan status kecocokkan antar teks

2. findall() --> untuk mengembalikan 'list' yang memuat semua string yang cocok

3. search() --> untuk mengembalikan status kecocokan dimanapun yang ada pada string

4. split() --> untuk mengembalikan list dari string yang telah di split berdasarkan kecocokan

5. sub() --> mengubah bagian dari string berdasarkan kecocokan
"""


import re

teks = "regex"
x = re.match("r...x$", teks)
# x = re.match("r..x$", teks) --> artinya kita akan mencocokkan string yang ada pada variable teks apakah sesuai dengan kondisi yang diminta yakni dimulai dari 'r' lalu 3 karakter bebas dan diakhiri dengan 'x'
print(x)


teks = "saya senang belajar regex"
y = re.split('\s',teks) #--> '\s' disini berfungsi untuk mengubah semua kalimat string yang memiliki spasi setelahnya untuk dijadikan value dalam satu list
print(y)


teks = """Ada 3 tipe loop atau perulangan di bahasa pemrograman Python yaitu while loop,
for loop dan nested loop 2022"""
q = re.sub("\d", "", teks) #--> artinya kita mencari semua 'digit'(maksudnya angka) yang ada di dalam string dan menggantinya dengan atau tanpa nilai
print(q)


teks = "Hujan deras di kawasan depok"
z = re.search("^Hujan.*depok$",teks) #--> artinya kita mencari susunan kalimat yang cocok(entah apapun kalimat itu ) selagi  dimulai dari kata "Hujan", dan diakhiri dengan kata "depok"

if z:
    print("Yes, we have a Match")
else:
    print("no Match")


teks = "23 oct 2021 23 oct,2019 23 october,2018 oct 26,2020"

c = re.findall("\d{2} [a-z]{3} \d{4}", teks) #--> mencari teks dengan diawali 2 digit angka, lalu kumpulan huruf dari a-z berjumlah 3 dan diakhiri dengan 4 digit angka,
print(c)

teks = "Harga 1 mobil antik tersebut yaitu $1000"
a = re.sub("\$\d+", "_",teks) #--> karakter '\$' disini mengartikan nilai suatu teks dalam mata uang dollar lalu 'd+' mengartikan untuk mengambil semua angka setelah simbol dolar tersebut untuk diganti dengan tanda  "_"
print(a)


teks = "Akan dialihkan ke http://medium.com"

b = re.sub("http[s]?\://\S+", "_", teks) #--> mencari teks yang merupakan URL (diawali http atau https) lalu menggantinya dengan karakter "_". '[s]?' membuat 's' opsional, dan '\S+' mencocokkan semua karakter non-spasi setelah '://'.
print(b)
teks = "Luar biasa! Banyak anak-anak muda traveling tahun ini, begini tanggapan lesti #travel #_lesti #viral #gadget"

w = re.findall("#[_]*[a-z]+", teks) #--> mencari semua hashtag yang diawali '#' lalu bisa diikuti underscore '[_]*' dan wajib diikuti satu atau lebih huruf '[a-z]+'. Hasilnya dikembalikan dalam bentuk list.
print(w)