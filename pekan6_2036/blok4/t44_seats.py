blocked_seat=int(input("masukkan batas: "))
for row in range (1,4):
    print("Row",row, ":", end=" ")
    for column in range (1,6):
        if column == blocked_seat:
            break
        print( column, end=" ")
    print()