# Задача 4. Котешка храна
# В приют за животни има определен брой котки, които изяждат различно количество храна на ден.
# Задачата ви е да изчислите колко е броят на котките във всяка група и парите, които са нужни на
# собственика за храната им за един ден, ако 1 кг храна = 12.45 лева.
# •	Ако котката изяжда от 100 (вкл.)  до 200 грама, то тя попада в група 1: малки котки.
# •	Ако котката изяжда от 200 (вкл.)  до 300 грама, то тя попада в група 2: големи котки.
# •	Ако котката изяжда от 300 (вкл.)  до 400 грама, то тя попада в група 3: огромни котки.

count_cats = int(input())
total_food_grams = 0
count_cats_group_one = 0
count_cats_group_two = 0
count_cats_group_three = 0

for cat in range(1, count_cats + 1):
    cat_food_amount = float(input())
    total_food_grams += cat_food_amount
    if 100 <= cat_food_amount < 200:
        count_cats_group_one += 1
    elif 200 <= cat_food_amount < 300:
        count_cats_group_two += 1
    elif 300 <= cat_food_amount < 400:
        count_cats_group_three += 1

total_food_kg = total_food_grams / 1000
price_food_per_day = total_food_kg * 12.45

print(f'Group 1: {count_cats_group_one} cats.')
print(f'Group 2: {count_cats_group_two} cats.')
print(f'Group 3: {count_cats_group_three} cats.')
print(f'Price for food per day: {price_food_per_day:.2f} lv.')
