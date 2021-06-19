# 5.	Filter Numbers
# You will be given two lines of input - a start integer and an end integer.
# Print all the numbers in the given range (inclusive) that are divisible by any of the numbers from 2 to 10.
# Use comprehensions for this problem.

# def is_divisible_by_2_10(num):
#     divisor = [num for divisor in range(2, 11) if num % divisor == 0]
#     return True if divisor else False
#
#
# start_range = int(input())
# end_range = int(input())
#
# print([number for number in range(start_range, end_range+1) if is_divisible_by_2_10(number)])

# Option 2 - without functions

start_range = int(input())
end_range = int(input())

print([number for number in range(start_range, end_range+1) if [d for d in range(2, 11) if number % d == 0]])
