# 2.	Sets of Elements
# Write a program that prints a set of elements. On the first line, you will receive two numbers - n and m,
# which represent the lengths of two separate sets. On the next n + m lines you will receive n numbers,
# which are the numbers in the first set, and m numbers, which are in the second set.
# Find all the unique elements that appear in both and print them on separate lines (the order does not matter).
# For example:
# Set with length n = 4: {1, 3, 5, 7}
# Set with length m = 3: {3, 4, 5}
# Set that contains all the elements that repeat in both sets -> {3, 5}

n, m = input().split()

n = int(n)
m = int(m)

first_set = set()
second_set = set()

for _ in range(n):
    first_set.add(input())

for _ in range(m):
    second_set.add(input())

intersection = first_set.intersection(second_set)

[print(el) for el in intersection]