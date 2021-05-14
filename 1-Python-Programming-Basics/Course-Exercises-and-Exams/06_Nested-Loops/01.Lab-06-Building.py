# 6.	Сграда
# Напишете програма, която извежда на конзолата номерата на стаите в една сграда (в низходящ ред), като са изпълнени
# следните условия:
# •	На всеки четен етаж има само офиси;
# •	На всеки нечетен етаж има само апартаменти;
# •	Всеки апартамент се означава по следния начин : А{номер на етажа}{номер на апартамента}, номерата на апартаментите
# започват от 0;
# •	Всеки офис се означава по следния начин : О{номер на етажа}{номер на офиса}, номерата на офисите също започват от 0;
# •	На последният етаж винаги има апартаменти и те са по-големи от останалите, затова пред номера им пише 'L', вместо 'А'.
# Ако има само един етаж, то има само големи апартаменти!
# От конзолата се прочитат две цели числа - броят на етажите и броят на стаите за един етаж.

count_floors = int(input())
count_rooms_per_floor = int(input())

for floor in range (count_floors, 0, -1):
    for room in range (0, count_rooms_per_floor):
        if floor == count_floors:
            if room == count_rooms_per_floor:
                print(f'L{floor}{room}')
            else:
                print(f'L{floor}{room}', end = ' ')
        elif floor % 2 != 0:
            if room == count_rooms_per_floor:
                print(f'A{floor}{room}')
            else:
                print(f'A{floor}{room}', end = ' ')
        elif floor % 2 == 0:
            if room == count_rooms_per_floor:
                print(f'O{floor}{room}')
            else:
                print(f'O{floor}{room}', end = ' ')
    print()