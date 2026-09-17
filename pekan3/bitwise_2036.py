print("\n==================================")
print("3. OPERATOR BITWISE")
print("===================================")

angka1_2036 = int(input("Input angka bitwise-1: "))
angka2_2036 = int(input("Input angka bitwise-2: "))

print("\nAngka dalam bentuk desimal dan biner")
print("angka1 =", angka1_2036, "| biner =", bin(angka1_2036))
print("angka2 =", angka2_2036, "| biner =", bin(angka2_2036))

# Bitwise AND
hasil_2036 = angka1_2036 & angka2_2036
print("\nBitwise AND (&)")
print(angka1_2036, "&", angka2_2036, "=", hasil_2036)
print("Biner hasil =", bin(hasil_2036))
print("Biner hasil (8 bit) =", format(hasil_2036, '08b'))

# Bitwise OR
hasil_2036 = angka1_2036 | angka2_2036
print("\nBitwise OR (|)")
print(angka1_2036, "|", angka2_2036, "=", hasil_2036)
print("Biner hasil =", bin(hasil_2036))
print("Biner hasil (8 bit) =", format(hasil_2036, '08b'))

# Bitwise XOR
hasil_2036 = angka1_2036 ^ angka2_2036
print("\nBitwise XOR (^)")
print(angka1_2036, "^", angka2_2036, "=", hasil_2036)
print("Biner hasil =", bin(hasil_2036))
print("Biner hasil (8 bit) =", format(hasil_2036, '08b'))

# Bitwise NOT
hasil_2036 = ~angka1_2036
print("\nBitwise NOT (~)")
print("~", angka1_2036, "=", hasil_2036)
print("Biner hasil =", bin(hasil_2036))
print("Biner hasil (8 bit) =", format(hasil_2036, '08b'))

# Bitwise geser kiri
jumlah_geser_2036 = int(input("\nMasukkan jumlah geser kiri: "))

hasil_2036 = angka1_2036 << jumlah_geser_2036
print("\nBitwise geser kiri (<<)")
print(angka1_2036, "<<", jumlah_geser_2036, "=", hasil_2036)
print("Biner hasil =", bin(hasil_2036))
print("Biner hasil (8 bit) =", format(hasil_2036, '08b'))

# Bitwise geser kanan
jumlah_geser_2036 = int(input("\nMasukkan jumlah geser kanan: "))

hasil_2036 = angka1_2036 >> jumlah_geser_2036
print("\nBitwise geser kanan (>>)")
print(angka1_2036, ">>", jumlah_geser_2036, "=", hasil_2036)
print("Biner hasil =", bin(hasil_2036))
print("Biner hasil (8 bit) =", format(hasil_2036, '08b'))