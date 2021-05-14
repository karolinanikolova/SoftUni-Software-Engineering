# 3.	Special Numbers
# A number is special when the sum of its digits is 5, 7 or 11.
#
# Write a program to read an integer n and for all numbers in the range 1…n, print the number and if it is special or not (True / False).

n = int(input())

for num in range(1, n+1):
    num_as_string = str(num)
    sum_digits = 0
    for num_str in num_as_string:
        sum_digits += int(num_str)
    if sum_digits == 5 or sum_digits == 7 or sum_digits == 11:
        print(f'{num} -> True')
    else:
        print(f'{num} -> False')

