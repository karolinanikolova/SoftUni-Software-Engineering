# елемент, равен на сумата на останалите
# Да се напише програма, която въвежда n цели числа и проверява дали сред тях съществува число, което е
# равно на сумата на всички останали. Ако има такъв елемент,
# се отпечатва "Yes" + неговата стойност, в противен случай - "No" + разликата между най-големия елемент и
# сумата на останалите (по абсолютна стойност).

import sys

n = int(input())
sum = 0
max = - sys.maxsize
special_element = 0

# Find the sum + max number
for i in range(1, n + 1):
    current_number = int(input())
    sum = sum + current_number
    if current_number > max:
        max = current_number

if max == sum - max:
    print('Yes')
    print(f'Sum = {max}')
else:
    print('No')
    print(f'Diff = {abs((sum - max) - max)}')





