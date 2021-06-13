# 1.	Sum Matrix Elements
# Write a program that reads a matrix from the console and prints:
# •	The sum of all matrix elements
# •	The matrix itself
# On the first line, you will receive the matrix sizes in format "{rows}, {columns}".
# On the next rows, you will get elements for each column separated with a ", ".

rows, cols = [int(el) for el in input().split(', ')]

matrix = []
sum_matrix = 0

for row in range(rows):
    matrix.append([int(el) for el in input().split(', ')])
    sum_matrix += sum(matrix[row])

# sum_matrix = sum([sum(row) for row in matrix])

print(sum_matrix)
print(matrix)