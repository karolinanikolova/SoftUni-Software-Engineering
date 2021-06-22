# 6.	Knight Game
# Chess is the oldest game, but it is still popular these days. For this task, we will use only one chess piece -
# the Knight.
# A chess knight has 8 possible moves it can make, as illustrated. It can move to the nearest square but not on the
# same row, column, or diagonal. (Foe example it can move two squares horizontally, then one square vertically,
# or it can move one square horizontally then two squares vertically - i.e. in an "L" pattern.)
# The knight game is played on a board with dimensions N x N.
# You will receive a board with "K" for knights and "0" for empty cells. Your task is to remove knights until there
# are no knights left that can attack one another.

N = int(input())

matrix = []

for row in range(N):
    matrix.append(list(input()))

def is_valid_bound(row, col):
    if 0 <= row < N and 0 <= col < N:
        return True
    return False

def calculate_kills(matrix, row, col):
    kills = 0
    rows = [-2, -2, -1, -1, 2, 2, 1, 1]
    cols = [-1, 1, -2, 2, -1, 1, -2, 2]

    for index in range(len(rows)):
        potential_row = row+rows[index]
        potential_col = col+cols[index]
        if is_valid_bound(potential_row, potential_col):
            potential_position = matrix[potential_row][potential_col]

            if potential_position == 'K':
                kills+=1

    return kills

removed_counter = 0

while True:
    max_kills = 0
    killer_position = []

    for row in range(N):
        for col in range(N):
            if matrix[row][col] == 'K':
                kills = calculate_kills(matrix, row, col)

                if max_kills < kills:
                    max_kills = kills
                    killer_position = [row, col]

    if killer_position:
        matrix[killer_position[0]][killer_position[1]] = '0'
        removed_counter += 1
    else:
        break

print(removed_counter)