# Задача 1. Разстояние до Луната
# Георги е космонавт и следващата му мисия е да отиде до Луната. Ако се движи със скорост от X километра в час,
# той ще стигне до там за N часа. Приемаме, че разстоянието между Луната и Земята е 384 400 км. Георги ще прекара
# 3 часа на Луната, след което ще тръгне обратно към Земята.
# Напишете програма, която пресмята за колко часа Георги ще отиде и ще се върне и колко литра гориво ще са му нужни.

from math import ceil

distance_one_way = 384400
speed = float(input())
litres_per_hundred_km = float(input())

total_distance = distance_one_way * 2
hours_moving = (total_distance / speed)
total_hours = ceil(hours_moving + 3)
fuel = (litres_per_hundred_km * total_distance / 100)

print(total_hours)
print(f'{fuel:.0f}')
