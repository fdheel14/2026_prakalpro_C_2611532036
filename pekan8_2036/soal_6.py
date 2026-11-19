LAST_DIGIT = 6  # change to the last digit of your NIM
daily_limit = 30000 + LAST_DIGIT * 1000
expenses = []
# Write your code below
for day in range(1, 8):
    values = int(input(f"Day {day}: "))
    expenses.append(values)
total = 0
highest_spent = expenses[0] if expenses else 0
highest_day = 1
days_above_limit = 0
for i in range(len(expenses)):
    total += expenses[i]
    if expenses[i] > highest_spent:
        highest_spent = expenses[i]
        highest_day = i + 1      
    if expenses[i] > daily_limit:
        days_above_limit += 1

average = total / 7

# Mencetak 5 baris output sesuai format
print(f"Daily limit: {daily_limit}")
print(f"Total: {total}")
print(f"Average: {average:.1f}")
print(f"Highest: day {highest_day} ({highest_spent})")
print(f"Days above limit: {days_above_limit}")
