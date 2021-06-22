# най-малко число
# Да се напише програма, която въвежда n цели числа (n > 0) и намира най-малкото измежду тях.
# Първо се въвежда броя числа n, след тях още n числа по едно на ред.

import sys

n = int(input())
min = sys.maxsize

for i in range(1, n + 1):
    current_num = int(input())
    if current_num < min:
        min = current_num

print(min)