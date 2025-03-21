# Data Gaji Status dan Bonus Golongan dalam bentuk list
data_gaji_status = [
    {"status": "Pegawai Tetap", "gaji": 1000000},
    {"status": "Pegawai Honor", "gaji": 750000}
]

data_bonus_golongan = [
    {"status": "Pegawai Tetap", "golongan": "A", "bonus": 200000},
    {"status": "Pegawai Tetap", "golongan": "B", "bonus": 400000},
    {"status": "Pegawai Tetap", "golongan": "C", "bonus": 550000},
    {"status": "Pegawai Honor", "golongan": "A", "bonus": 150000},
    {"status": "Pegawai Honor", "golongan": "B", "bonus": 275000},
    {"status": "Pegawai Honor", "golongan": "C", "bonus": 480000}
]

# Inputan
NIK = input("Masukan NIK: ")
Nama = input("Masukan Nama: ")
Status = input("Masukan Status (Pegawai Tetap/Honor): ").strip().title()
Golongan = input("Masukan Golongan (A/B/C): ").strip().upper()

# Inisialisasi nilai default
Gaji = 0
Bonus = 0

# Cek Status menggunakan for loop dan if-else
for item in data_gaji_status:
    if item["status"] == Status:
        Gaji = item["gaji"]
        break
else:
    print("Status tidak ada")
    Gaji = 0

# Cek Golongan menggunakan for loop dan if-else
if Gaji != 0:  # Hanya cek golongan jika status valid
    for item in data_bonus_golongan:
        if item["status"] == Status and item["golongan"] == Golongan:
            Bonus = item["bonus"]
            break
    else:
        print("Golongan tidak ada")
        Bonus = 0

# Menghitung Total Gaji
Gaji_Total = Gaji + Bonus

# Menampilkan Data
print("\n=== Detail Gaji ===")
print(f"Nama: {Nama}")
print(f"NIK: {NIK}")
print(f"Status: {Status}")
print(f"Golongan: {Golongan}")
print(f"Gaji: Rp {Gaji:,}")
print(f"Bonus: Rp {Bonus:,}")
print(f"Gaji Total: Rp {Gaji_Total:,}")