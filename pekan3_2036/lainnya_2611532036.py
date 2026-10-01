print("===================================")
print("1. OPERATOR KEANGGOTAAN")
print("===================================")

# Input beberapa data yang dipisahkan dengan koma
input_data_2036 = input("Masukkan beberapa angka, pisahkan dengan koma : ")

# Mengubah input menjadi list integer
data_2036 = [int(angka.strip()) for angka in input_data_2036.split(",")]

nilai_dicari_2036 = int(input("Masukkan nilai yang ingin dicari : "))

# Operator in
hasil_2036 = nilai_dicari_2036 in data_2036
print("\nOperator keanggotaan IN")
print(nilai_dicari_2036, "in", data_2036, "=", hasil_2036)

# Operator not in
hasil_2036 = nilai_dicari_2036 not in data_2036
print("\nOperator keanggotaan NOT IN")
print(nilai_dicari_2036, "not in", data_2036, "=", hasil_2036)

print("\n===================================")
print("2. OPERATOR IDENTITAS")
print("===================================")

# objek1 menggunakan list dari input pengguna
objek1_2036 = data_2036

# objek2 merujuk pada objek yang sama dengan objek1
objek2_2036 = objek1_2036

# objek3 memiliki isi sama, tetapi menggunakan objek baru
objek3_2036 = data_2036.copy()

print("objek1 =", objek1_2036)
print("objek2 =", objek2_2036)
print("objek3 =", objek3_2036)

# Operator is
hasil_2036 = objek1_2036 is objek2_2036
print("\nOperator identitas IS")
print("objek1 is objek2 =", hasil_2036)

# Operator is not
hasil_2036 = objek1_2036 is not objek3_2036
print("\nOperator identitas IS NOT")
print("objek1 is not objek3 =", hasil_2036)

# Membandingkan identitas dan nilai
print("\nPerbandingan identitas dan nilai")
print("objek1 is objek3 =", objek1_2036 is objek3_2036)
print("objek1 is objek2 =", objek1_2036 is objek2_2036)