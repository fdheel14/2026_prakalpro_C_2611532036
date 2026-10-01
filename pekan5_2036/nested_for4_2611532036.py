tinggi_2036 = int(input("Masukkan tinggi pola (bilangan genap, misal 10): "))

if tinggi_2036 % 2 != 0:
    print("Tinggi pola harus bilangan genap!")
else :
    a_2036 = tinggi_2036
    c_2036 = a_2036
    lebar_2036 = (2 * tinggi_2036) - 2

    for i_2036 in range(1, tinggi_2036 + 1):
        b_2036 = c_2036 + 1

        for j_2036 in range(1, lebar_2036 + 1):

            # Baris atas dan bawah
            if i_2036 == 1 or i_2036 == tinggi_2036:
                if j_2036 == 1 or j_2036 == lebar_2036:
                    print("#", end="")
                else:
                    print("=", end="")

            # Baris isi
            else:
                if j_2036 == 1 or j_2036 == lebar_2036:
                    print("|", end="")
                else:
                    if j_2036 == c_2036:
                        print("<", end="")
                    elif j_2036 == b_2036:
                        print(">", end="")
                    elif j_2036 == (lebar_2036 - c_2036):
                        print("<", end="")
                    elif j_2036 == (lebar_2036 - c_2036 + 1):
                        print(">", end="")
                    elif j_2036 > b_2036 and j_2036 < (lebar_2036 - c_2036):
                        print(".", end="")
                    else:
                        print(" ", end="")

                print()

                #Logika asli Java
                a_2036 -= 2

                if a_2036 <= 0:
                    c_2036 = (-a_2036) + 2
                else :
                    c_2036 = a_2036