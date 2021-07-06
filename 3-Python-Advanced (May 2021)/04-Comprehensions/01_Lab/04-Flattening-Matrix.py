# 4.	Flattening Matrix
# Write a program that receives a matrix and prints the flattened version of it (a list with all the values).
# For example, the flattened list of the matrix: [[1, 2], [3, 4]] will be [1, 2, 3, 4].
# On the first line, you will receive the matrix sizes in format "{rows}, {columns}".
# On the next rows, you will get elements for each column separated with a ", ".

# n = int(input())
#
# nums = []
#
# for _ in range(n):
#     nums.extend([int(el) for el in input().split(', ')])
#
# print(nums)

# Option 2 - with matrix and

n = int(input())

matrix = [[int(el) for el in input().split(', ')] for _ in range(n)]

flat_nums = [num for sublist in matrix for num in sublist]

print(flat_nums)