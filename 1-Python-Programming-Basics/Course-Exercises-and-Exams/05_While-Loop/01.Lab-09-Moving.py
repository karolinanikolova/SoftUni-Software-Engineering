# 9.	*Преместване
# На осемнадесетия си рожден ден Хосе взел решение, че ще се изнесе да живее на квартира. Опаковал багажа си в кашони
# и намерил подходяща обява за апартамент под наем. Той започва да пренася своя багаж на части, защото не може наведнъж.
# Има ограничено свободно пространство в новото си жилище, където може да разположи вещите, така че мястото да бъде
# подходящо за живеене.
# Напишете програма, която изчислява свободния обем от жилището на Хосе, който остава, след като пренесе багажа си.
# Всеки кашон е с точни размери:  1m x 1m x 1m.

width = int(input())
length = int(input())
height = int(input())
command = input()

free_space = width * length * height

while command != 'Done':
    count_box = int(command)
    free_space -= count_box
    if free_space <= 0:
        print(f'No more free space! You need {abs(free_space)} Cubic meters more.')
        break
    command = input()
else:
    print(f'{free_space} Cubic meters left.')
