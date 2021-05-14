# 7.	Най-малко число
# Напишете програма, която до получаване на командата "Stop", чете цели числа, въведени от потребителя,
# и намира най-малкото измежду тях. Въвежда се по едно число на ред.

import sys

command = input()
min = sys.maxsize

while command != 'Stop':
    number = int(command)
    if number < min:
        min = number
    command = input()

print(min)

