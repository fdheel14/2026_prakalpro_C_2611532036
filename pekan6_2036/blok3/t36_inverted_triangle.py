height = int(input("masukkan tinggi:" ))
for row in range(1, height + 1 ):
    for column in range(1, (height - row + 1 ) + 1):
        print("*", end=" ")
    print()
