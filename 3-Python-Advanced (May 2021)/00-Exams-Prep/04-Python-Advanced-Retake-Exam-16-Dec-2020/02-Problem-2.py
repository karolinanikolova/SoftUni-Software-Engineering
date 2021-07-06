# Problem 2
#
# You will be given a string. Then, you will be given an integer N for the size of the field with square shape.
# On the next N lines, you will receive the rows of the field. The player will be placed on a random position, marked with "P".
# On random positions there will be letters. All of the empty positions will be marked with "-".
# Each turn you will be given commands for the player’s movement. If he moves to a letter, he consumes it,
# concatеnates it to the initial string and the letter disappears from the field. If he tries to move outside of the field,
# he is punished - he loses the last letter in the string, if there are any, and the player’s position is not changed.
# At the end print all letters and the field.

def move_player(matrix, row, col, move):
    new_position_row = row + move[0]
    new_position_col = col + move[1]

    if new_position_row not in range(N) or new_position_col not in range(N):
        new_position_row = row
        new_position_col = col
        return False, [new_position_row, new_position_col]
    return True, [new_position_row, new_position_col]


string = input()
N = int(input())

matrix = [list(input()) for _ in range(N)]

turns = int(input())

possible_commands_dict = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}

while not turns == 0:
    command = input()

    move = possible_commands_dict[command]
    is_turn_done = False

    for row in range(N):
        if is_turn_done:
            break

        for col in range(N):
            if matrix[row][col] == 'P':
                has_player_moved, new_position = move_player(matrix, row, col, move)
                if not has_player_moved:
                    if string:
                        string = string[:-1]
                else:
                    consumed_character = matrix[new_position[0]][new_position[1]]
                    if consumed_character.isalpha():
                        string += consumed_character
                    matrix[new_position[0]][new_position[1]] = 'P'
                    matrix[row][col] = '-'

                is_turn_done = True

            if is_turn_done:
                break

    turns -= 1

print(string)
for row in matrix:
    print(*row, sep='')


# # Option 2
# def read_matrix_and_start_position(square_size):
#     square = []
#     start_row_index = None
#     start_column_index = None
#     for row_index in range(square_size):
#         current_row = list(input())
#         if "P" in current_row:
#             start_row_index = row_index
#             start_column_index = current_row.index("P")
#         square.append(current_row)
#     return square, start_row_index, start_column_index
#
#
# def get_player_next_position(player_row_idx, player_column_idx, current_direction):
#     if current_direction == "up":
#         player_row_idx -= 1
#     elif current_direction == "down":
#         player_row_idx += 1
#     elif current_direction == "left":
#         player_column_idx -= 1
#     elif current_direction == "right":
#         player_column_idx += 1
#     return player_row_idx, player_column_idx
#
#
# def check_if_player_next_position_is_inside(square_size, next_row_idx, next_column_idx):
#     if 0 <= next_row_idx < square_size and 0 <= next_column_idx < square_size:
#         return True
#     return False
#
#
# def move_player(square, player_row_idx, player_column_idx, string, next_row_idx, next_column_idx):
#     if square[next_row_idx][next_column_idx].isalpha():
#         string += square[next_row_idx][next_column_idx]
#     square[next_row_idx][next_column_idx] = "P"
#     square[player_row_idx][player_column_idx] = "-"
#     return square, string
#
#
# def remove_last_letter(string):
#     if string:
#         return string[:-1]
#     return string
#
#
# def print_matrix_and_string_final_state(square, string):
#     print(string)
#     [print(*row, sep="") for row in square]
#
#
# initial_string = input()
#
# matrix_size = int(input())
#
# matrix, player_row_index, player_column_index = read_matrix_and_start_position(matrix_size)
#
# moves_count = int(input())
#
# for move in range(moves_count):
#     direction = input()
#
#     next_row_index, next_column_index = get_player_next_position(player_row_index, player_column_index, direction)
#
#     if check_if_player_next_position_is_inside(matrix_size, next_row_index, next_column_index):
#         matrix, initial_string = move_player(matrix, player_row_index, player_column_index, initial_string,
#                                              next_row_index, next_column_index)
#         player_row_index = next_row_index
#         player_column_index = next_column_index
#     else:
#         initial_string = remove_last_letter(initial_string)
#
# print_matrix_and_string_final_state(matrix, initial_string)