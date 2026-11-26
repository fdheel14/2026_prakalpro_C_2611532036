menus = ["Nasi Goreng", "Mie Ayam", "Soto"]
number_of_days = 3
sales = []
# Write your code below

for day in range(1, number_of_days + 1):
    daily_sales = []
    for menu in menus:
        value = int(input(f"Day {day}, {menu}: "))
        daily_sales.append(value)
    sales.append(daily_sales)

print("Total per day :")
for day in range(number_of_days):
    daily_total = sum(sales[day])
    print(f"Day {day + 1}: {daily_total}")

menu_totals = []
for j in range(len(menus)):
    menu_total = 0
    for i in range(number_of_days):
        menu_total += sales[i][j]
    menu_totals.append(menu_total)

print(f"Total per menu : {menu_totals}")

best_selling = max(menu_totals)
best_total = menu_totals.index(best_selling)

best_menu = menus[best_total]

print(f"Best selling menu: {best_menu}")