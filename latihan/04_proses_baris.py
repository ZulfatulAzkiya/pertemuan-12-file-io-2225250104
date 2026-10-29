with open("data/nilai.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()

        if not baris:
            continue

        bagian = baris.split(",")

        if len(bagian) != 2:
            print(f"Format salah: {baris}")
            continue

        nama, teks_nilai = bagian

        try:
            nilai = float(teks_nilai)

        except ValueError:
            print(f"Nilai tidak valid untuk {nama}: {teks_nilai}")
            continue

        print(f"{nama}: {nilai:g}")
