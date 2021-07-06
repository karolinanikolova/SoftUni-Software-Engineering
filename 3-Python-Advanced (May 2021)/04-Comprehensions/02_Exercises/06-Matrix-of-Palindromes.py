# 6.	Matrix of Palindromes
# Write a program to generate the following matrix of palindromes of 3 letters with r rows and c columns
# like the one in the examples below.
# •	Rows define the first and the last letter: row 0  'a', row 1  'b', row 2  'c', …
# •	Columns + rows define the middle letter:
# o	column 0, row 0  'a', column 1, row 0  'b', column 2, row 0  'c', …
# o	column 0, row 1  'b', column 1, row 1  'c', column 2, row 1  'd', …

# Option 1 - without saving to matrix and directly printing
rows, cols = [int(el) for el in input().split()]

[print(*[f"{chr(97+row) + chr(97+row+col) + chr(97+row)}" for col in range(cols)]) for row in range(rows)]

# # Option 2 - with saving to matrix
# rows, cols = [int(el) for el in input().split()]
#
# matrix = [[] for row in range(rows)]
#
# [[matrix[row].append(chr(97+row) + chr(97+row+col) + chr(97+row)) for col in range(cols)] for row in range(rows)]
#
# [print(*matrix[row]) for row in range(rows)]

# # Option 3 - without comprehension
#
# rows, cols = [int(el) for el in input().split()]
#
# matrix = []
#
# for row in range(rows):
#     matrix.append([])
#
#     for col in range(cols):
#         string = chr(97+row) + chr(97+row+col) + chr(97+row)
#         matrix[row].append(string)
#
# for row in range(rows):
#     print(*matrix[row])