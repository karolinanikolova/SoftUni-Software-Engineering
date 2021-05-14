# 9.	Резервоар за гориво -  част 2
# Напишете програма, която да изчислява, колко ще струва на един шофьор да напълни резервоара на автомобила си,
# като знаете – какъв тип гориво зарежда, каква е цената за литър гориво и дали разполага с карта за отстъпки. Цените на горивата са както следва:
# •	Бензин – 2.22 лева за един литър,
# •	Дизел – 2.33 лева за един литър
# •	Газ – 0.93 лева за литър
# Ако водача има карта за отстъпки,  той се възползва от следните намаления за литър гориво: 18 ст. за литър бензин, 12 ст. за литър дизел и 8 ст.
# за литър газ.
# Ако шофьора е заредил между 20 и 25 литра включително, той получава 8 процента отстъпка от крайната цена, при повече от 25 литра гориво,
# той получава 10 процента отстъпка от крайната цена.

fuel_type = input()
fuel_quantity = float(input())
is_card_owner = input()

if is_card_owner == 'No':
    if fuel_type == 'Gasoline':
        price = fuel_quantity * 2.22
    elif fuel_type == 'Diesel':
        price = fuel_quantity * 2.33
    elif fuel_type == 'Gas':
        price = fuel_quantity * 0.93
elif is_card_owner == 'Yes':
    if fuel_type == 'Gasoline':
        price = fuel_quantity * (2.22 - 0.18)
    elif fuel_type == 'Diesel':
        price = fuel_quantity * (2.33 - 0.12)
    elif fuel_type == 'Gas':
        price = fuel_quantity * (0.93 - 0.08)

if 20 <= fuel_quantity <= 25:
    price = 0.92 * price
elif fuel_quantity > 25:
    price = 0.9 * price

print(f'{price:.2f} lv.')