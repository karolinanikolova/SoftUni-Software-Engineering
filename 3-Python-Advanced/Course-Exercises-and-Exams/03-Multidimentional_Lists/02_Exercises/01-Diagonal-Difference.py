# 1.	Diagonal Difference
# Write a program that finds the difference between the sums of the square matrix diagonals (absolute value).

N = int(input())

rows = N
cols = N

matrix = []
sum_primary = 0
sum_secondary = 0
counter = -1

for row in range(rows):
    matrix.append([int(el) for el in input().split()])
    sum_primary += matrix[row][row]
    sum_secondary += matrix[row][counter]

    counter -= 1

print(abs(sum_primary-sum_secondary))