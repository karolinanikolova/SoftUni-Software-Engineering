# 4.	Кола под наем
# Напишете програма, която спрямо даден бюджет и сезон да пресмята цената, типа и класа на кола под наем.
# Сезоните са лято и зима – "Summer" и "Winter". Типа коли са кабрио и джип – "Cabrio" и "Jeep".
# •	При бюджет по-малък или равен от 100лв.:
# o	Класът ще е - "Economy class"
# o	Според сезона колата и цената ще са:
# 	Лято – Кабрио – 35% от бюджета
# 	Зима – Джип – 65% от бюджета
# •	При бюджет по-голям от 100лв. и по-малък или равен от 500лв.:
# o	Класът ще е - "Compact class"
# o	Според сезона колата и цената ще са:
# 	Лято – Кабрио – 45% от бюджета
# 	Зима – Джип – 80% от бюджета
# •	При бюджет по-голям от 500лв.:
# o	Класът ще е – "Luxury class"
# o	За всеки сезон колата ще е джип и цената ще е:
# 	90% от бюджета

budget = float(input())
season = input()

if budget <= 100:
    car_class = 'Economy class'
    if season == 'Summer':
        car_type = 'Cabrio'
        car_price = 0.35 * budget
    elif season == 'Winter':
        car_type = 'Jeep'
        car_price = 0.65 * budget
elif 100 < budget <= 500:
    car_class = 'Compact class'
    if season == 'Summer':
        car_type = 'Cabrio'
        car_price = 0.45 * budget
    elif season == 'Winter':
        car_type = 'Jeep'
        car_price = 0.8 * budget
elif budget > 500:
    car_class = 'Luxury class'
    car_type = 'Jeep'
    car_price = 0.9 * budget

print(f'{car_class}')
print(f'{car_type} - {car_price:.2f}')
