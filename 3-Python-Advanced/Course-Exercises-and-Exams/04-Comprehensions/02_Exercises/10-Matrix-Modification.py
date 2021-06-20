# 10.	Matrix Modification
# Write a program that reads a matrix from the console. On the first line, you will get the matrix's rows.
# On next rows lines, you will get elements for each column, separated with space. You will be receiving commands
# in the following format:
# •	Add {row} {col} {value} – Increase the number at the given coordinates with the value.
# •	Subtract {row} {col} {value} – Decrease the number at the given coordinates by the value.
# If the coordinate is invalid, you should print "Invalid coordinates". A coordinate is valid if both of the given
# indexes are in range [0; len() – 1].
# When you receive "END", you should print the matrix and stop the program.

rows = int(input())

matrix = [[int(el) for el in input().split()] for _ in range(rows)]

data = input()

while not data == "END":
    command, row, col, value = data.split()

    row = int(row)
    col = int(col)
    value = int(value)

    if row not in range(rows) or col not in range(len(matrix[0])):
        print('Invalid coordinates')
        data = input()
        continue

    if command == "Add":
        matrix[row][col] += value
    elif command == "Subtract":
        matrix[row][col] -= value

    data = input()

[print(*matrix[row]) for row in range(rows)]