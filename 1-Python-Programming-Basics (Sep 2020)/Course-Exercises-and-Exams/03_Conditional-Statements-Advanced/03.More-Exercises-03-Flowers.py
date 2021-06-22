# 3.	Магазин за цветя
# Магазин за цветя предлага 3 вида цветя: хризантеми, рози и лалета. Цените зависят от сезона.
# Сезон	            Хризантеми	    Рози	        Лалета
# Пролет / Лято	    2.00 лв./бр.	4.10 лв./бр.	2.50 лв./бр.
# Есен / Зима	        3.75 лв./бр.	4.50 лв./бр.	4.15 лв./бр.
# В празнични дни цените на всички цветя се увеличават с 15%. Предлагат се следните отстъпки:
# •	За закупени повече от 7 лалета през пролетта – 5% от цената на целият букет.
# •	За закупени 10 или повече рози през зимата – 10% от цената на целият букет.
# •	За закупени повече от 20 цветя общо през всички сезони – 20% от цената на целият букет.
# Отстъпките се правят по така написания ред и могат да се наслагват! Всички отстъпки важат след оскъпяването за празничен ден!
# Цената за аранжиране на букета винаги е 2лв. Напишете програма, която изчислява цената за един букет.

count_chrysanthemum = int(input())
count_rose = int(input())
count_tulip = int(input())
season = input()
is_holiday = input()

if season == 'Spring' or season == 'Summer':
    price_chrysanthemum = 2.00
    price_rose = 4.10
    price_tulip = 2.50
elif season == 'Autumn' or season == 'Winter':
    price_chrysanthemum = 3.75
    price_rose = 4.50
    price_tulip = 4.15

price_flowers = count_chrysanthemum * price_chrysanthemum + count_rose * price_rose + count_tulip * price_tulip

if is_holiday == 'Y':
    price_flowers = price_flowers * 1.15

if count_tulip > 7 and season == 'Spring':
    price_flowers = 0.95 * price_flowers
if count_rose >= 10 and season == 'Winter':
    price_flowers = 0.9 * price_flowers
if (count_rose + count_tulip + count_chrysanthemum) > 20:
    price_flowers = 0.8 * price_flowers

price_flowers_total = price_flowers + 2

print(f'{price_flowers_total:.2f}')
