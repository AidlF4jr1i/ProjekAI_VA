count = 0

while(count < 9):
    print(f"Nilai Count = {count}")
    count += 1


list_angka = [1,2,3,4,5,6,7,8,9]

for angka in list_angka:
    print(f"list ke-{angka}")

"""
Tips membuat List lebih efisien
"""

#tips 1
list_efisien = list(range(1,10))

print(list_efisien)

#tips 2
list_2 = list(range(1,19,2)) #--> (1=Start, 19=Stop, 2=lompatan/skip )
print(list_2)


"""
Nested Loop
"""

x=80

while(x < 90):
    j = 2
    print(x/j)
    print('Loop Satu')

    while(j <= x/j):
        print("loop ke-2")
        x +=1
        j +=1
print("Selesai Loop")

#break and continue


for y in "String":

    if y == 'i' :
        break
    print(y)

for a in "JAB":

    if a == 'A' :
        continue
    print(a)


# Bonus "FOR ELSE"

nama_murid = ['angga','rudi','ambatron']
nama = 'rudi'
for c in nama_murid:
    if c == nama:
        print(f"nama nya termasuk dalam daftar, selamat datang {nama}")
        break
else:
    print("Nama murid tidak terdaftar")