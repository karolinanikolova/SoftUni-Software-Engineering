# 1.	Trains
# You will receive how many wagons the train has.
# Create a list with that length with all zeros. Until you receive the command "End", you get some of the following commands:
# •	add {people} -> adds the people in the last wagon
# •	insert {index} {people} -> adds the people at the given wagon
# •	leave {index} {people} -> removes the people from the wagon
# After you receive the "End" command print the train

n_wagons = int(input())

wagons = n_wagons * [0]

command = input()

while not command == 'End':
    command = command.split()
    action = command[0]

    if action == 'add':
        people_to_add = int(command[1])
        wagons[-1] += people_to_add
    if action == 'insert':
        index = int(command[1])
        people_to_add = int(command[2])
        wagons[index] += people_to_add
    if action == 'leave':
        index = int(command[1])
        people_to_add = int(command[2])
        wagons[index] -= people_to_add

    command = input()

print(wagons)