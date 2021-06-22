# 3.	Почивка
# Джеси е решила да събира пари за екскурзия и иска от вас да ѝ помогнете да разбере дали ще успее да събере необходимата
# сума. Тя спестява или харчи част от парите си всеки ден. Ако иска да похарчи повече от наличните си пари,
# то тя ще похарчи колкото има и ще ѝ останат 0 лева.

excursion_price = float(input())
available_money = float(input())
count_spend_days = 0
count_total_days = 0
has_failed_at_saving = False

while available_money < excursion_price:
    action = input()
    current_day_sum = float(input())
    count_total_days += 1
    if action == 'spend':
        count_spend_days += 1
        if current_day_sum > available_money:
            available_money = 0
        else:
            available_money -= current_day_sum
        if count_spend_days == 5:
            has_failed_at_saving = True
            break
    elif action == 'save':
        available_money += current_day_sum
        count_spend_days = 0

if has_failed_at_saving:
    print(f"You can't save the money.")
    print(count_total_days)
else:
    print(f'You saved the money for {count_total_days} days.')