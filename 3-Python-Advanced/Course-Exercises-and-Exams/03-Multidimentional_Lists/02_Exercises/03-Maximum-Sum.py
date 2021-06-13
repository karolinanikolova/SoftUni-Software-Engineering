# 3.	Maximal Sum
# Write a program that reads a rectangular matrix's dimensions and finds the 3x3 square that has maximal sum of its elements.

def init_matrix():
    matrix = []

    for row in range(rows):
        matrix.append([int(el) for el in input().split()])

    return matrix


def three_by_three_matrix_and_its_sum(row, col, matrix):
    three_by_three_matrix = [[matrix[row][col], matrix[row][col + 1], matrix[row][col + 2]],
                                 [matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2]],
                                    [matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]]]
    sum_three_by_three_matrix = sum(sum(row) for row in three_by_three_matrix)

    return three_by_three_matrix, sum_three_by_three_matrix


rows, cols = [int(el) for el in input().split()]

matrix = init_matrix()

max_sum = 0
max_matrix = 0

for row_index in range(rows-2):
    for col_index in range(cols-2):
        current_matrix, current_sum = three_by_three_matrix_and_its_sum(row_index, col_index, matrix)
        if current_sum >= max_sum:
            max_sum = current_sum
            max_matrix = current_matrix

print(f"Sum = {max_sum}")
for row in max_matrix:
    print(' '.join([str(el) for el in row]))