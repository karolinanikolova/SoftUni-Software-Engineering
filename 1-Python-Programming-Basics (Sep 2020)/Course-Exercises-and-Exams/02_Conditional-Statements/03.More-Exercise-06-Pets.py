# 6.	Домашни любимци
# Марина обича да пътува. Тя има 3 домашни любимеца (куче, котка и костенурка).
# Когато заминава на пътешествие трябва да съобрази колко храна да им остави, за да не останат гладни.
# Напишете програма, която пресмята колко килограма храна ще изядат всички за времето,
# в което Марина отсъства и дали оставената храна от нея ще им е достатъчна. Всяко животно изяжда определено количество храна на ден.

from math import floor
from math import ceil

days = int(input())
food_left = int(input())
food_dog = float(input())
food_cat = float(input())
food_turtle = float(input()) / 1000

food_needed = days * (food_dog + food_cat + food_turtle)

if food_left >= food_needed:
    print(f'{floor(food_left - food_needed)} kilos of food left.')
else:
    print(f'{ceil(food_needed - food_left)} more kilos of food are needed.')
