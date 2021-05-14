# билети за мач
# Група запалянковци решили да си закупят билети за Евро 2016. Цената на билета се определя спрямо две категории:
#
# VIP – 499.99 лева.
# Normal – 249.99 лева.
# Запалянковците имат определен бюджет, a броят на хората в групата определя какъв процент от бюджета трябва да се
# задели за транспорт:
#
# От 1 до 4 – 75% от бюджета.
# От 5 до 9 – 60% от бюджета.
# От 10 до 24 – 50% от бюджета.
# От 25 до 49 – 40% от бюджета.
# 50 или повече – 25% от бюджета.
# Напишете програма, която да пресмята дали с останалите пари от бюджета могат да си купят билети за избраната
# категория, както и колко пари ще им останат или ще са им нужни.

budget = float(input())
category = input()
count_people = int(input())

transport_charges = 0
price_total = 0

if 0 < count_people <= 4:
    transport_charges = budget * 0.75
elif 5 <= count_people <= 9:
    transport_charges = budget * 0.60
elif 10 <= count_people <= 24:
    transport_charges = budget * 0.5
elif 25 <= count_people <= 49:
    transport_charges = budget * 0.4
elif count_people >= 50:
    transport_charges = budget * 0.25

leftover_budget = budget - transport_charges

if category == 'VIP':
    price_total = count_people * 499.99
elif category == 'Normal':
    price_total = count_people * 249.99

if leftover_budget >= price_total:
    print(f'Yes! You have {abs(leftover_budget - price_total):.2f} leva left.')
else:
    print(f'Not enough money! You need {abs(leftover_budget - price_total):.2f} leva.')