# 4.	Water Dispenser
# Write a program which keeps track of people who are getting water from a dispenser and the
# amount of water left at the end.
# On the first line you will receive the starting quantity of water in a dispenser.
# Then on the next few lines you will be given the names of some people who want to get water
# (each on separate line) until you receive the command "Start". Add those people in a queue.
# Finally, you will receive some commands until the command "End":
# -	{liters} - Litters that the current person in the queue wants to get.
# Check if there is enough water in the dispenser for that person.
# o	If there is enough water, print "{person_name} got water" and remove him/her from the queue.
# o	Otherwise, print "{person} must wait" and remove the person from the queue without reducing
# the water in the dispenser.
# -	refill {liters} - add the given litters in the dispenser.
# At the end print how many litters of water have left in the format: "{left_liters} liters left".

from collections import deque

water = int(input())

queue = deque()

command = input()

while not command == "Start":
    queue.append(command)

    command = input()

command = input()

while not command == "End":
    if command.startswith("refill"):
        liters = int(command.split()[-1])
        water += liters
    else:
        liters = int(command)
        if liters <= water:
            print(f"{queue.popleft()} got water")
            water -= liters
        else:
            print(f"{queue.popleft()} must wait")

    command = input()

print(f"{water} liters left")