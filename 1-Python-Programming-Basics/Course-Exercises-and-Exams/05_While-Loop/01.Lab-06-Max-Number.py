# 6.	Най-голямо число
# Напишете програма, която до получаване на командата "Stop", чете цели числа, въведени от потребителя,
# и намира най-голямото измежду тях. Въвежда се по едно число на ред.

import sys

command = input()
max_number = - sys.maxsize

while command != 'Stop':
    command = int(command)
    if command > max_number:
        max_number = command
    command = input()

print(max_number)