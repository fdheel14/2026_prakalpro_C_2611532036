angka1_2036 = int(input("Input angka-1: "))
angka2_2036 = int(input("Input angka-2: "))

print("\nNilai awal angka1 = ", angka1_2036)
print("Nilai awal angka2 = ", angka2_2036)

#Assignment biasa
hasil_2036 = angka1_2036
print("\nHasil assignment biasa: (=)")
print("Hasil =", hasil_2036)

#Assignment penambahan
hasil_2036 = angka1_2036
hasil_2036 += angka2_2036
print("\nHasil assignment penambahan: (+=)")
print("Hasil =", hasil_2036)

#Assignment pengurangan
hasil_2036 = angka1_2036
hasil_2036 -= angka2_2036
print("\nHasil assignment pengurangan: (-=)")
print("Hasil =", hasil_2036)

#Assignment perkalian
hasil_2036 = angka1_2036
hasil_2036 *= angka2_2036
print("\nHasil assignment perkalian: (*=)")
print("Hasil =", hasil_2036)

#Assignment pembagian, pembagian bulat, dan sisa bagi
if angka2_2036 != 0:
    hasil_2036 = angka1_2036
    hasil_2036 /= angka2_2036
    print("\nHasil assignment pembagian: (/=)")
    print("Hasil =", hasil_2036)

    hasil_2036 = angka1_2036
    hasil_2036 //= angka2_2036
    print("\nHasil assignment pembagian bulat: (//=)")
    print("Hasil =", hasil_2036)

    hasil_2036 = angka1_2036
    hasil_2036 %= angka2_2036
    print("\nHasil assignment sisa bagi: (%=)")
    print("Hasil =", hasil_2036)
else :
    print("\nPembagian tidak dapat dilakukan.")
    print("Pembagian dengan nol tidak diperbolehkan.")

#Operasi tambahan : assignment perpangkatan
hasil = angka1_2036
hasil_2036 **= angka2_2036
print("\nHasil assignment perpangkatan: (**=)")
print("Hasil =", hasil_2036)