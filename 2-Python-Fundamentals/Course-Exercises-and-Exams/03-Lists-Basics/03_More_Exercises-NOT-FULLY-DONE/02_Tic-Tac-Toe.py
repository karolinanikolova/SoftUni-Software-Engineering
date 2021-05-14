# 2.	Tic-Tac-Toe
# You will receive a field of a tic-tac-toe game in three lines containing numbers separated by a single space.
# Legend:
# •	0 - empty space
# •	1 - first player move
# •	2 - second player move
# Find out who the winner is. If the first player wins print "First player won",
# otherwise if the second player wins print "Second player won", otherwise print "Draw!"

first_line = input().split()
first_line_numbers = list(map(int, first_line))

second_line = input().split()
second_line_numbers = list(map(int, second_line))

third_line = input().split()
third_line_numbers = list(map(int, third_line))

is_first_player_winner = False
is_second_player_winner = False

# Check if any of the columns have a [1, 1, 1] or [2, 2, 2] combination
for index in range(0, 2):
    if first_line_numbers[index] == second_line_numbers[index] and first_line_numbers[index] == third_line_numbers[index]:
        if first_line_numbers[index] == 1:
            is_first_player_winner = True
        elif first_line_numbers[index] == 2:
            is_second_player_winner = True

# Check if any of the lines have a [1, 1, 1] or [2, 2, 2] combination
if first_line_numbers.count(first_line_numbers[0]) == len(first_line_numbers):
    if first_line_numbers[0] == 1:
        is_first_player_winner = True
    elif first_line_numbers[0] == 2:
        is_second_player_winner = True

if second_line_numbers.count(second_line_numbers[0]) == len(second_line_numbers):
    if second_line_numbers[0] == 1:
        is_first_player_winner = True
    elif second_line_numbers[0] == 2:
        is_second_player_winner = True

if third_line_numbers.count(third_line_numbers[0]) == len(third_line_numbers):
    if third_line_numbers[0] == 1:
        is_first_player_winner = True
    elif third_line_numbers[0] == 2:
        is_second_player_winner = True

# Check if any of the diagonals have a [1, 1, 1] or [2, 2, 2] combination
if first_line_numbers[2] == second_line_numbers[1] and first_line_numbers[2] == third_line_numbers[0]:
    if first_line_numbers[2] == 1:
        is_first_player_winner = True
    elif first_line_numbers[2] == 2:
        is_second_player_winner = True

if first_line_numbers[0] == second_line_numbers[1] and first_line_numbers[0] == third_line_numbers[2]:
    if first_line_numbers[0] == 1:
        is_first_player_winner = True
    elif first_line_numbers[0] == 2:
        is_second_player_winner = True

if is_first_player_winner:
    print('First player won')
elif is_second_player_winner:
    print('Second player won')
else:
    print('Draw!')