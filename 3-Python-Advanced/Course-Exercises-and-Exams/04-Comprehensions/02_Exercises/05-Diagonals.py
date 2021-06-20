# 5.	Diagonals
# Using a nested list comprehension, write a program that reads NxN matrix, finds its diagonals,
# prints them and their sum as shown below.

rows = int(input())
cols = rows

matrix = [[int(el) for el in input().split(', ')] for _ in range(rows)]

first_diagonal = [matrix[row][row] for row in range(rows)]
second_diagonal = [matrix[row][cols - row - 1] for row in range(rows)]

print(f"First diagonal: {', '.join([str(el) for el in first_diagonal])}. Sum: {sum(first_diagonal)}")
print(f"Second diagonal: {', '.join([str(el) for el in second_diagonal])}. Sum: {sum(second_diagonal)}")