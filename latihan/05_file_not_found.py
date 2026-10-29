nama_file = input("Nama file yang ingin dibaca: ").strip()

try:
    with open(nama_file, "r", encoding="utf-8") as file:
        print(file.read())

except FileNotFoundError:
    print(f"File '{nama_file}' tidak ditemukan.")
