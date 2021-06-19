# 3.	Even Matrix
# Write a program that receives a matrix of numbers and prints a new one only with the numbers that are even.
# Use nested comprehension for that problem.
# On the first line, you will receive the matrix sizes in format "{rows}, {columns}".
# On the next rows, you will get elements for each column separated with a ", ".

rows = int(input())

matrix = [[int(el) for el in input().split(', ') if int(el) % 2 == 0] for _ in range(rows)]

print(matrix)

# # Option 2
# rows = int(input())
#
# matrix = [[int(el) for el in input().split(', ')] for _ in range(rows)]
#
# even_matrix = [[num for num in sublist if num % 2 == 0] for sublist in matrix]
#
# print(even_matrix)