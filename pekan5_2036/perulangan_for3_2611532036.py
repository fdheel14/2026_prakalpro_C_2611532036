ulang_2036 = int(input("Masukkan jumlah perulangan: "))

jumlah_2036 = 0
for i_2036 in range(1, ulang_2036 + 1):
    print(i_2036, end=" ")
    jumlah_2036 = jumlah_2036 + i_2036

    if i_2036 < ulang_2036:
        print("+", end=" ")
    else :
        print("= ", end="")
print()
print("Jumlah =", jumlah_2036)