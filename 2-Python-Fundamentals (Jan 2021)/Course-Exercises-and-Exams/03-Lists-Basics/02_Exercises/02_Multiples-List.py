# 2.	Multiples List
# Write a program that receives two numbers (factor and count) and creates a list with length of the given count
# and contains only elements that are multiples of the given factor.

factor = int(input())
count = int(input())

list = []

for counter in range(1, count+1):
    list.append(factor * counter)

print(list)
