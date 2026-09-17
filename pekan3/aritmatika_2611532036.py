angka1_2036 = int(input("Input angka-1: "))
angka2_2036 = int(input("Input angka-2: "))

# Penjumlahan
hasil_2036 = angka1_2036 + angka2_2036
print("\nOperator Penjumlahan")
print("Hasil =", hasil_2036)

# Pengurangan
hasil_2036 = angka1_2036 - angka2_2036
print("\nOperator Pengurangan")
print("Hasil =", hasil_2036)

# Perkalian
hasil_2036 = angka1_2036 * angka2_2036
print("\nOperator Perkalian")
print("Hasil =", hasil_2036)

# Pembagian, pembagian bulat, dan sisa bagi
if angka2_2036 != 0:
    hasil_2036 = angka1_2036 / angka2_2036
    print("\nOperator Pembagian")
    print("Hasil =", hasil_2036)

    hasil_2036 = angka1_2036 // angka2_2036
    print("\nOperator Pembagian Bulat")
    print("Hasil =", hasil_2036)

    hasil_2036 = angka1_2036 % angka2_2036
    print("\nOperator Sisa Bagi")
    print("Hasil =", hasil_2036)
else:
    print("\nOperator Pembagian")
    print("Pembagian dengan nol tidak diperbolehkan.")

# Pangkat
hasil_2036 = angka1_2036 ** angka2_2036
print("\nOperator Pangkat") 
print("Hasil =", hasil_2036)