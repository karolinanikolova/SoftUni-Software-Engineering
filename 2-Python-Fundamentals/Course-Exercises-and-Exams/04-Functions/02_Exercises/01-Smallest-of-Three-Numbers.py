# 1. Smallest of Three Numbers
# Write a function which receives three integer numbers and returns the smallest. Use appropriate name for the function.

def smallest_of_three_numbers(num1, num2, num3):
    return min(num1, num2, num3)


first_number = int(input())
second_number = int(input())
third_number = int(input())

result = smallest_of_three_numbers(first_number, second_number, third_number)

print(result)