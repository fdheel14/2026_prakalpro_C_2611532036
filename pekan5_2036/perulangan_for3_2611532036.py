ulang_2036 = int(input("Masukkan jumlah perulangan: "))

jumlah_2036 = 0
for i in range(1, ulang_2036 + 1):
    print(i, end=" ")
    jumlah_2036 = jumlah_2036 + i

    if i < ulang_2036:
        print("+", end=" ")
    else :
        print("= ", end="")
print()
print("Jumlah =", jumlah_2036)