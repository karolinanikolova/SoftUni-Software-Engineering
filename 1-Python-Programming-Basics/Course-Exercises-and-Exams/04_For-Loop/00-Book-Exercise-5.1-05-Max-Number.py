# най-голямо число
# Да се напише програма, която въвежда n цели числа (n > 0) и намира най-голямото измежду тях.
# На първия ред на входа се въвежда броят числа n. След това се въвеждат самите числа, по едно на ред.

import sys

n = int(input())
max = - sys.maxsize

for i in range(1, n + 1):
    current_num = int(input())
    if current_num > max:
        max = current_num

print(max)
