# 8.	* Moving Target
# You are at the shooting gallery again and you need a program that helps you keep track of moving targets.
# On the first line, you will receive a sequence of targets with their integer values, split by a single space.
# Then, you will start receiving commands for manipulating the targets, until the "End" command. The commands are the following:
# •	Shoot {index} {power}
# o	Shoot the target at the index, if it exists by reducing its value by the given power (integer value).
# A target is considered shot when its value reaches 0.
# o	Remove the target, if it is shot.
# •	Add {index} {value}
# o	Insert a target with the received value at the received index, if it exist. If not, print: "Invalid placement!"
# •	Strike {index} {radius}
# o	Remove the target at the given index and the ones before and after it depending on the radius, if such exist. If any of the indices in the range is invalid print:
# "Strike missed!" and skip this command.

target_values = [int(el) for el in input().split()]

command_data = input()

while command_data != 'End':
    command_data = command_data.split()
    action = command_data[0]
    index = int(command_data[1])

    if action == "Shoot":
        power = int(command_data[2])
        if 0 <= index < len(target_values):
            target_values[index] -= power
            if target_values[index] <= 0:
                target_values.pop(index)

    elif action == "Add":
        value = int(command_data[2])
        if 0 <= index < len(target_values):
            target_values.insert(index, value)
        else:
            print("Invalid placement!")

    elif action == "Strike":
        radius = int(command_data[2])
        if index - radius >= 0 and index + radius < len(target_values):
            del target_values[index-radius:index+radius+1]
        else:
            print(f"Strike missed!")

    command_data = input()

print(*target_values, sep="|")
