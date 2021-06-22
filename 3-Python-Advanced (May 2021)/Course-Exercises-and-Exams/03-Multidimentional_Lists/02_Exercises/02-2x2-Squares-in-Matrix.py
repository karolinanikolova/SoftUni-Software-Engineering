# 2.	2 X 2 Squares in Matrix
# Find the count of 2 x 2 squares with equal chars in a matrix.

# rows, cols = [int(el) for el in input().split()]
#
# matrix = []
#
# count = 0
#
# for row in range(rows):
#     matrix.append(input().split())
#
# for row in range(0, rows - 1):
#     for col in range(0, cols - 1):
#         if matrix[row][col] == matrix[row][col + 1] and matrix[row][col] == matrix[row + 1][col] and matrix[row][col] == \
#                 matrix[row + 1][col + 1]:
#             count += 1
#
# print(count)

def init_matrix():
    matrix = []

    for row in range(rows):
        matrix.append(input().split())

    return matrix

def check_if_elements_equal(row, col, matrix):
    if matrix[row][col] == matrix[row][col + 1] and matrix[row][col] == matrix[row + 1][col] and matrix[row][col] == \
            matrix[row + 1][col + 1]:
        return True


rows, cols = [int(el) for el in input().split()]

matrix = init_matrix()

count = 0

for row_index in range(rows-1):
    for col_index in range(cols-1):
        if check_if_elements_equal(row_index, col_index, matrix):
            count += 1

print(count)

