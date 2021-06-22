# 1.	Absolute Values
# Write a program that receives a sequence of numbers, separated by a single space, and prints their absolute value as
# a list. Use abs().

# # Option 1 - only comprehension with built-in function
# print([abs(float(el)) for el in input().split()])

def make_absolute(seq):
    return list(map(abs, seq))

nums = [float(el) for el in input().split()]

print(make_absolute(nums))
