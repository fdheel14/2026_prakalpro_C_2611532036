is_lulus = True
is_cumlaude = True

# Menggunakan Boolean
nilai_2036 = 50
batas_lulus_2036 = 75

# Menentukan nilai Boolean dari kondisi
status_kelulusan = nilai_2036 >= batas_lulus_2036 # Hasilnya akan True

print("=== Check Kelulusan ===")
print("Nilai :", nilai_2036)
print("Apakah Lulus?:", status_kelulusan)
if status_kelulusan is True :
    print("Selamat, Anda lulus dengan predikan Cum Laude")
if status_kelulusan is False :
    print("Maaf, anda tidak lulus")