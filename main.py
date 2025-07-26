# Copyright © 2022 Indonesia AI. All Rights Reserved.
# contact@aiforindonesia.org
# --- Diperbarui oleh Gemini ---

from Assistant import Assistant


def main():
    """
    Fungsi utama untuk menginisialisasi dan menjalankan asisten virtual.
    """
    # Membuat objek dari kelas Assistant dengan nama awal 'Jarvis'
    # Anda bisa mengganti 'Jarvis' dengan nama lain yang Anda suka.
    my_assistant = Assistant(name='Jarvis')

    # Menjalankan asisten
    my_assistant.run()


if __name__ == "__main__":
    main()


