# 8.	Редица цели числа
# Напишете програма, която чете n на брой цели числа. Принтирайте най-голямото и най-малкото число сред въведените.

import sys

n = int(input())

max = - sys.maxsize # -2147483647 We make the initial value of the maximum to be the smallest possible number a type integer ..
                    # can be, so that every number entered is the new maximum
min = sys.maxsize  # 2147483647 We make the initial value of the minimum to be the largest possible number an type integer ..
                    # can be, so that every number entered will be the new minimum

for number in range(1, n + 1):
    value = int(input())
    if value > max:
        max = value
    if value < min:
        min = value

print(f'Max number: {max}')
print(f'Min number: {min}')

