# 2.	Sum Matrix Columns
# Write a program that reads a matrix from the console and prints the sum for each column on separate lines.
# On the first line, you will get matrix sizes in format "{rows}, {columns}".
# On the next rows, you will get elements for each column separated with a single space.

# rows, cols = [int(el) for el in input().split(', ')]
#
# matrix = []
# sum_cols = []
#
# for row in range(rows):
#     matrix.append([int(el) for el in input().split()])
#
# for col in range(cols):
#     sum_cols.extend([0])
#     for row in range(rows):
#         sum_cols[col] += matrix[row][col]
#
# print("\n".join([str(el) for el in sum_cols]))

rows, cols = [int(el) for el in input().split(', ')]

matrix = []

for row in range(rows):
    matrix.append([int(el) for el in input().split()])

for col in range(cols):
    sum_col = 0
    for row in range(rows):
        sum_col += matrix[row][col]
    print(sum_col)
