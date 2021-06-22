# 7.	Магазин за цветя
# Мария иска да купи подарък на сина си. Тя работи в магазин за цветя.
# В магазина идва поръчка за цветя. Напишете програма, която пресмята сумата от поръчката и дали печалбата е достатъчна за подаръка.
# Цветята имат следните цени:
# •	Магнолии – 3.25 лева
# •	Зюмбюли – 4 лева
# •	Рози – 3.50 лева
# •	Кактуси – 8 лева
# От общата сума, Мария трябва да плати 5% данъци.

import math
count_magnolia = int(input())
count_zumbul = int(input())
count_rose = int(input())
count_cactus = int(input())
price_gift = float(input())

sum = count_magnolia * 3.25 + count_zumbul * 4 + count_rose * 3.50 + count_cactus * 8
earnings = 0.95 * sum

if earnings >= price_gift:
    print(f'She is left with {math.floor(abs(earnings - price_gift))} leva.')
else:
    print(f'She will have to borrow {math.ceil(abs(earnings - price_gift))} leva.')