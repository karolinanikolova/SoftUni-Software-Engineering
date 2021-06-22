#  квадрат от звездички
# Да се начертае на конзолата квадрат от N x N звездички:

N = int(input())

for row in range(1, N + 1):
    for col in range(1, N + 1):
        print('*', end = ' ')
    print()