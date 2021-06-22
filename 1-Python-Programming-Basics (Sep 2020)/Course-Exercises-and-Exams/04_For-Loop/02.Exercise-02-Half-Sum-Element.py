# 2.	 Елемент, равен на сумата на останалите
# Да се напише програма, която чете n-на брой цели числа, въведени от потребителя, и проверява дали сред тях съществува
# число, което е равно на сумата на всички останали. Ако има такъв елемент, печата "Yes", "Sum = "  + неговата стойност;
# иначе печата "No", "Diff = " + разликата между най-големия елемент и сумата на останалите (по абсолютна стойност).

import sys

numbers = int(input())
sum_of_all_numbers = 0
max_element = - sys.maxsize

for i in range(1, numbers + 1):
    current_number = int(input())
    sum_of_all_numbers += current_number
    if current_number > max_element:
        max_element = current_number

if max_element == sum_of_all_numbers - max_element:
    print('Yes')
    print(f'Sum = {max_element}')
else:
    print('No')
    print(f'Diff = {abs((sum_of_all_numbers - max_element) - max_element)}')