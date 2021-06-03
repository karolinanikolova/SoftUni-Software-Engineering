# 5.	Hot Potato
# Hot Potato is a game in which children form a circle and start tossing a hot potato.
# The counting starts with the first kid. Every nth toss the child who is holding the potato leaves the game.
# When a kid leaves the game, it passes the potato to the next kid.
# This continues until there is only one kid left.
# Create a program that simulates the game of Hot Potato. On the first line you will receive names of kids,
# separated by a single space. On the second line you will receive the nth toss (integer)
# in which a child leaves the game.
# Print every kid which is removed from the circle in the format "Removed {kid}".
# In the end, print the only kid left in the format "Last is {kid}".

from collections import deque

kids = deque(input().split())

n = int(input())

count = 1

while len(kids) > 1:
    if count == n:
        print(f"Removed {kids.popleft()}")
        count = 1
        continue
    else:
        kids.append(kids.popleft())
        count += 1

print(f"Last is {kids.popleft()}")

# # With deque method
#
# from collections import deque
#
# kids = deque(input().split())
#
# n = int(input())
# 
# while len(kids) > 1:
#     kids.rotate(-n+1)
#     print(f"Removed {kids.popleft()}")
#
# print(f"Last is {kids.popleft()}")