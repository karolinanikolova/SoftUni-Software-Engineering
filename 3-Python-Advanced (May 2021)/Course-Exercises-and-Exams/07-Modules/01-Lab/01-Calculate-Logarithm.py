# 1.	Calculate Logarithm
# Write a program that prints the calculated logarithm of any given number

from math import log


def calc_log(x, base):
    if base == 'natural':
        return log(x)
    else:
        return log(x, int(base))


print(f"{calc_log(10, 'natural'):.2f}")
print(f"{calc_log(10, '10'):.2f}")

