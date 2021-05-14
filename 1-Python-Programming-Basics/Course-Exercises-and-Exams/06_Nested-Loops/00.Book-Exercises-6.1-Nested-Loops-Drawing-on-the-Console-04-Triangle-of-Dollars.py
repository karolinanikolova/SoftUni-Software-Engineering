# триъгълник от долари
# Да се напише програма, която въвежда число n и печата триъгълник от долари.

n = int(input())

for row in range(1, n + 1):
    for col in range(1, row + 1):
        print('$', end = ' ')
    print()