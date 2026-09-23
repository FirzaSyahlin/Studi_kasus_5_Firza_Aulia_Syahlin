def hitung_hotel(jenis_kamar, durasi_menginap):
    if jenis_kamar == "Standard":
        tarif = 200000
    elif jenis_kamar == "Deluxe":
        tarif = 350000

    total = tarif * durasi_menginap
    return total


jenis_kamar = input("Jenis kamar: ")
check_in = (int(input("Tanggal check-in: ")))
check_out = (int(input("Tanggal check-out: ")))

durasi_menginap = check_out - check_in
total = hitung_hotel(jenis_kamar, durasi_menginap)

print("Jenis kamar:", jenis_kamar)
print("Check-in:", check_in)
print("Check-out:", check_out)
print("Durasi menginap:", durasi_menginap, "malam")
print("Total biaya: Rp", total)