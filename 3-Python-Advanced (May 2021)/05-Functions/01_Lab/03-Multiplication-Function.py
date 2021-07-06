# 3.	Multiplication Function
# Write a function called multiply that can receive any amount of numbers (integers) as different parameters and
# returns the result of the multiplication of all of them. Submit only your function in the Judge system.

# def multiply(*args):
#     result = 1
#     for index in range(len(args)):
#         result *= args[index]
#
#     return result

# Option 2
from functools import reduce


def multiply(*args):
    return reduce(lambda x, y: x*y, args)


print(multiply(1, 4, 5))
print(multiply(4, 5, 6, 1, 3))
print(multiply(2, 0, 1000, 5000))
