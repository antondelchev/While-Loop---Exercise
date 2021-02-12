money_for_holiday = float(input())
current_money = float(input())

days_total = 0
counter = 0

while current_money < money_for_holiday:
    action = input()
    money = float(input())
    days_total += 1
    if action == "spend":
        counter += 1
        current_money -= money
        if current_money < 0:
            current_money = 0
    elif action == "save":
        counter = 0
        current_money += money
    if counter == 5:
        break

if current_money >= money_for_holiday:
    print(f"You saved the money for {days_total} days.")
else:
    print(f"You can't save the money.")
    print(days_total)
