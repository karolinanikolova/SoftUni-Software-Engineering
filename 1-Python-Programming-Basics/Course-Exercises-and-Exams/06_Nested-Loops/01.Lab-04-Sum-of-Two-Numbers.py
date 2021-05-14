# 4.	Сума от две числа
# Напишете програма която проверява всички възможни комбинации от двойка числа в интервала от две дадени числа.
# а изхода се отпечатва, коя поред е комбинацията чиито сбор от числата е равен на дадено магическо число.
# Ако няма нито една комбинация отговаряща на условието се отпечатва съобщение, че не е намерено.

interval_start = int(input())
interval_end = int(input())
magic_number = int(input())
counter = 0
magic_combination_found = False

for number1 in range(interval_start, interval_end + 1):
    for number2 in range(interval_start, interval_end + 1):
        counter += 1
        if number1 + number2 == magic_number:
            print(f'Combination N:{counter} ({number1} + {number2} = {magic_number})')
            magic_combination_found = True
    if magic_combination_found:
        break

if not magic_combination_found:
    print(f'{counter} combinations - neither equals {magic_number}')