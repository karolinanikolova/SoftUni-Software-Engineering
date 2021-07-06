# 2.	Sort
# Write a program that receives a sequence of numbers (integers), separated by a single space.
# It should print a sorted list of numbers in ascending order. Use sorted().

nums = [int(el) for el in input().split()]

sorted_nums = sorted(nums, key=lambda x: x)

print(sorted_nums)