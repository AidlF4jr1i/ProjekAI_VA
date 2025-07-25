#Syntax error
"""

Syntax error adalah error yang terjadi karena kesalahan kita
dalam menulis program seperti kekurangan tanda ':' ketika membuat fungsi,
dan lain-lain
"""

# huruf = ['a','b','c','d']
#
# for x in huruf #--> penyebab Syntax error, kelupaan ':'
#     print(huruf)


#Logical Error
"""
error yang disebabkan oleh kesalah logic saat kita membuat sebuah persamaan
atau baris kode program, ini tidak akan menimbulkan tanda ketika kita menulis programnya,
namun ketika kode dijalankan maka baru akan terlihat kesalahannya
"""

# bagi = 10
# pembagi = 0
#
# print(bagi/pembagi) # error ZeroDivisionError: division by zero

#membuat program agar tidak berhenti ketika ada error menggunakan try except

# try:
#     bagi = 10
#     pembagi = 0
#
#     print(bagi / pembagi)
#
# except:
#     print(f"Oops, terjadi error {ZeroDivisionError} nih ")
#
# print("ikuti perintah ini.")

#Best practice!!!

#1.
# try:
#     bagi = 10
#     pembagi = 0
#
#     print(bagi / pembagi)
#
# except Exception as e:
#     print(f"Oops, terjadi error nih ", e.__class__)
#
# print("ikuti perintah ini.")


#2.
#
# try:
#     bagi = 10
#     pembagi = '0'
#
#     print(bagi / pembagi)
#
# except ZeroDivisionError:
#     print(f"Oops, terjadi error ZeroDivisionError nih ")
# except ValueError:
#     print(f"Oops, terjadi error ValueError nih ")
# except Exception as e:
#     print('error tak dikenal',e.__class__ )
#
# print("ikuti perintah ini.")


#minigame tebak angka
class ValueTooLargeError(Exception):
    pass

class ValueTooSmallError(Exception):
    pass

number = 15

while True:
    try:
        i_num = int(input("masukkan angka: "))

        if i_num > number:
            raise ValueTooLargeError
        elif i_num < number:
            raise ValueTooSmallError
        break


    except ValueTooLargeError:
        print("Angka terlalu besar!")
        print()
    except ValueTooSmallError:
        print("angka terlalu kecil!")
        print()

print("selamat tebakan anda benar!!")
