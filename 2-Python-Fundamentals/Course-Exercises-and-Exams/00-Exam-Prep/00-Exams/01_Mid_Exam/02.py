collection = input().split(" ")

command = input()

while not command == "end":
    command = command.split()
    action = command[0]

    if action == "reverse":
        start = int(command[2])
        count = int(command[4])
        end = start + count
        collection[start:end] = collection[start:end][::-1]
    elif action == "sort":
        start = int(command[2])
        count = int(command[4])
        end = start + count
        collection[start:end] = sorted(collection[start:end])
    elif action == "remove":
        count = int(command[1])
        collection = collection[count:]

    command = input()

print(", ".join(collection))


