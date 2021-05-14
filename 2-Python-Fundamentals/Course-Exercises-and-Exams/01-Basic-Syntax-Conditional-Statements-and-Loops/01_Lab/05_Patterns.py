# 5.	Patterns
# Write a program to create the following pattern:
# You will receive a number that represents the highest number of stars.

n = int(input())

for row in range(1, n + 1):
    print(row * '*')

for row in range(n - 1, 0, -1):
    print(row * '*')