# 2. Add and Subtract
# You will receive three integer numbers.
# Write a function sum_numbers() to get the sum of the first two integers and subtract() function that subtracts the
# third integer from the result. Wrap the two functions in a function called add_and_subtract()
# which will receive the three numbers

def sum_numbers(num1, num2):
    result_sum = num1 + num2
    return result_sum


def subtract(result_sum, num3):
    return result_sum - num3


def add_and_subtract(num1, num2, num3):
    result_sum = sum_numbers(num1, num2)
    return subtract(result_sum, num3)


first_number = int(input())
second_number = int(input())
third_number = int(input())

print(add_and_subtract(first_number, second_number, third_number))
