# 3.	Supermarket
# Write a program which reads an input consisting of a name and adds it to a queue until "End" is received.
# If you receive "Paid", print every customer's name, and empty the queue.
# Otherwise, you will receive a client and you should add them to the queue.
# When you receive "End", you must print the count of the remaining people in the queue in the format:
# "{count} people remaining.".

from collections import deque

command = input()

queue = deque()

while not command == "End":

    if command == "Paid":
        while len(queue) > 0:
            print(queue.popleft())
    else:
        queue.append(command)

    command = input()

print(f"{len(queue)} people remaining.")