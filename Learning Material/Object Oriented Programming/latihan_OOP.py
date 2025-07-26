class Mobil:
    """
    ini merupakan class yang berisi blueprint dari objek bernama mobil!
    """
    jenis_kendaraan = "Roda Empat"

    # 'warna' ditambahkan sebagai attribute saat objek dibuat
    def __init__(self, tipe, pabrik, jenis, warna):
        self.tipe = tipe
        self.pabrik = pabrik
        self.jenis = jenis
        self.warna = warna  # Warna kini menjadi attribute

    def tampilkan_info(self):
        # Menggabungkan beberapa info dalam satu method
        print(f"Mobil {self.pabrik} tipe {self.tipe}")
        print(f"Warnanya {self.warna} dan menggunakan jenis bahan bakar {self.jenis}.")

    def ganti_warna(self, warna_baru):
        print(f"Warna mobil diganti dari {self.warna} menjadi {warna_baru}")
        self.warna = warna_baru # Mengubah attribute warna

    def uji_medan(self, medan):
        print(f"Mobil ini sedang diuji di medan {medan}.")


# Membuat objek dengan menyertakan warna
Kijang = Mobil(tipe="LGX", pabrik="Toyota", jenis="Bensin", warna="Abu-Abu")

# Memanggil method
Kijang.tampilkan_info()
Kijang.uji_medan("Jalanan Umum")
Kijang.ganti_warna("Biru Metalik")
Kijang.tampilkan_info()