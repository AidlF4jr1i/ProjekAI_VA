# Fungsi non Parameter

def halo_dunia():
    var = "halo dunia, halo semuaaa"
    print(var)

halo_dunia()

# def nama_kamu(nama, asal):
#     var = f"Halo perkenalkan saya {nama}. asal saya dari {asal} selamat datang di Function!"
#     print(var)
#
# nama_kamu("Aidil","Palembang")

def selamat_datang(*daftar_nama):
    var= "halo "
    for name in daftar_nama:
        var += name + ', '

    var += "Welcome!!"
    print(var)

selamat_datang("Aidil","Fahri","Lukman","Sahrul")


#Docstring

def nama_kamu(nama, asal):
    """
    ini Fungsi untuk memanggil nama!
    """
    var = f"Halo perkenalkan saya {nama}. asal saya dari {asal} selamat datang di Function!"
    print(var)

nama_kamu("Aidil","Palembang")
# print(nama_kamu.__doc__) #--> cara melihat docstring

# Scope dan Return

a=1
b=3
x=100

def operasi(a,b,c):
    op1 = a+b
    op2 = op1 / c

    print(f"Nilai a={a} didalam fungsi")
    print(f"Nilai b={b} didalam fungsi")
    print(f"Nilai x={x} diluar fungsi")
    return op2
hasil = operasi(10,20,3)
print(hasil)

print(f"Nilai a={a} diluar fungsi")
print(f"Nilai b={b} diluar fungsi")
print(f"Nilai x={x} diluar fungsi")