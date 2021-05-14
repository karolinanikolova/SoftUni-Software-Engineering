string = input()

command = input()

while not command == "End":
    command = command.split(" ")
    action = command[0]

    if action == "Translate":
        char = command[1]
        replacement = command[2]

        string = string.replace(char, replacement)
        print(string)

    elif action == "Includes":
        substring = command[1]
        if substring in string:
            print("True")
        else:
            print("False")

    elif action == "Start":
        start_substring = command[1]
        if string.startswith(start_substring):
            print("True")
        else:
            print("False")

    elif action == "Lowercase":
        string = string.lower()
        print(string)

    elif action == "FindIndex":
        char = command[1]
        for index in range(len(string)):
            if string[index] == char:
                i = index
        print(i)

    elif action == "Remove":
        start_index = int(command[1])
        count = int(command[2])
        string = string[:start_index] + string[start_index+count:]
        print(string)

    command = input()