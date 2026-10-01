ulang_2036 = int(input("Masukkan nilai batas: "))

jumlah_2036 = 0
for i in range(1, ulang_2036 + 1):
    if i % 2 == 0:
        print(i, end=" ")
        jumlah_2036 = jumlah_2036 + i

        if i < ulang_2036:
            print("+", end=" ")
        else :
            print("= ", jumlah_2036, end="")
print()
print("Jumlah =", jumlah_2036)