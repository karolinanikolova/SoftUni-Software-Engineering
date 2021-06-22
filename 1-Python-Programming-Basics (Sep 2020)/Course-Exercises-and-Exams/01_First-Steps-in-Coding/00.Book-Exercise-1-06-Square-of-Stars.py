# a square of asterisks
# Write a Python console program that reads an integer N from the console and prints a square of N asterisks on the console , as in the examples below.

N = int(input())

for i in range(1, N+1):
    if (i == 1 or i == N):
        print('*' * N)
    else:
        print('*' + ' ' * (N - 2) + '*')
