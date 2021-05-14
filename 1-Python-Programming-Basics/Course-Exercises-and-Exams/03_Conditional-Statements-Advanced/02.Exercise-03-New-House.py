# # 3.	Нов дом
# # Марин и Нели си купуват къща недалеч от София. Нели толкова много обича цветята, че Ви убеждава да напишете програма,
# # която да изчисли колко  ще им струва, за да засадят определен брой цветя и дали наличният бюджет ще им е достатъчен. Различните цветя са с различни цени:
# # цвете	                Роза	Далия	Лале	Нарцис	Гладиола
# # Цена на брой в лева	    5	    3.80	2.80	3	    2.50
#
# Съществуват следните отстъпки:
# •	Ако Нели купи повече от 80 Рози - 10% отстъпка от крайната цена;
# •	Ако Нели купи повече от 90  Далии - 15% отстъпка от крайната цена;
# •	Ако Нели купи повече от 80 Лалета - 15% отстъпка от крайната цена;
# •	Ако Нели купи по-малко от 120 Нарциса - цената се оскъпява с 15%;
# •	Ако Нели Купи по-малко от 80 Гладиоли - цената се оскъпява с 20%.
# От конзолата се четат 3 реда:
# •	Вид цветя - текст с възможности "Roses", "Dahlias", "Tulips", "Narcissus" или "Gladiolus";
# •	Брой цветя - цяло число;
# •	Бюджет - цяло число.
# Да се отпечата на конзолата на един ред:
# •	Ако бюджетът им е достатъчен - "Hey, you have a great garden with {броя цвета} {вид цветя} and {останалата сума} leva left.";
# •	Ако бюджета им е НЕ достатъчен - "Not enough money, you need {нужната сума} leva more.".
# Сумата да бъде форматирана до втория знак след десетичната запетая.

type_flower = input()
count_flower = int(input())
budget = int(input())
price_flower = 0

if type_flower == 'Roses':
    if count_flower <= 80:
        price_flower = 5
    else:
        price_flower = 0.9 * 5
elif type_flower == 'Dahlias':
    if count_flower <= 90:
        price_flower = 3.80
    else:
        price_flower = 0.85 * 3.80
elif type_flower == 'Tulips':
    if count_flower <= 80:
        price_flower = 2.80
    else:
        price_flower = 0.9 * 2.80
elif type_flower == 'Narcissus':
    if count_flower < 120:
        price_flower = 3 * 1.15
    else:
        price_flower = 3
elif type_flower == 'Gladiolus':
    if count_flower < 80:
        price_flower = 2.5 * 1.2
    else:
        price_flower = 2.5

price_total = price_flower * count_flower

if price_total <= budget:
    print(f'Hey, you have a great garden with {count_flower} {type_flower} and {abs(price_total - budget):.2f} leva left.')
else:
    print(f'Not enough money, you need {abs(price_total - budget):.2f} leva more.')