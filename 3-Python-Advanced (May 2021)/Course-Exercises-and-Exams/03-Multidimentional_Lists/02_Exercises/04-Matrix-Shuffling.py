# 4.	Matrix Shuffling
# Write a program that reads a matrix, from the console and perform certain operations with its elements.
# User input is provided in a similar way like in the problems above - first you read the dimensions and then the data.
# Your program should receive commands in format: "swap {row1} {col1} {row2} {col2}" where row1, row2, col1, col2
# are coordinates in the matrix. A valid command starts with the "swap" keyword along with four valid
# coordinates (no more, no less).
# •	If the command is valid, you should swap the values at the given indexes and print the matrix at each step
# (thus you will be able to check if the operation was performed correctly).
# •	If the command is not valid (does not contain the keyword "swap", has fewer or more coordinates entered or the
# given coordinates do not exist), print "Invalid input!" and move on to the next command.
# Your program should finish when the string "END" is entered.

def init_matrix(rows, cols):

    matrix = []

    for row in range(rows):
        matrix.append(input().split())

    return matrix


def check_if_input_valid(index_1, index_2, index_3, index_4, rows, cols):
    if command[0] == "swap" and index_1 in range(max(rows, cols)) and index_2 in range(max(rows, cols)) and \
            index_3 in range(max(rows, cols)) and index_4 in range(max(rows, cols)):
        return True
    return False


rows, cols = [int(el) for el in input().split()]

matrix = init_matrix(rows, cols)

command = input()

while not command == "END":
    command = command.split()
    if len(command) == 5:
        index_1 = int(command[1])
        index_2 = int(command[2])
        index_3 = int(command[3])
        index_4 = int(command[4])
        if check_if_input_valid(index_1, index_2, index_3, index_4, rows, cols):
            matrix[index_1][index_2], matrix[index_3][index_4] = matrix[index_3][index_4], matrix[index_1][index_2]
            for row in matrix:
                print(' '.join(row))
        else:
            print('Invalid input!')
    else:
        print('Invalid input!')

    command = input()
