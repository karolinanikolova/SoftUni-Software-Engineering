# 5.	Can't Sleep? Count Sheep
# If you can't sleep, just count sheep! Given a non-negative integer, 3 for example, return a string with a murmur: ' \
#           '"1 sheep...2 sheep...3 sheep..." Input will always be valid, i.e. no negative integers.

number = int(input())

for count in range(1, number + 1):
    print(f'{count} sheep...', end='')
