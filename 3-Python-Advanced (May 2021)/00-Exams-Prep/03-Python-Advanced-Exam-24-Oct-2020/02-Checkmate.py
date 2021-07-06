def capture(matrix, r, c, size):
    possible_moves = [(x, y) for x in range(-1, 2) for y in range(-1, 2)]
    for move in possible_moves:
        first_step_row = r + move[0]
        first_step_col = c + move[1]
        next_row = first_step_row
        next_col = first_step_col
        while 0 <= next_row < size and 0 <= next_col < size:
            if matrix[next_row][next_col] == "K":
                return True, [r, c]
            elif matrix[next_row][next_col] == "Q":
                break
            next_row += move[0]
            next_col += move[1]
    return False, [r, c]


board_size = 8
board = [input().split() for row in range(board_size)]
queens = []
for row in range(board_size):
    for col in range(board_size):
        if board[row][col] == "Q":
            captured_king, position = capture(board, row, col, board_size)
            if captured_king:
                queens.append(position)
if queens:
    [print(pos) for pos in queens]
else:
    print("The king is safe!")



# def check_to_kill_king_on_row(matrix, row):
#     row_to_check = matrix[row]
#     if 'K' not in row_to_check:
#         return False
#     king_position = row_to_check.index('K')
#     if col < king_position:
#         if 'Q' in row_to_check[col+1:king_position]:
#             return False
#     else:
#         if 'Q' in row_to_check[king_position+1:col]:
#             return False
#     return True
#
#
# def check_to_kill_king_on_col(matrix, row, col):
#     column_to_check = [row[col] for row in matrix]
#     if 'K' not in column_to_check:
#         return False
#     king_position = column_to_check.index('K')
#     if row < king_position:
#         if 'Q' in column_to_check[row+1:king_position]:
#             return False
#     else:
#         if 'Q' in column_to_check[king_position+1:row]:
#             return False
#     return True
#
#
# def check_to_kill_king_on_first_diagonal(matrix, row, col):
#     current_queen = matrix[row][col]
#     first_diagonal_to_check = [current_queen]
#
#     current_row = row
#     current_col = col
#     while current_row in range(1, 8) and current_col in range(1, 8):
#         current_row -= 1
#         current_col -= 1
#         try:
#             first_diagonal_to_check.insert(0, matrix[current_row][current_col])
#         except IndexError:
#             pass
#
#     current_row = row
#     current_col = col
#     while current_row in range(0, 7) and current_row in range(0, 7):
#         current_row += 1
#         current_col += 1
#         try:
#             first_diagonal_to_check.append(matrix[current_row][current_col])
#         except IndexError:
#             pass
#
#     if 'K' not in first_diagonal_to_check:
#         return False
#
#     king_position = first_diagonal_to_check.index('K')
#     if col < king_position:
#         if 'Q' in first_diagonal_to_check[col+1:king_position]:
#             return False
#     else:
#         if 'Q' in first_diagonal_to_check[king_position+1:col]:
#             return False
#     return True
#
#
# def check_to_kill_king_on_second_diagonal(matrix, row, col):
#     current_queen = matrix[row][col]
#     second_diagonal_to_check = [current_queen]
#
#     current_row = row
#     current_col = col
#     while current_row in range(0, 7) and current_col in range(1, 8):
#         current_row += 1
#         current_col -= 1
#         try:
#             second_diagonal_to_check.insert(0, matrix[current_row][current_col])
#         except IndexError:
#             pass
#
#     current_row = row
#     current_col = col
#     while current_row in range(1, 8) and current_col in range(0, 7):
#         current_row -= 1
#         current_col += 1
#         try:
#             second_diagonal_to_check.append(matrix[current_row][current_col])
#         except IndexError:
#             pass
#     if 'K' not in second_diagonal_to_check:
#         return False
#
#     king_position = second_diagonal_to_check.index('K')
#     if col < king_position:
#         if 'Q' in second_diagonal_to_check[col+1:king_position]:
#             return False
#     else:
#         if 'Q' in second_diagonal_to_check[king_position+1:col]:
#             return False
#     return True
#
# rows = 8
# cols = rows
#
# matrix = []
#
# [matrix.append(input().split()) for _ in range(rows)]
#
# killer_queens_positions = []
#
# for row in range(rows):
#     for col in range(cols):
#         try:
#             if matrix[row][col] == 'Q':
#                 if check_to_kill_king_on_row(matrix, row):
#                     killer_queens_positions.append([row, col])
#                 if check_to_kill_king_on_col(matrix, row, col):
#                     killer_queens_positions.append([row, col])
#                 if check_to_kill_king_on_first_diagonal(matrix, row, col):
#                     killer_queens_positions.append([row, col])
#                 if check_to_kill_king_on_second_diagonal(matrix, row, col):
#                     killer_queens_positions.append([row, col])
#         except IndexError:
#             pass
#
# if killer_queens_positions:
#     print(*killer_queens_positions, sep='\n')
# else:
#     print('The king is safe!')
#
