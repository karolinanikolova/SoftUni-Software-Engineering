# 3.	Primary Diagonal
# Write a program that finds the sum of matrix primary diagonal. On the first line, you will receive an integer N –
# the size of the square matrix. The next N lines holds the values for every row – N numbers, separated by a single space

N = int(input())

rows = N
cols = N

matrix = []
sum_diagonal = 0

for row in range(rows):
    matrix.append([int(el) for el in input().split()])
    sum_diagonal += matrix[row][row]

print(sum_diagonal)