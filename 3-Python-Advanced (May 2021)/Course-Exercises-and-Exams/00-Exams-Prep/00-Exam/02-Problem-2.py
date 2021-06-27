# Problem 2
# You are participating in a Firearm course. It is a training day at the shooting range.
# You will be given a matrix with 5 rows and 5 columns. It is a shotgun range represented as some symbols separated
# by a single space:
# •	Your position is marked with the symbol "A"
# •	Targets marked with symbol "x"
# •	All of the empty positions will be marked with "."
# After the field state you will be given an integer representing the number of commands you are going to receive.
# The possible commands are:
# •	"move {right/left/up/down} {steps}" – you should move in the given direction with the given steps.
# You can move only if the field you want to step on is marked with ".".
# •	"shoot {right/left/up/down}" – you should shoot in the given direction (from your current position without moving).
# Beware that there might be targets that stand in the way of other targets and you cannot reach them -
# you can shoot only the nearest target. When you have shot a target, the field become empty position (".").
# Validate the positions since they can be outside the field.
# Keep track of all the shot targets:
# •	If at any point there are no targets left, end the program and print: "Training completed! All {count_targets} targets hit.".
# •	If, after you perform all the commands, there are some targets left print: "Training not completed! {count_left_targets} targets left.".
# Finally, print the index positions of the targets that you hit as shown in the examples.

def move(matrix, row, col, movement, move_count):
    new_position_row = row + movement[0] * move_count
    new_position_col = col + movement[1] * move_count

    if new_position_row not in range(5) or new_position_col not in range(5):
        new_position_row = row
        new_position_col = col
        return False, [new_position_row, new_position_col]

    if matrix[new_position_row][new_position_col] != '.':
        new_position_row = row
        new_position_col = col
        return False, [new_position_row, new_position_col]

    # temp_row = row
    # temp_col = col
    #
    # for _ in range(move_count):
    #     temp_row += movement[0]
    #     temp_col += movement[1]
    #     if matrix[temp_row][temp_col] != '.':
    #         new_position_row = row
    #         new_position_col = col
    #         return False, [new_position_row, new_position_col]

    return True, [new_position_row, new_position_col]

def shoot(matrix, row, col, movement):
    current_position_row = row
    current_position_col = col

    while current_position_row in range(5) and current_position_col in range(5):
        current_position_row += movement[0]
        current_position_col += movement[1]
        # try:
        #     if matrix[current_position_row][current_position_col] == '.':
        #         continue
        #     elif matrix[current_position_row][current_position_col] == 'x':
        #         return True, [current_position_row, current_position_col]
        # except IndexError:
        #     return False, [current_position_row - movement[0], current_position_col - movement[1]]
        if current_position_row in range(5) and current_position_col in range(5):
            if matrix[current_position_row][current_position_col] == '.':
                continue
            elif matrix[current_position_row][current_position_col] == 'x':
                return True, [current_position_row, current_position_col]
        else:
            return False, [current_position_row, current_position_col]
    return False, [current_position_row, current_position_col]


rows = 5
cols = 5

matrix = [input().split() for _ in range(rows)]
N = int(input())

shot_targets = []
count_targets = 0

for row in range(rows):
    for col in range(cols):
        if matrix[row][col] == 'x':
            count_targets += 1

possible_moves_dict = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}

for _ in range(N):
    if count_targets == 0:
        break
    command_data = input().split()
    command = command_data[0]
    movement = command_data[1]
    movement = possible_moves_dict[movement]

    is_turn_done = False

    for row in range(rows):
        if is_turn_done:
            break

        for col in range(cols):
            if matrix[row][col] == 'A':

                if command == "move":
                    move_count = int(command_data[2])
                    has_player_moved, new_position = move(matrix, row, col, movement, move_count)
                    if has_player_moved:
                        matrix[new_position[0]][new_position[1]] = 'A'
                        matrix[row][col] = '.'
                elif command == "shoot":
                    has_target_been_shot, shot_target_position = shoot(matrix, row, col, movement)
                    if has_target_been_shot:
                        matrix[shot_target_position[0]][shot_target_position[1]] = '.'
                        count_targets -= 1
                        shot_targets.append(shot_target_position)
                is_turn_done = True

            if is_turn_done:
                break

if count_targets == 0:
    print(f"Training completed! All {len(shot_targets)} targets hit.")
else:
    print(f"Training not completed! {count_targets} targets left.")

print(*shot_targets, sep='\n')

# for row in matrix:
#     print(*row, sep=' ')



