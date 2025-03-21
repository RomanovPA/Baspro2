# Input informasi
Nama = input("Nama: ")
Nik = input("NIK: ")
StatusInput = input("Status: ").lower()
Golongan = input("Golongan: ").lower()

# Status dan Golongan dalam list
Status =["tetap", "honor"]
Gol = ["a", "b", "c"]

# Cek Status dan Menghitung Gaji
for i in Status:
    if StatusInput == "tetap":
        for j in Gol:
                gaji = 1000000
                if Golongan == "a":
                    bonus = 200000
                elif Golongan == "b":
                    bonus = 400000
                elif Golongan == "c":
                    bonus = 550000
                else:
                    print("Golongan Tidak Diketahui")
        
        Total = gaji + bonus
        
                
    elif StatusInput == "honor":
        for j in Gol:
                gaji = 750000
                if Golongan == "a":
                    bonus = 150000
                elif Golongan == "b":
                    bonus = 275000
                elif Golongan == "c":
                    bonus = 480000
                else:
                    print("Golongan Tidak Diketahui")
        
        total = gaji + bonus
        
          
    else:
        print("Unknown")

# Print Informasi Input
print("Nama:", Nama)
print("NIK:", Nik)
print("Status:", status)
print("Golongan", Golongan)

# Print Hasil
print("Gaji:", gaji)
print("Bonus:", bonus)
print("Total Gaji:", total)