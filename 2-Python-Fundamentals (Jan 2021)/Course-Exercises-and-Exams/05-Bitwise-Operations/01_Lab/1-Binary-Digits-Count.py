# 1.	Binary Digits Count
# You are given a positive integer number and one binary digit B (0 or 1).
# Your task is to write a program that finds the number of binary digits (B) in given integer.

decimal_number = int(input())
b = int(input())

x = decimal_number
binary_number_as_string = ''

while x > 0:
    remainder = x % 2
    binary_number_as_string = str(remainder) + binary_number_as_string
    x = x // 2

print(f"{decimal_number} -> {binary_number_as_string}")
if b == 0:
    print(f"We have {binary_number_as_string.count(str(b))} zeroes.")
else:
    print(f"We have {binary_number_as_string.count(str(b))} ones.")

