# 7.	Chairs
# Write a program that receives names on the first line (separated by comma and space ", ") and number of chairs on
# the second line (an integer). Find all the ways to fit those people on the chairs. Print each combination on a separate line.
# Note: In the example below, "Peter, George" is same as "George, Peter", so we only print the first combination

# from itertools import combinations
#
# result = list(combinations(input().split(', '), int(input())))
#
# for x, y in result:
#     print(x, y, sep=', ')

# from math import factorial
#


def combinations(names, count, current_names=[]):
    if len(current_names) == count:
        print(*current_names, sep=', ')
        return

    for i in range(len(names)):
        current_names.append(names[i])

        combinations(names[i+1:], count, current_names)
        current_names.pop()


names = input().split(', ')
n = int(input())

combinations(names, n)