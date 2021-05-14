# Programming Fundamentals Final Exam 09.08.2020
# Problem 1. World Tour
# You are a world traveller and your next goal is to make a world tour. In order to do that, you have to plan out everything first.
# To start with, you would like to plan out all of your stops where you will have a break.
# On the first line you will be given a string containing all of your stops. Until you receive the command "Travel",
# you will be given some commands to manipulate that initial string. The commands can be:
# •	Add Stop:{index}:{string} – insert the given string at that index only if the index is valid
# •	Remove Stop:{start_index}:{end_index} – remove the elements of the string from the starting index to the end index (inclusive) if both indices are valid
# •	Switch:{old_string}:{new_string} – if the old string is in the initial string, replace it with the new one. (all occurrences)
# Note: After each command print the current state of the string
# After the "Travel" command, print the following: "Ready for world tour! Planned stops: {string}"

def is_index_valid(i, s):
    if i in range(len(s)):
        return True
    return False


string = input()

command = input()

while not command == "Travel":
    command = command.split(":")
    action = command[0]

    if action == "Add Stop":
        index = int(command[1])
        string_to_add = command[2]
        if is_index_valid(index, string):
            string = string[:index] + string_to_add + string[index:]
        print(string)

    elif action == "Remove Stop":
        start_index = int(command[1])
        end_index = int(command[2])
        if is_index_valid(start_index, string) and is_index_valid(end_index, string):
            string = string[:start_index] + string[end_index+1:]
        print(string)

    elif action == "Switch":
        old_string = command[1]
        new_string = command[2]
        if old_string in string:
            string = string.replace(old_string, new_string)
        print(string)

    command = input()

print(f"Ready for world tour! Planned stops: {string}")
