# 6.	Survival of the Biggest
# Write a program that receives a list of integer numbers and a number n. The number n represents the amount of
# numbers to remove from the list. You should remove the smallest ones.

import sys

numbers = input().split()
numbers = list(map(int, numbers))

n = int(input())

for _ in range(n):
    min_element = numbers[0]
    index_of_min_element = 0
    for i in range(len(numbers)):
        if numbers[i] < min_element:
            min_element = numbers[i]
            index_of_min_element = i

    numbers.remove(numbers[index_of_min_element])

print(numbers)