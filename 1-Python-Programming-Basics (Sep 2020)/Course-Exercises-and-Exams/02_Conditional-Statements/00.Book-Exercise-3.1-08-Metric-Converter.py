# конвертор за мерни единици
# Да се напише програма, която преобразува разстояние между следните 8 мерни единици: m, mm, cm, mi, in, km, ft, yd. Използвайте съответствията от таблицата по-долу:

amount = float(input())

unit_input = input().lower()
unit_output = input().lower()

if unit_input == 'mm':
    amount = amount / 1000
elif unit_input == 'cm':
    amount = amount / 100
elif unit_input == 'mi':
    amount = amount / 0.000621371192
elif unit_input == 'in':
    amount = amount / 39.3700787
elif unit_input == 'km':
    amount = amount / 0.001
elif unit_input == 'ft':
    amount = amount / 3.2808399
elif unit_input == 'yd':
    amount = amount / 1.0936133

if unit_output == 'mm':
    amount = amount * 1000
elif unit_output == 'cm':
    amount = amount * 100
elif unit_output == 'mi':
    amount = amount * 0.000621371192
elif unit_output == 'in':
    amount = amount * 39.3700787
elif unit_output == 'km':
    amount = amount * 0.001
elif unit_output == 'ft':
    amount = amount * 3.2808399
elif unit_output == 'yd':
    amount = amount * 1.0936133

print(amount)


# # Other method
# amount = float(input())
#
# unit_input = input().lower()
# unit_output = input().lower()
#
# dict = {'m':1, 'mm':1000, 'cm':100, 'mi':0.000621371192, 'in':39.3700787, 'km':0.001, 'ft':3.2808399, 'yd':1.0936133}
#
# amount = amount * dict[unit_output] / dict[unit_input]
#
# print(amount)
