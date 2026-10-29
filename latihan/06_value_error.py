teks = input("Masukkan nilai angka: ").strip()

try:
    nilai = float(teks)
    print(f"Nilai yang dimasukkan: {nilai:g}")

except ValueError:
    print(
        "Input tidak valid. "
        "Masukkan angka, misalnya 85 atau 72.5."
    )
