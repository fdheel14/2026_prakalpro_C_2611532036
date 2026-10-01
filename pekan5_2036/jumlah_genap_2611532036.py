ulang_2036 = int(input("Masukkan nilai batas: "))

jumlah_2036 = 0
for i_2036 in range(1, ulang_2036 + 1):
    if i_2036 % 2 == 0:
        print(i_2036, end=" ")
        jumlah_2036 = jumlah_2036 + i_2036

        if i_2036 < ulang_2036:
            print("+", end=" ")
        else :
            print("= ", jumlah_2036, end="")
print()
print("Jumlah =", jumlah_2036)