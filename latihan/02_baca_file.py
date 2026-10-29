try:
    with open("data/catatan.txt", "r", encoding="utf-8") as file:
        print(file.read())

except FileNotFoundError:
    print(
        "File catatan.txt belum tersedia. "
        "Jalankan 01_tulis_file.py terlebih dahulu."
    )
