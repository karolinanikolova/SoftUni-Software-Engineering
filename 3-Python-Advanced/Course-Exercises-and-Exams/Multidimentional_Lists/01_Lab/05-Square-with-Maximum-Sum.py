# 5.	Square with Maximum Sum
# Write a program that reads a matrix from the console. On first line you will get matrix sizes in format "{rows}, {columns}".
# On the next rows, you will get elements for each column separated with a ", ". Find the 2x2 top-left submatrix with
# biggest sum of its values. Print the matrix and the sum of its elements as shown in the examples.

rows, cols = [int(el) for el in input().split(', ')]

matrix = []

for row in range(rows):
    matrix.append(int(el) for el in input().split(', '))