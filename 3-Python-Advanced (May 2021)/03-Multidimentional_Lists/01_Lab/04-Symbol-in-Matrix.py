# 4.	Symbol in Matrix
# Write a program that reads a number - N, representing the rows and columns of a matrix.
# On the next N lines, you will receive rows of the matrix. Each row consists of ASCII characters.
# After that, you will receive a symbol. Find the first occurrence of that symbol in the matrix and
# print its position in the format: "({row}, {col})". You should start searching from the top left.
# If there is no such symbol print an error message "{symbol} does not occur in the matrix"

N = int(input())

rows = N
cols = N

matrix = []
is_symbol_in_matrix = False

for row in range(rows):
    matrix.append(list(input()))

symbol = input()

for col in range(cols):
    for row in range(rows):
        if matrix[row][col] == symbol:
            print(f"({row}, {col})")
            is_symbol_in_matrix = True
            break
    if is_symbol_in_matrix:
        break


if not is_symbol_in_matrix:
    print(f"{symbol} does not occur in the matrix")