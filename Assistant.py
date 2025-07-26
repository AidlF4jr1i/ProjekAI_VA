# Copyright © 2022 Indonesia AI. All Rights Reserved.
# contact@aiforindonesia.org
# --- Diperbarui oleh Gemini dengan penyimpanan jadwal .txt ---

# Mengimpor library yang diperlukan
import smtplib
import random
import getpass
from email.message import EmailMessage


class Assistant():
    """
    Kelas ini mendefinisikan fungsionalitas dari asisten virtual,
    menggunakan file .txt untuk manajemen jadwal.
    """

    def __init__(self, name):
        """
        Konstruktor untuk menginisialisasi nama asisten.
        """
        self.name = name
        self.file_jadwal = "schedule.txt"
        self.file_penerima = "receiver_list.txt"
        self.initialize()

    def initialize(self):
        """
        Pesan selamat datang saat asisten dibuat.
        """
        print(f"Asisten virtual '{self.name}' berhasil dibuat.")
        input("- Tekan ENTER untuk melanjutkan -")

    def run(self):
        """
        Fungsi utama untuk menjalankan loop interaksi dengan pengguna.
        """
        while True:
            print(f"\n--- Menu {self.name} ---")
            print("1. Ubah Nama")
            print("2. Buat Jadwal")
            print("3. Lihat Jadwal")
            print("4. Lempar Jokes")
            print("5. Kirim Email ke Daftar Penerima")
            print("0. Keluar")

            pilihan = input("Pilih menu (0-5): ")

            if pilihan == '1':
                nama_baru = input("Masukkan nama baru untuk asisten: ")
                self.ubah_nama(nama_baru)
            elif pilihan == '2':
                self.buat_jadwal()
            elif pilihan == '3':
                self.lihat_jadwal()
            elif pilihan == '4':
                self.lempar_jokes()
            elif pilihan == '5':
                self.kirim_email()
            elif pilihan == '0':
                print(f"Terima kasih telah menggunakan {self.name}. Sampai jumpa!")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

    def ubah_nama(self, name):
        """
        Mengubah nama panggilan asisten virtual.
        """
        self.name = name
        print(f"Nama berhasil diubah menjadi {self.name}")
        input("- Tekan ENTER untuk melanjutkan -")

    def buat_jadwal(self):
        """
        Membuat jadwal baru dan menyimpannya ke schedule.txt.
        """
        try:
            with open(self.file_jadwal, "a") as file:
                jadwal_baru = input("\nMasukkan agenda Anda (format: dd/mm/yyyy - nama_agenda):\n")
                file.write(jadwal_baru + "\n")
            print("Jadwal baru berhasil dibuat.")
        except Exception as e:
            print(f"Terjadi kesalahan saat menyimpan jadwal: {e}")
        input("- Tekan ENTER untuk melanjutkan -")

    def lihat_jadwal(self):
        """
        Membaca dan menampilkan semua jadwal dari schedule.txt.
        """
        print("\n--- JADWAL ANDA ---")
        try:
            with open(self.file_jadwal, "r") as file:
                jadwal = file.read()
                if not jadwal:
                    print("Belum ada jadwal yang tersimpan.")
                else:
                    print(jadwal)
        except FileNotFoundError:
            print(f"File jadwal '{self.file_jadwal}' tidak ditemukan. Silakan buat jadwal terlebih dahulu.")
        except Exception as e:
            print(f"Terjadi kesalahan saat membaca jadwal: {e}")
        print("-------------------\n")
        input("- Tekan ENTER untuk melanjutkan -")

    def lempar_jokes(self):
        """
        Menampilkan lelucon acak dan bertanya apakah pengguna ingin lagi.
        """
        jokes = [
            "Debugging is like being the detective in a crime movie where you're also the murderer at the same time.",
            "Algorithm: A word used by programmers when they don't want to explain how their code works.",
            "Kenapa air laut asin? Karena ikannya pada keringetan.",
            "Pintu apa yang didorong sepuluh orang nggak bakal kebuka? Pintu yang ada tulisan 'TARIK'."
        ]

        while True:
            print("\n" + random.choice(jokes))
            lagi = input("Lagi [Yes/No]? ")
            if lagi.lower() in ["no", "n", "tidak", "0"]:
                break

    def kirim_email(self):
        """
        Mengirim email ke semua alamat di receiver_list.txt.
        """
        try:
            with open(self.file_penerima, 'r') as f:
                penerima = [line.strip() for line in f if line.strip()]

            if not penerima:
                print(f"File '{self.file_penerima}' kosong atau tidak ditemukan. Mohon isi terlebih dahulu.")
                input("- Tekan ENTER untuk melanjutkan -")
                return

            print(f"Email akan dikirim ke: {', '.join(penerima)}")
            email_pengirim = input("Masukkan email Anda (contoh: email@gmail.com): ")
            password = getpass.getpass("Masukkan password email Anda: ")

            subjek = input("Masukkan subjek email: ")
            isi_pesan = input("Masukkan isi pesan: ")

            msg = EmailMessage()
            msg['Subject'] = subjek
            msg['From'] = email_pengirim
            msg['To'] = ", ".join(penerima)
            msg.set_content(f"{isi_pesan}\n\n- Dikirim dari {self.name} -")

            print("Menghubungkan ke server SMTP...")
            smtp = smtplib.SMTP('smtp.gmail.com', 587)
            smtp.starttls()

            print("Melakukan login...")
            smtp.login(email_pengirim, password)

            print("Mengirim email...")
            smtp.send_message(msg)

            smtp.quit()
            print("Email berhasil dikirim!")

        except FileNotFoundError:
            print(f"\n[GAGAL] File '{self.file_penerima}' tidak ditemukan.")
        except smtplib.SMTPAuthenticationError:
            print("\n[GAGAL] Autentikasi gagal. Periksa email/password dan pengaturan akun Anda.")
        except Exception as e:
            print(f"\nTerjadi kesalahan tak terduga: {e}")

        input("- Tekan ENTER untuk melanjutkan -")
