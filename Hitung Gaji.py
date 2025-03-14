# Soal :
# 1. Buat inputan, Nama, Nik, Status (Pegawai Tetap/Honor), Golongan (A/B/C)
# 2. Status Pegawai Tetap, Gaji 1.000.000, Bonus Golongan A, 200.000, B 400.000, C 550.000
# 3. Status Pegawai Honor, Gaji 750.000, Bonus Golongan A 150.000, B 275.000, C 480.000
# 4. Print Gaji, Bonus, dan Gaji Total
# 5. status dan golongan merupakan inputan String

# Inputan
NIK = int(input("Masukan NIK: "))
Nama = input("Masukan Nama: ")
Status = input("Masukan Status (Pegawai Tetap/Honor): ")
Golongan = input("Masukan Golongan (A/B/C): ")

# Menghitung Bonus berdasarkan Golongan
if Status == "Pegawai Tetap":
    Gaji = 1000000
    if Golongan == "A":
        Bonus = 200000
    elif Golongan == "B":
        Bonus = 400000
    elif Golongan == "C":
        Bonus = 550000
    else:
        print("Golongan tidak ada")
        Bonus = 0
elif Status == "Honor":
    Gaji = 750000
    if Golongan == "A":
        Bonus = 150000
    elif Golongan == "B":
        Bonus = 275000
    elif Golongan == "C":
        Bonus = 480000
    else:
        print("Golongan tidak ada")
        Bonus = 0
else:
    print("Status tidak ada")
    Gaji = 0
    Bonus = 0


# Menghitung Total Gaji
Gaji_Total = Gaji + Bonus

# Menampilkan Data
print("Nama: ", Nama)
print("NIK: ", NIK)
print("Status: ", Status)
print("Golongan: ", Golongan)
print("Gaji: ", Gaji)
print("Bonus: ", Bonus)
print("Gaji Total: ", Gaji_Total)

