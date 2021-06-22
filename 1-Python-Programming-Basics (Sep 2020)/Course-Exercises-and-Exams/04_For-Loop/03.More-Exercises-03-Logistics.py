# 3.	Логистика
# Отговаряте за логистиката на различни товари. В зависимост от теглото на товара е нужно различно превозно средство.
# Цената на тон, за която се превозва товара е различна за всяко превозно средство:
# •	До 3 тона – микробус (200 лева на тон)
# •	От 4 до 11 тона – камион (175 лева на тон)
# •	12 и повече тона – влак (120 лева на тон)
# Вашата задача е да изчислите средната цена на тон превозен товар, както и процента на тоновете  превозвани с всяко
# превозно средство, спрямо общото тегло(в тонове) на всички товари.

loads = int(input())
load_tonnage_total = 0
load_tonnage_minibus = 0
load_tonnage_truck = 0
load_tonnage_train = 0
price_load_total = 0

for load in range(1, loads + 1):
    load_tonnage_current = float(input())
    load_tonnage_total += load_tonnage_current
    if load_tonnage_current <= 3:
        load_tonnage_minibus += load_tonnage_current
        price_load_total += load_tonnage_current * 200
    elif 4 <= load_tonnage_current <= 11:
        load_tonnage_truck += load_tonnage_current
        price_load_total += load_tonnage_current * 175
    else:
        load_tonnage_train += load_tonnage_current
        price_load_total += load_tonnage_current * 120

print(f'{price_load_total / load_tonnage_total:.2f}')
print(f'{(load_tonnage_minibus / load_tonnage_total) * 100:.2f}%')
print(f'{(load_tonnage_truck / load_tonnage_total) * 100:.2f}%')
print(f'{(load_tonnage_train / load_tonnage_total) * 100:.2f}%')