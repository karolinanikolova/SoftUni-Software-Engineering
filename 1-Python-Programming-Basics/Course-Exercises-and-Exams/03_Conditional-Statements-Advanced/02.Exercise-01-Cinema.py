# 1.	Кино
# В една кинозала столовете са наредени в правоъгълна форма в r реда и c колони. Има три вида прожекции с билети на различни цени:
# •	Premiere – премиерна прожекция, на цена 12.00 лева;
# •	Normal – стандартна прожекция, на цена 7.50 лева;
# •	Discount – прожекция за деца, ученици и студенти на намалена цена от 5.00 лева.
# Напишете програма, която чете тип прожекция (текст), брой редове и брой колони в залата (цели числа),
# въведени от потребителя, и изчислява общите приходи от билети при пълна зала. Резултатът да се отпечата във формат 2 знака след десетичната точка.

film_type = input()
r = int(input())
c = int(input())

count_ticket = r * c

if film_type == 'Premiere':
    price_ticket = 12.00
elif film_type == 'Normal':
    price_ticket = 7.50
elif film_type == 'Discount':
    price_ticket = 5.00

print(f'{count_ticket*price_ticket:.2f}')



