tinggi_2036 = int(input("Masukkan nilai batas: "))

for i_2036 in range(1, tinggi_2036 + 1):
    print(" " * (tinggi_2036 - i_2036), end="")
    for j_2036 in range(1, i_2036 + 1):
        print("*", end=" ")
    print()