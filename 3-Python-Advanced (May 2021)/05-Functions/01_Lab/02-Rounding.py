# 2.	Rounding
# Write a program that rounds all the given numbers, separated by a single space, and prints the result as a list.
# Use round().

# # Option 1 - only comprehension with built-in function
# print([round(float(el)) for el in input().split()])

nums = [float(el) for el in input().split()]

rounded_nums = map(round, nums) # this is identical to bottom one, but it's по преференция
# rounded_nums = map(lambda x: round(x), nums)

print(list(rounded_nums))

