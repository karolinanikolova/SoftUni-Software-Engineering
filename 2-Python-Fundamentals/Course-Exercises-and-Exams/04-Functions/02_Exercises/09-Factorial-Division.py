# 9. * Factorial Division
# Write a function that receives two integer numbers. Calculate factorial of each number.
# Divide the first result by the second and print the division formatted to the second decimal point.

# from math import factorial
#
#
# def factorial_division(num1, num2):
#     first_number_factorial = factorial(num1)
#     second_number_factorial = factorial(num2)
#     return first_number_factorial / second_number_factorial
#
#
# first_number = int(input())
# second_number = int(input())
#
# result = factorial_division(first_number, second_number)
#
# print(f'{result:.2f}')

def calc_factorial(num):
    factorial = 1
    for n in range(1, num + 1):
        factorial *= n
    return factorial


def get_factorial_division(f1, f2):
    return f1 / f2


first_number = int(input())
second_number = int(input())

first_number_factorial = calc_factorial(first_number)
second_number_factorial = calc_factorial(second_number)

result = get_factorial_division(first_number_factorial, second_number_factorial)

print(f'{result:.2f}')
