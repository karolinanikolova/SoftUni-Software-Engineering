# 9.	Сума от две числа
# Напишете програма която проверява всички възможни комбинации от двойка числа в интервала от две дадени числа.
# На изхода се отпечатва, коя поред е комбинацията чиито сбор от числата е равен на дадено магическо число.
# Ако няма нито една комбинация отговаряща на условието се печата съобщение, че не е намерено.

start_of_interval = int(input())
end_of_interval = int(input())
magic_number = int(input())
counter_combinations = 0
is_combination_found = False

for first_number in range(start_of_interval, end_of_interval + 1):
    for second_number in range(start_of_interval, end_of_interval + 1):
        counter_combinations += 1
        if first_number + second_number == magic_number:
            print(f'Combination N:{counter_combinations} ({first_number} + {second_number} = {magic_number})')
            is_combination_found = True
    if is_combination_found:
        break

if not is_combination_found:
    print(f'{counter_combinations} combinations - neither equals {magic_number}')
