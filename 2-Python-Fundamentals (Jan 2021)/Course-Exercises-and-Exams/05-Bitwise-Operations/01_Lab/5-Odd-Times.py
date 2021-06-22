# 5.	* Odd Times
# You are given an array of positive integers in a single line, separated by a space (' ').
# All numbers occur even number of times except one number which occurs odd number of times. Find it, using only bitwise operations.

array = input().split()

result = 0

for element in array:
    result = result ^ int(element)

print(result)
