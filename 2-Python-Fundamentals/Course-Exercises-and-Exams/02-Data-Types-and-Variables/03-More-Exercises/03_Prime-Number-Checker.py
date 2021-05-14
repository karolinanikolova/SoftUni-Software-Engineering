# 3.	Prime Number Checker
# Write a program to check if a number is prime (only wholly divisible by itself and one).
# The input comes as an integer number.
# The output should be true for prime number and false otherwise.

import math

n = int(input())

for divisor in range(2, math.ceil(math.sqrt(n)) +1):
    if n % divisor == 0:
        is_prime = False
        break
    else:
        is_prime = True

if is_prime:
    print('True')
else:
    print('False')
