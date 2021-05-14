# ромбче от звездички
# Да се напише програма, която въвежда цяло положително число n и печата ромбче от звездички с размер N.

N = int(input())

for row in range(1, N + 1):
    for col in range(1, (N - row) + 1):
        print(' ', end = '')
    print('* ' * row, end = '')
    print()

for row in range(N - 1, 0, -1):
    for col in range((N - row) + 1, 1, -1):
        print(' ', end = '')
    print('* ' * row, end = '')
    print()

# for row in range(N - 1, 0, -1):
#     print('P' * (N - row) + '*P' * row + '' * (N - row))