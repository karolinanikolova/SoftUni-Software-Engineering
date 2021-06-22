# 1.	Билети за мач
# Когато пуснали билетите за Евро 2016, група запалянковци решили да си закупят. Билетите имат две категории с различни цени:
#
# •	VIP – 499.99 лева.
# •	Normal – 249.99 лева.
#
# Запалянковците имат определен бюджет, а броят на хората в групата определя какъв процент от бюджета трябва да се задели за транспорт:

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