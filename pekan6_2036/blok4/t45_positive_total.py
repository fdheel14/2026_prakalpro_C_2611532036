total = 0
while True:
    number=int(input("enter a number: "))
    if number < 0 :
        break
    if number == 0 :
        continue
    print(f"positive number: {number}")
    total += number
print(f"total : {total}")    