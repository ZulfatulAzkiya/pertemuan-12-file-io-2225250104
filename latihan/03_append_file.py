catatan = input("Catatan baru: ").strip()

with open("data/catatan.txt", "a", encoding="utf-8") as file:
    file.write(catatan + "\n")

print("Catatan ditambahkan.")
