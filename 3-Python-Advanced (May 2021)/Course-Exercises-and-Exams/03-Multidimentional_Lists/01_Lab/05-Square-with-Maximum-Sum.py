# 5.	Square with Maximum Sum
# Write a program that reads a matrix from the console. On first line you will get matrix sizes in format "{rows}, {columns}".
# On the next rows, you will get elements for each column separated with a ", ". Find the 2x2 top-left submatrix with
# biggest sum of its values. Print the matrix and the sum of its elements as shown in the examples.

# rows, cols = [int(el) for el in input().split(', ')]
#
# matrix = []
#
# for row in range(rows):
#     matrix.append([int(el) for el in input().split(', ')])
#
# two_by_two_matrix_max = []
# max_sum = 0
#
# for row in range(rows-1):
#     for col in range(cols-1):
#         current_two_by_two_matrix = [[matrix[row][col], matrix[row][col + 1]],
#                                      [matrix[row + 1][col], matrix[row + 1][col + 1]]]
#         sum_current_two_by_two_matrix = sum(sum(row) for row in current_two_by_two_matrix)
#         if sum_current_two_by_two_matrix > max_sum:
#             max_sum = sum_current_two_by_two_matrix
#             two_by_two_matrix_max = current_two_by_two_matrix
#
# for i in range(len(two_by_two_matrix_max)):
#     for j in range(len(two_by_two_matrix_max[i])):
#         print(two_by_two_matrix_max[i][j], end=" ")
#     print()
#
# print(max_sum)
#

rows, cols = [int(el) for el in input().split(', ')]

matrix = []

for row in range(rows):
    matrix.append([int(el) for el in input().split(', ')])

max_sum = 0
position = None

for row in range(rows-1, 0, -1):
    for col in range(cols-1, 0, -1):
        current_sum = matrix[row][col] + matrix[row][col-1] + matrix[row-1][col] + matrix[row-1][col-1]
        if current_sum >= max_sum:
            max_sum = current_sum
            position = (row, col)

row, col = position

print(matrix[row-1][col-1], matrix[row-1][col])
print(matrix[row][col-1], matrix[row][col])
print(max_sum)