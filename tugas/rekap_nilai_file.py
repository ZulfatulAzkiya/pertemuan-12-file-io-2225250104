from pathlib import Path

INPUT_FILE = Path("data/nilai.txt")
OUTPUT_FILE = Path("data/hasil_rekap.txt")
BATAS_LULUS = 60


def baca_nilai(path):
    data = []

    with path.open("r", encoding="utf-8") as file:
        for nomor, baris in enumerate(file, start=1):
            baris = baris.strip()

            if not baris:
                continue

            bagian = baris.split(",")

            if len(bagian) != 2:
                print(
                    f"Baris {nomor} dilewati: "
                    "format harus nama,nilai."
                )
                continue

            nama = bagian[0].strip()
            teks_nilai = bagian[1].strip()

            try:
                nilai = float(teks_nilai)

            except ValueError:
                print(
                    f"Baris {nomor} dilewati: "
                    "nilai bukan angka."
                )
                continue

            if not 0 <= nilai <= 100:
                print(
                    f"Baris {nomor} dilewati: "
                    "nilai harus 0-100."
                )
                continue

            data.append({
                "nama": nama,
                "nilai": nilai
            })

    return data


def buat_laporan(data):
    if not data:
        return "Tidak ada data nilai valid.\n"

    nilai = [item["nilai"] for item in data]
    tuntas = sum(x >= BATAS_LULUS for x in nilai)

    baris = [
        "REKAP NILAI MAHASISWA",
        f"Jumlah data valid: {len(nilai)}",
        f"Rata-rata: {sum(nilai) / len(nilai):.2f}",
        f"Nilai minimum: {min(nilai):g}",
        f"Nilai maksimum: {max(nilai):g}",
        f"Tuntas (nilai >= {BATAS_LULUS}): {tuntas}",
        "",
        "Detail:"
    ]

    for item in data:
        status = (
            "Tuntas"
            if item["nilai"] >= BATAS_LULUS
            else "Belum tuntas"
        )

        baris.append(
            f"- {item['nama']}: {item['nilai']:g} ({status})"
        )

    return "\n".join(baris) + "\n"


def main():
    try:
        data = baca_nilai(INPUT_FILE)

    except FileNotFoundError:
        print(f"File input tidak ditemukan: {INPUT_FILE}")
        return

    laporan = buat_laporan(data)

    OUTPUT_FILE.write_text(laporan, encoding="utf-8")

    print(laporan)
    print(f"Laporan disimpan di {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
