# 5.	Snake Moves
# You are tasked to visualize a snake's zigzag path in a rectangular matrix with size N x M.
# The snake is represented by a string. It starts moving from the top-left corner to the right.
# When the snake reaches the end of the row, it slithers its way down to the next row and turns left.
# The moves are repeated to the very end. The first cell is filled with the first symbol of the snake,
# the second cell is filled with the second symbol, etc. The snake is as long as it takes to fill the path
# completely - if you reach the end of the string representing the snake, start again at the first symbol.
# After you fill the matrix with the snake's path, you should print it.

from collections import deque

rows, cols = [int(el) for el in input().split()]

snake = deque(input())

matrix = []

for row in range(rows):
    matrix.append([])
    for col in range(cols):
        first_character = snake.popleft()
        snake.append(first_character)
        matrix[row].append(first_character)

for row in range(rows):
    if not row % 2 == 0:
        matrix[row].reverse()
        print(''.join(matrix[row]))
    else:
        print(''.join(matrix[row]))
