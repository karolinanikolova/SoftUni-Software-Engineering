# 13.	*Ски почивка
# Атанас решава да прекара отпуската си в Банско и да кара ски. Преди да отиде обаче, трябва да резервира хотел и да изчисли колко ще му струва престоят. Съществуват следните видове помещения със следните цени за престой:
# 	"room for one person" – 18.00 лв за нощувка
# 	"apartment" – 25.00 лв за нощувка
# 	"president apartment" – 35.00 лв за нощувка
# Според броят на дните, в които ще остане в хотела (пример: 11 дни = 10 нощувки) и видът на помещението, което ще избере,
# той може да ползва различно намаление. Намаленията са както следва:
# вид помещение	                    по-малко от 10 дни	        между 10 и 15 дни	        повече от 15 дни
# room for one person	            не ползва намаление	        не ползва намаление	        не ползва намаление
# apartment	                        30% от крайната цена	    35% от крайната цена	    50% от крайната цена
# president apartment	            10% от крайната цена	    15% от крайната цена	    20% от крайната цена
# След престоя оценката на Атанас за услугите на хотела може да е позитивна (positive) или негативна (negative) .
# Ако оценката му е позитивна, към цената с вече приспаднатото намаление Атанас добавя 25% от нея. Ако оценката му е негативна приспада от цената 10%.
# На конзолата трябва да се отпечата един ред - цената за престоят му в хотела, форматирана до втория знак след десетичната запетая.

days = int(input())
room_type = input()
grade = input()

final_price = 0
nights = days - 1

if room_type == 'room for one person':
    final_price = nights * 18
elif room_type == 'apartment':
    final_price = nights * 25
elif room_type == 'president apartment':
    final_price = nights * 35

if room_type == 'apartment':
    if days < 10:
        final_price = final_price * (1 - 0.3)
    elif 10 <= days <= 15:
        final_price = final_price * (1 - 0.35)
    elif days > 15:
        final_price = final_price * (1 - 0.5)
elif room_type == 'president apartment':
    if days < 10:
        final_price = final_price * (1 - 0.1)
    elif 10 <= days <= 15:
        final_price = final_price * (1 - 0.15)
    elif days > 15:
        final_price = final_price * (1 - 0.2)

if grade == 'positive':
    final_price = final_price * (1 + 0.25)
elif grade == 'negative':
    final_price = final_price * (1 - 0.1)

print(f'{final_price:.2f}')

